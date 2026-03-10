#! /usr/bin/env python3
#
def geyser_scatter ( ):

#*****************************************************************************80
#
## geyser_scatter() makes a scatter plot of geyser data.
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
  print ( 'geyser_scatter():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Read a data file of duration and pause lengths' )
  print ( '  for the Old Faithful geyser.' )
  print ( '  Display the data as a scatter plot.' )
#
#  Read the times and plasma levels from the data file.
#
  filename = 'geyser_data.txt'
  data = np.loadtxt ( filename )
#
#  Split the data.
#
  duration = data[:,0]
  pause = data[:,1]
#
#  Plot the data.
#
  plt.scatter ( duration, pause )
  plt.grid ( True )
  plt.xlabel ( '<--- Eruption duration (minutes) --->', fontsize = 16 )
  plt.ylabel ( '<--- Pause duration (minutes) --->', fontsize = 16 )
  plt.title ( 'Old Faithful Eruptions and Pauses', fontsize = 16 )
  filename = 'geyser_scatter.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'geyser_scatter():' )
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
  geyser_scatter ( )
  timestamp ( )
  
