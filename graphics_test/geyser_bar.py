#! /usr/bin/env python3
#
def geyser_bar ( ):

#*****************************************************************************80
#
## geyser_bar() makes a bar plot of geyser data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 April 2019
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
  print ( 'geyser_bar():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Read a list of binned data representing waiting times between' )
  print ( '  eruptions of the Old Faithful geyser.' )
  print ( '  Plot the data as a bar chart.' )
#
#  Read the values from the file.
#
  filename = 'geyser_bar_data.txt'
  data = np.loadtxt ( filename )
  tcenter = data[:,0]
  ycount = data[:,1]
#
#  Create the bar plot.
#
  plt.bar ( tcenter, ycount )

  plt.grid ( True )
  plt.title ( 'Time between eruptions of Old Faithful', fontsize = 16 )
  plt.xlabel ( 'Minutes', fontsize = 16 )
  plt.ylabel ( 'Frequency', fontsize = 16 )
  filename = 'geyser_bar.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'geyser_bar():' )
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
  geyser_bar ( )
  timestamp ( )

