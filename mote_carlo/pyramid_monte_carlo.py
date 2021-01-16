#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.append(os.path.join('../'))
from base import plot2d, plot3d
obj = plot3d()

def gamma_log_values(n_data):

    # *****************************************************************************80
    #
    # GAMMA_LOG_VALUES returns some values of the Log Gamma function.
    #
    #  Discussion:
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      Log[Gamma[x]]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Milton Abramowitz and Irene Stegun,
    #    Handbook of Mathematical Functions,
    #    US Department of Commerce, 1964.
    #
    #    Stephen Wolfram,
    #    The Mathematica Book,
    #    Fourth Edition,
    #    Wolfram Media / Cambridge University Press, 1999.
    #
    #  Parameters:
    #
    #    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
    #    first call.  On each call, the routine increments N_DATA by 1, and
    #    returns the corresponding data; when there is no more data, the
    #    output value of N_DATA will be 0 again.
    #
    #    Output, real X, the argument of the function.
    #
    #    Output, real FX, the value of the function.
    #
    import numpy as np

    n_max = 20

    fx_vec = np.array((
        0.1524063822430784E+01,
        0.7966778177017837E+00,
        0.3982338580692348E+00,
        0.1520596783998375E+00,
        0.0000000000000000E+00,
        -0.4987244125983972E-01,
        -0.8537409000331584E-01,
        -0.1081748095078604E+00,
        -0.1196129141723712E+00,
        -0.1207822376352452E+00,
        -0.1125917656967557E+00,
        -0.9580769740706586E-01,
        -0.7108387291437216E-01,
        -0.3898427592308333E-01,
        0.00000000000000000E+00,
        0.69314718055994530E+00,
        0.17917594692280550E+01,
        0.12801827480081469E+02,
        0.39339884187199494E+02,
        0.71257038967168009E+02))

    x_vec = np.array((
        0.20E+00,
        0.40E+00,
        0.60E+00,
        0.80E+00,
        1.00E+00,
        1.10E+00,
        1.20E+00,
        1.30E+00,
        1.40E+00,
        1.50E+00,
        1.60E+00,
        1.70E+00,
        1.80E+00,
        1.90E+00,
        2.00E+00,
        3.00E+00,
        4.00E+00,
        10.00E+00,
        20.00E+00,
        30.00E+00))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        x = 0.0
        fx = 0.0
    else:
        x = x_vec[n_data]
        fx = fx_vec[n_data]
        n_data = n_data + 1

    return n_data, x, fx


def gamma_log_values_test():

    # *****************************************************************************80
    #
    # GAMMA_LOG_VALUE_TEST demonstrates the use of GAMMA_LOG_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 February 2009
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('GAMMA_LOG_VALUES:')
    print('  GAMMA_LOG_VALUES stores values of')
    print('  the logarithm of the Gamma function.')
    print('')
    print('      X            GAMMA_LOG(X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx = gamma_log_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %24.16f' % (x, fx))
#
#  Terminate.
#
    print('')
    print('GAMMA_LOG_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def i4_uniform_ab(a, b, seed):

    # *****************************************************************************80
    #
    # I4_UNIFORM_AB returns a scaled pseudorandom I4.
    #
    #  Discussion:
    #
    #    The pseudorandom number will be scaled to be uniformly distributed
    #    between A and B.
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
    #    Input, integer A, B, the minimum and maximum acceptable values.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer C, the randomly chosen integer.
    #
    #    Output, integer SEED, the updated seed.
    #
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    seed = (seed % i4_huge)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('I4_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('I4_UNIFORM_AB - Fatal error!')

    k = (seed // 127773)

    seed = 16807 * (seed - k * 127773) - k * 2836

    if (seed < 0):
        seed = seed + i4_huge

    r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
    a = round(a)
    b = round(b)

    r = (1.0 - r) * (min(a, b) - 0.5) \
        + r * (max(a, b) + 0.5)
#
#  Use rounding to convert R to an integer between A and B.
#
    value = round(r)

    value = max(value, min(a, b))
    value = min(value, max(a, b))
    value = int(value)

    return value, seed


def i4_uniform_ab_test():

    # *****************************************************************************80
    #
    # I4_UNIFORM_AB_TEST tests I4_UNIFORM_AB.
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

    a = -100
    b = 200
    seed = 123456789

    print('')
    print('I4_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4_UNIFORM_AB computes pseudorandom values')
    print('  in an interval [A,B].')
    print('')
    print('  The lower endpoint A = %d' % (a))
    print('  The upper endpoint B = %d' % (b))
    print('  The initial seed is %d' % (seed))
    print('')

    for i in range(1, 21):
        j, seed = i4_uniform_ab(a, b, seed)
        print('  %8d  %8d' % (i, j))
#
#  Terminate.
#
    print('')
    print('I4_UNIFORM_AB_TEST:')
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
    #    08 September 2018
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
        print(title, end='')

    if (0 < n):
        for i in range(0, n):
            print(' %d' % (a[i]), end='')
            if ((i + 1) % 20 == 0 or i == n - 1):
                print('')
    else:
        print('(empty vector)')

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
    #    09 September 2018
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

    print('')
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


def pyramid01_integral(expon):

    # *****************************************************************************80
    #
    # PYRAMID01_INTEGRAL: monomial integral in a unit pyramid.
    #
    #  Discussion:
    #
    #    This routine returns the integral of
    #
    #      product ( 1 <= I <= 3 ) X(I)^EXPON(I)
    #
    #    over the unit pyramid.
    #
    #    The unit pyramid is defined as:
    #
    #    - ( 1 - Z ) <= X <= 1 - Z
    #    - ( 1 - Z ) <= Y <= 1 - Z
    #              0 <= Z <= 1.
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
    #    Arthur Stroud,
    #    Approximate Calculation of Multiple Integrals,
    #    Prentice Hall, 1971,
    #    ISBN: 0130438936,
    #    LC: QA311.S85.
    #
    #  Parameters:
    #
    #    Input, integer EXPON(3), the exponents.
    #
    #    Output, real VALUE, the integral of the monomial.
    #
    if (((expon[0] % 2) == 0) and ((expon[1] % 2) == 0)):

        i_hi = 2 + expon[0] + expon[1]

        value = 0.0
        for i in range(0, i_hi + 1):
            value = value + r8_mop(i) * r8_choose(i_hi,
                                                  i) / float(i + expon[2] + 1)

        value = value * 2.0 / float(expon[0] + 1) * 2.0 / float(expon[1] + 1)

    else:

        value = 0.0

    return value


def pyramid01_integral_test():

    # *****************************************************************************80
    #
    # PYRAMID01_INTEGRAL_TEST tests PYRAMID01_INTEGRAL.
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
    import numpy as np
    import platform

    m = 3
    n = 500000
    e_max = 6

    print('')
    print('PYRAMID01_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PYRAMID01_INTEGRAL returns the integral of a monomial')
    print('  over the unit pyramid in 3D.')
    print('  Compare to a Monte Carlo estimate.')
#
#  Get sample points.
#
    seed = 123456789
    x, seed = pyramid01_sample(n, seed)

    print('')
    print('  Number of sample points used is %d' % (n))
    print('')
    print('   E1  E2  E3     MC-Estimate      Exact           Error')
    print('')
#
#  Check all monomials, with only even dependence on X or Y,
#  up to total degree E_MAX.
#
    e = np.zeros(3, dtype=np.int32)

    for e3 in range(0, e_max + 1):
        e[2] = e3
        for e2 in range(0, e_max - e3 + 1, 2):
            e[1] = e2
            for e1 in range(0, e_max - e3 - e2 + 1, 2):
                e[0] = e1

                value = monomial_value(m, n, e, x)

                q = pyramid01_volume() * np.sum(value) / float(n)
                exact = pyramid01_integral(e)
                error = abs(q - exact)

                print('  %2d  %2d  %2d  %14.6g  %14.6g  %10.2g'
                      % (e[0], e[1], e[2], q, exact, error))
#
#  Terminate.
#
    print('')
    print('PYRAMID01_INTEGRAL_TEST:')
    print('  Normal end of execution.')
    return


def pyramid01_monte_carlo_test():

    # *****************************************************************************80
    #
    # PYRAMID01_MONTE_CARLO_TEST estimates some integrals.
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
    import numpy as np
    import platform

    m = 3
    test_num = 10

    e_test = np.array([
        [0, 0, 2, 0, 0, 2, 0, 0, 2, 2],
        [0, 0, 0, 2, 0, 0, 2, 0, 2, 0],
        [0, 1, 0, 0, 2, 1, 1, 3, 0, 2]])

    print('')
    print('PYRAMID01_MONTE_CARLO_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use PYRAMID01_SAMPLE to estimate integrals')
    print('  over the interior of the unit pyramid in 3D.')

    seed = 123456789

    result = np.zeros(test_num)
    n = 1
    while (n <= 65536):
        x, seed = pyramid01_sample(n, seed)
        print(' %8d' % (n), end='')
        for e in e_test:
            value = monomial_value(m, n, e, x)
            #result[j] = pyramid01_volume() * np.sum(value) / float(n)

        #for i in range(0, 10):
        #    print('  %14.6g' % (result[i])),
        #print('')

        obj.axs.scatter(*x, s=0.5)
        obj.axs.set_title("n={:d}".format(n))
        obj.SavePng_Serial()
        plt.close()
        obj.new_fig()

        n = 2 * n

    #print('')
    #
    #for j in range(0, 10):
    #
    #    for i in range(0, m):
    #        e[i] = e_test[i, j]
    #
    #    result[j] = pyramid01_integral(e)
    #
    #print('     Exact'),
    #for i in range(0, 10):
    #    print('  %14.6g' % (result[i])),
    #print('')
    print('')
    print('PYRAMID01_MONTE_CARLO_TEST')
    print('  Normal end of execution.')
    return


def pyramid01_sample(n, seed):

    # *****************************************************************************80
    #
    # PYRAMID01_SAMPLE: sample the unit pyramid.
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
    #  Parameters:
    #
    #    Input, integer N, the number of samples desired.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real X(3,N), the sample values.
    #
    one_third = 1.0 / 3.0

    x, seed = r8mat_uniform_01(3, n, seed)

    for j in range(0, n):
        x[2, j] = 1.0 - x[2, j] ** one_third
        x[1, j] = (1.0 - x[2, j]) * (2.0 * x[1, j] - 1.0)
        x[0, j] = (1.0 - x[2, j]) * (2.0 * x[0, j] - 1.0)

    return x, seed


def pyramid01_sample_test():

    # *****************************************************************************80
    #
    # PYRAMID01_SAMPLE_TEST tests PYRAMID01_SAMPLE.
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
    import platform

    print('')
    print('PYRAMID01_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PYRAMID01_SAMPLE samples points from the unit pyramid.')

    n = 20
    seed = 123456789
    x, seed = pyramid01_sample(n, seed)

    m = 3
    r8mat_transpose_print(m, n, x, '  Unit pyramid points')
#
#  Terminate.
#
    print('')
    print('PYRAMID01_SAMPLE_TEST')
    print('  Normal end of execution.')
    return


def pyramid01_volume():

    # *****************************************************************************80
    #
    # PYRAMID01_VOLUME returns the volume of a unit pyramid.
    #
    #  Discussion:
    #
    #    A pyramid with square base can be regarded as the upper half of a
    #    3D octahedron.
    #
    #    The integration region:
    #
    #      - ( 1 - Z ) <= X <= 1 - Z
    #      - ( 1 - Z ) <= Y <= 1 - Z
    #                0 <= Z <= 1.
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
    #  Parameters:
    #
    #    Output, real VALUE, the volume of the pyramid.
    #
    value = 4.0 / 3.0

    return value


def pyramid01_volume_test():

    # *****************************************************************************80
    #
    # PYRAMID01_VOLUME tests PYRAMID01_VOLUME.
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
    import platform

    print('')
    print('PYRAMID01_VOLUME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PYRAMID01_VOLUME returns the volume of the unit pyramid.')

    value = pyramid01_volume()

    print('')
    print('  PYRAMID01_VOLUME() = %g' % (value))
#
#  Terminate.
#
    print('')
    print('PYRAMID01_VOLUME_TEST')
    print('  Normal end of execution.')
    return


def pyramid_monte_carlo_test():

    # *****************************************************************************80
    #
    # PYRAMID_MONTE_CARLO_TEST tests the PYRAMID_MONTE_CARLO library.
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
    import platform

    print('')
    print('PYRAMID_MONTE_CARLO_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the PYRAMID_MONTE_CARLO library.')

    pyramid01_integral_test()
    pyramid01_monte_carlo_test()
    pyramid01_sample_test()
    pyramid01_volume_test()

    print('')
    print('PYRAMID_MONTE_CARLO_TEST:')
    print('  Normal end of execution.')
    return


def r8_choose(n, k):

    # *****************************************************************************80
    #
    # R8_CHOOSE computes the binomial coefficient C(N,K) as an R8.
    #
    #  Discussion:
    #
    #    The value is calculated in such a way as to avoid overflow and
    #    roundoff.  The calculation is done in R8 arithmetic.
    #
    #    The formula used is:
    #
    #      C(N,K) = N! / ( K! * (N-K)! )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, K, are the values of N and K.
    #
    #    Output, real VALUE, the number of combinations of N
    #    things taken K at a time.
    #
    import numpy as np

    if (n < 0):

        value = 0.0

    elif (k == 0):

        value = 1.0

    elif (k == 1):

        value = float(n)

    elif (1 < k and k < n - 1):

        facn = r8_gamma_log(float(n + 1))
        fack = r8_gamma_log(float(k + 1))
        facnmk = r8_gamma_log(float(n - k + 1))

        value = round(np.exp(facn - fack - facnmk))

    elif (k == n - 1):

        value = float(n)

    elif (k == n):

        value = 1.0

    else:

        value = 0.0

    return value


def r8_choose_test():

    # *****************************************************************************80
    #
    # R8_CHOOSE_TEST tests R8_CHOOSE.
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
    print('R8_CHOOSE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_CHOOSE evaluates C(N,K).')
    print('')
    print('         N         K       CNK')

    for n in range(0, 6):
        print('')
        for k in range(0, n + 1):
            cnk = r8_choose(n, k)
            print('  %8d  %8d  %14.6g' % (n, k, cnk))
#
#  Terminate.
#
    print('')
    print('R8_CHOOSE_TEST')
    print('  Normal end of execution.')
    return


def r8_gamma_log(x):

    # *****************************************************************************80
    #
    # R8_GAMMA_LOG evaluates the logarithm of the gamma function.
    #
    #  Discussion:
    #
    #    This routine calculates the LOG(GAMMA) function for a positive real
    #    argument X.  Computation is based on an algorithm outlined in
    #    references 1 and 2.  The program uses rational functions that
    #    theoretically approximate LOG(GAMMA) to at least 18 significant
    #    decimal digits.  The approximation for X > 12 is from reference
    #    3, while approximations for X < 12.0 are similar to those in
    #    reference 1, but are unpublished.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2014
    #
    #  Author:
    #
    #    Original FORTRAN77 version by William Cody, Laura Stoltz.
    #    PYTHON version by John Burkardt.
    #
    #  Reference:
    #
    #    William Cody, Kenneth Hillstrom,
    #    Chebyshev Approximations for the Natural Logarithm of the
    #    Gamma Function,
    #    Mathematics of Computation,
    #    Volume 21, Number 98, April 1967, pages 198-203.
    #
    #    Kenneth Hillstrom,
    #    ANL/AMD Program ANLC366S, DGAMMA/DLGAMA,
    #    May 1969.
    #
    #    John Hart, Ward Cheney, Charles Lawson, Hans Maehly,
    #    Charles Mesztenyi, John Rice, Henry Thatcher,
    #    Christoph Witzgall,
    #    Computer Approximations,
    #    Wiley, 1968,
    #    LC: QA297.C64.
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the function.
    #
    #    Output, real R8_GAMMA_LOG, the value of the function.
    #
    import numpy as np

    c = np.array([
        -1.910444077728E-03,
        8.4171387781295E-04,
        -5.952379913043012E-04,
        7.93650793500350248E-04,
        -2.777777777777681622553E-03,
        8.333333333333333331554247E-02,
        5.7083835261E-03])
    d1 = -5.772156649015328605195174E-01
    d2 = 4.227843350984671393993777E-01
    d4 = 1.791759469228055000094023E+00
    frtbig = 2.25E+76
    p1 = np.array([
        4.945235359296727046734888E+00,
        2.018112620856775083915565E+02,
        2.290838373831346393026739E+03,
        1.131967205903380828685045E+04,
        2.855724635671635335736389E+04,
        3.848496228443793359990269E+04,
        2.637748787624195437963534E+04,
        7.225813979700288197698961E+03])
    p2 = np.array([
        4.974607845568932035012064E+00,
        5.424138599891070494101986E+02,
        1.550693864978364947665077E+04,
        1.847932904445632425417223E+05,
        1.088204769468828767498470E+06,
        3.338152967987029735917223E+06,
        5.106661678927352456275255E+06,
        3.074109054850539556250927E+06])
    p4 = np.array([
        1.474502166059939948905062E+04,
        2.426813369486704502836312E+06,
        1.214755574045093227939592E+08,
        2.663432449630976949898078E+09,
        2.940378956634553899906876E+10,
        1.702665737765398868392998E+11,
        4.926125793377430887588120E+11,
        5.606251856223951465078242E+11])
    q1 = np.array([
        6.748212550303777196073036E+01,
        1.113332393857199323513008E+03,
        7.738757056935398733233834E+03,
        2.763987074403340708898585E+04,
        5.499310206226157329794414E+04,
        6.161122180066002127833352E+04,
        3.635127591501940507276287E+04,
        8.785536302431013170870835E+03])
    q2 = np.array([
        1.830328399370592604055942E+02,
        7.765049321445005871323047E+03,
        1.331903827966074194402448E+05,
        1.136705821321969608938755E+06,
        5.267964117437946917577538E+06,
        1.346701454311101692290052E+07,
        1.782736530353274213975932E+07,
        9.533095591844353613395747E+06])
    q4 = np.array([
        2.690530175870899333379843E+03,
        6.393885654300092398984238E+05,
        4.135599930241388052042842E+07,
        1.120872109616147941376570E+09,
        1.488613728678813811542398E+10,
        1.016803586272438228077304E+11,
        3.417476345507377132798597E+11,
        4.463158187419713286462081E+11])
    r8_epsilon = 2.220446049250313E-016
    sqrtpi = 0.9189385332046727417803297
    xbig = 2.55E+305
    xinf = 1.79E+308

    y = x

    if (0.0 < y and y <= xbig):

        if (y <= r8_epsilon):

            res = - np.log(y)
#
#  EPS < X <= 1.5.
#
        elif (y <= 1.5):

            if (y < 0.6796875):
                corr = - np.log(y)
                xm1 = y
            else:
                corr = 0.0
                xm1 = (y - 0.5) - 0.5

            if (y <= 0.5 or 0.6796875 <= y):

                xden = 1.0
                xnum = 0.0
                for i in range(0, 8):
                    xnum = xnum * xm1 + p1[i]
                    xden = xden * xm1 + q1[i]

                res = corr + (xm1 * (d1 + xm1 * (xnum / xden)))

            else:

                xm2 = (y - 0.5) - 0.5
                xden = 1.0
                xnum = 0.0
                for i in range(0, 8):
                    xnum = xnum * xm2 + p2[i]
                    xden = xden * xm2 + q2[i]

                res = corr + xm2 * (d2 + xm2 * (xnum / xden))
#
#  1.5 < X <= 4.0.
#
        elif (y <= 4.0):

            xm2 = y - 2.0
            xden = 1.0
            xnum = 0.0
            for i in range(0, 8):
                xnum = xnum * xm2 + p2[i]
                xden = xden * xm2 + q2[i]

            res = xm2 * (d2 + xm2 * (xnum / xden))
#
#  4.0 < X <= 12.0.
#
        elif (y <= 12.0):

            xm4 = y - 4.0
            xden = -1.0
            xnum = 0.0
            for i in range(0, 8):
                xnum = xnum * xm4 + p4[i]
                xden = xden * xm4 + q4[i]

            res = d4 + xm4 * (xnum / xden)
#
#  Evaluate for 12 <= argument.
#
        else:

            res = 0.0

            if (y <= frtbig):

                res = c[6]
                ysq = y * y

                for i in range(0, 6):
                    res = res / ysq + c[i]

            res = res / y
            corr = np.log(y)
            res = res + sqrtpi - 0.5 * corr
            res = res + y * (corr - 1.0)
#
#  Return for bad arguments.
#
    else:

        res = xinf

    return res


def r8_gamma_log_test():

    # *****************************************************************************80
    #
    # R8_GAMMA_LOG_TEST tests R8_GAMMA_LOG.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8_GAMMA_LOG_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_GAMMA_LOG evaluates the logarithm of the Gamma function.')
    print('')
    print('      X            GAMMA_LOG(X)    R8_GAMMA_LOG(X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx1 = gamma_log_values(n_data)

        if (n_data == 0):
            break

        fx2 = r8_gamma_log(x)

        print('  %12g  %24.16g  %24.16g' % (x, fx1, fx2))
#
#  Terminate.
#
    print('')
    print('R8_GAMMA_LOG_TEST')
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


def r8mat_uniform_01(m, n, seed):

    # *****************************************************************************80
    #
    # R8MAT_UNIFORM_01 returns a unit pseudorandom R8MAT.
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
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.
    #
    #    Output, real R(M,N), an array of random values between 0 and 1.
    #
    #    Output, integer SEED, the updated seed.  This would
    #    normally be used as the input seed on the next call.
    #
    import numpy as np
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8MAT_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8MAT_UNIFORM_01 - Fatal error!')

    r = np.zeros([m, n])

    for j in range(0, n):
        for i in range(0, m):

            k = (seed // 127773)

            seed = 16807 * (seed - k * 127773) - k * 2836

            seed = (seed % i4_huge)

            if (seed < 0):
                seed = seed + i4_huge

            r[i, j] = seed * 4.656612875E-10

    return r, seed


def r8mat_uniform_01_test():

    # *****************************************************************************80
    #
    # R8MAT_UNIFORM_01_TEST tests R8MAT_UNIFORM_01.
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
    seed = 123456789

    print('')
    print('R8MAT_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_UNIFORM_01 computes a random R8MAT.')
    print('')
    print('  0 <= X <= 1')
    print('  Initial seed is %d' % (seed))

    v, seed = r8mat_uniform_01(m, n, seed)

    r8mat_print(m, n, v, '  Random R8MAT:')
#
#  Terminate.
#
    print('')
    print('R8MAT_UNIFORM_01_TEST:')
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


def r8_mop(i):

    # *****************************************************************************80
    #
    # R8_MOP returns the I-th power of -1 as an R8 value.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 June 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer I, the power of -1.
    #
    #    Output, real R8_MOP, the I-th power of -1.
    #
    if ((i % 2) == 0):
        value = + 1.0
    else:
        value = - 1.0

    return value


def r8_mop_test():

    # *****************************************************************************80
    #
    # R8_MOP_TEST tests R8_MOP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8_MOP_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_MOP evaluates (-1.0)^I4 as an R8.')
    print('')
    print('    I4  R8_MOP(I4)')
    print('')

    i4_min = -100
    i4_max = +100
    seed = 123456789

    for test in range(0, 10):
        i4, seed = i4_uniform_ab(i4_min, i4_max, seed)
        r8 = r8_mop(i4)
        print('  %4d  %4.1f' % (i4, r8))
#
#  Terminate.
#
    print('')
    print('R8_MOP_TEST')
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


if (__name__ == '__main__'):
    timestamp()
    pyramid_monte_carlo_test()
    timestamp()
