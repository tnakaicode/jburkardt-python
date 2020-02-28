#! /usr/bin/env python3
#
def nile_plot ( ):

#*****************************************************************************80
#
## nile_plot makes a line plot of yearly flood levels for the Nile.
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
  print ( 'nile_plot:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Make a line plot of yearly Nile flood levels.' )
#
#  Read the pairs "Year, Population" from the file.
#
  filename = 'nile_data.txt'
  data = np.loadtxt ( filename )

  year = data[:,0]
  height = data[:,1]
#
#  Plot the data.
#
  plt.plot ( year, height, linewidth = 3, color = 'b' )
  plt.grid ( True )
  plt.xlabel ( '<--- Year index --->', fontsize = 16 )
  plt.ylabel ( '<-- Maximum Flood Height-->', fontsize = 16 )
  plt.title ( 'The Maximum Height of the Nile', fontsize = 16 )

  filename = 'nile_plot.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )

  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'nile_plot' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  nile_plot ( )
  timestamp ( )
 
