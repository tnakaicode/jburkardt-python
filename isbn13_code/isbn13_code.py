#! /usr/bin/env python3
#
def isbn13_code_test ( ):

#*****************************************************************************80
#
## isbn13_code_test() tests isbn13_code().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  timestamp ( )
  print ( '' )
  print ( 'isbn13_code_test():' )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  Test isbn13_code().' )

  isbn13_check_digit_test ( )
  isbn13_is_valid_test ( )
  s_to_digits_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'isbn13_code_test():' )
  print ( '  Normal end of execution.' )

  return

def isbn13_check_digit ( s ):

#*****************************************************************************80
#
## isbn13_check_digit_calculate() determines the check digit for an ISBN13.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string S, a string.  Dashes and spaces and other
#    nonnumeric data is ignored, but at least 13 digits are expected, and only
#    the first 12 digits will be examined.
#
#  Output:
#
#    character ISBN_CHECK_DIGIT, the ISBN13 
#    check digit that should be appended to form the full 13 digit ISBN.
#

#
#  Extract the first 12 numeric digits from character string.
#
  n = 12
  dvec = s_to_digits ( s, n )
#
#  Compute the check digit.
#  Coefficient S alternates between 1 and 3.
#
  d = 10
  s = 1
  for i in range ( 0, n ):
    d = d - s * dvec[i]
    s = 4 - s

  d = ( d % 10 )
#
#  Convert digits 0 through 9 to characters '0' through '9'.
#  C represents the 13-th digit in the ISBN13 string.
#
  c = str ( d )

  return c

def isbn13_check_digit_test ( ):

#*****************************************************************************80
#
## isbn13_check_digit_test() tests isbn13_check_digit_().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 May 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'isbn13_check_digit_test():' )
  print ( '  isbn13_check_digit() calculates the 13-th digit' )
  print ( '  (the check digit) of a 13-digit ISBN.' )
  print ( '' )
#
#  Supply the full code, with dashes.
#
  s1 = '978-0-306-40615-2?'
  c1 = '7'
  c2 = isbn13_check_digit ( s1 )
  print ( '  Check digit of "' + s1 + '" is "' + c2 + '", expecting "' + c1 + '"' )
#
#  Supply a partial code, with spaces.
#
  s1 = '978 0 8493 9640?'
  c1 = '3'
  c2 = isbn13_check_digit ( s1 )
  print ( '  Check digit of "' + s1 + '" is "' + c2 + '", expecting "' + c1 + '"' )
#
#  Supply a partial code, no spaces.
#
  s1 = '978158488059?'
  c1 = '2'
  c2 = isbn13_check_digit ( s1 )
  print ( '  Check digit of "' + s1 + '" is "' + c2 + '", expecting "' + c1 + '"' )
#
#  Supply a partial code, no spaces.
#
  s1 = '978246897531?'
  c1 = '1'
  c2 = isbn13_check_digit ( s1 )
  print ( '  Check digit of "' + s1 + '" is "' + c2 + '", expecting "' + c1 + '"' )
#
#  Supply a partial code, no spaces.
#
  s1 = '978135798642?'
  c1 = '1'
  c2 = isbn13_check_digit ( s1 )
  print ( '  Check digit of "' + s1 + '" is "' + c2 + '", expecting "' + c1 + '"' )

  return

def isbn13_is_valid ( s ):

#*****************************************************************************80
#
## isbn13_is_valid() reports whether an ISBN13 is valid.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string S, a string containing 13 digits.
#    Dashes and other characters will be ignored.
#
#  Output:
#
#    logical VALUE: true if the string is a valid ISBN13 code.
#

#
#  Compute the ISBN13 check digit and convert it to a digit.
#
  c1 = isbn13_check_digit ( s )
  d1 = ord ( c1 ) - ord ( '0' )
#
#  Retrieve the first 13 digits in the string.
#
  n = 13
  dvec = s_to_digits ( s, n )
#
#  Compare the check digit to the 13th digit in string.
#
  d2 = dvec[n-1]

  value = ( d1 == d2 )

  return value

def isbn13_is_valid_test ( ):

#*****************************************************************************80
#
## isbn13_is_valid_test() tests isbn13_is_valid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2026
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'isbn13_is_valid_test():' )
  print ( '  isbn13_is_valid() reports whether an ISBN13 is valid.' )
  print ( '' )
#
#  Supply a valid code, with dashes.
#
  s1 = '978-0-306-40615-7'
  value1 = True
  value2 = isbn13_is_valid ( s1 )
  print ( '  Validity of "' + s1 + '" is ', value2, ', expecting ', value1 )
#
#  Modify one digit.
#
  s1 = '978-0-326-80615-7'
  value1 = False
  value2 = isbn13_is_valid ( s1 )
  print ( '  Validity of "' + s1 + '" is ', value2, ', expecting ', value1 )
#
#  Supply a valid code, with spaces.
#
  s1 = '978 0 8493 9640 3'
  value1 = True
  value2 = isbn13_is_valid ( s1 )
  print ( '  Validity of "' + s1 + '" is ', value2, ', expecting ', value1 )
#
#  Modify the check digit.
#
  s1 = '978 0 8493 9640 9'
  value1 = False
  value2 = isbn13_is_valid ( s1 )
  print ( '  Validity of "' + s1 + '" is ', value2, ', expecting ', value1 )
#
#  Supply a valid code, with final digit '0'.
#
  s1 = '978-0-3878-9654-0'
  value1 = True
  value2 = isbn13_is_valid ( s1 )
  print ( '  Validity of "' + s1 + '" is ', value2, ', expecting ', value1 )

  return

def s_to_digits ( s, n ):

#*****************************************************************************80
#
## s_to_digits() extracts N digits from a string.
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
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    09 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string S, the string.
#
#    integer N, the number of digits to extract.
#
#  Output:
#
#    integer DVEC(N), the extracted digits.
#
  import numpy as np

  s_len = len ( s )

  s_pos = 0
  d_pos = 0

  dvec = np.zeros ( n, dtype = np.int32 )

  while ( d_pos < n ):

    if ( s_len <= s_pos ):
      print ( '' )
      print ( 's_to_digits(): Fatal error!' )
      print ( '  Could not read enough data from string.' )
      raise Exception ( 's_to_digits(): Fatal error!' );

    c = s[s_pos]
    s_pos = s_pos + 1

    if ( '0' <= c and c <= '9' ):
      d = ord ( c ) - ord ( '0' )
      dvec[d_pos] = d
      d_pos = d_pos + 1

  return dvec

def s_to_digits_test ( ):

#*****************************************************************************80
#
## s_to_digits_test() tests s_to_digits().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 September 2015
#
#  Author:
#
#    John Burkardt
#
  import pprint

  print ( '' )
  print ( 's_to_digits_test():' )
  print ( '  s_to_digits() converts string to digit vector' )
  
  s = '34E94-70.6'
  print ( '' )
  print ( '  Test string: "' + s + '"' )
  n = 5
  dvec = s_to_digits ( s, n )
  print ( '  Extracted 5 digits' )
  pprint.pprint ( dvec )

  s = '34E94-70.6'
  print ( '' )
  print ( '  Test string: "' + s + '"' )
  n = 7
  dvec = s_to_digits ( s, n )
  print ( '  Extracted 7 digits' )
  pprint.pprint ( dvec )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  isbn13_code_test ( )
  timestamp ( )

