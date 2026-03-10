#! /usr/bin/env python3
#
def animation_test ( ):

#*****************************************************************************80
#
## animation_test() tests the creation of animations in Python.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 November 2024
#
#  Author:
#
#    John Burkardt
#
  from allen_cahn_animation import allen_cahn_animation
  from gif_animation import gif_animation
  import numpy as np
  import platform

  print ( '' )
  print ( 'animation_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test animation in Python.' )

  allen_cahn_animation ( )
  arenstorf_animation ( )
  cos_animation ( )
  curve_animation ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'animation_test():' )
  print ( '  Normal end of execution.' )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == "__main__" ):
  timestamp ( )
  animation_test ( )
  timestamp ( )
