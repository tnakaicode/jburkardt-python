#! /usr/bin/env python
#
def perm1_cycle_to_index ( n, p1 ):

#*****************************************************************************80
#
## PERM1_CYCLE_TO_INDEX: permutation of (1,...,N) from cycle to index form.
#
#  Example:
#
#    Input:
#
#      N = 9
#      P1 = -1, 2, 3, 9, -4, 6, 8, -5, 7
#
#    Output:
#
#      P2 = 2, 3, 9, 6, 7, 8, 5, 4, 1
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
#    Input, integer P1(N), the permutation, in cycle form.
#
#    Output, integer P2(N), the permutation, in standard index form.
#
  import numpy as np

  p2 = np.zeros ( n, dtype = np.int32 )

  for j in range ( 1, n + 1 ):

    k1 = p1[j-1]

    if ( k1 < 0 ):
      k1 = -k1
      k3 = k1

    if ( j + 1 <= n ):
      k2 = p1[j]
      if ( k2 < 0 ):
        k2 = k3
    else:
      k2 = k3

    p2[k1-1] = k2

  return p2

def perm1_cycle_to_index_test ( ):

#*****************************************************************************80
#
## PERM1_CYCLE_TO_INDEX_TEST tests PERM1_CYCLE_TO_INDEX.
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
  from perm1_index_to_cycle import perm1_index_to_cycle
  from perm1_print import perm1_print

  n = 9
  p1 = np.array ( [ 2,3,9,6,7,8,5,4,1 ] )

  print ( '' )
  print ( 'PERM1_CYCLE_TO_INDEX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM1_CYCLE_TO_INDEX converts a permutation of (1,...,N) from' )
  print ( '  cycle to standard index form.' )
 
  perm1_print ( n, p1, '  The standard index form permutation:' )
 
  p2 = perm1_index_to_cycle ( n, p1 )

  perm1_print ( n, p2, '  The permutation in cycle form:' )

  p3 = perm1_cycle_to_index ( n, p2 )
 
  perm1_print ( n, p3, '  The standard index form permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM1_CYCLE_TO_INDEX_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm1_cycle_to_index_test ( )
  timestamp ( )

