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
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8mat_transpose_print import r8mat_transpose_print

from r8lib.r8_normal_ab import r8_normal_01, r8vec_normal_01, r8mat_normal_01
from r8lib.r8_uniform_ab import r8_uniform_01, r8vec_uniform_01, r8mat_uniform_01


def uniform_in_sphere01_map(m, n, seed):

    #
    # UNIFORM_IN_SPHERE01_MAP maps uniform points in the unit M-dimensional sphere.
    #
    #  Discussion:
    #
    #    The sphere has center 0 and radius 1.
    #
    #    We first generate a point ON the sphere, and then distribute it
    #    IN the sphere.
    #
    #  Reference:
    #
    #    Russell Cheng,
    #    Random Variate Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998, pages 168.
    #
    #    Reuven Rubinstein,
    #    Monte Carlo Optimization, Simulation, and Sensitivity
    #    of Queueing Networks,
    #    Wiley, 1986, page 232.
    #
    #  Parameters:
    #
    #    Input, integer M, the dimension of the space.
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(M,N), the points.
    #
    exponent = 1.0 / float(m)
    x = np.zeros([m, n])
    for j in range(0, n):
        #
        #  Fill a vector with normally distributed values.
        #
        v, seed = r8vec_normal_01(m, seed)

        #
        #  Compute the length of the vector.
        #
        norm = np.linalg.norm(v)

        #
        #  Normalize the vector.
        #
        v[0:m] = v[0:m] / norm

        #
        #  Now compute a value to map the point ON the sphere INTO the sphere.
        #
        r, seed = r8_uniform_01(seed)

        x[0:m, j] = r ** exponent * v[0:m]

    return x, seed


def uniform_in_sphere01_map_test():

    # *****************************************************************************80
    #
    # UNIFORM_IN_SPHERE01_MAP_TEST tests UNIFORM_IN_SPHERE01_MAP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('UNIFORM_IN_SPHERE01_MAP_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  UNIFORM_IN_SPHERE01_MAP computes points uniformly distributed')
    print('  inside the M-dimensional unit sphere.')

    m = 3
    n = 10
    seed = 123456789

    x, seed = uniform_in_sphere01_map(m, n, seed)
    r8mat_transpose_print(m, n, x, '  Random points inside unit 3-sphere')

    print('')
    print('UNIFORM_IN_SPHERE01_MAP_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    uniform_in_sphere01_map_test()
    timestamp()
