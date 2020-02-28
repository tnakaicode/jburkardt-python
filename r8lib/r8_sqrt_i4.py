#! /usr/bin/env python3
#
def r8_sqrt_i4 ( i ):

#*****************************************************************************80
#
## R8_SQRT_I4 returns the square root of an I4 as an R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the number whose square root is desired.
#
#    Output, real R8_SQRT_I4, the value of sqrt(I).
#
  import numpy as np

  value = np.sqrt ( float ( i ) )

  return value

def r8_sqrt_i4_test ( ):

#*****************************************************************************80
#
## R8_SQRT_I4_TEST tests R8_SQRT_I4.
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
  from i4_uniform_ab import i4_uniform_ab

  print ( '' )
  print ( 'R8_SQRT_I4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_SQRT_I4 returns the square root of an I4 as an R8.' )
  print ( '' )
  print ( '      I4      R8_SQRT_I4(I4)' )
  print ( '' )

  seed = 123456789

  for test in range ( 0, 10 ):
    i4, seed = i4_uniform_ab ( 0, 1000000, seed )
    r8 = r8_sqrt_i4 ( i4 )
    print ( '  %10d  %10g' % ( i4, r8 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_SQRT_I4_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_sqrt_i4_test ( )
  timestamp ( )
 
