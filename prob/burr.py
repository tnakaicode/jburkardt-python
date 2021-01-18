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
from r8lib.r8vec_min import r8vec_min
from r8lib.r8vec_max import r8vec_max
from r8lib.r8vec_mean import r8vec_mean
from r8lib.r8vec_variance import r8vec_variance
from prob.plot import plot_pnt


def burr_cdf(x, a, b, c, d):

    # *****************************************************************************80
    #
    # BURR_CDF evaluates the Burr CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the CDF.
    #
    #    Input, real A, B, C, D, the parameters of the PDF.
    #    0 < B,
    #    0 < C.
    #
    #    Output, real CDF, the value of the CDF.
    #
    if (x <= a):

        cdf = 0.0

    else:

        y = (x - a) / b

        cdf = 1.0 - 1.0 / (1.0 + y ** c) ** d

    return cdf


def burr_cdf_inv(cdf, a, b, c, d):

    # *****************************************************************************80
    #
    # BURR_CDF_INV inverts the Burr CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 August 2016
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
    #    Input, real A, B, C, D, the parameters of the PDF.
    #    0 < B,
    #    0 < C.
    #
    #    Output, real X, the corresponding argument.
    #

    if (cdf < 0.0 or 1.0 < cdf):
        
        print('')
        print('BURR_CDF_INV - Fatal error!')
        print('  CDF < 0 or 1 < CDF.')
        exit('BURR_CDF_INV - Fatal error!')

    y = ((1.0 / (1.0 - cdf)) ** (1.0 / d) - 1.0) ** (1.0 / c)
    x = a + b * y

    return x


def burr_cdf_test():

    # *****************************************************************************80
    #
    # BURR_CDF_TEST tests BURR_CDF, BURR_CDF_INV, BURR_PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('BURR_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  BURR_CDF evaluates the Burr CDF')
    print('  BURR_CDF_INV inverts the Burr CDF.')
    print('  BURR_PDF evaluates the Burr PDF')

    a = 1.0
    b = 2.0
    c = 3.0
    d = 2.0
    check = burr_check(a, b, c, d)

    if (not check):
        print('')
        print('BURR_CDF_TEST - Fatal error!')
        print('  The parameters are not legal.')

    print('')
    print('  PDF parameter A = %14g' % (a))
    print('  PDF parameter B = %14g' % (b))
    print('  PDF parameter C = %14g' % (c))
    print('  PDF parameter D = %14g' % (d))

    seed = 123456789

    print('')
    print('       X            PDF           CDF            CDF_INV')
    print('')

    dat = []
    for i in range(0, 10):

        x, seed = burr_sample(a, b, c, d, seed)
        pdf = burr_pdf(x, a, b, c, d)
        cdf = burr_cdf(x, a, b, c, d)
        x2 = burr_cdf_inv(cdf, a, b, c, d)

        print(' %14g  %14g  %14g  %14g' % (x, pdf, cdf, x2))
        dat.append(np.array([x, pdf, cdf, x2]))
    dat = np.array(dat)
    plot_pnt(dat, "burr")

    print('')
    print('BURR_DF_TEST')
    print('  Normal end of execution.')


def burr_check(a, b, c, d):

    # *****************************************************************************80
    #
    # BURR_CHECK checks the parameters of the Burr CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, B, C, D, the parameters of the PDF.
    #    0 < B,
    #    0 < C.
    #
    #    Output, logical CHECK, is TRUE if the parameters are legal.
    #
    check = True

    if (b <= 0.0):
        print('')
        print('BURR_CHECK - Fatal error!')
        print('  B <= 0.')
        check = False

    if (c <= 0):
        print('')
        print('BURR_CHECK - Fatal error!')
        print('  C <= 0.')
        check = False

    return check


def burr_mean(a, b, c, d):

    # *****************************************************************************80
    #
    # BURR_MEAN returns the mean of the Burr PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, B, C, D, the parameters of the PDF.
    #    0 < B,
    #    0 < C.
    #
    #    Output, real MEAN, the mean of the PDF.
    #

    ymean = d * r8_gamma(d - 1.0 / c) \
              * r8_gamma(1.0 + 1.0 / c) \
        / r8_gamma(d + 1.0)

    mean = a + b * ymean

    return mean


def burr_pdf(x, a, b, c, d):

    # *****************************************************************************80
    #
    # BURR_PDF evaluates the Burr PDF.
    #
    #  Discussion:
    #
    #    Y = ( X - A ) / B;
    #
    #    PDF(X)(A,B,C,D) = ( C * D / B ) * Y ^ ( C - 1 ) / ( 1 + Y ^ C ) ^ ( D + 1 )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    M E Johnson,
    #    Multivariate Statistical Simulation,
    #    Wiley, New York, 1987.
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the PDF.
    #    A <= X
    #
    #    Input, real A, B, C, D, the parameters of the PDF.
    #    0 < B,
    #    0 < C.
    #
    #    Output, real PDF, the value of the PDF.
    #
    if (x <= a):

        pdf = 0.0
    else:

        y = (x - a) / b
        pdf = (c * d / b) * y ** (c - 1.0) / (1.0 + y ** c) ** (d + 1.0)

    return pdf


def burr_sample(a, b, c, d, seed):

    # *****************************************************************************80
    #
    # BURR_SAMPLE samples the Burr PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, B, C, D, the parameters of the PDF.
    #    0 < B,
    #    0 < C.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    cdf, seed = r8_uniform_01(seed)
    x = burr_cdf_inv(cdf, a, b, c, d)

    return x, seed


def burr_sample_test():

    # *****************************************************************************80
    #
    # BURR_SAMPLE_TEST tests BURR_MEAN, BURR_VARIANCE, BURR_SAMPLE
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    nsample = 1000
    seed = 123456789

    print('')
    print('BURR_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  BURR_MEAN computes the Burr mean')
    print('  BURR_VARIANCE computes the Burr variance')
    print('  BURR_SAMPLE Burr samples the distribution')

    a = 1.0
    b = 2.0
    c = 3.0
    d = 2.0

    check = burr_check(a, b, c, d)

    if (not check):
        print('')
        print('BURR_SAMPLE_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    mean = burr_mean(a, b, c, d)
    variance = burr_variance(a, b, c, d)

    print('')
    print('  PDF parameter A = %14g' % (a))
    print('  PDF parameter B = %14g' % (b))
    print('  PDF parameter C = %14g' % (c))
    print('  PDF parameter D = %14g' % (d))
    print('  PDF mean =        %14g' % (mean))
    print('  PDF variance =    %14g' % (variance))

    x = np.zeros(nsample)

    for i in range(0, nsample):
        x[i], seed = burr_sample(a, b, c, d, seed)

    mean = r8vec_mean(nsample, x)
    variance = r8vec_variance(nsample, x)
    xmax = r8vec_max(nsample, x)
    xmin = r8vec_min(nsample, x)

    print('')
    print('  Sample size =     %6d' % (nsample))
    print('  Sample mean =     %14f' % (mean))
    print('  Sample variance = %14f' % (variance))
    print('  Sample maximum =  %14f' % (xmax))
    print('  Sample minimum =  %14f' % (xmin))
    print('')
    print('BURR_SAMPLE_TEST')
    print('  Normal end of execution.')


def burr_variance(a, b, c, d):

    # *****************************************************************************80
    #
    # BURR_VARIANCE returns the variance of the Burr PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, B, C, D, the parameters of the PDF.
    #    0 < B,
    #    0 < C.
    #
    #    Output, real VARIANCE, the variance of the PDF.
    #

    if (c <= 2.0):

        print('')
        print('BURR_VARIANCE - Warning!')
        print('  Variance undefined for C <= 2.')
        variance = r8_huge()
    else:

        mu1 = b * d * r8_gamma((c * d - 1.0) / c) \
            * r8_gamma((c + 1.0) / c) \
            / r8_gamma((c * d + c) / c)

        mu2 = b * b * d * r8_gamma((c * d - 2.0) / c) \
                        * r8_gamma((c + 2.0) / c) \
            / r8_gamma((c * d + c) / c)

        variance = - mu1 * mu1 + mu2
    return variance


if (__name__ == '__main__'):
    timestamp()
    burr_cdf_test()
    burr_sample_test()
    timestamp()
