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

from i4lib.i4_choose import i4_choose
from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write


def mono_between_enum(m, n1, n2):

    # *****************************************************************************80
    #
    # MONO_BETWEEN_ENUM enumerates monomials in M dimensions of degrees in a range.
    #
    #  Discussion:
    #
    #    For M = 3, we have the following table:
    #
    #     N2 0  1  2  3  4  5  6   7   8
    #   N1 +----------------------------
    #    0 | 1  4 10 20 35 56 84 120 165
    #    1 | 0  3  9 19 34 55 83 119 164
    #    2 | 0  0  6 16 31 52 80 116 161
    #    3 | 0  0  0 10 25 46 74 110 155
    #    4 | 0  0  0  0 15 36 64 100 145
    #    5 | 0  0  0  0  0 21 49  85 130
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N1, N2, the minimum and maximum degrees.
    #    0 <= N1 <= N2.
    #
    #    Output, integer VALUE, the number of monomials in M variables,
    #    of total degree between N1 and N2 inclusive.
    #

    n1 = max(n1, 0)

    if (n2 < n1):
        value = 0
        return value

    if (n1 == 0):
        value = i4_choose(n2 + m, n2)
    elif (n1 == n2):
        value = i4_choose(n2 + m - 1, n2)
    else:
        n0 = n1 - 1
        value = i4_choose(n2 + m, n2) - i4_choose(n0 + m, n0)

    return value


def mono_between_enum_test():

    # *****************************************************************************80
    #
    # MONO_BETWEEN_ENUM_TEST tests MONO_BETWEEN_ENUM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('MONO_BETWEEN_ENUM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MONO_BETWEEN_ENUM can enumerate the number of monomials')
    print('  in M variables, of total degree between N1 and N2.')

    m = 3
    print('')
    print('  Using spatial dimension M = %d' % (m))
    print('')
    print('   N2:', end='')
    for n2 in range(0, 9):
        print('  %4d' % (n2), end='')
    print('')
    print('  N1 +---------------------------------------------------------------')
    for n1 in range(0, 9):
        print('  %2d |' % (n1), end='')
        for n2 in range(0, 9):
            v = mono_between_enum(m, n1, n2)
            print('  %4d' % (v), end='')
        print('')
#
#  Terminate.
#
    print('')
    print('MONO_BETWEEN_ENUM_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    mono_between_enum_test()
    timestamp()
