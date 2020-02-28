#! /usr/bin/env python
#
def perm_mul ( n, p, q ):

#*****************************************************************************80
#
## PERM_MUL computes the product of two permutations.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,inson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N, the number of values being permuted.
#    N must be positive.
#
#    Input, integer P(N), Q(N), describes the permutation factors.
#
#    Output, integer R(N), the product permutation P * Q.
#    R(I) = P(Q(I)).
#
  import numpy as np
  from perm_check import perm_check
  from sys import exit
#
#  Check.
#
  check = perm_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM_MUL - Fatal error!' )
    print ( '  The input array P is illegal.' )
    exit ( 'PERM_MUL - Fatal error!' )

  check = perm_check ( n, q )

  if ( not check ):
    print ( '' )
    print ( 'PERM_MUL - Fatal error!' )
    print ( '  The input array Q is illegal.' )
    exit ( 'PERM_MUL - Fatal error!' )

  r = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    r[i] = p[q[i]-1]

  return r

def perm_mul_test ( ):

#*****************************************************************************80
#
## PERM_MUL_TEST tests PERM_MUL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from perm_print import perm_print

  n = 4

  print ( '' )
  print ( 'PERM_MUL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_MUL multiplies two permutations.' )

  p = np.array ( [ 3, 1, 2, 4 ], dtype = np.int32 )
  perm_print ( n, p, '  The permutation P:' )

  q = np.array ( [ 2, 3, 1, 4 ], dtype = np.int32 )
  perm_print ( n, q, '  The permutation Q:' )
#
#  Multiply.
#
  r = perm_mul ( n, p, q )
  perm_print ( n, r, '  The product R = P * Q:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_MUL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_mul_test ( )
  timestamp ( )
 
