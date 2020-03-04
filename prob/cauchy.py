#! /usr/bin/env python
#


def cauchy_cdf(x, a, b):

    # *****************************************************************************80
    #
    # CAUCHY_CDF evaluates the Cauchy CDF.
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
    #    Input, real X, the argument of the CDF.
    #
    #    Input, real A, B, the parameters of the PDF.
    #    0.0D+00 < B.
    #
    #    Output, real CDF, the value of the CDF.
    #
    import numpy as np

    y = (x - a) / b

    cdf = 0.5 + np.arctan(y) / np.pi

    return cdf


def cauchy_cdf_inv(cdf, a, b):

    # *****************************************************************************80
    #
    # CAUCHY_CDF_INV inverts the Cauchy CDF.
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
    #    0.0 <= CDF <= 1.0.
    #
    #    Input, real A, B, the parameters of the PDF.
    #    0.0 < B.
    #
    #    Output, real X, the corresponding argument.
    #
    import numpy as np

    x = a + b * np.tan(np.pi * (cdf - 0.5))

    return x


def cauchy_cdf_test():

    # *****************************************************************************80
    #
    # CAUCHY_CDF_TEST tests CAUCHY_CDF, CAUCHY_CDF_INV, CAUCHY_PDF.
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
    import platform

    print('')
    print('CAUCHY_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CAUCHY_CDF evaluates the Cauchy CDF')
    print('  CAUCHY_CDF_INV inverts the Cauchy CDF.')
    print('  CAUCHY_PDF evaluates the Cauchy PDF')

    a = 2.0
    b = 3.0

    check = cauchy_check(a, b)

    if (not check):
        print('')
        print('CAUCHY_CDF_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    print('')
    print('  PDF parameter A = %14g' % (a))
    print('  PDF parameter B = %14g' % (b))

    seed = 123456789

    print('')
    print('       X            PDF           CDF            CDF_INV')
    print('')
    import numpy as np
    from plot import plot_pnt

    dat = []
    for i in range(0, 10):

        x, seed = cauchy_sample(a, b, seed)
        pdf = cauchy_pdf(x, a, b)
        cdf = cauchy_cdf(x, a, b)
        x2 = cauchy_cdf_inv(cdf, a, b)

        print(' %14g  %14g  %14g  %14g' % (x, pdf, cdf, x2))
        dat.append(np.array([x, pdf, cdf, x2]))
    dat = np.array(dat)
    plot_pnt(dat, "cauchy")
#
#  Terminate.
#
    print('')
    print('CAUCHY_CDF_TEST')
    print('  Normal end of execution.')
    return


def cauchy_check(a, b):

    # *****************************************************************************80
    #
    # CAUCHY_CHECK checks the parameters of the Cauchy CDF.
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
    #    0.0 < B.
    #
    #    Output, logical CHECK, is TRUE if the parameters are legal.
    #
    check = True

    if (b <= 0.0):
        print('')
        print('CAUCHY_CHECK - Fatal error!')
        print('  B <= 0.')
        check = False

    return check


def cauchy_mean(a, b):

    # *****************************************************************************80
    #
    # CAUCHY_MEAN returns the mean of the Cauchy PDF.
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
    #    0.0 < B.
    #
    #    Output, real MEAN, the mean of the PDF.
    #
    mean = a

    return mean


def cauchy_pdf(x, a, b):

    # *****************************************************************************80
    #
    # CAUCHY_PDF evaluates the Cauchy PDF.
    #
    #  Discussion:
    #
    #    PDF(X)(A,B) = 1 / ( PI * B * ( 1 + ( ( X - A ) / B )^2 ) )
    #
    #    The Cauchy PDF is also known as the Breit-Wigner PDF.  It
    #    has some unusual properties.  In particular, the integrals for the
    #    expected value and higher order moments are "singular", in the
    #    sense that the limiting values do not exist.  A result can be
    #    obtained if the upper and lower limits of integration are set
    #    equal to +T and -T, and the limit as T=>INFINITY is taken, but
    #    this is a very weak and unreliable sort of limit.
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
    #    0.0 < B.
    #
    #    Output, real PDF, the value of the PDF.
    #
    import numpy as np

    y = (x - a) / b

    pdf = 1.0 / (np.pi * b * (1.0 + y * y))

    return pdf


def cauchy_sample(a, b, seed):

    # *****************************************************************************80
    #
    # CAUCHY_SAMPLE samples the Cauchy PDF.
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
    #    0.0 < B.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    from r8_uniform_01 import r8_uniform_01

    cdf, seed = r8_uniform_01(seed)

    x = cauchy_cdf_inv(cdf, a, b)

    return x, seed


def cauchy_sample_test():

    # *****************************************************************************80
    #
    # CAUCHY_SAMPLE_TEST tests CAUCHY_MEAN, CAUCHY_SAMPLE, CAUCHY_VARIANCE.
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
    import numpy as np
    import platform
    from r8vec_max import r8vec_max
    from r8vec_mean import r8vec_mean
    from r8vec_min import r8vec_min
    from r8vec_variance import r8vec_variance

    nsample = 1000
    seed = 123456789

    print('')
    print('CAUCHY_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CAUCHY_MEAN computes the Cauchy mean')
    print('  CAUCHY_VARIANCE computes the Cauchy variance')
    print('  CAUCHY_SAMPLE samples the Cauchy distribution.')

    a = 2.0
    b = 3.0

    check = cauchy_check(a, b)

    if (not check):
        print('')
        print('CAUCHY_SAMPLE_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    mean = cauchy_mean(a, b)
    variance = cauchy_variance(a, b)

    print('')
    print('  PDF parameter A = %14g' % (a))
    print('  PDF parameter B = %14g' % (b))
    print('  PDF mean =        %14g' % (mean))
    print('  PDF variance =    %14g' % (variance))

    x = np.zeros(nsample)
    for i in range(0, nsample):
        x[i], seed = cauchy_sample(a, b, seed)

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
#
#  Terminate.
#
    print('')
    print('CAUCHY_SAMPLE_TEST')
    print('  Normal end of execution.')
    return


def cauchy_variance(a, b):

    # *****************************************************************************80
    #
    # CAUCHY_VARIANCE returns the variance of the Cauchy PDF.
    #
    #  Discussion:
    #
    #    The variance of the Cauchy PDF is not well defined.  This routine
    #    is made available for completeness only, and simply returns
    #    a "very large" number.
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
    #    0.0 < B.
    #
    #    Output, real VARIANCE, the mean of the PDF.
    #
    from r8_huge import r8_huge

    variance = r8_huge()

    return variance


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    cauchy_cdf_test()
    cauchy_sample_test()
    timestamp()
