#! /usr/bin/env python
#
def clenshaw_curtis_exactness_test ( ):

#*****************************************************************************80
#
## CLENSHAW_CURTIS_EXACTNESS_TEST tests Clenshaw-Curtis rules for Legendre integrals.
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
  from clenshaw_curtis_set import clenshaw_curtis_set
  from legendre_exactness import legendre_exactness

  print ( '' )
  print ( 'CLENSHAW_CURTIS_EXACTNESS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test Clenshaw-Curtis rules on Legendre integrals.' )
  print ( '  Density function rho(x) = 1.' )
  print ( '  Region: -1 <= x <= +1.' )
  print ( '  Exactness: N   for N odd,' )
  print ( '             N-1 for N even.' )

  for n in range ( 1, 6 ):

    x, w = clenshaw_curtis_set ( n );
    if ( ( n % 2 ) == 1 ):
      p_max = n + 1
    else:
      p_max = n

    legendre_exactness ( n, x, w, p_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'CLENSHAW_CURTIS_EXACTNESS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  clenshaw_curtis_exactness_test ( )
  timestamp ( )
 
