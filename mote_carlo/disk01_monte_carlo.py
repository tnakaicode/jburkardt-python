#! /usr/bin/env python3
#


def disk_monte_carlo_test():

    # *****************************************************************************80
    #
    # DISK_MONTE_CARLO_TEST tests the DISK_MONTE_CARLO library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    from disk01_area import disk01_area_test
    from disk01_monomial_integral import disk01_monomial_integral_test
    from disk01_sample import disk01_sample_test
    from gamma_values import gamma_values_test
    from i4vec_print import i4vec_print_test
    from i4vec_transpose_print import i4vec_transpose_print_test
    from i4vec_uniform_ab import i4vec_uniform_ab_test
    from monomial_value import monomial_value_test
    from r8_gamma import r8_gamma_test
    from r8_normal_01 import r8_normal_01_test
    from r8_uniform_01 import r8_uniform_01_test
    from r8mat_transpose_print import r8mat_transpose_print_test
    from r8mat_transpose_print_some import r8mat_transpose_print_some_test
    from r8mat_uniform_ab import r8mat_uniform_ab_test
    from r8vec_print import r8vec_print_test
    from r8vec_normal_01 import r8vec_normal_01_test

    print('')
    print('DISK_MONTE_CARLO_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the DISK_MONTE_CARLO library.')

    disk01_monomial_integral_test()
    disk01_sample_test()
    monomial_value_test()

    print('')
    print('DISK_MONTE_CARLO_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    disk_monte_carlo_test()
    timestamp()
