#! /usr/bin/env python
#
def perm0_inverse3 ( n, p ):

#*****************************************************************************80
#
## PERM0_INVERSE3 produces the inverse of a permutation of (0,...,N-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of items permuted.
#
#    Input, integer P(N), a permutation.
#
#    Output, integer P_INV(N), the inverse permutation.
#
  import numpy as np
  from perm0_check import perm0_check
  from sys import exit

  check = perm0_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM0_INVERSE3 - Fatal error!' )
    print ( '  The input array does not represent' )
    print ( '  a proper permutation.' )
    exit ( 'PERM0_INVERSE3 - Fatal error!' )

  p_inv = np.zeros ( n )

  for i in range ( 0, n ):
    p_inv[p[i]] = i
 
  return p_inv

def perm0_inverse3_test ( ):

#*****************************************************************************80
#
## PERM0_INVERSE3_TEST tests PERM0_INVERSE3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from perm0_print import perm0_print

  n = 7
  p = np.array ( [ 3, 2, 4, 0, 6, 5, 1 ] )

  print ( '' )
  print ( 'PERM0_INVERSE3_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_INVERSE3 inverts a permutation.' )

  perm0_print ( n, p, '  The original permutation:' )
 
  p_inv = perm0_inverse3 ( n, p )
 
  perm0_print ( n, p_inv, '  The inverted permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_INVERSE3_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_inverse3_test ( )
  timestamp ( )

