#! /usr/bin/env python3
#
def snakes_and_ladders_simulation_test ( ):

#*****************************************************************************80
#
## snakes_and_ladders_simulation_test() tests snakes_and_ladders_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'snakes_and_ladders_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test snakes_and_ladders_simulation().' )
#
#  Get the minimum, average, and maximum game length over 1000 games.
#  Try this 10 times.
#
  m = 10
  n = 1000
  snakes_stats ( m, n )
#
#  Make a histogram of the game length over 1000 games.
#
  n = 1000
  snakes_histogram ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'snakes_and_ladders_simulation_test():' )
  print ( '  Normal end of execution.' )

  return

def snakes_histogram ( n ):

#*****************************************************************************80
#
## snakes_histogram() makes a game-length histogram for Snakes and Ladders.
#
#  Discussion:
#
#    For histograms, we plot the raw data, whereas for bar charts, we
#    plot the tallies.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of games to play.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'snakes_histogram():' )
  print ( '  Simulate N one-player games of Snakes and Ladders.' )
  print ( '  Use the simulation data to create histograms' )
  print ( '  of the estimated PDF and CDF of the game length.' )
#
#  Simulate N games.
#
  steps = np.zeros ( n )

  for game in range ( 0, n ):
    steps[game] = snakes_one_game ( )
#
#  Report data.
#
  print ( '' )
  print ( '  Number of trials was n =   ', n )
  print ( '  Minimum number of steps was', np.min ( steps ) )
  print ( '  Mean number of steps was   ', np.mean ( steps ) )
  print ( '  Maximum number of steps was', np.max ( steps ) )
  print ( '  Standard deviation was     ', np.std ( steps ) )
#
#  Histogram the PDF.
#
  plt.clf ( )
  nbins = 21
  plt.hist ( steps, bins = nbins, density = True )
  plt.grid ( True )
  plt.title ( 'Game length PDF for ' + str ( n ) + ' Games of Snakes and Ladders' )
  filename = 'snakes_pdf.png'
  print ( '  Graphics saved as "' + filename + '"' )
  plt.savefig ( filename )
#
#  Histogram the CDF.
#
  plt.clf ( )
  nbins = 21
  plt.hist ( steps, bins = nbins, density = True, cumulative = True )
  plt.grid ( True )
  plt.xlabel ( 'Game length' )
  plt.ylabel ( 'CDF' )
  plt.title ( 'Game length CDF for ' + str ( n ) + ' Games of Snakes and Ladders' )
  filename = 'snakes_cdf.png'
  print ( '  Graphics saved as "' + filename + '"' )
  plt.savefig ( filename )

  return

def snakes_ladder_setup ( ):

#*****************************************************************************80
#
## snakes_ladder_setup() defines the snakes and ladders for the game.
#
#  Discussion:
#
#    The two vectors could be merged into one.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer SNAKE(101), LADDER(101), define the snakes and
#    ladders.  If a player lands on square I, then if SNAKE(I) is not I,
#    the player is immediately moved to a previous square whose index
#    is SNAKE(I).  Similarly, if LADDER(I) is not I, then player is
#    immediately taken to a later square whose index is LADDER(I).
#
  import numpy as np

  ladder = list ( range ( 0, 101 ) )

  ladder[1] = 38
  ladder[4] = 14
  ladder[9] = 31
  ladder[21] = 42
  ladder[28] = 84
  ladder[36] = 44
  ladder[51] = 67
  ladder[71] = 91
  ladder[80] = 100

  snake = list ( range ( 0, 101 ) )

  snake[16] = 6
  snake[48] = 26
  snake[49] = 11
  snake[56] = 53
  snake[62] = 19
  snake[64] = 60
  snake[87] = 24
  snake[93] = 73
  snake[95] = 75
  snake[98] = 78

  return snake, ladder

def snakes_move ( i, snake, ladder ):

#*****************************************************************************80
#
## snakes_move() takes one move in a game of Snakes and Ladders.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the current location.
#
#    integer SNAKE(101), LADDER(101), define the snakes and
#    ladders.  If a player lands on square I, then if SNAKE(I) is not I,
#    the player is immediately moved to a previous square whose index
#    is SNAKE(I).  Similarly, if LADDER(I) is not I, then player is
#    immediately taken to a later square whose index is LADDER(I).
#
#  Output:
#
#    integer I, the current location.
#
#    integer D, the value of the die roll, between 1 and 6.
#
  from numpy.random import default_rng

  rng = default_rng ( )
#
#  Roll the die.
#
  d = rng.integers ( low = 1, high = 6, endpoint = True )
#
#  Move from I to I + D.
#
  i = i + d
#
#  Your position can't exceed 100.
#
  i = min ( i, 100 )
#
#  If we landed on a snake, we slide down.
#
  i = snake [ i ]
#
#  If we landed on a ladder, we climb up.
#
  i = ladder [ i ]

  return i, d

def snakes_one_game ( ):

#*****************************************************************************80
#
## snakes_one_game() plays Snakes and Ladders once.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    integer STEP: the number of steps required for a random simulated
#    one-player game of Snakes and Ladders.
#

#
#  Define the snakes and ladders.
#
  snake, ladder = snakes_ladder_setup ( )
#
#  Begin the simulation.
#
  step = 0
  i = 0

  while ( i < 100 ):

    step = step + 1
    i, d = snakes_move ( i, snake, ladder )

  return step

def snakes_stats ( m, n ):

#*****************************************************************************80
#
## snakes_stats() reports minimum, average and maximum game lengths.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 January 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of batches of games to play.
#
#    integer N, the number of games in each batch.
#
  import numpy as np

  print ( '' )
  print ( 'snakes_stats():' )
  print ( '  Simulate N = ', n, ' one-player games of Snakes and Ladders,' )
  print ( '  report minimum, mean, and maximum game lengths.' )
  print ( '  Do this M = ', m, ' times.' )
#
#  Simulate N games.
#
  print ( '' )
  print ( '  Batch    Min   Mean   Max    Std' )
  print ( '' )

  for batch in range ( 0, m ):

    steps = np.zeros ( n )

    for game in range ( 0, n ):
      steps[game] = snakes_one_game ( )
#
#  Report data.
#
    print ( '     %2d  %5d  %5d  %5d  %5g' \
      % ( batch, np.min ( steps ), np.mean ( steps ), np.max ( steps ), np.std ( steps ) ) )

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
  snakes_and_ladders_simulation_test ( )
  timestamp ( )

