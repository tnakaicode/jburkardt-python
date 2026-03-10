#! /usr/bin/env python3
#
def nile_histogram ( ):

#*****************************************************************************80
#
## nile_histogram() plots a histogram of yearly flood levels for the Nile.
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
  print ( 'nile_histogram():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Make a histogram of yearly Nile flood levels.' )
#
#  Read the pairs from the file.
#
  filename = 'nile_data.txt'
  data = np.loadtxt ( filename )
  year = data[:,0]
  height = data[:,1]

  m = len ( year )
  print ( '' )
  print ( '  ', m, ' data records read from file.' )
#
#  Plot the data.
#
  plt.hist ( height, rwidth = 0.95 )
  plt.grid ( True )
  plt.xlabel ( '<-- Height of Nile at Maximum Flood -->', fontsize = 16 )
  plt.ylabel ( '<-- Frequency -->', fontsize = 16 )
  plt.title ( 'Yearly Nile Flood Height', fontsize = 16 )
#
#  Save the graphics in a file.
#
  filename = 'nile_histogram.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )

  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'nile_histogram():' )
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
  nile_histogram ( )
  timestamp ( )
