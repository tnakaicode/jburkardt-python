#! /usr/bin/env python3
#
def lissajous_plot ( ):

#*****************************************************************************80
#
## lissajous_plot draws a Lissajous curve.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 May 2016
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import platform

  print ( '' )
  print ( 'lissajous_plot:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
#
#  Terminate.
#
  print ( '' )
  print ( 'lissajous_plot:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lissajous_plot ( )
  timestamp ( )
