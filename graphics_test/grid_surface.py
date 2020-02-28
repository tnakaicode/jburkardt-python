#! /usr/bin/env python3
#
def grid_surface ( ):

#*****************************************************************************80
#
## grid_surface draws a surface from a table Z(X,Y).
#
#  Discussion:
#
#    Here, the grid is a 41x41 array of equally spaced points in [-2,2]x[-2,2].
#
#      x = linspace ( -2.0, +2.0, 41 );
#      y = linspace ( -2.0, +2.0, 41 );
#      [ X, Y ] = meshgrid ( x, y );
#
#    and Z(X,Y) is a function which could be evaluated by:
#
#      Z = exp ( - ( X^2 + Y^2 ) ) ...
#       * cos ( 0.25 * X ) ...
#       * sin ( Y ) ...
#       * cos ( 2 * (X^2 + Y^2 ) );
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
  import numpy as np
  import platform
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm

  print ( '' )
  print ( 'grid_surface:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Make a surface plot Z(X,Y) for a 41x41 table.' )
#
#  Read the data from the file.
#
  x = []
  y = []
  z = []

  file = open ( 'grid_data.txt', 'r' )

  for line in file:
    line = line.strip ( )
    columns = line.split ( )
    x.append ( float ( columns[0] ) )
    y.append ( float ( columns[1] ) )
    z.append ( float ( columns[2] ) )

  file.close ( )
#
#  The data was stored as a vector.
#  Reshape it to 41x41 arrays.
#
  x = np.reshape ( x, ( 41, 41 ) )
  y = np.reshape ( y, ( 41, 41 ) )
  z = np.reshape ( z, ( 41, 41 ) )
#
#  Form the figure.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )

  ax.plot_surface ( x, y, z, rstride = 1, cstride = 1, \
    cmap = cm.coolwarm, edgecolor = 'none' )

  ax.set_title ( 'Surface plot of 41x41 table Z(X,Y)', fontsize = 16 )
  ax.set_xlabel ( '<--- X --->', fontsize = 16 )
  ax.set_ylabel ( '<--- Y --->', fontsize = 16 )
  ax.set_zlabel ( '<--- Z --->', fontsize = 16 )

  filename = 'grid_surface.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
#
#  Terminate.
#
  print ( '' )
  print ( 'grid_surface:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  grid_surface ( )
  timestamp ( )
 
