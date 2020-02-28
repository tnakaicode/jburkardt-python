#! /usr/bin/env python
#
def r8vec_normalize_l1 ( n, a ):

#*****************************************************************************80
#
## R8VEC_NORMALIZE_L1 normalizes an R8VEC to have unit sum.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A(N), the vector to be normalized.
#
#    Output, real A(N), the entries of A should have unit sum.  However, 
#    if the input vector has zero sum, the routine halts.
#
  from sys import exit

  a_sum = 0.0
  for i in range ( 0, n ):
    a_sum = a_sum + abs ( a[i] )

  if ( a_sum == 0.0 ):
    print ( '' )
    print ( 'R8VEC_NORMALIZE_L1 - Fatal error!' )
    print ( '  The vector entries sum to 0.' )
    exit ( 'R8VEC_NORMALIZE_L1 - Fatal error!' )

  for i in range ( 0, n ):
    a[i] = a[i] / a_sum

  return a

def r8vec_normalize_l1_test ( ):

#*****************************************************************************80
#
## R8VEC_NORMALIZE_L1_TEST tests R8VEC_NORMALIZE_L1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  n = 10

  print ( '' )
  print ( 'R8VEC_NORMALIZE_L1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORMALIZE_L1 normalizes an R8VEC in the L1 norm.' )
 
  r8_lo = - 10.0
  r8_hi = + 10.0

  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
 
  r8vec_print ( n, a, '  Input vector:' )

  a = r8vec_normalize_l1 ( n, a )

  r8vec_print ( n, a, '  After calling R8VEC_NORMALIZE_L1:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORMALIZE_L1_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_normalize_l1_test ( )
  timestamp ( )
 
