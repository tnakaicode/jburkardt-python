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


def polyomino_condense(mp1, np1, p1):

    # *****************************************************************************80
    #
    # POLYOMINO_CONDENSE condenses a polyomino.
    #
    #  Discussion:
    #
    #    A polyomino is a shape formed by connecting unit squares edgewise.
    #
    #    A polyomino can be represented by an MxN matrix, whose entries are
    #    1 for squares that are part of the polyomino, and 0 otherwise.
    #
    #    This program is given an MxN matrix that is meant to represent a
    #    polyomino.  It first replaces all nonzero entries by the value 1.
    #    It then "condenses" the matrix, if possible, by removing initial and
    #    final rows and columns that are entirely zero.
    #
    #    While this procedure might save a slight amount of space, its purpose
    #    is to simplify the task of manipulating polyominos, embedding them in
    #    larger shapes, and detecting whether two polyominos describe the same
    #    shape.
    #
    #    It is entirely possible, and usual, that the output quantities are
    #    simply copies of the input quantities.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer MP, NP, the number of rows and columns in the representation
    #    of the polyomino P.
    #
    #    Input, integer P(MP,NP), a matrix of 0's and 1's representing the
    #    polyomino.
    #
    #    Output, integer MQ, NQ, the number of rows and columns of the
    #    condensed polyomino.
    #
    #    Output, integer Q(MQ,NQ), the representation of the condensed
    #    polyomino.
    #

    #
    #  Discard nonsense.
    #
    if (mp1 <= 0 or np1 <= 0):
        mq = 0
        nq = 0
        q = np.zeros([0, 0])
        return mq, nq, q

    #
    #  Seek first and last nonzero rows, columns.
    #
    i_min = -1
    for i in range(0, mp1):
        for j in range(0, np1):
            if (p1[i, j] != 0):
                i_min = i
                break
        if (i_min != -1):
            break

    #
    #  If I_MIN = -1, then we have a null matrix.
    #
    if (i_min == -1):
        mq = 0
        nq = 0
        q = np.zeros([0, 0])
        return mq, nq, q

    i_max = mp1
    for i in range(mp1 - 1, -1, -1):
        for j in range(0, np1):
            if (p1[i, j] != 0):
                i_max = i
                break
        if (i_max != mp1):
            break

    j_min = -1
    for j in range(0, np1):
        for i in range(0, mp1):
            if (p1[i, j] != 0):
                j_min = j
                break
        if (j_min != -1):
            break

    j_max = np1
    for j in range(np1 - 1, -1, -1):
        for i in range(0, mp1):
            if (p1[i, j] != 0):
                j_max = j
                break
        if (j_max != np1):
            break

    #
    #  Measure the nonzero block.
    #
    mq = i_max + 1 - i_min
    nq = j_max + 1 - j_min
    q = np.zeros([mq, nq])

    #
    #  Copy the nonzero block.
    #
    for j in range(0, nq):
        for i in range(0, mq):
            if (p1[i + i_min, j + j_min] != 0):
                q[i, j] = 1
            else:
                q[i, j] = 0

    return mq, nq, q


def polyomino_condense_test():

    # *****************************************************************************80
    #
    # POLYOMINO_CONDENSE_TEST tests POLYOMINO_CONDENSE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Local parameters:
    #
    #    Local, integer MP, NP, the number of rows and columns in the representation
    #    of the polyomino P.
    #
    #    Local, integer P(MP,NP), a matrix representing the polyomino.
    #

    print('')
    print('POLYOMINO_CONDENSE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYOMINO_CONDENSE "cleans up" a matrix that is supposed')
    print('  to represent a polyomino:')
    print('  * nonzero entries are set to 1:')
    print('  * initial and final zero rows and columns are deleted.')

    #
    #  Nothing happens:
    #
    mp1 = 3
    np1 = 3
    p1 = np.array([[0, 1, 1], [1, 1, 0], [0, 1, 0]])
    condense_demo(mp1, np1, p1)

    #
    #  Nonzero, but non-one entries are set to 1.
    #
    mp2 = 3
    np2 = 3
    p2 = np.array([[0, 1, 2], [1, 3, 0], [0, -9, 0]])
    condense_demo(mp2, np2, p2)

    #
    #  Extraneous zero rows and columns are removed.
    #
    mp3 = 3
    np3 = 4
    p3 = np.array([[0, 0, 0, 0], [1, 3, 0, 0], [0, 0, 0, 0]])
    condense_demo(mp3, np3, p3)

    #
    #  Null matrices are detected.
    #
    mp3 = 2
    np3 = 4
    p3 = np.array([[0, 0, 0, 0], [0, 0, 0, 0]])
    condense_demo(mp3, np3, p3)

    print('')
    print('POLYOMINO_CONDENSE_TEST:')
    print('  Normal end of execution.')


def condense_demo(mp1, np1, p1):

    # *****************************************************************************80
    #
    # CONDENSE_DEMO demonstrates the result of calling POLYOMINO_CONDENSE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 April 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer MP, NP, the number of rows and columns in the representation
    #    of the polyomino P.
    #
    #    Input, integer P(MP,NP), a matrix representing the polyomino.
    #
    #    Local, integer MQ, NQ, the number of rows and columns in the representation
    #    of the condensed polyomino Q.
    #
    #    Local, integer Q(MQ,NQ), a matrix representing the condensed polyomino.
    #
    label = '  The initial (%d,%d) polynomino P:' % (mp1, np1)
    polyomino_print(mp1, np1, p1, label)

    mq, nq, q = polyomino_condense(mp1, np1, p1)

    label = '  The condensed (%d,%d) polynomino Q:' % (mq, nq)
    polyomino_print(mq, nq, q, label)


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
    polyomino_condense_test()
    timestamp()
