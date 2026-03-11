#! /usr/bin/env python3
#
def jumping_bean_simulation_test ( ):

#*****************************************************************************80
#
## jumping_bean_simulation_test() tests jumping_bean_simulation().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'jumping_bean_simulation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  jumping_bean_simulation() performs a 2d random walk.' )
#
#  Average the behavior over n simulations.
#
  n = 1000
  print ( '  The behavior will be averaged over ', n, ' simulations.' )
#
#  Observe the behavior over circles of radius 0, 1, ..., 10
#
  print ( '  Observe behavior over circles of radius 0 through 10.' )
  dvec = np.linspace ( 0, 10, 11 )

  t_average = np.zeros ( 11 )
  for d in range ( 0, 11 ):
    t_sum = 0
    for i in range ( 0, n ):
      t_sum = t_sum + jumping_bean_simulation ( d )
    t_average[d] = t_sum / n
#
#  Plot distance from origin versus time.
#
  plt.clf ( )
  plt.plot ( dvec, t_average, 'bo' )
  plt.plot ( dvec, dvec**2, 'r-', markersize = 20 )
  plt.legend ( [ 'Observed behavior', 'Theoretical behavior' ] )
  plt.grid ( True )
  plt.xlabel ( '<-- Distance from origin-->' )
  plt.ylabel ( '<-- Time -->' )
  plt.title ( 'Takes about D^2 steps to escape circle of radius D' )
  filename = 'jumping_bean_simulation.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'jumping_bean_simulation_test():' )
  print ( '  Normal end of execution.' )

  return

def jumping_bean_simulation ( dmax ):

#*****************************************************************************80
#
## jumping_bean_simulation() simulates the path of a jumping bean.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 December 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real dmax: the radius of the circle which the jumping bean
#    must escape.
#
#  Output:
#
#    integer t: the number of jumps required before the jumping bean
#    was at least dmax units away from the origin.
#
  import numpy as np

  directions = np.array ( [ 'N', 'S', 'E', 'W' ] )
  location = np.array ( [ 0, 0 ] )
  d = 0.0
  t = 0

  while ( d < dmax ):
    t = t + 1
    direction = np.random.choice ( directions )
    if ( direction == 'N' ):
      location[1] = location[1] + 1
    elif ( direction == 'S' ):
      location[1] = location[1] - 1
    elif ( direction == 'E' ):
      location[0] = location[0] + 1
    else:
      location[0] = location[0] - 1
    d = np.sqrt ( location[0]**2 + location[1]**2 )

  return t

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

if ( __name__ == "__main__" ):
  timestamp ( )
  jumping_bean_simulation_test ( )
  timestamp ( )

