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

from i4lib.i4_uniform_ab import i4_uniform_ab
from i4lib.i4vec_indicator0 import i4vec_indicator0
from subset.perm0_print import perm0_print


def perm0_random2(n, seed):

    # *****************************************************************************80
    #
    # PERM0_RANDOM2 selects a random permutation of (0,...,N-1).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    K L Hoffman, D R Shier,
    #    Algorithm 564,
    #    A Test Problem Generator for Discrete Linear L1 Approximation Problems,
    #    ACM Transactions on Mathematical Software,
    #    Volume 6, Number 4, December 1980, pages 615-617.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer P[N], a permutation in standard index form.
    #
    #    Output, integer SEED, an updated seed.
    #

    p = i4vec_indicator0(n)

    for i in range(0, n):

        iadd, seed = i4_uniform_ab(1, n, seed)
        j = ((i + iadd) % n)

        k = p[i]
        p[i] = p[j]
        p[j] = k

    return p, seed


def perm0_random2_test():

    # *****************************************************************************80
    #
    # PERM0_RANDOM2_TEST tests PERM0_RANDOM2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10

    print('')
    print('PERM0_RANDOM2_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PERM0_RANDOM2 randomly selects a 0-based permutation.')
    print('')

    seed = 123456789

    for test in range(0, 5):
        p, seed = perm0_random2(n, seed)
        perm0_print(n, p, '')
#
#  Terminate.
#
    print('')
    print('PERM0_RANDOM2_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    perm0_random2_test()
    timestamp()
