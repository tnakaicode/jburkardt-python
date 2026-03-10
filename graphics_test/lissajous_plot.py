#! /usr/bin/env python3
#
def lissajous_plot ( ):

#*****************************************************************************80
#
## lissajous_plot() draws a Lissajous curve.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 May 2016
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
  print ( 'lissajous_plot():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Make a plane curve by connecting a series of points.' )
#
#  Read the data from the file.
#
  x = []
  y = []

  file = open ( 'lissajous_data.txt', 'r' )

  for line in file:
    line = line.strip ( )
    columns = line.split ( )
    x.append ( float ( columns[0] ) )
    y.append ( float ( columns[1] ) )

  file.close ( )
#
#  Plot the data.
#
  plt.plot ( x, y, linewidth = 2, color = 'm' )
#
#  To avoid clutter, only plot every 10th point.
#
  plt.plot ( x[::10], y[::10], 'ko' )
  plt.grid ( True )
  plt.axis ( [ -1.2, +1.2, -1.2, +1.2 ] )
  plt.axis ( 'Equal' )
  plt.xlabel ( '<--- X --->', fontsize = 16 )
  plt.ylabel ( '<--- Y --->', fontsize = 16 )
  plt.title ( 'Lissajous, x=sin(3t+pi/2), y=sin(4t)', fontsize = 16 )

  filename = 'lissajous_plot.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'lissajous_plot():' )
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
#    06 April 2013
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
  lissajous_plot ( )
  timestamp ( )
