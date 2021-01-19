#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp

from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8vec_transpose_print import r8vec_transpose_print
from r8lib.r8mat_transpose_print import r8mat_transpose_print, r8mat_transpose_print_some

from i4lib.i4_wrap import i4_wrap


def polygon_integral_1(n, v):

    # *****************************************************************************80
    #
    # POLYGON_INTEGRAL_1 integrates the function 1 over a polygon.
    #
    #  Discussion
    #
    #    The polygon is bounded by the points (X(1:N), Y(1:N)).
    #
    #    INTEGRAL = 0.5 * SUM ( 1 <= I <= N )
    #      ( X(I) + X(I-1) ) * ( Y(I) - Y(I-1) )
    #
    #    where X(0) and Y(0) should be replaced by X(N) and Y(N).
    #
    #    Note that the integral of 1 over a polygon is the area of the polygon.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    S F Bockman,
    #    Generalizing the Formula for Areas of Polygons to Moments,
    #    American Mathematical Society Monthly,
    #    1989, pages 131-132.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of vertices of the polygon.
    #    N should be at least 3 for a nonzero result.
    #
    #    Input, real V(2,N), the coordinates of the vertices
    #    of the polygon.  These vertices should be given in counter-clockwise order.
    #
    #    Output, real RESULT, the value of the integral.
    #

    result = 0.0

    if (n < 3):
        print('')
        print('POLYGON_INTEGRAL_1 - Warning!')
        print('  The number of vertices must be at least 3.')
        print('  The input value of N = %d' % (n))
        exit('POLYGON_INTEGRAL_1 - Fatal error!')

    for i in range(0, n):

        im1 = i4_wrap(i - 1, 0, n - 1)
        result = result + 0.5 * (v[0, i] + v[0, im1]) * (v[1, i] - v[1, im1])

    return result


def polygon_integral_1_test():

    # *****************************************************************************80
    #
    # POLYGON_INTEGRAL_1_TEST tests POLYGON_INTEGRAL_1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n1 = 4
    v1 = np.array([
        [0.0, 1.0, 1.0, 0.0],
        [0.0, 0.0, 1.0, 1.0]])

    n2 = 3
    v2 = np.array([
        [1.0, 4.0, 2.0],
        [1.0, 3.0, 5.0]])

    print('')
    print('POLYGON_INTEGRAL_1_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_INTEGRAL_1 integrates 1 over a polygon')
    r8mat_transpose_print(2, n1, v1, '  The polygon vertices:')
    result = polygon_integral_1(n1, v1)
    print('')
    print('  1:    %14.6g' % (result))
    r8mat_transpose_print(2, n2, v2, '  The polygon vertices:')
    result = polygon_integral_1(n2, v2)
    print('')
    print('  1:    %14.6g' % (result))
    print('')
    print('POLYGON_INTEGRAL_1_TEST')
    print('  Normal end of execution.')


def polygon_integral_x(n, v):

    # *****************************************************************************80
    #
    # POLYGON_INTEGRAL_x integrates the function X over a polygon.
    #
    #  Discussion
    #
    #    The polygon is bounded by the points (X(1:N), Y(1:N)).
    #
    #    INTEGRAL = (1/6) * sum ( 1 <= I <= N )
    #      ( X(I)^2 + X(I) * X(I-1) + X(I-1)^2 ) * ( Y(I) - Y(I-1) )
    #
    #    where X(0) and Y(0) should be replaced by X(N) and Y(N).
    #
    #    Note that the integral of 1 over a polygon is the area of the polygon.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    S F Bockman,
    #    Generalizing the Formula for Areas of Polygons to Moments,
    #    American Mathematical Society Monthly,
    #    1989, pages 131-132.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of vertices of the polygon.
    #    N should be at least 3 for a nonzero result.
    #
    #    Input, real V(2,N), the coordinates of the vertices
    #    of the polygon.  These vertices should be given in counter-clockwise order.
    #
    #    Output, real RESULT, the value of the integral.
    #

    result = 0.0

    if (n < 3):
        print('')
        print('POLYGON_INTEGRAL_X - Warning!')
        print('  The number of vertices must be at least 3.')
        print('  The input value of N = %d' % (n))
        exit('POLYGON_INTEGRAL_X - Fatal error!')

    for i in range(0, n):

        im1 = i4_wrap(i - 1, 0, n - 1)
        result = result + (v[0, i] ** 2 + v[0, i] * v[0, im1] + v[0, im1] ** 2) \
            * (v[1, i] - v[1, im1])

    result = result / 6.0

    return result


def polygon_integral_x_test():

    # *****************************************************************************80
    #
    # POLYGON_INTEGRAL_X_TEST tests POLYGON_INTEGRAL_X.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n1 = 4
    v1 = np.array([
        [0.0, 1.0, 1.0, 0.0],
        [0.0, 0.0, 1.0, 1.0]])

    n2 = 3
    v2 = np.array([
        [1.0, 4.0, 2.0],
        [1.0, 3.0, 5.0]])

    print('')
    print('POLYGON_INTEGRAL_X_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_INTEGRAL_X integrates x over a polygon')
    r8mat_transpose_print(2, n1, v1, '  The polygon vertices:')
    result = polygon_integral_x(n1, v1)
    print('')
    print('  x:    %14.6g' % (result))
    r8mat_transpose_print(2, n2, v2, '  The polygon vertices:')
    result = polygon_integral_x(n2, v2)
    print('')
    print('  x:    %14.6g' % (result))
    print('')
    print('POLYGON_INTEGRAL_X_TEST')
    print('  Normal end of execution.')


def polygon_integral_xx(n, v):

    # *****************************************************************************80
    #
    # POLYGON_INTEGRAL_XX integrates the function x^2 over a polygon.
    #
    #  Discussion
    #
    #    The polygon is bounded by the points (X(1:N), Y(1:N)).
    #
    #    INTEGRAL = (1/12) * sum ( 1 <= I <= N )
    #      ( X(I)^3 + X(I)^2 * X(I-1) + X(I) * X(I-1)^2 + X(I-1)^3 )
    #      * ( Y(I) - Y(I-1) )
    #
    #    where X(0) and Y(0) should be replaced by X(N) and Y(N).
    #
    #    Note that the integral of 1 over a polygon is the area of the polygon.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    S F Bockman,
    #    Generalizing the Formula for Areas of Polygons to Moments,
    #    American Mathematical Society Monthly,
    #    1989, pages 131-132.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of vertices of the polygon.
    #    N should be at least 3 for a nonzero result.
    #
    #    Input, real V(2,N), the coordinates of the vertices
    #    of the polygon.  These vertices should be given in counter-clockwise order.
    #
    #    Output, real RESULT, the value of the integral.
    #

    result = 0.0

    if (n < 3):
        print('')
        print('POLYGON_INTEGRAL_XX - Warning!')
        print('  The number of vertices must be at least 3.')
        print('  The input value of N = %d' % (n))
        exit('POLYGON_INTEGRAL_XX - Fatal error!')

    for i in range(0, n):

        im1 = i4_wrap(i - 1, 0, n - 1)
        result = result + (v[0, i] ** 3 + v[0, i] ** 2 * v[0, im1]
                           + v[0, i] * v[0, im1] ** 2 + v[0, im1] ** 3) * (v[1, i] - v[1, im1])

    result = result / 12.0

    return result


def polygon_integral_xx_test():

    # *****************************************************************************80
    #
    # POLYGON_INTEGRAL_XX_TEST tests POLYGON_INTEGRAL_XX.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n1 = 4
    v1 = np.array([
        [0.0, 1.0, 1.0, 0.0],
        [0.0, 0.0, 1.0, 1.0]])

    n2 = 3
    v2 = np.array([
        [1.0, 4.0, 2.0],
        [1.0, 3.0, 5.0]])

    print('')
    print('POLYGON_INTEGRAL_XX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_INTEGRAL_XX integrates x^2 over a polygon')
    r8mat_transpose_print(2, n1, v1, '  The polygon vertices:')
    result = polygon_integral_xx(n1, v1)
    print('')
    print('  x^2:    %14.6g' % (result))
    r8mat_transpose_print(2, n2, v2, '  The polygon vertices:')
    result = polygon_integral_xx(n2, v2)
    print('')
    print('  x^2:    %14.6g' % (result))
    print('')
    print('POLYGON_INTEGRAL_XX_TEST')
    print('  Normal end of execution.')


def polygon_integral_xy(n, v):

    # *****************************************************************************80
    #
    # POLYGON_INTEGRAL_XY integrates the function x*y over a polygon.
    #
    #  Discussion
    #
    #    The polygon is bounded by the points (X(1:N), Y(1:N)).
    #
    #    INTEGRAL = (1/24) * sum ( 1 <= I <= N )
    #      ( Y(I)   * ( 3 * X(I)^2 + 2 * X(I) * X(I-1) +     X(I-1)^2 )
    #      + Y(I-1) * (     X(I)^2 + 2 * X(I) * X(I-1) + 3 * X(I-1)^2 ) )
    #      * ( Y(I) - Y(I-1) )
    #
    #    where X(0) and Y(0) should be replaced by X(N) and Y(N).
    #
    #    Note that the integral of 1 over a polygon is the area of the polygon.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    S F Bockman,
    #    Generalizing the Formula for Areas of Polygons to Moments,
    #    American Mathematical Society Monthly,
    #    1989, pages 131-132.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of vertices of the polygon.
    #    N should be at least 3 for a nonzero result.
    #
    #    Input, real V(2,N), the coordinates of the vertices
    #    of the polygon.  These vertices should be given in counter-clockwise order.
    #
    #    Output, real RESULT, the value of the integral.
    #

    result = 0.0

    if (n < 3):
        print('')
        print('POLYGON_INTEGRAL_XY - Warning!')
        print('  The number of vertices must be at least 3.')
        print('  The input value of N = %d' % (n))
        exit('POLYGON_INTEGRAL_XY - Fatal error!')

    for i in range(0, n):

        im1 = i4_wrap(i - 1, 0, n - 1)
        result = result + (
            v[1, i] * (3.0 * v[0, i] ** 2 + 2.0 * v[0, i] * v[0, im1]
                       + v[0, im1] ** 2) + v[1, im1] * (v[0, i] ** 2 + 2.0 * v[0, i] * v[0, im1]
                                                        + 3.0 * v[0, im1] ** 2)) * (v[1, i] - v[1, im1])

    result = result / 24.0

    return result


def polygon_integral_xy_test():

    # *****************************************************************************80
    #
    # POLYGON_INTEGRAL_XY_TEST tests POLYGON_INTEGRAL_XY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n1 = 4
    v1 = np.array([
        [0.0, 1.0, 1.0, 0.0],
        [0.0, 0.0, 1.0, 1.0]])

    n2 = 3
    v2 = np.array([
        [1.0, 4.0, 2.0],
        [1.0, 3.0, 5.0]])

    print('')
    print('POLYGON_INTEGRAL_XY_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_INTEGRAL_XY integrates x*y over a polygon')
    r8mat_transpose_print(2, n1, v1, '  The polygon vertices:')
    result = polygon_integral_xy(n1, v1)
    print('')
    print('  x*y:    %14.6g' % (result))
    r8mat_transpose_print(2, n2, v2, '  The polygon vertices:')
    result = polygon_integral_xy(n2, v2)
    print('')
    print('  x*y:    %14.6g' % (result))
    print('')
    print('POLYGON_INTEGRAL_XY_TEST')
    print('  Normal end of execution.')


def polygon_integral_y(n, v):

    # *****************************************************************************80
    #
    # POLYGON_INTEGRAL_Y integrates the function y over a polygon.
    #
    #  Discussion
    #
    #    The polygon is bounded by the points (X(1:N), Y(1:N)).
    #
    #    INTEGRAL = (1/6) * sum ( 1 <= I <= N )
    #      - ( Y(I)^2 + Y(I) * Y(I-1) + Y(I-1)^2 ) * ( X(I) - X(I-1) )
    #
    #    where X(0) and Y(0) should be replaced by X(N) and Y(N).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    S F Bockman,
    #    Generalizing the Formula for Areas of Polygons to Moments,
    #    American Mathematical Society Monthly,
    #    1989, pages 131-132.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of vertices of the polygon.
    #    N should be at least 3 for a nonzero result.
    #
    #    Input, real V(2,N), the coordinates of the vertices
    #    of the polygon.  These vertices should be given in counter-clockwise order.
    #
    #    Output, real RESULT, the value of the integral.
    #

    result = 0.0

    if (n < 3):
        print('')
        print('POLYGON_INTEGRAL_Y - Warning!')
        print('  The number of vertices must be at least 3.')
        print('  The input value of N = %d' % (n))
        exit('POLYGON_INTEGRAL_Y - Fatal error!')

    for i in range(0, n):

        im1 = i4_wrap(i - 1, 0, n - 1)
        result = result - (v[1, i] ** 2 + v[1, i] * v[1, im1] + v[1, im1] ** 2) \
            * (v[0, i] - v[0, im1])

    result = result / 6.0

    return result


def polygon_integral_y_test():

    # *****************************************************************************80
    #
    # POLYGON_INTEGRAL_Y_TEST tests POLYGON_INTEGRAL_Y.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n1 = 4
    v1 = np.array([
        [0.0, 1.0, 1.0, 0.0],
        [0.0, 0.0, 1.0, 1.0]])

    n2 = 3
    v2 = np.array([
        [1.0, 4.0, 2.0],
        [1.0, 3.0, 5.0]])

    print('')
    print('POLYGON_INTEGRAL_Y_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_INTEGRAL_Y integrates y over a polygon')
    r8mat_transpose_print(2, n1, v1, '  The polygon vertices:')
    result = polygon_integral_y(n1, v1)
    print('')
    print('  y:    %14.6g' % (result))
    r8mat_transpose_print(2, n2, v2, '  The polygon vertices:')
    result = polygon_integral_y(n2, v2)
    print('')
    print('  y:    %14.6g' % (result))
    print('')
    print('POLYGON_INTEGRAL_Y_TEST')
    print('  Normal end of execution.')


def polygon_integral_yy(n, v):

    # *****************************************************************************80
    #
    # POLYGON_INTEGRAL_YY integrates the function Y^2 over a polygon.
    #
    #  Discussion
    #
    #    The polygon is bounded by the points (X(1:N), Y(1:N)).
    #
    #    INTEGRAL = (1/12) * sum ( 1 <= I <= N )
    #      - ( Y(I)^3 + Y(I)^2 * Y(I-1) + Y(I) * Y(I-1)^2 + Y(I-1)^3 )
    #      * ( X(I) - X(I-1) )
    #
    #    where X(0) and Y(0) should be replaced by X(N) and Y(N).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    S F Bockman,
    #    Generalizing the Formula for Areas of Polygons to Moments,
    #    American Mathematical Society Monthly,
    #    1989, pages 131-132.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of vertices of the polygon.
    #    N should be at least 3 for a nonzero result.
    #
    #    Input, real V(2,N), the coordinates of the vertices
    #    of the polygon.  These vertices should be given in counter-clockwise order.
    #
    #    Output, real RESULT, the value of the integral.
    #

    result = 0.0

    if (n < 3):
        print('')
        print('POLYGON_INTEGRAL_YY - Warning!')
        print('  The number of vertices must be at least 3.')
        print('  The input value of N = %d' % (n))
        exit('POLYGON_INTEGRAL_YY - Fatal error!')

    for i in range(0, n):

        im1 = i4_wrap(i - 1, 0, n - 1)
        result = result - (v[1, i] ** 3 + v[1, i] ** 2 * v[1, im1]
                           + v[1, i] * v[1, im1] ** 2 + v[1, im1] ** 3) * (v[0, i] - v[0, im1])

    result = result / 12.0

    return result


def polygon_integral_yy_test():

    # *****************************************************************************80
    #
    # POLYGON_INTEGRAL_YY_TEST tests POLYGON_INTEGRAL_YY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n1 = 4
    v1 = np.array([
        [0.0, 1.0, 1.0, 0.0],
        [0.0, 0.0, 1.0, 1.0]])

    n2 = 3
    v2 = np.array([
        [1.0, 4.0, 2.0],
        [1.0, 3.0, 5.0]])

    print('')
    print('POLYGON_INTEGRAL_YY_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_INTEGRAL_YY integrates y^2 over a polygon')
    r8mat_transpose_print(2, n1, v1, '  The polygon vertices:')
    result = polygon_integral_yy(n1, v1)
    print('')
    print('  y^2:    %14.6g' % (result))
    r8mat_transpose_print(2, n2, v2, '  The polygon vertices:')
    result = polygon_integral_yy(n2, v2)
    print('')
    print('  y^2:    %14.6g' % (result))
    print('')
    print('POLYGON_INTEGRAL_YY_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    polygon_integral_1_test()
    polygon_integral_x_test()
    polygon_integral_y_test()
    polygon_integral_xy_test()
    polygon_integral_xx_test()
    polygon_integral_yy_test()
    timestamp()
