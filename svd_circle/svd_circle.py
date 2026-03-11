#! /usr/bin/env python3
#
def svd_circle ( A ):

#*****************************************************************************80
#
## svd_circle() plots the image of the unit circle under the 2x2 matrix A.
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
#    The singular value decomposition can predict the shape of the mapping:
#
#    * The vector V(1,1:2) maps to S(1)*U(1:2,1),
#    * The vector V(2,1:2) maps to S(2)*U(1:2,2).
#
#    The ellipse has an aspect ratio of S(1)/S(2).
#
#    The "tilt" or slope of the ellipse is U(2,1)/U(1,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2022
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
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'svd_circle():' )
  print ( '  Given a matrix A,' )
  print ( '  plot points x on the unit circle, and' )
  print ( '  the images A*x of those points.' )
  print ( '  Show right singular vectors V' )
  print ( '  and their images, the scaled left singular vectors U.' )
  print ( '' )
  print ( '  Matrix A:' )
  print ( '' )
  print ( A )
#
#  This call produces matrices U, S and V.
#
  U, svec, V = np.linalg.svd ( A )

  print ( '  Singular values of A are', svec[0], 'and', svec[1] )
  print ( '  Right singular vectors are columns of V:' )
  V = V.T
  print ( V )
  print ( '  Left singular vectors are columns of U:' )
  print ( U )
  print ( '  Aspect ratio of ellipse will be', svec[0] / svec[1] )
  print ( '  Slope of ellipse will be', U[1,0] / U[0,0] )
#
#  Select N evenly spaced points X on the unit circle.
#
  n = 20

  i = np.linspace ( 0, n - 1, n, dtype = float )

  angle = 2.0 * np.pi * i / float ( n )

  r = 1.0

  x = np.array ( [ r * np.cos ( angle ), r * np.sin ( angle ) ] )
#
#  AX contains the image of each point under the mapping X -> A*X.
#
  ax = np.dot ( A, x )
#
#  Determine a common plot range.
#
  p_min = min ( np.min ( ax ), np.min ( x ) )
  p_max = max ( np.max ( ax ), np.max ( x ) )
#
#  Plot the corners of the region.  This is a trick to force MATLAB
#  to plot in a square with equal axes.  
#
  plt.clf ( )
  plt.scatter ( \
    [ p_min, p_max, p_max, p_min ], \
    [ p_min, p_min, p_max, p_max ] )
#
#  Label the points X on the unit circle.
#
  i = 97
  for j in range ( 0, n ):
    plt.text ( x[0,j], x[1,j], chr ( i ) )
    i = i + 1
    if ( 122 < i ):
      i = 97
#
#  Plot V1 and V2.
#
  plt.plot ( [ 0.0, V[0,0]], [ 0.0, V[1,0]], 'b', linewidth = 3 )
  plt.plot ( [ 0.0, V[0,1]], [ 0.0, V[1,1]], 'b', linewidth = 3 )

  plt.xlabel ( '--X axis--' )
  plt.ylabel ( '--Y axis--' )
  plt.title ( 'Points X on unit circle, and right singular vectors' )
  plt.axis ( np.array ( [ p_min, p_max, p_min, p_max ] ) )
  plt.axis ( 'equal' )
  plt.axis ( 'tight' )
  plt.axis ( 'square' )
  plt.grid ( True )
  filename = 'svd_circle_1.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Label the points AX on the image of the unit circle.
#
  plt.clf ( )
  plt.scatter ( np.array ( [ p_min, p_max, p_max, p_min ] ), \
                np.array ( [ p_min, p_min, p_max, p_max ] ) )
#
#  Plot the images AX of points X on the unit circle.
#
  i = 65
  for j in range ( 0, n ):
    plt.text ( ax[0,j], ax[1,j], chr ( i ) )
    i = i + 1
    if ( 90 < i ):
      i = 65
#
#  Plot the images of V1 and V2.
#
  plt.plot ( [ 0.0, svec[0]*U[0,0]], [ 0.0, svec[0]*U[1,0]], 'r', linewidth = 3 )
  plt.plot ( [ 0.0, svec[1]*U[0,1]], [ 0.0, svec[1]*U[1,1]], 'r', linewidth = 3 )

  plt.xlabel ( '--X axis--' )
  plt.ylabel ( '--Y axis--' )
  plt.title ( 'Images A*X of points on unit circle and scaled left singular vectors' )
  plt.axis ( np.array ( [ p_min, p_max, p_min, p_max ] ) )
  plt.axis ( 'equal' )
  plt.axis ( 'tight' )
  plt.axis ( 'square' )
  plt.grid ( True )
  filename = 'svd_circle_2.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

  return

def svd_circle_test ( ):

#*****************************************************************************80
#
## svd_circle_test() tests svd_circle().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'svd_circle_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test svd_circle().' )

  A = np.array ( [ \
    [ 3.0, 2.0 ],
    [ 1.0, 0.0 ] ] )

  svd_circle ( A )
#
#  Terminate.
#
  print ( '' )
  print ( 'svd_circle_test():' )
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
  svd_circle_test ( )
  timestamp ( )

