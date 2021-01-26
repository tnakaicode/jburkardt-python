#! /usr/bin/env python
#
def rhs_stokes2 ( n, x, y ):

#*****************************************************************************80
#
## RHS_STOKES2 returns the right hand sides of the exact Stokes solution #2.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/stokes_2d_exact/rhs_stokes2.py
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
#    Output, real F(N), G(N), H(N), the right hand sides in the U,
#    V and P equations.
#
  import numpy as np

  f = np.zeros ( n )
  g = np.zeros ( n )
  h = np.zeros ( n )

  u =     2.0              * np.sin ( 2.0 * np.pi * x ) * np.cos ( 2.0 * np.pi * y )
  ux =    4.0 * np.pi      * np.cos ( 2.0 * np.pi * x ) * np.cos ( 2.0 * np.pi * y )
  uxx = - 8.0 * np.pi ** 2 * np.sin ( 2.0 * np.pi * x ) * np.cos ( 2.0 * np.pi * y )
  uy =  - 4.0 * np.pi      * np.sin ( 2.0 * np.pi * x ) * np.sin ( 2.0 * np.pi * y )
  uyy = - 8.0 * np.pi ** 2 * np.sin ( 2.0 * np.pi * x ) * np.cos ( 2.0 * np.pi * y )

  v =   - 2.0              * np.cos ( 2.0 * np.pi * x ) * np.sin ( 2.0 * np.pi * y )
  vx =    4.0 * np.pi      * np.sin ( 2.0 * np.pi * x ) * np.sin ( 2.0 * np.pi * y )
  vxx =   8.0 * np.pi ** 2 * np.cos ( 2.0 * np.pi * x ) * np.sin ( 2.0 * np.pi * y )
  vy =  - 4.0 * np.pi      * np.cos ( 2.0 * np.pi * x ) * np.cos ( 2.0 * np.pi * y )
  vyy =   8.0 * np.pi ** 2 * np.cos ( 2.0 * np.pi * x ) * np.sin ( 2.0 * np.pi * y )

  p = x ** 2 + y ** 2
  px = 2.0 * x
  py = 2.0 * y

  f = px - ( uxx + uyy )
  g = py - ( vxx + vyy )
  h = ux + vy

  return f, g, h

def rhs_stokes2_test ( ):

#*****************************************************************************80
#
## RHS_STOKES2_TEST samples the right hand sides.
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
  print ( 'RHS_STOKES2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Exact Stokes solution #2.' )
  print ( '  Estimate the range of the right hand side functions' )
  print ( '  using a region that is the unit square.' )

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )

  f, g, h = rhs_stokes2 ( n, x, y )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  U:  %14.6g  %14.6g' % ( np.min ( f ), np.max ( f ) ) )
  print ( '  V:  %14.6g  %14.6g' % ( np.min ( g ), np.max ( g ) ) )
  print ( '  P:  %14.6g  %14.6g' % ( np.min ( h ), np.max ( h ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RHS_STOKES2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rhs_stokes2_test ( )
  timestamp ( )

