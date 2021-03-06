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
from subset.dvec_add import dvec_add
from subset.dvec_print import dvec_print


def dvec_complementx(n, dvec1):

    # *****************************************************************************80
    #
    # DVEC_COMPLEMENTX computes the ten's complement of a DVEC.
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
    #    28 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the length of the vectors.
    #
    #    Input, integer DVEC1(N), the vector to be complemented.
    #
    #    Output, integer DVEC2(N), the ten's complemented vector.
    #

    base = 10

    dvec3 = np.zeros(n, dtype=np.int32)

    for i in range(0, n):
        dvec3[i] = (base - 1) - dvec1[i]

    dvec4 = np.zeros(n, dtype=np.int32)
    dvec4[0] = 1

    dvec2 = dvec_add(n, dvec3, dvec4)

    return dvec2


def dvec_complementx_test():

    # *****************************************************************************80
    #
    # DVEC_COMPLEMENTX_TEST tests DVEC_COMPLEMENTX;
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10
    seed = 123456789
    test_num = 5

    print('')
    print('DVEC_COMPLEMENTX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DVEC_COMPLEMENTX returns the ten\'s complement')
    print('  of a (signed) decimal vector;')

    for test in range(0, test_num):

        i, seed = i4_uniform_ab(-100, 100, seed)

        dvec1 = i4_to_dvec(i, n)

        dvec2 = dvec_complementx(n, dvec1)

        j = dvec_to_i4(n, dvec2)

        print('')
        print('  I = %8d' % (i))
        print('  J = %8d' % (j))

        dvec_print(n, dvec1, '')
        dvec_print(n, dvec2, '')
#
#  Terminate.
#
    print('')
    print('DVEC_COMPLEMENTX_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    dvec_complementx_test()
    timestamp()
