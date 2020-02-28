#! /usr/bin/env python
#
def bessel_in_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_IN_VALUES returns some values of the In Bessel function.
#
#  Discussion:
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
#    02 January 2015
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
     0.5016687513894678E-02, \
     0.1357476697670383E+00, \
     0.6889484476987382E+00, \
     0.1276466147819164E+01, \
     0.2245212440929951E+01, \
     0.1750561496662424E+02, \
     0.2281518967726004E+04, \
     0.3931278522104076E+08, \
     0.2216842492433190E-01, \
     0.2127399592398527E+00, \
     0.1033115016915114E+02, \
     0.1758380716610853E+04, \
     0.2677764138883941E+21, \
     0.2714631559569719E-03, \
     0.9825679323131702E-02, \
     0.2157974547322546E+01, \
     0.7771882864032600E+03, \
     0.2278548307911282E+21, \
     0.2752948039836874E-09, \
     0.3016963879350684E-06, \
     0.4580044419176051E-02, \
     0.2189170616372337E+02, \
     0.1071597159477637E+21, \
     0.3966835985819020E-24, \
     0.4310560576109548E-18, \
     0.5024239357971806E-10, \
     0.1250799735644948E-03, \
     0.5442008402752998E+19 ) )

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

def bessel_in_values_test ( ):

#*****************************************************************************80
#
## BESSEL_IN_VALUES_TEST demonstrates the use of BESSEL_IN_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BESSEL_IN_VALUES_TEST:' )
  print ( '  BESSEL_IN_VALUES stores values of the Bessel I function. of order NU.' )
  print ( '' )
  print ( '      NU  X           I(NU,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, nu, x, fx = bessel_in_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %12f  %24.16g' % ( nu, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSEL_IN_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_in_values_test ( )
  timestamp ( )
