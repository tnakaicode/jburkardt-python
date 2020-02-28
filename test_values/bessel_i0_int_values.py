#! /usr/bin/env python
#
def bessel_i0_int_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_I0_INT_VALUES returns some values of the Bessel I0 integral.
#
#  Discussion:
#
#    The function is defined by:
#
#      I0_INT(x) = Integral ( 0 <= t <= x ) I0(t) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 December 2014
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

  fx_vec = np.array ( ( \
      0.19531256208818052282E-02, \
     -0.39062549670565734544E-02, \
      0.62520348032546565850E-01, \
      0.12516285581366971819E+00, \
     -0.51051480879740303760E+00, \
      0.10865210970235898158E+01, \
      0.27750019054282535299E+01, \
     -0.13775208868039716639E+02, \
      0.46424372058106108576E+03, \
      0.64111867658021584522E+07, \
     -0.10414860803175857953E+08, \
      0.44758598913855743089E+08, \
     -0.11852985311558287888E+09, \
      0.31430078220715992752E+09, \
     -0.83440212900794309620E+09, \
      0.22175367579074298261E+10, \
      0.58991731842803636487E+10, \
     -0.41857073244691522147E+11, \
      0.79553885818472357663E+12, \
      0.15089715082719201025E+17 ) )

  x_vec = np.array ( ( \
       0.0019531250E+00, \
      -0.0039062500E+00, \
       0.0625000000E+00, \
       0.1250000000E+00, \
      -0.5000000000E+00, \
       1.0000000000E+00, \
       2.0000000000E+00, \
      -4.0000000000E+00, \
       8.0000000000E+00, \
      18.0000000000E+00, \
     -18.5000000000E+00, \
      20.0000000000E+00, \
     -21.0000000000E+00, \
      22.0000000000E+00, \
     -23.0000000000E+00, \
      24.0000000000E+00, \
      25.0000000000E+00, \
     -27.0000000000E+00, \
      30.0000000000E+00, \
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

def bessel_i0_int_values_test ( ):

#*****************************************************************************80
#
## BESSEL_I0_INT_VALUES_TEST demonstrates the use of BESSEL_I0_INT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BESSEL_I0_INT_VALUES_TEST:' )
  print ( '  BESSEL_I0_INT_VALUES stores values of the Bessel I integral. of order 0.' )
  print ( '' )
  print ( '      X           Int_I(0,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_i0_int_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSEL_I0_INT_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_i0_int_values_test ( )
  timestamp ( )
