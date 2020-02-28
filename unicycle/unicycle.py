#! /usr/bin/env python3
#
def i4_factorial ( n ) :

#*****************************************************************************80
#
## I4_FACTORIAL computes the factorial function.
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
#    Input, integer N, the argument.
#
#    Output, integer VALUE, the value of the factorial function.
#
  value = 1
  for i in range ( 1, n + 1 ):
    value = value * i

  return value

def i4_factorial_test ( ):

#*****************************************************************************80
#
## I4_FACTORIAL_TEST tests I4_FACTORIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    18 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4_FACTORIAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_FACTORIAL evaluates the factorial function.' )
  print ( '' )
  print ( '         N      Exact         I4_FACTORIAL(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, f1 = i4_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = i4_factorial ( n )

    print ( '  %8d  %12d  %12d' % ( n, f1, f2 ) ) 
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_FACTORIAL_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4_factorial_values ( n_data ):

#*****************************************************************************80
#
## I4_FACTORIAL_VALUES returns values of the factorial function.
#
#  Discussion:
#
#    0! = 1
#    I! = Product ( 1 <= J <= I ) I
#
#    In Mathematica, the function can be evaluated by:
#
#      n!
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, the argument of the function.
#
#    Output, integer FN, the value of the function.
#
  import numpy as np

  n_max = 13

  fn_vec = np.array ( [ \
            1, \
            1, \
            2, \
            6, \
           24, \
          120, \
          720, \
         5040, \
        40320, \
       362880, \
      3628800, \
     39916800, \
    479001600 ] )
  n_vec = np.array ( [ \
     0,  1,  2,  3, \
     4,  5,  6,  7, \
     8,  9, 10, 11, \
    12 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    fn = 0
  else:
    n = n_vec[n_data]
    fn = fn_vec[n_data]
    n_data = n_data + 1

  return n_data, n, fn

def i4_factorial_values_test ( ):

#*****************************************************************************80
#
## I4_FACTORIAL_VALUES_TEST tests I4_FACTORIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4_FACTORIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_FACTORIAL_VALUES returns values of the integer factorial function.' )
  print ( '' )
  print ( '          N          I4_FACTORIAL(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = i4_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8d  %12d' % ( n, fn ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_FACTORIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4_modp ( i, j ):

#*****************************************************************************80
#
## I4_MODP returns the nonnegative remainder of I4 division.
#
#  Discussion:
#
#    If
#      NREM = I4_MODP ( I, J )
#      NMULT = ( I - NREM ) / J
#    then
#      I = J * NMULT + NREM
#    where NREM is always nonnegative.
#
#    The MOD function computes a result with the same sign as the
#    quantity being divided.  Thus, suppose you had an angle A,
#    and you wanted to ensure that it was between 0 and 360.
#    Then mod(A,360) would do, if A was positive, but if A
#    was negative, your result would be between -360 and 0.
#
#    On the other hand, I4_MODP(A,360) is between 0 and 360, always.
#
#  Example:
#
#        I     J     MOD  I4_MODP    Factorization
#
#      107    50       7       7    107 =  2 *  50 + 7
#      107   -50       7       7    107 = -2 * -50 + 7
#     -107    50      -7      43   -107 = -3 *  50 + 43
#     -107   -50      -7      43   -107 =  3 * -50 + 43
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
#    Input, integer I, the number to be divided.
#
#    Input, integer J, the number that divides I.
#
#    Output, integer VALUE, the nonnegative remainder when I is
#    divided by J.
#
  from sys import exit

  if ( j == 0 ):
    print ( '' )
    print ( 'I4_MODP - Fatal error!' )
    print ( '  Illegal divisor J = %d' % ( j ) )
    exit ( 'I4_MODP - Fatal error!' )

  value = i % j

  if ( value < 0 ):
    value = value + abs ( j )

  return value

def i4_modp_test ( ):

#*****************************************************************************80
#
## I4_MODP_TEST tests I4_MODP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 4

  n_vec = np.array ( ( 107, 107, -107, -107 ) )
  d_vec = np.array ( ( 50, -50, 50, -50 ) )

  print ( '' )
  print ( 'I4_MODP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_MODP factors a number' )
  print ( '  into a multiple M and a positive remainder R.' )
  print ( '' )
  print ( '    Number   Divisor  Multiple Remainder' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    r = i4_modp ( n, d )
    m = ( n - r ) // d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )

  print ( '' )
  print ( '  Repeat using Python % Operator:' )
  print ( '' )

  for test in range ( 0, test_num ):
    n = n_vec[test]
    d = d_vec[test]
    m = n // d
    r = n % d
    print ( '  %8d  %8d  %8d  %8d' % ( n, d, m, r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_MODP_TEST' )
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
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge; 

  if ( seed == 0 ):
    print ( '' )
    print ( 'I4_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'I4_UNIFORM_AB - Fatal error!' )

  k = ( seed // 127773 )

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
    j, seed = i4_uniform_ab ( a, b, seed )
    print ( '  %8d  %8d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4vec_indicator1 ( n ):

#*****************************************************************************80
#
## I4VEC_INDICATOR1 sets an I4VEC to the indicator vector ( 1, 2, 3, ... ).
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
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
#  Parameters:
#
#    Input, integer N, the number of elements of the vector.
#
#    Output, integer A(N), the indicator array.
#
  import numpy as np

  a = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def i4vec_indicator1_test ( ):

#*****************************************************************************80
#
## I4VEC_INDICATOR1_TEST tests I4VEC_INDICATOR1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 November 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'I4VEC_INDICATOR1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_INDICATOR1 returns an indicator vector.' )

  n = 10
  a = i4vec_indicator1 ( n )
  i4vec_print ( n, a, '  The indicator1 vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_INDICATOR1_TEST' )
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

def i4vec_reverse ( n, a ):

#*****************************************************************************80
#
## I4VEC_REVERSE reverses the elements of an I4VEC.
#
#  Example:
#
#    Input:
#
#      N = 5,
#      A = ( 11, 12, 13, 14, 15 ).
#
#    Output:
#
#      A = ( 15, 14, 13, 12, 11 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 April 2005
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the array.
#
#    Input, integer A(N), the array to be reversed.
#
#    Output, integer A(N), the reversed array.
#
  for i in range ( 0, n // 2 ):
    j = n - i - 1
    t    = a[i]
    a[i] = a[j]
    a[j] = t

  return a

def i4vec_reverse_test ( ):

#*****************************************************************************80
#
## I4VEC_REVERSE_TEST tests I4VEC_REVERSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2009
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10
  b = 0
  c = 3 * n

  print ( '' )
  print ( 'I4VEC_REVERSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_REVERSE reverses a list of integers.' )

  seed = 123456789

  a, seed = i4vec_uniform_ab ( n, b, c, seed )

  i4vec_print ( n, a, '  Original vector:' )

  a = i4vec_reverse ( n, a )

  i4vec_print ( n, a, '  Reversed:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_REVERSE_TEST:' )
  print ( '  Normal end of execution.' )

  return

def i4vec_uniform_ab ( n, a, b, seed ):

#*****************************************************************************80
#
## I4VEC_UNIFORM_AB returns a scaled pseudorandom I4VEC.
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
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer A, B, the minimum and maximum acceptable values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer C(N), the randomly chosen integer vector.
#
#    Output, integer SEED, the updated seed.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed  )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'I4VEC_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'I4VEC_UNIFORM_AB - Fatal error!' )

  a = round ( a )
  b = round ( b )

  c = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    seed = ( seed % i4_huge )

    if ( seed < 0 ):
      seed = seed + i4_huge

    r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
    r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
      +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
    value = round ( r )

    value = max ( value, min ( a, b ) )
    value = min ( value, max ( a, b ) )

    c[i] = value

  return c, seed

def i4vec_uniform_ab_test ( ):

#*****************************************************************************80
#
## I4VEC_UNIFORM_AB_TEST tests I4VEC_UNIFORM_AB.
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

  n = 20
  a = -100
  b = 200
  seed = 123456789

  print ( '' )
  print ( 'I4VEC_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_UNIFORM_AB computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  v, seed = i4vec_uniform_ab ( n, a, b, seed )

  i4vec_print ( n, v, '  The random vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4_wrap ( ival, ilo, ihi ):

#*****************************************************************************80
#
## I4_WRAP forces an integer to lie between given limits by wrapping.
#
#  Example:
#
#    ILO = 4, IHI = 8
#
#    I   Value
#
#    -2     8
#    -1     4
#     0     5
#     1     6
#     2     7
#     3     8
#     4     4
#     5     5
#     6     6
#     7     7
#     8     8
#     9     4
#    10     5
#    11     6
#    12     7
#    13     8
#    14     4
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
#    Input, integer IVAL, an integer value.
#
#    Input, integer ILO, IHI, the desired bounds for the integer value.
#
#    Output, integer VALUE, a "wrapped" version of IVAL.
#
  jlo = min ( ilo, ihi )
  jhi = max ( ilo, ihi )

  wide = jhi - jlo + 1

  if ( wide == 1 ):
    value = jlo
  else:
    value = jlo + i4_modp ( ival - jlo, wide )

  return value

def i4_wrap_test ( ):

#*****************************************************************************80
#
## I4_WRAP_TEST tests I4_WRAP.
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
  import platform

  ilo = 4
  ihi = 8

  print ( '' )
  print ( 'I4_WRAP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_WRAP forces an integer to lie within given limits.' )
  print ( '' )
  print ( '  ILO = %d' % ( ilo ) )
  print ( '  IHI = %d' % ( ihi ) )
  print ( '' )
  print ( '     I  I4_WRAP(I)' )
  print ( '' )

  for i in range ( -10, 21 ):
    j = i4_wrap ( i, ilo, ihi )
    print ( '  %6d  %6d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_WRAP_TEST' )
  print ( '  Normal end of execution.' )
  return

def perm1_check ( n, p ):

#*****************************************************************************80
#
## PERM1_CHECK checks a permutation of (1,...,N).
#
#  Discussion:
#
#    The routine verifies that each of the integers from 1 to
#    to N occurs among the N entries of the permutation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries.
#
#    Input, integer P(N), the array to check.
#
#    Output, logical CHECK:
#    True if P is a legal permutation of (1,...,N).
#    False if P is not a legal permutation of (1,...,N).
#
  from sys import exit

  check = True

  for value in range ( 1, n + 1 ):

    check = False

    for location in range ( 0, n ):
      if ( p[location] == value ):
        check = True
        break

    if ( not check ):
#     print ( '' )
#     print ( 'PERM1_CHECK - Warning!' )
#     print ( '  Permutation is missing the value %d.' % ( value ) )
      return check

  return check

def perm1_check_test ( ):

#*****************************************************************************80
#
## PERM1_CHECK_TEST tests PERM1_CHECK.
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
  import numpy as np
  import platform

  n = 5
  p1 = np.array ( [ 5, 2, 3, 4, 1 ] )
  p2 = np.array ( [ 4, 1, 3, 0, 2 ] )
  p3 = np.array ( [ 0, 2, 1, 3, 2 ] )

  print ( '' )
  print ( 'PERM1_CHECK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM1_CHECK checks a permutation of 1,...,N.' )

  perm1_print ( n, p1, '  Permutation 1:' )
  check = perm1_check ( n, p1 )
  if ( check ):
    print ( '  This is a permutation.' )
  else:
    print ( '  This is not a permutation.' )

  perm1_print ( n, p2, '  Permutation 2:' )
  check = perm1_check ( n, p2 )
  if ( check ):
    print ( '  This is a permutation.' )
  else:
    print ( '  This is not a permutation.' )

  perm1_print ( n, p3, '  Permutation 3:' )
  check = perm1_check ( n, p3 )
  if ( check ):
    print ( '  This is a permutation.' )
  else:
    print ( '  This is not a permutation.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM1_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

def perm1_enum ( n ):

#*****************************************************************************80
#
## PERM1_ENUM enumerates the permutations on N digits.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of values being permuted.
#    N must be nonnegative.
#
#    Output, integer VALUE, the number of distinct elements.
#
  value = i4_factorial ( n )

  return value

def perm1_enum_test ( ):

#*****************************************************************************80
#
## PERM1_ENUM_TEST tests PERM1_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PERM1_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM1_ENUM enumerates the permutations of 1,...,N.' )
  print ( '' )
  print ( '         N      PERM1_ENUM' )
  print ( '' )

  for n in range ( 1, 11 ):

    value = perm1_enum ( n )

    print ( '  %8d  %12d' % ( n, value ) )   
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM1_ENUM_TEST' )
  print ( '  Normal end of execution.' )
  return

def perm1_inverse ( n, p ):

#*****************************************************************************80
#
#% PERM1_INVERSE computes the inverse of a 1-based permutation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N, the number of values being permuted.
#    N must be positive.
#
#    Input, integer P(N), describes the permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#    Output, integer P_INV(N), the inverse permutation.
#
  import numpy as np

  perm1_check ( n, p )

  p_inv = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    p_inv[p[i]-1] = i + 1

  return p_inv

def perm1_inverse_test ( ):

#*****************************************************************************80
#
## PERM1_INVERSE_TEST tests PERM1_INVERSE
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 7
  p1 = np.array ( [ 4, 3, 5, 1, 7, 6, 2 ] )

  print ( '' )
  print ( 'PERM1_INVERSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM1_INVERSE inverts a permutation of (1,...,N)' )

  perm1_print ( n, p1, '  The original permutation:' )
 
  p2 = perm1_inverse ( n, p1 )
 
  perm1_print ( n, p2, '  The inverted permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM1_INVERSE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def perm1_lex_next ( n, p, rank ):

#*****************************************************************************80
#
## PERM1_LEX_NEXT computes the lexicographic permutation successor.
#
#  Example:
#
#    RANK  Permutation
#
#       0  1 2 3 4
#       1  1 2 4 3
#       2  1 3 2 4
#       3  1 3 4 2
#       4  1 4 2 3
#       5  1 4 3 2
#       6  2 1 3 4
#       ...
#      23  4 3 2 1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N, the number of values being permuted.
#    N must be positive.
#
#    Input, integer P(N), the input permutation.
#
#    Input, integer RANK, the rank of the input permutation.
#    If RANK = -1, then the input permutation is ignored, and the
#    function returns the first permutation in the ordered list,
#    with RANK = 1.
#
#    Output, integer P(N), the successor permutation.  
#    If the input permutation was the last in the ordered list,
#    then the output permutation is the first permutation.
#
#    Output, integer RANK, the rank of the output permutation.
#

#
#  If RANK <= -1, return the first permutation.
#
  if ( rank <= -1 ):
    p = i4vec_indicator1 ( n )
    rank = 0
    return p, rank
#
#  Make sure the input permutation is legal.
#
  check = perm1_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM1_LEX_NEXT - Fatal error!' )
    print ( '  PERM1_CHECK failed.' )
    exit ( 'PERM1_LEX_NEXT - Fatal error!' )
#
#  Seek I, the highest index for which the next element is bigger.
#
  i = n - 2

  while ( True ):

    if ( i < 0 ):
      break

    if ( p[i] <= p[i+1] ):
      break

    i = i - 1
#
#  If no I could be found, then we have reach the final permutation,
#  N, N-1, ..., 2, 1.  Time to start over again.
#
  if ( i == -1 ):
    p = i4vec_indicator1 ( n )
    rank = -1
  else:
#
#  Otherwise, look for the the highest index after I whose element
#  is bigger than I's.  We know that I+1 is one such value, so the
#  loop will never fail.
#
    j = n - 1
    while ( p[j] < p[i] ): 
      j = j - 1
#
#  Interchange elements I and J.
#
    t    = p[i]
    p[i] = p[j]
    p[j] = t
#
#  Reverse the elements from I+1 to N-1.
#
    k_hi = ( n + i ) // 2

    for k in range ( i + 1, k_hi + 1 ):
      l = n + i - k
      t    = p[k]
      p[k] = p[l]
      p[l] = t

    rank = rank + 1

  return p, rank

def perm1_lex_next_test ( ):

#*****************************************************************************80
#
## PERM1_LEX_NEXT_TEST tests PERM1_LEX_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4

  print ( '' )
  print ( 'PERM1_LEX_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM1_LEX_NEXT generates 1-based permutations in lexicographic order.' )
  print ( '' )

  more = False
  p = np.zeros ( n, dtype = np.int32 )
  rank = -1

  while ( True ):

    p, rank = perm1_lex_next ( n, p, rank )

    if ( rank == -1 ):
      break

    print ( '  %2d:' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '  %2d' % ( p[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM1_LEX_NEXT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def perm1_lex_rank ( n, p ):

#*****************************************************************************80
#
## PERM1_LEX_RANK computes the lexicographic rank of a 1-based permutation.
#
#  Discussion:
#
#    The original code altered the input permutation.  
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N, the number of values being permuted.
#    N must be positive.
#
#    Input, integer P(N), describes the permutation.
#    P(I) is the item which is permuted into the I-th place
#    by the permutation.
#
#    Output, integer RANK, the rank of the permutation.
#
  import numpy as np
#
#  Check.
#
  check = perm1_check ( n, p )

  if ( not check ):
    print ( '' )
    print ( 'PERM1_LEX_RANK - Fatal error!' )
    print ( '  PERM1_CHECK failed!' )
    exit ( 'PERM1_LEX_RANK - Fatal error!' )

  rank = 0
  p2 = np.zeros ( n, dtype = np.int32 )
  for i in range ( 0, n ):
    p2[i] = p[i]

  for j in range ( 0, n ):

    rank = rank + ( p2[j] - 1 ) * i4_factorial ( n - j - 1 )

    for i in range ( j + 1, n ):
      if ( p2[j] < p2[i] ):
        p2[i] = p2[i] - 1

  return rank

def perm1_lex_rank_test ( ):

#*****************************************************************************80
#
## PERM1_LEX_RANK_TEST tests PERM1_LEX_RANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'PERM1_LEX_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM1_LEX_RANK returns the lexicographic rank of' )
  print ( '  a permutation of (1,...,N).' )

  n = 4
  p = np.array ( [ 4, 1, 3, 2 ] )
  perm1_print ( n, p, '  A 1-based permutation:' )
  rank = perm1_lex_rank ( n, p )

  print ( '' )
  print ( '  Rank = %d' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM1_LEX_RANK_TEST' )
  print ( '  Normal end of execution.' )
  return

def perm1_lex_unrank ( n, rank ):

#*****************************************************************************80
#
## PERM1_LEX_UNRANK computes the 1-based permutation of given lexicographic rank.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Parameters:
#
#    Input, integer N, the number of values being permuted.
#    N must be positive.
#
#    Input, integer RANK, the rank of the permutation.
#
#    Output, integer P(N), describes the permutation.
#
  import numpy as np
  from sys import exit
#
#  Check.
#
  if ( n < 1 ):
    print ( '' )
    print ( 'PERM1_LEX_UNRANK - Fatal error!' )
    print ( '  Input N is illegal.' )
    exit ( 'PERM1_LEX_UNRANK - Fatal error!' )

  nperm = perm1_enum ( n )

  if ( rank < 0 or nperm < rank ):
    print ( '' )
    print ( 'PERM1_LEX_UNRANK - Fatal error!' )
    print ( '  The input rank is illegal.' )
    exit ( 'PERM1_LEX_UNRANK - Fatal error!' )
 
  p = np.zeros ( n, dtype = np.int32 )

  p[n-1] = 1

  for j in range ( 1, n ):

    d = ( rank % i4_factorial ( j + 1 ) ) // i4_factorial ( j )
    rank = rank - d * i4_factorial ( j )
    p[n-j-1] = d + 1

    for i in range ( n - j + 1, n + 1 ):

      if ( d < p[i-1] ):
        p[i-1] = p[i-1] + 1

  return p

def perm1_lex_unrank_test ( ):

#*****************************************************************************80
#
## PERM1_LEX_UNRANK_TEST tests PERM1_LEX_UNRANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'PERM1_LEX_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM1_LEX_UNRANK returns the 1-based permutation' )
  print ( '  of given lexicographic rank.' )

  n = 4
  n_perm = perm1_enum ( n )

  seed = 123456789
  rank, seed = i4_uniform_ab ( 0, n_perm, seed )

  print ( '' )
  print ( '  Rank = %d' % ( rank ) )

  p = perm1_lex_unrank ( n, rank )
  perm1_print ( n, p, '  The corresponding permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM1_LEX_UNRANK_TEST' )
  print ( '  Normal end of execution.' )
  return

def perm1_print ( n, p, title ):

#*****************************************************************************80
#
## PERM1_PRINT prints a permutation of (1,...,N).
#
#  Example:
#
#    Input:
#
#      P = 7 2 4 1 5 3 6
#
#    Printed output:
#
#      "This is the permutation:"
#
#      1 2 3 4 5 6 7
#      7 2 4 1 5 3 6
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of objects permuted.
#
#    Input, integer P(N), the permutation, in standard index form.
#
#    Input, string TITLE, an optional title.
#    If no title is supplied, then only the permutation is printed.
#
  inc = 20

  if ( len ( title ) != 0 ):

    print ( '' )
    print ( title )

    for ilo in range ( 0, n, inc ):
      ihi = min ( n, ilo + inc )

      print ( '' )
      print ( '  ', end = '' )
      
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( i + 1 ), end = '' )
      print ( '' )

      print ( '  ', end = '' )
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( p[i] ), end = '' )
      print ( '' )

  else:

    for ilo in range ( 0, n, inc ):
      ihi = min ( n, ilo + inc )
      print ( '  ', end = '' )
      for i in range ( ilo, ihi ):
        print ( '%4d' % ( p[i] ), end = '' )
      print ( '' )

  return

def perm1_print_test ( ):

#*****************************************************************************80
#
## PERM1_PRINT_TEST tests PERM1_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'PERM1_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM1_PRINT prints a permutation of (1,...,N).' )

  n = 7
  p = np.array ( [ 7, 2, 4, 1, 5, 3, 6 ] )
  perm1_print ( n, p, '  A 1-based permutation:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM1_PRINT_TEST' )
  print ( '  Normal end of execution.' )
  return

def perm1_random ( n, seed ):

#*****************************************************************************80
#
## PERM1_RANDOM selects a random 1-based permutation of N objects.
#
#  Discussion:
#
#    An I4VEC is a vector of I4 values.
#
#    The algorithm is known as the Fisher-Yates or Knuth shuffle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer P[N], a permutation of the digits 0 through N-1.
#
#    Output, integer SEED, an updated seed.
#
  import numpy as np

  p = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    p[i] = i + 1

  for i in range ( 0, n - 1 ):
    j, seed = i4_uniform_ab ( i, n - 1, seed )
    k    = p[i]
    p[i] = p[j]
    p[j] = k

  return p, seed

def perm1_random_test ( ):

#*****************************************************************************80
#
## PERM1_RANDOM_TEST tests PERM1_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'PERM1_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM1_RANDOM randomly selects a 1-based permutation.' )
  print ( '' )

  seed = 123456789

  for test in range ( 0, 5 ):
    p, seed = perm1_random ( n, seed )
    perm1_print ( n, p, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM1_RANDOM_TEST' )
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

def perm1_is_unicycle ( n, p ):

#*****************************************************************************80
#
## PERM1_IS_UNICYCLE is TRUE if a 1-based permutation is a unicycle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of objects in the permutation.
#
#    Input, integer P(N), the permutation.
#
#    Output, logical VALUE, is TRUE if the permutation is a unicycle.
#
  check = perm1_check ( n, p )

  if ( not check ):
    value = False
    return value
#
#  From 1, you must be able to take N-1 steps without reaching 1...
#
  i = 1
  for j in range ( 1, n + 1 ):
    i = p[i-1]
    if ( i == 1 ):
      if ( j < n ):
        value = False
      else:
        value = True
      return value

  value = False

  return value

def perm1_is_unicycle_test ( ):

#*****************************************************************************80
#
## PERM1_IS_UNICYCLE_TEST tests PERM1_IS_UNICYCLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5
  test_num = 10
  seed = 123456789

  print ( '' )
  print ( 'PERM1_IS_UNICYCLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PERM1_IS_UNICYCLE determines whether a 1-based permutation' )
  print ( '  is a unicyle' )

  for test in range ( 0, test_num ):

    p, seed = perm1_random ( n, seed )

    value = perm1_is_unicycle ( n, p )

    if ( value ):

      perm1_print ( n, p, '  This permutation is a unicycle' )
      u = unicycle_index_to_sequence ( n, p )
      unicycle_print ( n, u, '  The permutation in sequence form' )

    else:

      perm1_print ( n, p, '  This permutation is NOT a unicycle' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PERM1_IS_UNICYCLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def unicycle_check ( n, p ):

#*****************************************************************************80
#
## UNICYCLE_CHECK checks that a vector represents a unicycle.
#
#  Discussion:
#
#    A unicycle is a permutation with a single cycle.  This might be called
#    a cyclic permutation, except that that name is used with at least two
#    other meanings.  So, to be clear, a unicycle is a permutation of N
#    objects in which each object is returned to itself precisely after
#    N applications of the permutation.
#
#    This routine verifies that each of the integers from 1
#    to N occurs among the N entries of the permutation.
#
#    Any permutation of the integers 1 to N describes a unicycle.
#    The permutation ( 3, 4, 2, 1 ) indicates that the unicycle
#    sends 3 to 4, 4 to 2, 2 to 1 and 1 to 3.  This is the sequential
#    description of a unicycle.
#
#    The standard sequence "rotates" the permutation so that it begins
#    with 1.  The above sequence becomes a standard sequence when
#    written as ( 1, 3, 4, 2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries.
#
#    Input, integer P(N), the unicycle sequence vector.
#
#    Output, logical CHECK, is TRUE if the sequence represents a unicycle.
#
  from sys import exit

  check = perm1_check ( n, p )

  if ( not check ):
#   print ( '' )
#   print ( 'UNICYCLE_CHECK - Warning!' )
#   print ( '  This is not a permutation!' )
    return check

  check = perm1_is_unicycle ( n, p )

  if ( not check ):
#   print ( '' )
#   print ( 'UNICYCLE_CHECK - Warning!' )
#   print ( '  Permutation is not a unicycle.' )
    return check

  return check

def unicycle_check_test ( ):

#*****************************************************************************80
#
## UNICYCLE_CHECK_TEST tests UNICYCLE_CHECK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  p1 = np.array ( [ 5, 2, 3, 4, 1 ] )
  p2 = np.array ( [ 4, 1, 3, 0, 2 ] )
  p3 = np.array ( [ 4, 2, 1, 3, 2 ] )
  p4 = np.array ( [ 2, 1, 4, 3, 5 ] )
  p5 = np.array ( [ 3, 4, 5, 1, 2 ] )

  print ( '' )
  print ( 'UNICYCLE_CHECK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNICYCLE_CHECK checks a unicycle.' )

  unicycle_print ( n, p1, '  Candidate 1:' )
  check = unicycle_check ( n, p1 )
  if ( check ):
    print ( '  This is a unicycle!' )
  else:
    print ( '  This is not a unicycle.' )

  unicycle_print ( n, p2, '  Candidate 2:' )
  check = unicycle_check ( n, p2 )
  if ( check ):
    print ( '  This is a unicycle!' )
  else:
    print ( '  This is not a unicycle.' )

  unicycle_print ( n, p3, '  Candidate 3:' )
  check = unicycle_check ( n, p3 )
  if ( check ):
    print ( '  This is a unicycle!' )
  else:
    print ( '  This is not a unicycle.' )

  unicycle_print ( n, p4, '  Candidate 4:' )
  check = unicycle_check ( n, p4 )
  if ( check ):
    print ( '  This is a unicycle!' )
  else:
    print ( '  This is not a unicycle.' )

  unicycle_print ( n, p5, '  Candidate 5:' )
  check = unicycle_check ( n, p5 )
  if ( check ):
    print ( '  This is a unicycle!' )
  else:
    print ( '  This is not a unicycle.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNICYCLE_CHECK_TEST:' )
  print ( '  Normal end of execution.' )
  return

def unicycle_enum ( n ):

#*****************************************************************************80
#
## UNICYCLE_ENUM enumerates the unicycles.
#
#  Discussion:
#
#    Each standard sequence corresponds to a unique unicycle.  Since the
#    first element of a standard sequence is always 1, the number of standard
#    sequences, and hence the number of unicycles, is (n-1)#.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the unicyle.
#
#    Output, integer VALUE, the number of unicycles.
#
  value = i4_factorial ( n - 1 )

  return value

def unicycle_enum_test ( ):

#*****************************************************************************80
#
## UNICYCLE_ENUM_TEST tests UNICYCLE_ENUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n_max = 10

  print ( '' )
  print ( 'UNICYCLE_ENUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNICYCLE_ENUM enumerates the unicycles of N objects.' )
  print ( '' )
  print ( '  N    Number' )
  print ( '' )

  for n in range ( 0, n_max + 1 ):

    num = unicycle_enum ( n )
    print ( '  %3d  %8d' % ( n, num ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNICYCLE_ENUM_TEST' )
  print ( '  Normal end of execution.' )
  return

def unicycle_index ( n, u ):

#*****************************************************************************80
#
## UNICYCLE_INDEX returns the index form of a unicycle.
#
#  Example:
#
#    N = 4
#
#    U       = 1 3 4 2
#    U_INDEX = 3 1 4 2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2025
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the unicycles.
#
#    Input, integer U(N), the unicycle sequence vector.
#
#    Output, integer U_INDEX(N), the unicycle index vector.
#
  import numpy as np

  u_index = np.zeros ( n, dtype = np.int32 )

  for i in range ( 0, n ):
    ip1 = i4_wrap ( i + 1, 0, n - 1 )
    u_index[u[i]-1] = u[ip1]

  return u_index

def unicycle_index_test ( ):

#*****************************************************************************80
#
## UNICYCLE_INDEX_TEST tests UNICYCLE_INDEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 6
  test_num = 5
  seed = 123456789

  print ( '' )
  print ( 'UNICYCLE_INDEX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNICYCLE_INDEX converts a unicycle to index form.' )

  for test in range ( 0, 5 ):

    u, seed = unicycle_random ( n, seed )

    unicycle_print ( n, u, '  The unicycle:' )

    u_index = unicycle_index ( n, u )
    
    unicycle_index_print ( n, u_index, '  The index form:' )

    u2 = unicycle_index_to_sequence ( n, u_index )

    unicycle_print ( n, u2, '  The unicycle recovered:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNICYCLE_INDEX_TEST' )
  print ( '  UNICYCLE_INDEX converts a unicycle to index form.' )
  return

def unicycle_index_print ( n, u_index, title ):

#*****************************************************************************80
#
## UNICYCLE_INDEX_PRINT prints a unicycle given in index form.
#
#  Example:
#
#    Input:
#
#      U_INDEX = 7 1 4 5 2 3 6
#
#    Printed output:
#
#      1 2 3 4 5 6 7
#      7 1 4 5 2 3 6
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the unicycle.
#
#    Input, integer U_INDEX(N), the unicycle index vector.
#
#    Input, string TITLE, a title.
#
  inc = 20

  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  for ilo in range ( 1, n, inc ):
    ihi = min ( n, ilo + inc - 1 )
    print ( '' )
    print ( '  ', end = '' )
    for i in range ( ilo, ihi + 1 ):
      print ( '%4d' % ( i ), end = '' )
    print ( '' )
    print ( '  ', end = '' )
    for i in range ( ilo, ihi + 1 ):
      print ( '%4d' % ( u_index[i-1] ), end = '' )
    print ( '' )

  return

def unicycle_index_print_test ( ):

#*****************************************************************************80
#
## UNICYCLE_INDEX_PRINT_TEST tests UNICYCLE_INDEX_PRINT;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 7

  print ( '' )
  print ( 'UNICYCLE_INDEX_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNICYCLE_INDEX_PRINT prints a unicyle given in index form;' )
  print ( '' )

  u_index = np.array ( [ 7, 1, 4, 5, 2, 3, 6 ] )

  unicycle_index_print ( n, u_index, '  The unicycle in index form:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNICYCLE_INDEX_PRINT_TEST' )
  print ( '  Normal end of execution.' )
  return

def unicycle_index_to_sequence ( n, u_index ):

#*****************************************************************************80
#
## UNICYCLE_INDEX_TO_SEQUENCE converts a unicycle from index to sequence form.
#
#  Example:
#
#    N = 4
#
#    U_INDEX = 3 1 4 2
#    U       = 1 3 4 2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the unicycles.
#
#    Output, integer U_INDEX(N), the unicycle index vector.
#
#    Input, integer U(N), the unicycle sequence vector.
#
  import numpy as np
  from sys import exit

  u = np.zeros ( n, dtype = np.int32 )

  u[0] = 1
  i = 1

  for j in range ( 1, n ):

    i = u_index[i-1]
    u[j] = i

    if ( i == 1 ):
      print ( '' )
      print ( 'UNICYCLE_INDEX_TO_SEQUENCE - Fatal error!' )
      print ( '  The index vector does not represent a unicycle.' )
      print ( '  On step %d, u_index(%d) = 1.' % ( j, i ) )
      exit ( 'UNICYCLE_INDEX_TO_SEQUENCE - Fatal error!' )

  return u

def unicycle_index_to_sequence_test ( ):

#*****************************************************************************80
#
## UNICYCLE_INDEX_TO_SEQUENCE_TEST tests UNICYCLE_INDEX_TO_SEQUENCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 6
  seed = 123456789

  print ( '' )
  print ( 'UNICYCLE_INDEX_TO_SEQUENCE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNICYCLE_INDEX_TO_SEQUENCE converts an index to unicycle form.' )

  for test in range ( 0, 5 ):

    u, seed = unicycle_random ( n, seed )

    unicycle_print ( n, u, '  The unicycle:' )

    u_index = unicycle_index ( n, u )
    
    unicycle_index_print ( n, u_index, '  The index form:' )

    u2 = unicycle_index_to_sequence ( n, u_index )

    unicycle_print ( n, u2, '  The unicycle recovered:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNICYCLE_INDEX_TO_SEQUENCE_TEST' )
  print ( '  Normal end of execution.' )
  return

def unicycle_inverse ( n, u ):

#*****************************************************************************80
#
## UNICYCLE_INVERSE returns the inverse of a unicycle.
#
#  Example:
#
#    N = 4
#
#    U         = 1 3 4 2
#    U_INVERSE = 1 2 4 3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the unicycles.
#
#    Input, integer U(N), the unicycle sequence vector.
#
#    Output, integer U_INVERSE(N), the inverse unicycle.
#
  import numpy as np

  u_inverse = np.zeros ( n, dtype = np.int32 )

  u_inverse[0] = 1
  for i in range ( 1, n ):
    u_inverse[i] = u[n-i]

  return u_inverse

def unicycle_inverse_test ( ):

#*****************************************************************************80
#
## UNICYCLE_INVERSE_TEST tests UNICYCLE_INVERSE;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 7
  u = np.array ( [ 1, 7, 6, 2, 4, 3, 5 ] )

  print ( '' )
  print ( 'UNICYCLE_INVERSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNICYCLE_INVERSE inverts a unicycle' )

  unicycle_print ( n, u, '  The original unicycle:' )
 
  u_inverse = unicycle_inverse ( n, u )

  unicycle_print ( n, u_inverse, '  The inverse unicycle:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNICYCLE_INVERSE_TEST' )
  print ( '  Normal end of execution.' )
  return

def unicycle_next ( n, u, rank ):

#*****************************************************************************80
#
## UNICYCLE_NEXT generates unicycles in lexical order, one at a time.
#
#  Example:
#
#    N = 4
#
#    1   1 2 3 4
#    2   1 2 4 3
#    3   1 3 2 4
#    4   1 3 4 2
#    5   1 4 2 3
#    6   1 4 3 2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the unicycles.
#
#    Input/output, integer U(N); on first call with MORE = FALSE,
#    this value is not used.  Otherwise, the input value is the previous
#    unicycle.  The output value is the next unicycle.
#
#    Input/output, integer RANK, the rank.
#    If RANK = -1 on input, then the routine understands that this is
#    the first call, and that the user wishes the routine to supply
#    the first element in the ordering, which has RANK = 0.
#    In general, the input value of RANK is increased by 1 for output,
#    unless the very last element of the ordering was input, in which
#    case the output value of RANK is -1.
#
  import numpy as np

  p = np.zeros ( n - 1, dtype = np.int32 )

  if ( rank == -1 ):
    u[0] = 1
  else:
    for i in range ( 0, n - 1 ):
      p[i] = u[i+1] - 1

  p, rank = perm1_lex_next ( n - 1, p, rank )

  for i in range ( 0, n - 1 ):
    u[i+1] = p[i] + 1

  return u, rank

def unicycle_next_test ( ):

#*****************************************************************************80
#
## UNICYCLE_NEXT_TEST tests UNICYCLE_NEXT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'UNICYCLE_NEXT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNICYCLE_NEXT generates unicycles in lex order.' )
  print ( '' )

  rank = -1
  u = np.zeros ( n, dtype = np.int32 )

  while ( True ):

    u, rank = unicycle_next ( n, u, rank )

    if ( rank == - 1 ):
      break

    print ( '  %3d:  ' % ( rank ), end = '' )
    for i in range ( 0, n ):
      print ( '%2d' % ( u[i] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNICYCLE_NEXT_TEST' )
  print ( '  Normal end of execution.' )
  return

def unicycle_print ( n, u, title ):

#*****************************************************************************80
#
## UNICYCLE_PRINT prints a unicycle given in sequence form.
#
#  Example:
#
#    Input:
#
#      U = 7 1 4 5 2 3 6
#
#    Printed output:
#
#      7 1 4 5 2 3 6
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the unicycle.
#
#    Input, integer U(N), the unicycle sequence vector.
#
#    Input, string TITLE, a title.
#
  inc = 20

  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
    print ( '' )

  for ilo in range ( 0, n, inc ):
    ihi = min ( n, ilo + inc )
    for i in range ( ilo, ihi ):
      print ( '  %4d' % ( u[i] ), end = '' )
    print ( '' )

  return

def unicycle_print_test ( ):

#*****************************************************************************80
#
## UNICYCLE_PRINT_TEST tests UNICYCLE_PRINT;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'UNICYCLE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNICYCLE_PRINT prints a unicyle;' )

  seed = 123456789

  u, seed = unicycle_random ( n, seed )

  unicycle_print ( n, u, '  The unicycle:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNICYCLE_PRINT_TEST' )
  print ( '  Normal end of execution.' )
  return

def unicycle_random ( n, seed ):

#*****************************************************************************80
#
## UNICYCLE_RANDOM selects a random unicycle of N objects.
#
#  Discussion:
#
#    The routine assumes the objects are labeled 1, 2, ... N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms for Computers and Calculators,
#    Second Edition,
#    Academic Press, 1978,
#    ISBN: 0-12-519260-6,
#    LC: QA164.N54.
#
#  Parameters:
#
#    Input, integer N, the number of objects to be permuted.
#
#    Input/output, integer SEED, a seed for the random number
#    generator.
#
#    Output, integer U(N), a unicycle in sequence form.
#
  u = i4vec_indicator1 ( n )

  for i in range ( 1, n ):
    j, seed = i4_uniform_ab ( i, n - 1, seed )
    t    = u[i]
    u[i] = u[j]
    u[j] = t

  return u, seed

def unicycle_random_test ( ):

#*****************************************************************************80
#
## UNICYCLE_RANDOM_TEST tests UNICYCLE_RANDOM;
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'UNICYCLE_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNICYCLE_RANDOM produces a random unicyle;' )
  print ( '  For this test, N = %d' % ( n ) )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 5 ):
    u, seed = unicycle_random ( n, seed )
    unicycle_print ( n, u, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNICYCLE_RANDOM_TEST' )
  print ( '  Normal end of execution.' )
  return

def unicycle_rank ( n, u ):

#*****************************************************************************80
#
## UNICYCLE_RANK computes the rank of a unicycle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, integer N, the order of the unicycle.
#
#    Input, integer U(N), a unicycle in sequence form.
#
#    Output, integer RANK, the rank of the unicycle.
#
  import numpy as np

  p = np.zeros ( n - 1, dtype = np.int32 )

  for i in range ( 0, n - 1 ):
    p[i] = u[i+1] - 1

  rank = perm1_lex_rank ( n - 1, p )

  return rank

def unicycle_rank_test ( ):

#*****************************************************************************80
#
## UNICYCLE_RANK_TEST tests UNICYCLE_RANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  u = np.array ( [ 1, 5, 2, 3, 4 ] )

  print ( '' )
  print ( 'UNICYCLE_RANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNICYCLE_RANK ranks a unicycle.' )

  unicycle_print ( n, u, '  The unicycle:' )
 
  rank = unicycle_rank ( n, u )
 
  print ( '' )
  print ( '  The rank is: %d' % ( rank ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNICYCLE_RANK_TEST' )
  print ( '  Normal end of execution.' )
  return

def unicycle_unrank ( n, rank ):

#*****************************************************************************80
#
## UNICYCLE_UNRANK "unranks" a unicycle.
#
#  Discussion:
#
#    That is, given a rank, it computes the corresponding unicycle.
#
#    The value of the rank should be between 0 and (N-1)#-1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dennis Stanton, Dennis White,
#    Constructive Combinatorics,
#    Springer, 1986,
#    ISBN: 0387963472,
#    LC: QA164.S79.
#
#  Parameters:
#
#    Input, integer N, the number of elements in the set.
#
#    Input, integer RANK, the desired rank of the permutation.
#
#    Output, integer U(N), the unicycle.
#
  import numpy as np

  p = perm1_lex_unrank ( n - 1, rank )

  u = np.zeros ( n, dtype = np.int32 )

  u[0] = 1
  for i in range ( 1, n ):
    u[i] = p[i-1] + 1

  return u

def unicycle_unrank_test ( ):

#*****************************************************************************80
#
## UNICYCLE_UNRANK_TEST tests UNICYCLE_UNRANK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 5

  print ( '' )
  print ( 'UNICYCLE_UNRANK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNICYCLE_UNRANK, given a rank, computes the' )
  print ( '  corresponding unicycle.' )
  print ( '' )

  rank = 6
  print ( '  The requested rank is %d' % ( rank ) )
 
  u = unicycle_unrank ( n, rank )
 
  unicycle_print ( n, u, '  The unicycle:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNICYCLE_UNRANK_TEST' )
  print ( '  Normal end of execution.' )
  return

def unicycle_test ( ):

#*****************************************************************************80
#
## UNICYCLE_TEST tests the UNICYCLE library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'UNICYCLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the UNICYCLE library.' )

  i4_factorial_test ( )
  i4_modp_test ( )
  i4_uniform_ab_test ( )
  i4_wrap_test ( )

  i4vec_indicator1_test ( )
  i4vec_print_test ( )
  i4vec_reverse_test ( )
  i4vec_uniform_ab_test ( )

  perm1_check_test ( )
  perm1_enum_test ( )
  perm1_inverse_test ( )
  perm1_lex_next_test ( )
  perm1_lex_rank_test ( )
  perm1_lex_unrank_test ( )
  perm1_print_test ( )
  perm1_random_test ( )

  perm1_is_unicycle_test ( )
  unicycle_check_test ( )
  unicycle_enum_test ( )
  unicycle_index_test ( )
  unicycle_index_print_test ( )
  unicycle_index_to_sequence_test ( )
  unicycle_inverse_test ( )
  unicycle_next_test ( )
  unicycle_random_test ( )
  unicycle_rank_test ( )
  unicycle_unrank_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNICYCLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  unicycle_test ( )
  timestamp ( )
 
