#! /usr/bin/env python3
#
def asa241_test ( ):

#*****************************************************************************80
#
## ASA241_TEST tests ASA241.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'ASA241_TEST:' )
  print ( '  Test the ASA241 library.' )

  normal_01_cdf_values_test ( )

  r4_huge_test ( )
  r4_normal_01_cdf_inverse_test ( )
  r4poly_print_test ( )
  r4poly_value_test ( )
  r4vec_is_zero_test ( )
  r4vec_print_test ( )
  r4vec_transpose_print_test ( )
  r4vec_uniform_01_test ( )

  r8_huge_test ( )
  r8_normal_01_cdf_inverse_test ( )
  r8poly_print_test ( )
  r8poly_value_test ( )
  r8vec_is_zero_test ( )
  r8vec_print_test ( )
  r8vec_transpose_print_test ( )
  r8vec_uniform_01_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ASA241_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_01_cdf_values ( n_data ):

#*****************************************************************************80
#
## NORMAL_01_CDF_VALUES returns some values of the Normal 01 CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NormalDistribution [ 0, 1 ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
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
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 17

  f_vec = np.array ( (\
     0.5000000000000000E+00, \
     0.5398278372770290E+00, \
     0.5792597094391030E+00, \
     0.6179114221889526E+00, \
     0.6554217416103242E+00, \
     0.6914624612740131E+00, \
     0.7257468822499270E+00, \
     0.7580363477769270E+00, \
     0.7881446014166033E+00, \
     0.8159398746532405E+00, \
     0.8413447460685429E+00, \
     0.9331927987311419E+00, \
     0.9772498680518208E+00, \
     0.9937903346742239E+00, \
     0.9986501019683699E+00, \
     0.9997673709209645E+00, \
     0.9999683287581669E+00 ))

  x_vec = np.array ((\
     0.0000000000000000E+00, \
     0.1000000000000000E+00, \
     0.2000000000000000E+00, \
     0.3000000000000000E+00, \
     0.4000000000000000E+00, \
     0.5000000000000000E+00, \
     0.6000000000000000E+00, \
     0.7000000000000000E+00, \
     0.8000000000000000E+00, \
     0.9000000000000000E+00, \
     0.1000000000000000E+01, \
     0.1500000000000000E+01, \
     0.2000000000000000E+01, \
     0.2500000000000000E+01, \
     0.3000000000000000E+01, \
     0.3500000000000000E+01, \
     0.4000000000000000E+01 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def normal_01_cdf_values_test ( ):

#*****************************************************************************80
#
## NORMAL_01_CDF_VALUES_TEST demonstrates the use of NORMAL_01_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'NORMAL_01_CDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_CDF_VALUES stores values of the unit normal CDF.' )
  print ( '' )
  print ( '      X         NORMAL_01_CDF(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_CDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r4_huge ( ):

#*****************************************************************************80
#
## R4_HUGE returns a "huge" real number.
#
#  Discussion:
#
#    The value returned by this function is NOT required to be the
#    maximum representable R4.  This value varies from machine to machine,
#    from compiler to compiler, and may cause problems when being printed.
#    We simply want a "very large" but non-infinite number.
#
#    MATLAB provides a built-in symbolic constant "inf" that can be used
#    if a huge number is really what you want!
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, a huge number.
#
  value = 1.0E+30

  return value

def r4_huge_test ( ):

#*****************************************************************************80
#
## R4_HUGE_TEST tests R4_HUGE.
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

  print ( '' )
  print ( 'R4_HUGE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4_HUGE returns a "huge" R4;' )
  print ( '' )
  print ( '    R4_HUGE = %g' % ( r4_huge ( ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4_HUGE_TEST' )
  print ( '  Normal end of execution.' )
  return

def r4_normal_01_cdf_inverse ( p ):

#*****************************************************************************80
#
## R4_NORMAL_01_CDF_INVERSE inverts the standard normal CDF.
#
#  Discussion:
#
#    The result is accurate to about 1 part in 10**7.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2004
#
#  Author:
#
#    Original FORTRAN77 version by Michael Wichura.
#    MATLAB version by John Burkardt.
#
#  Reference:
#
#    Michael Wichura,
#    The Percentage Points of the Normal Distribution,
#    Algorithm AS 241,
#    Applied Statistics,
#    Volume 37, Number 3, pages 477-484, 1988.
#
#  Parameters:
#
#    Input, real P, the value of the cumulative probability densitity function.
#    0 < P < 1.  If P is not in this range, an "infinite" value is returned.
#
#    Output, real VALUE, the normal deviate value with the property that
#    the probability of a standard normal deviate being less than or
#    equal to the value is P.
#
  import numpy as np
  from sys import exit

  a = np.array ( [ 3.3871327179, 50.434271938, 159.29113202, 59.109374720 ] )
  b = np.array ( [ 1.0, 17.895169469, 78.757757664, 67.187563600 ] )
  c = np.array ( [ 1.4234372777, 2.7568153900, 1.3067284816, 0.17023821103 ] )
  const1 = 0.180625
  const2 = 1.6
  d = np.array ( [ 1.0, 0.73700164250, 0.12021132975 ] )
  e = np.array ( [ 6.6579051150, 3.0812263860, 0.42868294337, 0.017337203997 ] )
  f = np.array ( [ 1.0, 0.24197894225, 0.012258202635 ] )
  split1 = 0.425
  split2 = 5.0

  if ( p <= 0.0 ):
    value = -r4_huge ( )
    return value

  if ( 1.0 <= p ):
    value = r4_huge ( )
    return value

  q = p - 0.5

  if ( abs ( q ) <= split1 ):

    r = const1 - q * q
    value = q * r4poly_value ( 4, a, r ) / r4poly_value ( 4, b, r )

  else:

    if ( q < 0.0 ):
      r = p
    else:
      r = 1.0 - p

    if ( r <= 0.0 ):
      value = -1.0
      exit ( 'R4_NORMAL_CDF_INVERSE - Fatal error!' )

    r = np.sqrt ( - np.log ( r ) )

    if ( r <= split2 ):

      r = r - const2

      value = r4poly_value ( 4, c, r ) / r4poly_value ( 3, d, r )

    else:

      r = r - split2

      value = r4poly_value ( 4, e, r ) / r4poly_value ( 3, f, r )

    if ( q < 0.0 ):
      value = -value

  return value

def r4_normal_01_cdf_inverse_test ( ):

#*****************************************************************************80
#
## R4_NORMAL_01_CDF_INVERSE_TEST tests R4_NORMAL_01_CDF_INVERSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 November 2006
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R4_NORMAL_01_CDF_INVERSE_TEST:' )
  print ( '  R4_NORMAL_01_CDF_INVERSE takes FX = NormalCDF ( X ) and computes' )
  print ( '  an estimate X2, of the corresponding input argument X,' )
  print ( '  accurate to about 7 decimal places.' )
  print ( '' )
  print ( '      X                       FX               X2' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    x2 = r4_normal_01_cdf_inverse ( fx )
    
    print ( '  %22.16g  %22.16g  %22.16g' % ( x, fx, x2 ) )

  return

def r4poly_print ( m, a, title ):

#*****************************************************************************80
#
## R4POLY_PRINT prints out a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the nominal degree of the polynomial.
#
#    Input, real A[M+1], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    Input, string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
  print ( '' )

  if ( r4vec_is_zero ( m + 1, a ) ):
    print ( '  p(x) = 0' )
    return
 
  first = True

  for i in range ( m, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( first ):
        print ( '  p(x) = ', end = '' )
        if ( plus_minus == '+' ):
          plus_minus = ' '
        first = False
      else:
        print ( '         ', end = '' )

      if ( 2 <= i ):
        print ( '         %c %g * x^%d' % ( plus_minus, mag, i ) )
      elif ( i == 1 ):
        print ( '         %c %g * x' % ( plus_minus, mag ) )
      elif ( i == 0 ):
        print ( '         %c %g' % ( plus_minus, mag ) )

def r4poly_print_test ( ):

#*****************************************************************************80
#
## R4POLY_PRINT_TEST tests R4POLY_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R4POLY_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4POLY_PRINT prints an R4POLY.' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )
  r4poly_print ( m, c, '  The R8POLY:' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 0.0 ] )
  r4poly_print ( m, c, '  The R8POLY:' )

  m = 5
  c = np.array ( [ 12.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  r4poly_print ( m, c, '  The R8POLY:' )

  m = 5
  c = np.array ( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  r4poly_print ( m, c, '  The R8POLY:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4POLY_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r4poly_value ( n, a, x ):

#*****************************************************************************80
#
## R4POLY_VALUE evaluates a real polynomial.
#
#  Discussion:
#
#    For sanity's sake, the value of N indicates the NUMBER of 
#    coefficients, or more precisely, the ORDER of the polynomial,
#    rather than the DEGREE of the polynomial.  The two quantities
#    differ by 1, but cause a great deal of confusion.
#
#    Given N and A, the form of the polynomial is:
#
#      p(x) = a(1) + a(2) * x + \ + a(n-1) * x^(n-2) + a(n) * x^(n-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2005
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the polynomial.
#
#    Input, real A(1:N), the coefficients of the polynomial.
#    A(1) is the constant term.
#
#    Input, real X, the point at which the polynomial is to be evaluated.
#
#    Output, real VALUE, the value of the polynomial at X.
#
  value = 0.0
  for i in range ( n - 1, -1, -1 ):
    value = value * x + a[i]

  return value

def r4poly_value_test ( ):

#*****************************************************************************80
#
## R4POLY_VALUE_TEST tests R4POLY_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 4
  n = 16
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )

  print ( '' )
  print ( 'R4POLY_VALUE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4POLY_VALUE evaluates a polynomial at a point' )
  print ( '  using a naive method.' )

  r4poly_print ( m, c, '  The polynomial coefficients:' )

  x_lo = 0.0
  x_hi = 5.0
  x = np.linspace ( x_lo, x_hi, n )

  print ( '' )
  print ( '   I    X    P(X)' )
  print ( '' )

  for i in range ( 0, n ):
    p = r4poly_value ( m, c, x[i] )
    print ( '  %2d  %8.4f  %14.6g' % ( i, x[i], p ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4POLY_VALUE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r4vec_is_zero ( n, x ):

#*****************************************************************************80
#
## R4VEC_IS_ZERO is true if every entry is zero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vectors.
#
#    Input, real X(N), the vector to be compared against.
#
#    Output, real VALUE, is true if all entries are zero.
#
  import numpy as np

  value = np.all ( x[0:n] == 0.0 )

  return value

def r4vec_is_zero_test ( ):

#*****************************************************************************80
#
## R4VEC_IS_ZERO_TEST tests R4VEC_IS_ZERO.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R4VEC_IS_ZERO_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4VEC_IS_ZERO is TRUE if an R8VEC contains' )
  print ( '  only zero entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 0.0 ] )
  print ( '' )
  r4vec_transpose_print ( n, x, '  X:' )
  if ( r4vec_is_zero ( n, x ) ):
    print ( '  X contains only zero entries.' )
  else:
    print ( '  X contains at least one nonzero entry.' )

  x = np.array ( [ 0.0, 0.0, 0.0 ] )
  print ( '' )
  r4vec_transpose_print ( n, x, '  X:' )
  if ( r4vec_is_zero ( n, x ) ):
    print ( '  X contains only zero entries.' )
  else:
    print ( '  X contains at least one nonzero entry.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r4vec_transpose_print ( n, x, '  X:' )
  if ( r4vec_is_zero ( n, x ) ):
    print ( '  X contains only zero entries.' )
  else:
    print ( '  X contains at least one nonzero entry.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4VEC_IS_ZERO_TEST' )
  print ( '  Normal end of execution.' )
  return

def r4vec_print ( n, a, title ):

#*****************************************************************************80
#
## R4VEC_PRINT prints an R4VEC.
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
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r4vec_print_test ( ):

#*****************************************************************************80
#
## R4VEC_PRINT_TEST tests R4VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R4VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4VEC_PRINT prints an R4VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r4vec_print ( n, v, '  Here is an R4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r4vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## R4VEC_TRANSPOSE_PRINT prints an R4VEC "transposed".
#
#  Discussion:
#
#    An R4VEC is a vector of R4's.
#
#  Example:
#
#    A = (/ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 /)
#    TITLE = 'My vector:  '
#
#    My vector:   1.0    2.1    3.2    4.3    5.4
#                 6.5    7.6    8.7    9.8   10.9
#                11.0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  title_length = len ( title )

  for ilo in range ( 0, n, 5 ):

    if ( ilo == 0 ):
      print ( title, end = '' )
    else:
      blanks = ''
      for i in range ( 0, title_length ):
        blanks = blanks + ' '
      print ( blanks, end = '' )

    print ( '  ', end = '' )

    ihi = min ( ilo + 5 - 1, n - 1 )

    for i in range ( ilo, ihi + 1 ):
      print ( '  %12g' % ( a[i] ), end = '' )
    print ( '' )

  return

def r4vec_transpose_print_test ( ):

#*****************************************************************************80
#
## R4VEC_TRANSPOSE_PRINT_TEST tests R4VEC_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 12
  seed = 123456789

  print ( '' )
  print ( 'R4VEC_TRANSPOSE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4VEC_TRANSPOSE_PRINT prints an R4VEC "tranposed",' )
  print ( '  that is, placing multiple entries on a line.' )

  x, seed = r4vec_uniform_01 ( n, seed )

  r4vec_transpose_print ( n, x, '  The vector X:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4VEC_TRANSPOSE_PRINT_TEST' )
  print ( '  Normal end of execution.' )
  return

def r4vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## R4VEC_UNIFORM_01 returns a unit pseudorandom R4VEC.
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
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R4VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R4VEC_UNIFORM_01 - Fatal error!' )

  x = np.zeros ( n );

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r4vec_uniform_01_test ( ):

#*****************************************************************************80
#
## R4VEC_UNIFORM_01_TEST tests R4VEC_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R4VEC_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4VEC_UNIFORM_01 computes a random R4VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r4vec_uniform_01 ( n, seed )

  r4vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4VEC_UNIFORM_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_huge ( ):

#*****************************************************************************80
#
## R8_HUGE returns a "huge" real number.
#
#  Discussion:
#
#    The value returned by this function is intended to be the largest
#    representable real value.
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
#    Output, real VALUE, a huge number.
#
  value = 1.79769313486231571E+308

  return value

def r8_huge_test ( ):

#*****************************************************************************80
#
## R8_HUGE_TEST tests R8_HUGE.
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

  print ( '' )
  print ( 'R8_HUGE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_HUGE returns a "huge" R8;' )
  print ( '' )
  print ( '    R8_HUGE = %g' % ( r8_huge ( ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_HUGE_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_normal_01_cdf_inverse ( p ):

#*****************************************************************************80
#
## R8_NORMAL_01_CDF_INVERSE inverts the standard normal CDF.
#
#  Discussion:
#
#    The result is accurate to about 1 part in 10**16.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2004
#
#  Author:
#
#    Original FORTRAN77 version by Michael Wichura.
#    MATLAB version by John Burkardt.
#
#  Reference:
#
#    Michael Wichura,
#    The Percentage Points of the Normal Distribution,
#    Algorithm AS 241,
#    Applied Statistics,
#    Volume 37, Number 3, pages 477-484, 1988.
#
#  Parameters:
#
#    Input, real P, the value of the cumulative probability 
#    densitity function.  0 < P < 1.  If P is outside this range, an
#    "infinite" value is returned.
#
#    Output, real VALUE, the normal deviate value with the 
#    property that the probability of a standard normal deviate being 
#    less than or equal to the value is P.
#
  import numpy as np
  from sys import exit

  a = np.array ( [ \
        3.3871328727963666080,      1.3314166789178437745e+2, \
        1.9715909503065514427e+3,   1.3731693765509461125e+4, \
        4.5921953931549871457e+4,   6.7265770927008700853e+4, \
        3.3430575583588128105e+4,   2.5090809287301226727e+3 ] )
  b = np.array ( [ \
        1.0,                        4.2313330701600911252e+1, \
        6.8718700749205790830e+2,   5.3941960214247511077e+3, \
        2.1213794301586595867e+4,   3.9307895800092710610e+4, \
        2.8729085735721942674e+4,   5.2264952788528545610e+3 ] )
  c = np.array ( [ \
        1.42343711074968357734,     4.63033784615654529590, \
        5.76949722146069140550,     3.64784832476320460504, \
        1.27045825245236838258,     2.41780725177450611770e-1, \
        2.27238449892691845833e-2,  7.74545014278341407640e-4 ] )
  const1 = 0.180625
  const2 = 1.6
  d = np.array ( [ \
        1.0,                        2.05319162663775882187,    \
        1.67638483018380384940,     6.89767334985100004550e-1, \
        1.48103976427480074590e-1,  1.51986665636164571966e-2, \
        5.47593808499534494600e-4,  1.05075007164441684324e-9 ] )
  e = np.array ( [ \
        6.65790464350110377720,     5.46378491116411436990,    \
        1.78482653991729133580,     2.96560571828504891230e-1, \
        2.65321895265761230930e-2,  1.24266094738807843860e-3, \
        2.71155556874348757815e-5,  2.01033439929228813265e-7 ] )
  f = np.array ( [ \
        1.0,                        5.99832206555887937690e-1, \
        1.36929880922735805310e-1,  1.48753612908506148525e-2, \
        7.86869131145613259100e-4,  1.84631831751005468180e-5, \
        1.42151175831644588870e-7,  2.04426310338993978564e-15 ] )
  split1 = 0.425
  split2 = 5.0

  if ( p <= 0.0 ):
    value = - r8_huge ( )
    return value

  if ( 1.0 <= p ):
    value = r8_huge ( )
    return value

  q = p - 0.5

  if ( abs ( q ) <= split1 ):

    r = const1 - q * q
    value = q * r8poly_value ( 8, a, r ) / r8poly_value ( 8, b, r )

  else:

    if ( q < 0.0 ):
      r = p
    else:
      r = 1.0 - p

    if ( r <= 0.0 ):
      value = -1.0
      exit ( 'R8_NORMAL_CDF_INVERSE - Fatal error!' )

    r = np.sqrt ( - np.log ( r ) )

    if ( r <= split2 ):

      r = r - const2
      value = r8poly_value ( 8, c, r ) / r8poly_value ( 8, d, r )

    else:

       r = r - split2
       value = r8poly_value ( 8, e, r ) / r8poly_value ( 8, f, r )

    if ( q < 0.0 ):
      value = - value

  return value

def r8_normal_01_cdf_inverse_test ( ):

#*****************************************************************************80
#
## R8_NORMAL_01_CDF_INVERSE_TEST tests R8_NORMAL_01_CDF_INVERSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 November 2006
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8_NORMAL_01_CDF_INVERSE_TEST:' )
  print ( '  R8_NORMAL_01_CDF_INVERSE takes FX = NormalCDF ( X ) and computes' )
  print ( '  an estimate X2, of the corresponding input argument X,' )
  print ( '  accurate to about 16 decimal places.' )
  print ( '' )
  print ( '      X                       FX               X2' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    x2 = r8_normal_01_cdf_inverse ( fx )

    print ( '  %22.16g  %22.16g  %22.16g' % ( x, fx, x2 ) )

  return

def r8poly_print ( m, a, title ):

#*****************************************************************************80
#
## R8POLY_PRINT prints out a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the nominal degree of the polynomial.
#
#    Input, real A[M+1], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    Input, string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
  print ( '' )

  if ( r8vec_is_zero ( m + 1, a ) ):
    print ( '  p(x) = 0' )
    return
 
  first = True

  for i in range ( m, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( first ):
        print ( '  p(x) = ', end = '' )
        if ( plus_minus == '+' ):
          plus_minus = ' '
        first = False
      else:
        print ( '         ', end = '' )

      if ( 2 <= i ):
        print ( '         %c %g * x^%d' % ( plus_minus, mag, i ) )
      elif ( i == 1 ):
        print ( '         %c %g * x' % ( plus_minus, mag ) )
      elif ( i == 0 ):
        print ( '         %c %g' % ( plus_minus, mag ) )

def r8poly_print_test ( ):

#*****************************************************************************80
#
## R8POLY_PRINT_TEST tests R8POLY_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8POLY_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_PRINT prints an R8POLY.' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )
  r8poly_print ( m, c, '  The R8POLY:' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 0.0 ] )
  r8poly_print ( m, c, '  The R8POLY:' )

  m = 5
  c = np.array ( [ 12.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  r8poly_print ( m, c, '  The R8POLY:' )

  m = 5
  c = np.array ( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  r8poly_print ( m, c, '  The R8POLY:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8poly_value ( n, a, x ):

#*****************************************************************************80
#
## R8POLY_VALUE evaluates an R8 polynomial.
#
#  Discussion:
#
#    For sanity's sake, the value of N indicates the NUMBER of 
#    coefficients, or more precisely, the ORDER of the polynomial,
#    rather than the DEGREE of the polynomial.  The two quantities
#    differ by 1, but cause a great deal of confusion.
#
#    Given N and A, the form of the polynomial is:
#
#      p(x) = a(1) + a(2) * x + \ + a(n-1) * x^(n-2) + a(n) * x^(n-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2005
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the polynomial.
#
#    Input, real A(1:N), the coefficients of the polynomial.
#    A(1) is the constant term.
#
#    Input, real X, the point at which the polynomial is to be evaluated.
#
#    Output, real VALUE, the value of the polynomial at X.
#
  value = 0.0
  for i in range ( n - 1, -1, -1 ):
    value = value * x + a[i]

  return value

def r8poly_value_test ( ):

#*****************************************************************************80
#
## R8POLY_VALUE_TEST tests R8POLY_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 4
  n = 16
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )

  print ( '' )
  print ( 'R8POLY_VALUE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_VALUE evaluates a polynomial at a point' )
  print ( '  using a naive method.' )

  r8poly_print ( m, c, '  The polynomial coefficients:' )

  x_lo = 0.0
  x_hi = 5.0
  x = np.linspace ( x_lo, x_hi, n )

  print ( '' )
  print ( '   I    X    P(X)' )
  print ( '' )

  for i in range ( 0, n ):
    p = r8poly_value ( m, c, x[i] )
    print ( '  %2d  %8.4f  %14.6g' % ( i, x[i], p ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_VALUE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_is_zero ( n, x ):

#*****************************************************************************80
#
## R8VEC_IS_ZERO is true if every entry is zero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vectors.
#
#    Input, real X(N), the vector to be compared against.
#
#    Output, real VALUE, is true if all entries are zero.
#
  import numpy as np

  value = np.all ( x[0:n] == 0.0 )

  return value

def r8vec_is_zero_test ( ):

#*****************************************************************************80
#
## R8VEC_IS_ZERO_TEST tests R8VEC_IS_ZERO.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_IS_ZERO_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_IS_ZERO is TRUE if an R8VEC contains' )
  print ( '  only zero entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_zero ( n, x ) ):
    print ( '  X contains only zero entries.' )
  else:
    print ( '  X contains at least one nonzero entry.' )

  x = np.array ( [ 0.0, 0.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_zero ( n, x ) ):
    print ( '  X contains only zero entries.' )
  else:
    print ( '  X contains at least one nonzero entry.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_zero ( n, x ) ):
    print ( '  X contains only zero entries.' )
  else:
    print ( '  X contains at least one nonzero entry.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_IS_ZERO_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
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
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

  return

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_TRANSPOSE_PRINT prints an R8VEC "transposed".
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Example:
#
#    A = (/ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 /)
#    TITLE = 'My vector:  '
#
#    My vector:   1.0    2.1    3.2    4.3    5.4
#                 6.5    7.6    8.7    9.8   10.9
#                11.0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  title_length = len ( title )

  for ilo in range ( 0, n, 5 ):

    if ( ilo == 0 ):
      print ( title, end = '' )
    else:
      blanks = ''
      for i in range ( 0, title_length ):
        blanks = blanks + ' '
      print ( blanks, end = '' )

    print ( '  ', end = '' )

    ihi = min ( ilo + 5 - 1, n - 1 )

    for i in range ( ilo, ihi + 1 ):
      print ( '  %12g' % ( a[i] ), end = '' )
    print ( '' )

  return

def r8vec_transpose_print_test ( ):

#*****************************************************************************80
#
## R8VEC_TRANSPOSE_PRINT_TEST tests R8VEC_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 12
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_TRANSPOSE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_TRANSPOSE_PRINT prints an R8VEC "tranposed",' )
  print ( '  that is, placing multiple entries on a line.' )

  x, seed = r8vec_uniform_01 ( n, seed )

  r8vec_transpose_print ( n, x, '  The vector X:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_TRANSPOSE_PRINT_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
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
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_01 - Fatal error!' )

  x = np.zeros ( n );

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_01 computes a random R8VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_01 ( n, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST:' )
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
  asa241_test ( )
  timestamp ( )

