#! /usr/bin/env python3
#
def president_heights_histogram ( ):

#*****************************************************************************80
#
## president_heights_histogram() plots a presidential height histogram.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 April 2019
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
  print ( 'president_heights_histogram():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Make a histogram of president heights.' )
#
#  Read the heights from a file.
#
  filename = 'president_heights_data.txt'
  data = np.loadtxt ( filename )
  height = data[:]
  m = len ( height )
  print ( '' )
  print ( '  %d data records read from file.' % ( m ) )
#
#  Plot the data.
#
  plt.hist ( height, rwidth = 0.95 )
  plt.grid ( True )
  plt.xlabel ( '<-- Height (inches) -->', fontsize = 16 )
  plt.ylabel ( '<-- Frequency -->', fontsize = 16 )
  plt.title ( 'Presidential heights', fontsize = 16 )
#
#  Save the graphics in a file.
#
  filename = 'president_heights_histogram.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )

  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'president_heights_histogram():' )
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
  president_heights_histogram ( )
  timestamp ( )
