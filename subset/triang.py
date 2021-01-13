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

from i4lib.i4vec_decrement import i4vec_decrement
from i4lib.i4mat_2perm0 import i4mat_2perm0
from subset.perm0_print import perm0_print
from subset.pord_check import pord_check


def triang(n, zeta):

    # *****************************************************************************80
    #
    # TRIANG renumbers elements in accordance with a partial ordering.
    #
    #  Discussion:
    #
    #    TRIANG is given a partially ordered set.  The partial ordering
    #    is defined by a matrix ZETA, where element I is partially less than
    #    or equal to element J if and only if ZETA(I,J) = 1.
    #
    #    TRIANG renumbers the elements with a permutation P so that if
    #    element I is partially less than element J in the partial ordering,
    #    then P(I) < P(J) in the usual, numerical ordering.
    #
    #    In other words, the elements are relabeled so that their labels
    #    reflect their ordering.  This is equivalent to relabeling the
    #    matrix so that, on unscrambling it, the matrix would be upper
    #    triangular.
    #
    #    Calling I4MAT_PERM or R8MAT_PERM with P used for both the row
    #    and column permutations applied to matrix ZETA will result in
    #    an upper triangular matrix.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 June 2015
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
    #    Input, integer N, the number of elements in the set.
    #
    #    Input, integer ZETA(N,N), describes the partial ordering.
    #    ZETA(I,J) =:
    #      0, for diagonal elements (I = J), or
    #         for unrelated elements, or
    #         if J << I.
    #      1, if I << J.
    #
    #    Output, integer P(N), a permutation of (0,...,N-1) that reflects
    #    the partial ordering of the elements.  P(I) is the new label of element
    #    I, with the property that if ZETA(I,J) = 1, that is, I << J,
    #    then P(I) < P(J) (in the usual ordering).
    #

    #
    #  Make sure ZETA represents a partially ordered set.  In other words,
    #  if ZETA(I,J) = 1, then ZETA(J,I) must NOT be 1.
    #
    ierror = pord_check(n, zeta)

    if (ierror != 0):
        print('')
        print('TRIANG - Fatal error!')
        print('  The matrix ZETA does not represent a')
        print('  partial ordering.')
        exit('TRIANG - Fatal error!')

    m = 1
    l = 0
    p = np.zeros(n, dtype=np.int32)

    it = m + 1
    ir = m + 1

    while (True):

        if (ir <= n):

            if (p[ir - 1] == 0 and zeta[ir - 1, m - 1] != 0):
                p[ir - 1] = m
                m = ir
                ir = it
            else:
                ir = ir + 1

        else:

            l = l + 1
            iq = p[m - 1]
            p[m - 1] = l

            if (iq != 0):

                ir = m + 1
                m = iq

            elif (m == n):

                break

            else:

                while (True):

                    m = m + 1

                    if (p[m - 1] == 0):
                        break

                    if (m == n):
                        p = i4vec_decrement(n, p)
                        return p

                it = m + 1
                ir = m + 1

    p = i4vec_decrement(n, p)

    return p


def triang_test():

    # *****************************************************************************80
    #
    # TRIANG_TEST tests TRIANG.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10

    a = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 1, 0, 1]], dtype=np.int32)

    print('')
    print('TRIANG_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TRIANG relabels elements for a partial ordering,')

    i4mat_print(n, n, a, '  The input matrix:')

    p = triang(n, a)

    perm0_print(n, p, '  The new ordering:')

    a = i4mat_2perm0(n, n, a, p, p)

    i4mat_print(n, n, a, '  The reordered matrix:')
#
#  Terminate.
#
    print('')
    print('TRIANG_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    triang_test()
    timestamp()
