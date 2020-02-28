#! /usr/bin/env python
#
def bessel_jn_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_JN_VALUES returns some values of the Jn Bessel function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselJ[n,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2015
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

  n_max = 20

  fx_vec = np.array ( ( \
      0.1149034849319005E+00, \
      0.3528340286156377E+00, \
      0.4656511627775222E-01, \
      0.2546303136851206E+00, \
     -0.5971280079425882E-01, \
      0.2497577302112344E-03, \
      0.7039629755871685E-02, \
      0.2611405461201701E+00, \
     -0.2340615281867936E+00, \
     -0.8140024769656964E-01, \
      0.2630615123687453E-09, \
      0.2515386282716737E-06, \
      0.1467802647310474E-02, \
      0.2074861066333589E+00, \
     -0.1138478491494694E+00, \
      0.3873503008524658E-24, \
      0.3918972805090754E-18, \
      0.2770330052128942E-10, \
      0.1151336924781340E-04, \
     -0.1167043527595797E+00 ) )

  nu_vec = np.array ( ( \
     2,  2,  2,  2, \
     2,  5,  5,  5, \
     5,  5, 10, 10, \
    10, 10, 10, 20, \
    20, 20, 20, 20 ))

  x_vec = np.array ( ( \
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

def bessel_jn_values_test ( ):

#*****************************************************************************80
#
## BESSEL_JN_VALUES_TEST demonstrates the use of BESSEL_JN_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BESSEL_JN_VALUES_TEST:' )
  print ( '  BESSEL_JN_VALUES stores values of the Bessel J function. of order NU.' )
  print ( '' )
  print ( '      NU  X           J(NU,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, nu, x, fx = bessel_jn_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %12f  %24.16g' % ( nu, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSEL_JN_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_jn_values_test ( )
  timestamp ( )
