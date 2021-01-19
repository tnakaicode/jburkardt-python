#! /usr/bin/env python3
#
def polygon_centroid(n, v):

    # *****************************************************************************80
    #
    # POLYGON_CENTROID computes the centroid of a polygon.
    #
    #  Discussion:
    #
    #    Denoting the centroid coordinates by CENTROID, then
    #
    #      CENTROID(1) = Integral ( Polygon interior ) x dx dy / Area ( Polygon )
    #      CENTROID(2) = Integral ( Polygon interior ) y dx dy / Area ( Polygon ).
    #
    #    Green's theorem states that for continuously differentiable functions
    #    M(x,y) and N(x,y),
    #
    #      Integral ( Polygon boundary ) ( M dx + N dy ) =
    #      Integral ( Polygon interior ) ( dN/dx - dM/dy ) dx dy.
    #
    #    Using M(x,y) = 0 and N(x,y) = x^2/2, we get:
    #
    #      CENTROID(1) = 0.5 * Integral ( Polygon boundary ) x^2 dy
    #                  / Area ( Polygon ),
    #
    #    which becomes
    #
    #      CENTROID(1) = 1/6 sum ( 1 <= I <= N )
    #        ( X(I+1) + X(I) ) * ( X(I) * Y(I+1) - X(I+1) * Y(I))
    #        / Area ( Polygon )
    #
    #    where, when I = N, the index "I+1" is replaced by 1.
    #
    #    A similar calculation gives us a formula for CENTROID(2).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Gerard Bashein and Paul Detmer,
    #    Centroid of a Polygon,
    #    Graphics Gems IV,
    #    edited by Paul Heckbert,
    #    AP Professional, 1994.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of sides of the polygon.
    #
    #    Input, real V(2,N), the coordinates of the vertices.
    #
    #    Output, real CENTROID(2,1), the coordinates of the centroid.
    #

    area = 0.0
    centroid = np.zeros(2)

    for i in range(0, n):

        ip1 = i4_wrap(i + 1, 0, n - 1)

        temp = (v[0, i] * v[1, ip1] - v[0, ip1] * v[1, i])

        area = area + temp

        centroid[0] = centroid[0] + (v[0, ip1] + v[0, i]) * temp
        centroid[1] = centroid[1] + (v[1, ip1] + v[1, i]) * temp

    area = area / 2.0

    if (area == 0.0):
        centroid[0] = v[0]
        centroid[1] = v[1]
    else:
        centroid[0] = centroid[0] / (6.0 * area)
        centroid[1] = centroid[1] / (6.0 * area)

    return centroid


def polygon_centroid_test():

    # *****************************************************************************80
    #
    # POLYGON_CENTROID_TEST tests POLYGON_CENTROID.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 4
    v = np.array([
        [1.0, 2.0, 1.0, 0.0],
        [0.0, 1.0, 2.0, 1.0]])

    print('')
    print('POLYGON_CENTROID_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_CENTROID computes the centroid of a polygon.')

    r8mat_transpose_print(2, n, v, '  The polygon vertices:')
    centroid = polygon_centroid(n, v)
    r8vec_print(2, centroid, '  POLYGON_CENTROID:')

    print('')
    print('POLYGON_CENTROID_TEST')
    print('  Normal end of execution.')


def polygon_centroid_2(n, v):

    # *****************************************************************************80
    #
    # POLYGON_CENTROID_2 computes the centroid of a polygon.
    #
    #  Discussion:
    #
    #    The centroid is the area-weighted sum of the centroids of
    #    disjoint triangles that make up the polygon.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Adrian Bowyer and John Woodwark,
    #    A Programmer's Geometry,
    #    Butterworths, 1983.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of sides of the polygon.
    #
    #    Input, real V(2,N), the coordinates of the vertices.
    #
    #    Output, real CENTROID(2), the coordinates of the centroid.
    #

    area = 0.0
    centroid = np.zeros(2)

    for i in range(0, n - 2):

        area_triangle = triangle_area(
            v[0, i], v[1, i],
            v[0, i + 1], v[1, i + 1],
            v[0, n - 1], v[1, n - 1])

        area = area + area_triangle

        centroid[0] = centroid[0] + \
            (v[0, i] + v[0, i + 1] + v[0, n - 1]) * area_triangle / 3.0
        centroid[1] = centroid[1] + \
            (v[1, i] + v[1, i + 1] + v[1, n - 1]) * area_triangle / 3.0

    if (area == 0.0):
        centroid[0] = v[0]
        centroid[1] = v[1]
    else:
        centroid[0] = centroid[0] / area
        centroid[1] = centroid[1] / area

    return centroid


def polygon_centroid_2_test():

    # *****************************************************************************80
    #
    # POLYGON_CENTROID_2_TEST tests POLYGON_CENTROID_2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 4
    v = np.array([
        [1.0, 2.0, 1.0, 0.0],
        [0.0, 1.0, 2.0, 1.0]])

    print('')
    print('POLYGON_CENTROID_2_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_CENTROID_2 computes the centroid of a polygon.')

    r8mat_transpose_print(2, n, v, '  The polygon vertices:')
    centroid = polygon_centroid_2(n, v)
    r8vec_print(2, centroid, '  POLYGON_CENTROID_2:')

    print('')
    print('POLYGON_CENTROID_2_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    polygon_centroid_test()
    timestamp()
