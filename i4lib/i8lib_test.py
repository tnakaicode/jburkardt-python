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


def i8lib_test():

    # *****************************************************************************80
    #
    # I8LIB_TEST tests the I8LIB library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('I8LIB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the I8LIB library.')

    i8vec_print_test()

    print('')
    print('I8LIB_TEST:')
    print('  Normal end of execution.')


def i8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # I8VEC_PRINT prints an I8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, integer A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d  %6d' % (i, a[i]))


def i8vec_print_test():

    # *****************************************************************************80
    #
    # I8VEC_PRINT_TEST tests I8VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('I8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I8VEC_PRINT prints an I4VEC.')

    n = 3
    v = np.array([123456789, 1234567890987654321, -7], dtype=np.int64)
    i8vec_print(n, v, '  Here is an I8VEC:')

    print('')
    print('I8VEC_PRINT_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    i8lib_test()
    timestamp()
