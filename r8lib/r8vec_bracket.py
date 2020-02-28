#! /usr/bin/env python
#
def r8vec_bracket ( n, x, xval ):

#*****************************************************************************80
#
## R8VEC_BRACKET searches a sorted array for successive brackets of a value.
#
#  Discussion:
#
#    A naive algorithm is used.
#
#    If the values in the vector are thought of as defining intervals
#    on the real line, then this routine searches for the interval
#    nearest to or containing the given value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, length of input array.
#
#    Input, real X(N), an array that has been sorted into ascending order.
#
#    Input, real XVAL, a value to be bracketed.
#
#    Output, integer LEFT, RIGHT, the results of the search.
#    Either:
#      XVAL < X(1), when LEFT = 1, RIGHT = 2
#      XVAL > X(N), when LEFT = N-1, RIGHT = N
#    or
#      X(LEFT) <= XVAL <= X(RIGHT).
#
  for i in range ( 1, n - 1 ):

    if ( xval < x[i] ):
      left = i - 1
      right = i
      return left, right

  left = n - 2
  right = n - 1

  return left, right

def r8vec_bracket_test ( ):

#*****************************************************************************80
#
## R8VEC_SORTED_NEAREST_TEST tests R8VEC_SORTED_NEAREST.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print
  from r8_uniform_ab import r8_uniform_ab

  n = 11
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_BRACKET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_BRACKET finds, for a given value R,' )
  print ( '  the nearest interval [low,high] in a sorted R8VEC' )
  print ( '  that "brackets" the value.' )

  s = np.linspace ( 0.0, 10.0, n );
  r8vec_print ( n, s, '  Sorted R8VEC:' )

  print ( '' )
  for i in range ( 0, 15 ):
    r, seed = r8_uniform_ab ( -1.0, 11.0, seed )
    [ low, high ] = r8vec_bracket ( n, s, r )
    print ( '  R = %g is bracketed by ( S[%d] = %g, S[%d] = %g' \
      % ( r, low, s[low], high, s[high] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_BRACKET_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_bracket_test ( )
  timestamp ( )

