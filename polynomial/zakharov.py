#! /usr/bin/env python3
#
def zakharov_b ( m ):

#*****************************************************************************80
#
## ZAKHAROV_B returns the bounds in the zakharov problem.
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

def zakharov_f ( m, n, x ):

#*****************************************************************************80
#
## ZAKHAROV_F returns the function in the zakharov problem.
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

  s1 = np.zeros ( n )
  s2 = np.zeros ( n )

  for i in range ( 0, m ):
    s1 = s1 +                         x[i,0:n] ** 2
    s2 = s2 + 0.5 * float ( i + 1 ) * x[i,0:n]

  value = s1 + s2 ** 2 + s2 ** 4

  return value

def zakharov_m ( ):

#*****************************************************************************80
#
## ZAKHAROV_M returns the number of variables in the zakharov problem.
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
  m = 5

  return m

def zakharov_test ( ):

#*****************************************************************************80
#
## ZAKHAROV_TEST uses sampling to estimate the range of the ZAKHAROV polynomial.
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
  print ( 'ZAKHAROV_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use N sample values of a polynomial over its domain to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = zakharov_m ( )
  l, u = zakharov_b ( m )
  print ( '  zakharov: [ 0, ? ]:' )

  seed = 123456789
  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x, seed = r8mat_uniform_abvec ( m, n, u, l, seed )
    f = zakharov_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ZAKHAROV_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  zakharov_test ( )
  timestamp ( )

