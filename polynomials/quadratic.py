#! /usr/bin/env python3
#
def quadratic_b ( m ):

#*****************************************************************************80
#
## QUADRATIC_B returns the bounds in the quadratic problem.
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
#    Output, real L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l =  -99.99 * np.ones ( m )
  u = +100.00 * np.ones ( m )

  return l, u

def quadratic_f ( m, n, x ):

#*****************************************************************************80
#
## QUADRATIC_F returns the function in the quadratic problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 December 2016
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
#    Output, real VALUE(N), the value of the function at X.
#
  import numpy as np

  r = - 2.0

  value = - r * np.ones ( n )

  for i in range ( 0, m ):
    value = value + x[i,0:n] ** 2

  return value

def quadratic_m ( ):

#*****************************************************************************80
#
## QUADRATIC_M returns the number of variables in the quadratic problem.
#
#  Discussion
#
#    Actually, the function can be defined for any 1 <= M.
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

def quadratic_test ( ):

#*****************************************************************************80
#
## QUADRATIC_TEST uses sampling to estimate the range of the QUADRATIC polynomial.
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
  print ( 'QUADRATIC_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use N sample values of a polynomial over its domain to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = quadratic_m ( )
  l, u = quadratic_b ( m )
  print ( '  quadratic: [ -2, ? ]:' )

  seed = 123456789
  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x, seed = r8mat_uniform_abvec ( m, n, u, l, seed )
    f = quadratic_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'QUADRATIC_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  quadratic_test ( )
  timestamp ( )

