#! /usr/bin/env python
#
def abram2_values ( n_data ):

#*****************************************************************************80
#
## ABRAM2_VALUES returns some values of the Abramowitz2 function.
#
#  Discussion:
#
#    The function is defined by:
#
#      ABRAM2(x) = Integral ( 0 <= t < infinity ) t^2 * exp( -t^2 - x / t ) dt
# 
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#    special functions,
#    ACM Transactions on Mathematical Software,
#    Volume 22, Number 3, September 1996, pages 288-301.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
     0.44213858162107913430E+00, \
     0.43923379545684026308E+00, \
     0.42789857297092602234E+00, \
     0.38652825661854504406E+00, \
     0.26538204413231368110E+00, \
     0.16848734838334595000E+00, \
     0.13609200032513227112E+00, \
     0.11070330027727917352E+00, \
     0.82126019995530382267E-01, \
     0.74538781999594581763E-01, \
     0.67732034377612811390E-01, \
     0.35641808698811851022E-01, \
     0.17956589956618269083E-01, \
     0.94058737143575370625E-02, \
     0.50809356204299213556E-02, \
     0.28149565414209719359E-02, \
     0.53808696422559303431E-03, \
     0.44821756380146327259E-04, \
     0.46890678427324100410E-05, \
     0.20161544850996420504E-08 ) )

  x_vec = np.array ( ( \
     0.0019531250E+00, \
     0.0078125000E+00, \
     0.0312500000E+00, \
     0.1250000000E+00, \
     0.5000000000E+00, \
     1.0000000000E+00, \
     1.2500000000E+00, \
     1.5000000000E+00, \
     1.8750000000E+00, \
     2.0000000000E+00, \
     2.1250000000E+00, \
     3.0000000000E+00, \
     4.0000000000E+00, \
     5.0000000000E+00, \
     6.0000000000E+00, \
     7.0000000000E+00, \
     10.0000000000E+00, \
     15.0000000000E+00, \
     20.0000000000E+00, \
     40.0000000000E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def abram2_values_test ( ):

#*****************************************************************************80
#
## ABRAM2_VALUES_TEST demonstrates the use of ABRAM2_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 April 2007
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ABRAM2_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ABRAM2_VALUES stores values of' )
  print ( '  the Abramowitz function of order 2.' )
  print ( '' )
  print ( '      X           FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = abram2_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ABRAM2_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  abram2_values_test ( )
  timestamp ( )
