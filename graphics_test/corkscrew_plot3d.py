#! /usr/bin/env python3
#
def corkscrew_plot3d ( ):

#*****************************************************************************80
#
## corkscrew_plot3d() makes a plot of a 3D curve that looks like a corkscrew.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2018
#
#  Author:
#
#    John Burkardt
#
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'corkscrew_plot3d():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Display a curve defined by points on a 3D curve.' )
#
#  Define N points (X,Y,Z) along a curve.
#
  n = 101
  z = np.linspace ( -2.0, 2.0, n );
  r = z ** 2 + 1.0
  theta = np.linspace ( - 6.0 * np.pi, + 6.0 * np.pi, n )
  x = r * np.sin ( theta )
  y = r * np.cos ( theta )
#
#  Save the data to a file.
#
  filename = 'corkscrew_data.txt'
  output = open ( filename, 'w' )

  for i in range ( 0, n ):
    s = '  %g  %g  %g\n' % ( x[i], y[i], z[i] )
    output.write ( s )

  output.close ( )

  print ( '' )
  print ( '  Data saved as "' + filename + '"' )
#
#  Plot the data.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot ( x, y, z, linewidth = 3 )
  ax.grid ( True )
  ax.set_xlabel ( '<-- X -->', fontsize = 16 )
  ax.set_ylabel ( '<-- Y -->', fontsize = 16 )
  ax.set_zlabel ( '<-- Z -->', fontsize = 16 )
  ax.set_title ( 'A 3D "corkscrew" curve' )
  
  filename = 'corkscrew_plot3d.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'corkscrew_plot3d():' )
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
  corkscrew_plot3d ( )
  timestamp ( )
 
