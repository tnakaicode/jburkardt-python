#! /usr/bin/env python
#
def disk01_quarter_area ( ):

#*****************************************************************************80
#
## DISK01_QUARTER_AREA returns the area of the unit quarter_disk.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real AREA, the area.
#
  import numpy as np

  value = np.pi / 4.0

  return value

def disk01_quarter_area_test ( ) :

#*****************************************************************************80
#
## DISK01_QUARTER_AREA tests DISK01_QUARTER_AREA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 May 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'DISK01_QUARTER_AREA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DISK01_QUARTER_AREA returns the area of the unit quarter disk.' )

  value = disk01_quarter_area ( )

  print ( '' )
  print ( '  DISK01_QUARTER_AREA() = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DISK01_QUARTER_AREA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  disk01_quarter_area_test ( )
  timestamp ( )

