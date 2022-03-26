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

from r8lib.r8vec import r8vec_uniform_01, r8vec_normal_01, r8vec_uniform_ab, r8vec_normal_01_test, r8vec_uniform_01_test, r8vec_uniform_ab_test
from r8lib.r8vec_print import r8vec_print, r8vec_print_test
from r8lib.r8vec_norm import r8vec_norm, r8vec_norm_test


def r8vec_uniform_unit(m, seed):

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_UNIT generates a random unit vector.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the dimension of the space.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real W(M), a random direction vector,
    #    with unit norm.
    #
    #    Output, integer SEED, a seed for the random number generator.
    #
    #
    #  Get N values from a standard normal distribution.
    #
    w, seed = r8vec_normal_01(m, seed)
#
#  Compute the length of the vector.
#
    norm = r8vec_norm(m, w)
#
#  Normalize the vector.
#
    for i in range(0, m):
        w[i] = w[i] / norm

    return w, seed


def r8vec_uniform_unit_test():

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_UNIT_TEST tests R8VEC_UNIFORM_UNIT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 5

    print('')
    print('R8VEC_UNIFORM_UNIT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_UNIFORM_UNIT returns a random R8VEC')
    print('  on the surface of the unit M sphere.')
    print('')

    seed = 123456789

    for j in range(0, 5):

        x, seed = r8vec_uniform_unit(m, seed)

        r8vec_print(m, x, '  Vector:')
#
#  Terminate.
#
    print('')
    print('R8VEC_UNIFORM_UNIT_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    r8vec_uniform_unit_test()
    timestamp()
