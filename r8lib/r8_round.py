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

from r8lib.r8_uniform_ab import r8_uniform_01


def r8_round(x):

    # *****************************************************************************80
    #
    # R8_ROUND sets an R8 to the nearest integral value.
    #
    #  Example:
    #
    #        X        R8_ROUND
    #
    #      1.3         1.0
    #      1.4         1.0
    #      1.5         1.0 or 2.0
    #      1.6         2.0
    #      0.0         0.0
    #     -0.7        -1.0
    #     -1.1        -1.0
    #     -1.6        -2.0
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
    #  Parameters:
    #
    #    Input, real X, the value.
    #
    #    Output, real R8_ROUND, the rounded value.
    #
    if (x < 0.0):
        value = - int(- x + 0.5)
    else:
        value = int(+ x + 0.5)

    return value


def r8_round_test():

    # *****************************************************************************80
    #
    # R8_ROUND_TEST tests R8_ROUND.
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

    print('')
    print('R8_ROUND_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_ROUND rounds a real number to a real number with integer value.')
    print('')
    print('  X     XROUND')
    print('')
    s = + 1.0

    for i in range(0, 10):

        x, seed = r8_uniform_01(seed)
        x = s * 100.0 * x
        xround = r8_round(x)
        print(' %f  %f' % (x, xround))
        s = - s

    print('')
    print('R8_ROUND_TEST')
    print('  Normal end of execution.')


def r8_roundx(nplace, x):

    # *****************************************************************************80
    #
    # R8_ROUNDX rounds an R8.
    #
    #  Discussion:
    #
    #    Assume that the input quantity X has the form
    #
    #      X = S * J * 10^L
    #
    #    where S is plus or minus 1, L is an integer, and J is a decimal
    #    mantissa which is either exactly zero, or greater than or equal
    #    to 0.1 and less than 1.0.
    #
    #    Then on return, XROUND will satisfy
    #
    #      XROUND = S * K * 10^L
    #
    #    where S and L are unchanged, and K is a decimal mantissa which
    #    agrees with J in the first NPLACE decimal digits and is zero
    #    thereafter.
    #
    #    Note that because of rounding, most decimal fraction quantities
    #    cannot be stored exactly in the computer, and hence will have
    #    trailing "bogus" digits.
    #
    #    If NPLACE is 0, XROUND will always be zero.
    #
    #    If NPLACE is 1, the mantissa of XROUND will be 0, 0.1,
    #    0.2, ..., or 0.9.
    #
    #    If NPLACE is 2, the mantissa of XROUND will be 0, 0.01, 0.02,
    #    0.03, ..., 0.98, 0.99.
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
    #  Parameters:
    #
    #    Input, integer NPLACE, the number of decimal digits to
    #    preserve.  NPLACE should be 0 or positive.
    #
    #    Input, real X, the number to be decomposed.
    #
    #    Output, real XROUND, the rounded value of X.
    #
    
    xround = 0.0
    
    #
    #  1: Handle the special case of 0.
    #
    if (x == 0.0):
        return xround

    if (nplace <= 0):
        return xround
    
    #
    #  2: Determine the sign S.
    #
    if (0.0 < x):
        s = 1
        xtemp = x
    else:
        s = -1
        xtemp = -x
    
    #
    #  3: Force XTEMP to lie between 1 and 10, and compute the
    #  logarithm L.
    #
    
    l = 0
    while (10.0 <= x):
        xtemp = xtemp / 10.0
        l = l + 1

    while (xtemp < 1.0):
        xtemp = xtemp * 10.0
        l = l - 1
    
    #
    #  4: Now strip out the digits of the mantissa as XMANT, and
    #  decrease L.
    #
    xmant = 0.0
    iplace = 0

    while (True):

        xmant = 10.0 * xmant

        if (1.0 <= xtemp):
            xmant = xmant + int(xtemp)
            xtemp = xtemp - int(xtemp)

        iplace = iplace + 1

        if (xtemp == 0.0 or nplace <= iplace):
            xround = s * xmant * 10.0 ** l
            break

        l = l - 1
        xtemp = xtemp * 10.0

    return xround


def r8_roundx_test():

    # *****************************************************************************80
    #
    # R8_ROUNDX_TEST tests R8_ROUNDX.
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
    x = np.pi

    print('')
    print('R8_ROUNDX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_ROUNDX rounds a number to a')
    print('  specified number of decimal digits.')
    print('')
    print('  Test effect on PI:')
    print('  X = %f' % (x))
    print('')
    print('  NPLACE  XROUND')
    print('')

    for i in range(0, 11):
        nplace = i
        xround = r8_roundx(nplace, x)
        print('  %6d  %f' % (i, xround))

    print('')
    print('  Test effect on random values:')
    print('')
    print('  NPLACE  X     XROUND')
    print('')

    for i in range(1, 6):

        x, seed = r8_uniform_01(seed)

        print('')

        for i in range(0, 6):
            nplace = 2 * i
            xround = r8_roundx(nplace, x)
            print('  %6d  %f  %f' % (nplace, x, xround))

    print('')
    print('R8_ROUNDX_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    r8_round_test()
    r8_roundx_test()
    timestamp()
