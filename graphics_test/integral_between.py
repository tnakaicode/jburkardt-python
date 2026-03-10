#! /usr/bin/env python3
#
def integral_between ( ):

#*****************************************************************************80
#
## integral_between() suggests how an integral relates to area under a curve.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 May 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'integral_between():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Plot a curve, and fill some of the area between it' )
  print ( '  and the x-axis.' )

# make data

  x1 = np.linspace ( -0.25, 6.5, 101 )
  y1 = np.sin ( x1 )

  x2 = np.linspace ( np.pi / 3.0, np.pi, 101 )
  y2_hi = np.sin ( x2 )
  y2_lo = np.zeros ( 101 )

  x3 = np.linspace ( np.pi, 4.0 * np.pi / 3.0, 101 )
  y3_hi = np.sin ( x3 )
  y3_lo = np.zeros ( 101 )
#
#  Plot the curve, the positive and negative areas, and the axis.
#
  plt.plot ( x1, y1, 'k-', linewidth = 2 )
  plt.fill_between ( x2, y2_lo, y2_hi, linewidth = 0 )
  plt.fill_between ( x3, y3_lo, y3_hi, linewidth = 0, color = 'r')
  plt.plot ( [ -0.25, 6.5 ], [ 0.0, 0.0 ], 'k--' )

  plt.grid ( True )
  plt.title ( 'Integral = Blue area - red area' )
  plt.xlabel ( '<-- x -->' )
  plt.ylabel ( '<-- y = sin(x) -->' )
  filename = 'integral_between.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )

if ( __name__ == '__main__' ):
  integral_between ( )

