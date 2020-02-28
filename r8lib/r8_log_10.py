#! /usr/bin/env python3
#
def r8_log_10 ( x ):

#*****************************************************************************80
#
## R8_LOG_10 returns the logarithm base 10 of |X|.
#
#  Discussion:
#
#    value = Log10 ( |X| )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose base 2 logarithm is desired.
#    X should not be 0.
#
#    Output, real VALUE, the logarithm base 10 of the absolute
#    value of X.  It should be true that |X| = 10^R8_LOG_10.
#
  import numpy as np

  if ( x == 0.0 ):
    value = - np.inf
  else:
    value = np.log ( abs ( x ) ) / np.log ( 10.0 )

  return value

def r8_log_10_test ( ):

#*****************************************************************************80
#
## R8_LOG_10_TEST tests R8_LOG_10.
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
  import numpy as np
  import platform

  test_num = 18

  x_test = np.array ( [ \
    0.0,  1.0,  2.0,   3.0,  9.0, \
   10.0, 11.0, 99.0, 101.0, -1.0, \
   -2.0, -3.0, -9.0,   0.5,  0.33, \
    0.25, 0.20, 0.01 ] )

  print ( '' )
  print ( 'R8_LOG_10_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_LOG_10 computes the logarithm base 10.' )
  print ( '' )
  print ( '      X      R8_LOG_10' )
  print ( '' )

  for test in range ( 0, test_num ):
    x = x_test[test]
    print ( '  %12f  %12f' % ( x, r8_log_10 ( x ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_LOG_10_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_log_10_test ( )
  timestamp ( )
 
