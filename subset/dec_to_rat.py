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
from i4lib.i4_uniform_ab import i4_uniform_ab
from r8lib.r8_to_dec import r8_to_dec
from subset.dec_to_s import dec_to_s


def dec_to_rat(mantissa, exponent):

    # *****************************************************************************80
    #
    # DEC_TO_RAT converts a decimal to a rational representation.
    #
    #  Discussion:
    #
    #    A decimal value is represented by MANTISSA * 10^EXPONENT.
    #
    #    A rational value is represented by TOP / BOT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer MANTISSA, EXPONENT, the decimal number.
    #
    #    Output, integer TOP, BOT, the rational value.
    #

    if (exponent == 0):
        top = mantissa
        bot = 1
    elif (0 < exponent):
        top = mantissa * 10 ** exponent
        bot = 1
    else:
        top = mantissa
        bot = 10 ** (- exponent)
        gcd = i4_gcd(top, bot)
        top = (top // gcd)
        bot = (bot // gcd)

    return top, bot


def dec_to_rat_test():

    # *****************************************************************************80
    #
    # DEC_TO_RAT_TEST tests DEC_TO_RAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('DEC_TO_RAT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DEC_TO_RAT decimal => fraction.')
    print('')
    print('  In this test, choose the top and bottom')
    print('  of a rational at random, and compute the')
    print('  equivalent real number.')
    print('')
    print('  Then convert to decimal, and the equivalent real.')
    print('')
    print('  Then convert back to rational and the equivalent real.')

    seed = 123456789

    for i in range(0, 10):

        rat_top, seed = i4_uniform_ab(-1000, 1000, seed)
        rat_bot, seed = i4_uniform_ab(1, 1000, seed)

        r1 = float(rat_top) / float(rat_bot)
        mantissa, exponent = rat_to_dec(rat_top, rat_bot)
        r2 = float(mantissa) * 10.0 ** exponent
        rat_top2, rat_bot2 = dec_to_rat(mantissa, exponent)
        r3 = float(rat_top2) / float(rat_bot2)

        print('')
        print('  %g = %d / %d' % (r1, rat_top, rat_bot))
        print('  %g = %d * 10^%d' % (r2, mantissa, exponent))
        print('  %g = %d / %d' % (r1, rat_top2, rat_bot2))
#
#  Terminate.
#
    print('')
    print('DEC_TO_RAT_TEST')
    print('  Normal end of execution.')
    return


def rat_to_dec(top, bot):

    # *****************************************************************************80
    #
    # RAT_TO_DEC converts a rational to a decimal representation.
    #
    #  Discussion:
    #
    #    A rational value is represented by TOP / BOT.
    #
    #    A decimal value is represented as MANTISSA * 10^EXPONENT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer TOP, BOT, the rational value.
    #
    #    Output, integer MANTISSA, EXPONENT, the decimal number.
    #

    if (top == 0):
        mantissa = 0
        exponent = 0
        return mantissa, exponent

    gcd = i4_gcd(top, bot)
    top = (top // gcd)
    bot = (bot // gcd)

    if (bot < 0):
        top = -top
        bot = -bot

    if (bot == 1):
        mantissa = top
        exponent = 0
        return mantissa, exponent

    exponent = 0

    while ((bot % 10) == 0):
        exponent = exponent - 1
        bot = (bot // 10)

    while ((top % 10) == 0):
        exponent = exponent + 1
        top = (top // 10)

    r = float(top) / float(bot)

    if (r < 0.0):
        s = -1
        r = -r
    else:
        s = 1

    while (r != round(r)):
        r = r * 10.0
        exponent = exponent - 1

    mantissa = s * r

    return mantissa, exponent


def rat_to_dec_test():

    # *****************************************************************************80
    #
    # RAT_TO_DEC_TEST tests RAT_TO_DEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('RAT_TO_DEC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RAT_TO_DEC fraction => decimal,')
    print('')
    print('  In this test, choose the top and bottom')
    print('  of a rational at random, and compute the')
    print('  equivalent real number.')
    print('')
    print('  Then convert to decimal, and the equivalent real.')
    print('')
    print('  Then convert back to rational and the equivalent real.')

    seed = 123456789

    for i in range(0, 10):

        rat_top, seed = i4_uniform_ab(-1000, 1000, seed)
        rat_bot, seed = i4_uniform_ab(1, 1000, seed)

        r1 = float(rat_top) / float(rat_bot)
        mantissa, exponent = rat_to_dec(rat_top, rat_bot)
        r2 = float(mantissa) * 10.0 ** exponent
        rat_top2, rat_bot2 = dec_to_rat(mantissa, exponent)
        r3 = float(rat_top2) / float(rat_bot2)

        print('')
        print('  %g = %d / %d' % (r1, rat_top, rat_bot))
        print('  %g = %d * 10^%d' % (r2, mantissa, exponent))
        print('  %g = %d / %d' % (r1, rat_top2, rat_bot2))
#
#  Terminate.
#
    print('')
    print('RAT_TO_DEC_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    dec_to_rat_test()
    timestamp()
