#! /usr/bin/env python
#
def exp3_int_values ( n_data ):

#*****************************************************************************80
#
## EXP3_INT_VALUES returns some values of the EXP3 integral function.
#
#  Discussion:
#
#    The function is defined by:
#
#      EXP3_INT(x) = Integral ( 0 <= t <= x ) exp ( -t^3 ) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
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
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 20

  fx_vec = np.array ( (
      0.19531249963620212007E-02, \
      0.78124990686775522671E-02, \
      0.31249761583499728667E-01, \
      0.12493899888803079984E+00, \
      0.48491714311363971332E+00, \
      0.80751118213967145286E+00, \
      0.86889265412623270696E+00, \
      0.88861722235357162648E+00, \
      0.89286018500218176869E+00, \
      0.89295351429387631138E+00, \
      0.89297479112737843939E+00, \
      0.89297880579798112220E+00, \
      0.89297950317496621294E+00, \
      0.89297951152951902903E+00, \
      0.89297951156918122102E+00, \
      0.89297951156924734716E+00, \
      0.89297951156924917298E+00, \
      0.89297951156924921121E+00, \
      0.89297951156924921122E+00, \
      0.89297951156924921122E+00 ))

  x_vec = np.array ( (
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
      2.2500000000E+00, \
      2.5000000000E+00, \
      2.7500000000E+00, \
      3.0000000000E+00, \
      3.1250000000E+00, \
      3.2500000000E+00, \
      3.5000000000E+00, \
      3.7500000000E+00, \
      4.0000000000E+00 ))
     
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

def exp3_int_values_test ( ):

#*****************************************************************************80
#
## EXP3_INT_VALUES_TEST demonstrates the use of EXP3_INT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'EXP3_INT_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EXP3_INT_VALUES stores values of the EXP3 integral.' )
  print ( '' )
  print ( '      X         F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = exp3_int_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'EXP3_INT_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  exp3_int_values_test ( )
  timestamp ( )

