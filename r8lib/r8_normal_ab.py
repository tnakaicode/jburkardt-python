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

from r8lib.r8_uniform_ab import r8_uniform_01


def r8_normal_01(seed):

    # *****************************************************************************80
    #
    # R8_NORMAL_01 samples the standard normal probability distribution.
    #
    #  Discussion:
    #
    #    The standard normal probability distribution function (PDF) has
    #    mean 0 and standard deviation 1.
    #
    #    The Box-Muller method is used.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the standard normal PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    r1, seed = r8_uniform_01(seed)
    r2, seed = r8_uniform_01(seed)

    x = np.sqrt(- 2.0 * np.log(r1)) * np.cos(2.0 * np.pi * r2)

    return x, seed


def r8_normal_01_test():

    # *****************************************************************************80
    #
    # R8_NORMAL_01_TEST tests R8_NORMAL_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    seed = 123456789
    test_num = 20

    print('')
    print('R8_NORMAL_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_NORMAL_01 generates normally distributed')
    print('  random values.')
    print('  Using initial random number seed = %d' % (seed))
    print('')

    for test in range(0, test_num):

        x, seed = r8_normal_01(seed)
        print('  %f' % (x))

    print('')
    print('R8_NORMAL_01_TEST')
    print('  Normal end of execution.')


def r8_normal_ab(a, b, seed):

    # *****************************************************************************80
    #
    # R8_NORMAL_AB returns a scaled pseudonormal R8.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, the mean of the normal PDF.
    #
    #    Input, real B, the standard deviation of the normal PDF.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the standard normal PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    x, seed = r8_normal_01(seed)
    x = a + b * x

    return x, seed


def r8_normal_ab_test():

    # *****************************************************************************80
    #
    # R8_NORMAL_AB_TEST tests R8_NORMAL_AB.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    x_mean = 100.0
    x_std = 10.0
    seed = 123456789
    test_num = 20

    print('')
    print('R8_NORMAL_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_NORMAL_AB generates normally distributed values')
    print('  with given mean and standard deviation.')
    print('  Using initial random number seed = %d' % (seed))
    print('  MEAN = %g' % (x_mean))
    print('  STD = %g' % (x_std))
    print('')

    for test in range(0, test_num):

        x, seed = r8_normal_ab(x_mean, x_std, seed)
        print('  %g' % (x))

    print('')
    print('R8_NORMAL_AB_TEST')
    print('  Normal end of execution.')


def r8vec_normal_01(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_01 returns a unit pseudonormal R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(N), the vector of pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    x = np.zeros(n)

    for i in range(0, n):
        x[i], seed = r8_normal_01(seed)

    return x, seed


def r8vec_normal_01_test():

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_01_TEST tests R8VEC_NORMAL_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10
    seed = 123456789

    print('')
    print('R8VEC_NORMAL_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_NORMAL_01 returns a vector of Normal 01 values')
    print('')
    print('  SEED = %d' % (seed))

    r, seed = r8vec_normal_01(n, seed)
    r8vec_print(n, r, '  Vector:')

    print('')
    print('R8VEC_NORMAL_01_TEST:')
    print('  Normal end of execution.')


def r8vec_normal_ab(n, mu, sigma, seed):

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_AB returns a scaled pseudonormal R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real MU, the average value of the PDF.
    #
    #    Input, real SIGMA, the standard deviation of the PDF.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(N), the vector of pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    x = np.zeros(n)

    for i in range(0, n):
        xi, seed = r8_normal_01(seed)
        x[i] = mu + sigma * xi

    return x, seed


def r8vec_normal_ab_test():

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_AB_TEST tests R8VEC_NORMAL_AB.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8VEC_NORMAL_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_NORMAL_AB returns a vector of Normal AB values')

    n = 10
    mu = 15.0
    sigma = 0.25
    seed = 123456789

    print('')
    print('  Mean = %g' % (mu))
    print('  Standard deviation = %g' % (sigma))
    print('  SEED = %d' % (seed))

    r, seed = r8vec_normal_ab(n, mu, sigma, seed)
    r8vec_print(n, r, '  Vector:')

    print('')
    print('R8VEC_NORMAL_AB_TEST:')
    print('  Normal end of execution.')


def r8mat_normal_01(m, n, seed):

    # *****************************************************************************80
    #
    # R8MAT_NORMAL_01 returns a unit pseudonormal R8MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(M,N), the pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    x = np.zeros((m, n))

    for i in range(0, m):
        for j in range(0, n):
            x[i, j], seed = r8_normal_01(seed)

    return x, seed


def r8mat_normal_01_test():

    # *****************************************************************************80
    #
    # R8MAT_NORMAL_01_TEST tests R8MAT_NORMAL_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 5
    n = 4
    seed = 123456789

    print('')
    print('R8MAT_NORMAL_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_NORMAL_01 returns a matrix of Normal 01 values')
    print('')
    print('  SEED = %d' % (seed))

    r, seed = r8mat_normal_01(m, n, seed)
    r8mat_print(m, n, r, '  Matrix:')

    print('')
    print('R8MAT_NORMAL_01_TEST:')
    print('  Normal end of execution.')


def r8mat_normal_ab(m, n, mu, sigma, seed):

    # *****************************************************************************80
    #
    # R8MAT_NORMAL_AB returns a scaled pseudonormal R8MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns.
    #
    #    Input, real MU, SIGMA, the mean and standard deviation.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(M,N), the pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    x = np.zeros((m, n))

    for i in range(0, m):
        for j in range(0, n):
            xi, seed = r8_normal_01(seed)
            x[i, j] = mu + sigma * xi

    return x, seed


def r8mat_normal_ab_test():

    # *****************************************************************************80
    #
    # R8MAT_NORMAL_AB_TEST tests R8MAT_NORMAL_AB.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8MAT_NORMAL_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_NORMAL_AB returns a matrix of Normal AB values')

    m = 5
    n = 4
    mu = 100.0
    sigma = 5.0
    seed = 123456789

    print('')
    print('  Mean = %g' % (mu))
    print('  Standard deviation = %g' % (sigma))
    print('  SEED = %d' % (seed))

    r, seed = r8mat_normal_ab(m, n, mu, sigma, seed)
    r8mat_print(m, n, r, '  Matrix:')

    print('')
    print('R8MAT_NORMAL_AB_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    r8_normal_01_test()
    r8_normal_ab_test()
    r8vec_normal_01_test()
    r8vec_normal_ab_test()
    r8mat_normal_01_test()
    r8mat_normal_ab_test()
    timestamp()
