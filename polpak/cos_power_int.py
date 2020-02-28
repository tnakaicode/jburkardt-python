#! /usr/bin/env python
#
def cos_power_int ( a, b, n ):

#*****************************************************************************80
#
## COS_POWER_INT evaluates the cosine power integral.
#
#  Discussion:
#
#    The function is defined by
#
#      COS_POWER_INT(A,B,N) = Integral ( A <= T <= B ) ( cos ( t ))^n dt
#
#    The algorithm uses the following fact:
#
#      Integral cos^n ( t ) = -(1/n) * (
#        cos^(n-1)(t) * sin(t) + ( n-1 ) * Integral cos^(n-2) ( t ) dt )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters
#
#    Input, real A, B, the limits of integration.
#
#    Input, integer N, the power of the sine function.
#
#    Output, real VALUE, the value of the integral.
#
  import numpy as np
  from sys import exit

  if ( n < 0 ):
    print ( '' )
    print ( 'COS_POWER_INT - Fatal error!' )
    print ( '  Power N < 0.' )
    exit ( 'COS_POWER_INT - Fatal error!' )

  sa = np.sin ( a );
  sb = np.sin ( b );
  ca = np.cos ( a );
  cb = np.cos ( b );

  if ( ( n % 2 ) == 0 ):
    value = b - a
    mlo = 2
  else:
    value = sb - sa
    mlo = 3

  for m in range ( mlo, n + 1, 2 ):
    value = ( ( m - 1 ) * value - ca ** ( m - 1 ) * sa \
                                + cb ** ( m - 1 ) * sb ) / float ( m )

  return value

def cos_power_int_test ( ):

#*****************************************************************************80
#
## COS_POWER_INT_TEST tests COS_POWER_INT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from cos_power_int_values import cos_power_int_values

  print ( '' )
  print ( 'COS_POWER_INT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  COS_POWER_INT returns values of' )
  print ( '  the integral of COS(X)^N from A to B.' )
  print ( '' )
  print ( '      A         B          N      Exact           Computed' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, n, fx = cos_power_int_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = cos_power_int ( a, b, n )

    print ( '  %8f  %8f  %6d  %14e  %14e' % ( a, b, n, fx, fx2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'COS_POWER_INT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cos_power_int_test ( )
  timestamp ( )
