#! /usr/bin/env python
#
def exponential_01_pdf_values ( n_data ):

#*****************************************************************************80
#
## EXPONENTIAL_01_PDF_VALUES returns some values of the standard exponential PDF.
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
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 10

  f_vec = np.array ( ( \
    0.4959398481993681, \
    0.00856777959135697, \
    0.01720937842266235, \
    0.07507070056996956, \
    0.1679332083261492, \
    0.0, \
    0.399845179478639, \
    0.9005384971416223, \
    0.0, \
    0.05044803826563792 ))

  x_vec = np.array ( ( \
        0.7013006334030669, \
         4.759746670799113, \
         4.062300786629853, \
         2.589324935217918, \
         1.784188948117787, \
       -0.1363469579618277, \
        0.9166778581012469, \
        0.1047623644285883, \
       -0.2589405122149109, \
         2.986811417663269 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def exponential_01_pdf_values_test ( ):

#*****************************************************************************80
#
## EXPONENTIAL_01_PDF_VALUES_TEST tests EXPONENTIAL_01_PDF_VALUES.
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
  print ( 'EXPONENTIAL_01_PDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EXPONENTIAL_01_PDF_VALUES stores values of the unit exponential PDF.' )
  print ( '' )
  print ( '      X         EXPONENTIAL_01_PDF(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = exponential_01_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %24.16g' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'EXPONENTIAL_01_PDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  exponential_01_pdf_values_test ( )
  timestamp ( )
