#! /usr/bin/env python
#
def bessel_kn_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_KN_VALUES returns some values of the Kn Bessel function.
#
#  Discussion:
#
#    The modified Bessel functions In(Z) and Kn(Z) are solutions of
#    the differential equation
#
#      Z^2 * W'' + Z * W' - ( Z^2 + N^2 ) * W = 0.
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselK[n,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
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
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer NU, the order of the function.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 28

  fx_vec = np.array ( ( \
     0.4951242928773287E+02, \
     0.1624838898635177E+01, \
     0.2537597545660559E+00, \
     0.1214602062785638E+00, \
     0.6151045847174204E-01, \
     0.5308943712223460E-02, \
     0.2150981700693277E-04, \
     0.6329543612292228E-09, \
     0.7101262824737945E+01, \
     0.6473853909486342E+00, \
     0.8291768415230932E-02, \
     0.2725270025659869E-04, \
     0.3727936773826211E-22, \
     0.3609605896012407E+03, \
     0.9431049100596467E+01, \
     0.3270627371203186E-01, \
     0.5754184998531228E-04, \
     0.4367182254100986E-22, \
     0.1807132899010295E+09, \
     0.1624824039795591E+06, \
     0.9758562829177810E+01, \
     0.1614255300390670E-02, \
     0.9150988209987996E-22, \
     0.6294369360424535E+23, \
     0.5770856852700241E+17, \
     0.4827000520621485E+09, \
     0.1787442782077055E+03, \
     0.1706148379722035E-20 ) )

  nu_vec = np.array ( ( \
     2,  2,  2,  2, \
     2,  2,  2,  2, \
     3,  3,  3,  3, \
     3,  5,  5,  5, \
     5,  5, 10, 10, \
    10, 10, 10, 20, \
    20, 20, 20, 20 ))

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
     50.0E+00 ) )

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

def bessel_kn_values_test ( ):

#*****************************************************************************80
#
## BESSEL_KN_VALUES_TEST demonstrates the use of BESSEL_KN_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BESSEL_KN_VALUES_TEST:' )
  print ( '  BESSEL_KN_VALUES stores values of the Bessel K function. of order NU.' )
  print ( '' )
  print ( '      NU  X           K(NU,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, nu, x, fx = bessel_kn_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %12f  %24.16g' % ( nu, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSEL_KN_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_kn_values_test ( )
  timestamp ( )
