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


def pythag_triple_next(i, j):

    # *****************************************************************************80
    #
    # PYTHAG_TRIPLE_NEXT computes the next Pythagorean triple.
    #
    #  Example:
    #
    #     I       J       A       B       C    A^2+B^2 = C^2
    #
    #     2       1       3       4       5      25
    #     3       2       5      12      13     169
    #     4       1      15       8      17     289
    #     4       3       7      24      25     625
    #     5       2      21      20      29     841
    #     5       4       9      40      41    1681
    #     6       1      35      12      37    1369
    #     6       3      27      36      45    2025
    #     6       5      11      60      61    3721
    #     7       2      45      28      53    2809
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer I, J, the generators.
    #    On first call, set I = J = 0.  On repeated calls, set I and J
    #    to the output values of I and J from the previous call.
    #
    #    Output, integer A, B, C, the next Pythagorean triple.
    #    A, B, and C are positive integers which have no common factors,
    #    and A**2 + B**2 = C**2.
    #
    #    Output, integer I, J, the updated values of the generators,
    #    which should be used as the input values of I and J if the routine
    #    is to be called again.
    #

    #
    #  I starts at 2, and when it increases, increases by 1 and resets J;
    #
    #  When I is reset, J starts out at 2 if I is odd, or 1 if I is even;
    #  Then I is held fixed and J increases by 2, as long as it remains less than I.
    #
    if (i == 0 and j == 0):
        i = 2
        j = 1
    elif (j + 2 < i):
        j = j + 2
    else:
        i = i + 1
        j = (i % 2) + 1

    a = i ** 2 - j ** 2
    b = 2 * i * j
    c = i ** 2 + j ** 2

    return a, b, c, i, j


def pythag_triple_next_test():

    # *****************************************************************************80
    #
    # PYTHAG_TRIPLE_NEXT_TEST tests PYTHAG_TRIPLE_NEXT
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('PYTHAG_TRIPLE_NEXT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PYTHAG_TRIPLE_NEXT computes the "next"')
    print('    Pythagorean triple.')
    print('')
    print('   I   J   A   B   C  A^2+B^2   C^2')
    print('')

    i = 0
    j = 0

    for k in range(0, 21):
        a, b, c, i, j = pythag_triple_next(i, j)
        d = a ** 2 + b ** 2
        e = c ** 2
        print('%4d  %4d  %4d  %4d  %4d  %8d  %8d' % (i, j, a, b, c, d, e))

    print('')
    print('PYTHAG_TRIPLE_NEXT_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    pythag_triple_next_test()
    timestamp()
