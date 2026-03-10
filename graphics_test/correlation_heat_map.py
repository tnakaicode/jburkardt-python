#! /usr/bin/env python3
#
def correlation_heat_map ( ):

#*****************************************************************************80
#
## correlation_heat_map() draws a heat map of a correlation matrix.
#
#  Discussion:
#
#    The matrix C is symmetric, with values between -1 (highest anticorrelation)
#    and +1 (highest correlation), with 1's on the diagonal.
#
#    In this example, all the entries are positive.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2025
#
#  Author:
#
#    John Burkardt
#
  from matplotlib import cm
  import csv
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'correlation_heat_map():' )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Make a heat map from a correlation matrix C(1:n,1:n)' )
#
#  Set the data.
#
  C = np.array ( [ \
    [ 1.00, 0.85, 0.81, 0.86, 0.47, 0.40, 0.30, 0.38 ], \
    [ 0.85, 1.00, 0.88, 0.83, 0.38, 0.33, 0.28, 0.41 ], \
    [ 0.81, 0.88, 1.00, 0.80, 0.38, 0.32, 0.24, 0.34 ], \
    [ 0.86, 0.83, 0.80, 1.00, 0.44, 0.33, 0.33, 0.36 ], \
    [ 0.47, 0.38, 0.38, 0.44, 1.00, 0.76, 0.73, 0.63 ], \
    [ 0.40, 0.33, 0.32, 0.33, 0.76, 1.00, 0.58, 0.58 ], \
    [ 0.30, 0.28, 0.24, 0.33, 0.73, 0.58, 1.00, 0.54 ], \
    [ 0.38, 0.41, 0.34, 0.36, 0.63, 0.58, 0.54, 1.00 ] ] )
#
#  Form the figure.
#
  plt.imshow ( C, cmap = 'hot', interpolation = 'nearest' )
  plt.colorbar ( )
  plt.title ( 'Heat map of a correlation matrix' )
  filename = 'correlation_heat_map.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.show ( block = False )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'correlation_heat_map():' )
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
  correlation_heat_map ( )
  timestamp ( )
 
