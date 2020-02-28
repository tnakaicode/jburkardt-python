#! /usr/bin/env python
#
def bessel_ix_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_IX_VALUES returns some values of the Ix Bessel function.
#
#  Discussion:
#
#    This set of data considers the less common case in which the
#    index of the Bessel function In is actually not an integer.
#    We may suggest this case by occasionally replacing the symbol
#    "In" by "Ix".
#
#    The modified Bessel functions In(Z) and Kn(Z) are solutions of
#    the differential equation
#
#      Z^2 W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselI[n,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real NU, the order of the function.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 28

  fx_vec = np.array ( ( \
    0.3592084175833614E+00,  \
    0.9376748882454876E+00,  \
    2.046236863089055E+00,   \
    3.053093538196718E+00,   \
    4.614822903407601E+00,   \
    26.47754749755907E+00,   \
    2778.784603874571E+00,   \
    4.327974627242893E+07,   \
    0.2935253263474798E+00,  \
    1.099473188633110E+00,   \
    21.18444226479414E+00,   \
    2500.906154942118E+00,   \
    2.866653715931464E+20,   \
    0.05709890920304825E+00, \
    0.3970270801393905E+00,  \
    13.76688213868258E+00,   \
    2028.512757391936E+00,   \
    2.753157630035402E+20,   \
    0.4139416015642352E+00,  \
    1.340196758982897E+00,   \
    22.85715510364670E+00,   \
    2593.006763432002E+00,   \
    2.886630075077766E+20,   \
    0.03590910483251082E+00, \
    0.2931108636266483E+00,  \
    11.99397010023068E+00,   \
    1894.575731562383E+00,   \
    2.716911375760483E+20 ) )

  nu_vec = np.array ( ( \
    0.50E+00, \
    0.50E+00, \
    0.50E+00, \
    0.50E+00, \
    0.50E+00, \
    0.50E+00, \
    0.50E+00, \
    0.50E+00, \
    1.50E+00, \
    1.50E+00, \
    1.50E+00, \
    1.50E+00, \
    1.50E+00, \
    2.50E+00, \
    2.50E+00, \
    2.50E+00, \
    2.50E+00, \
    2.50E+00, \
    1.25E+00, \
    1.25E+00, \
    1.25E+00, \
    1.25E+00, \
    1.25E+00, \
    2.75E+00, \
    2.75E+00, \
    2.75E+00, \
    2.75E+00, \
    2.75E+00 ))

  x_vec = np.array ( ( \
      0.2E+00, \
      1.0E+00, \
      2.0E+00, \
      2.5E+00, \
      3.0E+00, \
      5.0E+00, \
     10.0E+00, \
     20.0E+00, \
      1.0E+00, \
      2.0E+00, \
      5.0E+00, \
     10.0E+00, \
     50.0E+00, \
      1.0E+00, \
      2.0E+00, \
      5.0E+00, \
     10.0E+00, \
     50.0E+00, \
      1.0E+00, \
      2.0E+00, \
      5.0E+00, \
     10.0E+00, \
     50.0E+00, \
      1.0E+00, \
      2.0E+00, \
      5.0E+00, \
     10.0E+00, \
     50.0E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    nu = 0
    x = 0.0
    fx = 0.0
  else:
    nu = nu_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, nu, x, fx

def bessel_ix_values_test ( ):

#*****************************************************************************80
#
## BESSEL_IX_VALUES_TEST demonstrates the use of BESSEL_IX_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BESSEL_IX_VALUES_TEST:' )
  print ( '  BESSEL_IX_VALUES stores values of the Bessel I function. of real order NU.' )
  print ( '' )
  print ( '      NU          X           I(NU,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, nu, x, fx = bessel_ix_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( nu, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSEL_IX_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_ix_values_test ( )
  timestamp ( )
