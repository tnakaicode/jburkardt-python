#! /usr/bin/env python
#
def r8mat_diff_frobenius ( m, n, a, b ):

#*****************************************************************************80
#
## R8MAT_DIFF_FROBENIUS: Frobenius norm of the difference of two R8MAT's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), B(M,N), the matrices for which we
#    are to compute the Frobenius norm of the difference.
#
#    Output, real DIF, the Frobenius norm of A-B.
#
  import numpy as np

  diff = np.sqrt ( np.sum ( np.sum ( ( a[0:m,0:n] - b[0:m,0:n] ) ** 2 ) ) )

  return diff

def r8mat_diff_frobenius_test ( ):

#*****************************************************************************80
#
## R8MAT_DIFF_FROBENIUS_TEST tests R8MAT_DIFF_FROBENIUS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'R8MAT_DIFF_FROBENIUS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_DIFF_FROBENIUS computes the Frobenius norm of' )
  print ( '  the difference of two R8MATs.' )

  m = 2
  n = 3

  a = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], \
    [ 21.0, 22.0, 23.0 ] ] )

  b = np.array ( [ \
    [ 10.0, 13.0, 12.0 ], \
    [ 23.0, 21.0, 24.0 ] ] )

  c = a - b

  r8mat_print ( m, n, a, '  A:' )
  r8mat_print ( m, n, b, '  B:' )
  r8mat_print ( m, n, c, '  C = A-B:' )

  diff = r8mat_diff_frobenius ( m, n, a, b )

  print ( '' )
  print ( '  Frobenius norm ||A-B|| = %g' % ( diff ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_DIFF_FROBENIUS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_diff_frobenius_test ( )
  timestamp ( )
 
