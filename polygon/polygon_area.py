#! /usr/bin/env python3
#
def polygon_area(n, v):

    # *****************************************************************************80
    #
    # POLYGON_AREA computes the area of a polygon.
    #
    #  Discussion:
    #
    #    AREA = 1/2 * abs ( sum ( 1 <= I <= N ) X(I) * ( Y(I+1) - Y(I-1) ) )
    #    where Y(0) should be replaced by Y(N), and Y(N+1) by Y(1).
    #
    #    If the vertices are given in counterclockwise order, the area
    #    will be positive.  If the vertices are given in clockwise order,
    #    the area will be negative.
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
    #  Parameters:
    #
    #    Input, integer N, the number of vertices of the polygon.
    #
    #    Input, real V(2,N), the vertices.
    #
    #    Output, real AREA, the area of the polygon.
    #

    area = 0.0

    for i in range(0, n):

        im1 = i4_wrap(i - 1, 0, n - 1)
        ip1 = i4_wrap(i + 1, 0, n - 1)
        area = area + v[0, i] * (v[1, ip1] - v[1, im1])

    area = 0.5 * area

    return area


def polygon_area_test():

    # *****************************************************************************80
    #
    # POLYGON_AREA_TEST tests POLYGON_AREA.
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

    test_num = 2
    area_exact_test = np.array([2.0, 6.0])
    n_test = np.array([4, 8])

    print('')
    print('POLYGON_AREA_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_AREA computes the area of a polygon.')

    for test in range(0, test_num):

        n = n_test[test]
        area_exact = area_exact_test[test]

        if (test == 0):

            v = np.array([
                [1.0, 2.0, 1.0, 0.0],
                [0.0, 1.0, 2.0, 1.0]])

        elif (test == 1):

            v = np.array([
                [0.0, 3.0, 3.0, 2.0, 2.0, 1.0, 1.0, 0.0],
                [0.0, 0.0, 3.0, 3.0, 1.0, 1.0, 2.0, 2.0]])

        print('')
        print('  Number of polygonal vertices = %d' % (n))

        r8mat_transpose_print(2, n, v, '  The polygon vertices:')
        area = polygon_area(n, v)

        print('')
        print('  Exact area is        %g' % (area_exact))
        print('  The computed area is %g' % (area))

    print('')
    print('POLYGON_AREA_TEST')
    print('  Normal end of execution.')


def polygon_area_2(n, v):

    # *****************************************************************************80
    #
    # POLYGON_AREA_2 computes the area of a polygon.
    #
    #  Discussion:
    #
    #    The area is the sum of the areas of the triangles formed by
    #    node N with consecutive pairs of nodes.
    #
    #    If the vertices are given in counterclockwise order, the area
    #    will be positive.  If the vertices are given in clockwise order,
    #    the area will be negative.
    #
    #    Thanks to Martin Pineault for noticing that an earlier version
    #    of this routine would not correctly compute the area of a nonconvex
    #    polygon.
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
    #    Adrian Bowyer, John Woodwark,
    #    A Programmer's Geometry,
    #    Butterworths, 1983.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of vertices of the polygon.
    #
    #    Input, real V(2,N), the vertices.
    #
    #    Output, real AREA, the area of the polygon.
    #

    area = 0.0

    for i in range(0, n - 2):

        area_triangle = triangle_area(
            v[0, i], v[1, i],
            v[0, i + 1], v[1, i + 1],
            v[0, n - 1], v[1, n - 1])
        area = area + area_triangle

    return area


def polygon_area_2_test():

    # *****************************************************************************80
    #
    # POLYGON_AREA_2_TEST tests POLYGON_AREA_2.
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

    test_num = 2
    area_exact_test = np.array([2.0, 6.0])
    n_test = np.array([4, 8])

    print('')
    print('POLYGON_AREA_2_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_AREA_2 computes the area of a polygon.')

    for test in range(0, test_num):

        n = n_test[test]
        area_exact = area_exact_test[test]

        if (test == 0):

            v = np.array([
                [1.0, 2.0, 1.0, 0.0],
                [0.0, 1.0, 2.0, 1.0]])

        elif (test == 1):

            v = np.array([
                [0.0, 3.0, 3.0, 2.0, 2.0, 1.0, 1.0, 0.0],
                [0.0, 0.0, 3.0, 3.0, 1.0, 1.0, 2.0, 2.0]])

        print('')
        print('  Number of polygonal vertices = %d' % (n))

        r8mat_transpose_print(2, n, v, '  The polygon vertices:')
        area = polygon_area_2(n, v)

        print('')
        print('  Exact area is        %g' % (area_exact))
        print('  The computed area is %g' % (area))

    print('')
    print('POLYGON_AREA_2_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    polygon_area_test()
    timestamp()
