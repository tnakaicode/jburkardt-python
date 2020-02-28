#! /usr/bin/env python3
#
def ch_cap ( c ):

#*****************************************************************************80
#
## CH_CAP capitalizes a single character.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, character C, the character to capitalize.
#
#    Output, character C2, the capitalized character.
#
  i = ord ( c )

  if ( ord ( 'a' ) <= i and i <= ord ( 'z' ) ):
    i2 = i + ord ( 'A' ) - ord ( 'a' )
    c2 = chr ( i2 )
  else:
    c2 = c

  return c2

def ch_cap_test ( ):

#*****************************************************************************80
#
## CH_CAP_TEST tests CH_CAP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CH_CAP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CH_CAP uppercases a character.' )

  print ( '' )
  print ( '  C  CH_CAP(C)' )
  print ( '' )

  c = 'F'
  c2 = ch_cap ( c )
  print ( '  %c      %c' % ( c, c2 ) )
  c = 'f'
  c2 = ch_cap ( c )
  print ( '  %c      %c' % ( c, c2 ) )
  c = '1'
  c2 = ch_cap ( c )
  print ( '  %c      %c' % ( c, c2 ) )
  c = 'b'
  c2 = ch_cap ( c )
  print ( '  %c      %c' % ( c, c2 ) )
  c = '&'
  c2 = ch_cap ( c )
  print ( '  %c      %c' % ( c, c2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CH_CAP_TEST:' )
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

def chrpak_test ( ):

#*****************************************************************************80
#
## CHRPAK_TEST tests the CHRPAK library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CHRPAK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the CHRPAK library.' )

  ch_cap_test ( )
  ch_is_digit_test ( )
  ch_is_isbn_digit_test ( )
  ch_to_digit_test ( )
  ch_to_rot13_test ( )

  digit_to_ch_test ( )

  i4_length_test ( )
  i4_to_isbn_digit_test ( )
  i4_uniform_ab_test ( )

  i4vec_print_test ( )

  isbn_digit_to_i4_test ( )

  rat_to_s_test ( )

  s_digits_count_test ( )
  s_len_trim_test ( )
  s_quote_test ( )
  s_to_caesar_test ( )
  s_to_digits_test ( )
  s_to_isbn_digits_test ( )
  s_to_rot13_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHRPAK_TEST:' )
  print ( '  Normal end of execution.' )
  print ( '' )
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

def ch_to_rot13 ( ch ):

#*****************************************************************************80
#
## CH_TO_ROT13 converts a character to its ROT13 equivalent.
#
#  Discussion:
#
#    Two applications of CH_TO_ROT13 to a character will return the original.!
#
#    As a further scrambling, digits are similarly rotated using
#    a "ROT5" scheme.
#
#  Example:
#
#    Input:  Output:
#
#    a       n
#    C       P
#    J       W
#    1       6
#    5       0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, character CH, the character to be converted.
#
#    Output, character VALUE, the ROT13 equivalent of the character.
#
  i = ord ( ch )
#
#  [0:4] -> [5:9]
#
  if ( 48 <= i and i <= 52 ):
    value = i + 5
#
#  [5:9] -> [0:4]
#
  elif ( 53 <= i and i <= 57 ):
    value = i - 5
#
#  [A:M] -> [N:Z]
#
  elif ( 65 <= i and i <= 77 ):
    value = i + 13
#
#  [N:Z] -> [A:M]
#
  elif ( 78 <= i and i <= 90 ):
    value = i - 13
#
#  [a:m] -> [n:z]
#
  elif ( 97 <= i and i <= 109 ):
    value = i + 13
#
#  [n:z] -> [a:m]
#
  elif ( 110 <= i and i <= 122 ):
    value = i - 13
  else:
    value = i
 
  value = chr ( value )

  return value

def ch_to_rot13_test ( ):

#*****************************************************************************80
#
## CH_TO_ROT13_TEST tests CH_TO_ROT13.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CH_TO_ROT13_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CH_TO_ROT13 "encodes" characters using ROT13' )
  print ( '  (and digits using ROT5).' )
  print ( '  A second application of the function returns the' )
  print ( '  original character.' )

  s1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  s1_length = len ( s1 )
  s2 = ''
  s3 = ''

  for i in range ( 0, s1_length ):
    s2 = s2 + ch_to_rot13 ( s1[i] )
    s3 = s3 + ch_to_rot13 ( s2[i] )

  print ( '' )
  print ( '            CH  : %s' % ( s1 ) )
  print ( '      ROT13(CH) : %s' % ( s2 ) )
  print ( 'ROT13(ROT13(CH)): %s' % ( s3 ) )

  s1 = 'CH_TO_ROT13 "encodes" characters using ROT13'
  s1_length = len ( s1 )
  s2 = ''
  s3 = ''

  for i in range ( 0, s1_length ):
    s2 = s2 + ch_to_rot13 ( s1[i] )
    s3 = s3 + ch_to_rot13 ( s2[i] )

  print ( '' )
  print ( '            CH  : %s' % ( s1 ) )
  print ( '      ROT13(CH) : %s' % ( s2 ) )
  print ( 'ROT13(ROT13(CH)): %s' % ( s3 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CH_TO_ROT13_TEST:' )
  print ( '  Normal end of execution.' )
  return

def digit_to_ch ( digit ):

#*****************************************************************************80
#
## DIGIT_TO_CH returns the character representation of a decimal digit.
#
#  Example:
#
#    DIGIT   C
#    -----  ---
#      0    '0'
#      1    '1'
#    ...    ...
#      9    '9'
#     17    '*'
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
#    Input, integer DIGIT, the digit value between 0 and 9.
#
#    Output, character C, the corresponding character, or '*' if DIGIT
#    was illegal.
#
  if ( 0 <= digit and digit <= 9 ):
    i0 = ord ( '0' )
    c = chr ( i0 + digit )
  else:
    c = '*'

  return c

def digit_to_ch_test ( ):

#*****************************************************************************80
#
## DIGIT_TO_CH_TEST tests DIGIT_TO_CH.
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
  import platform

  print ( '' )
  print ( 'DIGIT_TO_CH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DIGIT_TO_CH: decimal digit -> character.' )
  print ( '' )
 
  for i in range ( -2, 12 ):
    c = digit_to_ch ( i )
    i2 = ch_to_digit ( c )
    print ( '  %8d  "%c"  %8d' % ( i, c, i2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DIGIT_TO_CH_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4_length ( i4 ):

#*****************************************************************************80
#
## I4_LENGTH computes the number of characters needed to print an I4.
#
#  Example:
#
#        I4    I4_LENGTH
#
#         0       1
#         1       1
#        -1       2
#      1952       4
#    123456       6
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the integer whose length is desired.
#
#    Output, integer VALUE, the number of characters required
#    to print the integer.
#

#
#  Ensure that I4 is an integer.
#
  i4 = int ( i4 )

  if ( i4 < 0 ):
    value = 1
    i4 = - i4
  elif ( i4 == 0 ):
    value = 1
    return value
  else:
    value = 0

  while ( i4 != 0 ):
    value = value + 1
    i4 = ( i4 // 10 )

  return value

def i4_length_test ( ):

#*****************************************************************************80
#
## I4_LENGTH_TEST tests I4_LENGTH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 6

  i4_test = np.array ( [ 0, 1, -1, 140, -1952, 123456 ], dtype = np.int32 )

  print ( '' )
  print ( 'I4_LENGTH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_LENGTH computes an integer\'s "length".' )
  print ( '' )
  print ( '        I4    Length' )
  print ( '' )

  for test in range ( 0, test_num ):

    i4 = i4_test[test]

    j4 = i4_length ( i4 )

    print ( '  %8d  %8d' % ( i4, j4 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_LENGTH_TEST:' )
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

def rat_to_s ( a, b ):

#*****************************************************************************80
#
## RAT_TO_S returns a left-justified representation of A/B.
#
#  Discussion:
#
#    If the ratio is negative, a minus sign precedes A.
#    A slash separates A and B.
#
#    Note that if A is nonzero and B is 0, S will
#    be returned as "Inf" or "-Inf" (Infinity), and if both
#    A and B are zero, S will be returned as "NaN"
#    (Not-a-Number).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, B, the numerator and denominator.
#
#    Output, character S(*), a left-justified string
#    containing the representation of A/B.
#

#
#  Take care of simple cases right away.
#
  if ( a == 0 ):

    if ( b != 0 ):
      s = '0'
    else:
      s = 'NaN'

  elif ( b == 0 ):

    if ( 0 < a ):
      s = 'Inf'
    else:
      s = '-Inf'

  else:

    s = str ( a ) + '/' + str ( b )

  return s

def rat_to_s_test ( ):

#*****************************************************************************80
#
#% RAT_TO_S_TEST tests RAT_TO_S.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'RAT_TO_S_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RAT_TO_S converts a rational to a string.' )

  rat_num = 7
  rat_top = np.array ( [ 3, 1,    20,  8, -10,   9, -11 ] )
  rat_bot = np.array ( [ 4, 1000,  1,  4,   7, -15, -11 ] )

  print ( '' )
  print ( '           A           B    A/B' )
  print ( '' )

  for i in range ( 0, rat_num ):
    a = rat_top[i]
    b = rat_bot[i]
    s = rat_to_s ( a, b )
    print ( '  %10d  %10d    %s' % ( a, b, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RAT_TO_S_TEST:' )
  print ( '  Normal end of execution.' )
  return

def s_digits_count ( s ):

#*****************************************************************************80
#
## S_DIGITS_COUNT counts the digits in a string.
#
#  Discussion:
#
#    The string may include spaces, letters, and dashes, but only the
#    digits 0 through 9 will be counted.
#
#  Example:
#
#    S  => 34E94-70.6
#    N <=  7
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
#    Output, integer N, the number of digits.
#
  s_len = len ( s )

  s_pos = 0
  n = 0

  while ( s_pos < s_len ):

    c = s[s_pos]
    s_pos = s_pos + 1

    if ( ch_is_digit ( c ) ):
      n = n + 1

  return n

def s_digits_count_test ( ):

#*****************************************************************************80
#
## S_DIGITS_COUNT_TEST tests S_DIGITS_COUNT.
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
  print ( 'S_DIGITS_COUNT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  S_DIGITS_COUNT counts the digits in a string.' )
  print ( '' )

  s = '34E94-70.6'
  n = s_digits_count ( s )
  print ( '  We count %d digits in "%s"' % ( n, s ) )

  s = 'Not a one!'
  n = s_digits_count ( s )
  print ( '  We count %d digits in "%s"' % ( n, s ) )

  s = '#8*k >>>> & SEVEN-0.3'
  n = s_digits_count ( s )
  print ( '  We count %d digits in "%s"' % ( n, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'S_DIGITS_COUNT_TEST' )
  print ( '  Normal end of execution.' )
  return

def s_len_trim ( s ):

#*****************************************************************************80
#
## S_LEN_TRIM returns the length of a character string to the last nonblank.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   03 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S, a string.
#
#    Output, integer LEN_TRIM, the length of the string to the last nonblank.
#
  n = len ( s )

  for i in range ( n - 1, -1, -1 ):
    if ( s[i] != ' ' ):
      value = i + 1
      return value

  value = 0
  return value

def s_len_trim_test ( ):

#*****************************************************************************80
#
## S_LEN_TRIM_TEST tests S_LEN_TRIM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'S_LEN_TRIM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  S_LEN_TRIM returns the length of string to the last nonblank.' )
  print ( '' )
  print ( '  LEN  S_LEN_TRIM  ---------S---------' )
  print ( '' )

  s = 'Hi, Bob!'
  l1 = len ( s )
  l2 = s_len_trim ( s )
  print ( '   %2d          %2d  "%s"' % ( l1, l2, s[0:l1] ) )

  s = '  How   are   you?     '
  l1 = len ( s )
  l2 = s_len_trim ( s )
  print ( '   %2d          %2d  "%s"' % ( l1, l2, s[0:l1] ) )

  s = '    '
  l1 = len ( s )
  l2 = s_len_trim ( s )
  print ( '   %2d          %2d  "%s"' % ( l1, l2, s[0:l1] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'S_LEN_TRIM_TEST' )
  print ( '  Normal end of execution.' )
  return

def s_quote ( s1, mark ):

#*****************************************************************************80
#
## S_QUOTE "quotes" a string.
#
#  Discussion:
#
#    Actually, it simply puts the string MARK before and after the string S1.
#
#    Sometimes, when you print a string, you want to put quote marks around it.
#    This is one way to do that.
#
#  Examples:
#
#    S1        MARK  S2
#    --------  ----  ----------
#    Hi, Bob!  "     "Hi, Bob!"
#    De        Loop  LoopDeLoop
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   30 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S1, a string to be "quoted".
#
#    Input, string MARK, the "quote mark".
#
#    Output, string S2, the "quoted" string.
#
  s2 = mark + s1 + mark

  return s2

def s_quote_test ( ):

#*****************************************************************************80
#
## S_QUOTE_TEST tests S_QUOTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'S_QUOTE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  S_QUOTE quotes a string S1 with a mark MARK.' )
  print ( '' )
  print ( '  ----S1----  ---MARK---  ----S2----' )
  print ( '' )

  s1 = 'Hi, Bob!'
  mark = '"'
  s2 = s_quote ( s1, mark )
  print ( '  %-10s  %-10s  %-10s' % ( s1, mark, s2 ) )

  s1 = 'De'
  mark = 'Loop'
  s2 = s_quote ( s1, mark )
  print ( '  %-10s  %-10s  %-10s' % ( s1, mark, s2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'S_QUOTE_TEST' )
  print ( '  Normal end of execution.' )
  return

def s_to_caesar ( s1, k ):

#*****************************************************************************80
#
## S_TO_CAESAR applies a Caesar shift cipher to a string.
#
#  Discussion:
#
#    The Caesar shift cipher incremented each letter by 1, with Z going to A.
#
#    This function can apply a Caesar shift cipher to a string of characters,
#    using an arbitrary shift K, which can be positive, negative or zero.
#
#    Letters A through Z will be shifted by K, mod 26.
#    Letters a through z will be shifted by K, mod 26.
#    Non-alphabetic characters are unchanged.
#
#    s2 = s_to_caesar ( s1, 1 ) will apply the traditional Caesar cipher.
#    s3 = s_to_caesar ( s2, -1 ) will decipher the result.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S1, a string of characters.
#
#    Input, integer K, the increment.
#
#    Output, string S2, the string of enciphered characters.
#
  iacap = ord ( 'A' )
  ialow = ord ( 'a' )

  s1_length = len ( s1 )
  s2 = ''

  for i in range ( 0, s1_length ):

    i1 = ord ( s1[i] )

    if ( iacap <= i1 and i1 <= iacap + 25 ):
      i2 = ( ( i1 + k - iacap ) % 26 ) + iacap
      s2 = s2 + chr ( i2 )
    elif ( ialow <= i1 and i1 <= ialow + 25 ):
      i2 = ( ( i1 + k - ialow ) % 26 ) + ialow
      s2 = s2 + chr ( i2 )
    else:
      s2 = s2 + s1[i]
  
  return s2

def s_to_caesar_test ( ):

#*****************************************************************************80
#
## S_TO_CAESAR_TEST tests the S_TO_CAESAR library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'S_TO_CAESAR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  S_TO_CAESAR applies a Caesar shift cipher to a string.' )

  print ( '' )
  print ( '  S2 = S_TO_CAESAR ( S1, K ), varying K.' )
  print ( '' )
  print ( '   K  ---------------S1----------------  ---------------S2----------------' )
  print ( '' )
  for k in range ( -5, 6 ):
    s1 = 'A man, a plan, a canal: Panama!'
    s2 = s_to_caesar ( s1, k )
    print ( '  %2d  "%s"  "%s"' % ( k, s1, s2 ) )

  print ( '' )
  print ( '  S2 = S_TO_CAESAR ( S1,  K ).' )
  print ( '  S3 = S_TO_CAESAR ( S2, -K )' )
  print ( '' )
  print ( '   K  ------------S1------------  ------------S2------------  ------------S3------------' )
  print ( '' )
  for k in range ( -5, 6 ):
    s1 = 'The key is under the mat'
    s2 = s_to_caesar ( s1, k )
    s3 = s_to_caesar ( s2, -k )
    print ( '  %2d  "%s"  "%s"  "%s"' % ( k, s1, s2, s3 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'S_TO_CAESAR_TEST:' )
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

def s_to_rot13 ( s1 ):

#*****************************************************************************80
#
## S_TO_ROT13 "rotates" the alphabetical characters in a string by 13 positions.
#
#  Discussion:
#
#    Two applications of the routine will return the original string.
#
#  Examples:
#
#    Input:                      Output:
#
#    abcdefghijklmnopqrstuvwxyz  nopqrstuvwxyzabcdefghijklm
#    Cher                        Pure
#    James Thurston Howell       Wnzrf Guhefgba Ubjryy
#    0123456789                  56789012345
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   30 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string S1, a string to be "rotated".
#
#    Output, string S2, the rotated string.
#
  s1_length = len ( s1 )
  s2 = ''

  for i in range ( 0, s1_length ):
    s2 = s2 + ch_to_rot13 ( s1[i] )
 
  return s2

def s_to_rot13_test ( ):

#*****************************************************************************80
#
## S_TO_ROT13_TEST tests S_TO_ROT13.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'S_TO_ROT13_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  S_TO_ROT13 applies the ROT13 cipher to a string.' )

  print ( '' )
  print ( '  S2 = S_TO_ROT13 ( S1 ).' )
  print ( '' )
  print ( '  -------------------S1-------------------  -------------------S2-------------------' )
  print ( '' )

  s1 = 'abcdefghijklmnopqrstuvwxyz'
  s2 = s_to_rot13 ( s1 )
  s1 = s_quote ( s1, '"' )
  s2 = s_quote ( s2, '"' )
  print ( '  %-40s  %-40s' % ( s1, s2 ) )

  s1 = 'Cher'
  s2 = s_to_rot13 ( s1 )
  s1 = s_quote ( s1, '"' )
  s2 = s_quote ( s2, '"' )
  print ( '  %-40s  %-40s' % ( s1, s2 ) )

  s1 = 'James Thurston Howell III'
  s2 = s_to_rot13 ( s1 )
  s1 = s_quote ( s1, '"' )
  s2 = s_quote ( s2, '"' )
  print ( '  %-40s  %-40s' % ( s1, s2 ) )

  s1 = 'The bill is $1,205,837.49 so pay now!'
  s2 = s_to_rot13 ( s1 )
  s1 = s_quote ( s1, '"' )
  s2 = s_quote ( s2, '"' )
  print ( '  %-40s  %-40s' % ( s1, s2 ) )

  print ( '' )
  print ( '  S2 = S_TO_ROT13 ( S1 ).' )
  print ( '  S3 = S_TO_ROT13 ( S2 ).' )
  print ( '' )
  print ( '  -------------------S1-------------------  -------------------S3-------------------' )
  print ( '' )

  s1 = 'abcdefghijklmnopqrstuvwxyz'
  s2 = s_to_rot13 ( s1 )
  s3 = s_to_rot13 ( s2 )
  s1 = s_quote ( s1, '"' )
  s3 = s_quote ( s3, '"' )
  print ( '  %-40s  %-40s' % ( s1, s3 ) )

  s1 = 'Cher'
  s2 = s_to_rot13 ( s1 )
  s3 = s_to_rot13 ( s2 )
  s1 = s_quote ( s1, '"' )
  s3 = s_quote ( s3, '"' )
  print ( '  %-40s  %-40s' % ( s1, s3 ) )

  s1 = 'James Thurston Howell III'
  s2 = s_to_rot13 ( s1 )
  s3 = s_to_rot13 ( s2 )
  s1 = s_quote ( s1, '"' )
  s3 = s_quote ( s3, '"' )
  print ( '  %-40s  %-40s' % ( s1, s3 ) )

  s1 = 'The bill is $1,205,837.49 so pay now!'
  s2 = s_to_rot13 ( s1 )
  s3 = s_to_rot13 ( s2 )
  s1 = s_quote ( s1, '"' )
  s3 = s_quote ( s3, '"' )
  print ( '  %-40s  %-40s' % ( s1, s3 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'S_TO_ROT13_TEST:' )
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
  chrpak_test ( )
  timestamp ( )

