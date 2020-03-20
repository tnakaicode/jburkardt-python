#
#    Licensing:
#
#    This code is distributed under the GNU LGPL license.
#

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.append(os.path.join('../'))
from rnd_uniform.uniform import r8vec_uniform_01, r8mat_uniform_01, r8_uniform_01
from rnd_uniform.sample import triangle01_sample, cube01_sample, ball01_sample, annulus_sample
from rnd_uniform.sample import circle01_sample_ergodic, circle01_sample_random
from rnd_uniform.sample import hypercube01_sample
from base import PlotBase


def angle_degree(x1, y1, x2, y2, x3, y3):

    #
    # ANGLE_DEGREE returns the degree angle defined by three points.
    #
    #  Discussion:
    #
    #        P1
    #        /
    #       /
    #      /7
    #     /
    #    P2--------->P3
    #
    #  Parameters:
    #
    #    Input, real X1, Y1, X2, Y2, X3, Y3, the coordinates of the points
    #    P1, P2, P3.
    #
    #    Output, real VALUE, the angle swept out by the rays, measured
    #    in degrees.  0 <= VALUE < 360.  If either ray has zero length,
    #    then VALUE is set to 0.
    #
    x = (x3 - x2) * (x1 - x2) + (y3 - y2) * (y1 - y2)
    y = (x3 - x2) * (y1 - y2) - (y3 - y2) * (x1 - x2)

    if (x == 0.0 and y == 0.0):
        value = 0.0
        return value

    value = np.arctan2(y, x)
    if (value < 0.0):
        value = value + 2.0 * np.pi
    value = 180.0 * value / np.pi
    return value


def between(xa, ya, xb, yb, xc, yc):

    #
    # BETWEEN is TRUE if vertex C is between vertices A and B.
    #
    #  Discussion:
    #
    #    The points must be (numerically) collinear.
    #
    #    Given that condition, we take the greater of XA - XB and YA - YB
    #    as a "scale" and check where C's value lies.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Parameters:
    #
    #    Input, real XA, YA, XB, YB, XC, YC, the coordinates of
    #    the vertices.
    #
    #    Output, logical VALUE, is TRUE if C is between A and B.
    #
    if (not collinear(xa, ya, xb, yb, xc, yc)):
        value = False
    elif (abs(ya - yb) < abs(xa - xb)):
        xmax = max(xa, xb)
        xmin = min(xa, xb)
        value = (xmin <= xc and xc <= xmax)
    else:
        ymax = max(ya, yb)
        ymin = min(ya, yb)
        value = (ymin <= yc and yc <= ymax)

    return value


def collinear(xa, ya, xb, yb, xc, yc):

    #
    # COLLINEAR returns a measure of collinearity for three points.
    #
    #  Discussion:
    #
    #    In order to deal with collinear points whose coordinates are not
    #    numerically exact, we compare the area of the largest square
    #    that can be created by the line segment between two of the points
    #    to (twice) the area of the triangle formed by the points.
    #
    #    If the points are collinear, their triangle has zero area.
    #    If the points are close to collinear, then the area of this triangle
    #    will be small relative to the square of the longest segment.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Parameters:
    #
    #    Input, real XA, YA, XB, YB, XC, YC, the coordinates of
    #    the vertices.
    #
    #    Output, logical VALULE, is TRUE if the points are judged
    #    to be collinear.
    #
    r8_eps = 2.220446049250313E-016

    area = triangle_area(xa, ya, xb, yb, xc, yc)

    side_ab_sq = (xa - xb) ** 2 + (ya - yb) ** 2
    side_bc_sq = (xb - xc) ** 2 + (yb - yc) ** 2
    side_ca_sq = (xc - xa) ** 2 + (yc - ya) ** 2

    side_max_sq = max(side_ab_sq, max(side_bc_sq, side_ca_sq))

    if (side_max_sq <= r8_eps):
        value = True
    elif (2.0 * abs(area) <= r8_eps * side_max_sq):
        value = True
    else:
        value = False

    return value


def l4_xor(l1, l2):

    #
    # L4_XOR returns the exclusive OR of two L4's.
    #
    #  Discussion:
    #
    #    An L4 is a logical value.
    #
    #  Parameters:
    #
    #    Input, logical L1, L2, two values whose exclusive OR
    #    is needed.
    #
    #    Output, logical VALUE, the exclusive OR of L1 and L2.
    #
    value1 = (l1 and (not l2))
    value2 = ((not l1) and l2)
    value = (value1 or value2)
    return value


def intersect_prop(xa, ya, xb, yb, xc, yc, xd, yd):

    #
    # INTERSECT_PROP is TRUE if lines VA:VB and VC:VD have a proper intersection.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Parameters:
    #
    #    Input, real XA, YA, XB, YB, XC, YC, XD, YD, the X and Y
    #    coordinates of the four vertices.
    #
    #    Output, logical VALUE, the result of the test.
    #
    if (collinear(xa, ya, xb, yb, xc, yc)):
        value = False
    elif (collinear(xa, ya, xb, yb, xd, yd)):
        value = False
    elif (collinear(xc, yc, xd, yd, xa, ya)):
        value = False
    elif (collinear(xc, yc, xd, yd, xb, yb)):
        value = False
    else:
        t1 = triangle_area(xa, ya, xb, yb, xc, yc)
        t2 = triangle_area(xa, ya, xb, yb, xd, yd)
        t3 = triangle_area(xc, yc, xd, yd, xa, ya)
        t4 = triangle_area(xc, yc, xd, yd, xb, yb)

        value1 = (0.0 < t1)
        value2 = (0.0 < t2)
        value3 = (0.0 < t3)
        value4 = (0.0 < t4)
        value = (l4_xor(value1, value2)) and (l4_xor(value3, value4))
    return value


def intersect(xa, ya, xb, yb, xc, yc, xd, yd):

    #
    # INTERSECT is true if lines VA:VB and VC:VD intersect.
    #
    #  Discussion:
    #
    #    Thanks to Gene Dial for correcting the call to intersect_prop(),
    #    08 September 2016.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Parameters:
    #
    #    Input, real XA, YA, XB, YB, XC, YC, XD, YD, the X and Y
    #    coordinates of the four vertices.
    #
    #    Output, logical VALUE, the value of the test.
    #
    if (intersect_prop(xa, ya, xb, yb, xc, yc, xd, yd)):
        value = True
    elif (between(xa, ya, xb, yb, xc, yc)):
        value = True
    elif (between(xa, ya, xb, yb, xd, yd)):
        value = True
    elif (between(xc, yc, xd, yd, xa, ya)):
        value = True
    elif (between(xc, yc, xd, yd, xb, yb)):
        value = True
    else:
        value = False
    return value


def diagonalie(im1, ip1, n, next_node, x, y):

    #
    # DIAGONALIE is true if VERTEX(IM1):VERTEX(IP1) is a proper diagonal.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Parameters:
    #
    #    Input, integer IM1, IP1, the indices of two vertices.
    #
    #    Input, integer N, the number of vertices.
    #
    #    Input, integer NEXT_NODE(N), the next neighbor of each vertex.
    #
    #    Input, real X(N), Y(N), the coordinates of each vertex.
    #
    #    Output, logical VALUE, the value of the test.
    #
    first = im1
    j = first
    jp1 = next_node[first]
    value = True
    #
    #  For each edge VERTEX(J):VERTEX(JP1) of the polygon:
    #
    while (True):
        #
        #  Skip any edge that includes vertex IM1 or IP1.
        #
        if (j == im1 or j == ip1 or jp1 == im1 or jp1 == ip1):
            pass
        else:
            value2 = intersect(
                x[im1], y[im1], x[ip1], y[ip1], x[j], y[j], x[jp1], y[jp1])
            if (value2):
                value = False
                break
        j = jp1
        jp1 = next_node[j]
        if (j == first):
            break
    return value


def diagonal(im1, ip1, n, prev_node, next_node, x, y):

    #
    # DIAGONAL: VERTEX(IM1) to VERTEX(IP1) is a proper internal diagonal.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Parameters:
    #
    #    Input, integer IM1, IP1, the indices of two vertices.
    #
    #    Input, integer N, the number of vertices.
    #
    #    Input, integer PREV_NODE(N), the previous neighbor of each vertex.
    #
    #    Input, integer NEXT_NODE(N), the next neighbor of each vertex.
    #
    #    Input, real X(N), Y(N), the coordinates of each vertex.
    #
    #    Output, logical VALUE, the value of the test.
    #
    value1 = in_cone(im1, ip1, n, prev_node, next_node, x, y)
    value2 = in_cone(ip1, im1, n, prev_node, next_node, x, y)
    value3 = diagonalie(im1, ip1, n, next_node, x, y)
    value = (value1 and value2 and value3)
    return value


def in_cone(im1, ip1, n, prev_node, next_node, x, y):

    #
    # IN_CONE is TRUE if the diagonal VERTEX(IM1):VERTEX(IP1) is strictly internal.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Parameters:
    #
    #    Input, integer IM1, IP1, the indices of two vertices.
    #
    #    Input, integer N, the number of vertices.
    #
    #    Input, integer PREV_NODE(N), the previous neighbor of each vertex.
    #
    #    Input, integer NEXT_NODE(N), the next neighbor of each vertex.
    #
    #    Input, real X(N), Y(N), the coordinates of each vertex.
    #
    #    Output, logical VALUE, the value of the test.
    #
    im2 = prev_node[im1]
    i = next_node[im1]

    t1 = triangle_area(x[im1], y[im1], x[i], y[i], x[im2], y[im2])
    if (0.0 <= t1):
        t2 = triangle_area(x[im1], y[im1], x[ip1], y[ip1], x[im2], y[im2])
        t3 = triangle_area(x[ip1], y[ip1], x[im1], y[im1], x[i], y[i])
        value = ((0.0 < t2) and (0.0 < t3))
    else:
        t4 = triangle_area(x[im1], y[im1], x[ip1], y[ip1], x[i], y[i])
        t5 = triangle_area(x[ip1], y[ip1], x[im1], y[im1], x[im2], y[im2])
        value = not ((0.0 <= t4) and (0.0 <= t5))
    return value


def polygon_area(n, x, y):

    #
    # POLYGON_AREA returns the area of a polygon.
    #
    #  Discussion:
    #
    #    The vertices should be listed in counter-clockwise order so that
    #    the area will be positive.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of vertices.
    #
    #    Input, real X(N), Y(N), the vertex coordinates.
    #
    #    Output, real AREA, the area of the polygon.
    #
    area = 0.0
    im1 = n - 1
    for i in range(0, n):
        area = area + x[im1] * y[i] - x[i] * y[im1]
        im1 = i
    area = 0.5 * area
    return area


def polygon_triangulate(n, x, y):

    #
    # POLYGON_TRIANGULATE determines a triangulation of a polygon.
    #
    #  Discussion:
    #
    #    There are N-3 triangles in the triangulation.
    #
    #    For the first N-2 triangles, the first edge listed is always an
    #    internal diagonal.
    #
    #    Thanks to Gene Dial for pointing out a mistake in the area calculation,
    #    10 September 2016.
    #
    #    Thanks to Gene Dial for suggesting that the next() array should be
    #    renamed next_node() to avoid the Python keyword next, 22 September 2016.
    #
    #  Reference:
    #
    #    Joseph ORourke,
    #    Computational Geometry in C,
    #    Cambridge, 1998,
    #    ISBN: 0521649765,
    #    LC: QA448.D38.
    #
    #  Parameters:
    #
    #    Input, int N, the number of vertices.
    #
    #    Input, real X[N], Y[N], the coordinates of each vertex.
    #
    #    Output, int TRIANGLES[N-2,3], the triangles.
    #
    #  We must have at least 3 vertices.
    #
    if (n < 3):
        print('')
        print('POLYGON_TRIANGULATE - Fatal error!')
        print('  N < 3')
        exit('POLYGON_TRIANGULATE - Fatal error!')
    #
    #  Consecutive vertices cannot be equal.
    #
    node_m1 = n - 1
    for node in range(0, n):
        if (x[node_m1] == x[node] and y[node_m1] == y[node]):
            print('')
            print('POLYGON_TRIANGULATE - Fatal error!')
            print('  Two consecutive nodes are identical.')
            exit('POLYGON_TRIANGULATE - Fatal error!')

        node_m1 = node
    #
    #  No node can be the vertex of an angle less than 1 degree
    #  in absolute value.
    #
    node1 = n - 1

    for node2 in range(0, n):

        node3 = ((node2 + 1) % n)

        angle = angle_degree(
            x[node1], y[node1],
            x[node2], y[node2],
            x[node3], y[node3])

        if (abs(angle) <= 1.0):
            print('')
            print('POLYGON_TRIANGULATE - Fatal error!')
            print('  Polygon has an angle %g smaller than 1 degree.' % (angle))
            print('  occurring at node %d' % (node2))
            return None

        node1 = node2
    #
    #  Area must be positive.
    #
    area = polygon_area(n, x, y)

    if (area <= 0.0):
        print('')
        print('POLYGON_TRIANGULATE - Fatal error!')
        print('  Polygon has zero or negative area.')
        exit('POLYGON_TRIANGULATE - Fatal error!')

    triangles = np.zeros([n - 2, 3], dtype=np.int32)
    #
    #  PREV_NODE and NEXT_NODE point to the previous and next nodes.
    #
    prev_node = np.zeros(n, dtype=np.int32)
    next_node = np.zeros(n, dtype=np.int32)

    i = 0
    prev_node[i] = n - 1
    next_node[i] = i + 1

    for i in range(1, n - 1):
        prev_node[i] = i - 1
        next_node[i] = i + 1

    i = n - 1
    prev_node[i] = i - 1
    next_node[i] = 0
    #
    #  EAR indicates whether the node and its immediate neighbors form an ear
    #  that can be sliced off immediately.
    #
    ear = np.zeros(n, dtype=np.bool)
    for i in range(0, n):
        ear[i] = diagonal(prev_node[i], next_node[i], n, prev_node,
                          next_node, x, y)

    triangle_num = 0

    i2 = 0

    while (triangle_num < n - 3):
        #
        #  If I2 is an ear, gather information necessary to carry out
        #  the slicing operation and subsequent "healing".
        #
        if (ear[i2]):
            i3 = next_node[i2]
            i4 = next_node[i3]
            i1 = prev_node[i2]
            i0 = prev_node[i1]
            #
            #  Make vertex I2 disappear.
            #
            next_node[i1] = i3
            prev_node[i3] = i1
            #
            #  Update the earity of I1 and I3, because I2 disappeared.
            #
            ear[i1] = diagonal(i0, i3, n, prev_node, next_node, x, y)
            ear[i3] = diagonal(i1, i4, n, prev_node, next_node, x, y)
            #
            #  Add the diagonal [I3, I1, I2] to the list.
            #
            triangles[triangle_num, 0] = i3
            triangles[triangle_num, 1] = i1
            triangles[triangle_num, 2] = i2
            triangle_num = triangle_num + 1
        #
        #  Try the next vertex.
        #
        i2 = next_node[i2]
    #
    #  The last triangle is formed from the three remaining vertices.
    #
    i3 = next_node[i2]
    i1 = prev_node[i2]

    triangles[triangle_num, 0] = i3
    triangles[triangle_num, 1] = i1
    triangles[triangle_num, 2] = i2
    triangle_num = triangle_num + 1

    return triangles


def triangle_area(xa, ya, xb, yb, xc, yc):

    #
    # TRIANGLE_AREA computes the signed area of a triangle.
    #
    #  Parameters:
    #
    #    Input, real XA, YA, XB, YB, XC, YC, the coordinates of
    #    the vertices of the triangle, given in counterclockwise order.
    #
    #    Output, real VALUE, the signed area of the triangle.
    #
    value = 0.5 * ((xb - xa) * (yc - ya) - (xc - xa) * (yb - ya))
    return value


def polygon_sample(nv, v, n, seed):

    #
    # POLYGON_SAMPLE uniformly samples a polygon.
    #
    #  Parameters:
    #
    #    Input, integer NV, the number of vertices.
    #
    #    Input, real V(NV,2), the vertices of the polygon, listed in
    #    counterclockwise order.
    #
    #    Input, integer N, the number of points to create.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real S(2,N), the points.
    #
    #
    #  Triangulate the polygon.
    #

    x = np.zeros(nv)
    y = np.zeros(nv)
    for j in range(0, nv):
        x[j] = v[j, 0]
        y[j] = v[j, 1]

    triangles = polygon_triangulate(nv, x, y)
    #
    #  Determine the areas of each triangle.
    #
    area_triangle = np.zeros(nv - 2)

    area_polygon = 0.0
    for i in range(0, nv - 2):
        area_triangle[i] = triangle_area(
            v[triangles[i, 0], 0], v[triangles[i, 0], 1],
            v[triangles[i, 1], 0], v[triangles[i, 1], 1],
            v[triangles[i, 2], 0], v[triangles[i, 2], 1])
        area_polygon = area_polygon + area_triangle[i]
    #
    #  Normalize the areas.
    #
    area_relative = np.zeros(nv - 1)

    for i in range(0, nv - 2):
        area_relative[i] = area_triangle[i] / area_polygon
    #
    #  Replace each area by the sum of itself and all previous ones.
    #
    area_cumulative = np.zeros(nv - 2)

    area_cumulative[0] = area_relative[0]
    for i in range(1, nv - 2):
        area_cumulative[i] = area_relative[i] + area_cumulative[i - 1]

    s = np.zeros([2, n])

    for j in range(0, n):
        #
        #  Choose triangle I at random, based on areas.
        #
        area_percent, seed = r8_uniform_01(seed)

        for k in range(0, nv - 2):

            i = k

            if (area_percent <= area_cumulative[k]):
                break
        #
        #  Now choose a point at random in triangle I.
        #
        r, seed = r8vec_uniform_01(2, seed)

        if (1.0 < r[0] + r[1]):
            r[0] = 1.0 - r[0]
            r[1] = 1.0 - r[1]

        s[0, j] = (1.0 - r[0] - r[1]) * v[triangles[i, 0], 0] \
            + r[0] * v[triangles[i, 1], 0] \
            + r[1] * v[triangles[i, 2], 0]

        s[1, j] = (1.0 - r[0] - r[1]) * v[triangles[i, 0], 1] \
            + r[0] * v[triangles[i, 1], 1] \
            + r[1] * v[triangles[i, 2], 1]

    return s, seed


class MonteCarlo (PlotBase):

    def __init__(self, aspect='equal'):
        PlotBase.__init__(self, aspect=aspect)
        self.create_tempdir(-1)

        nv = 6
        v = np.array([
            [0.0, 0.0],
            [2.0, 0.0],
            [2.0, 1.0],
            [1.0, 1.0],
            [1.0, 2.0],
            [0.0, 1.0]])

        seed = 123456789
        n = 1
        while (n <= 65536):
            self.PlotTest(*triangle01_sample(n, seed), title="triangle")
            self.PlotTest(*cube01_sample(n, seed), title="cube01")
            self.PlotTest(*ball01_sample(n, seed), title="ball")
            self.PlotTest(
                *annulus_sample([0, 0], 1.0, 2.0, n, seed), title="annulus01")
            self.PlotTest(*annulus_sample([1, 1], 0.5, 3.0, n, seed))
            self.PlotTest(*polygon_sample(nv, v, n, seed), title="polygon01")
            self.PlotTest(*circle01_sample_ergodic(n, seed),
                          title="circle_ergodic")
            self.PlotTest(*circle01_sample_random(n, seed),
                          title="circle_random")
            self.PlotTest(*hypercube01_sample(3, n, seed), title="cube02")
            n = 2 * n

    def PlotTest(self, x, seed, title=None):
        dim, num = x.shape
        self.new_fig(dim=dim)
        self.axs.scatter(*x, s=0.5)
        self.axs.set_title("{} n={:d}".format(title, num))
        if title == None:
            self.SavePng_Serial()
        else:
            self.SavePng_Serial(self.tempname + "_" + title + ".png")
        plt.close()


if (__name__ == '__main__'):
    obj = MonteCarlo()
