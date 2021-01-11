#! /usr/bin/env python3
#
def i8lib_test():

    # *****************************************************************************80
    #
    # I8LIB_TEST tests the I8LIB library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('I8LIB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the I8LIB library.')

    i8vec_print_test()

    timestamp_test()
#
#  Terminate.
#
    print('')
    print('I8LIB_TEST:')
    print('  Normal end of execution.')
    return


def i8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # I8VEC_PRINT prints an I8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, integer A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d  %6d' % (i, a[i]))

    return


def i8vec_print_test():

    # *****************************************************************************80
    #
    # I8VEC_PRINT_TEST tests I8VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('I8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I8VEC_PRINT prints an I4VEC.')

    n = 3
    v = np.array([123456789, 1234567890987654321, -7], dtype=np.int64)
    i8vec_print(n, v, '  Here is an I8VEC:')
#
#  Terminate.
#
    print('')
    print('I8VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def timestamp():

    # *****************************************************************************80
    #
    # TIMESTAMP prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import time

    t = time.time()
    print(time.ctime(t))

    return None


def timestamp_test():

    # *****************************************************************************80
    #
    # TIMESTAMP_TEST tests TIMESTAMP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import platform

    print('')
    print('TIMESTAMP_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TIMESTAMP prints a timestamp of the current date and time.')
    print('')

    timestamp()
#
#  Terminate.
#
    print('')
    print('TIMESTAMP_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    i8lib_test()
    timestamp()
