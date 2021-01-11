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


def mono_next_grevlex(m, x):

    # *****************************************************************************80
    #
    # MONO_NEXT_GREVLEX: grevlex next monomial.
    #
    #  Discussion:
    #
    #    Example:
    #
    #    M = 3
    #
    #    #  X(1)  X(2)  X(3)  Degree
    #      +------------------------
    #    1 |  0     0     0        0
    #      |
    #    2 |  0     0     1        1
    #    3 |  0     1     0        1
    #    4 |  1     0     0        1
    #      |
    #    5 |  0     0     2        2
    #    6 |  0     1     1        2
    #    7 |  1     0     1        2
    #    8 |  0     2     0        2
    #    9 |  1     1     0        2
    #   10 |  2     0     0        2
    #      |
    #   11 |  0     0     3        3
    #   12 |  0     1     2        3
    #   13 |  1     0     2        3
    #   14 |  0     2     1        3
    #   15 |  1     1     1        3
    #   16 |  2     0     1        3
    #   17 |  0     3     0        3
    #   18 |  1     2     0        3
    #   19 |  2     1     0        3
    #   20 |  3     0     0        3
    #
    #    Thanks to Stefan Klus for pointing out a discrepancy in a previous
    #    version of this code, 05 February 2015.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer X[M], the current monomial.
    #    The first element is X = [ 0, 0, ..., 0, 0 ].
    #
    #    Output, integer X[M], the next monomial.
    #

    if (i4vec_sum(m, x) < 0):
        print('')
        print('MONO_NEXT_GREVLEX - Fatal error!')
        print('  Input X sums to less than 0.')
        sys.exit('MONO_NEXT_GREVLEX - Fatal error!')
#
#  Seek the first index 0 < I for which 0 < X(I).
#
    j = 0

    for i in range(1, m):
        if (0 < x[i]):
            j = i
            break

    if (j == 0):
        t = x[0]
        x[0] = 0
        x[m - 1] = t + 1
    elif (j < m - 1):
        x[j] = x[j] - 1
        t = x[0] + 1
        x[0] = 0
        x[j - 1] = x[j - 1] + t
    elif (j == m - 1):
        t = x[0]
        x[0] = 0
        x[j - 1] = t + 1
        x[j] = x[j] - 1

    return x


def mono_next_grevlex_test():

    # *****************************************************************************80
    #
    # MONO_NEXT_GREVLEX_TEST tests MONO_NEXT_GREVLEX.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    m = 4

    print('')
    print('MONO_NEXT_GREVLEX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MONO_NEXT_GREVLEX computes the next monomial')
    print('  in M variables in grevlex order.')
    print('')
    print('  Let M =  %d' % (m))

    k = 0
    x = np.zeros(m)

    while (True):

        d = sum(x)
        print('  %2d  %2d  |' % (k, d), end='')
        for i in range(0, m):
            print('  %2d' % x[i], end='')
        print('')

        if (x[0] == 3):
            break
        k = k + 1
        x = mono_next_grevlex(m, x)
#
#  Terminate.
#
    print('')
    print('MONO_NEXT_GREVLEX_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    mono_next_grevlex_test()
    timestamp()
