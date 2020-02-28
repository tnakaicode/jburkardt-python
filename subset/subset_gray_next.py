#! /usr/bin/env python3
#
def subset_gray_next ( n, a, more, ncard ):

#*****************************************************************************80
#
## SUBSET_GRAY_NEXT generates all subsets of a set of order N, one at a time.
#
#  Discussion:
#
#    This routine generates the subsets one at a time, by adding or subtracting
#    exactly one element on each step.
#
#    This uses a Gray code ordering of the subsets.
#
#    The user should set MORE = FALSE and the value of N before
#    the first call.  On return, the user may examine A which contains
#    the definition of the new subset, and must check MORE, because
#    as soon as it is FALSE on return, all the subsets have been
#    generated and the user probably should cease calling.
#
#    The first set returned is the empty set.
#
#  Example:
#
#    N = 4
#
#    0 0 0 0
#    1 0 0 0
#    1 1 0 0
#    0 1 0 0
#    0 1 1 0
#    1 1 1 0
#    1 0 1 0
#    0 0 1 0
#    0 0 1 1
#    1 0 1 1
#    1 1 1 1
#    0 1 1 1
#    0 1 0 1
#    1 1 0 1
#    1 0 0 1
#    0 0 0 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
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
#    Input, integer N, the order of the total set from which
#    subsets will be drawn.
#
#    Input, integer A(N), the value of A on the previous call.
#    This value is not needed on the first call, with MORE = FALSE.
#
#    Input, logical MORE, should be set to FALSE on the first call, and
#    then set to TRUE for all subsequent calls.
#
#    Input, integer NCARD, the cardinality of A.  This value is not needed
#    on the first call, with MORE = FALSE.
#
#    Output, integer A(N), the Gray code for the next subset.  A(I) = 0
#    if element I is in the subset, 1 otherwise.
#
#    Output, logical MORE. will be returned TRUE until all the subsets
#    have been generated.
#
#    Output, integer NCARD, the cardinality of A.
#
#    Output, integer IADD, the element which was added or removed to the
#    previous subset to generate the current one.  Exception:
#    the empty set is returned on the first call, and IADD is set to -1.
#

#
#  The first set returned is the empty set.
#
  if ( not more ):

    for i in range ( 0, n ):
      a[i] = 0
    more = True
    ncard = 0
    iadd = -1

  else:

    iadd = 0

    if ( ( ncard % 2 ) != 0 ):

      while ( True ):

        iadd = iadd + 1
        if ( a[iadd-1] != 0 ):
          break

    a[iadd] = 1 - a[iadd]
    ncard = ncard + 2 * a[iadd] - 1
#
#  The last set returned is the singleton A(N).
#
    if ( ncard == a[n-1] ):
      more = False

  return a, more, ncard, iadd

def subset_gray_next_test ( ):

#*****************************************************************************80
#
## SUBSET_GRAY_NEXT_TEST tests SUBSET_GRAY_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'SUBSET_GRAY_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_GRAY_NEXT generates all subsets of an N set.' )
  print ( '  using the Gray code ordering:' )
  print ( '  0 0 1 0 1 means the subset contains 3 and 5.' )
  print ( '' )
  print ( '  Gray code' )
  print ( '' )
 
  rank = 0
  n = 5
  a = np.zeros ( n )
  more = False
  ncard = -1
  
  while ( True ):
 
    a, more, ncard, iadd = subset_gray_next ( n, a, more, ncard )

    rank = rank + 1

    print ( '  %2d' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %4d' % ( a[i] ), end = '' )
    print ( '' )

    if ( not more ):
      break
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_GRAY_NEXT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_gray_next_test ( )
  timestamp ( )

