#! /usr/bin/env python3
#
def r8_is_nan ( r ):

#*****************************************************************************80
#
## R8_IS_NAN determines if an R8 represents a NaN value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the number to be checked.
#
#    Output, bool VALUE, is TRUE if R is a NaN
#
  value = ( r != r )

  return value

def r8_is_nan_test ( ):

#*****************************************************************************80
#
## R8_IS_NAN_TEST tests R8_IS_NAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8_IS_NAN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_IS_NAN reports whether an R8 is a NaN.' )
  print ( '' )
  print ( '  These tests are wasted, since all the arithmetic' )
  print ( '  operations return run time errors.' )
  print ( '' )

  r8 = 1.0
  print ( '  R8_IS_NAN(1.0) = %d' % ( r8_is_nan ( r8 ) ) )

  if ( True ):
    print ( '  In Python, 1.0/0.0 just sets a run time error.' )
  else:
    r1 = 1.0
    r2 = 0.0
    r8 = r1 / r2
    print ( '  R8_IS_NAN(1.0/0.0) = %d' % ( r8_is_nan ( r8 ) ) )

  if ( True ):
    print ( '  In Python, 0.0/0.0 just sets a run time error.' )
  else:
    r1 = 0.0
    r2 = 0.0
    r8 = r1 / r2
    print ( '  R8_IS_NAN(0.0/0.0) = %d' % ( r8_is_nan ( r8 ) ) )

  r1 = 0.0
  r2 = 0.0
  r8 = r1 ** r2
  print ( '  R8_IS_NAN(0^0) = %d' % ( r8_is_nan ( r8 ) ) )

  if ( True ):
    print ( '  In Python, arccos(-2.0) just sets a run time warning.' )
  else:
    r1 = -2.0
    r8 = np.arccos ( r1 )
    print ( '  R8_IS_NAN(acos(-2)) = %d' % ( r8_is_nan ( r8 ) ) )

  if ( True ):
    print ( '  In Python, exp(1000) just sets a run time warning.' )
  else:
    r1 = 1000.0
    r8 = np.exp ( r1 )
    print ( '  R8_IS_NAN(exp(1000)) = %d' % ( r8_is_nan ( r8 ) ) )

  if ( True ):
    print ( '  In Python, log(0.0) just sets a run time warning.' )
  else:
    r1 = 0.0
    r8 = np.log ( r1 )
    print ( '  R8_IS_NAN(log(0)) = %d' % ( r8_is_nan ( r8 ) ) )

  if ( True ):
    print ( '  In Python, sqrt(-1.0) just sets a run time warning.' )
  else:
    r1 = -1.0
    r8 = np.sqrt ( r1 )
    print ( '  R8_IS_NAN(sqrt(-1)) = %d' % ( r8_is_nan ( r8 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_IS_NAN_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_is_nan_test ( )
  timestamp ( )
 
