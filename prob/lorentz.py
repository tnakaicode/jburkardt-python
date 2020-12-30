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


def lorentz_cdf(x):

    # *****************************************************************************80
    #
    # LORENTZ_CDF evaluates the Lorentz CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the CDF.
    #
    #    Output, real CDF, the value of the CDF.
    #
    import numpy as np

    cdf = 0.5 + np.arctan(x) / np.pi

    return cdf


def lorentz_cdf_inv(cdf):

    # *****************************************************************************80
    #
    # LORENTZ_CDF_INV inverts the Lorentz CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 April 2016
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
    #    Output, real X, the corresponding argument.
    #
    import numpy as np
    from sys import exit

    if (cdf < 0.0 or 1.0 < cdf):
        print('')
        print('LORENTZ_CDF_INV - Fatal error!')
        print('  CDF < 0 or 1 < CDF.')
        exit('LORENTZ_CDF_INV - Fatal error!')

    x = np.tan(np.pi * (cdf - 0.5))

    return x


def lorentz_cdf_test():

    # *****************************************************************************80
    #
    # LORENTZ_CDF_TEST tests LORENTZ_CDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('LORENTZ_CDF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  LORENTZ_CDF evaluates the Lorentz CDF')
    print('  LORENTZ_CDF_INV inverts the Lorentz CDF.')
    print('  LORENTZ_PDF evaluates the Lorentz PDF')

    seed = 123456789

    print('')
    print('       X            PDF           CDF            CDF_INV')
    print('')

    for i in range(0, 10):

        x, seed = lorentz_sample(seed)

        pdf = lorentz_pdf(x)

        cdf = lorentz_cdf(x)

        x2 = lorentz_cdf_inv(cdf)

        print(' %14g  %14g  %14g  %14g' % (x, pdf, cdf, x2))
#
#  Terminate.
#
    print('')
    print('LORENTZ_CDF_TEST')
    print('  Normal end of execution.')
    return


def lorentz_mean():

    # *****************************************************************************80
    #
    # LORENTZ_MEAN returns the mean of the Lorentz PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 April 2016
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


def lorentz_pdf(x):

    # *****************************************************************************80
    #
    # LORENTZ_PDF evaluates the Lorentz PDF.
    #
    #  Discussion:
    #
    #    PDF(X) = 1 / ( PI * ( 1 + X^2 ) )
    #
    #    The chief interest of the Lorentz PDF is that it is easily
    #    inverted, and can be used to dominate other PDF's in an
    #    acceptance/rejection method.
    #
    #    LORENTZ_PDF(X) = CAUCHY_PDF(X)(0,1)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 April 2016
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
    import numpy as np

    pdf = 1.0 / (np.pi * (1.0 + x * x))

    return pdf


def lorentz_sample(seed):

    # *****************************************************************************80
    #
    # LORENTZ_SAMPLE samples the Lorentz PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    from r8_uniform_01 import r8_uniform_01

    cdf, seed = r8_uniform_01(seed)

    x = lorentz_cdf_inv(cdf)

    return x, seed


def lorentz_sample_test():

    # *****************************************************************************80
    #
    # LORENTZ_SAMPLE_TEST tests LORENTZ_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 April 2016
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
    print('LORENTZ_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  LORENTZ_MEAN computes the Lorentz mean')
    print('  LORENTZ_VARIANCE computes the Lorentz variance')
    print('  LORENTZ_SAMPLE samples the Lorentz distribution.')

    mean = lorentz_mean()
    variance = lorentz_variance()

    print('')
    print('  PDF mean =                    %14g' % (mean))
    print('  PDF variance =                %14g' % (variance))

    x = np.zeros(nsample)
    for i in range(0, nsample):
        x[i], seed = lorentz_sample(seed)

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
    print('LORENTZ_SAMPLE_TEST')
    print('  Normal end of execution.')
    return


def lorentz_variance():

    # *****************************************************************************80
    #
    # LORENTZ_VARIANCE returns the variance of the Lorentz PDF.
    #
    #  Discussion:
    #
    #    The variance of the Lorentz PDF is not well defined.  This routine
    #    is made available for completeness only, and simply returns
    #    a "very large" number.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real VARIANCE, the mean of the PDF.
    #
    r8_huge = 1.0E+30

    variance = r8_huge

    return variance


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    lorentz_cdf_test()
    lorentz_sample_test()
    timestamp()
