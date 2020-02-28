#! /usr/bin/env python
#
def legendre_exactness ( n, x, w, p_max ):

#*****************************************************************************80
#
## LEGENDRE_EXACTNESS investigates exactness of Legendre quadrature.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of points in the rule.
#
#    Input, real X(N), the quadrature points.
#
#    Input, real W(N), the quadrature weights.
#
#    Input, integer P_MAX, the maximum exponent.
#    0 <= P_MAX.
#
  import numpy as np
  from legendre_integral import legendre_integral

  print ( '' )
  print ( 'LEGENDRE_EXACTNESS:' )
  print ( '  Quadrature rule for Legendre integral.' )
  print ( '  Rule of order N = %d' % ( n ) )
  print ( '  Degree          Relative Error' )
  print ( '' )

  for p in range ( 0, p_max + 1 ):

    s = legendre_integral ( p )

    v = np.zeros ( n )

    for i in range ( 0, n ):
      v[i] = x[i] ** p

    q = np.dot ( w, v )

    if ( s == 0.0 ):
      e = abs ( q - s )
    else:
      e = abs ( ( q - s ) / s )

    print ( '  %6d  %24.16f' % ( p, e ) )

  return

def legendre_exactness_test ( ):

#*****************************************************************************80
#
## LEGENDRE_EXACTNESS_TEST tests Gauss-Legendre rules for Legendre integrals.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from legendre_set import legendre_set

  print ( '' )
  print ( 'LEGENDRE_EXACTNESS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test Gauss-Legendre rules on Legendre integrals.' )
  print ( '  Density function rho(x) = 1.' )
  print ( '  Region: -1 <= x <= +1.' )
  print ( '  Exactness: 2*N-1.' )

  for n in range ( 1, 6 ):

    x, w = legendre_set ( n )
    p_max = 2 * n
    legendre_exactness ( n, x, w, p_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'LEGENDRE_EXACTNESS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  legendre_exactness_test ( )
  timestamp ( )
 
