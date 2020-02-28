#! /usr/bin/env python
#
def airy_bi_int_values ( n_data ):

#*****************************************************************************80
#
## AIRY_BI_INT_VALUES returns some values of the integral of the Airy function.
#
#  Discussion:
#
#    The function is defined by:
#
#      AIRY_BI_INT(x) = Integral ( 0 <= t <= x ) Bi(t) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
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
      0.17660819031554631869E-01, \
     -0.15040424806140020451E-01, \
      0.14756446293227661920E-01, \
     -0.11847304264848446271E+00, \
     -0.64916741266165856037E-01, \
      0.97260832464381044540E-01, \
      0.50760058495287539119E-01, \
     -0.37300500963429492179E+00, \
     -0.13962988442666578531E+00, \
     -0.12001735266723296160E-02, \
      0.12018836117890354598E-02, \
      0.36533846550952011043E+00, \
      0.87276911673800812196E+00, \
      0.48219475263803429675E+02, \
      0.44006525804904178439E+06, \
      0.17608153976228301458E+07, \
      0.73779211705220007228E+07, \
      0.14780980310740671617E+09, \
      0.97037614223613433849E+11, \
      0.11632737638809878460E+15 ) )

  x_vec = np.array ( ( \
     -12.0000000000E+00, \
     -10.0000000000E+00, \
      -8.0000000000E+00, \
      -7.5000000000E+00, \
      -7.0000000000E+00, \
      -6.5000000000E+00, \
      -4.0000000000E+00, \
      -1.0000000000E+00, \
      -0.2500000000E+00, \
      -0.0019531250E+00, \
       0.0019531250E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       4.0000000000E+00, \
       8.0000000000E+00, \
       8.5000000000E+00, \
       9.0000000000E+00, \
      10.0000000000E+00, \
      12.0000000000E+00, \
      14.0000000000E+00 ) ) 

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data =n_data + 1

  return n_data, x, fx

def airy_bi_int_values_test ( ):

#*****************************************************************************80
#
## AIRY_BI_INT_VALUES_TEST demonstrates the use of AIRY_BI_INT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'AIRY_BI_INT_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  AIRY_BI_INT_VALUES stores values of' )
  print ( '  the integral of the Airy Bi function.' )
  print ( '' )
  print ( '      X           FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = airy_bi_int_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'AIRY_BI_INT_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  airy_bi_int_values_test ( )
  timestamp ( )

