#! /usr/bin/env python3
#
def stats ( x = None ):

#*****************************************************************************80
#
## stats() does stats.
#
#  Discussion:
#
#    This function computes statistical quantities for a sequence of values
#    X which are supplied one at a time, like a data stream.  The statistical
#    quantities are updated every time a new value of X is supplied.
#
#    Because we are dealing with a data stream, and not saving the previous
#    data values, it is not possible to compute the median and mode.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the next item in the sequence.
#    If X is set to Inf, then its value is ignored, and the current data
#    is returned.
#    If no argument is specified, then all internal data is reset to 0.
#
#  Output:
#
#    integer N: the number of items in the sequence.
#
#    real X_SUM: the sum of the values.
#
#    real X_MIN, X_MEAN, X_MAX: the minimum, mean, and maximum values.
#
#    real X_VAR, X_STD: the variance and standard deviation.
#
  import numpy as np

  if not hasattr ( stats, "n" ):
    stats.n = 0

  if not hasattr ( stats, "x_max" ):
    stats.x_max = - np.Inf

  if not hasattr ( stats, "x_mean" ):
    stats.x_mean = 0.0

  if not hasattr ( stats, "x_min" ):
    stats.x_min = np.Inf

  if not hasattr ( stats, "x_std" ):
    stats.x_std = 0.0

  if not hasattr ( stats, "x_sum" ):
    stats.x_sum = 0.0

  if not hasattr ( stats, "x_var" ):
    stats.var = 0.0
#
#  No input.  Reset internal data to 0.
#
  if ( x is None ):
    stats.n = 0
    stats.x_max = - np.Inf
    stats.x_mean = 0.0
    stats.x_min = np.Inf
    stats.x_std = 0.0
    stats.x_sum = 0.0
    stats.x_var = 0.0
#
#  Input that is not Inf.  Process X.
#
  elif ( x is not np.Inf ):
    stats.n = stats.n + 1
    stats.x_max = max ( stats.x_max, x )
    stats.x_min = min ( stats.x_min, x )
    stats.x_sum = stats.x_sum + x
    x_mean_old = stats.x_mean
    stats.x_mean = stats.x_sum / stats.n
    if ( stats.n == 1 ):
      stats.x_var = 0.0
      stats.x_std = 0.0
    else:
      stats.x_var = ( stats.x_var * ( stats.n - 2 ) \
          + ( x - x_mean_old ) * ( x - stats.x_mean ) ) / ( stats.n - 1 )
      stats.x_std = np.sqrt ( stats.x_var )
#
#  Set output values.
#
  n      = stats.n
  x_max  = stats.x_max
  x_min  = stats.x_min
  x_sum  = stats.x_sum
  x_mean = stats.x_mean
  x_var  = stats.x_var
  x_std  = stats.x_std

  return n, x_sum, x_min, x_mean, x_max, x_var, x_std

def stats_test ( ):

#*****************************************************************************80
#
## stats_test() tests stats().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2021
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'stats_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test stats(), with the interface:' )
  print ( '    [n,sum,min,mean,max,var,std] = stats(x)' )
  print ( '    Call 10 times with random values' )
  print ( '    Compare results with a vector calculation.' )

  n2 = 10
  x2 = rng.random ( size = n2 )

  stats ( )
  for i in range ( 0, n2 ):
    x = x2[i]
    stats ( x )

  n, x_sum, x_min, x_mean, x_max, x_var, x_std = stats ( np.Inf )

  x_sum2  = np.sum ( x2 )
  x_min2  = np.min ( x2 )
  x_mean2 = np.mean ( x2 )
  x_max2  = np.max ( x2 )
  x_var2  = np.var ( x2, ddof = 1 )
  x_std2  = np.std ( x2, ddof = 1 )

  print ( '' )
  print ( '      n1    = ', n,      ' n2    = ', n2 )
  print ( '      sum1  = ', x_sum,  ' sum2  = ', x_sum2 )
  print ( '      min1  = ', x_min,  ' min2  = ', x_min2 )
  print ( '      mean1 = ', x_mean, ' mean2 = ', x_mean2 )
  print ( '      max1  = ', x_max,  ' max2  = ', x_max2 )
  print ( '      var1  = ', x_var,  ' var2  = ', x_var2 )
  print ( '      std1  = ', x_std,  ' std2  = ', x_std2 )
#
#  Terminate.
#
  print ( '' )
  print ( 'stats_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )

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
  stats_test ( )
  timestamp ( )

