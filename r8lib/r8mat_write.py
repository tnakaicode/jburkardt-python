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


def r8mat_write(filename, m, n, a):

    # *****************************************************************************80
    #
    # R8MAT_WRITE writes an R8MAT to a file.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, string FILENAME, the name of the output file.
    #
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, real A(M,N), the matrix.
    #
    output = open(filename, 'w')

    for i in range(0, m):
        for j in range(0, n):
            s = '\t%g' % (a[i, j])
            output.write(s)
        output.write('\n')

    output.close()


def r8mat_write_test():

    # *****************************************************************************80
    #
    # R8MAT_WRITE_TEST tests R8MAT_WRITE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8MAT_WRITE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test R8MAT_WRITE, which writes an R8MAT to a file.')

    filename = 'r8mat_write_test.txt'
    m = 5
    n = 3
    a = np.array((
        (1.1, 1.2, 1.3),
        (2.1, 2.2, 2.3),
        (3.1, 3.2, 3.3),
        (4.1, 4.2, 4.3),
        (5.1, 5.2, 5.3)))
    r8mat_write(filename, m, n, a)

    print('')
    print('  Created file "%s".' % (filename))
    print('')
    print('R8MAT_WRITE_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    r8mat_write_test()
    timestamp()
