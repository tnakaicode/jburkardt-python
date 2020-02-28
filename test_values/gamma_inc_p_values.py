#! /usr/bin/env python
#
def gamma_inc_p_values ( n_data ):

#*****************************************************************************80
#
## GAMMA_INC_P_VALUES values of the normalized incomplete Gamma function P(A,X)
#
#  Discussion:
#
#    The (normalized) incomplete Gamma function is defined as:
#
#      P(A,X) = 1/Gamma(A) * Integral ( 0 <= T <= X ) T^(A-1) * exp(-T) dT.
#
#    With this definition, for all A and X,
#
#      0 <= P(A,X) <= 1
#
#    and
#
#      P(A,oo) = 1.0
#
#    In Mathematica, the function can be evaluated by:
#
#      1 - GammaRegularized[A,X]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
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

  a_vec = np.array (( \
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
     0.41E+02  ))

  f_vec = (( \
     0.7382350532339351E+00, \
     0.9083579897300343E+00, \
     0.9886559833621947E+00, \
     0.3014646416966613E+00, \
     0.7793286380801532E+00, \
     0.9918490284064973E+00, \
     0.9516258196404043E-01, \
     0.6321205588285577E+00, \
     0.9932620530009145E+00, \
     0.7205974576054322E-01, \
     0.5891809618706485E+00, \
     0.9915368159845525E+00, \
     0.1018582711118352E-01, \
     0.4421745996289254E+00, \
     0.9927049442755639E+00, \
     0.4202103819530612E-01, \
     0.9796589705830716E+00, \
     0.9226039842296429E+00, \
     0.4470785799755852E+00, \
     0.7444549220718699E+00 ))

  x_vec = (( \
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

def gamma_inc_p_values_test ( ):

#*****************************************************************************80
#
## GAMMA_INC_P_VALUES_TEST demonstrates the use of GAMMA_INC_P_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'GAMMA_INC_P_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GAMMA_INC_P_VALUES stores values of an incomplete Gamma function.' )
  print ( '' )
  print ( '      A         X        GAMMA_INC_P(A,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, x, f = gamma_inc_p_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %12f  %24.16g' % ( a, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GAMMA_INC_P_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gamma_inc_p_values_test ( )
  timestamp ( )

