#! /usr/bin/env python3
#
def volcano_line_contour ( ):

#*****************************************************************************80
#
## volcano_line_contour() draws a filled contour plot of volcano (X,Y,Z) data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 May 2019
#
#  Author:
#
#    John Burkardt
#
  from matplotlib import cm
  import csv
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'volcano_line_contour():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Make a line contour plot Z(X,Y) of volcano elevation data.' )
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
  plt.contour ( xmat, ymat, zmat, levels, cmap = cm.coolwarm )
  plt.title ( 'Line contour plot of Volcano', fontsize = 16 )
  plt.xlabel ( '<--- X --->', fontsize = 16 )
  plt.ylabel ( '<--- Y --->', fontsize = 16 )
  filename = 'volcano_line_contour.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'volcano_line_contour():' )
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
  volcano_line_contour ( )
  timestamp ( )
