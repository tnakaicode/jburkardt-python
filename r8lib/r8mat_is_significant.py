#! /usr/bin/env python
#
def r8mat_is_significant ( m, n, r, s ):

#*****************************************************************************80
#
## R8MAT_IS_SIGNIFICANT determines if an R8MAT is relatively significant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 217
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the dimension of the matrices.
#
#    Input, real R(M,N), the vector to be compared against.
#
#    Input, real S(M,N), the vector to be compared.
#
#    Output, logical R8MAT_IS_SIGNIFICANT, is true if S is significant
#    relative to R.
#
  eps = 2.220446049250313E-016

  value = False

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      t = r[i,j] + s[i,j]
      tol = eps * abs ( r[i,j] )

      if ( tol < abs ( r[i,j] - t ) ):
        value = True
        break
  
  return value

