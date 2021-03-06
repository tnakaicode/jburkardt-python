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

from i4lib.i4_modp import i4_modp
from subset.chinese_check import chinese_check
from subset.chinese_to_i4 import chinese_to_i4


def i4_to_chinese(j, n, m):

    # *****************************************************************************80
    #
    # I4_TO_CHINESE converts an integer to its Chinese remainder form.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer J, the integer to be converted.
    #
    #    Input, integer N, the number of moduluses.
    #
    #    Input, integer M(N), the moduluses.  These should be positive
    #    and pairwise prime.
    #
    #    Output, integer R(N), the Chinese remainder representation of the integer.
    #

    ierror = chinese_check(n, m)

    if (ierror != 0):
        print('')
        print('I4_TO_CHINESE - Fatal error!')
        print('  The moduluses are not legal.')
        exit('I4_TO_CHINESE - Fatal error!')

    r = np.zeros(n)

    for i in range(0, n):
        r[i] = i4_modp(j, m[i])

    return r


def i4_to_chinese_test():

    # *****************************************************************************80
    #
    # I4_TO_CHINESE_TEST tests I4_TO_CHINESE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 4
    m = np.array([3, 4, 5, 7])

    print('')
    print('I4_TO_CHINESE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4_TO_CHINESE computes the Chinese Remainder')
    print('  representation of an integer.')

    i4vec_print(n, m, '  The moduli:')

    j = 37

    print('')
    print('  The number being analyzed is %d' % (j))

    r = i4_to_chinese(j, n, m)

    i4vec_print(n, r, '  The remainders:')

    j2 = chinese_to_i4(n, m, r)

    print('')
    print('  The reconstructed number is %d' % (j2))

    r = i4_to_chinese(j2, n, m)

    i4vec_print(n, r, '  The remainders of the reconstructed number are:')
#
#  Terminate.
#
    print('')
    print('I4_TO_CHINESE_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    i4_to_chinese_test()
    timestamp()
