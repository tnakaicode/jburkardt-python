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


def r8_uniform_ab(a, b, seed):

    # *****************************************************************************80
    #
    # R8_UNIFORM_AB returns a scaled pseudorandom R8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 April 2013
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
    #    Input, real A, B, the minimum and maximum values.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real R, the randomly chosen value.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    i4_huge = 2147483647

    if (seed == 0):
        print('')
        print('R8_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8_UNIFORM_AB - Fatal error!')

    seed = int(seed)
    seed = (seed % i4_huge)

    if (seed < 0):
        seed = seed + i4_huge

    k = (seed // 127773)
    seed = 16807 * (seed - k * 127773) - k * 2836

    if (seed < 0):
        seed = seed + i4_huge

    r = a + (b - a) * seed * 4.656612875E-10

    return r, seed


def r8_uniform_ab_test():

    # *****************************************************************************80
    #
    # R8_UNIFORM_AB_TEST tests R8_UNIFORM_AB.
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

    a = 10.0
    b = 20.0

    print('')
    print('R8_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_UNIFORM_AB returns random values in a given range:')
    print('  [ A, B ]')
    print('')
    print('  For this problem:')
    print('  A = %f' % (a))
    print('  B = %f' % (b))
    print('')

    seed = 123456789

    for i in range(0, 10):
        r, seed = r8_uniform_ab(a, b, seed)
        print('  %f' % (r))

    print('')
    print('R8_UNIFORM_AB_TEST')
    print('  Normal end of execution')


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    r8_uniform_01_test()
    timestamp()
