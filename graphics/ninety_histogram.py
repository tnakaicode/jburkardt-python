#! /usr/bin/env python3
#
def ninety_histogram ( ):

#*****************************************************************************80
#
## ninety_histogram uses a histogram to find outliers in 90 data values.
#
#  Discussion:
#
#    Because the number of data points is fairly large, we hope that a 
#    histogram will show us whether any values are outliers.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'ninety_histogram:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Read a text file of 90 values, and create a histogram' )
  print ( '  that will expose outliers as isolated values.' )
#
#  Read the values from the file.
#
  filename = 'ninety_data.txt'
  data = np.loadtxt ( filename )

  t = data[:]
  t_num = len ( t )
  print ( '  %d data records read from file' % ( t_num ) )

  bins = 14
  n, bins, patches = plt.hist ( t, bins, density = 1, facecolor = 'blue', rwidth = 0.95 )

  plt.grid ( True )
  plt.title ( 'NINETY: Looking for Outliers', fontsize = 16 )
  plt.xlabel ( '<-- Data Values -->', fontsize = 16 )
  plt.ylabel ( '<-- Frequency -->', fontsize = 16 )
  filename = 'ninety_histogram.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ninety_histogram:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ninety_histogram ( )
  timestamp ( )
