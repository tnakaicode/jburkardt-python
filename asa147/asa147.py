#! /usr/bin/env python3
#
def asa147_test ( ):

#*****************************************************************************80
#
## asa147_test() tests asa147().
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
  print ( 'asa147_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa147().' )

  asa147_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa147_test():' )
  print ( '  Normal end of execution.' )

  return

def asa147_test01 ( ):

#*****************************************************************************80
#
## asa147_test01() tests gammds().
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
  print ( 'asa147_test01():' )
  print ( '  gammds() computes the incomplete gamma function.' )
  print ( '  Compare to tabulated values.' )
  print ( '' )
  print ( '          A            X        ', end = '' )
  print ( 'FX                        FX2' )
  print ( '                                ', end = '' )
  print ( '(Tabulated)               (GAMMDS)                DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, fx = gamma_inc_p_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2, ifault = gammds ( x, a )

    print ( '  %12.8f  %12.8f  %24.16e  %24.16e  %10.4e' \
      % ( a, x, fx, fx2, np.abs ( fx - fx2 ) ) )

  return

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

def gammds ( x, p ):

#*****************************************************************************80
#
## gammds() computes the incomplete Gamma integral.
#
#  Discussion:
#
#    The parameters must be positive.  An infinite series is used.
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
#    Original FORTRAN77 version by Chi Leung Lau.
#    This version by John Burkardt.
#
#  Reference:
#
#    Chi Leung Lau,
#    Algorithm AS 147:
#    A Simple Series for the Incomplete Gamma Integral,
#    Applied Statistics,
#    Volume 29, Number 1, 1980, pages 113-114.
#
#  Input:
#
#    real X, P, the arguments of the incomplete
#    Gamma integral.  X and P must be greater than 0.
#
#  Output:
#
#    real VALUE, the value of the incomplete Gamma integral.
#
#    integer IFAULT, error flag.
#    0, no errors.
#    1, X <= 0 or P <= 0.
#    2, underflow during the computation.
#
  from scipy.special import gammaln
  import numpy as np

  e = 1.0E-09
  uflo = 1.0E-37
#
#  Check the input.
#
  if ( x <= 0.0 ):
    ifault = 1
    value = 0.0
    return value, ifault

  if ( p <= 0.0 ):
    ifault = 1
    value = 0.0
    return value, ifault
#
#  gammaln() computes the natural logarithm of the gamma function.
#
  arg = p * np.log ( x ) - gammaln ( p + 1.0 ) - x

  if ( arg < np.log ( uflo ) ):
    value = 0.0
    ifault = 2
    return value, ifault

  f = np.exp ( arg )

  if ( f == 0.0 ):
    value = 0.0
    ifault = 2
    return value, ifault

  ifault = 0
#
#  Series begins.
#
  c = 1.0
  value = 1.0
  a = p

  while ( True ):

    a = a + 1.0
    c = c * x / a
    value = value + c

    if ( c <= e * value ):
      break

  value = value * f

  return value, ifault

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
  asa147_test ( )
  timestamp ( )

