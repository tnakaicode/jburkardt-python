#! /usr/bin/env python
#
def fejer2_exactness_test ( ):

#*****************************************************************************80
#
## FEJER2_EXACTNESS_TEST tests Fejer Type 2 rules for Legendre integrals.
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
  from fejer2_set import fejer2_set
  from legendre_exactness import legendre_exactness

  print ( '' )
  print ( 'FEJER2_EXACTNESS_TEST;' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test Fejer Type 2 rules on Legendre integrals.' )
  print ( '  Density function rho(x) = 1.' )
  print ( '  Region: -1 <= x <= +1.' )
  print ( '  Exactness: N   for N odd,' )
  print ( '             N-1 for N even.' )

  for n in range ( 1, 6 ):

    x, w = fejer2_set ( n )

    if ( ( n % 2 ) == 1 ):
      p_max = n + 1
    else:
      p_max = n

    legendre_exactness ( n, x, w, p_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEJER2_EXACTNESS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  fejer2_exactness_test ( )
  timestamp ( )
 
