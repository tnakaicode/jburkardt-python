#! /usr/bin/env python
#
def perm1_cycle_to_canon ( n, p1 ):

#*****************************************************************************80
#
## PERM1_CYCLE_TO_CANON: permutation of (1,...,N) from cycle to canonical form.
#
#  Example:
#
#    Input:
#
#      -6 3 1 -5, 4 -2,
#      indicating the cycle structure
#      ( 6, 3, 1 ) ( 5, 4 ) ( 2 )
#
#    Output:
#
#      4 5 2 1 6 3
#
#  Discussion:
#
#    The procedure is to "rotate" the elements of each cycle so that
#    the smallest element is first:
#
#      ( 1, 6, 3 ) ( 4, 5 ) ( 2 )
#
#    and then to sort the cycles in decreasing order of their first
#    (and lowest) element:
#
#      ( 4, 5 ) ( 2 ) ( 1, 6, 3 )
#
#    and then to drop the parentheses:
#
#      4 5 2 1 6 3
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
#    Addison Wesley, 1968, pages 176.
#
#  Parameters:
#
#    Input, integer N, the number of objects permuted.
#
#    Input, integer P1(N), the permutation, in cycle form.
#
#    Output, integer P2(N), the permutation, in canonical form.
#
  import numpy as np
  from i4vec_sort_heap_index_d import i4vec_sort_heap_index_d

  hi = np.zeros ( n, dtype = np.int32 )
  lo = np.zeros ( n, dtype = np.int32 )
  pmin = np.zeros ( n, dtype = np.int32 )
  ptemp = np.zeros ( n, dtype = np.int32 )

  p2 = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    p2[i] = p1[i]
#
#  Work on the next cycle.
#
  nlo = 1
  ncycle = 0

  while ( nlo <= n ):
#
#  Identify NHI, the last index in this cycle.
#
    ncycle = ncycle + 1

    nhi = nlo

    while ( nhi < n ):
      if ( p2[nhi] < 0 ):
        break
      nhi = nhi + 1
#
#  Identify the smallest value in this cycle.
#
    p2[nlo-1] = - p2[nlo-1]
    pmin[ncycle-1] = p2[nlo-1]
    nmin = nlo

    for i in range ( nlo + 1, nhi + 1 ):
      if ( p2[i-1] < pmin[ncycle-1] ):
        pmin[ncycle-1] = p2[i-1]
        nmin = i
#
#  Rotate the cycle so A_MIN occurs first.
#
    for i in range ( nlo, nmin ):
      ptemp[i+nhi-nmin] = p2[i-1]
    for i in range ( nmin, nhi + 1 ):
      ptemp[i-nmin+nlo-1] = p2[i-1]

    lo[ncycle-1] = nlo
    hi[ncycle-1] = nhi
#
#  Prepare to operate on the next cycle.
#
    nlo = nhi + 1
#
#  Compute a sorting index for the cycle minima.
#  This is a 0-based index.
#
  indx = i4vec_sort_heap_index_d ( ncycle, pmin )
#
#  Copy the cycles out of the temporary array in sorted order.
#
  j = 0
  for i in range ( 0, ncycle ):
    next = indx[i]
    nlo = lo[next]
    nhi = hi[next]
    for k in range ( nlo, nhi + 1 ):
      j = j + 1
      p2[j-1] = ptemp[k-1]

  return p2

def perm1_cycle_to_canon_test ( ):

#*****************************************************************************80
#
## PERM1_CYCLE_TO_CANON_TEST tests PERM1_CYCLE_TO_CANON.
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
  p1 = np.array ( [ -6, 3, 1, -5, 4, -2 ] )

  print ( '' )
  print ( 'PERM1_CYCLE_TO_CANON_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM1_CYCLE_TO_CANON converts a permutation of (1,...,N) from' )
  print ( '  cycle to canonical form.' )
 
  perm1_print ( n, p1, '  The permutation in cycle form:' )
 
  p2 = perm1_cycle_to_canon ( n, p1 )

  perm1_print ( n, p2, '  The permutation in canonical form:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM1_CYCLE_TO_CANON_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm1_cycle_to_canon_test ( )
  timestamp ( )

