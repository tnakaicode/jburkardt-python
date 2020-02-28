#! /usr/bin/env python
#
def r8_exponential_01_pdf ( rval ):

#*****************************************************************************80
#
## R8_EXPONENTIAL_01_PDF: PDF of a standard exponential distribution.
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
#  Parameters:
#
#    Input, real RVAL, the point where the PDF is evaluated.
#
#    Output, real VALUE, the value of the PDF.
#
  import numpy as np

  if ( rval < 0.0 ):
    value = 0.0
  else:
    value = np.exp ( - rval )

  return value

def r8_exponential_01_pdf_values ( n_data ):

#*****************************************************************************80
#
## R8_EXPONENTIAL_01_PDF_VALUES: some values of the standard Exponential PDF.
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

def r8_exponential_01_pdf_test ( ):

#*****************************************************************************80
#
## R8_EXPONENTIAL_01_PDF_TEST tests R8_EXPONENTIAL_01_PDF.
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
  print ( 'R8_EXPONENTIAL_01_PDF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_EXPONENTIAL_01_PDF evaluates the standard exponential pdf.' )
  print ( '' )
  print ( '           X           PDF()            PDF()' )
  print ( '                       tabulated        computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, x, pdf1 = r8_exponential_01_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_exponential_01_pdf ( x )
    print ( '  %14.6g  %14.6g  %14.6g' % ( x, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_EXPONENTIAL_01_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_exponential_01_pdf_test ( )
  timestamp ( )
 
