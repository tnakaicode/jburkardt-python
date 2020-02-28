#! /usr/bin/env python
#
def dec_width ( mantissa, exponent ):

#*****************************************************************************80
#
## DEC_WIDTH returns the "width" of a decimal number.
#
#  Discussion:
#
#    A decimal value is represented by MANTISSA * 10^EXPONENT.
#
#    The "width" of a decimal number is the number of characters
#    required to print it.
#
#  Example:
#
#    Mantissa  Exponent Width  Representation:
#
#         523      -1       4           5.23
#         134       2       5       13400
#           0      10       1           0
#      123456     -10      12           0.0000123456
#      123456      -3       7         123.456
#      123456       0       6      123456
#      123456       3       9   123456000
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer MANTISSA, EXPONENT, the decimal number.
#
#    Output, integer WIDTH, the "width" of the decimal number.
#
  width = 1
  ten_pow = 10

  if ( mantissa == 0 ):
    return width
  
  mantissa_abs = abs ( mantissa )

  while ( ten_pow <= mantissa_abs ):
    width = width + 1
    ten_pow = ten_pow * 10

  if ( 0 < exponent ):
    width = width + exponent
  elif ( exponent < 0 ):
    width = max ( width, 1 - exponent )
#
#  An internal decimal point adds one position.
#
    if ( 0 < width ):
      width = width + 1
#
#  A leading "0." adds two positions.
#
    else:
      width = 2 - width

  if ( mantissa < 0 ):
    width = width + 1

  return width

def dec_width_test ( ):

#*****************************************************************************80
#
## DEC_WIDTH_TEST tests DEC_WIDTH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'DEC_WIDTH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DEC_WIDTH determines the "width" of a decimal.' )
  print ( '' )
  print ( '  Mantissa  Exponent  Width' )
  print ( '' )

  mantissa = 523
  exponent = -1
  i = dec_width ( mantissa, exponent )
  print ( '  %6d  %6d  %6d' % ( mantissa, exponent, i ) )

  mantissa = 134
  exponent = 2
  i = dec_width ( mantissa, exponent )
  print ( '  %6d  %6d  %6d' % ( mantissa, exponent, i ) )

  mantissa = -134
  exponent = 2
  i = dec_width ( mantissa, exponent )
  print ( '  %6d  %6d  %6d' % ( mantissa, exponent, i ) )

  mantissa = 0
  exponent = 10
  i = dec_width ( mantissa, exponent )
  print ( '  %6d  %6d  %6d' % ( mantissa, exponent, i ) )

  for exponent in range ( -8, 4 ):
    mantissa = 123456
    i = dec_width ( mantissa, exponent )
    print ( '  %6d  %6d  %6d' % ( mantissa, exponent, i ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DEC_WIDTH_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dec_width_test ( )
  timestamp ( )

