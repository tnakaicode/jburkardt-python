#! /usr/bin/env python
#
def chebyshev1_exactness ( n, x, w, p_max ):

#*****************************************************************************80
#
## CHEBYSHEV1_EXACTNESS: monomial exactness for the Chebyshev1 integral.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 January 2016
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
  from chebyshev1_integral import chebyshev1_integral

  print ( '' )
  print ( 'CHEBYSHEV1_EXACTNESS:' )
  print ( '  Quadrature rule for Chebyshev1 integral.' )
  print ( '  Order N = %d' % ( n ) )
  print ( '' )
  print ( '  Degree            Relative Error' )
  print ( '' )

  for p in range ( 0, p_max + 1 ):

    s = chebyshev1_integral ( p )

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

def chebyshev1_exactness_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV1_EXACTNESS_TEST tests rules for the Chebyshev1 integral.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from chebyshev1_set import chebyshev1_set

  print ( '' )
  print ( 'CHEBYSHEV1_EXACTNESS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test Gauss-Chebyshev1 rules for the Chebyshev1 integral.' )
  print ( '  Density function rho(x) = 1/sqrt(1-x^2).' )
  print ( '  Region: -1 <= x <= +1.' )
  print ( '  Exactness: 2*N-1.' )

  for n in range ( 1, 6 ):

    x, w = chebyshev1_set ( n )
    p_max = 2 * n
    chebyshev1_exactness ( n, x, w, p_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHEBSHEV1_EXACTNESS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  chebyshev1_exactness_test ( )
  timestamp ( )
 
