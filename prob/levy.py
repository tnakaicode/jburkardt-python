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


def levy_cdf(x, a, b):

    # *****************************************************************************80
    #
    # LEVY_CDF evaluates the Levy CDF.
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
    #  Parameters:
    #
    #    Input, real X, the argument of the CDF.
    #    Normally, A <= X.
    #
    #    Input, real A, B, the parameters of the PDF.
    #    0 < B.
    #
    #    Output, real CDF, the value of the PDF.
    #
    from r8_erf import r8_erf

    if (b <= 0.0):
        print('')
        print('  LEVY_PDF - Fatal error!')
        print('  Input parameter B <= 0.0')
        exit('LEVY_PDF - Fatal error!')

    if (x <= a):
        cdf = 0.0
    else:
        cdf = 1.0 - r8_erf(np.sqrt(b / (2.0 * (x - a))))

    return cdf


def levy_cdf_inv(cdf, a, b):

    # *****************************************************************************80
    #
    # LEVY_CDF_INV inverts the Levy CDF.
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
    #  Parameters:
    #
    #    Input, real CDF, the value of the CDF.
    #    0.0 <= CDF <= 1.0.
    #
    #    Input, real A, B, the parameters of the PDF.
    #    0 < B.
    #
    #    Output, real X, the corresponding argument.
    #
    from normal_01 import normal_01_cdf_inv

    if (cdf < 0.0 or 1.0 < cdf):
        print('')
        print('LEVY_CDF_INV - Fatal error!')
        print('  CDF < 0 or 1 < CDF.')
        exit('LEVY_CDF_INV - Fatal error!')

    if (b <= 0.0):
        print('')
        print('LEVY_CDF_INV - Fatal error!')
        print('  Input parameter B <= 0.0')
        exit('LEVY_CDF_INV - Fatal error!')

    cdf1 = 1.0 - 0.5 * cdf
    x1 = normal_01_cdf_inv(cdf1)
    x = a + b / (x1 * x1)

    return x


def levy_cdf_test():

    # *****************************************************************************80
    #
    # LEVY_CDF_TEST tests LEVY_CDF.
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

    print('')
    print('LEVY_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  LEVY_CDF evaluates the Levy CDF')
    print('  LEVY_CDF_INV inverts the Levy CDF.')
    print('  LEVY_PDF evaluates the Levy PDF')

    a = 1.0
    b = 2.0

    print('')
    print('  PDF parameter A =             %14g' % (a))
    print('  PDF parameter B =             %14g' % (b))

    seed = 123456789

    print('')
    print('       X            PDF           CDF            CDF_INV')
    print('')

    for i in range(0, 10):

        x, seed = levy_sample(a, b, seed)

        pdf = levy_pdf(x, a, b)

        cdf = levy_cdf(x, a, b)

        x2 = levy_cdf_inv(cdf, a, b)

        print(' %14g  %14g  %14g  %14g' % (x, pdf, cdf, x2))

    print('')
    print('LEVY_CDF_TEST')
    print('  Normal end of execution.')


def levy_pdf(x, a, b):

    # *****************************************************************************80
    #
    # LEVY_PDF evaluates the Levy PDF.
    #
    #  Discussion:
    #
    #    PDF(A,BX) = sqrt ( B / ( 2 * PI ) )
    #               * exp ( - B / ( 2 * ( X - A ) )
    #               / ( X - A )^(3/2)
    #
    #    for A <= X.
    #
    #    Note that the Levy PDF does not have a finite mean or variance.
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
    #  Parameters:
    #
    #    Input, real X, the argument of the PDF.
    #    Normally, A <= X.
    #
    #    Input, real A, B, the parameters of the PDF.
    #    0 < B.
    #
    #    Output, real PDF, the value of the PDF.
    #

    if (b <= 0.0):
        print('')
        print('  LEVY_PDF - Fatal error!')
        print('  Input parameter B <= 0.0')
        exit('LEVY_PDF - Fatal error!')

    if (x < a):
        pdf = 0.0
    else:
        pdf = np.sqrt(b / (2.0 * np.pi)) \
            * np.exp(- b / (2.0 * (x - a))) \
            / np.sqrt((x - a) ** 3)

    return pdf


def levy_sample(a, b, seed):

    # *****************************************************************************80
    #
    # LEVY_SAMPLE samples the Levy PDF.
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
    #  Parameters:
    #
    #    Input, real A, B, the parameters of the PDF.
    #    0.0 < B.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the PDF.
    #
    #    Output, integer SEED, a seed for the random number generator.
    #

    cdf, seed = r8_uniform_01(seed)

    x = levy_cdf_inv(cdf, a, b)

    return x, seed


if (__name__ == '__main__'):
    timestamp()
    levy_cdf_test()
    timestamp()
