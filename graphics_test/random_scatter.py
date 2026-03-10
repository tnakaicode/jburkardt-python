#! /usr/bin/env python3
#
def random_scatter ( ):

#*****************************************************************************80
#
## random_scatter() draws a scatter plot of X Y data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 May 2016
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'random_scatter():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Make a scatterplot of random XY data.' )

  n = 500
  r = rng.standard_normal ( size = n )
  t = np.pi * rng.random ( size = n )
  x = r * np.cos ( t )
  y = r * np.sin ( t )
#
#  Plot the data.
#
  plt.scatter ( x, y )
  plt.grid ( True )
  plt.axis ( 'Equal' )
  plt.xlabel ( '<--- X --->', fontsize = 16 )
  plt.ylabel ( '<--- Y --->', fontsize = 16 )
  plt.title ( '500 Normally Distributed (X,Y) Values', fontsize = 16 )

  filename = 'random_scatter.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'random_scatter():' )
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
  random_scatter ( )
  timestamp ( )
 
