#! /usr/bin/env python
#
def r8mat_is_identity ( n, a ):

#*****************************************************************************80
#
## R8MAT_IS_IDENTITY determines if a matrix is the identity.
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
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real A(N,N), the matrix.
#
#    Output, real ERROR_FROBENIUS, the Frobenius norm
#    of the difference matrix A - I, which would be exactly zero
#    if A were the identity matrix.
#
  import numpy as np

  error_frobenius = 0.0

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        error_frobenius = error_frobenius + ( a[i,j] - 1.0 ) ** 2
      else:
        error_frobenius = error_frobenius + a[i,j] ** 2

  error_frobenius = np.sqrt ( error_frobenius );

  return error_frobenius

def r8mat_is_identity_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_IDENTITY_TEST tests R8MAT_IS_IDENTITY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'R8MAT_IS_IDENTITY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_IDENTITY reports the Frobenius norm difference' )
  print ( '  between a given matrix A and the identity matrix.' )

  n = 4
  a = np.zeros ( [ n, n ] )
  r8mat_print ( n, n, a, '  Zero matrix:' )
  e = r8mat_is_identity ( n, a )
  print ( '' )
  print ( '  Difference is %g' % ( e ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0
  r8mat_print ( n, n, a, '  Identity matrix:' )
  e = r8mat_is_identity ( n, a )
  print ( '' )
  print ( '  Difference is %g' % ( e ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = a[i,j] + float ( i * j ) / 1000
  r8mat_print ( n, n, a, '  Almost identity matrix:' )
  e = r8mat_is_identity ( n, a )
  print ( '' )
  print ( '  Difference is %g' % ( e ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_IDENTITY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_identity_test ( )
  timestamp ( )
