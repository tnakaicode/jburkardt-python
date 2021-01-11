#! /usr/bin/env python3
#
def virasoro_b ( m ):

#*****************************************************************************80
#
## VIRASORO_B returns the bounds in the virasoro problem.
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

  l = np.array ( [ -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0 ] )
  u = np.array ( [ +1.0, +1.0, +1.0, +1.0, +1.0, +1.0, +1.0, +1.0 ] )

  return l, u

def virasoro_f ( m, n, x ):

#*****************************************************************************80
#
## VIRASORO_F returns the function in the virasoro problem.
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
#    Input, real x[M,N), the points.
#
#    Output, integer VALUE(N), the value of the function at X.
#
  value = ( \
    - 2.0 * x[0,0:n]      * x[3,0:n] \
    + 2.0 * x[0,0:n]      * x[6,0:n] \
    - 2.0 * x[1,0:n]      * x[4,0:n] \
    + 2.0 * x[1,0:n]      * x[6,0:n] \
    - 2.0 * x[2,0:n]      * x[5,0:n] \
    + 2.0 * x[2,0:n]      * x[6,0:n] \
    + 2.0 * x[3,0:n]      * x[6,0:n] \
    + 2.0 * x[4,0:n]      * x[6,0:n] \
    + 8.0 * x[5,0:n]      * x[6,0:n] \
    - 6.0 * x[5,0:n]      * x[7,0:n] \
    + 8.0 * x[6,0:n] ** 2             \
    + 6.0 * x[6,0:n]      * x[7,0:n] \
    -       x[6,0:n] )

  return value

def virasoro_m ( ):

#*****************************************************************************80
#
## VIRASORO_M returns the number of variables in the virasoro problem.
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
  m = 8

  return m

def virasoro_test ( ):

#*****************************************************************************80
#
## VIRASORO_TEST uses sampling to estimate the range of the VIRASORO polynomial.
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
  print ( 'VIRASORO_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use N sample values of a polynomial over its domain to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = virasoro_m ( )
  l, u = virasoro_b ( m )
  print ( '  virasoro: [-29.0, +21.0]' )

  seed = 123456789
  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x, seed = r8mat_uniform_abvec ( m, n, u, l, seed )
    f = virasoro_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'VIRASORO_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  virasoro_test ( )
  timestamp ( )

