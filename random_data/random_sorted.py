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


def normal_01_cdf(x):

    # *****************************************************************************80
    #
    # NORMAL_01_CDF evaluates the Normal 01 CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    A G Adams,
    #    Areas Under the Normal Curve,
    #    Algorithm 39,
    #    Computer j.,
    #    Volume 12, pages 197-198, 1969.
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the CDF.
    #
    #    Output, real CDF, the value of the CDF.
    #

    a1 = 0.398942280444E+00
    a2 = 0.399903438504E+00
    a3 = 5.75885480458E+00
    a4 = 29.8213557808E+00
    a5 = 2.62433121679E+00
    a6 = 48.6959930692E+00
    a7 = 5.92885724438E+00
    b0 = 0.398942280385E+00
    b1 = 3.8052E-08
    b2 = 1.00000615302E+00
    b3 = 3.98064794E-04
    b4 = 1.98615381364E+00
    b5 = 0.151679116635E+00
    b6 = 5.29330324926E+00
    b7 = 4.8385912808E+00
    b8 = 15.1508972451E+00
    b9 = 0.742380924027E+00
    b10 = 30.789933034E+00
    b11 = 3.99019417011E+00
    #
    #  |X| <= 1.28.
    #
    if (abs(x) <= 1.28):

        y = 0.5 * x * x

        q = 0.5 - abs(x) * (a1 - a2 * y / (y + a3
                                           - a4 / (y + a5
                                                   + a6 / (y + a7))))
    #
    #  1.28 < |X| <= 12.7
    #
    elif (abs(x) <= 12.7):

        y = 0.5 * x * x

        q = np.exp(- y) \
            * b0 / (abs(x) - b1
                    + b2 / (abs(x) + b3
                            + b4 / (abs(x) - b5
                                    + b6 / (abs(x) + b7
                                            - b8 / (abs(x) + b9
                                                    + b10 / (abs(x) + b11))))))
    #
    #  12.7 < |X|
    #
    else:

        q = 0.0

    #
    #  Take account of negative X.
    #
    if (x < 0.0):
        cdf = q
    else:
        cdf = 1.0 - q

    return cdf


def normal_01_cdf_test():

    # *****************************************************************************80
    #
    # NORMAL_01_CDF_TEST tests NORMAL_01_CDF, NORMAL_01_CDF_INV, NORMAL_01_PDF
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('NORMAL_01_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  NORMAL_01_CDF evaluates the Normal 01 CDF')
    print('  NORMAL_01_CDF_INV inverts the Normal 01 CDF.')
    print('  NORMAL_01_PDF evaluates the Normal 01 PDF')
    print('')
    print('       X            PDF           CDF            CDF_INV')
    print('')

    seed = 123456789
    for i in range(0, 10):
        x, seed = normal_01_sample(seed)
        pdf = normal_01_pdf(x)
        cdf = normal_01_cdf(x)
        x2 = normal_01_cdf_inv(cdf)
        print(' %14g  %14g  %14g  %14g' % (x, pdf, cdf, x2))

    print('')
    print('NORMAL_01_CDF_TEST')
    print('  Normal end of execution.')


def normal_01_cdf_inv(p):

    # *****************************************************************************80
    #
    # NORMAL_01_CDF_INV inverts the standard normal CDF.
    #
    #  Discussion:
    #
    #    The result is accurate to about 1 part in 10^16.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2016
    #
    #  Author:
    #
    #    Original FORTRAN77 version by Michael Wichura.
    #    Python version by John Burkardt.
    #
    #  Reference:
    #
    #    Michael Wichura,
    #    The Percentage Points of the Normal Distribution,
    #    Algorithm AS 241,
    #    Applied Statistics,
    #    Volume 37, Number 3, pages 477-484, 1988.
    #
    #  Parameters:
    #
    #    Input, real P, the value of the cumulative probability
    #    densitity function.  0 < P < 1.  If P is not in this range, an "infinite"
    #    result is returned.
    #
    #    Output, real VALUE, the normal deviate value with the
    #    property that the probability of a standard normal deviate being
    #    less than or equal to the value is P.
    #

    a = np.array([
        3.3871328727963666080,
        1.3314166789178437745e+2,
        1.9715909503065514427e+3,
        1.3731693765509461125e+4,
        4.5921953931549871457e+4,
        6.7265770927008700853e+4,
        3.3430575583588128105e+4,
        2.5090809287301226727e+3])

    b = np.array([
        1.0,
        4.2313330701600911252e+1,
        6.8718700749205790830e+2,
        5.3941960214247511077e+3,
        2.1213794301586595867e+4,
        3.9307895800092710610e+4,
        2.8729085735721942674e+4,
        5.2264952788528545610e+3])

    c = np.array([
        1.42343711074968357734,
        4.63033784615654529590,
        5.76949722146069140550,
        3.64784832476320460504,
        1.27045825245236838258,
        2.41780725177450611770e-1,
        2.27238449892691845833e-2,
        7.74545014278341407640e-4])

    const1 = 0.180625
    const2 = 1.6

    d = np.array([
        1.0,
        2.05319162663775882187,
        1.67638483018380384940,
        6.89767334985100004550e-1,
        1.48103976427480074590e-1,
        1.51986665636164571966e-2,
        5.47593808499534494600e-4,
        1.05075007164441684324e-9])

    e = np.array([
        6.65790464350110377720,
        5.46378491116411436990,
        1.78482653991729133580,
        2.96560571828504891230e-1,
        2.65321895265761230930e-2,
        1.24266094738807843860e-3,
        2.71155556874348757815e-5,
        2.01033439929228813265e-7])

    f = np.array([
        1.0,
        5.99832206555887937690e-1,
        1.36929880922735805310e-1,
        1.48753612908506148525e-2,
        7.86869131145613259100e-4,
        1.84631831751005468180e-5,
        1.42151175831644588870e-7,
        2.04426310338993978564e-15])

    r8_huge = 1.0E+30
    split1 = 0.425
    split2 = 5.0

    if (p <= 0.0):
        value = - r8_huge
        return value

    if (1.0 <= p):
        value = r8_huge
        return value

    q = p - 0.5

    if (abs(q) <= split1):

        r = const1 - q * q
        value = q * r8poly_value_horner(7, a, r) / r8poly_value_horner(7, b, r)

    else:

        if (q < 0.0):
            r = p
        else:
            r = 1.0 - p

        if (r <= 0.0):

            value = r8_huge

        else:

            r = np.sqrt(- np.log(r))

            if (r <= split2):

                r = r - const2
                value = r8poly_value_horner(
                    7, c, r) / r8poly_value_horner(7, d, r)

            else:

                r = r - split2
                value = r8poly_value_horner(
                    7, e, r) / r8poly_value_horner(7, f, r)

        if (q < 0.0):
            value = - value

    return value


def normal_01_mean():

    # *****************************************************************************80
    #
    # NORMAL_01_MEAN returns the mean of the Normal 01 PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real MEAN, the mean of the PDF.
    #
    mean = 0.0

    return mean


def normal_01_pdf(x):

    # *****************************************************************************80
    #
    # NORMAL_01_PDF evaluates the Normal 01 PDF.
    #
    #  Discussion:
    #
    #    The Normal 01 PDF is also called the "Standard Normal" PDF, or
    #    the Normal PDF with 0 mean and variance 1.
    #
    #  Formula:
    #
    #    PDF(x) = exp ( - 0.5 * x^2 ) / sqrt ( 2 * pi )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the PDF.
    #
    #    Output, real PDF, the value of the PDF.
    #

    pdf = np.exp(- 0.5 * x * x) / np.sqrt(2.0 * np.pi)

    return pdf


def normal_01_sample(seed):

    # *****************************************************************************80
    #
    # NORMAL_01_SAMPLE samples the standard normal probability distribution.
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
    #    04 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, X, a sample of the standard normal PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    r1, seed = r8_uniform_01(seed)
    r2, seed = r8_uniform_01(seed)
    x = np.sqrt(- 2.0 * np.log(r1)) * np.cos(2.0 * np.pi * r2)

    return x, seed


def normal_01_sample_test():

    # *****************************************************************************80
    #
    # NORMAL_01_SAMPLE_TEST tests NORMAL_01_MEAN, NORMAL_01__SAMPLE, NORMAL_01__VARIANCE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    nsample = 1000
    seed = 123456789

    print('')
    print('NORMAL_01_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  NORMAL_01_MEAN computes the Normal 01 mean')
    print('  NORMAL_01_SAMPLE samples the Normal 01 distribution')
    print('  NORMAL_01_VARIANCE returns the Normal 01 variance.')

    mean = normal_01_mean()
    variance = normal_01_variance()

    print('')
    print('  PDF mean =      %14g' % (mean))
    print('  PDF variance =  %14g' % (variance))

    x = np.zeros(nsample)

    for i in range(0, nsample):
        x[i], seed = normal_01_sample(seed)

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
    print('NORMAL_01_SAMPLE_TEST')
    print('  Normal end of execution.')


def normal_01_variance():

    # *****************************************************************************80
    #
    # NORMAL_01_VARIANCE returns the variance of the Normal 01 PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real VARIANCE, the variance of the PDF.
    #
    variance = 1.0

    return variance


def normal_cdf(x, a, b):

    # *****************************************************************************80
    #
    # NORMAL_CDF evaluates the Normal CDF.
    #
    #  Discussion:
    #
    #    The Normal CDF is related to the Error Function ERF(X) by:
    #
    #      ERF ( X ) = 2 * NORMAL_CDF ( SQRT ( 2 ) * X ) - 1.0.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 March 2016
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
    #    0.0 < B.
    #
    #    Output, real CDF, the value of the CDF.
    #
    y = (x - a) / b

    cdf = normal_01_cdf(y)

    return cdf


def normal_cdf_inv(cdf, a, b):

    # *****************************************************************************80
    #
    # NORMAL_CDF_INV inverts the Normal CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 March 2016
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
    #    0.0 < B.
    #
    #    Output, real X, the corresponding argument.
    #

    if (cdf < 0.0 or 1.0 < cdf):
        print('')
        print('NORMAL_CDF_INV - Fatal error!')
        print('  CDF < 0 or 1 < CDF.')
        exit('NORMAL_CDF_INV - Fatal error!')

    x2 = normal_01_cdf_inv(cdf)
    x = a + b * x2
    return x


def normal_cdf_test():

    # *****************************************************************************80
    #
    # NORMAL_CDF_TEST tests NORMAL_CDF, NORMAL_CDF_INV, NORMAL_PDF
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('NORMAL_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  NORMAL_CDF evaluates the Normal CDF')
    print('  NORMAL_CDF_INV inverts the Normal CDF.')
    print('  NORMAL_PDF evaluates the Normal PDF')

    a = 100.0
    b = 15.0

    check = normal_check(a, b)

    if (not check):
        print('')
        print('NORMAL_CDF_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    print('')
    print('  PDF parameter A =             %14g' % (a))
    print('  PDF parameter B =             %14g' % (b))

    seed = 123456789

    print('')
    print('       X            PDF           CDF            CDF_INV')
    print('')

    for i in range(0, 10):
        x, seed = normal_sample(a, b, seed)
        pdf = normal_pdf(x, a, b)
        cdf = normal_cdf(x, a, b)
        x2 = normal_cdf_inv(cdf, a, b)
        print(' %14g  %14g  %14g  %14g' % (x, pdf, cdf, x2))

    print('')
    print('NORMAL_CDF_TEST')
    print('  Normal end of execution.')


def normal_check(a, b):

    # *****************************************************************************80
    #
    # NORMAL_CHECK checks the parameters of the Normal PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 March 2016
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
    #    Output, logical CHECK, is true if the parameters are legal.
    #
    check = True

    if (b <= 0.0):
        print('')
        print('NORMAL_CHECK - Fatal error!')
        print('  B <= 0.')
        check = False

    return check


def normal_mean(a, b):

    # *****************************************************************************80
    #
    # NORMAL_MEAN returns the mean of the Normal PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 March 2016
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
    #    Output, real MEAN, the mean of the PDF.
    #
    mean = a

    return mean


def normal_pdf(x, a, b):

    # *****************************************************************************80
    #
    # NORMAL_PDF evaluates the Normal PDF.
    #
    #  Discussion:
    #
    #    The normal PDF is also known as the Gaussian PDF.
    #
    #  Formula:
    #
    #    PDF(X)(A,B) = EXP ( - 0.5 * ( ( X - A ) / B )^2 ) / SQRT ( 2 * PI * B^2 )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X(), the argument of the PDF.
    #
    #    Input, real A, a parameter of the PDF.
    #    A represents the mean value of the variables.
    #
    #    Input, real B, a parameter of the PDF.
    #    B represents the standard deviation of the variables.
    #
    #    Output, real PDF(), the value of the PDF.
    #

    pdf = np.exp(- 0.5 * ((x - a) / b) ** 2) \
        / np.sqrt(2.0 * np.pi * b ** 2)

    return pdf


def normal_sample(a, b, seed):

    # *****************************************************************************80
    #
    # NORMAL_SAMPLE samples the Normal PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 March 2016
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
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    y, seed = normal_01_sample(seed)

    x = a + b * y

    return x, seed


def normal_sample_test():

    # *****************************************************************************80
    #
    # NORMAL_SAMPLE_TEST tests NORMAL_MEAN, NORMAL_SAMPLE, NORMAL_VARIANCE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    nsample = 1000
    seed = 123456789

    print('')
    print('NORMAL_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  NORMAL_MEAN computes the Normal mean')
    print('  NORMAL_SAMPLE samples the Normal distribution')
    print('  NORMAL_VARIANCE returns the Normal variance.')

    a = 100.0
    b = 15.0

    check = normal_check(a, b)

    if (not check):
        print('')
        print('NORMAL_SAMPLE_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    mean = normal_mean(a, b)
    variance = normal_variance(a, b)

    print('')
    print('  PDF parameter A =     %14g' % (a))
    print('  PDF parameter B =     %14g' % (b))
    print('  PDF mean =            %14g' % (mean))
    print('  PDF variance =        %14g' % (variance))

    x = np.zeros(nsample)

    for i in range(0, nsample):
        x[i], seed = normal_sample(a, b, seed)

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
    print('NORMAL_SAMPLE_TEST')
    print('  Normal end of execution.')


def normal_variance(a, b):

    # *****************************************************************************80
    #
    # NORMAL_VARIANCE returns the variance of the Normal PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 September 2004
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
    #    Output, real VARIANCE, the variance of the PDF.
    #
    variance = b * b

    return variance


def r8poly_print(m, a, title):

    # *****************************************************************************80
    #
    # R8POLY_PRINT prints out a polynomial.
    #
    #  Discussion:
    #
    #    The power sum form is:
    #
    #      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the nominal degree of the polynomial.
    #
    #    Input, real A[0:M], the polynomial coefficients.
    #    A[0] is the constant term and
    #    A[M] is the coefficient of X^M.
    #
    #    Input, string TITLE, a title.
    #
    if (0 < len(title)):
        print('')
        print(title)
    print('')

    if (a[m] < 0.0):
        plus_minus = '-'
    else:
        plus_minus = ' '

    mag = abs(a[m])

    if (2 <= m):
        print('  p(x) = %c %g * x^%d' % (plus_minus, mag, m))
    elif (m == 1):
        print('  p(x) = %c %g * x' % (plus_minus, mag))
    elif (m == 0):
        print('  p(x) = %c %g' % (plus_minus, mag))

    for i in range(m - 1, -1, -1):

        if (a[i] < 0.0):
            plus_minus = '-'
        else:
            plus_minus = '+'

        mag = abs(a[i])

        if (mag != 0.0):

            if (2 <= i):
                print('         %c %g * x^%d' % (plus_minus, mag, i))
            elif (i == 1):
                print('         %c %g * x' % (plus_minus, mag))
            elif (i == 0):
                print('         %c %g' % (plus_minus, mag))


def r8poly_print_test():

    # *****************************************************************************80
    #
    # R8POLY_PRINT_TEST tests R8POLY_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8POLY_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8POLY_PRINT prints an R8POLY.')

    m = 5
    c = np.array([12.0, -3.4, 56.0, 0.0, 0.78, 9.0])

    r8poly_print(m, c, '  The R8POLY:')

    print('')
    print('R8POLY_PRINT_TEST:')
    print('  Normal end of execution.')


def r8poly_value_horner(m, c, x):

    # *****************************************************************************80
    #
    # R8POLY_VALUE_HORNER evaluates a polynomial using Horner's method.
    #
    #  Discussion:
    #
    #    The polynomial
    #
    #      p(x) = c0 + c1 * x + c2 * x^2 + ... + cm * x^m
    #
    #    is to be evaluated at the value X.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the degree.
    #
    #    Input, real C(0:M), the polynomial coefficients.
    #    C(I) is the coefficient of X^I.
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the polynomial value.
    #
    value = c[m]
    for i in range(m - 1, -1, -1):
        value = value * x + c[i]

    return value


def r8poly_value_horner_test():

    # *****************************************************************************80
    #
    # R8POLY_VALUE_HORNER_TEST tests R8POLY_VALUE_HORNER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 4
    n = 16
    c = np.array([24.0, -50.0, +35.0, -10.0, 1.0])

    print('')
    print('R8POLY_VALUE_HORNER_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8POLY_VALUE_HORNER evaluates a polynomial at a point')
    print('  using Horners method.')

    r8poly_print(m, c, '  The polynomial coefficients:')

    x_lo = 0.0
    x_hi = 5.0
    x = np.linspace(x_lo, x_hi, n)

    print('')
    print('   I    X    P(X)')
    print('')

    for i in range(0, n):
        p = r8poly_value_horner(m, c, x[i])
        print('  %2d  %8.4f  %14.6g' % (i, x[i], p))

    print('')
    print('R8POLY_VALUE_HORNER_TEST:')
    print('  Normal end of execution.')


def r8_uniform_01(seed):

    # *****************************************************************************80
    #
    # R8_UNIFORM_01 returns a unit pseudorandom R8.
    #
    #  Discussion:
    #
    #    This routine implements the recursion
    #
    #      seed = 16807 * seed mod ( 2^31 - 1 )
    #      r8_uniform_01 = seed / ( 2^31 - 1 )
    #
    #    The integer arithmetic never requires more than 32 bits,
    #    including a sign bit.
    #
    #    If the initial seed is 12345, then the first three computations are
    #
    #      Input     Output      R8_UNIFORM_01
    #      SEED      SEED
    #
    #         12345   207482415  0.096616
    #     207482415  1790989824  0.833995
    #    1790989824  2035175616  0.947702
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 March 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.  SEED should not be 0.
    #
    #    Output, real R, a random value between 0 and 1.
    #
    #    Output, integer SEED, the updated seed.  This would
    #    normally be used as the input seed on the next call.
    #
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    seed = (seed % i4_huge)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8_UNIFORM_01 - Fatal error!')

    k = (seed // 127773)

    seed = 16807 * (seed - k * 127773) - k * 2836

    if (seed < 0):
        seed = seed + i4_huge

    r = seed * 4.656612875E-10

    return r, seed


def r8_uniform_01_test():

    # *****************************************************************************80
    #
    # R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
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
    import platform

    print('')
    print('R8_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_UNIFORM_01 produces a sequence of random values.')

    seed = 123456789

    print('')
    print('  Using random seed %d' % (seed))

    print('')
    print('  SEED  R8_UNIFORM_01(SEED)')
    print('')
    for i in range(0, 10):
        seed_old = seed
        x, seed = r8_uniform_01(seed)
        print('  %12d  %14f' % (seed, x))

    print('')
    print('  Verify that the sequence can be restarted.')
    print('  Set the seed back to its original value, and see that')
    print('  we generate the same sequence.')

    seed = 123456789
    print('')
    print('  SEED  R8_UNIFORM_01(SEED)')
    print('')

    for i in range(0, 10):
        seed_old = seed
        x, seed = r8_uniform_01(seed)
        print('  %12d  %14f' % (seed, x))
#
#  Terminate.
#
    print('')
    print('R8_UNIFORM_01_TEST')
    print('  Normal end of execution.')
    return


def r8vec_normal_01_sorted(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_01_SORTED returns a sorted normal 01 random vector.
    #
    #  Discussion:
    #
    #    The Normal 01 distribution has mean 0 and standard deviation 1.
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
    #  Reference:
    #
    #    Jon Bentley, James Saxe,
    #    Generating sorted lists of random numbers,
    #    ACM Transactions on Mathematical Software,
    #    Volume 6, Number 3, September 1980, pages 359-364.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of values to generate.
    #
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.  SEED should not be 0.
    #
    #    Output, real R8VEC(N), a real vector of normal 01 random values
    #    in ascending order.
    #
    #    Output, integer SEED, the updated seed.
    #
    import numpy as np

    cdfvec, seed = r8vec_uniform_01_sorted1(n, seed)

    r8vec = np.zeros(n)

    for i in range(0, n):
        r8vec[i] = normal_01_cdf_inv(cdfvec[i])

    return r8vec, seed


def r8vec_normal_01_sorted_test():

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_01_SORTED_TEST tests R8VEC_NORMAL_01_SORTED_TEST,
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
    import platform

    print('')
    print('R8VEC_NORMAL_01_SORTED_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_NORMAL_01_SORTED generates a vector of N normal 01')
    print('  random values in ascending sorted order.')
    print('')
    print('  Generate several examples:')
    print('')

    n = 5
    seed = 123456789

    for i in range(0, 10):
        r8vec, seed = r8vec_normal_01_sorted(n, seed)
        r8vec_transpose_print(n, r8vec, '  R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_NORMAL_01_SORTED_TEST')
    print('  Normal end of execution.')
    return


def r8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_PRINT prints an R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d:  %12g' % (i, a[i]))


def r8vec_print_test():

    # *****************************************************************************80
    #
    # R8VEC_PRINT_TEST tests R8VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_PRINT prints an R8VEC.')

    n = 4
    v = np.array([123.456, 0.000005, -1.0E+06, 3.14159265], dtype=np.float64)
    r8vec_print(n, v, '  Here is an R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8vec_transpose_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_TRANSPOSE_PRINT prints an R8VEC "transposed".
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Example:
    #
    #    A = (/ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 /)
    #    TITLE = 'My vector:  '
    #
    #    My vector:   1.0    2.1    3.2    4.3    5.4
    #                 6.5    7.6    8.7    9.8   10.9
    #                11.0
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
    #    Input, integer N, the number of components of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    title_length = len(title)

    for ilo in range(0, n, 5):

        if (ilo == 0):
            print(title),
        else:
            blanks = ''
            for i in range(0, title_length):
                blanks = blanks + ' '
            print(blanks),

        print('  '),

        ihi = min(ilo + 5 - 1, n - 1)

        for i in range(ilo, ihi + 1):
            print('  %12g' % (a[i])),
        print('')

    return


def r8vec_transpose_print_test():

    # *****************************************************************************80
    #
    # R8VEC_TRANSPOSE_PRINT_TEST tests R8VEC_TRANSPOSE_PRINT.
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
    import platform

    n = 12
    seed = 123456789

    print('')
    print('R8VEC_TRANSPOSE_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_TRANSPOSE_PRINT prints an R8VEC "tranposed",')
    print('  that is, placing multiple entries on a line.')

    x, seed = r8vec_uniform_01(n, seed)

    r8vec_transpose_print(n, x, '  The vector X:')
#
#  Terminate.
#
    print('')
    print('R8VEC_TRANSPOSE_PRINT_TEST')
    print('  Normal end of execution.')
    return


def r8vec_uniform_01(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
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
    import numpy as np
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8VEC_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8VEC_UNIFORM_01 - Fatal error!')

    x = np.zeros(n)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        if (seed < 0):
            seed = seed + i4_huge

        x[i] = seed * 4.656612875E-10

    return x, seed


def r8vec_uniform_01_test():

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    n = 10
    seed = 123456789

    print('')
    print('R8VEC_UNIFORM_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_UNIFORM_01 computes a random R8VEC.')
    print('')
    print('  Initial seed is %d' % (seed))

    v, seed = r8vec_uniform_01(n, seed)

    r8vec_print(n, v, '  Random R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_UNIFORM_01_TEST:')
    print('  Normal end of execution.')
    return


def r8vec_uniform_01_sorted1(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01_SORTED1 returns a sorted real random vector in [0,1].
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
    #  Reference:
    #
    #    Jon Bentley, James Saxe,
    #    Generating sorted lists of random numbers,
    #    ACM Transactions on Mathematical Software,
    #    Volume 6, Number 3, September 1980, pages 359-364.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of values to generate.
    #
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.  SEED should not be 0.
    #
    #    Output, real R8VEC(N), a real vector of random values
    #    in ascending order.
    #
    #    Output, integer SEED, the updated seed.
    #
    import numpy as np

    r8vec = np.zeros(n)

    s = 0.0
    for i in range(0, n + 1):
        r, seed = r8_uniform_01(seed)
        s = s - np.log(r)
        if (i == n):
            break
        r8vec[i] = s

    for i in range(0, n):
        r8vec[i] = r8vec[i] / s

    return r8vec, seed


def r8vec_uniform_01_sorted1_test():

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01_SORTED1_TEST tests R8VEC_UNIFORM_01_SORTED1_TEST,
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
    import platform

    print('')
    print('R8VEC_UNIFORM_01_SORTED1_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_UNIFORM_01_SORTED1 generates a vector of N random')
    print('  values in ascending sorted order.')
    print('')
    print('  Generate several examples:')
    print('')

    n = 5
    seed = 123456789

    for i in range(0, 10):
        r8vec, seed = r8vec_uniform_01_sorted1(n, seed)
        r8vec_transpose_print(n, r8vec, '  R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_UNIFORM_01_SORTED1_TEST')
    print('  Normal end of execution.')
    return


def r8vec_uniform_01_sorted2(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01_SORTED2 returns a sorted real random vector in [0,1].
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
    #  Reference:
    #
    #    Jon Bentley, James Saxe,
    #    Generating sorted lists of random numbers,
    #    ACM Transactions on Mathematical Software,
    #    Volume 6, Number 3, September 1980, pages 359-364.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of values to generate.
    #
    #    Input, integer SEED, the integer "seed" used to generate
    #    the output random number.  SEED should not be 0.
    #
    #    Output, real R8VEC(N), a real vector of random values
    #    in ascending order.
    #
    #    Output, integer SEED, the updated seed.
    #
    import numpy as np

    r8vec = np.zeros(n)
    r, seed = r8vec_uniform_01(n, seed)

    curmax = 1.0
    for i in range(n - 1, -1, -1):
        curmax = curmax * np.exp(np.log(r[i]) / float(i + 1))
        r8vec[i] = curmax

    return r8vec, seed


def r8vec_uniform_01_sorted2_test():

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01_SORTED2_TEST tests R8VEC_UNIFORM_01_SORTED2_TEST.
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
    print('R8VEC_UNIFORM_01_SORTED2_TEST:')
    print('  R8VEC_UNIFORM_01_SORTED2 generates a vector of N random')
    print('  values in ascending sorted order.')
    print('')
    print('  Generate several examples:')
    print('')

    n = 5
    seed = 123456789

    for i in range(0, 10):
        r8vec, seed = r8vec_uniform_01_sorted2(n, seed)
        r8vec_transpose_print(n, r8vec, '  R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_UNIFORM_01_SORTED2_TEST')
    print('  Normal end of execution.')
    return


def random_sorted_test():

    # *****************************************************************************80
    #
    # RANDOM_SORTED_TEST tests the RANDOM_SORTED library.
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
    print('RANDOM_SORTED_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the RANDOM_SORTED library.')

    r8poly_print_test()
    r8poly_value_horner_test()

    r8vec_uniform_01_test()
    r8vec_uniform_01_sorted1_test()
    r8vec_uniform_01_sorted2_test()

    print('')
    print('RANDOM_SORTED_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    random_sorted_test()
    timestamp()
