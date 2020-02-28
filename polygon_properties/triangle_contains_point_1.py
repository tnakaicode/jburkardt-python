#! /usr/bin/env python
#
def triangle_contains_point_1 ( t, p ):

#*****************************************************************************80
#
## TRIANGLE_CONTAINS_POINT_1 finds if a point is inside a triangle.
#
#  Discussion:
#
#    It is conventional to list the triangle vertices in counter clockwise
#    order.  However, this routine does not require a particular order
#    for the vertices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T(2,3), the triangle vertices.
#
#    Input, real P(2,1), the point to be checked.
#
#    Output, logical INSIDE, is TRUE if the point is inside
#    the triangle or on its boundary.
#
  from triangle_barycentric import triangle_barycentric

  xsi = triangle_barycentric ( t, p )

  if ( xsi[0] < 0.0 or xsi[1] < 0.0 or xsi[2] < 0.0 ):
    inside = False
  else:
    inside = True

  return inside
