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


def lv3_b(m):

    # *****************************************************************************80
    #
    # LV3_B returns the bounds in the lv3 problem.
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

    l = np.array([-1.5, -1.5, -1.5])
    u = np.array([+2.0, +2.0, +2.0])

    return l, u


def lv3_f(m, n, x):

    # *****************************************************************************80
    #
    # LV3_F returns the function in the lv3 problem.
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
        - x[0, 0:n] * x[1, 0:n] ** 2
        + x[0, 0:n] * x[2, 0:n] ** 2
        - 1.1 * x[0, 0:n]
        + 1.0)

    return value


def lv3_m():

    # *****************************************************************************80
    #
    # LV3_M returns the number of variables in the lv3 problem.
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
    m = 3

    return m


def lv3_test():

    # *****************************************************************************80
    #
    # LV3_TEST uses sampling to estimate the range of the LV3 polynomial.
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
    print('LV3_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use N sample values of a polynomial over its domain to estimate')
    print('  its minimum Pmin and maximum Pmax')
    print('')
    print('         N           Pmin             Pmax')
    print('')

    m = lv3_m()
    l, u = lv3_b(m)
    print('  lv3: [-9.35, +14.8 ]')

    seed = 123456789
    n = 8
    obj = plot2d(aspect="auto")
    for n_log_2 in range(4, 15):
        n = n * 2
        x, seed = r8mat_uniform_abvec(m, n, u, l, seed)
        f = lv3_f(m, n, x)
        print('  %8d  %16.8g  %16.8g' % (n, min(f), max(f)))

        obj.new_2Dfig(aspect="auto")
        obj.axs.plot(x[0, :], f)
        obj.axs.plot(x[1, :], f)
        obj.axs.plot(x[2, :], f)
        obj.axs.plot(f)
        obj.SavePng(obj.tmpdir + "lv3_{:03d}.png".format(n_log_2))

        obj.new_3Dfig(aspect="auto")
        obj.axs.plot(x[0, :], x[1, :], x[2, :])
        obj.SavePng(obj.tmpdir + "lv3_3d_{:03d}.png".format(n_log_2))
        plt.close()

    #obj.SavePng(obj.tmpdir + "lv3.png")
    plt.close()

    print('')
    print('LV3_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    lv3_test()
    timestamp()
