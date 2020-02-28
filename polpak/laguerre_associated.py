#! /usr/bin/env python
#
def laguerre_associated ( n, m, x ):

#*****************************************************************************80
#
## LAGUERRE_ASSOCIATED evaluates the associated Laguerre polynomials L(N,M)(X) at X.
#
#  Differential equation:
#
#    X Y'' + (M+1-X) Y' + (N-M) Y = 0
#
#  First terms:
#
#    M = 0
#
#    L(0,0)(X) =   1
#    L(1,0)(X) =  -X    +  1
#    L(2,0)(X) =   X^2 -  4 X     +  2
#    L(3,0)(X) =  -X^3 +  9 X^2 -  18 X    +    6
#    L(4,0)(X) =   X^4 - 16 X^3 +  72 X^2 -   96 X +      24
#    L(5,0)(X) =  -X^5 + 25 X^4 - 200 X^3 +  600 X^2 -  600 x    +  120
#    L(6,0)(X) =   X^6 - 36 X^5 + 450 X^4 - 2400 X^3 + 5400 X^2 - 4320 X + 720
#
#    M = 1
#
#    L(0,1)(X) =    0
#    L(1,1)(X) =   -1,
#    L(2,1)(X) =    2 X - 4,
#    L(3,1)(X) =   -3 X^2 + 18 X - 18,
#    L(4,1)(X) =    4 X^3 - 48 X^2 + 144 X - 96
#
#    M = 2
#
#    L(0,2)(X) =    0
#    L(1,2)(X) =    0,
#    L(2,2)(X) =    2,
#    L(3,2)(X) =   -6 X + 18,
#    L(4,2)(X) =   12 X^2 - 96 X + 144
#
#    M = 3
#
#    L(0,3)(X) =    0
#    L(1,3)(X) =    0,
#    L(2,3)(X) =    0,
#    L(3,3)(X) =   -6,
#    L(4,3)(X) =   24 X - 96
#
#    M = 4
#
#    L(0,4)(X) =    0
#    L(1,4)(X) =    0
#    L(2,4)(X) =    0
#    L(3,4)(X) =    0
#    L(4,4)(X) =   24
#
#  Recursion:
#
#    if N = 0:
#
#      L(N,M)(X)   = 0 
#
#    if N = 1:
#
#      L(N,M)(X)   = (M+1-X)
#
#    if 2 <= N:
#
#      L(N,M)(X)   = ( (M+2*N-1-X) * L(N-1,M)(X) 
#                  +   (1-M-N)     * L(N-2,M)(X) ) / N
#
#  Special values:
#
#    For M = 0, the associated Laguerre polynomials L(N,M)(X) are equal 
#    to the Laguerre polynomials L(N)(X).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
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
#  Parameters:
#
#    Input, integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    Input, integer M, the parameter.  M must be nonnegative.
#
#    Input, real X, the point at which the polynomials are to be evaluated.
#
#    Output, real CX(1:N+1), the associated Laguerre polynomials of 
#    degrees 0 through N evaluated at the point X.
#
  import numpy as np
  from sys import exit

  if ( m < 0 ):
    print ( '' )
    print ( 'LAGUERRE_ASSOCIATED - Fatal error!' )
    print ( '  Input value of M = %d' % ( m ) )
    print ( '  but M must be nonnegative.' )
    exit ( 'LAGUERRE_ASSOCIATED - Fatal error!' )

  cx = np.zeros ( n + 1 )

  cx[0] = 1.0

  if ( 0 < n ):

    cx[1] = float ( m + 1 ) - x

    for i in range ( 2, n + 1 ):
      cx[i] = ( ( float (   m + 2 * i - 1 ) - x ) * cx[i-1]    \
              +   float ( - m     - i + 1       ) * cx[i-2] ) \
              /   float (           i )

  return cx

def laguerre_associated_test ( ):

#*****************************************************************************80
#
## LAGUERRE_ASSOCIATED_TEST tests LAGUERRE_ASSOCIATED.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 6
  m_test = np.array ( [ 0, 0, 1, 2, 3, 1 ] )
  x_test = np.array ( [ 0.0, 1.0, 0.0, 0.5, 0.5, 0.5 ] )

  print ( '' )
  print ( 'LAGUERRE_ASSOCIATED_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LAGUERRE_ASSOCIATED evaluates the associated Laguerre polynomials;' )

  for i in range ( 0, 6 ):

    m = m_test[i]
    x = x_test[i]

    print ( '' )
    print ( '  Table of L(N,M)(X) for' )
    print ( '' )
    print ( '  N(max) = %d' % ( n ) )
    print ( '  M      = %d' % ( m ) )
    print ( '  X =      %f' % ( x ) )
    print ( '' )
 
    c = laguerre_associated ( n, m, x )
 
    for j in range ( 0, n + 1 ):
      print ( '  %4d  %12g' % ( j, c[j] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LAGUERRE_ASSOCIATED_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  laguerre_associated_test ( )
  timestamp ( )
