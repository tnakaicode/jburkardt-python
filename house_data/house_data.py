#! /usr/bin/env python3
#
def house_data_test ( ):

#*****************************************************************************80
#
## house_data_test() tests house_data().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 December 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'house_data_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test house_data().' )

  house_data_plot ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'house_data_test():' )
  print ( '  Normal end of execution.' )

  return

def house_data ( ):

#*****************************************************************************80
#
## house_data() returns the coordinates of vertices that outline a house.
#
#  Discussion:
#
#    The vertices define a polygon, although it includes some degenerate
#    and non-simple portions.
#
#    To draw a closed polygon, a copy of the first point may have to be
#    appended at the end of the list.
#
#  License:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 December 2024
#
#  Author:
#
#    John Burkardt.
#
#  Output:
#
#    real xy(11,2), the coordinates of points that outline a house.
#
  import numpy as np

  xy = np.array ( [ \
    [ 0.0, -7.0 ], \
    [ 0.0, -2.0 ], \
    [-3.0, -2.0 ], \
    [-3.0, -7.0 ], \
    [ 6.0, -7.0 ], \
    [ 6.0,  2.0 ], \
    [ 7.0,  1.0 ], \
    [ 0.0,  8.0 ], \
    [-7.0,  1.0 ], \
    [-6.0,  2.0 ], \
    [-6.0, -7.0 ] ] )

  return xy

def house_data_plot ( ):

#*****************************************************************************80
#
## house_data_plot() plots the house data
#
#  License:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 December 2024
#
#  Author:
#
#    John Burkardt.
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'house_data_plot():' )
  print ( '  Plot the house data.' )
#
#  Retrieve the vertices.
#
  xy = house_data ( )
#
#  Repeat the first row at the end so the polygon closes.
#
  xy = np.vstack ( ( xy, xy[0,:] ) )
#
#  Plot the data.
#
  plt.clf ( )
  plt.plot ( xy[:,0], xy[:,1], 'c.-', markersize = 18, linewidth = 6 )
  plt.plot ( xy[:,0], xy[:,1], 'k.-', markersize = 18, linewidth = 2 )
  plt.grid ( True )
  plt.axis ( [ -10.0, 10.0, -10.0, 10.0 ] )
  plt.axis ( 'square' )
  plt.title ( 'The house data' )

  filename = 'house_data.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

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
#    21 August 2019
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
  house_data_test ( )
  timestamp ( )

