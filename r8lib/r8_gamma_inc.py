#! /usr/bin/env python
#
def r8_gamma_inc ( p, x ):

#*****************************************************************************80
#
## R8_GAMMA_INC computes the incomplete Gamma function.
#
#  Discussion:
#
#    GAMMA_INC(P,X) = Integral ( 0 <= T <= X ) T^(P-1) EXP(-T) DT / GAMMA(P).
#
#    GAMMA_INC(P,       0) = 0,
#    GAMMA_INC(P,Infinity) = 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    B L Shea,
#    Chi-squared and Incomplete Gamma Integral,
#    Algorithm AS239,
#    Applied Statistics,
#    Volume 37, Number 3, 1988, pages 466-473.
#
#  Parameters:
#
#    Input, real P, the exponent parameter.
#    0.0 < P.
#
#    Input, real X, the integral limit parameter.
#    If X is less than or equal to 0, the value is returned as 0.
#
#    Output, real VALUE, the value of the function.
#
  import numpy as np
  from normal_01 import normal_01_cdf
  from r8_gamma_log import r8_gamma_log
  from sys import exit

  exp_arg_min = -88.0
  overflow = 1.0E+37
  plimit = 1000.0
  tol = 1.0E-07
  xbig = 1.0E+08

  value = 0.0

  if ( p <= 0.0 ):
    print ( '' )
    print ( 'R8_GAMMA_INC - Fatal error!' )
    print ( '  Parameter P <= 0.' )
    exit ( 'R8_GAMMA_INC - Fatal error!' )

  if ( x <= 0.0 ):
    value = 0.0
    return value
#
#  Use a normal approximation if PLIMIT < P.
#
  if ( plimit < p ):
    pn1 = 3.0 * np.sqrt ( p ) * ( ( x / p ) ** ( 1.0 / 3.0 ) + 1.0 / ( 9.0 * p ) - 1.0 )
    cdf = normal_01_cdf ( pn1 )
    value = cdf
    return value
#
#  Is X extremely large compared to P?
#
  if ( xbig < x ):
    value = 1.0
    return value
#
#  Use Pearson's series expansion.
#  (P is not large enough to force overflow in the log of Gamma.
#
  if ( x <= 1.0 or x < p ):

    arg = p * np.log ( x ) - x - r8_gamma_log ( p + 1.0 )
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

    if ( exp_arg_min <= arg ):
      value = np.exp ( arg )
    else:
      value = 0.0

  else:
#
#  Use a continued fraction expansion.
#
    arg = p * np.log ( x ) - x - r8_gamma_log ( p )
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
      pn5 = b * pn3 - a * c * pn1
      pn6 = b * pn4 - a * c * pn2

      if ( 0.0 < abs ( pn6 ) ):

        rn = pn5 / pn6

        if ( abs ( value - rn ) <= min ( tol, tol * rn ) ):

          arg = arg + np.log ( value )

          if ( exp_arg_min <= arg ):
            value = 1.0 - np.exp ( arg )
          else:
            value = 1.0

          return value

        value = rn

      pn1 = pn3
      pn2 = pn4
      pn3 = pn5
      pn4 = pn6
#
#  Rescale terms in continued fraction if terms are large.
#
      if ( overflow <= abs ( pn5 ) ):
        pn1 = pn1 / overflow
        pn2 = pn2 / overflow
        pn3 = pn3 / overflow
        pn4 = pn4 / overflow

  return value

def r8_gamma_inc_test ( ):

#*****************************************************************************80
#
## R8_GAMMA_INC_TEST tests R8_GAMMA_INC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from gamma_inc_values import gamma_inc_values

  print ( '' )
  print ( 'R8_GAMMA_INC_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_GAMMA_INC evaluates the normalized incomplete Gamma' )
  print ( '  function P(A,X).' )
  print ( '' )
  print ( '         A         X         Exact F  R8_GAMMA_INC(A,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, fx = gamma_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamma_inc ( a, x )

    print ( '  %8g  %8g  %14g  %14g' % ( a, x, fx, fx2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAMMA_INC_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_gamma_inc_test ( )
  timestamp ( )

