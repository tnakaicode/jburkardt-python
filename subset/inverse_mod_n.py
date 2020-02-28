#! /usr/bin/env python
#
def inverse_mod_n ( b, n ):

#*****************************************************************************80
#
## INVERSE_MOD_N computes the inverse of B mod N.
#
#  Discussion:
#
#    If
#
#      Y = inverse_mod_n ( B, N )
#
#    then
#
#      mod ( B * Y, N ) = 1
#
#    The value Y will exist if and only if B and N are relatively prime.
#
#  Examples:
#
#    B  N  Y
#
#    1  2  1
#
#    1  3  1
#    2  3  2
#
#    1  4  1
#    2  4  0
#    3  4  3
#
#    1  5  1
#    2  5  3
#    3  5  2
#    4  5  4
#
#    1  6  1
#    2  6  0
#    3  6  0
#    4  6  0
#    5  6  5
#
#    1  7  1
#    2  7  4
#    3  7  5
#    4  7  2
#    5  7  3
#    6  7  6
#
#    1  8  1
#    2  8  0
#    3  8  3
#    4  8  0
#    5  8  5
#    6  8  0
#    7  8  7
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer B, the number whose inverse mod N is desired.
#    B should be positive.  Normally, B < N, but this is not required.
#
#    Input, integer N, the number with respect to which the
#    modulus is computed.  N should be positive.
#
#    Output, integer Y, the inverse of B mod N, or 0 if there
#    is not inverse for B mode N.  1 <= Y < N if the inverse exists.
#
  n0 = n
  b0 = b
  t0 = 0
  t = 1

  q = ( n // b )
  r = n - q * b

  while ( 0 < r ):

    temp = t0 - q * t

    if ( 0 <= temp ):
      temp = ( temp % n )

    if ( temp < 0 ):
      temp = n - ( ( - temp ) % n )

    t0 = t
    t = temp
    n0 = b0
    b0 = r
    q = ( n0 // b0 )
    r = n0 - q * b0

  if ( b0 != 1 ):
    y = 0
  else:
    y = ( t % n )

  return y

def inverse_mod_n_test ( ):

#*****************************************************************************80
#
## INVERSE_MOD_N_TEST tests INVERSE_MOD_N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'INVERSE_MOD_N_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  INVERSE_MOD_N seeks Y, the inverse of B mod N,' )
  print ( '  so that mod ( B * Y, N ) = 1, but returns 0' )
  print ( '  if the inverse does not exist.' )

  print ( '' )
  print ( '     B     N     Y     Z = mod ( B * Y, N )' )

  for n in range ( 1, 11 ):
    print ( '' )
    for b in range ( 1, n ):
      y = inverse_mod_n ( b, n )
      z = ( ( b * y ) % n )
      print ( '  %4d  %4d  %4d  %4d' % ( b, n, y, z ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'INVERSE_MOD_N_TEST' )
  print ( '  Normal end of execution' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  inverse_mod_n_test ( )
  timestamp ( )
