#! /usr/bin/env python
#
def perm0_mul ( n, p1, p2 ):

#*****************************************************************************80
#
## PERM0_MUL "multiplies" two permutations of (0,...,N-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the permutations.
#
#    Input, integer P1(N), P2(N), the permutations.
#
#    Output, integer P3(N), the product permutation.
#
  import numpy as np
  from sys import exit
  from perm0_check import perm0_check

  check = perm0_check ( n, p1 )

  if ( not check ):
    print ( '' )
    print ( 'PERM0_MUL - Fatal error!' )
    print ( '  The input array P1 does not represent' )
    print ( '  a proper permutation.' )
    exit ( 'PERM0_MUL - Fatal error!' )

  check = perm0_check ( n, p2 )

  if ( not check ):
    print ( '' )
    print ( 'PERM0_MUL - Fatal error!' )
    print ( '  The input array P2 does not represent' )
    print ( '  a proper permutation.' )
    exit ( 'PERM0_MUL - Fatal error!' )

  p3 = np.zeros ( n )

  for i in range ( 0, n ):
    p3[i] = p2[p1[i]]

  return p3

def perm0_mul_test ( ):

#*****************************************************************************80
#
## PERM0_MUL_TEST tests PERM0_MUL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from perm0_print import perm0_print
  from perm0_random import perm0_random

  n = 5

  print ( '' )
  print ( 'PERM0_MUL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_MUL multiplies two permutations.' )

  seed = 123456789

  p1, seed = perm0_random ( n, seed )
  p2, seed = perm0_random ( n, seed )

  perm0_print ( n, p1, '  Permutation P1:' )

  perm0_print ( n, p2, '  Permutation P2:' )

  p3 = perm0_mul ( n, p1, p2 )

  perm0_print ( n, p3, '  Product permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_MUL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_mul_test ( )
  timestamp ( )

