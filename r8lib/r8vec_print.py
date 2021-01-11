#! /usr/bin/env python
#
def r8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_PRINT prints an R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d:  %12g' % (i, a[i]))

    return


def r8vec_print_test():

    # *****************************************************************************80
    #
    # R8VEC_PRINT_TEST tests R8VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_PRINT prints an R8VEC.')

    n = 4
    v = np.array([123.456, 0.000005, -1.0E+06, 3.14159265], dtype=np.float64)
    r8vec_print(n, v, '  Here is an R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def r8vec_print_some(n, a, max_print, title):

    # *****************************************************************************80
    #
    # R8VEC_PRINT_SOME prints "some" of an R8VEC.
    #
    #  Discussion:
    #
    #    The user specifies MAX_PRINT, the maximum number of lines to print.
    #
    #    If N, the size of the vector, is no more than MAX_PRINT, then
    #    the entire vector is printed, one entry per line.
    #
    #    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
    #    followed by a line of periods suggesting an omission,
    #    and the last entry.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, integer MAX_PRINT, the maximum number of lines
    #    to print.
    #
    #    Input, string TITLE, a title.
    #
    if (max_print <= 0):
        return

    if (n <= 0):
        return

    print('')
    print(title)
    print('')

    if (n <= max_print):

        for i in range(0, n):
            print('  %6d  %14g' % (i, a[i]))

    elif (3 <= max_print):

        for i in range(0, max_print - 2):
            print('  %6d  %14g' % (i, a[i]))
        print('  ......  ..............')
        i = n - 1
        print('  %6d  %14g' % (i, a[i]))

    else:

        for i in range(0, max_print - 1):
            print('  %6d  %14g' % (i, a[i]))
        i = max_print - 1
        print('  %6d  %14g  ...more entries...' % (i, a[i]))

    return


def r8vec_print_some_test():

    # *****************************************************************************80
    #
    # R8VEC_PRINT_SOME_TEST tests R8VEC_PRINT_SOME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 February 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform
    from r8vec_indicator1 import r8vec_indicator1

    print('')
    print('R8VEC_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_PRINT_SOME prints some of an R8VEC.')

    n = 100
    a = r8vec_indicator1(n)

    max_print = 10

    r8vec_print_some(
        n, a, max_print, '  No more than 10 lines of this vector:')
#
#  Terminate.
#
    print('')
    print('R8VEC_PRINT_SOME_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    r8vec_print_test()
    timestamp()
