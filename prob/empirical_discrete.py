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
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8vec_transpose_print import r8vec_transpose_print
from r8lib.r8mat_transpose_print import r8mat_transpose_print, r8mat_transpose_print_some

from r8lib.r8_huge import r8_huge
from r8lib.r8_gamma import r8_gamma
from r8lib.r8_uniform_ab import r8_uniform_01
from r8lib.r8vec_sum import r8vec_sum
from r8lib.r8vec_min import r8vec_min
from r8lib.r8vec_max import r8vec_max
from r8lib.r8vec_mean import r8vec_mean
from r8lib.r8vec_variance import r8vec_variance
from prob.plot import plot_pnt


def empirical_discrete_cdf(x, a, b, c):

    # *****************************************************************************80
    #
    # EMPIRICAL_DISCRETE_CDF evaluates the Empirical Discrete CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the CDF.
    #
    #    Input, integer A, the number of values.
    #    0 < A.
    #
    #    Input, real B(A), the weights of each value.
    #    0 <= B(1:A) and at least one value is nonzero.
    #
    #    Input, real C(A), the values.
    #    The values must be distinct and in ascending order.
    #
    #    Output, real CDF, the value of the CDF.
    #

    cdf = 0.0
    bsum = np.sum(b)

    for i in range(0, a):
        if (x < c[i]):
            break
        cdf = cdf + b[i] / bsum

    return cdf


def empirical_discrete_cdf_inv(cdf, a, b, c):

    # *****************************************************************************80
    #
    # EMPIRICAL_DISCRETE_CDF_INV inverts the Empirical Discrete CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real CDF, the value of the CDF.
    #    0.0 <= CDF <= 1.0.
    #
    #    Input, integer A, the number of values.
    #    0 < A.
    #
    #    Input, real B(A), the weights of each value.
    #    0 <= B(1:A) and at least one value is nonzero.
    #
    #    Input, real C(A), the values.
    #    The values must be distinct and in ascending order.
    #
    #    Output, real X, the smallest argument whose CDF is greater
    #    than or equal to CDF.
    #

    if (cdf < 0.0 or 1.0 < cdf):
        print('')
        print('EMPIRICAL_DISCRETE_CDF_INV - Fatal error!')
        print('  CDF < 0 or 1 < CDF.')
        exit('EMPIRICAL_DISCRETE_CDF_INV - Fatal error!')

    bsum = np.sum(b)

    x = c[0]
    cdf2 = b[0] / bsum

    for i in range(1, a):

        if (cdf <= cdf2):
            break

        x = c[i]
        cdf2 = cdf2 + b[i] / bsum

    return x


def empirical_discrete_cdf_test():

    # *****************************************************************************80
    #
    # EMPIRICAL_DISCRETE_CDF_TEST tests EMPIRICAL_DISCRETE_CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    a = 6
    b = np.array([1.0, 1.0, 3.0, 2.0, 1.0, 2.0])
    c = np.array([0.0, 1.0, 2.0, 4.5, 6.0, 10.0])

    print('')
    print('EMPIRICAL_DISCRETE_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  EMPIRICAL_DISCRETE_CDF evaluates the Empirical Discrete CDF')
    print('  EMPIRICAL_DISCRETE_CDF_INV inverts the Empirical Discrete CDF.')
    print('  EMPIRICAL_DISCRETE_PDF evaluates the Empirical Discrete PDF')

    check = empirical_discrete_check(a, b, c)

    if (not check):
        print('')
        print('EMPIRICAL_DISCRETE_CDF_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    print('')
    print('  PDF parameter A = %6d' % (a))
    r8vec_print(a, b, '  PDF parameter B:')
    r8vec_print(a, c, '  PDF parameter C:')

    seed = 123456789

    print('')
    print('       X            PDF           CDF            CDF_INV')
    print('')

    for i in range(0, 10):
        x, seed = empirical_discrete_sample(a, b, c, seed)
        pdf = empirical_discrete_pdf(x, a, b, c)
        cdf = empirical_discrete_cdf(x, a, b, c)
        x2 = empirical_discrete_cdf_inv(cdf, a, b, c)
        print(' %14g  %14g  %14g  %14g' % (x, pdf, cdf, x2))
    print('')
    print('EMPIRICAL_DISCRETE_CDF_TEST')
    print('  Normal end of execution.')


def empirical_discrete_check(a, b, c):

    # *****************************************************************************80
    #
    # EMPIRICAL_DISCRETE_CHECK checks the parameters of the Empirical Discrete CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer A, the number of values.
    #    0 < A.
    #
    #    Input, real B(A), the weights of each value.
    #    0 <= B(1:A) and at least one value is nonzero.
    #
    #    Input, real C(A), the values.
    #    The values must be distinct and in ascending order.
    #
    #    Output, logical CHECK, is true if the parameters are legal.
    #

    check = True

    if (a <= 0):
        print('')
        print('EMPIRICAL_DISCRETE_CHECK - Fatal error!')
        print('  A must be positive.')
        print('  Input A = %d' % (a))
        print('  A is the number of weights.')
        check = False

    for i in range(0, a):
        if ((b[i] < 0.0)):
            print('')
            print('EMPIRICAL_DISCRETE_CHECK - Fatal error!')
            print('  Some B(*) < 0.')
            print('  But all B values must be nonnegative.')
            check = False

    if (np.sum(b) == 0):
        print('')
        print('EMPIRICAL_DISCRETE_CHECK - Fatal error!')
        print('  All B(*) = 0.')
        print('  But at least one B values must be nonzero.')
        check = False

    for i in range(0, a):
        for j in range(i + 1, a):
            if (c[i] == c[j]):
                print('')
                print('EMPIRICAL_DISCRETE_CHECK - Fatal error!')
                print('  All values C must be unique.')
                print('  But at least two values are identical.')
                check = False

    for i in range(0, a - 1):
        if (c[i + 1] < c[i]):
            print('')
            print('EMPIRICAL_DISCRETE_CHECK - Fatal error!')
            print('  The values in C must be in ascending order.')
            check = False

    return check


def empirical_discrete_mean(a, b, c):

    # *****************************************************************************80
    #
    # EMPIRICAL_DISCRETE_MEAN returns the mean of the Empirical Discrete PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer A, the number of values.
    #    0 < A.
    #
    #    Input, real B(A), the weights of each value.
    #    0 <= B(1:A) and at least one value is nonzero.
    #
    #    Input, real C(A), the values.
    #    The values must be distinct and in ascending order.
    #
    #    Output, real MEAN, the mean of the PDF.
    #

    mean = np.dot(b, c) / np.sum(b)

    return mean


def empirical_discrete_pdf(x, a, b, c):

    # *****************************************************************************80
    #
    # EMPIRICAL_DISCRETE_PDF evaluates the Empirical Discrete PDF.
    #
    #  Discussion:
    #
    #    A set of A values C(1:A) are assigned nonnegative weights B(1:A),
    #    with at least one B nonzero.  The probability of C(I) is the
    #    value of B(I) divided by the sum of the weights.
    #
    #    The C's must be distinct, and given in ascending order.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the PDF.
    #
    #    Input, integer A, the number of values.
    #    0 < A.
    #
    #    Input, real B(A), the weights of each value.
    #    0 <= B(1:A) and at least one value is nonzero.
    #
    #    Input, real C(A), the values.
    #    The values must be distinct and in ascending order.
    #
    #    Output, real PDF, the value of the PDF.
    #

    pdf = 0.0

    for i in range(0, a):
        if (x == c[i]):
            pdf = b[i] / np.sum(b)
            break

    return pdf


def empirical_discrete_sample(a, b, c, seed):

    # *****************************************************************************80
    #
    # EMPIRICAL_DISCRETE_SAMPLE samples the Empirical Discrete PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer A, the number of values.
    #    0 < A.
    #
    #    Input, real B(A), the weights of each value.
    #    0 <= B(1:A) and at least one value is nonzero.
    #
    #    Input, real C(A), the values.
    #    The values must be distinct and in ascending order.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    cdf, seed = r8_uniform_01(seed)
    x = empirical_discrete_cdf_inv(cdf, a, b, c)
    return x, seed


def empirical_discrete_sample_test():

    # *****************************************************************************80
    #
    # EMPIRICAL_DISCRETE_SAMPLE_TEST tests EMPIRICAL_DISCRETE_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    a = 6
    nsample = 1000

    b = np.array([1.0, 1.0, 3.0, 2.0, 1.0, 2.0])
    c = np.array([0.0, 1.0, 2.0, 4.5, 6.0, 10.0])

    seed = 123456789

    print('')
    print('EMPIRICAL_DISCRETE_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  EMPIRICAL_DISCRETE_MEAN computes the Empirical Discrete mean')
    print('  EMPIRICAL_DISCRETE_SAMPLE samples the Empirical Discrete distribution')
    print('  EMPIRICAL_DISCRETE_VARIANCE computes the Empirical Discrete variance.')

    check = empirical_discrete_check(a, b, c)

    if (not check):
        print('')
        print('EMPIRICAL_DISCRETE_SAMPLE_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    mean = empirical_discrete_mean(a, b, c)
    variance = empirical_discrete_variance(a, b, c)

    print('')
    print('  PDF parameter A = %6d' % (a))
    r8vec_print(a, b, '  PDF parameter B:')
    r8vec_print(a, c, '  PDF parameter C:')
    print('  PDF mean =                    %14g' % (mean))
    print('  PDF variance =                %14g' % (variance))

    x = np.zeros(nsample)
    for i in range(0, nsample):
        x[i], seed = empirical_discrete_sample(a, b, c, seed)

    mean = r8vec_mean(nsample, x)
    variance = r8vec_variance(nsample, x)
    xmax = r8vec_max(nsample, x)
    xmin = r8vec_min(nsample, x)

    print('')
    print('  Sample size =     %6d' % (nsample))
    print('  Sample mean =     %14g' % (mean))
    print('  Sample variance = %14g' % (variance))
    print('  Sample maximum =  %14g' % (xmax))
    print('  Sample minimum =  %14g' % (xmin))
    print('')
    print('EMPIRICAL_DISCRETE_SAMPLE_TEST')
    print('  Normal end of execution.')


def empirical_discrete_variance(a, b, c):

    # *****************************************************************************80
    #
    # EMPIRICAL_DISCRETE_VARIANCE returns the variance of the Empirical Discrete PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer A, the number of values.
    #    0 < A.
    #
    #    Input, real B(A), the weights of each value.
    #    0 <= B(1:A) and at least one value is nonzero.
    #
    #    Input, real C(A), the values.
    #    The values must be distinct and in ascending order.
    #
    #    Output, real VARIANCE, the variance of the PDF.
    #

    bsum = np.sum(b)
    mean = empirical_discrete_mean(a, b, c)
    variance = 0.0
    for i in range(0, a):
        variance = variance + (b[i] / bsum) * (c[i] - mean) ** 2

    return variance


if (__name__ == '__main__'):
    timestamp()
    empirical_discrete_cdf_test()
    empirical_discrete_sample_test()
    timestamp()
