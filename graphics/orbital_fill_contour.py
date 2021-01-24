#! /usr/bin/env python3
#
def orbital_fill_contour ( ):

#*****************************************************************************80
#
## orbital_fill_contour makes a filled contour plot of a set of tabular Z(X,Y) data.
#
#  Discussion:
#
#    The data represents values on a 101x101 grid over [0,4*pi]x[0,4*pi]
#    for the following function which computes the minimum distance d 
#    between two planets for certain orbital angles t1 and t2.
#
#    function d = sep2 ( t1, t2 )
#      A1 = 10;
#      P1 = 2;
#      phi1 = pi/8;
#      A2 = 4;
#      P2 = 1;
#      phi2 = -pi/7;
#      x0 = ((P1-A1)/2) + ((P1+A1)/2)*cos(t1);
#      y0 = sqrt(A1*P1)*sin(t1);
#      x1 =  cos(phi1) * x0 + sin(phi1) * y0;
#      y1 = -sin(phi1) * x0 + cos(phi1) * y0;
#      x0 = ((P2-A2)/2) + ((P2+A2)/2)*cos(t2);
#      y0 = sqrt(A2*P2)*sin(t2);
#      x2 =  cos(phi2) * x0 + sin(phi2) * y0;
#      y2 = -sin(phi2) * x0 + cos(phi2) * y0;
#      d = 0.5 * ( ( x1 - x2 ).^2 + ( y1 - y2 ).^2 );
#    end
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2019
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
  print ( 'orbital_fill_contour:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Make a filled contour plot of a table of data Z(X,Y).' )
#
#  Read the data from the file.
#
  x = []
  y = []
  z = []

  file = open ( 'orbital_data.txt', 'r' )
  i = 0
  for line in file:
    line = line.strip ( )
    columns = line.split ( )
    x.append ( float ( columns[0] ) )
    y.append ( float ( columns[1] ) )
    z.append ( float ( columns[2] ) )
    i = i + 1

  file.close ( )
#
#  Get the range of data so we can decide on contour levels.
#
  levels = 15
  zmax = np.max ( z )
  zmin = np.min ( z )
  zdel = ( zmax - zmin ) / levels
#
#  Rearrange X, Y, Z values as 2D arrays.
#
  nx = 101
  ny = 101
  x = np.reshape ( x, ( nx, ny ) )
  y = np.reshape ( y, ( nx, ny ) )
  z = np.reshape ( z, ( nx, ny ) )
#
#  Choose a color map.
#
# cmap = cm.PRGn
  cmap = cm.coolwarm

  ax = plt.figure ( )
  plt.contourf ( x, y, z, levels, cmap=cm.get_cmap(cmap, levels-1) )
#
#  Label the axes and the plot.
#
  plt.title ( 'Filled contour plot of orbitals', fontsize = 16 )
  plt.xlabel ( '<--- X --->', fontsize = 16 )
  plt.ylabel ( '<--- Y --->', fontsize = 16 )
  filename = 'orbital_contour.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.clf ( )

  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'orbital_fill_contour:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  orbital_fill_contour ( )
  timestamp ( )
 
