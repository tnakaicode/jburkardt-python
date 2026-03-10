#! /usr/bin/env python3
#
def hand_area_test ( ):

#*****************************************************************************80
#
## hand_area_test() tests hand_area().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'hand_area_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hand_area().' )

  sample_num = 1000
  hand_area ( sample_num )
#
#  Terminate.
#
  print ( '' )
  print ( 'hand_area_test():' )
  print ( '  Normal end of execution.' )

  return

def hand_area ( s_num ):

#*****************************************************************************80
#
## hand_area() estimates the area of the hand in the hand data file.
#
#  Discussion:
#
#    This program assumes that the file 'hand_data.txt' is available.
#
#    It uses sampling to estimate the area contained within the hand outline.
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
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625. 
#
#  Input:
#
#    integer S_NUM, the number of sample points.
#
  from numpy.random import default_rng
  import matplotlib.pyplot as plt
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'hand_area():' )
  print ( '  Estimate the area inside a curve that approximates the' )
  print ( '  shape of a hand, using sampling.' )
#
#  1: DATA
#

#
#  Read the hand data.
#  It comes in as an Nx2 array.
#
  xy = np.loadtxt ( 'hand_data.txt' )
#
#  We will want to know how many columns there are.  Use the SIZE command.
#
  xy_num = xy.shape[0]
#
#  Determine the range of the data.
#
  x_min = np.min ( xy[:,0] )
  x_max = np.max ( xy[:,0] )
  y_min = np.min ( xy[:,1] )
  y_max = np.max ( xy[:,1] )
#
#  Compute the area of the rectangle that contains the data.
#
  area_total = ( x_max - x_min ) * ( y_max - y_min )
#
#  2.  SAMPLING
#

#
#  Get an array of 2xS_NUM random values, each in [0,1].
#
  s = rng.random ( [ s_num, 2 ] )
#
#  Shift and stretch the points to fit in the rectangle.
#
  s[:,0] = x_min + s[:,0] * ( x_max - x_min )
  s[:,1] = y_min + s[:,1] * ( y_max - y_min )
#
#  Set up a vector Z to record if each sample point is inside (True)
#  or outside (False) the hand curve.
#
  z = np.zeros ( s_num, dtype = bool )
  j_num = 0
  k_num = 0
  for j in range ( 0, s_num ):
    z[j] = polygon_contains_point ( xy_num, xy, s[j,:] )
    if ( z[j] ):
      j_num = j_num + 1
    else:
      k_num = k_num + 1
#
#  Estimate the hand area using the proportion of sample points that landed
#  inside the hand.
#
  area_hand = area_total * j_num / s_num

  print ( '' )
  print ( '  Number of sample points = ', s_num )
  print ( '  Total area = ', area_total )
  print ( '  Estimated hand area = ', area_hand )
#
#  Since the hand is a polygon, we can actually compute the exact area.
#
  area_hand2 = polygon_area ( xy_num, xy )
  print ( '  Exact hand area = ', area_hand2 )
  e = np.abs ( area_hand - area_hand2 )
  print ( '  Error = ', e )
#
#  3: GRAPHICS
#

#
#  For graphics convenience only, append a copy of the first point
#  to the end, so the polygon is closed.
#
  xy = np.vstack ( ( xy, [xy[0,0],xy[0,1]] ) )
#
#  Clear any old graphics information from the screen.
#
  plt.clf ( )
#
#  Plot:
#    the hand curve (cyan)
#    the hand data points (blue)
#    the sample points inside the hand (red)
#    the sample points outside the hand (green)
#
  plt.plot ( xy[:,0], xy[:,1], 'c-', linewidth = 4 )
  plt.plot ( xy[:,0], xy[:,1], 'b.', markersize = 10 )
  for j in range ( 0, s_num ):
    if ( z[j] ):
      plt.plot ( s[j,0], s[j,1], 'r.', markersize = 10 )
    else:
      plt.plot ( s[j,0], s[j,1], 'g.', markersize = 10 )
#
#  Use the same scale for X and Y.
#  Draw grid lines.
#  Print a title.
#
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.title ( 'Samples inside (red) and outside (green) the hand data' )
#
#  Save a copy to a file.
#
  filename = 'hand_area.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'hand_area():' )
  print ( '  Normal end of execution.' )

  return

def i4_wrap ( value, lo, hi ):

#*****************************************************************************80
#
## i4_wrap() forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    LO = 4, HI = 8
#
#    In   Out
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer VALUE, an integer value.
#
#    integer LO, HI, the desired bounds for the integer value.
#
#  Output:
#
#    integer VALUE, a "wrapped" version of VALUE.
#
  value = lo + ( ( value - lo ) % ( hi - lo + 1 ) )

  return value

def polygon_area ( n, v ):

#*****************************************************************************80
#
## polygon_area() computes the area of a polygon.
#
#  Discussion:
#
#    AREA = 1/2 * abs ( sum ( 1 <= I <= N ) X(I) * ( Y(I+1) - Y(I-1) ) )
#    where Y(0) should be replaced by Y(N), and Y(N+1) by Y(1).
#
#    If the vertices are given in counterclockwise order, the area
#    will be positive.  If the vertices are given in clockwise order,
#    the area will be negative.
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
#    integer N, the number of vertices of the polygon.
#
#    real V(N,2), the vertices.
#
#  Output:
#
#    real AREA, the area of the polygon.
#
  area = 0.0

  for i in range ( 0, n ):

    im1 = i4_wrap ( i - 1, 0, n - 1 )
    ip1 = i4_wrap ( i + 1, 0, n - 1 )

    area = area + v[i,0] * ( v[ip1,1] - v[im1,1] )

  area = 0.5 * area

  return area

def polygon_contains_point ( n, v, p ):

#*****************************************************************************80
#
## polygon_contains_point() finds if a point is inside a convex polygon.
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
#    integer N, the number of nodes or vertices in the polygon.
#    N must be at least 3.
#
#    real V(N,2), the coordinates of the vertices of the polygon.
#
#    real P(2), the coordinates of the point to be tested.
#
#  Output:
#
#    bool INSIDE, is TRUE if the point is inside the polygon.
#
  import numpy as np

  inside = False
#
#  A point is inside a convex polygon if and only if it is inside
#  one of the triangles formed by X(1),Y(1) and any two consecutive
#  points on the polygon's circumference.
#
  t = np.zeros ( [ 3, 2 ] )

  t[0,0] = v[0,0]
  t[0,1] = v[0,1]

  for i in range ( 1, n - 1 ):

    t[1,0] = v[i,0]
    t[1,1] = v[i,1]
    t[2,0] = v[i+1,0]
    t[2,1] = v[i+1,1]

    inside = triangle_contains_point_1 ( t, p )

    if ( inside ):
      break

  return inside

def triangle_barycentric ( t, p ):

#*****************************************************************************80
#
## triangle_barycentric() finds the barycentric coordinates of a point.
#
#  Discussion:
#
#    The barycentric coordinate of point X related to vertex A can be
#    interpreted as the ratio of the area of the triangle with
#    vertex A replaced by vertex X to the area of the original
#    triangle.
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
#    real T(3,2), the triangle vertices.
#    The vertices should be given in counter clockwise order.
#
#    real P(2), the point to be checked.
#
#  Output:
#
#    real XSI(3), the barycentric coordinates of (X,Y).
#
  import numpy as np

  nrhs = 1
#
#  Set up the linear system
#
#    ( X1-X0  X2-X0 ) XSI(0)  = X-X0
#    ( Y1-Y0  Y2-Y0 ) XSI(1)    Y-Y0
#
#  which is satisfied by the barycentric coordinates of (X,Y).
#
  A = np.zeros ( [ 2, 2 ] )
  A[0,0] = t[1,0] - t[0,0]
  A[0,1] = t[2,0] - t[0,0]
  A[1,0] = t[1,1] - t[0,1]
  A[1,1] = t[2,1] - t[0,1]

  b = np.zeros ( 2 )
  b[0] = p[0]   - t[0,0]
  b[1] = p[1]   - t[0,1]
#
#  Solve the linear system.
#
  xsi = np.zeros ( 3 )
  xsi[0:2] = np.linalg.solve ( A, b )
  xsi[2] = 1.0 - xsi[0] - xsi[1]

  return xsi

def triangle_contains_point_1 ( t, p ):

#*****************************************************************************80
#
## triangle_contains_point_1() finds if a point is inside a triangle.
#
#  Discussion:
#
#    It is conventional to list the triangle vertices in counter clockwise
#    order.  However, this routine does not require a particular order
#    for the vertices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(3,2), the triangle vertices.
#
#    real P(2), the point to be checked.
#
#  Output:
#
#    bool INSIDE, is TRUE if the point is inside
#    the triangle or on its boundary.
#
  xsi = triangle_barycentric ( t, p )

  if ( xsi[0] < 0.0 or xsi[1] < 0.0 or xsi[2] < 0.0 ):
    inside = False
  else:
    inside = True

  return inside

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
  hand_area_test ( )
  timestamp ( )

