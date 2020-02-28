#! /usr/bin/env python
#
def i4vec_max_last ( l_length, l ):

#*****************************************************************************80
#
## I4VEC_MAX_LAST moves the maximum entry of an I4VEC to the last position.
#
#  Discussion:
#
#    This routine finds the largest entry in an array and moves
#    it to the end of the array.
#
#    If we ignore this last array entry, then the effect is the same
#    as "deleting" the maximum entry from the array.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Pavel Pevzner,
#    Computational Molecular Biology,
#    MIT Press, 2000,
#    ISBN: 0-262-16197-4,
#    LC: QH506.P47.
#
#  Parameters:
#
#    Input, integer L_LENGTH, the length of the array.
#
#    Input/output, integer L(L_LENGTH), the array.  On output,
#    the maximum entry has been shifted to the end.
#
#    Output, integer VALUE, the maximum entry in the
#    input array.
#
  for i in range ( 1, l_length ):
    if ( l[i] < l[i-1] ):
      t = l[i]
      l[i] = l[i-1]
      l[i-1] = t
 
  value = l[l_length-1];

  return l, value

def i4vec_max_last_test ( ):

#*****************************************************************************80
#
## I4VEC_MAX_LAST_TEST tests I4VEC_MAX_LAST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2018
#
#  Author:
#
#   John Burkardt
#
  import numpy as np
  from i4_uniform_ab import i4_uniform_ab
  from i4vec_print import i4vec_print

  n = 10

  print ( '' )
  print ( 'I4VEC_MAX_LAST_TEST' )
  print ( '  I4VEC_MAX_LAST identifies the largest element in an' )
  print ( '  I4VEC, and moves it to the final entry.' )

  seed = 123456789

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i], seed = i4_uniform_ab ( 1, 30, seed )

  i4vec_print ( n, x, '  Input vector:' )

  x, x_max = i4vec_max_last ( n, x )

  print ( '' )
  print ( '  Maximum: %d' % ( x_max ) )

  i4vec_print ( n, x, '  Output vector:' )

  return
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_MAX_LAST_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_max_last_test ( )
  timestamp ( )
