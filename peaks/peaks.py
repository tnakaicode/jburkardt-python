#! /usr/bin/env python3
#
def peaks_test ( ):

#*****************************************************************************80
#
## peaks_test() tests peaks().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 March 2025
#
#  Author:
#
#    John Burkardt
#
  from matplotlib import cm
  from mpl_toolkits.mplot3d import Axes3D
  import matplotlib
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'peaks_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  matplotlib version: ' + matplotlib.__version__ )
  print ( '  Test peaks().' )

  x = np.linspace ( -3.0, 3.0, 151 )
  y = np.linspace ( -3.0, 3.0, 151 )

  X, Y = np.meshgrid ( x, y )
  
  Z = peaks ( X, Y )

  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
  ax.plot_surface ( X, Y, Z, \
    cmap = cm.coolwarm, edgecolor = 'none' )
  ax.set_title ( 'The peaks() function' )
  ax.set_xlabel ( '<--- X --->', fontsize = 16 )
  ax.set_ylabel ( '<--- Y --->', fontsize = 16 )
  ax.set_zlabel ( '<--- Z --->', fontsize = 16 )
  filename = 'peaks.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'peaks_test():' )
  print ( '  Normal end of execution.' )

  return

def peaks ( x, y ):

#*****************************************************************************80
#
## peaks() evaluates the peaks function.
#
#  Discussion:
#
#    peaks() is a MATLAB library function used for various demonstrations
#    including the creation of contour plots and optimization.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real x, y: evaluation points.
#
#  Output:
#
#    real z: the value of peaks(x,y).
#
  import numpy as np

  e1 = - x**2 - ( y + 1.0 )**2
  e2 = - x**2 - y**2
  e3 = - ( x + 1.0 )**2 - y**2

  z = 3.0 * ( 1.0 - x**2 )             * np.exp ( e1 ) \
    - 10.0 * ( x / 5.0 - x**3 - y**5 ) * np.exp ( e2 ) \
    - 1.0 / 3.0                        * np.exp ( e3 )

  return z

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
  peaks_test ( )
  timestamp ( )

