#! /usr/bin/env python3
#
def rosenbrock_b ( m ):

#*****************************************************************************80
#
## ROSENBROCK_B returns the bounds in the rosenbrock problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2016
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

  l =  -5.0 * np.ones ( m )
  u = +10.0 * np.ones ( m )

  return l, u

def rosenbrock_f ( m, n, x ):

#*****************************************************************************80
#
## ROSENBROCK_F returns the function in the rosenbrock problem.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2016
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
  import numpy as np

  value = np.zeros ( n )

  for i in range ( 0, m - 1 ):
    value = value \
      + 100.0 * ( x[i,0:n] - x[i+1,0:n] ) ** 2 \
      +         ( x[i,0:n] - 1.0    ) ** 2

  return value

def rosenbrock_m ( ):

#*****************************************************************************80
#
## ROSENBROCK_M returns the number of variables in the rosenbrock problem.
#
#  Discussion
#
#    Actually, the function can be defined for any 2 <= M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2016
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
  m = 4

  return m

def rosenbrock_test ( ):

#*****************************************************************************80
#
## ROSENBROCK_TEST uses sampling to estimate the range of the ROSENBROCK polynomial.
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
  print ( 'ROSENBROCK_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use N sample values of a polynomial over its domain to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = rosenbrock_m ( )
  l, u = rosenbrock_b ( m )
  print ( '  rosenbrock: [ 0, ? ]:' )

  seed = 123456789
  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x, seed = r8mat_uniform_abvec ( m, n, u, l, seed )
    f = rosenbrock_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ROSENBROCK_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rosenbrock_test ( )
  timestamp ( )

