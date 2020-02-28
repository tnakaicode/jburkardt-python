#! /usr/bin/env python3
#
def bank_check_digit_calculate ( s ):

#*****************************************************************************80
#
## BANK_CHECK_DIGIT_CALCULATE returns the check digit of a bank checksum.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S, a string containing at least 8 digits.
#    Dashes and other characters will be ignored.  A 9th digit may be
#    included, but it will be ignored.
#
#    Output, integer D, the check digit.
#
  n = 8
  dvec = s_to_digits ( s, n )

  d = 3 * ( dvec[0] + dvec[3] + dvec[6] ) \
    + 7 * ( dvec[1] + dvec[4] + dvec[7] ) \
    +       dvec[2] + dvec[5]

  d = ( d % 10 )

  d = ( ( 10 - d ) % 10 )

  return d

def bank_check_digit_calculate_test ( ):

#*****************************************************************************80
#
## BANK_CHECK_DIGIT_CALCULATE_TEST tests BANK_CHECK_DIGIT_CALCULATE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BANK_CHECK_DIGIT_CALCULATE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BANK_CHECK_DIGIT_CALCULATE calculates the 9-th digit' )
  print ( '  (the check digit) of a bank checksum.' )
  print ( '' )
#
#  Supply the full code, with dashes.
#
  s1 = '123-456-780'
  d1 = 0
  d2 = bank_check_digit_calculate ( s1 )
  print ( '  Check digit of "%s" is %d, expecting %d' % ( s1, d2, d1 ) )
#
#  Supply a partial code, with spaces.
#
  s1 = '123 456 78'
  d1 = 0
  d2 = bank_check_digit_calculate ( s1 )
  print ( '  Check digit of "%s" is %d, expecting %d' % ( s1, d2, d1 ) )
#
#  Supply a partial code, no spaces.
#
  s1 = '323-371-076'
  d1 = 6
  d2 = bank_check_digit_calculate ( s1 )
  print ( '  Check digit of "%s" is %d, expecting %d' % ( s1, d2, d1 ) )
#
#  Supply a partial code, no spaces.
#
  s1 = '87654321'
  d1 = 2
  d2 = bank_check_digit_calculate ( s1 )
  print ( '  Check digit of "%s" is %d, expecting %d' % ( s1, d2, d1 ) )
#
#  Supply a partial code, no spaces.
#
  s1 = '13579864'
  d1 = 3
  d2 = bank_check_digit_calculate ( s1 )
  print ( '  Check digit of "%s" is %d, expecting %d' % ( s1, d2, d1 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BANK_CHECK_DIGIT_CALCULATE_TEST' )
  print ( '  Normal end of execution.' )
  return

def bank_is_valid ( s ):

#*****************************************************************************80
#
## BANK_IS_VALID reports whether a bank checksum is valid.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S, a string containing 9 digits.
#    Dashes and other characters will be ignored.
#
#    Output, bool VALUE, is TRUE if the string is valid.
#
  n = 9
  dvec = s_to_digits ( s, n )

  d1 = bank_check_digit_calculate ( s )
  d2 = dvec[8]

  if ( d1 == d2 ):
    value = True
  else:
    value = False

  return value

def bank_is_valid_test ( ):

#*****************************************************************************80
#
## BANK_IS_VALID_TEST tests BANK_IS_VALID.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BANK_IS_VALID_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BANK_IS_VALID reports whether a bank checksum is valid.' )
  print ( '' )
#
#  Supply a valid code code, with dashes.
#
  s1 = '323-371-076'
  value1 = 1
  value2 = bank_is_valid ( s1 )
  print ( '  Validity of "%s" is %d, expecting %d' % ( s1, value2, value1 ) )
#
#  Modify one digit.
#
  s1 = '323-371-576'
  value1 = 0
  value2 = bank_is_valid ( s1 )
  print ( '  Validity of "%s" is %d, expecting %d' % ( s1, value2, value1 ) )
#
#  Supply a valid code, with spaces.
#
  s1 = '123 456 780'
  value1 = 1
  value2 = bank_is_valid ( s1 )
  print ( '  Validity of "%s" is %d, expecting %d' % ( s1, value2, value1 ) )
#
#  Modify the check digit.
#
  s1 = '123 456 789'
  value1 = 0
  value2 = bank_is_valid ( s1 )
  print ( '  Validity of "%s" is %d, expecting %d' % ( s1, value2, value1 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BANK_IS_VALID_TEST' )
  print ( '  Normal end of execution.' )
  return

def bank_test ( ):

#*****************************************************************************80
#
## BANK_TEST tests the BANK library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the BANK library.' )

  ch_is_digit_test ( )
  ch_to_digit_test ( )
  i4vec_print_test ( )
  s_to_digits_test ( )
  bank_check_digit_calculate_test ( )
  bank_is_valid_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'BANK_TEST:' )
  print ( '  Normal end of execution.' )
  return

def ch_is_digit ( c ):

#*****************************************************************************80
#
## CH_IS_DIGIT returns TRUE if the character C is a digit.
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
#  Parameters:
#
#    Input, character C, the character to be checked.
#
#    Output, logical VALUE is TRUE if C is a decimal digit.
#
  i0 = ord ( '0' )
  i9 = ord ( '9' )
  ic = ord ( c )

  if ( i0 <= ic and ic <= i9 ):

    value = True

  else:

    value = False

  return value

def ch_is_digit_test ( ):

#*****************************************************************************80
#
## CH_IS_DIGIT_TEST tests CH_IS_DIGIT.
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
  import numpy as np
  import platform

  c_test = np.array ( [ 
    '0', '1', '2', '3', '4', \
    '5', '6', '7', '8', '9', \
    'X', '?', ' ' ] )

  print ( '' )
  print ( 'CH_IS_DIGIT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CH_IS_DIGIT is TRUE if a character is a decimal digit.' )
  print ( '' )
 
  for i in range ( 0, 13 ):
    c = c_test[i]
    value = ch_is_digit ( c )
    print ( '  %8d  "%c"  %s' % ( i, c, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CH_IS_DIGIT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def ch_to_digit ( c ):

#*****************************************************************************80
#
## CH_TO_DIGIT returns the integer value of a base 10 digit.
#
#  Example:
#
#     C   DIGIT
#    ---  -----
#    '0'    0
#    '1'    1
#    ...  ...
#    '9'    9
#    ' '   -1
#    'X'   -1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, character C, the decimal digit, '0' through '9'
#    are legal.
#
#    Output, integer DIGIT, the corresponding integer value.  If C was
#    'illegal', then DIGIT is -1.
#
  i0 = ord ( '0' )
  i9 = ord ( '9' )
  ic = ord ( c )

  if ( i0 <= ic and ic <= i9 ):

    digit = ic - i0

  else:

    digit = -1

  return digit

def ch_to_digit_test ( ):

#*****************************************************************************80
#
## CH_TO_DIGIT_TEST tests CH_TO_DIGIT.
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
  import numpy as np
  import platform

  c_test = np.array ( [ 
    '0', '1', '2', '3', '4', \
    '5', '6', '7', '8', '9', \
    'X', '?', ' ' ] )

  print ( '' )
  print ( 'CH_TO_DIGIT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CH_TO_DIGIT: character -> decimal digit' )
  print ( '' )
 
  for i in range ( 0, 13 ):
    c = c_test[i]
    i2 = ch_to_digit ( c )
    print ( '  %8d  "%c"  %8d' % ( i, c, i2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CH_TO_DIGIT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## I4VEC_PRINT prints an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, integer A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_print_test ( ):

#*****************************************************************************80
#
## I4VEC_PRINT_TEST tests I4VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_PRINT prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def s_to_digits ( s, n ):

#*****************************************************************************80
#
## S_TO_DIGITS extracts N digits from a string.
#
#  Discussion:
#
#    The string may include spaces, letters, and dashes, but only the
#    digits 0 through 9 will be extracted.
#
#  Example:
#
#    S  => 34E94-70.6
#    N  => 5
#    D <=  (/ 3, 4, 9, 4, 7 /)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    09 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S, the string.
#
#    Input, integer N, the number of digits to extract.
#
#    Output, integer DVEC(N), the extracted digits.
#
  import numpy as np
  from sys import exit

  s_len = len ( s )

  s_pos = 0
  d_pos = 0

  dvec = np.zeros ( n, dtype = np.int32 )

  while ( d_pos < n ):

    if ( s_len <= s_pos ):
      print ( '' )
      print ( 'S_TO_DIGITS - Fatal error!' )
      print ( '  Could not read enough data from string.' )
      error ( 'S_TO_DIGITS - Fatal error!' );

    c = s[s_pos]
    s_pos = s_pos + 1

    if ( ch_is_digit ( c ) ):
      d = ch_to_digit ( c )
      dvec[d_pos] = d
      d_pos = d_pos + 1

  return dvec

def s_to_digits_test ( ):

#*****************************************************************************80
#
## S_TO_DIGITS_TEST tests S_TO_DIGITS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'S_TO_DIGITS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  S_TO_DIGITS: string -> digit vector' )
  
  s = '34E94-70.6'
  print ( '' )
  print ( '  Test string: "%s"' % ( s ) )
  n = 5
  dvec = s_to_digits ( s, n )
  i4vec_print ( n, dvec, '  Extracted 5 digits:' )

  s = '34E94-70.6'
  print ( '' )
  print ( '  Test string: "%s"' % ( s ) )
  n = 7
  dvec = s_to_digits ( s, n )
  i4vec_print ( n, dvec, '  Extracted 7 digits:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'S_TO_DIGITS_TEST' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  bank_test ( )
  timestamp ( )

