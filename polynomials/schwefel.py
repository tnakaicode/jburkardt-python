#! /usr/bin/env python3
#
def schwefel_b ( m ):

#*****************************************************************************80
#
## SCHWEFEL_B returns the bounds in the schwefel problem.
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
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Parameters:
#
#    Input, integer M, the number of variables.
#
#    Output, integer L(M), U(M), the lower and upper bounds.
#
  import numpy as np

  l = np.array ( [ -10.0, -10.0, -10.0 ] )
  u = np.array ( [ +10.0, +10.0, +10.0 ] )

  return l, u

def schwefel_f ( m, n, x ):

#*****************************************************************************80
#
## SCHWEFEL_F returns the function in the schwefel problem.
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
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
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
      ( x[0,1:n] - x[1,1:n] ** 2 ) ** 2 \
    + ( x[1,1:n] - 1.0           ) ** 2 \
    + ( x[0,1:n] - x[2,1:n] ** 2 ) ** 2 \
    + ( x[2,1:n] - 1.0           ) ** 2 )

  return value

def schwefel_m ( ):

#*****************************************************************************80
#
## SCHWEFEL_M returns the number of variables in the schwefel problem.
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
#    Cesar Munoz, Anthony Narkawicz,
#    Formalization of Bernstein polynomials and applications to global 
#    optimization,
#    Journal of Automated Reasoning,
#    Volume 51, Number 2, 2013, pages 151-196.
#
#  Parameters:
#
#    Output, integer M, the number of variables.
#
  m = 3

  return m

def schwefel_test ( ):

#*****************************************************************************80
#
## SCHWEFEL_TEST uses sampling to estimate the range of the SCHWEFEL polynomial.
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
  print ( 'SCHWEFEL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use N sample values of a polynomial over its domain to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = schwefel_m ( )
  l, u = schwefel_b ( m )
  print ( '  schwefel: [ 0, ? ]:' )

  seed = 123456789
  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x, seed = r8mat_uniform_abvec ( m, n, u, l, seed )
    f = schwefel_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SCHWEFEL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  schwefel_test ( )
  timestamp ( )

