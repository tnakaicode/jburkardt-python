#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp

from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write


def ui4_to_ubvec(ui4, n):

    # *****************************************************************************80
    #
    # UI4_TO_UBVEC makes a unsigned binary vector from an integer.
    #
    #  Discussion:
    #
    #    A UBVEC is an integer vector of binary digits, intended to
    #    represent a nonnegative integer.  BVEC(1) is the units digit, BVEC(N)
    #    is the coefficient of 2**(N-1).
    #
    #    To guarantee that there will be enough space for any
    #    value of I, it would be necessary to set N = 32.
    #
    #  Example:
    #
    #     I       BVEC         binary
    #    --  ----------------  ------
    #     1  1, 0, 0, 0, 0, 0       1
    #     2  0, 1, 0, 0, 0, 0      10
    #     3  1, 1, 0, 0, 0, 0      11
    #     4  0, 0, 1, 0, 0, 0     100
    #     9  1, 0, 0, 1, 0, 0    1001
    #    -9  1, 1, 1, 0, 1, 1  110111
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer UI4, an integer to be represented.
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Output, integer BVEC(N), the unsigned binary representation.
    #
    import numpy as np

    ubvec = np.zeros(n)

    for i in range(n - 1, -1, -1):
        ubvec[i] = (ui4 % 2)
        ui4 = (ui4 // 2)

    return ubvec


def ui4_to_ubvec_test():

    # *****************************************************************************80
    #
    # UI4_TO_UBVEC_TEST tests UI4_TO_UBVEC;
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10

    print('')
    print('UI4_TO_UBVEC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  UI4_TO_UBVEC converts an unsigned integer to an')
    print('  unsigned binary vector;')
    print('')
    print('  UI4 --> UBVEC  -->  UI4')
    print('')

    for i in range(0, 11):
        bvec = ui4_to_ubvec(i, n)
        i2 = ubvec_to_ui4(n, bvec)
        print('  %2d  ' % (i)),
        for i in range(0, n):
            print('%1d' % (bvec[i])),
        print('  %2d' % (i2))
#
#  Terminate.
#
    print('')
    print('UI4_TO_UBVEC_TEST')
    print('  Normal end of execution.')
    return


def ubvec_to_ui4(n, ubvec):

    # *****************************************************************************80
    #
    # UBVEC_TO_UI4 makes an unsigned integer from an unsigned binary vector.
    #
    #  Discussion:
    #
    #    A UBVEC is an integer vector of binary digits, intended to
    #    represent a nonnegative integer.  UBVEC(1) is the units digit, UBVEC(N)
    #    is the coefficient of 2^(N-1).
    #
    #  Example:
    #
    #    N = 4
    #
    #        UBVEC   binary  I
    #    ----------  -----  --
    #    1  2  3  4
    #    ----------
    #    1, 0, 0, 0       1  1
    #    0, 1, 0, 0      10  2
    #    0, 0, 1, 1      11  3
    #    0, 0, 1, 0     100  4
    #    1, 0, 0, 1    1001  9
    #    1, 1, 1, 1    1111 15
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 November 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, integer UBVEC(N), the binary representation.
    #
    #    Output, integer VALUE, the integer.
    #
    value = 0
    for i in range(0, n):
        value = 2 * value + ubvec[i]

    return value


def ubvec_to_ui4_test():

    # *****************************************************************************80
    #
    # UBVEC_TO_UI4_TEST tests UBVEC_TO_UI4
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 November 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10

    print('')
    print('UBVEC_TO_UI4_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  UBVEC_TO_UI4 converts an unsigned binary vector')
    print('  to an unsigned integer')
    print('')
    print('  UI4 --> UBVEC  -->  UI4')
    print('')

    for ui4 in range(0, 11):
        ubvec = ui4_to_ubvec(ui4, n)
        i2 = ubvec_to_ui4(n, ubvec)
        print('  %2d  ' % (ui4)),
        for j in range(0, n):
            print('%1d' % (ubvec[j])),
        print('  %2d' % (i2))
#
#  Terminate.
#
    print('')
    print('UBVEC_TO_UI4_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    ui4_to_ubvec_test()
    timestamp()
