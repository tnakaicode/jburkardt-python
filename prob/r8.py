#! /usr/bin/env python
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

    r1, seed = r8_uniform_01(seed)
    r2, seed = r8_uniform_01(seed)

    x = np.sqrt(- 2.0 * np.log(r1)) * np.cos(2.0 * np.pi * r2)

    return x, seed


def r8_zeta(p):

    # *****************************************************************************80
    #
    # R8_ZETA estimates the Riemann Zeta function.
    #
    #  Discussion:
    #
    #    For 1 < P, the Riemann Zeta function is defined as:
    #
    #      ZETA ( P ) = Sum ( 1 <= N < oo ) 1 / N ^ P
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Daniel Zwillinger, editor,
    #    CRC Standard Mathematical Tables and Formulae,
    #    30th Edition,
    #    CRC Press, 1996.
    #
    #  Parameters:
    #
    #    Input, real P, the power to which the integers are raised.
    #    P must be greater than 1.  For integral P up to 20, a
    #    precomputed value of ZETA is returned otherwise the infinite
    #    sum is approximated.
    #
    #    Output, real VALUE, an approximation to the Riemann
    #    Zeta function.
    #

    if (p <= 1.0):
        value = r8_huge()
    elif (p == 2.0):
        value = np.pi ** 2 / 6.0
    elif (p == 3.0):
        value = 1.2020569032
    elif (p == 4.0):
        value = np.pi ** 4 / 90.0
    elif (p == 5.0):
        value = 1.0369277551
    elif (p == 6.0):
        value = np.pi ** 6 / 945.0
    elif (p == 7.0):
        value = 1.0083492774
    elif (p == 8.0):
        value = np.pi ** 8 / 9450.0
    elif (p == 9.0):
        value = 1.0020083928
    elif (p == 10.0):
        value = np.pi ** 10 / 93555.0
    elif (p == 11.0):
        value = 1.0004941886
    elif (p == 12.0):
        value = 1.0002460866
    elif (p == 13.0):
        value = 1.0001227133
    elif (p == 14.0):
        value = 1.0000612482
    elif (p == 15.0):
        value = 1.0000305882
    elif (p == 16.0):
        value = 1.0000152823
    elif (p == 17.0):
        value = 1.0000076372
    elif (p == 18.0):
        value = 1.0000038173
    elif (p == 19.0):
        value = 1.0000019082
    elif (p == 20.0):
        value = 1.0000009540
    else:
        zsum = 0.0
        n = 0
        while (True):
            n = n + 1
            zsum_old = zsum
            zsum = zsum + 1.0 / n ** p
            if (zsum <= zsum_old):
                break
        value = zsum

    return value


def r8_huge():

    # *****************************************************************************80
    #
    # R8_HUGE returns a "huge" real number.
    #
    #  Discussion:
    #
    #    The value returned by this function is intended to be the largest
    #    representable real value.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real VALUE, a huge number.
    #
    value = 1.79769313486231571E+308

    return value


def r8_factorial_values(n_data):

    # *****************************************************************************80
    #
    # R8_FACTORIAL_VALUES returns values of the real factorial function.
    #
    #  Discussion:
    #
    #    0! = 1
    #    I! = Product ( 1 <= J <= I ) J
    #
    #    Although the factorial is an integer valued function, it quickly
    #    becomes too large for an integer to hold.  This routine still accepts
    #    an integer as the input argument, but returns the function value
    #    as a real number.
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      n!
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 December 2014
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
    #    Output, integer N, the argument of the function.
    #
    #    Output, real FN, the value of the function.
    #

    n_max = 25

    fn_vec = np.array([
        0.1000000000000000E+01,
        0.1000000000000000E+01,
        0.2000000000000000E+01,
        0.6000000000000000E+01,
        0.2400000000000000E+02,
        0.1200000000000000E+03,
        0.7200000000000000E+03,
        0.5040000000000000E+04,
        0.4032000000000000E+05,
        0.3628800000000000E+06,
        0.3628800000000000E+07,
        0.3991680000000000E+08,
        0.4790016000000000E+09,
        0.6227020800000000E+10,
        0.8717829120000000E+11,
        0.1307674368000000E+13,
        0.2092278988800000E+14,
        0.3556874280960000E+15,
        0.6402373705728000E+16,
        0.1216451004088320E+18,
        0.2432902008176640E+19,
        0.1551121004333099E+26,
        0.3041409320171338E+65,
        0.9332621544394415E+158,
        0.5713383956445855E+263])

    n_vec = np.array([
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        25,
        50,
        100,
        150])

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        n = 0
        fn = 0
    else:
        n = n_vec[n_data]
        fn = fn_vec[n_data]
        n_data = n_data + 1

    return n_data, n, fn


def r8_factorial(n):

    # *****************************************************************************80
    #
    # R8_FACTORIAL returns N factorial.
    #
    #  Discussion:
    #
    #    factorial ( N ) = Product ( 1 <= I <= N ) I
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 June 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the argument of the function.
    #    0 <= N.
    #
    #    Output, real VALUE, the factorial of N.
    #

    if (n < 0):
        print('')
        print('R8_FACTORIAL - Fatal error!')
        print('  N < 0.')
        exit('R8_FACTORIAL - Fatal error!')

    value = 1.0

    for i in range(2, n + 1):
        value = value * i

    return value


def r8_factorial_test():

    # *****************************************************************************80
    #
    # R8_FACTORIAL_TEST tests R8_FACTORIAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8_FACTORIAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_FACTORIAL evaluates the factorial function.')
    print('')
    print('      N                     Exact'),
    print('                  Computed')

    n_data = 0

    while (True):
        n_data, n, f1 = r8_factorial_values(n_data)
        if (n_data == 0):
            break
        f2 = r8_factorial(n)
        print('  %4d  %24.16g  %24.16g' % (n, f1, f2))

    print('')
    print('R8_FACTORIAL_TEST')
    print('  Normal end of execution.')


def r8_factorial_values_test():

    # *****************************************************************************80
    #
    # R8_FACTORIAL_VALUES_TEST tests R8_FACTORIAL_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8_FACTORIAL_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_FACTORIAL_VALUES returns values of the real factorial function.')
    print('')
    print('          N          R8_FACTORIAL(N)')
    print('')

    n_data = 0

    while (True):

        n_data, n, fn = r8_factorial_values(n_data)

        if (n_data == 0):
            break

        print('  %8d  %14.6g' % (n, fn))

    print('')
    print('R8_FACTORIAL_VALUES_TEST:')
    print('  Normal end of execution.')


def r8_huge_test():

    # *****************************************************************************80
    #
    # R8_HUGE_TEST tests R8_HUGE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 September 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8_HUGE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_HUGE returns a "huge" R8;')
    print('')
    print('    R8_HUGE = %g' % (r8_huge()))
    print('')
    print('R8_HUGE_TEST')
    print('  Normal end of execution.')


def r8_zeta_test():

    # *****************************************************************************80
    #
    # R8_ZETA_TEST tests R8_ZETA.
    #
    #  Discussion:
    #
    #    Note that SCIPY provides a ZETA function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8_ZETA_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_ZETA estimates the Zeta function.')

    print('')
    print('       P     R8_Zeta(P)')
    print('')
    for p in range(1, 26):
        v = r8_zeta(p)
        print('  %6d  %14.6g' % (p, v))

    print('')
    for i in range(0, 9):
        p = 3.0 + float(i) / 8.0
        v = r8_zeta(p)
        print('  %6g  %14.6g' % (p, v))

    print('')
    print('R8_ZETA_TEST')
    print('  Normal end of execution.')


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

    print('')
    print('R8_UNIFORM_01_TEST')
    print('  Normal end of execution.')


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

    print('')
    print('R8_NORMAL_01_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
