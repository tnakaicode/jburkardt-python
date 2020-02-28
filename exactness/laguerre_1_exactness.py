#! /usr/bin/env python
#
def laguerre_1_exactness_test ( ):

#*****************************************************************************80
#
## LAGUERRE_1_EXACTNESS_TEST tests rules for Laguerre integrals with rho=1.
#
#  Discussion:
#
#    Instead of the usual density rho(x)=exp(-x), these rules apply to
#    approximating the integral:
#      I(f) = integral ( 0 <= x < +oo ) f(x) dx
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
  import numpy as np
  import platform
  from laguerre_1_set import laguerre_1_set
  from laguerre_exactness import laguerre_exactness

  print ( '' )
  print ( 'LAGUERRE_1_EXACTNESS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test quadrature rules on Laguerre integrals.' )
  print ( '  Density function rho(x) = 1.' )
  print ( '  Region: 0 <= x < +oo.' )
  print ( '  Exactness: 2N-1.' )

  for n in range ( 1, 6 ):

    x, w = laguerre_1_set ( n )
#
#  Standardize the rule by multiplying every weight w(i) by exp(-x(i)).
#
    for i in range ( 0, n ):
      w[i] = np.exp ( - x[i] ) * w[i]
#
#  Now test the rule in standard form.
#
    p_max = 2 * n
    laguerre_exactness ( n, x, w, p_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'LAGUERRE_1_EXACTNESS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  laguerre_1_exactness_test ( )
  timestamp ( )
 
