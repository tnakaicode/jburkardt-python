#! /usr/bin/env python3
#


def boundary(nx, ny, x, y, A, rhs):

    # *****************************************************************************80
    #
    # BOUNDARY sets up the matrix and right hand side at boundary nodes.
    #
    #  Discussion:
    #
    #    For this simple problem, the boundary conditions specify that the solution
    #    is 10 on the left size, 100 on the right side, and 0 on the top and bottom.
    #
    #    Nodes are assigned a single index K, which increases as:
    #
    #    (NY-1)*NX+1  (NY-1)*NX+2  ...  NY * NX
    #           ....         ....  ...    .....
    #           NX+1         NX+2  ...   2 * NX
    #              1            2  ...       NX
    #
    #    The index K of a node on the lower boundary satisfies:
    #      1 <= K <= NX
    #    The index K of a node on the upper boundary satisfies:
    #      (NY-1)*NX+1 <= K <= NY * NX
    #    The index K of a node on the left boundary satisfies:
    #      mod ( K, NX ) = 1
    #    The index K of a node on the right boundary satisfies:
    #      mod ( K, NX ) = 0
    #
    #    If we number rows from bottom I = 1 to top I = NY
    #    and columns from left J = 1 to right J = NX, then the relationship
    #    between the single index K and the row and column indices I and J is:
    #      K = ( I - 1 ) * NX + J
    #    and
    #      J = 1 + mod ( K - 1, NX )
    #      I = 1 + ( K - J ) / NX
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 March 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer NX, NY, the number of grid points in X and Y.
    #
    #    Input, real X(NX), Y(NY), the coordinates of grid lines.
    #
    #    Input, real sparse A(N,N), the system matrix, with the entries for the
    #    interior nodes filled in.
    #
    #    Input, real RHS(N), the system right hand side, with the entries for the
    #    interior nodes filled in.
    #
    #    Output, real sparse A(N,N), the system matrix, with the entries for all
    #    nodes filled in.
    #
    #    Output, real RHS(N), the system right hand side, with the entries for
    #    all nodes filled in.
    #

    #
    #  Left boundary.
    #
    j = 0
    for i in range(0, ny):
        kc = i * nx + j
        xc = x[j]
        yc = y[i]
        A[kc, kc] = 1.0
        rhs[kc] = 10.0
#
#  Right boundary.
#
    j = nx - 1
    for i in range(0, ny):
        kc = i * nx + j
        xc = x[j]
        yc = y[i]
        A[kc, kc] = 1.0
        rhs[kc] = 100.0
#
#  Lower boundary.
#
    i = 0
    for j in range(0, nx):
        kc = i * nx + j
        xc = x[j]
        yc = y[i]
        A[kc, kc] = 1.0
        rhs[kc] = 0.0
#
#  Upper boundary.
#
    i = ny - 1
    for j in range(0, nx):
        kc = i * nx + j
        xc = x[j]
        yc = y[i]
        A[kc, kc] = 1.0
        rhs[kc] = 0.0

    return A, rhs


def fd2d_heat_steady(nx, ny, x, y, d, f):

    # *****************************************************************************80
    #
    # FD2D_HEAT_STEADY solves the steady 2D heat equation.
    #
    #  Discussion:
    #
    #    Nodes are assigned a singled index K, which increases as:
    #
    #    (NY-1)*NX+1  (NY-1)*NX+2  ...  NY * NX
    #           ....         ....  ...    .....
    #           NX+1         NX+2  ...   2 * NX
    #              1            2  ...       NX
    #
    #    Therefore, the neighbors of an interior node numbered C are
    #
    #             C+NY
    #              |
    #      C-1 --- C --- C+1
    #              |
    #             C-NY
    #
    #    Nodes on the lower boundary satisfy:
    #      1 <= K <= NX
    #    Nodes on the upper boundary satisfy:
    #      (NY-1)*NX+1 <= K <= NY * NX
    #    Nodes on the left boundary satisfy:
    #      mod ( K, NX ) = 1
    #    Nodes on the right boundary satisfy:
    #      mod ( K, NX ) = 0
    #
    #    If we number rows from bottom I = 1 to top I = NY
    #    and columns from left J = 1 to right J = NX, we have
    #      K = ( I - 1 ) * NX + J
    #    and
    #      J = 1 + mod ( K - 1, NX )
    #      I = 1 + ( K - J ) / NX
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 March 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer NX, NY, the number of grid points in X and Y.
    #
    #    Input, real X(NX), Y(NY), the coordinates of grid lines.
    #
    #    Input, function D(X,Y), evaluates the thermal conductivity.
    #
    #    Input, function F(X,Y), evaluates the heat source term.
    #
    #    Output, real U(NX,NY), the approximation to the solution at the grid points.
    #
    import numpy as np
#
#  Set the total number of unknowns.
#
    n = nx * ny
#
#  Allocate the matrix and right hand side.
#
    A = np.zeros([n, n])
    rhs = np.zeros(n)
#
#  Define the matrix at interior points.
#
    A, rhs = interior(nx, ny, x, y, d, f, A, rhs)
#
#  Handle boundary conditions.
#
    A, rhs = boundary(nx, ny, x, y, A, rhs)

# for i in range ( 0, 5 ):
#   for j in range ( 0, nx ):
#     kc = i * nx + j
#     xc = x[j]
#     yc = y[i]
#     print ( '  %d  %d  %d  %f  %f  %g  %g' % ( i, j, kc, xc, yc, A[kc,kc], rhs[kc] ) )
#
#  Solve the linear system.
#
    u = np.linalg.solve(A, rhs)

    u.shape = (ny, nx)

    return u


def fd2d_heat_steady_test01():

    # *****************************************************************************80
    #
    # FD2D_HEAT_STEADY_TEST01 demonstrates the use of FD2D_HEAT_STEADY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 March 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    from matplotlib import cm
#
#  Specify the spatial grid.
#
    nx = 21
    ny = 11
    xvec = np.linspace(0.0, 2.0, nx)
    yvec = np.linspace(0.0, 1.0, ny)
#
#  Solve the finite difference approximation to the steady 2D heat equation.
#
    umat = fd2d_heat_steady(nx, ny, xvec, yvec, d, f)
#
#  Plotting.
#
    xmat, ymat = np.meshgrid(xvec, yvec)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(xmat, ymat, umat, cmap=cm.coolwarm,
                    linewidth=0, antialiased=False)
    ax.set_xlabel('<--- Y --->')
    ax.set_ylabel('<--- X --->')
    ax.set_zlabel('<---U(X,Y)--->')
    ax.set_title('Solution of steady heat equation')
    plt.draw()
    plt.show(block=False)
    filename = 'fd2d_heat_steady_test01.png'
    fig.savefig(filename)

    print('')
    print('  Plotfile saved as "%s".' % (filename))

    return


def d(x, y):

    # *****************************************************************************80
    #
    # D evaluates the heat conductivity coefficient.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 July 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, Y, the evaluation point.
    #
    #    Output, real VALUE, the value of the heat conductivity at (X,Y).
    #
    value = 1.0

    return value


def f(x, y):

    # *****************************************************************************80
    #
    # F evaluates the heat source term.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 July 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, Y, the evaluation point.
    #
    #    Output, real VALUE, the value of the heat source term at (X,Y).
    #
    value = 0.0

    return value


def interior(nx, ny, x, y, d, f, A, rhs):

    # *****************************************************************************80
    #
    # INTERIOR sets up the matrix and right hand side at interior nodes.
    #
    #  Discussion:
    #
    #    Nodes are assigned a single index K, which increases as:
    #
    #    (NY-1)*NX+1  (NY-1)*NX+2  ...  NY * NX
    #           ....         ....  ...    .....
    #           NX+1         NX+2  ...   2 * NX
    #              1            2  ...       NX
    #
    #    Therefore, the neighbors of an interior node numbered C are
    #
    #             C+NY
    #              |
    #      C-1 --- C --- C+1
    #              |
    #             C-NY
    #
    #    If we number rows from bottom I = 1 to top I = NY
    #    and columns from left J = 1 to right J = NX, then the relationship
    #    between the single index K and the row and column indices I and J is:
    #      K = ( I - 1 ) * NX + J
    #    and
    #      J = 1 + mod ( K - 1, NX )
    #      I = 1 + ( K - J ) / NX
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 March 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer NX, NY, the number of grid points in X and Y.
    #
    #    Input, real X(NX), Y(NY), the coordinates of grid lines.
    #
    #    Input, function pointer @D(X,Y), evaluates the thermal conductivity.
    #
    #    Input, function pointer @F(X,Y), evaluates the heat source term.
    #
    #    Input, real sparse A(N,N), the system matrix, without any entries set.
    #
    #    Input, real RHS(N), the system right hand side, without any entries set.
    #
    #    Output, real sparse A(N,N), the system matrix, with the entries for the
    #    interior nodes filled in.
    #
    #    Output, real RHS(N), the system right hand side, with the entries for the
    #    interior nodes filled in.
    #
    import numpy as np
#
#  For now, assume X and Y are equally spaced.
#
    dx = x[1] - x[0]
    dy = y[1] - y[0]

    for ic in range(1, ny - 1):
        for jc in range(1, nx - 1):

            ino = ic + 1
            iso = ic - 1
            je = jc + 1
            jw = jc - 1

            kc = ic * nx + jc
            ke = kc + 1
            kw = kc - 1
            kn = kc + nx
            ks = kc - nx

            dce = d(0.5 * (x[jc] + x[je]), y[ic])
            dcw = d(0.5 * (x[jc] + x[jw]), y[ic])
            dcn = d(x[jc], 0.5 * (y[ic] + y[ino]))
            dcs = d(x[jc], 0.5 * (y[ic] + y[iso]))

            A[kc, kc] = (dce + dcw) / dx / dx + (dcn + dcs) / dy / dy
            A[kc, ke] = - dce / dx / dx
            A[kc, kw] = - dcw / dx / dx
            A[kc, kn] = - dcn / dy / dy
            A[kc, ks] = - dcs / dy / dy

            rhs[kc] = f(x[jc], y[ic])

    return A, rhs


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


if (__name__ == '__main__'):
    timestamp()

    # *****************************************************************************80
    #
    # FD2D_HEAT_STEADY_TEST tests the FD2D_HEAT_STEADY library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 August 2013
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('FD2D_HEAT_STEADY_TEST:')
    print('  Python version')
    print('  Test the FD2D_HEAT_STEADY library.')

    fd2d_heat_steady_test01()

    print('')
    print('FD2D_HEAT_STEADY_TEST:')
    print('  Normal end of execution.')
	
    timestamp()
