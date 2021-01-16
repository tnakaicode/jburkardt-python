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
    #    05 July 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform
    import numpy as np

    from disk_area import disk_area_test
    from disk_sample import disk_sample_test

    print('')
    print('DISK_MONTE_CARLO_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the DISK_MONTE_CARLO library.')

    disk_area_test()

    center = np.zeros(2)
    center = np.array([0.0, 0.0])
    r = 1.0
    disk_sample_test(center, r)

    center = np.zeros(2)
    center = np.array([1.0, 0.0])
    r = 1.0
    disk_sample_test(center, r)

    center = np.zeros(2)
    center = np.array([1.0, 2.0])
    r = 3.0
    disk_sample_test(center, r)
#
#  Terminate.
#
    print('')
    print('DISK_MONTE_CARLO_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    disk_monte_carlo_test()
    timestamp()
