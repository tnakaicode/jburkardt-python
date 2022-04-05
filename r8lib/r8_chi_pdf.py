#! /usr/bin/env python
#
def r8_chi_pdf ( df, rval ):

#*****************************************************************************80
#
## R8_CHI_PDF evaluates the PDF of a chi-squared distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 July 2015
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
#    Input, real RVAL, the point where the PDF is evaluated.
#
#    Output, real VALUE, the value of the PDF at RVAL.
#
  import numpy as np
  from r8_gamma_log import r8_gamma_log
  from sys import exit

  if ( df <= 0.0 ):
    print ( '' )
    print ( 'R8_CHI_PDF - Fatal error!' )
    print ( '  Degrees of freedom must be positive.' )
    exit ( 'R8_CHI_PDF - Fatal error!' )
      
  if ( rval <= 0.0 ):

    value = 0.0

  else:

    temp2 = df * 0.5;

    temp1 = ( temp2 - 1.0 ) * np.log ( rval ) - 0.5 * rval \
      - temp2 * np.log ( 2.0 ) - r8_gamma_log ( temp2 )

    value = np.exp ( temp1 )

  return value

def r8_chi_pdf_values ( n_data ):

#*****************************************************************************80
#
## R8_CHI_PDF_VALUES returns some values of the standard Gamma PDF.
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
#    Output, real DF, the degrees of freedom
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 21

  df_vec = np.array ( ( \
     1.0,  2.0,  1.0,  2.0,  1.0,  \
     2.0,  3.0,  4.0,  1.0,  2.0,  \
     3.0,  4.0,  5.0,  3.0,  3.0,  \
     3.0,  3.0,  3.0, 10.0, 10.0, \
    10.0 ))

  f_vec = np.array ( ( \
         3.969525474770117, \
        0.4975062395963412, \
         2.792879016972342, \
        0.4950249168745841, \
        0.5164415474672784, \
        0.4093653765389909, \
        0.2065766189869113, \
       0.08187307530779819, \
        0.2419707245191434, \
        0.3032653298563167, \
        0.2419707245191434, \
        0.1516326649281584, \
       0.08065690817304777, \
        0.2075537487102974, \
        0.1541803298037693, \
        0.1079819330263761, \
       0.07322491280963248, \
       0.04865217332964145, \
     0.0007897534631674914, \
       0.00766415502440505, \
       0.02353325907815472 ))

  x_vec = np.array ( ( \
     0.01, \
     0.01, \
     0.02, \
     0.02, \
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
     3.00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    df = 0.0
    x = 0.0
    f = 0.0
  else:
    df = df_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, df, x, f

def r8_chi_pdf_test ( ):

#*****************************************************************************80
#
## R8_CHI_PDF_TEST tests R8_CHI_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 July 2015
#
#  Author:
#
#    John Burkardt.
#
  import platform

  print ( '' )
  print ( 'R8_CHI_PDF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CHI_PDF evaluates the standard chi PDF.' )
  print ( '' )
  print ( '           DF             X              PDF()          PDF()' )
  print ( '                                         tabulated      computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, df, x, pdf1 = r8_chi_pdf_values ( n_data )

    if ( n_data == 0 ): 
      break

    pdf2 = r8_chi_pdf ( df, x )

    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( df, x, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CHI_PDF_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8_chi_pdf_test ( )
  timestamp ( )

