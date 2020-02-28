#! /usr/bin/env python
#
def hermite_1_exactness_test ( ):

#*****************************************************************************80
#
## HERMITE_1_EXACTNESS_TEST tests rules for Hermite integrals with density 1.
#
#  Discussion:
#
#    Instead of the usual density rho(x)=exp(-x*x), these rules apply to
#    approximating the integral:
#      I(f) = integral ( -oo < x < +oo ) f(x) dx
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
  from hermite_1_set import hermite_1_set
  from hermite_exactness import hermite_exactness

  print ( '' )
  print ( 'HERMITE_1_EXACTNESS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test Gauss-Hermite rules on Hermite integrals.' )
  print ( '  Density function rho(x) = 1.' )
  print ( '  Region: -oo < x < +oo.' )
  print ( '  Exactness: 2N-1.' )

  for n in range ( 1, 6 ):

    x, w = hermite_1_set ( n );
#
#  Standardize the rule by multiplying every weight w(i) by exp(-x(i)^2).
#
    for i in range ( 0, n ):
      w[i] = np.exp ( - x[i] * x[i] ) * w[i]
#
#  Now test the rule in standard form.
#
    p_max = 2 * n
    hermite_exactness ( n, x, w, p_max );
#
#  Terminate.
#
  print ( '' )
  print ( 'HERMITE_1_EXACTNESS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  hermite_1_exactness_test ( )
  timestamp ( )
 
