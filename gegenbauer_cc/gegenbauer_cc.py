#! /usr/bin/env python3
#
def chebyshev_even1 ( n, f ):

#*****************************************************************************80
#
## chebyshev_even1() returns the even Chebyshev coefficients of F.
#
#  Discussion:
#
#    The coefficients are calculated using the extreme points of Tn(x).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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
#  Input:
#
#    integer N, the number of points to use.
#    1 <= N.
#
#    real F(x), the handle for the function to be integrated with the
#    Gegenbauer weight.
#
#  Output:
#
#    real A2(1+N/2), the even Chebyshev coefficients of F.
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
## chebyshev_even1_test() tests chebyshev_even1().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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
  print ( 'chebyshev_even1_test:' )
  print ( '  chebyshev_even1 computes the even Chebyshev coefficients' )
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

  return

def f1 ( x ):

#*****************************************************************************80
#
## f1() defines the function whose Fourier coefficients are desired.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value.
#
  import numpy as np

  a = 2.0
  value = np.cos ( a * x )

  return value

def chebyshev_even2 ( n, f ):

#*****************************************************************************80
#
## chebyshev_even2() returns the even Chebyshev coefficients of F.
#
#  Discussion:
#
#    The coefficients are calculated using the zeros of Tn(x).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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
#  Input:
#
#    integer N, the number of points to use.
#    1 <= N.
#
#    real F(x), the handle for the function to be integrated with the
#    Gegenbauer weight.
#
#  Output:
#
#    real B2(1+N/2), the even Chebyshev coefficients of F.
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
## chebyshev_even2_test() tests chebyshev_even2().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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
  print ( 'chebyshev_even2_test:' )
  print ( '  chebyshev_even2 computes the even Chebyshev coefficients' )
  print ( '  of a function F, using the zeros of Tn(x).' )

  lam = 0.75
  a = 2.0
  n = 6

  b2 = chebyshev_even2 ( n, f2 )

  s = ( n // 2 )
  r8vec_print ( s + 1, b2, '  Computed Coefficients:' )

  return

def f2 ( x ):

#*****************************************************************************80
#
## f2() defines the function whose Fourier coefficients are desired.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value.
#
  import numpy as np

  a = 2.0
  value = np.cos ( a * x )

  return value

def gegenbauer_cc1 ( n, lam, f ):

#*****************************************************************************80
#
## gegenbauer_cc1() estimates the Gegenbauer integral of a function.
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
#    This code is distributed under the MIT license. 
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
#  Input:
#
#    integer N, the number of points to use.
#    1 <= N.
#
#    real LAM, used in the exponent of (1-x^2).
#    -0.5 < LAM.
#
#    real F(x), the handle for the function to be integrated with the
#    Gegenbauer weight.
#
#  Output:
#
#    real WEIGHT, the estimate for the Gegenbauer integral of F.
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
## gegenbauer_cc1_test() tests gegenbauer_cc1().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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
  print ( 'gegenbauer_cc1_test:' )
  print ( '  gegenbauer_cc1 estimates the Gegenbauer integral of' )
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

  return

def f3 ( x ):

#*****************************************************************************80
#
## f3() defines the function whose Fourier coefficients are desired.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value.
#
  import numpy as np

  a = 2.0
  value = np.cos ( a * x )

  return value

def gegenbauer_cc2 ( n, lam, f ):

#*****************************************************************************80
#
## gegenbauer_cc2() estimates the Gegenbauer integral of a function.
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
#    This code is distributed under the MIT license. 
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
#  Input:
#
#    integer N, the number of points to use.
#    1 <= N.
#
#    real LAM, used in the exponent of (1-x^2).
#    -0.5 < LAM.
#
#    real F(x), the handle for the function to be integrated with the
#    Gegenbauer weight.
#
#  Output:
#
#    real WEIGHT, the estimate for the Gegenbauer integral of F.
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
## gegenbauer_cc2_test() tests gegenbauer_cc2().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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
  print ( 'gegenbauer_cc2_test:' )
  print ( '  gegenbauer_cc2 estimates the Gegenbauer integral of' )
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

  return

def f4 ( x ):

#*****************************************************************************80
#
## f4() defines the function whose Fourier coefficients are desired.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    14 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value.
#
  import numpy as np

  a = 2.0
  value = np.cos ( a * x )

  return value

def gegenbauer_cc_test ( ):

#*****************************************************************************80
#
## gegenbauer_cc_test() tests gegenbauer_cc().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
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
  print ( 'gegenbauer_cc_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test gegenbauer_cc().' )

  chebyshev_even1_test ( )
  chebyshev_even2_test ( )
  gegenbauer_cc1_test ( )
  gegenbauer_cc2_test ( )
  r8_mop_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'gegenbauer_cc_test():' )
  print ( '  Normal end of execution.' )
  return

def r8_mop ( i ):

#*****************************************************************************80
#
## r8_mop() returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the power of -1.
#
#  Output:
#
#    real r8_mop, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( ):

#*****************************************************************************80
#
## r8_mop_test() tests r8_mop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'r8_mop_test' )
  print ( '  r8_mop evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  r8_mop(I4)' )
  print ( '' )

  for test in range ( 0, 10 ):
    i4 = rng.integers ( low = -100, high = +100, endpoint = True )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )

  return

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
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
## r8vec2_print_test() tests r8vec2_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'r8vec2_print_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_print prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
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
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

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
  gegenbauer_cc_test ( )
  timestamp ( )

