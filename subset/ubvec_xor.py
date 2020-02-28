#! /usr/bin/env python
#
def ubvec_xor ( n, ubvec1, ubvec2 ):

#*****************************************************************************80
#
## UBVEC_XOR computes the exclusive OR of two UBVEC's.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  BVEC(1) is the units digit, BVEC(N)
#    is the coefficient of 2^(N-1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the length of the vectors.
#
#    Input, integer UBVEC1(N), UBVEC2(N), the binary vectors to be XOR'ed.
#
#    Input, integer UBVEC3(N), the exclusive OR of the two vectors.
#
  import numpy as np

  ubvec3 = np.zeros ( n )

  for i in range ( 0, n ):
    ubvec3[i] = ( ( ubvec1[i] + ubvec2[i] ) % 2 )

  return ubvec3

def ubvec_xor_test ( ):

#*****************************************************************************80
#
## UBVEC_XOR_TEST tests UBVEC_XOR
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4_uniform_ab import i4_uniform_ab
  from ubvec_to_ui4 import ubvec_to_ui4
  from ui4_to_ubvec import ui4_to_ubvec

  n = 10
  seed = 123456789
  test_num = 10

  print ( '' )
  print ( 'UBVEC_XOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UBVEC_XOR exclusive-ors unsigned binary vectors representing' )
  print ( '  unsigned integers' )
  print ( '' )
  print ( '        I        J        K = I XOR J' )
  print ( '' )

  for test in range ( 0, 10 ):
    i, seed = i4_uniform_ab ( 0, 100, seed )
    j, seed = i4_uniform_ab ( 0, 100, seed )
    ubvec1 = ui4_to_ubvec ( i, n )
    ubvec2 = ui4_to_ubvec ( j, n )
    ubvec3 = ubvec_xor ( n, ubvec1, ubvec2 )
    k = ubvec_to_ui4 ( n, ubvec3 )
    print ( '  %8d  %8d  %8d' % ( i, j, k ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'UBVEC_XOR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ubvec_xor_test ( )
  timestamp ( )

