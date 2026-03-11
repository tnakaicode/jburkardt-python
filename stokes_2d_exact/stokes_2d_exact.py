#! /usr/bin/env python3
#
def stokes_2d_exact_test ( ):

#*****************************************************************************80
#
## stokes_2d_exact_test() tests stokes_2d_exact().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'stokes_2d_exact_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test stokes_2d_exact().' )
 
  rng = default_rng ( )

  grid_2d_test ( )

  uvp_stokes1_test ( rng )
  rhs_stokes1_test ( rng )
  resid_stokes1_test ( rng )
  stokes1_gnuplot_test ( )
  stokes1_matplotlib_test ( )

  uvp_stokes2_test ( rng )
  rhs_stokes2_test ( rng )
  resid_stokes2_test ( rng )
  stokes2_gnuplot_test ( )
  stokes2_matplotlib_test ( )

  uvp_stokes3_test ( rng )
  rhs_stokes3_test ( rng )
  resid_stokes3_test ( rng )
  stokes3_gnuplot_test ( )
  stokes3_matplotlib_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'stokes_2d_exact_test():' )
  print ( '  Normal end of execution.' )
  return
def grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi ):

#*****************************************************************************80
#
## grid_2d() returns a regular 2D grid.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer X_NUM, the number of X values to use.
#
#    real X_LO, X_HI, the range of X values.
#
#    integer Y_NUM, the number of Y values to use.
#
#    real Y_LO, Y_HI, the range of Y values.
#
#  Output:
#
#    real X(X_NUM*Y_NUM), Y(X_NUM*Y_NUM), the coordinates of the grid.
#
  import numpy as np

  x = np.zeros ( x_num * y_num )
  y = np.zeros ( x_num * y_num )

  if ( x_num == 1 ):
    xi = ( x_lo + x_hi ) / 2.0
    k = 0
    for j in range ( 0, y_num ):
      for i in range ( 0, x_num ):
        x[k] = xi
        k = k + 1
  else:
    k = 0
    for j in range ( 0, y_num ):
      for i in range ( 0, x_num ):
        xi = ( float ( x_num - i - 1 ) * x_lo   \
             + float (         i     ) * x_hi ) \
             / float ( x_num     - 1 )
        x[k] = xi
        k = k + 1

  if ( y_num == 1 ):
    yj = ( y_lo + y_hi ) / 2.0
    k = 0
    for j in range ( 0, y_num ):
      for i in range ( 0, x_num ):
        y[k] = yj
        k = k + 1
  else:
    k = 0
    for j in range ( 0, y_num ):
      yj = ( float ( y_num - j - 1 ) * y_lo   \
           + float (         j     ) * y_hi ) \
           / float ( y_num     - 1 )
      for i in range ( 0, x_num ):
        y[k] = yj
        k = k + 1

  return x, y

def grid_2d_test ( ):

#*****************************************************************************80
#
## grid_2d_test() tests grid_2d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'grid_2d_test():' )
  print ( '  grid_2d() generates a regular grid.' )

  x_lo = 10.0
  x_hi = 20.0
  x_num = 5

  y_lo = 5.0
  y_hi = 6.0
  y_num = 3

  x, y = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  print ( '' )
  k = 0
  for j in range ( 0, y_num ):
    for i in range ( 0, x_num):
      print ( '  %2d  %2d  %2d  %14.6f  %14.6f' % ( k, i, j, x[k], y[k] ) )
      k = k + 1

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

def resid_stokes1 ( n, x, y ):

#*****************************************************************************80
#
## resid_stokes1() returns residuals of the exact Stokes solution #1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N, the number of points at which the solution is to
#    be evaluated.
#
#    real X(N), Y(N), the coordinates of the points.
#
#  Output:
#
#    real UR(N), VR(N), PR(N), the residuals in the U,
#    V and P equations.
#
  import numpy as np

  ur = np.zeros ( n )
  vr = np.zeros ( n )
  pr = np.zeros ( n )

  f, g, h = rhs_stokes1 ( n, x, y )

  u = - 2.0 * x ** 2 * ( x - 1.0 ) ** 2 * y * ( y - 1.0 ) * ( 2.0 * y - 1.0 )

  ux = - 2.0 * ( 4.0 * x ** 3 - 6.0 * x ** 2  \
       + 2.0 * x ) * y * ( y - 1.0 ) * ( 2.0 * y - 1.0 )

  uxx = - 2.0 * ( 12.0 * x ** 2 - 12.0 * x + 2.0 ) \
        * ( 2.0 * y ** 3 - 3.0 * y ** 2 + y )

  uy = - 2.0 * x ** 2 * ( x - 1.0 ) ** 2 * ( 6.0 * y ** 2 - 3.0 * y + 1.0 )

  uyy = - 2.0 * ( x ** 4 - 2.0 * x ** 3 + x ** 2 ) * ( 12.0 * y - 6.0 )

  v =   2.0 * x * ( x - 1.0 ) * ( 2.0 * x - 1.0 ) * y ** 2 * ( y - 1.0 ) ** 2

  vx =   2.0 * ( 6.0 * x ** 2 - 6.0 * x + 1.0 ) * y ** 2 * ( y - 1.0 ) ** 2

  vxx =   2.0 * ( 12.0 * x - 6.0 ) * y ** 2 * ( y - 1.0 ) ** 2

  vy =   2.0 * x * ( x - 1.0 ) * ( 2.0 * x - 1.0 ) \
         * ( 4.0 * y ** 3 - 6.0 * y ** 2 + 2.0 * y )

  vyy =   2.0 * x * ( x - 1.0 ) * ( 2.0 * x - 1.0 ) \
          * ( 12.0 * y ** 2 - 12.0 * y + 2.0 )

  p = 0.0
  px = 0.0
  py = 0.0

  ur = px - ( uxx + uyy ) - f
  vr = py - ( vxx + vyy ) - g
  pr = ux + vy - h

  return ur, vr, pr

def resid_stokes1_test ( rng ):

#*****************************************************************************80
#
## resid_stokes1_test() samples the residuals.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
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

  print ( '' )
  print ( 'resid_stokes1_test():' )
  print ( '  Exact Stokes solution #1.' )
  print ( '  Sample the Stokes residuals.' )

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )

  ur, vr, pr = resid_stokes1 ( n, x, y )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  Ur:  %14.6g  %14.6g' % ( np.min ( np.abs ( ur ) ), np.max ( np.abs ( ur ) ) ) )
  print ( '  Vr:  %14.6g  %14.6g' % ( np.min ( np.abs ( vr ) ), np.max ( np.abs ( vr ) ) ) )
  print ( '  Pr:  %14.6g  %14.6g' % ( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) ) )

  return

def resid_stokes2 ( n, x, y ):

#*****************************************************************************80
#
## resid_stokes2() returns residuals of the exact Stokes solution #2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N, the number of points at which the solution is to
#    be evaluated.
#
#    real X(N), Y(N), the coordinates of the points.
#
#  Output:
#
#    real UR(N), VR(N), PR(N), the residuals in the U,
#    V and P equations.
#
  import numpy as np

  ur = np.zeros ( n )
  vr = np.zeros ( n )
  pr = np.zeros ( n )

  f, g, h = rhs_stokes2 ( n, x, y )

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

  ur = px - ( uxx + uyy ) - f
  vr = py - ( vxx + vyy ) - g
  pr = ux + vy - h

  return ur, vr, pr

def resid_stokes2_test ( rng ):

#*****************************************************************************80
#
## resid_stokes2_test() samples the residuals.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
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

  print ( '' )
  print ( 'resid_stokes2_test():' )
  print ( '  Exact Stokes solution #2.' )
  print ( '  Sample the Stokes residuals.' )

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )

  ur, vr, pr = resid_stokes2 ( n, x, y )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  Ur:  %14.6g  %14.6g' % ( np.min ( np.abs ( ur ) ), np.max ( np.abs ( ur ) ) ) )
  print ( '  Vr:  %14.6g  %14.6g' % ( np.min ( np.abs ( vr ) ), np.max ( np.abs ( vr ) ) ) )
  print ( '  Pr:  %14.6g  %14.6g' % ( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) ) )

  return

def resid_stokes3 ( n, x, y ):

#*****************************************************************************80
#
## resid_stokes3() returns residuals of the exact Stokes solution #3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Howard Elman, Alison Ramage, David Silvester,
#    Finite Elements and Fast Iterative Solvers with
#    Applications in Incompressible Fluid Dynamics,
#    Oxford, 2005,
#    ISBN: 978-0198528678,
#    LC: QA911.E39.
#
#  Input:
#
#    integer N, the number of points at which the solution is to
#    be evaluated.
#
#    real X(N), Y(N), the coordinates of the points.
#
#  Output:
#
#    real UR(N), VR(N), PR(N), the residuals in the U,
#    V and P equations.
#
  import numpy as np

  ur = np.zeros ( n )
  vr = np.zeros ( n )
  pr = np.zeros ( n )

  f, g, h = rhs_stokes3 ( n, x, y )

  u =   20.0 * x * y ** 3
  ux = 20.0 * y ** 3
  uxx = 0.0
  uy = 60.0 * x * y ** 2
  uyy = 120.0 * x * y

  v = 5.0 * ( x ** 4 - y ** 4 )
  vx = 20.0 * x ** 3
  vxx = 60.0 * x ** 2
  vy = - 20.0 * y ** 3
  vyy = - 60.0 * y ** 2

  p =   60.0 * x ** 2 * y - 20.0 * y ** 3 + 10.0
  px = 120.0 * x * y
  py =  60.0 * x ** 2 - 60.0 * y ** 2

  ur = px - ( uxx + uyy ) - f
  vr = py - ( vxx + vyy ) - g
  pr = ux + vy - h

  return ur, vr, pr

def resid_stokes3_test ( rng ):

#*****************************************************************************80
#
## resid_stokes3_test() samples the residuals.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
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

  print ( '' )
  print ( 'resid_stokes3_test():' )
  print ( '  Exact Stokes solution #3.' )
  print ( '  Sample the Stokes residuals.' )

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )

  ur, vr, pr = resid_stokes3 ( n, x, y )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  Ur:  %14.6g  %14.6g' % ( np.min ( np.abs ( ur ) ), np.max ( np.abs ( ur ) ) ) )
  print ( '  Vr:  %14.6g  %14.6g' % ( np.min ( np.abs ( vr ) ), np.max ( np.abs ( vr ) ) ) )
  print ( '  Pr:  %14.6g  %14.6g' % ( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) ) )

  return

def rhs_stokes1 ( n, x, y ):

#*****************************************************************************80
#
## rhs_stokes1() returns the right hand sides of the exact Stokes solution #1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N, the number of points at which the solution is to
#    be evaluated.
#
#    real X(N), Y(N), the coordinates of the points.
#
#  Output:
#
#    real F(N), G(N), H(N), the right hand sides in the U,
#    V and P equations.
#
  import numpy as np

  f = np.zeros ( n )
  g = np.zeros ( n )
  h = np.zeros ( n )

  f = + 2.0 \
          * ( 12.0 * x ** 2 - 12.0 * x + 2.0 ) \
          * ( 2.0 * y ** 3 - 3.0 * y ** 2 + y ) \
          + 2.0 \
          * ( x ** 4 - 2.0 * x ** 3 + x ** 2 ) \
          * ( 12.0 * y - 6.0 )

  g = - 2.0 \
          * ( 12.0 * x - 6.0 ) \
          * ( y ** 4 - 2.0 * y ** 3 + y ** 2 ) \
          - 2.0 \
          * ( 2.0 * x ** 3 - 3.0 * x ** 2 + x ) \
          * ( 12.0 * y ** 2 - 12.0 * y + 2.0 )

  return f, g, h

def rhs_stokes1_test ( rng ):

#*****************************************************************************80
#
## rhs_stokes1_test() samples the right hand sides.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
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

  print ( '' )
  print ( 'rhs_stokes1_test():' )
  print ( '  Exact Stokes solution #1.' )
  print ( '  Estimate the range of the right hand side functions' )
  print ( '  using a region that is the unit square.' )

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )

  f, g, h = rhs_stokes1 ( n, x, y )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  U:  %14.6g  %14.6g' % ( np.min ( f ), np.max ( f ) ) )
  print ( '  V:  %14.6g  %14.6g' % ( np.min ( g ), np.max ( g ) ) )
  print ( '  P:  %14.6g  %14.6g' % ( np.min ( h ), np.max ( h ) ) )

  return

def rhs_stokes2 ( n, x, y ):

#*****************************************************************************80
#
## rhs_stokes2() returns the right hand sides of the exact Stokes solution #2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N, the number of points at which the solution is to
#    be evaluated.
#
#    real X(N), Y(N), the coordinates of the points.
#
#  Output:
#
#    real F(N), G(N), H(N), the right hand sides in the U,
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

def rhs_stokes2_test ( rng ):

#*****************************************************************************80
#
## rhs_stokes2_test() samples the right hand sides.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
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

  print ( '' )
  print ( 'rhs_stokes2_test():' )
  print ( '  Exact Stokes solution #2.' )
  print ( '  Estimate the range of the right hand side functions' )
  print ( '  using a region that is the unit square.' )

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )

  f, g, h = rhs_stokes2 ( n, x, y )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  U:  %14.6g  %14.6g' % ( np.min ( f ), np.max ( f ) ) )
  print ( '  V:  %14.6g  %14.6g' % ( np.min ( g ), np.max ( g ) ) )
  print ( '  P:  %14.6g  %14.6g' % ( np.min ( h ), np.max ( h ) ) )

  return

def rhs_stokes3 ( n, x, y ):

#*****************************************************************************80
#
## rhs_stokes3() returns the right hand sides of the exact Stokes solution #3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Howard Elman, Alison Ramage, David Silvester,
#    Finite Elements and Fast Iterative Solvers with
#    Applications in Incompressible Fluid Dynamics,
#    Oxford, 2005,
#    ISBN: 978-0198528678,
#    LC: QA911.E39.
#
#  Input:
#
#    integer N, the number of points at which the solution is to
#    be evaluated.
#
#    real X(N), Y(N), the coordinates of the points.
#
#  Output:
#
#    real F(N), G(N), H(N), the right hand sides in the U,
#    V and P equations.
#
  import numpy as np

  f = np.zeros ( n )
  g = np.zeros ( n )
  h = np.zeros ( n )

  return f, g, h

def rhs_stokes3_test ( rng ):

#*****************************************************************************80
#
## rhs_stokes3_test() samples the right hand sides.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
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

  print ( '' )
  print ( 'rhs_stokes3_test():' )
  print ( '  Exact Stokes solution #3.' )
  print ( '  Estimate the range of the right hand side functions' )
  print ( '  using a region that is [-1,+1]x[-1,+1].' )

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )

  f, g, h = rhs_stokes3 ( n, x, y )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  U:  %14.6g  %14.6g' % ( np.min ( f ), np.max ( f ) ) )
  print ( '  V:  %14.6g  %14.6g' % ( np.min ( g ), np.max ( g ) ) )
  print ( '  P:  %14.6g  %14.6g' % ( np.min ( h ), np.max ( h ) ) )

  return

def stokes_gnuplot ( header, n, x, y, u, v, s ):

#*****************************************************************************80
#
## stokes_gnuplot() writes the Stokes velocity vector field to files for GNUPLOT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string HEADER, a header to be used to name the files.
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the coordinates of the evaluation points.
#
#    real U(N), V(N), the velocity components.
#
#    real S, a scale factor for the velocity vectors.
#

#
#  Write the data file.
#
  data_filename = header + '_data.txt'

  data_unit = open ( data_filename, 'w' )

  for i in range ( 0, n ):
    st = '  %g' % ( x[i] )
    data_unit.write ( st )
    st = '  %g' % ( y[i] )
    data_unit.write ( st )
    st = '  %g' % ( s * u[i] )
    data_unit.write ( st )
    st = '  %g' % ( s * v[i] )
    data_unit.write ( st )
    data_unit.write ( '\n' );

  data_unit.close ( )

  print ( '' )
  print ( '  Data written to "%s".' % ( data_filename ) )
#
#  Write the command file.
#
  command_filename = header + '_commands.txt'
  plot_filename = header + '.png'

  command_unit = open ( command_filename, 'w' )

  command_unit.write ( '#  %s\n' % ( command_filename ) )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set term png\n' )
  command_unit.write ( 'set output "%s"\n' % ( plot_filename ) )
  command_unit.write ( '#\n' )
  command_unit.write ( '#  Add titles and labels.\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set xlabel "<--- X --->"\n' )
  command_unit.write ( 'set ylabel "<--- Y --->"\n' )
  command_unit.write ( 'set title "Stokes velocity field"\n' )
  command_unit.write ( 'unset key\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( '#  Add grid lines.\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set grid\n' )
  command_unit.write ( 'set size ratio -1\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( '#  Timestamp the plot.\n' )
  command_unit.write ( '#\n' )
  command_unit.write ( 'set timestamp\n' )
  command_unit.write ( 'plot "%s" using 1:2:3:4 with vectors \\\n' % ( data_filename ) )
  command_unit.write ( '  head filled lt 2 linecolor rgb "blue"\n' )
  command_unit.write ( 'quit\n' )

  data_unit.close ( )

  print ( '  Commands written to "%s".' % ( command_filename ) )

  return

def stokes1_gnuplot_test ( ):

#*****************************************************************************80
#
## stokes1_gnuplot_test() generates a field on a regular grid and plots it.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'stokes1_gnuplot_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Exact solution #1.' )
  print ( '  Generate a Stokes velocity field on a regular grid.' )
  print ( '  Store in GNUPLOT data and command files.' )

  x_lo = 0.0
  x_hi = 1.0
  x_num = 21

  y_lo = 0.0
  y_hi = 1.0
  y_num = 21

  x, y = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num
 
  u, v, p = uvp_stokes1 ( n, x, y )

  header = 'stokes1'
  s = 4.0
  stokes_gnuplot ( header, n, x, y, u, v, s )

  return

def stokes2_gnuplot_test ( ):

#*****************************************************************************80
#
## stokes2_gnuplot_test() generates a field on a regular grid and plots it.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'stokes2_gnuplot_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Exact solution #2.' )
  print ( '  Generate a Stokes velocity field on a regular grid.' )
  print ( '  Store in GNUPLOT data and command files.' )

  x_lo = 0.0
  x_hi = 1.0
  x_num = 21

  y_lo = 0.0
  y_hi = 1.0
  y_num = 21

  x, y = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num

  u, v, p = uvp_stokes2 ( n, x, y )

  header = 'stokes2'
  s = 0.05
  stokes_gnuplot ( header, n, x, y, u, v, s )

  return

def stokes3_gnuplot_test ( ):

#*****************************************************************************80
#
## stokes3_gnuplot_test() generates a field on a regular grid and plots it.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'stokes3_gnuplot_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Exact solution #3.' )
  print ( '  Generate a Stokes velocity field on a regular grid.' )
  print ( '  Store in GNUPLOT data and command files.' )

  x_lo = -1.0
  x_hi = +1.0
  x_num = 21

  y_lo = -1.0
  y_hi = +1.0
  y_num = 21

  x, y = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num
 
  u, v, p = uvp_stokes3 ( n, x, y )

  header = 'stokes3'
  s = 0.05
  stokes_gnuplot ( header, n, x, y, u, v, s )

  return

def stokes_matplotlib ( header, n, x, y, u, v, s ):

#*****************************************************************************80
#
## stokes_matplotlib() plots the Stokes velocity vector field with MATPLOTLIB.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string HEADER, a header to be used to name the files.
#
#    integer N, the number of evaluation points.
#
#    real X(N), Y(N), the coordinates of the evaluation points.
#
#    real U(N), V(N), the velocity components.
#
#    real S, a scale factor for the velocity vectors.
#
  import matplotlib.pyplot as plt

  myplot = plt.figure ( )
  ax = plt.gca ( )
  ax.quiver ( x, y, u, v )
  ax.set_xlabel ( '<--X-->' )
  ax.set_ylabel ( '<--Y-->' )
  ax.set_title ( header )
  ax.axis ( 'equal' )
  plt.draw ( )
  plot_filename = header + '_matplotlib.png'
  myplot.savefig ( plot_filename )
  plt.show ( block = False )
  plt.close ( )

  return

def stokes1_matplotlib_test ( ):

#*****************************************************************************80
#
## stokes1_matplotlib_test() generates a field on a regular grid and plots it.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'stokes1_matplotlib_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Exact flow #1.' )
  print ( '  Generate a Stokes velocity field on a regular grid.' )
  print ( '  Display it using MATPLOTLIB' )

  x_lo = 0.0
  x_hi = 1.0
  x_num = 21

  y_lo = 0.0
  y_hi = 1.0
  y_num = 21

  x, y = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num
 
  u, v, p = uvp_stokes1 ( n, x, y )

  header = 'stokes1'
  s = 4.0
  stokes_matplotlib ( header, n, x, y, u, v, s )

  return

def stokes2_matplotlib_test ( ):

#*****************************************************************************80
#
## stokes2_matplotlib_test() generates a field on a regular grid and plots it.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'stokes2_matplotlib_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Exact flow #2.' )
  print ( '  Generate a Stokes velocity field on a regular grid.' )
  print ( '  Display it using MATPLOTLIB' )

  x_lo = 0.0
  x_hi = 1.0
  x_num = 21

  y_lo = 0.0
  y_hi = 1.0
  y_num = 21

  x, y = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num
 
  u, v, p = uvp_stokes2 ( n, x, y )

  header = 'stokes2'
  s = 0.05
  stokes_matplotlib ( header, n, x, y, u, v, s )

  return

def stokes3_matplotlib_test ( ):

#*****************************************************************************80
#
## stokes3_matplotlib_test() generates a field on a regular grid and plots it.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'stokes3_matplotlib_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Exact flow #3.' )
  print ( '  Generate a Stokes velocity field on a regular grid.' )
  print ( '  Display it using MATPLOTLIB' )

  x_lo = -1.0
  x_hi = +1.0
  x_num = 21

  y_lo = -1.0
  y_hi = +1.0
  y_num = 21

  x, y = grid_2d ( x_num, x_lo, x_hi, y_num, y_lo, y_hi )

  n = x_num * y_num
 
  u, v, p = uvp_stokes3 ( n, x, y )

  header = 'stokes3'
  s = 0.05
  stokes_matplotlib ( header, n, x, y, u, v, s )

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

def uvp_stokes1 ( n, x, y ):

#*****************************************************************************80
#
## uvp_stokes1() evaluates the exact Stokes solution #1.
#
#  Discussion:
#
#    The solution is defined over the unit square [0,1]x[0,1].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N, the number of points at which the solution is to
#    be evaluated.
#
#    real X(N), Y(N), the coordinates of the points.
#
#  Output:
#
#    real U(N), V(N), P(N), the velocity components and
#    pressure at each of the points.
#
  import numpy as np

  u = np.zeros ( n )
  v = np.zeros ( n )
  p = np.zeros ( n )

  u = - 2.0 * x ** 2 * ( x - 1.0 ) ** 2 * y * ( y - 1.0 ) * ( 2.0 * y - 1.0 )

  v =   2.0 * x * ( x - 1.0 ) * ( 2.0 * x - 1.0 ) * y ** 2 * ( y - 1.0 ) ** 2

  return u, v, p

def uvp_stokes1_test ( rng ):

#*****************************************************************************80
#
## uvp_stokes1_test() samples the solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
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

  print ( '' )
  print ( 'uvp_stokes1_test():' )
  print ( '  Exact Stokes solution #1.' )
  print ( '  Estimate the range of velocity and pressure' )
  print ( '  using a region that is the unit square.' )

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )

  u, v, p = uvp_stokes1 ( n, x, y )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) ) )
  print ( '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) ) )
  print ( '  P:  %14.6g  %14.6g' % ( np.min ( p ), np.max ( p ) ) )

  return

def uvp_stokes2 ( n, x, y ):

#*****************************************************************************80
#
## uvp_stokes2() evaluates the exact Stokes solution #2.
#
#  Discussion:
#
#    The solution is defined over the unit square [0,1]x[0,1].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer N, the number of points at which the solution is to
#    be evaluated.
#
#    real X(N), Y(N), the coordinates of the points.
#
#  Output:
#
#    real U(N), V(N), P(N), the velocity components and
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

def uvp_stokes2_test ( rng ):

#*****************************************************************************80
#
## uvp_stokes2_test() samples the solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 January 2015
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

  print ( '' )
  print ( 'uvp_stokes2_test():' )
  print ( '  Exact Stokes solution #2.' )
  print ( '  Estimate the range of velocity and pressure' )
  print ( '  using a region that is the unit square.' )

  n = 1000
  x_lo = 0.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )

  u, v, p = uvp_stokes2 ( n, x, y )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) ) )
  print ( '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) ) )
  print ( '  P:  %14.6g  %14.6g' % ( np.min ( p ), np.max ( p ) ) )

  return

def uvp_stokes3 ( n, x, y ):

#*****************************************************************************80
#
## uvp_stokes3() evaluates the exact Stokes solution #3.
#
#  Discussion:
#
#    The solution is defined over the unit square [-1,+1]x[-1,+1].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Howard Elman, Alison Ramage, David Silvester,
#    Finite Elements and Fast Iterative Solvers with
#    Applications in Incompressible Fluid Dynamics,
#    Oxford, 2005,
#    ISBN: 978-0198528678,
#    LC: QA911.E39.
#
#  Input:
#
#    integer N, the number of points at which the solution is to
#    be evaluated.
#
#    real X(N), Y(N), the coordinates of the points.
#
#  Output:
#
#    real U(N), V(N), P(N), the velocity components and
#    pressure at each of the points.
#
  import numpy as np

  u = np.zeros ( n )
  v = np.zeros ( n )
  p = np.zeros ( n )

  u =   20.0 * x * y ** 3
  v =    5.0 * ( x ** 4  - y ** 4 )
  p =   60.0 * x ** 2 * y - 2.0 * y ** 3 + 10.0

  return u, v, p

def uvp_stokes3_test ( rng ):

#*****************************************************************************80
#
## uvp_stokes3_test() samples the solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
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

  print ( '' )
  print ( 'uvp_stokes3_test():' )
  print ( '  Exact Stokes solution #3.' )
  print ( '  Estimate the range of velocity and pressure' )
  print ( '  using a region that is [-1,+1]x[-1,+1].' )

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  x = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )
  y = x_lo + ( x_hi - x_lo ) * rng.random ( size = n )

  u, v, p = uvp_stokes3 ( n, x, y )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) ) )
  print ( '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) ) )
  print ( '  P:  %14.6g  %14.6g' % ( np.min ( p ), np.max ( p ) ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  stokes_2d_exact_test ( )
  timestamp ( )

