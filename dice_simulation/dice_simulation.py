#! /usr/bin/env python3
#
def dice_simulation_test ( ):

#*****************************************************************************80
#
## dice_simulation_test() tests dice_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'dice_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test dice_simulation().' )

  rng = default_rng ( )

  throw_num = 100
  die_num = 1
  dice_simulation ( throw_num, die_num, rng )

  throw_num = 1000
  die_num = 2
  dice_simulation ( throw_num, die_num, rng )

  throw_num = 10000
  die_num = 3
  dice_simulation ( throw_num, die_num, rng )

  throw_num = 100000
  die_num = 4
  dice_simulation ( throw_num, die_num, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'dice_simulation_test():' )
  print ( '  Normal end of execution.' )

  return

def dice_simulation ( throw_num, die_num, rng ):

#*****************************************************************************80
#
## dice_simulation() simulates the repeated tossing and summing of M dice.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer THROW_NUM, the number of times the dice are thrown.
#
#    integer DIE_NUM, the number of dice.
#
#    rng(): the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'dice_simulation():' )
  print ( '  Simulate throwing and totaling %d dice %d times.' \
    % ( die_num, throw_num ) )
#
#  Throw all the dice, all the times.
#
  throws = rng.integers ( low = 1, high = 6, size = [ throw_num, die_num ], endpoint = True )
#
#  Total the dice in each throw.
#
  score = np.sum ( throws, axis = 1 )
#
#  Make a frequency plot.
#  Poor implementation makes it difficult to reduce width of bars.
#
  plt.clf ( )
  nbins = die_num * 5 + 1
  plt.hist ( score, bins = nbins, rwidth = 0.95 )
  plt.grid ( True )
  plt.xlabel ( 'Score' )
  plt.ylabel ( 'Frequency' )
  title_string = ( 'Sums for %d throws of %d dice' \
    % ( throw_num, die_num ) )
  plt.title ( title_string )
  filename = ( 'dice_freq_%d_%d.png' % ( throw_num, die_num ) )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Make an estimated probability plot.
#
  plt.clf ( )
  x = np.linspace ( die_num, die_num*6, die_num*5+1 )
  y = np.zeros ( die_num*5+1 )
  for i in range ( die_num, die_num * 6 + 1 ):
    j = ( score == i )
    y[i-die_num] = np.sum ( j ) / throw_num

  plt.bar ( x, y, width = 0.9 )

  plt.grid ( True )
  plt.xlabel ( 'Score' )
  plt.ylabel ( 'Estimated Probability' )
  title_string = ( 'Probability estimates for %d throws of %d dice' \
    % ( throw_num, die_num ) )
  plt.title ( title_string )
  filename = ( 'dice_prob_%d_%d.png' % ( throw_num, die_num  ) )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Statistics.
#
  score_ave = np.sum ( score ) / throw_num
  score_var = np.var ( score )
  print ( '' )
  print ( '  Number of dice         = ', die_num )
  print ( '  Number of throws       = ', throw_num )
  print ( '  Maximum possible score = ', 6 * die_num )
  print ( '  Average score          = ', score_ave )
  print ( '  Minimum possible score = ', die_num )
  print ( '  Variance of score      = ', score_var )

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
  dice_simulation_test ( )
  timestamp ( )

