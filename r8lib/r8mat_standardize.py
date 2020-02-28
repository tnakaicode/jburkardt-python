#! /usr/bin/env python
#
def r8mat_standardize ( m, n, x ):

#*****************************************************************************80
#
## R8MAT_STANDARDIZE standardizes an R8MAT.
#
#  Discussion:
#
#    Each column of the output array has 0 mean and unit standard deviation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the dimensions of the array.
#
#    Input, real X(M,N), the array to be standardized.
#
#    Output, real XS(M,N), the standardized array.
#
  import numpy as np

  mu = np.mean ( x, axis = 0 )
  sigma = np.std ( x, axis = 0, ddof = 1 )
  xs = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    if ( sigma[j] != 0.0 ):
      xs[:,j] = ( xs[:,j] - mu[j] ) / sigma[j]

  return xs

def r8mat_standardize_test ( ):

#*****************************************************************************80
#
## R8MAT_STANDARDIZE_TEST tests R8MAT_STANDARDIZE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 October 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print
  from r8mat_uniform_ab import r8mat_uniform_ab

  print ( '' )
  print ( 'R8MAT_STANDARDIZE_TEST' )
  print ( '  R8MAT_STANDARDIZE shifts and scales an R8MAT so that' )
  print ( '  each column has zero mean and unit standard deviation.' )

  m = 10
  n = 3
  a = -5.0
  b = 15.0
  seed = 123456789

  x, seed = r8mat_uniform_ab ( m, n, a, b, seed )
 
  r8mat_print ( m, n, x, '  Vector X:' )
  mu = np.mean ( x, axis = 0 )
  sigma = np.std ( x, axis = 0, ddof = 1 )
  xmax = np.ndarray.max ( x, axis = 0 )
  xmin = np.ndarray.min ( x, axis = 0 )
  print ( '' )
  print ( '  mean(X) = %g  %g  %g' % ( mu[0], mu[1], mu[2] ) )
  print ( '  std(X)  = %g  %g  %g' % ( sigma[0], sigma[1], sigma[2] ) )
  print ( '  max(X)  = %g  %g  %g' % ( xmax[0], xmax[1], xmax[2] ) )
  print ( '  min(X)  = %g  %g  %g' % ( xmin[0], xmin[1], xmin[2] ) )

  xs = r8mat_standardize ( m, n, x )

  r8mat_print ( m, n, xs, '  Vector XS:' )
  mu = np.mean ( xs, axis = 0 )
  sigma = np.std ( xs, axis = 0, ddof = 1 )
  xmax = np.ndarray.max ( xs, axis = 0 )
  xmin = np.ndarray.min ( xs, axis = 0 )
  print ( '' )
  print ( '  mean(X) = %g  %g  %g' % ( mu[0], mu[1], mu[2] ) )
  print ( '  std(X)  = %g  %g  %g' % ( sigma[0], sigma[1], sigma[2] ) )
  print ( '  max(X)  = %g  %g  %g' % ( xmax[0], xmax[1], xmax[2] ) )
  print ( '  min(X)  = %g  %g  %g' % ( xmin[0], xmin[1], xmin[2] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_STANDARDIZE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_standardize_test ( )
  timestamp ( )
