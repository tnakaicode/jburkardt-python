#! /usr/bin/env python3
#
def mod_bar3d ( ):

#*****************************************************************************80
#
## mod_bar3d() makes a 3D bar plot of mod(I,J).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2019
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
  print ( 'mod_bar3d():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Make a 3D bar plot of mod(1:10,1:10)' )
#
#  Define the data.
#
  i = np.linspace ( 1, 10, 10 )
  I, J = np.meshgrid ( i, i.transpose() )
#
#  There is some extra nonsense here to keep bar3d() happy...
#
  I = np.ravel ( I )
  J = np.ravel ( J )
  Z = I % J
  width = 1
  depth = 1
  bottom = np.zeros_like ( Z )
#
#  Plot the data.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.bar3d ( I, J, bottom, width, depth, Z )
  ax.grid ( True )
  ax.set_xlabel ( '<-- I -->', fontsize = 16 )
  ax.set_ylabel ( '<-- J -->', fontsize = 16 )
  ax.set_zlabel ( '<-- I%%J -->', fontsize = 16 )
  ax.set_title ( 'Mod(I,J)' )
  
  filename = 'mod_bar3d.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'mod_bar3d():' )
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
  mod_bar3d ( )
  timestamp ( )
 
