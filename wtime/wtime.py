#! /usr/bin/env python3
#
import time

def wtime_test01():

    # *****************************************************************************80
    #
    # WTIME_TEST01 times the NUMPY.RANDOM.RANDOM_SAMPLE() function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 May 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform
    from time import time

    n_log_min = 10
    n_log_max = 22
    n_min = 2 ** n_log_min
    n_max = 2 ** n_log_max
    n_rep = 5
    n_test = 1

    print('')
    print('WTIME_TEST01')
    print('  Python version: %s' % (platform.python_version()))
    print('  Time the RANDOM_SAMPLE function using time():')
    print('')
    print('    x = numpy.random.random_sample ( ( n, 1 ) );')
    print('')
    print('  Data vectors will be of minimum size %d' % (n_min))
    print('  Data vectors will be of maximum size %d' % (n_max))
    print('  Number of repetitions of the operation: %d' % (n_rep))
    print('')
    print('  Timing results in seconds:')
    print('')
    print('      Size         Rep #1         Rep #2         Rep #3        Rep #4         Rep #5')
    print('')

    for n_log in range(n_log_min, n_log_max + 1):

        n = 2 ** (n_log)

        print('  %8d' % (n), end='')

        for i_rep in range(0, n_rep):

            seconds = time()

            x = np.random.random_sample((n, 1))

            seconds = time() - seconds

            print('  %12f' % (seconds), end='')

        print('')
#
#  Terminate.
#
    print('')
    print('WTIME_TEST01')
    print('  Normal end of execution.')
    return


def wtime_test02():

    # *****************************************************************************80
    #
    # WTIME_TEST02 times the NUMPY.RANDOM.RANDOM_SAMPLE() function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    n_log_min = 10
    n_log_max = 22
    n_min = 2 ** n_log_min
    n_max = 2 ** n_log_max
    n_rep = 5
    n_test = 1

    print('')
    print('WTIME_TEST02')
    print('  Python version: %s' % (platform.python_version()))
    print('  Time the RANDOM_SAMPLE function using clock():')
    print('')
    print('    x = numpy.random.random_sample ( ( n, 1 ) );')
    print('')
    print('  Data vectors will be of minimum size %d' % (n_min))
    print('  Data vectors will be of maximum size %d' % (n_max))
    print('  Number of repetitions of the operation: %d' % (n_rep))
    print('')
    print('  Timing results in seconds:')
    print('')
    print('      Size         Rep #1         Rep #2         Rep #3        Rep #4         Rep #5')
    print('')

    for n_log in range(n_log_min, n_log_max + 1):

        n = 2 ** (n_log)

        print('  %8d' % (n), end='')

        for i_rep in range(0, n_rep):

            seconds = time.time()

            x = np.random.random_sample((n, 1))

            seconds = time.time() - seconds

            print('  %12f' % (seconds), end='')

        print('')
#
#  Terminate.
#
    print('')
    print('WTIME_TEST02')
    print('  Normal end of execution.')
    return


def wtime_test():

    # *****************************************************************************80
    #
    # WTIME_TEST tests the WTIME library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 May 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('WTIME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the Python facility for computing wall clock time.')

    wtime_test01()
    wtime_test02()
#
#  Terminate.
#
    print('')
    print('WTIME_TEST:')
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
    wtime_test()
    timestamp()
