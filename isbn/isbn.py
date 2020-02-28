#! /usr/bin/env python3
#
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

def ch_is_isbn_digit ( c ):

#*****************************************************************************80
#
## CH_IS_ISBN_DIGIT returns TRUE if the character C is an ISBN digit.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, character C, the character to be checked.
#
#    Output, logical VALUE is TRUE if C is an ISBN digit.
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
## CH_IS_ISBN_DIGIT_TEST tests CH_IS_ISBN_DIGIT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  c_test = np.array ( [ 
    '0', '1', '2', '3', '4', \
    '5', '6', '7', '8', '9', \
    'X', 'x', 'Y', '*', '?', \
    ' ' ] )

  print ( '' )
  print ( 'CH_IS_ISBN_DIGIT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CH_IS_ISBN_DIGIT is TRUE if a character is an ISBN digit.' )
  print ( '' )
 
  for i in range ( 0, 16 ):
    c = c_test[i]
    value = ch_is_isbn_digit ( c )
    print ( '  "%c"  %s' % ( c, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CH_IS_ISBN_DIGIT_TEST:' )
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

def i4_to_isbn_digit ( i ):

#*****************************************************************************80
#
## I4_TO_ISBN_DIGIT converts an integer to an ISBN digit.
#
#  Discussion:
#
#    Only the integers 0 through 10 can be input.  The representation
#    of 10 is 'X'.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, an integer between 0 and 10.
#
#    Output, character VALUE, the ISBN character code of the integer.
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
## I4_TO_ISBN_DIGIT_TEST tests I4_TO_ISBN_DIGIT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4_TO_ISBN_DIGIT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_TO_ISBN_DIGIT converts digits 0 to 10 to an ISBN digit.' )
  print ( '' )

  for i4 in range ( 0, 11 ):
    c = i4_to_isbn_digit ( i4 )
    print ( '  %8d     "%c"' % ( i4, c ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_TO_ISBN_DIGIT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## I4_UNIFORM_AB returns a scaled pseudorandom I4.
#
#  Discussion:
#
#    The pseudorandom number will be scaled to be uniformly distributed
#    between A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer A, B, the minimum and maximum acceptable values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer C, the randomly chosen integer.
#
#    Output, integer SEED, the updated seed.
#
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge; 

  if ( seed == 0 ):
    print ( '' )
    print ( 'I4_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'I4_UNIFORM_AB - Fatal error!' )

  k = floor ( seed / 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
  a = round ( a )
  b = round ( b )

  r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
    +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
  value = round ( r )

  value = max ( value, min ( a, b ) )
  value = min ( value, max ( a, b ) )
  value = int ( value )

  return value, seed

def i4_uniform_ab_test ( ):

#*****************************************************************************80
#
## I4_UNIFORM_AB_TEST tests I4_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  a = -100
  b = 200
  seed = 123456789

  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_UNIFORM_AB computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  for i in range ( 1, 21 ):
    [ j, seed ] = i4_uniform_ab ( a, b, seed )
    print ( '  %8d  %8d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST:' )
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

def isbn_check_digit_calculate ( s ):

#*****************************************************************************80
#
## ISBN_CHECK_DIGIT_CALCULATE determines the check digit for an ISBN.
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
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S, a string.  Dashes and spaces and other
#    nonnumeric data is ignored, but at least 9 digits are expected, and only
#    the first 9 digits will be examined.
#
#    Output, character ISBN_CHECK_DIGIT_CALCULATE, the ISBN 
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
## ISBN_CHECK_DIGIT_CALCULATE_TEST tests ISBN_CHECK_DIGIT_CALCULATE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ISBN_CHECK_DIGIT_CALCULATE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ISBN_CHECK_DIGIT_CALCULATE calculates the 10-th digit' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'ISBN_CHECK_DIGIT_CALCULATE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def isbn_digit_to_i4 ( c ):

#*****************************************************************************80
#
## ISBN_DIGIT_TO_I4 converts an ISBN digit to an I4.
#
#  Discussion:
#
#    The characters '0' through '9' stand for themselves, but
#    the character 'X' or 'x' stands for 10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, character C, the ISBN character code to be converted.
#
#    Output, integer VALUE, the numeric value of the character
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
## ISBN_DIGIT_TO_I4_TEST tests ISBN_DIGIT_TO_I4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  c_test = np.array ( [ \
    '0', '1', '2', '3', '4', \
    '5', '6', '7', '8', '9', \
    'X', 'x', 'Y', '*', '?', \
    ' ' ] )

  print ( '' )
  print ( 'ISBN_DIGIT_TO_I4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ISBN_DIGIT_TO_I4 converts an ISBN digit to an I4' )
  print ( '' )

  for i in range ( 0, 16 ):
    c = c_test[i]
    i4 = isbn_digit_to_i4 ( c )
    print ( '  "%c"      %2d' % ( c, i4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ISBN_DIGIT_TO_I4_TEST:' )
  print ( '  Normal end of execution.' )
  return

def isbn_is_valid ( s ):

#*****************************************************************************80
#
## ISBN_IS_VALID reports whether an ISBN is valid.
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
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S, a string containing 12 digits.
#    Dashes and other characters will be ignored.
#
#    Output, bool VALUE, is TRUE if the string is valid.
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
## ISBN_IS_VALID_TEST tests ISBN_IS_VALID.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ISBN_IS_VALID_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ISBN_IS_VALID reports whether a ISBN is valid.' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'ISBN_IS_VALID_TEST:' )
  print ( '  Normal end of execution.' )
  return

def isbn_test ( ):

#*****************************************************************************80
#
## ISBN_TEST tests the ISBN library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ISBN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the ISBN library.' )

  ch_is_digit_test ( )
  ch_is_isbn_digit_test ( )
  ch_to_digit_test ( )
  i4_to_isbn_digit_test ( )
  i4vec_print_test ( )
  isbn_check_digit_calculate_test ( )
  isbn_is_valid_test ( )
  isbn_digit_to_i4_test ( )
  s_to_digits_test ( )
  s_to_isbn_digits_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ISBN_TEST:' )
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

def s_to_isbn_digits ( s, n ):

#*****************************************************************************80
#
## S_TO_ISBN_DIGITS extracts N ISBN digits from a string.
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
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 September 2015
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
      print ( 'S_TO_ISBN_DIGITS - Fatal error!' )
      print ( '  Could not read enough data from string.' )
      error ( 'S_TO_ISBN_DIGITS - Fatal error!' );

    c = s[s_pos]
    s_pos = s_pos + 1

    if ( ch_is_isbn_digit ( c ) ):
      dvec[d_pos] = isbn_digit_to_i4 ( c )
      d_pos = d_pos + 1

  return dvec

def s_to_isbn_digits_test ( ):

#*****************************************************************************80
#
## S_TO_ISBN_DIGITS_TEST tests S_TO_ISBN_DIGITS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'S_TO_ISBN_DIGITS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  S_TO_ISBN_DIGITS: string -> ISBN digit vector' )
  
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
#
#  Terminate.
#
  print ( '' )
  print ( 'S_TO_ISBN_DIGITS_TEST' )
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
  isbn_test ( )
  timestamp ( )

