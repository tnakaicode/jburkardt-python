#! /usr/bin/env python
#
def logarithmic_integral_values ( n_data ):

#*****************************************************************************80
#
## LOGARITHMIC_INTEGRAL_VALUES returns values of the logarithmic integral LI(X).
#
#  Discussion:
#
#    The logarithmic integral is defined as:
#
#      LI(X) = integral ( 0 <= T <= Z ) dT / log ( T )
#
#    The principal value of the integral is taken.  There is a
#    branch cut discontinuity in the complex plane from -infinity
#    to +1.
#
#    Abramowitz and Stegun assume 1 < X.
#
#    In Mathematica, the function can be evaluated by:
#
#      LogIntegral[x]
#
#    There is a simple relationship with the exponential integral EI:
#
#      LI(X) = EI(LN(X))
#
#    The function LI(X) provides a good approximation to PI(X),
#    the number of primes less than or equal to X.
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
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 28

  f_vec = np.array ( ( \
      0.0000000000000000E+00, \
     -0.3238978959329102E-01, \
     -0.8512648672879405E-01, \
     -0.1574149028946895E+00, \
     -0.2529494192126213E+00, \
     -0.3786710430610880E+00, \
     -0.5468514142104170E+00, \
     -0.7809468775455607E+00, \
     -0.1134011957382327E+01, \
     -0.1775800683423525E+01, \
     -0.2443622553873225E+01, \
     -0.3124190050507211E+01, \
     -0.2872935510329120E+01, \
     -0.2164282524138207E+01, \
     -0.1440351296279408E+01, \
     -0.6864884538258716E+00, \
      0.1250649863152964E+00, \
      0.1045163780117493E+01, \
      0.2967585095039051E+01, \
      0.5253718299558931E+01, \
      0.8519716463711059E+01, \
      0.1360509217709172E+02, \
      0.2193466832805100E+02, \
      0.3604254831722944E+02, \
      0.6051306533791733E+02, \
      0.1037211171690373E+03, \
      0.1810780396816945E+03, \
      0.3211144156746837E+03 ))

  x_vec = np.array ( ( \
     0.000000E+00, \
     0.100000E+00, \
     0.200000E+00, \
     0.300000E+00, \
     0.400000E+00, \
     0.500000E+00, \
     0.600000E+00, \
     0.700000E+00, \
     0.800000E+00, \
     0.900000E+00, \
     0.950000E+00, \
     0.975000E+00, \
     0.103125E+01, \
     0.106250E+01, \
     0.112500E+01, \
     0.125000E+01, \
     0.150000E+01, \
     0.200000E+01, \
     0.400000E+01, \
     0.800000E+01, \
     0.160000E+02, \
     0.320000E+02, \
     0.640000E+02, \
     0.128000E+03, \
     0.256000E+03, \
     0.512000E+03, \
     0.102400E+04, \
     0.204800E+04 ))

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

def logarithmic_integral_values_test ( ):

#*****************************************************************************80
#
## LOGARITHMIC_INTEGRAL_VALUES_TEST demonstrates the use of LOGARITHMIC_INTEGRAL_VALUES.
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
  print ( 'LOGARITHMIC_INTEGRAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LOGARITHMIC_INTEGRAL_VALUES stores values of the LOGARITHMIC_INTEGRAL function.' )
  print ( '' )
  print ( '      X         LOGARITHMIC_INTEGRAL(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = logarithmic_integral_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LOGARITHMIC_INTEGRAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  logarithmic_integral_values_test ( )
  timestamp ( )

