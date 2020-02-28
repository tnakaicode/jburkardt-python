#! /usr/bin/env python3
#
def r8vec_standardize ( n, x ):

#*****************************************************************************80
#
## r8vec_standardize standarizes an R8VEC.
#
#  Discussion:
#
#    The output vector will have 0 mean and unit standard deviation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real X(N), the vector to be standardized.
#
#    Output, real XS(N), the standardized vector.
#
  import numpy as np

  mu = np.mean ( x )
  sigma = np.std ( x, ddof = 1 )
  
  if ( sigma != 0.0 ):
    xs = ( x - mu ) / sigma
  else:
    xs = np.zeros ( n )

  return xs

def r8vec_standardize_test ( ):

#*****************************************************************************80
#
## r8vec_standardize_test tests r8vec_standardize.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ( '' )
  print ( 'r8vec_standardize_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec_standardize shifts and scales an R8VEC so that' )
  print ( '  it has zero mean and unit standard deviation.' )

  n = 10
  a = -5.0
  b = 15.0
  seed = 123456789

  x, seed = r8vec_uniform_ab ( n, a, b, seed )
 
  r8vec_print ( n, x, '  Vector X:' )
  mu = np.mean ( x )
  sigma = np.std ( x, ddof = 1 )
  xmax = np.ndarray.max ( x )
  xmin = np.ndarray.min ( x )
  print ( '' )
  print ( '  mean(X) = %g' % ( mu ) )
  print ( '  std(X)  = %g' % ( sigma ) )
  print ( '  max(X)  = %g' % ( xmax ) )
  print ( '  min(X)  = %g' % ( xmin ) )

  xs = r8vec_standardize ( n, x )

  r8vec_print ( n, xs, '  Vector XS:' )
  mu = np.mean ( xs )
  sigma = np.std ( xs, ddof = 1 )
  xmax = np.ndarray.max ( xs )
  xmin = np.ndarray.min ( xs )
  print ( '' )
  print ( '  mean(XS) = %g' % ( mu ) )
  print ( '  std(XS)  = %g' % ( sigma ) )
  print ( '  max(XS)  = %g' % ( xmax ) )
  print ( '  min(XS)  = %g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_standardize_test' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_standardize_test ( )
  timestamp ( )
 
