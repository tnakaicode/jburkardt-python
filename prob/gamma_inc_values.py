#! /usr/bin/env python
#
def gamma_inc_values ( n_data ):

#*****************************************************************************80
#
## GAMMA_INC_VALUES returns some values of the incomplete Gamma function.
#
#  Discussion:
#
#    The (normalized) incomplete Gamma function is defined as:
#
#      Integral ( X <= T < oo ) T^(A-1) * exp(-T) dT.
#
#    In Mathematica, the function can be evaluated by:
#
#      Gamma[A,X]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 April 2016
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
#    Output, real A, the parameter of the function.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  a_vec = np.array ( ( \
     0.10E+00, \
     0.10E+00, \
     0.10E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.10E+01, \
     0.10E+01, \
     0.10E+01, \
     0.11E+01, \
     0.11E+01, \
     0.11E+01, \
     0.20E+01, \
     0.20E+01, \
     0.20E+01, \
     0.60E+01, \
     0.60E+01, \
     0.11E+02, \
     0.26E+02, \
     0.41E+02 ))

  f_vec = np.array ( ( \
    2.490302836300570E+00, \
    0.8718369702247978E+00, \
    0.1079213896175866E+00, \
    1.238121685818417E+00, \
    0.3911298052193973E+00, \
    0.01444722098952533E+00, \
    0.9048374180359596E+00, \
    0.3678794411714423E+00, \
    0.006737946999085467E+00, \
    0.8827966752611692E+00, \
    0.3908330082003269E+00, \
    0.008051456628620993E+00, \
    0.9898141728888165E+00, \
    0.5578254003710746E+00, \
    0.007295055724436130E+00, \
    114.9574754165633E+00, \
    2.440923530031405E+00, \
    280854.6620274718E+00, \
    8.576480283455533E+24, \
    2.085031346403364E+47 ))

  x_vec = np.array ( ( \
     0.30E-01, \
     0.30E+00, \
     0.15E+01, \
     0.75E-01, \
     0.75E+00, \
     0.35E+01, \
     0.10E+00, \
     0.10E+01, \
     0.50E+01, \
     0.10E+00, \
     0.10E+01, \
     0.50E+01, \
     0.15E+00, \
     0.15E+01, \
     0.70E+01, \
     0.25E+01, \
     0.12E+02, \
     0.16E+02, \
     0.25E+02, \
     0.45E+02 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, x, f

def gamma_inc_values_test ( ):

#*****************************************************************************80
#
## GAMMA_INC_VALUES_TEST demonstrates the use of GAMMA_INC_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'GAMMA_INC_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GAMMA_INC_VALUES stores values of the incomplete Gamma function.' )
  print ( '' )
  print ( '      A         X        GAMMA_INC(A,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, f = gamma_inc_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( a, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GAMMA_INC_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gamma_inc_values_test ( )
  timestamp ( )

