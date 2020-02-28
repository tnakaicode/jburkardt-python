#! /usr/bin/env python
#
def r8mat_is_zero_one ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_IS_ZERO_ONE checks for a zero-one matrix.
#
#  Discussion:
#
#    The routine returns the Frobenius norm of A - I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, real A(M,N), the matrix.
#
#    Output, bool R8MAT_IS_ZERO_ONE, is True if the matrix is a
#    zero-one matrix, and False otherwise.
#
  value = True

  for i in range ( 0, m ):
    for j in range ( 0, n ):

      if ( a[i,j] != 0.0 and a[i,j] != 1.0 ):
        value = False
        return value

  return value

def r8mat_is_zero_one_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_ZERO_ONE_TEST tests R8MAT_IS_ZERO_ONE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'R8MAT_IS_ZERO_ONE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_ZERO_ONE reports whether a matrix' )
  print ( '  only has entries of 0 and 1.' )

  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  r8mat_print ( m, n, a, '  Zero matrix:' )
  value = r8mat_is_zero_one ( m, n, a )
  print ( '' )
  print ( '  Zero/one = %s' % ( value ) )

  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0
  r8mat_print ( m, n, a, '  Identity matrix:' )
  value = r8mat_is_zero_one ( m, n, a )
  print ( '' )
  print ( '  Zero/one = %s' % ( value ) )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = a[i,j] + float ( i * j ) / 1000
  r8mat_print ( m, n, a, '  Almost identity matrix:' )
  value = r8mat_is_zero_one ( m, n, a )
  print ( '' )
  print ( '  Zero/one = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_ZERO_ONE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_zero_one_test ( )
  timestamp ( )
