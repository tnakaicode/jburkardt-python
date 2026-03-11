#! /usr/bin/env python3
#
def stats_test ( ):

#*****************************************************************************80
#
## stats_test() tests some scipy() statistics functions.
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
  from scipy.stats import norm
  import numpy as np
 
  print ( '' )
  print ( 'stats_test():' )
  print ( '  Test some scipy() statistics functions.' )

  x = np.array ( [ -2, -1., 0, 1, 3, 4, 6 ] )

  print ( x )
  print ( norm.pdf ( x ) )
  print ( norm.cdf ( x ) )
#
#  Find median.
#
  p = np.linspace ( 0.1, 0.9, 9 )
  print ( norm.ppf ( p ) )
#
#  Print 5 random samples.
#
  x = norm.rvs ( size = 5 )
  print ( x )
#
#  Plot pdf, cdf, ppf
#
  x = np.linspace ( -2.0, +2.0, 101 )
  pdf = norm.pdf ( x )
  cdf = norm.cdf ( x )
  ppf = norm.ppf ( x )
#
#  Random sample, then histogram.
#
  return

if ( __name__ == "__main__" ):
  stats_test ( )
