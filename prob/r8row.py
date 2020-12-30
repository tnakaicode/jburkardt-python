#! /usr/bin/env python
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
from prob.r8mat import r8mat_print
from prob.r8vec import r8vec_print


def r8row_max(m, n, x):

    # *****************************************************************************80
    #
    # R8ROW_MAX returns the maximums of rows of an R8ROW.
    #
    #  Discussion:
    #
    #    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
    #    each of length N.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns in the array.
    #
    #    Input, real X(M,N), the R8ROW.
    #
    #    Output, real XMAX(M), the maximums of the rows of X.
    #

    xmax = np.zeros(m)

    for i in range(0, m):
        xmax[i] = x[i, 0]
        for j in range(1, n):
            xmax[i] = max(xmax[i], x[i, j])

    return xmax


def r8row_max_test():

    # *****************************************************************************80
    #
    # R8ROW_MAX_TEST tests R8ROW_MAX
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 3
    n = 4

    print('')
    print('R8ROW_MAX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8ROW_MAX computes maximums of an R8ROW.')

    a = np.zeros([m, n])
    k = 0
    for i in range(0, m):
        for j in range(0, n):
            k = k + 1
            a[i, j] = float(k)

    amax = r8row_max(m, n, a)
    r8mat_print(m, n, a, '  The matrix:')
    r8vec_print(m, amax, '  Row maximums:')

    print('')
    print('R8ROW_MAX_TEST:')
    print('  Normal end of execution.')


def r8row_mean(m, n, a):

    # *****************************************************************************80
    #
    # R8ROW_MEAN returns the means of an R8ROW.
    #
    #  Discussion:
    #
    #    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
    #    each of length N.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns.
    #
    #    Input, real A(M,N), the R8ROW
    #
    #    Output, real ROW_MEAN(M), the row means.
    #

    mean = np.zeros(m)

    for i in range(0, m):
        for j in range(0, n):
            mean[i] = mean[i] + a[i, j]
        mean[i] = mean[i] / float(n)

    return mean


def r8row_mean_test():

    # *****************************************************************************80
    #
    # R8ROW_MEAN_TEST tests R8ROW_MEAN.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 3
    n = 4

    print('')
    print('R8ROW_MEAN_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8ROW_MEAN computes row means of an R8ROW.')

    a = np.zeros([m, n])
    k = 0
    for i in range(0, m):
        for j in range(0, n):
            k = k + 1
            a[i, j] = float(k)

    means = r8row_mean(m, n, a)
    r8mat_print(m, n, a, '  The matrix:')
    r8vec_print(m, means, '  The row means:')

    print('')
    print('R8ROW_MEAN_TEST:')
    print('  Normal end of execution.')


def r8row_min(m, n, x):

    # *****************************************************************************80
    #
    # R8ROW_MIN returns the minimums of rows of an R8ROW.
    #
    #  Discussion:
    #
    #    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
    #    each of length N.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns in the array.
    #
    #    Input, real X(M,N), the R8ROW.
    #
    #    Output, real XMIN(M), the minimums of the rows of X.
    #

    xmin = np.zeros(m)

    for i in range(0, m):
        xmin[i] = x[i, 0]
        for j in range(1, n):
            xmin[i] = min(xmin[i], x[i, j])

    return xmin


def r8row_min_test():

    # *****************************************************************************80
    #
    # R8ROW_MIN_TEST tests R8ROW_MIN
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 3
    n = 4

    print('')
    print('R8ROW_MIN_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8ROW_MIN computes minimums of an R8ROW.')

    a = np.zeros([m, n])
    k = 0
    for i in range(0, m):
        for j in range(0, n):
            k = k + 1
            a[i, j] = float(k)

    amin = r8row_min(m, n, a)
    r8mat_print(m, n, a, '  The matrix:')
    r8vec_print(m, amin, '  Row minimums:')

    print('')
    print('R8ROW_MIN_TEST:')
    print('  Normal end of execution.')


def r8row_variance(m, n, x):

    # *****************************************************************************80
    #
    # R8ROW_VARIANCE returns the variances of an R8ROW.
    #
    #  Discussion:
    #
    #    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
    #    each of length N.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns in the array.
    #
    #    Input, real X(M,N), the R8ROW whose row means are desired.
    #
    #    Output, real VARIANCE(M), the variances of the rows of X.
    #

    variance = np.zeros(m)

    for i in range(0, m):

        mean = 0.0
        for j in range(0, n):
            mean = mean + x[i, j]
        mean = mean / float(n)

        for j in range(0, n):
            variance[i] = variance[i] + (x[i, j] - mean) ** 2

        if (1 < n):
            variance[i] = variance[i] / float(n - 1)
        else:
            variance[i] = 0.0

    return variance


def r8row_variance_test():

    # *****************************************************************************80
    #
    # R8ROW_VARIANCE_TEST tests R8ROW_VARIANCE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 3
    n = 4

    print('')
    print('R8ROW_VARIANCE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8ROW_VARIANCE computes variances of an R8ROW.')

    a = np.zeros([m, n])
    k = 0
    for i in range(0, m):
        for j in range(0, n):
            k = k + 1
            a[i, j] = float(k)

    variance = r8row_variance(m, n, a)
    r8mat_print(m, n, a, '  The matrix:')
    r8vec_print(m, variance, '  The row variances:')

    print('')
    print('R8ROW_VARIANCE_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    r8row_max_test()
    timestamp()
