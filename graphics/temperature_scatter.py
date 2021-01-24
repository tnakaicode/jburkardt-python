#! /usr/bin/env python3
#
def temperature_scatter ( ):

#*****************************************************************************80
#
## temperature_scatter draws a scatter plot of temperature reading locations.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'temperature_scatter:' )
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
  plt.scatter ( longitude, latitude )
  plt.grid ( True )
  plt.xlabel ( '<--- Longitude (West) --->', fontsize = 16 )
  plt.ylabel ( '<--- Latitude (North) --->', fontsize = 16 )
  plt.title ( 'Location of January temperature readings', fontsize = 16 )
  filename = 'temperature_scatter.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'temperature_scatter' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  temperature_scatter ( )
  timestamp ( )
 
