#! /usr/bin/env python3
#
def temperature_scatter ( ):

#*****************************************************************************80
#
## temperature_scatter() draws a scatter plot of temperature reading locations.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'temperature_scatter():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
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
  plt.scatter ( longitude, latitude )
  plt.grid ( True )
  plt.xlabel ( '<--- Longitude (West) --->', fontsize = 16 )
  plt.ylabel ( '<--- Latitude (North) --->', fontsize = 16 )
  plt.title ( 'Location of January temperature readings', fontsize = 16 )
  filename = 'temperature_scatter.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'temperature_scatter():' )
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
  temperature_scatter ( )
  timestamp ( )
 
