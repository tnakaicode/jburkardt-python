#! /usr/bin/env python
#
def abram0_values ( n_data ):

#*****************************************************************************80
#
## ABRAM0_VALUES returns some values of the Abramowitz0 function.
#
#  Discussion:
#
#    The function is defined by:
#
#      ABRAM0(X) = integral ( 0 <= T < infinity ) exp ( -T * T - X / T ) dT
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 November 2014
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
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( ( \
     0.87377726306985360531E+00, \
     0.84721859650456925922E+00, \
     0.77288934483988301615E+00, \
     0.59684345853450151603E+00, \
     0.29871735283675888392E+00, \
     0.15004596450516388138E+00, \
     0.11114662419157955096E+00, \
     0.83909567153151897766E-01, \
     0.56552321717943417515E-01, \
     0.49876496603033790206E-01, \
     0.44100889219762791328E-01, \
     0.19738535180254062496E-01, \
     0.86193088287161479900E-02, \
     0.40224788162540127227E-02, \
     0.19718658458164884826E-02, \
     0.10045868340133538505E-02, \
     0.15726917263304498649E-03, \
     0.10352666912350263437E-04, \
     0.91229759190956745069E-06, \
     0.25628287737952698742E-09 ) )

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

def abram0_values_test ( ):

#*****************************************************************************80
#
## ABRAM0_VALUES_TEST demonstrates the use of ABRAM0_VALUES.
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
  print ( 'ABRAM0_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ABRAM0_VALUES stores values of' )
  print ( '  the Abramowitz function of order 0.' )
  print ( '' )
  print ( '      X           FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    [ n_data, x, fx ] = abram0_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ABRAM0_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  abram0_values_test ( )
  timestamp ( )
