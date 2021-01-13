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


def rat_add(top1, bot1, top2, bot2):

    # *****************************************************************************80
    #
    # RAT_ADD adds two rational values.
    #
    #  Discussion:
    #
    #    The routine computes
    #
    #      TOP/BOT = TOP1/BOT1 + TOP2/BOT2
    #
    #    while trying to avoid integer overflow.
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
    #    Input, integer TOP1, BOT1, the first value to add.
    #
    #    Input, integer TOP2, BOT2, the second value to add.
    #
    #    Output, integer TOP, BOT, the sum.
    #
    #    Output, integer IERROR.
    #    0, no error occurred.
    #    1, an error occurred.  The addition of the two values
    #    requires a numerator or denominator larger than the
    #    maximum legal integer.
    #

    i_max = i4_huge()

    ierror = 0

    if (top1 == 0):
        top = top2
        bot = bot2
        return top, bot, ierror
    elif (top2 == 0):
        top = top1
        bot = bot1
        return top, bot, ierror
#
#  Compute the greatest common factor of the two denominators,
#  and factor it out.
#
    bot3 = i4_gcd(bot1, bot2)
    bot1 = bot1 // bot3
    bot2 = bot2 // bot3
#
#  The fraction may now be formally written as:
#
#    (top1*bot2 + top2*bot1) / (bot1*bot2*bot3)
#
#  Check the tops for overflow.
#
    if (i_max < abs(top1 * bot2)):
        print('')
        print('RAT_ADD - Warning!')
        print('  Overflow of top of rational sum.')
        top = 0
        bot = 1
        ierror = 1
        return top, bot, ierror

    top1 = top1 * bot2

    if (i_max < abs(top2 * bot1)):
        ierror = 1
        print('')
        print('RAT_ADD - Fatal error!')
        print('  Overflow of top of rational sum.')
        top = 0
        bot = 1
        ierror = 1
        return top, bot, ierror

    top2 = top2 * bot1

    if (i_max < abs(top1 + top2)):
        print('')
        print('RAT_ADD - Fatal error!')
        print('  Overflow of top of rational sum.')
        top = 0
        bot = 1
        return top, bot, ierror

    top = top1 + top2
#
#  Check the bottom for overflow.
#
    if (i_max < abs(bot1 * bot2 * bot3)):
        print('')
        print('RAT_ADD - Fatal error!')
        print('  Overflow of bottom of rational sum.')
        top = 0
        bot = 1
        ierror = 1
        return top, bot, ierror

    bot = bot1 * bot2 * bot3
#
#  Put the fraction in lowest terms.
#
    itemp = i4_gcd(top, bot)
    top = top // itemp
    bot = bot // itemp
#
#  The bottom should be positive.
#
    if (bot < 0):
        bot = -bot
        top = -top

    return top, bot, ierror


def rat_add_test():

    # *****************************************************************************80
    #
    # % RAT_ADD_TEST tests RAT_ADD.
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
    print('RAT_ADD_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RAT_ADD adds two rationals.')

    atop = 3
    abot = 4
    btop = 10
    bbot = 7

    ctop, cbot, ierror = rat_add(atop, abot, btop, bbot)

    print('')
    s = rat_to_s(atop, abot)
    print('  A = %s' % (s))
    s = rat_to_s(btop, bbot)
    print('  B = %s' % (s))
    s = rat_to_s(ctop, cbot)
    print('  C = A + B = %s' % (s))
#
#  Terminate.
#
    print('')
    print('RAT_ADD_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    rat_add_test()
    timestamp()
