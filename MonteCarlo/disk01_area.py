#! /usr/bin/env python3
#


def disk01_area():

    # *****************************************************************************80
    #
    # DISK01_AREA returns the area of the unit disk.
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
    #  Parameters:
    #
    #    Output, real AREA, the area of the unit disk.
    #
    import numpy as np

    r = 1.0
    value = np.pi * r * r

    return value


def disk01_area_test():

    # *****************************************************************************80
    #
    # DISK01_AREA tests DISK01_AREA.
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

    print('')
    print('DISK01_AREA_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DISK01_AREA returns the area of the unit disk.')

    value = disk01_area()

    print('')
    print('  DISK01_AREA() = %g' % (value))
#
#  Terminate.
#
    print('')
    print('DISK01_AREA_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    disk01_area_test()
    timestamp()
