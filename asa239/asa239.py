#! /usr/bin/env python3
#
def asa239_test ( ):

#*****************************************************************************80
#
## asa239_test() tests asa239().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'asa239_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa239().' )

  asa239_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa239_test():' )
  print ( '  Normal end of execution.' )

  return

def asa239_test01 ( ):

#*****************************************************************************80
#
## asa239_test01() tests gammad().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'asa239_test01():' )
  print ( '  gammad() computes the incomplete gamma function.' )
  print ( '  Compare to tabulated values.' )
  print ( '' )
  print ( '          A            X        ', end = '' )
  print ( 'FX                        FX2' )
  print ( '                                ', end = '' )
  print ( '(Tabulated)               (GAMMAD)                DIFF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, fx = gamma_inc_p_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2, ifault = gammad ( x, a )

    print ( '  %12.8f  %12.8f  %24.16e  %24.16e  %10.4e' \
      % ( a, x, fx, fx2, np.abs ( fx - fx2 ) ) )

  return

def alnorm ( x, upper ):

#*****************************************************************************80
#
## alnorm() computes the cumulative density of the standard normal distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 June 2022
#
#  Author:
#
#    Original FORTRAN77 version by David Hill.
#    This version by John Burkardt.
#
#  Reference:
#
#    David Hill,
#    Algorithm AS 66:
#    The Normal Integral,
#    Applied Statistics,
#    Volume 22, Number 3, 1973, pages 424-427.
#
#  Input:
#
#    real X, is one endpoint of the semi-infinite interval
#    over which the integration takes place.
#
#    logical UPPER, determines whether the upper or lower
#    interval is to be integrated:
#    1 => integrate from X to + Infinity
#    0 => integrate from - Infinity to X.
#
#  Output:
#
#    real VALUE, the integral of the standard normal
#    distribution over the desired interval.
#
  import numpy as np

  a1 = 5.75885480458 
  a2 = 2.62433121679 
  a3 = 5.92885724438 
  b1 = -29.8213557807 
  b2 = 48.6959930692 
  c1 = -0.000000038052 
  c2 = 0.000398064794 
  c3 = -0.151679116635 
  c4 = 4.8385912808 
  c5 = 0.742380924027 
  c6 = 3.99019417011
  con = 1.28
  d1 = 1.00000615302
  d2 = 1.98615381364
  d3 = 5.29330324926
  d4 = -15.1508972451
  d5 = 30.789933034
  ltone = 7.0
  p = 0.39894228044 
  q = 0.39990348504
  r = 0.398942280385
  utzero = 18.66

  up = upper
  z = x

  if ( z < 0.0 ):
    if ( up ):
      up = 0
    else:
      up = 1
    z = - z

  if ( ltone < z and ( ( not up ) or utzero < z ) ):

    if ( up ):
      value = 0.0
    else:
      value = 1.0
 
    return value

  y = 0.5 * z * z

  if ( z <= con ):

    value = 0.5  - z * ( p - q * y \
      / ( y + a1 + b1 \
      / ( y + a2 + b2 \
      / ( y + a3 ))))

  else:

    value = r * np.exp ( - y ) \
      / ( z + c1 + d1 \
      / ( z + c2 + d2 \
      / ( z + c3 + d3 \
      / ( z + c4 + d4 \
      / ( z + c5 + d5 \
      / ( z + c6 ))))))

  if ( not up ):
    value = 1.0  - value

  return value

def gammad ( x, p ):

#*****************************************************************************80
#
## gammad() computes the incomplete Gamma integral.
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
#    Original FORTRAN77 version by B Shea.
#    This version by John Burkardt.
#
#  Reference:
#
#    B Shea,
#    Algorithm AS 239:
#    Chi-squared and Incomplete Gamma Integral,
#    Applied Statistics,
#    Volume 37, Number 3, 1988, pages 466-473.
#
#  Input:
#
#    real X, P, the parameters of the incomplete
#    gamma ratio.  0 <= X, and 0 < P.
#
#  Output:
#
#    real GAMMAD, the value of the incomplete Gamma integral.
#
#    integer IFAULT, error flag.
#    0, no error.
#    1, X < 0 or P <= 0.
#
  from scipy.special import gammaln
  import numpy as np

  elimit = - 88.0
  oflo = 1.0E+37
  plimit = 1000.0
  tol = 1.0E-14
  xbig = 1.0E+08

  value = 0.0
#
#  Check the input.
#
  if ( x < 0.0 ):
    ifault = 1
    return value, ifault

  if ( p <= 0.0 ):
    ifault = 1
    return value, ifault

  ifault = 0

  if ( x == 0.0 ):
    value = 0.0
    return value, ifault
#
#  If P is large, use a normal approximation.
#
  if ( plimit < p ):

    pn1 = 3.0 * np.sqrt ( p ) * ( ( x / p )**( 1.0 / 3.0 ) \
      + 1.0 / ( 9.0 * p ) - 1.0 )

    upper = 0
    value = alnorm ( pn1, upper )
    return value, ifault
#
#  If X is large set GAMMAD = 1.
#
  if ( xbig < x ):
    value = 1.0
    return value, ifault
#
#  Use Pearson's series expansion.
#  (Note that P is not large enough to force overflow in ALOGAM).
#  No need to test IFAULT on exit since P > 0.
#
  if ( x <= 1.0 or x < p ):

    arg = p * np.log ( x ) - x - gammaln ( p + 1.0 )
    c = 1.0
    value = 1.0
    a = p

    while ( True ):

      a = a + 1.0
      c = c * x / a
      value = value + c

      if ( c <= tol ):
        break

    arg = arg + np.log ( value )

    if ( elimit <= arg ):
      value = np.exp ( arg )
    else:
      value = 0.0
#
#  Use a continued fraction expansion.
#
  else:

    arg = p * np.log ( x ) - x - gammaln ( p )
    a = 1.0 - p
    b = a + x + 1.0
    c = 0.0
    pn1 = 1.0
    pn2 = x
    pn3 = x + 1.0
    pn4 = x * b
    value = pn3 / pn4

    while ( True ):

      a = a + 1.0
      b = b + 2.0
      c = c + 1.0
      an = a * c
      pn5 = b * pn3 - an * pn1
      pn6 = b * pn4 - an * pn2

      if ( pn6 != 0.0 ):

        rn = pn5 / pn6

        if ( np.abs ( value - rn ) <= min ( tol, tol * rn ) ):
          break

        value = rn

      pn1 = pn3
      pn2 = pn4
      pn3 = pn5
      pn4 = pn6
#
#  Re-scale terms in continued fraction if terms are large.
#
      if ( oflo <= np.abs ( pn5 ) ):
        pn1 = pn1 / oflo
        pn2 = pn2 / oflo
        pn3 = pn3 / oflo
        pn4 = pn4 / oflo

    arg = arg + np.log ( value )

    if ( elimit <= arg ):
      value = 1.0 - np.exp ( arg )
    else:
      value = 1.0

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
  asa239_test ( )
  timestamp ( )


