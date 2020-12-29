#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import math
import platform
import time
import sys
import os
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp


def fd1d_heat_implicit_cfl(k, t_num, t_min, t_max, x_num, x_min, x_max):

    # *****************************************************************************80
    #
    # FD1D_HEAT_IMPLICIT_CFL: compute the Courant-Friedrichs-Loewy coefficient.
    #
    #  Discussion:
    #
    #    The equation to be solved has the form:
    #
    #      dUdT - k * d2UdX2 = F(X,T)
    #
    #    over the interval [X_MIN,X_MAX] with boundary conditions
    #
    #      U(X_MIN,T) = U_X_MIN(T),
    #      U(X_MIN,T) = U_X_MAX(T),
    #
    #    over the time interval [T_MIN,T_MAX] with initial conditions
    #
    #      U(X,T_MIN) = U_T_MIN(X)
    #
    #    The code uses the finite difference method to approximate the
    #    second derivative in space, and an explicit forward Euler approximation
    #    to the first derivative in time.
    #
    #    The finite difference form can be written as
    #
    #      U(X,T+dt) - U(X,T)                  ( U(X-dx,T) - 2 U(X,T) + U(X+dx,T) )
    #      ------------------  = F(X,T) + k *  ------------------------------------
    #               dt                                   dx * dx
    #
    #    or, assuming we have solved for all values of U at time T, we have
    #
    #      U(X,T+dt) = U(X,T) + cfl * ( U(X-dx,T) - 2 U(X,T) + U(X+dx,T) ) + dt * F(X,T)
    #
    #    Here "cfl" is the Courant-Friedrichs-Loewy coefficient:
    #
    #      cfl = k * dt / dx / dx
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 April 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    George Lindfield, John Penny,
    #    Numerical Methods Using MATLAB,
    #    Second Edition,
    #    Prentice Hall, 1999,
    #    ISBN: 0-13-012641-1,
    #    LC: QA297.P45.
    #
    #  Parameters:
    #
    #    Input, real K, the heat conductivity coefficient.
    #
    #    Input, integer T_NUM, the number of time values, including the initial
    #    value.
    #
    #    Input, real T_MIN, T_MAX, the minimum and maximum times.
    #
    #    Input, integer X_NUM, the number of nodes.
    #
    #    Input, real X_MIN, X_MAX, the minimum and maximum spatial coordinates.
    #
    #    Output, real CFL, the Courant-Friedrichs-Loewy coefficient.
    #
    x_step = (x_max - x_min) / float(x_num - 1)
    t_step = (t_max - t_min) / float(t_num - 1)
    cfl = k * t_step / x_step / x_step

    return cfl


def fd1d_heat_implicit_matrix(x_num, cfl):

    # *****************************************************************************80
    #
    # FD1D_HEAT_IMPLICIT_MATRIX: set the system matrix.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 April 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer X_NUM, the number of nodes.
    #
    #    Input, real CFL, the Courant-Friedrichs-Loewy coefficient.
    #
    #    Output, real A(X_NUM,X_NUM), the system matrix.
    #

    a = np.zeros((x_num, x_num))

    a[0, 0] = 1.0

    for i in range(1, x_num - 1):
        a[i, i - 1] = - cfl
        a[i, i] = 1.0 + 2.0 * cfl
        a[i, i + 1] = - cfl

    a[x_num - 1, x_num - 1] = 1.0

    return a


def fd1d_heat_implicit(a, x_num, x, t, dt, cfl, rhs_fun, bc_fun, u):

    # *****************************************************************************80
    #
    # FD1D_HEAT_IMPLICIT: Finite difference solution of 1D heat equation.
    #
    #  Discussion:
    #
    #    FD1D_HEAT_IMPLICIT solves the 1D heat equation with an implicit method.
    #
    #    This program solves
    #
    #      dUdT - k * d2UdX2 = F(X,T)
    #
    #    over the interval [A,B] with boundary conditions
    #
    #      U(A,T) = UA(T),
    #      U(B,T) = UB(T),
    #
    #    over the time interval [T0,T1] with initial conditions
    #
    #      U(X,T0) = U0(X)
    #
    #    The code uses the finite difference method to approximate the
    #    second derivative in space, and an implicit backward Euler approximation
    #    to the first derivative in time.
    #
    #    The finite difference form can be written as
    #
    #      U(X,T+dt) - U(X,T)                  ( U(X-dx,T+dt) - 2 U(X,T+dt) + U(X+dx,T+dt) )
    #      ------------------ = F(X,T+dt) + k *  --------------------------------------
    #               dt                                   dx * dx
    #
    #    so that we have the following linear system for the values of U at time T+dt:
    #
    #            -     k * dt / dx / dx   * U(X-dt,T+dt)
    #      + ( 1 + 2 * k * dt / dx / dx ) * U(X,   T+dt)
    #            -     k * dt / dx / dx   * U(X+dt,T+dt)
    #      =               dt             * F(X,   T+dt)
    #      +                                U(X,   T)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 April 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A(X_NUM,X_NUM), the system matrix.
    #
    #    Input, integer X_NUM, the number of nodes.
    #
    #    Input, real X(X_NUM), the node coordinates.
    #
    #    Input, real T, the current time.
    #
    #    Input, real DT, the size of the time step.
    #
    #    Input, real CFL, the Courant-Friedrichs-Loewy coefficient.
    #
    #    Input, f = RHS_FUN ( x_num, x, t ), returns in F the right hand side
    #    forcing function at every non-boundary node.
    #
    #    Input, hbc = BC_FUN ( x_num, x, t, h ), returns in HBC a copy of the
    #    input solution H, after imposing Dirichlet boundary conditions.
    #
    #    Input, real U(X_NUM), the solution values at the old time.
    #
    #    Output, real U(X_NUM), the solution values at the new time.
    #
#
#  Compute b, the right hand side of the system.
#
    fvec = rhs_fun(x_num, x, t)

    b = u.copy()
    for i in range(1, x_num - 1):
        b[i] = b[i] + dt * fvec[i]
#
#  Solve A*u=b.
#
    u = np.linalg.solve(a, b)
#
#  Impose boundary conditions on U.
#
    u = bc_fun(x_num, x, t, u)

    return u


def fd1d_heat_implicit_test01():

    # *****************************************************************************80
    #
    # FD1D_HEAT_IMPLICIT_TEST01 does a simple test problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import matplotlib.pyplot as plt
    import numpy as np
    import platform
    from mpl_toolkits.mplot3d import Axes3D

    print('')
    print('FD1D_HEAT_IMPLICIT_TEST01:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Compute an approximate solution to the time-dependent')
    print('  one dimensional heat equation:')
    print('    dH/dt - K * d2H/dx2 = f(x,t)')
    print('  Run a simple test case.')
#
#  Get the heat coefficient.
#
    k = k_test01()
#
#  X_NUM is the number of equally spaced nodes to use between 0 and 1.
#
    x_num = 21
    x_min = 0.0
    x_max = 1.0
    dx = (x_max - x_min) / (x_num - 1)
    x = np.linspace(x_min, x_max, x_num)
#
#  T_NUM is the number of equally spaced time points between 0 and 10.0.
#
    t_num = 201
    t_min = 0.0
    t_max = 80.0
    dt = (t_max - t_min) / (t_num - 1)
    t = np.linspace(t_min, t_max, t_num)
#
#  Compute the CFL coefficient.
#
    cfl = fd1d_heat_implicit_cfl(k, t_num, t_min, t_max, x_num, x_min, x_max)

    print('')
    print('  Number of X nodes = %d' % (x_num))
    print('  X interval is [%f,%f]' % (x_min, x_max))
    print('  X spacing is %f' % (dx))
    print('  Number of T values = %d' % (t_num))
    print('  T interval is [%f,%f]' % (t_min, t_max))
    print('  T spacing is %f' % (dt))
    print('  Constant K = %g' % (k))
    print('  CFL coefficient = %g' % (cfl))
#
#  Compute the system matrix.
#
    a = fd1d_heat_implicit_matrix(x_num, cfl)
#
#  Save every solution vector H in a matrix HMAT, for plotting.
#
    hmat = np.zeros((x_num, t_num))
#
#  Compute T_NUM solutions (including the initial condition).
#
    for j in range(0, t_num):

        if (j == 0):
            h = ic_test01(x_num, x, t[j])
            h = bc_test01(x_num, x, t[j], h)
        else:
            h = fd1d_heat_implicit(a, x_num, x, t[j - 1], dt, cfl, rhs_test01,
                                   bc_test01, h)

        for i in range(0, x_num):
            hmat[i, j] = h[i]
#
#  Plot X and T versus H.
#
    tmat, xmat = np.meshgrid(t, x)
    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_surface(xmat, tmat, hmat)
    plt.xlabel('<---X--->')
    plt.ylabel('<---T--->')
    plt.title('H(X,T)')
    plt.savefig('plot_test01.png')
    plt.show(block=False)
#
#  Write the data to files.
#
    r8mat_write('h_test01.txt', x_num, t_num, hmat)
    r8vec_write('t_test01.txt', t_num, t)
    r8vec_write('x_test01.txt', x_num, x)

    print('')
    print('  H(X,T) written to "h_test01.txt"')
    print('  T values written to "t_test01.txt"')
    print('  X values written to "x_test01.txt"')
#
#  Terminate.
#
    print('')
    print('FD1D_HEAT_IMPLICIT_TEST01:')
    print('  Normal end of execution.')
    return


def bc_test01(x_num, x, t, h):

    # *****************************************************************************80
    #
    # BC_TEST01 evaluates the boundary conditions for problem 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 January 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer X_NUM, the number of nodes.
    #
    #    Input, real X(X_NUM), the node coordinates.
    #
    #    Input, real T, the current time.
    #
    #    Input, real H(X_NUM), the current heat values.
    #
    #    Output, real H(X_NUM), the current heat values, after boundary
    #    conditions have been imposed.
    #
    h[0] = 90.0
    h[x_num - 1] = 70.0

    return h


def ic_test01(x_num, x, t):

    # *****************************************************************************80
    #
    # IC_TEST01 evaluates the initial condition for problem 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 January 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer X_NUM, the number of nodes.
    #
    #    Input, real X(X_NUM), the node coordinates.
    #
    #    Input, real T, the initial time.
    #
    #    Output, real H(X_NUM), the heat values at the initial time.
    #
    import numpy as np

    h = np.zeros(x_num)

    for i in range(0, x_num):
        h[i] = 50.0

    return h


def k_test01():

    # *****************************************************************************80
    #
    # K_TEST01 evaluates the conductivity for problem 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real K, the conducitivity.
    #
    k = 0.002

    return k


def rhs_test01(x_num, x, t):

    # *****************************************************************************80
    #
    # RHS_TEST01 evaluates the right hand side for problem 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 January 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer X_NUM, the number of nodes.
    #
    #    Input, real X(X_NUM), the node coordinates.
    #
    #    Input, real T, the current time.
    #
    #    Output, real VALUE(X_NUM), the source term.
    #
    import numpy as np

    value = np.zeros(x_num)

    return value


def fd1d_heat_implicit_test02():

    # *****************************************************************************80
    #
    # FD1D_HEAT_IMPLICIT_TEST02 does a problem with known solution.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import matplotlib.pyplot as plt
    import numpy as np
    import platform
    from mpl_toolkits.mplot3d import Axes3D

    print('')
    print('FD1D_HEAT_IMPLICIT_TEST02:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Compute an approximate solution to the time-dependent')
    print('  one dimensional heat equation for a problem where we')
    print('  know the exact solution.')
    print('')
    print('    dH/dt - K * d2H/dx2 = f(x,t)')
    print('')
    print('  Run a simple test case.')
#
#  Heat coefficient.
#
    k = k_test02()
#
#  X_NUM is the number of equally spaced nodes to use between 0 and 1.
#
    x_num = 21
    x_min = 0.0
    x_max = 1.0
    dx = (x_max - x_min) / (x_num - 1)
    x = np.linspace(x_min, x_max, x_num)
#
#  T_NUM is the number of equally spaced time points between 0 and 10.0.
#
    t_num = 26
    t_min = 0.0
    t_max = 10.0
    dt = (t_max - t_min) / (t_num - 1)
    t = np.linspace(t_min, t_max, t_num)
#
#  Get the CFL coefficient.
#
    cfl = fd1d_heat_implicit_cfl(k, t_num, t_min, t_max, x_num, x_min, x_max)

    print('')
    print('  Number of X nodes = %d' % (x_num))
    print('  X interval is [%f,%f]' % (x_min, x_max))
    print('  X spacing is %f' % (dx))
    print('  Number of T values = %d' % (t_num))
    print('  T interval is [%f,%f]' % (t_min, t_max))
    print('  T spacing is %f' % (dt))
    print('  Constant K = %g' % (k))
    print('  CFL coefficient = %g' % (cfl))
#
#  Get the system matrix.
#
    a = fd1d_heat_implicit_matrix(x_num, cfl)

    gmat = np.zeros((x_num, t_num))
    hmat = np.zeros((x_num, t_num))

    print('')
    print('  Step            Time       RMS Error')
    print('')

    for j in range(0, t_num):
        if (j == 0):
            h = ic_test02(x_num, x, t[j])
            h = bc_test02(x_num, x, t[j], h)
        else:
            h = fd1d_heat_implicit(
                a, x_num, x, t[j - 1], dt, cfl, rhs_test02, bc_test02, h)
        g = np.zeros(x_num)
        for i in range(0, x_num):
            g[i] = exact_test02(x[i], t[j])
        e = 0.0
        for i in range(0, x_num):
            e = e + (h[i] - g[i]) ** 2
        e = np.sqrt(e) / np.sqrt(x_num)
        print('  %4d  %14.6g  %14.6g' % (j, t[j], e))
        for i in range(0, x_num):
            gmat[i, j] = g[i]
            hmat[i, j] = h[i]
#
#  Plot the data.
#
    tmat, xmat = np.meshgrid(t, x)
    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_surface(xmat, tmat, hmat)
    plt.xlabel('<---X--->')
    plt.ylabel('<---T--->')
    plt.title('H(X,T)')
    plt.savefig('plot_test02.png')
    plt.show(block=False)
#
#  Write the data to files.
#
    r8mat_write('g_test02.txt', x_num, t_num, gmat)
    r8mat_write('h_test02.txt', x_num, t_num, hmat)
    r8vec_write('t_test02.txt', t_num, t)
    r8vec_write('x_test02.txt', x_num, x)

    print('')
    print('  G(X,T) written to "g_test02.txt"')
    print('  H(X,T) written to "h_test02.txt"')
    print('  T values written to "t_test02.txt"')
    print('  X values written to "x_test02.txt"')
#
#  Terminate.
#
    print('')
    print('FD1D_HEAT_IMPLICIT_TEST02:')
    print('  Normal end of execution')
    return


def bc_test02(x_num, x, t, h):

    # *****************************************************************************80
    #
    # BC_TEST02 evaluates the boundary conditions for problem 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer X_NUM, the number of nodes.
    #
    #    Input, real X(X_NUM), the node coordinates.
    #
    #    Input, real T, the current time.
    #
    #    Input, real H(X_NUM), the current heat values.
    #
    #    Output, real H(X_NUM), the current heat values, after boundary
    #    conditions have been imposed.
    #
    h[0] = exact_test02(x[0], t)

    h[x_num - 1] = exact_test02(x[x_num - 1], t)

    return h


def exact_test02(x, t):

    # *****************************************************************************80
    #
    # EXACT_TEST02 evaluates the exact solution for problem 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, a node coordinate.
    #
    #    Input, real T, the initial time.
    #
    #    Output, real H, the exact solution at X and T.
    #
    import numpy as np

    k = k_test02()

    h = np.exp(- t) * np.sin(np.sqrt(k) * x)

    return h


def ic_test02(x_num, x, t):

    # *****************************************************************************80
    #
    # IC_TEST02 evaluates the initial condition for problem 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer X_NUM, the number of nodes.
    #
    #    Input, real X(X_NUM), the node coordinates.
    #
    #    Input, real T, the initial time.
    #
    #    Output, real H(X_NUM), the heat values at the initial time.
    #
    import numpy as np

    h = np.zeros(x_num)

    for i in range(0, x_num):
        h[i] = exact_test02(x[i], t)

    return h


def k_test02():

    # *****************************************************************************80
    #
    # K_TEST02 evaluates the conductivity for problem 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real K, the conducitivity.
    #
    k = 0.002

    return k


def rhs_test02(x_num, x, t):

    # *****************************************************************************80
    #
    # RHS_TEST02 evaluates the right hand side for problem 2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer X_NUM, the number of nodes.
    #
    #    Input, real X(X_NUM), the node coordinates.
    #
    #    Input, real T, the current time.
    #
    #    Output, real VALUE(X_NUM), the source term.
    #
    import numpy as np

    value = np.zeros(x_num)

    return value


def fd1d_heat_implicit_test03():

    # *****************************************************************************80
    #
    # FD1D_HEAT_IMPLICIT_TEST03 does a simple test problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import matplotlib.pyplot as plt
    import numpy as np
    import platform
    from mpl_toolkits.mplot3d import Axes3D

    print('')
    print('FD1D_HEAT_IMPLICIT_TEST03:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Compute an approximate solution to the time-dependent')
    print('  one dimensional heat equation:')
    print('    dH/dt - K * d2H/dx2 = f(x,t)')
    print('  Run a simple test case.')
#
#  Heat coefficient.
#
    k = k_test03()
#
#  X_NUM is the number of equally spaced nodes to use between 0 and 1.
#
    x_num = 21
    x_min = -5.0
    x_max = +5.0
    dx = (x_max - x_min) / (x_num - 1)
    x = np.linspace(x_min, x_max, x_num)
#
#  T_NUM is the number of equally spaced time points between 0 and 10.0.
#
    t_num = 81
    t_min = 0.0
    t_max = 4.0
    dt = (t_max - t_min) / (t_num - 1)
    t = np.linspace(t_min, t_max, t_num)
#
#  Get the CFL coefficient.
#
    cfl = fd1d_heat_implicit_cfl(k, t_num, t_min, t_max, x_num, x_min, x_max)

    print('')
    print('  Number of X nodes = %d' % (x_num))
    print('  X interval is [%f,%f]' % (x_min, x_max))
    print('  X spacing is %f' % (dx))
    print('  Number of T values = %d' % (t_num))
    print('  T interval is [%f,%f]' % (t_min, t_max))
    print('  T spacing is %f' % (dt))
    print('  Constant K = %g' % (k))
    print('  CFL coefficient = %g' % (cfl))
#
#  Get the system matrix.
#
    a = fd1d_heat_implicit_matrix(x_num, cfl)

    hmat = np.zeros((x_num, t_num))

    for j in range(0, t_num):
        if (j == 0):
            h = ic_test03(x_num, x, t[j])
            h = bc_test03(x_num, x, t[j], h)
        else:
            h = fd1d_heat_implicit(
                a, x_num, x, t[j - 1], dt, cfl, rhs_test03, bc_test03, h)
        for i in range(0, x_num):
            hmat[i, j] = h[i]
#
#  Plot the data.
#
    tmat, xmat = np.meshgrid(t, x)
    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_surface(xmat, tmat, hmat)
    plt.xlabel('<---X--->')
    plt.ylabel('<---T--->')
    plt.title('H(X,T)')
    plt.savefig('plot_test03.png')
    plt.show(block=False)
#
#  Write the data to files.
#
    r8mat_write('h_test03.txt', x_num, t_num, hmat)
    r8vec_write('t_test03.txt', t_num, t)
    r8vec_write('x_test03.txt', x_num, x)

    print('')
    print('  H(X,T) written to "h_test03.txt"')
    print('  T values written to "t_test03.txt"')
    print('  X values written to "x_test3.txt"')
#
#  Terminate.
#
    print('')
    print('FD1D_HEAT_IMPLICIT_TEST03:')
    print('  Normal end of execution.')
    return


def bc_test03(x_num, x, t, h):

    # *****************************************************************************80
    #
    # BC_TEST03 evaluates the boundary conditions for problem 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 January 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer X_NUM, the number of nodes.
    #
    #    Input, real X(X_NUM), the node coordinates.
    #
    #    Input, real T, the current time.
    #
    #    Input, real H(X_NUM), the current heat values.
    #
    #    Output, real H(X_NUM), the current heat values, after boundary
    #    conditions have been imposed.
    #
    h[0] = 15.0
    h[x_num - 1] = 25.0

    return h


def ic_test03(x_num, x, t):

    # *****************************************************************************80
    #
    # IC_TEST03 evaluates the initial condition for problem 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 January 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer X_NUM, the number of nodes.
    #
    #    Input, real X(X_NUM), the node coordinates.
    #
    #    Input, real T, the initial time.
    #
    #    Output, real H(X_NUM), the heat values at the initial time.
    #
    import numpy as np

    h = np.zeros(x_num)

    for i in range(0, x_num):
        if (x[i] < 0.0):
            h[i] = 50.0
        elif (x[i] == 0.0):
            h[i] = 20.0
        else:
            h[i] = 25.0

    return h


def k_test03():

    # *****************************************************************************80
    #
    # K_TEST03 evaluates the conductivity for problem 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real K, the conducitivity.
    #
    k = 2.0

    return k


def rhs_test03(x_num, x, t):

    # *****************************************************************************80
    #
    # RHS_TEST03 evaluates the right hand side for problem 3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 January 2012
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer X_NUM, the number of nodes.
    #
    #    Input, real X(X_NUM), the node coordinates.
    #
    #    Input, real T, the current time.
    #
    #    Output, real VALUE(X_NUM), the source term.
    #
    import numpy as np

    value = np.zeros(x_num)

    return value


def fd1d_heat_implicit_test():

    # *****************************************************************************80
    #
    # FD1D_HEAT_IMPLICIT_TEST tests the FD1D_HEAT_IMPLICIT library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('FD1D_HEAT_IMPLICIT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the FD1D_HEAT_IMPLICIT library.')

    fd1d_heat_implicit_test01()
    fd1d_heat_implicit_test02()
    fd1d_heat_implicit_test03()
#
#  Terminate.
#
    print('')
    print('FD1D_HEAT_IMPLICIT_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_write(filename, m, n, a):

    # *****************************************************************************80
    #
    # R8MAT_WRITE writes an R8MAT to a file.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, string FILENAME, the name of the output file.
    #
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, real A(M,N), the matrix.
    #
    output = open(filename, 'w')

    for i in range(0, m):
        for j in range(0, n):
            s = '  %g' % (a[i, j])
            output.write(s)
        output.write('\n')

    output.close()

    return


def r8mat_write_test():

    # *****************************************************************************80
    #
    # R8MAT_WRITE_TEST tests R8MAT_WRITE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8MAT_WRITE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test R8MAT_WRITE, which writes an R8MAT to a file.')

    filename = 'r8mat_write_test.txt'
    m = 5
    n = 3
    a = np.array((
        (1.1, 1.2, 1.3),
        (2.1, 2.2, 2.3),
        (3.1, 3.2, 3.3),
        (4.1, 4.2, 4.3),
        (5.1, 5.2, 5.3)))
    r8mat_write(filename, m, n, a)

    print('')
    print('  Created file "%s".' % (filename))
#
#  Terminate.
#
    print('')
    print('R8MAT_WRITE_TEST:')
    print('  Normal end of execution.')
    return


def r8vec_write(filename, n, a):

    # *****************************************************************************80
    #
    # R8VEC_WRITE writes an R8VEC to a file.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, string FILENAME, the name of the output file.
    #
    #    Input, integer N, the number of entries in A.
    #
    #    Input, real A(N), the matrix.
    #
    output = open(filename, 'w')

    for i in range(0, n):
        s = '  %g\n' % (a[i])
        output.write(s)

    output.close()

    return


def r8vec_write_test():

    # *****************************************************************************80
    #
    # R8VEC_WRITE_TEST tests R8VEC_WRITE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8VEC_WRITE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test R8VEC_WRITE, which writes an R8VEC to a file.')
    filename = 'r8vec_write_test.txt'
    n = 5
    a = np.array((1.1, 2.2, 3.3, 4.4, 5.5))
    r8vec_write(filename, n, a)

    print('')
    print('  Created file "%s".' % (filename))
#
#  Terminate.
#
    print('')
    print('R8VEC_WRITE_TEST:')
    print('  Normal end of execution.')
    return



if (__name__ == '__main__'):
    timestamp()
    fd1d_heat_implicit_test()
    timestamp()
