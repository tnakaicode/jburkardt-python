#! /usr/bin/env python
#
def chebyshev3_exactness_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV3_EXACTNESS_TEST tests Gauss-Chebyshev3 rules for the Chebyshev1 integral.
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

  from chebyshev1_exactness import chebyshev1_exactness
  from chebyshev3_set import chebyshev3_set

  print ( '' )
  print ( 'CHEBYSHEV3_EXACTNESS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test Gauss-Chebyshev3 rules for the Chebyshev1 integral.' )
  print ( '  Density function rho(x) = 1/sqrt(1-x^2).' )
  print ( '  Region: -1 <= x <= +1.' )
  print ( '  Exactness: 2*N-3.' )

  for n in range ( 1, 6 ):

    x, w = chebyshev3_set ( n )
    if ( n == 1 ):
      p_max = 2 * n
    else:
      p_max = 2 * n - 2

    chebyshev1_exactness ( n, x, w, p_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHEBSHEV3_EXACTNESS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  chebyshev3_exactness_test ( )
  timestamp ( )
 
