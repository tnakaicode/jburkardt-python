#! /usr/bin/env python
#
def airy_hi_values ( n_data ):

#*****************************************************************************80
#
## AIRY_HI_VALUES returns some values of the Airy Hi(x) function.
#
#  Discussion:
#
#    The function is defined by:
#
#      AIRY_HI(x) = Integral ( 0 <= t < infinity ) exp ( x*t-t^3/3) dt / pi
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 December 2014
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
     0.40936798278458884024E+00, \
     0.37495291608048868619E+00, \
     0.22066960679295989454E+00, \
     0.77565356679703713590E-01, \
     0.39638826473124717315E-01, \
     0.38450072575004151871E-01, \
     0.35273216868317898556E-01, \
     0.31768535282502272742E-01, \
     0.28894408288051391369E-01, \
     0.24463284011678541180E-01, \
     0.41053540139998941517E+00, \
     0.44993502381204990817E+00, \
     0.97220515514243332184E+00, \
     0.83764237105104371193E+02, \
     0.80327744952044756016E+05, \
     0.15514138847749108298E+06, \
     0.11995859641733262114E+07, \
     0.21472868855967642259E+08, \
     0.45564115351632913590E+09, \
     0.32980722582904761929E+12 ) )

  x_vec = np.array ( ( \
      -0.0019531250E+00, \
      -0.1250000000E+00, \
      -1.0000000000E+00, \
      -4.0000000000E+00, \
      -8.0000000000E+00, \
      -8.2500000000E+00, \
      -9.0000000000E+00, \
     -10.0000000000E+00, \
     -11.0000000000E+00, \
     -13.0000000000E+00, \
       0.0019531250E+00, \
       0.1250000000E+00, \
       1.0000000000E+00, \
       4.0000000000E+00, \
       7.0000000000E+00, \
       7.2500000000E+00, \
       8.0000000000E+00, \
       9.0000000000E+00, \
      10.0000000000E+00, \
      12.0000000000E+00 ) )

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

def airy_hi_values_test ( ):

#*****************************************************************************80
#
## AIRY_HI_VALUES_TEST demonstrates the use of AIRY_HI_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'AIRY_HI_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  AIRY_HI_VALUES stores values of' )
  print ( '  the Airy function Hi(x).' )
  print ( '' )
  print ( '      X           Hi(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, ai = airy_hi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, ai ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'AIRY_HI_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  airy_hi_values_test ( )
  timestamp ( )

