#! /usr/bin/env python
#
def triangle_centroid ( t ):

#*****************************************************************************80
#
## TRIANGLE_CENTROID computes the centroid of a triangle in 2D.
#
#  Discussion:
#
#    The centroid of a triangle can also be considered the
#    center of gravity, or center of mass, assuming that the triangle
#    is made of a thin uniform sheet of massy material.
#
#    The centroid of a triangle is the intersection of the medians.
#
#    A median of a triangle is a line connecting a vertex to the
#    midpoint of the opposite side.
#
#    In barycentric coordinates, in which the vertices of the triangle
#    have the coordinates (1,0,0), (0,1,0) and (0,0,1), the centroid
#    has coordinates (1/3,1/3,1/3).
#
#    In geometry, the centroid of a triangle is often symbolized by "G".
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Adrian Bowyer and John Woodwark,
#    A Programmer's Geometry,
#    Butterworths, 1983.
#
#  Parameters:
#
#    Input, real T(2,3), the triangle vertices.
#
#    Output, real CENTROID(2), the coordinates of the centroid.
#
  import numpy as np

  centroid = np.zeros ( 2 )

  for i in range ( 0, 2 ):
    for j in range ( 0, 3 ):
      centroid[i] = centroid[i] + t[i,j]
    centroid[i] = centroid[i] / 3.0

  return centroid

def triangle_centroid_test ( ):

#*****************************************************************************80
#
## TRIANGLE_CENTROID_TEST tests TRIANGLE_CENTROID;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_transpose_print import r8mat_transpose_print
  from r8vec_print import r8vec_print

  ntest = 4

  print ( '' )
  print ( 'TRIANGLE_CENTROID_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_CENTROID computes the centroid of a triangle' )

  for i in range ( 0, ntest ):

    if ( i == 0 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.0 ], \
        [ 0.0, 0.0, 1.0 ] ] )
    elif ( i == 1 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.5 ], \
        [ 0.0, 0.0, 0.86602539 ] ] )
    elif ( i == 2 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 0.5 ], \
        [ 0.0, 0.0, 10.0 ] ] )
    elif ( i == 3 ):
      t = np.array ( [ \
        [ 0.0, 1.0, 10.0 ], \
        [ 0.0, 0.0, 2.0 ] ] )

    r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

    centroid = triangle_centroid ( t )

    r8vec_print ( 2, centroid, '  Centroid:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_CENTROID_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_centroid_test ( )
  timestamp ( )
