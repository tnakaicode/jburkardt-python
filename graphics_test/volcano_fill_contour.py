#! /usr/bin/env python3
#
def volcano_fill_contour ( ):

#*****************************************************************************80
#
## volcano_fill_contour draws a filled contour plot of volcano (X,Y,Z) data.
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
  import csv
  import matplotlib.pyplot as plt
  import numpy as np
  import platform
  from matplotlib import cm

  print ( '' )
  print ( 'volcano_fill_contour:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Make a filled contour plot Z(X,Y) of volcano elevation data.' )
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
  levels = 15
  ax = plt.figure ( )
  plt.contourf ( xmat, ymat, zmat, levels, cmap = cm.coolwarm )
  plt.title ( 'Filled contour plot of Volcano', fontsize = 16 )
  plt.xlabel ( '<--- X --->', fontsize = 16 )
  plt.ylabel ( '<--- Y --->', fontsize = 16 )
  filename = 'volcano_fill_contour.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
#
#  Terminate.
#
  print ( '' )
  print ( 'volcano_fill_contour:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  volcano_fill_contour ( )
  timestamp ( )
 
