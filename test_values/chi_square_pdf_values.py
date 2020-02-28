#! /usr/bin/env python
#
def chi_square_pdf_values ( n_data ):

#*****************************************************************************80
#
## CHI_SQUARE_PDF_VALUES returns some values of the Chi-Square PDF.
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
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real DF, the degrees of freedom.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
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
     0.01E+00, \
     0.01E+00, \
     0.02E+00, \
     0.02E+00, \
     0.40E+00, \
     0.40E+00, \
     0.40E+00, \
     0.40E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     2.00E+00, \
     3.00E+00, \
     4.00E+00, \
     5.00E+00, \
     6.00E+00, \
     1.00E+00, \
     2.00E+00, \
     3.00E+00 ))

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

def chi_square_pdf_values_test ( ):

#*****************************************************************************80
#
## CHI_SQUARE_PDF_VALUES_TEST tests CHI_SQUARE_PDF_VALUES.
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
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CHI_SQUARE_PDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHI_SQUARE_PDF_VALUES stores values of the Chi Square PDF.' )
  print ( '' )
  print ( '      DF      X        CHI_SQUARE_PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, df, x, f = chi_square_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %12g  %24.16g' % ( df, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHI_SQUARE_PDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  chi_square_pdf_values_test ( )
  timestamp ( )

