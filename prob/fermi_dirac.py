#! /usr/bin/env python
#


def fermi_dirac_sample(u, v, seed):

    # *****************************************************************************80
    #
    # FERMI_DIRAC_SAMPLE samples a (continuous) Fermi-Dirac distribution.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 April 2016
    #
    #  Author:
    #
    #    Original BASIC version by Frederick Ruckdeschel.
    #    Python version by John Burkardt
    #
    #  Reference:
    #
    #    Frederick Ruckdeschel,
    #    BASIC Scientific Subroutines,
    #    Volume I,
    #    McGraw Hill, 1980,
    #    ISBN: 0-07-054201-5,
    #    LC: QA76.95.R82.
    #
    #  Parameters:
    #
    #    Input, real U, V, the parameters of the distribution.
    #    The value of U represents the halfway point for the distribution.
    #    Half the probability is to the left, and half to the right, of
    #    the value U.  The value of V controls the shape of the distribution.
    #    The ratio U/V determines the relative shape of the distribution.
    #    Values of U/V in excess of 100 will risk overflow.
    #
    #    Input/output, integer SEED, a seed for the random
    #    number generator.
    #
    #    Output, real Z, a sample from the Fermi-Dirac distribution.
    #    Output values will be nonnegative, and roughly half of them should
    #    be less than or equal to U.
    #
    import numpy as np
    from r8_uniform_01 import r8_uniform_01

    iter_max = 1000

    x, seed = r8_uniform_01(seed)
    y = 1.0
    a = np.exp(4.0 * u / v)
    b = (x - 1.0) * np.log(1.0 + a)

    iter_num = 0

    while (True):

        y1 = b + np.log(a + np.exp(y))

        if (abs(y - y1) < 0.001):
            break

        y = y1

        iter_num = iter_num + 1

        if (iter_max < iter_num):
            break

    z = v * y1 / 4.0

    return z, seed


def fermi_dirac_sample_test():

    # *****************************************************************************80
    #
    # FERMI_DIRAC_SAMPLE_TEST tests FERMI_DIRAC_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 April 2016
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

    sample_num = 10000
    test_num = 7

    u_test = np.array([1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 1.0])
    v_test = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.25])

    print('')
    print('FERMI_DIRAC_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  FERMI_DIRAC_SAMPLE samples the Fermi Dirac distribution.')

    for test in range(0, test_num):

        u = u_test[test]
        v = v_test[test]
        seed = 123456789

        print('')
        print('  U =          %g' % (u))
        print('  V =          %g' % (v))

        z = np.zeros(sample_num)
        for i in range(0, sample_num):
            z[i], seed = fermi_dirac_sample(u, v, seed)

        z_max = r8vec_max(sample_num, z)
        z_min = r8vec_min(sample_num, z)

        mean = r8vec_mean(sample_num, z)
        variance = r8vec_variance(sample_num, z)

        print('')
        print('  SAMPLE_NUM =      %d' % (sample_num))
        print('  Sample mean =     %g' % (mean))
        print('  Sample variance = %g' % (variance))
        print('  Maximum value =   %g' % (z_max))
        print('  Minimum value =   %g' % (z_min))
#
#  Terminate.
#
    print('')
    print('FERMI_DIRAC_SAMPLE_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    fermi_dirac_sample_test()
    timestamp()
