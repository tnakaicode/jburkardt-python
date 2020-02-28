#! /usr/bin/env python
#
def euler_poly_values ( n_data ):

#*****************************************************************************80
#
## EULER_POLY_VALUES returns some values of the Euler polynomials.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      EulerE[n,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
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
#    Output, integer N, the order of the Euler polynomial.
#
#    Output, real X, the argument of the Euler polynomial.
#
#    Output, real FX, the value of the Euler polynomial.
#
  import numpy as np

  n_max = 27

  fx_vec = np.array ( (
      0.100000000000E+01, \
     -0.300000000000E+00, \
     -0.160000000000E+00, \
      0.198000000000E+00, \
      0.185600000000E+00, \
     -0.403680000000E+00, \
     -0.560896000000E+00, \
      0.171878880000E+01, \
      0.318043136000E+01, \
     -0.125394670080E+02, \
     -0.289999384576E+02, \
     -0.625000000000E-01, \
     -0.174240000000E+00, \
     -0.297680000000E+00, \
     -0.404320000000E+00, \
     -0.475260000000E+00, \
     -0.500000000000E+00, \
     -0.475240000000E+00, \
     -0.403680000000E+00, \
     -0.292820000000E+00, \
     -0.153760000000E+00, \
      0.000000000000E+00, \
      0.153760000000E+00, \
      0.292820000000E+00, \
      0.403680000000E+00, \
      0.475240000000E+00, \
      0.500000000000E+00 ))

  n_vec = np.array ( (
     0, \
     1, \
     2, \
     3, \
     4, \
     5, \
     6, \
     7, \
     8, \
     9, \
    10, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5, \
     5 ))

  x_vec = np.array ( (
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
      0.2E+00, \
     -0.5E+00, \
     -0.4E+00, \
     -0.3E+00, \
     -0.2E+00, \
     -0.1E+00, \
      0.0E+00, \
      0.1E+00, \
      0.2E+00, \
      0.3E+00, \
      0.4E+00, \
      0.5E+00, \
      0.6E+00, \
      0.7E+00, \
      0.8E+00, \
      0.9E+00, \
      1.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def euler_poly_values_test ( ):

#*****************************************************************************80
#
## EULER_POLY_VALUES_TEST demonstrates the use of EULER_POLY_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'EULER_POLY_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EULER_POLY_VALUES stores values of the Euler polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = euler_poly_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'EULER_POLY_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  euler_poly_values_test ( )
  timestamp ( )
