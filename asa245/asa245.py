#! /usr/bin/env python3
#
def asa245_test ( ):

#*****************************************************************************80
#
## asa245_test() tests asa245().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'asa245_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa245().' )

  asa245_test01 ( )
  asa245_test02 ( )
  asa245_test03 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa245_test():' )
  print ( '  Normal end of execution.' )

  return

def asa245_test01 ( ):

#*****************************************************************************80
#
## asa245_test01() tests alngam().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'asa245_test01():' )
  print ( '  alngam() computes the logarithm of the' )
  print ( '  Gamma function.  We compare the result' )
  print ( '  to tabulated values.' )
  print ( '' )
  print ( '          X                     ', end = '' )
  print ( 'FX                        FX2' )
  print ( '                                ', end = '' )
  print ( '(Tabulated)               (ALNGAM)                DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2, ifault = alngam ( x )

    print ( '  %24.16f  %24.16e  %24.16e  %10.4e' \
      % ( x, fx, fx2, np.abs ( fx - fx2 ) ) )

  return

def asa245_test02 ( ):

#*****************************************************************************80
#
## asa245_test02() tests lngamma().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'asa245_test02():' )
  print ( '  lngamma() computes the logarithm of the' )
  print ( '  Gamma function.  We compare the result' )
  print ( '  to tabulated values.' )
  print ( '' )
  print ( '          X                     ', end = '' )
  print ( 'FX                        FX2' )
  print ( '                                ', end = '' )
  print ( '(Tabulated)               (LNGAMMA)                DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2, ier = lngamma ( x )

    print ( '  %24.16f  %24.16e  %24.16e  %10.4e' \
      % ( x, fx, fx2, np.abs ( fx - fx2 ) ) )

  return

def asa245_test03 ( ):

#*****************************************************************************80
#
## asa245_test03() tests gammaln().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    John Burkardt
#
  from scipy.special import gammaln
  import numpy as np

  print ( '' )
  print ( 'asa245_test03():' )
  print ( '  gammaln() computes the logarithm of the' )
  print ( '  Gamma function.' )
  print ( '  gammaln() is a builtin function in scipy.special.' )
  print ( '  We compare the result to tabulated values.' )
  print ( '' )
  print ( '          X                     ', end = '' )
  print ( 'FX                        FX2' )
  print ( '                                ', end = '' )
  print ( '(Tabulated)               (GAMMALN)                DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = gammaln ( x )

    print ( '  %24.16f  %24.16e  %24.16e  %10.4e' \
      % ( x, fx, fx2, np.abs ( fx - fx2 ) ) )

  return

def alngam ( xvalue ):

#*****************************************************************************80
#
## alngam() computes the logarithm of the gamma function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    Original FORTRAN77 version by Allan Macleod.
#    This version by John Burkardt.
#
#  Reference:
#
#    Allan Macleod,
#    Algorithm AS 245,
#    A Robust and Reliable Algorithm for the Logarithm of the Gamma Function,
#    Applied Statistics,
#    Volume 38, Number 2, 1989, pages 397-402.
#
#  Input:
#
#    real XVALUE, the argument of the Gamma function.
#
#  Output:
#
#    real VALUE, the logarithm of the gamma function of X.
#
#    integer IFAULT, error flag.
#    0, no error occurred.
#    1, XVALUE is less than or equal to 0.
#    2, XVALUE is too big.
#
  import numpy as np

  alr2pi = 0.918938533204673

  r1 = np.array ( [ \
    -2.66685511495, \
    -24.4387534237, \
    -21.9698958928, \
     11.1667541262, \
     3.13060547623, \
     0.607771387771, \
     11.9400905721, \
     31.4690115749, \
     15.2346874070 ] )

  r2 = np.array ( [ \
    -78.3359299449, \
    -142.046296688, \
     137.519416416, \
     78.6994924154, \
     4.16438922228, \
     47.0668766060, \
     313.399215894, \
     263.505074721, \
     43.3400022514 ] )

  r3 = np.array ( [ \
    -2.12159572323E+05, \
     2.30661510616E+05, \
     2.74647644705E+04, \
    -4.02621119975E+04, \
    -2.29660729780E+03, \
    -1.16328495004E+05, \
    -1.46025937511E+05, \
    -2.42357409629E+04, \
    -5.70691009324E+02 ] )

  r4 = np.array ( [ \
     0.279195317918525, \
     0.4917317610505968, \
     0.0692910599291889, \
     3.350343815022304, \
     6.012459259764103 ] )

  xlge = 5.10E+05
  xlgst = 1.0E+30

  x = xvalue
  value = 0.0
#
#  Check the input.
#
  if ( xlgst <= x ):
    ifault = 2
    return value, ifault

  if ( x <= 0.0 ):
    ifault = 1
    return value, ifault

  ifault = 0
#
#  Calculation for 0 < X < 0.5 and 0.5 <= X < 1.5 combined.
#
  if ( x < 1.5 ):

    if ( x < 0.5 ):

      value = - np.log ( x )
      y = x + 1.0
#
#  Test whether X < machine epsilon.
#
      if ( y == 1.0 ):
        return value, ifault

    else:

      value = 0.0
      y = x
      x = ( x - 0.5 ) - 0.5

    value = value + x * (((( \
        r1[4]   * y \
      + r1[3] ) * y \
      + r1[2] ) * y \
      + r1[1] ) * y \
      + r1[0] ) / (((( \
                  y \
      + r1[8] ) * y \
      + r1[7] ) * y \
      + r1[6] ) * y \
      + r1[5] )

    return value, ifault
#
#  Calculation for 1.5 <= X < 4.0.
#
  if ( x < 4.0 ):

    y = ( x - 1.0 ) - 1.0

    value = y * (((( \
        r2[4]   * x \
      + r2[3] ) * x \
      + r2[2] ) * x \
      + r2[1] ) * x \
      + r2[0] ) / (((( \
                  x \
      + r2[8] ) * x \
      + r2[7] ) * x \
      + r2[6] ) * x \
      + r2[5] )
#
#  Calculation for 4.0 <= X < 12.0.
#
  elif ( x < 12.0 ):

    value = (((( \
        r3[4]   * x \
      + r3[3] ) * x \
      + r3[2] ) * x \
      + r3[1] ) * x \
      + r3[0] ) / (((( \
                  x \
      + r3[8] ) * x \
      + r3[7] ) * x \
      + r3[6] ) * x \
      + r3[5] )
#
#  Calculation for 12.0 <= X.
#
  else:

    y = np.log ( x )
    value = x * ( y - 1.0 ) - 0.5 * y + alr2pi

    if ( x <= xlge ):

      x1 = 1.0 / x
      x2 = x1 * x1

      value = value + x1 * ( ( \
             r4[2]   * \
        x2 + r4[1] ) * \
        x2 + r4[0] ) / ( ( \
        x2 + r4[4] ) * \
        x2 + r4[3] )

  return value, ifault

def gamma_log_values ( n_data ):

#*****************************************************************************80
#
## gamma_log_values() returns some values of the Log Gamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Log[Gamma[x]]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 November 2014
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
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
      0.1524063822430784E+01, \
      0.7966778177017837E+00, \
      0.3982338580692348E+00, \
      0.1520596783998375E+00, \
      0.0000000000000000E+00, \
     -0.4987244125983972E-01, \
     -0.8537409000331584E-01, \
     -0.1081748095078604E+00, \
     -0.1196129141723712E+00, \
     -0.1207822376352452E+00, \
     -0.1125917656967557E+00, \
     -0.9580769740706586E-01, \
     -0.7108387291437216E-01, \
     -0.3898427592308333E-01, \
     0.00000000000000000E+00, \
     0.69314718055994530E+00, \
     0.17917594692280550E+01, \
     0.12801827480081469E+02, \
     0.39339884187199494E+02, \
     0.71257038967168009E+02 ) )

  x_vec = np.array ( ( \
      0.20E+00, \
      0.40E+00, \
      0.60E+00, \
      0.80E+00, \
      1.00E+00, \
      1.10E+00, \
      1.20E+00, \
      1.30E+00, \
      1.40E+00, \
      1.50E+00, \
      1.60E+00, \
      1.70E+00, \
      1.80E+00, \
      1.90E+00, \
      2.00E+00, \
      3.00E+00, \
      4.00E+00, \
     10.00E+00, \
     20.00E+00, \
     30.00E+00 ) )

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

def lngamma ( z ):

#*****************************************************************************80
#
## lngamma() computes Log(Gamma(X)) using a Lanczos approximation.
#
#  Discussion:
#
#    This algorithm is not part of the Applied Statistics algorithms.
#    It is slower but gives 14 or more significant decimal digits
#    accuracy, except around X = 1 and X = 2.   The Lanczos series from
#    which this algorithm is derived is interesting in that it is a
#    convergent series approximation for the gamma function, whereas
#    the familiar series due to De Moivre (and usually wrongly called
#    the Stirling approximation) is only an asymptotic approximation, as
#    is the true and preferable approximation due to Stirling.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    Original FORTRAN77 version by Alan Miller.
#    This version by John Burkardt.
#
#  Reference:
#
#    Cornelius Lanczos,
#    A precision approximation of the gamma function,
#    SIAM Journal on Numerical Analysis, B,
#    Volume 1, 1964, pages 86-96.
#
#  Input:
#
#    real Z, the argument of the Gamma function.
#
#  Output:
#
#    real VALUE, the logarithm of the gamma function of Z.
#
#    integer IER, error flag.
#    0, no error occurred.
#    1, Z is less than or equal to 0.
#
  import numpy as np

  a = np.array ( [ \
         0.9999999999995183, \
       676.5203681218835, \
    - 1259.139216722289, \
       771.3234287757674, \
     - 176.6150291498386, \
        12.50734324009056, \
       - 0.1385710331296526, \
         0.9934937113930748E-05, \
         0.1659470187408462E-06 ] )

  lnsqrt2pi = 0.9189385332046727

  if ( z <= 0.0 ):
    ier = 1
    value = 0.0
    return value, ier

  ier = 0

  value = 0.0
  tmp = z + 7.0

  for j in range ( 8, 0, -1 ):
    value = value + a[j] / tmp
    tmp = tmp - 1.0

  value = value + a[0]
  value = np.log ( value ) + lnsqrt2pi - ( z + 6.5 ) + \
    ( z - 0.5 ) * np.log ( z + 6.5 )

  return value, ier

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

if ( __name__ == '__main__' ):
  timestamp ( )
  asa245_test ( )
  timestamp ( )

