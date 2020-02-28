#! /usr/bin/env python
#
def ksub_next2 ( n, k, a ):

#*****************************************************************************80
#
## KSUB_NEXT2 generates the subsets of size K from a set of size N, one at a time.
#
#  Discussion:
#
#    This routine uses the revolving door method.  It has no "memory".
#    As far as this routine is concerned, the subsets of size K are
#    arranged in a ring that "wraps around".  There is no last subset,
#    and so the routine can be started anywhere, and called indefinitely.
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
#    N must be positive.
#
#    Input, integer K, the size of the desired subset.  K must be
#    between 0 and N.
#
#    Input, integer A(K), a subset of size K.  A must contain K unique 
#    numbers, in order, between 1 and N.  
#
#    Output, integer A(K), the "next" subset of size K.  
#
#    Output, integer INN, the element of the output subset which
#    was not in the input set.  Each new subset differs from the
#    last one by adding one element and deleting another.
#
#    Output, integer OUT, the element of the input subset which
#    is not in the output subset.
#  
  from sys import exit

  if ( n <= 0 ):
    print ( '' )
    print ( 'KSUB_NEXT2 - Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  but 0 < N is required!' )
    exit ( 'KSUB_NEXT2 - Fatal error!' )

  if ( k < 0 ):
    print ( '' )
    print ( 'KSUB_NEXT2 - Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 <= K is required!' )
    exit ( 'KSUB_NEXT2 - Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'KSUB_NEXT2 - Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  but K <= N is required!' )
    exit ( 'KSUB_NEXT2 - Fatal error!' )

  j = 0

  while ( True ):

    if ( 0 < j or ( k % 2 ) == 0 ):

      j = j + 1

      if ( k < j ):
        a[k-1] = k
        inn = k
        out = n
        return a, inn, out

      if ( a[j-1] != j ):

        out = a[j-1]
        inn = out - 1
        a[j-1] = inn

        if ( j != 1 ):
          inn = j - 1
          a[j-2] = inn

        return a, inn, out

    j = j + 1
    m = n

    if ( j < k ):
      m = a[j] - 1

    if ( m != a[j-1] ):
      break

  inn = a[j-1] + 1
  a[j-1] = inn
  out = inn - 1

  if ( j != 1 ):
    a[j-2] = out
    out = j - 1

  return a, inn, out

def ksub_next2_test ( ):

#*****************************************************************************80
#
## KSUB_NEXT2_TEST tests KSUB_NEXT2.
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
  import platform
  from i4vec_indicator1 import i4vec_indicator1

  k = 3
  n = 5

  print ( '' )
  print ( 'KSUB_NEXT2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUB_NEXT2 generates the next K subset of an' )
  print ( '  N set by the revolving door method.' )
  print ( '' )
  print ( 'Rank         Subset      Add  Remove' )
  print ( '          -----------' )
  print ( '' )
#
#  KSUB_NEXT2 doesn't have a good way of stopping.  
#  We will save the starting subset, and stop when the
#  new subset is the same as the starting one.
#
  inn = 0
  out = 0
  rank = 0
 
  a = i4vec_indicator1 ( k )
 
  while ( True ):
 
    rank = rank + 1
    print ( '  %2d  ' % ( rank ) ),
    for i in range ( 0, k ):
      print ( '  %2d' % ( a[i] ) ),
    print ( '    %2d' % ( inn ) ),
    print ( '  %2d' % ( out ) )
 
    a, inn, out = ksub_next2 ( n, k, a )
 
    more = False

    for i in range ( 0, k ):
      if ( a[i] != i + 1 ):
        more = True
        break

    if ( not more ):
      break
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUB_NEXT2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksub_next2_test ( )
  timestamp ( )

