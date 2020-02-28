#! /usr/bin/env python
#
def index_unrank0 ( n, hi, rank ):

#*****************************************************************************80
#
## INDEX_UNRANK0 unranks an index vector within given upper limits.
#
#  Example:
#
#    N = 3,
#    HI = 3
#    RANK = 12
#
#    A = ( 3, 1, 2 )
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
#    Input, integer HI, the upper limit for the array indices.
#    The lower limit is implicitly 1, and HI should be at least 1.
#
#    Input, integer RANK, the rank of the desired index vector.
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

  rang = hi ** n
#
#  The rank might be too large.
#
  if ( rang < rank ):
    return a

  k = rank - 1
  for i in range ( n - 1, -1, -1 ):
    rang = ( rang // hi )
    j = ( k // rang )
    a[i] = j + 1
    k = k - j * rang

  return a

def index_unrank0_test ( ):

#*****************************************************************************80
#
## INDEX_UNRANK0_TEST tests INDEX_UNRANK0.
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
  import platform

  n = 3
  hi = 3

  print ( '' )
  print ( 'INDEX_UNRANK0_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  INDEX_UNRANK0 unranks a multi-index.' )
  print ( '' )
  print ( '  The multi-index has dimension %d' % ( n ) )
  print ( '' )
  print ( '  The upper limit is HI = %d' % ( hi ) )
  print ( '' )
  print ( '  Rank, Multi-Index:' )
  print ( '' )
 
  maxrank = hi ** n

  for rank in range ( 1, maxrank + 1 ):
    a = index_unrank0 ( n, hi, rank )
    print ( '  %2d  ' % ( rank ) ),
    for i in range ( 0, n ):
      print ( '  %2d' % ( a[i] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'INDEX_UNRANK0_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  index_unrank0_test ( )
  timestamp ( )

