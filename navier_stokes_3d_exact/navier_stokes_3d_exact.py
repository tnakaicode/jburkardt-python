#! /usr/bin/env python3
#


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
    import numpy as np
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
    import numpy as np
    import platform

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
#
#  Terminate.
#
    print('')
    print('RESID_BURGERS_TEST:')
    print('  Normal end of execution.')
    return


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
    import numpy as np

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
    import numpy as np
    import platform

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
#
#  Terminate.
#
    print('')
    print('UVWP_BURGERS_TEST:')
    print('  Normal end of execution.')
    return


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
    import numpy as np
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
#
#  Form the functions and derivatives.
#
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
#
#  Evaluate the residuals.
#
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
    import numpy as np
    import platform

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
#
#  Terminate.
#
    print('')
    print('RESID_ETHIER_TEST:')
    print('  Normal end of execution.')
    return


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
    import numpy as np

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
    import numpy as np
    import platform

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
#
#  Terminate.
#
    print('')
    print('UVWP_ETHIER_TEST:')
    print('  Normal end of execution.')
    return


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
    import platform

    print('')
    print('NS3DE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the NS3DE library.')
#
#  Utilities.
#
    r8_erf_test()
    r8vec_amax_test()
    r8vec_amin_test()
    r8vec_max_test()
    r8vec_min_test()
    r8vec_print_test()
    r8vec_uniform_ab_test()
#
#  Libraries.
#
    uvwp_burgers_test()
    resid_burgers_test()

    uvwp_ethier_test()
    resid_ethier_test()
#
#  Terminate.
#
    print('')
    print('NS3DE_TEST:')
    print('  Normal end of execution.')
    return


def r8_erf(x):

    # *****************************************************************************80
    #
    # R8_ERF evaluates the error function.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 February 2015
    #
    #  Author:
    #
    #    W J Cody,
    #    Mathematics and Computer Science Division,
    #    Argonne National Laboratory,
    #    Argonne, Illinois, 60439.
    #
    #  Reference:
    #
    #    W J Cody,
    #    "Rational Chebyshev approximations for the error function",
    #    Mathematics of Computation,
    #    1969, pages 631-638.
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the error function.
    #
    #    Output, real VALUE, the value of the error function.
    #
    import numpy as np

    a = np.array((
        3.16112374387056560E+00,
        1.13864154151050156E+02,
        3.77485237685302021E+02,
        3.20937758913846947E+03,
        1.85777706184603153E-01))
    b = np.array((
        2.36012909523441209E+01,
        2.44024637934444173E+02,
        1.28261652607737228E+03,
        2.84423683343917062E+03))
    c = np.array((
        5.64188496988670089E-01,
        8.88314979438837594E+00,
        6.61191906371416295E+01,
        2.98635138197400131E+02,
        8.81952221241769090E+02,
        1.71204761263407058E+03,
        2.05107837782607147E+03,
        1.23033935479799725E+03,
        2.15311535474403846E-08))
    d = np.array((
        1.57449261107098347E+01,
        1.17693950891312499E+02,
        5.37181101862009858E+02,
        1.62138957456669019E+03,
        3.29079923573345963E+03,
        4.36261909014324716E+03,
        3.43936767414372164E+03,
        1.23033935480374942E+03))
    p = np.array((
        3.05326634961232344E-01,
        3.60344899949804439E-01,
        1.25781726111229246E-01,
        1.60837851487422766E-02,
        6.58749161529837803E-04,
        1.63153871373020978E-02))
    q = np.array((
        2.56852019228982242E+00,
        1.87295284992346047E+00,
        5.27905102951428412E-01,
        6.05183413124413191E-02,
        2.33520497626869185E-03))
    sqrpi = 0.56418958354775628695E+00
    thresh = 0.46875E+00
    xbig = 26.543E+00
    xsmall = 1.11E-16

    xabs = abs(x)
#
#  Evaluate ERF(X) for |X| <= 0.46875.
#
    if (xabs <= thresh):

        if (xsmall < xabs):
            xsq = xabs * xabs
        else:
            xsq = 0.0

        xnum = a[4] * xsq
        xden = xsq
        for i in range(0, 3):
            xnum = (xnum + a[i]) * xsq
            xden = (xden + b[i]) * xsq

        value = x * (xnum + a[3]) / (xden + b[3])
#
#  Evaluate ERFC(X) for 0.46875 <= |X| <= 4.0.
#
    elif (xabs <= 4.0):

        xnum = c[8] * xabs
        xden = xabs
        for i in range(0, 7):
            xnum = (xnum + c[i]) * xabs
            xden = (xden + d[i]) * xabs

        value = (xnum + c[7]) / (xden + d[7])
        xsq = np.floor(xabs * 16.0) / 16.0
        delt = (xabs - xsq) * (xabs + xsq)
        value = np.exp(- xsq * xsq) * np.exp(- delt) * value

        value = (0.5 - value) + 0.5

        if (x < 0.0):
            value = -value
#
#  Evaluate ERFC(X) for 4.0 < |X|.
#
    else:

        if (xbig <= xabs):

            if (0.0 < x):
                value = 1.0
            else:
                value = -1.0

        else:

            xsq = 1.0 / (xabs * xabs)

            xnum = p[5] * xsq
            xden = xsq
            for i in range(0, 4):
                xnum = (xnum + p[i]) * xsq
                xden = (xden + q[i]) * xsq

            value = xsq * (xnum + p[4]) / (xden + q[4])
            value = (sqrpi - value) / xabs
            xsq = np.floor(xabs * 16.0) / 16.0
            delt = (xabs - xsq) * (xabs + xsq)
            value = np.exp(- xsq * xsq) * np.exp(- delt) * value

            value = (0.5 - value) + 0.5

            if (x < 0.0):
                value = -value

    return value


def erf_values(n_data):

    # *****************************************************************************80
    #
    # ERF_VALUES returns some values of the ERF or "error" function.
    #
    #  Discussion:
    #
    #    The error function is defined by:
    #
    #      ERF(X) = ( 2 / sqrt ( PI ) * integral ( 0 <= T <= X ) exp ( - T^2 ) dT
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      Erf[x]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 September 2004
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Milton Abramowitz, Irene Stegun,
    #    Handbook of Mathematical Functions,
    #    National Bureau of Standards, 1964,
    #    ISBN: 0-486-61272-4,
    #    LC: QA47.A34.
    #
    #    Stephen Wolfram,
    #    The Mathematica Book,
    #    Fourth Edition,
    #    Cambridge University Press, 1999,
    #    ISBN: 0-521-64314-7,
    #    LC: QA76.95.W65.
    #
    #  Parameters:
    #
    #    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
    #    first call.  On each call, the routine increments N_DATA by 1, and
    #    returns the corresponding data; when there is no more data, the
    #    output value of N_DATA will be 0 again.
    #
    #    Output, real X, the argument of the function.
    #
    #    Output, real FX, the value of the function.
    #
    import numpy as np

    n_max = 21

    fx_vec = np.array((
        0.0000000000000000E+00,
        0.1124629160182849E+00,
        0.2227025892104785E+00,
        0.3286267594591274E+00,
        0.4283923550466685E+00,
        0.5204998778130465E+00,
        0.6038560908479259E+00,
        0.6778011938374185E+00,
        0.7421009647076605E+00,
        0.7969082124228321E+00,
        0.8427007929497149E+00,
        0.8802050695740817E+00,
        0.9103139782296354E+00,
        0.9340079449406524E+00,
        0.9522851197626488E+00,
        0.9661051464753107E+00,
        0.9763483833446440E+00,
        0.9837904585907746E+00,
        0.9890905016357307E+00,
        0.9927904292352575E+00,
        0.9953222650189527E+00))

    x_vec = np.array((
        0.0E+00,
        0.1E+00,
        0.2E+00,
        0.3E+00,
        0.4E+00,
        0.5E+00,
        0.6E+00,
        0.7E+00,
        0.8E+00,
        0.9E+00,
        1.0E+00,
        1.1E+00,
        1.2E+00,
        1.3E+00,
        1.4E+00,
        1.5E+00,
        1.6E+00,
        1.7E+00,
        1.8E+00,
        1.9E+00,
        2.0E+00))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        x = 0.0
        fx = 0.0
    else:
        x = x_vec[n_data]
        fx = fx_vec[n_data]
        n_data = n_data + 1

    return n_data, x, fx


def r8_erf_test():

    # *****************************************************************************80
    #
    # R8_ERF_TEST tests R8_ERF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8_ERF_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_ERF evaluates the error function.')
    print('')
    print('      X            ERF(X)    R8_ERF(X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx1 = erf_values(n_data)

        if (n_data == 0):
            break

        fx2 = r8_erf(x)

        print('  %12g  %24.16g  %24.16g' % (x, fx1, fx2))
#
#  Terminate.
#
    print('')
    print('R8_ERF_TEST')
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


def r8vec_amax_test():

    # *****************************************************************************80
    #
    # R8VEC_AMAX_TEST tests R8VEC_AMAX.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8VEC_AMAX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_AMAX computes the maximum absolute value entry in an R8VEC.')

    n = 10
    a_lo = - 10.0
    a_hi = + 10.0
    seed = 123456789

    a, seed = r8vec_uniform_ab(n, a_lo, a_hi, seed)

    r8vec_print(n, a, '  Input vector:')

    value = r8vec_amax(n, a)
    print('')
    print('  Max Abs = %g' % (value))
#
#  Terminate.
#
    print('')
    print('R8VEC_AMAX_TEST:')
    print('  Normal end of execution.')
    return


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


def r8vec_amin_test():

    # *****************************************************************************80
    #
    # R8VEC_AMIN_TEST tests R8VEC_AMIN.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8VEC_AMIN_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_AMIN computes the minimum absolute entry in an R8VEC.')

    n = 10
    a_lo = - 10.0
    a_hi = + 10.0
    seed = 123456789

    a, seed = r8vec_uniform_ab(n, a_lo, a_hi, seed)

    r8vec_print(n, a, '  Input vector:')

    value = r8vec_amin(n, a)
    print('')
    print('  Min Abs = %g' % (value))
#
#  Terminate.
#
    print('')
    print('R8VEC_AMIN_TEST:')
    print('  Normal end of execution.')
    return


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


def r8vec_max_test():

    # *****************************************************************************80
    #
    # R8VEC_MAX_TEST tests R8VEC_MAX.
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
    import platform

    print('')
    print('R8VEC_MAX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_MAX computes the maximum entry in an R8VEC.')

    n = 10
    a_lo = - 10.0
    a_hi = + 10.0
    seed = 123456789

    a, seed = r8vec_uniform_ab(n, a_lo, a_hi, seed)

    r8vec_print(n, a, '  Input vector:')

    value = r8vec_max(n, a)
    print('')
    print('  Max = %g' % (value))
#
#  Terminate.
#
    print('')
    print('R8VEC_MAX_TEST:')
    print('  Normal end of execution.')
    return


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


def r8vec_min_test():

    # *****************************************************************************80
    #
    # R8VEC_MIN_TEST tests R8VEC_MIN.
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
    import platform

    print('')
    print('R8VEC_MIN_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_MIN computes the minimum entry in an R8VEC.')

    n = 10
    a_lo = - 10.0
    a_hi = + 10.0
    seed = 123456789

    a, seed = r8vec_uniform_ab(n, a_lo, a_hi, seed)

    r8vec_print(n, a, '  Input vector:')

    value = r8vec_min(n, a)
    print('')
    print('  Min = %g' % (value))
#
#  Terminate.
#
    print('')
    print('R8VEC_MIN_TEST:')
    print('  Normal end of execution.')
    return


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


def r8vec_print_test():

    # *****************************************************************************80
    #
    # R8VEC_PRINT_TEST tests R8VEC_PRINT.
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
    import numpy as np
    import platform

    print('')
    print('R8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_PRINT prints an R8VEC.')

    n = 4
    v = np.array([123.456, 0.000005, -1.0E+06, 3.14159265], dtype=np.float64)
    r8vec_print(n, v, '  Here is an R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


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


def r8vec_uniform_ab_test():

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_AB_TEST tests R8VEC_UNIFORM_AB.
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
    import numpy as np
    import platform

    n = 10
    a = -1.0
    b = +5.0
    seed = 123456789

    print('')
    print('R8VEC_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_UNIFORM_AB computes a random R8VEC.')
    print('')
    print('  %g <= X <= %g' % (a, b))
    print('  Initial seed is %d' % (seed))

    v, seed = r8vec_uniform_ab(n, a, b, seed)

    r8vec_print(n, v, '  Random R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_UNIFORM_AB_TEST:')
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


if (__name__ == '__main__'):
    timestamp()
    ns3de_test()
    timestamp()
