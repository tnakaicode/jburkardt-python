#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.append(os.path.join('../'))
from base import plot2d

obj = plot2d()

def monomial_value(m, n, e, x):

    # *****************************************************************************80
    #
    # MONOMIAL_VALUE evaluates a monomial.
    #
    #  Discussion:
    #
    #    This routine evaluates a monomial of the form
    #
    #      product ( 1 <= i <= m ) x(i)^e(i)
    #
    #    The combination 0.0^0, if encountered, is treated as 1.0.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, integer E(M), the exponents.
    #
    #    Input, real X(M,N), the point coordinates.
    #
    #    Output, real V(N), the monomial values.
    #
    import numpy as np

    v = np.ones(n)

    for i in range(0, m):
        if (0 != e[i]):
            for j in range(0, n):
                v[j] = v[j] * x[i, j] ** e[i]

    return v


def monomial_value_test():

    # *****************************************************************************80
    #
    # MONOMIAL_VALUE_TEST tests MONOMIAL_VALUE on sets of data in various dimensions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('MONOMIAL_VALUE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use monomial_value() to evaluate some monomials')
    print('  in dimensions 1 through 3.')

    e_min = -3
    e_max = 6
    n = 5
    seed = 123456789
    x_min = -2.0
    x_max = +10.0

    for m in range(1, 4):

        print('')
        print('  Spatial dimension M =  %d' % (m))

        e, seed = i4vec_uniform_ab(m, e_min, e_max, seed)
        i4vec_transpose_print(m, e, '  Exponents:')
        x, seed = r8mat_uniform_ab(m, n, x_min, x_max, seed)
#
#  To make checking easier, make the X values integers.
#
        for i in range(0, m):
            for j in range(0, n):
                x[i, j] = round(x[i, j])

        v = monomial_value(m, n, e, x)

        print('')
        print('   V(X)         ', end='')
        for i in range(0, m):
            print('      X(%d)' % (i), end='')
        print('')
        print('')
        for j in range(0, n):
            print('%14.6g  ' % (v[j]), end='')
            for i in range(0, m):
                print('%10.4f' % (x[i, j]), end='')
            print('')
#
#  Terminate.
#
    print('')
    print('MONOMIAL_VALUE_TEST')
    print('  Normal end of execution.')
    return


def r8mat_transpose_print(m, n, a, title):

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT prints an R8MAT, transposed.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, real A(M,N), the matrix.
    #
    #    Input, string TITLE, a title.
    #
    r8mat_transpose_print_some(m, n, a, 0, 0, m - 1, n - 1, title)

    return


def r8mat_transpose_print_test():

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT_TEST tests R8MAT_TRANSPOSE_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8MAT_TRANSPOSE_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_TRANSPOSE_PRINT prints an R8MAT.')

    m = 4
    n = 3
    v = np.array([
        [11.0, 12.0, 13.0],
        [21.0, 22.0, 23.0],
        [31.0, 32.0, 33.0],
        [41.0, 42.0, 43.0]], dtype=np.float64)
    r8mat_transpose_print(m, n, v, '  Here is an R8MAT, transposed:')
#
#  Terminate.
#
    print('')
    print('R8MAT_TRANSPOSE_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_transpose_print_some(m, n, a, ilo, jlo, ihi, jhi, title):

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT_SOME prints a portion of an R8MAT, transposed.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns of the matrix.
    #
    #    Input, real A(M,N), an M by N matrix to be printed.
    #
    #    Input, integer ILO, JLO, the first row and column to print.
    #
    #    Input, integer IHI, JHI, the last row and column to print.
    #
    #    Input, string TITLE, a title.
    #
    incx = 5

    print('')
    print(title)

    if (m <= 0 or n <= 0):
        print('')
        print('  (None)')
        return

    for i2lo in range(max(ilo, 0), min(ihi, m - 1), incx):

        i2hi = i2lo + incx - 1
        i2hi = min(i2hi, m - 1)
        i2hi = min(i2hi, ihi)

        print('')
        print('  Row: ', end='')

        for i in range(i2lo, i2hi + 1):
            print('%7d       ' % (i), end='')

        print('')
        print('  Col')

        j2lo = max(jlo, 0)
        j2hi = min(jhi, n - 1)

        for j in range(j2lo, j2hi + 1):

            print('%7d :' % (j), end='')

            for i in range(i2lo, i2hi + 1):
                print('%12g  ' % (a[i, j]), end='')

            print('')

    return


def r8mat_transpose_print_some_test():

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT_SOME_TEST tests R8MAT_TRANSPOSE_PRINT_SOME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8MAT_TRANSPOSE_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_TRANSPOSE_PRINT_SOME prints some of an R8MAT, transposed.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_transpose_print_some(
        m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:')
#
#  Terminate.
#
    print('')
    print('R8MAT_TRANSPOSE_PRINT_SOME_TEST:')
    print('  Normal end of execution.')
    return


def r8vec_uniform_01(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(N), the vector of pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    import numpy as np
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8VEC_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8VEC_UNIFORM_01 - Fatal error!')

    x = np.zeros(n)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        if (seed < 0):
            seed = seed + i4_huge

        x[i] = seed * 4.656612875E-10

    return x, seed


def r8vec_uniform_01_test():

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    n = 10
    seed = 123456789

    print('')
    print('R8VEC_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_UNIFORM_01 computes a random R8VEC.')
    print('')
    print('  Initial seed is %d' % (seed))

    v, seed = r8vec_uniform_01(n, seed)

    r8vec_print(n, v, '  Random R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_UNIFORM_01_TEST:')
    print('  Normal end of execution.')
    return


def reference_to_physical_t3(t, n, ref):

    # *****************************************************************************80
    #
    # REFERENCE_TO_PHYSICAL_T3 maps a reference point to a physical point.
    #
    #  Discussion:
    #
    #    Given the vertices of an order 3 physical triangle and a point
    #    (XSI,ETA) in the reference triangle, the routine computes the value
    #    of the corresponding image point (X,Y) in physical space.
    #
    #    Note that this routine may also be appropriate for an order 6
    #    triangle, if the mapping between reference and physical space
    #    is linear.  This implies, in particular, that the sides of the
    #    image triangle are straight and that the "midside" nodes in the
    #    physical triangle are halfway along the sides of
    #    the physical triangle.
    #
    #  Reference Element T3:
    #
    #    |
    #    1  3
    #    |  |\
    #    |  | \
    #    S  |  \
    #    |  |   \
    #    |  |    \
    #    0  1-----2
    #    |
    #    +--0--R--1-->
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 July 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real T(2,3), the coordinates of the vertices.  The vertices are assumed
    #    to be the images of (0,0), (1,0) and (0,1) respectively.
    #
    #    Input, integer N, the number of points to transform.
    #
    #    Input, real REF(2,N), the coordinates of points in the reference space.
    #
    #    Output, real PHY(2,N), the coordinates of the corresponding points in the
    #    physical space.
    #
    import numpy as np

    phy = np.zeros([2, n])

    for i in range(0, 2):

        phy[i, :] = t[i, 0] * (1.0 - ref[0, :] - ref[1, :]) \
            + t[i, 1] * ref[0, :]              \
            + t[i, 2] * ref[1, :]

    return phy


def reference_to_physical_t3_test():

    # *****************************************************************************80
    #
    # REFERENCE_TO_PHYSICAL_T3_TEST tests REFERENCE_TO_PHYSICAL_T3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 July 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('REFERENCE_TO_PHYSICAL_T3_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  REFERENCE_TO_PHYSICAL_T3 maps points in a reference triangle')
    print('  to points in a physical triangle.')

    t = np.array([
        [2.0, 3.0, 0.0],
        [0.0, 4.0, 3.0]])

    n = 3

    ref = np.array([
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]])

    r8mat_transpose_print(2, 3, t, '  XY triangle vertices:')

    phy = reference_to_physical_t3(t, n, ref)

    print('')
    print('  Apply map to RS triangle vertices.')
    print('  Recover XY vertices (2,0), (3,4) and (0,3).')
    print('')

    for j in range(0, 3):
        print('  V(%d) = ( %g, %g )' % (j, phy[0, j], phy[1, j]))
#
#  Terminate.
#
    print('')
    print('REFERENCE_TO_PHYSICAL_T3_TEST:')
    print('  Normal end of execution.')
    return


def timestamp():

    # *****************************************************************************80
    #
    # TIMESTAMP prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import time

    t = time.time()
    print(time.ctime(t))

    return None


def timestamp_test():

    # *****************************************************************************80
    #
    # TIMESTAMP_TEST tests TIMESTAMP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import platform

    print('')
    print('TIMESTAMP_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TIMESTAMP prints a timestamp of the current date and time.')
    print('')

    timestamp()
#
#  Terminate.
#
    print('')
    print('TIMESTAMP_TEST:')
    print('  Normal end of execution.')
    return


def triangle01_sample(n, seed):

    # *****************************************************************************80
    #
    # TRIANGLE01_SAMPLE samples the interior of the unit triangle in 2D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Reuven Rubinstein,
    #    Monte Carlo Optimization, Simulation, and Sensitivity
    #    of Queueing Networks,
    #    Krieger, 1992,
    #    ISBN: 0894647644,
    #    LC: QA298.R79.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real XY(2,N), the points.
    #
    import numpy as np

    m = 2

    xy = np.zeros([m, n])

    for j in range(0, n):

        e, seed = r8vec_uniform_01(m + 1, seed)

        e = - np.log(e)

        d = np.sum(e)

        xy[0:2, j] = e[0:2] / d

    return xy, seed


def triangle01_sample_test():

    # *****************************************************************************80
    #
    # TRIANGLE01_SAMPLE_TEST tests TRIANGLE01_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    seed = 123456789
    t = np.array([
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0]])

    print('')
    print('TRIANGLE01_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TRIANGLE01_SAMPLE samples the unit triangle.')

    r8mat_transpose_print(2, 3, t, '  Triangle vertices:')

    n = 10
    xy, seed = triangle01_sample(n, seed)
    r8mat_transpose_print(2, n, xy, '  Sample points:')
#
#  Terminate.
#
    print('')
    print('TRIANGLE01_SAMPLE_TEST')
    print('  Normal end of execution.')
    return


def triangle_area(t):

    # *****************************************************************************80
    #
    # TRIANGLE_AREA computes the area of a triangle in 2D.
    #
    #  Discussion:
    #
    #    If the triangle's vertices are given in counterclockwise order,
    #    the area will be positive.  If the triangle's vertices are given
    #    in clockwise order, the area will be negative!
    #
    #    An earlier version of this routine always returned the absolute
    #    value of the computed area.  I am convinced now that that is
    #    a less useful result!  For instance, by returning the signed
    #    area of a triangle, it is possible to easily compute the area
    #    of a nonconvex polygon as the sum of the (possibly negative)
    #    areas of triangles formed by node 1 and successive pairs of vertices.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real T(2,3), the triangle vertices.
    #
    #    Output, real AREA, the area of the triangle.
    #
    area = 0.5 * (
        t[0, 0] * (t[1, 1] - t[1, 2])
        + t[0, 1] * (t[1, 2] - t[1, 0])
        + t[0, 2] * (t[1, 0] - t[1, 1]))

    return area


def triangle_area_test():

    # *****************************************************************************80
    #
    # TRIANGLE_AREA_TEST tests TRIANGLE_AREA.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    t = np.array([
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 0.0]])

    print('')
    print('TRIANGLE_AREA_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TRIANGLE_AREA computes the area of a triangle.')

    r8mat_transpose_print(2, 3, t, '  Triangle vertices (columns)')

    area = triangle_area(t)

    print('')
    print('  Triangle area is %g' % (area))
#
#  Terminate.
#
    print('')
    print('TRIANGLE_AREA_TEST')
    print('  Normal end of execution.')
    return


def triangle_monte_carlo(t, n, triangle_integrand, seed):

    # *****************************************************************************80
    #
    # TRIANGLE_MONTE_CARLO applies the Monte Carlo rule to integrate a function.
    #
    #  Discussion:
    #
    #    The function f(x,y) is to be integrated over a triangle T.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 February 2010
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real T(2,3), the triangle vertices.
    #
    #    Input, integer N, the number of sample points.
    #
    #    Input, external TRIANGLE_INTEGRAND, the integrand routine.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real RESULT, the approximate integral.
    #
    import numpy as np

    area = triangle_area(t)

    p, seed = triangle01_sample(n, seed)

    p2 = reference_to_physical_t3(t, n, p)

    fp = triangle_integrand(p2)

    result = area * np.sum(fp[:]) / float(n)
    
    obj.axs.scatter(*p, s=0.5)
    obj.axs.set_title("n={:d}".format(n))
    obj.SavePng_Serial()
    plt.close()
    obj.new_fig()

    return result, seed


def triangle_monte_carlo_test():

    # *****************************************************************************80
    #
    # TRIANGLE_MONTE_CARLO_TEST estimates integrals over a general triangle.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 July 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    global e

    m = 2

    e_test = np.array([
        [0, 0],
        [1, 0],
        [0, 1],
        [2, 0],
        [1, 1],
        [0, 2],
        [3, 0]])

    print('')
    print('TRIANGLE_MONTE_CARLO_TEST')
    print('  TRIANGLE_MONTE_CARLO estimates an integral over')
    print('  a general triangle using the Monte Carlo method.')

    t = np.array([
        [2.0, 3.0, 0.0],
        [0.0, 4.0, 3.0]])

    r8mat_transpose_print(2, 3, t, '  Triangle vertices:')

    seed = 123456789

    print('')
    print('         N        1               X               Y '),
    print('             X^2               XY             Y^2             X^3')
    print('')

    n = 1
    e = np.zeros(m, dtype=np.int32)

    while (n <= 65536):

        print('  %8d' % (n)),

        for j in range(0, 7):

            e[0:m] = e_test[j, 0:m]

            result, seed = triangle_monte_carlo(t, n, triangle_integrand, seed)

            print('  %14.6g' % (result)),

        print('')

        n = 2 * n
#
#  Terminate.
#
    print('')
    print('TRIANGLE_MONTE_CARLO_TEST:')
    print('  Normal end of execution.')
    return


def triangle_integrand(xy):

    # *****************************************************************************80
    #
    # TRIANGLE_INTEGRAND is a sample integrand function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real XY(XY_NUM), the number of evaluation points.
    #
    #    Output, real FXY(XY_NUM), the function values.
    #
    m = 2
    n = xy.shape[1]

    fxy = monomial_value(m, n, e, xy)

    return fxy


def triangle_monte_carlo_test01():

    # *****************************************************************************80
    #
    # TRIANGLE_MONTE_CARLO_TEST01 samples the unit triangle.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 August 2009
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    t = np.array([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]])

    print('')
    print('TRIANGLE_MONTE_CARLO_TEST01')
    print('  Integrate xy^3')
    print('  Integration region is the unit triangle.')
    print('  Use an increasing number of points N.')

    seed = 123456789

    print('')
    print('     N          XY^3')
    print('')

    n = 1

    while (n <= 65536):

        result, seed = triangle_monte_carlo(t, n, triangle_integrand, seed)

        print('  %8d  %14f' % (n, result))

        n = 2 * n

    return


def triangle_integrand(p):

    # *****************************************************************************80
    #
    # TRIANGLE_INTEGRAND evaluates xy^3
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 August 2009
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real P(2,P_NUM), the evaluation points.
    #
    #    Output, real FP(P_NUM), the integrand values.
    #
    fp = p[0, :] * p[1, :] ** 3

    return fp


def triangle_monte_carlo_test02():

    # *****************************************************************************80
    #
    # TRIANGLE_MONTE_CARLO_TEST02 samples a general triangle.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 July 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    t = np.array([
        [2.0, 3.0, 0.0],
        [0.0, 4.0, 3.0]])

    r8mat_transpose_print(2, 3, t, '  Triangle vertices:')

    print('')
    print('TRIANGLE_MONTE_CARLO_TEST02')
    print('  Integrate xy^3')
    print('  Integration region is a general triangle.')
    print('  Use an increasing number of points N.')

    seed = 123456789

    print('')
    print('     N          XY^3')
    print('')

    n = 1

    while (n <= 65536):

        result, seed = triangle_monte_carlo(t, n, triangle_integrand, seed)

        print('  %8d  %14f' % (n, result))

        n = 2 * n

    return


def triangle_integrand(p):

    # *****************************************************************************80
    #
    # TRIANGLE_INTEGRAND evaluates xy^3
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 August 2009
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real P(2,P_NUM), the evaluation points.
    #
    #    Output, real FP(P_NUM), the integrand values.
    #
    fp = p[0, :] * p[1, :] ** 3

    return fp


def triangle_monte_carlo_tests():

    # *****************************************************************************80
    #
    # TRIANGLE_MONTE_CARLO_TESTS tests the TRIANGLE_MONTE_CARLO library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 July 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('TRIANGLE_MONTE_CARLO_TESTS')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the TRIANGLE_MONTE_CARLO library.')

    triangle_area_test
    reference_to_physical_t3_test()
    triangle01_sample_test()
    triangle_monte_carlo_test()
#
#  Sample on the unit triangle, integrating XY^3.
#
    triangle_monte_carlo_test01()
#
#  Sample on a general triangle, integrating X*Y^3.
#
    triangle_monte_carlo_test02()
#
#  Terminate.
#
    print('')
    print('TRIANGLE_MONTE_CARLO_TESTS:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    triangle_monte_carlo_tests()
    timestamp()
