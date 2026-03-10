#! /usr/bin/env python3
#
def cos_animation ( ):

#*****************************************************************************80
#
## cos_animation() creates an animation as a GIF file.
#
#  Discussion:
#
#    The animation depicts successive images of the function
#
#      y(x,t) = cos ( x * t )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2024
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import os
  import platform

  print ( '' )
  print ( 'cos_animation():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Create a sequence of graphic figures.' )
  print ( '  Save each one to a png file.' )
  print ( '  Use "convert()" to create a gif animation.' )
#
#  Set the x values.
#
  x = np.linspace ( 0.0, 10.0, 101 )
#
#  Generate 51 frames 0 <= t <= 5.0.
#
  for k in range ( 0, 51 ):

    t = k / 10.0
    y = np.cos ( x * t )
    plt.clf ( )
    plt.plot ( x, y, linewidth = 3 )
    plt.grid ( True )
    plt.xlabel ( "x" )
    plt.ylabel ( "y" )
    s = 'y=cos( x *' + str ( t ) + ' )'
    plt.title ( s )
#
#  Save each figure to a file.
#
    filename = 'cos_%05d.png' % ( k )
    plt.savefig (  filename )
#
#  Merge png images into a gif.
#
  print ( '  Use "convert()" to merge png files into "cos_animation.gif".' )
  os.system ( "convert -delay 10 -loop 1 cos_*.png cos_animation.gif" )
#
#  Cleanup
#
  print ( '  Remove "cos_*.png" files.' )
  os.system ( "rm cos_*.png" )
#
#  Terminate.
#
  print ( '' )
  print ( 'cos_animation():' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  cos_animation ( )
  timestamp ( )

