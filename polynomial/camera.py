#! /usr/bin/env python3
#
def camera_b ( m ):

#*****************************************************************************80
#
## CAMERA_B returns the bounds in the camera problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Parameters:
#
#    Input, integer M, the number of variables.
#
#    Output, integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -100.0, -100.0, -100.0, -100.0, -100.0, -100.0 ] )
  u = np.array ( [ +100.0, +100.0, +100.0, +100.0, +100.0, +100.0 ] )

  return l, u

def camera_f ( m, n, x ):

#*****************************************************************************80
#
## CAMERA_F returns the function in the camera problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Parameters:
#
#    Input, integer M, the number of variables.
#
#    Input, integer N, the number of points.
#
#    Input, real X(M,N), the points.
#
#    Output, integer VALUE(N), the value of the function at X.
#
  value = ( \
    - 6.8 * x[0,0:n] * x[3,0:n] \
    - 3.2 * x[0,0:n] * x[4,0:n] \
    + 1.3 * x[0,0:n] * x[5,0:n] \
    + 5.1 * x[0,0:n]             \
    - 3.2 * x[1,0:n] * x[3,0:n] \
    - 4.8 * x[1,0:n] * x[4,0:n] \
    - 0.7 * x[1,0:n] * x[5,0:n] \
    - 7.1 * x[1,0:n]             \
    + 1.3 * x[2,0:n] * x[3,0:n] \
    - 0.7 * x[2,0:n] * x[4,0:n] \
    + 9.0 * x[2,0:n] * x[5,0:n] \
    -       x[2,0:n] \
    + 5.1 * x[3,0:n] \
    - 7.1 * x[4,0:n] \
    -       x[5,0:n] \
    + 2.6 )

  return value

def camera_m ( ):

#*****************************************************************************80
#
## CAMERA_M returns the number of variables in the camera problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Sashwati Ray, PSV Nataraj,
#    An efficient algorithm for range computation of polynomials using the
#    Bernstein form,
#    Journal of Global Optimization,
#    Volume 45, 2009, pages 403-426.
#
#  Parameters:
#
#    Output, integer M, the number of variables.
#
  m = 6

  return m

def camera_test ( ):

#*****************************************************************************80
#
## CAMERA_TEST uses sampling to estimate the range of the CAMERA polynomial.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8mat_uniform_abvec import r8mat_uniform_abvec

  print ( '' )
  print ( 'CAMERA_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use N sample values of a polynomial over its domain to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = camera_m ( )
  l, u = camera_b ( m )
  print ( '  camera: [-270397.4, +270202.6]' )

  seed = 123456789
  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x, seed = r8mat_uniform_abvec ( m, n, u, l, seed )
    f = camera_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CAMERA_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  camera_test ( )
  timestamp ( )

