#! /usr/bin/env python
#
def i4vec_binary_next ( n, bvec ):

#*****************************************************************************80
#
## I4VEC_BINARY_NEXT generates the next binary vector.
#
#  Discussion:
#
#    The vectors have the order
#
#      (0,0,...,0),
#      (0,0,...,1),
#      ...
#      (1,1,...,1)
#
#    and the "next" vector after (1,1,...,1) is (0,0,...,0).  That is,
#    we allow wrap around.
#
#  Example:
#
#    N = 3
#
#    Input      Output
#    -----      ------
#    0 0 0  =>  0 0 1
#    0 0 1  =>  0 1 0
#    0 1 0  =>  0 1 1
#    0 1 1  =>  1 0 0
#    1 0 0  =>  1 0 1
#    1 0 1  =>  1 1 0
#    1 1 0  =>  1 1 1
#    1 1 1  =>  0 0 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vectors.
#
#    Input, integer BVEC(N), the vector whose successor is desired.
#
#    Output, integer BVEC(N), the successor to the input vector.
#
  for i in range ( n - 1, -1, -1 ):

    if ( bvec[i] == 0 ):
      bvec[i] = 1
      break

    bvec[i] = 0

  return bvec

def i4vec_binary_next_test ( ):

#*****************************************************************************80
#
## I4VEC_BINARY_NEXT_TEST tests I4VEC_BINARY_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 3

  print ( '' )
  print ( 'I4VEC_BINARY_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_BINARY_NEXT generates the next binary vector.' )
  print ( '' )
 
  bvec = np.zeros ( n )

  while ( True ):

    print ( '  ', end = '' )
    for i in range ( 0, n ):
      print ( '%d' % ( bvec[i] ), end = '' )
    print ( '' )

    if ( all ( bvec[0:n] == 1 ) ):
      break

    bvec = i4vec_binary_next ( n, bvec )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_BINARY_NEXT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_binary_next_test ( )
  timestamp ( )

