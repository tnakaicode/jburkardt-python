#! /usr/bin/env python
#
def subset_complement ( n, a ):

#*****************************************************************************80
#
## SUBSET_COMPLEMENT computes the complement of a set.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2015
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
#    Input, integer N, the order of the master set, of which A is
#    a subset.  N must be positive.
#
#    Input, integer A(N), a subset of the master set.
#    A(I) = 0 if the I-th element is in the subset A, and is
#    1 otherwise.
#
#    Output, integer B(N), the complement of A.
#
  import numpy as np
  from subset_check import subset_check
#
#  Check.
#
  check = subset_check ( n, a )

  if ( not check ):
    print ( '' )
    print ( 'SUBSET_COMPLEMENT - Fatal error!' )
    print ( '  The subset is not legal.' )
    exit ( 'SUBSET_COMPLEMENT - Fatal error!\n' )

  b = np.zeros ( n )

  b = 1 - a

  return b

def subset_complement_test ( ):

#*****************************************************************************80
#
## SUBSET_COMPLEMENT_TEST tests SUBSET_COMPLEMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_transpose_print import i4vec_transpose_print
  from subset_random import subset_random

  print ( '' )
  print ( 'SUBSET_COMPLEMENT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_COMPLEMENT returns the complement of a subset.' )

  n = 5
  seed = 123456789

  s1, seed = subset_random ( n, seed )
  i4vec_transpose_print ( n, s1, '  Subset S1:' )

  s2 = subset_complement ( n, s1 )
  i4vec_transpose_print ( n, s2, '  S2 = complement of S1:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_COMPLEMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_complement_test ( )
  timestamp ( )
 
