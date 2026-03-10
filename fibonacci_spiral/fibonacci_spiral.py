#! /usr/bin/env python3
#
def fibonacci_spiral_connected ( n = 101 ):

#*****************************************************************************80
#
## fibonacci_spiral_connected() draws connected points on a Fibonacci spiral.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points to plot.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  PHI is the golden ratio, the limit of the ratio of
#  successive Fibonacci numbers:  
#
#    PHI = limit ( N->oo ) F(N+1)/F(N)
#
  phi = ( 1.0 + np.sqrt ( 5.0 ) ) / 2.0
#
#  Allocate storage for the data.
#
  x = np.zeros ( n )
  y = np.zeros ( n )
#
#  Set the angle and radius of the first point.
#
  a = 0.0
  r = 0.0
#
#  Set the increments.
#
  da = 2.0 * np.pi * ( phi - 1.0 ) / phi
  dr = 1.0
#
#  Create a spiral in which the radius R and angle A both
#  increase by a constant increment,
#
  for i in range ( 0, n ):
    x[i] = r * np.cos ( a )
    y[i] = r * np.sin ( a )
    a =  ( a + da ) % ( 2.0 * np.pi )
    r = r + dr
#
#  SCALE controls how many steps we take between the actual points.
#  A value of 5 is enough to see the basic spiral that connects the points.
#  A vale of 10 would make a smoother spiral.
#
  scale = 5
#
#  Allocate storage for the intermediate data.
#
  n2 = scale * ( n - 1 ) + 1
  x2 = np.zeros ( n2 )
  y2 = np.zeros ( n2 )
#
#  Set the angle and radius of the first point.
#
  a = 0.0
  r = 0.0
#
#  Set the increments.
#
  da = 2.0 * np.pi * ( phi - 1.0 ) / phi
  dr = 1.0

  da = da / scale
  dr = dr / scale
#
#  Create a spiral in which the radius R and angle A both
#  increase by a constant increment,
#
  for i in range ( 0, n2 ):
    x2[i] = r * np.cos ( a )
    y2[i] = r * np.sin ( a )
    a = ( a + da ) % ( 2.0 * np.pi )
    r = r + dr
#
#  Display the points, 
#  and use the intermediate points to draw lines that display the spiral.
#
  plt.clf ( )
  plt.scatter ( x, y )
  plt.plot ( x2, y2, 'r-' )
  plt.axis ( 'equal' )
  plt.title ( 'Connected Fibonacci spiral, N = ' + str ( n ) )
  filename = 'spiral_' + str ( n ) + '_connected.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def fibonacci_spiral ( n = 101 ):

#*****************************************************************************80
#
## fibonacci_spiral() draws points on a Fibonacci spiral.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points to plot.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  PHI is the golden ratio, the limit of the ratio of
#  successive Fibonacci numbers:  
#
#    PHI = limit ( N->oo ) F(N+1)/F(N)
#
  phi = ( 1.0 + np.sqrt ( 5.0 ) ) / 2.0
#
#  Allocate storage for the data.
#
  x = np.zeros ( n )
  y = np.zeros ( n )
#
#  Set the angle and radius of the first point.
#
  a = 0.0
  r = 0.0
#
#  Set the increments.
#
  da = 2.0 * np.pi * ( phi - 1.0 ) / phi
  dr = 1.0
#
#  Create a spiral in which the radius R and angle A both
#  increase by a constant increment,
#
  for i in range ( 0, n ):
    x[i] = r * np.cos ( a )
    y[i] = r * np.sin ( a )
    a = ( a + da ) % ( 2.0 * np.pi )
    r = r + dr
#
#  Display the data in a scatter plot.
#
  plt.clf ( )
  plt.scatter ( x, y )
  plt.axis ( 'equal' )
  plt.title ( 'Fibonacci spiral, n = ' + str ( n ) )
  filename = 'spiral_' + str ( n ) + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def fibonacci_spiral_test ( ):

#*****************************************************************************80
#
## fibonacci_spiral_test() tests fibonacci_spiral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'fibonacci_spiral_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test fibonacci_spiral().' )

  for n in [ 50, 100, 500, 1000 ]:
    fibonacci_spiral ( n )

  for n in [ 50, 100 ]:
    fibonacci_spiral_connected ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'fibonacci_spiral_test():' )
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
  fibonacci_spiral_test ( )
  timestamp ( )

