#! /usr/bin/env python3
#
def tri_u_inverse ( n, a ):

#*****************************************************************************80
#
#% TRI_U_INVERSE inverts an upper triangular R8MAT.
#
#  Discussion:
#
#    An R8MAT is an array of R8 values.
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
#    24 March 2015
#
#  Author:
#
#    John Burkardt.
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
#    Input, integer N, the order of the matrix.
#
#    Input, real A(N,N), the upper triangular matrix.
#
#    Output, real B(N,N), the inverse matrix.
#
  import numpy as np

  b = np.zeros ( ( n, n ) )

  for j in range ( n - 1, -1, -1 ):
    for i in range ( n - 1, -1, -1 ):

      if ( i == j ):
        b[i,j] = 1.0 / a[i,j]
      elif ( i < j ):
        t = 0.0
        for k in range ( i + 1, j + 1 ):
          t = t + a[i,k] * b[k,j]
        b[i,j] = - t / a[i,i]

  return b

