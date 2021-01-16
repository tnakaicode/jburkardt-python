#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.append(os.path.join('../'))
from base import plot2d, plot3d

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
            print('%8d' % (a[i])),
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
        print('   V(X)         '),
        for i in range(0, m):
            print('      X(%d)' % (i)),
        print('')
        print('')
        for j in range(0, n):
            print('%14.6g  ' % (v[j])),
            for i in range(0, m):
                print('%10.4f' % (x[i, j])),
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
        print('  Col: '),

        for j in range(j2lo, j2hi + 1):
            print('%7d       ' % (j)),

        print('')
        print('  Row')

        i2lo = max(ilo, 0)
        i2hi = min(ihi, m)

        for i in range(i2lo, i2hi + 1):

            print('%7d :' % (i)),

            for j in range(j2lo, j2hi + 1):
                print('%12g  ' % (a[i, j])),

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
        print('  Row: '),

        for i in range(i2lo, i2hi + 1):
            print('%7d       ' % (i)),

        print('')
        print('  Col')

        j2lo = max(jlo, 0)
        j2hi = min(jhi, n - 1)

        for j in range(j2lo, j2hi + 1):

            print('%7d :' % (j)),

            for i in range(i2lo, i2hi + 1):
                print('%12g  ' % (a[i, j])),

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


def simplex_general_sample(m, n, t, seed):

    # *****************************************************************************80
    #
    # SIMPLEX_GENERAL_SAMPLE samples a general simplex in M dimensions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 March 2017
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
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real T(M,M+1), the simplex vertices.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real X(M,N), the points.
    #
    x1, seed = simplex_unit_sample(m, n, seed)

    x = simplex_unit_to_general(m, n, t, x1)

    return x, seed


def simplex_general_sample_test():

    # *****************************************************************************80
    #
    # SIMPLEX_GENERAL_SAMPLE_TEST estimates integrals in 3D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 March 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    m = 3

    e_test = np.array([
        [0, 1, 0, 0, 2, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 2, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 1, 2]], dtype=np.int32)

    t = np.array([
        [1.0, 2.0, 1.0, 1.0],
        [0.0, 0.0, 2.0, 0.0],
        [0.0, 0.0, 0.0, 3.0]])

    print('')
    print('SIMPLEX_GENERAL_SAMPLE_TEST')
    print('  SIMPLEX_GENERAL_SAMPLE computes a Monte Carlo estimate of an')
    print('  integral over the interior of a general simplex in 3D.')

    print('')
    print('  Simplex vertices:')
    print('')
    for j in range(0, 4):
        for i in range(0, 3):
            print('%14.6g' % (t[i, j]), end='')
        print('')

    obj = plot3d()
    obj.create_tempdir(-1)
    seed = 123456789
    
    n = 1
    while (n <= 65536):
        x, seed = simplex_general_sample(m, n, t, seed)
        print('  %8d' % (n), end='')
        for e in e_test:
            value = monomial_value(m, n, e, x)
            result = simplex_general_volume(m, t) * np.sum(value[0:n]) / n
            print('  %14.6g' % (result), end='')
        print('')

        obj.axs.scatter(*x, s=0.5)
        obj.axs.set_title("n={:d}".format(n))
        obj.SavePng_Serial(obj.rootname)
        plt.close()
        obj.new_fig()

        n = 2 * n

    return


def simplex_general_volume(m, t):

    # *****************************************************************************80
    #
    # SIMPLEX_GENERAL_VOLUME computes the volume of a simplex in N dimensions.
    #
    #  Discussion:
    #
    #    The formula is:
    #
    #      volume = 1/M! * det ( B )
    #
    #    where B is the M by M matrix obtained by subtracting one
    #    vector from all the others.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 March 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the dimension of the space.
    #
    #    Input, real T(M,M+1), the vertices.
    #
    #    Output, real VOLUME, the volume of the simplex.
    #
    import numpy as np

    b = np.zeros([m, m])

    b[0:m, 0:m] = t[0:m, 0:m]
    for j in range(0, m):
        b[0:m, j] = b[0:m, j] - t[0:m, m]

    volume = abs(np.linalg.det(b))

    for i in range(1, m + 1):
        volume = volume / float(i)

    return volume


def simplex_unit_monomial_integral(m, e):

    # *****************************************************************************80
    #
    # SIMPLEX_UNIT_MONOMIAL_INTEGRAL: integrals in the unit simplex in M dimensions.
    #
    #  Discussion:
    #
    #    The monomial is F(X) = product ( 1 <= I <= M ) X(I)^E(I).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer E(M), the exponents.
    #    Each exponent must be nonnegative.
    #
    #    Output, real INTEGRAL, the integral.
    #
    from sys import exit

    for i in range(0, m):
        if (e[i] < 0):
            print('')
            print('SIMPLEX_UNIT_MONOMIAL_INTEGRAL - Fatal error!')
            print('  All exponents must be nonnegative.')
            exit('SIMPLEX_UNIT_MONOMIAL_INTEGRAL - Fatal error!')

    k = 0
    integral = 1.0

    for i in range(0, m):

        for j in range(1, e[i] + 1):
            k = k + 1
            integral = integral * float(j) / float(k)

    for i in range(0, m):
        k = k + 1
        integral = integral / float(k)

    return integral


def simplex_unit_monomial_integral_test():

    # *****************************************************************************80
    #
    # SIMPLEX_UNIT_MONOMIAL_INTEGRAL_TEST compares exact and estimated integrals in 3D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    m = 3
    n = 4192
    test_num = 20

    print('')
    print('SIMPLEX_UNIT_MONOMIAL_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Estimate monomial integrals using Monte Carlo')
    print('  over the interior of the unit simplex in M dimensions.')
#
#  Get sample points.
#
    seed = 123456789
    x, seed = simplex_unit_sample(m, n, seed)

    print('')
    print('  Number of sample points used is %d' % (n))
#
#  Randomly choose exponents.
#
    print('')
    print('  We randomly choose the exponents.')
    print('')
    print('  Ex  Ey  Ez     MC-Estimate      Exact           Error')
    print('')

    for test in range(0, test_num):

        e, seed = i4vec_uniform_ab(m, 0, 4, seed)

        value = monomial_value(m, n, e, x)

        result = simplex_unit_volume(m) * np.sum(value) / float(n)
        exact = simplex_unit_monomial_integral(m, e)
        error = abs(result - exact)

        for i in range(0, m):
            print('  %2d' % (e[i])),
        print('  %14.6g  %14.6g  %10.2g' % (result, exact, error))
#
#  Terminate.
#
    print('')
    print('SIMPLEX_UNIT_MONOMIAL_INTEGRAL_TEST:')
    print('  Normal end of execution.')
    return


def simplex_unit_sample(m, n, seed):

    # *****************************************************************************80
    #
    # SIMPLEX_UNIT_SAMPLE samples the unit simplex in M dimensions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 June 2015
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
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real X(M,N), the points.
    #
    import numpy as np

    x = np.zeros([m, n])

    for j in range(0, n):

        e, seed = r8vec_uniform_01(m + 1, seed)

        e_sum = 0.0
        for i in range(0, m + 1):
            e[i] = - np.log(e[i])
            e_sum = e_sum + e[i]

        for i in range(0, m):
            x[i, j] = e[i] / e_sum

    return x, seed


def simplex_unit_sample_test00():

    # *****************************************************************************80
    #
    # SIMPLEX_UNIT_SAMPLE_TEST00 tests SIMPLEX_UNIT_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('SIMPLEX_UNIT_SAMPLE_TEST00')
    print('  Python version: %s' % (platform.python_version()))
    print('  SIMPLEX_UNIT_SAMPLE samples the unit simplex in M dimensions.')

    m = 3
    n = 10
    seed = 123456789

    x, seed = simplex_unit_sample(m, n, seed)

    r8mat_transpose_print(m, n, x, '  Sample points in the unit simplex.')
#
#  Terminate.
#
    print('')
    print('SIMPLEX_UNIT_SAMPLE_TEST00')
    print('  Normal end of execution.')
    return


def simplex_unit_sample_test01():

    # *****************************************************************************80
    #
    # SIMPLEX_UNIT_SAMPLE_TEST01 estimates integrals in 3D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 March 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    m = 3

    e_name = ["U", "V", "W", "X", "Y", "z"]
    e_test = np.array([
        [0, 1, 0, 0, 2, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 2, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 1, 2]], dtype=np.int32)

    print('')
    print('SIMPLEX_UNIT_SAMPLE_TEST01')
    print('  SIMPLEX_UNIT_SAMPLE computes a Monte Carlo estimate of an')
    print('  integral over the interior of the unit simplex in 3D.')

    seed = 123456789

    n = 1
    while (n <= 65536):
        x, seed = simplex_unit_sample(m, n, seed)
        print('  %8d' % (n), end='')
        for e in e_test:
            value = monomial_value(m, n, e, x)
            result = simplex_unit_volume(m) * np.sum(value[0:n]) / n
            print('  %14.6g' % (result), end='')
        print('')

        n = 2 * n

    print('')
    print('     Exact')
    for e in e_test:
        result = simplex_unit_monomial_integral(m, e)
        print('  %14.6g' % (result), end='')

    print('')

    return


def simplex_unit_sample_test02():

    # *****************************************************************************80
    #
    # SIMPLEX_UNIT_SAMPLE_TEST02 estimates integrals in 6D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 March 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    m = 6

    e_test = np.array([
        [0, 1, 0, 0, 0, 2, 0],
        [0, 0, 2, 2, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 2, 6]], dtype=np.int32)

    e = np.zeros(m, dtype=np.int32)

    print('')
    print('SIMPLEX_UNIT_SAMPLE_TEST02')
    print('  SIMPLEX_UNIT_SAMPLE computes a Monte Carlo estimate of an')
    print('  integral over the interior of the unit simplex in 6D.')

    seed = 123456789

    print('')
    print('         N', end='')
    print('        1      ', end='')
    print('        U      ', end='')
    print('         V^2   ', end='')
    print('         V^2W^2', end='')
    print('         X^4   ', end='')
    print('         Y^2Z^2', end='')
    print('         Z^6')
    print('')

    n = 1

    while (n <= 65536):

        x, seed = simplex_unit_sample(m, n, seed)

        print('  %8d' % (n), end='')

        for j in range(0, 7):

            e[0:m] = e_test[0:m, j]

            value = monomial_value(m, n, e, x)

            result = simplex_unit_volume(m) * np.sum(value[0:n]) / n
            print('  %14.6g' % (result), end='')

        print('')

        n = 2 * n

    print('')
    print('     Exact')
    for j in range(0, 7):

        e[0:m] = e_test[0:m, j]

        result = simplex_unit_monomial_integral(m, e)
        print('  %14.6g' % (result), end='')

    print('')

    return


def simplex_unit_to_general(m, n, t, ref):

    # *****************************************************************************80
    #
    # SIMPLEX_UNIT_TO_GENERAL maps the unit simplex to a general simplex.
    #
    #  Discussion:
    #
    #    Given that the unit simplex has been mapped to a general simplex
    #    with vertices T, compute the images in T, under the same linear
    #    mapping, of points whose coordinates in the unit simplex are REF.
    #
    #    The vertices of the unit simplex are listed as suggested in the
    #    following:
    #
    #      (0,0,0,...,0)
    #      (1,0,0,...,0)
    #      (0,1,0,...,0)
    #      (0,0,1,...,0)
    #      (...........)
    #      (0,0,0,...,1)
    #
    #    Thanks to Andrei ("spiritualworlds") for pointing out a mistake in the
    #    previous implementation of this routine, 02 March 2008.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 March 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of points to transform.
    #
    #    Input, real T(M,M+1), the vertices of the
    #    general simplex.
    #
    #    Input, real REF(M,N), points in the
    #    reference triangle.
    #
    #    Output, real PHY(M,N), corresponding points
    #    in the physical triangle.
    #
    import numpy as np
#
#  The image of each point is initially the image of the origin.
#
#  Insofar as the pre-image differs from the origin in a given vertex
#  direction, add that proportion of the difference between the images
#  of the origin and the vertex.
#
    phy = np.zeros([m, n])

    for i in range(0, m):

        for j in range(0, n):

            phy[i, j] = t[i, 0]

            for vertex in range(1, m + 1):

                phy[i, j] = phy[i, j] + \
                    (t[i, vertex] - t[i, 0]) * ref[vertex - 1, j]

    return phy


def simplex_unit_to_general_test01():

    # *****************************************************************************80
    #
    # SIMPLEX_UNIT_TO_GENERAL_TEST01 tests SIMPLEX_UNIT_TO_GENERAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 March 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    m = 2
    n = 10

    t = np.array([
        [1.0, 3.0, 2.0],
        [1.0, 1.0, 5.0]])

    t_unit = np.array([
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]])

    seed = 123456789

    print('')
    print('SIMPLEX_UNIT_TO_GENERAL_TEST01')
    print('  SIMPLEX_UNIT_TO_GENERAL')
    print('  maps points in the unit simplex to a general simplex.')
    print('')
    print('  Here we consider a simplex in 2D, a triangle.')
    print('')
    print('  The vertices of the general triangle are:')
    print('')
    for j in range(0, m + 1):
        for i in range(0, m):
            print('  %8.4f' % (t[i, j]), end="")
        print('')

    print('')
    print('   (  XSI     ETA )   ( X       Y  )')
    print('')

    phy_unit = simplex_unit_to_general(m, m + 1, t, t_unit)

    for j in range(0, m + 1):
        for i in range(0, m):
            print('  %8.4f' % (t_unit[i, j]), end="")
        for i in range(0, m):
            print('  %8.4f' % (phy_unit[i, j]), end="")
        print('')

    ref, seed = simplex_unit_sample(m, n, seed)

    phy = simplex_unit_to_general(m, n, t, ref)

    for j in range(0, n):
        for i in range(0, m):
            print('  %8.4f' % (ref[i, j]), end="")
        for i in range(0, m):
            print('  %8.4f' % (phy[i, j]), end="")
        print('')

    return


def simplex_unit_to_general_test02():

    # *****************************************************************************80
    #
    # SIMPLEX_UNIT_TO_GENERAL_TEST02 tests SIMPLEX_UNIT_TO_GENERAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 March 2008
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    m = 3
    n = 10

    t = np.array([
        [1.0, 3.0, 1.0, 1.0],
        [1.0, 1.0, 4.0, 1.0],
        [1.0, 1.0, 1.0, 5.0]])

    t_unit = np.array([
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]])

    seed = 123456789

    print('')
    print('SIMPLEX_UNIT_TO_GENERAL_TEST02')
    print('  SIMPLEX_UNIT_TO_GENERAL')
    print('  maps points in the unit simplex to a general simplex.')
    print('')
    print('  Here we consider a simplex in 3D, a tetrahedron.')
    print('')
    print('  The vertices of the general tetrahedron are:')
    print('')
    for j in range(0, m + 1):
        for i in range(0, m):
            print('  %8.4f' % (t[i, j]), end="")
        print('')

    print('')
    print('   (  XSI     ETA )   ( X       Y  )')
    print('')

    phy_unit = simplex_unit_to_general(m, m + 1, t, t_unit)

    for j in range(0, m + 1):
        for i in range(0, m):
            print('  %8.4f' % (t_unit[i, j]), end="")
        for i in range(0, m):
            print('  %8.4f' % (phy_unit[i, j]), end="")
        print('')

    ref, seed = simplex_unit_sample(m, n, seed)

    phy = simplex_unit_to_general(m, n, t, ref)

    for j in range(0, n):
        for i in range(0, m):
            print('  %8.4f' % (ref[i, j]), end="")
        for i in range(0, m):
            print('  %8.4f' % (phy[i, j]), end="")
        print('')

    return


def simplex_unit_volume(m):

    # *****************************************************************************80
    #
    # SIMPLEX_UNIT_VOLUME returns the volume of the unit simplex in M dimensions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 January 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Output, real VALUE, the volume.
    #
    value = 1.0
    for i in range(1, m + 1):
        value = value / float(i)

    return value


def simplex_unit_volume_test():

    # *****************************************************************************80
    #
    # SIMPLEX_UNIT_VOLUME_TEST tests SIMPLEX_UNIT_VOLUME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('SIMPLEX_UNIT_VOLUME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SIMPLEX_UNIT_VOLUME returns the volume of the unit simplex')
    print('  in M dimensions.')
    print('')
    print('   M   Volume')
    print('')

    for m in range(1, 10):
        value = simplex_unit_volume(m)
        print('  %2d  %g' % (m, value))
#
#  Terminate.
#
    print('')
    print('SIMPLEX_UNIT_VOLUME_TEST')
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


def simplex_monte_carlo_test():

    # *****************************************************************************80
    #
    # SIMPLEX_MONTE_CARLO_TEST tests the SIMPLEX_MONTE_CARLO library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('SIMPLEX_MONTE_CARLO_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the SIMPLEX_MONTE_CARLO library.')

    simplex_general_sample_test()
    simplex_unit_monomial_integral_test()
    simplex_unit_sample_test00()
    simplex_unit_sample_test01()
    simplex_unit_sample_test02()
    simplex_unit_to_general_test01()
    simplex_unit_to_general_test02()
    simplex_unit_volume_test()
#
#  Terminate.
#
    print('')
    print('SIMPLEX_MONTE_CARLO_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    simplex_monte_carlo_test()
    timestamp()
