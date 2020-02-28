#! /usr/bin/env python
#
def l4vec_next ( n, l4vec ):

#*****************************************************************************80
#
## L4VEC_NEXT generates the next logical vector.
#
#  Discussion:
#
#    In the following discussion, we will let '0' stand for FALSE and
#    '1' for TRUE.
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
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vectors.
#
#    Input, logical L4VEC(N), the vector whose successor is desired.
#
#    Output, logical L4VEC(N), the successor to the input vector.
#
  for i in range ( n - 1, -1, -1 ):

    if ( not l4vec[i] ):
      l4vec[i] = True
      break

    l4vec[i] = False

  return l4vec

def l4vec_next_test ( ):

#*****************************************************************************80
#
## L4VEC_NEXT_TEST tests L4VEC_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'L4VEC_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  L4VEC_NEXT generates logical vectors of dimension N one at a time.' )

  for n in range ( 2, 4 ):

    print ( '' )
    print ( '  Vector size N = %d' % ( n ) )
    print ( '' )

    k = 0

    l4vec = np.zeros ( n, dtype = np.bool )

    for i in range ( 0, n ):
      l4vec[i] = False

    while ( True ):

      print ( '  %2d:  ' % ( k ) ),
      for i in range ( 0, n ):
        print ( '  %s' % ( l4vec[i] ) ),
      print ( '' )

      l4vec = l4vec_next ( n, l4vec )

      if ( not any ( l4vec ) ):
        break

      k = k + 1
#
#  Terminate.
#
  print ( '' )
  print ( 'L4VEC_NEXT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  l4vec_next_test ( )
  timestamp ( )
