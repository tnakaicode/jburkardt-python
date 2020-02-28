#! /usr/bin/env python
#
def triangle01_area ( ):

#*****************************************************************************80
#
## TRIANGLE01_AREA computes the area of the unit triangle in 2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 January 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real AREA, the area.
#
  area = 0.5

  return area

def triangle01_area_test ( ):

#*****************************************************************************80
#
## TRIANGLE01_AREA_TEST tests TRIANGLE01_AREA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 November 2016
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
  print ( 'TRIANGLE01_AREA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE01_AREA computes the area of the unit triangle.' )

  r8mat_print ( 2, 3, t, '  Triangle vertices (columns)' )

  area = triangle01_area ( )

  print ( '' )
  print ( '  Triangle area is %g' % ( area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE01_AREA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle01_area_test ( )
  timestamp ( )
 
