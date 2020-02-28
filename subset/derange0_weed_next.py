#! /usr/bin/env python
#
def derange0_weed_next ( n, a, more, maxder, numder ):

#*****************************************************************************80
#
## DERANGE0_WEED_NEXT computes derangements of (0,...,N-1), one at a time.
#
#  Discussion:
#
#    A derangement of N objects is a permutation which leaves no object
#    unchanged.
#
#    A derangement of N objects is a permutation with no fixed
#    points.  If we symbolize the permutation operation by "P",
#    then for a derangment, P(I) is never equal to I.
#
#    The number of derangements of N objects is sometimes called
#    the subfactorial function, or the derangement number D(N).
#
#    This routine simply generates all permutations, one at a time,
#    and weeds out those that are not derangements.
#
#  Example:
#
#    Here are the derangements when N = 4:
#
#    1032
#    1230
#    1302
#    2031
#    2301
#    2310
#    3012
#    3201
#    3210
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of objects being permuted.
#
#    Input, integer A(N).  On an initialization call, A is ignored.
#    Otherwise, A should be the output value of A from the previous call.
#
#    Input, logical MORE, is FALSE on an initialization call, and TRUE otherwise.
#
#    Input, integer MAXDER, NUMDER, two parameters
#    used by the program for bookkeeping.  The user should declare these
#    variables, and pass the output values from one call to the next,
#    but should not alter them.
#
#    Output, integer A(N), if MORE is TRUE, the next derangement.
#    If MORE is FALSE, then A contains no useful information.
#
#    Output, logical MORE is TRUE if the next derangement was output in
#    A, and FALSE if there are no more derangements.
#
#    Output, integer MAXDER, NUMDER, two parameters
#    used by the program for bookkeeping.  The user should declare these
#    variables, and pass the output values from one call to the next,
#    but should not alter them.
#
  from derange_enum import derange_enum
  from derange0_check import derange0_check
  from perm0_lex_next import perm0_lex_next
#
#  Initialization on call with MORE = FALSE.
#
  if ( not more ):
    maxder = derange_enum ( n )
    numder = 0
#
#  Watch out for cases where there are no derangements.
#
  if ( maxder == 0 ):
    more = False
    return a, more, maxder, numder
#
#  Get the next permutation.
#
  while ( True ):

    a, more = perm0_lex_next ( n, a, more )
#
#  See if it is a derangment.
#
    deranged = derange0_check ( n, a )

    if ( deranged ):
      break

  numder = numder + 1

  if ( maxder <= numder ):
    more = False

  return a, more, maxder, numder

def derange0_weed_next_test ( ):

#*****************************************************************************80
#
## DERANGE0_WEED_NEXT_TEST tests DERANGE0_WEED_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  a = np.zeros ( n )
  more = 0
  maxder = 0
  numder = 0

  print ( '' )
  print ( 'DERANGE0_WEED_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DERANGE0_WEED_NEXT generates derangements' )
  print ( '  by generating ALL permutations, and "weeding out"' )
  print ( '  the ones that are not derangements.' )
  print ( '' )
  print ( '  Here, we seek all derangements of order N = %d' % ( n ) )
  print ( '' )

  rank = 0
 
  while ( True ):

    a, more, maxder, numder = derange0_weed_next ( n, a, more, maxder, numder )

    rank = rank + 1
    print ( '  %2d:' % ( rank ) ),
    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ) ),
    print ( '' )

    if ( not more ):
      break
#
#  Terminate.
#
  print ( '' )
  print ( 'DERANGE0_WEED_NEXT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  derange0_weed_next_test ( )
  timestamp ( )

