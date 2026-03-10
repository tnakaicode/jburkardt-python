#! /usr/bin/env python3
#
def craps_game ( bet, rng ):

#*****************************************************************************80
#
## craps_game() simulates one game of craps.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer bet: the amount of money that the player has bet.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer result: the amount the player has won or lost.
#
#    integer roll: the number of times the dice were rolled.
#
#    integer point: the sum of the dice on the first roll.
#
  roll = 0

  while ( True ):

    roll = roll + 1
    dice = rng.integers ( low = 1, high = 6, size = 2, endpoint = True )
    value = sum ( dice )

    if ( roll == 1 ):

      point = value

      if ( value == 7 or value == 11 ):
        result = + bet
        break
      elif ( value == 2 or value == 3 or value == 12 ):
        result = - bet
        break

    else:

      if ( value == point ):
        result = + bet
        break
      elif ( value == 7 ):
        result = - bet
        break

    roll = roll + 1

  return result, roll, point

def craps_game_test ( ):

#*****************************************************************************80
#
## craps_game_test() tests craps_game().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng

  print ( '' )
  print ( 'craps_game_test():' )
  print ( '  craps_game() simulates a game of craps.' )

  rng = default_rng ( )

  bankroll = 1000.0
  print ( '' )
  print ( '  Player starts with bankroll of', bankroll )

  for i in range ( 0, 10 ):
    bet = bankroll / 2.0
    result, roll, point = craps_game ( bet, rng )
    bankroll = bankroll + result

    print ( '' )
    print ( '  The player bet $', bet )
    print ( '  The first roll had the value ', point )
    print ( '  There were a total of ', roll, ' rolls', roll )
    print ( '  The player''s result was', result )
    print ( '  The player''s bankroll is now', bankroll )

  return

def craps_probability ( ):

#*****************************************************************************80
#
## craps_probability() returns the probabiity of winning one game of craps.
#
#  Discussion:
#
#    The exact probability of a single win in craps is 244/495.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real p: the probability of winning one game of craps.
#
  p = 244.0 / 495.0

  return p

def craps_simulation_test ( ):

#*****************************************************************************80
#
## craps_simulation_test() tests craps_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'craps_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  craps_simulation() simulates a game of craps.' )

  craps_game_test ( )
  craps_stats_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'craps_simulation_test()' )
  print ( '  Normal end of execution.' )

  return

def craps_stats ( n, rng ):

#*****************************************************************************80
#
## craps_stats() returns statistics for N games of craps.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of games played.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    integer win_total: the number of wins.
#
#    integer roll_total: the number of rolls.
#
  bet = 1.0
  win_total = 0
  roll_total = 0

  for i in range ( 0, n ):
    result, roll, point = craps_game ( bet, rng )
    if ( 0.0 < result ):
      win_total = win_total + 1
    roll_total = roll_total + roll

  return win_total, roll_total

def craps_stats_test ( ):

#*****************************************************************************80
#
## craps_stats_test() tests craps_stats().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng

  print ( '' )
  print ( 'craps_stats_test():' )
  print ( '  craps_stats() reports statistics for N instances' )
  print ( '  of a craps game.' )

  rng = default_rng ( )

  print ( '' )
  print ( '       N    Win/N   Rolls/N' )
  print ( '' )

  for n in [ 1, 10, 100, 1000, 10000 ]:
    win_total, roll_total = craps_stats ( n, rng )
    print ( '   %6d  %8.4f  %8.4f' % ( n, win_total / n, roll_total / n ) )

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
  craps_simulation_test ( )
  timestamp ( )

