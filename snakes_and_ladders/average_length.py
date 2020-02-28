#! /usr/bin/env python
#
def average_length ( ):

#*****************************************************************************80
#
## AVERAGE_LENGTH estimates the average length of a one-player game.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 September 2014
#
#  Author:
#
#    John Burkardt
#
  import platform
  from game_length import game_length

  print ( '' )
  print ( 'AVERAGE_LENGTH' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Estimate the average length of a game of snakes and ladders.' )

  games = 0
  total = 0

  while ( games < 1000 ):
    games = games + 1
    n = game_length ( )
    total = total + n

  average = total / 1000
  print ( 'Average number of moves is %d' % ( average ) )

  print ( '' )
  print ( 'AVERAGE_LENGTH' )
  print ( '  Normal end of execution.' )

if ( __name__ == '__main__' ):
  average_length ( )
      
