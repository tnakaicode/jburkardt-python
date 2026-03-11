#! /usr/bin/env python3
#
def polygon_average ( n, p ):

#*****************************************************************************80
#
## polygon_average() takes one step of polygon averaging.
#
#  Discussion:
#
#    A polygon is represented by a list of N vertices.
#
#    An averaging step involves:
#    * replacing each vertex by the average of itself and its neighbor, 
#    * shifting these vertices to have centroid 0
#    * scaling the X and Y coordinates separately so that the max-norms
#      of the X and Y coordinate vectors are both 1.
#
#    If the averaging process is carried out recursively, the resulting
#    polygon rapidly converges to an ellipse at a 45 degree tilt.
#
#    The direction of the tilt, and the ratio between the major and minor
#    axis lengths, vary depending on the initial polygon.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Van Loan, Daisy Fan,
#    Insight Through Computing,
#    SIAM Publishing, 2010,
#    ISBN: 978-0-898716-91-7
#
#    Adam Elmachtoub, Charles Van Loan,
#    From Random Polygon to Ellipse: An Eigenanalysis,
#    SIAM Review,
#    Volume 52, Number 1, March 2010, pages 151-170.
#
#  Input:
#
#    integer N, the number of vertices.
#
#    real P(N,2), the vertices of the polygon.
#
#  Output:
#
#    real P2(N,2), the vertices of the averaged polygon.
#
  import numpy as np
#
#  Average consecutive pairs of vertices.
#
  p2 = np.vstack ( ( p[1:n,:], p[0,:] ) )
  p2 = ( p + p2 ) / 2.0
#
#  Compute the centroid.
#
  c = np.sum ( p2, axis = 0 ) / n
#
#  Shift P2 so the centroid is zero.
#
  p2[:,0] = p2[:,0] - c[0]
  p2[:,1] = p2[:,1] - c[1]
#
#  Compute the max-norms of X and Y.
#
  x_norm2 = np.max ( np.abs ( p2[:,0] ) )
  y_norm2 = np.max ( np.abs ( p2[:,1] ) )
#
#  Scale P2 so X and Y have max-norm 1.
#
  p2[:,0] = p2[:,0] / x_norm2
  p2[:,1] = p2[:,1] / y_norm2

  return p2
 
def polygon_average_test ( ):

#*****************************************************************************80
#
## polygon_average_test() tests polygon_average().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 October 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'polygon_average_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  polygon_average() repeatedly averages the vertices of a polygon.' )
#
#  Define the starting polygon.
#
  n = 10

  print ( '' )
  print ( '  Number of vertices will be', n )

  p = 2.0 * rng.random ( size = ( n, 2 ) ) - 1.0

  x = np.append ( p[:,0], p[0,0] )
  y = np.append ( p[:,1], p[0,1] )

  plt.clf ( )
  plt.plot ( x, y, 'bo-' )
  plt.grid ( True )
  plt.axis ( [ -1.0, 1.0, -1.0, 1.0 ] )
  plt.axis ( 'equal' )
  plt.title ( 'Original polygon' )
  filename = 'polygon_original.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Repeatedly average the vertices.
#
  for step in range ( 1, 21 ):

    p2 = polygon_average ( n, p )

    plt.clf ( )
    plt.grid ( True )
    plt.axis ( [ -1.0, 1.0, -1.0, 1.0 ] )
    plt.axis ( 'equal' )
    x = np.append ( p[:,0], p[0,0] )
    y = np.append ( p[:,1], p[0,1] )
    plt.plot ( x, y, 'bo-' )
    x = np.append ( p2[:,0], p2[0,0] )
    y = np.append ( p2[:,1], p2[0,1] )
    plt.plot ( x, y, 'ro-', linewidth = 3 )
    label = 'Step ' + str ( step )
    plt.title ( label )

    p = p2.copy ( )
#
#  Save an image of the last polygon.
#
  filename = 'polygon_average.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_average_test():' )
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
  polygon_average_test ( )
  timestamp ( )


