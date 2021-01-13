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

from i4lib.i4vec_product import i4vec_product


def index_unrank1(n, hi, rank):

    # *****************************************************************************80
    #
    # INDEX_UNRANK1 unranks an index vector within given upper limits.
    #
    #  Example:
    #
    #    N = 3,
    #    HI(1) = 4, HI(2) = 2, HI(3) = 3
    #    RANK = 11
    #
    #    A = ( 3, 1, 2 )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in A.
    #
    #    Input, integer HI(N), the upper limits for the array indices.
    #    The lower limit is implicitly 1, and each HI(I) should be at least 1.
    #
    #    Input, integer RANK, the rank of the desired index vector.
    #
    #    Output, integer A(N), the index vector of the given rank.
    #

    a = np.zeros(n)
#
#  The rank might be too small.
#
    if (rank < 1):
        return a

    rang = i4vec_product(n, hi)
#
#  The rank might be too large.
#
    if (rang < rank):
        return a

    k = rank - 1

    for i in range(n - 1, -1, -1):
        rang = (rang // hi[i])
        j = (k // rang)
        a[i] = j + 1
        k = k - j * rang

    return a


def index_unrank1_test():

    # *****************************************************************************80
    #
    # INDEX_UNRANK1_TEST tests INDEX_UNRANK1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 3
    hi = np.array([4, 2, 3])

    print('')
    print('INDEX_UNRANK1_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  INDEX_UNRANK1 unranks a multi-index.')
    print('')
    print('  The multi-index has dimension %d' % (n))

    i4vec_print(n, hi, '  The upper limits:')

    print('')
    print('  Rank, Multi-Index:')
    print('')

    maxrank = i4vec_product(n, hi)

    for rank in range(1, maxrank + 1):
        a = index_unrank1(n, hi, rank)
        print('  %2d  ' % (rank)),
        for i in range(0, n):
            print('  %2d' % (a[i])),
        print('')
#
#  Terminate.
#
    print('')
    print('INDEX_UNRANK1_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    index_unrank1_test()
    timestamp()
