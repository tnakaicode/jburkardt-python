#! /usr/bin/env python3
#
def mexican_hat_surface ( ):

#*****************************************************************************80
#
## mexican_hat_surface draws a surface plot of "Mexican hat" data.
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
  import matplotlib.pyplot as plt
  import numpy as np
  import platform
  from mpl_toolkits.mplot3d import Axes3D
  from matplotlib import cm

  print ( '' )
  print ( 'mexican_hat_surface:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Make a surface plot Z(X,Y) of volcano elevation data.' )
#
#  Set up X, Y grid and Z data.
#
  xvec = np.linspace( -8.0, 8.0, 33 )
  yvec = np.linspace( -8.0, 8.0, 33 )
  xmat, ymat = np.meshgrid ( xvec, yvec )
  rmat = np.sqrt ( xmat**2 + ymat**2 + np.finfo(float).eps )
  zmat = np.sin ( rmat ) / rmat 
#
#  Form the figure.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( xmat, ymat, zmat, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_title ( 'The Mexican Hat function', fontsize = 16 )
  ax.set_xlabel ( '<--- X --->', fontsize = 16 )
  ax.set_ylabel ( '<--- Y --->', fontsize = 16 )
  ax.set_zlabel ( '<--- Z(X,Y) --->', fontsize = 16 )
  filename = 'mexican_hat_surface.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
#
#  Terminate.
#
  print ( '' )
  print ( 'mexican_hat_surface:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  mexican_hat_surface ( )
  timestamp ( )
 
