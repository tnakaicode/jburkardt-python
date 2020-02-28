#! /usr/bin/env python
#
def i4_div_rounded ( a, b ):

#*****************************************************************************80
#
## I4_DIV_ROUNDED computes the rounded result of I4 division.
#
#  Discussion:
#
#    This routine computes C = A / B, where A, B and C are integers
#    and C is the closest integer value to the exact real result.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, B, the number to be divided,
#    and the divisor.
#
#    Output, integer VALUE, the rounded result of the division.
#
  from math import floor

  i4_huge = 2147483647

  if ( a == 0 and b == 0 ):

    value = i4_huge
 
  elif ( a == 0 ):

    value = 0

  elif ( b == 0 ):

    if ( a < 0 ):
      value = - i4_huge
    else:
      value = + i4_huge

  else:

    a_abs = abs ( a )
    b_abs = abs ( b )

    value = floor ( a_abs / b_abs )
#
#  Round the value.
#
    if ( ( 2 * value + 1 ) * b_abs < 2 * a_abs ):
      value = value + 1
#
#  Set the sign.
#
    if ( ( a < 0 and 0 < b ) or ( 0 < a and b < 0 ) ):
      value = - value

  return value

def i4_div_rounded_test ( ):

#*****************************************************************************80
#
## I4_DIV_ROUNDED_TEST tests I4_DIV_ROUNDED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4_uniform_ab import i4_uniform_ab
  from math import floor

  a_hi =  100
  a_lo = -100
  b_hi =  10
  b_lo = -10
  test_num = 20

  print ( '' )
  print ( 'I4_DIV_ROUNDED_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_DIV_ROUNDED performs rounded integer division.' )
  print ( ' ' )
  print ( '  C0 = real ( a ) / real ( b )' )
  print ( '  C1 = I4_DIV_ROUNDED ( A, B )' )
  print ( '  C2 = nint ( real ( a ) / real ( b ) )' )
  print ( '  C3 = int ( A / B )' )
  print ( '  C4 = floor ( real ( a ) / real ( b ) )' )
  print ( '  C5 = a // b' )
  print ( ' ' )
  print ( '  C1 and C2 should be equal;' )
  print ( '  C3 and C4 should be equal.' )
  print ( ' ' )
  print ( '     A     B           C0         C1    C2      C3    C4      C5' )
  print ( ' ' )

  seed = 123456789

  for test in range ( 1, test_num ):
    a, seed = i4_uniform_ab ( a_lo, a_hi, seed )
    b, seed = i4_uniform_ab ( b_lo, b_hi, seed )
    if ( b == 0 ):
      b = 7
    c0 = float ( a ) / float ( b )
    c1 = i4_div_rounded ( a, b )
    c2 = round ( float ( a ) / float ( b ) )
    c3 = int ( a / b )
    c4 = floor ( float ( a ) / float ( b ) )
    c5 = a // b
    print ( '  %4d  %4d    %14.6f  %4d  %4d    %4d  %4d    %4d' \
      % ( a, b, c0, c1, c2, c3, c4, c5 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_DIV_ROUNDED_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_div_rounded_test ( )
  timestamp ( )

