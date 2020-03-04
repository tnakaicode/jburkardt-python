#! /usr/bin/env python
#


def bradford_cdf_inv(cdf, a, b, c):

    # *****************************************************************************80
    #
    # BRADFORD_CDF_INV inverts the Bradford CDF.
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
    #    Input, real CDF, the value of the CDF.
    #    0.0 <= CDF <= 1.0.
    #
    #    Input, real A, B, C, the parameters of the PDF.
    #    A < B,
    #    0.0 < C.
    #
    #    Output, real X, the corresponding argument of the CDF.
    #
    from sys import exit

    if (cdf < 0.0 or 1.0 < cdf):
        print('')
        print('BRADFORD_CDF_INV - Fatal error!')
        print('  CDF < 0 or 1 < CDF.')
        exit('BRADFORD_CDF_INV - Fatal error!')

    if (cdf <= 0.0):
        x = a
    elif (cdf < 1.0):
        x = a + (b - a) * ((c + 1.0) ** cdf - 1.0) / c
    elif (1.0 <= cdf):
        x = b

    return x


def bradford_cdf(x, a, b, c):

    # *****************************************************************************80
    #
    # BRADFORD_CDF evaluates the Bradford CDF.
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
    #    Input, real X, the argument of the CDF.
    #
    #    Input, real A, B, C, the parameters of the PDF.
    #    A < B,
    #    0.0 < C.
    #
    #    Output, real CDF, the value of the CDF.
    #
    import numpy as np

    if (x <= a):
        cdf = 0.0
    elif (x <= b):
        cdf = np.log(1.0 + c * (x - a) / (b - a)) / np.log(c + 1.0)
    elif (b < x):
        cdf = 1.0

    return cdf


def bradford_cdf_test():

    # *****************************************************************************80
    #
    # BRADFORD_CDF_TEST tests BRADFORD_CDF, BRADFORD_CDF_INV, BRADFORD_PDF.
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
    import platform

    print('')
    print('BRADFORD_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  BRADFORD_CDF evaluates the Bradford CDF')
    print('  BRADFORD_CDF_INV inverts the Bradford CDF.')
    print('  BRADFORD_PDF evaluates the Bradford PDF')

    a = 1.0
    b = 2.0
    c = 3.0

    check = bradford_check(a, b, c)

    if (not check):
        print('')
        print('BRADFORD_CDF_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    print('')
    print('  PDF parameter A = %14g' % (a))
    print('  PDF parameter B = %14g' % (b))
    print('  PDF parameter C = %14g' % (c))

    seed = 123456789

    print('')
    print('       X            PDF           CDF            CDF_INV')
    print('')

    import numpy as np
    from plot import plot_pnt

    dat = []
    for i in range(0, 10):

        x, seed = bradford_sample(a, b, c, seed)
        pdf = bradford_pdf(x, a, b, c)
        cdf = bradford_cdf(x, a, b, c)
        x2 = bradford_cdf_inv(cdf, a, b, c)

        print(' %14g  %14g  %14g  %14g' % (x, pdf, cdf, x2))
        dat.append(np.array([x, pdf, cdf, x2]))
    dat = np.array(dat)
    plot_pnt(dat, "bradford")
#
#  Terminate.
#
    print('')
    print('BRADFORD_CDF_TEST')
    print('  Normal end of execution.')
    return


def bradford_check(a, b, c):

    # *****************************************************************************80
    #
    # BRADFORD_CHECK checks the parameters of the Bradford PDF.
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
    #    Input, real A, B, C, the parameters of the PDF.
    #    A < B,
    #    0.0 < C.
    #
    #    Output, logical CHECK, is TRUE if the parameters are legal.
    #
    check = True

    if (b <= a):
        print('')
        print('BRADFORD_CHECK - Fatal error!')
        print('  B <= A.')
        check = False
    elif (c <= 0.0):
        print('')
        print('BRADFORD_CHECK - Fatal error!')
        print('  C <= 0.')
        check = False

    return check


def bradford_mean(a, b, c):

    # *****************************************************************************80
    #
    # BRADFORD_MEAN returns the mean of the Bradford PDF.
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
    #    Input, real A, B, C, the parameters of the PDF.
    #    A < B,
    #    0.0 < C.
    #
    #    Output, real MEAN, the mean of the PDF.
    #
    import numpy as np

    mean = (c * (b - a) + np.log(c + 1.0) * (a * (c + 1.0) - b)) \
        / (c * np.log(c + 1.0))

    return mean


def bradford_pdf(x, a, b, c):

    # *****************************************************************************80
    #
    # BRADFORD_PDF evaluates the Bradford PDF.
    #
    #  Discussion:
    #
    #    PDF(X)(A,B,C) =
    #      C / ( ( C * ( X - A ) + B - A ) * log ( C + 1 ) )
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
    #    Input, real X, the argument of the PDF.
    #    A <= X
    #
    #    Input, real A, B, C, the parameters of the PDF.
    #    A < B,
    #    0.0 < C.
    #
    #    Output, real PDF, the value of the PDF.
    #
    import numpy as np

    if (x <= a):
        pdf = 0.0
    elif (x <= b):
        pdf = c / ((c * (x - a) + b - a) * np.log(c + 1.0))
    elif (b < x):
        pdf = 0.0

    return pdf


def bradford_sample(a, b, c, seed):

    # *****************************************************************************80
    #
    # BRADFORD_SAMPLE samples the Bradford PDF.
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
    #    Input, real A, B, C, the parameters of the PDF.
    #    A < B,
    #    0.0 < C.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the PDF.
    #
    #    Output, integer SEED, a seed for the random number generator.
    #
    from r8_uniform_01 import r8_uniform_01

    cdf, seed = r8_uniform_01(seed)

    x = a + (b - a) * ((c + 1.0) ** cdf - 1.0) / c

    return x, seed


def bradford_sample_test():

    # *****************************************************************************80
    #
    # BRADFORD_SAMPLE_TEST tests BRADFORD_MEAN, BRADFORD_SAMPLE, BRADFORD_VARIANCE.
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
    import numpy as np
    import platform
    from r8vec_max import r8vec_max
    from r8vec_mean import r8vec_mean
    from r8vec_min import r8vec_min
    from r8vec_variance import r8vec_variance

    nsample = 1000
    seed = 123456789

    print('')
    print('BRADFORD_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  BRADFORD_MEAN computes the Bradford mean')
    print('  BRADFORD_SAMPLE samples the Bradford distribution')
    print('  BRADFORD_VARIANCE computes the Bradford variance.')

    a = 1.0
    b = 2.0
    c = 3.0

    check = bradford_check(a, b, c)

    if (not check):
        print('')
        print('BRADFORD_SAMPLE_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    mean = bradford_mean(a, b, c)
    variance = bradford_variance(a, b, c)

    print('')
    print('  PDF parameter A = %14g' % (a))
    print('  PDF parameter B = %14g' % (b))
    print('  PDF parameter C = %14g' % (c))
    print('  PDF mean =        %14g' % (mean))
    print('  PDF variance =    %14g' % (variance))

    x = np.zeros(nsample)

    for i in range(0, nsample):
        x[i], seed = bradford_sample(a, b, c, seed)

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
    print('BRADFORD_SAMPLE_TEST')
    print('  Normal end of execution.')
    return


def bradford_variance(a, b, c):

    # *****************************************************************************80
    #
    # BRADFORD_VARIANCE returns the variance of the Bradford PDF.
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
    #    Input, real A, B, C, the parameters of the PDF.
    #    A < B,
    #    0.0 < C.
    #
    #    Output, real VARIANCE, the variance of the PDF.
    #
    import numpy as np

    variance = (b - a) ** 2 * \
        (c * (np.log(c + 1.0) - 2.0) + 2.0 * np.log(c + 1.0)) \
        / (2.0 * c * (np.log(c + 1.0)) ** 2)

    return variance


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    bradford_cdf_test()
    bradford_sample_test()
    timestamp()
