#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.append(os.path.join('../'))
from base import plot2d, plot3d
obj = plot2d()


def ellipse_area1(a, r):

    # *****************************************************************************80
    #
    # ELLIPSE_AREA1 returns the area of an ellipse defined by a matrix.
    #
    #  Discussion:
    #
    #    The points X in the ellipse are described by a 2 by 2
    #    positive definite symmetric matrix A, and a "radius" R, such that
    #      X' * A * X <= R * R
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A(2,2), the matrix that describes
    #    the ellipsoid.  A must be symmetric and positive definite.
    #
    #    Input, real R, the "radius" of the ellipse.
    #
    #    Output, real VALUE, the area of the ellipse.
    #
    import numpy as np

    value = r * r * np.pi / np.sqrt(a[0, 0] * a[1, 1] - a[1, 0] * a[0, 1])

    return value


def ellipse_area1_test():

    # *****************************************************************************80
    #
    # ELLIPSE_AREA1_TEST tests ELLIPSE_AREA1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('ELLIPSE_AREA1_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  ELLIPSE_AREA1 computes the area of an ellipse.')

    r = 10.0
    a = np.array([[5.0, 1.0], [1.0, 2.0]])
    area = ellipse_area1(a, r)
    print('')
    print('  R = %g' % (r))
    r8mat_print(2, 2, a, '  Matrix A in ellipse definition x*A*x=r^2')
    print('  Area = %g' % (area))
#
#  Terminate.
#
    print('')
    print('ELLIPSE_AREA1_TEST')
    print('  Normal end of execution.')
    return


def ellipse_area2(a, b, c, d):

    # *****************************************************************************80
    #
    # ELLIPSE_AREA2 returns the area of an ellipse defined by an equation.
    #
    #  Discussion:
    #
    #    The ellipse is described by the formula
    #      a x^2 + b xy + c y^2 = d
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, B, C, coefficients on the left hand side.
    #
    #    Input, real D, the right hand side.
    #
    #    Output, real VALUE, the area of the ellipse.
    #
    import numpy as np

    value = 2.0 * d * d * np.pi / np.sqrt(4.0 * a * c - b * b)

    return value


def ellipse_area2_test():

    # *****************************************************************************80
    #
    # ELLIPSE_AREA2_TEST tests ELLIPSE_AREA2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('ELLIPSE_AREA2_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  ELLIPSE_AREA2 computes the area of an ellipse.')

    a = 5.0
    b = 2.0
    c = 2.0
    d = 10.0

    area = ellipse_area2(a, b, c, d)
    print('')
    print('  Ellipse: %g * x^2 + %g * xy + %g * y^2 = %g' % (a, b, c, d))
    print('  Area = %g' % (area))
#
#  Terminate.
#
    print('')
    print('ELLIPSE_AREA2_TEST')
    print('  Normal end of execution.')
    return


def ellipse_monte_carlo_test():

    # *****************************************************************************80
    #
    # ELLIPSE_MONTE_CARLO_TEST uses ELLIPSE01_SAMPLE to estimate an integral.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 April 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    a = np.array([
        [9.0, 1.0],
        [1.0, 4.0]])

    e_test = np.array([
        [0, 0],
        [1, 0],
        [0, 1],
        [2, 0],
        [1, 1],
        [0, 2],
        [3, 0]])

    r = 2.0

    print('')
    print('ELLIPSE_MONTE_CARLO_TEST')
    print('  Use ELLIPSE01_SAMPLE to estimate integrals')
    print('  in the ellipse x'' * A * x <= r^2.')

    obj.create_tempdir(-1)
    seed = 123456789

    print('')
    txt = " \tN"
    for e in e_test:
        txt += "\tX^{:d} Y^{:d}".format(*e)
    print(txt)
    print('')

    n = 1
    while (n <= 65536):
        x, seed = ellipse_sample(n, a, r, seed)
        print('  %8d' % (n), end='')
        for e in e_test:
            value = monomial_value(2, n, e, x)
            result = ellipse_area1(a, r) * np.sum(value[0:n]) / float(n)
            print('\t%14.6g' % (result), end='')
        print('')

        obj.axs.scatter(*x, s=0.5)
        obj.axs.set_title("n={:d}".format(n))
        obj.axs.set_xlim(-0.25, 0.25)
        obj.axs.set_ylim(-0.75, 0.75)
        obj.SavePng_Serial(obj.rootname)
        plt.close()
        obj.new_fig()

        n = 2 * n
#
#  Terminate.
#
    print('')
    print('ELLIPSE_MONTE_CARLO_TEST:')
    print('  Normal end of execution.')
    return


def ellipse_sample(n, a, r, seed):

    # *****************************************************************************80
    #
    # ELLIPSE_SAMPLE samples points in an ellipse.
    #
    #  Discussion:
    #
    #    The points X in the ellipse are described by a 2 by 2
    #    positive definite symmetric matrix A, and a "radius" R, such that
    #      X' * A * X <= R * R
    #
    #    If the ellipse is described by the formula
    #      a x^2 + b xy + c y^2 = d
    #    then
    #      A = (  a  b/2 )
    #          ( b/2  c  )
    #      R = sqrt ( d )
    #
    #    The algorithm computes the Cholesky factorization of A:
    #      A = U' * U.
    #    A set of uniformly random points Y is generated, satisfying:
    #      Y' * Y <= R * R.
    #    The appropriate points in the ellipsoid are found by solving
    #      U * X = Y
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 April 2014
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
    #    Wiley, 1986.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real A(2,2), the matrix that describes the ellipse.
    #
    #    Input, real R, the right hand side of the ellipse equation.
    #
    #    Input/output, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(2,N), the points.
    #
    import numpy as np
#
#  Get the factor U such that U' * U = A.
#
    u_fa = r8po_fa(2, a)
#
#  Get the points Y that satisfy Y' * Y = R * R.
#
    x, seed = uniform_in_sphere01_map(2, n, seed)

    x = r * x
#
#  Solve U * X = Y.
#
    s = np.zeros(2)
    t = np.zeros(2)

    for j in range(0, n):
        t[0:2] = x[0:2, j]
        s[0:2] = r8po_sl(2, u_fa, t)
        x[0:2, j] = s[0:2]

    return x, seed


def ellipse_sample_test():

    # *****************************************************************************80
    #
    # ELLIPSE_SAMPLE_TEST tests ELLIPSE_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('ELLIPSE_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  ELLIPSE_SAMPLE computes points uniformly distributed')
    print('  inside an ellipse x\'*A*x=r^2.')

    n = 10
    a = np.array([[5.0, 1.0], [1.0, 2.0]])
    r = 10.0
    seed = 123456789

    x, seed = ellipse_sample(n, a, r, seed)

    r8mat_transpose_print(2, n, x, '  Random points inside ellipse')
#
#  Terminate.
#
    print('')
    print('ELLIPSE_SAMPLE_TEST')
    print('  Normal end of execution.')
    return


def i4vec_print(n, a, title):

    # *****************************************************************************80
    #
    # I4VEC_PRINT prints an I4VEC.
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
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, integer A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d  %6d' % (i, a[i]))

    return


def i4vec_print_test():

    # *****************************************************************************80
    #
    # I4VEC_PRINT_TEST tests I4VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('I4VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_PRINT prints an I4VEC.')

    n = 4
    v = np.array([91, 92, 93, 94], dtype=np.int32)
    i4vec_print(n, v, '  Here is an I4VEC:')
#
#  Terminate.
#
    print('')
    print('I4VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def i4vec_transpose_print(n, a, title):

    # *****************************************************************************80
    #
    # I4VEC_TRANSPOSE_PRINT prints an I4VEC "transposed".
    #
    #  Example:
    #
    #    A = (/ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 /)
    #    TITLE = 'My vector:  '
    #
    #    My vector:
    #
    #       1    2    3    4    5
    #       6    7    8    9   10
    #      11
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of components of the vector.
    #
    #    Input, integer A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    if (0 < len(title)):
        print('')
        print(title)

    if (0 < n):
        for i in range(0, n):
            print('%8d' % (a[i]), end='')
            if ((i + 1) % 10 == 0 or i == n - 1):
                print('')
    else:
        print('  (empty vector)')

    return


def i4vec_transpose_print_test():

    # *****************************************************************************80
    #
    # I4VEC_TRANSPOSE_PRINT_TEST tests I4VEC_TRANSPOSE_PRINT.
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
    import numpy as np
    import platform

    print('')
    print('I4VEC_TRANSPOSE_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_TRANSPOSE_PRINT prints an I4VEC')
    print('  with 5 entries to a row, and an optional title.')

    n = 12
    a = np.zeros(n, dtype=np.int32)

    for i in range(0, n):
        a[i] = i + 1

    i4vec_transpose_print(n, a, '  My array:  ')
#
#  Terminate.
#
    print('')
    print('I4VEC_TRANSPOSE_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def i4vec_uniform_ab(n, a, b, seed):

    # *****************************************************************************80
    #
    # I4VEC_UNIFORM_AB returns a scaled pseudorandom I4VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 April 2013
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
    #    Input, integer A, B, the minimum and maximum acceptable values.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer C(N), the randomly chosen integer vector.
    #
    #    Output, integer SEED, the updated seed.
    #
    import numpy as np
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('I4VEC_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('I4VEC_UNIFORM_AB - Fatal error!')

    a = round(a)
    b = round(b)

    c = np.zeros(n, dtype=np.int32)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        seed = (seed % i4_huge)

        if (seed < 0):
            seed = seed + i4_huge

        r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
        r = (1.0 - r) * (min(a, b) - 0.5) \
            + r * (max(a, b) + 0.5)
#
#  Use rounding to convert R to an integer between A and B.
#
        value = round(r)

        value = max(value, min(a, b))
        value = min(value, max(a, b))

        c[i] = value

    return c, seed


def i4vec_uniform_ab_test():

    # *****************************************************************************80
    #
    # I4VEC_UNIFORM_AB_TEST tests I4VEC_UNIFORM_AB.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    n = 20
    a = -100
    b = 200
    seed = 123456789

    print('')
    print('I4VEC_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_UNIFORM_AB computes pseudorandom values')
    print('  in an interval [A,B].')
    print('')
    print('  The lower endpoint A = %d' % (a))
    print('  The upper endpoint B = %d' % (b))
    print('  The initial seed is %d' % (seed))
    print('')

    v, seed = i4vec_uniform_ab(n, a, b, seed)

    i4vec_print(n, v, '  The random vector:')
#
#  Terminate.
#
    print('')
    print('I4VEC_UNIFORM_AB_TEST:')
    print('  Normal end of execution.')
    return


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


def r8mat_print(m, n, a, title):

    # *****************************************************************************80
    #
    # R8MAT_PRINT prints an R8MAT.
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
    r8mat_print_some(m, n, a, 0, 0, m - 1, n - 1, title)

    return


def r8mat_print_test():

    # *****************************************************************************80
    #
    # R8MAT_PRINT_TEST tests R8MAT_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8MAT_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_PRINT prints an R8MAT.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_print(m, n, v, '  Here is an R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_print_some(m, n, a, ilo, jlo, ihi, jhi, title):

    # *****************************************************************************80
    #
    # R8MAT_PRINT_SOME prints out a portion of an R8MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 February 2015
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

    for j2lo in range(max(jlo, 0), min(jhi + 1, n), incx):

        j2hi = j2lo + incx - 1
        j2hi = min(j2hi, n)
        j2hi = min(j2hi, jhi)

        print('')
        print('  Col: ', end='')

        for j in range(j2lo, j2hi + 1):
            print('%7d       ' % (j), end='')

        print('')
        print('  Row')

        i2lo = max(ilo, 0)
        i2hi = min(ihi, m)

        for i in range(i2lo, i2hi + 1):

            print('%7d :' % (i), end='')

            for j in range(j2lo, j2hi + 1):
                print('%12g  ' % (a[i, j]), end='')

            print('')

    return


def r8mat_print_some_test():

    # *****************************************************************************80
    #
    # R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
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
    print('R8MAT_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_PRINT_SOME prints some of an R8MAT.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_print_some(m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_PRINT_SOME_TEST:')
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


def r8_normal_01(seed):

    # *****************************************************************************80
    #
    # R8_NORMAL_01 samples the standard normal probability distribution.
    #
    #  Discussion:
    #
    #    The standard normal probability distribution function (PDF) has
    #    mean 0 and standard deviation 1.
    #
    #    The Box-Muller method is used.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the standard normal PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    import numpy as np

    r1, seed = r8_uniform_01(seed)
    r2, seed = r8_uniform_01(seed)

    x = np.sqrt(- 2.0 * np.log(r1)) * np.cos(2.0 * np.pi * r2)

    return x, seed


def r8_normal_01_test():

    # *****************************************************************************80
    #
    # R8_NORMAL_01_TEST tests R8_NORMAL_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    seed = 123456789
    test_num = 20

    print('')
    print('R8_NORMAL_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_NORMAL_01 generates normally distributed')
    print('  random values.')
    print('  Using initial random number seed = %d' % (seed))
    print('')

    for test in range(0, test_num):

        x, seed = r8_normal_01(seed)
        print('  %f' % (x))
#
#  Terminate.
#
    print('')
    print('R8_NORMAL_01_TEST')
    print('  Normal end of execution.')
    return


def r8po_fa(n, a):

    # *****************************************************************************80
    #
    # R8PO_FA factors a R8PO matrix.
    #
    #  Discussion:
    #
    #    The R8PO storage format is appropriate for a symmetric positive definite
    #    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
    #    upper triangular matrix, so it will be in R8GE storage format.)
    #
    #    Only the diagonal and upper triangle of the square array are used.
    #    This same storage scheme is used when the matrix is factored by
    #    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
    #    is set to zero.
    #
    #    The positive definite symmetric matrix A has a Cholesky factorization
    #    of the form:
    #
    #      A = R' * R
    #
    #    where R is an upper triangular matrix with positive elements on
    #    its diagonal.  This routine overwrites the matrix A with its
    #    factor R.
    #
    #    This function failed miserably when I wrote "r = a", because of a
    #    disastrously misconceived feature of Python, which does not copy
    #    one matrix to another, but makes them both point to the same object.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 August 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Dongarra, Bunch, Moler, Stewart,
    #    LINPACK User's Guide,
    #    SIAM, 1979.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real A(N,N), the matrix in R8PO storage.
    #
    #    Output, real R(N,N), the Cholesky factor R in R8GE storage.
    #
    #    Output, integer INFO, error flag.
    #    0, normal return.
    #    K, error condition.  The principal minor of order K is not
    #    positive definite, and the factorization was not completed.
    #
    import numpy as np
    from sys import exit

    r = np.zeros([n, n])

    for i in range(0, n):
        for j in range(i, n):
            r[i, j] = a[i, j]

    for j in range(0, n):

        for k in range(0, j):
            t = 0.0
            for i in range(0, k):
                t = t + r[i, k] * r[i, j]
            r[k, j] = (r[k, j] - t) / r[k, k]

        t = 0.0
        for i in range(0, j):
            t = t + r[i, j] ** 2

        s = r[j, j] - t

        if (s <= 0.0):
            print('')
            print('R8PO_FA - Fatal error!')
            print('  Factorization fails on column %d.' % (j))
            exit('R8PO_FA - Fatal error!')

        r[j, j] = np.sqrt(s)
#
#  Since the Cholesky factor is stored in R8GE format, be sure to
#  zero out the lower triangle.
#
    for i in range(0, n):
        for j in range(0, i):
            r[i, j] = 0.0

    return r


def r8po_fa_test():

    # *****************************************************************************80
    #
    # R8PO_FA_TEST tests R8PO_FA;
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    n = 5

    print('')
    print('R8PO_FA_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8PO_FA factors a positive definite symmetric')
    print('  linear system,')
    print('')
    print('  Matrix order N = %d' % (n))

    a = np.zeros([n, n])

    for i in range(0, n):
        for j in range(0, n):
            a[i, j] = min(i, j) + 1

    r8mat_print(n, n, a, '  The matrix A:')
#
#  Factor the matrix.
#
    r = r8po_fa(n, a)

    r8mat_print(n, n, r, '  The factor R (a R8UT matrix):')
#
#  Compute the product R' * R.
#
    rtr = np.zeros([n, n])

    for i in range(0, n):
        for j in range(0, n):
            k_hi = min(i + 1, j + 1)
            for k in range(0, k_hi):
                rtr[i, j] = rtr[i, j] + r[k, i] * r[k, j]

    r8mat_print(n, n, rtr, '  The product R\' * R:')
#
#  Terminate
#
    print('')
    print('R8PO_FA_TEST:')
    print('  Normal end of execution.')
    return


def r8po_sl(n, r, b):

    # *****************************************************************************80
    #
    # R8PO_SL solves a R8PO system factored by R8PO_FA.
    #
    #  Discussion:
    #
    #    The R8PO storage format is appropriate for a symmetric positive definite
    #    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
    #    upper triangular matrix, so it will be in R8GE storage format.)
    #
    #    Only the diagonal and upper triangle of the square array are used.
    #    This same storage scheme is used when the matrix is factored by
    #    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
    #    is set to zero.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 August 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Dongarra, Bunch, Moler, Stewart,
    #    LINPACK User's Guide,
    #    SIAM, 1979.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real R(N,N), the Cholesky factor, in R8GE storage,
    #    returned by R8PO_FA.
    #
    #    Input, real B(N), the right hand side.
    #
    #    Output, real X(N), the solution vector.
    #
    import numpy as np

    x = np.zeros(n)

    for i in range(0, n):
        x[i] = b[i]
#
#  Solve R' * y = b.
#
    for k in range(0, n):
        t = 0.0
        for i in range(0, k):
            t = t + x[i] * r[i, k]
        x[k] = (x[k] - t) / r[k, k]
#
#  Solve R * x = y.
#
    for k in range(n - 1, -1, -1):
        x[k] = x[k] / r[k, k]
        for i in range(0, k):
            x[i] = x[i] - r[i, k] * x[k]

    return x


def r8po_sl_test():

    # *****************************************************************************80
    #
    # R8PO_SL_TEST tests R8PO_SL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 August 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    n = 5

    print('')
    print('R8PO_SL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8PO_SL solves a linear system with an R8PO matrix')
    print('  after it has been factored by R8PO_FA.')
    print('')
    print('  Matrix order N = %d' % (n))
#
#  Set (the upper half of) matrix A.
#
    a = np.zeros([n, n])

    for i in range(0, n):
        a[i, i] = 2.0
    for i in range(0, n - 1):
        a[i, i + 1] = -1.0

    r8mat_print(n, n, a, '  Matrix A:')
#
#  Factor the matrix.
#
    r = r8po_fa(n, a)
#
#  Set the right hand side.
#
    b = np.zeros(n)
    b[n - 1] = float(n + 1)
    r8vec_print(n, b, '  Right hand side b:')
#
#  Solve the linear system.
#
    x = r8po_sl(n, r, b)
    r8vec_print(n, x, '  Solution x:')
#
#  Terminate.
#
    print('')
    print('R8PO_SL_TEST')
    print('  Normal end of execution.')
    return


def r8_uniform_01(seed):

    # *****************************************************************************80
    #
    # R8_UNIFORM_01 returns a unit pseudorandom R8.
    #
    #  Discussion:
    #
    #    This routine implements the recursion
    #
    #      seed = 16807 * seed mod ( 2^31 - 1 )
    #      r8_uniform_01 = seed / ( 2^31 - 1 )
    #
    #    The integer arithmetic never requires more than 32 bits,
    #    including a sign bit.
    #
    #    If the initial seed is 12345, then the first three computations are
    #
    #      Input     Output      R8_UNIFORM_01
    #      SEED      SEED
    #
    #         12345   207482415  0.096616
    #     207482415  1790989824  0.833995
    #    1790989824  2035175616  0.947702
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 March 2013
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
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.  SEED should not be 0.
    #
    #    Output, real R, a random value between 0 and 1.
    #
    #    Output, integer SEED, the updated seed.  This would
    #    normally be used as the input seed on the next call.
    #
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    seed = (seed % i4_huge)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8_UNIFORM_01 - Fatal error!')

    k = (seed // 127773)

    seed = 16807 * (seed - k * 127773) - k * 2836

    if (seed < 0):
        seed = seed + i4_huge

    r = seed * 4.656612875E-10

    return r, seed


def r8_uniform_01_test():

    # *****************************************************************************80
    #
    # R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_UNIFORM_01 produces a sequence of random values.')

    seed = 123456789

    print('')
    print('  Using random seed %d' % (seed))

    print('')
    print('  SEED  R8_UNIFORM_01(SEED)')
    print('')
    for i in range(0, 10):
        seed_old = seed
        x, seed = r8_uniform_01(seed)
        print('  %12d  %14f' % (seed, x))

    print('')
    print('  Verify that the sequence can be restarted.')
    print('  Set the seed back to its original value, and see that')
    print('  we generate the same sequence.')

    seed = 123456789
    print('')
    print('  SEED  R8_UNIFORM_01(SEED)')
    print('')

    for i in range(0, 10):
        seed_old = seed
        x, seed = r8_uniform_01(seed)
        print('  %12d  %14f' % (seed, x))
#
#  Terminate.
#
    print('')
    print('R8_UNIFORM_01_TEST')
    print('  Normal end of execution.')
    return


def r8mat_print(m, n, a, title):

    # *****************************************************************************80
    #
    # R8MAT_PRINT prints an R8MAT.
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
    r8mat_print_some(m, n, a, 0, 0, m - 1, n - 1, title)

    return


def r8mat_print_test():

    # *****************************************************************************80
    #
    # R8MAT_PRINT_TEST tests R8MAT_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8MAT_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_PRINT prints an R8MAT.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_print(m, n, v, '  Here is an R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_print_some(m, n, a, ilo, jlo, ihi, jhi, title):

    # *****************************************************************************80
    #
    # R8MAT_PRINT_SOME prints out a portion of an R8MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 February 2015
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

    for j2lo in range(max(jlo, 0), min(jhi + 1, n), incx):

        j2hi = j2lo + incx - 1
        j2hi = min(j2hi, n)
        j2hi = min(j2hi, jhi)

        print('')
        print('  Col: ', end='')

        for j in range(j2lo, j2hi + 1):
            print('%7d       ' % (j), end='')

        print('')
        print('  Row')

        i2lo = max(ilo, 0)
        i2hi = min(ihi, m)

        for i in range(i2lo, i2hi + 1):

            print('%7d :' % (i), end='')

            for j in range(j2lo, j2hi + 1):
                print('%12g  ' % (a[i, j]), end='')

            print('')

    return


def r8mat_print_some_test():

    # *****************************************************************************80
    #
    # R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
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
    print('R8MAT_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_PRINT_SOME prints some of an R8MAT.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_print_some(m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_PRINT_SOME_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_uniform_ab(m, n, a, b, seed):

    # *****************************************************************************80
    #
    # R8MAT_UNIFORM_AB returns a scaled pseudorandom R8MAT.
    #
    #  Discussion:
    #
    #    An R8MAT is an array of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 April 2013
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
    #    Input, integer M, N, the number of rows and columns in the array.
    #
    #    Input, real A, B, the range of the pseudorandom values.
    #
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.
    #
    #    Output, real R(M,N), an array of random values between 0 and 1.
    #
    #    Output, integer SEED, the updated seed.  This would
    #    normally be used as the input seed on the next call.
    #
    import numpy
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8MAT_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8MAT_UNIFORM_AB - Fatal error!')

    r = numpy.zeros([m, n])

    for j in range(0, n):
        for i in range(0, m):

            k = (seed // 127773)

            seed = 16807 * (seed - k * 127773) - k * 2836

            seed = (seed % i4_huge)

            if (seed < 0):
                seed = seed + i4_huge

            r[i, j] = a + (b - a) * seed * 4.656612875E-10

    return r, seed


def r8mat_uniform_ab_test():

    # *****************************************************************************80
    #
    # R8MAT_UNIFORM_AB_TEST tests R8MAT_UNIFORM_AB.
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
    from r8mat_print import r8mat_print

    m = 5
    n = 4
    a = -1.0
    b = +5.0
    seed = 123456789

    print('')
    print('R8MAT_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_UNIFORM_AB computes a random R8MAT.')
    print('')
    print('  %g <= X <= %g' % (a, b))
    print('  Initial seed is %d' % (seed))

    v, seed = r8mat_uniform_ab(m, n, a, b, seed)

    r8mat_print(m, n, v, '  Random R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_UNIFORM_AB_TEST:')
    print('  Normal end of execution.')
    return


def r8vec_normal_01(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_01 returns a unit pseudonormal R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2015
    #
    #  Author:
    #
    #    John Burkardt
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

    x = np.zeros(n)

    for i in range(0, n):
        x[i], seed = r8_normal_01(seed)

    return x, seed


def r8vec_normal_01_test():

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_01_TEST tests R8VEC_NORMAL_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2015
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
    print('R8VEC_NORMAL_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_NORMAL_01 returns a vector of Normal 01 values')
    print('')
    print('  SEED = %d' % (seed))

    r, seed = r8vec_normal_01(n, seed)

    r8vec_print(n, r, '  Vector:')
#
#  Terminate.
#
    print('')
    print('R8VEC_NORMAL_01_TEST:')
    print('  Normal end of execution.')
    return


def r8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_PRINT prints an R8VEC.
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
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d:  %12g' % (i, a[i]))


def r8vec_print_test():

    # *****************************************************************************80
    #
    # R8VEC_PRINT_TEST tests R8VEC_PRINT.
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

    print('')
    print('R8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_PRINT prints an R8VEC.')

    n = 4
    v = np.array([123.456, 0.000005, -1.0E+06, 3.14159265], dtype=np.float64)
    r8vec_print(n, v, '  Here is an R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_PRINT_TEST:')
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


def uniform_in_sphere01_map(m, n, seed):

    # *****************************************************************************80
    #
    # UNIFORM_IN_SPHERE01_MAP maps uniform points in the unit M-dimensional sphere.
    #
    #  Discussion:
    #
    #    The sphere has center 0 and radius 1.
    #
    #    We first generate a point ON the sphere, and then distribute it
    #    IN the sphere.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Russell Cheng,
    #    Random Variate Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998, pages 168.
    #
    #    Reuven Rubinstein,
    #    Monte Carlo Optimization, Simulation, and Sensitivity
    #    of Queueing Networks,
    #    Wiley, 1986, page 232.
    #
    #  Parameters:
    #
    #    Input, integer M, the dimension of the space.
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(M,N), the points.
    #
    import numpy as np

    exponent = 1.0 / float(m)

    x = np.zeros([m, n])

    for j in range(0, n):
        #
        #  Fill a vector with normally distributed values.
        #
        v, seed = r8vec_normal_01(m, seed)
#
#  Compute the length of the vector.
#
        norm = np.linalg.norm(v)
#
#  Normalize the vector.
#
        v[0:m] = v[0:m] / norm
#
#  Now compute a value to map the point ON the sphere INTO the sphere.
#
        r, seed = r8_uniform_01(seed)

        x[0:m, j] = r ** exponent * v[0:m]

    return x, seed


def uniform_in_sphere01_map_test():

    # *****************************************************************************80
    #
    # UNIFORM_IN_SPHERE01_MAP_TEST tests UNIFORM_IN_SPHERE01_MAP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('UNIFORM_IN_SPHERE01_MAP_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  UNIFORM_IN_SPHERE01_MAP computes points uniformly distributed')
    print('  inside the M-dimensional unit sphere.')

    m = 3
    n = 10
    seed = 123456789

    x, seed = uniform_in_sphere01_map(m, n, seed)

    r8mat_transpose_print(m, n, x, '  Random points inside unit 3-sphere')
#
#  Terminate.
#
    print('')
    print('UNIFORM_IN_SPHERE01_MAP_TEST')
    print('  Normal end of execution.')
    return


def ellipse_monte_carlo_tests():

    # *****************************************************************************80
    #
    # ELLIPSE_MONTE_CARLO_TESTS tests the ELLIPSE_MONTE_CARLO library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('ELLIPSE_MONTE_CARLO_TESTS')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the ELLIPSE_MONTE_CARLO library.')

    ellipse_area1_test()
    ellipse_area2_test()
    ellipse_monte_carlo_test()
    ellipse_sample_test()

    print('')
    print('ELLIPSE_MONTE_CARLO_TESTS')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    ellipse_monte_carlo_tests()
    timestamp()
