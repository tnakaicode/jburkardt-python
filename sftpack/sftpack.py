#! /usr/bin/env python3
#
def sftpack_test():

    # *****************************************************************************80
    #
    # SFTPACK_TEST tests the SFTPACK library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform
    from c8mat_print import c8mat_print_test
    from c8mat_print_some import c8mat_print_some_test
    from c8mat_sft import c8mat_sft_test
    from c8mat_uniform_01 import c8mat_uniform_01_test
    from c8vec_indicator import c8vec_indicator_test
    from c8vec_print import c8vec_print_test
    from c8vec_print_part import c8vec_print_part_test
    from c8vec_sft import c8vec_sft_test
    from c8vec_uniform_01 import c8vec_uniform_01_test
    from i4_modp import i4_modp_test
    from i4_wrap import i4_wrap_test
    from r8vec_indicator1 import r8vec_indicator1_test
    from r8vec_print import r8vec_print_test
    from r8vec_print_part import r8vec_print_part_test
    from r8vec_sct import r8vec_sct_test
    from r8vec_sft import r8vec_sft_test
    from r8vec_sht import r8vec_sht_test
    from r8vec_sqct import r8vec_sqct_test
    from r8vec_sqst import r8vec_sqst_test
    from r8vec_sst import r8vec_sst_test
    from r8vec_swt import r8vec_swt_test
    from r8vec_uniform_ab import r8vec_uniform_ab_test

    print('')
    print('SFTPACK_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the SFTPACK library.')
    #
    #  Utility functions.
    #
    # c8mat_print_test()
    # c8mat_print_some_test()
    # c8mat_uniform_01_test()
    # c8vec_indicator_test()
    # c8vec_print_test()
    # c8vec_print_part_test()
    # c8vec_uniform_01_test()
    # i4_modp_test()
    # i4_wrap_test()
    # r8vec_indicator1_test()
    # r8vec_print_test()
    # r8vec_print_part_test()
    # r8vec_uniform_ab_test()

    #
    #  Library functions.
    #
    c8mat_sft_test()
    c8vec_sft_test()

    r8vec_sct_test()
    r8vec_sft_test()
    r8vec_sht_test()
    r8vec_sqct_test()
    r8vec_sqst_test()
    r8vec_sst_test()
    r8vec_swt_test()
    
    #
    #  Terminate.
    #
    print('')
    print('SFTPACK_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    sftpack_test()
    timestamp()
