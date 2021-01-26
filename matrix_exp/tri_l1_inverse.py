#! /usr/bin/env python3
#
def tri_l1_inverse ( n, a ):

#*****************************************************************************80
#
## TRI_L1_INVERSE inverts a double precision unit lower triangular matrix.
#
#  Discussion:
#
#    A unit lower triangular matrix is a matrix with only 1's on the main
#    diagonal, and only 0's above the main diagonal.
#
#    The inverse of a unit lower triangular matrix is also
#    a unit lower triangular matrix.
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
#    John Burkardt
#
#  Reference:
#
#    A Nijenhuis, H Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, number of rows and columns in the matrix.
#
#    Input, real A(N,N), the unit lower triangular matrix.
#
#    Output, real B(N,N), the inverse matrix.
#
  import numpy as np

  b = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i ):
        b[i,j] = 1.0
      elif ( j < i ):
        t = 0.0
        for k in range ( 0, i ):
          t = t + a[i,k] * b[k,j]
        b[i,j] = - t

  return b

