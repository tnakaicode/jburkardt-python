#! /usr/bin/env python3
#


def lorenz_ode_test():

    # *****************************************************************************80
    #
    # LORENZ_ODE_TEST tests LORENZ_ODE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 May 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('LORENZ_ODE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Compute solutions of the Lorenz system.')
    print('  Plot solution components (T,X(T)), (T,Y(T)), and (T,Z(T)).')
    print('  Plot (X(T),Y(T),Z(T)).')

    n = 2000

    t, x, y, z = lorenz_ode_compute(n)
    lorenz_ode_plot_components(n, t, x, y, z)
    lorenz_ode_plot_3d(n, t, x, y, z)
#
#  Terminate.
#
    print('')
    print('LORENZ_ODE_TEST:')
    print('  Normal end of execution.')
    return


def lorenz_ode_compute(n):

    # *****************************************************************************80
    #
    # LORENZ_ODE_COMPUTE computes a solution of the Lorenz ODE system.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 May 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real T(N+1), X(N+1), Y(N+1), Z(N+1), the T, X, Y, and Z values
    #    of the discrete solution.
    #
    import numpy as np
    import sys

    t_final = 40.0
    dt = t_final / n
#
#  Initial conditions.
#
    t = np.linspace(0.0, t_final, n + 1)

    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    z = np.zeros(n + 1)

    x[0] = 8.0
    y[0] = 1.0
    z[0] = 1.0
#
#  Compute the approximate solution at equally spaced times.
#
#  I really can't decide whether it's better to use X, Y, Z vectors,
#  or one big array XYZ.  Each approach has its drawbacks and uglinesses.
#
    for j in range(0, n):

        xyz = np.array([x[j], y[j], z[j]])
        xyz = rk4vec(t[j], 3, xyz, dt, lorenz_rhs)

        x[j + 1] = xyz[0]
        y[j + 1] = xyz[1]
        z[j + 1] = xyz[2]
        sys.stdout.write("\r {} / {}".format(j, n))
        sys.stdout.flush()

    return t, x, y, z


def lorenz_ode_plot_components(n, t, x, y, z):

    # *****************************************************************************80
    #
    # LORENZ_ODE_PLOT_COMPONENTS plots X(T), Y(T) and Z(T) for the Lorenz ODE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 May 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real T(N+1), the value of the independent variable.
    #
    #    Input, real X(N+1), Y(N+1), Z(N+1), the values of the dependent
    #    variables at time T.
    #
    #
    import matplotlib.pyplot as plt
#
#  Plot the data.
#
    plt.plot(t, x, linewidth=2, color='b')
    plt.plot(t, y, linewidth=2, color='r')
    plt.plot(t, z, linewidth=2, color='g')
    plt.grid(True)
    plt.xlabel('<--- Time --->')
    plt.ylabel('<--- X(T), Y(T), Z(T) --->')
    plt.title('Lorenz Time Series Plot')
    plt.savefig('lorenz_ode_components.png')
    print('')
    print('  Graphics data saved as "lorenz_ode_components.png"')
    plt.show(block=False)
    plt.clf()

    return


def lorenz_ode_plot_3d(n, t, x, y, z):

    # *****************************************************************************80
    #
    # LORENZ_ODE_PLOT_3D plots (X,Y,Z) for the Lorenz ODE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 May 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real T(N+1), the value of the independent variable.
    #
    #    Input, real X(N+1), Y(N+1), Z(N+1), the values of the dependent
    #    variables at time T.
    #
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
#
#  Plot the data.
#
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z, linewidth=2, color='b')
    ax.grid(True)
    ax.set_xlabel('<--- X(T) --->')
    ax.set_ylabel('<--- Y(T) --->')
    ax.set_zlabel('<--- Z(T) --->')
    ax.set_title('Lorenz 3D Plot')
    plt.savefig('lorenz_ode_3d.png')
    print('')
    print('  Graphics data saved as "lorenz_ode_3d.png"')
    plt.show(block=False)
    plt.clf()

    return


def lorenz_rhs(t, m, xyz):

    # *****************************************************************************80
    #
    # LORENZ_RHS evaluates the right hand side of the Lorenz ODE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 May 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real T, the value of the independent variable.
    #
    #    Input, integer M, the dimension of XYZ.
    #
    #    Input, real XYZ[3], the values of the dependent variables at time T.
    #
    #    Output, real DXDT(M), the values of the derivatives
    #    of the dependent variables at time T.
    #
    import numpy as np

    beta = 8.0 / 3.0
    rho = 28.0
    sigma = 10.0

    dxdt = np.zeros(3)

    dxdt[0] = sigma * (xyz[1] - xyz[0])
    dxdt[1] = xyz[0] * (rho - xyz[2]) - xyz[1]
    dxdt[2] = xyz[0] * xyz[1] - beta * xyz[2]

    return dxdt


def rk4vec(t0, m, u0, dt, f):

    # *****************************************************************************80
    #
    # RK4VEC takes one Runge-Kutta step for a vector ODE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 May 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real T0, the current time.
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, real U0(M), the solution estimate at the current time.
    #
    #    Input, real DT, the time step.
    #
    #    Input, function uprime = F ( t, m, u  )
    #    which evaluates the derivative UPRIME(1:M) given the time T and
    #    solution vector U(1:M).
    #
    #    Output, real U(M), the fourth-order Runge-Kutta solution
    #    estimate at time T0+DT.
    #
    import numpy as np
#
#  Get four sample values of the derivative.
#
    f0 = f(t0, m, u0)

    t1 = t0 + dt / 2.0
    u1 = u0 + dt * f0 / 2.0
    f1 = f(t1, m, u1)

    t2 = t0 + dt / 2.0
    u2 = u0 + dt * f1 / 2.0
    f2 = f(t2, m, u2)

    t3 = t0 + dt
    u3 = u0 + dt * f2
    f3 = f(t1, m, u1)
#
#  Combine them to estimate the solution U at time T1.
#
    u = u0 + dt * (f0 + 2.0 * f1 + 2.0 * f2 + f3) / 6.0

    return u


def timestamp():

    # *****************************************************************************80
    #
    # TIMESTAMP prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import time

    t = time.time()
    print(time.ctime(t))

    return None


def timestamp_test():

    # *****************************************************************************80
    #
    # TIMESTAMP_TEST tests TIMESTAMP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import platform

    print('')
    print('TIMESTAMP_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TIMESTAMP prints a timestamp of the current date and time.')
    print('')

    timestamp()
#
#  Terminate.
#
    print('')
    print('TIMESTAMP_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    lorenz_ode_test()
    timestamp()
