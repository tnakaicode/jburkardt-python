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

from i4lib.i4vec_sum import i4vec_sum
from subset.comp_next import comp_next


def subcomp_next(n, k, a, more, h, t, n2, more2):

    # *****************************************************************************80
    #
    # SUBCOMP_NEXT computes the next subcomposition of N into K parts.
    #
    #  Discussion:
    #
    #    A composition of the integer N into K parts is an ordered sequence
    #    of K nonnegative integers which sum to a value of N.
    #
    #    A subcomposition of the integer N into K parts is a composition
    #    of M into K parts, where 0 <= M <= N.
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
    #    Input, integer N, the integer whose subcompositions are desired.
    #
    #    Input, integer K, the number of parts in the subcomposition.
    #
    #    Input, integer A(K), the parts of the subcomposition.
    #
    #    Input, logical MORE, set to FALSE by the user to start the computation.
    #
    #    Input, integer H, T, N2, internal parameters needed for the
    #    computation.  The user may need to initialize these before the
    #    very first call, but these initial values are not important.
    #    The user should not alter these parameters once the computation
    #    begins.
    #
    #    Input, logical MORE2, an internal parameter needed for the
    #    computation.  The user may need to initialize this before the
    #    very first call, but the initial value is not important.
    #    The user should not alter this parameter once the computation
    #    begins.
    #
    #    Output, integer A(K), the parts of the subcomposition.
    #
    #    Output, logical MORE, set to FALSE by the routine to terminate
    #    the computation.
    #
    #    Output, integer H, T, N2, updated values.
    #
    #    Output, logical MORE2, an updated value.
    #

    #
    #  The first computation.
    #
    if (not more):

        for i in range(0, k):
            a[i] = 0
        more = True
        h = 0
        t = 0
        n2 = 0
        more2 = False
#
#  Do the next element at the current value of N.
#
    elif (more2):

        a, more2, h, t = comp_next(n2, k, a, more2, h, t)

    else:

        more2 = False
        n2 = n2 + 1

        a, more2, h, t = comp_next(n2, k, a, more2, h, t)
#
#  Termination occurs if MORE2 = FALSE and N2 = N.
#
    if (not more2 and n2 == n):
        more = False

    return a, more, h, t, n2, more2


def subcomp_next_test():

    # *****************************************************************************80
    #
    # SUBCOMP_NEXT_TEST tests SUBCOMP_NEXT.
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

    n = 6
    k = 3
    a = np.zeros(k)
    more = False
    h = 0
    t = 0
    n2 = 0
    more2 = False

    print('')
    print('SUBCOMP_NEXT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SUBCOMP_NEXT generates subcompositions.')
    print('')
    print('  Seek all subcompositions of N = %d' % (n))
    print('  Into K = %d parts.' % (k))
    print('')
    print('     #   Sum')
    print('')

    rank = 0

    while (True):

        a, more, h, t, n2, more2 = subcomp_next(n, k, a, more, h, t, n2, more2)

        rank = rank + 1
        print('  %4d  %4d  ' % (rank, i4vec_sum(k, a))),
        for i in range(0, k):
            print('%4d' % (a[i])),
        print('')

        if (not more):
            break
#
#  Terminate.
#
    print('')
    print('SUBCOMP_NEXT_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    subcomp_next_test()
    timestamp()
