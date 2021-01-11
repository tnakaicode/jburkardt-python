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

from r8lib.r8mat_print import r8mat_print
from r8lib.r8mat_print_some import r8mat_print_some
from r8lib.r8mat_uniform_abvec import r8mat_uniform_abvec
from r8lib.r8vec2_print import r8vec2_print


def smith2_b(m):

    # *****************************************************************************80
    #
    # SMITH2_B returns the bounds in the smith2 problem.
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
    #  Reference:
    #
    #    Andrew Smith,
    #    Fast construction of constant bound functions for sparse polynomials,
    #    Journal of Global Optimization,
    #    Volume 43, 2009, pages 445-458.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Output, integer L(M), U(M), the lower and upper bounds.
    #
    import numpy as np

    l = np.array([+1.0, +1.0, +1.0, +1.0, +1.0, +1.0, +1.0])
    u = np.array([+2.0, +2.0, +2.0, +2.0, +2.0, +2.0, +2.0])

    return l, u


def smith2_f(m, n, x):

    # *****************************************************************************80
    #
    # SMITH2_F returns the function in the smith2 problem.
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
    #    Andrew Smith,
    #    Fast construction of constant bound functions for sparse polynomials,
    #    Journal of Global Optimization,
    #    Volume 43, 2009, pages 445-458.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Input, integer N, the number of points.
    #
    #    Input, real x[M,N), the points.
    #
    #    Output, integer VALUE(N), the value of the function at X.
    #
    value = (
        3.0 * x[0, 0:n] * x[1, 0:n] ** 5
        + 2.0 * x[0, 0:n] ** 4 * x[1, 0:n]
        - 8.0 * x[0, 0:n] ** 2 * x[2, 0:n] ** 6 * x[3, 0:n] ** 2
        - x[0, 0:n] * x[3, 0:n] ** 8
        + 3.0 * x[1, 0:n] ** 3 * x[4, 0:n]
        - 10.0 * x[3, 0:n] ** 5 * x[4, 0:n] ** 5 * x[5, 0:n] ** 5
        - 0.01 * x[4, 0:n] ** 2 * x[5, 0:n] ** 2
        + 4.0 * x[4, 0:n] ** 3 * x[6, 0:n] ** 4)

    return value


def smith2_m():

    # *****************************************************************************80
    #
    # SMITH2_M returns the number of variables in the smith2 problem.
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
    #    Andrew Smith,
    #    Fast construction of constant bound functions for sparse polynomials,
    #    Journal of Global Optimization,
    #    Volume 43, 2009, pages 445-458.
    #
    #  Parameters:
    #
    #    Output, integer M, the number of variables.
    #
    m = 7

    return m


def smith2_test():

    # *****************************************************************************80
    #
    # SMITH2_TEST uses sampling to estimate the range of the SMITH2 polynomial.
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
    print('SMITH2_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use N sample values of a polynomial over its domain to estimate')
    print('  its minimum Pmin and maximum Pmax')
    print('')
    print('         N           Pmin             Pmax')
    print('')

    m = smith2_m()
    l, u = smith2_b(m)
    print('  smith2: [ ?, ? ]:')

    seed = 123456789
    n = 8

    for n_log_2 in range(4, 15):

        n = n * 2
        x, seed = r8mat_uniform_abvec(m, n, u, l, seed)
        f = smith2_f(m, n, x)
        print('  %8d  %16.8g  %16.8g' % (n, min(f), max(f)))
#
#  Terminate.
#
    print('')
    print('SMITH2_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    smith2_test()
    timestamp()
