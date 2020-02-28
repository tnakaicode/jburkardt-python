#! /usr/bin/env python
#
def perm0_rank ( n, p ):

#*****************************************************************************80
#
## PERM0_RANK ranks a permutation of (0,...,N-1).
#
#  Discussion:
#
#    This is the same as asking for the step at which PERM0_NEXT2
#    would compute the permutation.  The value of the rank will be
#    between 1 and N!.
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
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, New York, 1986.
#
#  Parameters:
#
#    Input, integer N, the number of elements in the set that
#    is permuted by P.
#
#    Input, integer P(N), a permutation, in standard index form.
#
#    Output, integer RANK, the rank of the permutation.  This
#    gives the order of the given permutation in the set of all
#    the permutations on N elements.
#
  from perm0_check import perm0_check
  from perm0_inverse2 import perm0_inverse2
  from sys import exit
#
#  Make sure the permutation is a legal one.
#  (This is not an efficient way to do so!)
#
  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM0_RANK - Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    exit ( 'PERM0_RANK - Fatal error!' )
#
#  Compute the inverse permutation.
#
  inverse = perm0_inverse2 ( n, p )

  rank = 0

  for i in range ( 0, n ):

    count = 0

    for j in range ( 0, inverse[i] + 1 ):
      if ( p[j] < i ):
        count = count + 1

    if ( ( rank % 2 ) == 1 ):
      rem = count
    else:
      rem = i - count

    rank = ( i + 1 ) * rank + rem

  rank = rank + 1

  return rank

def perm0_rank_test ( ):

#*****************************************************************************80
#
## PERM0_RANK_TEST tests PERM0_RANK.
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

  n = 4
  p = np.array ( [ 0, 3, 1, 2 ] )

  print ( '' )
  print ( 'PERM0_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_RANK ranks a permutation.' )

  perm0_print ( n, p, '  The permutation:' )
 
  rank = perm0_rank ( n, p )
 
  print ( '' )
  print ( '  The rank is: %d' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_RANK_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_rank_test ( )
  timestamp ( )
