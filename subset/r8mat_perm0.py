#! /usr/bin/env python
#
def r8mat_perm0 ( n, a, p ):

#*****************************************************************************80
#
## R8MAT_PERM0 applies a permutation of (0,...,N-1) to a square R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 June 2015
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
#    Input, real A(N,N), the matrix to be permuted.
#
#    Input, integer P(N), the permutation.  P(I) is the new number of row
#    and column I.
#
#    Output, integer A(N,N), the permuted matrix.
#
  from perm0_cycle import perm0_cycle

  s, nc, tag = perm0_cycle ( n, p )

  for i in range ( 0, n ):

    i1 = - tag[i] * p[i]

    if ( 0 < i1 ):

      lc = 0

      while ( True ):

        i1 = tag[i1] * p[i1]
        lc = lc + 1

        if ( i1 < 0 ):
          break

      i1 = i

      for j in range ( 0, n ):

        if ( tag[j] < 0 ):

          j2 = j
          k = lc

          while ( True ):

            j1 = j2
            it = a[i1,j1]

            while ( True ):

              i1 = p[i1]
              j1 = p[j1]

              t = a[i1,j1]
              a[i1,j1] = it
              it = t

              if ( j1 != j2 ):
                continue

              k = k - 1

              if ( i1 == i ):
                break

            j2 = p[j2]

            if ( k == 0 ):
              break

  return a

def r8mat_perm0_test ( ):

#*****************************************************************************80
#
## R8MAT_PERM0_TEST test R8MAT_PERM0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print
  from perm0_print import perm0_print

  n = 9

  p = np.array ( [ 1, 2, 8, 5, 6, 7, 4, 3, 0 ] )

  print ( '' )
  print ( 'R8MAT_PERM0_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PERM0 reorders an integer matrix in place.' )
  print ( '  The rows and columns use the same permutation.' )

  a = np.zeros ( [ n, n ], dtype = np.float64 )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = float ( ( i + 1 ) * 10 + j + 1 )

  r8mat_print ( n, n, a, '  The input matrix:' )
 
  perm0_print ( n, p, '  The row and column permutation:' )
 
  a = r8mat_perm0 ( n, a, p )
 
  r8mat_print ( n, n, a, '  The permuted matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PERM0_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_perm0_test ( )
  timestamp ( )


