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
from prob.r8 import r8_huge, r8_uniform_01
from prob.r8vec import r8vec_mean, r8vec_variance, r8vec_min, r8vec_max


def rayleigh_cdf(x, a):

    # *****************************************************************************80
    #
    # RAYLEIGH_CDF evaluates the Rayleigh CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the CDF.
    #    0.0 <= X.
    #
    #    Input, real A, the parameter of the PDF.
    #    0.0 < A.
    #
    #    Output, real CDF, the value of the CDF.
    #

    if (x < 0.0):
        cdf = 0.0
    else:
        cdf = 1.0 - np.exp(- x * x / (2.0 * a * a))

    return cdf


def rayleigh_cdf_inv(cdf, a):

    # *****************************************************************************80
    #
    # RAYLEIGH_CDF_INV inverts the Rayleigh CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2016
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
    #    Input, real A, the parameter of the PDF.
    #    0.0 < A.
    #
    #    Output, real X, the corresponding argument.
    #

    if (cdf < 0.0 or 1.0 < cdf):
        print('')
        print('RAYLEIGH_CDF_INV - Fatal error!')
        print('  CDF < 0 or 1 < CDF.')
        exit('RAYLEIGH_CDF_INV - Fatal error!')

    x = np.sqrt(- 2.0 * a * a * np.log(1.0 - cdf))

    return x


def rayleigh_cdf_test():

    # *****************************************************************************80
    #
    # RAYLEIGH_CDF_TEST tests RAYLEIGH_CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('RAYLEIGH_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RAYLEIGH_CDF evaluates the Rayleigh CDF')
    print('  RAYLEIGH_CDF_INV inverts the Rayleigh CDF.')
    print('  RAYLEIGH_PDF evaluates the Rayleigh PDF')

    a = 2.0
    check = rayleigh_check(a)

    if (not check):
        print('')
        print('RAYLEIGH_CDF_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    print('')
    print('  PDF parameter A =             %14g' % (a))

    seed = 123456789

    print('')
    print('       X            PDF           CDF            CDF_INV')
    print('')

    for i in range(0, 10):
        x, seed = rayleigh_sample(a, seed)
        pdf = rayleigh_pdf(x, a)
        cdf = rayleigh_cdf(x, a)
        x2 = rayleigh_cdf_inv(cdf, a)

        print(' %14g  %14g  %14g  %14g' % (x, pdf, cdf, x2))

    print('')
    print('RAYLEIGH_CDF_TEST')
    print('  Normal end of execution.')


def rayleigh_check(a):

    # *****************************************************************************80
    #
    # RAYLEIGH_CHECK checks the parameter of the Rayleigh PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2016
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
    #    Output, logical CHECK, is true if the parameters are legal.
    #
    check = True

    if (a <= 0.0):
        print('')
        print('RAYLEIGH_CHECK - Fatal error!')
        print('  A <= 0.')
        check = False

    return check


def rayleigh_mean(a):

    # *****************************************************************************80
    #
    # RAYLEIGH_MEAN returns the mean of the Rayleigh PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2016
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

    mean = a * np.sqrt(0.5 * np.pi)

    return mean


def rayleigh_pdf(x, a):

    # *****************************************************************************80
    #
    # RAYLEIGH_PDF evaluates the Rayleigh PDF.
    #
    #  Formula:
    #
    #    PDF(X)(A) = ( X / A^2 ) * EXP ( - X^2 / ( 2 * A^2 ) )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the PDF.
    #    0.0 <= X
    #
    #    Input, real A, the parameter of the PDF.
    #    0 < A.
    #
    #    Output, real PDF, the value of the PDF.
    #

    if (x < 0.0):
        pdf = 0.0
    else:
        pdf = (x / (a * a)) * np.exp(- x * x / (2.0 * a * a))

    return pdf


def rayleigh_sample(a, seed):

    # *****************************************************************************80
    #
    # RAYLEIGH_SAMPLE samples the Rayleigh PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2016
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
    #    Output, real X, a sample of the PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    cdf, seed = r8_uniform_01(seed)

    x = rayleigh_cdf_inv(cdf, a)

    return x, seed


def rayleigh_sample_test():

    # *****************************************************************************80
    #
    # RAYLEIGH_SAMPLE_TEST tests RAYLEIGH_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    nsample = 1000
    seed = 123456789

    print('')
    print('RAYLEIGH_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RAYLEIGH_MEAN computes the Rayleigh mean')
    print('  RAYLEIGH_SAMPLE samples the Rayleigh distribution')
    print('  RAYLEIGH_VARIANCE computes the Rayleigh variance.')

    a = 2.0
    check = rayleigh_check(a)

    if (not check):
        print('')
        print('RAYLEIGH_SAMPLE_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    mean = rayleigh_mean(a)
    variance = rayleigh_variance(a)

    print('')
    print('  PDF parameter A =             %14g' % (a))
    print('  PDF mean =                    %14g' % (mean))
    print('  PDF variance =                %14g' % (variance))

    x = np.zeros(nsample)
    for i in range(0, nsample):
        x[i], seed = rayleigh_sample(a, seed)

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
    print('RAYLEIGH_SAMPLE_TEST')
    print('  Normal end of execution.')


def rayleigh_variance(a):

    # *****************************************************************************80
    #
    # RAYLEIGH_VARIANCE returns the variance of the Rayleigh PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, the parameters of the PDF.
    #    0.0 < A.
    #
    #    Output, real VARIANCE, the variance of the PDF.
    #

    variance = 2.0 * a * a * (1.0 - 0.25 * np.pi)

    return variance


if (__name__ == '__main__'):
    timestamp()
    rayleigh_cdf_test()
    rayleigh_sample_test()
    timestamp()
