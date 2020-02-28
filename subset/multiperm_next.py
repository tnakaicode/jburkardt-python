#! /usr/bin/env python
#
def multiperm_next ( n, a ):

#*****************************************************************************80
#
## MULTIPERM_NEXT returns the next multipermutation.
#
#  Discussion:
#
#    To begin the computation, the user must set up the first multipermutation.
#    To compute ALL possible multipermutations, this first permutation should
#    list the values in ascending order.
#
#    The routine will compute, one by one, the next multipermutation,
#    in lexicographical order.  On the call after computing the last 
#    multipermutation, the routine will return MORE = FALSE (and will
#    reset the multipermutation to the FIRST one again.)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of items in the multipermutation.
#
#    Input, integer A[N], the current multipermutation.
#
#    Output, integer A[N], the next multipermutation.
#
#    Output, logical MORE, is TRUE if the next multipermutation
#    was computed, or FALSE if no further multipermutations could
#    be computed.
#

#
#  Step 1:
#  Find M, the last location in A for which A(M) < A(M+1).
#
  m = 0
  for i in range ( 1, n ):
    if ( a[i-1] < a[i] ):
      m = i
#
#  Step 2:
#  If no M was found, we've run out of multipermutations.
#
  if ( m == 0 ):
    more = False
    for i in range ( 0, n ):
      for j in range ( i + 1, n ):
        if ( a[j] < a[i] ):
          t    = a[i]
          a[i] = a[j]
          a[j] = t
    return a, more

  more = True
#
#  Step 3:
#  Ascending sort A(M+1:N).
#
  if ( m + 1 < n ):
    for i in range ( m, n ):
      for j in range ( i + 1, n ):
        if ( a[j] < a[i] ):
          t    = a[i]
          a[i] = a[j]
          a[j] = t
#
#  Step 4:
#  Locate the first larger value after A(M).
#
  i = 1
  while ( a[m+i-1] <= a[m-1] ):
    i = i + 1
#
#  Step 5:
#  Interchange A(M) and next larger value.
#
  temp = a[m-1]
  a[m-1] = a[m+i-1]
  a[m+i-1] = temp

  return a, more

def multiperm_next_test ( ):

#*****************************************************************************80
#
## MULTIPERM_NEXT_TEST tests MULTIPERM_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'MULTIPERM_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MULTIPERM_NEXT computes multipermutations in' )
  print ( '  lexical order.' )
  print ( '' )

  rank = 0
  a = np.array ( [ 1, 2, 2, 3, 3, 3 ] )
  n = 6
  more = True
  
  while ( more ):
      
    rank = rank + 1
    
    print ( '  %4d    ' % ( rank ) ),
    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ) ),
    print ( '' )

    a, more = multiperm_next ( n, a )
#
#  Terminate.
#
  print ( '' )
  print ( 'MULTIPERM_NEXT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  multiperm_next_test ( )
  timestamp ( )

