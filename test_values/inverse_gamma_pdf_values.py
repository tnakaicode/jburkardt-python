#! /usr/bin/env python
#
def inverse_gamma_pdf_values ( n_data ):

#*****************************************************************************80
#
## INVERSE_GAMMA_PDF_VALUES returns values of the inverse gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0
#    before the first call.  On each call, the routine increments N_DATA by 1,
#    and returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real ALPHA, BETA, the parameters.
#
#    Output, real X, the argument of the function.
#
#    Output real FX, the value of the function.
#
  import numpy as np

  n_max = 12

  alpha_vec = np.array ( [ \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    2.00, \
    3.00, \
    4.00, \
    5.00 ] )
  beta_vec = np.array ( [ \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    2.00, \
    3.00, \
    4.00, \
    5.00, \
    2.00, \
    2.00, \
    2.00, \
    2.00 ] )
  fx_vec = np.array ( [ \
    0.3032653298563167, \
    0.09735009788392561, \
    0.04702676249392300, \
    0.02757802820576861, \
    0.1839397205857212, \
    0.1673476201113224, \
    0.1353352832366127, \
    0.1026062482798735, \
    0.07606179541223586, \
    0.02535393180407862, \
    0.005634207067573026, \
    0.0009390345112621711 ] )
  x_vec = np.array ( [ \
    1.00, \
    2.00, \
    3.00, \
    4.00, \
    2.00, \
    2.00, \
    2.00, \
    2.00, \
    3.00, \
    3.00, \
    3.00, \
    3.00 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    alpha = 0.0
    beta = 0.0
    x = 0.0
    fx = 0.0
  else:
    alpha = alpha_vec[n_data]
    beta = beta_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, alpha, beta, x, fx

def inverse_gamma_pdf_values_test ( ):

#*****************************************************************************80
#
## INVERSE_GAMMA_PDF_VALUES_TEST tests INVERSE_GAMMA_PDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'INVERSE_GAMMA_PDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  INVERSE_GAMMA_PDF_VALUES returns values of' )
  print ( '  the inverse gamma Probability Density Function.' )
  print ( '' )
  print ( '        ALPHA     BETA       X         PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, alpha, beta, x, fx = inverse_gamma_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8g  %8g  %8g  %24.16g' % ( alpha, beta, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'INVERSE_GAMMA_PDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  inverse_gamma_pdf_values_test ( )
  timestamp ( )

