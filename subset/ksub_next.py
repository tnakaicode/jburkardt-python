#! /usr/bin/env python
#
def ksub_next ( n, k, a, more, m, m2 ):

#*****************************************************************************80
#
## KSUB_NEXT generates the subsets of size K from a set of size N, one at a time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2015
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
#    Input, integer N, the size of the set from which subsets are drawn.
#
#    Input, integer K, the desired size of the subsets.  K must
#    be between 0 and N.
#
#    Input, integer A(K).  A(I) is the I-th element of the
#    subset.  Thus A(I) will be an integer between 1 and N.
#    Note that the routine will return the values in A
#    in sorted order: 1 <= A(1) < A(2) < ... < A(K) <= N
#
#    Input, logical MORE.  Set MORE = FALSE before first call
#    for a new sequence of subsets.  It then is set and remains
#    TRUE as long as the subset computed on this call is not the
#    final one.  When the final subset is computed, MORE is set to
#    FALSE as a signal that the computation is done.
#
#    Output, integer A(K).  A(I) is the I-th element of the
#    subset.  Thus A(I) will be an integer between 1 and N.
#    Note that the routine will return the values in A
#    in sorted order: 1 <= A(1) < A(2) < ... < A(K) <= N
#
#    Output, logical MORE.  Set MORE = FALSE before first call
#    for a new sequence of subsets.  It then is set and remains
#    TRUE as long as the subset computed on this call is not the
#    final one.  When the final subset is computed, MORE is set to
#    FALSE as a signal that the computation is done.
#
#    Input/output, integer M, M2, two variables used by this
#    procedure for bookkeeping.  The user must declare these variables,
#    and the output values from one call must be used as the input values
#    on the next.  The user should not change these values.
#
  from sys import exit

  if ( k < 0 ):
    print ( '' )
    print ( 'KSUB_NEXT - Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 <= K is required!' )
    exit ( 'KSUB_NEXT - Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'KSUB_NEXT - Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  but K <= N is required!' )
    exit ( 'KSUB_NEXT - Fatal error!' )

  if ( not more ):
    m2 = 0
    m = k
  else:
    if ( m2 < n - m ):
      m = 0
    m = m + 1
    m2 = a[k-m]

  for j in range ( 1, m + 1 ):
    a[k+j-m-1] = m2 + j

  more = ( a[0] != ( n - k + 1 ) )

  return a, more, m, m2

def ksub_next_test ( ):

#*****************************************************************************80
#
## KSUB_NEXT_TEST tests KSUB_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'KSUB_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUB_NEXT generates all K subsets of an N set' )
  print ( '  in lexicographic order.' )
  print ( '' )

  rank = 0

  n = 5
  k = 3
  a = np.zeros ( k )
  more = False
  m = 0
  m2 = 0
 
  while ( True ):

    a, more, m, m2 = ksub_next ( n, k, a, more, m, m2 )

    rank = rank + 1
    print ( '  %2d  ' % ( rank ) ),
    for i in range ( 0, k ):
      print ( '  %2d' % ( a[i] ) ),
    print ( '' )

    if ( not more ):
      break
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUB_NEXT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksub_next_test ( )
  timestamp ( )
