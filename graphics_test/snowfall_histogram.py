#! /usr/bin/env python3
#
def snowfall_histogram ( ):

#*****************************************************************************80
#
## snowfall_histogram() plots a histogram of snowfall levels.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2025
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
  print ( 'snowfall_histogram():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Make a histogram of yearly snowfall levels.' )
#
#  Read the pairs from the file.
#
  filename = 'snowfall_data.txt'
  data = np.loadtxt ( filename )
  inches = data[:,9]

  m = len ( inches )
  print ( '' )
  print ( '  ', m, ' data records read from file.' )
#
#  Plot the data.
#
  plt.hist ( inches, rwidth = 0.95 )
  plt.grid ( True )
  plt.xlabel ( '<-- Yearly Snowfall (inches) -->', fontsize = 16 )
  plt.ylabel ( '<-- Frequency -->', fontsize = 16 )
  plt.title ( 'Yearly snowfall at Michigan Tech', fontsize = 16 )
#
#  Save the graphics in a file.
#
  filename = 'snowfall_histogram.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'snowfall_histogram():' )
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
  snowfall_histogram ( )
  timestamp ( )
