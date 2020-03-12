#! /usr/bin/env python3
#


def grid_2d(x_num, x_lo, x_hi, y_num, y_lo, y_hi):

    # *****************************************************************************80
    #
    # GRID_2D returns a regular 2D grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer X_NUM, the number of X values to use.
    #
    #    Input, real X_LO, X_HI, the range of X values.
    #
    #    Input, integer Y_NUM, the number of Y values to use.
    #
    #    Input, real Y_LO, Y_HI, the range of Y values.
    #
    #    Output, real X(X_NUM*Y_NUM), Y(X_NUM*Y_NUM), the coordinates of the grid.
    #
    import numpy as np

    x = np.zeros(x_num * y_num)
    y = np.zeros(x_num * y_num)

    if (x_num == 1):
        xi = (x_lo + x_hi) / 2.0
        k = 0
        for j in range(0, y_num):
            for i in range(0, x_num):
                x[k] = xi
                k = k + 1
    else:
        k = 0
        for j in range(0, y_num):
            for i in range(0, x_num):
                xi = (float(x_num - i - 1) * x_lo
                      + float(i) * x_hi) \
                    / float(x_num - 1)
                x[k] = xi
                k = k + 1

    if (y_num == 1):
        yj = (y_lo + y_hi) / 2.0
        k = 0
        for j in range(0, y_num):
            for i in range(0, x_num):
                y[k] = yj
                k = k + 1
    else:
        k = 0
        for j in range(0, y_num):
            yj = (float(y_num - j - 1) * y_lo
                  + float(j) * y_hi) \
                / float(y_num - 1)
            for i in range(0, x_num):
                y[k] = yj
                k = k + 1

    return x, y


def grid_2d_test():

    # *****************************************************************************80
    #
    # GRID_2D_TEST makes a small 2D grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('GRID_2D_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate a regular grid.')

    x_lo = 10.0
    x_hi = 20.0
    x_num = 5

    y_lo = 5.0
    y_hi = 6.0
    y_num = 3

    [x, y] = grid_2d(x_num, x_lo, x_hi, y_num, y_lo, y_hi)

    print('')
    k = 0
    for j in range(0, y_num):
        for i in range(0, x_num):
            print('  %2d  %2d  %2d  %14.6f  %14.6f' % (k, i, j, x[k], y[k]))
            k = k + 1
#
#  Terminate.
#
    print('')
    print('GRID_2D_TEST:')
    print('  Normal end of execution.')
    return


def ns2de_gnuplot(header, n, x, y, u, v, p, s):

    # *****************************************************************************80
    #
    # NS2DE_GNUPLOT writes the Navier-Stokes velocity field to files for GNUPLOT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, string HEADER, a header to be used to name the files.
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the coordinates of the evaluation points.
    #
    #    Input, real U(N), V(N), P(N), the flow field samples.
    #
    #    Input, real S, a scale factor for the velocity vectors.
    #

    #
    #  Write the data file.
    #
    data_filename = header + '_data.txt'

    data_unit = open(data_filename, 'w')

    for i in range(0, n):
        st = '  %g' % (x[i])
        data_unit.write(st)
        st = '  %g' % (y[i])
        data_unit.write(st)
        st = '  %g' % (u[i])
        data_unit.write(st)
        st = '  %g' % (v[i])
        data_unit.write(st)
        st = '  %g' % (s * u[i])
        data_unit.write(st)
        st = '  %g' % (s * v[i])
        data_unit.write(st)
        st = '  %g' % (p[i])
        data_unit.write(st)
        data_unit.write('\n')

    data_unit.close()

    print('')
    print('  Data written to "%s".' % (data_filename))
#
#  Write the command file.
#
    command_filename = header + '_commands.txt'
    plot_filename = header + '.png'

    command_unit = open(command_filename, 'w')

    command_unit.write('#  %s\n' % (command_filename))
    command_unit.write('#\n')
    command_unit.write('set term png\n')
    command_unit.write('set output "%s"\n' % (plot_filename))
    command_unit.write('#\n')
    command_unit.write('#  Add titles and labels.\n')
    command_unit.write('#\n')
    command_unit.write('set xlabel "<--- X --->"\n')
    command_unit.write('set ylabel "<--- Y --->"\n')
    command_unit.write('set title "Navier-Stokes velocity field"\n')
    command_unit.write('unset key\n')
    command_unit.write('#\n')
    command_unit.write('#  Add grid lines.\n')
    command_unit.write('#\n')
    command_unit.write('set grid\n')
    command_unit.write('set size ratio -1\n')
    command_unit.write('#\n')
    command_unit.write('#  Timestamp the plot.\n')
    command_unit.write('#\n')
    command_unit.write('set timestamp\n')
    command_unit.write(
        'plot "%s" using 1:2:5:6 with vectors \\\n' % (data_filename))
    command_unit.write('  head filled lt 2 linecolor rgb "blue"\n')
    command_unit.write('quit\n')

    data_unit.close()

    print('  Commands written to "%s".' % (command_filename))

    return


def ns2de_gnuplot_lukas_test():

    # *****************************************************************************80
    #
    # NS2DE_GNUPLOT_LUKAS_TEST plots the Lukas Bystricky flow field.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NS2DE_GNUPLOT_LUKAS_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate the Lukas Bystricky velocity field on a regular grid.')
    print('  Store in GNUPLOT data and command files.')

    x_lo = 0.0
    x_hi = 1.0
    x_num = 21

    y_lo = 0.0
    y_hi = 1.0
    y_num = 21

    [x, y] = grid_2d(x_num, x_lo, x_hi, y_num, y_lo, y_hi)

    nu = 1.0
    rho = 1.0
    n = x_num * y_num
    t = 0.0

    [u, v, p] = uvp_lukas(nu, rho, n, x, y, t)

    header = 'lukas'
    s = 0.25
    ns2de_gnuplot(header, n, x, y, u, v, p, s)
#
#  Terminate.
#
    print('')
    print('NS2DE_GNUPLOT_LUKAS_TEST:')
    print('  Normal end of execution.')
    return


def ns2de_gnuplot_poiseuille_test():

    # *****************************************************************************80
    #
    # NS2DE_GNUPLOT_POISEUILLE_TEST plots a Poiseuille velocity field.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NS2DE_GNUPLOT_POISEUILLE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate a Poiseuille velocity field on a regular grid.')
    print('  Store in GNUPLOT data and command files.')

    x_lo = 0.0
    x_hi = 6.0
    x_num = 61

    y_lo = -1.0
    y_hi = +1.0
    y_num = 21

    [x, y] = grid_2d(x_num, x_lo, x_hi, y_num, y_lo, y_hi)

    nu = 1.0
    rho = 1.0
    n = x_num * y_num
    t = 0.0

    [u, v, p] = uvp_poiseuille(nu, rho, n, x, y, t)

    header = 'poiseuille'
    s = 0.5
    ns2de_gnuplot(header, n, x, y, u, v, p, s)
#
#  Terminate.
#
    print('')
    print('NS2DE_GNUPLOT_POISEUILLE_TEST:')
    print('  Normal end of execution.')
    return


def ns2de_gnuplot_spiral_test():

    # *****************************************************************************80
    #
    # NS2DE_GNUPLOT_SPIRAL_TEST plots a Spiral velocity field.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NS2DE_GNUPLOT_SPIRAL_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate a Spiral Flow velocity field on a regular grid.')
    print('  Store in GNUPLOT data and command files.')

    x_lo = 0.0
    x_hi = 1.0
    x_num = 21

    y_lo = 0.0
    y_hi = 1.0
    y_num = 21

    [x, y] = grid_2d(x_num, x_lo, x_hi, y_num, y_lo, y_hi)

    nu = 1.0
    rho = 1.0
    n = x_num * y_num
    t = 0.0

    [u, v, p] = uvp_spiral(nu, rho, n, x, y, t)

    header = 'spiral'
    s = 5.0
    ns2de_gnuplot(header, n, x, y, u, v, p, s)
#
#  Terminate.
#
    print('')
    print('NS2DE_GNUPLOT_SPIRAL_TEST:')
    print('  Normal end of execution.')
    return


def ns2de_gnuplot_taylor_test():

    # *****************************************************************************80
    #
    # NS2DE_GNUPLOT_TAYLOR_TEST plots a Taylor velocity field.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NS2DE_GNUPLOT_TAYLOR_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate a Taylor velocity field on a regular grid.')
    print('  Store in GNUPLOT data and command files.')

    x_lo = 0.5
    x_hi = 2.5
    x_num = 21

    y_lo = 0.5
    y_hi = 2.5
    y_num = 21

    [x, y] = grid_2d(x_num, x_lo, x_hi, y_num, y_lo, y_hi)

    nu = 1.0
    rho = 1.0
    n = x_num * y_num
    t = 0.0

    [u, v, p] = uvp_taylor(nu, rho, n, x, y, t)

    header = 'taylor'
    s = 0.10
    ns2de_gnuplot(header, n, x, y, u, v, p, s)
#
#  Terminate.
#
    print('')
    print('NS2DE_GNUPLOT_TAYLOR_TEST:')
    print('  Normal end of execution.')
    return


def ns2de_gnuplot_vortex_test():

    # *****************************************************************************80
    #
    # NS2DE_GNUPLOT_VORTEX_TEST plots a Vortex velocity field.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NS2DE_GNUPLOT_VORTEX_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate a Vortex velocity field on a regular grid.')
    print('  Store in GNUPLOT data and command files.')

    x_lo = 0.5
    x_hi = 1.5
    x_num = 21

    y_lo = 0.5
    y_hi = 1.5
    y_num = 21

    [x, y] = grid_2d(x_num, x_lo, x_hi, y_num, y_lo, y_hi)

    nu = 1.0
    rho = 1.0
    n = x_num * y_num
    t = 0.0

    [u, v, p] = uvp_vortex(nu, rho, n, x, y, t)

    header = 'vortex'
    s = 0.10
    ns2de_gnuplot(header, n, x, y, u, v, p, s)
#
#  Terminate.
#
    print('')
    print('NS2DE_GNUPLOT_VORTEX_TEST:')
    print('  Normal end of execution.')
    return


def ns2de_matplotlib(header, n, x, y, u, v, p, s):

    # *****************************************************************************80
    #
    # NS2DE_MATPLOTLIB plots a velocity vector field with MATPLOTLIB.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, string HEADER, a header to be used to name the files.
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, real X(N), Y(N), the coordinates of the evaluation points.
    #
    #    Input, real U(N), V(N), P(N), the solution samples.
    #
    #    Input, real S, a scale factor for the velocity vectors.
    #
    import matplotlib.pyplot as plt

    myplot = plt.figure()
    ax = plt.gca()
    ax.quiver(x, y, u, v)
    ax.set_xlabel('<--X-->')
    ax.set_ylabel('<--Y-->')
    ax.set_title(header)
    ax.axis('equal')
    plt.draw()
    plt.show(block=False)

    plot_filename = header + '_matplotlib.png'
    myplot.savefig(plot_filename)

    return


def ns2de_matplotlib_lukas_test():

    # *****************************************************************************80
    #
    # NS2DE_MATPLOTLIB_LUKAS_TEST plots a Lukas Bystricky velocity field.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NS2DE_MATPLOTLIB_LUKAS_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate a Lukas Bystricky Flow field on a regular grid.')
    print('  Display it using MATPLOTLIB')

    x_lo = 0.0
    x_hi = 1.0
    x_num = 21

    y_lo = 0.0
    y_hi = 1.0
    y_num = 21

    x, y = grid_2d(x_num, x_lo, x_hi, y_num, y_lo, y_hi)

    nu = 1.0
    rho = 1.0
    n = x_num * y_num
    t = 0.0

    u, v, p = uvp_lukas(nu, rho, n, x, y, t)

    header = 'lukas'
    s = 0.25
    ns2de_matplotlib(header, n, x, y, u, v, p, s)
#
#  Terminate.
#
    print('')
    print('NS2DE_MATPLOTLIB_LUKAS_TEST:')
    print('  Normal end of execution.')
    return


def ns2de_matplotlib_poiseuille_test():

    # *****************************************************************************80
    #
    # NS2DE_MATPLOTLIB_POISEUILLE_TEST plots a Poiseuille velocity field.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NS2DE_MATPLOTLIB_POISEUILLE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate a Poiseuille velocity field on a regular grid.')
    print('  Display it using MATPLOTLIB')

    x_lo = 0.0
    x_hi = 6.0
    x_num = 61

    y_lo = -1.0
    y_hi = +1.0
    y_num = 21

    x, y = grid_2d(x_num, x_lo, x_hi, y_num, y_lo, y_hi)

    nu = 1.0
    rho = 1.0
    n = x_num * y_num
    t = 0.0

    u, v, p = uvp_poiseuille(nu, rho, n, x, y, t)

    header = 'poiseuille'
    s = 5.0
    ns2de_matplotlib(header, n, x, y, u, v, p, s)
#
#  Terminate.
#
    print('')
    print('NS2DE_MATPLOTLIB_POISEUILLE_TEST:')
    print('  Normal end of execution.')
    return


def ns2de_matplotlib_spiral_test():

    # *****************************************************************************80
    #
    # NS2DE_MATPLOTLIB_SPIRAL_TEST plots a Spiral velocity field.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NS2DE_MATPLOTLIB_SPIRAL_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate a Spiral Flow velocity field on a regular grid.')
    print('  Display it using MATPLOTLIB')

    x_lo = 0.0
    x_hi = 1.0
    x_num = 21

    y_lo = 0.0
    y_hi = 1.0
    y_num = 21

    x, y = grid_2d(x_num, x_lo, x_hi, y_num, y_lo, y_hi)

    nu = 1.0
    rho = 1.0
    n = x_num * y_num
    t = 0.0

    u, v, p = uvp_spiral(nu, rho, n, x, y, t)

    header = 'spiral'
    s = 5.0
    ns2de_matplotlib(header, n, x, y, u, v, p, s)
#
#  Terminate.
#
    print('')
    print('NS2DE_MATPLOTLIB_SPIRAL_TEST:')
    print('  Normal end of execution.')
    return


def ns2de_matplotlib_taylor_test():

    # *****************************************************************************80
    #
    # NS2DE_MATPLOTLIB_TAYLOR_TEST plots a Taylor Flow field.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NS2DE_MATPLOTLIB_TAYLOR_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate a Taylor velocity field on a regular grid.')
    print('  Display it using MATPLOTLIB')

    x_lo = 0.5
    x_hi = 2.5
    x_num = 21

    y_lo = 0.5
    y_hi = 2.5
    y_num = 21

    x, y = grid_2d(x_num, x_lo, x_hi, y_num, y_lo, y_hi)

    nu = 1.0
    rho = 1.0
    n = x_num * y_num
    t = 0.0

    u, v, p = uvp_taylor(nu, rho, n, x, y, t)

    header = 'taylor'
    s = 0.10
    ns2de_matplotlib(header, n, x, y, u, v, p, s)
#
#  Terminate.
#
    print('')
    print('NS2DE_MATPLOTLIB_TAYLOR_TEST:')
    print('  Normal end of execution.')
    return


def ns2de_matplotlib_vortex_test():

    # *****************************************************************************80
    #
    # NS2DE_MATPLOTLIB_VORTEX_TEST plots a Vortex velocity field.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NS2DE_MATPLOTLIB_VORTEX_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Generate a Vortex velocity field on a regular grid.')
    print('  Display it using MATPLOTLIB')

    x_lo = 0.5
    x_hi = 1.5
    x_num = 21

    y_lo = 0.5
    y_hi = 1.5
    y_num = 21

    x, y = grid_2d(x_num, x_lo, x_hi, y_num, y_lo, y_hi)

    nu = 1.0
    rho = 1.0
    n = x_num * y_num
    t = 0.0

    u, v, p = uvp_vortex(nu, rho, n, x, y, t)

    header = 'vortex'
    s = 0.25
    ns2de_matplotlib(header, n, x, y, u, v, p, s)
#
#  Terminate.
#
    print('')
    print('NS2DE_MATPLOTLIB_VORTEX_TEST:')
    print('  Normal end of execution.')
    return


def parameter_poiseuille_test():

    # *****************************************************************************80
    #
    # PARAMETER_POISEUILLE_TEST: Poiseuille solution norms for various values of NU, RHO.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/parameter_poiseuille_test.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('PARAMETER_POISEUILLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Poiseuille Flow')
    print('  Monitor solution norms for various')
    print('  values of NU, RHO.')

    n = 1000
    x_lo = 0.0
    x_hi = 6.0
    y_lo = -1.0
    y_hi = +1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, y_lo, y_hi, seed)
#
#  Vary RHO.
#
    print('')
    print('  RHO affects the pressure scaling.')
    print('')
    print('     RHO         NU           T     ||U||       ||V||       ||P||')
    print('')

    nu = 1.0
    rho = 1.0

    for j in range(0, 3):

        for k in range(0, 6):

            t = k / 5.0

            u, v, p = uvp_poiseuille(nu, rho, n, x, y, t)

            u_norm = r8vec_norm_l2(n, u) / n
            v_norm = r8vec_norm_l2(n, v) / n
            p_norm = r8vec_norm_l2(n, p) / n

            print('  %10.4g  %10.4g  %8.4g  %10.4g  %10.4g  %10.4g'
                  % (rho, nu, t, u_norm, v_norm, p_norm))

        print('')
        rho = rho / 100.0
#
#  Vary NU.
#
    print('')
    print('  NU affects the time scaling.')
    print('')
    print('     RHO         NU           T     ||U||       ||V||       ||P||')
    print('')

    nu = 1.0
    rho = 1.0

    for i in range(0, 4):

        for k in range(0, 6):

            t = k / 5.0

            u, v, p = uvp_poiseuille(nu, rho, n, x, y, t)

            u_norm = r8vec_norm_l2(n, u) / n
            v_norm = r8vec_norm_l2(n, v) / n
            p_norm = r8vec_norm_l2(n, p) / n

            print('  %10.4g  %10.4g  %8.4g  %10.4g  %10.4g  %10.4g'
                  % (rho, nu, t, u_norm, v_norm, p_norm))

        print('')

        nu = nu / 10.0
#
#  Terminate.
#
    print('')
    print('PARAMETER_POISEUILLE_TEST:')
    print('  Normal end of execution.')
    return


def parameter_spiral_test():

    # *****************************************************************************80
    #
    # PARAMETER_SPIRAL_TEST: solution norms over time for various values of NU, RHO.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/parameter_spiral_test.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('PARAMETER_SPIRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Spiral Flow')
    print('  Monitor solution norms over time for various')
    print('  values of NU, RHO.')

    n = 1000
    xy_lo = 0.0
    xy_hi = 1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, xy_lo, xy_hi, seed)
    y, seed = r8vec_uniform_ab(n, xy_lo, xy_hi, seed)
#
#  Vary RHO.
#
    print('')
    print('  RHO affects the pressure scaling.')
    print('')
    print('     RHO         NU           T     ||U||       ||V||       ||P||')
    print('')

    nu = 1.0
    rho = 1.0

    for j in range(0, 3):

        for k in range(0, 6):

            t = k / 5.0

            u, v, p = uvp_spiral(nu, rho, n, x, y, t)

            u_norm = r8vec_norm_l2(n, u) / n
            v_norm = r8vec_norm_l2(n, v) / n
            p_norm = r8vec_norm_l2(n, p) / n

            print('  %10.4g  %10.4g  %8.4g  %10.4g  %10.4g  %10.4g'
                  % (rho, nu, t, u_norm, v_norm, p_norm))

        print('')
        rho = rho / 100.0
#
#  Vary NU.
#
    print('')
    print('  NU affects the time scaling.')
    print('')
    print('     RHO         NU           T     ||U||       ||V||       ||P||')
    print('')

    nu = 1.0
    rho = 1.0

    for i in range(0, 4):

        for k in range(0, 6):

            t = k / 5.0

            u, v, p = uvp_spiral(nu, rho, n, x, y, t)

            u_norm = r8vec_norm_l2(n, u) / n
            v_norm = r8vec_norm_l2(n, v) / n
            p_norm = r8vec_norm_l2(n, p) / n

            print('  %10.4g  %10.4g  %8.4g  %10.4g  %10.4g  %10.4g'
                  % (rho, nu, t, u_norm, v_norm, p_norm))

        print('')

        nu = nu / 10.0
#
#  Terminate.
#
    print('')
    print('PARAMETER_SPIRAL_TEST:')
    print('  Normal end of execution.')
    return


def parameter_taylor_test():

    # *****************************************************************************80
    #
    # PARAMETER_TAYLOR_TEST monitors Taylor solution norms for various NU, RHO.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/parameter_taylor_test.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('PARAMETER_TAYLOR_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Taylor Flow')
    print('  Monitor solution norms over time for various')
    print('  values of NU, RHO.')

    n = 1000
    xy_lo = 0.5
    xy_hi = 2.5
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, xy_lo, xy_hi, seed)
    y, seed = r8vec_uniform_ab(n, xy_lo, xy_hi, seed)
#
#  Vary RHO.
#
    print('')
    print('  RHO affects the pressure scaling.')
    print('')
    print('     RHO         NU           T     ||U||       ||V||       ||P||')
    print('')

    nu = 1.0
    rho = 1.0

    for j in range(0, 3):

        for k in range(0, 6):

            t = k / 5.0

            u, v, p = uvp_taylor(nu, rho, n, x, y, t)

            u_norm = r8vec_norm_l2(n, u) / n
            v_norm = r8vec_norm_l2(n, v) / n
            p_norm = r8vec_norm_l2(n, p) / n

            print('  %10.4g  %10.4g  %8.4g  %10.4g  %10.4g  %10.4g'
                  % (rho, nu, t, u_norm, v_norm, p_norm))

        print('')
        rho = rho / 100.0
#
#  Vary NU.
#
    print('')
    print('  NU affects the time scaling.')
    print('')
    print('     RHO         NU           T     ||U||       ||V||       ||P||')
    print('')

    nu = 1.0
    rho = 1.0

    for i in range(0, 4):

        for k in range(0, 6):

            t = k / 5.0

            u, v, p = uvp_taylor(nu, rho, n, x, y, t)

            u_norm = r8vec_norm_l2(n, u) / n
            v_norm = r8vec_norm_l2(n, v) / n
            p_norm = r8vec_norm_l2(n, p) / n

            print('  %10.4g  %10.4g  %8.4g  %10.4g  %10.4g  %10.4g'
                  % (rho, nu, t, u_norm, v_norm, p_norm))

        print('')

        nu = nu / 10.0
#
#  Terminate.
#
    print('')
    print('PARAMETER_TAYLOR_TEST:')
    print('  Normal end of execution.')
    return


def parameter_vortex_test():

    # *****************************************************************************80
    #
    # PARAMETER_VORTEX_TEST monitors Vortex solution norms for various values of NU, RHO.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/parameter_vortex_test.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('PARAMETER_VORTEX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Vortex Flow')
    print('  Monitor solution norms over time for various')
    print('  values of NU, RHO.')

    n = 1000
    xy_lo = 0.5
    xy_hi = 2.5
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, xy_lo, xy_hi, seed)
    y, seed = r8vec_uniform_ab(n, xy_lo, xy_hi, seed)
#
#  Vary RHO.
#
    print('')
    print('  RHO affects the pressure scaling.')
    print('')
    print('     RHO         NU           T     ||U||       ||V||       ||P||')
    print('')

    nu = 1.0
    rho = 1.0

    for j in range(0, 3):

        for k in range(0, 6):

            t = k / 5.0

            u, v, p = uvp_vortex(nu, rho, n, x, y, t)

            u_norm = r8vec_norm_l2(n, u) / n
            v_norm = r8vec_norm_l2(n, v) / n
            p_norm = r8vec_norm_l2(n, p) / n

            print('  %10.4g  %10.4g  %8.4g  %10.4g  %10.4g  %10.4g'
                  % (rho, nu, t, u_norm, v_norm, p_norm))

        print('')
        rho = rho / 100.0
#
#  Vary NU.
#
    print('')
    print('  NU affects the time scaling.')
    print('')
    print('     RHO         NU           T     ||U||       ||V||       ||P||')
    print('')

    nu = 1.0
    rho = 1.0

    for i in range(0, 4):

        for k in range(0, 6):

            t = k / 5.0

            u, v, p = uvp_vortex(nu, rho, n, x, y, t)

            u_norm = r8vec_norm_l2(n, u) / n
            v_norm = r8vec_norm_l2(n, v) / n
            p_norm = r8vec_norm_l2(n, p) / n

            print('  %10.4g  %10.4g  %8.4g  %10.4g  %10.4g  %10.4g'
                  % (rho, nu, t, u_norm, v_norm, p_norm))

        print('')

        nu = nu / 10.0
#
#  Terminate.
#
    print('')
    print('PARAMETER_VORTEX_TEST:')
    print('  Normal end of execution.')
    return


def r8vec_amax(n, a):

    # *****************************************************************************80
    #
    # R8VEC_AMAX returns the maximum absolute value in an R8VEC.
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A(N), the vector.
    #
    #    Output, real VALUE, the maximum absolute value in the vector.
    #
    value = 0.0
    for i in range(0, n):
        if (value < abs(a[i])):
            value = abs(a[i])

    return value


def r8vec_amin(n, a):

    # *****************************************************************************80
    #
    # R8VEC_AMIN returns the minimum absolute value in an R8VEC.
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A(N), the vector.
    #
    #    Output, real VALUE, the minimum absolute value in the vector.
    #
    r8_huge = 1.79769313486231571E+308

    value = r8_huge
    for i in range(0, n):
        if (abs(a[i]) < value):
            value = abs(a[i])

    return value


def r8vec_max(n, a):

    # *****************************************************************************80
    #
    # R8VEC_MAX returns the maximum value in an R8VEC.
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A(N), the vector.
    #
    #    Output, real VALUE, the maximum value in the vector.
    #
    r8_huge = 1.79769313486231571E+308

    value = - r8_huge
    for i in range(0, n):
        if (value < a[i]):
            value = a[i]

    return value


def r8vec_min(n, a):

    # *****************************************************************************80
    #
    # R8VEC_MIN returns the minimum value in an R8VEC.
    #
    #  Discussion:
    #
    #    An R8VEC is a vector of R8's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A(N), the vector.
    #
    #    Output, real VALUE, the minimum value in the vector.
    #
    r8_huge = 1.79769313486231571E+308

    value = r8_huge
    for i in range(0, n):
        if (a[i] < value):
            value = a[i]

    return value


def r8vec_norm_l2(n, a):

    # *****************************************************************************80
    #
    # R8VEC_NORM_L2 returns the L2 norm of an R8VEC.
    #
    #  Discussion:
    #
    #    The vector L2 norm is defined as:
    #
    #      value = sqrt ( sum ( 1 <= I <= N ) A(I)^2 ).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in A.
    #
    #    Input, real A(N), the vector whose L2 norm is desired.
    #
    #    Output, real VALUE, the L2 norm of A.
    #
    import numpy as np

    value = 0.0
    for i in range(0, n):
        value = value + a[i] * a[i]
    value = np.sqrt(value)

    return value


def r8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_PRINT prints an R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d:  %12g' % (i, a[i]))


def r8vec_uniform_ab(n, a, b, seed):

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_AB returns a scaled pseudorandom R8VEC.
    #
    #  Discussion:
    #
    #    Each dimension ranges from A to B.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Springer Verlag, pages 201-202, 1983.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, pages 362-376, 1986.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, pages 136-143, 1969.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, real A, B, the range of the pseudorandom values.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(N), the vector of pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    import numpy
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8VEC_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8VEC_UNIFORM_AB - Fatal error!')

    x = numpy.zeros(n)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        if (seed < 0):
            seed = seed + i4_huge

        x[i] = a + (b - a) * seed * 4.656612875E-10

    return x, seed


def resid_lukas(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # RESID_LUKAS returns residuals of the Lukas Bystricky Flow.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/resid_lukas.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinate or coordinates.
    #
    #    Output, real UR(N), VR(N), PR(N), the residuals in the U, V and P equations.
    #
    import numpy as np

    ur = np.zeros(n)
    vr = np.zeros(n)
    pr = np.zeros(n)
#
#  Get the right hand side functions.
#
    f, g, h = rhs_lukas(nu, rho, n, x, y, t)
#
#  Form the functions and derivatives for the left hand side.
#
    u = - np.cos(np.pi * x) / np.pi
    dudt = np.zeros(n)
    dudx = np.sin(np.pi * x)
    dudxx = np.pi * np.cos(np.pi * x)
    dudy = np.zeros(n)
    dudyy = np.zeros(n)

    v = - y * np.sin(np.pi * x)
    dvdt = np.zeros(n)
    dvdx = - np.pi * y * np.cos(np.pi * x)
    dvdxx = + np.pi * np.pi * y * np.sin(np.pi * x)
    dvdy = - np.sin(np.pi * x)
    dvdyy = np.zeros(n)

    p = np.zeros(n)
    dpdx = np.zeros(n)
    dpdy = np.zeros(n)
#
#  Evaluate the residuals.
#
    ur = dudt - nu * (dudxx + dudyy) + u * dudx + v * dudy + dpdx / rho - f
    vr = dvdt - nu * (dvdxx + dvdyy) + u * dvdx + v * dvdy + dpdy / rho - g
    pr = dudx + dvdy - h

    return ur, vr, pr


def resid_lukas_test():

    # *****************************************************************************80
    #
    # RESID_LUKAS_TEST samples Lukas Bystricky Flow residuals at the initial time.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('RESID_LUKAS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Lukas Bystricky Flow')
    print('  Sample the Navier-Stokes residuals')
    print('  at the initial time T = 0, over the unit square.')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    r8_lo = 0.0
    r8_hi = 1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, r8_lo, r8_hi, seed)
    y, seed = r8vec_uniform_ab(n, r8_lo, r8_hi, seed)
    t = 0.0

    ur, vr, pr = resid_lukas(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  Ur:  %14.6g  %14.6g' % (np.min(np.abs(ur)), np.max(np.abs(ur))))
    print('  Vr:  %14.6g  %14.6g' % (np.min(np.abs(vr)), np.max(np.abs(vr))))
    print('  Pr:  %14.6g  %14.6g' % (np.min(np.abs(pr)), np.max(np.abs(pr))))
#
#  Terminate.
#
    print('')
    print('RESID_LUKAS_TEST:')
    print('  Normal end of execution.')
    return


def resid_poiseuille(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # RESID_POISEUILLE returns Poiseuille residualss.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/resid_poiseuille.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinate or coordinates.
    #
    #    Output, real UR(N), VR(N), PR(N), the residuals in the U, V and P equations.
    #
    import numpy as np

    ur = np.zeros(n)
    vr = np.zeros(n)
    pr = np.zeros(n)
#
#  Get the right hand side functions.
#
    f, g, h = rhs_poiseuille(nu, rho, n, x, y, t)
#
#  Form the functions and derivatives for the left hand side.
#
    u = 1.0 - y ** 2
    dudt = 0.0
    dudx = 0.0
    dudxx = 0.0
    dudy = - 2.0 * y
    dudyy = - 2.0

    v = 0.0
    dvdt = 0.0
    dvdx = 0.0
    dvdxx = 0.0
    dvdy = 0.0
    dvdyy = 0.0

    p = - 2.0 * nu * rho * x
    dpdx = - 2.0 * nu * rho
    dpdy = 0.0
#
#  Evaluate the residuals.
#
    ur = dudt - nu * (dudxx + dudyy) \
        + u * dudx + v * dudy + dpdx / rho - f

    vr = dvdt - nu * (dvdxx + dvdyy) \
        + u * dvdx + v * dvdy + dpdy / rho - g

    pr = dudx + dvdy - h

    return ur, vr, pr


def resid_poiseuille_test():

    # *****************************************************************************80
    #
    # RESID_POISEUILLE_TEST samples the Poiseuille residual.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('RESID_POISEUILLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Poiseuille Flow:')
    print('  Sample the Navier-Stokes residuals')
    print('  at the initial time T = 0, over a channel region.')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    x_lo = 0.0
    x_hi = 6.0
    y_lo = -1.0
    y_hi = +1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, y_lo, y_hi, seed)
    t = 0.0

    ur, vr, pr = resid_poiseuille(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  Ur:  %14.6g  %14.6g' % (np.min(np.abs(ur)), np.max(np.abs(ur))))
    print('  Vr:  %14.6g  %14.6g' % (np.min(np.abs(vr)), np.max(np.abs(vr))))
    print('  Pr:  %14.6g  %14.6g' % (np.min(np.abs(pr)), np.max(np.abs(pr))))
#
#  Terminate.
#
    print('')
    print('RESID_POISEUILLE_TEST:')
    print('  Normal end of execution.')
    return


def resid_spiral(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # RESID_SPIRAL returns residuals of the Spiral Flow equations.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/resid_spiral.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Geoffrey Taylor,
    #    On the decay of vortices in a viscous fluid,
    #    Philosophical Magazine,
    #    Volume 46, 1923, pages 671-674.
    #
    #    Geoffrey Taylor, A E Green,
    #    Mechanism for the production of small eddies from large ones,
    #    Proceedings of the Royal Society of London,
    #    Series A, Volume 158, 1937, pages 499-521.
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinate or coordinates.
    #
    #    Output, real UR(N), VR(N), PR(N), the residuals in the U, V and P equations.
    #
    import numpy as np

    ur = np.zeros(n)
    vr = np.zeros(n)
    pr = np.zeros(n)
#
#  Get the right hand side functions.
#
    f, g, h = rhs_spiral(nu, rho, n, x, y, t)
#
#  Form the functions and derivatives for the left hand side.
#
    u = (1.0 + nu * t) * 2.0 \
        * (x ** 4 - 2.0 * x ** 3 + x ** 2) \
        * (2.0 * y ** 3 - 3.0 * y ** 2 + y)

    dudt = nu * 2.0 \
        * (x ** 4 - 2.0 * x ** 3 + x ** 2) \
        * (2.0 * y ** 3 - 3.0 * y ** 2 + y)

    dudx = (1.0 + nu * t) * 2.0 \
        * (4.0 * x ** 3 - 6.0 * x ** 2 + 2.0 * x) \
        * (2.0 * y ** 3 - 3.0 * y ** 2 + y)

    dudxx = (1.0 + nu * t) * 2.0 \
        * (12.0 * x ** 2 - 12.0 * x + 2.0) \
        * (2.0 * y ** 3 - 3.0 * y ** 2 + y)

    dudy = (1.0 + nu * t) * 2.0 \
        * (x ** 4 - 2.0 * x ** 3 + x ** 2) \
        * (6.0 * y ** 2 - 6.0 * y + 1.0)

    dudyy = (1.0 + nu * t) * 2.0 \
        * (x ** 4 - 2.0 * x ** 3 + x ** 2) \
        * (12.0 * y - 6.0)

    v = - (1.0 + nu * t) * 2.0 \
        * (2.0 * x ** 3 - 3.0 * x ** 2 + x) \
        * (y ** 4 - 2.0 * y ** 3 + y ** 2)

    dvdt = - nu * 2.0 \
        * (2.0 * x ** 3 - 3.0 * x ** 2 + x) \
        * (y ** 4 - 2.0 * y ** 3 + y ** 2)

    dvdx = - (1.0 + nu * t) * 2.0 \
        * (6.0 * x ** 2 - 6.0 * x + 1.0) \
        * (y ** 4 - 2.0 * y ** 3 + y ** 2)

    dvdxx = - (1.0 + nu * t) * 2.0 \
        * (12.0 * x - 6.0) \
        * (y ** 4 - 2.0 * y ** 3 + y ** 2)

    dvdy = - (1.0 + nu * t) * 2.0 \
        * (2.0 * x ** 3 - 3.0 * x ** 2 + x) \
        * (4.0 * y ** 3 - 6.0 * y ** 2 + 2.0 * y)

    dvdyy = - (1.0 + nu * t) * 2.0 \
        * (2.0 * x ** 3 - 3.0 * x ** 2 + x) \
        * (12.0 * y ** 2 - 12.0 * y + 2.0)

    p = rho * y
    dpdx = 0.0
    dpdy = rho
#
#  Evaluate the residuals.
#
    ur = dudt - nu * (dudxx + dudyy) \
        + u * dudx + v * dudy + dpdx / rho - f

    vr = dvdt - nu * (dvdxx + dvdyy) \
        + u * dvdx + v * dvdy + dpdy / rho - g

    pr = dudx + dvdy - h

    return ur, vr, pr


def resid_spiral_test():

    # *****************************************************************************80
    #
    # RESID_SPIRAL_TEST samples the residuals at the initial time.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('RESID_SPIRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Spiral Flow:')
    print('  Sample the Navier-Stokes residuals')
    print('  at the initial time T = 0, over the unit square.')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    x_lo = 0.0
    x_hi = 1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    t = 0.0

    ur, vr, pr = resid_spiral(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  Ur:  %14.6g  %14.6g' % (np.min(np.abs(ur)), np.max(np.abs(ur))))
    print('  Vr:  %14.6g  %14.6g' % (np.min(np.abs(vr)), np.max(np.abs(vr))))
    print('  Pr:  %14.6g  %14.6g' % (np.min(np.abs(pr)), np.max(np.abs(pr))))
#
#  Terminate.
#
    print('')
    print('RESID_SPIRAL_TEST:')
    print('  Normal end of execution.')
    return


def resid_taylor(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # RESID_TAYLOR returns Taylor residuals.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/resid_taylor.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Geoffrey Taylor,
    #    On the decay of vortices in a viscous fluid,
    #    Philosophical Magazine,
    #    Volume 46, 1923, pages 671-674.
    #
    #    Geoffrey Taylor, A E Green,
    #    Mechanism for the production of small eddies from large ones,
    #    Proceedings of the Royal Society of London,
    #    Series A, Volume 158, 1937, pages 499-521.
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinate or coordinates.
    #
    #    Output, real UR(N), VR(N), PR(N), the residuals in the U, V and P equations.
    #
    import numpy as np
#
#  Get the right hand sides.
#
    f, g, h = rhs_taylor(nu, rho, n, x, y, t)
#
#  Make space.
#
    c2x = np.array(n)
    c2y = np.array(n)
    cx = np.array(n)
    cy = np.array(n)
    e2t = np.array(n)
    e4t = np.array(n)
    p = np.array(n)
    px = np.array(n)
    py = np.array(n)
    s2x = np.array(n)
    s2y = np.array(n)
    sx = np.array(n)
    sy = np.array(n)
    u = np.array(n)
    ut = np.array(n)
    ux = np.array(n)
    uxx = np.array(n)
    uy = np.array(n)
    uyy = np.array(n)
    v = np.array(n)
    vt = np.array(n)
    vx = np.array(n)
    vxx = np.array(n)
    vy = np.array(n)
    vyy = np.array(n)
#
#  Make some temporaries.
#
    cx = np.cos(np.pi * x)
    cy = np.cos(np.pi * y)

    sx = np.sin(np.pi * x)
    sy = np.sin(np.pi * y)

    e2t = np.exp(- 2.0 * np.pi * np.pi * nu * t)

    c2x = np.cos(2.0 * np.pi * x)
    c2y = np.cos(2.0 * np.pi * y)

    s2x = np.sin(2.0 * np.pi * x)
    s2y = np.sin(2.0 * np.pi * y)

    e4t = np.exp(- 4.0 * np.pi * np.pi * nu * t)
#
#  Form the functions and derivatives.
#
    u = -                            cx * sy * e2t
    dudx = np.pi * sx * sy * e2t
    dudxx = np.pi * np.pi * cx * sy * e2t
    dudy = -                    np.pi * cx * cy * e2t
    dudyy = np.pi * np.pi * cx * sy * e2t
    dudt = + 2.0 * nu * np.pi * np.pi * cx * sy * e2t

    v = sx * cy * e2t
    dvdx = np.pi * cx * cy * e2t
    dvdxx = -            np.pi * np.pi * sx * cy * e2t
    dvdy = -                    np.pi * sx * sy * e2t
    dvdyy = -            np.pi * np.pi * sx * cy * e2t
    dvdt = - 2.0 * nu * np.pi * np.pi * sx * cy * e2t

    p = - 0.25 * rho * (c2x + c2y) * e4t
    dpdx = + 0.5 * rho * np.pi * s2x * e4t
    dpdy = + 0.5 * rho * np.pi * s2y * e4t
#
#  Evaluate the residuals.
#
    ur = dudt + u * dudx + v * dudy + (1.0 / rho) * dpdx \
        - nu * (dudxx + dudyy) - f

    vr = dvdt + u * dvdx + v * dvdy + (1.0 / rho) * dpdy \
        - nu * (dvdxx + dvdyy) - g

    pr = dudx + dvdy - h

    return ur, vr, pr


def resid_taylor_test():

    # *****************************************************************************80
    #
    # RESID_TAYLOR_TEST samples the Taylor residual.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('RESID_TAYLOR_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Sample the Taylor residuals')
    print('  at the initial time T = 0, using a region that is')
    print('  the square centered at (1.5,1.5) with "radius" 1.0,')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    x_lo = 0.5
    x_hi = +2.5
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    t = 0.0

    ur, vr, pr = resid_taylor(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  Ur:  %14.6g  %14.6g' % (np.min(np.abs(ur)), np.max(np.abs(ur))))
    print('  Vr:  %14.6g  %14.6g' % (np.min(np.abs(vr)), np.max(np.abs(vr))))
    print('  Pr:  %14.6g  %14.6g' % (np.min(np.abs(pr)), np.max(np.abs(pr))))
#
#  Terminate.
#
    print('')
    print('RESID_TAYLOR_TEST:')
    print('  Normal end of execution.')
    return


def resid_vortex(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # RESID_VORTEX returns Vortex residuals.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/resid_vortex.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinate or coordinates.
    #
    #    Output, real UR(N), VR(N), PR(N), the residuals in the U, V and P equations.
    #
    import numpy as np
#
#  Get the right hand sides.
#
    f, g, h = rhs_vortex(nu, rho, n, x, y, t)
#
#  Make space.
#
    c2x = np.array(n)
    c2y = np.array(n)
    cx = np.array(n)
    cy = np.array(n)
    e2t = np.array(n)
    e4t = np.array(n)
    p = np.array(n)
    px = np.array(n)
    py = np.array(n)
    s2x = np.array(n)
    s2y = np.array(n)
    sx = np.array(n)
    sy = np.array(n)
    u = np.array(n)
    ut = np.array(n)
    ux = np.array(n)
    uxx = np.array(n)
    uy = np.array(n)
    uyy = np.array(n)
    v = np.array(n)
    vt = np.array(n)
    vx = np.array(n)
    vxx = np.array(n)
    vy = np.array(n)
    vyy = np.array(n)
#
#  Make some temporaries.
#
    cx = np.cos(np.pi * x)
    cy = np.cos(np.pi * y)

    sx = np.sin(np.pi * x)
    sy = np.sin(np.pi * y)

    c2x = np.cos(2.0 * np.pi * x)
    c2y = np.cos(2.0 * np.pi * y)

    s2x = np.sin(2.0 * np.pi * x)
    s2y = np.sin(2.0 * np.pi * y)
#
#  Form the functions and derivatives.
#
    u = -                            cx * sy
    dudx = np.pi * sx * sy
    dudxx = np.pi * np.pi * cx * sy
    dudy = -                    np.pi * cx * cy
    dudyy = np.pi * np.pi * cx * sy
    dudt = np.zeros(n)

    v = sx * cy
    dvdx = np.pi * cx * cy
    dvdxx = -            np.pi * np.pi * sx * cy
    dvdy = -                    np.pi * sx * sy
    dvdyy = -            np.pi * np.pi * sx * cy
    dvdt = np.zeros(n)

    p = - 0.25 * rho * (c2x + c2y)
    dpdx = + 0.5 * rho * np.pi * s2x
    dpdy = + 0.5 * rho * np.pi * s2y
#
#  Evaluate the residuals.
#
    ur = dudt + u * dudx + v * dudy + (1.0 / rho) * dpdx \
        - nu * (dudxx + dudyy) - f

    vr = dvdt + u * dvdx + v * dvdy + (1.0 / rho) * dpdy \
        - nu * (dvdxx + dvdyy) - g

    pr = dudx + dvdy - h

    return ur, vr, pr


def resid_vortex_test():

    # *****************************************************************************80
    #
    # RESID_VORTEX_TEST samples the Vortex residual.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('RESID_VORTEX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Sample the Vortex residuals')
    print('  at the initial time T = 0, using a region that is')
    print('  the square centered at (1.5,1.5) with "radius" 1.0,')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    x_lo = 0.5
    x_hi = +2.5
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    t = 0.0

    ur, vr, pr = resid_vortex(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  Ur:  %14.6g  %14.6g' % (np.min(np.abs(ur)), np.max(np.abs(ur))))
    print('  Vr:  %14.6g  %14.6g' % (np.min(np.abs(vr)), np.max(np.abs(vr))))
    print('  Pr:  %14.6g  %14.6g' % (np.min(np.abs(pr)), np.max(np.abs(pr))))
#
#  Terminate.
#
    print('')
    print('RESID_VORTEX_TEST:')
    print('  Normal end of execution.')
    return


def rhs_lukas(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # RHS_LUKAS returns right hand sides of the Spiral Flow equations.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/rhs_lukas.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinate or coordinates.
    #
    #    Output, real F(N), G(N), H(N), the right hand sides in the U, V and P equations.
    #
    import numpy as np

    f = np.zeros(n)
    g = np.zeros(n)
    h = np.zeros(n)

    u = - np.cos(np.pi * x) / np.pi
    dudt = np.zeros(n)
    dudx = np.sin(np.pi * x)
    dudxx = np.pi * np.cos(np.pi * x)
    dudy = np.zeros(n)
    dudyy = np.zeros(n)

    v = - y * np.sin(np.pi * x)
    dvdt = np.zeros(n)
    dvdx = - np.pi * y * np.cos(np.pi * x)
    dvdxx = + np.pi * np.pi * y * np.sin(np.pi * x)
    dvdy = - np.sin(np.pi * x)
    dvdyy = np.zeros(n)

    p = np.zeros(n)
    dpdx = np.zeros(n)
    dpdy = np.zeros(n)

    f = dudt - nu * (dudxx + dudyy) + u * dudx + v * dudy + dpdx / rho
    g = dvdt - nu * (dvdxx + dvdyy) + u * dvdx + v * dvdy + dpdy / rho
    h = dudx + dvdy

    return f, g, h


def rhs_lukas_test():

    # *****************************************************************************80
    #
    # RHS_LUKAS_TEST samples the right hand sides at the initial time.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('RHS_LUKAS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Lukas Bystricky Flow')
    print('  Sample the Navier-Stokes right hand sides')
    print('  at the initial time T = 0, over the unit square.')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    r8_lo = 0.0
    r8_hi = 1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, r8_lo, r8_hi, seed)
    y, seed = r8vec_uniform_ab(n, r8_lo, r8_hi, seed)
    t = 0.0

    f, g, h = rhs_lukas(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  Ur:  %14.6g  %14.6g' % (np.min(f), np.max(f)))
    print('  Vr:  %14.6g  %14.6g' % (np.min(g), np.max(g)))
    print('  Pr:  %14.6g  %14.6g' % (np.min(h), np.max(h)))
#
#  Terminate.
#
    print('')
    print('RHS_LUKAS_TEST:')
    print('  Normal end of execution.')
    return


def rhs_poiseuille(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # RHS_POISEUILLE returns the Poiseuille right hand side.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/rhs_poiseuille.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinate or coordinates.
    #
    #    Output, real F(N), G(N), H(N), the right hand sides in the
    #    U, V and P equations.
    #
    import numpy as np

    f = np.zeros(n)
    g = np.zeros(n)
    h = np.zeros(n)

    return f, g, h


def rhs_poiseuille_test():

    # *****************************************************************************80
    #
    # RHS_POISEUILLE_TEST samples the Poiseuille right hand side.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('RHS_POISEUILLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Poiseuille Flow:')
    print('  Sample the Navier-Stokes right hand sides')
    print('  at the initial time T = 0, over a channel region.')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    x_lo = 0.0
    x_hi = 6.0
    y_lo = -1.0
    y_hi = +1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, y_lo, y_hi, seed)
    t = 0.0

    f, g, h = rhs_poiseuille(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  Ur:  %14.6g  %14.6g' % (np.min(f), np.max(f)))
    print('  Vr:  %14.6g  %14.6g' % (np.min(g), np.max(g)))
    print('  Pr:  %14.6g  %14.6g' % (np.min(h), np.max(h)))
#
#  Terminate.
#
    print('')
    print('RHS_POISEUILLE_TEST:')
    print('  Normal end of execution.')
    return


def rhs_spiral(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # RHS_SPIRAL returns right hand sides of the Spiral Flow equations.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/rhs_spiral.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Geoffrey Taylor,
    #    On the decay of vortices in a viscous fluid,
    #    Philosophical Magazine,
    #    Volume 46, 1923, pages 671-674.
    #
    #    Geoffrey Taylor, A E Green,
    #    Mechanism for the production of small eddies from large ones,
    #    Proceedings of the Royal Society of London,
    #    Series A, Volume 158, 1937, pages 499-521.
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinate or coordinates.
    #
    #    Output, real F(N), G(N), H(N), the right hand sides in the U, V and P equations.
    #
    import numpy as np

    f = np.zeros(n)
    g = np.zeros(n)
    h = np.zeros(n)

    u = (1.0 + nu * t) * 2.0 \
        * (x ** 4 - 2.0 * x ** 3 + x ** 2) \
        * (2.0 * y ** 3 - 3.0 * y ** 2 + y)

    dudt = nu * 2.0 \
        * (x ** 4 - 2.0 * x ** 3 + x ** 2) \
        * (2.0 * y ** 3 - 3.0 * y ** 2 + y)

    dudx = (1.0 + nu * t) * 2.0 \
        * (4.0 * x ** 3 - 6.0 * x ** 2 + 2.0 * x) \
        * (2.0 * y ** 3 - 3.0 * y ** 2 + y)

    dudxx = (1.0 + nu * t) * 2.0 \
        * (12.0 * x ** 2 - 12.0 * x + 2.0) \
        * (2.0 * y ** 3 - 3.0 * y ** 2 + y)

    dudy = (1.0 + nu * t) * 2.0 \
        * (x ** 4 - 2.0 * x ** 3 + x ** 2) \
        * (6.0 * y ** 2 - 6.0 * y + 1.0)

    dudyy = (1.0 + nu * t) * 2.0 \
        * (x ** 4 - 2.0 * x ** 3 + x ** 2) \
        * (12.0 * y - 6.0)

    v = - (1.0 + nu * t) * 2.0 \
        * (2.0 * x ** 3 - 3.0 * x ** 2 + x) \
        * (y ** 4 - 2.0 * y ** 3 + y ** 2)

    dvdt = - nu * 2.0 \
        * (2.0 * x ** 3 - 3.0 * x ** 2 + x) \
        * (y ** 4 - 2.0 * y ** 3 + y ** 2)

    dvdx = - (1.0 + nu * t) * 2.0 \
        * (6.0 * x ** 2 - 6.0 * x + 1.0) \
        * (y ** 4 - 2.0 * y ** 3 + y ** 2)

    dvdxx = - (1.0 + nu * t) * 2.0 \
        * (12.0 * x - 6.0) \
        * (y ** 4 - 2.0 * y ** 3 + y ** 2)

    dvdy = - (1.0 + nu * t) * 2.0 \
        * (2.0 * x ** 3 - 3.0 * x ** 2 + x) \
        * (4.0 * y ** 3 - 6.0 * y ** 2 + 2.0 * y)

    dvdyy = - (1.0 + nu * t) * 2.0 \
        * (2.0 * x ** 3 - 3.0 * x ** 2 + x) \
        * (12.0 * y ** 2 - 12.0 * y + 2.0)

    p = rho * y
    dpdx = 0.0
    dpdy = rho

    f = dudt - nu * (dudxx + dudyy) \
        + u * dudx + v * dudy + dpdx / rho

    g = dvdt - nu * (dvdxx + dvdyy) \
        + u * dvdx + v * dvdy + dpdy / rho

    h = dudx + dvdy

    return f, g, h


def rhs_spiral_test():

    # *****************************************************************************80
    #
    # RHS_SPIRAL_TEST samples the right hand sides at the initial time.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('RHS_SPIRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Spiral Flow:')
    print('  Sample the Navier-Stokes right hand sides')
    print('  at the initial time T = 0, over the unit square.')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    x_lo = 0.0
    x_hi = 1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    t = 0.0

    f, g, h = rhs_spiral(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  Ur:  %14.6g  %14.6g' % (np.min(f), np.max(f)))
    print('  Vr:  %14.6g  %14.6g' % (np.min(g), np.max(g)))
    print('  Pr:  %14.6g  %14.6g' % (np.min(h), np.max(h)))
#
#  Terminate.
#
    print('')
    print('RHS_SPIRAL_TEST:')
    print('  Normal end of execution.')
    return


def rhs_taylor(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # RHS_TAYLOR returns the Taylor right hand side.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/rhs_taylor.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Geoffrey Taylor,
    #    On the decay of vortices in a viscous fluid,
    #    Philosophical Magazine,
    #    Volume 46, 1923, pages 671-674.
    #
    #    Geoffrey Taylor, A E Green,
    #    Mechanism for the production of small eddies from large ones,
    #    Proceedings of the Royal Society of London,
    #    Series A, Volume 158, 1937, pages 499-521.
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinate or coordinates.
    #
    #    Output, real F(N), G(N), H(N), the residuals in the U, V and P equations.
    #
    import numpy as np

    f = np.zeros(n)
    g = np.zeros(n)
    h = np.zeros(n)

    return f, g, h


def rhs_taylor_test():

    # *****************************************************************************80
    #
    # RHS_TAYLOR_TEST samples the Taylor ight hand side.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('RHS_TAYLOR_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Taylor Flow:')
    print('  Sample the Navier-Stokes right hand sides')
    print('  at the initial time T = 0, using a region that is')
    print('  the square centered at (1.5,1.5) with "radius" 1.0,')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    x_lo = 0.5
    x_hi = +2.5
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    t = 0.0

    f, g, h = rhs_taylor(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  Ur:  %14.6g  %14.6g' % (np.min(f), np.max(f)))
    print('  Vr:  %14.6g  %14.6g' % (np.min(g), np.max(g)))
    print('  Pr:  %14.6g  %14.6g' % (np.min(h), np.max(h)))
#
#  Terminate.
#
    print('')
    print('RHS_TAYLOR_TEST:')
    print('  Normal end of execution.')
    return


def rhs_vortex(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # RHS_VORTEX returns the Vortex right hand side.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/rhs_vortex.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinate or coordinates.
    #
    #    Output, real F(N), G(N), H(N), the residuals in the U, V and P equations.
    #
    import numpy as np

    f = - 2.0 * nu * (np.pi) ** 2 * (np.cos(np.pi * x) * np.sin(np.pi * y))
    g = 2.0 * nu * (np.pi) ** 2 * (np.sin(np.pi * x) * np.cos(np.pi * y))
    h = np.zeros(n)

    return f, g, h


def rhs_vortex_test():

    # *****************************************************************************80
    #
    # RHS_VORTEX_TEST samples the Vortex right hand side.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('RHS_VORTEX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Sample the Vortex right hand sides')
    print('  at the initial time T = 0, using a region that is')
    print('  the square centered at (1.5,1.5) with "radius" 1.0,')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    x_lo = 0.5
    x_hi = +2.5
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    t = 0.0

    f, g, h = rhs_vortex(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  Ur:  %14.6g  %14.6g' % (np.min(f), np.max(f)))
    print('  Vr:  %14.6g  %14.6g' % (np.min(g), np.max(g)))
    print('  Pr:  %14.6g  %14.6g' % (np.min(h), np.max(h)))
#
#  Terminate.
#
    print('')
    print('RHS_VORTEX_TEST:')
    print('  Normal end of execution.')
    return


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


def uvp_lukas(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # UVP_LUKAS evaluates Lukas Bystricky's exact Navier Stokes solution.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/uvp_lukas.py
    #
    #  Discussion:
    #
    #    There is no time dependence.
    #
    #    The pressure is 0.
    #
    #    The preferred domain is the unit square.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T or T(N), the time coordinate or coordinates.
    #
    #    Output, real U(N), V(N), P(N), the velocity components and
    #    pressure at each of the points.
    #
    import numpy as np

    u = np.zeros(n)
    v = np.zeros(n)
    p = np.zeros(n)

    u = - np.cos(np.pi * x) / np.pi

    v = - y * np.sin(np.pi * x)

    return u, v, p


def uvp_lukas_test():

    # *****************************************************************************80
    #
    # UVP_LUKAS_TEST samples the Lukas Bystricky solution at the initial time.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('UVP_LUKAS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Lukas Bystricky Flow:')
    print('  Estimate the range of velocity and pressure')
    print('  at the initial time T = 0, over the unit square.')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    r8_lo = 0.0
    r8_hi = +1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, r8_lo, r8_hi, seed)
    y, seed = r8vec_uniform_ab(n, r8_lo, r8_hi, seed)
    t = 0.0

    u, v, p = uvp_lukas(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  U:  %14.6g  %14.6g' % (np.min(u), np.max(u)))
    print('  V:  %14.6g  %14.6g' % (np.min(v), np.max(v)))
    print('  P:  %14.6g  %14.6g' % (np.min(p), np.max(p)))
#
#  Terminate.
#
    print('')
    print('UVP_LUKAS_TEST:')
    print('  Normal end of execution.')
    return


def uvp_lukas_test2():

    # *****************************************************************************80
    #
    # UVP_LUKAS_TEST2 samples the Lukas Bystricky flow on the boundary.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    r8_lo = 0.0
    r8_hi = +1.0

    nu = 1.0
    rho = 1.0
    t = 0.0

    print('')
    print('UVP_LUKAS_TEST2')
    print('  Python version: %s' % (platform.python_version()))
    print('  Lukas Bystricky Flow:')
    print('  Estimate the range of velocity and pressure')
    print('  on the boundary')
    print('  at the initial time T = 0, over the unit square.')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 400

    x = np.zeros(n)
    y = np.zeros(n)

    x[0:100] = np.linspace(r8_lo, r8_hi, 100)
    y[0:100] = r8_lo

    x[100:200] = r8_hi
    y[100:200] = np.linspace(r8_lo, r8_hi, 100)

    x[200:300] = np.linspace(r8_hi, r8_lo, 100)
    y[200:300] = r8_hi

    x[300:400] = r8_lo
    y[300:400] = np.linspace(r8_lo, r8_hi, 100)

    u, v, p = uvp_lukas(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  U:  %14.6g  %14.6g' % (np.min(u), np.max(u)))
    print('  V:  %14.6g  %14.6g' % (np.min(v), np.max(v)))
    print('  P:  %14.6g  %14.6g' % (np.min(p), np.max(p)))
#
#  Terminate.
#
    print('')
    print('UVP_LUKAS_TEST2:')
    print('  Normal end of execution.')
    return


def uvp_poiseuille(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # UVP_POISEUILLE evaluates the Poiseuille solution.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/uvp_poiseuille.py
    #
    #  Discussion:
    #
    #    This flow is known as a Poiseuille Flow solution.
    #
    #    The given velocity and pressure fields are exact solutions for the 2D
    #    incompressible time-dependent Navier Stokes equations over the unit square.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T or T(N), the time coordinate or coordinates.
    #
    #    Output, real U(N), V(N), P(N), the velocity components and
    #    pressure at each of the points.
    #
    import numpy as np

    u = np.zeros(n)
    v = np.zeros(n)
    p = np.zeros(n)

    u = 1.0 - y ** 2
#
#  Can't write it this way or V becomes a scalar!
#
# v = 0.0;

    p = -2.0 * rho * nu * x

    return u, v, p


def uvp_poiseuille_test():

    # *****************************************************************************80
    #
    # UVP_POISEUILLE_TEST samples the Poiseuille solution.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('UVP_POISEUILLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Poiseuille Flow:')
    print('  Estimate the range of velocity and pressure')
    print('  at the initial time T = 0, over a channel region.')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    x_lo = +0.0
    x_hi = +6.0
    y_lo = -1.0
    y_hi = + 1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, y_lo, y_hi, seed)
    t = 0.0

    u, v, p = uvp_poiseuille(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  U:  %14.6g  %14.6g' % (np.min(u), np.max(u)))
    print('  V:  %14.6g  %14.6g' % (np.min(v), np.max(v)))
    print('  P:  %14.6g  %14.6g' % (np.min(p), np.max(p)))
#
#  Terminate.
#
    print('')
    print('UVP_POISEUILLE_TEST:')
    print('  Normal end of execution.')
    return


def uvp_poiseuille_test2():

    # *****************************************************************************80
    #
    # UVP_POISEUILLE_TEST2 samples the Poiseuille solution on the boundary.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    x_lo = +0.0
    x_hi = +6.0
    y_lo = -1.0
    y_hi = + 1.0

    nu = 1.0
    rho = 1.0
    t = 0.0

    print('')
    print('UVP_POISEUILLE_TEST2')
    print('  Python version: %s' % (platform.python_version()))
    print('  Poiseuille Flow:')
    print('  Estimate the range of velocity and pressure')
    print('  on the boundary')
    print('  at the initial time T = 0, over a channel region.')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 400

    x = np.zeros(n)
    y = np.zeros(n)

    x[0:100] = np.linspace(x_lo, x_hi, 100)
    y[0:100] = y_lo

    x[100:200] = x_hi
    y[100:200] = np.linspace(y_lo, y_hi, 100)

    x[200:300] = np.linspace(x_hi, x_lo, 100)
    y[200:300] = y_hi

    x[300:400] = x_lo
    y[300:400] = np.linspace(y_hi, y_lo, 100)

    u, v, p = uvp_poiseuille(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  U:  %14.6g  %14.6g' % (np.min(u), np.max(u)))
    print('  V:  %14.6g  %14.6g' % (np.min(v), np.max(v)))
    print('  P:  %14.6g  %14.6g' % (np.min(p), np.max(p)))
#
#  Terminate.
#
    print('')
    print('UVP_POISEUILLE_TEST2:')
    print('  Normal end of execution.')
    return


def uvp_spiral(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # UVP_SPIRAL evaluates the Spiral Flow exact Navier Stokes solution.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/uvp_spiral.py
    #
    #  Discussion:
    #
    #    This flow is known as a Spiral Flow solution.
    #
    #    The given velocity and pressure fields are exact solutions for the 2D
    #    incompressible time-dependent Navier Stokes equations over the unit square.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Maxim Olshanskii, Leo Rebholz,
    #    Application of barycenter refined meshes in linear elasticity
    #    and incompressible fluid dynamics,
    #    ETNA: Electronic Transactions in Numerical Analysis,
    #    Volume 38, pages 258-274, 2011.
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T or T(N), the time coordinate or coordinates.
    #
    #    Output, real U(N), V(N), P(N), the velocity components and
    #    pressure at each of the points.
    #
    import numpy as np

    u = np.zeros(n)
    v = np.zeros(n)
    p = np.zeros(n)

    u = (1.0 + nu * t) * 2.0 \
        * x ** 2 * (x - 1.0) ** 2 \
        * y * (2.0 * y - 1.0) * (y - 1.0)

    v = - (1.0 + nu * t) * 2.0 \
        * x * (2.0 * x - 1.0) * (x - 1.0) \
        * y ** 2 * (y - 1.0) ** 2

    p = rho * y

    return u, v, p


def uvp_spiral_test():

    # *****************************************************************************80
    #
    # UVP_SPIRAL_TEST samples the Spiral Flow solution at the initial time.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('UVP_SPIRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Spiral Flow:')
    print('  Estimate the range of velocity and pressure')
    print('  at the initial time T = 0, over the unit square.')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    x_lo = 0.0
    x_hi = +1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    t = 0.0

    u, v, p = uvp_spiral(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  U:  %14.6g  %14.6g' % (np.min(u), np.max(u)))
    print('  V:  %14.6g  %14.6g' % (np.min(v), np.max(v)))
    print('  P:  %14.6g  %14.6g' % (np.min(p), np.max(p)))
#
#  Terminate.
#
    print('')
    print('UVP_SPIRAL_TEST:')
    print('  Normal end of execution.')
    return


def uvp_spiral_test2():

    # *****************************************************************************80
    #
    # UVP_SPIRAL_TEST2 samples the Spiral Flow on the boundary at the initial time.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    r8_lo = 0.0
    r8_hi = +1.0

    nu = 1.0
    rho = 1.0
    t = 0.0

    print('')
    print('UVP_SPIRAL_TEST2')
    print('  Python version: %s' % (platform.python_version()))
    print('  Spiral Flow:')
    print('  Estimate the range of velocity and pressure')
    print('  on the boundary')
    print('  at the initial time T = 0, over the unit square.')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 400

    x = np.zeros(n)
    y = np.zeros(n)

    x[0:100] = np.linspace(r8_lo, r8_hi, 100)
    y[0:100] = r8_lo

    x[100:200] = r8_hi
    y[100:200] = np.linspace(r8_lo, r8_hi, 100)

    x[200:300] = np.linspace(r8_hi, r8_lo, 100)
    y[200:300] = r8_hi

    x[300:400] = r8_lo
    y[300:400] = np.linspace(r8_lo, r8_hi, 100)

    u, v, p = uvp_spiral(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  U:  %14.6g  %14.6g' % (np.min(u), np.max(u)))
    print('  V:  %14.6g  %14.6g' % (np.min(v), np.max(v)))
    print('  P:  %14.6g  %14.6g' % (np.min(p), np.max(p)))
#
#  Terminate.
#
    print('')
    print('UVP_SPIRAL_TEST2:')
    print('  Normal end of execution.')
    return


def uvp_taylor(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # UVP_TAYLOR evaluates the Taylor exact Navier Stokes solution.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/uvp_taylor.py
    #
    #  Discussion:
    #
    #    This flow is known as a Taylor-Green vortex.
    #
    #    The given velocity and pressure fields are exact solutions for the 2D
    #    incompressible time-dependent Navier Stokes equations over any region.
    #
    #    To define a typical problem, one chooses a bounded spatial region
    #    and a starting time, and then imposes boundary and initial conditions
    #    by referencing the exact solution appropriately.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Geoffrey Taylor,
    #    On the decay of vortices in a viscous fluid,
    #    Philosophical Magazine,
    #    Volume 46, 1923, pages 671-674.
    #
    #    Geoffrey Taylor, A E Green,
    #    Mechanism for the production of small eddies from large ones,
    #    Proceedings of the Royal Society of London,
    #    Series A, Volume 158, 1937, pages 499-521.
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T or T(N), the time coordinate or coordinates.
    #
    #    Output, real U(N), V(N), P(N), the velocity components and
    #    pressure at each of the points.
    #
    import numpy as np

    cx = np.cos(np.pi * x)
    cy = np.cos(np.pi * y)
    c2x = np.cos(2.0 * np.pi * x)
    c2y = np.cos(2.0 * np.pi * y)
    sx = np.sin(np.pi * x)
    sy = np.sin(np.pi * y)
    e2t = np.exp(- 2.0 * np.pi * np.pi * nu * t)
    e4t = np.exp(- 4.0 * np.pi * np.pi * nu * t)

    u = np.zeros(n)
    v = np.zeros(n)
    p = np.zeros(n)

    u = - cx * sy * e2t
    v = sx * cy * e2t
    p = - 0.25 * rho * (c2x + c2y) * e4t

    return u, v, p


def uvp_taylor_test():

    # *****************************************************************************80
    #
    # UVP_TAYLOR_TEST samples the solution at the initial time.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('UVP_TAYLOR_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Estimate the range of velocity and pressure')
    print('  at the initial time T = 0, using a region that is')
    print('  the square centered at (1.5,1.5) with "radius" 1.0,')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    x_lo = 0.5
    x_hi = +2.5
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    t = 0.0

    u, v, p = uvp_taylor(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  U:  %14.6g  %14.6g' % (np.min(u), np.max(u)))
    print('  V:  %14.6g  %14.6g' % (np.min(v), np.max(v)))
    print('  P:  %14.6g  %14.6g' % (np.min(p), np.max(p)))
#
#  Terminate.
#
    print('')
    print('UVP_TAYLOR_TEST:')
    print('  Normal end of execution.')
    return


def uvp_taylor_test2():

    # *****************************************************************************80
    #
    # UVP_TAYLOR_TEST2 samples the solution on the boundary at the initial time.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    r8_lo = 0.5
    r8_hi = +2.5

    nu = 1.0
    rho = 1.0
    t = 0.0

    print('')
    print('UVP_TAYLOR_TEST2')
    print('  Python version: %s' % (platform.python_version()))
    print('  Estimate the range of velocity and pressure')
    print('  on the boundary')
    print('  at the initial time T = 0, using a region that is')
    print('  the square centered at (1.5,1.5) with "radius" 1.0,')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 400

    x = np.zeros(n)
    y = np.zeros(n)
#
#  Python is consistent in its willful flouting of sensible conventions.
#  X[0:100] means X from 0 to 99...!
#
    x[0:100] = np.linspace(r8_lo, r8_hi, 100)
    y[0:100] = r8_lo

    x[100:200] = r8_hi
    y[100:200] = np.linspace(r8_lo, r8_hi, 100)

    x[200:300] = np.linspace(r8_hi, r8_lo, 100)
    y[200:300] = r8_hi

    x[300:400] = r8_lo
    y[300:400] = np.linspace(r8_lo, r8_hi, 100)

    u, v, p = uvp_taylor(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  U:  %14.6g  %14.6g' % (np.min(u), np.max(u)))
    print('  V:  %14.6g  %14.6g' % (np.min(v), np.max(v)))
    print('  P:  %14.6g  %14.6g' % (np.min(p), np.max(p)))
#
#  Terminate.
#
    print('')
    print('UVP_TAYLOR_TEST2:')
    print('  Normal end of execution.')
    return


def uvp_vortex(nu, rho, n, x, y, t):

    # *****************************************************************************80
    #
    # UVP_VORTEX evaluates the Vortex solution.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/uvp_vortex.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, real RHO, the density.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), the coordinates of the points.
    #
    #    Input, real T or T(N), the time coordinate or coordinates.
    #
    #    Output, real U(N), V(N), P(N), the velocity components and
    #    pressure at each of the points.
    #
    import numpy as np

    cx = np.cos(np.pi * x)
    cy = np.cos(np.pi * y)
    c2x = np.cos(2.0 * np.pi * x)
    c2y = np.cos(2.0 * np.pi * y)
    sx = np.sin(np.pi * x)
    sy = np.sin(np.pi * y)

    u = np.zeros(n)
    v = np.zeros(n)
    p = np.zeros(n)

    u = - cx * sy
    v = sx * cy
    p = - 0.25 * rho * (c2x + c2y)

    return u, v, p


def uvp_vortex_test():

    # *****************************************************************************80
    #
    # UVP_TAYLOR_TEST samples the Vortex solution at the initial time.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    nu = 1.0
    rho = 1.0

    print('')
    print('UVP_VORTEX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Sample the Vortex solution.')
    print('  Estimate the range of velocity and pressure')
    print('  at the initial time T = 0, using a region that is')
    print('  the square centered at (1.5,1.5) with "radius" 1.0,')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 1000
    x_lo = 0.5
    x_hi = +2.5
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    t = 0.0

    u, v, p = uvp_vortex(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  U:  %14.6g  %14.6g' % (np.min(u), np.max(u)))
    print('  V:  %14.6g  %14.6g' % (np.min(v), np.max(v)))
    print('  P:  %14.6g  %14.6g' % (np.min(p), np.max(p)))
#
#  Terminate.
#
    print('')
    print('UVP_VORTEX_TEST:')
    print('  Normal end of execution.')
    return


def uvp_vortex_test2():

    # *****************************************************************************80
    #
    # UVP_VORTEX_TEST2 samples the Vortex solution on the boundary.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    r8_lo = 0.5
    r8_hi = +2.5

    nu = 1.0
    rho = 1.0
    t = 0.0

    print('')
    print('UVP_VORTEX_TEST2')
    print('  Python version: %s' % (platform.python_version()))
    print('  Sample the Vortex solution.')
    print('  Estimate the range of velocity and pressure')
    print('  on the boundary')
    print('  at the initial time T = 0, using a region that is')
    print('  the square centered at (1.5,1.5) with "radius" 1.0,')
    print('  Kinematic viscosity NU = %g' % (nu))
    print('  Fluid density RHO = %g' % (rho))

    n = 400

    x = np.zeros(n)
    y = np.zeros(n)
#
#  Python is consistent in its willful flouting of sensible conventions.
#  X[0:100] means X from 0 to 99...!
#
    x[0:100] = np.linspace(r8_lo, r8_hi, 100)
    y[0:100] = r8_lo

    x[100:200] = r8_hi
    y[100:200] = np.linspace(r8_lo, r8_hi, 100)

    x[200:300] = np.linspace(r8_hi, r8_lo, 100)
    y[200:300] = r8_hi

    x[300:400] = r8_lo
    y[300:400] = np.linspace(r8_lo, r8_hi, 100)

    u, v, p = uvp_vortex(nu, rho, n, x, y, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  U:  %14.6g  %14.6g' % (np.min(u), np.max(u)))
    print('  V:  %14.6g  %14.6g' % (np.min(v), np.max(v)))
    print('  P:  %14.6g  %14.6g' % (np.min(p), np.max(p)))
#
#  Terminate.
#
    print('')
    print('UVP_VORTEX_TEST2:')
    print('  Normal end of execution.')
    return


def ns2de_test():

    # *****************************************************************************80
    #
    # NS2DE_TEST tests the NS2DE library.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/ns2de_test.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NS2DE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the NS2DE library.')

    grid_2d_test()
#
#  Lukas Bystricky
#
    uvp_lukas_test()
    uvp_lukas_test2()
    rhs_lukas_test()
    resid_lukas_test()
    ns2de_gnuplot_lukas_test()
    ns2de_matplotlib_lukas_test()
#
#  Poiseuille
#
    uvp_poiseuille_test()
    uvp_poiseuille_test2()
    rhs_poiseuille_test()
    resid_poiseuille_test()
    ns2de_gnuplot_poiseuille_test()
    ns2de_matplotlib_poiseuille_test()
    parameter_poiseuille_test()
#
#  Spiral
#
    uvp_spiral_test()
    uvp_spiral_test2()
    rhs_spiral_test()
    resid_spiral_test()
    ns2de_gnuplot_spiral_test()
    ns2de_matplotlib_spiral_test()
    parameter_spiral_test()
#
#  Taylor Vortex
#
    uvp_taylor_test()
    uvp_taylor_test2()
    rhs_taylor_test()
    resid_taylor_test()
    ns2de_gnuplot_taylor_test()
    ns2de_matplotlib_taylor_test()
    parameter_taylor_test()

    print('')
    print('NS2DE_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    ns2de_test()
    timestamp()
