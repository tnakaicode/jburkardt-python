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

from i4lib.i4vec_backtrack import i4vec_backtrack
from subset.perm0_free import perm0_free


def derange0_back_next(n, a, more, indx, k, maxstack, nstack, stacks, ncan):

    # *****************************************************************************80
    #
    # DERANGE0_BACK_NEXT returns the next derangement of N items.
    #
    #  Discussion:
    #
    #    A derangement of N objects is a permutation of (0,...,N-1) which leaves no object
    #    unchanged.
    #
    #    A derangement of N objects is a permutation with no fixed
    #    points.  If we symbolize the permutation operation by "P",
    #    then for a derangment, P(I) is never equal to I.
    #
    #    The number of derangements of N objects is sometimes called
    #    the subfactorial function, or the derangement number D(N).
    #
    #    This routine uses backtracking.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of items to be deranged.
    #
    #    Input, integer A(N), the output value of A from the previous call.
    #    On first call with MORE = FALSE, the input value of A is not important.
    #
    #    Input, logical MORE, should be set to FALSE on the first call, to force
    #    initialization, and should be TRUE thereafter.
    #
    #    Input, integer INDX, K, MAXSTACK, NSTACK, STACKS(N*(N+1)/2), NCAN(N),
    #    bookkeeping variables which the user must set up, but not alter.
    #
    #    Output, integer A(N), contains the next derangement, if MORE is TRUE.
    #
    #    Output, logical MORE, is TRUE if another derangement was found, and
    #    FALSE if there are no more derangements to return.
    #
    #    Output, integer INDX, K, MAXSTACK, NSTACK, STACKS(N*(N+1)/2), NCAN(N),
    #    bookkeeping variables which the user must set up, but not alter.
    #

    if (not more):

        if (n < 2):
            more = False
            return a, more, indx, k, maxstack, nstack, stacks, ncan

        indx = 0
        k = 0
        maxstack = ((n * (n + 1)) // 2)
        nstack = 0
        for i in range(0, maxstack):
            stacks[i] = 0
        for i in range(0, n):
            ncan[i] = 0
        more = True

    while (True):

        a, indx, k, nstack, stacks, ncan = i4vec_backtrack(n, maxstack,
                                                           a, indx, k, nstack, stacks, ncan)

        if (indx == 1):

            break

        elif (indx == 2):

            nstack, stacks, ncan = derange0_back_candidate(n, a, k, nstack,
                                                           stacks, ncan)

        else:

            more = False
            break

    return a, more, indx, k, maxstack, nstack, stacks, ncan


def derange0_back_candidate(n, a, k, nstack, stacks, ncan):

    # *****************************************************************************80
    #
    # DERANGE0_BACK_CANDIDATE: possible K-th entries of a derangement of (1,...,N).
    #
    #  Discussion:
    #
    #    A derangement of N objects is a permutation of (0,...,N-1) which leaves
    #    no object unchanged.
    #
    #    A derangement of N objects is a permutation with no fixed
    #    points.  If we symbolize the permutation operation by "P",
    #    then for a derangment, P(I) is never equal to I.
    #
    #    The number of derangements of N objects is sometimes called
    #    the subfactorial function, or the derangement number D(N).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the derangement.
    #
    #    Input, integer A(N).  The first K-1 entries of A
    #    record the currently set values of the derangement.
    #
    #    Input, integer K, the entry of the derangement for which candidates
    #    are to be found.
    #
    #    Input, integer NSTACK, the length of the stack.
    #
    #    Input, integer STACKS((N*(N+1))/2).
    #
    #    Input, integer NCAN(N), the number of candidates for each level.
    #
    #    Output, integer NSTACK, the length of the output stack.
    #
    #    Output, integer STACKS((N*(N+1))/2), contains candidates for entry K
    #    added to the end of the stack.
    #
    #    Output, integer NCAN(N), the number of candidates for each level.
    #

    #
    #  Consider all the integers from 1 through N that have not been used yet.
    #
    nfree = n - k + 1

    ifree = perm0_free(k - 1, a, nfree)
#
#  Everything but K is a legitimate candidate for the K-th entry.
#
    ncan[k - 1] = 0

    for ican in range(0, nfree):

        if (ifree[ican] != k - 1):
            ncan[k - 1] = ncan[k - 1] + 1
            stacks[nstack] = ifree[ican]
            nstack = nstack + 1

    return nstack, stacks, ncan


def derange0_back_next_test():

    # *****************************************************************************80
    #
    # DERANGE0_BACK_NEXT_TEST tests DERANGE0_BACK_NEXT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    n = 5
    a = np.zeros(n)
    more = False
    indx = 0
    k = 0
    maxstack = ((n * (n + 1)) // 2)
    nstack = 0
    stacks = np.zeros(maxstack, dtype=np.int32)
    ncan = np.zeros(n, dtype=np.int32)

    print('')
    print('DERANGE0_BACK_NEXT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DERANGE0_BACK_NEXT generates derangements')
    print('  using backtracking.')
    print('')
    print('  Here, we seek all derangements of order N = %d' % (n))
    print('')

    rank = 0

    while (True):

        a, more, indx, k, maxstack, nstack, stacks, ncan = derange0_back_next(n,
                                                                              a, more, indx, k, maxstack, nstack, stacks, ncan)

        if (not more):
            break

        rank = rank + 1
        print('  %2d' % (rank)),
        for i in range(0, n):
            print('  %2d' % (a[i])),
        print('')
#
#  Terminate.
#
    print('')
    print('DERANGE0_BACK_NEXT_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    derange0_back_next_test()
    timestamp()
