#! /usr/bin/env python
#
def power_series1 ( n, alpha, a ):

#*****************************************************************************80
#
## POWER_SERIES1 computes the power series for G(Z) = (1+F(Z))^ALPHA.
#
#  Discussion:
#
#    The power series for F(Z) is given.
#
#    The form of the power series are:
#
#      F(Z) = A1*Z + A2*Z^2 + A3*Z^3 + ... + AN*Z^N
#
#      G(Z) = B1*Z + B2*Z^2 + B3*Z^3 + ... + BN*Z^N
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the number of terms in the power series.
#
#    Input, real ALPHA, the exponent of 1+F(Z) in the definition of G(Z).
#
#    Input, real A(N), the power series coefficients for F(Z).
#
#    Output, real B(N), the power series coefficients for G(Z).
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):

    v = 0.0

    for i in range ( 0, j + 1 ):
      v = v + b[i] * a[j-i-1] * ( alpha * ( j - i ) - i - 1 )

    b[j] = ( alpha * a[j] + v / float ( j + 1 ) )

  return b

def power_series1_test ( ):

#*****************************************************************************80
#
## POWER_SERIES1_TEST tests POWER_SERIES1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'POWER_SERIES1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POWER_SERIES1 composes a power series' )

  n = 10
  alpha = 7.0
  a = np.zeros ( n )
  a[0] = 1.0

  print ( '' )
  print ( '  Power series of G(x) = (1+F(x))^alpha' )
  print ( '' )
  print ( '  N = %d' % ( n ) )
  print ( '  ALPHA = %g' % ( alpha ) )
  print ( '' )
  print ( '  Series for F(x):' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %12g' % ( a[i] ) ),
    if (  ( ( i + 1 ) % 5 ) == 0 or i == n - 1 ):
      print ( '' )
   
  b = power_series1 ( n, alpha, a )

  print ( '' )
  print ( '  Series for G(x):' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %12g' % ( b[i] ) ),
    if (  ( ( i + 1 ) % 5 ) == 0 or i == n - 1 ):
      print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'POWER_SERIES1_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  power_series1_test ( )
  timestamp ( )

