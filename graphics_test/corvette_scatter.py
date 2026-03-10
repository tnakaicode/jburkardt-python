#! /usr/bin/env python3
#
def corvette_scatter ( ):

#*****************************************************************************80
#
## corvette_scatter() makes a scatter plot of Corvette resale prices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 April 2019
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
  print ( 'corvette_scatter():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Read a data file of resale prices for Corvettes.' )
  print ( '  Display the data as a scatter plot.' )
#
#  Read the year and price from the data file.
#
  filename = 'corvette_data.txt'
  data = np.loadtxt ( filename )
#
#  Split the data.
#
  year = data[:,0]
  price = data[:,1]
#
#  Plot the data.
#
  plt.scatter ( year, price )
  plt.grid ( True )
  plt.xlabel ( '<--- Model year --->', fontsize = 16 )
  plt.ylabel ( '<--- Resale price ($) --->', fontsize = 16 )
  plt.title ( 'Corvette resale price by model year', fontsize = 16 )
  filename = 'corvette_scatter.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'corvette_scatter():' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  corvette_scatter ( )
  timestamp ( )
 
