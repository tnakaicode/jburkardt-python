#! /usr/bin/env python
#
def fejer1_exactness_test ( ):

#*****************************************************************************80
#
## FEJER1_EXACTNESS_TEST tests Fejer Type 1 rules for Legendre integrals.
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
  from fejer1_set import fejer1_set
  from legendre_exactness import legendre_exactness

  print ( '' )
  print ( 'FEJER1_EXACTNESS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test Fejer Type 1 rules on Legendre integrals.' )
  print ( '  Density function rho(x) = 1.' )
  print ( '  Region: -1 <= x <= +1.' )
  print ( '  Exactness: N   for N odd,' )
  print ( '             N-1 for N even.' )

  for n in range ( 1, 6 ):

    x, w = fejer1_set ( n )

    if ( ( n % 2 ) == 1 ):
      p_max = n + 1
    else:
      p_max = n

    legendre_exactness ( n, x, w, p_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'FEJER1_EXACTNESS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  fejer1_exactness_test ( )
  timestamp ( )
 
