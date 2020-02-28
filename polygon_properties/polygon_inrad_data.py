#! /usr/bin/env python3
#
def polygon_inrad_data ( n, radin ):

#*****************************************************************************80
#
## POLYGON_INRAD_DATA determines polygonal data from its inner radius.
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
#    Input, real RADIN, the inner radius of the polygon, that is,
#    the radius of the largest circle that can be inscribed within
#    the polygon.
#
#    Output, real AREA, the area of the regular polygon.
#
#    Output, real RADOUT, the outer radius of the polygon, that is,
#    the radius of the smallest circle that can be described about
#    the polygon.
#
#    Output, real SIDE, the length of one side of the polygon.
#
  import numpy as np
  from sys import exit

  if ( n < 3 ):
    print ( '' )
    print ( 'POLYGON_INRAD_DATA - Fatal error!' )
    print ( '  Input value of N must be at least 3' )
    print ( '  but your input value was N = %d' % ( n ) )
    exit ( 'POLYGON_INRAD_DATA - Fatal error!' )

  angle = np.pi / n
  area = n * radin * radin * np.tan ( angle )
  side = 2.0 * radin * np.tan ( angle )
  radout = 0.5 * side / np.sin ( angle )

  return area, radout, side

def polygon_inrad_data_test ( ):

#*****************************************************************************80
#
## POLYGON_INRAD_DATA_TEST tests POLYGON_INRAD_DATA.
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
  print ( 'POLYGON_INRAD_DATA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_INRAD_DATA uses the inradius of a regular polygon' )
  print ( '  to determine the area, outradius, and side length.' )

  for n in range ( 3, 6 ):

    print ( '' )
    print ( '  Number of polygonal sides = %d' % ( n ) )

    radin = 1.0
    print ( '' )
    print ( '  Assuming RADIN = %g' % ( radin ) )
    area, radout, side = polygon_inrad_data ( n, radin )
    print ( '    AREA =   %g' % ( area ) )
    print ( '    RADOUT = %g' % ( radout ) )
    print ( '    SIDE =   %g' % ( side ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_INRAD_DATA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_inrad_data_test ( )
  timestamp ( )

