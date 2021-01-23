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


def r8vec_transpose_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_TRANSPOSE_PRINT prints an R8VEC "transposed".
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Example:
    #
    #    A = (/ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 /)
    #    TITLE = 'My vector:  '
    #
    #    My vector:   1.0    2.1    3.2    4.3    5.4
    #                 6.5    7.6    8.7    9.8   10.9
    #                11.0
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 September 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of components of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #

    title_length = len(title)

    for ilo in range(0, n, 5):

        if (ilo == 0):
            print(title, end='')
        else:
            blanks = ''
            for i in range(0, title_length):
                blanks = blanks + ' '
            print(blanks, end='')

        print('  ', end='')
        ihi = min(ilo + 5 - 1, n - 1)

        for i in range(ilo, ihi + 1):
            print('  %12g' % (a[i]), end='')
        print('')


def r8vec_transpose_print_test():

    # *****************************************************************************80
    #
    # R8VEC_TRANSPOSE_PRINT_TEST tests R8VEC_TRANSPOSE_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 August 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 11

    print('')
    print('R8VEC_TRANSPOSE_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_TRANSPOSE_PRINT prints an R8VEC "tranposed",')
    print('  that is, placing multiple entries on a line.')

    x = np.array([1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0])
    r8vec_transpose_print(n, x, '  The vector X:')

    print('')
    print('R8VEC_TRANSPOSE_PRINT_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    r8vec_transpose_print_test()
    timestamp()
