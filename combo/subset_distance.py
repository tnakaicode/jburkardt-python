#! /usr/bin/env python
#
def subset_distance ( n, t1, t2 ):

#*****************************************************************************80
#
## SUBSET_DISTANCE computes the Hamming distance between two sets.
#
#  Discussion:
#
#    The sets T1 and T2 are assumed to be subsets of a set of N elements.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N, the order of the master set, of which T1 and
#    T2 are subsets.  N must be positive.
#
#    Input, integer T1(N), T2(N), two subsets of the master set.
#    T1(I) = 0 if the I-th element is in the subset T1, and is
#    1 otherwise T2 is defined similarly.
#
#    Output, integer DIST, the Hamming distance between T1 and T2,
#    defined as the number of elements of the master set which are
#    in either T1 or T2 but not both.
#
  import numpy as np
  from subset_check import subset_check
  from sys import exit
#
#  Check.
#
  check = subset_check ( n, t1 )

  if ( not check ):
    print ( '' )
    print ( 'SUBSET_DISTANCE - Fatal error!' )
    print ( '  The subset is not legal.' )
    exit ( 'SUBSET_DISTANCE - Fatal error!\n' )

  check = subset_check ( n, t2 )

  if ( not check ):
    print ( '' )
    print ( 'SUBSET_DISTANCE - Fatal error!' )
    print ( '  The subset is not legal.' )
    exit ( 'SUBSET_DISTANCE - Fatal error!\n' )

  dist = np.sum ( abs ( t1 - t2 ) )

  return dist

def subset_distance_test ( ):

#*****************************************************************************80
#
## SUBSET_DISTANCE_TEST tests SUBSET_DISTANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_transpose_print import i4vec_transpose_print
  from subset_random import subset_random
 
  print ( '' )
  print ( 'SUBSET_DISTANCE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_DISTANCE returns the distance between two subsets.' )

  n = 10
  seed = 123456789

  s1, seed = subset_random ( n, seed )
  i4vec_transpose_print ( n, s1, '  Subset S1:' )

  s2, seed = subset_random ( n, seed )
  i4vec_transpose_print ( n, s2, '  Subset S2:' )

  d = subset_distance ( n, s1, s2 )
  print ( '' )
  print ( '  Distance between S1 and S2 is %d' % ( d ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_DISTANCE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_distance_test ( )
  timestamp ( )
 
