#! /usr/bin/env python3
#
def hunecke_b ( m ):

#*****************************************************************************80
#
## HUNECKE_B returns the bounds in the hunecke problem.
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

  l = np.array ( [  0.0, +2.0, -2.0, +1.0, -2.0 ] )
  u = np.array ( [ +1.0, +3.0, -1.0, +3.0, -1.0 ] )

  return l, u

def hunecke_f ( m, n, x ):

#*****************************************************************************80
#
## HUNECKE_F returns the function in the hunecke problem.
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
    +       x[1,0:n] ** 6  * x[2,0:n]                                                 \
    +       x[1,0:n]       * x[2,0:n] ** 6                                            \
    +       x[0,0:n] ** 2  * x[1,0:n] ** 4 * x[4,0:n]                                 \
    - 3.0 * x[0,0:n]       * x[1,0:n] ** 2 * x[2,0:n] ** 2 * x[3,0:n]      * x[4,0:n] \
    +       x[2,0:n] ** 4  * x[3,0:n] ** 2 * x[4,0:n]                                 \
    -       x[0,0:n] ** 3  * x[2,0:n]      * x[3,0:n]      * x[4,0:n] ** 2            \
    -       x[0,0:n]       * x[1,0:n]      * x[3,0:n] ** 3 * x[4,0:n] ** 2            \
    +       x[1,0:n]       * x[2,0:n]      * x[4,0:n] ** 5 )

  return value

def hunecke_m ( ):

#*****************************************************************************80
#
## HUNECKE_M returns the number of variables in the hunecke problem.
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
  m = 5

  return m

def hunecke_test ( ):

#*****************************************************************************80
#
## HUNECKE_TEST uses sampling to estimate the range of the HUNECKE polynomial.
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
  print ( 'HUNECKE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use N sample values of a polynomial over its domain to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = hunecke_m ( )
  l, u = hunecke_b ( m )
  print ( '  hunecke: [-1436.515078155, +161.120543283]' )

  seed = 123456789
  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x, seed = r8mat_uniform_abvec ( m, n, u, l, seed )
    f = hunecke_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'HUNECKE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hunecke_test ( )
  timestamp ( )

