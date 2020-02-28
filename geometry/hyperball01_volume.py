#! /usr/bin/env python
#
def hyperball01_volume ( m ):

#*****************************************************************************80
#
## HYPERBALL01_VOLUME returns the volume of the unit hyperball in M dimensions.
#
#  Discussion:
#
#     M  Volume
#
#     1    2
#     2    1        * PI
#     3  ( 4 /   3) * PI
#     4  ( 1 /   2) * PI^2
#     5  ( 8 /  15) * PI^2
#     6  ( 1 /   6) * PI^3
#     7  (16 / 105) * PI^3
#     8  ( 1 /  24) * PI^4
#     9  (32 / 945) * PI^4
#    10  ( 1 / 120) * PI^5
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real VOLUME, the volume of the unit ball.
#
  import numpy as np

  if ( ( m % 2 ) == 0 ):
    m_half = ( m // 2 );
    volume = np.pi ** m_half
    for i in range ( 1, m_half + 1 ):
      volume = volume / float ( i )
  else:
    m_half = ( ( m - 1 ) // 2 )
    volume = np.pi ** m_half * 2.0 ** m
    for i in range ( m_half + 1, 2 * m_half + 2 ):
      volume = volume / float ( i )

  return volume

def hyperball01_volume_test ( ) :

#*****************************************************************************80
#
## HYPERBALL01_VOLUME tests HYPERBALL01_VOLUME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'HYPERBALL01_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HYPERBALL01_VOLUME returns the volume of the unit hyperball' )
  print ( '  in M dimensions.' )
  print ( '' )
  print ( '   M  Volume' )
  print ( '' )

  for m in range ( 1, 11 ):
    value = hyperball01_volume ( m )
    print ( '  %2d  %g' % ( m, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'HYPERBALL01_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hyperball01_volume_test ( )
  timestamp ( )

