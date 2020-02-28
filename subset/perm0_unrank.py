#! /usr/bin/env python
#
def perm0_unrank ( n, rank ):

#*****************************************************************************80
#
## PERM0_UNRANK produces the permutation of (0,...,N-1) of given rank.
#
#  Discussion:
#
#    The value of the rank should be between 1 and N!.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 June 2004
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer Verlag, New York, 1986.
#
#  Parameters:
#
#    Input, integer N, the number of elements in the set.
#
#    Input, integer RANK, the desired rank of the permutation.  This
#    gives the order of the given permutation in the set of all
#    the permutations on N elements.
#
#    Output, integer P(N), the permutation, in standard index form.
#
  import numpy as np
  from sys import exit
 
  p = np.zeros ( n )
  for i in range ( 0, n ):
    p[i] = -1

  nfact = 1

  for i in range ( 1, n + 1 ):
    nfact = nfact * i

  if ( rank < 1 or nfact < rank ):
    print ( '' )
    print ( 'PERM0_UNRANK - Fatal error!' )
    print ( '  Illegal input value for RANK.' )
    print ( '  RANK must be between 1 and %d' % ( nfact ) )
    print ( '  but the input value is %d' % ( rank ) )
    exit ( 'PERM0_UNRANK - Fatal error!' )

  jrank = rank - 1

  for iprev in range ( n, 0, -1 ):

    irem = ( jrank % iprev )
    jrank = ( jrank // iprev )

    if ( ( jrank % 2 ) == 1 ):
      j = 0
      jdir = 1
    else:
      j = n + 1
      jdir = -1

    icount = 0

    while ( True ):

      j = j + jdir

      if ( p[j-1] == -1 ):
        icount = icount + 1

      if ( irem < icount ):
        break

    p[j-1] = iprev - 1

  return p

def perm0_unrank_test ( ):

#*****************************************************************************80
#
## PERM0_UNRANK_TEST tests PERM0_UNRANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from perm0_print import perm0_print

  n = 4

  print ( '' )
  print ( 'PERM0_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_UNRANK, given a rank, computes the' )
  print ( '  corresponding permutation.' )
  print ( '' )

  rank = 6

  print ( '  The requested rank is %d' % ( rank ) )
 
  p = perm0_unrank ( n, rank )
 
  perm0_print ( n, p, '  The permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_UNRANK_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_unrank_test ( )
  timestamp ( )
