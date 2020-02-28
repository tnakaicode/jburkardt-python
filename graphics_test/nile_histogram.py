#! /usr/bin/env python3
#
def nile_histogram ( ):

#*****************************************************************************80
#
## nile_histogram plots a histogram of yearly flood levels for the Nile.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'nile_histogram:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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
  print ( '  %d data records read from file.' % ( m ) )
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
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )

  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'nile_histogram:' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  nile_histogram ( )
  timestamp ( )
