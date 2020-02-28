#! /usr/bin/env python
#
def index_next0 ( n, hi, a, more ):

#*****************************************************************************80
#
## INDEX_NEXT0 generates all index vectors within given upper limits.
#
#  Discussion:
#
#    The index vectors are generated in such a way that the reversed
#    sequences are produced in lexicographic order.
#
#  Example:
#
#    N = 3,
#    HI = 3
#
#    1   2   3
#    ---------
#    1   1   1
#    2   1   1
#    3   1   1
#    1   2   1
#    2   2   1
#    3   2   1
#    1   3   1
#    2   3   1
#    3   3   1
#    1   1   2
#    2   1   2
#    3   1   2
#    1   2   2
#    2   2   2
#    3   2   2
#    1   3   2
#    2   3   2
#    3   3   2
#    1   1   3
#    2   1   3
#    3   1   3
#    1   2   3
#    2   2   3
#    3   2   3
#    1   3   3
#    2   3   3
#    3   3   3
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
#    Input, integer HI, the upper limit for the array indices.
#    The lower limit is implicitly 1 and HI must be at least 1.
#
#    Input, integer A(N), contains the output value of A from
#    the previous call.  On a startup call, with MORE = FALSE,
#    the input value of A doesn't matter.
#
#    Input, logical MORE.  Set this variable FALSE before
#    the first call.  Normally, MORE will be returned TRUE but
#    once all the vectors have been generated, MORE will be
#    reset to FALSE and you should stop calling the program.
#
#    Output, integer A(N), the next index set.
#
#    Output, logical MORE, is normally TRUE on output, but
#    once all the vectors have been generated, MORE will be
#    reset to FALSE and you should stop calling the program.
#
  from sys import exit

  if ( not more ):

    if ( hi < 1 ):
      print ( '' )
      print ( 'INDEX_NEXT0 - Fatal error!' )
      print ( '  HI is %d' % ( hi ) )
      print ( '  but HI must be at least 1.' )
      exit ( 'INDEX_NEXT0 - Fatal error!' )
 
    for i in range ( 0, n ):
      a[i] = 1

  else:

    inc = 0

    while ( hi <= a[inc] ):
      a[inc] = 1
      inc = inc + 1

    a[inc] = a[inc] + 1
#
#  See if there are more entries to compute.
#
  more = False

  for i in range ( 0, n ):
    if ( a[i] < hi ):
      more = True
      break

  return a, more

def index_next0_test ( ):

#*****************************************************************************80
#
## INDEX_NEXT0_TEST tests INDEX_NEXT0.
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
  hi = 3

  print ( '' )
  print ( 'INDEX_NEXT0_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  INDEX_NEXT0 generates all indices of an' )
  print ( '  array of given shape, with' )
  print ( '  lower limit 1 and given upper limit.' )
  print ( '' )
  print ( '  Number of index entries = %d' % ( n ) )
  print ( '  Coordinate maximum HI =   %d' % ( hi ) )
 
  print ( '' )
  print ( '  Index arrays:' )
  print ( '' )

  a = np.zeros ( n )
  more = False

  while ( True ):

    a, more = index_next0 ( n, hi, a, more )

    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ) ),
    print ( '' )

    if ( not more ):
      break
#
#  Terminate.
#
  print ( '' )
  print ( 'INDEX_NEXT0_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  index_next0_test ( )
  timestamp ( )

