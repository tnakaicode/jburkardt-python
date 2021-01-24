#! /usr/bin/env python3
#
def president_heights_bar ( ):

#*****************************************************************************80
#
## president_heights_bar makes a bar plot of Presidential heights.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'president_heights_bar:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Create a bar plot of the height in inches of US presidents.' )
#
#  Read the values from the file.
#
  filename = 'president_heights_data.txt'
  data = np.loadtxt ( filename )
  height = data[:]
  n = len ( height )
  index = np.arange ( n )
#
#  Create the bar plot.
#
  plt.bar ( index, height )
  plt.grid ( True )
  plt.title ( 'US President Heights', fontsize = 16 )
  plt.xlabel ( '<-- Index -->', fontsize = 16 )
  plt.ylabel ( '<-- Height (inches) -->', fontsize = 16 )
  filename = 'president_heights_bar.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.clf ( )

  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'president_heights_bar:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  president_heights_bar ( )
  timestamp ( )

