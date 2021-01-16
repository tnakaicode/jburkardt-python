#! /usr/bin/env python3
#
def chebyshev_even1 ( n, f ):

#*****************************************************************************80
#
## CHEBYSHEV_EVEN1 returns the even Chebyshev coefficients of F.
#
#  Discussion:
#
#    The coefficients are calculated using the extreme points of Tn(x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    D B Hunter, H V Smith,
#    A quadrature formula of Clenshaw-Curtis type for the Gegenbauer weight function,
#    Journal of Computational and Applied Mathematics,
#    Volume 177, 2005, pages 389-400.
#
#  Parameters:
#
#    Input, integer N, the number of points to use.
#    1 <= N.
#
#    Input, real F(x), the handle for the function to be integrated with the
#    Gegenbauer weight.
#
#    Output, real A2(1+N/2), the even Chebyshev coefficients of F.
#
  import numpy as np

  s = ( n // 2 )
  sigma = ( n % 2 )

  a2 = np.zeros ( s + 1 )

  for r in range ( 0, 2 * s + 1, 2 ):
    total = 0.5 * f ( 1.0 )
    for j in range ( 1, n ):
      total = total + f ( np.cos ( float ( j ) * np.pi / float ( n ) ) ) \
      * np.cos ( float ( r * j ) * np.pi / float ( n ) )
    total = total + 0.5 * r8_mop ( r ) * f ( -1.0 )
    rh = ( r // 2 )
    a2[rh] = ( 2.0 / float ( n ) ) * total

  return a2

def chebyshev_even1_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV_EVEN1_TEST tests CHEBYSHEV_EVEN1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'CHEBYSHEV_EVEN1_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHEBYSHEV_EVEN1 computes the even Chebyshev coefficients' )
  print ( '  of a function F, using the extreme points of Tn(x).' )

  a2_exact = np.array ( [ \
    0.4477815660, \
   -0.7056685603, \
    0.0680357987, \
   -0.0048097159 ] )

  lam = 0.75
  a = 2.0
  n = 6

  a2 = chebyshev_even1 ( n, f1 )

  s = ( n // 2 )
  r8vec2_print ( s + 1, a2, a2_exact, '  Computed and Exact Coefficients:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHEBYSHEV_EVEN1_TEST' )
  print ( '  Normal end of execution.' )
  return

def f1 ( x ):

#*****************************************************************************80
#
## F1 defines the function whose Fourier coefficients are desired.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the value.
#
  import numpy as np

  a = 2.0
  value = np.cos ( a * x )

  return value

def chebyshev_even2 ( n, f ):

#*****************************************************************************80
#
## CHEBYSHEV_EVEN2 returns the even Chebyshev coefficients of F.
#
#  Discussion:
#
#    The coefficients are calculated using the zeros of Tn(x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    D B Hunter, H V Smith,
#    A quadrature formula of Clenshaw-Curtis type for the Gegenbauer weight function,
#    Journal of Computational and Applied Mathematics,
#    Volume 177, 2005, pages 389-400.
#
#  Parameters:
#
#    Input, integer N, the number of points to use.
#    1 <= N.
#
#    Input, real F(x), the handle for the function to be integrated with the
#    Gegenbauer weight.
#
#    Output, real B2(1+N/2), the even Chebyshev coefficients of F.
#
  import numpy as np

  s = ( n // 2 )
  sigma = ( n % 2 )

  b2 = np.zeros ( s + 1 )

  for r in range ( 0, 2 * s + 1, 2 ):
    total = 0.0
    for j in range ( 0, n + 1 ):
      total = total \
        + f ( np.cos ( float ( 2 * j + 1 ) * np.pi / 2.0 / float ( n + 1 ) ) ) \
        * np.cos ( r * float ( 2 * j + 1 ) * np.pi / 2.0 / float ( n + 1 ) )
    rh = ( r // 2 )
    b2[rh] = ( 2.0 / ( n + 1 ) ) * total

  return b2

def chebyshev_even2_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV_EVEN2_TEST tests CHEBYSHEV_EVEN2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CHEBYSHEV_EVEN2_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHEBYSHEV_EVEN2 computes the even Chebyshev coefficients' )
  print ( '  of a function F, using the zeros of Tn(x).' )

  lam = 0.75
  a = 2.0
  n = 6

  b2 = chebyshev_even2 ( n, f2 )

  s = ( n // 2 )
  r8vec_print ( s + 1, b2, '  Computed Coefficients:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHEBYSHEV_EVEN2_TEST' )
  print ( '  Normal end of execution.' )
  return

def f2 ( x ):

#*****************************************************************************80
#
## F2 defines the function whose Fourier coefficients are desired.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the value.
#
  import numpy as np

  a = 2.0
  value = np.cos ( a * x )

  return value

def gegenbauer_cc1 ( n, lam, f ):

#*****************************************************************************80
#
## GEGENBAUER_CC1 estimates the Gegenbauer integral of a function.
#
#  Discussion:
#
#     value = integral ( -1 <= x <= + 1 ) ( 1 - x^2 )^(lambda-1/2) * f(x) dx
#
#     The approximation uses the practical abscissas, that is, the extreme
#     points of Tn(x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    D B Hunter, H V Smith,
#    A quadrature formula of Clenshaw-Curtis type for the Gegenbauer weight function,
#    Journal of Computational and Applied Mathematics,
#    Volume 177, 2005, pages 389-400.
#
#  Parameters:
#
#    Input, integer N, the number of points to use.
#    1 <= N.
#
#    Input, real LAM, used in the exponent of (1-x^2).
#    -0.5 < LAM.
#
#    Input, real F(x), the handle for the function to be integrated with the
#    Gegenbauer weight.
#
#    Output, real WEIGHT, the estimate for the Gegenbauer integral of F.
#
  import numpy as np
  from scipy.special import gamma

  value = 0.0

  s = ( n // 2 )
  sigma = ( n % 2 )

  a2 = chebyshev_even1 ( n, f )

  rh = s
  u = 0.5 * ( sigma + 1.0 ) * a2[rh]
  for rh in range ( s - 1, 0, -1 ):
    u = ( rh - lam ) / ( rh + lam + 1 ) * u + a2[rh]
  u = - lam * u / ( lam + 1.0 ) + 0.5 * a2[0]

  value = gamma ( lam + 0.5 ) * np.sqrt ( np.pi ) * u / gamma ( lam + 1.0 );

  return value

def gegenbauer_cc1_test ( ):

#*****************************************************************************80
#
## GEGENBAUER_CC1_TEST tests GEGENBAUER_CC1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from scipy.special import gamma
  from scipy.special import jv

  print ( '' )
  print ( 'GEGENBAUER_CC1_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GEGENBAUER_CC1 estimates the Gegenbauer integral of' )
  print ( '  a function f(x) using a Clenshaw-Curtis type approach' )
  print ( '  based on the extreme points of Tn(x).' )

  lam = 0.75
  a = 2.0
  n = 6

  value = gegenbauer_cc1 ( n, lam, f3 )

  print ( '' )
  print ( '  Value = %g' % ( value ) )

  exact = gamma ( lam + 0.5 ) * np.sqrt ( np.pi ) * jv ( lam, a ) / ( 0.5 * a ) ** lam

  print ( '  Exact = %g' % ( exact ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEGENBAUER_CC1_TEST' )
  print ( '  Normal end of execution.' )
  return

def f3 ( x ):

#*****************************************************************************80
#
## F3 defines the function whose Fourier coefficients are desired.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the value.
#
  import numpy as np

  a = 2.0
  value = np.cos ( a * x )

  return value

def gegenbauer_cc2 ( n, lam, f ):

#*****************************************************************************80
#
## GEGENBAUER_CC2 estimates the Gegenbauer integral of a function.
#
#  Discussion:
#
#     value = integral ( -1 <= x <= + 1 ) ( 1 - x^2 )^(lambda-1/2) * f(x) dx
#
#     The approximation uses the classical abscissas, that is, the zeros
#     of Tn(x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    D B Hunter, H V Smith,
#    A quadrature formula of Clenshaw-Curtis type for the Gegenbauer weight function,
#    Journal of Computational and Applied Mathematics,
#    Volume 177, 2005, pages 389-400.
#
#  Parameters:
#
#    Input, integer N, the number of points to use.
#    1 <= N.
#
#    Input, real LAM, used in the exponent of (1-x^2).
#    -0.5 < LAM.
#
#    Input, real F(x), the handle for the function to be integrated with the
#    Gegenbauer weight.
#
#    Output, real WEIGHT, the estimate for the Gegenbauer integral of F.
#
  import numpy as np
  from scipy.special import gamma

  value = 0.0

  s = ( n // 2 )
  sigma = ( n % 2 )

  b2 = chebyshev_even2 ( n, f )

  rh = s
  u = ( sigma + 1.0 ) * b2[rh]
  for rh in range ( s - 1, 0, -1 ):
    u = ( float ( rh ) - lam ) / ( float ( rh + 1 ) + lam ) * u + b2[rh]
  u = - lam * u / ( lam + 1.0 ) + 0.5 * b2[0]

  value = gamma ( lam + 0.5 ) * np.sqrt ( np.pi ) * u / gamma ( lam + 1.0 )

  return value

def gegenbauer_cc2_test ( ):

#*****************************************************************************80
#
## GEGENBAUER_CC2_TEST tests GEGENBAUER_CC2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from scipy.special import gamma
  from scipy.special import jv

  print ( '' )
  print ( 'GEGENBAUER_CC2_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GEGENBAUER_CC2 estimates the Gegenbauer integral of' )
  print ( '  a function f(x) using a Clenshaw-Curtis type approach' )
  print ( '  based on the zeros of Tn(x).' )

  lam = 0.75
  a = 2.0
  n = 6

  value = gegenbauer_cc2 ( n, lam, f4 )

  print ( '' )
  print ( '  Value = %g' % ( value ) )

  exact = gamma ( lam + 0.5 ) * np.sqrt ( np.pi ) * jv ( lam, a ) / ( 0.5 * a ) ** lam

  print ( '  Exact = %g' % ( exact ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEGENBAUER_CC2_TEST' )
  print ( '  Normal end of execution.' )
  return

def f4 ( x ):

#*****************************************************************************80
#
## F4 defines the function whose Fourier coefficients are desired.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the value.
#
  import numpy as np

  a = 2.0
  value = np.cos ( a * x )

  return value

def gegenbauer_cc_test ( ):

#*****************************************************************************80
#
## GEGENBAUER_CC_TEST tests the GEGENBAUER_CC library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'GEGENBAUER_CC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the GEGENBAUER_CC library.' )

  chebyshev_even1_test ( )
  chebyshev_even2_test ( )
  gegenbauer_cc1_test ( )
  gegenbauer_cc2_test ( )
  i4_uniform_ab_test ( )
  r8_mop_test ( )
  r8vec_print_test ( )
  r8vec2_print_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEGENBAUER_CC_TEST:' )
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

def r8_mop ( i ):

#*****************************************************************************80
#
## R8_MOP returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the power of -1.
#
#    Output, real R8_MOP, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( ):

#*****************************************************************************80
#
## R8_MOP_TEST tests R8_MOP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_MOP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_MOP evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  R8_MOP(I4)' )
  print ( '' )

  i4_min = -100;
  i4_max = +100;
  seed = 123456789;

  for test in range ( 0, 10 ):
    i4, seed = i4_uniform_ab ( i4_min, i4_max, seed )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_MOP_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## R8VEC2_PRINT prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, real A1(N), A2(N), the vectors to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## R8VEC2_PRINT_TEST tests R8VEC2_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC2_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC2_PRINT prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_PRINT_TEST:' )
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
  gegenbauer_cc_test ( )
  timestamp ( )

