#! /usr/bin/env python
#
def angle_cdf(x, n):

    # *****************************************************************************80
    #
    # ANGLE_CDF evaluates the Angle CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Reuven Rubinstein,
    #    Monte Carlo Optimization, Simulation and Sensitivity of Queueing Networks,
    #    Wiley, 1986.
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the PDF.
    #
    #    Input, integer N, the spatial dimension.
    #    N must be at least 2.
    #
    #    Output, real CDF, the value of the CDF.
    #
    import numpy as np
    from r8_gamma import r8_gamma
    from sin_power_int import sin_power_int
    from sys import exit

    if (n < 2):
        print('')
        print('ANGLE_CDF - Fatal error!')
        print('  N must be at least 2.')
        print('  The input value of N = %d' % (n))
        exit('ANGLE_CDF - Fatal error!')

    if (x <= 0.0):
        cdf = 0.0
    elif (np.pi <= x):
        cdf = 1.0
    elif (n == 2):
        cdf = x / np.pi
    else:
        cdf = sin_power_int(0.0, x, n - 2) * r8_gamma(n / 2.0) \
            / (np.sqrt(np.pi) * r8_gamma((n - 1) / 2.0))

    return cdf


def angle_cdf_test():

    # *****************************************************************************80
    #
    # ANGLE_CDF_TEST tests ANGLE_CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('ANGLE_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  ANGLE_CDF evaluates the Angle CDF')

    n = 5
    x = 0.50

    cdf = angle_cdf(x, n)

    print('')
    print('  PDF parameter N = %6d' % (n))
    print('  PDF argument X =  %14g' % (x))
    print('  CDF value =       %14g' % (cdf))
#
#  Terminate.
#
    print('')
    print('ANGLE_CDF_TEST')
    print('  Normal end of execution.')
    return


def angle_mean(n):

    # *****************************************************************************80
    #
    # ANGLE_MEAN returns the mean of the Angle PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the spatial dimension.
    #    N must be at least 2.
    #
    #    Output, real MEAN, the mean of the PDF.
    #
    import numpy as np

    mean = np.pi / 2.0

    return mean


def angle_mean_test():

    # *****************************************************************************80
    #
    # ANGLE_MEAN_TEST tests ANGLE_MEAN
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('ANGLE_MEAN_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  ANGLE_MEAN computes the Angle mean')

    n = 5
    mean = angle_mean(n)

    print('')
    print('  PDF parameter N = %6d' % (n))
    print('  PDF mean =        %14g' % (mean))
#
#  Terminate.
#
    print('')
    print('ANGLE_MEAN_TEST')
    print('  Normal end of execution.')
    return


def angle_pdf(x, n):

    # *****************************************************************************80
    #
    # ANGLE_PDF evaluates the Angle PDF.
    #
    #  Discussion:
    #
    #    X is an angle between 0 and PI, corresponding to the angle
    #    made in an N-dimensional space, between a fixed line passing
    #    through the origin, and an arbitrary line that also passes
    #    through the origin, which is specified by a choosing any point
    #    on the N-dimensional sphere with uniform probability.
    #
    #  Formula:
    #
    #    PDF(X) = ( sin ( X ) )**(N-2) * Gamma ( N / 2 )
    #             / ( sqrt ( PI ) * Gamma ( ( N - 1 ) / 2 ) )
    #
    #    PDF(X) = 1 / PI if N = 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Reuven Rubinstein,
    #    Monte Carlo Optimization, Simulation and Sensitivity of Queueing Networks,
    #    Wiley, 1986.
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the PDF.
    #
    #    Input, integer N, the spatial dimension.
    #    N must be at least 2.
    #
    #    Output, real PDF, the value of the PDF.
    #
    import numpy as np
    from r8_gamma import r8_gamma
    from sys import exit

    if (n < 2):
        print('')
        print('ANGLE_PDF - Fatal error!')
        print('  N must be at least 2.')
        print('  The input value of N = %d' % (n))
        exit('ANGLE_PDF - Fatal error!')

    if (x < 0.0 or np.pi < x):
        pdf = 0.0
    elif (n == 2):
        pdf = 1.0 / np.pi
    else:
        pdf = (np.sin(x)) ** (n - 2) * r8_gamma(n / 2.0) \
            / (np.sqrt(np.pi) * r8_gamma((n - 1) / 2.0))

    return pdf


def angle_pdf_test():

    # *****************************************************************************80
    #
    # ANGLE_PDF_TEST tests ANGLE_PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('ANGLE_PDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  ANGLE_PDF evaluates the Angle PDF')

    n = 5
    x = 0.50

    pdf = angle_pdf(x, n)

    print('')
    print('  PDF parameter N = %6d' % (n))
    print('  PDF argument X =  %14g' % (x))
    print('  PDF value =       %14g' % (pdf))
#
#  Terminate.
#
    print('')
    print('ANGLE_PDF_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    angle_cdf_test()
    angle_mean_test()
    angle_pdf_test()
    timestamp()
