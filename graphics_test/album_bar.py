#! /usr/bin/env python3
#
def album_bar ( ):

#*****************************************************************************80
#
## album_bar makes a bar graph of music album sales over 11 years.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'album_bar:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Read a data file of yearly music album sales.' )
  print ( '  Plot the data as a bar chart.' )
#
#  Read the year and sales from the data file.
#
  filename = 'album_data.txt'
  data = np.loadtxt ( filename )
  year = data[:,0]
  sales = data[:,1]
#
#  Create the bar plot.
#
  plt.bar ( year, sales )
  plt.grid ( True )
  plt.title ( 'Music album sales, all formats', fontsize = 16 )
  plt.xlabel ( '<-- Year -->', fontsize = 16 )
  plt.ylabel ( '<-- Sales (millions) -->', fontsize = 16 )
  filename = 'album_bar.png'
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.clf ( )

  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'album_bar:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  album_bar ( )
  timestamp ( )

