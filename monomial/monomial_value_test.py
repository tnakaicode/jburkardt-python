#! /usr/bin/env python
#
def monomial_value_test():

    # *****************************************************************************80
    #
    # MONOMIAL_VALUE_TEST tests the MONOMIAL_VALUE library.
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
    from i4vec_print import i4vec_print_test
    from i4vec_transpose_print import i4vec_transpose_print_test
    from i4vec_uniform_ab import i4vec_uniform_ab_test
    from monomial_value import monomial_value_test
    from monomial_value_1d import monomial_value_1d_test
    from r8mat_nint import r8mat_nint_test
    from r8mat_print import r8mat_print_test
    from r8mat_print_some import r8mat_print_some_test
    from r8mat_uniform_ab import r8mat_uniform_ab_test
    from r8vec_uniform_ab import r8vec_uniform_ab_test
    from timestamp import timestamp

    print('')
    print('MONOMIAL_VALUE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the MONOMIAL_VALUE library.')
#
#  Utilities:
#
    i4vec_print_test()
    i4vec_transpose_print_test()
    i4vec_uniform_ab_test()

    r8mat_nint_test()
    r8mat_print_test()
    r8mat_print_some_test()
    r8mat_uniform_ab_test()
    r8vec_uniform_ab_test()
#
#  The library.
#
    monomial_value_test()
    monomial_value_1d_test()
#
#  Terminate.
#
    print('')
    print('MONOMIAL_VALUE_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    monomial_value_test()
    timestamp()
