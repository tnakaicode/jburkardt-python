#! /usr/bin/env python3
#
def volcano_surface ( ):

#*****************************************************************************80
#
## volcano_surface draws a surface plot of volcano (X,Y,Z) data.
#
#  Discussion:
#
#    I originally meant to read this data file as a "csv" file, but the
#    necessary steps are so cumbersome that I switched to loadtxt!
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 April 2019
#
#  Author:
#
#    John Burkardt
#
  import csv
  import matplotlib.pyplot as plt
  import numpy as np
  import platform
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm

  print ( '' )
  print ( 'volcano_surface:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Make a surface plot Z(X,Y) of volcano elevation data.' )
#
#  Read the Z data from the file.
#
  zmat = np.loadtxt ( 'volcano_data.txt', dtype = 'f', delimiter = ' ' )
#
#  We have to create a grid of X and Y values corresponding to Z.
#
  m, n = zmat.shape
  print ( '  Z data has %d rows and %d columns' % ( m, n ) )
  xvec = np.linspace ( 0, n, n )
  yvec = np.linspace ( 0, m, m )
  xmat, ymat = np.meshgrid ( xvec, yvec )  
#
#  Form the figure.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( xmat, ymat, zmat, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_title ( 'Surface plot of Volcano', fontsize = 16 )
  ax.set_xlabel ( '<--- X --->', fontsize = 16 )
  ax.set_ylabel ( '<--- Y --->', fontsize = 16 )
  ax.set_zlabel ( '<--- Z --->', fontsize = 16 )
  filename = 'volcano_surface.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
#
#  Terminate.
#
  print ( '' )
  print ( 'volcano_surface:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  volcano_surface ( )
  timestamp ( )
 
