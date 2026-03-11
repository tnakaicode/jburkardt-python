#! /usr/bin/env python3
#
def resid_burgers ( nu, n, x, y, z, t ):

#*****************************************************************************80
#
## resid_burgers(): Burgers Navier Stokes residual.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    real NU, the viscosity.
#
#    integer N, the number of points at which the solution is to
#    be evaluated.
#
#    real X(N), Y(N), Z(N), the coordinates of the points.
#
#    real T(N), the time coordinates.
#
#  Output:
#
#    real UR(N), VR(N), WR(N), PR(N), the residuals.
#
  import numpy as np
  from scipy.special import erf
#
#  Form the functions and derivatives.
#
  u =   2.0 * x
  ux =  2.0 * np.ones ( n )
  uxx = np.zeros ( n )
  uy =  np.zeros ( n )
  uyy = np.zeros ( n )
  uz =  np.zeros ( n )
  uzz = np.zeros ( n )
  ut =  np.zeros ( n )

  v =   - 2.0 * y
  vx =  np.zeros ( n )
  vxx = np.zeros ( n )
  vy =  - 2.0 * np.ones ( n )
  vyy = np.zeros ( n )
  vz =  np.zeros ( n )
  vzz = np.zeros ( n )
  vt =  np.zeros ( n )

  w = np.zeros ( n )
  for i in range ( 0, n ):
    w[i] = erf ( y[i] / np.sqrt ( nu ) )
  wx =  np.zeros ( n )
  wxx = np.zeros ( n )
  wy =    2.0 * np.sqrt ( 1.0 / nu / np.pi )     * np.exp ( - y ** 2 / nu )
  wyy = - 4.0 * np.sqrt ( 1.0 / nu / np.pi ) * y * np.exp ( - y ** 2 / nu ) / nu
  wz =  np.zeros ( n )
  wzz = np.zeros ( n )
  wt =  np.zeros ( n )

  p = - 2.0 * ( x ** 2 + y ** 2 )
  px = - 4.0 * x
  py = - 4.0 * y
  pz = np.zeros ( n )
#
#  Evaluate the residuals.
#
  ur = ut + u * ux + v * uy + w * uz + px - nu * ( uxx + uyy + uzz )
  vr = vt + u * vx + v * vy + w * vz + py - nu * ( vxx + vyy + vzz )
  wr = wt + u * wx + v * wy + w * wz + pz - nu * ( wxx + wyy + wzz )
  pr = ux + vy + wz

  return ur, vr, wr, pr

def resid_burgers_test ( rng ):

#*****************************************************************************80
#
## resid_burgers_test() samples the Burgers residual at the initial time.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  nu = 0.25

  print ( '' )
  print ( 'resid_burgers_test():' )
  print ( '  resid_burgers() evaluates the Burgers residual.' )
  print ( '  Sample at the initial time T = 0, using a region that is' )
  print ( '  the cube centered at (0,0,0) with "radius" 1.0,' )
  print ( '  Viscosity NU = %g' % ( nu ) )

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  z = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  t = np.zeros ( n )

  ur, vr, wr, pr = resid_burgers ( nu, n, x, y, z, t )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  Ur:  %14.6g  %14.6g' % ( np.min ( np.abs ( ur ) ), np.max ( np.abs ( ur ) ) ) )
  print ( '  Vr:  %14.6g  %14.6g' % ( np.min ( np.abs ( vr ) ), np.max ( np.abs ( vr ) ) ) )
  print ( '  Wr:  %14.6g  %14.6g' % ( np.min ( np.abs ( wr ) ), np.max ( np.abs ( wr ) ) ) )
  print ( '  Pr:  %14.6g  %14.6g' % ( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) ) )

  return

def uvwp_burgers ( nu, n, x, y, z, t ):

#*****************************************************************************80
#
## uvwp_burgers() evaluates the Burgers solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    real NU, the kinematic viscosity.
#
#    integer N, the number of points at which the solution is to
#    be evaluated.
#
#    real X(N), Y(N), Z(N), the coordinates of the points.
#
#    real T(N), the time coordinates.
#
#  Output:
#
#    real U(N), V(N), W(N), P(N), the velocity components and
#    pressure at each of the points.
#
  import numpy as np
  from scipy.special import erf

  u =   2.0 * x
  v =   - 2.0 * y
  w = np.zeros ( n )
  for i in range ( 0, n ):
    w[i] = erf ( y[i] / np.sqrt ( nu ) )
  p = - 2.0 * ( x ** 2 + y ** 2 )

  return u, v, w, p

def uvwp_burgers_test ( rng ):

#*****************************************************************************80
#
## uvwp_burgers_test() samples the Burgers solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  nu = 0.25

  print ( '' )
  print ( 'uvwp_burgers_test():' )
  print ( '  uvwp_burgers() samples the Burgers solution.' )
  print ( '  Estimate the range of velocity and pressure' )
  print ( '  at the initial time T = 0, using a region that is' )
  print ( '  the cube centered at (0,0,0) with "radius" 1.0,' )
  print ( '  Viscosity NU = %g' % ( nu ) )

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  z = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  t = np.zeros ( n )

  u, v, w, p = uvwp_burgers ( nu, n, x, y, z, t )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) ) )
  print ( '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) ) )
  print ( '  W:  %14.6g  %14.6g' % ( np.min ( w ), np.max ( w ) ) )
  print ( '  P:  %14.6g  %14.6g' % ( np.min ( p ), np.max ( p ) ) )

  return

def resid_ethier ( a, d, n, x, y, z, t ):

#*****************************************************************************80
#
## resid_ethier() evaluates the Ethier residual.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    real A, D, the parameters.  Sample values are A = PI/4 and
#    D = PI/2.
#
#    integer N, the number of points at which the solution is to
#    be evaluated.
#
#    real X(N), Y(N), Z(N), the coordinates of the points.
#
#    real T(N), the time coordinates.
#
#  Output:
#
#    real UR(N), VR(N), WR(N), PR(N), the residuals.
#
  import numpy as np
#
#  Make some temporaries.
#
  ex = np.exp ( a * x )
  ey = np.exp ( a * y )
  ez = np.exp ( a * z )

  e2x = np.exp ( 2.0 * a * x )
  e2y = np.exp ( 2.0 * a * y )
  e2z = np.exp ( 2.0 * a * z )

  e2t = np.exp  ( -       d * d * t )
  e4t = np.exp  ( - 2.0 * d * d * t )

  exy = np.exp ( a * ( x + y ) )
  eyz = np.exp ( a * ( y + z ) )
  ezx = np.exp ( a * ( z + x ) )

  sxy = np.sin ( a * x + d * y )
  syz = np.sin ( a * y + d * z )
  szx = np.sin ( a * z + d * x )

  cxy = np.cos ( a * x + d * y )
  cyz = np.cos ( a * y + d * z )
  czx = np.cos ( a * z + d * x )
#
#  Form the functions and derivatives.
#
  u =   -         a * (           ex * syz +         ez * cxy ) * e2t
  ux =  -         a * (       a * ex * syz -     a * ez * sxy ) * e2t
  uxx = -         a * (   a * a * ex * syz - a * a * ez * cxy ) * e2t
  uy =  -         a * (       a * ex * cyz -     d * ez * sxy ) * e2t
  uyy = -         a * ( - a * a * ex * syz - d * d * ez * cxy ) * e2t
  uz =  -         a * (       d * ex * cyz +     a * ez * cxy ) * e2t
  uzz =  -        a * ( - d * d * ex * syz + a * a * ez * cxy ) * e2t
  ut =  + d * d * a * (           ex * syz +         ez * cxy ) * e2t

  v =   -         a * (           ey * szx +         ex * cyz ) * e2t
  vx =  -         a * (       d * ey * czx +     a * ex * cyz ) * e2t
  vxx = -         a * ( - d * d * ey * szx + a * a * ex * cyz ) * e2t
  vy =  -         a * (       a * ey * szx -     a * ex * syz ) * e2t
  vyy = -         a * (   a * a * ey * szx - a * a * ex * cyz ) * e2t
  vz =  -         a * (       a * ey * czx -     d * ex * syz ) * e2t
  vzz =  -        a * ( - a * a * ey * szx - d * d * ex * cyz ) * e2t
  vt =  + d * d * a * (           ey * szx +         ex * cyz ) * e2t

  w =   -         a * (           ez * sxy +         ey * czx ) * e2t
  wx =  -         a * (       a * ez * cxy -     d * ey * szx ) * e2t
  wxx = -         a * ( - a * a * ez * sxy - d * d * ey * czx ) * e2t
  wy =  -         a * (       d * ez * cxy +     a * ey * czx ) * e2t
  wyy = -         a * ( - d * d * ez * sxy + a * a * ey * czx ) * e2t
  wz =  -         a * (       a * ez * sxy -     a * ey * szx ) * e2t
  wzz = -         a * (   a * a * ez * sxy - a * a * ey * czx ) * e2t
  wt =  + d * d * a * (           ez * sxy +         ey * czx ) * e2t

  p = - 0.5 * a * a * e4t * ( \
    + e2x + 2.0 * sxy * czx * eyz \
    + e2y + 2.0 * syz * cxy * ezx \
    + e2z + 2.0 * szx * cyz * exy )

  px = - 0.5 * a * a * e4t * ( \
    + 2.0 * a * e2x + 2.0 * a * cxy * czx * eyz - 2.0 * d * sxy * szx * eyz \
                    - 2.0 * a * syz * sxy * ezx + 2.0 * a * syz * cxy * ezx \
                    + 2.0 * d * czx * cyz * exy + 2.0 * a * szx * cyz * exy )

  py = - 0.5 * a * a * e4t * ( \
                    + 2.0 * d * cxy * czx * eyz + 2.0 * a * sxy * czx * eyz \
    + 2.0 * a * e2y + 2.0 * a * cyz * cxy * ezx - 2.0 * d * syz * sxy * ezx \
                    - 2.0 * a * szx * syz * exy + 2.0 * a * szx * cyz * exy )

  pz = - 0.5 * a * a * e4t * ( \
                    - 2.0 * a * sxy * szx * eyz + 2.0 * a * sxy * czx * eyz \
                    + 2.0 * d * cyz * cxy * ezx + 2.0 * a * syz * cxy * ezx \
    + 2.0 * a * e2z + 2.0 * a * czx * cyz * exy - 2.0 * d * szx * syz * exy )
#
#  Evaluate the residuals.
#
  ur = ut + u * ux + v * uy + w * uz + px - ( uxx + uyy + uzz )
  vr = vt + u * vx + v * vy + w * vz + py - ( vxx + vyy + vzz )
  wr = wt + u * wx + v * wy + w * wz + pz - ( wxx + wyy + wzz )
  pr = ux + vy + wz;

  return ur, vr, wr, pr

def resid_ethier_test ( rng ):

#*****************************************************************************80
#
## resid_ethier_test() samples the Ethier residual.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  a = np.pi / 4.0
  d = np.pi / 2.0

  print ( '' )
  print ( 'resid_ethier_test():' )
  print ( '  resid_ethier() evaluates the Ethier residual.' )
  print ( '  Sample the residuals' )
  print ( '  at the initial time T = 0, using a region that is' )
  print ( '  the cube centered at (0,0,0) with "radius" 1.0,' )
  print ( '  Parameter A = %g' % ( a ) )
  print ( '  Parameter D = %g' % ( d ) )

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  z = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  t = np.zeros ( n )

  ur, vr, wr, pr = resid_ethier ( a, d, n, x, y, z, t )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  Ur:  %14.6g  %14.6g' % ( np.min ( np.abs ( ur ) ), np.max ( np.abs ( ur ) ) ) )
  print ( '  Vr:  %14.6g  %14.6g' % ( np.min ( np.abs ( vr ) ), np.max ( np.abs ( vr ) ) ) )
  print ( '  Wr:  %14.6g  %14.6g' % ( np.min ( np.abs ( wr ) ), np.max ( np.abs ( wr ) ) ) )
  print ( '  Pr:  %14.6g  %14.6g' % ( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) ) )

  return

def uvwp_ethier ( a, d, n, x, y, z, t ):

#*****************************************************************************80
#
## uvwp_ethier() evaluates the Ethier exact Navier Stokes solution.
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
#    This code is distributed under the MIT license.
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
#  Input:
#
#    real A, D, the parameters.  Sample values are A = PI/4 and
#    D = PI/2.
#
#    integer N, the number of points at which the solution is to
#    be evaluated.
#
#    real X(N), Y(N), Z(N), the coordinates of the points.
#
#    real T(N), the time coordinates.
#
#  Output:
#
#    real U(N), V(N), W(N), P(N), the velocity components and
#    pressure at each of the points.
#
  import numpy as np

  ex = np.exp ( a * x )
  ey = np.exp ( a * y )
  ez = np.exp ( a * z )

  e2t = np.exp  ( - d * d * t )

  exy = np.exp ( a * ( x + y ) )
  eyz = np.exp ( a * ( y + z ) )
  ezx = np.exp ( a * ( z + x ) )

  sxy = np.sin ( a * x + d * y )
  syz = np.sin ( a * y + d * z )
  szx = np.sin ( a * z + d * x )

  cxy = np.cos ( a * x + d * y )
  cyz = np.cos ( a * y + d * z )
  czx = np.cos ( a * z + d * x )

  u = - a * ( ex * syz + ez * cxy ) * e2t
  v = - a * ( ey * szx + ex * cyz ) * e2t
  w = - a * ( ez * sxy + ey * czx ) * e2t
  p = 0.5 * a * a * e2t * e2t * ( \
    + ex * ex + 2.0 * sxy * czx * eyz \
    + ey * ey + 2.0 * syz * cxy * ezx \
    + ez * ez + 2.0 * szx * cyz * exy )

  return u, v, w, p

def uvwp_ethier_test ( rng ):

#*****************************************************************************80
#
## uvwp_ethier_test() samples the solution at the initial time.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  a = np.pi / 4.0
  d = np.pi / 2.0

  print ( '' )
  print ( 'uvwp_ethier_test():' )
  print ( '  uvwp_ethier() evaluates the Ethier solution.' )
  print ( '  Estimate the range of velocity and pressure' )
  print ( '  at the initial time T = 0, using a region that is' )
  print ( '  the cube centered at (0,0,0) with "radius" 1.0,' )
  print ( '  Parameter A = %g' % ( a ) )
  print ( '  Parameter D = %g' % ( d ) )

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  z = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  t = np.zeros ( n )

  u, v, w, p = uvwp_ethier ( a, d, n, x, y, z, t )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) ) )
  print ( '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) ) )
  print ( '  W:  %14.6g  %14.6g' % ( np.min ( w ), np.max ( w ) ) )
  print ( '  P:  %14.6g  %14.6g' % ( np.min ( p ), np.max ( p ) ) )

  return

def navier_stokes_3d_exact_test ( ):

#*****************************************************************************80
#
## navier_stokes_3d_exact_test() tests navier_stokes_3d_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'navier_stokes_3d_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test navier_stokes_3d_exact()' )

  rng = default_rng ( )

  uvwp_burgers_test ( rng )
  resid_burgers_test ( rng )

  uvwp_ethier_test ( rng )
  resid_ethier_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'navier_stokes_3d_exact_test():' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  navier_stokes_3d_exact_test ( )
  timestamp ( )

