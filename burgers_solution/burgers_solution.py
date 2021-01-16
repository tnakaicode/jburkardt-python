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
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8_epsilon import r8_epsilon
from r8lib.r8_gamma import r8_gamma
from r8lib.r8_sign import r8_sign

obj = plot2d()


def burgers_solution_test():

    # *****************************************************************************80
    #
    # BURGERS_SOLUTION_TEST tests the BURGERS_SOLUTION library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('BURGERS_SOLUTION_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  BURGERS_SOLUTION evaluates exact solutions of the Burgers equation.')

    burgers_viscous_time_exact1_test01()
    burgers_viscous_time_exact1_test02()
    burgers_viscous_time_exact2_test01()
    burgers_viscous_time_exact2_test02()

    print('')
    print('BURGERS_SOLUTION_TEST:')
    print('  Normal end of execution.')


def burgers_viscous_time_exact1(nu, vxn, vx, vtn, vt):

    # *****************************************************************************80
    #
    # BURGERS_VISCOUS_TIME_EXACT1 evaluates a solution to the Burgers equation.
    #
    #  Discussion:
    #
    #    The form of the Burgers equation considered here is
    #
    #      du       du        d^2 u
    #      -- + u * -- = nu * -----
    #      dt       dx        dx^2
    #
    #    for -1.0 < x < +1.0, and 0 < t.
    #
    #    Initial conditions are u(x,0) = - sin(pi*x).  Boundary conditions
    #    are u(-1,t) = u(+1,t) = 0.  The viscosity parameter nu is taken
    #    to be 0.01 / pi, although this is not essential.
    #
    #    The authors note an integral representation for the solution u(x,t),
    #    and present a better version of the formula that is amenable to
    #    approximation using Hermite quadrature.
    #
    #    This program library does little more than evaluate the exact solution
    #    at a user-specified set of points, using the quadrature rule.
    #    Internally, the order of this quadrature rule is set to 8, but the
    #    user can easily modify this value if greater accuracy is desired.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 September 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Claude Basdevant, Michel Deville, Pierre Haldenwang, J Lacroix,
    #    J Ouazzani, Roger Peyret, Paolo Orlandi, Anthony Patera,
    #    Spectral and finite difference solutions of the Burgers equation,
    #    Computers and Fluids,
    #    Volume 14, Number 1, 1986, pages 23-41.
    #
    #  Parameters:
    #
    #    Input, real NU, the viscosity.
    #
    #    Input, integer VXN, the number of spatial grid points.
    #
    #    Input, real VX(VXN), the spatial grid points.
    #
    #    Input, integer VTN, the number of time grid points.
    #
    #    Input, real VT(VTN), the time grid points.
    #
    #    Output, real VU(VXN,VTN), the solution of the Burgers
    #    equation at each space and time grid point.
    #

    qn = 8

    #  Compute the rule.
    qx, qw = hermite_ek_compute(qn)

    #  Evaluate U(X,T) for later times.
    vu = np.zeros([vxn, vtn])

    for vti in range(0, vtn):
        if (vt[vti] == 0.0):
            for i in range(0, vxn):
                vu[i, vti] = - np.sin(np.pi * vx[i])
        else:
            for vxi in range(0, vxn):
                top = 0.0
                bot = 0.0
                for qi in range(0, qn):
                    c = 2.0 * np.sqrt(nu * vt[vti])
                    top = top - qw[qi] * c * np.sin(np.pi * (vx[vxi] - c * qx[qi])) \
                        * np.exp(- np.cos(np.pi * (vx[vxi] - c * qx[qi]))
                                 / (2.0 * np.pi * nu))

                    bot = bot + qw[qi] * c \
                        * np.exp(- np.cos(np.pi * (vx[vxi] - c * qx[qi]))
                                 / (2.0 * np.pi * nu))

                    vu[vxi, vti] = top / bot

    obj.new_2Dfig()
    obj.axs.imshow(vu, cmap="jet")
    obj.SavePng_Serial(obj.tmpdir + "burgers_viscous_time_exact1.png")
    plt.clf()

    return vu


def burgers_viscous_time_exact1_test01():

    # *****************************************************************************80
    #
    # BURGERS_VISCOUS_TIME_EXACT1_TEST01 tests sets up a small test case.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    vtn = 51
    vxn = 51
    nu = 0.01 / np.pi

    print('')
    print('BURGERS_VISCOUS_TIME_EXACT1_TEST01')
    print('  Python version: %s' % (platform.python_version()))
    print('  BURGERS_VISCOUS_TIME_EXACT1 evaluates solution #1')
    print('  to the Burgers equation.')
    print('')
    print('  Viscosity NU = %g' % (nu))
    print('  NX = %d' % (vxn))
    print('  NT = %d' % (vtn))

    xlo = -1.0
    xhi = +1.0
    vx = np.linspace(xlo, xhi, vxn)
    r8vec_print(vxn, vx, '  X grid points:')

    tlo = 0.0
    thi = 3.0 / np.pi
    vt = np.linspace(tlo, thi, vtn)
    r8vec_print(vtn, vt, '  T grid points:')

    vu = burgers_viscous_time_exact1(nu, vxn, vx, vtn, vt)

    filename = 'burgers_solution_test01.txt'
    r8mat_print(vxn, vtn, vu, '  U(X,T) at grid points:')
    r8mat_write(filename, vxn, vtn, vu)

    print('')
    print('  Data written to file "%s"' % (filename))
    print('')
    print('BURGERS_VISCOUS_TIME_EXACT1_TEST01')
    print('  Normal end of execution.')


def burgers_viscous_time_exact1_test02():

    # *****************************************************************************80
    #
    # BURGERS_VISCOUS_TIME_EXACT1_TEST02 tests sets up a finer test case.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    vtn = 101
    vxn = 101
    nu = 0.01 / np.pi

    print('')
    print('BURGERS_VISCOUS_TIME_EXACT1_TEST02')
    print('  Python version: %s' % (platform.python_version()))
    print('  BURGERS_VISCOUS_TIME_EXACT1 computes solution #1')
    print('  to the Burgers equation.')
    print('')
    print('  Viscosity NU = %g' % (nu))
    print('  NX = %d' % (vxn))
    print('  NT = %d' % (vtn))

    xlo = -1.0
    xhi = +1.0
    vx = np.linspace(xlo, xhi, vxn)
    r8vec_print(vxn, vx, '  X grid points:')

    tlo = 0.0
    thi = 3.0 / np.pi
    vt = np.linspace(tlo, thi, vtn)
    r8vec_print(vtn, vt, '  T grid points:')

    vu = burgers_viscous_time_exact1(nu, vxn, vx, vtn, vt)

    filename = 'burgers_solution_test02.txt'
    r8mat_print(vxn, vtn, vu, '  U(X,T) at grid points:')
    r8mat_write(filename, vxn, vtn, vu)

    print('')
    print('  Data written to file "%s"' % (filename))
    print('')
    print('BURGERS_VISCOUS_TIME_EXACT1_TEST02')
    print('  Normal end of execution.')


def burgers_viscous_time_exact2(nu, xn, x, tn, t):

    # *****************************************************************************80
    #
    # BURGERS_VISCOUS_TIME_EXACT2 evaluates a solution to the Burgers equation.
    #
    #  Discussion:
    #
    #    The form of the Burgers equation considered here is
    #
    #      du       du        d^2 u
    #      -- + u * -- = nu * -----
    #      dt       dx        dx^2
    #
    #    for 0.0 < x < 2 Pi, and 0 < t.
    #
    #    The initial condition is
    #
    #      u(x,0) = 4 - 2 * nu * dphi(x,0)/dx / phi(x,0)
    #
    #    where
    #
    #      phi(x,t) = exp ( - ( x-4*t      ) / ( 4*nu*(t+1) ) )
    #               + exp ( - ( x-4*t-2*pi ) / ( 4*nu*(t+1) ) )
    #
    #    The boundary conditions are periodic:
    #
    #      u(0,t) = u(2 Pi,t)
    #
    #    The viscosity parameter nu may be taken to be 0.01, but other values
    #    may be chosen.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 September 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Claude Basdevant, Michel Deville, Pierre Haldenwang, J Lacroix,
    #    J Ouazzani, Roger Peyret, Paolo Orlandi, Anthony Patera,
    #    Spectral and finite difference solutions of the Burgers equation,
    #    Computers and Fluids,
    #    Volume 14, Number 1, 1986, pages 23-41.
    #
    #  Parameters:
    #
    #    Input, real NU, the viscosity.
    #
    #    Input, integer XN, the number of spatial grid points.
    #
    #    Input, real X(XN), the spatial grid points.
    #
    #    Input, integer TN, the number of time grid points.
    #
    #    Input, real T(TN), the time grid points.
    #
    #    Output, real U(XN,TN), the solution of the Burgers
    #    equation at each space and time grid point.
    #

    u = np.zeros([xn, tn])

    for j in range(0, tn):
        for i in range(0, xn):
            a = (x[i] - 4.0 * t[j])
            b = (x[i] - 4.0 * t[j] - 2.0 * np.pi)
            c = 4.0 * nu * (t[j] + 1.0)
            phi = np.exp(- a * a / c) + np.exp(- b * b / c)
            dphi = - 2.0 * a * np.exp(- a * a / c) / c \
                   - 2.0 * b * np.exp(- b * b / c) / c
            u[i, j] = 4.0 - 2.0 * nu * dphi / phi

    obj.new_2Dfig()
    obj.axs.imshow(u, cmap="jet")
    obj.SavePng_Serial(obj.tmpdir + "burgers_viscous_time_exact2.png")
    plt.clf()

    return u


def burgers_viscous_time_exact2_test01():

    # *****************************************************************************80
    #
    # BURGERS_VISCOUS_TIME_EXACT2_TEST01 tests sets up a small test case.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    vtn = 51
    vxn = 51
    nu = 0.5

    print('')
    print('BURGERS_VISCOUS_TIME_EXACT2_TEST01')
    print('  Python version: %s' % (platform.python_version()))
    print('  BURGERS_VISCOUS_TIME_EXACT2 evaluates solution #2')
    print('  to the Burgers equation.')
    print('')
    print('  Viscosity NU = %g' % (nu))
    print('  NX = %d' % (vxn))
    print('  NT = %d' % (vtn))

    xlo = 0.0
    xhi = 2.0 * np.pi
    vx = np.linspace(xlo, xhi, vxn)
    r8vec_print(vxn, vx, '  X grid points:')

    tlo = 0.0
    thi = 1.0
    vt = np.linspace(tlo, thi, vtn)
    r8vec_print(vtn, vt, '  T grid points:')

    vu = burgers_viscous_time_exact2(nu, vxn, vx, vtn, vt)

    filename = 'burgers_solution_test03.txt'
    r8mat_print(vxn, vtn, vu, '  U(X,T) at grid points:')
    r8mat_write(filename, vxn, vtn, vu)

    print('')
    print('  Data written to file "%s"' % (filename))
    print('')
    print('BURGERS_VISCOUS_TIME_EXACT2_TEST01')
    print('  Normal end of execution.')


def burgers_viscous_time_exact2_test02():

    # *****************************************************************************80
    #
    # BURGERS_VISCOUS_TIME_EXACT2_TEST02 tests sets up a finer test case.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    vtn = 101
    vxn = 101
    nu = 0.5

    print('')
    print('BURGERS_VISCOUS_TIME_EXACT2_TEST02')
    print('  Python version: %s' % (platform.python_version()))
    print('  BURGERS_VISCOUS_TIME_EXACT2 computes solution #2')
    print('  to the Burgers equation.')
    print('')
    print('  Viscosity NU = %g' % (nu))
    print('  NX = %d' % (vxn))
    print('  NT = %d' % (vtn))

    xlo = 0.0
    xhi = 2.0 * np.pi
    vx = np.linspace(xlo, xhi, vxn)
    r8vec_print(vxn, vx, '  X grid points:')

    tlo = 0.0
    thi = 1.0
    vt = np.linspace(tlo, thi, vtn)
    r8vec_print(vtn, vt, '  T grid points:')

    vu = burgers_viscous_time_exact2(nu, vxn, vx, vtn, vt)

    filename = 'burgers_solution_test04.txt'
    r8mat_print(vxn, vtn, vu, '  U(X,T) at grid points:')
    r8mat_write(filename, vxn, vtn, vu)

    print('')
    print('  Data written to file "%s"' % (filename))
    print('')
    print('BURGERS_VISCOUS_TIME_EXACT2_TEST02')
    print('  Normal end of execution.')


def hermite_ek_compute(n):

    # *****************************************************************************80
    #
    # HERMITE_EK_COMPUTE computes a Gauss-Hermite quadrature rule.
    #
    #  Discussion:
    #
    #    The code uses an algorithm by Elhay and Kautsky.
    #
    #    The abscissas are the zeros of the N-th order Hermite polynomial.
    #
    #    The integral:
    #
    #      integral ( -oo < x < +oo ) exp ( - x * x ) * f(x) dx
    #
    #    The quadrature rule:
    #
    #      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 June 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Sylvan Elhay, Jaroslav Kautsky,
    #    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
    #    Interpolatory Quadrature,
    #    ACM Transactions on Mathematical Software,
    #    Volume 13, Number 4, December 1987, pages 399-415.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of abscissas.
    #
    #    Output, real X(N), the abscissas.
    #
    #    Output, real W(N), the weights.
    #

    #  Define the zero-th moment.
    zemu = r8_gamma(0.5)

    #  Define the Jacobi matrix.
    bj = np.zeros(n)
    for i in range(0, n):
        bj[i] = np.sqrt(float(i + 1) / 2.0)

    x = np.zeros(n)

    w = np.zeros(n)
    w[0] = np.sqrt(zemu)

    #  Diagonalize the Jacobi matrix.
    x, w = imtqlx(n, x, bj, w)

    #  If N is odd, force the center X to be exactly 0.
    if ((n % 2) == 1):
        x[(n - 1) // 2] = 0.0

    for i in range(0, n):
        w[i] = w[i] ** 2

    return x, w


def imtqlx(n, d, e, z):

    # *****************************************************************************80
    #
    # IMTQLX diagonalizes a symmetric tridiagonal matrix.
    #
    #  Discussion:
    #
    #    This routine is a slightly modified version of the EISPACK routine to
    #    perform the implicit QL algorithm on a symmetric tridiagonal matrix.
    #
    #    The authors thank the authors of EISPACK for permission to use this
    #    routine.
    #
    #    It has been modified to produce the product Q' * Z, where Z is an input
    #    vector and Q is the orthogonal matrix diagonalizing the input matrix.
    #    The changes consist (essentially) of applying the orthogonal
    #    transformations directly to Z as they are generated.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 June 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Sylvan Elhay, Jaroslav Kautsky,
    #    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
    #    Interpolatory Quadrature,
    #    ACM Transactions on Mathematical Software,
    #    Volume 13, Number 4, December 1987, pages 399-415.
    #
    #    Roger Martin, James Wilkinson,
    #    The Implicit QL Algorithm,
    #    Numerische Mathematik,
    #    Volume 12, Number 5, December 1968, pages 377-383.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real D(N), the diagonal entries of the matrix.
    #
    #    Input, real E(N), the subdiagonal entries of the
    #    matrix, in entries E(1) through E(N-1).
    #
    #    Input, real Z(N), a vector to be operated on.
    #
    #    Output, real LAM(N), the diagonal entries of the diagonalized matrix.
    #
    #    Output, real QTZ(N), the value of Q' * Z, where Q is the matrix that
    #    diagonalizes the input symmetric tridiagonal matrix.
    #

    lam = np.zeros(n)
    for i in range(0, n):
        lam[i] = d[i]

    qtz = np.zeros(n)
    for i in range(0, n):
        qtz[i] = z[i]

    if (n == 1):
        return lam, qtz

    itn = 30
    prec = r8_epsilon()
    e[n - 1] = 0.0

    for l in range(1, n + 1):
        j = 0
        while (True):
            for m in range(l, n + 1):
                if (m == n):
                    break

                if (abs(e[m - 1]) <= prec * (abs(lam[m - 1]) + abs(lam[m]))):
                    break

            p = lam[l - 1]
            if (m == l):
                break
            if (itn <= j):
                print('')
                print('IMTQLX - Fatal error!')
                print('  Iteration limit exceeded.')
                exit('IMTQLX - Fatal error!')

            j = j + 1
            g = (lam[l] - p) / (2.0 * e[l - 1])
            r = np.sqrt(g * g + 1.0)

            if (g < 0.0):
                t = g - r
            else:
                t = g + r

            g = lam[m - 1] - p + e[l - 1] / (g + t)

            s = 1.0
            c = 1.0
            p = 0.0
            mml = m - l

            for ii in range(1, mml + 1):

                i = m - ii
                f = s * e[i - 1]
                b = c * e[i - 1]

                if (abs(g) <= abs(f)):
                    c = g / f
                    r = np.sqrt(c * c + 1.0)
                    e[i] = f * r
                    s = 1.0 / r
                    c = c * s
                else:
                    s = f / g
                    r = np.sqrt(s * s + 1.0)
                    e[i] = g * r
                    c = 1.0 / r
                    s = s * c

                g = lam[i] - p
                r = (lam[i - 1] - g) * s + 2.0 * c * b
                p = s * r
                lam[i] = g + p
                g = c * r - b
                f = qtz[i]
                qtz[i] = s * qtz[i - 1] + c * f
                qtz[i - 1] = c * qtz[i - 1] - s * f

            lam[l - 1] = lam[l - 1] - p
            e[l - 1] = g
            e[m - 1] = 0.0

    for ii in range(2, n + 1):

        i = ii - 1
        k = i
        p = lam[i - 1]

        for j in range(ii, n + 1):

            if (lam[j - 1] < p):
                k = j
                p = lam[j - 1]

        if (k != i):

            lam[k - 1] = lam[i - 1]
            lam[i - 1] = p

            p = qtz[i - 1]
            qtz[i - 1] = qtz[k - 1]
            qtz[k - 1] = p

    return lam, qtz


if (__name__ == '__main__'):
    timestamp()
    burgers_solution_test()
    timestamp()
