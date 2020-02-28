#! /usr/bin/env python
#
def subset_xor ( n, a, b ):

#*****************************************************************************80
#
## SUBSET_XOR computes the symmetric difference of two sets.
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
#    Input, integer N, the order of the master set, of which A and
#    B are subsets.  N must be positive.
#
#    Input, integer A(N), B(N), two subsets of the master set.
#    A(I) = 0 if the I-th element is in the subset A, and is
#    1 otherwise B is defined similarly.
#
#    Output, integer C(N), the symmetric difference of A and B.
#
  import numpy as np
  from subset_check import subset_check
  from sys import exit
#
#  Check.
#
  check = subset_check ( n, a )

  if ( not check ):
    print ( '' )
    print ( 'SUBSET_XOR - Fatal error!' )
    print ( '  The subset is not legal.' )
    exit ( 'SUBSET_XOR - Fatal error!' )

  check = subset_check ( n, b )

  if ( not check ):
    print ( '' )
    print ( 'SUBSET_XOR - Fatal error!' )
    print ( '  The subset is not legal.' )
    exit ( 'SUBSET_XOR - Fatal error!' )

  c = np.zeros ( n )
  for i in range ( 0, n ):
    c[i] = max ( a[i], b[i] ) - min ( a[i], b[i] )

  return c

def subset_xor_test ( ):

#*****************************************************************************80
#
## SUBSET_XOR_TEST tests SUBSET_XOR.
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
  print ( 'SUBSET_XOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUBSET_XOR returns the exclusive OR of two subsets.' )

  n = 10
  seed = 123456789

  s1, seed = subset_random ( n, seed )
  i4vec_transpose_print ( n, s1, '  Subset S1:' )

  s2, seed = subset_random ( n, seed )
  i4vec_transpose_print ( n, s2, '  Subset S2:' )

  s3 = subset_xor ( n, s1, s2 )
  i4vec_transpose_print ( n, s3, '  S3 = S1 xor S2:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUBSET_XOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  subset_xor_test ( )
  timestamp ( )
 
