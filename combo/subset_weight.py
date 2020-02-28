#! /usr/bin/env python
#
def subset_weight ( n, t ):

#*****************************************************************************80
#
## SUBSET_WEIGHT computes the Hamming weight of a set.
#
#  Discussion:
#
#    The Hamming weight is simply the number of elements in the set.
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
#    Input, integer N, the order of the master set, of which T
#    is a subset.  N must be positive.
#
#    Input, integer T(N), defines the subset T.
#    T(I) is 1 if I is an element of T, and 0 otherwise.
#
#    Output, integer WEIGHT, the Hamming weight of the subset T.
#
  import numpy as np
  from subset_check import subset_check
  from sys import exit
#
#  Check.
#
  check = subset_check ( n, t )

  if ( not check ):
    print ( '' )
    print ( 'SUBSET_WEIGHT - Fatal error!' )
    print ( '  The subset is not legal.' )
    exit ( 'SUBSET_WEIGHT - Fatal error!' )

  weight = np.sum ( t )

  return weight

def subset_weight_test ( ):

#*****************************************************************************80
#
## SUBSET_WEIGHT_TEST tests SUBSET_WEIGHT.
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
  print ( 'SUBSET_WEIGHT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_WEIGHT returns the weight of a subset.' )

  n = 10
  seed = 123456789

  s1, seed = subset_random ( n, seed )
  i4vec_transpose_print ( n, s1, '  Subset S1:' )

  w = subset_weight ( n, s1 )
  print ( '' )
  print ( '  The weight of the subset is %d' % ( w ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_WEIGHT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_weight_test ( )
  timestamp ( )
 
