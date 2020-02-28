#! /usr/bin/env python
#
def r8mat_u_inverse ( n, a ):

#*****************************************************************************80
#
## R8MAT_U_INVERSE inverts an upper triangular R8MAT.
#
#  Discussion:
#
#    An upper triangular matrix is a matrix whose only nonzero entries
#    occur on or above the diagonal.
#
#    The inverse of an upper triangular matrix is an upper triangular matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 August 2017
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, number of rows and columns in the matrix.
#
#    Input, real A(N,N), the upper triangular matrix.
#
#    Output, real B(N,N), the inverse matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for j in range ( n - 1, -1, -1 ):
    for i in range ( n - 1, -1, -1 ):

      if ( i == j ):
        b[i,j] = 1.0 / a[i,j]
      elif ( i < j ):
        b[i,j] = - np.dot ( a[i,i+1:n],  b[i+1:n,j] ) / a[i,i]

  return b

def r8mat_u_inverse_test ( ):

#*****************************************************************************80
#
## R8MAT_U_INVERSE_TEST tests R8MAT_U_INVERSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_print import r8mat_print

  n = 4

  a = np.array ( [ \
    [ 1.0, 2.0, 4.0,  7.0 ], \
    [ 0.0, 3.0, 5.0,  8.0 ], \
    [ 0.0, 0.0, 6.0,  9.0 ], \
    [ 0.0, 0.0, 0.0, 10.0 ] ] )

  print ( '' )
  print ( 'R8MAT_U_INVERSE_TEST' )
  print ( '  R8MAT_U_INVERSE inverts an upper triangular matrix.' )

  r8mat_print ( n, n, a, '  Input matrix A' )
 
  b = r8mat_u_inverse ( n, a )
 
  r8mat_print ( n, n, b, '  Inverse matrix B:' )
 
  c = np.dot ( a, b )

  r8mat_print ( n, n, c, '  Product C = A * B:' )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_u_inverse_test ( )
  timestamp ( )
 
