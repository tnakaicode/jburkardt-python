#! /usr/bin/env python3
#
def president_heights_histogram ( ):

#*****************************************************************************80
#
## president_heights_histogram plots a presidential height histogram.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'president_heights_histogram:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )

  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'president_heights_histogram:' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  president_heights_histogram ( )
  timestamp ( )
