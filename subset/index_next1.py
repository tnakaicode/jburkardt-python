#! /usr/bin/env python
#
def index_next1 ( n, hi, a, more ):

#*****************************************************************************80
#
## INDEX_NEXT1 generates all index vectors within given upper limits.
#
#  Discussion:
#
#    The index vectors are generated in such a way that the reversed
#    sequences are produced in lexicographic order.
#
#  Example:
#
#    N = 3,
#    HI(1) = 4, HI(2) = 2, HI(3) = 3
#
#    1   2   3
#    ---------
#    1   1   1
#    2   1   1
#    3   1   1
#    4   1   1
#    1   2   1
#    2   2   1
#    3   2   1
#    4   2   1
#    1   1   2
#    2   1   2
#    3   1   2
#    4   1   2
#    1   2   2
#    2   2   2
#    3   2   2
#    4   2   2
#    1   1   3
#    2   1   3
#    3   1   3
#    4   1   3
#    1   2   3
#    2   2   3
#    3   2   3
#    4   2   3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in A.
#
#    Input, integer HI(N), the upper limits for the array indices.
#    The lower limit is implicitly 1, and each HI(I) should be at least 1.
#
#    Input, integer A(N), the output value of A on the previous call.
#    On startup calls with MORE = FALSE, the input value of A doesn't matter.
#
#    Input, logical MORE, is set to the output value of MORE on the
#    previous call, or to FALSE on a startup call.
#
#    Output, integer A(N), the next index vector.
#
#    Output, logical MORE, is normally TRUE, but will be FALSE once there
#    are no more index vectors to generate.
#
  from sys import exit

  if ( not more ):

    for i in range ( 0, n ):
      a[i] = 1

    for i in range ( 0, n ):
      if ( hi[i] < 1 ):
        print ( '' )
        print ( 'INDEX_NEXT1 - Fatal error!' )
        print ( '  Entry %d of HI is %d' % ( i, hi[i] ) )
        exit ( '  but all entries must be at least 1.' )

  else:

    inc = 0

    while ( hi[inc] <= a[inc] ):
      a[inc] = 1
      inc = inc + 1

    a[inc] = a[inc] + 1
#
#  See if there are more entries to compute.
#
  more = False

  for i in range ( 0, n ):
    if ( a[i] < hi[i] ):
      more = True

  return a, more

def index_next1_test ( ):

#*****************************************************************************80
#
## INDEX_NEXT1_TEST tests INDEX_NEXT1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_print import i4vec_print

  n = 3
  hi = np.array ( [ 4, 2, 3 ] )

  print ( '' )
  print ( 'INDEX_NEXT1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  INDEX_NEXT1 generates all indices of an' )
  print ( '  array of given shape, with' )
  print ( '  lower limit 1 and given upper limits.' )
  print ( '' )
  print ( '  Number of index entries = %d\n' % ( n ) )

  i4vec_print ( n, hi, '  Coordinate maximum indices:' )
 
  print ( '' )
  print ( '  Index arrays:' )
  print ( '' )

  a = np.zeros ( n )
  more = False

  while ( True ):

    a, more = index_next1 ( n, hi, a, more )

    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ) ),
    print ( '' )

    if ( not more ):
      break
#
#  Terminate.
#
  print ( '' )
  print ( 'INDEX_NEXT1_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  index_next1_test ( )
  timestamp ( )

