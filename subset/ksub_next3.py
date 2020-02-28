#! /usr/bin/env python
#
def ksub_next3 ( n, k, a, more ):

#*****************************************************************************80
#
## KSUB_NEXT3 generates the subsets of size K from a set of size N, one at a time.
#
#  Discussion:
#
#    The routine uses the revolving door method.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 June 2015
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
#    Input, integer K, the size of the desired subsets.  K must be
#    between 0 and N.
#
#    Input, integer A(K).  A(I) is the I-th element of the
#    output subset.  The elements of A are sorted.
#
#    Input, logical MORE.  On first call, set MORE = FALSE
#    to signal the beginning.  MORE will be set to TRUE, and on
#    each call, the routine will return another K-subset.
#    Finally, when the last subset has been returned,
#    MORE will be set FALSE and you may stop calling.
#
#    Output, integer A(K).  A(I) is the I-th element of the
#    output subset.  The elements of A are sorted.
#
#    Output, logical MORE.  On first call, set MORE = FALSE
#    to signal the beginning.  MORE will be set to TRUE, and on
#    each call, the routine will return another K-subset.
#    Finally, when the last subset has been returned,
#    MORE will be set FALSE and you may stop calling.
#
#    Output, integer INN, the element of the output subset which
#    was not in the input set.  Each new subset differs from the
#    last one by adding one element and deleting another.  IN is not
#    defined the first time that the routine returns, and is
#    set to -1.
#
#    Output, integer IOUT, the element of the input subset which is
#    not in the output subset.  IOUT is not defined the first time
#    the routine returns, and is set to -1.
#
  from sys import exit
  from i4vec_indicator1 import i4vec_indicator1

  if ( n <= 0 ):
    print ( '' )
    print ( 'KSUB_NEXT3 - Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  but 0 < N is required!' )
    exit ( 'KSUB_NEXT3 - Fatal error!' )

  if ( k < 0 ):
    print ( '' )
    print ( 'KSUB_NEXT3 - Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 <= K is required!' )
    exit ( 'KSUB_NEXT3 - Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'KSUB_NEXT3 - Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  but K <= N is required!' )
    exit ( 'KSUB_NEXT3 - Fatal error!' )

  if ( not more ):
    inn = -1
    iout = -1
    a = i4vec_indicator1 ( k )
    more = ( k != n )
    return a, more, inn, iout

  j = 0

  while ( True ):

    if ( 0 < j or ( k % 2 ) == 0 ):

      j = j + 1

      if ( a[j-1] != j ):

        iout = a[j-1]
        inn = iout - 1
        a[j-1] = inn

        if ( j != 1 ):
          inn = j - 1
          a[j-2] = inn

        if ( k != 1 ):
          more = ( a[k-2] == k - 1 )

        more = ( not more ) or ( a[k-1] != n )

        return a, more, inn, iout

    j = j + 1
    m = n

    if ( j < k ):
      m = a[j] - 1

    if ( m != a[j-1] ):
      break

  inn = a[j-1] + 1
  a[j-1] = inn
  iout = inn - 1

  if ( j != 1 ):
    a[j-2] = iout
    iout = j - 1

  if ( k != 1 ):
    more = ( a[k-2] == k - 1 )

  more = ( ( not more ) or ( a[k-1] != n ) )

  return a, more, inn, iout

def ksub_next3_test ( ):

#*****************************************************************************80
#
## KSUB_NEXT3_TEST tests KSUB_NEXT3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  k = 3
  n = 5

  print ( '' )
  print ( 'KSUB_NEXT3_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUB_NEXT3 generates all K subsets of an N set' )
  print ( '  using the revolving door method.' )
  print ( '' )
  print ( 'Rank    Subset  Added Removed' )
  print ( '' )

  rank = 0
  a = np.zeros ( k )
  more = False
 
  while ( True ):

    a, more, inn, out = ksub_next3 ( n, k, a, more)

    rank = rank + 1
    print ( '  %2d' % ( rank ) ),
    for i in range ( 0, k ):
      print ( '  %2d' % ( a[i] ) ),
    print ( '     %2d  %2d' % ( inn, out ) )

    if ( not more ):
      break
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUB_NEXT3_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksub_next3_test ( )
  timestamp ( )

