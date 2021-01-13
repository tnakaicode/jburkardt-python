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

from i4lib.i4_uniform_ab import i4_uniform_ab
from i4lib.i4_to_dvec import i4_to_dvec
from i4lib.dvec_to_i4 import dvec_to_i4
from subset.dvec_complementx import dvec_complementx
from subset.dvec_add import dvec_add


def dvec_sub(n, dvec1, dvec2):

    # *****************************************************************************80
    #
    # DVEC_SUB subtracts two decimal vectors.
    #
    #  Discussion:
    #
    #    A DVEC is an integer vector of decimal digits, intended to
    #    represent an integer.  DVEC(1) is the units digit, DVEC(N-1)
    #    is the coefficient of 10**(N-2), and DVEC(N) contains sign
    #    information.  It is 0 if the number is positive, and 1 if
    #    the number is negative.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the length of the vectors.
    #
    #    Input, integer DVEC1(N), DVEC2(N), the vectors to be subtracted.
    #
    #    Output, integer DVEC3(N), the value of DVEC1 - DVEC2.
    #

    dvec4 = dvec_complementx(n, dvec2)

    dvec3 = dvec_add(n, dvec1, dvec4)

    return dvec3


def dvec_sub_test():

    # *****************************************************************************80
    #
    # DVEC_SUB_TEST tests DVEC_SUB;
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10
    seed = 123456789
    test_num = 10

    print('')
    print('DVEC_SUB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DVEC_SUB subtracts decimal vectors representing integers;')
    print('')
    print('        I        J        L = I - J')

    for test in range(0, test_num):

        i, seed = i4_uniform_ab(-100, 100, seed)
        j, seed = i4_uniform_ab(-100, 100, seed)

        print('')
        print('  %8d  %8d' % (i, j))

        l = i - j

        print('  Directly:           %8d' % (l))

        dvec1 = i4_to_dvec(i, n)
        dvec2 = i4_to_dvec(j, n)

        dvec4 = dvec_sub(n, dvec1, dvec2)
        l = dvec_to_i4(n, dvec4)

        print('  DVEC_SUB  %8d' % (l))
#
#  Terminate.
#
    print('')
    print('DVEC_SUB_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    dvec_sub_test()
    timestamp()
