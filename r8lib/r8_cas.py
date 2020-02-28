#! /usr/bin/env python3
#
def r8_cas ( x ):

#*****************************************************************************80
#
## R8_CAS returns the "casine" of a number.
#
#  Definition:
#
#    The "casine", used in the discrete Hartley transform, is abbreviated
#    CAS(X), and defined by:
#
#      CAS(X) = cos ( X ) + sin( X )
#             = sqrt ( 2 ) * sin ( X + pi/4 )
#             = sqrt ( 2 ) * cos ( X - pi/4 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose casine is desired.
#
#    Output, real VALUE, the casine of X, which will be between
#    plus or minus the square root of 2.
#
  import numpy as np

  value = np.cos ( x ) + np.sin ( x )

  return value

def r8_cas_test ( ):

#*****************************************************************************80
#
## R8_CAS_TEST tests R8_CAS.
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
  import numpy as np
  import platform

  test_num = 12

  print ( '' )
  print ( 'R8_CAS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CAS evaluates the casine of a number.' )
  print ( '' )
  print ( '	X	   R8_CAS ( X )' )
  print ( '' )
  for test in range ( 0, test_num + 1 ):
    x = np.pi * float ( test ) / float ( test_num )
    print ( '  %14f  %14f' % ( x, r8_cas ( x ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CAS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_cas_test ( )
  timestamp ( )
