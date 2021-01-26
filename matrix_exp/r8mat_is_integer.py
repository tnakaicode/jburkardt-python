#! /usr/bin/env python
#
def r8mat_is_integer ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_IS_INTEGER checks whether A has only integer entries.
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
#    Output, real ERROR_FROBENIUS, the Frobenius norm of the
#    difference between A and the nearest integer matrix.
#
  import numpy as np

  error_frobenius = 0.0

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      t = a[i,j] - np.round ( a[i,j] )
      error_frobenius = error_frobenius + t * t

  error_frobenius = np.sqrt ( error_frobenius )

  return error_frobenius

def r8mat_is_integer_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_INTEGER_TEST tests R8MAT_IS_INTEGER.
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
  from invol import invol
  from maxij import maxij
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'R8MAT_IS_INTEGER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_INTEGER reports the Frobenius norm of the' )
  print ( '  distance between a matrix A and the nearest integer matrix.' )

  m = 5
  n = 4
  a = maxij ( m, n )
  r8mat_print ( m, n, a, '  MAXIJ matrix:' )
  value = r8mat_is_integer ( m, n, a )
  print ( '' )
  print ( '  Frobenius norm = %g' % ( value ) )

  n = 4
  a = invol ( n )
  r8mat_print ( n, n, a, '  INVOL matrix:' )
  value = r8mat_is_integer ( n, n, a )
  print ( '' )
  print ( '  Frobenius norm = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_INTEGER_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_integer_test ( )
  timestamp ( )
