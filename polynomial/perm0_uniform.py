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
from i4lib.i4_fall import i4_fall
from i4lib.i4_uniform_ab import i4_uniform_ab
from i4lib.i4vec_concatenate import i4vec_concatenate
from i4lib.i4vec_permute import i4vec_permute
from i4lib.i4vec_print import i4vec_print
from i4lib.i4vec_sort_heap_index_a import i4vec_sort_heap_index_a
from i4lib.i4vec_sum import i4vec_sum
from i4lib.i4vec_uniform_ab import i4vec_uniform_ab
from r8lib.r8vec_concatenate import r8vec_concatenate
from r8lib.r8vec_permute import r8vec_permute
from r8lib.r8vec_print import r8vec_print


def perm0_uniform(n, seed):

    # *****************************************************************************80
    #
    # PERM0_UNIFORM selects a random permutation of 0, ..., N-1.
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


def perm0_uniform_test():

    # *****************************************************************************80
    #
    # PERM0_UNIFORM_TEST tests PERM0_UNIFORM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10

    print('')
    print('PERM0_UNIFORM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PERM0_UNIFORM randomly selects a permutation of 0, ..., N-1.')
    print('')

    seed = 123456789

    for test in range(0, 5):
        p, seed = perm0_uniform(n, seed)
        print('  ', end='')
        for i in range(0, n):
            print('%4d' % (p[i]), end='')
        print(' ')

    print('')
    print('PERM0_UNIFORM_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    perm0_uniform_test()
    timestamp()
