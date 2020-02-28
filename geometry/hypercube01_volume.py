#! /usr/bin/env python
#
def hypercube01_volume ( m ):

#*****************************************************************************80
#
## HYPERCUBE01_VOLUME returns the volume of the unit hypercube in M dimensions.
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
#    Output, real VALUE, the volume.
#
  value = 1.0

  return value

def hypercube01_volume_test ( ) :

#*****************************************************************************80
#
## HYPERCUBE01_VOLUME tests HYPERCUBE01_VOLUME.
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
  print ( 'HYPERCUBE01_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HYPERCUBE01_VOLUME returns the volume of the unit hypercube' )
  print ( '  in M dimensions.' )

  m = 3

  value = hypercube01_volume ( m )

  print ( '' )
  print ( '  HYPERCUBE01_VOLUME(%d) = %g' % ( m, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'HYPERCUBE01_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hypercube01_volume_test ( )
  timestamp ( )

