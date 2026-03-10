#! /usr/bin/env python3
#
def sombrero_surface ( ):

#*****************************************************************************80
#
## sombrero_surface() draws a surface plot of "Mexican hat" data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2022
#
#  Author:
#
#    John Burkardt
#
  from matplotlib import cm
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'sombrero_surface():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Make a surface plot Z(X,Y) of sombrero data.' )
#
#  Set up X, Y grid and Z data.
#
  xvec = np.linspace( -8.0, 8.0, 33 )
  yvec = np.linspace( -8.0, 8.0, 33 )
  xmat, ymat = np.meshgrid ( xvec, yvec )
  rmat = np.sqrt ( xmat**2 + ymat**2 )
  zmat = np.sin ( rmat ) / rmat 
  zmat[rmat == 0] = 1.0
#
#  Form the figure.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection='3d' )
  ax.plot_surface ( xmat, ymat, zmat, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_title ( 'The sombrero function' )
  ax.set_xlabel ( '<--- X --->' )
  ax.set_ylabel ( '<--- Y --->' )
  ax.set_zlabel ( '<--- Z(X,Y) --->' )
  filename = 'sombrero_surface.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'sombrero_surface():' )
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
  sombrero_surface ( )
  timestamp ( )
 
