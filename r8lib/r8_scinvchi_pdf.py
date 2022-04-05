#! /usr/bin/env python
#
def r8_scinvchi_pdf ( df, s, x ):

#*****************************************************************************80
#
## R8_SCINVCHI_PDF: PDF for a scaled inverse chi-squared distribution.
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
#    John Burkardt.
#
#  Parameters:
#
#    Input, real DF, the degrees of freedom.
#    0.0 < DF.
#
#    Input, real S, the scale factor.
#    0.0 < S.
#
#    Input, real X, the point where the PDF is evaluated.
#
#    Output, real VALUE, the value of the PDF.
#
  import numpy as np
  from r8_gamma_log import r8_gamma_log

  if ( df <= 0.0 ):
    print ( '' )
    print ( 'R8_SCINVCHI_PDF - Fatal error!' )
    print ( '  Degrees of freedom must be positive.' )
    exit ( 'R8_SCINVCHI_PDF - Fatal error!' )

  if ( s <= 0.0 ):
    print ( '' )
    print ( 'R8_SCINVCHI_PDF - Fatal error!' )
    print ( '  Scale parameter must be positive.' )
    exit ( 'R8_SCINVCHI_PDF - Fatal error!' )

  if ( x <= 0.0 ):

    value = 0.0

  else:

    temp2 = df * 0.5
    temp1 = temp2 * np.log ( temp2 ) + temp2 * np.log ( s ) \
      - ( temp2 * s / x ) \
      - ( temp2 + 1.0 ) * np.log ( x ) - r8_gamma_log ( temp2 )

    value = np.exp ( temp1 )

  return value

def scaled_inverse_chi_square_pdf_values ( n_data ):

#*****************************************************************************80
#
## SCALED_INVERSE_CHI_SQUARE_PDF_VALUES: scaled inverse chi square PDF values.
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
#    Output, real DF, the degrees of freedom.
#
#    Output, real XI, the scale parameter.
#
#    Output, real X, the argument of the function.
#
#    Output real FX, the value of the function.
#
  import numpy as np

  n_max = 18

  df_vec = np.array ( [ \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0 ] )
  fx_vec = np.array ( [ \
     0.7322491280963244, \
     0.3368973499542734, \
     0.9036119633409063, \
     1.026062482798735, \
     0.5968580144169457, \
     0.8953274901880941, \
     0.08500366602520342, \
     0.004539992976248485, \
     0.3661245640481622, \
     0.1684486749771367, \
     0.4518059816704532, \
     0.5130312413993675, \
     0.0008099910956089117, \
     4.122307244877116E-07, \
     0.04250183301260171, \
     0.002269996488124243, \
     0.1830622820240811, \
     0.08422433748856834 ] )
  x_vec = np.array ( [ \
    0.10, \
    0.10, \
    0.20, \
    0.20, \
    0.40, \
    0.40, \
    0.10, \
    0.10, \
    0.20, \
    0.20, \
    0.40, \
    0.40, \
    0.10, \
    0.10, \
    0.20, \
    0.20, \
    0.40, \
    0.40 ] )
  xi_vec = np.array ( [ \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    2.00, \
    2.00, \
    2.00, \
    2.00, \
    2.00, \
    2.00 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    df = 0.0
    xi = 0.0
    x = 0.0
    fx = 0.0
  else:
    df = df_vec[n_data]
    xi = xi_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, df, xi, x, fx

def r8_scinvchi_pdf_test ( ):

#*****************************************************************************80
#
## R8_SCINVCHI_PDF_TEST tests R8_SCINVCHI_PDF.
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
  print ( 'R8_SCINVCHI_PDF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_SCINVCHI_PDF evaluates' )
  print ( '  the scaled inverse Chi Square Probability Density Function.' )
  print ( '' )
  print ( '        DF        XI         X         PDF       PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, df, xi, x, pdf1 = scaled_inverse_chi_square_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_scinvchi_pdf ( df, xi, x  )

    print ( '  %8g  %8g  %8g  %24.16g  %24.16g' % ( df, xi, x, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_SCINVCHI_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_scinvchi_pdf_test ( )
  timestamp ( )

