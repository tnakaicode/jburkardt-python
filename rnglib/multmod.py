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


def multmod(a, s, m):

    # *****************************************************************************80
    #
    # MULTMOD carries out modular multiplication.
    #
    #  Discussion:
    #
    #    This procedure returns
    #
    #      ( A * S ) mod M
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 July 2015
    #
    #  Author:
    #
    #    Original Pascal version by Pierre L'Ecuyer, Serge Cote.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Pierre LEcuyer, Serge Cote,
    #    Implementing a Random Number Package with Splitting Facilities,
    #    ACM Transactions on Mathematical Software,
    #    Volume 17, Number 1, March 1991, pages 98-111.
    #
    #  Parameters:
    #
    #    Input, integer A, S, M, the arguments.
    #
    #    Output, integer VALUE, the value of the product of A and S,
    #    modulo M.
    #

    h = 32768

    if (a <= 0):
        print('')
        print('MULTMOD - Fatal error!')
        print('  A <= 0.')
        exit('MULTMOD - Fatal error!')

    if (m <= a):
        print('')
        print('MULTMOD - Fatal error!')
        print('  M <= A.')
        exit('MULTMOD - Fatal error!')

    if (s <= 0):
        print('')
        print('MULTMOD - Fatal error!')
        print('  S <= 0.')
        exit('MULTMOD - Fatal error!')

    if (m <= s):
        print('')
        print('MULTMOD - Fatal error!')
        print('  M <= S.')
        exit('MULTMOD - Fatal error!')

    if (a < h):

        a0 = a
        p = 0

    else:

        a1 = (a // h)
        a0 = a - h * a1
        qh = (m // h)
        rh = m - h * qh

        if (h <= a1):

            a1 = a1 - h
            k = (s // qh)
            p = h * (s - k * qh) - k * rh

            while (p < 0):
                p = p + m

        else:

            p = 0

        if (a1 != 0):

            q = (m // a1)
            k = (s // q)
            p = p - k * (m - a1 * q)

            if (0 < p):
                p = p - m

            p = p + a1 * (s - k * q)

            while (p < 0):
                p = p + m

        k = (p // qh)
        p = h * (p - k * qh) - k * rh

        while (p < 0):
            p = p + m

    if (a0 != 0):

        q = (m // a0)
        k = (s // q)
        p = p - k * (m - a0 * q)

        if (0 < p):
            p = p - m

        p = p + a0 * (s - k * q)

        while (p < 0):
            p = p + m

    return p
