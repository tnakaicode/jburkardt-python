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


def magnetism6_b(m):

    # *****************************************************************************80
    #
    # MAGNETISM6_B returns the bounds in the magnetism6 problem.
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
    #    Sashwati Ray, PSV Nataraj,
    #    An efficient algorithm for range computation of polynomials using the
    #    Bernstein form,
    #    Journal of Global Optimization,
    #    Volume 45, 2009, pages 403-426.
    #
    #  Parameters:
    #
    #    Input, integer M, the number of variables.
    #
    #    Output, integer L(M), U(M), the lower and upper bounds.
    #
    import numpy as np

    l = np.array([-5.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0])
    u = np.array([+5.0, +5.0, +5.0, +5.0, +5.0, +5.0, +5.0])

    return l, u


def magnetism6_f(m, n, x):

    # *****************************************************************************80
    #
    # MAGNETISM6_F returns the function in the magnetism6 problem.
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
    #    Sashwati Ray, PSV Nataraj,
    #    An efficient algorithm for range computation of polynomials using the
    #    Bernstein form,
    #    Journal of Global Optimization,
    #    Volume 45, 2009, pages 403-426.
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
        2.0 * x[0, 0:n] ** 2
        + 2.0 * x[1, 0:n] ** 2
        + 2.0 * x[2, 0:n] ** 2
        + 2.0 * x[3, 0:n] ** 2
        + 2.0 * x[4, 0:n] ** 2
        + x[5, 0:n] ** 2
        - x[5, 0:n])

    return value


def magnetism6_m():

    # *****************************************************************************80
    #
    # MAGNETISM6_M returns the number of variables in the magnetism6 problem.
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
    #    Sashwati Ray, PSV Nataraj,
    #    An efficient algorithm for range computation of polynomials using the
    #    Bernstein form,
    #    Journal of Global Optimization,
    #    Volume 45, 2009, pages 403-426.
    #
    #  Parameters:
    #
    #    Output, integer M, the number of variables.
    #
    m = 6

    return m


def magnetism6_test():

    # *****************************************************************************80
    #
    # MAGNETISM6_TEST uses sampling to estimate the range of the MAGNETISM6 polynomial.
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
    print('MAGNETISM6_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use N sample values of a polynomial over its domain to estimate')
    print('  its minimum Pmin and maximum Pmax')
    print('')
    print('         N           Pmin             Pmax')
    print('')

    m = magnetism6_m()
    l, u = magnetism6_b(m)
    print('  magnetism6: [-0.25, +280.0]')

    seed = 123456789
    n = 8

    for n_log_2 in range(4, 15):

        n = n * 2
        x, seed = r8mat_uniform_abvec(m, n, u, l, seed)
        f = magnetism6_f(m, n, x)
        print('  %8d  %16.8g  %16.8g' % (n, min(f), max(f)))
#
#  Terminate.
#
    print('')
    print('MAGNETISM6_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    magnetism6_test()
    timestamp()
