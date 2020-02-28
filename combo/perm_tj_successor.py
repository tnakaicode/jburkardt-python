#! /usr/bin/env python
#
def perm_tj_successor ( n, p, rank ):

#*****************************************************************************80
#
#% PERM_TJ_SUCCESSOR computes the Trotter-Johnson permutation successor.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 January 2011
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N, the number of values being permuted.
#    N must be positive.
#
#    Input/output, integer P(N), describes the permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#    Input/output, integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.  
#    In general, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is 0.
#
  import numpy as np
  from perm_check import perm_check
  from perm_parity import perm_parity
#
#  Return the first element.
#
  if ( rank == -1 ):
    for i in range ( 0, n ):
      p[i] = i + 1
    rank = 0
    return p, rank
#
#  Check.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM_TJ_SUCCESSOR - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'PERM_TJ_SUCCESSOR - Fatal error!' )

  st = 0

  q = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    q[i] = p[i]
  done = False
  m = n

  while ( 1 < m and not done ):

    d = 1
    while ( q[d-1] != m ):
      d = d + 1

    for i in range ( d, m ):
      q[i-1] = q[i]

    par = perm_parity ( m - 1, q )

    if ( par == 1 ):

      if ( d == m ):
        m = m - 1
      else:
        t           = p[st+d-1]
        p[st+d-1]   = p[st+d+1-1]
        p[st+d+1-1] = t
        done = True

    else:

      if ( d == 1 ):
        m = m - 1
        st = st + 1
      else:
        t             = p[st+d-1]
        p[st+d-1]     = p[st+d-1-1]
        p[st+d-1-1]   = t
        done = True
#
#  Last element was input.  Return first one.
#
  if ( m == 1 ):
    for i in range ( 0, n ):
      p[i] = i + 1
    rank = 0
    return p, rank

  rank = rank + 1

  return p, rank

def perm_tj_successor_test ( ):

#*****************************************************************************80
#
## PERM_TJ_SUCCESSOR_TEST tests PERM_TJ_SUCCESSOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_transpose_print import i4vec_transpose_print

  n = 4

  print ( '' )
  print ( 'PERM_TJ_SUCCESSOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_TJ_SUCCESSOR lists' )
  print ( '  permutations using the Trotter-Johnson ordering.' )

  p = np.zeros ( n, dtype = np.int32 )
  rank = -1

  while ( True ):

    rank_old = rank

    p, rank = perm_tj_successor ( n, p, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( n, p, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_TJ_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_tj_successor_test ( )
  timestamp ( )
 
