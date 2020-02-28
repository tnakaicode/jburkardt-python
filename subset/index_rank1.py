#! /usr/bin/env python
#
def index_rank1 ( n, hi, a ):

#*****************************************************************************80
#
## INDEX_RANK1 ranks an index vector within given upper limits.
#
#  Example:
#
#    N = 3,
#    HI(1) = 4, HI(2) = 2, HI(3) = 3
#    A = ( 4, 1, 2 )
#
#    RANK = 12
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
#  Parameters:
#
#    Input, integer N, the number of entries in A.
#
#    Input, integer HI(N), the upper limits for the array indices.
#    The lower limit is implicitly 1, and each HI(I) should be at least 1.
#
#    Input, integer A(N), the index to be ranked.
#
#    Output, integer RANK, the rank of the index vector, or -1 if A
#    is not a legal index.
#
  rank = -1
  for i in range ( 0, n ):
    if ( a[i] < 1 or hi[i] < a[i] ):
      return rank

  rank = 0
  for i in range ( n - 1, -1, -1 ):
    rank = hi[i] * rank + a[i]

  rank = 1
  rang = 1
  for i in range ( 0, n ):
    rank = rank + ( a[i] - 1 ) * rang
    rang = rang * hi[i]

  return rank

def index_rank1_test ( ):

#*****************************************************************************80
#
## INDEX_RANK1_TEST tests INDEX_RANK1.
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
  from i4vec_print import i4vec_print

  n = 3
  a = np.array ( [ 4, 1, 2 ] )
  hi = np.array ( [ 4, 2, 3 ] )

  print ( '' )
  print ( 'INDEX_RANK1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  INDEX_RANK1 ranks an index with' )
  print ( '  lower limit 1 and given upper limits.' )
  print ( '' )
  print ( '  Number of index entries = %d' % ( n ) )
  print ( '' )
  print ( '  Coordinate, Maximum Index' )
  print ( '' )

  for i in range ( 0, n ):
    print ( '  %8d  %8d' % ( i, hi[i] ) )
 
  i4vec_print ( n, a, '  The index array:' )

  rank = index_rank1 ( n, hi, a )

  print ( '' )
  print ( '  The rank of this object is %d' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'INDEX_RANK1_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  index_rank1_test ( )
  timestamp ( )

