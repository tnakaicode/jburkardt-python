#! /usr/bin/env python3
#
def brownian_2d_plot ( ):

#*****************************************************************************80
#
## brownian_2d_plot() plots Brownian motion in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2019
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
  print ( 'brownian_2d_plot():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Plot Brownian motion in two dimensions.' )
#
#  Read data from the file.
#
  filename = 'brownian_2d_data.txt'
  data = np.loadtxt ( filename )
  x = data[:,0]
  y = data[:,1]
  n = len ( x )
#
#  Plot the data.
#
  plt.plot ( x, y, linewidth = 2, color = 'b' )
  plt.plot ( x[0], y[0], 'g.', markersize = 35 )
  plt.plot ( x[n-1], y[n-1], 'r.', markersize = 35 )
  plt.grid ( True )
  plt.axis ( 'equal' )
  plt.xlabel ( '<--- X --->', fontsize = 16 )
  plt.ylabel ( '<--- Y --->', fontsize = 16 )
  plt.title ( 'Brownian motion in two dimensions', fontsize = 16 )

  filename = 'brownian_2d_plot.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'brownian_2d_plot():' )
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
  brownian_2d_plot ( )
  timestamp ( )
 
