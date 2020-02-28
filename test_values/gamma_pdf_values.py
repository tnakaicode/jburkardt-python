#! /usr/bin/env python
#
def gamma_pdf_values ( n_data ):

#*****************************************************************************80
#
## GAMMA_PDF_VALUES returns some values of a Gamma PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 July 2015
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
#    Output, real BETA, the rate parameter.
#
#    Output, real ALPHA, the shape parameter.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 10

  beta_vec = np.array ( ( \
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

  alpha_vec = np.array ( ( \
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
        0.1672017697220646, \
        0.8522122814089312, \
         2.122272611165834, \
     6.993771842317114e-05, \
       0.01679379733182281, \
     6.687464259463117e-10, \
      0.001295436045931343, \
                       0.0, \
       0.01189893036865762, \
        0.3658836103539945 ))

  x_vec = np.array ( ( \
         4.942957250382744, \
        0.2099361564793942, \
       0.07173978623046406, \
         2.587141553904492, \
         4.743179115458788, \
         1.974664495479389, \
         5.126400502735112, \
       -0.1534233427414219, \
        0.5047170879434957, \
         1.456220075613112 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    beta = 0.0
    alpha = 0.0
    x = 0.0
    f = 0.0
  else:
    beta = beta_vec[n_data]
    alpha = alpha_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, beta, alpha, x, f

def gamma_pdf_values_test ( ):

#*****************************************************************************80
#
## GAMMA_PDF_VALUES_TEST demonstrates the use of GAMMA_PDF_VALUES.
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
  import platform

  print ( '' )
  print ( 'GAMMA_PDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GAMMA_PDF_VALUES stores values of the standard Gamma PDF.' )
  print ( '' )
  print ( '           BETA            ALPHA          X               PDF' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, beta, alpha, x, f = gamma_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %14g  %14g  %14g  %24.16g' % ( beta, alpha, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GAMMA_PDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gamma_pdf_values_test ( )
  timestamp ( )

