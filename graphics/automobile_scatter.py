#! /usr/bin/env python3
#
def automobile_scatter ( ):

#*****************************************************************************80
#
## automobile_scatter reads the automobile dataset and makes a scatterplot.
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
  print ( 'automobile_scatter:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Read a data file of automobile prices and weights.' )
  print ( '  Display the data as a scatter plot.' )
#
#  Load the data.
#
  filename = 'automobile_data.txt'
  data = np.loadtxt ( filename )
#
#  Split the data.
#
  price = data[:,0]
  weight = data[:,1]
#
#  Plot the data.
#
  plt.scatter ( price, weight )
  plt.grid ( True )
  plt.xlabel ( '<--- Price (1985 Dollars) --->', fontsize = 16 )
  plt.ylabel ( '<--- Curb weight (Pounds) --->', fontsize = 16 )
  plt.title ( '1985 car price versus weight', fontsize = 16 )
  filename = 'automobile_scatter.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'automobile_scatter' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  automobile_scatter ( )
  timestamp ( )
 
