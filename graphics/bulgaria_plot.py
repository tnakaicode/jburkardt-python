#! /usr/bin/env python3
#
def bulgaria_plot ( ):

#*****************************************************************************80
#
## bulgaria_plot plots the population of Bulgaria over time.
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
  print ( 'bulgaria_plot:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Plot the population of Bulgaria over time.' )
#
#  Read the pairs "Year, Population" from the file.
#
  filename = 'bulgaria_data.txt'
  data = np.loadtxt ( filename )
#
#  Split data into separate year and population vectors.
#
  year = data[:,0]
  population = data[:,1]
#
#  Plot the data.
#
  plt.plot ( year, population, linewidth = 3, color = 'b' )
  plt.grid ( True )
  plt.xlabel ( '<--- Year --->', fontsize = 16 )
  plt.ylabel ( '<--- Population --->', fontsize = 16 )
  plt.title ( 'The Population of Bulgaria', fontsize = 16 )
#
#  Save the plot as a file.
#
  filename = 'bulgaria_plot.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
#
#  Display the plot.
#
  plt.show ( block = False )
  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'bulgaria_plot' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bulgaria_plot ( )
  timestamp ( )
 
