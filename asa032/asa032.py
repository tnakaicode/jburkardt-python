#! /usr/bin/env python3
#
def asa032_test ( ):

#*****************************************************************************80
#
## asa032_test() tests asa032().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'asa032_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa032().' )

  asa032_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa032_test():' )
  print ( '  Normal end of execution.' )

  return

def asa032_test01 ( ):

#*****************************************************************************80
#
## asa032_test01() tests gamain().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'asa032_test01():' )
  print ( '  gamain() computes the incomplete Gamma function.' )
  print ( '  Compare the result to tabulated values.' )
  print ( '' )
  print ( '      A             X             ', end = '' )
  print ( 'FX                        FX2' )
  print ( '                                 ', end = '' )
  print ( '(Tabulated)               (GAMAIN)                 DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, fx = gamma_inc_p_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2, ifault = gamain ( x, a )

    print ( '  %12.8f  %12.8f  %24.16e  %24.16e  %10.4e' \
      % ( a, x, fx, fx2, np.abs ( fx - fx2 ) ) )

  return

def gamain ( x, p ):

#*****************************************************************************80
#
## gamain() computes the incomplete gamma ratio.
#
#  Discussion:
#
#    A series expansion is used if P > X or X <= 1.  Otherwise, a
#    continued fraction approximation is used.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    Original FORTRAN77 version by G Bhattacharjee.
#    This version by John Burkardt.
#
#  Reference:
#
#    G Bhattacharjee,
#    Algorithm AS 32:
#    The Incomplete Gamma Integral,
#    Applied Statistics,
#    Volume 19, Number 3, 1970, pages 285-287.
#
#  Input:
#
#    real X, P, the parameters of the incomplete 
#    gamma ratio.  0 <= X, and 0 < P.
#
#  Output:
#
#    integer IFAULT, error flag.
#    0, no errors.
#    1, P <= 0.
#    2, X < 0.
#    3, underflow.
#    4, error return from the Log Gamma routine.
#
#    real VALUE, the value of the incomplete gamma ratio.
#
  from scipy.special import gammaln
  import numpy as np

  acu = 1.0E-08
  oflo = 1.0E+37
  uflo = 1.0E-37
#
#  Check the input.
#
  if ( p <= 0.0 ):
    ifault = 1
    value = 0.0
    return value, ifault

  if ( x < 0.0 ):
    ifault = 2
    value = 0.0
    return value, ifault

  if ( x == 0.0 ):
    ifault = 0
    value = 0.0
    return value, ifault

  g = gammaln ( p )

  arg = p * np.log ( x ) - x - g

  if ( arg < np.log ( uflo ) ):
    ifault = 3
    value = 0.0
    return value, ifault

  ifault = 0
  factor = np.exp ( arg )
#
#  Calculation by series expansion.
#
  if ( x <= 1.0 or x < p ):

    gin = 1.0
    term = 1.0
    rn = p

    while ( True ):

      rn = rn + 1.0
      term = term * x / rn
      gin = gin + term

      if ( term <= acu ):
        break

    value = gin * factor / p
    return value, ifault
#
#  Calculation by continued fraction.
#
  a = 1.0 - p
  b = a + x + 1.0
  term = 0.0

  pn = np.zeros ( 6 )

  pn[0] = 1.0
  pn[1] = x
  pn[2] = x + 1.0
  pn[3] = x * b

  gin = pn[2] / pn[3]

  while ( True ):

    a = a + 1.0
    b = b + 2.0
    term = term + 1.0
    an = a * term
    pn[4] = b * pn[2] - an * pn[0]
    pn[5] = b * pn[3] - an * pn[1]

    if ( pn[5] != 0.0 ):

      rn = pn[4] / pn[5]
      dif = np.abs ( gin - rn )
#
#  Absolute error tolerance satisfied?
#
      if ( dif <= acu ):
#
#  Relative error tolerance satisfied?
#
        if ( dif <= acu * rn ):
          value = 1.0 - factor * gin
          break

      gin = rn

    for i in range ( 0, 4 ):
      pn[i] = pn[i+2]

    if ( oflo <= np.abs ( pn[4] ) ):

      for i in range ( 0, 4 ):
        pn[i] = pn[i] / oflo
 
  return value, ifault

def gamma_inc_p_values ( n_data ):

#*****************************************************************************80
#
## gamma_inc_p_values() values of the normalized incomplete Gamma function P(A,X)
#
#  Discussion:
#
#    The (normalized) incomplete Gamma function is defined as:
#
#      P(A,X) = 1/Gamma(A) * Integral ( 0 <= T <= X ) T^(A-1) * exp(-T) dT.
#
#    With this definition, for all A and X,
#
#      0 <= P(A,X) <= 1
#
#    and
#
#      P(A,oo) = 1.0
#
#    In Mathematica, the function can be evaluated by:
#
#      1 - GammaRegularized[A,X]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
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
#    real A, the parameter of the function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  a_vec = np.array (( \
     0.10E+00, \
     0.10E+00, \
     0.10E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.10E+01, \
     0.10E+01, \
     0.10E+01, \
     0.11E+01, \
     0.11E+01, \
     0.11E+01, \
     0.20E+01, \
     0.20E+01, \
     0.20E+01, \
     0.60E+01, \
     0.60E+01, \
     0.11E+02, \
     0.26E+02, \
     0.41E+02  ))

  f_vec = (( \
     0.7382350532339351E+00, \
     0.9083579897300343E+00, \
     0.9886559833621947E+00, \
     0.3014646416966613E+00, \
     0.7793286380801532E+00, \
     0.9918490284064973E+00, \
     0.9516258196404043E-01, \
     0.6321205588285577E+00, \
     0.9932620530009145E+00, \
     0.7205974576054322E-01, \
     0.5891809618706485E+00, \
     0.9915368159845525E+00, \
     0.1018582711118352E-01, \
     0.4421745996289254E+00, \
     0.9927049442755639E+00, \
     0.4202103819530612E-01, \
     0.9796589705830716E+00, \
     0.9226039842296429E+00, \
     0.4470785799755852E+00, \
     0.7444549220718699E+00 ))

  x_vec = (( \
     0.30E-01, \
     0.30E+00, \
     0.15E+01, \
     0.75E-01, \
     0.75E+00, \
     0.35E+01, \
     0.10E+00, \
     0.10E+01, \
     0.50E+01, \
     0.10E+00, \
     0.10E+01, \
     0.50E+01, \
     0.15E+00, \
     0.15E+01, \
     0.70E+01, \
     0.25E+01, \
     0.12E+02, \
     0.16E+02, \
     0.25E+02, \
     0.45E+02 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, x, f

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
  asa032_test ( )
  timestamp ( )

