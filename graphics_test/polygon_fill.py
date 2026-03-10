#! /usr/bin/env python3
#
def polygon_fill ( ):

#*****************************************************************************80
#
## polygon_fill() makes a plot of filled polygons.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 May 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'polygon_fill():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Create a plot using filled polygons.' )
#
#  Read the values from the file.
#
  x1 = [ 0, 3, 3, 0 ]
  y1 = [ 0, 0, 1, 1 ]
  c1 = 'c'

  x2 = [ 3, 4, 4, 2, 2, 3 ]
  y2 = [ 0, 0, 2, 2, 1, 1 ]
  c2 = 'r'

  x3 = [ 0, 2, 2, 1, 1, 0 ]
  y3 = [ 1, 1, 2, 2, 4, 4 ]
  c3 = 'b'
#
#  Create the bar plot.
#
  plt.clf ( )
  plt.fill ( x1, y1, c1, x2, y2, c2, x3, y3, c3 )
  plt.grid ( True )
  plt.axis ( 'Equal' )
  plt.title ( 'Three polygons' )
  filename = 'polygon_fill.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_fill():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  polygon_fill ( )

