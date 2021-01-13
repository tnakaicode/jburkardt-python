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
from i4lib.i4_huge import i4_huge
from subset.rat_to_s import rat_to_s


def rat_div(top1, bot1, top2, bot2):

    # *****************************************************************************80
    #
    # RAT_DIV divides one rational value by another.
    #
    #  Discussion:
    #
    #    The routine computes
    #
    #      TOP / BOT = ( TOP1 / BOT1 ) / ( TOP2 / BOT2 ).
    #
    #    while avoiding integer overflow.
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
    #    Input, integer TOP1, BOT1, the numerator.
    #
    #    Input, integer TOP2, BOT2, the denominator.
    #
    #    Output, integer TOP, BOT, the result.
    #
    #    Output, integer IERROR.
    #    0, no error occurred.
    #    1, an error occurred.  One of the quantities BOT1, BOT2,
    #    or TOP2 is zero, or the result of the division
    #    requires a numerator or denominator larger than the
    #    maximum legal integer.
    #

    ierror = 0
    top = 0
    bot = 1

    i_max = i4_huge()

    if (bot1 == 0 or top2 == 0 or bot2 == 0):
        ierror = 1
        return top, bot, ierror

    if (top1 == 0):
        top = 0
        bot = 1
        return top, bot, ierror
#
#  Implicitly invert the divisor fraction here.  The rest of
#  the code will be a multiply operation.
#
    jbot1 = bot1
    jbot2 = top2
    jtop1 = top1
    jtop2 = bot2
#
#  Get rid of all common factors in top and bottom.
#
    itemp = i4_gcd(jtop1, jbot1)
    jtop1 = jtop1 // itemp
    jbot1 = jbot1 // itemp
    itemp = i4_gcd(jtop1, jbot2)
    jtop1 = jtop1 // itemp
    jbot2 = jbot2 // itemp
    itemp = i4_gcd(jtop2, jbot1)
    jtop2 = jtop2 // itemp
    jbot1 = jbot1 // itemp
    itemp = i4_gcd(jtop2, jbot2)
    jtop2 = jtop2 // itemp
    jbot2 = jbot2 // itemp
#
#  The fraction (TOP1*BOT2)/(BOT1*TOP2) is in lowest terms.
#
#  Check the top for overflow.
#
    if (i_max < abs(jtop1 * jtop2)):
        print('')
        print('RAT_DIV - Warning!')
        print('  Overflow of top of rational fraction.')
        top = 0
        bot = 1
        ierror = 1
        return top, bot, ierror

    top = jtop1 * jtop2
#
#  Check the bottom BOT1*TOP2 for overflow.
#
    if (i_max < abs(jbot1 * jbot2)):
        print('')
        print('RAT_DIV - Fatal error!')
        print('  Overflow of bottom of rational fraction.')
        top = 0
        bot = 1
        ierror = 1
        return top, bot, ierror

    bot = jbot1 * jbot2
#
#  The bottom should be positive.
#
    if (bot < 0):
        bot = -bot
        top = -top

    return top, bot, ierror


def rat_div_test():

    # *****************************************************************************80
    #
    # RAT_DIV_TEST tests RAT_DIV.
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

    print('')
    print('RAT_DIV_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RAT_DIV divides two rationals.')

    atop = 3
    abot = 4
    btop = 10
    bbot = 7

    ctop, cbot, ierror = rat_div(atop, abot, btop, bbot)

    print('')
    s = rat_to_s(atop, abot)
    print('  A = %s' % (s))
    s = rat_to_s(btop, bbot)
    print('  B = %s' % (s))
    s = rat_to_s(ctop, cbot)
    print('  C = A / B = %s' % (s))
#
#  Terminate.
#
    print('')
    print('RAT_DIV_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    rat_div_test()
    timestamp()
