#! /usr/bin/env python
#
def lobachevsky_values ( n_data ):

#*****************************************************************************80
#
## LOBACHEVSKY_VALUES returns some values of the Lobachevsky function.
#
#  Discussion:
#
#    The function is defined by:
#
#      LOBACHEVSKY(x) = Integral ( 0 <= t <= x ) -ln ( abs ( cos ( t ) ) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
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
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
     0.12417639065161393857E-08, \
     0.79473344770001088225E-07, \
     0.50867598186208834198E-05, \
     0.32603097901207200319E-03, \
     0.21380536815408214419E-01, \
     0.18753816902083824050E+00, \
     0.83051199971883645115E+00, \
     0.18854362426679034904E+01, \
     0.21315988986516411053E+01, \
     0.21771120185613427221E+01, \
     0.22921027921896650849E+01, \
     0.39137195028784495586E+01, \
     0.43513563983836427904E+01, \
     0.44200644968478185898E+01, \
     0.65656013133623829156E+01, \
     0.10825504661504599479E+02, \
     0.13365512855474227325E+02, \
     0.21131002685639959927E+02, \
     0.34838236589449117389E+02, \
     0.69657062437837394278E+02 ))

  x_vec = np.array ( ( \
       0.0019531250E+00, \
       0.0078125000E+00, \
       0.0312500000E+00, \
       0.1250000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       1.5000000000E+00, \
       2.0000000000E+00, \
       2.5000000000E+00, \
       3.0000000000E+00, \
       4.0000000000E+00, \
       5.0000000000E+00, \
       6.0000000000E+00, \
       7.0000000000E+00, \
      10.0000000000E+00, \
      15.0000000000E+00, \
      20.0000000000E+00, \
      30.0000000000E+00, \
      50.0000000000E+00, \
     100.0000000000E+00 ))

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

def lobachevsky_values_test ( ):

#*****************************************************************************80
#
## LOBACHEVSKY_VALUES_TEST demonstrates the use of LOBACHEVSKY_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LOBACHEVSKY_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LOBACHEVSKY_VALUES stores values of the LOBACHEVSKY function.' )
  print ( '' )
  print ( '      X         LOBACHEVSKY(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = lobachevsky_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LOBACHEVSKY_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lobachevsky_values_test ( )
  timestamp ( )

