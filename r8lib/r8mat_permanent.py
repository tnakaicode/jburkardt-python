#! /usr/bin/env python
#
def r8mat_permanent ( n, a ):

#*****************************************************************************80
#
## R8MAT_PERMANENT computes the permanent of an R8MAT.
#
#  Discussion:
#
#    The permanent function is similar to the determinant.  Recall that
#    the determinant of a matrix may be defined as the sum of all the
#    products:
#
#      S * A(1,I(1)) * A(2,I(2)) * ... * A(N,I(N))
#
#    where I is any permutation of the columns of the matrix, and S is the
#    sign of the permutation.  By contrast, the permanent function is
#    the (unsigned) sum of all the products
#
#      A(1,I(1)) * A(2,I(2)) * ... * A(N,I(N))
#
#    where I is any permutation of the columns of the matrix.  The only
#    difference is that there is no permutation sign multiplying each summand.
#
#    Symbolically, then, the determinant of a 2 by 2 matrix
#
#      a b
#      c d
#
#    is a*d-b*c, whereas the permanent of the same matrix is a*d+b*c.
#
#
#    The permanent is invariant under row and column permutations.
#    If a row or column of the matrix is multiplied by S, then the
#      permanent is likewise multiplied by S.
#    If the matrix is square, then the permanent is unaffected by
#      transposing the matrix.
#    Unlike the determinant, however, the permanent does change if
#      one row is added to another, and it is not true that the
#      permanent of the product is the product of the permanents.
#
#
#    Note that if A is a matrix of all 1's and 0's, then the permanent
#    of A counts exactly which permutations hit exactly 1's in the matrix.
#    This fact can be exploited for various combinatorial purposes.
#
#    For instance, setting the diagonal of A to 0, and the offdiagonals
#    to 1, the permanent of A counts the number of derangements of N
#    objects.
#
#    Setting the diagonal of A to 0, and ensuring that the offdiagonal
#    entries are symmetric, then A is the adjacency matrix of a graph,
#    and its permanent counts the number of perfect matchings.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 June 2015
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
#    Input, real A(N,N), the value of the matrix.
#
#    Output, real PERM, the value of the permanent of the matrix.
#
  import numpy as np
  from subset_gray_next import subset_gray_next

  more = False

  c = np.zeros ( n )

  for i in range ( 0, n ):
    s = 0.0
    for j in range ( 0, n ):
      s = s + a[i,j]
    c[i] = a[i,n-1] - 0.5 * s

  p = 0.0
  sgn = -1.0
  b = np.zeros ( n )
  ncard = 0

  while ( True ):

    sgn = -sgn
#
#  The proper form of this call to SUBSET_GRAY_NEXT has not been set yet.
#
    b, more, ncard, iadd = subset_gray_next ( n - 1, b, more, ncard )

    if ( ncard != 0 ):
      z = ( 2 * b[iadd] - 1 )
      for i in range ( 0, n ):
        c[i] = c[i] + z * a[i,iadd]

    p = p + sgn * np.prod ( c )

    if ( not more ):
      break

  perm = p * ( 4 * ( n % 2 ) - 2 )

  return perm

def r8mat_permanent_test ( ):

#*****************************************************************************80
#
## R8MAT_PERMANENT_TEST tests R8MAT_PERMANENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PERMANENT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PERMANENT: the matrix permanent function.' )
  print ( '  We will analyze matrices with 0 diagonal and' )
  print ( '  1 on all offdiagonals.' )
  print ( '' )
  print ( '  Order	    Permanent.' )
  print ( '' )
 
  for n in range ( 2, 13 ):
 
    a = np.ones ( [ n, n ] )

    for i in range ( 0, n ):
      a[i,i] = 0.0

    perm = r8mat_permanent ( n, a )
 
    print ( '  %2d  %18g' % ( n, perm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PERMANENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_permanent_test ( )
  timestamp ( )

