#! /usr/bin/env python
#
def tuple_next_fast ( m, n, rank, base ):

#*****************************************************************************80
#
## TUPLE_NEXT_FAST computes the next element of a tuple space, "fast".
#
#  Discussion:
#
#    The elements are N vectors.  Each entry is constrained to lie
#    between 1 and M.  The elements are produced one at a time.
#    The first element is
#      (1,1,...,1)
#    and the last element is
#      (M,M,...,M)
#    Intermediate elements are produced in lexicographic order.
#
#    This code was written as a possibly faster version of TUPLE_NEXT.
#
#  Example:
#
#    N = 2,
#    M = 3
#
#    INPUT        OUTPUT
#    -------      -------
#    Rank          X
#    ----          ----
#   -1            -1 -1
#
#    0             1  1
#    1             1  2
#    2             1  3
#    3             2  1
#    4             2  2
#    5             2  3
#    6             3  1
#    7             3  2
#    8             3  3
#    9             1  1
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
#    Input, integer M, the maximum entry in each component.
#    M must be greater than 0.
#
#    Input, integer N, the number of components.
#    N must be greater than 0.
#
#    Input, integer RANK, indicates the rank of the tuples.
#    Typically, 0 <= RANK < N^M values greater than this are
#    legal and meaningful, being equivalent to the corresponding
#    value mod N^M.  RANK < 0 indicates that this is the first
#    call for the given values of (M,N).  Initialization is done,
#    and X is set to a dummy value.
#
#    Input/output, integer BASE(N), a bookkeeping array needed by 
#    this procedure.  The user should allocate space for this array, but
#    should not alter it between successive calls.
#
#    Output, integer X(N), the next tuple of the given rank,
#    or a dummy value if initialization is being done.
#
  import numpy as np
  from sys import exit

  x = np.zeros ( n, dtype = np.int32 )

  if ( rank < 0 ):

    if ( m <= 0 ):
      print ( '' )
      print ( 'TUPLE_NEXT_FAST - Fatal error!' )
      print ( '  M <= 0 is illegal.' )
      print ( '  M = %d' % ( m ) )
      exit ( 'TUPLE_NEXT_FAST - Fatal error!' )

    if ( n <= 0 ):
      print ( '' )
      print ( 'TUPLE_NEXT_FAST - Fatal error!' )
      print ( '  N <= 0 is illegal.' )
      print ( '  N = %d' % ( n ) )
      exit ( 'TUPLE_NEXT_FAST - Fatal error!' )

    base[n-1] = 1
    for i in range ( n - 2, -1, -1 ):
      base[i] = base[i+1] * m

    for i in range ( 0, n ):
      x[i] = -1

  else:

    for i in range ( 0, n ):
      x[i] = ( ( rank // base[i] ) % m ) + 1

  return x, base

def tuple_next_fast_test ( ):

#*****************************************************************************80
#
## TUPLE_NEXT_FAST_TEST tests TUPLE_NEXT_FAST.
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

  n = 2
  m = 3

  print ( '' )
  print ( 'TUPLE_NEXT_FAST_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TUPLE_NEXT_FAST returns the next "tuple", that is,' )
  print ( '  a vector of N integers, each between 1 and M.' )
  print ( '' )
  print ( '  M = %d' % ( m ) )
  print ( '  N = %d' % ( n ) )
  print ( '' )
#
#  Initialize.
#
  rank = -1
  base = np.zeros ( n )
  x, base = tuple_next_fast ( m, n, rank, base )

  rank_max = ( m ** n ) - 1

  for rank in range ( 0, rank_max + 1 ):

    x, base = tuple_next_fast ( m, n, rank, base )

    print ( '%4d  ' % ( rank ) ),
    for j in range ( 0, n ):
      print ( '%10d  ' % ( x[j] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TUPLE_NEXT_FAST_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tuple_next_fast_test ( )
  timestamp ( )

