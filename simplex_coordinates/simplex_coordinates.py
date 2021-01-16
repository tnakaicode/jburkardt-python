#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from mpi4py import MPI
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
from r8lib.r8mat_transpose_print import r8mat_transpose_print, r8mat_transpose_print_some
from r8lib.r8_factorial import r8_factorial, r8_factorial_values


def simplex01_volume(m):

    # *****************************************************************************80
    #
    # SIMPLEX01_VOLUME returns the volume of the unit simplex in M dimensions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 January 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Output, real VALUE, the volume.
    #
    value = 1.0
    for i in range(1, m + 1):
        value = value / float(i)

    return value


def simplex01_volume_test():

    # *****************************************************************************80
    #
    # SIMPLEX01_VOLUME_TEST tests SIMPLEX01_VOLUME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('SIMPLEX01_VOLUME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SIMPLEX01_VOLUME returns the volume of the unit simplex')
    print('  in M dimensions.')
    print('')
    print('   M   Volume')
    print('')

    for m in range(1, 10):
        value = simplex01_volume(m)
        print('  %2d  %g' % (m, value))

    print('')
    print('SIMPLEX01_VOLUME_TEST')
    print('  Normal end of execution.')


def simplex_coordinates1(m):

    # *****************************************************************************80
    #
    # SIMPLEX_COORDINATES1 computes the Cartesian coordinates of simplex vertices.
    #
    #  Discussion:
    #
    #    The simplex will have its centroid at 0
    #
    #    The sum of the vertices will be zero.
    #
    #    The distance of each vertex from the origin will be 1.
    #
    #    The length of each edge will be constant.
    #
    #    The dot product of the vectors defining any two vertices will be - 1 / M.
    #    This also means the angle subtended by the vectors from the origin
    #    to any two distinct vertices will be arccos ( - 1 / M ).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Output, real X(M,M+1), the coordinates of the vertices
    #    of a simplex in M dimensions.
    #

    x = np.zeros([m, m + 1])

    for k in range(0, m):

        #
        #  Set X(K,K) so that sum ( X(1:K,K)^2 ) = 1.
        #
        s = 0.0
        for i in range(0, k):
            s = s + x[i, k] ** 2
        x[k, k] = np.sqrt(1.0 - s)

        #
        #  Set X(K,J) for J = K+1 to M+1 by using the fact that XK dot XJ = - 1 / M.
        #
        for j in range(k + 1, m + 1):
            s = 0.0
            for i in range(0, k):
                s = s + x[i, k] * x[i, j]

            x[k, j] = (- 1.0 / float(m) - s) / x[k, k]

    return x


def simplex_coordinates1_test(m):

    # *****************************************************************************80
    #
    # SIMPLEX_COORDINATES1_TEST tests SIMPLEX_COORDINATES1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #

    print('')
    print('SIMPLEX_COORDINATES1_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test SIMPLEX_COORDINATES1')

    x = simplex_coordinates1(m)
    r8mat_transpose_print(m, m + 1, x, '  Simplex vertex coordinates:')

    s = 0.0
    for i in range(0, m):
        s = s + (x[i, 0] - x[i, 1]) ** 2

    side = np.sqrt(s)
    volume = simplex_volume(m, x)
    volume2 = np.sqrt(m + 1) / r8_factorial(m) \
        / np.sqrt(2.0 ** m) * side ** m

    print('')
    print('  Side length =     %g' % (side))
    print('  Volume =          %g' % (volume))
    print('  Expected volume = %g' % (volume2))

    xtx = np.dot(np.transpose(x), x)
    r8mat_transpose_print(m + 1, m + 1, xtx, '  Dot product matrix:')

    print('')
    print('SIMPLEX_COORDINATES1_TEST')
    print('  Normal end of execution.')


def simplex_coordinates2(m):

    # *****************************************************************************80
    #
    # SIMPLEX_COORDINATES2 computes the Cartesian coordinates of simplex vertices.
    #
    #  Discussion:
    #
    #    This routine uses a simple approach to determining the coordinates of
    #    the vertices of a regular simplex in n dimensions.
    #
    #    We want the vertices of the simplex to satisfy the following conditions:
    #
    #    1) The centroid, or average of the vertices, is 0.
    #    2) The distance of each vertex from the centroid is 1.
    #       By 1), this is equivalent to requiring that the sum of the squares
    #       of the coordinates of any vertex be 1.
    #    3) The distance between any pair of vertices is equal (and is not zero.)
    #    4) The dot product of any two coordinate vectors for distinct vertices
    #       is -1/M; equivalently, the angle subtended by two distinct vertices
    #       from the centroid is arccos ( -1/M).
    #
    #    Note that if we choose the first M vertices to be the columns of the
    #    MxM identity matrix, we are almost there.  By symmetry, the last column
    #    must have all entries equal to some value A.  Because the square of the
    #    distance between the last column and any other column must be 2 (because
    #    that's the distance between any pair of columns), we deduce that
    #    (A-1)^2 + (M-1)*A^2 = 2, hence A = (1-sqrt(1+M))/M.  Now compute the
    #    centroid C of the vertices, and subtract that, to center the simplex
    #    around the origin.  Finally, compute the norm of one column, and rescale
    #    the matrix of coordinates so each vertex has unit distance from the origin.
    #
    #    This approach devised by John Burkardt, 19 September 2010.  What,
    #    I'm not the first?
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Output, real X(M,M+1), the coordinates of the vertices
    #    of a simplex in M dimensions.
    #

    x = np.zeros([m, m + 1])
    for j in range(0, m):
        x[j, j] = 1.0

    a = (1.0 - np.sqrt(float(1 + m))) / float(m)
    for i in range(0, m):
        x[i, m] = a

    #
    #  Adjust coordinates so the centroid is at zero.
    #
    c = np.zeros(m)
    for i in range(0, m):
        s = 0.0
        for j in range(0, m + 1):
            s = s + x[i, j]
        c[i] = s / float(m + 1)

    for j in range(0, m + 1):
        for i in range(0, m):
            x[i, j] = x[i, j] - c[i]

    #
    #  Scale so each column has norm 1.
    #
    s = 0.0
    for i in range(0, m):
        s = s + x[i, 0] ** 2
    s = np.sqrt(s)

    for j in range(0, m + 1):
        for i in range(0, m):
            x[i, j] = x[i, j] / s

    return x


def simplex_coordinates2_test(m):

    # *****************************************************************************80
    #
    # SIMPLEX_COORDINATES2_TEST tests SIMPLEX_COORDINATES2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #

    print('')
    print('SIMPLEX_COORDINATES2_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test SIMPLEX_COORDINATES2')

    x = simplex_coordinates2(m)
    r8mat_transpose_print(m, m + 1, x, '  Simplex vertex coordinates:')

    s = 0.0
    for i in range(0, m):
        s = s + (x[i, 0] - x[i, 1]) ** 2

    side = np.sqrt(s)
    volume = simplex_volume(m, x)
    volume2 = np.sqrt(m + 1) / r8_factorial(m) \
        / np.sqrt(2.0 ** m) * side ** m

    print('')
    print('  Side length =     %g' % (side))
    print('  Volume =          %g' % (volume))
    print('  Expected volume = %g' % (volume2))

    xtx = np.dot(np.transpose(x), x)
    r8mat_transpose_print(m + 1, m + 1, xtx, '  Dot product matrix:')

    print('')
    print('SIMPLEX_COORDINATES2_TEST')
    print('  Normal end of execution.')


def simplex_coordinates_test():

    # *****************************************************************************80
    #
    # SIMPLEX_COORDINATES_TEST tests the SIMPLEX_COORDINATES library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('SIMPLEX_COORDINATES_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the SIMPLEX_COORDINATES library.')

    simplex_coordinates1_test(3)
    simplex_coordinates1_test(4)
    simplex_coordinates2_test(3)
    simplex_coordinates2_test(4)
    simplex_volume_test()
    simplex01_volume_test()

    print('')
    print('SIMPLEX_COORDINATES_TEST:')
    print('  Normal end of execution.')


def simplex_volume(m, x):

    # *****************************************************************************80
    #
    # SIMPLEX_VOLUME computes the volume of a simplex.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, real X(M,M+1), the coordinates of the vertices
    #    of a simplex in M dimensions.
    #
    #    Output, real VOLUME, the volume of the simplex.
    #

    a = np.zeros([m, m])
    for j in range(0, m):
        for i in range(0, m):
            a[i, j] = x[i, j] - x[i, m]

    volume = abs(np.linalg.det(a))
    volume01 = simplex01_volume(m)
    volume = volume * volume01

    return volume


def simplex_volume_test():

    # *****************************************************************************80
    #
    # SIMPLEX_VOLUME_TEST tests SIMPLEX_VOLUME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('SIMPLEX_VOLUME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SIMPLEX_VOLUME returns the volume of a simplex')
    print('  in M dimensions.')

    m = 2
    x2 = np.array([
        [0.0, 7.0, 4.0],
        [0.0, 2.0, 4.0]])
    r8mat_transpose_print(m, m + 1, x2, '  Triangle:')
    value = simplex_volume(m, x2)

    print('')
    print('  Volume = %g' % (value))

    m = 3
    x3 = np.array([
        [0.0, 7.0, 4.0, 0.0],
        [0.0, 2.0, 4.0, 0.0],
        [0.0, 0.0, 0.0, 6.0]])
    r8mat_transpose_print(m, m + 1, x3, '  Tetrahedron:')
    value = simplex_volume(m, x3)

    print('')
    print('  Volume = %g' % (value))
    print('')
    print('SIMPLEX_VOLUME_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    simplex_coordinates_test()
    timestamp()
