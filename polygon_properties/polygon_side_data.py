#! /usr/bin/env python3
#
def polygon_side_data ( n, side ):

#*****************************************************************************80
#
## POLYGON_SIDE_DATA determines polygonal data from its side length.
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
#  Parameters:
#
#    Input, integer N, the number of sides of the polygon.
#    N must be at least 3.
#
#    Input, real SIDE, the length of one side of the polygon.
#
#    Output, real AREA, the area of the regular polygon.
#
#    Output, real RADIN, the inner radius of the polygon, that is,
#    the radius of the largest circle that can be inscribed within
#    the polygon.
#
#    Output, real RADOUT, the outer radius of the polygon, that is,
#    the radius of the smallest circle that can be described about
#    the polygon.
#
  import numpy as np
  from sys import exit

  if ( n < 3 ):
    print ( '' )
    print ( 'POLYGON_SIDE_DATA - Fatal error!' )
    print ( '  Input value of N must be at least 3.' )
    print ( '  but your input value was N = %d' % ( n ) )
    exit ( 'POLYGON_SIDE_DATA - Fatal error!' )

  angle = np.pi / n
  area = 0.5 * n * side * side / np.tan ( angle )
  radin = 0.5 * side / np.tan ( angle )
  radout = 0.5 * side / np.sin ( angle )

  return area, radin, radout

def polygon_side_data_test ( ):

#*****************************************************************************80
#
## POLYGON_SIDE_DATA_TEST tests POLYGON_SIDE_DATA;
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
  print ( 'POLYGON_SIDE_DATA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_SIDE_DATA uses the side length of a regular polygon' )
  print ( '  to compute the area, inradius, and outradius.' )

  for n in range ( 3, 6 ):

    print ( '' )
    print ( '  Number of polygonal sides = %d' % ( n ) )

    side = 1.0
    print ( '' )
    print ( '  Assuming SIDE = %g' % ( side ) )
    area, radin, radout = polygon_side_data ( n, side )
    print ( '    AREA =   %g' % ( area ) )
    print ( '    RADIN =  %g' % ( radin ) )
    print ( '    RADOUT = %g' % ( radout ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_SIDE_DATA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_side_data_test ( )
  timestamp ( )
