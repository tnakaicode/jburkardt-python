#! /usr/bin/env python
#
def r8mat_is_orthogonal ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_IS_ORTHOGONAL determines if a matrix is orthogonal.
#
#  Discussion:
#
#    The routine returns the Frobenius norm of A'*A - I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 April 2017
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
#    Output, real ERROR_FROBENIUS, the Frobenius orthogonality
#    error, which is zero if the matrix is exactly orthogonal.
#
  import numpy as np
  from r8mat_is_identity import r8mat_is_identity

  if ( m != n ):
    error_frobenius = float ( 'Inf' )
    return error_frobenius

  b = np.dot ( a.transpose ( ), a )

  error_frobenius = r8mat_is_identity ( n, b )

  return error_frobenius

def r8mat_is_orthogonal_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_ORTHOGONAL_TEST tests R8MAT_IS_ORTHOGONAL.
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
  from orth_random import orth_random
  from r8mat_print import r8mat_print
  from summation import summation

  print ( '' )
  print ( 'R8MAT_IS_ORTHOGONAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_ORTHOGONAL reports the Frobenius norm difference' )
  print ( '  between A\'*A and the identity matrix.' )

  n = 4
  key = 123456789
  a = orth_random ( n, key )
  r8mat_print ( n, n, a, '  Random orthogonal matrix:' )
  e = r8mat_is_orthogonal ( n, n, a )
  print ( '' )
  print ( '  Frobenius error = %g' % ( e ) )

  n = 4
  a = summation ( n, n )
  r8mat_print ( n, n, a, '  Summation matrix:' )
  e = r8mat_is_orthogonal ( n, n, a )
  print ( '' )
  print ( '  Frobenius error = %g' % ( e ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_ORTHOGONAL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_orthogonal_test ( )
  timestamp ( )
