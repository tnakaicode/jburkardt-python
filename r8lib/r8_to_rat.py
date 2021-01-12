#! /usr/bin/env python
#
def r8_to_rat ( r, ndig ):

#*****************************************************************************80
#
## R8_TO_RAT converts a real value to a rational value.
#
#  Discussion:
#
#    The rational value (IATOP/IABOT) is essentially computed by truncating
#    the decimal representation of the real value after a given number of
#    decimal digits.
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
#    Input, real R, the real value to be converted.
#
#    Input, integer NDIG, the number of decimal digits used.
#
#    Output, integer IATOP, IABOT, the numerator and denominator
#    of the rational value that approximates the real number.
#
  from i4_gcd import i4_gcd

  factor = 10 ** ndig

  if ( 0 < ndig ):
    ifac = 10 ** ndig
    jfac = 1
  else:
    ifac = 1
    jfac = 10 ** ( - ndig )

  itop = int ( round ( r * factor ) * jfac )
  ibot = ifac
#
#  Factor out the greatest common factor.
#
  itemp = i4_gcd ( itop, ibot )

  iatop = ( itop // itemp )
  iabot = ( ibot // itemp )

  return iatop, iabot

def r8_to_rat_test ( ):

#*****************************************************************************80
#
## R8_TO_RAT_TEST tests R8_TO_RAT.
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
  from r8_uniform_01 import r8_uniform_01
  from rat_to_r8 import rat_to_r8

  ndig = 4

  print ( '' )
  print ( 'R8_TO_RAT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_TO_RAT converts a real number to a rational' )
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
  print ( 'R8_TO_RAT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_to_rat_test ( )
  timestamp ( )

