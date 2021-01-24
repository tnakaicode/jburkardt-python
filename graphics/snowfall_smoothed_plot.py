#! /usr/bin/env python3
#
def snowfall_smoothed_plot ( ):

#*****************************************************************************80
#
## snowfall_smoothed_plot plots smoothed snowfall data.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2019
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np
  import platform

  print ( '' )
  print ( 'snowfall_smoothed_plot:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Make a line plot of smoothed snowfall data.' )
#
#  Read the data.
#
  filename = 'snowfall_data.txt'
  data = np.loadtxt ( filename )

  year = data[:,0]
  total = data[:,9]
#
#  Smooth the data.
#
  n = len ( total )
  total = r8vec_smooth ( n, total, 10 )
#
#  Plot the data.
#
  plt.plot ( year, total, linewidth = 3, color = 'b' )
  plt.grid ( True )
  plt.xlabel ( '<--- Year --->', fontsize = 16 )
  plt.ylabel ( '<--- Total Snowfall (inches) --->', fontsize = 16 )
  plt.title ( 'Yearly Snowfall at Michigan Tech', fontsize = 16 )

  filename = 'snowfall_smoothed_plot.png'
  plt.savefig ( filename )
  print ( '' )
  print ( '  Graphics saved as "%s"' % ( filename ) )
  plt.show ( block = False )

  plt.clf ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'snowfall_smoothed_plot' )
  print ( '  Normal end of execution.' )
  return

def r8vec_smooth ( n, x, s ):

#*****************************************************************************80
#
## r8vec_smooth smooths an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    Except for the beginning and ending entries, the vector values
#    are replaced by averages of 2*S+1 neighbors.
#
#  Example:
#
#    S = 2
#
#    Z(1)   =                     X(1)
#    Z(2)   = (          X(1)   + X(2)   + X(3) ) / 3
#    Z(3)   = ( X(1)   + X(2)   + X(3)   + X(4)   + X(5) ) / 5
#    Z(4)   = ( X(2)   + X(3)   + X(4)   + X(5)   + X(6) ) / 5
#    ...
#    Z(N-2) = ( X(N-4) + X(N-3) + X(N-2) + X(N-1) + X(N) ) / 5
#    Z(N-1) =          ( X(N-2) + X(N-1) + X(N) ) / 3
#    Z(N) =                       X(N)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of X.
#
#    Input, real X(N), the vector to be smoothed.
#
#    Output, real Z(N), the smoothed vector.
#
  import numpy as np

  z = np.zeros ( n )

  for j in range ( 1, s + 1 ):
    z[j-1] = np.sum ( x[0:2*j-1] ) / ( 2 * j - 1 )

  for j in range ( s + 1, n - s + 1 ):
    z[j-1] = np.sum ( x[j-s-1:j+s] ) / ( 2 * s + 1 )

  for j in range ( s, 0, -1 ):
    z[n-j] = np.sum ( x[n-(2*j-1):n] ) / ( 2 * j - 1 )

  return z

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  snowfall_smoothed_plot ( )
  timestamp ( )
 
