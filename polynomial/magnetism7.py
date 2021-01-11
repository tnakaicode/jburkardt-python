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


def magnetism7_b(m):

    # *****************************************************************************80
    #
    # MAGNETISM7_B returns the bounds in the magnetism7 problem.
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
    import numpy as np

    l = np.array([-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0])
    u = np.array([+1.0, +1.0, +1.0, +1.0, +1.0, +1.0, +1.0])

    return l, u


def magnetism7_f(m, n, x):

    # *****************************************************************************80
    #
    # MAGNETISM7_F returns the function in the magnetism7 problem.
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
        x[0, 0:n] ** 2
        + 2.0 * x[1, 0:n] ** 2
        + 2.0 * x[2, 0:n] ** 2
        + 2.0 * x[3, 0:n] ** 2
        + 2.0 * x[4, 0:n] ** 2
        + 2.0 * x[5, 0:n] ** 2
        + 2.0 * x[6, 0:n] ** 2
        - x[0, 0:n])

    return value


def magnetism7_m():

    # *****************************************************************************80
    #
    # MAGNETISM7_M returns the number of variables in the magnetism7 problem.
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
    m = 7

    return m


def magnetism7_test():

    # *****************************************************************************80
    #
    # MAGNETISM7_TEST uses sampling to estimate the range of the MAGNETISM7 polynomial.
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
    print('MAGNETISM7_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use N sample values of a polynomial over its domain to estimate')
    print('  its minimum Pmin and maximum Pmax')
    print('')
    print('         N           Pmin             Pmax')
    print('')

    m = magnetism7_m()
    l, u = magnetism7_b(m)
    print('  magnetism7: [-0.25, +330.0]')

    seed = 123456789
    n = 8

    for n_log_2 in range(4, 15):

        n = n * 2
        x, seed = r8mat_uniform_abvec(m, n, u, l, seed)
        f = magnetism7_f(m, n, x)
        print('  %8d  %16.8g  %16.8g' % (n, min(f), max(f)))
#
#  Terminate.
#
    print('')
    print('MAGNETISM7_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    magnetism7_test()
    timestamp()
