#! /usr/bin/env python3
#
def corkscrew_plot3d ( ):

#*****************************************************************************80
#
## corkscrew_plot3d makes a plot of a 3D curve that looks like a corkscrew.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 April 2018
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform
  from mpl_toolkits.mplot3d import Axes3D

  print ( '' )
  print ( 'corkscrew_plot3d:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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
  print ( '  Data saved as "%s"' % ( filename ) )
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
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )

  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'corkscrew_plot3d:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  corkscrew_plot3d ( )
  timestamp ( )
 
