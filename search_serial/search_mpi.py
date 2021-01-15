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


def search_mpi(a, b, c):

    # *****************************************************************************80
    #
    # SEARCH_MPI searches for a solution to an integer equation.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 October 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer A, the lower limit of the search.
    #
    #    Input, integer B, the upper limit of the search.
    #
    #    Input, integer C, the desired value.
    #
    #    Output, integer J, is:
    #    -1, if no solution could be found.
    #    otherwise, F(J) = C and A <= J <= B.
    #

    comm = MPI.COMM_WORLD

    indx = comm.Get_rank()

    p = comm.Get_size()

    if (indx == 0):
        print('')
        print('SEARCH_MPI:')
        print('  Python/MPI version')
        print('  Search the integers from A to B')
        print('  for a value J such that F(J) = C.')
        print('')
        print('  Use MPI to divide the computation among')
        print('  %d processes.' % (p))
        print('')
        print('  A        = %d' % (a))
        print('  B        = %d' % (b))
        print('  C        = %d' % (c))
        wtime = MPI.Wtime()

    j = search_partial(a, b, c, indx, p)

    if (j != -1):
        print('  Process %d found J = %d' % (indx, j))
        print('  Verify F(J) = %d' % (f(j)))

    if (indx == 0):
        wtime = MPI.Wtime() - wtime
        print('  Time     = %g' % (wtime))

    print('')
    print('SEARCH_MPI:')
    print('  Normal end of execution.')
    return j


def search_partial(a, b, c, id, p):

    # *****************************************************************************80
    #
    # SEARCH_PARTIAL searches 'partially' through [A,B] for a J so that F(J) = C.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 October 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer A, B, the search range.
    #
    #    Input, integer C, the desired function value.
    #
    #    Input, integer ID, the increment between successive values that
    #    are to be checked.
    #
    #    Input, integer P, the number of processes.
    #
    #    Output, integer J, the computed solution, or -1
    #    if no solution was found.
    #
    for i in range(a + id, b + 1, p):

        if (f(i) == c):
            return i

    return (- 1)


def f(i):

    # *****************************************************************************80
    #
    # F is the function we are analyzing.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer I, the argument.
    #
    #    Input, integer VALUE, the value.
    #
    i4_huge = 2147483647

    value = i

    for j in range(0, 5):

        k = (value // 127773)

        value = 16807 * (value - k * 127773) - k * 2836

        if (value <= 0):
            value = value + i4_huge

    return value


if (__name__ == '__main__'):
    timestamp()
    search_mpi(1, 10000, 45)
    search_mpi(1, 100000, 45)
    search_mpi(1, 1000000, 45)
    search_mpi(1674924000, 1674924999, 45)
    timestamp()
