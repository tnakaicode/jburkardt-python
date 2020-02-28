#! /usr/bin/env python
#
def r8mat_2perm0 ( m, n, a, p, q ):

#*****************************************************************************80
#
#% R8MAT_2PERM0 uses permutations of (0,...,M-1) and (0,...,N-1) on an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 June 2015
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
#    Input, integer M, the number of rows in the matrix.
#
#    Input, integer N, the number of columns in the matrix.
#
#    Input, real A(M,N), the matrix to be permuted.
#
#    Input, integer P(M), the row permutation.  P(I) is the new number of row I.
#
#    Input, integer Q(N), the column permutation.  Q(I) is the new number
#    of column I. 
#
#    Output, real A(M,N), the permuted matrix.
#
  from perm0_cycle import perm0_cycle

  sp, ncp, tagp = perm0_cycle ( m, p )

  sq, ncq, tagq = perm0_cycle ( n, q )

  for i in range ( 0, m ):

    i1 = - tagp[i] * p[i]

    if ( 0 < i1 ):

      lc = 0

      while ( True ):

        i1 = tagp[i1] * p[i1]
        lc = lc + 1

        if ( i1 < 0 ):
          break

      i1 = i

      for j in range ( 0, n ):

        if ( tagq[j] < 0 ):

          j2 = j
          k = lc

          while ( True ):

            j1 = j2
            it = a[i1,j1]

            while ( True ):

              i1 = p[i1]
              j1 = q[j1]

              t        = a[i1,j1]
              a[i1,j1] = it
              it       = t

              if ( j1 != j2 ):
                continue

              k = k - 1

              if ( i1 == i ):
                break

            j2 = q[j2]

            if ( k == 0 ):
              break

  return a

def r8mat_2perm0_test ( ):

#*****************************************************************************80
#
## R8MAT_2PERM0_TEST test R8MAT_2PERM0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from perm0_print import perm0_print
  from r8mat_print import r8mat_print

  m = 9
  n = 7

  p = np.array ( [ 1,2,8,5,6,7,4,3,0 ] )
  q = np.array ( [ 2,3,4,5,6,0,1 ] )

  print ( '' )
  print ( 'R8MAT_2PERM0_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_2PERM0 reorders an R8MAT in place.' )
  print ( '  Rows and columns use different permutations.' )

  a = np.zeros ( [ m, n ] )
 
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = float ( ( i + 1 ) * 10 + ( j + 1 ) )
 
  r8mat_print ( m, n, a, '  The input matrix:' )
 
  perm0_print ( m, p, '  The row permutation:' )

  perm0_print ( n, q, '  The column permutation:' )
 
  a = r8mat_2perm0 ( m, n, a, p, q )
 
  r8mat_print ( m, n, a, '  The permuted matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_2PERM0_TEST' )
  print ( '  Normal end of execution.' )

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_2perm0_test ( )
  timestamp ( )
