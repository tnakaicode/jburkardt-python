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
from polynomial.mono_next_grlex import mono_next_grlex, mono_upto_next_grlex
from polynomial.mono_upto_enum import mono_upto_enum


def mono_rank_grlex(m, x):

    # *****************************************************************************80
    #
    # MONO_RANK_GRLEX computes the graded lexicographic rank of a monomial.
    #
    #  Discussion:
    #
    #    The graded lexicographic ordering is used, over all monomials in
    #    M dimensions, for total degree = 0, 1, 2, ...
    #
    #    For example, if M = 3, the ranking begins:
    #
    #    Rank  Sum    1  2  3
    #    ----  ---   -- -- --
    #       1    0    0  0  0
    #
    #       2    1    0  0  1
    #       3    1    0  1  0
    #       4    1    1  0  1
    #
    #       5    2    0  0  2
    #       6    2    0  1  1
    #       7    2    0  2  0
    #       8    2    1  0  1
    #       9    2    1  1  0
    #      10    2    2  0  0
    #
    #      11    3    0  0  3
    #      12    3    0  1  2
    #      13    3    0  2  1
    #      14    3    0  3  0
    #      15    3    1  0  2
    #      16    3    1  1  1
    #      17    3    1  2  0
    #      18    3    2  0  1
    #      19    3    2  1  0
    #      20    3    3  0  0
    #
    #      21    4    0  0  4
    #      ..   ..   .. .. ..
    #
    #  Licensing:
    #
    #   This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #    1 <= M.
    #
    #    Input, integer X[M], the composition.
    #    For each 1 <= I <= M, we have 0 <= X(I).
    #
    #    Output, integer RANK, the rank.
    #

    #
    #  Ensure that 1 <= M.
    #
    if (m < 1):
        print('')
        print('MONO_RANK_GRLEX - Fatal error!')
        print('  M < 1')
        exit('MONO_RANK_GRLEX - Fatal error!')

    #
    #  Ensure that 0 <= X(I).
    #
    for i in range(0, m):
        if (x[i] < 0):
            print('')
            print('MONO_RANK_GRLEX - Fatal error!')
            print('  X[I] < 0')
            exit('MONO_RANK_GRLEX - Fatal error!')

    #
    #  NM = sum ( X )
    #
    nm = i4vec_sum(m, x)

    #
    #  Convert to KSUBSET format.
    #
    ns = nm + m - 1
    ks = m - 1
    if (0 < ks):
        xs = np.zeros(ks, dtype=np.int32)
        xs[0] = x[0] + 1
        for i in range(2, m):
            xs[i - 1] = xs[i - 2] + x[i - 1] + 1

    #
    #  Compute the rank.
    #
    rank = 1

    for i in range(1, ks + 1):
        if (i == 1):
            tim1 = 0
        else:
            tim1 = xs[i - 2]

        if (tim1 + 1 <= xs[i - 1] - 1):
            for j in range(tim1 + 1, xs[i - 1]):
                rank = rank + i4_choose(ns - j, ks - i)

    for n in range(0, nm):
        rank = rank + i4_choose(n + m - 1, n)

    return rank


def mono_rank_grlex_test():

    # ******************************************************************************/
    #
    # MONO_RANK_GRLEX_TEST tests MONO_RANK_GRLEX.
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

    m = 3
    test_num = 8
    x_test = np.array([
        0, 0, 0,
        1, 0, 0,
        0, 0, 1,
        0, 2, 0,
        1, 0, 2,
        0, 3, 1,
        3, 2, 1,
        5, 2, 1], dtype=np.int32)

    print('')
    print('MONO_RANK_GRLEX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MONO_RANK_GRLEX returns the rank of a monomial in the sequence')
    print('  of all monomials in M dimensions, in grlex order.')

    print('')
    print('  Print a monomial sequence with ranks assigned.')

    n = 4

    print('')
    print('  Let M = %d' % (m))
    print('      N = %d' % (n))
    print('')

    x = np.zeros(m, dtype=np.int32)

    x[0] = 0
    x[1] = 0
    x[2] = 0

    i = 1

    while (True):
        print('  %2d    ' % (i)),
        for j in range(0, m):
            print('%2d' % (x[j])),
        print('')

        if (x[0] == n):
            break

        mono_upto_next_grlex(m, n, x)
        i = i + 1

    print('')
    print('  Now, given a monomial, retrieve its rank in the sequence:')
    print('')

    for test in range(0, test_num):
        for j in range(0, m):
            x[j] = x_test[j + test * m]
        rank = mono_rank_grlex(m, x)

        print('  %3d    ' % (rank)),
        for j in range(0, m):
            print('%2d' % (x[j])),
        print('')
    print('')
    print('MONO_RANK_GRLEX_TEST')
    print('  Normal end of execution.')


def mono_unrank_grlex(m, rank):

    # *****************************************************************************80
    #
    # MONO_UNRANK_GRLEX computes the monomial of given grlex rank.
    #
    #  Licensing:
    #
    #   This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 October 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #    1 <= M.
    #
    #    Input, integer RANK, the rank of the monomial.
    #
    #    Output, integer X[M], the monomial.
    #

    #
    #  Ensure that 1 <= M.
    #
    if (m < 1):
        print('')
        print('MONO_UNRANK_GRLEX - Fatal error!')
        print('  M < 1')
        exit('MONO_UNRANK_GRLEX - Fatal error!')

    #
    #  Ensure that 1 <= RANK.
    #
    if (rank < 1):
        print('')
        print('MONO_UNRANK_GRLEX - Fatal error!')
        print('  RANK < 1')
        exit('MONO_UNRANK_GRLEX - Fatal error!')

    x = np.zeros(m, dtype=np.int32)

    #
    #  Special case M = 1.
    #
    if (m == 1):
        x[0] = rank - 1
        return x

    #
    #  Determine the appropriate value of NM.
    #  Do this by adding up the number of compositions of sum 0, 1, 2,
    #  ..., without exceeding RANK.  Moreover, RANK - this sum essentially
    #  gives you the rank of the composition within the set of compositions
    #  of sum NM.  And that's the number you need in order to do the
    #  unranking.
    #
    rank1 = 1
    nm = -1
    while (True):
        nm = nm + 1
        r = i4_choose(nm + m - 1, nm)
        if (rank < rank1 + r):
            break
        rank1 = rank1 + r

    rank2 = rank - rank1

    #
    #  Convert to KSUBSET format.
    #  Apology: an unranking algorithm was available for KSUBSETS,
    #  but not immediately for compositions.  One day we will come back
    #  and simplify all this.
    #
    ks = m - 1
    ns = nm + m - 1
    xs = np.zeros(ks, dtype=np.int32)

    nksub = i4_choose(ns, ks)

    j = 1

    for i in range(1, ks + 1):
        r = i4_choose(ns - j, ks - i)

        while (r <= rank2 and 0 < r):
            rank2 = rank2 - r
            j = j + 1
            r = i4_choose(ns - j, ks - i)

        xs[i - 1] = j
        j = j + 1

    #
    #  Convert from KSUBSET format to COMP format.
    #
    x[0] = xs[0] - 1
    for i in range(2, m):
        x[i - 1] = xs[i - 1] - xs[i - 2] - 1
    x[m - 1] = ns - xs[ks - 1]

    return x


def mono_unrank_grlex_test():

    # ******************************************************************************/
    #
    # MONO_UNRANK_GRLEX_TEST tests MONO_UNRANK_GRLEX.
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

    m = 3
    print('')
    print('MONO_UNRANK_GRLEX')
    print('  Python version: %s' % (platform.python_version()))
    print('  MONO_UNRANK_GRLEX is given a rank, and returns the corresponding')
    print('  monomial in the sequence of all monomials in M dimensions')
    print('  in grlex order.')

    print('')
    print('  For reference, print a monomial sequence with ranks.')

    n = 4
    rank_max = mono_upto_enum(m, n)

    print('')
    print('  Let M = %d' % (m))
    print('      N = %d' % (n))
    print('')

    x = np.zeros(m, dtype=np.int32)

    i = 1

    while (True):
        print('  %2d    ' % (i)),
        for j in range(0, m):
            print('%2d' % (x[j])),
        print('')

        if (x[0] == n):
            break

        mono_upto_next_grlex(m, n, x)
        i = i + 1

    print('')
    print('  Now choose random ranks between 1 and %d' % (rank_max))
    print('')

    seed = 123456789
    test_num = 5

    for test in range(0, test_num):
        rank, seed = i4_uniform_ab(1, rank_max, seed)
        x = mono_unrank_grlex(m, rank)
        print('  %2d    ' % (rank)),
        for j in range(0, m):
            print('%2d' % (x[j])),
        print('')
    print('')
    print('MONO_UNRANK_GRLEX_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    mono_rank_grlex_test()
    mono_unrank_grlex_test()
    timestamp()
