#! /usr/bin/env python3
#


def euler(dydt, tspan, y0, n):

    # *****************************************************************************80
    #
    # euler approximates an ODE solution using Euler's method.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2020
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    function dydt: the right hand side of the differential equation.
    #
    #    real tspan[2]: the starting and ending points.
    #
    #    real y0: the initial condition.
    #
    #    integer n: the number of steps to take.
    #
    #  Output:
    #
    #    real t(n+1), y(n+1): the sequence of solution estimates.
    #
    import numpy as np

    t0 = tspan[0]
    t1 = tspan[1]
    dt = (t1 - t0) / float(n)
    t = np.linspace(t0, t1, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + dt * dydt(t[i], y[i])

    return t, y


def humps_deriv(x, y):

    # *****************************************************************************80
    #
    # humps_deriv evaluates the derivative of the humps def for an ODE solver.
    #
    #  Discussion:
    #
    #    This verion of "humps_deriv" appends the input argument "y", as expected
    #    by most ODE solving software.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x(): the arguments.
    #
    #    real y(): the value of the humps function.
    #
    #  Output:
    #
    #    real yp(): the value of the derivative of the humps function.
    #
    yp = - 1.0 / ((x - 0.3)**2 + 0.01)**2 \
        * 2.0 * (x - 0.3) \
        - 1.0 / ((x - 0.9)**2 + 0.04)**2 \
        * 2.0 * (x - 0.9)

    return yp


def humps_euler():

    # *****************************************************************************80
    #
    # humps_euler ???
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import matplotlib.pyplot as plt
    import numpy as np
    import platform

    print('')
    print('humps_euler')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the euler ode integrator on the humps problem.')

    t0 = 0.0
    t1 = 2.0
    tspan = np.array([t0, t1])
    y0 = humps_fun(t0)
    n = 100

    [t, y] = euler(humps_deriv, tspan, y0, n)

    plt.clf()

    plt.plot(t, y, 'b-', linewidth=2)

    if (t0 <= 0.0 and 0.0 <= t1):
        plt.plot([t0, t1], [0, 0], 'k-', linewidth=2)

    ymin = min(y)
    ymax = max(y)
    if (ymin <= 0.0 and 0.0 <= ymax):
        plt.plot([0, 0], [ymin, ymax], 'k-', linewidth=2)

    plt.grid(True)
    plt.xlabel('<--- t --->')
    plt.ylabel('<--- y(t) --->')
    plt.title('y = humps(t)')
    filename = 'humps_euler.png'
    plt.savefig(filename)
    print('  Graphics saved as "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('humps_euler_test:')
    print('  Normal end of execution.')

    return


def humps_fun(x):

    # *****************************************************************************80
    #
    # humps_fun evaluates the humps function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Input:
    #
    #    real x(): the evaluation points.
    #
    #  Output:
    #
    #    real y(): the def values.
    #
    y = 1.0 / ((x - 0.3)**2 + 0.01) \
        + 1.0 / ((x - 0.9)**2 + 0.04) \
        - 6.0

    return y


def timestamp():

    # *****************************************************************************80
    #
    # timestamp prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 August 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import time

    t = time.time()
    print(time.ctime(t))

    return


if (__name__ == '__main__'):
    timestamp()
    humps_euler()
    timestamp()
