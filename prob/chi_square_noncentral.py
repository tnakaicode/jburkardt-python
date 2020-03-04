#! /usr/bin/env python
#


def chi_square_noncentral_check(a, b):

    # *****************************************************************************80
    #
    # CHI_SQUARE_NONCENTRAL_CHECK checks the parameters of the noncentral Chi Squared PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer A, the parameter of the PDF.
    #    1.0 <= A.
    #
    #    Input, real B, the noncentrality parameter of the PDF.
    #    0.0 <= B.
    #
    check = True

    if (a < 1.0):
        print('')
        print('CHI_SQUARE_NONCENTRAL_CHECK - Fatal error!')
        print('  A < 1.')
        check = False

    if (b < 0.0):
        print('')
        print('CHI_SQUARE_NONCENTRAL_CHECK - Fatal error!')
        print('  B < 0.')
        check = False

    return check


def chi_square_noncentral_mean(a, b):

    # *****************************************************************************80
    #
    # CHI_SQUARE_NONCENTRAL_MEAN returns the mean of the noncentral Chi squared PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer A, the parameter of the PDF.
    #    1.0 <= A.
    #
    #    Input, real B, the noncentrality parameter of the PDF.
    #    0.0 <= B.
    #
    #    Output, real MEAN, the mean value.
    #
    mean = a + b

    return mean


def chi_square_noncentral_sample(a, b, seed):

    # *****************************************************************************80
    #
    # CHI_SQUARE_NONCENTRAL_SAMPLE samples the noncentral Chi squared PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer A, the parameter of the PDF.
    #    1.0 <= A.
    #
    #    Input, real B, the noncentrality parameter of the PDF.
    #    0.0 <= B.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X, a sample of the PDF.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    import numpy as np
    from chi_square import chi_square_sample
    from normal import normal_sample

    a1 = a - 1.0

    x1, seed = chi_square_sample(a1, seed)

    a2 = np.sqrt(b)
    b2 = 1.0
    x2, seed = normal_sample(a2, b2, seed)

    x = x1 + x2 * x2

    return x, seed


def chi_square_noncentral_sample_test():

    # *****************************************************************************80
    #
    # CHI_SQUARE_NONCENTRAL_SAMPLE_TEST tests CHI_SQUARE_NONCENTRAL_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 April 2016
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
    print('CHI_SQUARE_NONCENTRAL_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CHI_SQUARE_NONCENTRAL_MEAN computes the Chi Square Noncentral mean.')
    print('  CHI_SQUARE_NONCENTRAL_SAMPLE samples the Chi Square Noncentral PDF.')
    print('  CHI_SQUARE_NONCENTRAL_VARIANCE computes the Chi Square Noncentral variance.')

    a = 3.0
    b = 2.0

    check = chi_square_noncentral_check(a, b)

    if (not check):
        print('')
        print('CHI_SQUARE_NONCENTRAL_SAMPLE_TEST - Fatal error!')
        print('  The parameters are not legal.')
        return

    mean = chi_square_noncentral_mean(a, b)
    variance = chi_square_noncentral_variance(a, b)

    print('')
    print('  PDF parameter A = %14g' % (a))
    print('  PDF parameter B = %14g' % (b))
    print('  PDF mean =        %14g' % (mean))
    print('  PDF variance =    %14g' % (variance))
    print('')
    print('  Initial seed =    %12d' % (seed))

    x = np.zeros(nsample)
    for i in range(0, nsample):
        x[i], seed = chi_square_noncentral_sample(a, b, seed)

    mean = r8vec_mean(nsample, x)
    variance = r8vec_variance(nsample, x)
    xmax = r8vec_max(nsample, x)
    xmin = r8vec_min(nsample, x)

    print('  Final seed =      %12d' % (seed))
    print('  Sample size =     %6d' % (nsample))
    print('  Sample mean =     %14g' % (mean))
    print('  Sample variance = %14g' % (variance))
    print('  Sample maximum =  %14g' % (xmax))
    print('  Sample minimum =  %14g' % (xmin))
#
#  Terminate.
#
    print('')
    print('CHI_SQUARE_NONCENTRAL_SAMPLE_TEST')
    print('  Normal end of execution.')
    return


def chi_square_noncentral_variance(a, b):

    # *****************************************************************************80
    #
    # CHI_SQUARE_NONCENTRAL_VARIANCE returns the variance of the noncentral Chi squared PDF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A, the parameter of the PDF.
    #    1 <= A.
    #
    #    Input, real B, the noncentrality parameter of the PDF.
    #    0.0 <= B.
    #
    #    Output, real VARIANCE, the variance value.
    #
    variance = 2.0 * (a + 2.0 * b)

    return variance


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    chi_square_noncentral_sample_test()
    timestamp()
