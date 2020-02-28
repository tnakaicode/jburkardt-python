#! /usr/bin/env python
#
def simplex01_volume ( m ):

#*****************************************************************************80
#
## SIMPLEX01_VOLUME returns the volume of the unit simplex in M dimensions.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the spatial dimension.
#
#    Output, real VALUE, the volume.
#
  value = 1.0
  for i in range ( 1, m + 1 ):
    value = value / float ( i )

  return value

def simplex01_volume_test ( ) :

#*****************************************************************************80
#
## SIMPLEX01_VOLUME_TEST tests SIMPLEX01_VOLUME.
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
  print ( 'SIMPLEX01_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SIMPLEX01_VOLUME returns the volume of the unit simplex' )
  print ( '  in M dimensions.' )
  print ( '' )
  print ( '   M   Volume' )
  print ( '' )

  for m in range ( 1, 10 ):
    value = simplex01_volume ( m )
    print ( '  %2d  %g' % ( m, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SIMPLEX01_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  simplex01_volume_test ( )
  timestamp ( )

