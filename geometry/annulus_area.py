#! /usr/bin/env python
#
def annulus_area ( r1, r2 ):

#*****************************************************************************80
#
## ANNULUS_AREA computes the area of a circular annulus in 2D.
#
#  Discussion:
#
#    A circular annulus with center (XC,YC), inner radius R1 and
#    outer radius R2, is the set of points (X,Y) so that
#
#      R1^2 <= (X-XC)^2 + (Y-YC)^2 <= R2^2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R1, R2, the inner and outer radii of the annulus.
#
#    Output, real AREA, the area of the annulus.
#
  import numpy as np

  area = np.pi * ( r2 + r1 ) * ( r2 - r1 )

  return area

def annulus_area_test ( ):

#*****************************************************************************80
#
## ANNULUS_AREA_TEST tests ANNULUS_AREA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  pc = np.array ( [ 5.0, 3.0 ] )
  r1 = 2.0
  r2 = 3.0

  print ( '' )
  print ( 'ANNULUS_AREA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ANNULUS_AREA computes the centroid of a' )
  print ( '  circular annulus.' )
  print ( '' )
  print ( '  The circle has center        %f  %f' % ( pc[0], pc[1] ) )
  print ( '  The inner radius is R1 =     %f' % ( r1 ) )
  print ( '  The outer radius is R2 =     %f' % ( r2 ) )

  area = annulus_area ( r1, r2 )

  print ( '' )
  print ( '  Area: %f' % ( area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ANNULUS_AREA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  annulus_area_test ( )
  timestamp ( )
