#! /usr/bin/env python
#
def r8_invgam_pdf ( beta, alpha, rval ):

#*****************************************************************************80
#
## R8_INVGAM_PDF evaluates the PDF of an inverse gamma distribution.
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
#    Input, real BETA, the rate parameter.
#    0.0 < BETA.
#
#    Input, real ALPHA, the shape parameter.
#    0.0 < ALPHA.
#
#    Input, real RVAL, the point where the PDF is evaluated.
#
#    Output, real VALUE, the value of the PDF at RVAL.
#
  import numpy as np
  from r8_gamma_log import r8_gamma_log

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'R8_INVGAM_PDF - Fatal error!' )
    print ( '  Parameter ALPHA is not positive.' )
    exit ( 'R8_INVGAM_PDF - Fatal error!' )

  if ( beta <= 0.0 ):
    print ( '' )
    print ( 'R8_INVGAM_PDF - Fatal error!' )
    print ( '  Parameter BETA is not positive.' )
    exit ( 'R8_INVGAM_PDF - Fatal error!' )

  if ( rval <= 0.0 ):

    value = 0.0

  else:

    temp = alpha * np.log ( beta ) - ( alpha + 1.0 ) * np.log ( rval ) \
      - beta / rval - r8_gamma_log ( alpha )

    value = np.exp ( temp )

  return value

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

def r8_invgam_pdf_test ( ):

#*****************************************************************************80
#
## R8_INVGAM_PDF_TEST tests R8_INVGAM_PDF.
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
  print ( 'R8_INVGAM_PDF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_INVGAM_PDF evaluates' )
  print ( '  the inverse gamma Probability Density Function.' )
  print ( '' )
  print ( '        ALPHA     BETA       X         PDF       PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, alpha, beta, x, pdf1 = inverse_gamma_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_invgam_pdf ( beta, alpha, x )

    print ( '  %8g  %8g  %8g  %24.16g  %24.16g' % ( alpha, beta, x, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_INVGAM_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_invgam_pdf_test ( )
  timestamp ( )

