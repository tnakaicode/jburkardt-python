#! /usr/bin/env python
#
def polygon_outrad_data ( n, radout ):

#*****************************************************************************80
#
## POLYGON_OUTRAD_DATA determines polygonal data from its outer radius.
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
#    Input, real RADOUT, the outer radius of the polygon, that is,
#    the radius of the smallest circle that can be described
#    around the polygon.
#
#    Output, real AREA, the area of the regular polygon.
#
#    Output, real RADIN, the inner radius of the polygon, that is,
#    the radius of the largest circle that can be inscribed
#    within the polygon.
#
#    Output, real SIDE, the length of one side of the polygon.
#
  import numpy as np
  from sys import exit

  if ( n < 3 ):
    print ( '' )
    print ( 'POLYGON_OUTRAD_DATA - Fatal error!' )
    print ( '  Input value of N must be at least 3.' )
    print ( '  but your input value was N = %d' % ( n ) )
    exit ( 'POLYGON_OUTRAD_DATA - Fatal error!' )

  angle = np.pi / float ( n )
  area = 0.5 * float ( n ) * radout * radout * np.sin ( 2.0 * angle )
  side = 2.0 * radout * np.sin ( angle )
  radin = 0.5 * side / np.tan ( angle )

  return area, radin, side

def polygon_outrad_data_test ( ):

#*****************************************************************************80
#
## POLYGON_OUTRAD_DATA_TEST tests POLYGON_OUTRAD_DATA.
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
  print ( 'POLYGON_OUTRAD_DATA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POLYGON_OUTRAD_DATA uses the outradius of a regular polygon' )
  print ( '  to determine the area, inradius, and sidelength.' )

  for n in range ( 3, 6 ):

    print ( '' )
    print ( '  Number of polygonal sides = %d' % ( n ) )

    radout = 1.0
    print ( '' )
    print ( '  Assuming RADOUT = %g' % ( radout ) )
    area, radin, side = polygon_outrad_data ( n, radout )
    print ( '    AREA =   %g' % ( area ) )
    print ( '    RADIN =  %g' % ( radin ) )
    print ( '    SIDE =   %g' % ( side ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POLYGON_OUTRAD_DATA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  polygon_outrad_data_test ( )
  timestamp ( )
