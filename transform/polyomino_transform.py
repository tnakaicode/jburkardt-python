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


def polyomino_transform(m, n, p, rotate, reflect):

    # *****************************************************************************80
    #
    # POLYOMINO_TRANSFORM transforms a polyomino.
    #
    #  Discussion:
    #
    #    A polyomino can be rotated or reflected.
    #
    #    This program is given a polyomino and returns the resulting polyomino
    #    after the specified reflection and rotation.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns in the representation
    #    of the polyomino P.
    #
    #    Input, integer P(M,N), a matrix of 0's and 1's representing the
    #    polyomino.  The matrix should be "tight", that is, there should be a
    #    1 in row 1, and in column 1, and in row M, and in column N.
    #
    #    Input, integer ROTATE, is 0, 1, 2, or 3, the number of 90 degree
    #    counterclockwise rotations to be applied.
    #
    #    Input, integer REFLECT, is 0 or 1.  If it is 1, then each row of the
    #    polyomino matrix is to be reflected before any rotations are performed.
    #
    #    Output, integer MQ, NQ, the number of rows and columns of the
    #    representation of the transformed polyomino
    #
    #    Output, integer Q(MQ,NQ), the representation of the transformed
    #    polyomino.
    #

    mq = m
    nq = n
    q = np.copy(p)

    reflect = (reflect % 2)

    if (reflect == 1):
        q = i4mat_flip_cols(mq, nq, q)

    rotate = (rotate % 4)

    for k in range(0, rotate):
        q = i4mat_transpose(mq, nq, q)
        r = mq
        s = nq
        mq = s
        nq = r

        q = i4mat_flip_rows(mq, nq, q)

    return mq, nq, q


def i4mat_flip_cols(m, n, a):

    # *****************************************************************************80
    #
    # I4MAT_FLIP_COLS swaps the columns of an I4MAT.
    #
    #  Discussion:
    #
    #    An I4MAT is an M by N array of I4's.
    #
    #    To "flip" the columns of an I4MAT is to start with something like
    #
    #      11 12 13 14 15
    #      21 22 23 24 25
    #      31 32 33 34 35
    #      41 42 43 44 45
    #      51 52 53 54 55
    #
    #    and return
    #
    #      15 14 13 12 11
    #      25 24 23 22 21
    #      35 34 33 32 31
    #      45 44 43 42 41
    #      55 54 53 52 51
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns.
    #
    #    Input, integer A(M,N), the matrix to be flipped.
    #
    #    Output, integer B(M,N), the flipped matrix.
    #

    b = np.zeros([m, n], dtype=np.int32)

    for i in range(0, m):
        for j in range(0, n):
            b[i, j] = a[i, n - 1 - j]

    return b


def i4mat_flip_rows(m, n, a):

    # *****************************************************************************80
    #
    # I4MAT_FLIP_ROWS swaps the rows of an I4MAT.
    #
    #  Discussion:
    #
    #    An I4MAT is an M by N array of I4's.
    #
    #    To "flip" the rows of an I4MAT is to start with something like
    #
    #      11 12 13 14 15
    #      21 22 23 24 25
    #      31 32 33 34 35
    #      41 42 43 44 45
    #      51 52 53 54 55
    #
    #    and return
    #
    #      51 52 53 54 55
    #      41 42 43 44 45
    #      31 32 33 34 35
    #      21 22 23 24 25
    #      11 12 13 14 15
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns.
    #
    #    Input, integer A(M,N), the matrix to be flipped.
    #
    #    Output, integer B(M,N), the flipped matrix.
    #

    b = np.zeros([m, n], dtype=np.int32)

    for i in range(0, m):
        for j in range(0, n):
            b[i, j] = a[m - 1 - i, j]

    return b


def i4mat_transpose(m, n, a):

    # *****************************************************************************80
    #
    # I4MAT_TRANSPOSE transposes an I4MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns.
    #
    #    Input, integer A(M,N), the matrix to be flipped.
    #
    #    Output, integer B(N,M), the transposed matrix.
    #

    b = np.zeros([n, m], dtype=np.int32)

    for i in range(0, m):
        for j in range(0, n):
            b[j, i] = a[i, j]

    return b


def polyomino_print(m, n, p, label):

    # *****************************************************************************80
    #
    # POLYOMINO_PRINT prints a polyomino.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Local parameters:
    #
    #    Input, integer M, N, the number of rows and columns in the representation
    #    of the polyomino P.
    #
    #    Input, integer P(M,N), a matrix of 0's and 1's representing the
    #    polyomino.  The matrix should be "tight", that is, there should be a
    #    1 in row 1, and in column 1, and in row M, and in column N.
    #
    #    Input, string LABEL, a title for the polyomino.
    #
    print('')
    print(label)
    print('')
    if (m <= 0 or n <= 0):
        print('  [ Null matrix ]')
    else:
        for i in range(0, m):
            for j in range(0, n):
                print(' %d' % (p[i, j])),
            print('')

    return


def polyomino_transform_test():

    # *****************************************************************************80
    #
    # POLYOMINO_TRANSFORM_TEST tests POLYOMINO_TRANSFORM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Local parameters:
    #
    #    Input, integer M, N, the number of rows and columns in the representation
    #    of the polyomino P.
    #
    #    Input, integer P(M,N), a matrix of 0's and 1's representing the
    #    polyomino.  The matrix should be "tight", that is, there should be a
    #    1 in row 1, and in column 1, and in row M, and in column N.
    #

    print('')
    print('POLYOMINO_TRANSFORM_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYOMINO_TRANSFORM can transform a polyomino.')
    print('  Generate all 8 combinations of rotation and reflection')
    print('  applied to a polyomino represented by a binary matrix.')

    m = 3
    n = 3
    p = np.array([
        [0, 1, 1],
        [1, 1, 0],
        [0, 1, 0]])

    polyomino_print(m, n, p, '  The given polyomino P')

    for reflect in range(0, 2):
        for rotate in range(0, 4):
            mq, nq, q = polyomino_transform(m, n, p, rotate, reflect)
            label = '  P after %d reflections and %d rotations:' % (
                reflect, rotate)
            polyomino_print(mq, nq, q, label)

    print('')
    print('POLYOMINO_TRANSFORM_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    polyomino_transform_test()
    timestamp()
