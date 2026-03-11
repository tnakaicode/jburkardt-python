#! /usr/bin/env python3
#
def random_walk_2d_plot ( step_num, walk_num, filename, rng ):

#*****************************************************************************80
#
## random_walk_2d_plot() plots 1 or more random walks in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 November 2022
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
#    string FILENAME, the name of the file in which to store
#    a copy of the image.
#
#    rng: the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Clear the plotting frame.
#
  plt.clf ( )
  
  plt.plot ( 0.0, 0.0, 'ko', markersize = 10 )
  plt.grid ( True )

  for walk in range ( 0, walk_num ):

    x = np.zeros(step_num+1)
    y = np.zeros(step_num+1)
#
#  Take a walk of STEP_NUM random steps.
#
    for step in range ( 1, step_num + 1 ):
#
#  We are currently at ( X(STEP-1), Y(STEP-1) ).
#  Consider the four possible points to step to.
#
      k = rng.integers ( low = 0, high = 3, endpoint = True )

      if ( k == 0 ):
        x[step] = x[step-1] + 1.0
        y[step] = y[step-1]
      elif ( k == 1 ):
        x[step] = x[step-1] - 1.0
        y[step] = y[step-1]
      elif ( k == 2 ):
        x[step] = x[step-1]
        y[step] = y[step-1] + 1.0 
      else:
        x[step] = x[step-1]
        y[step] = y[step-1] - 1.0
 
      plt.plot ( [ x[step-1], x[step] ], [ y[step-1], y[step] ], 'r-', linewidth = 1 )

    plt.plot ( x[step_num], y[step_num], 'r*', markersize = 10 )
#
#  Plot the results.
#
    s = '2D Random Walk: ' + str ( walk ) + ' walks, ' + str ( step_num ) + ' steps.'
    plt.title ( s )
    plt.xlabel ( 'X' )
    plt.ylabel ( 'Y' )

    for step in range ( 1, step_num ):
      plt.plot ( [ x[step-1], x[step] ], [ y[step-1], y[step] ], 'b-', linewidth = 1 )
    plt.plot ( x[step_num], y[step_num], 'k*', markersize = 10 )
#
#  Save the graphics file.
#
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def random_walk_2d_simulation ( step_num, walk_num, filename, rng ):

#*****************************************************************************80
#
## random_walk_2d_simulation() simulates a random walk in 2D.
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
#    27 November 2022
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
#    string FILENAME, a name for the graphics file.
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
  for walk in range ( 0, walk_num ):

    x = np.zeros(step_num+1)
    y = np.zeros(step_num+1)
#
#  Take a walk of STEP_NUM random steps.
#
    for step in range ( 1, step_num + 1 ):
#
#  We are currently at ( X(STEP-1), Y(STEP-1) ).
#  Consider the four possible points to step to.
#
      k = rng.integers ( low = 0, high = 3, endpoint = True )

      if ( k == 0 ):
        x[step] = x[step-1] + 1.0
        y[step] = y[step-1]
      elif ( k == 1 ):
        x[step] = x[step-1] - 1.0
        y[step] = y[step-1]
      elif ( k == 2 ):
        x[step] = x[step-1]
        y[step] = y[step-1] + 1.0 
      else:
        x[step] = x[step-1]
        y[step] = y[step-1] - 1.0
#
#  Update the sum of every particle's distance at step J.
#
      d2 = x[step]**2 + y[step]**2
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
  plt.grid ( True )
  plt.legend ( [ 'Average', 'Maximum' ] )
  plt.xlabel ( 'Time' )
  plt.ylabel ( 'Distance squared' )
  s = '2D Random Walk Distance^2 - ' + str ( walk_num ) + ' walks, ' + str ( step_num ) + ' steps'
  plt.title ( s )

  plt.savefig ( filename )
  print ( '  Graphics file saved in "' + filename + '"' )

  return

def random_walk_2d_simulation_test ( ):

#*****************************************************************************80
#
## random_walk_2d_simulation_test() tests random_walk_2d_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'random_walk_2d_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test random_walk_2d_simulation().' )

  rng = default_rng ( )

  step_num = 100
  walk_num = 10
  filename = 'random_walk_2d_plot.png'
  random_walk_2d_plot ( step_num, walk_num, filename, rng )

  step_num = 100
  walk_num = 10
  filename = 'random_walk_2d_simulation.png'
  random_walk_2d_simulation ( step_num, walk_num, filename, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'random_walk_2d_simulation_test():' )
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
  random_walk_2d_simulation_test ( )
  timestamp ( )

