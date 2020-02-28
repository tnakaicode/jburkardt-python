#! /usr/bin/env python
#
def bessel_y0_spherical_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_Y0_SPHERICAL_VALUES returns some values of the Spherical Bessel function y0.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Sqrt[Pi/(2*x)] * BesselY[1/2,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2015
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
#    LC: QA47.A34,
#    ISBN: 0-486-61272-4.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  fx_vec = np.array ( ( \
     -0.9950041652780258E+01, \
     -0.4900332889206208E+01, \
     -0.2302652485007213E+01, \
     -0.1375559358182797E+01, \
     -0.8708833866839568E+00, \
     -0.5403023058681397E+00, \
     -0.3019647953972280E+00, \
     -0.1214051020716007E+00, \
      0.1824970143830545E-01, \
      0.1262233859406039E+00, \
      0.2080734182735712E+00, \
      0.2675005078433390E+00, \
      0.3072473814755190E+00, \
      0.3295725974495951E+00, \
      0.3365079788102351E+00, \
      0.3299974988668152E+00, \
      0.3119671174358603E+00, \
      0.2843524095821944E+00, \
      0.2490995600928186E+00, \
      0.2081493978722149E+00, \
      0.1634109052159030E+00 ) )

  x_vec = np.array ( ( \
     0.1E+00, \
     0.2E+00, \
     0.4E+00, \
     0.6E+00, \
     0.8E+00, \
     1.0E+00, \
     1.2E+00, \
     1.4E+00, \
     1.6E+00, \
     1.8E+00, \
     2.0E+00, \
     2.2E+00, \
     2.4E+00, \
     2.6E+00, \
     2.8E+00, \
     3.0E+00, \
     3.2E+00, \
     3.4E+00, \
     3.6E+00, \
     3.8E+00, \
     4.0E+00  ) )

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

def bessel_y0_spherical_values_test ( ):

#*****************************************************************************80
#
## BESSEL_Y0_SPHERICAL_VALUES_TEST tests BESSEL_Y0_SPHERICAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BESSEL_Y0_SPHERICAL_VALUES_TEST:' )
  print ( '  BESSEL_Y0_SPHERICAL_VALUES stores values of the spherical Bessel Y function. of order 0.' )
  print ( '' )
  print ( '      X        Spherical Y(0,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_y0_spherical_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSEL_Y0_SPHERICAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_y0_spherical_values_test ( )
  timestamp ( )
