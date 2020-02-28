#! /usr/bin/env python
#
def i4vec_red ( n, a, incx ):

#*****************************************************************************80
#
## I4VEC_RED divides out common factors in an I4VEC.
#
#  Discussion:
#
#    If A is a simple vector, then it has dimension N.
#
#    If A is a row of a matrix, then INCX will not be 1, and
#    the actual dimension of A is at least 1+(N-1)*INCX.
#
#    On output, the entries of A have no common factor
#    greater than 1.
#
#    If A is a simple vector, then INCX is 1, and we simply
#    check the first N entries of A.
#
#    If A is a row of a matrix, then INCX will be the number
#    of rows declared in the matrix, in order to allow us to
#    "skip" along the row.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer A(*), the vector to be reduced.
#
#    Input, integer INCX, the distance between successive
#    entries of A that are to be checked.
#
#    Output, integer A(*), the reduced vector.
#
#    Output, integer IFACT, the common factor that was divided out.
#
  from i4_gcd import i4_gcd
#
#  Find the smallest nonzero value.
#
  ifact = 0
  indx = 0

  for i in range ( 0, n ):

    if ( a[indx] != 0 ):

      if ( ifact == 0 ):
        ifact = abs ( a[indx] )
      else:
        ifact = min ( ifact, abs ( a[indx] ) )

    indx = indx + incx

  if ( ifact == 0 ):
    return a, ifact
#
#  Find the greatest common factor of the entire vector.
#
  indx = 0
  for i in range ( 0, n ):
    ifact = i4_gcd ( a[indx], ifact )
    indx = indx + incx

  if ( ifact == 1 ):
    return a, ifact
#
#  Divide out the common factor.
#
  indx = 0
  for i in range ( 0, n ):
    a[indx] = a[indx] / ifact
    indx = indx + incx

  return a, ifact

def i4vec_red_test ( ):

#*****************************************************************************80
#
## I4VEC_RED_TEST tests I4VEC_RED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print

  print ( '' )
  print ( 'I4VEC_RED_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_RED divides out any common factors in the' )
  print ( '  entries of an I4VEC.' )

  m = 5
  n = 3
  a = np.array ( [ \
   [ 12, 88,   9 ], \
   [  4,  8, 192 ], \
   [-12, 88,  94 ], \
   [ 30, 18,  42 ], \
   [  0,  4,   8 ] ] )
 
  i4mat_print ( m, n, a, '  Apply I4VEC_RED to each row of this matrix:' )

  for i in range ( 0, m ):
    a[i,0:n], factor = i4vec_red ( n, a[i,0:n], 1 )

  i4mat_print ( m, n, a, '  Reduced matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_RED_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_red_test ( )
  timestamp ( )

