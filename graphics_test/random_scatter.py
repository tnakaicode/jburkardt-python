#! /usr/bin/env python3
#
def random_scatter ( ):

#*****************************************************************************80
#
## random_scatter draws a scatter plot of X Y data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2016
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'random_scatter:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Make a scatterplot of random XY data.' )

  n = 500
  r = np.random.normal ( 0.0, 1.0, n )
  t = np.pi * np.random.random ( n )
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
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )
  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'random_scatter' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  random_scatter ( )
  timestamp ( )
 
