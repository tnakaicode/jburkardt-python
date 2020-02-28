#! /usr/bin/env python
#
def r8_beta_pdf ( alpha, beta, rval ):

#*****************************************************************************80
#
## R8_BETA_PDF evaluates the PDF of a beta distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, real ALPHA, BETA, shape parameters.
#    0.0 < ALPHA, BETA.
#
#    Input, real RVAL, the point where the PDF is evaluated.
#
#    Output, real VALUE, the value of the PDF at RVAL.
#
  import numpy as np
  from r8_gamma_log import r8_gamma_log
  from sys import exit

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'R8_BETA_PDF - Fatal error!' )
    print ( '  Parameter ALPHA is not positive.' )
    exit ( 'R8_BETA_PDF - Fatal error!' )

  if ( beta <= 0.0 ):
    print ( '' )
    print ( 'R8_BETA_PDF - Fatal error!' )
    print ( '  Parameter BETA is not positive.' )
    exit ( 'R8_BETA_PDF - Fatal error!' )

  if ( rval <= 0.0 or 1.0 <= rval ):

    value = 0.0

  else:

    temp = r8_gamma_log ( alpha + beta ) - r8_gamma_log ( alpha ) \
      - r8_gamma_log ( beta )

    value = np.exp ( temp ) * rval ** ( alpha - 1.0 ) * ( 1.0 - rval ) ** ( beta - 1.0 )
 
  return value

def beta_pdf_values ( n_data ):

#*****************************************************************************80
#
## BETA_PDF_VALUES returns some values of the Beta PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 July 2015
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
#    Output, real ALPHA, BETA, the parameters of the function.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 10

  alpha_vec = np.array ( ( \
       1.092091484911879, \
       2.808477213834471, \
       1.287888961910225, \
       3.169828561512062, \
       2.006531407488083, \
    0.009191855792026001, \
       0.472723751058401, \
       4.204237253278341, \
       1.301514988836825, \
       1.758143299519481 ))

  beta_vec = np.array ( ( \
       4.781587882544648, \
       2.076535407379806, \
       0.549783967662353, \
      0.3086361453280091, \
       3.773367432107051, \
       4.487520304498656, \
     0.06808445791730976, \
      0.6155195788227712, \
       4.562418534907164, \
       4.114436583429598 ))

  f_vec = np.array ( ( \
    0.002826137156803199, \
     0.04208950342768649, \
      0.2184064957817208, \
      0.1335142301445414, \
      0.1070571849830009, \
    0.005796394377470491, \
      0.5518796772414584, \
                     0.0, \
        2.87907465409348, \
       2.126992854611924 ) )

  x_vec = np.array ( ( \
      0.8667224264776531, \
     0.04607764003473368, \
     0.02211617261254013, \
      0.4582543823302144, \
      0.8320834756642252, \
      0.3520587633290876, \
       0.898529119425846, \
    -0.01692420862048847, \
     0.09718884992568674, \
      0.2621671905296927 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    alpha = 0.0
    beta = 0.0
    x = 0.0
    f = 0.0
  else:
    alpha = alpha_vec[n_data]
    beta = beta_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, alpha, beta, x, f

def r8_beta_pdf_test ( ):

#*****************************************************************************80
#
## R8_BETA_PDF_TEST demonstrates the use of R8_BETA_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_BETA_PDF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_BETA_PDF evaluates the BETA PDF.' )
  print ( '' )
  print ( '         ALPHA         BETA         X           PDF()         PDF()' )
  print ( '                                                tabulated     computed' )  
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, alpha, beta, x, pdf1 = beta_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_beta_pdf ( alpha, beta, x )

    print ( '  %12g  %12g  %12g  %12g  %12g' % ( alpha, beta, x, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_BETA_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_beta_pdf_test ( )
  timestamp ( )
