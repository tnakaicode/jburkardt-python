#! /usr/bin/env python3
#


def line01_length():

    # *****************************************************************************80
    #
    # LINE01_LENGTH: length of the unit line in 1D.
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
    #    Output, real VALUE, the length.
    #
    value = 1.0

    return value


def line01_length_test():

    # *****************************************************************************80
    #
    # LINE01_LENGTH_TEST tests LINE01_LENGTH.
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
    print('LINE01_LENGTH_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  LINE01_LENGTH returns the length of the unit line.')

    value = line01_length()

    print('')
    print('  LINE01_LENGTH() = %g' % (value))
#
#  Terminate.
#
    print('')
    print('LINE01_LENGTH_TEST')
    print('  Normal end of execution.')
    return


def line01_monomial_integral(e):

    # *****************************************************************************80
    #
    # LINE01_MONOMIAL_INTEGRAL: monomial integral over the unit line in 1D.
    #
    #  Discussion:
    #
    #    The integration region is
    #
    #      0 <= X <= 1.
    #
    #    The monomial is F(X) = X^E.
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
    #    Philip Davis, Philip Rabinowitz,
    #    Methods of Numerical Integration,
    #    Second Edition,
    #    Academic Press, 1984, page 263.
    #
    #  Parameters:
    #
    #    Input, integer E, the exponent.
    #    E must not equal -1.
    #
    #    Output, real INTEGRAL, the integral.
    #
    from sys import exit

    if (e == -1):
        print('')
        print('LINE01_MONOMIAL_INTEGRAL - Fatal error!')
        print('  Exponent E = -1 is not allowed!')
        exit('LINE01_MONOMIAL_INTEGRAL - Fatal error!')

    integral = 1.0 / float(e + 1)

    return integral


def line01_monomial_integral_test():

    # *****************************************************************************80
    #
    # LINE01_MONOMIAL_INTEGRAL_TEST tests LINE01_MONOMIAL_INTEGRAL.
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

    m = 1
    n = 4192
    test_num = 11

    print('')
    print('LINE01_MONOMIAL_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  LINE01_MONOMIAL_INTEGRAL computes integrals of monomials')
    print('  along the length of the unit line in 1D.')
    print('  Compare with a Monte Carlo estimate.')
#
#  Get sample points.
#
    seed = 123456789
    x, seed = line01_sample_random(n, seed)

    print('')
    print('  Number of sample points used is %d' % (n))
    print('')
    print('   E     MC-Estimate      Exact           Error')
    print('')

    import numpy as np
    from plot import plot_1d

    dat = []
    for test in range(0, test_num):

        e = test
        value = monomial_value_1d(n, e, x)
        result = line01_length() * np.sum(value) / float(n)
        exact = line01_monomial_integral(e)
        error = abs(result - exact)

        print('  %2d  %14.6g  %14.6g  %10.2g' % (e, result, exact, error))
        dat.append(np.array([e, result, exact, error]))
    dat = np.array(dat)
    plot_1d(dat, "./line_monte_carlo.png")
    print('')
    print('LINE01_MONOMIAL_INTEGRAL_TEST:')
    print('  Normal end of execution.')
    return


def line01_sample_ergodic(n, shift):

    # *****************************************************************************80
    #
    # LINE01_SAMPLE_ERGODIC samples the unit line in 1D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 June 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, real SHIFT, a value between 0 and 1.
    #
    #    Output, real X(N), the points.
    #
    import numpy as np

    golden = (1.0 + np.sqrt(5.0)) / 2.0

    x = np.zeros(n, dtype=np.float64)

    shift = np.mod(shift, 1.0)

    for j in range(0, n):
        x[j] = shift
        shift = np.mod(shift + golden, 1.0)

    return x, shift


def line01_sample_ergodic_test():

    # *****************************************************************************80
    #
    # LINE01_SAMPLE_ERGODIC_TEST estimates integrals in 1D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 June 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('LINE01_SAMPLE_ERGODIC_TEST')
    print('  LINE01_SAMPLE_ERGODIC ergodically samples the unit line segment.')
    print('  Use it to estimate integrals.')
    print('')
    print('         N', end='')
    print('               1', end='')
    print('               X', end='')
    print('             X^2', end='')
    print('             X^3', end='')
    print('             X^4', end='')
    print('             X^5', end='')
    print('             X^6')
    print('')

    import numpy as np

    n = 1
    dat = []
    while (n <= 65536):

        shift = 0.0
        x, shift = line01_sample_ergodic(n, shift)
        print('  %8d' % (n), end='')
        for j in range(0, 7):
            e = j
            value = monomial_value_1d(n, e, x)
            result = line01_length() * np.sum(value[0:n]) / float(n)
            print('  %14.6g' % (result), end='')
        print('')
        dat.append(np.array([n, result]))
        n = 2 * n
    dat = np.array(dat)

    from plot import plot_1d
    plot_1d(dat, "./line_monte_carlo_ergotic.png")

    print('')
    print('     Exact', end='')

    for j in range(0, 7):
        e = j
        result = line01_monomial_integral(e)
        print('  %14.6g' % (result), end='')

    print('')
    print('LINE01_SAMPLE_ERGODIC_TEST:')
    print('  Normal end of execution.')
    return


def line01_sample_random(n, seed):

    # *****************************************************************************80
    #
    # LINE01_SAMPLE_RANDOM samples the unit line in 1D.
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
    #    Input, integer N, the number of points.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real X(N), the points.
    #
    x, seed = r8vec_uniform_01(n, seed)

    return x, seed


def line01_sample_random_test():

    # *****************************************************************************80
    #
    # LINE01_SAMPLE_RANDOM_TEST estimates integrals in 1D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 June 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    print('')
    print('LINE01_SAMPLE_RANDOM_TEST')
    print('  LINE01_SAMPLE_RANDOM randomly samples the unit line segment.')
    print('  Use it to estimate integrals.')
    print('')
    print('         N', end='')
    print('               1', end='')
    print('               X', end='')
    print('             X^2', end='')
    print('             X^3', end='')
    print('             X^4', end='')
    print('             X^5', end='')
    print('             X^6')
    print('')

    import numpy as np

    n = 1
    dat = []
    while (n <= 65536):

        seed = 123456789
        x, seed = line01_sample_random(n, seed)
        print('  %8d' % (n), end='')
        for j in range(0, 7):
            e = j
            value = monomial_value_1d(n, e, x)
            result = line01_length() * np.sum(value[0:n]) / float(n)
            print('  %14.6g' % (result), end='')
        print('')
        dat.append(np.array([n, result]))
        n = 2 * n
    dat = np.array(dat)

    from plot import plot_1d
    plot_1d(dat, "./line_monte_carlo_random.png")

    print('')
    print('     Exact', end='')
    for j in range(0, 7):
        e = j
        result = line01_monomial_integral(e)
        print('  %14.6g' % (result), end='')
    print('')
    print('LINE01_SAMPLE_RANDOM_TEST:')
    print('  Normal end of execution.')
    return


def monomial_value_1d(n, e, x):

    # *****************************************************************************80
    #
    # MONOMIAL_VALUE_1D evaluates a monomial in 1D.
    #
    #  Discussion:
    #
    #    This routine evaluates a monomial of the form
    #
    #      x^e
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
    #    Input, integer N, the number of points.
    #
    #    Input, integer E, the exponent.
    #
    #    Input, real X(N), the point coordinates.
    #
    #    Output, real VALUE(N), the value of the monomial.
    #
    import numpy as np

    value = np.zeros(n)

    for i in range(0, n):
        value[i] = x[i] ** e

    return value


def monomial_value_1d_test():

    # *****************************************************************************80
    #
    # MONOMIAL_VALUE_1D_TEST tests MONOMIAL_VALUE_1D.
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
    print('MONOMIAL_VALUE_1D_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MONOMIAL_VALUE_1D evaluates a monomial of a 1D argument.')
    print('')
    print('      X^(-1)       X^(0)       X^(1)       X^(2)       X^(5)')
    print('')

    n = 5
    x_min = -2.0
    x_max = +10.0
    seed = 123456789

    x, seed = r8vec_uniform_ab(n, x_min, x_max, seed)

    e = -1
    vm1 = monomial_value_1d(n, e, x)
    e = 0
    v0 = monomial_value_1d(n, e, x)
    e = 1
    v1 = monomial_value_1d(n, e, x)
    e = 2
    v2 = monomial_value_1d(n, e, x)
    e = 5
    v5 = monomial_value_1d(n, e, x)

    for j in range(0, n):
        print('  %10g  %10g  %10g  %10g  %10g'
              % (vm1[j], v0[j], v1[j], v2[j], v5[j]))
#
#  Terminate.
#
    print('')
    print('MONOMIAL_VALUE_1D_TEST')
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

    return


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
    import numpy
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

    x = numpy.zeros(n)

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


def r8vec_uniform_ab(n, a, b, seed):

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_AB returns a scaled pseudorandom R8VEC.
    #
    #  Discussion:
    #
    #    Each dimension ranges from A to B.
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
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Springer Verlag, pages 201-202, 1983.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, pages 362-376, 1986.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, pages 136-143, 1969.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A, B, the range of the pseudorandom values.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(N), the vector of pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    import numpy
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8VEC_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8VEC_UNIFORM_AB - Fatal error!')

    x = numpy.zeros(n)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        if (seed < 0):
            seed = seed + i4_huge

        x[i] = a + (b - a) * seed * 4.656612875E-10

    return x, seed


def r8vec_uniform_ab_test():

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_AB_TEST tests R8VEC_UNIFORM_AB.
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

    n = 10
    a = -1.0
    b = +5.0
    seed = 123456789

    print('')
    print('R8VEC_UNIFORM_AB_TEST')
    print('  R8VEC_UNIFORM_AB computes a random R8VEC.')
    print('')
    print('  %g <= X <= %g' % (a, b))
    print('  Initial seed is %d' % (seed))

    v, seed = r8vec_uniform_ab(n, a, b, seed)

    r8vec_print(n, v, '  Random R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_UNIFORM_AB_TEST:')
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


def line_monte_carlo_test():

    # *****************************************************************************80
    #
    # LINE_MONTE_CARLO_TEST tests the LINE_MONTE_CARLO library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 June 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('LINE_MONTE_CARLO_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the LINE_MONTE_CARLO library.')

    line01_monomial_integral_test()
    line01_sample_ergodic_test()
    line01_sample_random_test()

    print('')
    print('LINE_MONTE_CARLO_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    line_monte_carlo_test()
    timestamp()
