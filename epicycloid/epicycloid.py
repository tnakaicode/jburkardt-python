#! /usr/bin/env python3
#
def epicycloid_plot ( k, s, n ):

#*****************************************************************************80
#
## epicycloid_plot() plots points along an epicycloid.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real K, the ratio between the large and small circles.
#
#    real S, the number of times the small circle rotates around
#    the large circle.
#
#    integer N: the number of points to plot.
#
  import matplotlib.pyplot as plt

  x, y = epicycloid_xy ( k, s, n )

  plt.clf ( )
  plt.plot ( x, y )
  plt.axis ( 'equal' )
  w = 'Ratio R/r = ' + str ( k ) + ' Revolutions = ' + str ( s )
  plt.title ( w )

  filename = 'epicycloid.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def epicycloid_test ( ):

#*****************************************************************************80
#
## epicycloid_test() tests epicycloid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'epicycloid_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test epicycloid().' )

  k = 2.1
  s = 10.0
  n = 501

  print ( '' )
  print ( '  Ratio R/r =', k )
  print ( '  Number of rotations =', s )
  print ( '  Number of points computed will be', n )

  epicycloid_plot ( k, s, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'epicycloid_test():' )
  print ( '  Normal end of execution.' )

  return

def epicycloid_xy ( k, s, n ):

#*****************************************************************************80
#
## epicycloid_xy() computes XY points along an epicycloid.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real K, the ratio between the large and small circles.
#
#    real S, the number of times the small circle rotates around
#    the large circle.
#
#    integer N, the number of points to compute.
#
#  Output:
#
#    real X(*), Y(*), the Cartesian coordinates of points along the epicycloid.
#
  import numpy as np

  rsmall = 1.0

  t = np.linspace ( 0.0, 2.0 * np.pi * s, n )
  x = rsmall * ( k + 1 ) * np.cos ( t ) - rsmall * np.cos ( ( k + 1 ) * t )
  y = rsmall * ( k + 1 ) * np.sin ( t ) - rsmall * np.sin ( ( k + 1 ) * t )

  return x, y

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
  epicycloid_test ( )
  timestamp ( )


