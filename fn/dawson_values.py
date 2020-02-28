#! /usr/bin/env python
#
def dawson_values ( n_data ):

#*****************************************************************************80
#
## DAWSON_VALUES returns some values of Dawson's integral.
#
#  Discussion:
#
#    The definition of Dawson's integral is
#
#      D(X) = exp ( -X * X ) * Integral ( 0 <= Y <= X ) exp ( Y * Y ) dY
#
#    Dawson's integral has a maximum at roughly
#
#      X = 0.9241388730
#
#    In Mathematica, the function can be evaluated by:
#
#      Sqrt[Pi] * Exp[-x^2] * I * Erf[I*x] / 2
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
#    Eric Weisstein,
#    CRC Concise Encyclopedia of Mathematics,
#    CRC Press, 1998.
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

  fx_vec = np.array ( ( \
     0.0000000000000000E+00, \
     0.9933599239785286E-01, \
     0.1947510333680280E+00, \
     0.2826316650213119E+00, \
     0.3599434819348881E+00, \
     0.4244363835020223E+00, \
     0.4747632036629779E+00, \
     0.5105040575592318E+00, \
     0.5321017070563654E+00, \
     0.5407243187262987E+00, \
     0.5380795069127684E+00, \
     0.5262066799705525E+00, \
     0.5072734964077396E+00, \
     0.4833975173848241E+00, \
     0.4565072375268973E+00, \
     0.4282490710853986E+00, \
     0.3999398943230814E+00, \
     0.3725593489740788E+00, \
     0.3467727691148722E+00, \
     0.3229743193228178E+00, \
     0.3013403889237920E+00 ))

  x_vec = np.array ( ( \
     0.0E+00, \
     0.1E+00, \
     0.2E+00, \
     0.3E+00, \
     0.4E+00, \
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00, \
     1.1E+00, \
     1.2E+00, \
     1.3E+00, \
     1.4E+00, \
     1.5E+00, \
     1.6E+00, \
     1.7E+00, \
     1.8E+00, \
     1.9E+00, \
     2.0E+00 ))

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

def dawson_values_test ( ):

#*****************************************************************************80
#
## DAWSON_VALUES_TEST demonstrates the use of DAWSON_VALUES.
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
  print ( 'DAWSON_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DAWSON_VALUES stores values of the Dawson integral function.' )
  print ( '' )
  print ( '      X         F(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = dawson_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DAWSON_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  dawson_values_test ( )
  timestamp ( )

