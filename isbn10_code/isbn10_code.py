#! /usr/bin/env python3
#
def isbn10_code_test ( ):

#*****************************************************************************80
#
## isbn10_code_test() tests isbn10_code().
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

  print ( '' )
  print ( 'isbn10_code_test():' )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  Test isbn10_code().' )

  ch_is_digit_test ( )
  ch_is_isbn_digit_test ( )
  ch_to_digit_test ( )
  i4_to_isbn_digit_test ( )
  isbn_check_digit_calculate_test ( )
  isbn_is_valid_test ( )
  isbn_digit_to_i4_test ( )
  s_to_digits_test ( )
  s_to_isbn_digits_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'isbn10_code_test():' )
  print ( '  Normal end of execution.' )
  return

def ch_is_digit ( c ):

#*****************************************************************************80
#
## ch_is_digit() returns TRUE if the character C is a digit.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character C, the character to be checked.
#
#  Output:
#
#    logical VALUE is TRUE if C is a decimal digit.
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
## ch_is_digit_test() tests ch_is_digit().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  c_test = np.array ( [ 
    '0', '1', '2', '3', '4', \
    '5', '6', '7', '8', '9', \
    'X', '?', ' ' ] )

  print ( '' )
  print ( 'ch_is_digit_test():' )
  print ( '  ch_is_digit() is TRUE if a character is a decimal digit.' )
  print ( '' )
 
  for i in range ( 0, 13 ):
    c = c_test[i]
    value = ch_is_digit ( c )
    print ( '  %8d  "%c"  %s' % ( i, c, value ) )

  return

def ch_is_isbn_digit ( c ):

#*****************************************************************************80
#
## ch_is_isbn_digit() returns TRUE if the character C is an ISBN digit.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character C, the character to be checked.
#
#  Output:
#
#    logical VALUE is TRUE if C is an ISBN digit.
#
  i0 = ord ( '0' )
  i9 = ord ( '9' )
  ic = ord ( c )

  if ( i0 <= ic and ic <= i9 ):

    value = True

  elif ( c == 'X' or c == 'x' ):

    value = True

  else:

    value = False

  return value

def ch_is_isbn_digit_test ( ):

#*****************************************************************************80
#
## ch_is_isbn_digit_test() tests ch_is_isbn_digit().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  c_test = np.array ( [ 
    '0', '1', '2', '3', '4', \
    '5', '6', '7', '8', '9', \
    'X', 'x', 'Y', '*', '?', \
    ' ' ] )

  print ( '' )
  print ( 'ch_is_isbn_digit_test():' )
  print ( '  ch_is_isbn_digit() is TRUE if a character is an ISBN digit.' )
  print ( '' )
 
  for i in range ( 0, 16 ):
    c = c_test[i]
    value = ch_is_isbn_digit ( c )
    print ( '  "%c"  %s' % ( c, value ) )

  return

def ch_to_digit ( c ):

#*****************************************************************************80
#
## ch_to_digit() returns the integer value of a base 10 digit.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character C: the decimal digit, '0' through '9' are legal.
#
#  Output:
#
#    integer DIGIT: the corresponding integer value.  If C was
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
## ch_to_digit_test() tests ch_to_digit().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  c_test = np.array ( [ 
    '0', '1', '2', '3', '4', \
    '5', '6', '7', '8', '9', \
    'X', '?', ' ' ] )

  print ( '' )
  print ( 'ch_to_digit_test():' )
  print ( '  ch_to_digit() converts a character to a decimal digit' )
  print ( '' )
 
  for i in range ( 0, 13 ):
    c = c_test[i]
    i2 = ch_to_digit ( c )
    print ( '  %8d  "%c"  %8d' % ( i, c, i2 ) )

  return

def i4_to_isbn_digit ( i ):

#*****************************************************************************80
#
## i4_to_isbn_digit() converts an integer to an ISBN digit.
#
#  Discussion:
#
#    Only the integers 0 through 10 can be input.  The representation
#    of 10 is 'X'.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, an integer between 0 and 10.
#
#  Output:
#
#    character VALUE, the ISBN character code of the integer.
#    If I is illegal, then VALUE is set to '?'.
#
  if ( i == 0 ):
    value = '0'
  elif ( i == 1 ):
    value = '1'
  elif ( i == 2 ):
    value = '2'
  elif ( i == 3 ):
    value = '3'
  elif ( i == 4 ):
    value = '4'
  elif ( i == 5 ):
    value = '5'
  elif ( i == 6 ):
    value = '6'
  elif ( i == 7 ):
    value = '7'
  elif ( i == 8 ):
    value = '8'
  elif ( i == 9 ):
    value = '9'
  elif ( i == 10 ):
    value = 'X'
  else:
    value = '?'

  return value

def i4_to_isbn_digit_test ( ):

#*****************************************************************************80
#
## i4_to_isbn_digit_test() tests i4_to_isbn_digit().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'i4_to_isbn_digit_test():' )
  print ( '  i4_to_isbn_digit() converts digits 0 to 10 to an ISBN digit.' )
  print ( '' )

  for i4 in range ( 0, 11 ):
    c = i4_to_isbn_digit ( i4 )
    print ( '  %8d     "%c"' % ( i4, c ) )

  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_print() prints an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def isbn_check_digit_calculate ( s ):

#*****************************************************************************80
#
## isbn_check_digit_calculate() determines the check digit for an ISBN.
#
#  Discussion:
#
#    ISBN stands for International Standard Book Number.  A unique ISBN
#    is assigned to each new book.  The ISBN includes 10 digits.  There is
#    an initial digit, then a dash, then a set of digits which are a
#    code for the publisher, another digit, and then the check digit:
#
#      initial-publisher-book-check
#
#    The number of digits used for the publisher and book codes can vary,
#    but the check digit is always one digit, and the total number of
#    digits is always 10.
#
#    The check digit is interesting, because it is a way of trying to
#    make sure that an ISBN has not been incorrectly copied.  Specifically,
#    if the ISBN is correct, then its ten digits will satisfy
#
#       10 * A + 9 * B + 8 * C + 7 * D + 6 * E
#      + 5 * F * 4 * G * 3 * H + 2 * I +     J  = 0 mod 11.
#
#    Here, we've taken 'A' to represent the first digit and 'J' the
#    last (which is the check digit).  In order for the code to work,
#    the value of J must be allowed to be anything from 0 to 10.  In
#    cases where J works out to be 10, the special digit 'X' is used.
#    An 'X' digit can only occur in this last check-digit position
#    on an ISBN.
#
#  Example:
#
#    S  => 0-8493-9640-?
#    D <=  9
#
#    meaning the ISBN is 0-8493-9640-9
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string S, a string.  Dashes and spaces and other
#    nonnumeric data is ignored, but at least 9 digits are expected, and only
#    the first 9 digits will be examined.
#
#  Output:
#
#    character isbn_check_digit_calculate, the ISBN 
#    check digit that should be appended to form the full 10 digit ISBN.
#

#
#  Extract first 9 digits.
#
  n = 9
  dvec = s_to_digits ( s, n )
#
#  Compute the check digit.
#
  d = 0
  for i in range ( 0, 9 ):
    d = d + ( 10 - i ) * dvec[i]

  d = ( ( 11 - ( d % 11 ) ) % 11 )
#
#  Convert digits 0 through 9, 10 to characters '0' through '9', 'X'.
#
  c = i4_to_isbn_digit ( d )

  return c

def isbn_check_digit_calculate_test ( ):

#*****************************************************************************80
#
## isbn_check_digit_calculate_test() tests isbn_check_digit_calculate().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'isbn_check_digit_calculate_test():' )
  print ( '  isbn_check_digit_calculate() calculates the 10-th digit' )
  print ( '  (the check digit) of a 10-digit ISBN.' )
  print ( '' )
#
#  Supply the full code, with dashes.
#
  s1 = '0-306-40615-2'
  c1 = '2'
  c2 = isbn_check_digit_calculate ( s1 )
  print ( '  Check digit of "%s" is "%c", expecting "%c"' % ( s1, c2, c1 ) )
#
#  Supply a partial code, with spaces.
#
  s1 = '0 8493 9640'
  c1 = '9'
  c2 = isbn_check_digit_calculate ( s1 )
  print ( '  Check digit of "%s" is "%c", expecting "%c"' % ( s1, c2, c1 ) )
#
#  Supply a partial code, no spaces.
#
  s1 = '158488059'
  c1 = '7'
  c2 = isbn_check_digit_calculate ( s1 )
  print ( '  Check digit of "%s" is "%c", expecting "%c"' % ( s1, c2, c1 ) )
#
#  Supply a partial code, no spaces.
#
  s1 = '246897531'
  c1 = '6'
  c2 = isbn_check_digit_calculate ( s1 )
  print ( '  Check digit of "%s" is "%c", expecting "%c"' % ( s1, c2, c1 ) )
#
#  Supply a partial code, no spaces.
#
  s1 = '135798642'
  c1 = '4'
  c2 = isbn_check_digit_calculate ( s1 )
  print ( '  Check digit of "%s" is "%c", expecting "%c"' % ( s1, c2, c1 ) )

  return

def isbn_digit_to_i4 ( c ):

#*****************************************************************************80
#
## isbn_digit_to_i4() converts an ISBN digit to an I4.
#
#  Discussion:
#
#    The characters '0' through '9' stand for themselves, but
#    the character 'X' or 'x' stands for 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character C, the ISBN character code to be converted.
#
#  Output:
#
#    integer VALUE, the numeric value of the character
#    code, between 0 and 10.  This value is returned as -1 if C is
#    not a valid character code.
#
  if ( c == '0' ):
    value = 0
  elif ( c == '1' ):
    value = 1
  elif ( c == '2' ):
    value = 2
  elif ( c == '3' ):
    value = 3
  elif ( c == '4' ):
    value = 4
  elif ( c == '5' ):
    value = 5
  elif ( c == '6' ):
    value = 6
  elif ( c == '7' ):
    value = 7
  elif ( c == '8' ):
    value = 8
  elif ( c == '9' ):
    value = 9
  elif ( c == 'X' or c == 'x' ):
    value = 10
  else:
    value = -1

  return value

def isbn_digit_to_i4_test ( ):

#*****************************************************************************80
#
## isbn_digit_to_i4_test() tests isbn_digit_to_i4().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  c_test = np.array ( [ \
    '0', '1', '2', '3', '4', \
    '5', '6', '7', '8', '9', \
    'X', 'x', 'Y', '*', '?', \
    ' ' ] )

  print ( '' )
  print ( 'isbn_digit_to_i4_test():' )
  print ( '  isbn_digit_to_i4() converts an ISBN digit to an I4' )
  print ( '' )

  for i in range ( 0, 16 ):
    c = c_test[i]
    i4 = isbn_digit_to_i4 ( c )
    print ( '  "%c"      %2d' % ( c, i4 ) )

  return

def isbn_is_valid ( s ):

#*****************************************************************************80
#
## isbn_is_valid() reports whether an ISBN is valid.
#
#  Discussion:
#
#    ISBN stands for International Standard Book Number.  A unique ISBN
#    is assigned to each new book.  The ISBN includes 10 digits.  There is
#    an initial digit, then a dash, then a set of digits which are a
#    code for the publisher, another digit, and then the check digit:
#
#      initial-publisher-book-check
#
#    The number of digits used for the publisher and book codes can vary,
#    but the check digit is always one digit, and the total number of
#    digits is always 10.
#
#    The check digit is interesting, because it is a way of trying to
#    make sure that an ISBN has not been incorrectly copied.  Specifically,
#    if the ISBN is correct, then its ten digits will satisfy
#
#       10 * A + 9 * B + 8 * C + 7 * D + 6 * E
#      + 5 * F * 4 * G * 3 * H + 2 * I +     J  = 0 mod 11.
#
#    Here, we've taken 'A' to represent the first digit and 'J' the
#    last (which is the check digit).  In order for the code to work,
#    the value of J must be allowed to be anything from 0 to 10.  In
#    cases where J works out to be 10, the special digit 'X' is used.
#    An 'X' digit can only occur in this last check-digit position
#    on an ISBN.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string S, a string containing 12 digits.
#    Dashes and other characters will be ignored.
#
#  Output:
#
#    bool VALUE, is TRUE if the string is valid.
#
  n = 10
  dvec = s_to_isbn_digits ( s, n )

  c1 = isbn_check_digit_calculate ( s )
  d1 = isbn_digit_to_i4 ( c1 )

  d2 = dvec[9]

  if ( d1 == d2 ):
    value = True
  else:
    value = False

  return value

def isbn_is_valid_test ( ):

#*****************************************************************************80
#
## isbn_is_valid_test() tests isbn_is_valid().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'isbn_is_valid_test():' )
  print ( '  isbn_is_valid() reports whether a ISBN is valid.' )
  print ( '' )
#
#  Supply a valid code, with dashes.
#
  s1 = '0-306-40615-2'
  value1 = True
  value2 = isbn_is_valid ( s1 )
  print ( '  Validity of "%s" is %s, expecting %s' % ( s1, value2, value1 ) )
#
#  Modify one digit.
#
  s1 = '0-326-40615-2'
  value1 = False
  value2 = isbn_is_valid ( s1 )
  print ( '  Validity of "%s" is %s, expecting %s' % ( s1, value2, value1 ) )
#
#  Supply a valid code, with spaces.
#
  s1 = '0 8493 9640 9';
  value1 = True
  value2 = isbn_is_valid ( s1 )
  print ( '  Validity of "%s" is %s, expecting %s' % ( s1, value2, value1 ) )
#
#  Modify the check digit.
#
  s1 = '0 8493 9640 3'
  value1 = False
  value2 = isbn_is_valid ( s1 )
  print ( '  Validity of "%s" is %s, expecting %s' % ( s1, value2, value1 ) )
#
#  Supply a valid code, with final digit 'X'.
#
  s1 = '0-3870-9654-X'
  value1 = True
  value2 = isbn_is_valid ( s1 )
  print ( '  Validity of "%s" is %s, expecting %s' % ( s1, value2, value1 ) )
#
#  Supply a valid code, with final digit 'x'.
#
  s1 = '0-201-38597-x'
  value1 = True
  value2 = isbn_is_valid ( s1 )
  print ( '  Validity of "%s" is %s, expecting %s' % ( s1, value2, value1 ) )

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

    if ( ch_is_digit ( c ) ):
      d = ch_to_digit ( c )
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
  print ( '' )
  print ( 's_to_digits_test():' )
  print ( '  s_to_digits() converts string to digit vector' )
  
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

  return

def s_to_isbn_digits ( s, n ):

#*****************************************************************************80
#
## s_to_isbn_digits() extracts N ISBN digits from a string.
#
#  Discussion:
#
#    The string may include spaces, letters, and dashes, but only the
#    digits '0' through '9' and 'X' will be extracted.
#
#  Example:
#
#    S  => 34E9X-70.6
#    N  => 5
#    D <=  (/ 3, 4, 9, 10, 7 /)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 September 2015
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
      print ( 's_to_isbn_digits(): Fatal error!' )
      print ( '  Could not read enough data from string.' )
      raise Exception ( 's_to_isbn_digits(): Fatal error!' );

    c = s[s_pos]
    s_pos = s_pos + 1

    if ( ch_is_isbn_digit ( c ) ):
      dvec[d_pos] = isbn_digit_to_i4 ( c )
      d_pos = d_pos + 1

  return dvec

def s_to_isbn_digits_test ( ):

#*****************************************************************************80
#
## s_to_isbn_digits_test() tests s_to_isbn_digits().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 's_to_isbn_digits_test():' )
  print ( '  s_to_isbn_digits() converts string to ISBN digit vector' )
  
  s = '34E9X-70.6'
  print ( '' )
  print ( '  Test string: "%s"' % ( s ) )
  n = 5
  dvec = s_to_isbn_digits ( s, n )
  i4vec_print ( n, dvec, '  Extracted 5 digits:' )

  s = '34E9X-70.6'
  print ( '' )
  print ( '  Test string: "%s"' % ( s ) )
  n = 7
  dvec = s_to_isbn_digits ( s, n )
  i4vec_print ( n, dvec, '  Extracted 7 digits:' )

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
  isbn10_code_test ( )
  timestamp ( )

