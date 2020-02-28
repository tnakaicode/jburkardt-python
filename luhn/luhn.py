#! /usr/bin/env python3
#
def luhn_check_digit_calculate ( partial_card_number ):

#*****************************************************************************80
#
## LUHN_CHECK_DIGIT_CALCULATE calculates the Luhn checkdigit for a string.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 September 2015
#
#  Reference:
#
#    https://en.wikipedia.org/wiki/Luhn_algorithm
#
#  Parameters:
#
#    Input, string PARTIAL_CARD_NUMBER, the string.
#
#    Output, integer VALUE, the Luhn checkdigit.
#

#
#  Append a 0 to the original string, then compute the checksum.
#
  value = luhn_checksum ( int ( partial_card_number ) * 10 )

  if ( value != 0 ):
    value = 10 - value

  return value

def luhn_check_digit_calculate_test ( ):

#*****************************************************************************80
#
## LUHN_CHECK_DIGIT_CALCULATE_TEST tests LUHN_CHECK_DIGIT_CALCULATE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LUHN_CHECK_DIGIT_CALCULATE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LUHN_CHECK_DIGIT_CALCULATE computes the Luhn check digit for a string of digits.' )
  print ( '' )

  s = '7992739871'
  d1 = luhn_check_digit_calculate ( s )
  d2 = 3
  print ( '  Check digit for %s is %d, expecting %d' % ( s, d1, d2 ) )

  s = '9876234510'
  d1 = luhn_check_digit_calculate ( s )
  d2 = 0
  print ( '  Check digit for %s is %d, expecting %d' % ( s, d1, d2 ) )

  s = '246897531'
  d1 = luhn_check_digit_calculate ( s )
  d2 = 9
  print ( '  Check digit for %s is %d, expecting %d' % ( s, d1, d2 ) )

  s = '135798642'
  d1 = luhn_check_digit_calculate ( s )
  d2 = 9
  print ( '  Check digit for %s is %d, expecting %d' % ( s, d1, d2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LUHN_CHECK_DIGIT_CALCULATE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def luhn_checksum ( card_number ):

#*****************************************************************************80
#
## LUHN_CHECKSUM determines the Luhn checksum of a string.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 September 2015
#
#  Reference:
#
#    https://en.wikipedia.org/wiki/Luhn_algorithm
#
#  Parameters:
#
#    Input, string CARD_NUMBER, the string of digits to be checked.
#
#    Output, integer VALUE, is the Luhn checksum for this string.
#
  def digits_of ( n ):
    return [ int ( d ) for d in str ( n ) ]

  digits = digits_of ( card_number )
  odd_digits = digits[-1::-2]
  even_digits = digits[-2::-2]

  checksum = sum ( odd_digits )
  for d in even_digits:
    checksum = checksum + sum ( digits_of ( d * 2 ) )

  value = ( checksum % 10 )

  return value

def luhn_checksum_test ( ):

#*****************************************************************************80
#
## LUHN_CHECKSUM_TEST tests LUHN_CHECKSUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LUHN_CHECKSUM_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LUHN_CHECKSUM computes the Luhn checksum for a string.' )

  s1 = '7992739871'
  d2 = 3
  print ( '' )
  print ( '  Luhn check digit for %s is %d.' % ( s1, d2 ) )
  print ( '' )
  for d1 in range ( 0, 10 ):
    s2 = s1 + str ( d1 )
    value = luhn_checksum ( s2 )
    print ( '  luhn_checksum ( %s ) = %d' % ( s2, value ) )

  s1 = '9876234510'
  d2 = 0
  print ( '' )
  print ( '  Luhn check digit for %s is %d.' % ( s1, d2 ) )
  print ( '' )
  for d1 in range ( 0, 10 ):
    s2 = s1 + str ( d1 )
    value = luhn_checksum ( s2 )
    print ( '  luhn_checksum ( %s ) = %d' % ( s2, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LUHN_CHECKSUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def luhn_is_valid ( card_number ):

#*****************************************************************************80
#
## LUHN_IS_VALID determines whether a string has a valid Luhn checkdigit.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 September 2015
#
#  Reference:
#
#    https://en.wikipedia.org/wiki/Luhn_algorithm
#
#  Parameters:
#
#    Input, string CARD_NUMBER, the string of digits to be checked.
#
#    Output, logical VALUE, is true if the final digit is the correct
#    Luhn checkdigit for this string.
#
  value = ( luhn_checksum ( card_number ) == 0 )

  return value

def luhn_is_valid_test ( ):

#*****************************************************************************80
#
## LUHN_IS_VALID_TEST tests LUHN_IS_VALID.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LUHN_IS_VALID_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LUHN_IS_VALID reports whether a string has a valid Luhn checkdigit.' )

  s1 = '7992739871'
  d2 = 3
  print ( '' )
  print ( '  Luhn check digit for %s is %d.' % ( s1, d2 ) )
  print ( '' )
  for d1 in range ( 0, 10 ):
    s2 = s1 + str ( d1 )
    value = luhn_is_valid ( s2 )
    print ( '  luhn_is_valid ( %s ) = %s' % ( s2, value ) )

  s1 = '9876234510'
  d2 = 0
  print ( '' )
  print ( '  Luhn check digit for %s is %d.' % ( s1, d2 ) )
  print ( '' )
  for d1 in range ( 0, 10 ):
    s2 = s1 + str ( d1 )
    value = luhn_is_valid ( s2 )
    print ( '  luhn_is_valid ( %s ) = %s' % ( s2, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LUHN_IS_VALID_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def luhn_test ( ):

#*****************************************************************************80
#
## LUHN_TEST tests the LUHN library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 October 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LUHN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the LUHN library.' )

  luhn_check_digit_calculate_test ( )
  luhn_checksum_test ( )
  luhn_is_valid_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'LUHN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  luhn_test ( )
  timestamp ( )
 
