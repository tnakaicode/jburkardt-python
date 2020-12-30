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
from prob.r8 import r8_huge, r8_uniform_01
from prob.r8vec import r8vec_mean, r8vec_variance, r8vec_min, r8vec_max

from i4vec_max import i4vec_max
from i4vec_min import i4vec_min
from i4vec_mean import i4vec_mean
from i4vec_variance import i4vec_variance
from r8_factorial import r8_factorial


def poisson_cdf(x, a):

    # *****************************************************************************80
    #
    # POISSON_CDF evaluates the Poisson CDF.
    #
    #  Discussion:
    #
    #    CDF(X,A) is the probability that the number of events observed
    #    in a unit time period will be no greater than X, given that the
    #    expected number of events in a unit time period is A.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer X, the argument of the CDF.
    #    0 <= X.
    #
    #    Input, real A, the parameter of the PDF.
    #    0.0 < A.
    #
    #    Output, real CDF, the value of the CDF.
    #

    if (x < 0):
        cdf = 0.0

    else:
        next = np.exp(- a)
        sum2 = next

        for i in range(1, x + 1):
            last = next
            next = last * a / float(i)
            sum2 = sum2 + next

        cdf = sum2

    return cdf


def poisson_cdf_inv(cdf, a):

    # *****************************************************************************80
    #
    # POISSON_CDF_INV inverts the Poisson CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real CDF, a value of the CDF.
    #    0 <= CDF < 1.
    #
    #    Input, real A, the parameter of the PDF.
    #    0.0 < A.
    #
    #    Output, integer X, the corresponding argument.
    #

    xmax = 100
    #
    #  Now simply start at X = 0, and find the first value for which
    #  CDF(X-1) <= CDF <= CDF(X).
    #
    sum2 = 0.0

    for i in range(0, xmax + 1):
        sumold = sum2
        if (i == 0):
            next = np.exp(- a)
            sum2 = next
        else:
            last = next
            next = last * a / float(i)
            sum2 = sum2 + next

        if (sumold <= cdf and cdf <= sum2):
            x = i
            return x

    print('')
    print('POISSON_CDF_INV - Warning!')
    print('  Exceeded XMAX = %d' % (xmax))

    x = xmax

    return x


def poisson_cdf_test():

    # *****************************************************************************80
    #
    # POISSON_CDF_TEST tests POISSON_CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('POISSON_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POISSON_CDF evaluates the Poisson CDF,')
    print('  POISSON_CDF_INV inverts the Poisson CDF.')
    print('  POISSON_PDF evaluates the Poisson PDF.')

    a = 10.0
    check = poisson_check(a)

    if (not check):
        print('')
        print('POISSON_CDF_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    print('')
    print('  PDF parameter A =  %14g' % (a))

    seed = 123456789

    print('')
    print('       X            PDF           CDF            CDF_INV')
    print('')

    for i in range(0, 10):
        x, seed = poisson_sample(a, seed)
        pdf = poisson_pdf(x, a)
        cdf = poisson_cdf(x, a)
        x2 = poisson_cdf_inv(cdf, a)
        print('  %14d  %14g  %14g  %14d' % (x, pdf, cdf, x2))

    print('')
    print('POISSON_CDF_TEST')
    print('  Normal end of execution.')


def poisson_check(a):

    # *****************************************************************************80
    #
    # POISSON_CHECK checks the parameter of the Poisson PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 September 2004
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, the parameter of the PDF.
    #    0.0 < A.
    #
    check = True

    if (a <= 0.0):
        print('')
        print('POISSON_CHECK - Fatal error!')
        print('  A <= 0.')
        check = False

    return check


def poisson_mean(a):

    # *****************************************************************************80
    #
    # POISSON_MEAN returns the mean of the Poisson PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, the parameter of the PDF.
    #    0.0 < A.
    #
    #    Output, real MEAN, the mean of the PDF.
    #
    mean = a

    return mean


def poisson_pdf(x, a):

    # *****************************************************************************80
    #
    # POISSON_PDF evaluates the Poisson PDF.
    #
    #  Formula:
    #
    #    PDF(X)(A) = EXP ( - A ) * A^X / X!
    #
    #  Discussion:
    #
    #    PDF(X)(A) is the probability that the number of events observed
    #    in a unit time period will be X, given the expected number
    #    of events in a unit time.
    #
    #    The parameter A is the expected number of events per unit time.
    #
    #    The Poisson PDF is a discrete version of the Exponential PDF.
    #
    #    The time interval between two Poisson events is a random
    #    variable with the Exponential PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer X, the argument of the PDF.
    #    0 <= X
    #
    #    Input, real A, the parameter of the PDF.
    #    0.0 < A.
    #
    #    Output, real PDF, the value of the PDF.
    #

    if (x < 0):
        pdf = 0.0
    else:
        pdf = np.exp(- a) * a ** x / r8_factorial(x)

    return pdf


def poisson_sample(a, seed):

    # *****************************************************************************80
    #
    # POISSON_SAMPLE samples the Poisson PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, the parameter of the PDF.
    #    0.0 < A.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer X, a sample of the PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    cdf, seed = r8_uniform_01(seed)

    x = poisson_cdf_inv(cdf, a)

    return x, seed


def poisson_sample_test():

    # *****************************************************************************80
    #
    # POISSON_SAMPLE_TEST tests POISSON_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    nsample = 1000
    seed = 123456789

    print('')
    print('POISSON_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POISSON_MEAN computes the Poisson mean')
    print('  POISSON_SAMPLE samples the Poisson distribution')
    print('  POISSON_VARIANCE computes the Poisson variance.')

    a = 10.0

    check = poisson_check(a)

    if (not check):
        print('')
        print('POISSON_SAMPLE_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    mean = poisson_mean(a)
    variance = poisson_variance(a)

    print('')
    print('  PDF parameter A =             %14g' % (a))
    print('  PDF mean =                    %14g' % (mean))
    print('  PDF variance =                %14g' % (variance))

    x = np.zeros(nsample)
    for i in range(0, nsample):
        x[i], seed = poisson_sample(a, seed)

    mean = i4vec_mean(nsample, x)
    variance = i4vec_variance(nsample, x)
    xmax = i4vec_max(nsample, x)
    xmin = i4vec_min(nsample, x)

    print('')
    print('  Sample size =     %6d' % (nsample))
    print('  Sample mean =     %14g' % (mean))
    print('  Sample variance = %14g' % (variance))
    print('  Sample maximum =  %6d' % (xmax))
    print('  Sample minimum =  %6d' % (xmin))
    print('')
    print('POISSON_SAMPLE_TEST')
    print('  Normal end of execution.')


def poisson_variance(a):

    # *****************************************************************************80
    #
    # POISSON_VARIANCE returns the variance of the Poisson PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, the parameter of the PDF.
    #    0.0 < A.
    #
    #    Output, real VARIANCE, the variance of the PDF.
    #
    variance = a

    return variance


if (__name__ == '__main__'):
    timestamp()
    poisson_cdf_test()
    poisson_sample_test()
    timestamp()
