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
from timestamp.timestamp import timestamp

from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write


def r8mat_mm(n1, n2, n3, a, b):

    # *****************************************************************************80
    #
    # R8MAT_MM multiplies two R8MAT's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N1, N2, N3, the order of the matrices.
    #
    #    Input, real A(N1,N2), B(N2,N3), the matrices to multiply.
    #
    #    Output, real  C(N1,N3), the product matrix C = A * B.
    #

    c = np.zeros((n1, n3))

    for j in range(0, n3):
        for i in range(0, n1):
            for k in range(0, n2):
                c[i, j] = c[i, j] + a[i, k] * b[k, j]

    return c


def r8mat_mm_test():

    # *****************************************************************************80
    #
    # R8MAT_MM_TEST tests R8MAT_MM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n1 = 4
    n2 = 3
    n3 = n1

    print('')
    print('R8MAT_MM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_MM computes a matrix-matrix product C = A * B;')

    a = np.zeros((n1, n2))

    for i in range(0, n1):
        for j in range(0, n2):

            if (j == 0):
                a[i, j] = 1.0
            elif (i == 0):
                a[i, j] = 0.0
            else:
                a[i, j] = a[i - 1, j - 1] + a[i - 1, j]

    b = np.transpose(a)

    c = r8mat_mm(n1, n2, n3, a, b)

    r8mat_print(n1, n2, a, '  A:')
    r8mat_print(n2, n3, b, '  B:')
    r8mat_print(n1, n3, c, '  C = A*B:')

    print('')
    print('R8MAT_MM_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    r8mat_mm_test()
    timestamp()
