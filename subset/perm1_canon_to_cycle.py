#! /usr/bin/env python
#
def perm1_canon_to_cycle ( n, p1 ):

#*****************************************************************************80
#
## PERM1_CANON_TO_CYCLE: permutation of (1,...,N) from canonical to cycle form.
#
#  Example:
#
#    Input:
#
#      4 5 2 1 6 3
#
#    Output:
#
#      -4 5 -2 -1 6 3,
#      indicating the cycle structure
#      ( 4, 5 ) ( 2 ) ( 1, 6, 3 )
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
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms,
#    Addison Wesley, 1968, page 176.
#
#  Parameters:
#
#    Input, integer N, the number of objects permuted.
#
#    Input, integer P1(N), the permutation, in canonical form.
#
#    Output, integer P2(N), the permutation, in cycle form.
#
  import numpy as np

  p2 = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    p2[i] = p1[i]

  pmin = p2[0] + 1

  for i in range ( 0, n ):

    if ( p2[i] < pmin ):
      pmin = p2[i]
      p2[i] = - p2[i]

  return p2

def perm1_canon_to_cycle_test ( ):

#*****************************************************************************80
#
## PERM1_CANON_TO_CYCLE_TEST tests PERM1_CANON_TO_CYCLE.
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
  from perm1_print import perm1_print

  n = 6
  p1 = np.array ( [ 4, 5, 2, 1, 6, 3 ] )

  print ( '' )
  print ( 'PERM1_CANON_TO_CYCLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM1_CANON_TO_CYCLE converts a permutation of (1,...,N) from' )
  print ( '  canonical to cycle form.' )
 
  perm1_print ( n, p1, '  The permutation in canonical form:' )
 
  p2 = perm1_canon_to_cycle ( n, p1 )

  perm1_print ( n, p2, '  The permutation in cycle form:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM1_CANON_TO_CYCLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm1_canon_to_cycle_test ( )
  timestamp ( )
 
