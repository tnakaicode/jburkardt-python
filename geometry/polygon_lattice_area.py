#! /usr/bin/env python
#
def polygon_lattice_area ( i, b ):

#*****************************************************************************80
#
## POLYGON_LATTICE_AREA computes the area of a lattice polygon.
#
#  Discussion:
#
#    We define a lattice to be the 2D plane, in which the points
#    whose (X,Y) coordinates are both integers are given a special
#    status as "lattice points".
#
#    A lattice polygon is a polygon whose vertices are lattice points.
#
#    The area of a lattice polygon can be computed by Pick's Theorem:
#
#      Area = I + B / 2 - 1
#
#    where
#
#      I = the number of lattice points contained strictly inside the polygon;
#
#      B = the number of lattice points that lie exactly on the boundary.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Branko Gruenbaum and G C Shephard,
#    Pick's Theorem,
#    The American Mathematical Monthly,
#    Volume 100, 1993, pages 150-161.
#
#  Parameters:
#
#    Input, integer I, the number of interior lattice points.
#
#    Input, integer B, the number of boundary lattice points.
#
#    Output, real AREA, the area of the lattice polygon.
#
  area = i + b / 2.0 - 1.0

  return area

def polygon_lattice_area_test ( ):

#*****************************************************************************80
#
## POLYGON_LATTICE_AREA_TEST tests POLYGON_LATTICE_AREA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'POLYGON_LATTICE_AREA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_LATTICE_AREA returns the "area"' )
  print ( '  of a polygon, measured in lattice points.' )

  i = 5
  b = 6

  print ( '' )
  print ( '  Number of interior lattice points = %d' % ( i ) )
  print ( '  Number of boundary lattice points = %d' % ( b ) )

  area = polygon_lattice_area ( i, b )

  print ( '  Area of polygon is %g' % ( area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_LATTICE_AREA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_lattice_area_test ( )
  timestamp ( )

