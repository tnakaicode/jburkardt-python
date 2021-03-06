#! /usr/bin/env python3
#
def truncated_normal_a_pdf_values ( n_data ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_PDF_VALUES: values of the Truncated Normal A PDF.
#
#  Discussion:
#
#    The Normal distribution, with mean Mu and standard deviation Sigma,
#    is truncated to the interval [A,+oo).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real MU, the mean of the distribution.
#
#    Output, real SIGMA, the standard deviation of the distribution.
#
#    Output, real A, the lower truncation limit.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 11

  a_vec = np.array ( ( \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0, \
     50.0 ))

  f_vec = np.array ( ( \
     0.01507373507401876, \
     0.01551417047139894, \
     0.01586560931024694, \
     0.01612150073158793, \
     0.01627701240029317, \
     0.01632918226724295, \
     0.01627701240029317, \
     0.01612150073158793, \
     0.01586560931024694, \
     0.01551417047139894, \
     0.01507373507401876 ))

  mu_vec = np.array ( ( \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0, \
     100.0 )) 

  sigma_vec = np.array ( ( \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0, \
    25.0  ))

  x_vec = np.array ( ( \
     90.0, \
     92.0, \
     94.0, \
     96.0, \
     98.0, \
    100.0, \
    102.0, \
    104.0, \
    106.0, \
    108.0, \
    110.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    mu = 0.0
    sigma = 0.0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    mu = mu_vec[n_data]
    sigma = sigma_vec[n_data]
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, mu, sigma, a, x, f

def truncated_normal_a_pdf_values_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_PDF_VALUES_TEST demonstrates the use of TRUNCATED_NORMAL_A_PDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_PDF_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_A_PDF_VALUES stores values of the TRUNCATED_NORMAL_a_PDF function.' )
  print ( '' )
  print ( '            MU         SIGMA             A             X               F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, mu, sigma, a, x, f = truncated_normal_a_pdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12g  %12g  %12g  %12g  %24.16g' % ( mu, sigma, a, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_PDF_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  truncated_normal_a_pdf_values_test ( )
  timestamp ( )

