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

from i4lib.i4_choose import i4_choose
from i4lib.i4vec_sum import i4vec_sum
from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write


def mono_total_enum(m, n):

    # *****************************************************************************80
    #
    # MONO_TOTAL_ENUM enumerates monomials in M dimensions of degree equal to N.
    #
    #  Discussion:
    #
    #    For M = 3, we have the following values:
    #
    #    N  VALUE
    #
    #    0    1
    #    1    3
    #    2    6
    #    3   10
    #    4   15
    #    5   21
    #
    #    In particular, VALUE(3,3) = 10 because we have the 10 monomials:
    #
    #      x^3, x^2y, x^2z, xy^2, xyz, xz^3, y^3, y^2z, yz^2, z^3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the maximum degree.
    #
    #    Output, integer VALUE, the number of monomials in M variables,
    #    of total degree N.
    #

    value = i4_choose(n + m - 1, n)

    return value


def mono_total_enum_test():

    # *****************************************************************************80
    #
    # MONO_TOTAL_ENUM_TEST tests MONO_TOTAL_ENUM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('MONO_TOTAL_ENUM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MONO_TOTAL_ENUM can enumerate the number of monomials')
    print('  in M variables, of total degree N.')

    print('')
    print('    N:', end='')
    for n in range(0, 9):
        print('  %4d' % (n), end='')
    print('')
    print('   M +---------------------------------------------------------------')
    for m in range(1, 9):
        print('  %2d |' % (m), end='')
        for n in range(0, 9):
            v = mono_total_enum(m, n)
            print('  %4d' % (v), end='')
        print('')
#
#  Terminate
#
    print('')
    print('MONO_TOTAL_ENUM_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    mono_total_enum_test()
    timestamp()
