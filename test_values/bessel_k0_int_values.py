#! /usr/bin/env python
#
def bessel_k0_int_values ( n_data ):

#*****************************************************************************80
#
## BESSEL_K0_INT_VALUES returns some values of the Bessel K0 integral.
#
#  Discussion:
#
#    The function is defined by:
#
#      K0_INT(x) = Integral ( 0 <= t <= x ) K0(t) dt
#
#    The data was reported by McLeod.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
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
     0.78587929563466784589E-02, \
     0.26019991617330578111E-01, \
     0.24311842237541167904E+00, \
     0.39999633750480508861E+00, \
     0.92710252093114907345E+00, \
     0.12425098486237782662E+01, \
     0.14736757343168286825E+01, \
     0.15606495706051741364E+01, \
     0.15673873907283660493E+01, \
     0.15696345532693743714E+01, \
     0.15701153443250786355E+01, \
     0.15706574852894436220E+01, \
     0.15707793116159788598E+01, \
     0.15707942066465767196E+01, \
     0.15707962315469192247E+01, \
     0.15707963262340149876E+01, \
     0.15707963267948756308E+01, \
     0.15707963267948966192E+01, \
     0.15707963267948966192E+01, \
     0.15707963267948966192E+01 ) )

  x_vec = np.array ( ( \
       0.0009765625E+00, \
       0.0039062500E+00, \
       0.0625000000E+00, \
       0.1250000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       2.0000000000E+00, \
       4.0000000000E+00, \
       5.0000000000E+00, \
       6.0000000000E+00, \
       6.5000000000E+00, \
       8.0000000000E+00, \
      10.0000000000E+00, \
      12.0000000000E+00, \
      15.0000000000E+00, \
      20.0000000000E+00, \
      30.0000000000E+00, \
      50.0000000000E+00, \
      80.0000000000E+00, \
     100.0000000000E+00 ) )

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

def bessel_k0_int_values_test ( ):

#*****************************************************************************80
#
## BESSEL_K0_INT_VALUES_TEST demonstrates the use of BESSEL_K0_INT_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'BESSEL_K0_INT_VALUES_TEST:' )
  print ( '  BESSEL_K0_INT_VALUES stores values of the Bessel K integral. of order 0.' )
  print ( '' )
  print ( '      X           Int_K(0,X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = bessel_k0_int_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16g' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BESSEL_K0_INT_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bessel_k0_int_values_test ( )
  timestamp ( )
