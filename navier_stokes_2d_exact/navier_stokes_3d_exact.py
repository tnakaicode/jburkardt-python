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
from r8lib.r8vec_transpose import r8vec_transpose_print
from r8lib.r8mat_transpose import r8mat_transpose_print, r8mat_transpose_print_some

from r8lib.r8_erf import r8_erf
from r8lib.r8vec_uniform_ab import r8vec_uniform_ab


def resid_burgers(nu, n, x, y, z, t):

    # *****************************************************************************80
    #
    # RESID_BURGERS: Burgers Navier Stokes residual.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Martin Bazant, Henry Moffatt,
    #    Exact solutions of the Navier-Stokes equations having steady vortex structures,
    #    Journal of Fluid Mechanics,
    #    Volume 541, pages 55-64, 2005.
    #
    #    Johannes Burgers,
    #    A mathematical model illustrating the theory of turbulence,
    #    Advances in Applied Mechanics,
    #    Volume 1, pages 171-199, 1948.
    #
    #  Parameters:
    #
    #    Input, real NU, the viscosity.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), Z(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinates.
    #
    #    Output, real UR(N), VR(N), WR(N), PR(N), the residuals.
    #
    #
    #  Form the functions and derivatives.
    #
    u = 2.0 * x
    ux = 2.0 * np.ones(n)
    uxx = np.zeros(n)
    uy = np.zeros(n)
    uyy = np.zeros(n)
    uz = np.zeros(n)
    uzz = np.zeros(n)
    ut = np.zeros(n)

    v = - 2.0 * y
    vx = np.zeros(n)
    vxx = np.zeros(n)
    vy = - 2.0 * np.ones(n)
    vyy = np.zeros(n)
    vz = np.zeros(n)
    vzz = np.zeros(n)
    vt = np.zeros(n)

    w = np.zeros(n)
    for i in range(0, n):
        w[i] = r8_erf(y[i] / np.sqrt(nu))
    wx = np.zeros(n)
    wxx = np.zeros(n)
    wy = 2.0 * np.sqrt(1.0 / nu / np.pi) * np.exp(- y ** 2 / nu)
    wyy = - 4.0 * np.sqrt(1.0 / nu / np.pi) * y * np.exp(- y ** 2 / nu) / nu
    wz = np.zeros(n)
    wzz = np.zeros(n)
    wt = np.zeros(n)

    p = - 2.0 * (x ** 2 + y ** 2)
    px = - 4.0 * x
    py = - 4.0 * y
    pz = np.zeros(n)
    #
    #  Evaluate the residuals.
    #
    ur = ut + u * ux + v * uy + w * uz + px - nu * (uxx + uyy + uzz)
    vr = vt + u * vx + v * vy + w * vz + py - nu * (vxx + vyy + vzz)
    wr = wt + u * wx + v * wy + w * wz + pz - nu * (wxx + wyy + wzz)
    pr = ux + vy + wz

    return ur, vr, wr, pr


def resid_burgers_test():

    # *****************************************************************************80
    #
    # RESID_BURGERS_TEST samples the Burgers residual at the initial time.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    nu = 0.25

    print('')
    print('RESID_BURGERS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RESID_BURGERS evaluates the Burgers residual.')
    print('  Sample at the initial time T = 0, using a region that is')
    print('  the cube centered at (0,0,0) with "radius" 1.0,')
    print('  Viscosity NU = %g' % (nu))

    n = 1000
    x_lo = -1.0
    x_hi = +1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    z, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    t = np.zeros(n)
    ur, vr, wr, pr = resid_burgers(nu, n, x, y, z, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  Ur:  %14.6g  %14.6g' % (np.min(np.abs(ur)), np.max(np.abs(ur))))
    print('  Vr:  %14.6g  %14.6g' % (np.min(np.abs(vr)), np.max(np.abs(vr))))
    print('  Wr:  %14.6g  %14.6g' % (np.min(np.abs(wr)), np.max(np.abs(wr))))
    print('  Pr:  %14.6g  %14.6g' % (np.min(np.abs(pr)), np.max(np.abs(pr))))
    print('')
    print('RESID_BURGERS_TEST:')
    print('  Normal end of execution.')


def uvwp_burgers(nu, n, x, y, z, t):

    # *****************************************************************************80
    #
    # UVWP_BURGERS evaluates the Burgers solution.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Martin Bazant, Henry Moffatt,
    #    Exact solutions of the Navier-Stokes equations having steady vortex structures,
    #    Journal of Fluid Mechanics,
    #    Volume 541, pages 55-64, 2005.
    #
    #    Johannes Burgers,
    #    A mathematical model illustrating the theory of turbulence,
    #    Advances in Applied Mechanics,
    #    Volume 1, pages 171-199, 1948.
    #
    #  Parameters:
    #
    #    Input, real NU, the kinematic viscosity.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), Z(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinates.
    #
    #    Output, real U(N), V(N), W(N), P(N), the velocity components and
    #    pressure at each of the points.
    #

    u = 2.0 * x
    v = - 2.0 * y
    w = np.zeros(n)
    for i in range(0, n):
        w[i] = r8_erf(y[i] / np.sqrt(nu))
    p = - 2.0 * (x ** 2 + y ** 2)

    return u, v, w, p


def uvwp_burgers_test():

    # *****************************************************************************80
    #
    # UVWP_BURGERS_TEST samples the Burgers solution.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    nu = 0.25

    print('')
    print('UVWP_BURGERS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  UVWP samples the Burgers solution.')
    print('  Estimate the range of velocity and pressure')
    print('  at the initial time T = 0, using a region that is')
    print('  the cube centered at (0,0,0) with "radius" 1.0,')
    print('  Viscosity NU = %g' % (nu))

    n = 1000
    x_lo = -1.0
    x_hi = +1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    z, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    t = np.zeros(n)
    u, v, w, p = uvwp_burgers(nu, n, x, y, z, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  U:  %14.6g  %14.6g' % (np.min(u), np.max(u)))
    print('  V:  %14.6g  %14.6g' % (np.min(v), np.max(v)))
    print('  W:  %14.6g  %14.6g' % (np.min(w), np.max(w)))
    print('  P:  %14.6g  %14.6g' % (np.min(p), np.max(p)))
    print('')
    print('UVWP_BURGERS_TEST:')
    print('  Normal end of execution.')


def resid_ethier(a, d, n, x, y, z, t):

    # *****************************************************************************80
    #
    # RESID_ETHIER evaluates the Ethier residual.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    C Ross Ethier, David Steinman,
    #    Exact fully 3D Navier-Stokes solutions for benchmarking,
    #    International Journal for Numerical Methods in Fluids,
    #    Volume 19, Number 5, March 1994, pages 369-375.
    #
    #  Parameters:
    #
    #    Input, real A, D, the parameters.  Sample values are A = PI/4 and
    #    D = PI/2.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), Z(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinates.
    #
    #    Output, real UR(N), VR(N), WR(N), PR(N), the residuals.
    #
    #
    #  Make some temporaries.
    #
    ex = np.exp(a * x)
    ey = np.exp(a * y)
    ez = np.exp(a * z)

    e2x = np.exp(2.0 * a * x)
    e2y = np.exp(2.0 * a * y)
    e2z = np.exp(2.0 * a * z)

    e2t = np.exp(- d * d * t)
    e4t = np.exp(- 2.0 * d * d * t)

    exy = np.exp(a * (x + y))
    eyz = np.exp(a * (y + z))
    ezx = np.exp(a * (z + x))

    sxy = np.sin(a * x + d * y)
    syz = np.sin(a * y + d * z)
    szx = np.sin(a * z + d * x)

    cxy = np.cos(a * x + d * y)
    cyz = np.cos(a * y + d * z)
    czx = np.cos(a * z + d * x)

    #  Form the functions and derivatives.
    u = -         a * (ex * syz + ez * cxy) * e2t
    ux = -         a * (a * ex * syz - a * ez * sxy) * e2t
    uxx = -         a * (a * a * ex * syz - a * a * ez * cxy) * e2t
    uy = -         a * (a * ex * cyz - d * ez * sxy) * e2t
    uyy = -         a * (- a * a * ex * syz - d * d * ez * cxy) * e2t
    uz = -         a * (d * ex * cyz + a * ez * cxy) * e2t
    uzz = -        a * (- d * d * ex * syz + a * a * ez * cxy) * e2t
    ut = + d * d * a * (ex * syz + ez * cxy) * e2t

    v = -         a * (ey * szx + ex * cyz) * e2t
    vx = -         a * (d * ey * czx + a * ex * cyz) * e2t
    vxx = -         a * (- d * d * ey * szx + a * a * ex * cyz) * e2t
    vy = -         a * (a * ey * szx - a * ex * syz) * e2t
    vyy = -         a * (a * a * ey * szx - a * a * ex * cyz) * e2t
    vz = -         a * (a * ey * czx - d * ex * syz) * e2t
    vzz = -        a * (- a * a * ey * szx - d * d * ex * cyz) * e2t
    vt = + d * d * a * (ey * szx + ex * cyz) * e2t

    w = -         a * (ez * sxy + ey * czx) * e2t
    wx = -         a * (a * ez * cxy - d * ey * szx) * e2t
    wxx = -         a * (- a * a * ez * sxy - d * d * ey * czx) * e2t
    wy = -         a * (d * ez * cxy + a * ey * czx) * e2t
    wyy = -         a * (- d * d * ez * sxy + a * a * ey * czx) * e2t
    wz = -         a * (a * ez * sxy - a * ey * szx) * e2t
    wzz = -         a * (a * a * ez * sxy - a * a * ey * czx) * e2t
    wt = + d * d * a * (ez * sxy + ey * czx) * e2t

    p = - 0.5 * a * a * e4t * (
        + e2x + 2.0 * sxy * czx * eyz
        + e2y + 2.0 * syz * cxy * ezx
        + e2z + 2.0 * szx * cyz * exy)

    px = - 0.5 * a * a * e4t * (
        + 2.0 * a * e2x + 2.0 * a * cxy * czx * eyz - 2.0 * d * sxy * szx * eyz
        - 2.0 * a * syz * sxy * ezx + 2.0 * a * syz * cxy * ezx
        + 2.0 * d * czx * cyz * exy + 2.0 * a * szx * cyz * exy)

    py = - 0.5 * a * a * e4t * (
        + 2.0 * d * cxy * czx * eyz + 2.0 * a * sxy * czx * eyz
        + 2.0 * a * e2y + 2.0 * a * cyz * cxy * ezx - 2.0 * d * syz * sxy * ezx
        - 2.0 * a * szx * syz * exy + 2.0 * a * szx * cyz * exy)

    pz = - 0.5 * a * a * e4t * (
        - 2.0 * a * sxy * szx * eyz + 2.0 * a * sxy * czx * eyz
        + 2.0 * d * cyz * cxy * ezx + 2.0 * a * syz * cxy * ezx
        + 2.0 * a * e2z + 2.0 * a * czx * cyz * exy - 2.0 * d * szx * syz * exy)

    #  Evaluate the residuals.
    ur = ut + u * ux + v * uy + w * uz + px - (uxx + uyy + uzz)
    vr = vt + u * vx + v * vy + w * vz + py - (vxx + vyy + vzz)
    wr = wt + u * wx + v * wy + w * wz + pz - (wxx + wyy + wzz)
    pr = ux + vy + wz

    return ur, vr, wr, pr


def resid_ethier_test():

    # *****************************************************************************80
    #
    # RESID_ETHIER_TEST samples the Ethier residual.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    a = np.pi / 4.0
    d = np.pi / 2.0

    print('')
    print('RESID_ETHIER_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RESID_ETHIER evaluates the Ethier residual.')
    print('  Sample the residuals')
    print('  at the initial time T = 0, using a region that is')
    print('  the cube centered at (0,0,0) with "radius" 1.0,')
    print('  Parameter A = %g' % (a))
    print('  Parameter D = %g' % (d))

    n = 1000
    x_lo = -1.0
    x_hi = +1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    z, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    t = np.zeros(n)
    ur, vr, wr, pr = resid_ethier(a, d, n, x, y, z, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  Ur:  %14.6g  %14.6g' % (np.min(np.abs(ur)), np.max(np.abs(ur))))
    print('  Vr:  %14.6g  %14.6g' % (np.min(np.abs(vr)), np.max(np.abs(vr))))
    print('  Wr:  %14.6g  %14.6g' % (np.min(np.abs(wr)), np.max(np.abs(wr))))
    print('  Pr:  %14.6g  %14.6g' % (np.min(np.abs(pr)), np.max(np.abs(pr))))
    print('')
    print('RESID_ETHIER_TEST:')
    print('  Normal end of execution.')


def uvwp_ethier(a, d, n, x, y, z, t):

    # *****************************************************************************80
    #
    # UVWP_ETHIER evaluates the Ethier exact Navier Stokes solution.
    #
    #  Discussion:
    #
    #    The reference asserts that the given velocity and pressure fields
    #    are exact solutions for the 3D incompressible time-dependent
    #    Navier Stokes equations over any region.
    #
    #    To define a typical problem, one chooses a bounded spatial region
    #    and a starting time, and then imposes boundary and initial conditions
    #    by referencing the exact solution appropriately.
    #
    #    In the reference paper, a calculation is made for the cube centered
    #    at (0,0,0) with a "radius" of 1 unit, and over the time interval
    #    from t = 0 to t = 0.1, with parameters a = PI/4 and d = PI/2,
    #    and with Dirichlet boundary conditions on all faces of the cube.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    C Ross Ethier, David Steinman,
    #    Exact fully 3D Navier-Stokes solutions for benchmarking,
    #    International Journal for Numerical Methods in Fluids,
    #    Volume 19, Number 5, March 1994, pages 369-375.
    #
    #  Parameters:
    #
    #    Input, real A, D, the parameters.  Sample values are A = PI/4 and
    #    D = PI/2.
    #
    #    Input, integer N, the number of points at which the solution is to
    #    be evaluated.
    #
    #    Input, real X(N), Y(N), Z(N), the coordinates of the points.
    #
    #    Input, real T(N), the time coordinates.
    #
    #    Output, real U(N), V(N), W(N), P(N), the velocity components and
    #    pressure at each of the points.
    #

    ex = np.exp(a * x)
    ey = np.exp(a * y)
    ez = np.exp(a * z)

    e2t = np.exp(- d * d * t)

    exy = np.exp(a * (x + y))
    eyz = np.exp(a * (y + z))
    ezx = np.exp(a * (z + x))

    sxy = np.sin(a * x + d * y)
    syz = np.sin(a * y + d * z)
    szx = np.sin(a * z + d * x)

    cxy = np.cos(a * x + d * y)
    cyz = np.cos(a * y + d * z)
    czx = np.cos(a * z + d * x)

    u = - a * (ex * syz + ez * cxy) * e2t
    v = - a * (ey * szx + ex * cyz) * e2t
    w = - a * (ez * sxy + ey * czx) * e2t
    p = 0.5 * a * a * e2t * e2t * (
        + ex * ex + 2.0 * sxy * czx * eyz
        + ey * ey + 2.0 * syz * cxy * ezx
        + ez * ez + 2.0 * szx * cyz * exy)

    return u, v, w, p


def uvwp_ethier_test():

    # *****************************************************************************80
    #
    # UVWP_ETHIER_TEST samples the solution at the initial time.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    a = np.pi / 4.0
    d = np.pi / 2.0

    print('')
    print('UVWP_ETHIER_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  UVWP_ETHIER evaluates the Ethier solution.')
    print('  Estimate the range of velocity and pressure')
    print('  at the initial time T = 0, using a region that is')
    print('  the cube centered at (0,0,0) with "radius" 1.0,')
    print('  Parameter A = %g' % (a))
    print('  Parameter D = %g' % (d))

    n = 1000
    x_lo = -1.0
    x_hi = +1.0
    seed = 123456789
    x, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    y, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    z, seed = r8vec_uniform_ab(n, x_lo, x_hi, seed)
    t = np.zeros(n)
    u, v, w, p = uvwp_ethier(a, d, n, x, y, z, t)

    print('')
    print('           Minimum       Maximum')
    print('')
    print('  U:  %14.6g  %14.6g' % (np.min(u), np.max(u)))
    print('  V:  %14.6g  %14.6g' % (np.min(v), np.max(v)))
    print('  W:  %14.6g  %14.6g' % (np.min(w), np.max(w)))
    print('  P:  %14.6g  %14.6g' % (np.min(p), np.max(p)))
    print('')
    print('UVWP_ETHIER_TEST:')
    print('  Normal end of execution.')


def ns3de_test():

    # *****************************************************************************80
    #
    # NS3DE_TEST tests the NS3DE library.
    #
    #  Location:
    #
    #    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_3d_exact/ns3de_test.py
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('NS3DE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the NS3DE library.')

    #  Libraries.
    uvwp_burgers_test()
    resid_burgers_test()
    uvwp_ethier_test()
    resid_ethier_test()

    print('')
    print('NS3DE_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    ns3de_test()
    timestamp()
