#! /usr/bin/env python3
#
def julia_set ( h, w, xl, xr, yb, yt ):

#*****************************************************************************80
#
## julia_set() returns points in a Julia set.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 December 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer H, W, the height and width of the region in pixels.
#
#    real XL, XR, YB, YT, the left, right, bottom and top limits.
#
#  Output:
#
#    logical J(h,w): true if the corresponding point is in the Julia set.
#
#    real X(h,w), Y(h,w): the coordinates of the points.
#
  import numpy as np
#
#  Create a hxw grid of X and Y coordinates.
#
  x = np.linspace ( xl, xr, w )
  y = np.linspace ( yb, yt, h )
  X, Y = np.meshgrid ( x, y )
#
#  Construct a complex copy of X + Yi.
#
  A = X + Y * 1j
#
#  Repeatedly apply the following transformation:
#    A -> A * A + C
#
  c = - 0.8 + 0.156 * 1j
  for k in range ( 0, 200 ):
    A = A**2 + c
#
#  Record the points that didn't diverge.
#
  J = np.abs ( A ) < 1000.0

  return J, X, Y

def julia_set_test ( ):

#*****************************************************************************80
#
## julia_set_test() tests julia_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 December 2022
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform
  import warnings

  print ( '' )
  print ( 'julia_set_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Compute and plot a Julia set.' )
  print ( '  under the transformation A=A^2-0.8+0.156i' )

  w = 1000
  h = 1000
  xl = -1.5
  xr = 1.5
  yb = -1.5
  yt = 1.5
#
#  Before calling "julia_set()", we suppress warnings, which
#  report overflow.
#
  with warnings.catch_warnings ( ):
    warnings.simplefilter ( "ignore" )
    J, X, Y = julia_set ( w, h, xl, xr, yb, yt )
#
#  Use a plot() command directly on the X, Y values.
#
  plt.figure ( )
  plt.clf ( )
  plt.plot ( X[J], Y[J], 'r.', markersize = 0.25 )
  plt.grid ( True )
  filename = 'julia_plot.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Use a spy() command on the logical 0/1 J array.
#
  plt.figure ( )
  plt.clf ( )
  plt.spy ( J, markersize = 0.25, color = 'b' )
  filename = 'julia_spy.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
#
#  Terminate.
#
  print ( '' )
  print ( 'julia_set_test():' )
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
  julia_set_test ( )
  timestamp ( )


