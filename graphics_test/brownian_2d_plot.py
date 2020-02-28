#! /usr/bin/env python3
#
def brownian_2d_plot ( ):

#*****************************************************************************80
#
## brownian_2d plots Brownian motion in 2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'brownian_2d_plot:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )

  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'brownian_2d_plot' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  brownian_2d_plot ( )
  timestamp ( )
 
