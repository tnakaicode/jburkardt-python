#! /usr/bin/env python
#
def r8vec_is_insignificant ( n, r, s ):

#*****************************************************************************80
#
## R8VEC_IS_INSIGNIFICANT determines if an R8VEC is relatively insignificant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real R(N), the vector to be compared against.
#
#    Input, real S(N), the vector to be compared.
#
#    Output, logical R8VEC_IS_INSIGNIFICANT, is true if S is insignificant
#    relative to R.
#
  eps = 2.220446049250313E-016

  value = True

  for i in range ( 0, n ):
    t = r[i] + s[i]
    tol = eps * abs ( r[i] )

    if ( tol < abs ( r[i] - t ) ):
      value = False
      break
  
  return value

def r8vec_is_insignificant_test ( ):

#*****************************************************************************80
#
## R8VEC_IS_INSIGNIFICANT_TEST tests R8VEC_IS_INSIGNIFICANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_transpose_print import r8vec_transpose_print

  print ( '' )
  print ( 'R8VEC_IS_INSIGNIFICANT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_IS_INSIGNIFICANT is TRUE if an R8VEC only contains' )
  print ( '  negative entries.' )

  eps = 2.220446049250313E-016

  n = 3

  x = np.array ( [ 1.0, 2.0, 100.0 ] )
  y = 100000.0 * eps * np.array ( [ 1.0, 2.0, 100.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  r8vec_transpose_print ( n, y, '  Y:' )
  if ( r8vec_is_insignificant ( n, x, y ) ):
    print ( '  Y is insignificant compared to X.' )
  else:
    print ( '  Y is NOT insignificant compared to X.' )

  x = np.array ( [ 1.0, 2.0, 100.0 ] )
  y = 10.0 * eps * np.array ( [ 1.0, 0.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  r8vec_transpose_print ( n, y, '  Y:' )
  if ( r8vec_is_insignificant ( n, x, y ) ):
    print ( '  Y is insignificant compared to X.' )
  else:
    print ( '  Y is NOT insignificant compared to X.' )

  x = np.array ( [ 1.0, 2.0, 100.0 ] )
  y = 0.0001 * eps * np.array ( [ 1.0, 2.0, 100.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  r8vec_transpose_print ( n, y, '  Y:' )
  if ( r8vec_is_insignificant ( n, x, y ) ):
    print ( '  Y is insignificant compared to X.' )
  else:
    print ( '  Y is NOT insignificant compared to X.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IS_INSIGNIFICANT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_is_insignificant_test ( )
  timestamp ( )
