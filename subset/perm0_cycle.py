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

from subset.perm0_print import perm0_print
from subset.perm0_check import perm0_check


def perm0_cycle(n, p):

    # *****************************************************************************80
    #
    # PERM0_CYCLE analyzes a permutation of (0,...,N-1).
    #
    #  Discussion:
    #
    #    The routine will count cycles, find the sign of a permutation,
    #    and tag a permutation.
    #
    #  Example:
    #
    #    Input:
    #
    #      N = 9
    #      P = 1, 2, 8, 5, 6, 7, 4, 3, 0
    #
    #    Output:
    #
    #      S = +1
    #      NCYCLE = 3
    #      TAG = -1, 1, 1,-1, -1, 1, 1, 1, 1
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 June 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Albert Nijenhuis, Herbert Wilf,
    #    Combinatorial Algorithms,
    #    Academic Press, 1978, second edition,
    #    ISBN 0-12-519260-6.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of objects being permuted.
    #
    #    Input, integer P(N), the permutation to be analyzed.
    #
    #    Output, integer S, the "sign" of the permutation, which is
    #    +1 if the permutation is even, -1 if odd.  Every permutation
    #    may be produced by a certain number of pairwise switches.
    #    If the number of switches is even, the permutation itself is
    #    called even.
    #
    #    Output, integer NCYCLE, the number of cycles in the permutation.
    #
    #    Output, integer TAG(N).  If TAG(I) is -1, then P(I) is the first element
    #    of a cycle.
    #

    check = perm0_check(n, p)

    if (not check):
        print('')
        print('PERM0_CYCLE - Fatal error!')
        print('  The input array does not represent')
        print('  a proper permutation.')
        exit('PERM0_CYCLE - Fatal error!')

    ncycle = n
    tag = np.ones(n, dtype=np.int32)

    for i in range(0, n):

        i1 = p[i] * tag[i]

        while (i < i1):
            ncycle = ncycle - 1
            i2 = p[i1]
            tag[i1] = - tag[i1]
            i1 = i2

    s = 1 - 2 * ((n - ncycle) % 2)

    for i in range(0, n):
        tag[i] = - tag[i]

    return s, ncycle, tag


def perm0_cycle_test():

    # *****************************************************************************80
    #
    # PERM0_CYCLE_TEST tests PERM0_CYCLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 9

    p = np.array([1, 2, 8, 5, 6, 7, 4, 3, 0], dtype=np.int32)

    print('')
    print('PERM0_CYCLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PERM0_CYCLE analyzes a permutation.')

    perm0_print(n, p, '  The permutation:')

    s, ncycle, tag = perm0_cycle(n, p)

    print('')
    print('  S    =   %d' % (s))
    print('  NCYCLE = %d' % (ncycle))

    perm0_print(n, tag, '  The permutation cycle tags:')
#
#  Terminate.
#
    print('')
    print('PERM0_CYCLE_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    perm0_cycle_test()
    timestamp()
