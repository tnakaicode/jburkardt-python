#! /usr/bin/env python3
#
def hexagon_chaos_test ( ):

#*****************************************************************************80
#
## hexagon_chaos_test() tests hexagon_chaos().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 April 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'hexagon_chaos_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  hexagon_chaos() uses an iterated map to plot a hexagon fractal.' )

  rng = default_rng ( )

  n = 5000
  print ( '  Apply the map', n, ' times.' )
  hexagon_chaos ( n, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'hexagon_chaos_test():' )
  print ( '  Normal end of execution.' )

  return

def hexagon_chaos ( n, rng ):

#*****************************************************************************80
#
## hexagon_chaos() draws a fractal by applying randomly chosen maps.
#
#  Discussion:
#
#    An initial point p inside the unit hexagon is randomly chosen.
#    On each iteration, a side of the hexagon is chosen at random,
#    and p plus this side forms a triangle.  The next p is the barycenter
#    of this triangle - which is simply the average of p and the two
#    hexagon vertices.
#
#    The set of points p will gradually display a fractal of hexagons.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    John D Cook,
#    Random Hexagon Fractal,
#    https://www.johndcook.com/blog/2026/04/09/random-hexagon-fractal/
#    Posted 09 April 2026.
#
#  Input:
#
#    integer n: the number of times the mapping is to be applied.
#
#    rng, the random number generator.
#
  import matplotlib.pyplot as plt
#
#  Define vertices of unit hexagon.
#
  v = hexagon01_vertices ( )
#
#  Pick a random starting point in the hexagon.
#
  p = hexagon01_sample ( rng )
#
#  Iterate the map n times.
#
  plt.clf ( )
#
#  Hexagon edges.
#
  i = 5
  for ip1 in range ( 0, 6 ):
    plt.plot ( [v[i,0],v[ip1,0]], [v[i,1],v[ip1,1]], 'm-', linewidth = 2 )
    i = ip1
#
#  Hexagon vertices.
#
  for i in range ( 0, 6 ):
    plt.plot ( v[i,0], v[i,1], 'b.', markersize = 15 )
#
#  Chaos points.
#
  for i in range ( 0, n ):
#
#  Randomly pick the hexagon side with vertices v(j) and v(j+1).
#
    j = rng.integers ( low = 0, high = 6, endpoint = False )
    k = ( ( j + 1 ) % 6 )
#
#  Average the current point and the two vertices.
#  We are computing the barycenter of the triangle we have formed.
#
    p = ( p + v[j,:] + v[k,:] ) / 3.0
#
#  Display the new point.
#
    plt.plot ( p[0], p[1], 'ro', markersize = 2 )

  plt.axis ( 'equal' )
  filename = 'hexagon_chaos.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def hexagon01_sample ( rng ):

#*****************************************************************************80
#
## hexagon01_sample() samples uniformly from the regular unit hexagon.
#
#  Discussion:
#
#    The unit hexagon has center (0,0) and "radius" 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
#  Output:
#
#    real P(2), the sample point.
#
  import numpy as np
#
#  Set basis vectors for each rhombus.
#
  v = np.array ( [ \
    [ -1.0,   0.0 ], \
    [  0.5,   np.sqrt ( 3.0 ) / 2.0 ], \
    [  0.5, - np.sqrt ( 3.0 ) / 2.0 ], \
    [ -1.0,   0.0 ] ] )
#
#  Assign the point randomly to rhombus 0, 1 or 2.
#
  rh = rng.integers ( low = 0, high = 2, endpoint = True )
#
#  Set barycentric coordinates of the point in its rhombus.
#
  r = rng.random ( 2 )
#
#  Convert to physical coordinates.
#
  if ( rh == 0 ):
    p = np.dot ( r[:], v[0:2,0:2] )
  elif ( rh == 1 ):
    p = np.dot ( r[:], v[1:3,0:2] )
  else:
    p = np.dot ( r[:], v[2:4,0:2] )

  return p

def hexagon01_vertices ( ):

#*****************************************************************************80
#
## hexagon01_vertices() returns the vertices of the unit hexagon.
#
#  Discussion:
#
#    The unit hexagon has maximum radius 1, and is the hull of the points
#
#      (   1,              0 ),
#      (   0.5,   sqrt (3)/2 ),
#      ( - 0.5,   sqrt (3)/2 ),
#      ( - 1,              0 ),
#      ( - 0.5, - sqrt (3)/2 ),
#      (   0.5, - sqrt (3)/2 ).
#
#      120_____60
#        /     \
#    180/       \0
#       \       /
#        \_____/
#      240     300
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2026
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real V(6,2), the coordinates of the vertices.
#
  import numpy as np

  a = np.sqrt ( 3.0 ) / 2.0

  v = np.array ( [ \
   [  1.0, 0.0 ], \
   [  0.5,   a ], \
   [ -0.5,   a ], \
   [ -1.0, 0.0 ], \
   [ -0.5,  -a ], \
   [  0.5,  -a ] ] )

  return v

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
#    06 April 2013
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
  hexagon_chaos_test ( )
  timestamp ( )

