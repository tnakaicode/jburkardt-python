#! /usr/bin/env python3
#
def ConvexHull_test ( ):

#*****************************************************************************80
#
## ConvexHull_test() tests the scipy ConvexHull() function on several cases.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 March 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  import scipy as sp

  print ( '' )
  print ( 'ConvexHull_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  scipy version:  ' + sp.version.version )
  print ( '  ConvexHull() is a scipy.spatial function which computes' )
  print ( '  the convex hull of a set of points.' )

  points = eddy ( )
  ConvexHull_test_case ( points, 'eddy' )

  points = graham ( )
  ConvexHull_test_case ( points, 'graham' )

  points = kn57 ( )
  ConvexHull_test_case ( points, 'kn57' )

  points = np.random.rand ( 30, 2 )
  ConvexHull_test_case ( points, 'random' )

  return

def ConvexHull_test_case ( points, prefix ):

#*****************************************************************************80
#
## ConvexHull_test_case() tests ConvexHull() on a specific case.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real points[n,2]: a set of points whose convex hull is to be computed.
#
#    string prefix: an identifier for the case.
#
  from scipy.spatial import ConvexHull
  from scipy.spatial import convex_hull_plot_2d
  import matplotlib.pyplot as plt

  hull = ConvexHull ( points )

  plt.clf ( )
#
#  Plot the points.
#
  plt.plot ( points[:,0], points[:,1], 'bo' )
#
#  Plot the outline of the hull.
#
  plt.plot ( points[hull.vertices,0], points[hull.vertices,1], 'r--', lw = 2 )
#
#  Don't forget the line segment from last point to first point!
#
  plt.plot ( 
    [ points[hull.vertices[-1],0], points[hull.vertices[0],0] ],
    [ points[hull.vertices[-1],1], points[hull.vertices[0],1] ], 'r--', lw = 2 )

  plt.title ( prefix )
  plt.axis ( 'equal' )
  filename = 'ConvexHull_' + prefix + '.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

def eddy ( ):

#*****************************************************************************80
#
## eddy() returns a set of points whose convex hull is desired.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real points[20,2]: the points.
#
  import numpy as np

  points = np.array ( [ \
    [  2.00,  0.00 ], \
    [  1.73, -1.00 ], \
    [  1.00,  1.73 ], \
    [  0.00,  2.00 ], \
    [  0.10,  0.10 ], \
    [ -1.00, -1.73 ], \
    [  0.20, -0.20 ], \
    [ -1.73,  1.00 ], \
    [ -0.30,  0.30 ], \
    [  0.00, -2.00 ], \
    [ -0.40, -0.40 ], \
    [ -2.00,  0.00 ], \
    [  0.50,  0.50 ], \
    [  1.73,  1.00 ], \
    [  0.60, -0.60 ], \
    [ -1.00,  1.73 ], \
    [ -0.70,  0.70 ], \
    [ -1.73, -1.00 ], \
    [ -0.80, -0.80 ], \
    [  1.00, -1.73 ] ] )

  return points

def graham ( ):

#*****************************************************************************80
#
## graham() returns a set of points whose convex hull is desired.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real points[11,2]: the points.
#
  import numpy as np

  points = np.array ( [ \
    [  7,  4 ], \
    [  6,  5 ], \
    [  3,  3 ], \
    [  0,  5 ], \
    [ -2,  3 ], \
    [ -2,  2 ], \
    [ -5,  1 ], \
    [  0,  0 ], \
    [ -3, -2 ], \
    [  3, -2 ], \
    [  2,  1 ] ] )

  return points

def kn57 ( ):

#*****************************************************************************80
#
## kn57() returns a set of points whose convex hull is desired.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 March 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real points[57,2]: the points.
#
  import numpy as np

  points = np.array ( [ \
    [ -2.06990,       33.1419 ], \
    [ -652.782,      -32.7306 ], \
    [ -99.5826,       368.102 ], \
    [ -681.204,      -195.968 ], \
    [  501.306,      -1060.52 ], \
    [  188.407,       664.309 ], \
    [  162.558,       189.839 ], \
    [  46.0342,      -1322.17 ], \
    [  2.06628,      -329.396 ], \
    [ -175.211,      -120.239 ], \
    [  32.8010,       28.0221 ], \
    [ -97.9094,      -46.8562 ], \
    [ -735.028,      -876.999 ], \
    [ -95.3201,      -1332.47 ], \
    [ -10.3429,      -668.916 ], \
    [  85.4978,      -59.6836 ], \
    [ -321.164,      -289.105 ], \
    [ -47.6442,      -175.748 ], \
    [ -17.6695,       343.754 ], \
    [  599.268,      -1719.31 ], \
    [ -984.741,      -815.440 ], \
    [ -154.114,      -225.868 ], \
    [ -800.323,      -418.586 ], \
    [ -906.238,       160.767 ], \
    [ -257.497,      -577.921 ], \
    [ -219.171,      -729.470 ], \
    [  89.8398,      -117.206 ], \
    [ -616.071,      -570.802 ], \
    [ -519.394,      -2322.04 ], \
    [ -269.658,      -181.698 ], \
    [ -567.949,      -427.349 ], \
    [  115.172,      -370.724 ], \
    [  267.077,      -668.629 ], \
    [ -464.425,      -218.200 ], \
    [ -984.451,      -408.854 ], \
    [  1.84420,       530.073 ], \
    [ -24.9747,      -814.513 ], \
    [ -83.9815,      -423.290 ], \
    [ -46.1370,       447.656 ], \
    [ -642.575,      -1904.29 ], \
    [  290.789,      -1068.03 ], \
    [ -21.3996,       131.598 ], \
    [  585.683,      -2426.60 ], \
    [ -438.513,       339.157 ], \
    [ -265.639,      -441.173 ], \
    [  84.2537,      -1791.43 ], \
    [ -107.111,      -2544.79 ], \
    [  772.383,      -2323.59 ], \
    [  728.356,      -2024.41 ], \
    [ -163.674,      -418.096 ], \
    [ -372.668,      -638.733 ], \
    [ -1088.30,       181.380 ], \
    [  20.3818,      -87.0339 ], \
    [ -220.034,      -798.150 ], \
    [ -464.384,      -803.393 ], \
    [ -136.879,       355.881 ], \
    [ -335.392,      -903.372 ] ] )

  return points

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
  ConvexHull_test ( )
  timestamp ( )

