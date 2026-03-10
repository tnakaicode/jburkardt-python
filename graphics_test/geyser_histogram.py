#! /usr/bin/env python3
#
def geyser_histogram ( ):

#*****************************************************************************80
#
## geyser_histogram() makes a histogram.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2019
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
  print ( 'geyser_histogram():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Read a long list of values.' )
  print ( '  Create and plot a histogram.' )
#
#  Read the values from the file.
#
  filename = 'geyser_data.txt'
  data = np.loadtxt ( filename )
  t = data[:,0]

  bins = 14
  n, bins, patches = plt.hist ( t, bins, density = 1, facecolor = 'blue', rwidth = 0.95 )

  plt.grid ( True )
  plt.title ( 'Time between eruptions of Old Faithful', fontsize = 16 )
  plt.xlabel ( '<-- Minutes -->', fontsize = 16 )
  plt.ylabel ( '<-- Frequency -->', fontsize = 16 )
  filename = 'geyser_histogram.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'geyser_histogram():' )
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
  geyser_histogram ( )
  timestamp ( )

