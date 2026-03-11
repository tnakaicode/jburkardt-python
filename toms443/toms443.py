#! /usr/bin/env python3
#
def lambert_w_values ( n_data ):

#*****************************************************************************80
#
## lambert_w_values() returns some values of the Lambert W function.
#
#  Discussion:
#
#    The function W(X) is defined implicitly by:
#
#      W(X) * e^W(X) = X
#
#    The function is also known as the "Omega" function.
#
#    In Mathematica, the function can be evaluated by:
#
#      W = ProductLog [ X ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Brian Hayes,
#    "Why W?",
#    The American Scientist,
#    Volume 93, March-April 2005, pages 104-108.
#
#    Eric Weisstein,
#    "Lambert's W-Function",
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1998.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer N_data.  The user sets N_data to 0 before the first call.  
#
#  Output:
#
#    integer N_data.  On each call, the routine increments N_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_data will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 22

  f_vec = np.array ( ( \
    0.0000000000000000E+00, \
    0.3517337112491958E+00, \
    0.5671432904097839E+00, \
    0.7258613577662263E+00, \
    0.8526055020137255E+00, \
    0.9585863567287029E+00, \
    0.1000000000000000E+01, \
    0.1049908894964040E+01, \
    0.1130289326974136E+01, \
    0.1202167873197043E+01, \
    0.1267237814307435E+01, \
    0.1326724665242200E+01, \
    0.1381545379445041E+01, \
    0.1432404775898300E+01, \
    0.1479856830173851E+01, \
    0.1524345204984144E+01, \
    0.1566230953782388E+01, \
    0.1605811996320178E+01, \
    0.1745528002740699E+01, \
    0.3385630140290050E+01, \
    0.5249602852401596E+01, \
    0.1138335808614005E+02 ))

  x_vec = np.array ( ( \
    0.0000000000000000E+00, \
    0.5000000000000000E+00, \
    0.1000000000000000E+01, \
    0.1500000000000000E+01, \
    0.2000000000000000E+01, \
    0.2500000000000000E+01, \
    0.2718281828459045E+01, \
    0.3000000000000000E+01, \
    0.3500000000000000E+01, \
    0.4000000000000000E+01, \
    0.4500000000000000E+01, \
    0.5000000000000000E+01, \
    0.5500000000000000E+01, \
    0.6000000000000000E+01, \
    0.6500000000000000E+01, \
    0.7000000000000000E+01, \
    0.7500000000000000E+01, \
    0.8000000000000000E+01, \
    0.1000000000000000E+02, \
    0.1000000000000000E+03, \
    0.1000000000000000E+04, \
    0.1000000000000000E+07 ))

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

def toms443_test01 ( ):

#*****************************************************************************80
#
## toms443_test01() tests wew_a().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'toms443_test01():' )
  print ( '  wew_a() evaluates Lambert''s W function.' )
  print ( '' )
  print ( '      X      Exact    Computed      Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, w1 = lambert_w_values ( n_data )

    if ( n_data <= 0 ):
      break

    if ( x == 0.0 ):
      w2 = 0.0
    else:
      w2, en = wew_a ( x )

    print ( '  %12.4f  %16.8g  %16.8g  %10.2e' \
      % ( x, w1, w2, np.abs ( w1 - w2 ) ) )

  return

def toms443_test02 ( ):

#*****************************************************************************80
#
## toms443_test02() tests wew_b().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'toms443_test02():' )
  print ( '  wew_b() evaluates Lambert''s W function.' )
  print ( '' )
  print ( '      X      Exact    Computed      Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, w1 = lambert_w_values ( n_data )

    if ( n_data <= 0 ):
      break

    if ( x == 0.0 ):
      w2 = 0.0
    else:
      w2, en = wew_b ( x )

    print ( '  %12.4f  %16.8g  %16.8g  %10.2e' \
      % ( x, w1, w2, np.abs ( w1 - w2 ) ) )

  return

  return

def toms443_test ( ):

#*****************************************************************************80
#
## toms443_test() tests toms443().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 July 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'toms443_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test toms443().' )

  toms443_test01 ( )
  toms443_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'toms443_test():' )
  print ( '  Normal end of execution.' )

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
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

def wew_a ( x ):

#*****************************************************************************80
#
## wew_a() estimates Lambert's W function.
#
#  Discussion:
#
#    For a given X, this routine estimates the solution W of Lambert's 
#    equation:
#
#      X = W * EXP ( W )
#
#    This routine has higher accuracy than WEW_B.
#
#  Modified:
#
#    24 July 2022
#
#  Reference:
#
#    Fred Fritsch, R Shafer, W Crowley,
#    Algorithm 443: Solution of the transcendental equation w e^w = x,
#    Communications of the ACM,
#    October 1973, Volume 16, Number 2, pages 123-124.
#
#  Input:
#
#    real X, the argument of W(X)
#
#  Output:
#
#    real VALUE, the estimated value of W(X).
#
#    real EN, the last relative correction to W(X).
#
  import numpy as np

  c1 = 4.0 / 3.0
  c2 = 7.0 / 3.0
  c3 = 5.0 / 6.0
  c4 = 2.0 / 3.0
#
#  Initial guess.
#
  f = np.log ( x )

  if ( x <= 6.46 ):

    wn = x * ( 1.0 + c1 * x ) / ( 1.0 + x * ( c2 + c3 * x ) )
    zn = f - wn - np.log ( wn )

  else:

    wn = f
    zn = - np.log ( wn )
#
#  Iteration 1.
#
  temp = 1.0 + wn
  y = 2.0 * temp * ( temp + c4 * zn ) - zn
  wn = wn * ( 1.0 + zn * y / ( temp * ( y - zn ) ) )
#
#  Iteration 2.
#
  zn = f - wn - np.log ( wn )
  temp = 1.0 + wn
  temp2 = temp + c4 * zn
  en = zn * temp2 / ( temp * temp2 - 0.5 * zn )
  wn = wn * ( 1.0 + en )

  value = wn

  return value, en

def wew_b ( x ):

#*****************************************************************************80
#
## wew_b() estimates Lambert's W function.
#
#  Discussion:
#
#    For a given X, this routine estimates the solution W of Lambert's 
#    equation:
#
#      X = W * EXP ( W )
#
#    This routine has lower accuracy than WEW_A.
#
#  Modified:
#
#    24 July 2022
#
#  Reference:
#
#    Fred Fritsch, R Shafer, W Crowley,
#    Algorithm 443: Solution of the transcendental equation w e^w = x,
#    Communications of the ACM,
#    October 1973, Volume 16, Number 2, pages 123-124.
#
#  Input:
#
#    real X, the argument of W(X)
#
#  Output:
#
#    real VALUE, the estimated value of W(X).
#
#    real EN, the last relative correction to W(X).
#
  import numpy as np

  c1 = 4.0 / 3.0
  c2 = 7.0 / 3.0
  c3 = 5.0 / 6.0
  c4 = 2.0 / 3.0
#
#  Initial guess.
#
  f = np.log ( x )

  if ( x <= 0.7385 ):
    wn = x * ( 1.0 + c1 * x ) / ( 1.0 + x * ( c2 + c3 * x ) )
  else:
    wn = f - 24.0 * ( ( f + 2.0 ) * f - 3.0 ) \
      / ( ( 0.7 * f + 58.0 ) * f + 127.0 )
#
#  Iteration 1.
#
  zn = f - wn - np.log ( wn )
  temp = 1.0 + wn
  y = 2.0 * temp * ( temp + c4 * zn ) - zn
  en = zn * y / ( temp * ( y - zn ) )
  wn = wn * ( 1.0 + en )

  value = wn

  return value, en

if ( __name__ == '__main__' ):
  timestamp ( )
  toms443_test ( )
  timestamp ( )

