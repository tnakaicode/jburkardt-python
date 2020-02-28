#! /usr/bin/env python
#
def index_rank0 ( n, hi, a ):

#*****************************************************************************80
#
## INDEX_RANK0 ranks an index vector within given upper limits.
#
#  Example:
#
#    N = 3,
#    HI = 3
#    A = ( 3, 1, 2 )
#
#    RANK = 12
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
#    The lower limit is implicitly 1, and HI should be at least 1.
#
#    Input, integer A(N), the index vector to be ranked.
#
#    Output, integer RANK, the rank of the index vector, or -1 if A
#    is not a legal index.
#
  rank = -1

  for i in range ( 0, n ):
    if ( a[i] < 1 or hi < a[i] ):
      return rank

  rank = 0
  for i in range ( n - 1, -1, -1 ):
    rank = hi * rank + a[i]

  rank = 1
  rang = 1
  for i in range ( 0, n ):
    rank = rank + ( a[i] - 1 ) * rang
    rang = rang * hi

  return rank

def index_rank0_test ( ):

#*****************************************************************************80
#
## INDEX_RANK0_TEST tests INDEX_RANK0.
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
  a = np.array ( [ 3, 1, 2 ] )
  hi = 3

  print ( '' )
  print ( 'INDEX_RANK0_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  INDEX_RANK0 ranks an index with' )
  print ( '  lower limit 1 and given upper limit.' )
  print ( '' )
  print ( '  Number of index entries = %d' % ( n ) )
  print ( '  Coordinate maximum index = %d' % ( hi ) )

  i4vec_print ( n, a, '  The index array:' )

  rank = index_rank0 ( n, hi, a )

  print ( '' )
  print ( '  The rank of this object is %d' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'INDEX_RANK0_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  index_rank0_test ( )
  timestamp ( )

