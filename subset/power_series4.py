#! /usr/bin/env python
#
def power_series4 ( n, a, b ):

#*****************************************************************************80
#
## POWER_SERIES4 computes the power series for H(Z) = G ( 1/F(Z) ).
#
#  Discussion:
#
#    The routine is given the power series for the functions F and G.
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
#    10 June 2014
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
#    Input, real A(N), the power series for F.  A(1) may not be 0.0.
#
#    Input, real B(N), the power series for G.
#
#    Output, real C(N), the power series for H.
#
  import numpy as np
  from sys import exit

  if ( a[0] == 0.0 ):
    print ( '' )
    print ( 'POWER_SERIES4 - Fatal error!' )
    print ( '  A(1) is zero.' )
    exit ( 'POWER_SERIES4 - Fatal error!' )

  c = np.zeros ( n )
  work = np.zeros ( n )

  t = 1.0

  for i in range ( 0, n ):
    t = t / a[0]
    c[i] = b[i] * t
    work[i] = a[i] * t

  for k in range ( 2, n + 1 ):
    s = -work[k-1]
    for i in range ( k, n + 1 ):
      for j in range ( i, n + 1 ):
        c[j-1] = c[j-1] + s * c[j-k]
        work[j-1] = work[j-1] + s * work[j-k]

  return c

def power_series4_test ( ):

#*****************************************************************************80
#
## POWER_SERIES4_TEST tests POWER_SERIES4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print

  n = 10

  print ( '' )
  print ( 'POWER_SERIES4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POWER_SERIES4 composes a power series.' )
  print ( '  Power series of H(x) = G(1/F(x))' )
  print ( '' )
  print ( '  Number of terms N = %d' % ( n ) )

  a = np.zeros ( n )
  for i in range ( 0, n ):
    a[i] = 1.0 / float ( i + 1 )

  b = np.zeros ( n )
  b[0] = 1.0

  r8vec_print ( n, a, '  Series for F(x):' )
  r8vec_print ( n, b, '  Series for G(x):' )
 
  c = power_series4 ( n, a, b )
 
  r8vec_print ( n, c, '  Series for H(x):' )
#
#  Terminate.
#
  print ( '' )
  print ( 'POWER_SERIES4_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  power_series4_test ( )
  timestamp ( )

