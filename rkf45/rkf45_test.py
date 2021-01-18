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
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8vec_transpose_print import r8vec_transpose_print
from r8lib.r8mat_transpose_print import r8mat_transpose_print, r8mat_transpose_print_some

from rkf45.rkf45lib import r8_fehl, r8_rkf45


def rkf45_test():

    # ********************************************************************
    #
    # RKF45_TEST tests the RKF45 ODE integrator.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 April 2011
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('\n')
    print('RKF45_TEST')
    print('  Python version')
    print('  Test the RKF45 library.')

    rkf45_test04()
    rkf45_test05()
    rkf45_test06()

    print('')
    print('RKF45_TEST')
    print('  Normal end of execution.')
    print('\n')


def rkf45_test04():

    # *****************************************************************************80
    #
    # RKF45_TEST04 solves a scalar ODE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 June 2006
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('RKF45_TEST04')
    print('  Solve a scalar equation using R8_RKF45:')
    print('')
    print('  Y'' = 0.25 * Y * ( 1 - Y / 20 )')
    neqn = 1
    abserr = np.sqrt(np.finfo(np.double).eps)
    relerr = np.sqrt(np.finfo(np.double).eps)
    flag = 1
    t_start = 0.0
    t_stop = 20.0
    n_step = 5
    t_out = 0.0
    t = t_out
    y = np.array([1.0])
    yp = r8_f1(t, y)
    print('')
    print('  FLAG     T             Y            Y''           Y_Exact         Error')
    print('%4d  %12f  %12f  %12f  %12f  %12e' % (
        flag, t, y[0], yp[0], r8_y1x(t), y[0] - r8_y1x(t)))
    for i_step in range(1, n_step + 1):
        t = ((n_step - i_step + 1) * t_start + (i_step - 1) * t_stop) / (n_step)
        t_out = ((n_step - i_step) * t_start + (i_step) * t_stop) / (n_step)
        y, yp, t, flag = r8_rkf45(
            r8_f1, neqn, y, yp, t, t_out, relerr, abserr, flag)
        print('%4d  %12f  %12f  %12f  %12f  %12e' % (
            flag, t, y[0], yp[0], r8_y1x(t), y[0] - r8_y1x(t)))
    return


def r8_f1(t, y):

    # *****************************************************************************80
    #
    # % R8_F1 evaluates the derivative for the ODE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 August 2010
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real T, the value of the independent variable.
    #
    #    Input, real Y, the value of the dependent variable.
    #
    #    Output, real YP, the value of the derivative
    #    dY(1:NEQN)/dT.
    #

    yp = np.zeros(np.size(y))
    yp[0] = 0.25 * y[0] * (1.0 - y[0] / 20.0)
    return(yp)


def rkf45_test05():

    # *****************************************************************************80
    #
    # % RKF45_TEST05 solves a vector ODE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 June 2006
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('RKF45_TEST05')
    print('  Solve a vector equation using R8_RKF45')
    print('')
    print('  Y''(1) =  Y(2)')
    print('  Y''(2) = -Y(1)')
    neqn = 2
    abserr = np.sqrt(np.finfo(np.double).eps)
    relerr = np.sqrt(np.finfo(np.double).eps)
    flag = 1
    t_start = 0.0
    t_stop = 2.0 * 3.14159265
    n_step = 12
    t = 0.0
    t_out = 0.0
    y = np.zeros(2)
    y[0] = 1.0
    yp = r8_f2(t, y)
    print('')
    print('  FLAG       T          Y(1)          Y(2)')
    print('%4d  %12f  %12f  %12f' % (flag, t, y[0], y[1]))
    for i_step in range(1, n_step + 1):
        t = ((n_step - i_step + 1) * t_start
             + (i_step - 1) * t_stop) \
            / (n_step)
        t_out = ((n_step - i_step) * t_start
                 + (i_step) * t_stop) \
            / (n_step)
        y, yp, t, flag = r8_rkf45(
            r8_f2, neqn, y, yp, t, t_out, relerr, abserr, flag)
        print('%4d  %12f  %12f  %12f' % (flag, t, y[0], y[1]))
    return


def r8_f2(t, y):

    # *****************************************************************************80
    #
    # % R8_F2 evaluates the derivative for the ODE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 August 2010
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real T, the value of the independent variable.
    #
    #    Input, real Y(NEQN), the value of the dependent variable.
    #
    #    Output, real YP(NEQN), the value of the derivative
    #    dY(1:NEQN)/dT.
    #

    yp = np.zeros(np.size(y))
    yp[0] = y[1]
    yp[1] = -y[0]
    return(yp)


def r8_y1x(t):

    # *****************************************************************************80
    #
    # % R8_Y1X evaluates the exact solution of the ODE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 August 2010
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real T, the value of the independent variable.
    #
    #    Output, real Y1X, the exact solution.
    #

    y1x = 20.0 / (1.0 + 19.0 * np.exp(- 0.25 * t))
    return(y1x)


def rkf45_test06():

    # *******************************
    #
    # % RKF45_TEST06 solves a scalar ODE and uses one-step integration.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 August 2010
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('RKF45_TEST06')
    print('  Solve a scalar equation using R8_RKF45')
    print('')
    print('  Y'' = 0.25 * Y * ( 1 - Y / 20 )')
    print('')
    print('  Use the special SINGLE_STEP mode')
    print('  which returns after every step.')
    neqn = 1
    abserr = np.sqrt(np.finfo(np.double).eps)
    relerr = np.sqrt(np.finfo(np.double).eps)
    flag = -1
    t_start = 0.0
    t_stop = 20.0
    n_step = 5
    t = 0.0
    t_out = 0.0
    y = np.zeros(1)
    y[0] = 1.0
    yp = r8_f1(t, y)
    print('')
    print('  FLAG     T             Y            dY/dt         Y_Exact      Error')
    print('%4d  %12f  %12f  %12f  %12f    %12e' % (
        flag, t, y[0], yp[0], r8_y1x(t), y[0] - r8_y1x(t)))
    for i_step in range(1, n_step + 1):
        t = ((n_step - i_step + 1) * t_start
             + (i_step - 1) * t_stop) \
            / (n_step)
        t_out = ((n_step - i_step) * t_start
                 + (i_step) * t_stop) \
            / (n_step)
        #
        #  As long as FLAG is negative, we are heading towards T_OUT, but
        #  have not reached it.
        #
        while (flag < 0):
            y, yp, t, flag = r8_rkf45(
                r8_f1, neqn, y, yp, t, t_out, relerr, abserr, flag)
            print('%4d  %12f  %12f  %12f  %12f    %12e' % (
                flag, t, y[0], yp[0], r8_y1x(t), y[0] - r8_y1x(t)))
        #
        #  FLAG is returned as +2 when we reach T_OUT.  Reset it to -2
        # to continue to the next T_OUT in one step mode.
        #
        flag = -2
    return


if (__name__ == '__main__'):
    timestamp()
    rkf45_test()
    timestamp()
