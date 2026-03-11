#! /usr/bin/env python3
#
def xy_display_test ( ):

#*****************************************************************************80
#
## xy_display_test() tests xy_display().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 March 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib
  import numpy as np
  import platform

  print ( '' )
  print ( 'xy_display_test():' )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test xy_display() which displays an xy file of point data.' )

  header = 'lsup_303'

  xy_display ( header )
#
#  Terminate.
#
  print ( '' )
  print ( 'xy_display_test():' )
  print ( '  Normal end of execution.' )

  return

def xy_display ( header ):

#*****************************************************************************80
#
## xy_display() plots a set of 2D points.
#
#  Discussion:
#
#    The data is stored in a text file with N rows and 2 columns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string xy_filename: the name of the data file.
#
  import matplotlib.pyplot as plt
  import numpy as np
#
#  Read the data.
#
  xy_filename = header + '.xy'
  xy = np.loadtxt ( xy_filename )
  point_num = xy.shape[0]

  print ( '' )
  print ( '  Number of points POINT_NUM  = ', point_num )
  print ( '' )
  print ( '  First 5 nodes:' )
  print ( xy[0:min(point_num,5),:] )

  plt.clf ( )
  plt.scatter ( xy[:,0], xy[:,1] )
  plt.grid ( True )
  plt.xlabel ( '<-- X -->', fontsize = 16 )
  plt.ylabel ( '<-- Y -->', fontsize = 16 )
  plt.title ( header )
  filename = header + '.png'
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
  xy_display_test ( )
  timestamp ( )

