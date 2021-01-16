#! /usr/bin/env python3
#


def disk_area(center, r):

    # *****************************************************************************80
    #
    # DISK_AREA returns the area of a general disk.
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
    #  Parameters:
    #
    #    Input, real CENTER(2), the center of the disk.
    #    This information is not needed for the area calculation.
    #
    #    Input, real R, the radius of the disk.
    #
    #    Output, real AREA, the area of the unit disk.
    #
    import numpy as np

    value = np.pi * r * r

    return value


def disk_area_test():

    # *****************************************************************************80
    #
    # DISK_AREA tests DISK_AREA.
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
    import numpy as np
    import platform
    from r8vec_uniform_01 import r8vec_uniform_01

    print('')
    print('DISK_AREA_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DISK_AREA returns the area of the unit disk.')

    seed = 123456789
    center = np.zeros(2)

    print('')
    print('  (   CX        CY     )    R          Area')
    print('')

    for i in range(0, 10):
        data, seed = r8vec_uniform_01(3, seed)
        center[0] = 10.0 * data[0] - 5.0
        center[1] = 10.0 * data[1] - 5.0
        r = data[2]
        area = disk_area(center, r)
        print('  (%9.6f,%9.6f)  %9.6f  %9.6f'
              % (center[0], center[1], r, area))
#
#  Terminate.
#
    print('')
    print('DISK_AREA_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    disk_area_test()
    timestamp()
