#! /usr/bin/env python
#
def multinomial_pdf_sizes ( n_data ):

#*****************************************************************************80
#
## MULTINOMIAL_PDF_SIZES returns sizes of some multinomial PDF data.
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
#    Output, integer M, the size of the given problem.
#
  import numpy as np

  n_max = 10

  m_vec = np.array ( ( \
     2, 2, 2, 3, 5, \
     5, 5, 5, 5, 5 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    m = 0
  else:
    m = m_vec[n_data]
    n_data = n_data + 1

  return n_data, m

def multinomial_pdf_values ( n_data, m ):

#*****************************************************************************80
#
## MULTINOMIAL_PDF_VALUES returns some values of the multinomial PDF.
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
#    Input, integer M, the number of outcomes.
#
#    Output, int N, the number of trials.
#
#    Output, real P(M), the probability of each outcome on one trial.
#
#    Output, integer X(M), the number of times each outcome occurred in
#    N trials.
#
#    Output, real PDF, the probability of X.
#
  import numpy as np

  n_max = 10

  n_vec = np.array ( ( \
     3, 4, 3, 3, 3, \
     3, 3, 3, 3, 3 ))

  p_cell = ( \
    ( 0.7, 0.3 ), \
    ( 0.7, 0.3 ), \
    ( 0.5, 0.5 ), \
    ( 0.6, 0.0, 0.4 ), \
    ( 0.6, 0.1, 0.1, 0.1, 0.1 ), \
    ( 0.6, 0.1, 0.1, 0.1, 0.1 ), \
    ( 0.6, 0.1, 0.1, 0.1, 0.1 ), \
    ( 0.6, 0.1, 0.1, 0.1, 0.1 ), \
    ( 0.6, 0.1, 0.1, 0.1, 0.1 ), \
    ( 0.6, 0.1, 0.1, 0.1, 0.1 ) )

  x_cell = ( \
    ( 2, 1 ), \
    ( 2, 2 ), \
    ( 2, 1 ), \
    ( 1, 1, 1 ), \
    ( 3, 0, 0, 0, 0 ), \
    ( 2, 1, 0, 0, 0 ), \
    ( 1, 0, 2, 0, 0 ), \
    ( 1, 0, 0, 1, 1 ), \
    ( 0, 0, 0, 3, 0 ), \
    ( 0, 1, 1, 1, 0 ) )

  pdf_vec = np.array ( ( \
    0.441, \
    0.2646, \
    0.375, \
    0.0, \
    0.216, \
    0.108, \
    0.018, \
    0.036, \
    0.001, \
    0.006 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    p = []
    x = []
    pdf = 0.0
  else:
    n = n_vec[n_data]
    p = p_cell[n_data]
    x = x_cell[n_data]
    pdf = pdf_vec[n_data]
    n_data = n_data + 1

  return n_data, n, p, x, pdf

def multinomial_pdf_values_test ( ):

#*****************************************************************************80
#
##_MULTINOMIAL_PDF_VALUES_TEST tests MULTINOMIAL_PDF_VALUES.
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
  print ( 'MULTINOMIAL_PDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MULTINOMIAL_PDF_VALUES resturns some values of the multinomial PDF.' )
  print ( '  Given M possible outcomes on a single trial,' )
  print ( '  with each outcome having probability P,' )
  print ( '  PDF is the probability that after N trials,' )
  print ( '  outcome I occurred X(I) times.' )
  print ( '' )
  print ( '     N     M     I      P        X        PDF()' )
  
  n_data1 = 0
  n_data2 = 0

  while ( True ):

    n_data1, m            = multinomial_pdf_sizes ( n_data1 )
    n_data2, n, p, x, pdf = multinomial_pdf_values ( n_data2, m )

    if ( n_data1 == 0 ):
      break

    print ( '' )
    for i in range ( 0, m ):
      print ( '              %4d  %8.4f  %4d' % ( i, p[i], x[i] ) )
    print ( '  %4d  %4d                        %14.6g' % ( n, m, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'MULTINOMIAL_PDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  multinomial_pdf_values_test ( )
  timestamp ( )
 
