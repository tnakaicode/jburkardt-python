#! /usr/bin/env python
#
def bessel_yx_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_YX_VALUES returns some values of the Yx Bessel function.
#
#  Discussion:
#
#    This set of data considers the less common case in which the
#    index of the Bessel function Kn is actually not an integer.
#    We may suggest this case by occasionally replacing the symbol
#    "Yn" by "Yx".
#
#    In Mathematica, the function can be evaluated by:
#
#      BesselY[n,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 January 2015
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
       -1.748560416961876E+00, \
       -0.4310988680183761E+00, \
        0.2347857104062485E+00, \
        0.4042783022390569E+00, \
        0.4560488207946332E+00, \
       -0.1012177091851084E+00, \
        0.2117088663313982E+00, \
       -0.07280690478506185E+00, \
       -1.102495575160179E+00, \
       -0.3956232813587035E+00, \
        0.3219244429611401E+00, \
        0.1584346223881903E+00, \
        0.02742813676191382E+00, \
       -2.876387857462161E+00, \
       -0.8282206324443037E+00, \
        0.2943723749617925E+00, \
       -0.1641784796149411E+00, \
        0.1105304445562544E+00, \
       -0.9319659251969881E+00, \
       -0.2609445010948933E+00, \
        0.2492796362185881E+00, \
        0.2174410301416733E+00, \
       -0.01578576650557229E+00, \
       -4.023453301501028E+00, \
       -0.9588998694752389E+00, \
        0.2264260361047367E+00, \
       -0.2193617736566760E+00, \
        0.09413988344515077E+00 ) )

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

def bessel_yx_values_test ( ):

#*****************************************************************************80
#
## BESSEL_YX_VALUES_TEST demonstrates the use of BESSEL_YX_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BESSEL_YX_VALUES_TEST:' )
  print ( '  BESSEL_YX_VALUES stores values of the Bessel Y function. of real order NU.' )
  print ( '' )
  print ( '      NU          X           Y(NU,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, nu, x, fx = bessel_yx_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( nu, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSEL_YX_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_yx_values_test ( )
  timestamp ( )
