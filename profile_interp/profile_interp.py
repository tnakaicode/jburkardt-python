#! /usr/bin/env python3
#
def profile_interp_test ( ):

#*****************************************************************************80
#
## profile_interp_test() tests profile_interp().
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
  import scipy as sp

  print ( '' )
  print ( 'profile_interp_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  scipy version:  ' + sp.version.version )
  print ( '  profile_interp() interpolates facial profile data.' )

  xy = profile_data ( )
  xd = xy[:,0].copy()
  yd = xy[:,1].copy()

  interp_spline_test ( xd, yd )
#
#  Terminate.
#
  print ( '' )
  print ( 'profile_interp_test():' )
  print ( '  Normal end of execution.' )

  return

def interp_plot ( xd, yd, xi, yi, filename ):

#*****************************************************************************80
#
## interp_plot() plots the profile data using splines.
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
#    real xd(nd), yd(nd): data to be interpolated.
#
#    real xi(ni), yi(ni): the interpolated values.
#
#    string filename: the name of a file in which to save the plot.
#
  import matplotlib.pyplot as plt
#
#  Display the parameterized spline U(T), V(T):
#
  plt.clf ( )
  plt.plot ( xi, yi, linewidth = 3 )
  plt.plot ( xd, yd, 'k.', markersize = 20 )
  plt.axis ( 'equal' )
  plt.grid ( True )
  plt.legend ( [ 'Spline', 'Data' ] )
  plt.title ( 'Spline interpolant to profile data' )

  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def interp_spline ( xd, yd, ni ):

#*****************************************************************************80
#
## interp_spline() evaluates a spline interpolant to data.
#
#  Discussion:
#
#    This program assumes that the file 'profile_data.txt' is available.
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
#    real xd(nd), yd(nd): data to be interpolated.  It is assumed that
#    there is a functional relationship y=f(x).
#
#    integer ni: the number of equally spaced interpolating arguments to use.
#
#  Output:
#
#    real xi(ni), yi(ni): equally spaced x arguments over the xd range,
#    and spline-interpolated values for y.
#
  from scipy.interpolate import interp1d
  import numpy as np
#
#  Define a cubic spline through the data.
#
  f_cubic = interp1d ( xd, yd, kind = 'cubic' )
#
#  Evaluate the spline through the data.
#
  xi = np.linspace ( np.min ( xd ), np.max ( xd ), ni )
  yi = f_cubic ( xi )

  return xi, yi

def interp_spline_test ( xd, yd ):

#*****************************************************************************80
#
## interp_spline_test() interpolates the profile data using splines.
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
#    real xd(nd), yd(nd): data to be interpolated.
#
  print ( '' )
  print ( 'interp_spline_test():' )
  print ( '  Compute and display a cubic spline interpolant to' )
  print ( '  sample data from a facial profile.' )
#
#  Extract xd and yd data vectors.
#
  md = len ( xd )
  print ( '  The data consists of ', md, ' (x,y) pairs.' )
#
#  Evaluate the spline through the data.
#
  ni = 101
  xi, yi = interp_spline ( xd, yd, ni )

  filename = 'interp_spline_test.png'
  interp_plot ( xd, yd, xi, yi, filename )

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
  profile_interp_test ( )
  timestamp ( )

