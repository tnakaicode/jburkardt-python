#! /usr/bin/env python
#
def r8_exponential_pdf ( beta, x ):

#*****************************************************************************80
#
## R8_EXPONENTIAL_PDF evaluates the PDF of an exponential distribution.
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
#    John Burkardt.
#
#  Parameters:
#
#    Input, real BETA, the scale value.
#    0.0 < BETA.
#
#    Input, real X, the point where the PDF is evaluated.
#
#    Output, real VALUE, the value of the PDF at RVAL.
#
  import numpy as np

  if ( beta <= 0.0 ):
    print ( '' )
    print ( 'R8_EXPONENTIAL_PDF - Fatal error!' )
    print ( '  BETA parameter must be positive.' )
    exit ( 'R8_EXPONENTIAL_PDF - Fatal error!' )

  if ( x < 0.0 ):
    value = 0.0
  else:
    value = np.exp ( - x / beta ) / beta

  return value

def r8_exponential_pdf_values ( n_data ):

#*****************************************************************************80
#
## R8_EXPONENTIAL_PDF_VALUES: some values of the Exponential PDF.
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
#    Output, real BETA, the shape parameter.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 10

  beta_vec = np.array ( ( \
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
     0.0001446999730194618, \
       0.06289850821824726, \
        0.3663607831924032, \
        0.3542787877169571, \
     1.472582451176006e-12, \
     1.829637907028298e-06, \
       0.01173398427218792, \
                       0.0, \
        0.1034724689882351, \
          1.95394780436833 ))

  x_vec = np.array ( ( \
         9.558807522740191, \
         5.573123971945631, \
        0.5677992226519164, \
         1.010563614677953, \
         6.303053694254367, \
         4.440343499102481, \
         7.522202212856243, \
      -0.08143245130010748, \
         3.442598613603521, \
       0.03753060499296568 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    beta = 0.0
    x = 0.0
    f = 0.0
  else:
    beta = beta_vec[n_data];
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, beta, x, f

def r8_exponential_pdf_test ( ):

#*****************************************************************************80
#
## R8_EXPONENTIAL_PDF_TEST tests R8_EXPONENTIAL_PDF.
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
  print ( 'R8_EXPONENTIAL_PDF_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_EXPONENTIAL_PDF evaluates the exponential PDF.' )
  print ( '' )
  print ( '           BETA             X          PDF()            PDF()' )
  print ( '                                       tabulated        computed' )
  print ( '' )
  
  n_data = 0

  while ( True ):

    n_data, beta, x, pdf1 = r8_exponential_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    pdf2 = r8_exponential_pdf ( beta, x )
    print ( '  %14.6g  %14.6g  %14.6g  %14.6g' % ( beta, x, pdf1, pdf2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_EXPONENTIAL_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_exponential_pdf_test ( )
  timestamp ( )
 
