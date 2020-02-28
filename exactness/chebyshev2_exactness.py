#! /usr/bin/env python
#
def chebyshev2_exactness ( n, x, w, p_max ):

#*****************************************************************************80
#
## CHEBYSHEV2_EXACTNESS: monomial exactness for the Chebyshev2 integral.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 January 2016
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
  from chebyshev2_integral import chebyshev2_integral

  print ( '' )
  print ( 'CHEBYSHEV2_EXACTNESS:' )
  print ( '  Quadrature rule for Chebyshev2 integral.' )
  print ( '  Order N = %d' % ( n ) )
  print ( '' )
  print ( '  Degree          Relative Error' )
  print ( '' )

  for p in range ( 0, p_max + 1 ):

    s = chebyshev2_integral ( p )

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

def chebyshev2_exactness_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV2_EXACTNESS_TEST tests rules for the Chebyshev2 integral.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from chebyshev2_set import chebyshev2_set

  print ( '' )
  print ( 'CHEBYSHEV2_EXACTNESS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test Gauss-Chebyshev2 rules for the Chebyshev2 integral.' )
  print ( '  Density function rho(x) = sqrt(1-x^2).' )
  print ( '  Region: -1 <= x <= +1.' )
  print ( '  Exactness: 2*N-1.' )

  for n in range ( 1, 6 ):

    x, w = chebyshev2_set ( n )
    p_max = 2 * n
    chebyshev2_exactness ( n, x, w, p_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHEBSHEV2_EXACTNESS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  chebyshev2_exactness_test ( )
  timestamp ( )
 
