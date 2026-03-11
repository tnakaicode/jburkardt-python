#! /usr/bin/env python3
#
def random_walk_3d_plot ( step_num, walk_num, rng ):

#*****************************************************************************80
#
## random_walk_3d_plot() plots 1 or more random walks in 3D.
#
#  Discussion:
#
#    The program takes a random walk in 3D, and plots the trajectory.
#    It uses "HOLD ON" to hold the screen.  If the user hits RETURN,
#    another random walk is taken and appears in the same plot.  This
#    continues until the user presses "Q".
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 March 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer STEP_NUM, the number of steps to take in one test.
#
#    integer WALK_NUM, the number of walks to take.
#
#    rng: the current random number generator.
#
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Clear the plotting frame.
#
  plt.clf ( )
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )

  ax.plot ( 0.0, 0.0, 0.0, 'ko', markersize = 10 )
  ax.grid ( True )

  for walk in range ( 0, walk_num ):

    x = np.zeros(step_num+1)
    y = np.zeros(step_num+1)
    z = np.zeros(step_num+1)
#
#  Take a walk of STEP_NUM random steps.
#
    for step in range ( 1, step_num + 1 ):

      xyz = rng.integers ( low = 0, high = 1, size = 3, endpoint = True )
      xyz = 2 * xyz - 1
#
#  Move there.
#
      x[step] = x[step-1] + xyz[0]
      y[step] = y[step-1] + xyz[1]
      z[step] = z[step-1] + xyz[2]
 
      ax.plot ( [ x[step-1], x[step] ], [ y[step-1], y[step] ], \
        [ z[step-1], z[step] ], 'r-', linewidth = 1 )

    ax.plot ( x[step_num], y[step_num], z[step_num], 'r*', markersize = 10 )
#
#  Plot the results.
#
    s = ( '3D Random Walk - %d walks, %d steps' % ( walk, step_num ) )
    ax.set_title ( s )
    ax.set_xlabel ( 'X' )
    ax.set_ylabel ( 'Y' )
    ax.set_zlabel ( 'Z' )
#
#  Save the plot.
#
  filename = ( 'walk_%d_steps_%d_plot.png' % ( walk_num, step_num ) )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def random_walk_3d_simulation ( step_num, walk_num, rng ):

#*****************************************************************************80
#
## random_walk_3d_simulation() simulates a random walk in 3D.
#
#  Discussion:
#
#    The expectation should be that, the average distance squared D^2 
#    is equal to the time, or number of steps N.
#
#    Or, equivalently
#
#      average ( D ) = sqrt ( N )
#
#    The program makes a plot of both the average and the maximum values
#    of D^2 versus time.  The maximum value grows much more quickly,
#    and that curve is much more jagged.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2014
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
#
#  Set up arrays for plotting.
#
  time = np.linspace ( 0, step_num, step_num + 1 )
  d2_ave = np.zeros(step_num+1)
  d2_max = np.zeros(step_num+1)
#
#  Take the walk WALK_NUM times.
#
  for walk in range ( 0, walk_num ):

    x = np.zeros(step_num+1)
    y = np.zeros(step_num+1)
    z = np.zeros(step_num+1)
#
#  Take a walk of STEP_NUM random steps.
#
    for step in range ( 1, step_num + 1 ):

      xyz = rng.integers ( low = 0, high = 1, size = 3, endpoint = True )
      xyz = 2 * xyz - 1
#
#  Move there.
#
      x[step] = x[step-1] + xyz[0]
      y[step] = y[step-1] + xyz[1]
      z[step] = z[step-1] + xyz[2]
#
#  Update the sum of every particle's distance at step J.
#
      d2 = x[step]**2 + y[step]**2 + z[step]**2
      d2_ave[step] = d2_ave[step] + d2
      d2_max[step] = max ( d2_max[step], d2 )
#
#  Average the squared distance at each step over all walks.
#
  d2_ave = d2_ave / walk_num
#
#  Make a plot.
#
  plt.clf ( )
  plt.plot ( time, d2_ave, linewidth = 2 )
  plt.plot ( time, d2_max, linewidth = 2 )

  plt.xlabel ( 'Time' )
  plt.ylabel ( 'Distance squared' )
  plt.title ( '3D Random Walk - Max and average of Distance^2 versus Time' )
  plt.grid ( True )

  filename = ( 'walk_%d_steps_%d.png' % ( walk_num, step_num ) )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def random_walk_3d_simulation_test ( ):

#*****************************************************************************80
#
## random_walk_3d_simulation_test() tests random_walk_3d_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'random_walk_3d_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test random_walk_3d_simulation().' )

  rng = default_rng ( )

  random_walk_3d_plot ( 100, 10, rng )

  random_walk_3d_simulation ( 100, 10, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'random_walk_3d_simulation_test():' )
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
  random_walk_3d_simulation_test ( )
  timestamp ( )

