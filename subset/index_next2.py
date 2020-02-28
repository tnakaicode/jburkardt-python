#! /usr/bin/env python
#
def index_next2 ( n, lo, hi, a, more ):

#*****************************************************************************80
#
## INDEX_NEXT2 generates all index vectors within given lower and upper limits.
#
#  Example:
#
#    N = 3,
#    LO(1) = 1, LO(2) = 10, LO(3) = 4
#    HI(1) = 2, HI(2) = 11, HI(3) = 6
#
#    1   2   3
#    ---------
#    1  10   4
#    2  10   4
#    1  11   4
#    2  11   4
#    1  10   5
#    2  10   5
#    1  11   5
#    2  11   5
#    1  10   6
#    2  10   6
#    1  11   6
#    2  11   6
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
#    Input, integer N, the number of entries in A.  The rank of
#    the object being indexed.
#
#    Input, integer LO(N), HI(N), the lower and upper limits for the array
#    indices.  LO(I) should be less than or equal to HI(I), for each I.
#
#    Input, integer A(N), the output value of A from the previous call.
#    This value is not needed on startup calls with MORE = FALSE.
#
#    Input, logical MORE, the output value of MORE from the previous call,
#    or set to FALSE if this is a startup call.
#
#    Output, integer A(N), the successor set of indices to the input
#    value.
#
#    Output, logical MORE, will normally be returned TRUE but
#    once all the vectors have been generated, it will be
#    reset FALSE and you should stop calling the program.
#
  from sys import exit

  if ( not more ):

    for i in range ( 0, n ):
      a[i] = lo[i]

    for i in range ( 0, n ):
      if ( hi[i] < lo[i] ):
        print ( '' )
        print ( 'INDEX_NEXT2 - Fatal error!' )
        print ( '  Entry %d of HI is %d' % ( i, hi[i] ) )
        print ( '  Entry %d of LO is %d' % ( i, lo[i] ) )
        print ( '  but LO(I) <= HI(I) is required.' )
        exit ( 'INDEX_NEXT2 - Fatal error!' )

  else:

    inc = 0

    while ( hi[inc] <= a[inc] ):
      a[inc] = lo[inc]
      inc = inc + 1

    a[inc] = a[inc] + 1
#
#  See if there are more entries to compute.
#
  more = False

  for i in range ( 0, n ):
    if ( a[i] < hi[i] ):
      more = True
      break

  return a, more

def index_next2_test ( ):

#*****************************************************************************80
#
## INDEX_NEXT2_TEST tests INDEX_NEXT2.
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

  n = 3
  lo = np.array ( [ 10, -5, 0 ] )
  hi = np.array ( [ 11, -3, 1 ] )

  print ( '' )
  print ( 'INDEX_NEXT2_TEST' )
  print ( '  INDEX_NEXT2 generates all indices of an' )
  print ( '  array of given shape with given' )
  print ( '  lower and upper limits.' )
  print ( '' )
  print ( '  Number of index entries = %d' % ( n ) )
  print ( '' )
  print ( '  Coordinate, Maximum Index' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %8d  %8d  %8d' % ( i, lo[i], hi[i] ) )
 
  print ( '' )
  print ( '  Index arrays:' )
  print ( '' )

  a = np.zeros ( n )
  more = False

  while ( True ):

    a, more = index_next2 ( n, lo, hi, a, more )

    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ) ),
    print ( '' )

    if ( not more ):
      break
#
#  Terminate.
#
  print ( '' )
  print ( 'INDEX_NEXT2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  index_next2_test ( )
  timestamp ( )

