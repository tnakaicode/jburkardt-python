#! /usr/bin/env python
#
def rat_to_r8 ( a, b ):

#*****************************************************************************80
#
## RAT_TO_R8 converts rational values to real values.
#
#  Example:
#
#    A    B    R
#   --   --    ---
#    1    2    0.5
#    7    5    1.4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, B, the rational quantity to be converted.
#
#    Output, real R, the value of the rational quantity as a real number.
#
  from sys import exit

  if ( b == 0 ):
    print ( '' )
    print ( 'RAT_TO_R8 - Fatal error!' )
    print ( '  The input fraction to be converted had a' )
    print ( '  zero denominator.' )
    exit ( 'RAT_TO_R8 - Fatal error!' )

  r = a / b

  return r

def rat_to_r8_test ( ):

#*****************************************************************************80
#
## RAT_TO_R8_TEST tests RAT_TO_R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_to_rat import r8_to_rat
  from r8_uniform_01 import r8_uniform_01

  ndig = 4

  print ( '' )
  print ( 'RAT_TO_R8_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RAT_TO_R8 converts a rational to a real number.' )
  print ( '' )
  print ( '  The maximum number of digits allowed is %d' % ( ndig ) )

  seed = 123456789

  print ( '' )
  print ( '     R   =>  A / B  =>  R2' )
  print ( '' )

  for i in range ( 0, 10 ):
    r, seed = r8_uniform_01 ( seed )
    r = 10.0 * ( r - 0.25 )
    a, b = r8_to_rat ( r, ndig )
    r2 = rat_to_r8 ( a, b )
    print ( '  %10g  %6d  %6d  %10g' % ( r, a, b, r2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RAT_TO_R8_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rat_to_r8_test ( )
  timestamp ( )
