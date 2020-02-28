#! /usr/bin/env python
#
def stats ( x, n ):

#*****************************************************************************80
#
## STATS computes statistics for a given array.
#
#  Discussion:
#
#    This procedure computes the average and variance of an array.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Input, real X(N), the array to be analyzed.
#
#    Input, integer N, the dimension of the array.
#
#    Output, real AV, the average value.
#
#    Output, real VAR, the variance.
#
#    Output, real XMIN, XMAX, the minimum and maximum entries.
#
  import numpy as np

  xmin = np.min ( x[0:n] )
  xmax = np.max ( x[0:n] )
  av = np.mean ( x[0:n] )
  var = np.var ( x[0:n], ddof = 1 )
 
  return av, var, xmin, xmax

def stats_test ( ):

#*****************************************************************************80
#
## STATS_TEST tests STATS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'STATS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  STATS computes min, max, mean and variance for a vector.' )

  n = 5
  x = np.array ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ] )

  print ( '' )
  print ( '  Vector X:' )
  print ( '    ' ),
  for i in range ( 0, n ):
    print ( '%g' % ( x[i] ) ),
  print ( '' )

  av, var, xmin, xmax = stats ( x, n )

  print ( '' )
  print ( '  %g <= X <= %g' % ( xmin, xmax ) )
  print ( '  Mean = %g, Variance = %g' % ( av, var ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'STATS_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  stats_test ( )
  timestamp ( )

