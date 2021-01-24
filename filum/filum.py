#! /usr/bin/env python3
#
def file_column_count(filename):

    # *****************************************************************************80
    #
    # FILE_COLUMN_COUNT counts the number of words in a typical column of a file.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, string FILENAME, the name of the file.
    #
    #    Output, integer COLUMN_COUNT, the number of words in a typical column.
    #
    column_count = -1

    input = open(filename, 'r')

    column_count = 0

    for line in input:

        if (line[0] == '#'):
            continue
        else:

            wc = 0
            for word in line.strip().split():
                wc = wc + 1

            if (wc == 0):
                continue
            elif (column_count == 0):
                column_count = wc
                break

    input.close()

    return column_count


def file_column_count_test():

    # *****************************************************************************80
    #
    # FILE_COLUMN_COUNT_TEST tests FILE_COLUMN_COUNT.
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
    import platform

    print('')
    print('FILE_COLUMN_COUNT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Count the number of columns in a typical text file line.')

    filename = 'r8mat_write_test.txt'
    column_count = file_column_count(filename)

    print('')
    print('  Number of columns in "%s" is %d' % (filename, column_count))
#
#  Terminate.
#
    print('')
    print('FILE_COLUMN_COUNT_TEST:')
    print('  Normal end of execution.')
    return


def file_row_count(filename):

    # *****************************************************************************80
    #
    # FILE_ROW_COUNT counts the number of rows (lines) in a file.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, string FILENAME, the name of the file.
    #
    #    Output, integer ROW_COUNT, the number of rows in the file.
    #
    row_count = -1

    input = open(filename, 'r')

    row_count = 0

    for line in input:

        if (line[0] == '#'):
            continue
        else:

            wc = 0
            for word in line.strip().split():
                wc = wc + 1

            if (wc == 0):
                continue
            else:
                row_count = row_count + 1

    input.close()

    return row_count


def file_row_count_test():

    # *****************************************************************************80
    #
    # FILE_ROW_COUNT_TEST tests FILE_ROW_COUNT.
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
    import platform

    print('')
    print('FILE_ROW_COUNT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Count the number of rows in a text file.')

    filename = 'i4mat_write_test.txt'
    row_count = file_row_count(filename)

    print('')
    print('  Number of rows in "%s" is %d' % (filename, row_count))
#
#  Terminate.
#
    print('')
    print('FILE_ROW_COUNT_TEST:')
    print('  Normal end of execution.')
    return


def filum_test():

    # *****************************************************************************80
    #
    # FILUM_TEST tests the FILUM library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 September 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('FILUM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the FILUM library.')

    file_column_count_test()
    file_row_count_test()
    print('')
    print('FILUM_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    filum_test()
    timestamp()
