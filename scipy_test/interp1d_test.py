#! /usr/bin/env python3
#
def interp1d_test ( ):

#*****************************************************************************80
#
## interp1d_test() tests the scipy() interp1d() function.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 December 2024
#
#  Author:
#
#    John Burkardt
#
  from scipy.interpolate import interp1d
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'interp1d_test():' )
  print ( '  interp1d() performas several types of 1D interpolation.' )

  x = np.linspace ( 0.0, 0.5, 8 )
  y = f ( x )
#
#  Construct interpolating functions.
#
  f_nearest = interp1d ( x, y, kind = 'nearest' )
  f_linear = interp1d ( x, y, kind = 'linear' )
  f_cubic = interp1d ( x, y, kind = 'cubic' )
#
#  Evaluate interpolants.
#
  x2 = np.linspace ( 0.0, 0.5, 101 )

  plt.clf ( )
  plt.plot ( x, y, 'o', label = 'data points' )
  plt.plot ( x2, f(x2), label = 'exact' )
  plt.plot ( x2, f_nearest(x2), label = 'nearest' )
  plt.plot ( x2, f_linear(x2), label = 'linear' )
  plt.plot ( x2, f_cubic(x2), label = 'cubic' )
  plt.grid ( True )
  plt.legend ( )
  filename = 'interp1d_test.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def f ( x ):
  import numpy as np
  value = 10 * np.exp ( - 2.0 * x ) * np.cos ( 2.0 * np.pi * 4.0 * x )
  return value

if ( __name__ == "__main__" ):
  interp1d_test ( )

