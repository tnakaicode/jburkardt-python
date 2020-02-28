#! /usr/bin/env python
#
def triangle_area ( t ):

#*****************************************************************************80
#
## TRIANGLE_AREA computes the area of a triangle in 2D.
#
#  Discussion:
#
#    If the triangle's vertices are given in counterclockwise order,
#    the area will be positive.  If the triangle's vertices are given
#    in clockwise order, the area will be negative!
#
#    An earlier version of this routine always returned the absolute
#    value of the computed area.  I am convinced now that that is
#    a less useful result!  For instance, by returning the signed 
#    area of a triangle, it is possible to easily compute the area 
#    of a nonconvex polygon as the sum of the (possibly negative) 
#    areas of triangles formed by node 1 and successive pairs of vertices.
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
#  Parameters:
#
#    Input, real T(2,3), the triangle vertices.
#
#    Output, real AREA, the area of the triangle.
#
  area = 0.5 * ( \
      t[0,0] * ( t[1,1] - t[1,2] ) \
    + t[0,1] * ( t[1,2] - t[1,0] ) \
    + t[0,2] * ( t[1,0] - t[1,1] ) )

  return area

def triangle_area_test ( ):

#*****************************************************************************80
#
## TRIANGLE_AREA_TEST tests TRIANGLE_AREA.
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
  from r8mat_print import r8mat_print

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  print ( '' )
  print ( 'TRIANGLE_AREA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_AREA computes the area of a triangle.' )

  r8mat_print ( 2, 3, t, '  Triangle vertices (columns)' )

  area = triangle_area ( t )

  print ( '' )
  print ( '  Triangle area is %g' % ( area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_AREA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_area_test ( )
  timestamp ( )
 
