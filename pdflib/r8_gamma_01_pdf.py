#! /usr/bin/env python
#
def r8_gamma_01_pdf ( alpha, rval ):

#*****************************************************************************80
#
## R8_GAMMA_01_PDF evaluates the PDF of a standard gamma distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 June 2013
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
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
  from sys import exit

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'R8_GAMMA_01_PDF - Fatal error!' )
    print ( '  Parameter ALPHA is not positive.' )
    exit ( 'R8_GAMMA_01_PDF - Fatal error!' )

  if ( rval <= 0.0 ):

    value = 0.0

  else:

    temp = ( alpha - 1.0 ) * np.log ( rval ) - rval - r8_gamma_log ( alpha )

    value = np.exp ( temp )

  return value

def r8_gamma_01_pdf_values ( n_data ):

#*****************************************************************************80
#
## R8_GAMMA_01_PDF_VALUES returns some values of the standard Gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 July 2015
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
#    Output, real ALPHA, the shape parameter.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 10

  alpha_vec = np.array ( ( \
         1.092091484911879, \
         4.147546169663503, \
         2.076535407379806, \
         1.287888961910225, \
        0.2191449888955355, \
        0.3086361453280091, \
         2.006531407488083, \
         3.986434770531281, \
         4.487520304498656, \
         0.472723751058401 ))

  f_vec = np.array ( ( \
    0.00009260811963612823, \
        0.1260335478747823, \
        0.1363536772414351, \
        0.5114450139194701, \
     0.0001230139468263628, \
      0.001870342832511005, \
      0.004476000451227789, \
                       0.0, \
        0.2056668486524041, \
                       0.0 ))

  x_vec = np.array ( ( \
         9.541334553343761, \
          5.39780214905239, \
        0.1942467166183289, \
        0.6545463320909413, \
         6.156639979175331, \
         4.220159083225351, \
         7.424071607424807, \
       -0.4806971028367454, \
          3.18289954879574, \
       -0.3570226383736496 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    alpha = 0.0
    x = 0.0
    f = 0.0
  else:
    alpha = alpha_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, alpha, x, f

def r8_gamma_01_pdf_test ( ):

#*****************************************************************************80
#
## R8_GAMMA_01_PDF_TEST tests R8_GAMMA_01_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt.
#
  import platform

  print ( '' )
  print ( 'R8_GAMMA_01_PDF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_GAMMA_01_PDF evaluates the standard gamma PDF.' )
  print ( '' )
  print ( '           ALPHA          X              PDF(0,1)       PDF(0,1)' )
  print ( '                                         tabulated      computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, alpha, x, pdf1 = r8_gamma_01_pdf_values ( n_data )

    if ( n_data == 0 ): 
      break

    pdf2 = r8_gamma_01_pdf ( alpha, x )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( alpha, x, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAMMA_01_PDF_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_gamma_01_pdf_test ( )
  timestamp ( )

