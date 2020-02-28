#! /usr/bin/env python
#
def r8_invchi_pdf ( df, x ):

#*****************************************************************************80
#
## R8_INVCHI_PDF evaluates the PDF of an inverse chi-squared distribution.
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
#    Input, real X, the point where the PDF is evaluated.
#
#    Output, real VALUE, the value of the PDF at RVAL.
#
  import numpy as np
  from r8_gamma_log import r8_gamma_log
  from sys import exit

  if ( df <= 0.0 ):
    print ( '' )
    print ( 'R8_INVCHI_PDF - Fatal error!' )
    print ( '  Degrees of freedom must be positive.' )
    exit ( 'R8_INVCHI_PDF - Fatal error!' )

  if ( x <= 0.0 ):

    value = 0.0

  else:

    temp2 = df * 0.5;
    temp1 = - temp2 * np.log ( 2.0 ) - ( temp2 + 1.0 ) * np.log ( x ) \
      - 0.5 / x - r8_gamma_log ( temp2 )

    value = np.exp ( temp1 )

  return value

def inverse_chi_square_pdf_values ( n_data ):

#*****************************************************************************80
#
## INVERSE_CHI_SQUARE_PDF_VALUES returns values of the inverse chi square PDF.
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
#    Output, real X, the argument of the function.
#
#    Output real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  df_vec = np.array ( [ \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     1.0, \
     2.0, \
     3.0, \
     4.0, \
     1.0, \
     2.0, \
     3.0, \
     4.0, \
     5.0, \
     3.0, \
     3.0, \
     3.0, \
     3.0, \
     3.0, \
    10.0, \
    10.0, \
    10.0 ] )
  fx_vec = np.array ( [ \
    0.08500366602520342, \
    0.3368973499542734, \
    0.3661245640481622, \
    1.026062482798735, \
    0.4518059816704532, \
    0.8953274901880941, \
    1.129514954176133, \
    1.119159362735118, \
    0.2419707245191433, \
    0.3032653298563167, \
    0.2419707245191433, \
    0.1516326649281584, \
    0.08065690817304778, \
    0.05492391118346530, \
    0.02166329508030457, \
    0.01100204146138436, \
    0.006457369034861447, \
    0.004162370481945731, \
    0.0007897534631674914, \
    0.00001584474249412852, \
    1.511920090468204E-06 ] )
  x_vec = np.array ( [ \
    0.10, \
    0.10, \
    0.20, \
    0.20, \
    0.40, \
    0.40, \
    0.40, \
    0.40, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    1.00, \
    2.00, \
    3.00, \
    4.00, \
    5.00, \
    6.00, \
    1.00, \
    2.00, \
    3.00 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    df = 0.0
    x = 0.0
    fx = 0.0
  else:
    df = df_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1
 
  return n_data, df, x, fx

def r8_invchi_pdf_test ( ):

#*****************************************************************************80
#
## R8_INVCHI_PDF_TEST tests R8_INVCHI_PDF.
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
  print ( 'R8_INVCHI_PDF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_INVCHI_PDF returns values of' )
  print ( '  the inverse Chi Square Probability Density Function.' )
  print ( '' )
  print ( '        DF         X         PDF          PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, df, x, pdf1 = inverse_chi_square_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_invchi_pdf ( df, x )

    print ( '  %8g  %8g  %24.16g  %24.16g' % ( df, x, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_INVCHI_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_invchi_pdf_test ( )
  timestamp ( )

