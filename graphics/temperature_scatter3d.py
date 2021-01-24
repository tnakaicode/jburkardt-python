#! /usr/bin/env python3
#
def temperature_scatter3d ( ):

#*****************************************************************************80
#
## temperature_scatter3d draws a 3d scatter plot of temperature reading locations.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D
  import numpy as np
  import platform

  print ( '' )
  print ( 'temperature_scatter3d:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Make a scatter plot of temperature reading locations.' )
#
#  Read temperature, -longitude, latitude.
#
  filename = 'temperature_data.txt'
  data = np.loadtxt ( filename )
#
#  Split the data.
#
  temperature = data[:,0]
  longitude = data[:,1]
  latitude = data[:,2]
#
#  Plot the data.
#
  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.scatter ( longitude, latitude, temperature )
  ax.grid ( True )
  ax.set_xlabel ( '<--- Longitude (West) --->', fontsize = 16 )
  ax.set_ylabel ( '<--- Latitude (North) --->', fontsize = 16 )
  ax.set_zlabel ( '<--- Temperature --->', fontsize = 16 )
  ax.set_title ( 'January temperature readings', fontsize = 16 )
  filename = 'temperature_scatter3d.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'temperature_scatter3d' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  temperature_scatter3d ( )
  timestamp ( )
 
