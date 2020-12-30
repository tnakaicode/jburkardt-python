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
from prob.r8 import r8_huge
from prob.r8vec import r8vec_mean, r8vec_variance, r8vec_min, r8vec_max
from prob.disk import disk_sample


def dipole_cdf(x, a, b):

    # *****************************************************************************80
    #
    # DIPOLE_CDF evaluates the Dipole CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the CDF.
    #
    #    Input, real A, B, the parameters of the PDF.
    #    A is arbitrary, but represents an angle, so only 0 <= A <= 2 * PI
    #    is interesting, and -1.0 <= B <= 1.0.
    #
    #    Output, real CDF, the value of the CDF.
    #

    cdf = 0.5 + (1.0 / np.pi) * np.arctan(x) + b * b \
        * (x * np.cos(2.0 * a) - np.sin(2.0 * a)) \
        / (np.pi * (1.0 + x * x))

    return cdf


def dipole_cdf_inv(cdf, a, b):

    # *****************************************************************************80
    #
    # DIPOLE_CDF_INV inverts the Dipole CDF.
    #
    #  Discussion:
    #
    #    A simple bisection method is used.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real CDF, the value of the CDF.
    #
    #    Input, real A, B, the parameters of the PDF.
    #    -1.0 <= B <= 1.0.
    #
    #    Output, real X, the corresponding argument of the CDF.
    #

    it_max = 100
    tol = 0.0001
    #
    #  Take care of horrible input.
    #
    if (cdf <= 0.0):
        x = - r8_huge()
        return x
    elif (1.0 <= cdf):
        x = r8_huge()
        return x
    #
    #  Seek X1 < X < X2.
    #
    x1 = -1.0

    while (True):

        cdf1 = dipole_cdf(x1, a, b)

        if (cdf1 <= cdf):
            break

        x1 = 2.0 * x1

    x2 = 1.0

    while (True):

        cdf2 = dipole_cdf(x2, a, b)

        if (cdf <= cdf2):
            break

        x2 = 2.0 * x2
    #
    #  Now use bisection.
    #
    it = 0

    while (True):

        it = it + 1

        x3 = 0.5 * (x1 + x2)
        cdf3 = dipole_cdf(x3, a, b)

        if (abs(cdf3 - cdf) < tol):
            x = x3
            break

        if (it_max < it):
            print('')
            print('DIPOLE_CDF_INV - Fatal error!')
            print('  Iteration limit exceeded.')
            exit('DIPOLE_CDF_INV - Fatal error!')

        if ((cdf3 <= cdf and cdf1 <= cdf) or (cdf <= cdf3 and cdf <= cdf1)):
            x1 = x3
            cdf1 = cdf3
        else:
            x2 = x3
            cdf2 = cdf3

    return x


def dipole_cdf_test():

    # *****************************************************************************80
    #
    # DIPOLE_CDF_TEST tests DIPOLE_CDF, DIPOLE_CDF_INV, DIPOLE_PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('DIPOLE_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DIPOLE_CDF evaluates the Dipole CDF.')
    print('  DIPOLE_CDF_INV inverts the Dipole CDF.')
    print('  DIPOLE_PDF evaluates the Dipole PDF.')

    atest = np.array([0.0, np.pi / 4.0, np.pi / 2.0])
    btest = np.array([1.0, 0.5, 0.0])

    for itest in range(0, 3):

        a = atest[itest]
        b = btest[itest]

        check = dipole_check(a, b)

        if (not check):
            print('')
            print('DIPOLE_CDF_TEST - Fatal error!')
            print('  The parameters are not legal.')
            return

        print('')
        print('  PDF parameter A = %14g' % (a))
        print('  PDF parameter B = %14g' % (b))

        seed = 123456789

        print('')
        print('       X            PDF           CDF            CDF_INV')
        print('')

        for i in range(0, 10):

            x, seed = dipole_sample(a, b, seed)

            pdf = dipole_pdf(x, a, b)

            cdf = dipole_cdf(x, a, b)

            x2 = dipole_cdf_inv(cdf, a, b)

            print(' %14g  %14g  %14g  %14g' % (x, pdf, cdf, x2))

    print('')
    print('DIPOLE_CDF_TEST')
    print('  Normal end of execution.')


def dipole_check(a, b):

    # *****************************************************************************80
    #
    # DIPOLE_CHECK checks the parameters of the Dipole CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, B, the parameters of the PDF.
    #    A is arbitrary, but represents an angle, so only 0 <= A <= 2 * PI
    #    is interesting, and -1.0 <= B <= 1.0.
    #
    #    Output, logical CHECK, is true if the parameters are legal.
    #
    check = True

    if (b < -1.0 or 1.0 < b):
        print('')
        print('DIPOLE_CHECK - Fatal error!')
        print('  -1.0 <= B <= 1.0 is required.')
        print('  The input B = %g' % (b))
        check = False

    return check


def dipole_pdf(x, a, b):

    # *****************************************************************************80
    #
    # DIPOLE_PDF evaluates the Dipole PDF.
    #
    #  Discussion:
    #
    #    PDF(X)(A,B) =
    #        1 / ( PI * ( 1 + X^2 ) )
    #      + B^2 * ( ( 1 - X^2 ) * cos ( 2 * A ) + 2.0 * X * sin ( 2 * A ) )
    #      / ( PI * ( 1 + X )^2 )
    #
    #    Densities of this kind commonly occur in the analysis of resonant
    #    scattering of elementary particles.
    #
    #    DIPOLE_PDF(X)(A,0) = CAUCHY_PDF(X)(A)
    #    A = 0, B = 1 yields the single channel dipole distribution.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Robert Knop,
    #    Algorithm 441,
    #    ACM Transactions on Mathematical Software.
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the PDF.
    #
    #    Input, real A, B, the parameters of the PDF.
    #    A is arbitrary, but represents an angle, so only 0 <= A <= 2 * PI
    #      is interesting,
    #    and -1.0 <= B <= 1.0.
    #
    #    Output, real PDF, the value of the PDF.
    #

    pdf = 1.0 / (np.pi * (1.0 + x * x)) \
        + b * b * ((1.0 - x * x) * np.cos(2.0 * a)
                   + 2.0 * x * np.sin(2.0 * x)) \
        / (np.pi * (1.0 + x * x) * (1.0 + x * x))

    return pdf


def dipole_sample(a, b, seed):

    # *****************************************************************************80
    #
    # DIPOLE_SAMPLE samples the Dipole PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Robert Knop,
    #    Algorithm 441,
    #    ACM Transactions on Mathematical Software.
    #
    #  Parameters:
    #
    #    Input, real A, B, the parameters of the PDF.
    #    A is arbitrary, but represents an angle, so only 0 <= A <= 2 * PI
    #      is interesting,
    #    and -1.0 <= B <= 1.0.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    #
    #  Find (X1,X2) at random in a circle.
    #
    a2 = b * np.sin(a)
    b2 = b * np.cos(a)
    c2 = 1.0

    x1, x2, seed = disk_sample(a2, b2, c2, seed)
    #
    #  The dipole variate is the ratio X1 / X2.
    #
    x = x1 / x2

    return x, seed


def dipole_sample_test():

    # *****************************************************************************80
    #
    # DIPOLE_SAMPLE_TEST tests DIPOLE_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    nsample = 1000
    ntest = 3
    seed = 123456789

    print('')
    print('DIPOLE_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DIPOLE_SAMPLE samples the Dipole distribution.')

    atest = np.array([0.0, np.pi / 4.0, np.pi / 2.0])
    btest = np.array([1.0, 0.5, 0.0])

    for itest in range(0, 3):

        a = atest[itest]
        b = btest[itest]

        check = dipole_check(a, b)

        if (not check):
            print('')
            print('DIPOLE_SAMPLE_TEST - Fatal error!')
            print('  The parameters are not legal.')
            return

        print('')
        print('  PDF parameter A = %14g' % (a))
        print('  PDF parameter B = %14g' % (b))

        x = np.zeros(nsample)

        for i in range(0, nsample):
            x[i], seed = dipole_sample(a, b, seed)

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
    print('DIPOLE_SAMPLE_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    dipole_cdf_test()
    dipole_sample_test()
    timestamp()
