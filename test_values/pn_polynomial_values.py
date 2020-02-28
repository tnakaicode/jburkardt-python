#! /usr/bin/env python
#
def pn_polynomial_values ( n_data ):

#*****************************************************************************80
#
## PN_POLYNOMIAL_VALUES: selected values of the normalized Legendre polynomials.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, the order of the function.
#
#    Output, real X, the point where the function is evaluated.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 22

  f_vec = np.array ( ( \
    0.7071067811865475, \
    0.3061862178478972, \
   -0.642337649721702, \
   -0.6284815141846855, \
    0.3345637065282053, \
    0.7967179601799685, \
    0.06189376866246124, \
   -0.766588850921089, \
   -0.4444760242953344, \
    0.5450094674858101, \
    0.7167706229835538, \
    0.0000000000000000, \
   -0.2759472322745781, \
   -0.5238320341483518, \
   -0.7155919752205163, \
   -0.823164625090267, \
   -0.8184875533567997, \
   -0.6734983296193094, \
   -0.360134523476992, \
    0.1496662954709581, \
    0.8839665576253438, \
    1.870828693386971 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3 ))

  x_vec = np.array ( ( \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.00E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.90E+00, \
     1.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def pn_polynomial_values_test ( ):

#*****************************************************************************80
#
## PN_POLYNOMIAL_VALUES_TEST tests PN_POLYNOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PN_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PN_POLYNOMIAL_VALUES stores values of the normalized Legendre polynomials.' )
  print ( '' )
  print ( '      N            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = pn_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12g  %24.16g' % ( n, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PN_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  pn_polynomial_values_test ( )
  timestamp ( )

