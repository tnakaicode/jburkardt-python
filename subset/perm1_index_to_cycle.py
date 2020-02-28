#! /usr/bin/env python
#
def perm1_index_to_cycle ( n, p1 ):

#*****************************************************************************80
#
## PERM1_INDEX_TO_CYCLE: permutation of (1,...,N) from index to cycle form.
#
#  Example:
#
#    Input:
#
#      N = 9
#      P1 = 2, 3, 9, 6, 7, 8, 5, 4, 1
#
#    Output:
#
#      P2 = -1, 2, 3, 9, -4, 6, 8, -5, 7
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    24 June 2015
#
#  Author:
#
#    John Burkardt
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
#    Input, integer N, the number of objects being permuted.
#
#    Input, integer P1(N), the permutation, in standard index form.
#
#    Output, integer P2(N), the permutation, in cycle form.
#
  import numpy as np

  p2 = np.zeros ( n, dtype = np.int32 )

  i = 0
  j = 1

  while ( j <= n ):

    if ( p1[j-1] < 0 ):

      j = j + 1

    else:

      k = j

      i = i + 1
      p2[i-1] = -k

      while ( p1[k-1] != j ):
        i = i + 1
        p2[i-1] = p1[k-1]
        p1[k-1] = -p1[k-1]
        k = abs ( p1[k-1] )

      p1[k-1] = -p1[k-1]

  for i in range ( 0, n ):
    p1[i] = abs ( p1[i] )

  return p2

def perm1_index_to_cycle_test ( ):

#*****************************************************************************80
#
## PERM1_INDEX_TO_CYCLE_TEST tests PERM1_INDEX_TO_CYCLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from perm1_cycle_to_index import perm1_cycle_to_index
  from perm1_print import perm1_print

  n = 9
  p1 = np.array ( [ 2,3,9,6,7,8,5,4,1 ] )

  print ( '' )
  print ( 'PERM1_INDEX_TO_CYCLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM1_INDEX_TO_CYCLE converts a permutation of (1,...,N) from' )
  print ( '  standard index to cycle form.' )
 
  perm1_print ( n, p1, '  The standard index form permutation:' )
 
  p2 = perm1_index_to_cycle ( n, p1 )

  perm1_print ( n, p2, '  The permutation in cycle form:' )

  p3 = perm1_cycle_to_index ( n, p2 )
 
  perm1_print ( n, p3, '  The standard index form permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM1_INDEX_TO_CYCLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm1_index_to_cycle_test ( )
  timestamp ( )

