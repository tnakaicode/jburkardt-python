#! /usr/bin/env python3
#
def random_walk_2d_avoid_plot ( step_num, walk_num, rng ):

#*****************************************************************************80
#
## random_walk_2d_avoid_plot() plots a random self-avoiding walk.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Brian Hayes,
#    How To Avoid Yourself,
#    American Scientist,
#    Volume 86, Number 4, July-August 1998, pages 314-319.
#
#  Input:
#
#    integer STEP_NUM, the number of steps to take in one test.
#
#    integer WALK_NUM, the number of walks to take.
#
#    rng: the current random number generator.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Take as many walks as the user wants to try.
#
  for walk in range ( 0, walk_num ):
#
#  Clear the plotting frame.
#
    plt.clf ( )
#
#  Mark the origin.
#
    plt.plot ( 0.0, 0.0, 'ko', markersize = 10 )
    plt.grid ( True )

    x = 0   
    y = 0

    trajectory = np.zeros ( [ step_num + 1, 2 ] )
    trajectory[0,:] = [ x, y ]

    step_length = step_num
#
#  Take as many steps as the user specified.
#
    for step in range ( 0, step_num ):   
#
#  There are four neighbors of the current point (X,Y).
#
      nabes = 0

      for x1, y1 in [ [x+1,y], [x-1,y], [x,y+1], [x,y-1] ]:
        if ( not vector_in_list ( [ x1, y1 ], trajectory[0:step+1,:] ) ):
          nabes = nabes + 1
          r = rng.random ( )
          if ( r <= 1.0 / nabes ):
            x = x1
            y = y1
#
#  If we ran out of choices, the walk has terminated early.
#
      if ( nabes == 0 ):
        step_length = step
        break
#
#  Add the neighbor to the trajectory .
#
      trajectory[step+1,0] = x
      trajectory[step+1,1] = y
#
#  Plot the trajectory.
#
    for step in range ( 0, step_length ):
      plt.plot ( [ trajectory[step,0], trajectory[step+1,0] ], \
                 [ trajectory[step,1], trajectory[step+1,1] ], 'r-', linewidth = 2 )
#
#  Mark the first position.
#
    plt.plot ( trajectory[0,0], trajectory[0,1], \
      'g*', markersize = 10 )
#
#  Mark the last position.
#
    if ( step_length == step_num ):
      plt.plot ( trajectory[step_length,0], trajectory[step_length,1], \
        'r*', markersize = 10 )
    else:
      plt.plot ( trajectory[step_length,0], trajectory[step_length,1], \
        'bx', markersize = 10 )
#
#  Label the result.
#
    s = ( '2D Random Self-Avoiding Walk - %d walks, %d steps' % ( walk, step_length ) )
    plt.title ( s )
    plt.xlabel ( 'X' )
    plt.ylabel ( 'Y' )
    plt.axis ( 'equal' )
    filename = 'random_walk_2d_avoid_' + str ( walk ) + '_' + str ( step_length ) + '.png'
    plt.savefig ( filename )
    print ( '  Graphics saved as "' + filename + '"' )
    plt.close ( )

  return

def vector_in_list ( vector, vector_list ):

  x = vector[0]
  y = vector[1]
  listed = False
  for x2, y2 in vector_list:
    if ( x == x2 and y == y2 ):
      listed = True
      break

  return listed

def random_walk_2d_avoid_simulation_test ( ):

#*****************************************************************************80
#
## random_walk_2d_avoid_simulation_test() tests random_walk_2d_avoid_simulation().
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
  print ( 'random_walk_2d_avoid_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test random_walk_2d_avoid_simulation().' )

  rng = default_rng ( )

  step_num = 100
  walk_num = 10
  random_walk_2d_avoid_plot ( step_num, walk_num, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'random_walk_2d_avoid_simulation_test():' )
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
  random_walk_2d_avoid_simulation_test ( )
  timestamp ( )

