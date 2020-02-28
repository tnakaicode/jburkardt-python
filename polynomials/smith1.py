#! /usr/bin/env python3
#
def smith1_b ( m ):

#*****************************************************************************80
#
## SMITH1_B returns the bounds in the smith1 problem.
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
#  Reference:
#
#    Andrew Smith,
#    Fast construction of constant bound functions for sparse polynomials,
#    Journal of Global Optimization,
#    Volume 43, 2009, pages 445-458.
#
#  Parameters:
#
#    Input, integer M, the number of variables.
#
#    Output, integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ +1.0, +2.0, +4.0, -5.0,  +2.0 ] )
  u = np.array ( [ +2.0, +3.0, +6.0, -2.0, +10.0 ] )

  return l, u

def smith1_f ( m, n, x ):

#*****************************************************************************80
#
## SMITH1_F returns the function in the smith1 problem.
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
#    Andrew Smith,
#    Fast construction of constant bound functions for sparse polynomials,
#    Journal of Global Optimization,
#    Volume 43, 2009, pages 445-458.
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
      3.0 * x[0,0:n] ** 2 * x[1,0:n] ** 3 * x[2,0:n] ** 4 \
    +       x[0,0:n] ** 3 * x[1,0:n]      * x[2,0:n] ** 3 \
    - 5.0 * x[0,0:n]      * x[1,0:n]      * x[3,0:n] ** 5 \
    +       x[2,0:n]      * x[3,0:n]      * x[4,0:n] ** 3 )
 
  return value

def smith1_m ( ):

#*****************************************************************************80
#
## SMITH1_M returns the number of variables in the smith1 problem.
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
#    Andrew Smith,
#    Fast construction of constant bound functions for sparse polynomials,
#    Journal of Global Optimization,
#    Volume 43, 2009, pages 445-458.
#
#  Parameters:
#
#    Output, integer M, the number of variables.
#
  m = 5

  return m

def smith1_test ( ):

#*****************************************************************************80
#
## SMITH1_TEST uses sampling to estimate the range of the SMITH1 polynomial.
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
  print ( 'SMITH1_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use N sample values of a polynomial over its domain to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = smith1_m ( )
  l, u = smith1_b ( m )
  print ( '  smith1: [ ?, ? ]:' )

  seed = 123456789
  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x, seed = r8mat_uniform_abvec ( m, n, u, l, seed )
    f = smith1_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SMITH1_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  smith1_test ( )
  timestamp ( )

