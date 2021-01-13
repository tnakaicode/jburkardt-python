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
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write

from i4lib.i4_gcd import i4_gcd
from r8lib.r8_uniform_01 import r8_uniform_01


def rat_to_r8(a, b):

    # *****************************************************************************80
    #
    # RAT_TO_R8 converts rational values to real values.
    #
    #  Example:
    #
    #    A    B    R
    #   --   --    ---
    #    1    2    0.5
    #    7    5    1.4
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer A, B, the rational quantity to be converted.
    #
    #    Output, real R, the value of the rational quantity as a real number.
    #

    if (b == 0):
        print('')
        print('RAT_TO_R8 - Fatal error!')
        print('  The input fraction to be converted had a')
        print('  zero denominator.')
        exit('RAT_TO_R8 - Fatal error!')

    r = a / b

    return r


def rat_to_r8_test():

    # *****************************************************************************80
    #
    # RAT_TO_R8_TEST tests RAT_TO_R8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    ndig = 4

    print('')
    print('RAT_TO_R8_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RAT_TO_R8 converts a rational to a real number.')
    print('')
    print('  The maximum number of digits allowed is %d' % (ndig))

    seed = 123456789

    print('')
    print('     R   =>  A / B  =>  R2')
    print('')

    for i in range(0, 10):
        r, seed = r8_uniform_01(seed)
        r = 10.0 * (r - 0.25)
        a, b = r8_to_rat(r, ndig)
        r2 = rat_to_r8(a, b)
        print('  %10g  %6d  %6d  %10g' % (r, a, b, r2))
#
#  Terminate.
#
    print('')
    print('RAT_TO_R8_TEST')
    print('  Normal end of execution.')
    return


def r8_to_rat(r, ndig):

    # *****************************************************************************80
    #
    # R8_TO_RAT converts a real value to a rational value.
    #
    #  Discussion:
    #
    #    The rational value (IATOP/IABOT) is essentially computed by truncating
    #    the decimal representation of the real value after a given number of
    #    decimal digits.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real R, the real value to be converted.
    #
    #    Input, integer NDIG, the number of decimal digits used.
    #
    #    Output, integer IATOP, IABOT, the numerator and denominator
    #    of the rational value that approximates the real number.
    #

    factor = 10 ** ndig

    if (0 < ndig):
        ifac = 10 ** ndig
        jfac = 1
    else:
        ifac = 1
        jfac = 10 ** (- ndig)

    itop = int(round(r * factor) * jfac)
    ibot = ifac
#
#  Factor out the greatest common factor.
#
    itemp = i4_gcd(itop, ibot)

    iatop = (itop // itemp)
    iabot = (ibot // itemp)

    return iatop, iabot


def r8_to_rat_test():

    # *****************************************************************************80
    #
    # R8_TO_RAT_TEST tests R8_TO_RAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    ndig = 4

    print('')
    print('R8_TO_RAT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_TO_RAT converts a real number to a rational')
    print('')
    print('  The maximum number of digits allowed is %d' % (ndig))

    seed = 123456789

    print('')
    print('     R   =>  A / B  =>  R2')
    print('')

    for i in range(0, 10):
        r, seed = r8_uniform_01(seed)
        r = 10.0 * (r - 0.25)
        a, b = r8_to_rat(r, ndig)
        r2 = rat_to_r8(a, b)
        print('  %10g  %6d  %6d  %10g' % (r, a, b, r2))
#
#  Terminate.
#
    print('')
    print('R8_TO_RAT_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    rat_to_r8_test()
    timestamp()
