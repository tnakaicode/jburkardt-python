#! /usr/bin/env python
#
def dec_to_rat ( mantissa, exponent ):

#*****************************************************************************80
#
## DEC_TO_RAT converts a decimal to a rational representation.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#    A rational value is represented by TOP / BOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer MANTISSA, EXPONENT, the decimal number.
#
#    Output, integer TOP, BOT, the rational value.
#
  from i4_gcd import i4_gcd

  if ( exponent == 0 ):
    top = mantissa
    bot = 1
  elif ( 0 < exponent ):
    top = mantissa * 10 ** exponent
    bot = 1
  else:
    top = mantissa
    bot = 10 ** ( - exponent )
    gcd = i4_gcd ( top, bot )
    top = ( top // gcd )
    bot = ( bot // gcd )

  return top, bot

def dec_to_rat_test ( ):

#*****************************************************************************80
#
## DEC_TO_RAT_TEST tests DEC_TO_RAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4_uniform_ab import i4_uniform_ab
  from rat_to_dec import rat_to_dec

  print ( '' )
  print ( 'DEC_TO_RAT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DEC_TO_RAT decimal => fraction.' )
  print ( '' )
  print ( '  In this test, choose the top and bottom' )
  print ( '  of a rational at random, and compute the' )
  print ( '  equivalent real number.' )
  print ( '' )
  print ( '  Then convert to decimal, and the equivalent real.' )
  print ( '' )
  print ( '  Then convert back to rational and the equivalent real.' )
  
  seed = 123456789

  for i in range ( 0, 10 ):

    rat_top, seed = i4_uniform_ab ( -1000, 1000, seed )
    rat_bot, seed = i4_uniform_ab (     1, 1000, seed )

    r1 = float ( rat_top ) / float ( rat_bot )
    mantissa, exponent = rat_to_dec ( rat_top, rat_bot )
    r2 = float ( mantissa ) * 10.0 ** exponent
    rat_top2, rat_bot2 = dec_to_rat ( mantissa, exponent )
    r3 = float ( rat_top2 ) / float ( rat_bot2 )

    print ( '' )
    print ( '  %g = %d / %d' % ( r1, rat_top, rat_bot ) )
    print ( '  %g = %d * 10^%d' % ( r2, mantissa, exponent ) )
    print ( '  %g = %d / %d' % ( r1, rat_top2, rat_bot2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DEC_TO_RAT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dec_to_rat_test ( )
  timestamp ( )

