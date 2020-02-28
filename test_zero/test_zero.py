#! /usr/bin/env python3
#
def test_zero_test ( ):

#*****************************************************************************80
#
## TEST_ZERO_TEST tests the TEST_ZERO library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    02 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from bisection    import bisection_test
  from brent        import brent_test
  from muller       import muller_test
  from newton       import newton_test
  from regula_falsi import regula_falsi_test
  from secant       import secant_test

  print ( '' )
  print ( 'TEST_ZERO_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the TEST_ZERO library.' )

  bisection_test ( )
  brent_test ( )
  muller_test ( )
  newton_test ( )
  regula_falsi_test ( )
  secant_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TEST_ZERO_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  test_zero_test ( )
  timestamp ( )

