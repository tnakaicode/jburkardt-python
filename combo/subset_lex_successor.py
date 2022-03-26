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

from combo.subset_check import subset_check

from i4lib.i4_choose import i4_choose
from i4lib.i4vec_print import i4vec_print, i4vec_print_test
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from r8lib.i4vec_transpose import i4vec_transpose_print, i4vec_transpose_print_test
from r8lib.r8vec_transpose import r8vec_transpose_print, r8vec_transpose_print_test
from r8lib.r8mat_transpose import r8mat_transpose_print, r8mat_transpose_print_some


def subset_lex_successor(n, t, rank):

    # *****************************************************************************80
    #
    # SUBSET_LEX_SUCCESSOR computes the subset lexicographic successor.
    #
    #  Discussion:
    #
    #    In the original code, there is a last element with no successor.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Donald Kreher, Douglas Simpson,
    #    Combinatorial Algorithms,
    #    CRC Press, 1998,
    #    ISBN: 0-8493-3988-X,
    #    LC: QA164.K73.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of elements in the master set.
    #    N must be positive.
    #
    #    Input/output, integer T(N), describes a subset.  T(I) is 0 if
    #    the I-th element of the master set is not in the subset, and is
    #    1 if the I-th element is part of the subset.
    #    On input, T describes a subset.
    #    On output, T describes the next subset in the ordering.
    #    If the input T was the last in the ordering, then the output T
    #    will be the first.
    #
    #    Input/output, integer RANK, the rank.
    #    If RANK = -1 on input, then the routine understands that this is
    #    the first call, and that the user wishes the routine to supply
    #    the first element in the ordering, which has RANK = 0.
    #    In general, the input value of RANK is increased by 1 for output,
    #    unless the very last element of the ordering was input, in which
    #    case the output value of RANK is 0.
    #

    #
    #  Return the first element.
    #
    if (rank == -1):
        for i in range(0, n):
            t[i] = 0
        rank = 0
        return t, rank
#
#  Check.
#
    check = subset_check(n, t)

    if (not check):
        print('')
        print('SUBSET_LEX_SUCCESSOR - Fatal error!')
        print('  The subset is not legal.')
        exit('SUBSET_LEX_SUCCESSOR - Fatal error!')

    for i in range(n - 1, -1, -1):

        if (t[i] == 0):
            t[i] = 1
            rank = rank + 1
            return t, rank
        else:
            t[i] = 0

    rank = 0

    return t, rank


def subset_lex_successor_test():

    # *****************************************************************************80
    #
    # SUBSET_LEX_SUCCESSOR_TEST tests SUBSET_LEX_SUCCESSOR.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 December 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 5

    print('')
    print('SUBSET_LEX_SUCCESSOR_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SUBSET_LEX_SUCCESSOR lists subsets of a set,')
    print('  using the lexicographic ordering.')

    t = np.zeros(n)
    rank = -1

    while (True):

        rank_old = rank

        t, rank = subset_lex_successor(n, t, rank)

        if (rank <= rank_old):
            break

        i4vec_transpose_print(n, t, '')
#
#  Terminate.
#
    print('')
    print('SUBSET_LEX_SUCCESSOR_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    subset_lex_successor_test()
    timestamp()
