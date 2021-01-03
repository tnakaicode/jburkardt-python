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


def polyomino_embed_list(mr1, nr1, r1, mp1, np1, p1, number):

    # *****************************************************************************80
    #
    # POLYOMINO_EMBED_LIST lists the polyomino embeddings in a region.
    #
    #  Discusion:
    #
    #    A region R is a subset of an MRxNR grid of squares.
    #
    #    A polyomino P is a subset of an MPxNP grid of squares.
    #
    #    Both objects are represented by binary matrices, with the property that
    #    there are no initial or final zero rows or columns.
    #
    #    For this computation, we regard P as a "fixed" polyomino in other words,
    #    no reflections or rotations will be allowed.
    #
    #    An "embedding" of P into R is an offset (MI,NJ) such that
    #      P(I,J) = R(I+MI,J+NJ)
    #      for 1 <= I <= MP, 1 <= J <= NP, and
    #      for 0 <= MI <= MR-MP, 0 <= MJ <= NR-NP.
    #    We can detect an embedding simply by taking what amounts to a kind of
    #    dot product of P with a corresponding subregion of R.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 May 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer MR, NR, the number of rows and columns in the representation
    #    of the region R.
    #
    #    Input, integer R(MR,NR), a matrix of 0's and 1's representing the
    #    region.
    #
    #    Input, integer MP, NP, the number of rows and columns in the representation
    #    of the polyomino P.
    #
    #    Input, integer P(MP,NP), a matrix of 0's and 1's representing the
    #    polyomino.
    #
    #    Input, integer NUMBER, the number of embeddings.
    #
    #    Output, integer EMBED_LIST(NUMBER,2), for each embedding, the I and J
    #    offsets applied to the polyomino P.
    #

    embed_list = np.zeros([number, 2], dtype=np.int32)

    #
    #  Count the 1's in P.
    #
    pr = sum(sum(p1))

    #
    #  For each possible (I,J) coordinate of the upper left corner of a subset of R,
    #  see if it matches P.
    #
    k = 0
    for mi in range(0, mr1 - mp1 + 1):
        for nj in range(0, nr1 - np1 + 1):
            srp = 0
            for i in range(0, mp1):
                for j in range(0, np1):
                    srp = srp + p1[i, j] * r1[i + mi, j + nj]
            if (srp == pr):
                embed_list[k, 0] = mi
                embed_list[k, 1] = nj
                k = k + 1

    return embed_list


def polyomino_embed_list_test():

    # *****************************************************************************80
    #
    # POLYOMINO_EMBED_LIST_TEST tests POLYOMINO_EMBED_LIST.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 May 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('POLYOMINO_EMBED_LIST_TEST:')
    print('  POLYOMINO_EMBED_LIST lists the offsets used')
    print('  to embed a fixed polyomino in a region.')

    mr1 = 4
    nr1 = 4
    r1 = np.array([
        [0, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 1]])
    polyomino_print(mr1, nr1, r1, '  The given region R:')

    mp1 = 3
    np1 = 2
    p1 = np.array([
        [0, 1],
        [0, 1],
        [1, 1]])
    polyomino_print(mp1, np1, p1, '  The given polyomino P:')

    #
    #  Get the number of embeddings.
    #
    number = polyomino_embed_number(mr1, nr1, r1, mp1, np1, p1)

    print('')
    print('  As a fixed polyomino, P can be embedded in R in %d ways' % (number))

    #
    #  Get the list of embeddings.
    #
    embed_list = polyomino_embed_list(mr1, nr1, r1, mp1, np1, p1, number)

    for k in range(0, number):
        mk = embed_list[k, 0]
        nk = embed_list[k, 1]
        mq = mr1
        nq = nr1
        q = r1.copy()
        for i in range(0, mp1):
            for j in range(0, np1):
                q[i + mk, j + nk] = q[i + mk, j + nk] + p1[i, j]
        print('')
        print('  Embedding number %d:' % (k))
        print('')
        for i in range(0, mq):
            for j in range(0, nq):
                print(' %d' % (q[i, j])),
            print('')

    print('')
    print('POLYOMINO_EMBED_LIST_TEST:')
    print('  Normal end of execution.')


def polyomino_embed_number(mr1, nr1, r1, mp1, np1, p1):

    # *****************************************************************************80
    #
    # POLYOMINO_EMBED_NUMBER counts the number of polyomino embeddings in a region.
    #
    #  Discusion:
    #
    #    A region R is a subset of an MRxNR grid of squares.
    #
    #    A polyomino P is a subset of an MPxNP grid of squares.
    #
    #    Both objects are represented by binary matrices, with the property that
    #    there are no initial or final zero rows or columns.
    #
    #    For this computation, we regard P as a "fixed" polyomino in other words,
    #    no reflections or rotations will be allowed.
    #
    #    An "embedding" of P into R is an offset (MI,NJ) such that
    #      P(I,J) = R(I+MI,J+NJ)
    #      for 1 <= I <= MP, 1 <= J <= NP, and
    #      for 0 <= MI <= MR-MP, 0 <= MJ <= NR-NP.
    #    We can detect an embedding simply by taking what amounts to a kind of
    #    dot product of P with a corresponding subregion of R.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 May 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer MR, NR, the number of rows and columns in the representation
    #    of the region R.
    #
    #    Input, integer R(MR,NR), a matrix of 0's and 1's representing the
    #    region.
    #
    #    Input, integer MP, NP, the number of rows and columns in the representation
    #    of the polyomino P.
    #
    #    Input, integer P(MP,NP), a matrix of 0's and 1's representing the
    #    polyomino.
    #
    #    Output, integer NUMBER, the number of distinct embeddings of P into R.
    #
    number = 0

    #
    #  Count the 1's in P.
    #
    pr = sum(sum(p1))

    #
    #  For each possible (I,J) coordinate of the upper left corner of a subset of R,
    #  see if it matches P.
    #
    for mi in range(0, mr1 - mp1 + 1):
        for nj in range(0, nr1 - np1 + 1):
            srp = 0
            for i in range(0, mp1):
                for j in range(0, np1):
                    srp = srp + p1[i, j] * r1[i + mi, j + nj]
            if (srp == pr):
                number = number + 1

    return number


def polyomino_embed_number_test():

    # *****************************************************************************80
    #
    # POLYOMINO_EMBED_NUMBER_TEST tests POLYOMINO_EMBED_NUMBER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 May 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('POLYOMINO_EMBED_NUMBER_TEST:')
    print('  POLYOMINO_EMBED_NUMBER reports the number of ways a')
    print('  fixed polyomino can be embedded in a region.')

    mr1 = 4
    nr1 = 4
    r1 = np.array([
        [0, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 1]])
    polyomino_print(mr1, nr1, r1, '  The given region R:')

    mp1 = 3
    np1 = 2
    p1 = np.array([
        [0, 1],
        [0, 1],
        [1, 1]])
    polyomino_print(mp1, np1, p1, '  The given polyomino P:')

    number = polyomino_embed_number(mr1, nr1, r1, mp1, np1, p1)

    print('')
    print('  As a fixed polyomino, P can be embedded in R in %d ways.' % (number))
    print('')
    print('POLYOMINO_EMBED_NUMBER_TEST:')
    print('  Normal end of execution.')


def polyomino_embed_test():

    # *****************************************************************************80
    #
    # POLYOMINO_TEMBED_TEST tests POLYOMINO_EMBED.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 May 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('POLYOMINO_EMBED_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the POLYOMINO_EMBED library.')

    polyomino_embed_number_test()
    polyomino_embed_list_test()

    print('')
    print('POLYOMINO_EMBED_TEST:')
    print('  Normal end of execution.')
    print('')


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


if (__name__ == '__main__'):
    timestamp()
    polyomino_embed_test()
    timestamp()
