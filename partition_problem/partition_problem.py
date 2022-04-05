#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import math
import platform
import time
import sys
import os
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp


def partition_brute(n, w):

    # *****************************************************************************80
    #
    # PARTITION_BRUTE approaches the partition problem using brute force.
    #
    #  Discussion:
    #
    #    We are given a set of N integers W.
    #
    #    We seek to partition W into subsets W0 and W1, such that the subsets
    #    have equal sums.
    #
    #    The "discrepancy" is the absolute value of the difference between the
    #    two sums, and will be zero if we have solved the problem.
    #
    #    For a given set of integers, there may be zero, one, or many solutions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 November 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the size of the set.
    #
    #    Input, integer W(N), the integers.
    #
    #    Output, bool C(N), indicates the proposed solution.
    #    C(I) is True or False if weight I is or is not in the left set of the
    #    partition.
    #
    #    Output, integer DISCREPANCY, the discrepancy.
    #
    import numpy as np

    w_sum = np.sum(w)

    c = np.zeros(n, dtype=np.int32)
    discrepancy = w_sum

    d = np.zeros(n, dtype=np.int32)

    rank = -1

    while (True):

        d, rank = subset_next(n, d, rank)

        if (rank == -1):
            break

        p_sum = 0
        for i in range(0, n):
            if (d[i]):
                p_sum = p_sum + w[i]

        d_discrepancy = abs(w_sum - 2 * p_sum)

        if (d_discrepancy < discrepancy):
            discrepancy = d_discrepancy
            for i in range(0, n):
                c[i] = d[i]

        if (discrepancy == 0):
            break

    return c, discrepancy


def partition_brute_test(n, w):

    # *****************************************************************************80
    #
    # PARTITION_BRUTE_TEST tests PARTITION_BRUTE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 November 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of weights.
    #
    #    Input, integer W(N), a set of weights.
    #
    import platform

    print('')
    print('PARTITION_BRUTE_TEST:')
    print('  PARTITION_BRUTE seeks a balanced partition using brute force.')
    print('  Partition a set of N integers W so that the subsets')
    print('  have equal sums.')

    c, discrepancy = partition_brute(n, w)

    print('')
    print('     I        W0        W1')
    print('')
    w0_sum = 0
    w1_sum = 0
    for i in range(0, n):
        if (c[i]):
            w0_sum = w0_sum + w[i]
            print('  %4d  %8d' % (i, w[i]))
        else:
            w1_sum = w1_sum + w[i]
            print('  %4d            %8d' % (i, w[i]))

    print('        --------  --------')
    print('        %8d  %8d' % (w0_sum, w1_sum))
    print('')
    print('  Discrepancy = %d' % (discrepancy))
#
#  Terminate.
#
    print('')
    print('PARTITION_BRUTE_TEST:')
    print('  Normal end of execution.')
    return


def partition_brute_tests():

    # *****************************************************************************80
    #
    # PARTITION_BRUTE_TESTS tests PARTITION_BRUTE_TEST.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 November 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('PARTITION_BRUTE_TESTS:')
    print('  Python version: %s' % (platform.python_version()))
    print('  PARTITION_BRUTE_TEST calls PARTITION_BRUTE with a particular.')
    print('  set of weights.')

    for test in range(0, 5):

        if (test == 0):
            n = 5
            w = np.array([19, 17, 13, 9, 6])
        elif (test == 1):
            n = 9
            w = np.array([484, 114, 205, 288, 506, 503, 201, 127, 410])
        elif (test == 2):
            n = 10
            w = np.array([771, 121, 281, 854, 885, 734, 486, 1003, 83, 62])
        elif (test == 3):
            n = 10
            w = np.array([2, 10, 3, 8, 5, 7, 9, 5, 3, 2])
        elif (test == 4):
            n = 9
            w = np.array([3, 4, 3, 1, 3, 2, 3, 2, 1])

        partition_brute_test(n, w)
#
#  Terminate.
#
    print('')
    print('PARTITION_BRUTE_TESTS:')
    print('  Normal end of execution.')
    return


def partition_count(n, w):

    # *****************************************************************************80
    #
    # PARTITION_COUNT counts the solutions to a partition problem.
    #
    #  Discussion:
    #
    #    We are given a set of N integers W.
    #
    #    We seek to partition W into subsets W0 and W1, such that the subsets
    #    have equal sums.
    #
    #    The "discrepancy" is the absolute value of the difference between the
    #    two sums, and will be zero if we have solved the problem.
    #
    #    For a given set of integers, there may be zero, one, or many solutions.
    #
    #    In the case where the weights are distinct, the count returned by this
    #    function may be regarded as twice as big as it should be, since the
    #    partition (W0,W1) is counted a second time as (W1,W0).  A more serious
    #    overcount can occur if the set W contains duplicate elements - in the
    #    extreme case, W might be entirely 1's, in which case there is really
    #    only one (interesting) solution, but this function will count many.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 May 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the size of the set.
    #
    #    Input, integer W(N), the integers.
    #
    #    Output, integer COUNT, the number of solutions.
    #
    import numpy as np

    w_sum = np.sum(w)

    c = np.zeros(n, dtype=bool)
    rank = -1
    count = 0

    while (True):

        c, rank = subset_next(n, c, rank)

        if (rank == -1):
            break

        p_sum = 0
        for i in range(0, n):
            if (c[i]):
                p_sum = p_sum + w[i]

        discrepancy = abs(w_sum - 2 * p_sum)

        if (discrepancy == 0):
            count = count + 1

    return count


def partition_count_test(n, w):

    # *****************************************************************************80
    #
    # PARTITION_COUNT_TEST tests PARTITION_COUNT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 November 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of weights.
    #
    #    Input, integer W(N), a set of weights.
    #
    print('')
    print('PARTITION_COUNT_TEST:')
    print('  PARTITION_COUNT counts the number of exact solutions')
    print('  of the partition problem.')

    count = partition_count(n, w)

    print('')
    print('     I        W')
    print('')
    for i in range(0, n):
        print('  %4d  %8d' % (i, w[i]))
    print('')
    print('  Number of solutions = %d' % (count))
#
#  Terminate.
#
    print('')
    print('PARTITION_COUNT_TEST:')
    print('  Normal end of execution.')
    return


def partition_count_tests():

    # *****************************************************************************80
    #
    # PARTITION_COUNT_TESTS tests PARTITION_COUNT_TEST.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 November 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('PARTITION_COUNT_TESTS:')
    print('  Python version: %s' % (platform.python_version()))
    print('  PARTITION_COUNT_TEST calls PARTITION_COUNT with a particular')
    print('  set of weights.')

    for test in range(0, 5):

        if (test == 0):
            n = 5
            w = np.array([19, 17, 13, 9, 6])
        elif (test == 1):
            n = 9
            w = np.array([484, 114, 205, 288, 506, 503, 201, 127, 410])
        elif (test == 2):
            n = 10
            w = np.array([771, 121, 281, 854, 885, 734, 486, 1003, 83, 62])
        elif (test == 3):
            n = 10
            w = np.array([2, 10, 3, 8, 5, 7, 9, 5, 3, 2])
        elif (test == 4):
            n = 9
            w = np.array([3, 4, 3, 1, 3, 2, 3, 2, 1])

        partition_count_test(n, w)
#
#  Terminate.
#
    print('')
    print('PARTITION_COUNT_TESTS:')
    print('  Normal end of execution.')
    return


def partition_problem_test():

    # *****************************************************************************80
    #
    # PARTITION_PROBLEM_TEST tests the PARTITION_PROBLEM library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 November 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('PARTITION_PROBLEM_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the PARTITION_PROBLEM library.')

    partition_brute_tests()
    partition_count_tests()
    subset_next_test()

    print('')
    print('PARTITION_PROBLEM_TEST:')
    print('  Normal end of execution.')
    return


def subset_next(n, t, rank):

    # *****************************************************************************80
    #
    # % SUBSET_NEXT computes the subset lexicographic successor.
    #
    #  Discussion:
    #
    #    This is a lightly modified version of "subset_lex_successor()" from COMBO.
    #
    #  Example:
    #
    #    On initial call, N is 5 and the input value of RANK is -1.
    #    Then here are the successive outputs from the program:
    #
    #   Rank   T1   T2   T3   T4   T5
    #   ----   --   --   --   --   --
    #      0    0    0    0    0    0
    #      1    0    0    0    0    1
    #      2    0    0    0    1    0
    #      3    0    0    0    1    1
    #     ..   ..   ..   ..   ..   ..
    #     30    1    1    1    1    0
    #     31    1    1    1    1    1
    #     -1    0    0    0    0    0  <-- Reached end of cycle.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 November 2015
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
    #    Input/output, bool T(N), describes a subset.  T(I) is False if
    #    the I-th element of the master set is not in the subset, and is
    #    True if the I-th element is part of the subset.
    #    On input, T describes a subset.
    #    On output, T describes the next subset in the ordering.
    #
    #    Input/output, integer RANK, the rank.
    #    If RANK = -1 on input, then the routine understands that this is
    #    the first call, and that the user wishes the routine to supply
    #    the first element in the ordering, which has RANK = 0.
    #    In general, the input value of RANK is increased by 1 for output,
    #    unless the very last element of the ordering was input, in which
    #    case the output value of RANK is -1.
    #

    #
    #  Return the first element.
    #
    if (rank == -1):
        rank = 0
        return t, rank

    for i in range(n - 1, -1, -1):

        if (not t[i]):
            t[i] = True
            rank = rank + 1
            return t, rank

        t[i] = False

    rank = -1

    return t, rank


def subset_next_test():

    # *****************************************************************************80
    #
    # SUBSET_NEXT_TEST tests SUBSET_NEXT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 November 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('SUBSET_NEXT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SUBSET_NEXT generates all subsets of an N set.')

    print('')
    n = 5
    t = np.zeros(n, dtype=bool)
    rank = -1

    while (True):

        t, rank = subset_next(n, t, rank)

        if (rank == -1):
            break

        k = 0

        for i in range(0, n):

            if (t[i]):
                k = k + 1
                print('  %d' % (i)),

        if (k == 0):
            print('  (empty set)'),

        print('')

    print('')
    print('SUBSET_NEXT_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    partition_problem_test()
    timestamp()
