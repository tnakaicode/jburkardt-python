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


def index_rank2(n, lo, hi, a):

    # *****************************************************************************80
    #
    # INDEX_RANK2 ranks an index vector within given lower and upper limits.
    #
    #  Example:
    #
    #    N = 3,
    #    LO(1) = 1, LO(2) = 10, LO(3) = 4
    #    HI(1) = 2, HI(2) = 11, HI(3) = 6
    #    A = ( 1, 11, 5 )
    #
    #    RANK = 7
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in A.
    #
    #    Input, integer LO(N), HI(N), the lower and upper limits for the array
    #    indices.  LO(I) should be less than or equal to HI(I), for each I.
    #
    #    Input, integer A(N), the index vector to be ranked.
    #
    #    Output, integer RANK, the rank of the index vector, or -1 if A
    #    is not a legal index vector.
    #
    for i in range(0, n):
        if (a[i] < lo[i] or hi[i] < a[i]):
            rank = -1
            return rank

    rank = 1
    rang = 1
    for i in range(0, n):
        rank = rank + (a[i] - lo[i]) * rang
        rang = rang * (hi[i] + 1 - lo[i])

    return rank


def index_rank2_test():

    # *****************************************************************************80
    #
    # INDEX_RANK2_TEST tests INDEX_RANK2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 3

    a = np.array([1, 11, 5])
    hi = np.array([2, 11, 6])
    lo = np.array([1, 10, 4])

    print('')
    print('INDEX_RANK2_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  INDEX_RANK2 ranks an index with given')
    print('  lower and upper limits.')
    print('')
    print('  Number of index entries = %d' % (n))
    print('')
    print('  Coordinate, Minimum index, Maximum Index')
    print('')

    for i in range(0, n):
        print('  %8d  %8d  %8d' % (i, lo[i], hi[i]))

    i4vec_print(n, a, '  The index array:')

    rank = index_rank2(n, lo, hi, a)

    print('')
    print('  The rank of this object is %d' % (rank))
#
#  Terminate.
#
    print('')
    print('INDEX_RANK2_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    index_rank2_test()
    timestamp()
