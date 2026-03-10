#! /usr/bin/env python3
#
def circle_map_test ( ):

#*****************************************************************************80
#
## circle_map_test() tests circle_map().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2025
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'circle_map_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Test circle_map().' )

  A = np.array ( [ [ np.sqrt(3.0), 1.0 ], [ - 1.0, np.sqrt(3.0) ] ] )
  filename = 'circle_map_rotation.png'
  circle_map ( A, filename )

  A = np.array ( [ [ 2.5, 0.0 ], [ 0.0, 0.5 ] ] )
  filename = 'circle_map_diagonal.png'
  circle_map ( A, filename )

  A = np.array ( [ [ 1.0, 2.0 ], [ 0.5, 1.0 ] ] )
  filename = 'circle_map_singular.png'
  circle_map ( A, filename )

  A = np.array ( [ [ 0.70, 0.10 ], [ 0.30, 0.90 ] ] )
  filename = 'circle_map_california.png'
  circle_map ( A, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'circle_map_test():' )
  print ( '  Normal end of execution.' )

  return

def circle_map ( A, filename ):

#*****************************************************************************80
#
## circle_map() plots the image of the unit circle under the 2x2 matrix A.
#
#  Discussion:
#
#    A typical 2x2 matrix will map the unit circle to some kind of tilted 
#    ellipse.  The aspect ratio of the ellipse (ratio of major to minor axes) 
#    is a measure of the conditioning of the matrix.
#
#    A singular matrix maps the unit circle to a line.
#
#    A diagonal matrix maps the unit circle to an ellipse with no tilting.
#    (There is no rotation.)
#
#    An orthogonal matrix maps the unit circle to the unit circle (but points
#    may have rotated.)
#
#    The identity matrix maps the unit circle to itself.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(2,2), the matrix whose mapping of the unit circle 
#    is to be studied.
#
#    string filename: the name of a file in which the image is stored.
#
  import matplotlib.pyplot as plt
  import numpy as np

  n = 20
  angle = np.linspace ( 0.0, 2.0 * np.pi * ( n - 1 ) / n, n )
  r = 1.0

  plt.clf ( )

  x = np.array ( [ r*np.cos(angle), r*np.sin(angle) ] )
  plt.plot ( x[0,:], x[1,:], 'o', markersize = 7 )
  Ax = np.matmul ( A, x )
  plt.plot ( Ax[0,:], Ax[1,:], 'o', markersize = 7 )

  plt.axis ( 'equal' )
  plt.legend ( [ 'x', 'A*x' ] )
  plt.grid ( True )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

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
  circle_map_test ( )
  timestamp ( )

