#! /usr/bin/env python3
#
def subset_by_size_next ( n, a, subsize, more, more2, m, m2 ):

#*****************************************************************************80
#
## SUBSET_BY_SIZE_NEXT returns all subsets of an N set, in order of size.
#
#  Example:
#
#    N = 4:
#
#    1 2 3 4
#    1 2 3
#    1 2 4
#    1 3 4
#    1 3
#    1 4
#    2 3
#    1
#    2
#    3
#    (the empty set)
#
#  Discussion:
#
#    The subsets are returned in decreasing order of size, with the
#    empty set last.
#
#    For a given size K, the K subsets are returned in lexicographic order.
#
#    On the first call, it is only important that MORE be set FALSE.  The
#    input values of A and SUBSIZE are not important.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the size of the set.
#
#    Input, integer A(N), the previous output subset.
#
#    Input, integer SUBSIZE, the size of the previous output subset.
#
#    Input, logical MORE, is FALSE on the first call, which signals
#    the routine to initialize itself.  Thereafter, MORE should be TRUE.
#
#    Input, logical MORE2, a variable for bookkeeping.
#    The user should declare this variable, but need not initialize it.
#    The output value from one call must be the input value for the next.
#
#    Input, integer M, M2, variables for bookkeeping.
#    The user should declare this variable, but need not initialize it.
#    The output value from one call must be the input value for the next.
#
#    Output, integer A(N), the next subset.
#
#    Output, integer SUBSIZE, the size of the next subset.
#
#    Output, logical MORE, is TRUE as long as there are even more subsets
#    that can be produced by further calls.
#
#    Output, logical MORE2, a variable for bookkeeping.
#    The user should declare this variable, but need not initialize it.
#    The output value from one call must be the input value for the next.
#
#    Output, integer M, M2, variables for bookkeeping.
#    The user should declare this variable, but need not initialize it.
#    The output value from one call must be the input value for the next.
#
  from ksub_next import ksub_next

  if ( not more ):
    subsize = n
    more = True
    more2 = False
    m = 0
    m2 = 0
  else:
    if ( not more2 ):
      subsize = subsize - 1
#
#  Compute the next subset of size SIZE.
#
  if ( 0 < subsize ):
    a, more2, m, m2 = ksub_next ( n, subsize, a, more2, m, m2 )
  else:
    more = False

  return a, subsize, more, more2, m, m2

def subset_by_size_next_test ( ):

#*****************************************************************************80
#
#3 SUBSET_BY_SIZE_NEXT_TEST tests SUBSET_BY_SIZE_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'SUBSET_BY_SIZE_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_BY_SIZE_NEXT generates all subsets of an N set.' )
  print ( '' )

  n = 5
  a = np.zeros ( n )
  subsize = 0
  more = False
  more2 = False
  m = 0
  m2 = 0

  rank = 0

  while ( True ):

    a, subsize, more, more2, m, m2 = subset_by_size_next ( n, a, \
      subsize, more, more2, m, m2 )

    rank = rank + 1
    print ( '  %2d' % ( rank ) ),

    if ( 0 < subsize ):
      for i in range ( 0, subsize ):
        print ( '  %2d' % ( a[i] ) ),
      print ( '' )
    else:
      print ( '  The empty set' )

    if ( not more ):
      break
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_BY_SIZE_NEXT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_by_size_next_test ( )
  timestamp ( )
