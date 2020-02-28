#! /usr/bin/env python3
#
def clausen ( x ):

#*****************************************************************************80
#
## CLAUSEN evaluates the Clausen function Cl2(x).
#
#  Discussion:
#
#    Note that the first coefficient, a0 in Koelbig's paper, 
#    is doubled here, to account for a different convention in
#    Chebyshev coefficients.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Kurt Koelbig,
#    Chebyshev coefficients for the Clausen function Cl2(x),
#    Journal of Computational and Applied Mathematics,
#    Volume 64, Number 3, 1995, pages 295-297.
#
#  Parameters:
#
#    Input, real X, the evaluation point.
#
#    Output, real VALUE, the value of the function.
#
  import numpy as np
#
#  Chebyshev expansion for -pi/2 < x < +pi/2.
#
  n1 = 19
  c1 = np.array ( [ \
    0.05590566394715132269, \
    0.00000000000000000000, \
    0.00017630887438981157, \
    0.00000000000000000000, \
    0.00000126627414611565, \
    0.00000000000000000000, \
    0.00000001171718181344, \
    0.00000000000000000000, \
    0.00000000012300641288, \
    0.00000000000000000000, \
    0.00000000000139527290, \
    0.00000000000000000000, \
    0.00000000000001669078, \
    0.00000000000000000000, \
    0.00000000000000020761, \
    0.00000000000000000000, \
    0.00000000000000000266, \
    0.00000000000000000000, \
    0.00000000000000000003 ] )
#
#  Chebyshev expansion for pi/2 < x < 3pi/2.
#
  n2 = 32
  c2 = np.array ( [ \
    0.00000000000000000000, \
   -0.96070972149008358753, \
    0.00000000000000000000, \
    0.04393661151911392781, \
    0.00000000000000000000, \
    0.00078014905905217505, \
    0.00000000000000000000, \
    0.00002621984893260601, \
    0.00000000000000000000, \
    0.00000109292497472610, \
    0.00000000000000000000, \
    0.00000005122618343931, \
    0.00000000000000000000, \
    0.00000000258863512670, \
    0.00000000000000000000, \
    0.00000000013787545462, \
    0.00000000000000000000, \
    0.00000000000763448721, \
    0.00000000000000000000, \
    0.00000000000043556938, \
    0.00000000000000000000, \
    0.00000000000002544696, \
    0.00000000000000000000, \
    0.00000000000000151561, \
    0.00000000000000000000, \
    0.00000000000000009172, \
    0.00000000000000000000, \
    0.00000000000000000563, \
    0.00000000000000000000, \
    0.00000000000000000035, \
    0.00000000000000000000, \
    0.00000000000000000002 ] )
#
#  The function is periodic.  Wrap X into [-pi/2, 3pi/2].
#
  xa = - 0.5 * np.pi
  xb =   0.5 * np.pi
  xc =   1.5 * np.pi
  x2 = r8_wrap ( x, xa, xc )
#
#  Choose the appropriate expansion.
#
  if ( x2 < xb ):
    x3 = 2.0 * x2 / np.pi
    value = x2 - x2 * np.log ( abs ( x2 ) ) \
      + 0.5 * x2 ** 3 * r8_csevl ( x3, c1, n1 )
  else:
    x3 = 2.0 * x2 / np.pi - 2.0
    value = r8_csevl ( x3, c2, n2 )

  return value

def clausen_values ( n_data ):

#*****************************************************************************80
#
## CLAUSEN_VALUES returns some values of the Clausen's integral.
#
#  Discussion:
#
#    The function is defined by:
#
#      CLAUSEN(x) = Integral ( 0 <= t <= x ) -ln ( 2 * sin ( t / 2 ) ) dt
#
#    The data was reported by McLeod.
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
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964, page 1006.
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#    special functions,
#    ACM Transactions on Mathematical Software,
#    Volume 22, Number 3, September 1996, pages 288-301.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
      0.14137352886760576684E-01, \
      0.13955467081981281934E+00, \
     -0.38495732156574238507E+00, \
      0.84831187770367927099E+00, \
      0.10139591323607685043E+01, \
     -0.93921859275409211003E+00, \
      0.72714605086327924743E+00, \
      0.43359820323553277936E+00, \
     -0.98026209391301421161E-01, \
     -0.56814394442986978080E+00, \
     -0.70969701784448921625E+00, \
      0.99282013254695671871E+00, \
     -0.98127747477447367875E+00, \
     -0.64078266570172320959E+00, \
      0.86027963733231192456E+00, \
      0.39071647608680211043E+00, \
      0.47574793926539191502E+00, \
      0.10105014481412878253E+01, \
      0.96332089044363075154E+00, \
     -0.61782699481929311757E+00 ) )

  x_vec = np.array ( ( \
       0.0019531250E+00, \
       0.0312500000E+00, \
      -0.1250000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
      -1.5000000000E+00, \
       2.0000000000E+00, \
       2.5000000000E+00, \
      -3.0000000000E+00, \
       4.0000000000E+00, \
       4.2500000000E+00, \
      -5.0000000000E+00, \
       5.5000000000E+00, \
       6.0000000000E+00, \
       8.0000000000E+00, \
     -10.0000000000E+00, \
      15.0000000000E+00, \
      20.0000000000E+00, \
     -30.0000000000E+00, \
      50.0000000000E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def r8_csevl ( x, a, n ):

#*****************************************************************************80
#
## R8_CSEVL evaluates a Chebyshev series.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Roger Broucke,
#    Algorithm 446:
#    Ten Subroutines for the Manipulation of Chebyshev Series,
#    Communications of the ACM,
#    Volume 16, Number 4, April 1973, pages 254-256.
#
#  Parameters:
#
#    Input, real X, the evaluation point.
#
#    Input, real CS(N), the Chebyshev coefficients.
#
#    Input, integer N, the number of Chebyshev coefficients.
#
#    Output, real VALUE, the Chebyshev series evaluated at X.
#
  from sys import exit

  if ( n < 1 ):
    print ( '' )
    print ( 'R8_CSEVL - Fatal error!' )
    print ( '  Number of terms <= 0.' )
    exit ( 'R8_CSEVL - Fatal error!' )

  if ( 1000 < n ):
    print ( '' )
    print ( 'R8_CSEVL - Fatal error!' )
    print ( '  Number of terms > 1000.' )
    exit ( 'R8_CSEVL - Fatal error!' )

  if ( x < -1.1 or 1.1 < x ):
    print ( '' )
    print ( 'R8_CSEVL - Fatal error!' )
    print ( '  X outside (-1,+1)' )
    print ( '  X = %g' % ( x ) )
    exit ( 'R8_CSEVL - Fatal error!' )

  b1 = 0.0
  b0 = 0.0

  for i in range ( n - 1, -1, -1 ):
    b2 = b1
    b1 = b0
    b0 = 2.0 * x * b1 - b2 + a[i]

  value = 0.5 * ( b0 - b2 )

  return value

def r8_csevl_test ( ):

#*****************************************************************************80
#
## R8_CSEVL_TEST tests R8_CSEVL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  expcs = np.array ( [ \
   2.532131755504016E+00, \
   1.130318207984970E+00, \
   0.271495339534077E+00, \
   0.044336849848664E+00, \
   0.005474240442094E+00, \
   0.000542926311914E+00, \
   0.000044977322954E+00, \
   0.000003198436462E+00, \
   0.000000199212481E+00, \
   0.000000011036772E+00, \
   0.000000000550590E+00, \
   0.000000000024980E+00, \
   0.000000000001039E+00, \
   0.000000000000040E+00, \
   0.000000000000001E+00 ] )

  print ( '' )
  print ( 'R8_CSEVL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CSEVL evaluates a Chebyshev approximant' )
  print ( '  of N terms at a point X.' )
  print ( '' )
  print ( '  Here we use an approximant to the exponential function' )
  print ( '  and average the absolute error at 21 points.' )
  print ( '' )
  print ( '   N    error' )
  print ( '' )

  for n in range ( 1, 13 ):
    err = 0.0
    for i in range ( -10, 11 ):
      x = float ( i ) / 10.0
      s = r8_csevl ( x, expcs, n )
      err = err + abs ( s - np.exp ( x ) )
    err = err / 21.0
    print ( '  %2d  %14.6g' % ( n, err ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CSEVL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_wrap ( r, rlo, rhi ):

#*****************************************************************************80
#
## R8_WRAP forces an R8 to lie between given limits by wrapping.
#
#  Discussion:
#
#    An R8 is a real value.
#
#  Example:
#
#    RLO = 4.0, RHI = 8.0
#
#     R  Value
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
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, a value.
#
#    Input, real RLO, RHI, the desired bounds.
#
#    Output, real R, a "wrapped" version of the value.
#

#
#  Guarantee RLO2 < RHI2.
#
  rlo2 = min ( rlo, rhi )
  rhi2 = max ( rlo, rhi )
#
#  Find the width.
#
  rwide = rhi2 - rlo2
#
#  Add enough copies of (RHI2-RLO2) to R so that the
#  result ends up in the interval RLO2 - RHI2.
#
  if ( rwide == 0.0 ):
    value = rlo
  elif ( r < rlo2 ):
    n = int ( ( rlo2 - r ) / rwide ) + 1
    value = r + n * rwide
    if ( value == rhi ):
      value = rlo
  else:
    n = int ( ( r - rlo2 ) / rwide )
    value = r - n * rwide
    if ( value == rlo ):
      value = rhi

  return value

def r8_wrap_test ( ):

#*****************************************************************************80
#
## R8_WRAP_TEST tests R8_WRAP
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_uniform_ab import r8_uniform_ab

  a = - 2.0
  b = 12.0
  rhi = 6.5
  rlo = 3.0
  seed = 123456789
  test_num = 20

  print ( '' )
  print ( 'R8_WRAP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_WRAP "wraps" an R8 to lie within an interval:' )
  print ( '' )
  print ( '  Wrapping interval is %f, %f' % ( rlo, rhi ) )
  print ( '' )
  print ( '      R      R8_WRAP ( R )' )
  print ( '' )

  for test in range ( 0, test_num ):

    r, seed = r8_uniform_ab ( a, b, seed )
    r2 = r8_wrap ( r, rlo, rhi )
    print ( '  %14g  %14g' % ( r, r2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_WRAP_TEST' )
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

def clausen_test ( ):

#*****************************************************************************80
#
## CLAUSEN_TEST compares the CLAUSEN function to some tabulated values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CLAUSEN_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CLAUSEN evaluates the Clausen function.' )
  print ( '  Compare its results to tabulated data.' )
  print ( '' )
  print ( '                               Tabulated               Computed' )
  print ( '             X                        FX                     FX        Diff' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = clausen_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = clausen ( x )

    diff = abs ( fx1 - fx2 )

    print ( '  %12f  %24.16f  %24.16f  %6.1e' % ( x, fx1, fx2, diff ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CLAUSEN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  clausen_test ( )
  timestamp ( )


