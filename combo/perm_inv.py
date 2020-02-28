#! /usr/bin/env python
#
def perm_inv ( n, p ):

#*****************************************************************************80
#
## PERM_INV computes the inverse of a permutation.
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
#    Donald Kreher, Douglas Simpson,
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
#    Input, integer P(N), describes the permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#    Output, integer PINV(N), the inverse permutation.
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
    print ( 'PERM_INV - Fatal error!' )
    print ( '  The input array is illegal.' )
    exit ( 'PERM_INV - Fatal error!' )

  pinv = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    pinv[p[i]-1] = i + 1

  return pinv

def perm_inv_test ( ):

#*****************************************************************************80
#
## PERM_INV_TEST tests PERM_INV.
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
  from perm_mul import perm_mul
  from perm_print import perm_print

  n = 4

  print ( '' )
  print ( 'PERM_INV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM_INV computes an inverse permutation.' )

  p = np.array ( [ 3, 1, 2, 4 ], dtype = np.int32 )
  perm_print ( n, p, '  The permutation P:' )

  q = perm_inv ( n, p )

  perm_print ( n, q, '  The inverse permutation Q:' )

  r = perm_mul ( n, p, q )

  perm_print ( n, r, '  The product R = P * Q:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM_INV_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm_inv_test ( )
  timestamp ( )
 
