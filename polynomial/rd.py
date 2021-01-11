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

from r8lib.r8vec_print import r8vec_print_test
from r8lib.r8mat_uniform_abvec import r8mat_uniform_abvec


def rd_b(m):

    # *****************************************************************************80
    #
    # RD_B returns the bounds in the rd problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Cesar Munoz, Anthony Narkawicz,
    #    Formalization of Bernstein polynomials and applications to global
    #    optimization,
    #    Journal of Automated Reasoning,
    #    Volume 51, Number 2, 2013, pages 151-196.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Output, integer L(M), U(M), the lower and upper bounds.
    #

    l = np.array([-5.0, -5.0, -5.0])
    u = np.array([+5.0, +5.0, +5.0])

    return l, u


def rd_f(m, n, x):

    # *****************************************************************************80
    #
    # RD_F returns the function in the rd problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Cesar Munoz, Anthony Narkawicz,
    #    Formalization of Bernstein polynomials and applications to global
    #    optimization,
    #    Journal of Automated Reasoning,
    #    Volume 51, Number 2, 2013, pages 151-196.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real X(M,N), the points.
    #
    #    Output, integer VALUE(N), the value of the function at X.
    #
    value = (
        - x[0, 0:n]
        + 2.0 * x[1, 0:n]
        - x[2, 0:n]
        - 0.835634534 * x[1, 0:n]
        - 0.835634534 * x[1, 0:n] ** 2)

    return value


def rd_m():

    # *****************************************************************************80
    #
    # RD_M returns the number of variables in the rd problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Cesar Munoz, Anthony Narkawicz,
    #    Formalization of Bernstein polynomials and applications to global
    #    optimization,
    #    Journal of Automated Reasoning,
    #    Volume 51, Number 2, 2013, pages 151-196.
    #
    #  Parameters:
    #
    #    Output, integer M, the number of variables.
    #
    m = 3

    return m


def rd_test():

    # *****************************************************************************80
    #
    # RD_TEST uses sampling to estimate the range of the RD polynomial.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 December 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('RD_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use N sample values of a polynomial over its domain to estimate')
    print('  its minimum Pmin and maximum Pmax')
    print('')
    print('         N           Pmin             Pmax')
    print('')

    m = rd_m()
    l, u = rd_b(m)
    print('  rd: [-36.71269068, +10.40560403]')

    seed = 123456789
    n = 8

    for n_log_2 in range(4, 15):

        n = n * 2
        x, seed = r8mat_uniform_abvec(m, n, u, l, seed)
        f = rd_f(m, n, x)
        print('  %8d  %16.8g  %16.8g' % (n, min(f), max(f)))

    print('')
    print('RD_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    rd_test()
    timestamp()
