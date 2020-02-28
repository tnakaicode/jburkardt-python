#! /usr/bin/env python
#
def hypersphere01_area ( m ):

#*****************************************************************************80
#
## HYPERSPHERE01_AREA returns the surface area of the unit hypersphere.
#
#  Discussion:
#
#     M   Area
#
#     2    2        * PI
#     3    4        * PI
#     4  ( 2 /   1) * PI^2
#     5  ( 8 /   3) * PI^2
#     6  ( 1 /   1) * PI^3
#     7  (16 /  15) * PI^3
#     8  ( 1 /   3) * PI^4
#     9  (32 / 105) * PI^4
#    10  ( 1 /  12) * PI^5
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 January 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real VALUE, the area of the unit hypersphere.
#
  import numpy as np

  if ( ( m % 2 ) == 0 ):
    m_half = ( m // 2 )
    value = 2.0 * np.pi ** m_half
    for i in range (  1, m_half ):
      value = value / float ( i )
  else:
    m_half = ( ( m - 1 ) // 2 )
    value = np.pi ** m_half * 2.0 ** m
    for i in range ( m_half + 1, 2 * m_half + 1 ):
      value = value / float ( i )

  return value

def hypersphere01_area_test ( ) :

#*****************************************************************************80
#
## HYPERSPHERE01_AREA_TEST tests HYPERSPHERE01_AREA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'HYPERSPHERE01_AREA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HYPERSPHERE01_AREA returns the volume of the unit hypersphere.' )
  print ( '' )
  print ( '   M  Area' )
  print ( '' )

  for m in range ( 1, 11 ):
    value = hypersphere01_area ( m )
    print ( '  %2d  %g' % ( m, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'HYPERSPHERE01_AREA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hypersphere01_area_test ( )
  timestamp ( )

