from ._skia.core cimport (
    SkPath,
    SkPoint,
    SkScalar,
    SkRect,
    kMove_Verb,
    kLine_Verb,
    kQuad_Verb,
    kConic_Verb,
    kCubic_Verb,
    kClose_Verb,
    kDone_Verb,
    kWinding_FillType,
    kEvenOdd_FillType,
    kInverseWinding_FillType,
    kInverseEvenOdd_FillType,
)
from ._skia.pathops cimport (
    Op,
    Simplify,
    SkOpBuilder,
    SkPathOp,
    kDifference_SkPathOp,
    kIntersect_SkPathOp,
    kUnion_SkPathOp,
    kXOR_SkPathOp,
    kReverseDifference_SkPathOp,
)
from libc.stdint cimport uint8_t
from libc.float cimport FLT_EPSILON
from libc.math cimport fabs
from cpython.mem cimport PyMem_Malloc, PyMem_Free, PyMem_Realloc
from libc.string cimport memset
cimport cython
import itertools


cdef class PathOpsError(Exception):
    pass


cdef class UnsupportedVerbError(PathOpsError):
    pass


cdef class OpenPathError(PathOpsError):
    pass


cpdef enum PathOp:
    DIFFERENCE = kDifference_SkPathOp
    INTERSECTION = kIntersect_SkPathOp
    UNION = kUnion_SkPathOp
    XOR = kXOR_SkPathOp
    REVERSE_DIFFERENCE = kReverseDifference_SkPathOp


cpdef enum FillType:
    WINDING = kWinding_FillType
    EVEN_ODD = kEvenOdd_FillType
    INVERSE_WINDING = kInverseWinding_FillType
    INVERSE_EVEN_ODD = kInverseEvenOdd_FillType


cdef Path new_path(SkPath skpath):
    cdef Path p = Path()
    p.path = skpath
    return p


cdef class Path:

    cdef SkPath path

    def __init__(self, other=None, fillType=None):
        cdef Path static_path
        if other is not None:
            if isinstance(other, Path):
                static_path = other
                self.path = static_path.path
            else:
                other.draw(self.getPen())
        if fillType is not None:
            self.fillType = fillType

    cpdef PathPen getPen(self, bint allow_open_paths=True):
        return PathPen(self, allow_open_paths=allow_open_paths)

    def __iter__(self):
        return PathIterator(self)

    cpdef bint add(self, PathVerb verb, tuple pts) except False:
        if verb is PathVerb.MOVE:
            self.path.moveTo(pts[0][0], pts[0][1])
        elif verb is PathVerb.LINE:
            self.path.lineTo(pts[0][0], pts[0][1])
        elif verb is PathVerb.QUAD:
            self.path.quadTo(pts[0][0], pts[0][1],
                             pts[1][0], pts[1][1])
        elif verb is PathVerb.CONIC:
            self.path.conicTo(pts[0][0], pts[0][1],
                              pts[1][0], pts[1][1], pts[2])
        elif verb is PathVerb.CUBIC:
            self.path.cubicTo(pts[0][0], pts[0][1],
                              pts[1][0], pts[1][1],
                              pts[2][0], pts[2][1])
        elif verb is PathVerb.CLOSE:
            self.path.close()
        else:
            raise AssertionError(verb)
        return True

    cpdef void moveTo(self, SkScalar x, SkScalar y):
        self.path.moveTo(x, y)

    cpdef void lineTo(self, SkScalar x, SkScalar y):
        self.path.lineTo(x, y)

    cpdef void quadTo(
        self,
        SkScalar x1,
        SkScalar y1,
        SkScalar x2,
        SkScalar y2
    ):
        self.path.quadTo(x1, y1, x2, y2)

    cpdef void conicTo(
        self,
        SkScalar x1,
        SkScalar y1,
        SkScalar x2,
        SkScalar y2,
        SkScalar w
    ):
        self.path.conicTo(x1, y2, x2, y2, w)

    cpdef void cubicTo(
        self,
        SkScalar x1,
        SkScalar y1,
        SkScalar x2,
        SkScalar y2,
        SkScalar x3,
        SkScalar y3,
    ):
        self.path.cubicTo(x1, y1, x2, y2, x3, y3)

    cpdef void close(self):
        self.path.close()

    cpdef void reset(self):
        self.path.reset()

    cpdef void rewind(self):
        self.path.rewind()

    cpdef draw(self, pen):
        cdef PathVerb verb
        cdef tuple pts
        cdef list quads
        cdef bint closed = True
        cdef PathIterator iterator = iter(self)

        for verb, pts in iterator:
            try:
                method = getattr(pen, PEN_METHODS[verb])
            except KeyError:
                raise UnsupportedVerbError(PathVerb(verb).name)

            if verb is PathVerb.MOVE:
                if not closed:
                    # skia contours starting with "moveTo" are implicitly
                    # open, unless they end with a "close" verb
                    pen.endPath()
                closed = False
            elif verb is PathVerb.CLOSE:
                closed = True
            elif verb is PathVerb.QUAD:
                # try concatenating multiple quadratics with implied oncurves
                if iterator.peek() is PathVerb.QUAD:
                    quads = [pts]
                    while iterator.peek() is PathVerb.QUAD:
                        quads.append(next(iterator)[1])
                    quads = join_quadratic_segments(quads)
                    for pts in quads:
                        method(*pts)
                    continue

            method(*pts)

        if not closed:
            pen.endPath()

    def dump(self, cpp=False):
        # print a text repesentation to stdout
        if cpp:
            self.path.dump()  # C++
        else:
            print(self)  # Python

    def __str__(self):
        # return a text repesentation as Python code
        if self.path.isEmpty():
            return ""
        s = ["path.fillType = %s" % self.fillType]
        for verb, pts in self:
            method = VERB_METHODS[verb]
            args = ", ".join(map(str, itertools.chain(*pts)))
            s.append("path.%s(%s)" % (method, args))
        return "\n".join(s)

    def __repr__(self):
        return "<pathops.Path object at %s: %d contours>" % (
            hex(id(self)), self.countContours()
        )

    def __len__(self):
        return self.countContours()

    cpdef addPath(self, Path path):
        self.path.addPath(path.path)

    @property
    def fillType(self):
        return FillType(self.path.getFillType())

    @fillType.setter
    def fillType(self, value):
        self.path.setFillType(FillType(value))

    @property
    def isConvex(self):
        return self.path.isConvex()

    def contains(self, tuple pt):
        return self.path.contains(pt[0], pt[1])

    @property
    def bounds(self):
        cdef SkRect r = self.path.computeTightBounds()
        return (r.left(), r.top(), r.right(), r.bottom())

    @property
    def controlPointBounds(self):
        cdef SkRect r = self.path.getBounds()
        return (r.left(), r.top(), r.right(), r.bottom())

    @property
    def area(self):
        return fabs(get_path_area(self.path))

    @property
    def clockwise(self):
        return get_path_area(self.path) < 0

    @clockwise.setter
    def clockwise(self, value):
        if self.clockwise != value:
            self.reverse()

    cpdef reverse(self):
        cdef Path contour
        cdef SkPath skpath
        skpath.setFillType(self.path.getFillType())
        for contour in self.contours:
            reverse_contour(contour)
            skpath.addPath(contour.path)
        self.path = skpath

    cpdef simplify(self, bint fix_winding=True, keep_starting_points=True):
        cdef list first_points
        if keep_starting_points:
            first_points = self.firstPoints
        if not Simplify(self.path, &self.path):
            raise PathOpsError("simplify operation did not succeed")
        if fix_winding:
            winding_from_even_odd(self)
        if keep_starting_points:
            restore_starting_points(self, first_points)

    cdef list getVerbs(self):
        cdef int i, count
        cdef uint8_t *verbs
        count = self.path.countVerbs()
        verbs = <uint8_t *> PyMem_Malloc(count)
        if not verbs:
            raise MemoryError()
        try:
            assert self.path.getVerbs(verbs, count) == count
            return [PathVerb(verbs[i]) for i in range(count)]
        finally:
            PyMem_Free(verbs)

    @property
    def verbs(self):
        return self.getVerbs()

    cdef list getPoints(self):
        cdef int i, count
        cdef SkPoint *pts
        count = self.path.countPoints()
        pts = <SkPoint *> PyMem_Malloc(count * sizeof(SkPoint))
        if not pts:
            raise MemoryError()
        try:
            assert self.path.getPoints(pts, count) == count
            return [(pts[i].x(), pts[i].y()) for i in range(count)]
        finally:
            PyMem_Free(pts)

    @property
    def points(self):
        return self.getPoints()

    cdef int countContours(self) except -1:
        if self.path.isEmpty():
            return 0
        cdef int i, n, count
        cdef uint8_t *verbs
        count = self.path.countVerbs()
        verbs = <uint8_t *> PyMem_Malloc(count)
        if not verbs:
            raise MemoryError()
        try:
            self.path.getVerbs(verbs, count)
            n = 0
            for i in range(count):
                if verbs[i] == kMove_Verb:
                    n += 1
            return n
        finally:
            PyMem_Free(verbs)

    @property
    def firstPoints(self):
        cdef SkPoint *p = NULL
        cdef int count = 0
        cdef list result = []
        if self.getFirstPoints(&p, &count):
            for i in range(count):
                result.append((p[i].x(), p[i].y()))
            if p is not NULL:
                PyMem_Free(p)
        return result

    cdef int getFirstPoints(self, SkPoint **pp, int *count) except -1:
        cdef int c = self.path.countVerbs()
        if c == 0:
            return 0  # empty

        cdef SkPoint *points = <SkPoint *> PyMem_Malloc(c * sizeof(SkPoint))
        if not points:
            raise MemoryError()

        cdef SkPath.RawIter iterator = SkPath.RawIter(self.path)
        cdef SkPath.Verb verb
        cdef SkPoint p[4]

        cdef int i = 0
        while True:
            verb = iterator.next(p)
            if verb == kMove_Verb:
                points[i] = p[0]
                i += 1
            elif verb == kDone_Verb:
                break

        points = <SkPoint *> PyMem_Realloc(points, i * sizeof(SkPoint))
        count[0] = i
        pp[0] = points

        return 1

    @property
    def contours(self):
        cdef SkPath temp
        cdef SkPath.FillType fillType = self.path.getFillType()

        temp.setFillType(fillType)

        cdef SkPath.Verb verb
        cdef SkPoint p[4]
        cdef SkPath.RawIter iterator = SkPath.RawIter(self.path)

        while True:
            verb = iterator.next(p)
            if verb == kMove_Verb:
                if not temp.isEmpty():
                    yield new_path(temp)
                    temp.rewind()
                    temp.setFillType(fillType)
                temp.moveTo(p[0])
            elif verb == kLine_Verb:
                temp.lineTo(p[1])
            elif verb == kQuad_Verb:
                temp.quadTo(p[1], p[2])
            elif verb == kConic_Verb:
                temp.conicTo(p[1], p[2], iterator.conicWeight())
            elif verb == kCubic_Verb:
                temp.cubicTo(p[1], p[2], p[3])
            elif verb == kClose_Verb:
                temp.close()
                yield new_path(temp)
                temp.rewind()
                temp.setFillType(fillType)
            elif verb == kDone_Verb:
                if not temp.isEmpty():
                    yield new_path(temp)
                    temp.reset()
                break
            else:
                raise AssertionError(verb)


cpdef enum PathVerb:
    MOVE = kMove_Verb
    LINE = kLine_Verb
    QUAD = kQuad_Verb
    CONIC = kConic_Verb  # unsupported
    CUBIC = kCubic_Verb
    CLOSE = kClose_Verb
    DONE = kDone_Verb  # unused; we raise StopIteration instead

DEF NUM_VERBS = 7

cdef uint8_t *POINTS_IN_VERB = [
    1,  # MOVE
    1,  # LINE
    2,  # QUAD
    2,  # CONIC
    3,  # CUBIC
    0,  # CLOSE
    0   # DONE
]

cpdef dict VERB_METHODS = {
    kMove_Verb: "moveTo",
    kLine_Verb: "lineTo",
    kQuad_Verb: "quadTo",
    kConic_Verb: "conicTo",
    kCubic_Verb: "cubicTo",
    kClose_Verb: "close",
}

cpdef dict PEN_METHODS = {
    kMove_Verb: "moveTo",
    kLine_Verb: "lineTo",
    kQuad_Verb: "qCurveTo",
    kCubic_Verb: "curveTo",
    kClose_Verb: "closePath",
}


cdef class PathIterator:

    cdef Path path
    cdef SkPath.RawIter iterator

    def __cinit__(self, Path path):
        self.path = path
        self.iterator = SkPath.RawIter(self.path.path)

    def __iter__(self):
        return self

    def __next__(self):
        cdef tuple pts
        cdef SkPath.Verb verb
        cdef SkPoint p[4]

        verb = self.iterator.next(p)

        if verb == kMove_Verb:
            pts = ((p[0].x(), p[0].y()),)
        elif verb == kLine_Verb:
            pts = ((p[1].x(), p[1].y()),)
        elif verb == kQuad_Verb:
            pts = ((p[1].x(), p[1].y()),
                   (p[2].x(), p[2].y()))
        elif verb == kConic_Verb:
            pts = ((p[1].x(), p[1].y()),
                   (p[2].x(), p[2].y()),
                   self.iterator.conicWeight())
        elif verb == kCubic_Verb:
            pts = ((p[1].x(), p[1].y()),
                   (p[2].x(), p[2].y()),
                   (p[3].x(), p[3].y()))
        elif verb == kClose_Verb:
            pts = ()
        elif verb == kDone_Verb:
            raise StopIteration()
        else:
            raise UnsupportedVerbError(verb)

        return (PathVerb(verb), pts)

    cpdef PathVerb peek(self):
        return PathVerb(self.iterator.peek())


cdef class PathPen:

    cdef Path path
    cdef bint allow_open_paths

    def __cinit__(self, Path path, bint allow_open_paths=True):
        self.path = path
        self.allow_open_paths = allow_open_paths

    cpdef moveTo(self, pt):
        self.path.moveTo(pt[0], pt[1])

    cpdef lineTo(self, pt):
        self.path.lineTo(pt[0], pt[1])

    cpdef curveTo(self, pt1, pt2, pt3):
        # support BasePen "super-beziers"? Nah.
        self.path.cubicTo(
            pt1[0], pt1[1],
            pt2[0], pt2[1],
            pt3[0], pt3[1])

    def qCurveTo(self, *points):
        for pt1, pt2 in decompose_quadratic_segment(points):
            self._qCurveToOne(pt1, pt2)

    cdef _qCurveToOne(self, pt1, pt2):
        self.path.quadTo(pt1[0], pt1[1], pt2[0], pt2[1])

    cpdef closePath(self):
        self.path.close()

    cpdef endPath(self):
        if not self.allow_open_paths:
            raise OpenPathError()

    cpdef addComponent(self, glyphName, transformation):
        pass


cdef double get_path_area(const SkPath& path) except? FLT_EPSILON:
    # Adapted from fontTools/pens/areaPen.py
    cdef double value = .0
    cdef SkPath.Verb verb
    cdef SkPoint p[4]
    cdef SkPoint p0, start_point
    cdef SkScalar x0, y0, x1, y1, x2, y2, x3, y3
    # here we pass forceClose=True for simplicity. Make it optional?
    cdef SkPath.Iter iterator = SkPath.Iter(path, True)

    p0 = start_point = SkPoint.Make(.0, .0)
    while True:
        verb = iterator.next(p, False)
        if verb == kMove_Verb:
            p0 = start_point = p[0]
        elif verb == kLine_Verb:
            x0, y0 = p0.x(), p0.y()
            x1, y1 = p[1].x(), p[1].y()
            value -= (x1 - x0) * (y1 + y0) * .5
            p0 = p[1]
        elif verb == kQuad_Verb:
            # https://github.com/Pomax/bezierinfo/issues/44
            x0, y0 = p0.x(), p0.y()
            x1, y1 = p[1].x() - x0, p[1].y() - y0
            x2, y2 = p[2].x() - x0, p[2].y() - y0
            value -= (x2 * y1 - x1 * y2) / 3
            value -= (p[2].x() - x0) * (p[2].y() + y0) * .5
            p0 = p[2]
        elif verb == kConic_Verb:
            raise UnsupportedVerbError("CONIC")
        elif verb == kCubic_Verb:
            # https://github.com/Pomax/bezierinfo/issues/44
            x0, y0 = p0.x(), p0.y()
            x1, y1 = p[1].x() - x0, p[1].y() - y0
            x2, y2 = p[2].x() - x0, p[2].y() - y0
            x3, y3 = p[3].x() - x0, p[3].y() - y0
            value -= (
                       x1 * (   -   y2 -   y3) +
                       x2 * (y1        - 2*y3) +
                       x3 * (y1 + 2*y2       )
                     ) * 0.15
            value -= (p[3].x() - x0) * (p[3].y() + y0) * .5
            p0 = p[3]
        elif verb == kClose_Verb:
            x0, y0 = p0.x(), p0.y()
            x1, y1 = start_point.x(), start_point.y()
            value -= (x1 - x0) * (y1 + y0) * .5
            p0 = start_point = SkPoint.Make(.0, .0)
        elif verb == kDone_Verb:
            break
        else:
            raise AssertionError(verb)

    return value


cdef class _VerbArray:

    cdef uint8_t *data
    cdef int count

    def __cinit__(self, Path path):
        self.count = path.path.countVerbs()
        self.data = <uint8_t *> PyMem_Malloc(self.count)
        if not self.data:
            raise MemoryError()
        path.path.getVerbs(self.data, self.count)

    def __dealloc__(self):
        PyMem_Free(self.data)  # no-op if data is NULL


cdef class _SkPointArray:

    cdef SkPoint *data
    cdef int count

    def __cinit__(self, Path path):
        self.count = path.path.countPoints()
        self.data = <SkPoint *> PyMem_Malloc(self.count * sizeof(SkPoint))
        if not self.data:
            raise MemoryError()
        path.path.getPoints(self.data, self.count)

    def __dealloc__(self):
        PyMem_Free(self.data)  # no-op if data is NULL


cdef inline int pts_in_verb(unsigned v) except -1:
    if v >= NUM_VERBS:
        raise IndexError(v)
    return POINTS_IN_VERB[v]


cdef bint reverse_contour(Path path) except False:
    cdef SkPath *skpath = &path.path
    cdef SkPath temp
    cdef SkPoint lastPt

    if not skpath.getLastPt(&lastPt):
        return True  # ignore empty path

    cdef _VerbArray va = _VerbArray(path)
    cdef uint8_t *verbsStart = va.data  # pointer to the first verb
    cdef uint8_t *verbs = verbsStart + va.count - 1  # pointer to the last verb

    cdef _SkPointArray pa = _SkPointArray(path)
    cdef SkPoint *pts = pa.data + pa.count - 1  # pointer to the last point

    # the last point becomes the first
    temp.moveTo(lastPt)

    cdef uint8_t v
    cdef bint closed = False
    # loop over both arrays in reverse, break before the first verb
    while verbs > verbsStart:
        v = verbs[0]
        verbs -= 1
        pts -= pts_in_verb(v)
        if v == kMove_Verb:
            # if the path has multiple contours, stop after reversing the last
            break
        elif v == kLine_Verb:
            temp.lineTo(pts[0])
        elif v == kQuad_Verb:
            temp.quadTo(pts[1], pts[0])
        elif v == kConic_Verb:
            raise UnsupportedVerbError("CONIC")
        elif v == kCubic_Verb:
            temp.cubicTo(pts[2], pts[1], pts[0])
        elif v == kClose_Verb:
            closed = True
        else:
            raise AssertionError(v)

    if closed:
        temp.close()

    temp.setFillType(skpath.getFillType())
    skpath[0] = temp
    return True


# NOTE This is meant to be used only on simplified paths (i.e. without
# overlapping contours), like the ones returned from Skia's path operations.
# It only tests the bounding boxes and the on-curve points.
cdef int path_is_inside(const SkPath& self, const SkPath& other) except -1:
    cdef SkRect r1, r2
    cdef SkPath.RawIter iterator
    cdef SkPath.Verb verb
    cdef SkPoint[4] p
    cdef SkPoint oncurve

    r1 = self.computeTightBounds()
    r2 = other.computeTightBounds()
    if not SkRect.Intersects(r1, r2):
        return 0

    iterator = SkPath.RawIter(other)
    while True:
        verb = iterator.next(p)
        if verb == kMove_Verb:
            oncurve = p[0]
        elif verb == kLine_Verb:
            oncurve = p[1]
        elif verb == kQuad_Verb:
            oncurve = p[2]
        elif verb == kConic_Verb:
            raise UnsupportedVerbError("CONIC")
        elif verb == kCubic_Verb:
            oncurve = p[3]
        elif verb == kClose_Verb:
            continue
        elif verb == kDone_Verb:
            break
        else:
            raise AssertionError(verb)
        if not self.contains(oncurve.x(), oncurve.y()):
            return 0

    return 1


@cython.wraparound(False)
@cython.boundscheck(False)
cpdef int restore_starting_points(Path path, list points) except -1:
    if not points:
        return 0

    cdef list contours = list(path.contours)
    cdef Py_ssize_t n = len(contours)
    cdef Py_ssize_t m = len(points)
    cdef int i, j
    cdef Path this
    cdef bint modified = False

    for i in range(n):
        this = contours[i]
        for j in range(m):
            pt = points[j]
            if set_contour_start_point(this, pt[0], pt[1]):
                modified = True
                # we don't retry the same point again on a different contour
                del points[j]
                m -= 1
                break

    if not modified:
        return 0

    path.path.rewind()
    for i in range(n):
        this = contours[i]
        path.path.addPath(this.path)

    return 1


DEF DEBUG_WINDING = False


@cython.wraparound(False)
@cython.boundscheck(False)
cpdef bint winding_from_even_odd(Path path, bint truetype=False) except False:
    """ Take a simplified path (without overlaps) and set the contours
    directions according to the non-zero winding fill type.
    The outermost contours are set to counter-clockwise direction, unless
    'truetype' is True.
    """
    cdef int i, j
    cdef bint inverse = not truetype
    cdef bint is_clockwise, is_even
    cdef Path contour, other

    # sort contours by area, from largest to smallest
    cdef dict contours_by_area = {}
    cdef object area
    for contour in path.contours:
        area = -fabs(get_path_area(contour.path))
        if area not in contours_by_area:
            contours_by_area[area] = []
        contours_by_area[area].append(contour)
    cdef list group
    cdef list contours = []
    for _, group in sorted(contours_by_area.items()):
        contours.extend(group)
    cdef Py_ssize_t n = len(contours)

    # XXX permature optimization? needs profile
    cdef size_t* nested
    nested = <size_t*>PyMem_Malloc(n * sizeof(size_t))
    if not nested:
        raise MemoryError()
    memset(nested, 0, n * sizeof(size_t))
    try:
        # increment the nesting level when a contour is inside another
        for i in range(n):
            contour = contours[i]
            for j in range(i + 1, n):
                other = contours[j]
                if path_is_inside(contour.path, other.path):
                    nested[j] += 1

        IF DEBUG_WINDING:
            print("nested: ", end="")
            for i in range(n):
                print(nested[i], end=" ")
            print("")

        # reverse a contour when its winding and even-odd number disagree;
        # for TrueType, set the outermost direction to clockwise
        for i in range(n):
            contour = contours[i]
            is_clockwise = get_path_area(contour.path) < .0
            is_even = not (nested[i] & 1)

            IF DEBUG_WINDING:
                print(
                    "%d: inverse=%s is_clockwise=%s is_even=%s"
                    % (i, inverse, is_clockwise, is_even)
                )
            if inverse ^ is_clockwise ^ is_even:
                IF DEBUG_WINDING:
                    print("reverse_contour %d" % i)
                reverse_contour(contour)
    finally:
        PyMem_Free(nested)

    path.path.rewind()
    for i in range(n):
        contour = contours[i]
        path.path.addPath(contour.path)

    path.path.setFillType(kWinding_FillType)
    return True


cdef list decompose_quadratic_segment(tuple points):
    cdef:
        int i, n = len(points) - 1
        list quad_segments = []
        SkScalar x, y, nx, ny
        tuple implied_pt

    assert n > 0
    for i in range(n - 1):
        x, y = points[i]
        nx, ny = points[i+1]
        implied_pt = (0.5 * (x + nx), 0.5 * (y + ny))
        quad_segments.append((points[i], implied_pt))
    quad_segments.append((points[-2], points[-1]))
    return quad_segments


cdef double ROUGH_EPSILON = FLT_EPSILON * 64


cdef bint almost_equal(SkScalar v1, SkScalar v2):
    return fabs(v1 - v2) < ROUGH_EPSILON


cdef list join_quadratic_segments(list quad_segments):
    cdef:
        int i
        list new_segments, points
        SkScalar off1x, off1y, onx, ony, off2x, off2y

    new_segments = []
    points = []
    for i in range(len(quad_segments) - 1):
        (off1x, off1y), (onx, ony) = quad_segments[i]
        (off2x, off2y), _ = quad_segments[i + 1]
        points.append((off1x, off1y))
        # skip oncurve if equal to midpoint between two consecutive offcurves
        if not (
            almost_equal(onx, (off1x + off2x) / 2)
            and almost_equal(ony, (off1y + off2y) / 2)
        ):
            points.append((onx, ony))
            new_segments.append(tuple(points))
            del points[:]
    new_segments.append(tuple(points) + quad_segments[-1])
    return new_segments


cdef int find_oncurve_point(
    SkScalar x,
    SkScalar y,
    const SkPoint *pts,
    int pt_count,
    const uint8_t *verbs,
    int verb_count,
    int *pt_index,
    int *verb_index,
) except -1:
    cdef SkPoint oncurve
    cdef uint8_t v
    cdef int i, j, n
    cdef int seen = 0

    for i in range(verb_count):
        v = verbs[i]
        n = pts_in_verb(v)
        if n == 0:
            continue
        assert seen + n <= pt_count
        j = seen + n - 1
        oncurve = pts[j]
        if oncurve.equals(x, y):
            pt_index[0] = j
            verb_index[0] = i
            return 1
        seen += n

    return 0


cdef int contour_is_closed(const uint8_t *verbs, int verb_count) except -1:
    cdef int i
    cdef uint8_t v
    cdef bint closed = False
    for i in range(1, verb_count):
        v = verbs[i]
        if v == kMove_Verb:
            raise ValueError("expected single contour")
        elif v == kClose_Verb:
            closed = True
    return closed


cpdef int set_contour_start_point(Path path, SkScalar x, SkScalar y) except -1:
    cdef SkPath *skpath = &path.path

    cdef _VerbArray va = _VerbArray(path)
    cdef uint8_t *verbs = va.data
    cdef int verb_count = va.count

    cdef _SkPointArray pa = _SkPointArray(path)
    cdef SkPoint *pts = pa.data
    cdef int pt_count = pa.count

    cdef bint closed = contour_is_closed(verbs, verb_count)

    cdef int pt_index = -1
    cdef int verb_index = -1
    cdef bint found = find_oncurve_point(
        x, y,
        pts,
        pt_count,
        verbs,
        verb_count,
        &pt_index,
        &verb_index,
    )
    if not found or pt_index == 0 or (
        not closed and pt_index != (pt_count - 1)
    ):
        return 0

    if not closed and pt_index == (pt_count - 1):
        reverse_contour(path)
        return 1

    cdef SkPath.FillType fill = skpath.getFillType()
    skpath.rewind()
    skpath.setFillType(fill)

    cdef uint8_t first_verb
    cdef SkPoint first_pt
    cdef int vi, pi

    first_verb = verbs[verb_index]
    vi = (verb_index + 1) % verb_count

    first_pt = pts[pt_index]
    pi = (pt_index + 1) % pt_count

    skpath.moveTo(first_pt)

    cdef int i, n
    cdef uint8_t v = kDone_Verb
    cdef SkPoint *last = &first_pt
    for i in range(1, verb_count):
        v = verbs[vi]
        n = pts_in_verb(v)
        assert pi + n <= pt_count
        if v == kMove_Verb:
            if last[0] != pts[pi]:
                skpath.lineTo(pts[pi])
        elif v == kLine_Verb:
            skpath.lineTo(pts[pi])
            last = pts + pi
        elif v == kQuad_Verb:
            skpath.quadTo(pts[pi], pts[pi + 1])
            last = pts + pi + 1
        elif v == kConic_Verb:
            raise UnsupportedVerbError("CONIC")
        elif v == kCubic_Verb:
            skpath.cubicTo(pts[pi], pts[pi + 1], pts[pi + 2])
            last = pts + pi + 2
        elif v == kClose_Verb:
            pass
        else:
            raise AssertionError(v)
        vi = (vi + 1) % verb_count
        pi = (pi + n) % pt_count

    if first_verb == kQuad_Verb:
        skpath.quadTo(pts[pi], pts[pi + 1])
    elif first_verb == kCubic_Verb:
        skpath.cubicTo(pts[pi], pts[pi + 1], pts[pi + 2])

    skpath.close()
    return 1


cpdef Path op(
    Path one,
    Path two,
    SkPathOp operator,
    fix_winding=True,
    keep_starting_points=True
):
    cdef list first_points
    if keep_starting_points:
        first_points = one.firstPoints + two.firstPoints
    cdef Path result = Path()
    if not Op(one.path, two.path, operator, &result.path):
        raise PathOpsError("operation did not succeed")
    if fix_winding:
        winding_from_even_odd(result)
    if keep_starting_points:
        restore_starting_points(result, first_points)
    return result


cpdef Path simplify(Path path, fix_winding=True, keep_starting_points=True):
    cdef list first_points
    if keep_starting_points:
        first_points = path.firstPoints
    cdef Path result = Path()
    if Simplify(path.path, &result.path):
        return result
    if fix_winding:
        winding_from_even_odd(result)
    if keep_starting_points:
        restore_starting_points(result, first_points)
    raise PathOpsError("operation did not succeed")


cdef class OpBuilder:

    cdef SkOpBuilder builder
    cdef bint fix_winding
    cdef bint keep_starting_points
    cdef list first_points

    def __init__(self, bint fix_winding=True, keep_starting_points=True):
        self.fix_winding = fix_winding
        self.keep_starting_points = keep_starting_points
        self.first_points = []

    cpdef add(self, Path path, SkPathOp operator):
        self.builder.add(path.path, operator)
        if self.keep_starting_points:
            self.first_points.extend(path.firstPoints)

    cpdef Path resolve(self):
        cdef Path result = Path()
        if self.builder.resolve(&result.path):
            if self.fix_winding:
                winding_from_even_odd(result)
            if self.keep_starting_points:
                restore_starting_points(result, self.first_points)
            return result
        raise PathOpsError("operation did not succeed")
