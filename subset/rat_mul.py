#! /usr/bin/env python
#
def rat_mul ( top1, bot1, top2, bot2 ):

#*****************************************************************************80
#
## RAT_MUL multiplies two fractions.
#
#  Discussion:
#
#    The routine computes
#
#      TOP / BOT = ( TOP1 / BOT1 ) * ( TOP2 / BOT2 ).
#
#    while avoiding integer overflow.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer TOP1, BOT1, the first factor.
#
#    Input, integer TOP2, BOT2, the second factor.
#
#    Output, integer TOP, BOT, the product.
#
  from sys import exit
  from i4_gcd import i4_gcd
  from i4_huge import i4_huge

  i_max = i4_huge ( )

  if ( top1 == 0 or top2 == 0 ):
    top = 0
    bot = 1
    return top, bot
#
#  Get rid of all common factors in top and bottom.
#
  temp = i4_gcd ( top1, bot1 )
  top1 = top1 // temp
  bot1 = bot1 // temp
  temp = i4_gcd ( top1, bot2 )
  top1 = top1 // temp
  bot2 = bot2 // temp
  temp = i4_gcd ( top2, bot1 )
  top2 = top2 // temp
  bot1 = bot1 // temp
  temp = i4_gcd ( top2, bot2 )
  top2 = top2 // temp
  bot2 = bot2 // temp
#
#  The fraction (TOP1*TOP2)/(BOT1*BOT2) is in lowest terms.
#
#  Check the top TOP1*TOP2 for overflow.
#
  if ( i_max < abs ( top1 * top2 ) ):
    print ( '' )
    print ( 'RAT_MUL - Fatal error!' )
    print ( '  Overflow of top of rational product.' )
    exit ( 'RAT_MUL - Fatal error!' )

  top = top1 * top2
#
#  Check the bottom BOT1*BOT2 for overflow.
#
  if ( i_max < abs ( bot1 * bot2 ) ):
    print ( '' )
    print ( 'RAT_MUL - Fatal error!' )
    print ( '  Overflow of bottom of rational product.' )
    exit ( 'RAT_MUL - Fatal error!' )

  bot = bot1 * bot2
#
#  The bottom should be positive.
#
  if ( bot < 0 ):
    bot = -bot
    top = -top

  return top, bot

def rat_mul_test ( ):

#*****************************************************************************80
#
## RAT_MUL_TEST tests RAT_MUL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from rat_to_s import rat_to_s

  print ( '' )
  print ( 'RAT_MUL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RAT_MUL multiplies two rationals.' )

  atop = 3
  abot = 4
  btop = 10
  bbot = 7

  ctop, cbot = rat_mul ( atop, abot, btop, bbot )

  print ( '' )
  s = rat_to_s ( atop, abot )
  print ( '  A = %s' % ( s ) )
  s = rat_to_s ( btop, bbot )
  print ( '  B = %s' % ( s ) )
  s = rat_to_s ( ctop, cbot )
  print ( '  C = A * B = %s' % ( s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RAT_MUL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rat_mul_test ( )
  timestamp ( )

