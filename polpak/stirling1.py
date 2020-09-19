#! /usr/bin/env python
#
def stirling1(n, m):

    # *****************************************************************************80
    #
    # STIRLING1 computes the Stirling numbers of the first kind.
    #
    #  Discussion:
    #
    #    The absolute value of the Stirling number S1(N,M) gives the number
    #    of permutations on N objects having exactly M cycles, while the
    #    sign of the Stirling number records the sign (odd or even) of
    #    the permutations.  For example, there are six permutations on 3 objects:
    #
    #      A B C   3 cycles (A) (B) (C)
    #      A C B   2 cycles (A) (BC)
    #      B A C   2 cycles (AB) (C)
    #      B C A   1 cycle  (ABC)
    #      C A B   1 cycle  (ABC)
    #      C B A   2 cycles (AC) (B)
    #
    #    There are
    #
    #      2 permutations with 1 cycle, and S1(3,1) = 2
    #      3 permutations with 2 cycles, and S1(3,2) = -3,
    #      1 permutation with 3 cycles, and S1(3,3) = 1.
    #
    #    Since there are N! permutations of N objects, the sum of the absolute
    #    values of the Stirling numbers in a given row,
    #
    #      sum ( 1 <= I <= N ) abs ( S1(N,I) ) = N!
    #
    #  First terms:
    #
    #    N/M:  1     2      3     4     5    6    7    8
    #
    #    1     1     0      0     0     0    0    0    0
    #    2    -1     1      0     0     0    0    0    0
    #    3     2    -3      1     0     0    0    0    0
    #    4    -6    11     -6     1     0    0    0    0
    #    5    24   -50     35   -10     1    0    0    0
    #    6  -120   274   -225    85   -15    1    0    0
    #    7   720 -1764   1624  -735   175  -21    1    0
    #    8 -5040 13068 -13132  6769 -1960  322  -28    1
    #
    #  Recursion:
    #
    #    S1(N,1) = (-1)^(N-1) * (N-1)! for all N.
    #    S1(I,I) = 1 for all I.
    #    S1(I,J) = 0 if I < J.
    #
    #    S1(N,M) = S1(N-1,M-1) - (N-1) * S1(N-1,M)
    #
    #  Properties:
    #
    #    sum ( 1 <= K <= M ) S2(I,K) * S1(K,J) = Delta(I,J)
    #
    #    X_N = sum ( 0 <= K <= N ) S1(N,K) X^K
    #    where X_N is the falling factorial function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of rows of the table.
    #
    #    Input, integer M, the number of columns of the table.
    #
    #    Output, integer S1(N,M), the Stirling numbers of the first kind.
    #
    import numpy as np

    s1 = np.zeros((n, m))

    if (n <= 0):
        return s1

    if (m <= 0):
        return s1

    s1[0, 0] = 1
    for j in range(1, m):
        s1[0, j] = 0

    for i in range(1, n):

        s1[i, 0] = - i * s1[i - 1, 0]

        for j in range(1, m):
            s1[i, j] = s1[i - 1, j - 1] - i * s1[i - 1, j]

    return s1


def stirling1_test():

    # *****************************************************************************80
    #
    # STIRLING1_TEST tests STIRLING1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform
    from i4mat_print import i4mat_print

    print('')
    print('STIRLING1_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test STIRLING1, which returns Stirling numbers of the first kind.')

    m = 8
    n = 8
    s1 = stirling1(m, n)
    i4mat_print(m, n, s1, '  Stirling1 matrix:')
#
#  Terminate.
#
    print('')
    print('STIRLING1_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    stirling1_test()
    timestamp()
