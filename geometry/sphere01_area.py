#! /usr/bin/env python
#
def sphere01_area ( ):

#*****************************************************************************80
#
## SPHERE01_AREA returns the area of the surface of the unit sphere in 3D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the area.
#
  import numpy as np

  r = 1.0
  value = 4.0 * np.pi * r * r

  return value

def sphere01_area_test ( ) :

#*****************************************************************************80
#
## SPHERE01_AREA_TEST tests SPHERE01_AREA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SPHERE01_AREA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SPHERE01_AREA returns the volume of the unit sphere.' )
  print ( '' )

  value = sphere01_area ( )

  print ( '  SPHERE01_AREA() =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SPHERE01_AREA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sphere01_area_test ( )
  timestamp ( )

