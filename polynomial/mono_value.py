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

from i4lib.i4_uniform_ab import i4_uniform_ab
from polynomial.mono_print import mono_print
from polynomial.mono_upto_enum import mono_upto_enum
from polynomial.mono_rank_grlex import mono_unrank_grlex


def mono_value(m, n, f, x):

    # *****************************************************************************80
    #
    # MONO_VALUE evaluates a monomial.
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
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, integer F[M], the exponents of the monomial.
    #
    #    Input, real X[M*N], the coordinates of the evaluation points.
    #
    #    Output, real MONO_VALUE[N], the value of the monomial at X.
    #

    v = np.zeros(n, dtype=np.float64)

    for j in range(0, n):
        v[j] = 1.0
        for i in range(0, m):
            v[j] = v[j] * (x[i + j * m] ** f[i])

    return v


def mono_value_test():

    # *****************************************************************************80
    #
    # MONO_VALUE_TEST tests MONO_VALUE.
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
    nx = 2
    x = np.array([1.0, 2.0, 3.0, -2.0, 4.0, 1.0], dtype=np.float64)

    print('')
    print('MONO_VALUE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MONO_VALUE evaluates a monomial.')

    n = 6

    print('')
    print('  Let M = %d' % (m))
    print('      N = %d' % (n))

    seed = 123456789
    test_num = 5

    for test in range(0, test_num):
        f, rank, seed = mono_upto_random(m, n, seed)
        print('')
        mono_print(m, f, '  M(X) = ')
        v = mono_value(m, nx, f, x)
        for j in range(0, nx):
            print('  M(%g,%g,%g) = %g' %
                  (x[0 + j * m], x[1 + j * m], x[2 + j * m], v[j]))

    print('')
    print('MONO_VALUE_TEST:')
    print('  Normal end of execution.')


def mono_upto_random(m, n, seed):

    # *****************************************************************************80
    #
    # MONO_UPTO_RANDOM: random monomial with total degree less than or equal to N.
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
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the degree.
    #    0 <= N.
    #
    #    Input, integer SEED, the random number seed.
    #
    #    Output, integer X[M], the random monomial.
    #
    #    Output, integer RANK, the rank of the monomial.
    #
    #    Output, integer SEED, the random number seed.
    #

    rank_min = 1
    rank_max = mono_upto_enum(m, n)
    rank, seed = i4_uniform_ab(rank_min, rank_max, seed)
    x = mono_unrank_grlex(m, rank)

    return x, rank, seed


def mono_upto_random_test():

    # *****************************************************************************80
    #
    # MONO_UPTO_RANDOM_TEST tests MONO_UPTO_RANDOM.
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
    print('MONO_UPTO_RANDOM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MONO_UPTO_RANDOM selects at random a monomial')
    print('  in M dimensions of total degree no greater than N.')

    n = 4

    print('')
    print('  Let M = %d' % (m))
    print('      N = %d' % (n))
    print('')

    seed = 123456789
    test_num = 5

    for test in range(0, test_num):
        x, rank, seed = mono_upto_random(m, n, seed)
        print('  %2d    ' % (rank)),
        for j in range(0, m):
            print('%2d' % (x[j])),
        print('')
    print('')
    print('MONO_UPTO_RANDOM_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    mono_value_test()
    timestamp()
