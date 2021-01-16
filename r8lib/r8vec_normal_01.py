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
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8_normal_01 import r8_normal_01


def r8vec_normal_01(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_01 returns a unit pseudonormal R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(N), the vector of pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #

    x = np.zeros(n)

    for i in range(0, n):
        x[i], seed = r8_normal_01(seed)

    return x, seed


def r8vec_normal_01_test():

    # *****************************************************************************80
    #
    # R8VEC_NORMAL_01_TEST tests R8VEC_NORMAL_01.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10
    seed = 123456789

    print('')
    print('R8VEC_NORMAL_01_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_NORMAL_01 returns a vector of Normal 01 values')
    print('')
    print('  SEED = %d' % (seed))

    r, seed = r8vec_normal_01(n, seed)

    r8vec_print(n, r, '  Vector:')
#
#  Terminate.
#
    print('')
    print('R8VEC_NORMAL_01_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    r8vec_normal_01_test()
    timestamp()
