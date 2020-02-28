#! /usr/bin/env python
#
def laguerre_exactness ( n, x, w, p_max ):

#*****************************************************************************80
#
## LAGUERRE_EXACTNESS investigates exactness of Laguerre quadrature.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
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
  from laguerre_integral import laguerre_integral

  print ( '' )
  print ( '  Quadrature rule for Laguerre integral.' )
  print ( '  Rule of order N = %d' % ( n ) )
  print ( '  Degree          Relative Error' )
  print ( '' )

  for p in range ( 0, p_max + 1 ):

    s = laguerre_integral ( p )

    v = np.zeros ( n )

    for i in range ( 0, n ):
      v[i] = x[i] ** p

    q = np.dot ( w, v )

    if ( s == 0.0 ):
      e = abs ( q - s )
    else:
      e = abs ( ( q - s ) / s )

    print ( '  %6d  %24.16f' % ( p, e ) )

def laguerre_exactness_test ( ):

#*****************************************************************************80
#
## LAGUERRE_EXACTNESS_TEST tests Gauss-Laguerre rules for Laguerre integrals.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from laguerre_set import laguerre_set

  print ( '' )
  print ( 'LAGUERRE_EXACTNESS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test Gauss-Laguerre rules on Laguerre integrals.' )
  print ( '  Density function rho(x) = exp(-x).' )
  print ( '  Region: 0 <= x < +oo.' )
  print ( '  Exactness: 2N-1.' )

  for n in range ( 1, 6 ):

    x, w = laguerre_set ( n )
    p_max = 2 * n
    laguerre_exactness ( n, x, w, p_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'LAGUERRE_EXACTNESS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  laguerre_exactness_test ( )
  timestamp ( )
 
