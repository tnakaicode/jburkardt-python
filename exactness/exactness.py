#! /usr/bin/env python3
#
def exactness_test ( ):

#*****************************************************************************80
#
## EXACTNESS_TEST tests EXACTNESS.
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
  from chebyshev1_exactness           import chebyshev1_exactness_test
  from chebyshev1_integral            import chebyshev1_integral_test
  from chebyshev2_exactness           import chebyshev2_exactness_test
  from chebyshev2_integral            import chebyshev2_integral_test
  from chebyshev3_exactness           import chebyshev3_exactness_test
  from clenshaw_curtis_exactness      import clenshaw_curtis_exactness_test
  from fejer1_exactness               import fejer1_exactness_test
  from fejer2_exactness               import fejer2_exactness_test
  from gegenbauer_exactness           import gegenbauer_exactness_test
  from gegenbauer_integral            import gegenbauer_integral_test
  from hermite_1_exactness            import hermite_1_exactness_test
  from hermite_exactness              import hermite_exactness_test
  from hermite_integral               import hermite_integral_test
  from laguerre_1_exactness           import laguerre_1_exactness_test
  from laguerre_exactness             import laguerre_exactness_test
  from laguerre_integral              import laguerre_integral_test
  from legendre_exactness             import legendre_exactness_test
  from legendre_integral              import legendre_integral_test
  from r8_factorial                   import r8_factorial_test
  from r8_factorial2                  import r8_factorial2_test
  from r8_gamma                       import r8_gamma_test

  print ( '' )
  print ( 'EXACTNESS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the EXACTNESS library.' )

  chebyshev1_exactness_test ( )
  chebyshev1_integral_test ( )
  chebyshev2_exactness_test ( )
  chebyshev2_integral_test ( )
  chebyshev3_exactness_test ( )
  clenshaw_curtis_exactness_test ( )
  fejer1_exactness_test ( )
  fejer2_exactness_test ( )
  gegenbauer_exactness_test ( )
  gegenbauer_integral_test ( )
  hermite_1_exactness_test ( )
  hermite_exactness_test ( )
  hermite_integral_test ( )
  laguerre_1_exactness_test ( )
  laguerre_exactness_test ( )
  laguerre_integral_test ( )
  legendre_exactness_test ( )
  legendre_integral_test ( )
  r8_factorial_test ( )
  r8_factorial2_test ( )
  r8_gamma_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'EXACTNESS_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  exactness_test ( )
  timestamp ( )

