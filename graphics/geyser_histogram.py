#! /usr/bin/env python3
#
def geyser_histogram ( ):

#*****************************************************************************80
#
## geyser_histogram makes a histogram.
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
  print ( 'geyser_histogram:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'geyser_histogram:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  geyser_histogram ( )
  timestamp ( )

