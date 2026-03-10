#! /usr/bin/env python3
#
def bulgaria_plot ( ):

#*****************************************************************************80
#
## bulgaria_plot() plots the population of Bulgaria over time.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2019
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
  print ( 'bulgaria_plot():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
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
  plt.title ( 'The population of Bulgaria', fontsize = 16 )
  filename = 'bulgaria_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'bulgaria_plot():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  bulgaria_plot ( )
 
