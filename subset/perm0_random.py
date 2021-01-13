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
from subset.perm0_print import perm0_print
from subset.perm0_check import perm0_check


def perm0_random(n, seed):

    # *****************************************************************************80
    #
    # PERM0_RANDOM selects a random permutation of N objects.
    #
    #  Discussion:
    #
    #    An I4VEC is a vector of I4 values.
    #
    #    The algorithm is known as the Fisher-Yates or Knuth shuffle.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer P[N], a permutation of the digits 0 through N-1.
    #
    #    Output, integer SEED, an updated seed.
    #

    p = np.zeros(n, dtype=np.int32)

    for i in range(0, n):
        p[i] = i

    for i in range(0, n - 1):
        j, seed = i4_uniform_ab(i, n - 1, seed)
        k = p[i]
        p[i] = p[j]
        p[j] = k

    return p, seed


def perm0_random_test():

    # *****************************************************************************80
    #
    # PERM0_RANDOM_TEST tests PERM0_RANDOM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10

    print('')
    print('PERM0_RANDOM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PERM0_RANDOM randomly selects a 0-based permutation.')
    print('')

    seed = 123456789

    for test in range(0, 5):
        p, seed = perm0_random(n, seed)
        perm0_print(n, p, '')
#
#  Terminate.
#
    print('')
    print('PERM0_RANDOM_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    perm0_random_test()
    timestamp()
