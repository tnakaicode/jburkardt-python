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
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8_uniform_01 import r8_uniform_01
from r8lib.r8mat_transpose_print import r8mat_transpose_print


def grid_generate(m, n, center, seed):

    # *****************************************************************************80
    #
    # GRID_GENERATE generates a grid dataset.
    #
    #  Discussion:
    #
    #    N points are needed in an M dimensional space.
    #
    #    The points are to lie on a uniform grid of side N_SIDE.
    #
    #    Unless the N = N_SIDE^M for some N_SIDE, we can't use all the
    #    points on a grid.  What we do is find the smallest N_SIDE
    #    that's big enough, and randomly omit some points.
    #
    #    If N_SIDE is 4, then the choices in 1D are:
    #
    #    A: 0,   1/3, 2/3, 1
    #    B: 1/5, 2/5, 3/5, 4/5
    #    C: 0,   1/4, 2/4, 3/4
    #    D: 1/4, 2/4, 3/4, 1
    #    E: 1/8, 3/8, 5/8, 7/8
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of points to generate.
    #
    #    Input, integer CENTER, specifies the 1D grid centering:
    #    1: first point is 0.0, last point is 1.0
    #    2: first point is 1/(N+1), last point is N/(N+1)
    #    3: first point is 0, last point is (N-1)/N
    #    4: first point is 1/N, last point is 1
    #    5: first point is 1/(2*N), last point is (2*N-1)/(2*N)
    #
    #    Input, integer SEED, the random number seed.
    #
    #    Output, real R(M,N), the points.
    #
    #    Output, integer SEED, the updated random number seed.
    #

    #
    #  Find the dimension of the smallest grid with N points.
    #
    n_side = grid_side(m, n)

    #
    #  We need to select N points out of N_SIDE^M set.
    #
    n_grid = n_side ** m

    #
    #  Generate a random subset of N items from a set of size N_GRID.
    #
    rank_list, seed = ksub_random2(n_grid, n, seed)

    #
    #  Must make one dummy call to TUPLE_NEXT_FAST with RANK = 0.
    #
    base = np.zeros(m)
    rank = -1
    tple, base = tuple_next_fast(n_side, m, rank, base)

    #
    #  Now generate the appropriate indices, and "center" them.
    #
    r = np.zeros([m, n])

    for j in range(0, n):

        rank = rank_list[j] - 1
        tple, base = tuple_next_fast(n_side, m, rank, base)

        for i in range(0, m):

            if (center == 1):
                r[i, j] = float(tple[i] - 1) / float(n_side - 1)
            elif (center == 2):
                r[i, j] = float(tple[i]) / float(n_side + 1)
            elif (center == 3):
                r[i, j] = float(tple[i] - 1) / float(n_side)
            elif (center == 4):
                r[i, j] = float(tple[i]) / float(n_side)
            elif (center == 5):
                r[i, j] = float(2 * tple[i] - 1) / float(2 * n_side)

    return r, seed


def grid_generate_test(center, seed):

    # *****************************************************************************80
    #
    # GRID_GENERATE_TEST tests GRID_GENERATE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #

    m = 2
    n = 10

    print('')
    print('GRID_GENERATE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  GRID_GENERATE randomly chooses a given number of')
    print('  points on a uniform grid.')
    print('')
    print('  Spatial dimension =  %d' % (m))
    print('  Number of points =   %d' % (n))
    print('  Random number SEED = %d' % (seed))
    print('  Centering option =   %d' % (center))

    x, seed = grid_generate(m, n, center, seed)
    r8mat_transpose_print(m, n, x, '  Grid points:')

    print('')
    print('GRID_GENERATE_TEST:')
    print('  Normal end of execution.')


def grid_generate_tests():

    # *****************************************************************************80
    #
    # GRID_GENERATE_TESTS tests GRID_GENERATE_TEST.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('GRID_GENERATE_TESTS:')
    print('  GRID_GENERATE_TEST generates a specific grid.')

    center = 1
    seed = 123456789

    grid_generate_test(center, seed)

    print('')
    print('  Repeat with a different seed from the first run.')

    seed = 987654321
    grid_generate_test(center, seed)

    print('')
    print('  Repeat with the same seed as the first run.')

    seed = 123456789
    grid_generate_test(center, seed)

    print('')
    print('  Repeat with different centering values.')

    for center in range(1, 6):
        seed = 123456789
        grid_generate_test(center, seed)

    print('')
    print('GRID_GENERATE_TESTS:')
    print('  Normal end of execution.')


def grid_side(m, n):

    # *****************************************************************************80
    #
    # GRID_SIDE finds the smallest M-D grid containing at least N points.
    #
    #  Discussion:
    #
    #    Each coordinate of the grid will have N_SIDE distinct values.
    #    Thus the total number of points in the grid is N_SIDE**M.
    #    This routine seeks the smallest N_SIDE such that N <= N_SIDE**M.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of points to generate.
    #
    #    Output, integer N_SIDE, the length of one side of the smallest
    #    grid in M dimensions that contains at least N points.
    #
    if (n <= 0):

        n_side = 0

    elif (m <= 0):

        n_side = -1

    else:

        exponent = 1.0 / float(m)

        n_side = int((float(n)) ** exponent)

        if ((n_side ** m) < n):
            n_side = n_side + 1

    return n_side


def grid_side_test():

    # *****************************************************************************80
    #
    # GRID_SIDE_TEST tests GRID_SIDE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('GRID_SIDE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  GRID_SIDE returns the smallest N_SIDE, such that')
    print('  N <= NSIDE^M')

    print('')
    print('  M      N  NSIDE  NSIDE^M')

    for m in range(2, 5):
        print('')
        for n in [10, 100, 1000, 10000]:
            n_side = grid_side(m, n)
            print('  %1d  %5d  %5d  %5d' % (m, n, n_side, n_side ** m))

    print('')
    print('GRID_SIDE_TEST:')
    print('  Normal end of execution.')


def grid_test():

    # *****************************************************************************80
    #
    # GRID_TEST tests the GRID library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('GRID_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the GRID library.')

    grid_generate_tests()
    grid_side_test()
    tuple_next_fast_test()

    print('')
    print('GRID_TEST:')
    print('  Normal end of execution.')


def ksub_random2(n, k, seed):

    # *****************************************************************************80
    #
    # KSUB_RANDOM2 selects a random subset of size K from a set of size N.
    #
    #  Discussion:
    #
    #    This algorithm is designated Algorithm RKS2 in the reference.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 December 2014
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
    #    Input, integer N, the size of the set from which subsets are drawn.
    #
    #    Input, integer K, number of elements in desired subsets.  K must
    #    be between 0 and N.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer A(K).  A(I) is the I-th element of the
    #    output set.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    if (k < 0):
        print('')
        print('KSUB_RANDOM - Fatal error!')
        print('  K = %d' % (k))
        print('  but 0 < K is required!')
        exit('KSUB_RANDOM - Fatal error!')

    if (n < k):
        print('')
        print('KSUB_RANDOM - Fatal error!')
        print('  N = %d' % (n))
        print('  K = %d' % (k))
        print('  K <= N is required!')
        exit('KSUB_RANDOM - Fatal error!')

    a = np.zeros(k)

    if (k == 0):
        return a

    need = k
    have = 0

    available = n
    candidate = 0

    while (True):

        candidate = candidate + 1

        r, seed = r8_uniform_01(seed)

        if (available * r <= need):

            need = need - 1
            a[have] = candidate
            have = have + 1

            if (need <= 0):
                break

        available = available - 1

    return a, seed


def ksub_random2_test():

    # *****************************************************************************80
    #
    # KSUB_RANDOM2_TEST tests KSUB_RANDOM2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    k = 3
    n = 5

    print('')
    print('KSUB_RANDOM2_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  KSUB_RANDOM2 generates a random K subset of an N set.')
    print('  Set size is N =    %d' % (n))
    print('  Subset size is K = %d' % (k))
    print('')

    seed = 123456789

    for i in range(0, 10):

        a, seed = ksub_random2(n, k, seed)

        for j in range(0, k):
            print('  %3d' % (a[j]), end='')
        print('')

    print('')
    print('KSUB_RANDOM2_TEST:')
    print('  Normal end of execution.')


def tuple_next_fast(m, n, rank, base):

    # *****************************************************************************80
    #
    # TUPLE_NEXT_FAST computes the next element of a tuple space, "fast".
    #
    #  Discussion:
    #
    #    The elements are N vectors.  Each entry is constrained to lie
    #    between 1 and M.  The elements are produced one at a time.
    #    The first element is
    #      (1,1,...,1)
    #    and the last element is
    #      (M,M,...,M)
    #    Intermediate elements are produced in lexicographic order.
    #
    #    This code was written as a possibly faster version of TUPLE_NEXT.
    #
    #  Example:
    #
    #    N = 2,
    #    M = 3
    #
    #    INPUT        OUTPUT
    #    -------      -------
    #    Rank          X
    #    ----          ----
    #   -1            -1 -1
    #
    #    0             1  1
    #    1             1  2
    #    2             1  3
    #    3             2  1
    #    4             2  2
    #    5             2  3
    #    6             3  1
    #    7             3  2
    #    8             3  3
    #    9             1  1
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the maximum entry in each component.
    #    M must be greater than 0.
    #
    #    Input, integer N, the number of components.
    #    N must be greater than 0.
    #
    #    Input, integer RANK, indicates the rank of the tuples.
    #    Typically, 0 <= RANK < N^M values greater than this are
    #    legal and meaningful, being equivalent to the corresponding
    #    value mod N^M.  RANK < 0 indicates that this is the first
    #    call for the given values of (M,N).  Initialization is done,
    #    and X is set to a dummy value.
    #
    #    Input/output, integer BASE(N), a bookkeeping array needed by
    #    this procedure.  The user should allocate space for this array, but
    #    should not alter it between successive calls.
    #
    #    Output, integer X(N), the next tuple of the given rank,
    #    or a dummy value if initialization is being done.
    #

    x = np.zeros(n, dtype=np.int32)

    if (rank < 0):

        if (m <= 0):
            print('')
            print('TUPLE_NEXT_FAST - Fatal error!')
            print('  M <= 0 is illegal.')
            print('  M = %d' % (m))
            exit('TUPLE_NEXT_FAST - Fatal error!')

        if (n <= 0):
            print('')
            print('TUPLE_NEXT_FAST - Fatal error!')
            print('  N <= 0 is illegal.')
            print('  N = %d' % (n))
            exit('TUPLE_NEXT_FAST - Fatal error!')

        base[n - 1] = 1
        for i in range(n - 2, -1, -1):
            base[i] = base[i + 1] * m

        for i in range(0, n):
            x[i] = -1

    else:

        for i in range(0, n):
            x[i] = ((rank // base[i]) % m) + 1

    return x, base


def tuple_next_fast_test():

    # *****************************************************************************80
    #
    # TUPLE_NEXT_FAST_TEST tests TUPLE_NEXT_FAST.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 2
    m = 3

    print('')
    print('TUPLE_NEXT_FAST_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TUPLE_NEXT_FAST returns the next "tuple", that is,')
    print('  a vector of N integers, each between 1 and M.')
    print('')
    print('  M = %d' % (m))
    print('  N = %d' % (n))
    print('')

    #
    #  Initialize.
    #
    rank = -1
    base = np.zeros(n)
    x, base = tuple_next_fast(m, n, rank, base)

    rank_max = (m ** n) - 1

    for rank in range(0, rank_max + 1):

        x, base = tuple_next_fast(m, n, rank, base)

        print('%4d  ' % (rank), end='')
        for j in range(0, n):
            print('%10d  ' % (x[j]), end='')
        print('')
    print('')
    print('TUPLE_NEXT_FAST_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    grid_test()
    timestamp()
