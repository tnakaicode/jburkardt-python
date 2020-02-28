#! /usr/bin/env python
#
def dec_to_s ( mantissa, exponent ):

#*****************************************************************************80
#
## DEC_TO_S returns a string representation of a decimal.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#  Example:
#
#    MANTISSA EXPONENT   S
#    ----     ----       ------
#       0        0       0
#      21        3       21000
#      -3        0       -3
#     147       -2       14.7
#      16       -5       0.00016
#     123      -21       0.0000000000000000012
#      34      -30       0.0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer MANTISSA, EXPONENT, integers which represent the decimal.
#
#    Output, string S, the representation of the value.
#
  from digit_to_ch import digit_to_ch

  s = ''

  if ( mantissa == 0 ):
    s = '0'
    return s

  if ( mantissa < 0 ):
    s = '-'
    mantissa = abs ( mantissa )
#
#  Mantissas should be normalized so that they do not end in 0!
#
  while ( 10 * ( mantissa // 10 ) == mantissa ):
    mantissa = ( mantissa // 10 )
    exponent = exponent + 1
#
#  How many digits are there in the mantissa?
#
  mantissa_digits = 0
  mantissa_ten = 1

  while ( mantissa_ten <= mantissa ):
    mantissa_ten = mantissa_ten * 10
    mantissa_digits = mantissa_digits + 1
#
#  For a positive exponent, we just print the mantissa,
#  possibly followed by some zeros.
#
  if ( 0 <= exponent ):

    for i in range ( 0, mantissa_digits ):
      mantissa_ten = ( mantissa_ten // 10 )
      d = ( mantissa // mantissa_ten )
      mantissa = mantissa - d * mantissa_ten
      c = digit_to_ch ( d )
      s = s + c

    for i in range ( 0, exponent ):
      s = s + '0'
#
#  A negative mantissa means, 
#  * possibly some digits, or else 0,
#  * a decimal point,
#  * possibly some zeros
#  * the remaining digits.
#
  elif ( exponent < 0 ):

    if ( 0 < mantissa_digits + exponent ):

      for i in range ( 0, mantissa_digits + exponent ):
        mantissa_ten = ( mantissa_ten // 10 )
        d = ( mantissa // mantissa_ten )
        mantissa = mantissa - d * mantissa_ten
        c = digit_to_ch ( d )
        s = s + c

      s = s + '.'

      ihi = - exponent

      for i in range ( 0, ihi ):
        mantissa_ten = ( mantissa_ten // 10 )
        d = ( mantissa // mantissa_ten )
        mantissa = mantissa - d * mantissa_ten
        c = digit_to_ch ( d )
        s = s + c

    elif ( 0 == mantissa_digits + exponent ):

      s = s + '0' + '.'

      for i in range ( 0, mantissa_digits ):
        mantissa_ten = ( mantissa_ten // 10 )
        d = ( mantissa // mantissa_ten )
        mantissa = mantissa - d * mantissa_ten
        c = digit_to_ch ( d )
        s = s + c

    elif ( mantissa_digits + exponent < 0 ):

      s = s + '0' + '.'

      ihi = - ( mantissa_digits + exponent )

      for i in range ( 0, ihi ):
        s = s + '0'

      for i in range ( 0, mantissa_digits ):
        mantissa_ten = ( mantissa_ten // 10 )
        d = ( mantissa // mantissa_ten )
        mantissa = mantissa - d * mantissa_ten
        c = digit_to_ch ( d )
        s = s + c

  return s

def dec_to_s_test ( ):

#*****************************************************************************80
#
## DEC_TO_S_TEST tests DEC_TO_S.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'DEC_TO_S_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DEC_TO_S prints a decimal value.' )
  print ( '' )
  print ( '  Mantissa  Exponent  String' )
  print ( '' )

  mantissa = 523
  exponent = -1
  s = dec_to_s ( mantissa, exponent )
  print ( '    %6d  %8d  %s' % ( mantissa, exponent, s ) )

  mantissa = 134
  exponent = 2
  s = dec_to_s ( mantissa, exponent )
  print ( '    %6d  %8d  %s' % ( mantissa, exponent, s ) )

  mantissa = -134
  exponent = 2
  s = dec_to_s ( mantissa, exponent )
  print ( '    %6d  %8d  %s' % ( mantissa, exponent, s ) )

  mantissa = 0
  exponent = 10
  s = dec_to_s ( mantissa, exponent )
  print ( '    %6d  %8d  %s' % ( mantissa, exponent, s ) )

  for exponent in range ( -8, 4 ):
    mantissa = 123456
    s = dec_to_s ( mantissa, exponent )
    print ( '    %6d  %8d  %s' % ( mantissa, exponent, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DEC_TO_S_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dec_to_s_test ( )
  timestamp ( )

