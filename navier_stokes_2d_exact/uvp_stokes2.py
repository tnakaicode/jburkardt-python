#! /usr/bin/env python
#
def uvp_stokes2 ( n, x, y ):

#*****************************************************************************80
#
## UVP_STOKES2 evaluates the exact Stokes solution #2.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/stokes_2d_exact/uvp_stokes2.py
#
#  Discussion:
#
#    The solution is defined over the unit square [0,1]x[0,1].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Junping Wang, Yanqiu Wang, Xiu Ye,
#    A robust numerical method for Stokes equations based on divergence-free
#    H(div) finite element methods,
#    SIAM Journal on Scientific Computing,
#    Volume 31, Number 4, 2009, pages 2784-2802.
#
#  Parameters:
#
#    Input, integer N, the number of points at which the solution is to
#    be evaluated.
#
#    Input, real X(N), Y(N), the coordinates of the points.
#
#    Output, real U(N), V(N), P(N), the velocity components and
#    pressure at each of the points.
#
  import numpy as np

  u = np.zeros ( n )
  v = np.zeros ( n )
  p = np.zeros ( n )

  u =   2.0 * np.sin ( 2 * np.pi * x ) * np.cos ( 2 * np.pi * y )

  v = - 2.0 * np.cos ( 2 * np.pi * x ) * np.sin ( 2 * np.pi * y )

  p = x ** 2 + y ** 2

  return u, v, p

def uvp_stokes2_test ( ):

#*****************************************************************************80
#
## UVP_STOKES2_TEST samples the solution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ( '' )
  print ( 'UVP_STOKES2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Exact Stokes solution #2.' )
  print ( '  Estimate the range of velocity and pressure' )
  print ( '  using a region that is the unit square.' )

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  u, v, p = uvp_stokes2 ( n, x, y )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) ) )
  print ( '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) ) )
  print ( '  P:  %14.6g  %14.6g' % ( np.min ( p ), np.max ( p ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'UVP_STOKES2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  uvp_stokes2_test ( )
  timestamp ( )

