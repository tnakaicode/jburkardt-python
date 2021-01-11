#! /usr/bin/env python3
#
def reimer6_b ( m ):

#*****************************************************************************80
#
## REIMER6_B returns the bounds in the reimer6 problem.
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

  l = np.array ( [ -5.0, -5.0, -5.0, -5.0, -5.0, -5.0 ] )
  u = np.array ( [ +5.0, +5.0, +5.0, +5.0, +5.0, +5.0 ] )

  return l, u

def reimer6_f ( m, n, x ):

#*****************************************************************************80
#
## REIMER6_F returns the function in the reimer6 problem.
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
    - 1.0 \
    + 2.0 * x[0,0:n] ** 7 \
    - 2.0 * x[1,0:n] ** 7 \
    + 2.0 * x[2,0:n] ** 7 \
    - 2.0 * x[3,0:n] ** 7 \
    + 2.0 * x[4,0:n] ** 7 \
    - 2.0 * x[5,0:n] ** 7 )

  return value

def reimer6_m ( ):

#*****************************************************************************80
#
## REIMER6_M returns the number of variables in the reimer6 problem.
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

def reimer6_test ( ):

#*****************************************************************************80
#
## REIMER6_TEST uses sampling to estimate the range of the REIMER6 polynomial.
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
  print ( 'REIMER6_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use N sample values of a polynomial over its domain to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = reimer6_m ( )
  l, u = reimer6_b ( m )
  print ( '  reimer6: [-937501, +937499]' )

  seed = 123456789
  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x, seed = r8mat_uniform_abvec ( m, n, u, l, seed )
    f = reimer6_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'REIMER6_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  reimer6_test ( )
  timestamp ( )

