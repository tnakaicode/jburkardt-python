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


def fd1d_bvp(n, a, aprime, c, f, x):

    # *****************************************************************************80
    #
    # FD1D_BVP solves a two point boundary value problem.
    #
    #  Discussion:
    #
    #    The program uses the finite difference method to solve a BVP
    #    (boundary value problem) in one dimension.
    #
    #    The problem is defined on the region X(1) <= x <= X(N).
    #
    #    The following differential equation is imposed in the region:
    #
    #      - d/dx a(x) du/dx + c(x) * u(x) = f(x)
    #
    #    where a(x), c(x), and f(x) are given functions.  We write out
    #    the equation in full as
    #
    #      - a(x) * u''(x) - a'(x) * u'(x) + c(x) * u(x) = f(x)
    #
    #    At the boundaries, the following conditions are applied:
    #
    #      u(X(1)) = 0.0
    #      u(X(N)) = 0.0
    #
    #    A set of N equally spaced nodes is defined on this
    #    interval, with X(1) < X(2) < \ < X(N).
    #
    #    We replace the function U(X) by a vector of values U(1)
    #    through U(N), associated with the nodes.
    #
    #    The values of U(1) and U(N) are determined by the boundary conditions.
    #
    #    At each interior node I, we write an equation to help us determine
    #    U[i].  We do this by approximating the derivatives of U(X) by
    #    finite differences.  Let us write XL, XM, and XR for X(I-1), X[i] and X(I+1).
    #    Similarly we have UL, UM, and UR.  Other quantities to be evaluated at
    #    X[i] = XM will also be labeled with an M:
    #
    #      - AM * ( UL - 2 UM + UR ) / DX^2
    #      - A'M * ( UL - UR ) / ( 2 * DX )
    #      + CM * UM = FM
    #
    #    These N-2 linear equations for the unknown coefficients complete the
    #    linear system and allow us to compute the finite difference approximation
    #    to the solution of the BVP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of nodes.
    #
    #    Input, function A ( X ), evaluates a(x)
    #
    #    Input, function APRIME ( X ), evaluates a'(x)
    #
    #    Input, function C ( X ), evaluates c(x)
    #
    #    Input, function F ( X ), evaluates f(x)
    #
    #    Input, real X(N), the mesh points, which may be nonuniformly spaced.
    #
    #    Output, real U(N), the value of the finite difference approximation
    #    to the solution.
    #
    import numpy as np
#
#  Make room for the matrix A and right hand side b.
#
    A = np.zeros([n, n])
    rhs = np.zeros(n)

    am = a(x)
    apm = aprime(x)
    cm = c(x)
    fm = f(x)
#
#  The first equation is the left boundary condition, U(X(1)) = 0.0
#
    A[0, 0] = 1.0
    rhs[0] = 0.0
#
#  Now gather the multipliers of U(I-1) to get the matrix entry A(I,I-1), and so on.
#
    for i in range(1, n - 1):
        A[i, i - 1] = - 2.0 * am[i] / (x[i] - x[i - 1]) / (x[i + 1] - x[i - 1]) \
            + apm[i] / (x[i + 1] - x[i - 1])

        A[i, i] = + 2.0 * am[i] / (x[i] - x[i - 1]) / (x[i + 1] - x[i]) + cm[i]

        A[i, i + 1] = - 2.0 * am[i] / (x[i + 1] - x[i]) / (x[i + 1] - x[i - 1]) \
            - apm[i] / (x[i + 1] - x[i - 1])

        rhs[i] = fm[i]
#
#  The last equation is the right boundary condition, U(X(N)) = 0.0
#
    A[n - 1, n - 1] = 1.0
    rhs[n - 1] = 0.0
#
#  Solve the linear system.
#
    u = np.linalg.solve(A, rhs)

    return u


def fd1d_bvp_test():

    # *****************************************************************************80
    #
    # FD1D_BVP_TEST tests FD1D_BVP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('FD1D_BVP_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test FD1D_BVP')

    fd1d_bvp_test01()
    fd1d_bvp_test02()
    fd1d_bvp_test03()
    fd1d_bvp_test04()
    fd1d_bvp_test05()
    fd1d_bvp_test06()
#
#  Terminate.
#
    print('')
    print('FD1D_BVP_TEST')
    print('  Normal end of execution.')

    return


def fd1d_bvp_test01():

    # *****************************************************************************80
    #
    # FD1D_BVP_TEST01 carries out test case #1.
    #
    #  Discussion:
    #
    #    Use A1, C1, F1, EXACT1.
    #
    #    Repeat, using a nonuniform mesh.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    n = 21
    x1 = 0.0
    x2 = 1.0

    print('')
    print('FD1D_BVP_TEST01')
    print('  A1(X)  = 1.0')
    print('  A1\'(X) = 0.0')
    print('  C1(X)  = 0.0')
    print('  F1(X)  = X * ( X + 3 ) * exp ( X )')
    print('  U1(X)  = X * ( 1 - X ) * exp ( X )')
    print('')
    print('  Number of nodes = %d' % (n))
    print('  X1 =  %f' % (x1))
    print('  X2 =  %f' % (x2))
#
#  Set up X, and force it to be a column vector.
#
    x = np.linspace(x1, x2, n)

    u = fd1d_bvp(n, a1, a1prime, c1, f1, x)

    uexact = exact1(x)

    print('')
    print('     I    X         U         Uexact    Error')
    print('')

    for i in range(0, n):
        print('  %4d  %8f  %8f  %8f  %8e' %
              (i, x[i], u[i], uexact[i], np.abs(u[i] - uexact[i])))
#
#  Set up X.
#
    print('')
    print('  Repeat, using a nonuniform mesh.')

    x = np.linspace(x1, x2, n)

    x = np.sqrt(x)

    u = fd1d_bvp(n, a1, a1prime, c1, f1, x)

    uexact = exact1(x)

    print('')
    print('     I    X         U         Uexact    Error')
    print('')

    for i in range(0, n):
        print('  %4d  %8f  %8f  %8f  %8e' %
              (i, x[i], u[i], uexact[i], np.abs(u[i] - uexact[i])))
#
#  Write the FD data to files.
#
    filename = 'fd1d_bvp_test01_nodes.txt'
    r8vec_write(filename, n, x)

    u2 = np.zeros([2, n])
    u2[0, :] = u[:]
    u2[1, :] = uexact[:]

    filename = 'fd1d_bvp_test01_values.txt'
    r8mat_write(filename, 2, n, u2)

    return


def fd1d_bvp_test02():

    # *****************************************************************************80
    #
    # FD1D_BVP_TEST02 carries out test case #2.
    #
    #  Discussion:
    #
    #    Use A1, C2, F2, EXACT1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    n = 11
    x1 = 0.0
    x2 = 1.0

    print('')
    print('FD1D_BVP_TEST02')
    print('  A1(X)  = 1.0')
    print('  A1\'(X) = 0.0')
    print('  C2(X)  = 2.0')
    print('  F2(X)  = X * ( 5 - X ) * exp ( X )')
    print('  U1(X)  = X * ( 1 - X ) * exp ( X )')
    print('')
    print('  Number of nodes = %d' % (n))
    print('  X1 =  %f' % (x1))
    print('  X2 =  %f' % (x2))
#
#  Set up X, and force it to be a column vector.
#
    x = np.linspace(x1, x2, n)

    u = fd1d_bvp(n, a1, a1prime, c2, f2, x)

    uexact = exact1(x)

    print('')
    print('     I    X         U         Uexact    Error')
    print('')

    for i in range(0, n):
        print('  %4d  %8f  %8f  %8f  %8e' %
              (i, x[i], u[i], uexact[i], np.abs(u[i] - uexact[i])))
#
#  Write the FD data to files.
#
    filename = 'fd1d_bvp_test02_nodes.txt'
    r8vec_write(filename, n, x)

    u2 = np.zeros([2, n])
    u2[0, :] = u[:]
    u2[1, :] = uexact[:]

    filename = 'fd1d_bvp_test02_values.txt'
    r8mat_write(filename, 2, n, u2)

    return


def fd1d_bvp_test03():

    # *****************************************************************************80
    #
    # FD1D_BVP_TEST03 carries out test case #3.
    #
    #  Discussion:
    #
    #    Use A1, C3, F3, EXACT1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    n = 11
    x1 = 0.0
    x2 = 1.0

    print('')
    print('FD1D_BVP_TEST03')
    print('  A1(X)  = 1.0')
    print('  A1\'(X) = 0.0')
    print('  C3(X)  = 2.0 * X')
    print('  F3(X)  = - X * ( 2 * X * X - 3 * X - 3 ) * exp ( X )')
    print('  U1(X)  = X * ( 1 - X ) * exp ( X )')
    print('')
    print('  Number of nodes = %d' % (n))
    print('  X1 =  %f' % (x1))
    print('  X2 =  %f' % (x2))
#
#  Set up X, and force it to be a column vector.
#
    x = np.linspace(x1, x2, n)

    u = fd1d_bvp(n, a1, a1prime, c3, f3, x)

    uexact = exact1(x)

    print('')
    print('     I    X         U         Uexact    Error')
    print('')

    for i in range(0, n):
        print('  %4d  %8f  %8f  %8f  %8e' %
              (i, x[i], u[i], uexact[i], np.abs(u[i] - uexact[i])))
#
#  Write the FD data to files.
#
    filename = 'fd1d_bvp_test03_nodes.txt'
    r8vec_write(filename, n, x)

    u2 = np.zeros([2, n])
    u2[0, :] = u[:]
    u2[1, :] = uexact[:]

    filename = 'fd1d_bvp_test03_values.txt'
    r8mat_write(filename, 2, n, u2)

    return


def fd1d_bvp_test04():

    # *****************************************************************************80
    #
    # FD1D_BVP_TEST04 carries out test case #4.
    #
    #  Discussion:
    #
    #    Use A2, C1, F4, EXACT1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    n = 11
    x1 = 0.0
    x2 = 1.0

    print('')
    print('FD1D_BVP_TEST04')
    print('  A2(X)  = 1.0 + X * X')
    print('  A2\'(X) = 2.0 * X')
    print('  C1(X)  = 0.0')
    print('  F4(X)  = ( X + 3 X^2 + 5 X^3 + X^4 ) * exp ( X )')
    print('  U1(X)  = X * ( 1 - X ) * exp ( X )')
    print('')
    print('  Number of nodes = %d' % (n))
    print('  X1 =  %f' % (x1))
    print('  X2 =  %f' % (x2))
#
#  Set up X, and force it to be a column vector.
#
    x = np.linspace(x1, x2, n)

    u = fd1d_bvp(n, a2, a2prime, c1, f4, x)

    uexact = exact1(x)

    print('')
    print('     I    X         U         Uexact    Error')
    print('')

    for i in range(0, n):
        print('  %4d  %8f  %8f  %8f  %8e' %
              (i, x[i], u[i], uexact[i], np.abs(u[i] - uexact[i])))
#
#  Write the FD data to files.
#
    filename = 'fd1d_bvp_test04_nodes.txt'
    r8vec_write(filename, n, x)

    u2 = np.zeros([2, n])
    u2[0, :] = u[:]
    u2[1, :] = uexact[:]

    filename = 'fd1d_bvp_test04_values.txt'
    r8mat_write(filename, 2, n, u2)

    return


def fd1d_bvp_test05():

    # *****************************************************************************80
    #
    # FD1D_BVP_TEST05 carries out test case #5.
    #
    #  Discussion:
    #
    #    Use A3, C1, F5, EXACT1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    n = 11
    x1 = 0.0
    x2 = 1.0

    print('')
    print('FD1D_BVP_TEST05')
    print('  A3(X)  = 1.0 + X * X for X <= 1/3')
    print('         = 7/9 + X     for      1/3 < X')
    print('  A3\'(X) = 2.0 * X     for X <= 1/3')
    print('           1           for      1/3 < X')
    print('  C1(X)  = 0.0')
    print('  F5(X)  = ( X + 3 X^2 + 5 X^3 + X^4 ) * exp ( X )')
    print('                       for X <= 1/3')
    print('         = ( - 1 + 10/3 X + 43/9 X^2 + X^3 ) * exp ( X )')
    print('                       for      1/3 <= X')
    print('  U1(X)  = X * ( 1 - X ) * exp ( X )')
    print('')
    print('  Number of nodes = %d' % (n))
    print('  X1 =  %f' % (x1))
    print('  X2 =  %f' % (x2))

    x = np.linspace(x1, x2, n)

    u = fd1d_bvp(n, a3, a3prime, c1, f5, x)

    uexact = exact1(x)

    print('')
    print('     I    X         U         Uexact    Error')
    print('')

    for i in range(0, n):
        print('  %4d  %8f  %8f  %8f  %8e' %
              (i, x[i], u[i], uexact[i], np.abs(u[i] - uexact[i])))
#
#  Write the FD data to files.
#
    filename = 'fd1d_bvp_test05_nodes.txt'
    r8vec_write(filename, n, x)

    u2 = np.zeros([2, n])
    u2[0, :] = u[:]
    u2[1, :] = uexact[:]

    filename = 'fd1d_bvp_test05_values.txt'
    r8mat_write(filename, 2, n, u2)

    return


def fd1d_bvp_test06():

    # *****************************************************************************80
    #
    # FD1D_BVP_TEST06 carries out test case #6.
    #
    #  Discussion:
    #
    #    Use A2, C2, F6, EXACT1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np

    n = 11
    x1 = 0.0
    x2 = 1.0

    print('')
    print('FD1D_BVP_TEST06')
    print('  A2(X)  = 1.0 + X * X')
    print('  A2\'(X) = 2.0 * X')
    print('  C2(X)  = 2.0')
    print('  F6(X)  = ( 3X + X^2 + 5 X^3 + X^4 ) * exp ( X )')
    print('  U1(X)  = X * ( 1 - X ) * exp ( X )')
    print('')
    print('  Number of nodes = %d' % (n))
    print('  X1 =  %f' % (x1))
    print('  X2 =  %f' % (x2))
#
#  Set up X, and force it to be a column vector.
#
    x = np.linspace(x1, x2, n)

    u = fd1d_bvp(n, a2, a2prime, c2, f6, x)

    uexact = exact1(x)

    print('')
    print('     I    X         U         Uexact    Error')
    print('')

    for i in range(0, n):
        print('  %4d  %8f  %8f  %8f  %8e' %
              (i, x[i], u[i], uexact[i], np.abs(u[i] - uexact[i])))
#
#  Write the FD data to files.
#
    filename = 'fd1d_bvp_test06_nodes.txt'
    r8vec_write(filename, n, x)

    u2 = np.zeros([2, n])
    u2[0, :] = u[:]
    u2[1, :] = uexact[:]

    filename = 'fd1d_bvp_test06_values.txt'
    r8mat_write(filename, 2, n, u2)

    return


def a1(x):

    # *****************************************************************************80
    #
    # A1 evaluates A function #1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of A(X).
    #
    import numpy as np

    value = np.empty_like(x)
    value[:] = 1.0

    return value


def a1prime(x):

    # *****************************************************************************80
    #
    # A1PRIME evaluates A' function #1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 March 2009
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of A(X).
    #
    import numpy as np

    value = np.empty_like(x)
    value[:] = 0.0

    return value


def a2(x):

    # *****************************************************************************80
    #
    # A2 evaluates A function #2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of A(X).
    #
    value = 1.0 + x * x

    return value


def a2prime(x):

    # *****************************************************************************80
    #
    # A2PRIME evaluates A' function #2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of A(X).
    #
    value = 2.0 * x

    return value


def a3(x):

    # *****************************************************************************80
    #
    # A3 evaluates A function #3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of A(X).
    #
    import numpy as np

    value = np.empty_like(x)

    i1 = np.where(x <= 1.0 / 3.0)
    value[i1] = 1.0 + x[i1]**2
    i2 = np.where(1.0 / 3.0 < x)
    value[i2] = x[i2] + 7.0 / 9.0

    return value


def a3prime(x):

    # *****************************************************************************80
    #
    # A3PRIME evaluates A' function #3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of A(X).
    #
    import numpy as np

    value = np.empty_like(x)
    i1 = np.where(x <= 1.0 / 3.0)
    value[i1] = 2.0 * x[i1]
    i2 = np.where(1.0 / 3.0 < x)
    value[i2] = 1.0

    return value


def c1(x):

    # *****************************************************************************80
    #
    # C1 evaluates C function #1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of C(X).
    #
    import numpy as np

    value = np.empty_like(x)
    value[:] = 0.0

    return value


def c2(x):

    # *****************************************************************************80
    #
    # C2 evaluates C function #2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of C(X).
    #
    import numpy as np

    value = np.empty_like(x)
    value[:] = 2.0

    return value


def c3(x):

    # *****************************************************************************80
    #
    # C3 evaluates C function #3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of C(X).
    #
    value = 2.0 * x

    return value


def f1(x):

    # *****************************************************************************80
    #
    # F1 evaluates right hand side function #1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of F(X).
    #
    import numpy as np

    value = x * (x + 3.0) * np.exp(x)

    return value


def f2(x):

    # *****************************************************************************80
    #
    # F2 evaluates right hand side function #2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of F(X).
    #
    import numpy as np

    value = x * (5.0 - x) * np.exp(x)

    return value


def f3(x):

    # *****************************************************************************80
    #
    # F3 evaluates right hand side function #3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of F(X).
    #
    import numpy as np

    value = - x * (2.0 * x * x - 3.0 * x - 3.0) * np.exp(x)

    return value


def f4(x):

    # *****************************************************************************80
    #
    # F4 evaluates right hand side function #4.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of F(X).
    #
    import numpy as np

    value = (x + 3.0 * x**2 + 5.0 * x**3 + x**4) * np.exp(x)

    return value


def f5(x):

    # *****************************************************************************80
    #
    # F5 evaluates right hand side function #5.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of F(X).
    #
    import numpy as np

    value = np.empty_like(x)
    i1 = np.where(x <= 1.0 / 3.0)
    value[i1] = (x[i1] + 3.0 * x[i1]**2 + 5.0 *
                 x[i1]**3 + x[i1]**4) * np.exp(x[i1])
    i2 = np.where(1.0 / 3.0 < x)
    value[i2] = (- 1.0 + (10.0 / 3.0) * x[i2] + (43.0 / 9.0)
                 * x[i2]**2 + x[i2]**3) * np.exp(x[i2])

    return value


def f6(x):

    # *****************************************************************************80
    #
    # F6 evaluates right hand side function #6.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of F(X).
    #
    import numpy as np

    value = (3.0 * x + x**2 + 5.0 * x**3 + x**4) * np.exp(x)

    return value


def exact1(x):

    # *****************************************************************************80
    #
    # EXACT1 evaluates exact solution #1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of U(X).
    #
    import numpy as np

    value = x * (1.0 - x) * np.exp(x)

    return value


def exact2(x):

    # *****************************************************************************80
    #
    # EXACT2 returns exact solution #2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of U(X).
    #
    import numpy as np

    value = np.empty_like(x)
    i1 = np.where(x <= 2.0 / 3.0)
    value[i1] = x[i1] * (1.0 - x[i1]) * np.exp(x[i1])
    i2 = np.where(2.0 / 3.0 < x)
    value[i2] = (x[i2] * (1.0 - x[i2]) * np.exp(2.0 / 3.0))

    return value


def exact3(x):

    # *****************************************************************************80
    #
    # EXACT3 returns exact solution #3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the value of U(X).
    #
    import numpy as np

    value = np.empty_like(x)
    i1 = np.where(x <= 2.0 / 3.0)
    value[i1] = x[i1] * (1.0 - x[i1]) * np.exp(x[i1])
    i2 = np.where(2.0 / 3.0 < x)
    value[i2] = x[i2] * (1.0 - x[i2])

    return value


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
    print('')
    print('R8VEC_WRITE_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    fd1d_bvp_test()
    timestamp()
