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


def cardioid_cdf(x, a, b):

    # *****************************************************************************80
    #
    # CARDIOID_CDF evaluates the Cardioid CDF.
    #
    #  Discussion:
    #
    #    The angle X is assumed to lie between A - PI and A + PI.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the PDF.
    #
    #    Input, real A, B, the parameters of the PDF.
    #    0.0 <= B <= 0.5.
    #
    #    Output, real CDF, the value of the PDF.
    #
    import numpy as np

    if (x <= a - np.pi):
        cdf = 0.0
    elif (x < a + np.pi):
        cdf = (np.pi + x - a + 2.0 * b * np.sin(x - a)) / (2.0 * np.pi)
    else:
        cdf = 1.0

    return cdf


def cardioid_cdf_inv(cdf, a, b):

    # *****************************************************************************80
    #
    # CARDIOID_CDF_INV inverts the Cardioid CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real CDF, the value of the CDF.
    #    0 <= CDF <= 1.
    #
    #    Input, real A, B, the parameters.
    #    0.0 <= B <= 0.5.
    #
    #    Output, real X, the argument with the given CDF.
    #    A - PI <= X <= A + PI.
    #

    tol = 0.000001

    if (cdf <= 0.0):
        x = a - np.pi
    elif (cdf < 1.0):
        x = a
        it = 0
        while (True):

            fx = cdf - (np.pi + x - a + 2.0 * b *
                        np.sin(x - a)) / (2.0 * np.pi)

            if (abs(fx) < tol):
                break

            if (10 < it):
                exit('CARDIOID_CDF_INV - Too many iterations!')

            fp = - (1.0 + 2.0 * b * np.cos(x - a)) / (2.0 * np.pi)

            x = x - fx / fp
            x = max(x, a - np.pi)
            x = min(x, a + np.pi)

            it = it + 1

    else:
        x = a + np.pi

    return x


def cardioid_cdf_test():

    # *****************************************************************************80
    #
    # CARDIOID_CDF_TEST tests CARDIOID_CDF, CARDIOID_CDF_INV and CARDIOID_PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    a = 0.0
    b = 0.25
    seed = 123456789

    print('')
    print('CARDIOID_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CARDIOID_CDF evaluates the Cardioid CDF')
    print('  CARDIOID_CDF_INV inverts the Cardioid CDF.')
    print('  CARDIOID_PDF evaluates the Cardioid PDF')

    print('')
    print('  PDF parameter A = %g' % (a))
    print('  PDF parameter B = %g' % (b))

    if (not cardioid_check(a, b)):
        print('')
        print('CARDIOID_CDF_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    print('')
    print('       X            PDF           CDF            CDF_INV')
    print('')

    dat = []
    for i in range(0, 10):

        x, seed = cardioid_sample(a, b, seed)
        pdf = cardioid_pdf(x, a, b)
        cdf = cardioid_cdf(x, a, b)
        x2 = cardioid_cdf_inv(cdf, a, b)

        print('  %12g  %12g  %12g  %12g' % (x, pdf, cdf, x2))
        dat.append(np.array([x, pdf, cdf, x2]))
    dat = np.array(dat)
    plot_pnt(dat, "cardioid")

    print('')
    print('CARDIOID_CDF_TEST')
    print('  Normal end of execution.')


def cardioid_check(a, b):

    # *****************************************************************************80
    #
    # CARDIOID_CHECK checks the parameters of the Cardioid CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, B, the parameters of the PDF.
    #    -0.5 <= B <= 0.5.
    #
    #    Output, logical CHECK, is true if the parameters are legal.
    #
    check = True

    if (b < -0.5 or 0.5 < b):
        print('')
        print('CARDIOID_CHECK - Fatal error!')
        print('  B < -0.5 or 0.5 < B.')
        check = False

    return check


def cardioid_mean(a, b):

    # *****************************************************************************80
    #
    # CARDIOID_MEAN returns the mean of the Cardioid PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, B, the parameters of the PDF.
    #    0.0 <= B <= 0.5.
    #
    #    Output, real MEAN, the mean of the PDF.
    #
    mean = a

    return mean


def cardioid_pdf(x, a, b):

    # *****************************************************************************80
    #
    # CARDIOID_PDF evaluates the Cardioid PDF.
    #
    #  Discussion:
    #
    #    The cardioid PDF can be thought of as being applied to points on
    #    a circle.  Compare this distribution with the "Cosine PDF".
    #
    #    PDF(A,BX) = ( 1 / ( 2 * PI ) ) * ( 1 + 2 * B * COS ( X - A ) )
    #    for 0 <= B <= 1/2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    N I Fisher,
    #    Statistical Analysis of Circular Data,
    #    Cambridge, 1993.
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the PDF.
    #
    #    Input, real A, B, the parameters of the PDF.
    #    0.0 <= B <= 0.5.
    #
    #    Output, real PDF, the value of the PDF.
    #

    pdf = (1.0 + 2.0 * b * np.cos(x - a)) / (2.0 * np.pi)

    return pdf


def cardioid_sample(a, b, seed):

    # *****************************************************************************80
    #
    # CARDIOID_SAMPLE samples the Cardioid PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, B, the parameters of the PDF.
    #    0.0 <= B <= 0.5.
    #
    #    Input/output, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the PDF.
    #    A - PI <= X <= A + PI.
    #

    cdf, seed = r8_uniform_01(seed)
    x = cardioid_cdf_inv(cdf, a, b)

    return x, seed


def cardioid_sample_test():

    # *****************************************************************************80
    #
    # CARDIOID_SAMPLE_TEST tests CARDIOID_MEAN, CARDIOID_SAMPLE, CARDIOID_VARIANCE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    sample_num = 1000

    a = 0.0
    b = 0.25
    seed = 123456789

    print('')
    print('CARDIOID_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CARDIOID_MEAN computes the Cardioid mean')
    print('  CARDIOID_SAMPLE samples the Cardioid distribution')
    print('  CARDIOID_VARIANCE computes the Cardioid variance.')

    print('')
    print('  PDF parameter A = %g' % (a))
    print('  PDF parameter B = %g' % (b))

    if (not cardioid_check(a, b)):
        print('')
        print('CARDIOID_SAMPLE_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    mean = cardioid_mean(a, b)
    variance = cardioid_variance(a, b)

    print('')
    print('  PDF mean =                    %g' % (mean))
    print('  PDF variance =                %g' % (variance))

    x = np.zeros(sample_num)
    for i in range(0, sample_num):
        x[i], seed = cardioid_sample(a, b, seed)

    mean = r8vec_mean(sample_num, x)
    variance = r8vec_variance(sample_num, x)
    xmax = r8vec_max(sample_num, x)
    xmin = r8vec_min(sample_num, x)

    print('')
    print('  Sample size =     %6d' % (sample_num))
    print('  Sample mean =     %14g' % (mean))
    print('  Sample variance = %14g' % (variance))
    print('  Sample maximum =  %14g' % (xmax))
    print('  Sample minimum =  %14g' % (xmin))
    print('')
    print('CARDIOID_SAMPLE_TEST')
    print('  Normal end of execution.')


def cardioid_variance(a, b):

    # *****************************************************************************80
    #
    # CARDIOID_VARIANCE returns the variance of the Cardioid PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, B, the parameters of the PDF.
    #    0.0 <= B <= 0.5.
    #
    #    Output, real VARIANCE, the variance of the PDF.
    #
    variance = a

    return variance


if (__name__ == '__main__'):
    timestamp()
    cardioid_cdf_test()
    cardioid_sample_test()
    timestamp()
