#! /usr/bin/env python3
#


def binom(n, k):

    # *****************************************************************************80
    #
    # BINOM computes the binomial coefficient.
    #
    #  Discussion:
    #
    #    This is ACM algorithm 160 translated.
    #
    #    It calculates the number of combinations of N things taken K at a time.
    #
    #  Modified:
    #
    #    31 March 2016
    #
    #  Author:
    #
    #    Bill Buckles, Matthew Lybanon
    #
    #  Reference:
    #
    #    Bill Buckles, Matthew Lybanon,
    #    Algorithm 515: Generation of a Vector from the Lexicographical Index,
    #    ACM Transactions on Mathematical Software,
    #    Volume 3, Number 2, June 1977, pages 180-182.
    #
    #  Parameters:
    #
    #    Input, integer N, K, the parameters for the binomial
    #    coefficient.
    #
    #    Output, integer VALUE, the binomial coefficient.
    #

    #
    #  Force the input arguments to be integers.
    #
    n = int(n)
    k = int(k)

    k1 = k
    p = n - k1

    if (k1 < p):
        p = k1
        k1 = n - p

    if (p == 0):
        r = 1
    else:
        r = k1 + 1

    for i in range(2, p + 1):
        r = (r * (k1 + i)) // i

    value = int(r)

    return value


def comb(n, p, l):

    # *****************************************************************************80
    #
    # COMB selects a subset of order P from a set of order N.
    #
    #  Discussion:
    #
    #    This subroutine finds the combination set of N things taken
    #    P at a time for a given lexicographic index.
    #
    #  Modified:
    #
    #    31 March 2016
    #
    #  Author:
    #
    #    Bill Buckles, Matthew Lybanon
    #
    #  Reference:
    #
    #    Bill Buckles, Matthew Lybanon,
    #    Algorithm 515: Generation of a Vector from the Lexicographical Index,
    #    ACM Transactions on Mathematical Software,
    #    Volume 3, Number 2, June 1977, pages 180-182.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of things in the set.
    #
    #    Input, integer P, the number of things in each combination.
    #    0 < P < N.
    #
    #    Input, integer L, the lexicographic index of the
    #    desired combination.  1 <= L <= choose(N,P).
    #
    #    Output, integer C(P), the combination set.
    #
    import numpy as np

    c = np.zeros(p)
#
#  Special case: P = 1
#
    if (p == 1):
        c[0] = l
        return c
#
#  Initialize lower bound index.
#
    k = 0
#
#  Select elements in ascending order.
#
    p1 = p - 1
    c[0] = 0

    for i in range(1, p1 + 1):
        #
        #  Update lower bound as the previously selected element.
        #
        if (1 < i):
            c[i - 1] = c[i - 2]
#
#  Check validity of each entry.
#
        while (True):

            c[i - 1] = c[i - 1] + 1
            r = binom(n - c[i - 1], p - i)
            k = k + r

            if (l <= k):
                break

        k = k - r

    c[p - 1] = c[p1 - 1] + l - k

    return c


def comb_test01():

    # *****************************************************************************80
    #
    # COMB_TEST01 tests COMB by generating all 3-subsets of a 5 set.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    n = 5
    k = 3
    lmax = binom(n, k)

    print('')
    print('COMB_TEST01')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate all K-subsets of an N set.')
    print('  K = %d' % (k))
    print('  N = %d' % (n))
    print('  LMAX = %d' % (lmax))

    if (not i4_choose_check(n, k)):
        print('')
        print('COMB_TEST01 - Warning!')
        print('  The binomial coefficient cannot be')
        print('  computed in integer arithmetic for')
        print('  this choice of parameters.')
        return

    print('')

    for l in range(1, lmax + 1):
        c = comb(n, k, l)
        print('  %6d:  ' % (l)),
        for i in range(0, k):
            print('  %6d' % (c[i])),
        print('')
#
#  Terminate.
#
    print('')
    print('COMB_TEST01_TEST:')
    print('  Normal end of execution.')
    return


def comb_test02():

    # *****************************************************************************80
    #
    # COMB_TEST02 tests COMB by generating 10 random 3-subsets of a 10 set.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    n = 5
    k = 3
    lmax = binom(n, k)

    print('')
    print('COMB_TEST02')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate all K-subsets of an N set.')
    print('  K = %d' % (k))
    print('  N = %d' % (n))
    print('  LMAX = %d' % (lmax))

    if (not i4_choose_check(n, k)):
        print('')
        print('COMB_TEST02 - Warning!')
        print('  The binomial coefficient cannot be')
        print('  computed in integer arithmetic for')
        print('  this choice of parameters.')
        return

    print('')

    seed = 123456789

    for i in range(0, 10):
        l, seed = i4_uniform_ab(1, lmax, seed)
        c = comb(n, k, l)
        print('  %6d:  ' % (l)),
        for i in range(0, k):
            print('  %6d' % (c[i])),
        print('')
#
#  Terminate.
#
    print('')
    print('COMB_TEST02_TEST:')
    print('  Normal end of execution.')
    return


def comb_test03():

    # *****************************************************************************80
    #
    # COMB_TEST03 tests COMB by generating 10 random 3-subsets of a 25 set.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    n = 25
    k = 3
    lmax = binom(n, k)

    print('')
    print('COMB_TEST03')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate 10 random K-subsets of an N set.')
    print('  K = %d' % (k))
    print('  N = %d' % (n))
    print('  LMAX = %d' % (lmax))

    if (not i4_choose_check(n, k)):
        print('')
        print('COMB_TEST03 - Warning!')
        print('  The binomial coefficient cannot be')
        print('  computed in integer arithmetic for')
        print('  this choice of parameters.')
        return

    print('')

    seed = 123456789

    for i in range(0, 10):
        l, seed = i4_uniform_ab(1, lmax, seed)
        c = comb(n, k, l)
        print('  %6d:  ' % (l)),
        for i in range(0, k):
            print('  %6d' % (c[i])),
        print('')
#
#  Terminate.
#
    print('')
    print('COMB_TEST03_TEST:')
    print('  Normal end of execution.')
    return


def comb_test04():

    # *****************************************************************************80
    #
    # COMB_TEST04 tests COMB by generating 10 random 3-subsets of a 100 set.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    n = 100
    k = 3
    lmax = binom(n, k)

    print('')
    print('COMB_TEST04')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate 10 random K-subsets of an N set.')
    print('  K = %d' % (k))
    print('  N = %d' % (n))
    print('  LMAX = %d' % (lmax))

    if (not i4_choose_check(n, k)):
        print('')
        print('COMB_TEST04 - Warning!')
        print('  The binomial coefficient cannot be')
        print('  computed in integer arithmetic for')
        print('  this choice of parameters.')
        return

    print('')

    seed = 123456789

    for i in range(0, 10):
        l, seed = i4_uniform_ab(1, lmax, seed)
        c = comb(n, k, l)
        print('  %6d:  ' % (l)),
        for i in range(0, k):
            print('  %6d' % (c[i])),
        print('')
#
#  Terminate.
#
    print('')
    print('COMB_TEST04_TEST:')
    print('  Normal end of execution.')
    return


def comb_test05():

    # *****************************************************************************80
    #
    # COMB_TEST05 tests COMB by generating 10 random 10-subsets of a 100 set.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    n = 100
    k = 10
    lmax = binom(n, k)

    print('')
    print('COMB_TEST05')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate 10 random K-subsets of an N set.')
    print('  K = %d' % (k))
    print('  N = %d' % (n))
    print('  LMAX = %d' % (lmax))
    print('')
    print('  Note that this function is already')
    print('  failing because LMAX is negative.')
    print('  The combinatorial coefficient C(100,10)')
    print('  is too large to store in an integer.')
    print('')
    print('  Although the program continues to give')
    print('  results, they cannot be relied on!')

    if (not i4_choose_check(n, k)):
        print('')
        print('COMB_TEST05 - Warning!')
        print('  The binomial coefficient cannot be')
        print('  computed in integer arithmetic for')
        print('  this choice of parameters.')
        return

    print('')

    seed = 123456789

    for i in range(0, 10):
        l, seed = i4_uniform_ab(1, lmax, seed)
        c = comb(n, k, l)
        print('  %6d:  ' % (l)),
        for i in range(0, k):
            print('  %6d' % (c[i])),
        print('')
#
#  Terminate.
#
    print('')
    print('COMB_TEST05_TEST:')
    print('  Normal end of execution.')
    return


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


def i4_choose_check(n, k):

    # *****************************************************************************80
    #
    # I4_CHOOSE_CHECK reports whether the binomial coefficient can be computed.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, K, the binomial parameters.
    #
    #    Output, logical CHECK is:
    #    TRUE, if C(N,K) < maximum integer.
    #    FALSE, otherwise.
    #
    import numpy as np

    i4_huge = 2147483647

    i4_huge_log = np.log(i4_huge)

    choose_nk_log = \
        r8_gamma_log(n + 1) \
        - r8_gamma_log(k + 1) \
        - r8_gamma_log(n - k + 1)

    check = (choose_nk_log < i4_huge_log)

    return check


def i4_choose_check_test():

    # *****************************************************************************80
    #
    # I4_CHOOSE_CHECK_TEST tests I4_CHOOSE_CHECK.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    k_test = np.array([3, 999, 3, 10])
    n_test = np.array([10, 1000, 100, 100])

    print('')
    print('I4_CHOOSE_CHECK_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4_CHOOSE_CHECK checks whether C(N,K)')
    print('  can be computed with integer arithmetic')
    print('  or not.')
    print('')
    print('     N     K    CHECK?    I4_CHOOSE')
    print('')

    for i in range(0, 4):
        n = n_test[i]
        k = k_test[i]
        check = i4_choose_check(n, k)
        print('  %4d  %4d        %d' % (n, k, check)),
        if (check):
            cnk = i4_choose(n, k)
            print('        %d' % (cnk))
        else:
            print('   Not computable')
#
#  Terminate.
#
    print('')
    print('I4_CHOOSE_CHECK_TEST:')
    print('  Normal end of execution.')
    return


def i4_choose(n, k):

    # *****************************************************************************80
    #
    # I4_CHOOSE computes the binomial coefficient C(N,K) as an I4.
    #
    #  Discussion:
    #
    #    The value is calculated in such a way as to avoid overflow and
    #    roundoff.  The calculation is done in integer arithmetic.
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
    #    30 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    ML Wolfson, HV Wright,
    #    Algorithm 160:
    #    Combinatorial of M Things Taken N at a Time,
    #    Communications of the ACM,
    #    Volume 6, Number 4, April 1963, page 161.
    #
    #  Parameters:
    #
    #    Input, integer N, K, are the values of N and K.
    #
    #    Output, integer VALUE, the number of combinations of N
    #    things taken K at a time.
    #
    mn = min(k, n - k)
    mx = max(k, n - k)

    if (mn < 0):

        value = 0

    elif (mn == 0):

        value = 1

    else:

        value = mx + 1

        for i in range(2, mn + 1):
            value = (value * (mx + i)) / i

    return value


def i4_choose_test():

    # *****************************************************************************80
    #
    # I4_CHOOSE_TEST tests I4_CHOOSE.
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

    print('')
    print('I4_CHOOSE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4_CHOOSE evaluates C(N,K).')
    print('')
    print('       N       K     CNK')

    for n in range(0, 5):
        print('')
        for k in range(0, n + 1):
            cnk = i4_choose(n, k)

            print('  %6d  %6d  %6d' % (n, k, cnk))
#
#  Terminate.
#
    print('')
    print('I4_CHOOSE_TEST:')
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


def toms515_test():

    # *****************************************************************************80
    #
    # TOMS515_TEST tests the TOMS515 library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('TOMS515_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the TOMS515 library.')

    comb_test01()
    comb_test02()
    comb_test03()
    comb_test04()
    comb_test05()

    i4_choose_test()
    i4_choose_check_test()
    i4_uniform_ab_test()

    r8_gamma_log_test()
#
#  Terminate.
#
    print('')
    print('TOMS515_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    toms515_test()
    timestamp()
