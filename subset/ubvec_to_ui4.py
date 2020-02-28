#! /usr/bin/env python
#
def ubvec_to_ui4 ( n, ubvec ):

#*****************************************************************************80
#
## UBVEC_TO_UI4 makes an unsigned integer from an unsigned binary vector.
#
#  Discussion:
#
#    A UBVEC is an integer vector of binary digits, intended to
#    represent a nonnegative integer.  UBVEC(1) is the units digit, UBVEC(N)
#    is the coefficient of 2^(N-1).
#
#  Example:
#
#    N = 4
#
#        UBVEC   binary  I
#    ----------  -----  --
#    1  2  3  4
#    ----------
#    1, 0, 0, 0       1  1
#    0, 1, 0, 0      10  2
#    0, 0, 1, 1      11  3
#    0, 0, 1, 0     100  4
#    1, 0, 0, 1    1001  9
#    1, 1, 1, 1    1111 15
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
#    Input, integer N, the dimension of the vector.
#
#    Input, integer UBVEC(N), the binary representation.
#
#    Output, integer VALUE, the integer.
#
  value = 0
  for i in range ( 0, n ):
    value = 2 * value + ubvec[i]

  return value

def ubvec_to_ui4_test ( ):

#*****************************************************************************80
#
## UBVEC_TO_UI4_TEST tests UBVEC_TO_UI4
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
  from ui4_to_ubvec import ui4_to_ubvec

  n = 10

  print ( '' )
  print ( 'UBVEC_TO_UI4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UBVEC_TO_UI4 converts an unsigned binary vector' )
  print ( '  to an unsigned integer' )
  print ( '' )
  print ( '  UI4 --> UBVEC  -->  UI4' )
  print ( '' )

  for ui4 in range ( 0, 11 ):
    ubvec = ui4_to_ubvec ( ui4, n )
    i2 = ubvec_to_ui4 ( n, ubvec )
    print ( '  %2d  ' % ( ui4 ) ),
    for j in range ( 0, n ):
      print ( '%1d' % ( ubvec[j] ) ),
    print ( '  %2d' % ( i2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'UBVEC_TO_UI4_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  ubvec_to_ui4_test ( )
  timestamp ( )

