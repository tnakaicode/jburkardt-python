#! /usr/bin/env python
#
def r8vec_permute_cyclic ( n, k, a ):

#*****************************************************************************80
#
## R8VEC_PERMUTE_CYCLIC performs a cyclic permutation of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    For 0 <= K < N, this function cyclically permutes the input vector
#    to have the form
#
#     ( A(K+1), A(K+2), ..., A(N), A(1), ..., A(K) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of objects.
#
#    Input, integer K, the increment used.
#
#    Input, real A(N), the array to be permuted.
#
#    Output, real B(N), the permuted array.
#
  import numpy as np
  from i4_wrap import i4_wrap

  b = np.zeros ( n )

  for i in range ( 0, n ):
    ipk = i4_wrap ( i + k, 0, n - 1 )
    b[i] = a[ipk];

  return b

def r8vec_permute_cyclic_test ( ):

#*****************************************************************************80
#
## R8VEC_PERMUTE_CYCLIC_TEST tests R8VEC_PERMUTE_CYCLIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'R8VEC_PERMUTE_CYCLIC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PERMUTE_CYCLIC performa a cyclic permutation' )
  print ( '  of K positions on an R8VEC.' )

  k = 4
  print ( '' )
  print ( '  K = %d' % ( k ) )

  n = 10
  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  Original array X:' )

  x = r8vec_permute_cyclic ( n, k, x )

  r8vec_print ( n, x, '  Array after permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PERMUTE_CYCLIC_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_permute_cyclic_test ( )
  timestamp ( )
 
