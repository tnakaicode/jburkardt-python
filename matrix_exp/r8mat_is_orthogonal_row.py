#! /usr/bin/env python
#
def r8mat_is_orthogonal_row ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_IS_ORTHOGONAL_ROW checks whether an R8MAT is row orthogonal.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the row and column dimensions of 
#    the matrix.  M and N must be positive.
#
#    Input, real A(M,N), the matrix.
#
#    Output, real ERROR_FROBENIUS, the sum of the errors.
#
  import numpy as np
  from r8mat_is_identity import r8mat_is_identity

  b = np.dot ( a, a.transpose ( ) )

  error_frobenius = r8mat_is_identity ( m, b )

  return error_frobenius

def r8mat_is_orthogonal_row_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_ORTHOGONAL_ROW_TEST tests R8MAT_IS_ORTHOGONAL_ROW.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from orth_random import orth_random
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'R8MAT_IS_ORTHOGONAL_ROW_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_ORTHOGONAL_ROW reports the Frobenius norm difference' )
  print ( '  between A*A\' and the NxN identity matrix.' )

  nb = 4
  key = 123456789
  b = orth_random ( nb, key )

  m = 4
  n = 4
  a = b.copy ( )
  r8mat_print ( m, n, a, '  Random 4x4 orthogonal matrix:' )
  e = r8mat_is_orthogonal_row ( m, n, a )
  print ( '' )
  print ( '  Frobenius error = %g' % ( e ) )

  m = 4
  n = 3
  a = b[0:m,0:n]
  r8mat_print ( m, n, a, '  3 columns of random 4x4 orthogonal matrix:' )
  e = r8mat_is_orthogonal_row ( m, n, a )
  print ( '' )
  print ( '  Frobenius error = %g' % ( e ) )

  m = 3
  n = 4
  a = b[0:m,0:n]
  r8mat_print ( m, n, a, '  3 rows of random 4x4 orthogonal matrix:' )
  e = r8mat_is_orthogonal_row ( m, n, a )
  print ( '' )
  print ( '  Frobenius error = %g' % ( e ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_ORTHOGONAL_ROW_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_orthogonal_row_test ( )
  timestamp ( )
