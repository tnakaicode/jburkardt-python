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

from i4lib.i4_modp import i4_modp
from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write


def i4_wrap(ival, ilo, ihi):

    # *****************************************************************************80
    #
    # I4_WRAP forces an integer to lie between given limits by wrapping.
    #
    #  Example:
    #
    #    ILO = 4, IHI = 8
    #
    #    I   Value
    #
    #    -2     8
    #    -1     4
    #     0     5
    #     1     6
    #     2     7
    #     3     8
    #     4     4
    #     5     5
    #     6     6
    #     7     7
    #     8     8
    #     9     4
    #    10     5
    #    11     6
    #    12     7
    #    13     8
    #    14     4
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 May 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer IVAL, an integer value.
    #
    #    Input, integer ILO, IHI, the desired bounds for the integer value.
    #
    #    Output, integer VALUE, a "wrapped" version of IVAL.
    #

    jlo = min(ilo, ihi)
    jhi = max(ilo, ihi)

    wide = jhi - jlo + 1

    if (wide == 1):
        value = jlo

    else:
        value = jlo + i4_modp(ival - jlo, wide)

    return value


def i4_wrap_test():

    # *****************************************************************************80
    #
    # I4_WRAP_TEST tests I4_WRAP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 May 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    ilo = 4
    ihi = 8

    print('')
    print('I4_WRAP_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4_WRAP forces an integer to lie within given limits.')
    print('')
    print('  ILO = %d' % (ilo))
    print('  IHI = %d' % (ihi))
    print('')
    print('     I  I4_WRAP(I)')
    print('')

    for i in range(-10, 21):
        j = i4_wrap(i, ilo, ihi)
        print('  %6d  %6d' % (i, j))

    print('')
    print('I4_WRAP_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    i4_wrap_test()
    timestamp()
