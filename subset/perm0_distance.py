#! /usr/bin/env python
#
def perm0_distance ( n, a, b ):

#*****************************************************************************80
#
## PERM0_DISTANCE computes the distance of two permutations of (0,...,N-1).
#
#  Discussion:
#
#    The distance is known as the Ulam metric.
#
#    If we let N be the order of the permutations A and B, and L(P) be
#    the length of the longest ascending subsequence of a permutation P,
#    then the Ulam metric distance between A and B is
#
#      N - L ( A * inverse ( B ) ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the permutation.
#
#    Input, integer A(N), B(N), the permutations to be examined.
#
#    Output, integer K, the Ulam metric distance between A and B.
#
  from perm_ascend import perm_ascend
  from perm0_inverse import perm0_inverse
  from perm0_mul import perm0_mul

  binv = perm0_inverse ( n, b )

  c = perm0_mul ( n, a, binv )

  length, c2 = perm_ascend ( n, c )

  k = n - length

  return k

def perm0_distance_test ( ):

#*****************************************************************************80
#
## PERM0_DISTANCE_TEST tests PERM0_DISTANCE
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from perm0_print import perm0_print
  from perm0_random2 import perm0_random2

  n = 10

  print ( '' )
  print ( 'PERM0_DISTANCE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM0_DISTANCE computes the Ulam metric distance' )
  print ( '  between two permutations.' )

  seed = 123456789

  p1, seed = perm0_random2 ( n, seed )
  perm0_print ( n, p1, '  Permutation P1' )
  p2, seed = perm0_random2 ( n, seed )
  perm0_print ( n, p2, '  Permutation P2' )
  p3, seed = perm0_random2 ( n, seed )
  perm0_print ( n, p3, '  Permutation P3' )

  k11 = perm0_distance ( n, p1, p1 )
  k12 = perm0_distance ( n, p1, p2 )
  k21 = perm0_distance ( n, p2, p1 )
  k13 = perm0_distance ( n, p1, p3 )
  k23 = perm0_distance ( n, p2, p3 )

  print ( '' )
  print ( '  K(P1,P1) should be 0.' )
  print ( '' )
  print ( '  K(P1,P1) = %d' % ( k11 ) )
  print ( '' )
  print ( '  K(P1,P2) should equal K(P2,P1).' )
  print ( '' )
  print ( '  K(P1,P2) = %d' % ( k12 ) )
  print ( '  K(P2,P1) = %d' % ( k21 ) )
  print ( '' )
  print ( '  K(P1,P3) <= K(P1,P2) + K(P2,P3).' )
  print ( '' )
  print ( '  K(P1,P3) = %d' % ( k13 ) )
  print ( '  K(P1,P2) = %d' % ( k12 ) )
  print ( '  K(P2,P3) = %d' % ( k23 ) )
  print ( '  K(P1,P2) + K(P2,P3) = %d' % ( k12 + k23 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM0_DISTANCE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  perm0_distance_test ( )
  timestamp ( )

