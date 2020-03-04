#! /usr/bin/env python
#


def half_normal_cdf(x, a, b):

    # *****************************************************************************80
    #
    # HALF_NORMAL_CDF evaluates the Half Normal CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 April 2016
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
    from normal import normal_cdf

    if (x <= a):
        cdf = 0.0
    else:
        cdf2 = normal_cdf(x, a, b)
        cdf = 2.0 * cdf2 - 1.0

    return cdf


def half_normal_cdf_inv(cdf, a, b):

    # *****************************************************************************80
    #
    # HALF_NORMAL_CDF_INV inverts the Half Normal CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 April 2016
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
    from normal import normal_cdf_inv
    from sys import exit

    if (cdf < 0.0 or 1.0 < cdf):
        print('')
        print('HALF_NORMAL_CDF_INV - Fatal error!')
        print('  CDF < 0 or 1 < CDF.')
        exit('HALF_NORMAL_CDF_INV - Fatal error!')

    cdf2 = 0.5 * (cdf + 1.0)

    x = normal_cdf_inv(cdf2, a, b)

    return x


def half_normal_cdf_test():

    # *****************************************************************************80
    #
    # HALF_NORMAL_CDF_TEST tests HALF_NORMAL_CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('HALF_NORMAL_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  HALF_NORMAL_CDF evaluates the Half Normal CDF.')
    print('  HALF_NORMAL_CDF_INV inverts the Half Normal CDF.')
    print('  HALF_NORMAL_PDF evaluates the Half Normal PDF.')

    a = 0.0
    b = 2.0

    check = half_normal_check(a, b)

    if (not check):
        print('')
        print('HALF_NORMAL_CDF_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    print('')
    print('  PDF parameter A =         %14g' % (a))
    print('  PDF parameter B =         %14g' % (b))

    seed = 123456789

    print('')
    print('       X            PDF           CDF            CDF_INV')
    print('')

    import numpy as np
    from plot import plot_pnt

    dat = []
    for i in range(0, 10):

        [x, seed] = half_normal_sample(a, b, seed)
        pdf = half_normal_pdf(x, a, b)
        cdf = half_normal_cdf(x, a, b)
        x2 = half_normal_cdf_inv(cdf, a, b)

        print(' %14g  %14g  %14g  %14g' % (x, pdf, cdf, x2))
        dat.append(np.array([x, pdf, cdf, x2]))
    dat = np.array(dat)
    plot_pnt(dat, "half_normal")

#
#  Terminate.
#
    print('')
    print('HALF_NORMAL_CDF_TEST')
    print('  Normal end of execution.')
    return


def half_normal_check(a, b):

    # *****************************************************************************80
    #
    # HALF_NORMAL_CHECK checks the parameters of the Half Normal PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 April 2016
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
        print('HALF_NORMAL_CHECK - Fatal error!')
        print('  B <= 0.')
        check = False

    return check


def half_normal_mean(a, b):

    # *****************************************************************************80
    #
    # HALF_NORMAL_MEAN returns the mean of the Half Normal PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 April 2016
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
    import numpy as np

    mean = a + b * np.sqrt(2.0 / np.pi)

    return mean


def half_normal_pdf(x, a, b):

    # *****************************************************************************80
    #
    # HALF_NORMAL_PDF evaluates the Half Normal PDF.
    #
    #  Discussion:
    #
    #    PDF(X)(A,B) =
    #      SQRT ( 2 / PI ) * ( 1 / B ) * EXP ( - 0.5 * ( ( X - A ) / B )^2 )
    #
    #    for A <= X
    #
    #    The Half Normal PDF is a special case of both the Chi PDF and the
    #    Folded Normal PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the PDF.
    #    A <= X
    #
    #    Input, real  A, B, the parameters of the PDF.
    #    0.0 < B.
    #
    #    Output, real PDF, the value of the PDF.
    #
    import numpy as np

    if (x <= a):

        pdf = 0.0

    else:

        y = (x - a) / b

        pdf = np.sqrt(2.0 / np.pi) * (1.0 / b) * np.exp(- 0.5 * y * y)

    return pdf


def half_normal_sample(a, b, seed):

    # *****************************************************************************80
    #
    # HALF_NORMAL_SAMPLE samples the Half Normal PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 April 2016
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

    x = half_normal_cdf_inv(cdf, a, b)

    return x, seed


def half_normal_sample_test():

    # *****************************************************************************80
    #
    # HALF_NORMAL_SAMPLE_TEST tests HALF_NORMAL_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 April 2016
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
    print('HALF_NORMAL_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  HALF_NORMAL_MEAN computes the Half Normal mean')
    print('  HALF_NORMAL_SAMPLE samples the Half Normal distribution')
    print('  HALF_NORMAL_VARIANCE computes the Half Normal variance.')

    a = 0.0
    b = 10.0

    check = half_normal_check(a, b)

    if (not check):
        print('')
        print('HALF_NORMAL_SAMPLE_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    mean = half_normal_mean(a, b)
    variance = half_normal_variance(a, b)

    print('')
    print('  PDF parameter A =             %14g' % (a))
    print('  PDF parameter B =             %14g' % (b))
    print('  PDF mean =                    %14g' % (mean))
    print('  PDF variance =                %14g' % (variance))

    x = np.zeros(nsample)
    for i in range(0, nsample):
        x[i], seed = half_normal_sample(a, b, seed)

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
    print('HALF_NORMAL_SAMPLE_TEST')
    print('  Normal end of execution.')
    return


def half_normal_variance(a, b):

    # *****************************************************************************80
    #
    # HALF_NORMAL_VARIANCE returns the variance of the Half Normal PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 April 2016
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
    import numpy as np

    variance = b * b * (1.0 - 2.0 / np.pi)

    return variance


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    half_normal_cdf_test()
    half_normal_sample_test()
    timestamp()
