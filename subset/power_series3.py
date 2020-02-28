#! /usr/bin/env python
#
def power_series3 ( n, a, b ):

#*****************************************************************************80
#
## POWER_SERIES3 computes the power series for H(Z) = G(F(Z)).
#
#  Discussion:
#
#    The power series for G and H are given.
#
#    We assume that
#
#      F(Z) = A1*Z + A2*Z^2 + A3*Z^3 + ... + AN*Z^N
#      G(Z) = B1*Z + B2*Z^2 + B3*Z^3 + ... + BN*Z^N
#      H(Z) = C1*Z + C2*Z^2 + C3*Z^3 + ... + CN*Z^N
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 June 2015
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
#    Input, real A(N), the power series for F.
#
#    Input, real B(N), the power series for G.
#
#    Output, real C(N), the power series for H.
#
  import numpy as np

  c = np.zeros ( n )
  for i in range ( 0, n ):
    c[i] = b[0] * a[i]
#
#  Search for IQ, the index of the first nonzero entry in A.
#
  iq = 0

  for i in range ( 0, n ):

    if ( a[i-1] != 0.0 ):
      iq = i
      break

  d = np.zeros ( n )

  if ( iq != 0 ):

    m = 1

    while ( True ):

      m = m + 1

      if ( n < m * iq ):
        break

      if ( b[m-1] == 0.0 ):
        continue

      r = b[m-1] * a[iq-1] ** m
      c[m*iq-1] = c[m*iq-1] + r

      for j in range ( 1, n-m*iq + 1 ):

        v = 0.0
        for i in range ( 1, j ):
          v = v + d[i-1] * a[j-i+iq-1] * ( m * ( j - i ) - i )

        d[j-1] = ( m * a[j-1] + v / j ) / a[iq-1]

      for i in range ( 1, n-m*iq + 1 ):
        c[i+m*iq-1] = c[i+m*iq-1] + d[i-1] * r

  return c

def power_series3_test ( ):

#*****************************************************************************80
#
## POWER_SERIES3_TEST tests POWER_SERIES3
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print

  n = 4

  print ( '' )
  print ( 'POWER_SERIES3_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POWER_SERIES3 composes a power series' )
 
  a = np.zeros ( n )
  a[0] = 1.0
  a[1] = 1.0
 
  b = np.zeros ( n )
  b[0] = 1.0
  b[1] = 1.0

  print ( '' )
  print ( '  Power series of H(x) = G(F(x))' )
  print ( '' )
  print ( '  Number of terms, N = %d' % ( n ) )

  r8vec_print ( n, a, '  Series for F(x):' )
  r8vec_print ( n, b, '  Series for G(x):' )
 
  c = power_series3 ( n, a, b )
 
  r8vec_print ( n, c, '  Series for H(x):' )
#
#  Terminate.
#
  print ( '' )
  print ( 'POWER_SERIES3_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  power_series3_test ( )
  timestamp ( )

