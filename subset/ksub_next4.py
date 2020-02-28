#! /usr/bin/env python
#
def ksub_next4 ( n, k, a, done ):

#*****************************************************************************80
#
## KSUB_NEXT4 generates the subsets of size K from a set of size N, one at a time.
#
#  Discussion:
#
#    The subsets are generated one at a time.
#
#    The routine should be used by setting DONE to TRUE, and then calling
#    repeatedly.  Each call returns with DONE equal to FALSE, the array
#    A contains information defining a new subset.  When DONE returns
#    equal to TRUE, there are no more subsets.
#
#    There are ( N*(N-1)*...*(N+K-1)) / ( K*(K-1)*...*2*1) such subsets.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 May 2018
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, integer N, the size of the entire set.
#
#    Input, integer K, the size of the desired subset.  K must be
#    between 0 and N.
#
#    Input, integer A(K), is not needed on the first call, with DONE = TRUE.
#    On subsequent calls, it should be the output value of A from the
#    previous call.
#
#    Input, logical DONE, should be TRUE on the first call, to force initialization,
#    and then FALSE on subsequent calls.
#
#    Output, integer A(K), as long as DONE is returned FALSE, A 
#    is the next K subset.
#
#    Output, logical DONE, is TRUE if the routine is returning the
#    next K subset, and FALSE if there are no more subsets to return.
#
  import numpy as np
  from sys import exit

  if ( k < 0 ):
    print ( '' )
    print ( 'KSUB_NEXT4 - Fatal error!' )
    print ( '  K = %d' % ( k ) )
    print ( '  but 0 <= K is required!' )
    exit ( 'KSUB_NEXT4 - Fatal error!' )

  if ( n < k ):
    print ( '' )
    print ( 'KSUB_NEXT4 - Fatal error!' )
    print ( '  N = %d' % ( n ) )
    print ( '  K = %d' % ( k ) )
    print ( '  but K <= N is required!' )
    exit ( 'KSUB_NEXT4 - Fatal error!' )
#
#  First call:
#
  if ( done ):

    a = np.zeros ( n, dtype = np.int32 )

    for i in range ( 0, n ):
      a[i] = i + 1

    done = False
#
#  Empty set returned on previous call.
#
  elif ( 0 == n or 0 == k ):

    done = True
#
#  Next call.
#
  elif ( a[0] < n - k + 1 ):

    jsave = k

    for j in range ( 1, k ):

      if ( a[j-1] + 1 < a[j] ):
        jsave = j
        break

    for j in range ( 0, jsave - 1 ):
      a[j] = j + 1
    a[jsave-1] = a[jsave-1] + 1
    done = False

  else:

    done = True

  return a, done

def ksub_next4_test ( ):

#*****************************************************************************80
#
## KSUB_NEXT4_TEST tests KSUB_NEXT4.
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
  print ( 'KSUB_NEXT4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KSUB_NEXT4 generates K subsets of an N set.' )
  print ( '  N = %d' % ( n ) )
  print ( '  K = %d' % ( k ) )
  print ( '' )
  print ( 'Rank    Subset' )
  print ( '' )

  a = np.zeros ( k )
  done = True
  rank = 0
 
  while ( True ):
 
    a, done = ksub_next4 ( n, k, a, done )
 
    if ( done ):
      break

    rank = rank + 1
    print ( '  %2d  ' % ( rank ), end = '' )
    for i in range ( 0, k ):
      print ( '  %2d' % ( a[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'KSUB_NEXT4_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ksub_next4_test ( )
  timestamp ( )

