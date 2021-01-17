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


def lagrange_basis_1d(nd, xd, ni, xi):

    # *****************************************************************************80
    #
    # LAGRANGE_BASIS_1D evaluates a 1D Lagrange basis.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer ND, the number of data points.
    #
    #    Input, real XD(ND,1), the interpolation nodes.
    #
    #    Input, integer NI, the number of evaluation points.
    #
    #    Input, real XI(NI,1), the evaluation points.
    #
    #    Output, real LB(NI,ND), the value, at the I-th point XI, of the
    #    Jth basis function.
    #

    lb = np.zeros([ni, nd])

    for i in range(0, ni):
        for j in range(0, nd):
            lb[i, j] = 1.0
            for k in range(0, nd):
                if (k != j):
                    lb[i, j] = lb[i, j] * (xi[i] - xd[k]) / (xd[j] - xd[k])

    return lb


def lagrange_basis_1d_test():

    # *****************************************************************************80
    #
    # LAGRANGE_BASIS_1D_TEST tests LAGRANGE_BASIS_1D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    nd = 4
    ni = 21

    xd = np.array([0.0, 2.0, 5.0, 10.0])

    print('')
    print('LAGRANGE_BASIS_1D_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  LAGRANGE_BASIS_1D evaluates the Lagrange 1D basis')
    print('  functions.')

    x_min = 0.0
    x_max = 10.0
    xi = np.linspace(x_min, x_max, ni)
    lb = lagrange_basis_1d(nd, xd, ni, xi)
    r8mat_print(ni, nd, lb, '  The Lagrange basis functions:')

    obj = plot2d(aspect="auto")
    obj.axs.plot(xi, lb)
    obj.SavePng()

    print('')
    print('LAGRANGE_BASIS_1D_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    lagrange_basis_1d_test()
    timestamp()
