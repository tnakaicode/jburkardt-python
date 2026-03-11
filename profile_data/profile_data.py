#! /usr/bin/env python3
#
def profile_data_test ( ):

#*****************************************************************************80
#
## profile_data_test() tests profile_data().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 January 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'profile_data_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  profile_data() returns (x,y) coordinates along' )
  print ( '  a facial profile.' )

  xy = profile_data ( )

  xd = xy[:,0].copy()
  yd = xy[:,1].copy()
  filename = 'profile_data.png'
  profile_data_plot ( xd, yd, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'profile_data_test():' )
  print ( '  Normal end of execution.' )

  return

def profile_data ( ):

#*****************************************************************************80
#
## profile_data() returns (x,y) coordinates of points along a facial profile.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 January 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625. 
#
#  Output:
#
#    real xd(nd), yd(nd): data to be interpolated.
#
  import numpy as np

  xy = np.array ( [ \
    [ 2.0,   0.0 ], \
    [ 3.0,  -1.0 ], \
    [ 4.0,  -0.5 ], \
    [ 5.0,   0.0 ], \
    [ 6.0,   1.0 ], \
    [ 7.0,   2.0 ], \
    [ 7.5,   5.0 ], \
    [ 8.0,   7.5 ], \
    [ 9.0,   8.0 ], \
    [10.0,   8.0 ], \
    [11.0,   8.2 ], \
    [11.5,   9.0 ], \
    [12.0,   8.2 ], \
    [12.5,   6.5 ], \
    [12.9,   8.9 ], \
    [13.0,   9.0 ], \
    [14.0,   9.0 ], \
    [14.7,  10.0 ], \
    [14.8,  10.5 ], \
    [14.9,  11.0 ], \
    [15.0,  11.4 ], \
    [15.3,  11.6 ], \
    [15.6,  11.5 ], \
    [16.0,  11.5 ], \
    [17.0,  11.0 ], \
    [18.0,  10.4 ], \
    [19.0,  10.0 ], \
    [20.0,   9.7 ], \
    [21.0,  10.0 ], \
    [22.0,  10.5 ], \
    [23.0,  10.7 ], \
    [24.0,  11.2 ], \
    [25.0,  10.9 ], \
    [26.0,  10.4 ], \
    [27.0,  10.2 ], \
    [28.0,  10.0 ], \
    [29.0,  11.2 ], \
    [30.0,  11.3 ], \
    [31.0,  10.2 ], \
    [32.0,   9.0 ], \
    [33.0,   7.0 ], \
    [34.0,   5.0 ], \
    [35.0,   3.0 ], \
    [36.0,   0.0 ] ] )

  return xy

def profile_data_plot ( xd, yd, filename ):

#*****************************************************************************80
#
## profile_data_plot() plots the profile data
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 January 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625. 
#
#  Input:
#
#    real xd(nd), yd(nd): the profile data.
#
#    string filename: the name of a file in which to save the plot.
#
  import matplotlib.pyplot as plt

  plt.clf ( )
  plt.plot ( xd, yd, 'k.', markersize = 20 )
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.title ( 'Profile data' )

  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

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
  profile_data_test ( )
  timestamp ( )

