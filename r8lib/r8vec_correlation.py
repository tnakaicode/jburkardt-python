#! /usr/bin/env python3
#
def r8vec_correlation ( n, x, y ):

#*****************************************************************************80
#
## r8vec_correlation returns the correlation of two R8VEC's.
#
#  Discussion:
#
#    The correlation coefficient is also known as Pearson's r coefficient.
#
#    It must be the case that -1 <= r <= +1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 August 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the dimension of the vectors.
#
#    real x(n), y(n): the vectors.
#
#  Output:
#
#    real r: the correlation coefficient.
#
  import numpy as np

  x_mean = np.mean ( x )
  x_std = np.std ( x, ddof = 1 )

  y_mean = np.mean ( y )
  y_std = np.std ( y, ddof = 1 )

  if ( n <= 1 ):
    r = 0.0
  else:
    r = np.dot ( ( x - x_mean ), ( y - y_mean ) ) / x_std / y_std / ( n - 1 )

  return r

def r8vec_correlation_test ( ):

#*****************************************************************************80
#
## r8vec_correlation_test tests r8vec_correlation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 August 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_print import r8vec_print

  print ( '\n' )
  print ( 'r8vec_correlation_test:' )
  print ( '  r8vec_correlation computes the correlation of two R8VEC\'s.' )

  n = 6
  v1 = np.array ( [ 43, 21, 25, 42, 57, 59 ] )
  r8vec_print ( n, v1, '  Vector V1:' )
  v2 = np.array ( [ 99, 65, 79, 75, 87, 81 ] )
  r8vec_print ( n, v2, '  Vector V2:' )

  value = r8vec_correlation ( n, v1, v2 )
  print ( '' )
  print ( '  V1 V2 Correlation coefficient r = ', value )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_correlation_test ( )
  timestamp ( )
 
