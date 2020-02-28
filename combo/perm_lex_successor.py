#! /usr/bin/env python
#
def perm_lex_successor ( n, p, rank ):

#*****************************************************************************80
#
## PERM_LEX_SUCCESSOR computes the lexicographic permutation successor.
#
#  Example:
#
#    RANK  Permutation
#
#       0  1 2 3 4
#       1  1 2 4 3
#       2  1 3 2 4
#       3  1 3 4 2
#       4  1 4 2 3
#       5  1 4 3 2
#       6  2 1 3 4
#       ...
#      23  4 3 2 1
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
#    Input, integer P(N), the input permutation.
#
#    Input, integer RANK, the rank of the input permutation.
#    If RANK = -1, then the input permutation is ignored, and the
#    function returns the first permutation in the ordered list,
#    with RANK = 1.
#
#    Output, integer P(N), the successor permutation.  
#    If the input permutation was the last in the ordered list,
#    then the output permutation is the first permutation.
#
#    Output, integer RANK, the rank of the output permutation.
#
  import numpy as np
  from perm_check import perm_check
  from sys import exit
#
#  If RANK <= -1, return the first permutation.
#
  if ( rank <= -1 ):
    for i in range ( 0, n ):
      p[i] = i + 1
    rank = 0
    return p, rank
#
#  Make sure the input permutation is legal.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM_LEX_SUCCESSOR - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'PERM_LEX_SUCCESSOR - Fatal error!' )
#
#  Seek I, the highest index for which the next element is bigger.
#
  i = n - 2

  while ( True ):

    if ( i < 0 ):
      break

    if ( p[i] <= p[i+1] ):
      break

    i = i - 1
#
#  If no I could be found, then we have reach the final permutation,
#  N, N-1, ..., 2, 1.  Time to start over again.
#
  if ( i == -1 ):
    for i in range ( 0, n ):
      p[i] = i + 1
    rank = 0
  else:
#
#  Otherwise, look for the the highest index after I whose element
#  is bigger than I's.  We know that I+1 is one such value, so the
#  loop will never fail.
#
    j = n - 1
    while ( p[j] < p[i] ):
      j = j - 1
#
#  Interchange elements I and J.
#
    t    = p[i]
    p[i] = p[j]
    p[j] = t
#
#  Reverse the elements from I+1 to N.
#  There are more elegant ways to do this.
#
    q = np.zeros ( n )
    for j in range ( 0, n ):
      q[j] = p[j]

    for j in range ( i + 1, n ):
      p[j] = q[n-1 + i+1 - j]

    rank = rank + 1

  return p, rank

def perm_lex_successor_test ( ):

#*****************************************************************************80
#
## PERM_LEX_SUCCESSOR_TEST tests PERM_LEX_SUCCESSOR.
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
  print ( 'PERM_LEX_SUCCESSOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_LEX_SUCCESSOR lists' )
  print ( '  permutations using the lexicographic ordering.' )

  p = np.zeros ( n )
  rank = -1

  while ( True ):

    rank_old = rank

    p, rank = perm_lex_successor ( n, p, rank )

    if ( rank <= rank_old ):
      break

    i4vec_transpose_print ( n, p, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_LEX_SUCCESSOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_lex_successor_test ( )
  timestamp ( )
 
