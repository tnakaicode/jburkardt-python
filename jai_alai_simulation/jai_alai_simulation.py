#! /usr/bin/env python3
#
def i4_wrap ( value, lo, hi ):

#*****************************************************************************80
#
## i4_wrap() forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    LO = 4, HI = 8
#
#    In   Out
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer VALUE, an integer value.
#
#    integer LO, HI, the desired bounds for the integer value.
#
#  Output:
#
#    integer VALUE, a "wrapped" version of VALUE.
#
  value = lo + ( ( value - lo ) % ( hi - lo + 1 ) )

  return value

def jai_alai_match ( strength, rng ):

#*****************************************************************************80
#
## jai_alai_match() simulates one match of jai_alai.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Steven Skiena,
#    Calculated Bets,
#    Computers, Gambling, and Mathematical Modeling to Win,
#    Cambridge University Press, 2001,
#    ISBN13: 978-0521009621.
#
#  Input:
#
#    real strength(8), the strengths of each player.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer winner, the winner of the match.
#
#    integer games, the number of games played before the match was won.
#
  import numpy as np

  first = 0
  second = 1
  waiting = list ( range ( 2, 8 ) )

  score = np.zeros ( 8 )

  games = 0

  while ( True ):

   games = games + 1
   if ( games <= 7 ):
     points = 1
   else:
     points = 2
 
   p1 = strength[first] / ( strength[first] + strength[second] )
   p2 = strength[second] / ( strength[first] + strength[second] )

   r = rng.random ( )

   if ( r < p1 ):
     score[first] = score[first] + points
     if ( 7 <= score[first] ):
       winner = first
       break
     else:
       next = waiting[0]
       for i in range ( 0, 5 ):
         waiting[i] = waiting[i+1]
       waiting[5] = second
       second = next
   else:
     score[second] = score[second] + points
     if ( 7 <= score[second] ):
       winner = second
       break
     else:
       next = waiting[0]
       for i in range ( 0, 5 ):
         waiting[i] = waiting[i+1]
       waiting[5] = first
       first = next

  return winner, games

def jai_alai_simulation ( strength, n, rng ):

#*****************************************************************************80
#
## jai_alai_simulation() simulates many games of jai_alai.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Steven Skiena,
#    Calculated Bets,
#    Computers, Gambling, and Mathematical Modeling to Win,
#    Cambridge University Press, 2001,
#    ISBN13: 978-0521009621.
#
#  Input:
#
#    real strength(8): the strengths of each player.
#
#    integer n: the number of games to play.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer stats(8): the number of wins for each player.
#
  import numpy as np

  stats = np.zeros ( 8 )
  for i in range ( 0, n ):
    winner, games = jai_alai_match ( strength, rng )
    stats[winner] = stats[winner] + 1

  return stats

def jai_alai_simulation_test ( ):

#*****************************************************************************00
#
## jai_alai_simulation_test() tests jai_alai_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'jai_alai_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test jai_alai_simulation()' )
#
#  Equal strengths.
#
  strength = np.ones ( 8 )
  n = 10000
  results = jai_alai_simulation ( strength, n, rng )
  print ( '' )
  print ( '  Case of equal strengths:' )
  print ( '  Player  Strength  Wins  Percentage' )
  print ( '' )
  for i in range ( 0, 8 ):
    print ( '  %d  %8.4f  %4d  %8.4f' \
      % ( i, strength[i], results[i], results[i] / n ) )
#
#  Random strengths.
#
  strength = rng.random ( size = 8 )
  n = 10000
  results = jai_alai_simulation ( strength, n, rng )
  print ( '' )
  print ( '  Case of random strengths' )
  print ( '  Player  Wins  Percentage' )
  print ( '' )
  for i in range ( 0, 8 ):
    print ( '  %d  %8.4f  %4d  %8.4f' \
      % ( i, strength[i], results[i], results[i] / n ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'jai_alai_simulation_test():' )
  print ( '  Normal end of execution.' )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  jai_alai_simulation_test ( )
  timestamp ( )


