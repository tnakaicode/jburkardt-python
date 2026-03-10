#! /usr/bin/env python3
#
def gamblers_ruin_plot ( a_stakes, b_stakes, rng ):

#*****************************************************************************80
#
## gamblers_ruin_plot() plots a game of gambler's ruin.
#
#  Discussion:
#
#    Two players, A and B, repeatedly toss a coin.  
#    For heads, A wins one dollar from B
#    For tails, B wins one dollar from A.
#    Play continues until one player is bankrupt.
#
#    The program simulates the game, and then produces a plot of the
#    amount of money that A has at each stage of the game.  At the end,
#    A must have either nothing or all the money.
#
#    The program produces a plot of A's money.  It also displays the
#    initial stakes, the number of steps, and the number of times the
#    lead changed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A_STAKES, B_STAKES, the number of dollars that A and
#    B have initially.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'gamblers_ruin_plot():' )
  print ( '  Display the bankrolls of two gambling opponents.' )

  step_num = 0
  leader = '0'
  flip_num = -1
  a = a_stakes
  b = b_stakes
  steps = np.array ( [ 0 ] )
  value = np.array (  [ a ] )

  while ( 0 < a and 0 < b ):

    step_num = step_num + 1

    r = rng.random ( )

    if ( r <= 0.5 ):
      a = a + 1
      b = b - 1
    else:
      a = a - 1
      b = b + 1

#   print ( ' %d %d' % ( a, b ) )
    value = np.append ( value, a )
    steps = np.append ( steps, step_num )

    if ( a_stakes < a and leader != 'A' ):
      leader = 'A'
      flip_num = flip_num + 1
    elif ( a < a_stakes and leader != 'B' ):
      leader = 'B'
      flip_num = flip_num + 1
#
#  Plot the results.
#
  plt.clf ( )
  plt.plot ( [ 0, step_num], [ a_stakes, a_stakes ], 'r-', linewidth = 2 )
  plt.plot ( [ 0, step_num], [ 0, 0 ], 'r-', linewidth = 2 )
  plt.plot ( [ 0, step_num], [ a_stakes + b_stakes, a_stakes + b_stakes ], \
    'r-', linewidth = 2 )

  plt.plot ( steps, value, 'b-', linewidth = 2 )

  title_string = ( 'Gambler\'s Ruin - A = %d, B = %d, Steps = %d, Flips = %d' \
    % ( a, b, step_num, flip_num ) )

  plt.grid ( True )
  plt.title ( title_string )
  plt.xlabel ( 'Coin Tosses' )
  plt.ylabel ( 'A''s Money' )
  plt.axis ( 'tight' )
  filename = 'gamblers_ruin_simulation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def gamblers_ruin_simulation ( a_stakes, b_stakes, game_num, rng ):

#*****************************************************************************80
#
## gamblers_ruin_simulation() simulates the game of gambler's ruin.
#
#  Discussion:
#
#    Two players, A and B, repeatedly toss a coin.  
#    For heads, A wins one dollar from B
#    For tails, B wins one dollar from A.
#    Play continues until one player is bankrupt.
#
#    This program "plays" the game GAME_NUM times, always starting from
#    the same initial configuration.
#
#    it keeps track of the number of coin tosses required, the number
#    of times the lead changes, and the number of times each player wins.
#
#    At the end, it prints some statistics, and plots histograms of the
#    length of the game, and the number of lead changes.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer A_STAKES, B_STAKES, the number of dollars that A and
#    B have initially.
#
#    integer GAME_NUM, the number of games to simulate.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'gamblers_ruin_simulation():' )
  print ( '  Simulate many instances of a two person gambling competition.' )

  flip = np.zeros ( game_num )
  step = np.zeros ( game_num )

  a_wins = 0
  b_wins = 0
#
#  Play GAME_NUM games.
#
  for game in range ( 0, game_num ):

    step_num = 0
    leader = '0'
    flip_num = -1
    a = a_stakes
    b = b_stakes

    while ( 0 < a and 0 < b ):

      step_num = step_num + 1

      r = rng.random ( )
 
      if ( r <= 0.5 ):
        a = a + 1
        b = b - 1
      else:
        a = a - 1
        b = b + 1

      if ( a_stakes < a and leader != 'A' ):
        leader = 'A'
        flip_num = flip_num + 1
      elif ( a < a_stakes and leader != 'B' ):
        leader = 'B'
        flip_num = flip_num + 1

    if ( b == 0 ):
      a_wins = a_wins + 1
    else:
      b_wins = b_wins + 1
 
    flip[game] = flip_num
    step[game] = step_num
#
#  Average over the number of games.
#
  step_ave = np.sum ( step ) / game_num
  prob_a_win = a_wins / game_num
  prob_b_win = b_wins / game_num
#
#  Print statistics.
#
  print ( '' )
  print ( '  Number of games in simulation =', game_num )
  print ( '  A starts game with', a_stakes )
  print ( '  B starts game with', b_stakes )
  print ( '' )
  print ( '  Average number of steps  =', step_ave )
  print ( '  Expected number of steps =', a_stakes * b_stakes )
  print ( '  Maximum number of steps  =', np.max ( step ) )
  print ( '' )
  print ( '  Average chance of A winning = ', prob_a_win )
  print ( '  Expected chance of A winning =', a_stakes / ( a_stakes + b_stakes ) )
  print ( '  Average chance of B winning = ', prob_b_win )
  print ( '  Expected chance of B winning =', b_stakes / ( a_stakes + b_stakes ) )
  print ( '' )
  print ( '  Average number of flips = ', np.sum ( flip ) / game_num )
  print ( '  Maximum number of flips = ', np.max ( flip ) )
  print ( '' )
  print ( '  Initial flip table:' )
  print ( '' )
  print ( '  Number Freq Prob' )
  print ( '' )
  for flip_num in range ( 0, 11 ):
    k = np.sum ( flip == flip_num )
    print ( '  %4d  %6d  %f' % ( flip_num, k, k / game_num ) )
#
#  Plot steps.
#
  plt.clf ( )
  plt.hist ( step, 40 )
  plt.title ( 'Gambler''s ruin, number of steps' )
  plt.grid ( True )
  plt.xlabel ( 'Steps' )
  plt.ylabel ( 'Frequency' )
  filename = 'gamblers_ruin_steps.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  plt.clf ( )
  plt.hist ( flip, 40 )
  plt.title ( 'Gambler''s ruin, number of changes in the lead (flips)' )
  plt.grid ( True )
  plt.xlabel ( 'Flips' )
  plt.ylabel ( 'Frequency' )
  filename = 'gamblers_ruin_flips.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def gamblers_ruin_simulation_test ( ):

#*****************************************************************************80
#
## gamblers_ruin_simulation_test() tests gamblers_ruin_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'gamblers_ruin_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test gamblers_ruin_simulation().' )

  rng = default_rng ( )
#
#  Simulate a single short game.
#
  a_stakes = 5.0
  b_stakes = 7.0
  game_num = 1
  gamblers_ruin_simulation ( a_stakes, b_stakes, game_num, rng )
#
#  Simulate many longer games.
#
  a_stakes = 70.0
  b_stakes = 70.0
  game_num = 1000
  gamblers_ruin_simulation ( a_stakes, b_stakes, game_num, rng )
#
#  Plot the course of a single game.
#
  a_stakes = 70.0
  b_stakes = 70.0
  gamblers_ruin_plot ( a_stakes, b_stakes, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'gamblers_ruin_simulation_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )

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
  gamblers_ruin_simulation_test ( )
  timestamp ( )

