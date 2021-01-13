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

from i4lib.ui4_to_ubvec import ui4_to_ubvec
from i4lib.ubvec_to_ui4 import ubvec_to_ui4
from i4lib.i4_uniform_ab import i4_uniform_ab
from subset.ubvec_print import ubvec_print
from subset.ubvec_xor import ubvec_xor


def nim_sum(i, j):

    # *****************************************************************************80
    #
    # NIM_SUM computes the Nim sum of two integers.
    #
    #  Discussion:
    #
    #    If K is the Nim sum of I and J, then each bit of K is the exclusive
    #    OR of the corresponding bits of I and J.
    #
    #  Example:
    #
    #     I     J     K     I base 2    J base 2    K base 2
    #   ----  ----  ----  ----------  ----------  ----------
    #      0     0     0           0           0           0
    #      1     0     1           1           0           1
    #      1     1     0           1           1           0
    #      2     7     5          10         111         101
    #     11    28    23        1011       11100       10111
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer I, J, the integers to be Nim-summed.
    #
    #    Output, integer K, the Nim sum of I and J.
    #

    nbits = 32

    ivec = ui4_to_ubvec(i, nbits)
    jvec = ui4_to_ubvec(j, nbits)

    kvec = ubvec_xor(nbits, ivec, jvec)

    k = ubvec_to_ui4(nbits, kvec)

    return k


def nim_sum_test():

    # *****************************************************************************80
    #
    # NIM_SUM_TEST tests NIM_SUM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 32
    ihi = 1000
    ilo = 0
    ntest = 5

    print('')
    print('NIM_SUM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  NIM_SUM computes the Nim sum of two integers.')
    print('')
    print('    I    J    Nim(I+J)')
    print('')

    seed = 123456789

    for i in range(0, ntest):

        i1, seed = i4_uniform_ab(ilo, ihi, seed)
        i1vec = ui4_to_ubvec(i1, n)

        i2, seed = i4_uniform_ab(ilo, ihi, seed)
        i2vec = ui4_to_ubvec(i2, n)

        i3 = nim_sum(i1, i2)
        i3vec = ui4_to_ubvec(i3, n)

        print('')
        print('  I1, I2, I3 in decimal:')
        print('')
        print('  %3d' % (i1))
        print('  %3d' % (i2))
        print('  %3d' % (i3))
        print('')
        print('  I1, I2, I3 in binary:')
        print('')

        ubvec_print(n, i1vec, '')
        ubvec_print(n, i2vec, '')
        ubvec_print(n, i3vec, '')
#
#  Terminate.
#
    print('')
    print('NIM_SUM_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    nim_sum_test()
    timestamp()
