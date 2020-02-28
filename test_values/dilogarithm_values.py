#! /usr/bin/env python
#
def dilogarithm_values ( n_data ):

#*****************************************************************************80
#
## DILOGARITHM_VALUES returns some values of the dilogarithm function.
#
#  Discussion:
#
#    The dilogarithm is defined as
#
#      Li_2(X) = - Integral ( 0 <= T <= X ) ln ( 1 - T ) / T dT
#
#    The dilogarithm is also known as Spence's integral. 
#
#    In Abramowitz and Stegun form of the function is different,
#    and is equivalent to evaluated Li_2(1-X).
#
#    The dilogarithm is the special case, with N = 2, of the 
#    polylogarithm Li_N(X).
#
#    In Mathematica, the function can be evaluated by:
#
#      PolyLog[2,X]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2015
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
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 21

  fx_vec = np.array ( (
     0.0000000000000000E+00, \
     0.5063929246449603E-01, \
     0.1026177910993911E+00, \
     0.1560350339454831E+00, \
     0.2110037754397048E+00, \
     0.2676526390827326E+00, \
     0.3261295100754761E+00, \
     0.3866059411605865E+00, \
     0.4492829744712817E+00, \
     0.5143989891542119E+00, \
     0.5822405264650125E+00, \
     0.6531576315069018E+00, \
     0.7275863077163334E+00, \
     0.8060826895177240E+00, \
     0.8893776242860387E+00, \
     0.9784693929303061E+00, \
     0.1074794600008248E+01, \
     0.1180581123830255E+01, \
     0.1299714723004959E+01, \
     0.1440633796970039E+01, \
     0.1644934066848226E+01 ))

  x_vec = np.array ( (
     0.00E+00, \
     0.05E+00, \
     0.10E+00, \
     0.15E+00, \
     0.20E+00, \
     0.25E+00, \
     0.30E+00, \
     0.35E+00, \
     0.40E+00, \
     0.45E+00, \
     0.50E+00, \
     0.55E+00, \
     0.60E+00, \
     0.65E+00, \
     0.70E+00, \
     0.75E+00, \
     0.80E+00, \
     0.85E+00, \
     0.90E+00, \
     0.95E+00, \
     0.10E+01 ))

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

def dilogarithm_values_test ( ):

#*****************************************************************************80
#
## DILOGARITHM_VALUES_TEST demonstrates the use of DILOGARITHM_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'DILOGARITHM_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DILOGARITHM_VALUES stores values of the dilogarithm function.' )
  print ( '' )
  print ( '      X         F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = dilogarithm_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DILOGARITHM_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dilogarithm_values_test ( )
  timestamp ( )

