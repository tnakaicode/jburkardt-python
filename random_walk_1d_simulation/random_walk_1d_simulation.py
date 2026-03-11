#! /usr/bin/env python3
#
def random_walk_1d_histogram ( step_num, walker_num, rng ):

#*****************************************************************************80
#
## random_walk_1d_histogram() makes a histogram of multiple random walkers.
#
#  Discussion:
#
#    The program takes a given number of walkers who start at 0, allows each
#    walker to take one random step and then displays a histogram of the results,
#    that is, it shows where each walker is.  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer STEP_NUM, the number of steps to take.
#
#    integer WALKER_NUM, the number of walkers.
#
#    rng: the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'random_walk_1d_histogram():' )
  print ( '  Make a histogram of multiple random walkers.' )
#
#  Clear the plotting frame.
#
  plt.clf ( )
#
#  X stores the location of each walker.
#
  x_final = np.zeros ( walker_num )

  for walker in range ( 0, walker_num ):
    s = 2 * rng.integers ( low = 0, high = 1, size = walker_num, endpoint = True ) - 1
    x_final[walker] = np.sum ( s )
#
#  Make the histogram and annotate it.
#
  plt.hist ( x_final, bins = 21 )
 
  s = ( '1D Random Walkers - %g walkers, %g steps' % ( walker_num, step_num ) )
  plt.title ( s )
  plt.grid ( True )
  plt.xlabel ( 'Final location' )
  plt.ylabel ( 'Number of walkers' )

  filename = 'random_walk_1d_histogram.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def random_walk_1d_plot ( step_num, walk_num, rng ):

#*****************************************************************************80
#
## random_walk_1d_plot() plots 1 or more random walks in 1D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer STEP_NUM, the number of steps to take in one test.
#
#    integer WALK_NUM, the number of walks.
#
#    rng: the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'random_walk_1d_plot():' )
  print ( '  Simulate and plot WALK_NUM random walks of STEP_NUM steps each.' )
#
#  Clear the plotting frame.
#
  plt.clf ( )

  time = np.linspace ( 0.0, step_num, step_num + 1 )

  plt.plot ( [0, step_num], [0, 0], 'r-', linewidth = 2 )

  for walk in range ( 0, walk_num ):
#
#  Take a walk of STEP_NUM random +1 or -1 steps.
#
    s = 2 * rng.integers ( low = 0, high = 1, size = step_num, endpoint = True ) - 1
    x = np.zeros ( step_num + 1 )
    x[1:] = np.cumsum ( s )
#
#  Plot the results.
#
    plt.plot ( time, x, linewidth = 1 )

    title_string = ( '1D Random Walk - %d walks, %d steps' % ( walk + 1, step_num ) )
    plt.title ( title_string )
    plt.xlabel ( 'Time' )
    plt.ylabel ( 'X(T)' )

  filename = 'random_walk_1d_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def random_walk_1d_simulation ( step_num, walk_num, rng ):

#*****************************************************************************80
#
## random_walk_1d_simulation() simulates a random walk in 1D.
#
#  Discussion:
#
#    The expectation should be that, the average distance squared X^2 
#    is equal to the time, or number of steps N.
#
#    Or, equivalently
#
#      average ( |X| ) = sqrt ( N )
#
#    The program makes a plot of both the average and the maximum values
#    of X^2 versus time.  The maximum value grows much more quickly,
#    and that curve is much more jagged.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer STEP_NUM, the number of steps to take in one test.
#
#    integer WALK_NUM, the number of times to repeat the walk.
#
#    rng: the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'random_walk_1d_simulation():' )
  print ( '  Simulate WALK_NUM random walks of STEP_NUM steps each.' )

  time = np.linspace ( 0, step_num, step_num + 1 )
  x2_ave = np.zeros(step_num+1)
  x2_max = np.zeros(step_num+1)
#
#  Take WALK_NUM walks, each of STEP_NUM random +1 or -1 steps.
#
  for walk in range ( 0, walk_num ):

    s = 2 * rng.integers ( low = 0, high = 1, size = step_num, endpoint = True ) - 1
    x = np.zeros ( step_num + 1 )
    x[1:] = np.cumsum ( s )
#
#  Update the average and max.
#
    x2_ave = x2_ave + x**2
    for i in range ( 0, step_num + 1 ):
      x2_max[i] = max ( x2_max[i], x[i]**2 )
#
#  Average over the number of walks.
#
  x2_ave = x2_ave / walk_num
#
#  Plot the results.
#
  plt.plot ( time, x2_ave, linewidth = 2 )
  plt.plot ( time, x2_max, linewidth = 2 )

  plt.legend ( [ 'Average Distance', 'Maximum Distance' ] )
  plt.title ( '1D Random Walk - Max and average of distance^2 versus time' )
  plt.xlabel ( 'Time' )
  plt.ylabel ( 'Distance Squared' )
  filename = 'random_walk_1d_simulation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def random_walk_1d_simulation_test ( ):

#*****************************************************************************80
#
## random_walk_1d_simulation_test() tests random_walk_1d_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'random_walk_1d_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test random_walk_1d_simulation().' )

  rng = default_rng ( )

  step_num = 500
  walk_num = 5
  random_walk_1d_simulation ( step_num, walk_num, rng )

  step_num = 500
  walk_num = 5
  random_walk_1d_plot ( step_num, walk_num, rng )

  step_num = 50
  walk_num = 10000
  random_walk_1d_histogram ( step_num, walk_num, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'random_walk_1d_simulation_test():' )
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
  random_walk_1d_simulation_test ( )
  timestamp ( )

