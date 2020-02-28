#! /usr/bin/env python
#
def index_unrank2 ( n, lo, hi, rank ):

#*****************************************************************************80
#
## INDEX_UNRANK2 unranks an index vector within given lower and upper limits.
#
#  Example:
#
#    N = 3,
#    LO(1) = 1, LO(2) = 10, LO(3) = 4
#    HI(1) = 2, HI(2) = 11, HI(3) = 6
#    RANK = 7
#
#    A = ( 1, 11, 5 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in A.
#
#    Input, integer LO(N), HI(N), the lower and upper limits for the array
#    indices.  It should be the case that LO(I) <= HI(I) for each I.
#
#    Input, integer RANK, the rank of the desired index.
#
#    Output, integer A(N), the index vector of the given rank.
#
  import numpy as np

  a = np.zeros ( n )
#
#  The rank might be too small.
#
  if ( rank < 1 ):
    return a

  rang = 1
  for i in range ( 0, n ):
    rang = rang * ( hi[i] + 1 - lo[i] )
#
#  The rank might be too large.
#
  if ( rang < rank ):
    return a

  k = rank - 1

  for i in range ( n - 1, -1, -1 ):
    rang = ( rang // ( hi[i] + 1 - lo[i] ) )
    j = ( k // rang )
    a[i] = j + lo[i]
    k = k - j * rang

  return a

def index_unrank2_test ( ):

#*****************************************************************************80
#
## INDEX_UNRANK2_TEST tests INDEX_UNRANK2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2003
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 3
  hi = np.array ( [ 2, 11, 6 ] )
  lo = np.array ( [ 1, 10, 4 ] )

  print ( '' )
  print ( 'INDEX_UNRANK2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  INDEX_UNRANK2 unranks a multi-index.' )
  print ( '' )
  print ( '  The multi-index has dimension %d' % ( n ) )
  print ( '' )
  print ( '  The lower and upper limits are:' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %8d  %8d  %8d' % ( i, lo[i], hi[i] ) )
  print ( '' )
  print ( '  Rank, Multi-Index:' )
  print ( '' )
 
  rank = 7

  a = index_unrank2 ( n, lo, hi, rank )
  print ( '  %2d' % ( rank ) ),
  for i in range ( 0, n ):
    print ( '  %2d' % ( a[i] ) ),
  print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'INDEX_UNRANK2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  index_unrank2_test ( )
  timestamp ( )

