#! /usr/bin/env python3
#
def caprasse_b ( m ):

#*****************************************************************************80
#
## CAPRASSE_B returns the bounds in the caprasse problem.
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

  l = np.array ( [ -0.5, -0.5, -0.5, -0.5 ] )
  u = np.array ( [ +0.5, +0.5, +0.5, +0.5 ] )

  return l, u

def caprasse_f ( m, n, x ):

#*****************************************************************************80
#
## CAPRASSE_F returns the function in the caprasse problem.
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
    -        x[0,0:n]       * x[2,0:n] ** 3                 \
    +  4.0 * x[1,0:n]       * x[2,0:n] ** 2 * x[3,0:n]      \
    +  4.0 * x[0,0:n]       * x[2,0:n]      * x[3,0:n] ** 2 \
    +  2.0 * x[1,0:n]       * x[3,0:n] ** 3                 \
    +  4.0 * x[0,0:n]       * x[2,0:n]                      \
    +  4.0 * x[2,0:n] ** 2                                  \
    - 10.0 * x[1,0:n]       * x[3,0:n]                      \
    - 10.0 * x[3,0:n] ** 2                                  \
    +  2.0 )

  return value

def caprasse_m ( ):

#*****************************************************************************80
#
## CAPRASSE_M returns the number of variables in the caprasse problem.
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
  m = 4

  return m

def caprasse_test ( ):

#*****************************************************************************80
#
## CAPRASSE_TEST uses sampling to estimate the range of the CAPRASSE polynomial.
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
#    26 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8mat_uniform_abvec import r8mat_uniform_abvec

  print ( '' )
  print ( 'CAPRASSE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Use N sample values of a polynomial over its domain to estimate' )
  print ( '  its minimum Pmin and maximum Pmax' )
  print ( '' )
  print ( '         N           Pmin             Pmax' )
  print ( '' )

  m = caprasse_m ( )
  l, u = caprasse_b ( m )
  print ( '  caprasse: [-3.1800966258, +4.4852773332]' )

  seed = 123456789
  n = 8

  for n_log_2 in range ( 4, 15 ):

    n = n * 2
    x, seed = r8mat_uniform_abvec ( m, n, u, l, seed )
    f = caprasse_f ( m, n, x )
    print ( '  %8d  %16.8g  %16.8g' % ( n, min ( f ), max ( f ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CAPRASSE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  caprasse_test ( )
  timestamp ( )


