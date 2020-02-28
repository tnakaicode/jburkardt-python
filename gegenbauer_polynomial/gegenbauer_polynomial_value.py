#! /usr/bin/env python3
#
def gegenbauer_polynomial_value ( m, n, alpha, x ):

#*****************************************************************************80
#
## GEGENBAUER_POLYNOMIAL_VALUE computes the Gegenbauer polynomials C(I,ALPHA)(X).
#
#  Differential equation:
#
#    (1-X*X) Y'' - (2 ALPHA + 1) X Y' + M (M + 2 ALPHA) Y = 0
#
#  Recursion:
#
#    C(0,ALPHA,X) = 1,
#    C(1,ALPHA,X) = 2*ALPHA*X
#    C(M,ALPHA,X) = (  ( 2*M-2+2*ALPHA) * X * C(M-1,ALPHA,X) 
#                    + (  -M+2-2*ALPHA)   *   C(M-2,ALPHA,X) ) / M
#
#  Restrictions:
#
#    ALPHA must be greater than -0.5.
#
#  Special values:
#
#    If ALPHA = 1, the Gegenbauer polynomials reduce to the Chebyshev
#    polynomials of the second kind.
#
#  Norm:
#
#    Integral ( -1 <= X <= 1 ) ( 1 - X^2 )^( ALPHA - 0.5 ) * C(M,ALPHA,X)^2 dX
#
#    = PI * 2^( 1 - 2 * ALPHA ) * Gamma ( M + 2 * ALPHA ) 
#      / ( M! * ( M + ALPHA ) * ( Gamma ( ALPHA ) )^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input, integer M, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    Input, integer N, the number of evaluation points.
#
#    Input, real ALPHA, a parameter which is part of the definition of
#    the Gegenbauer polynomials.  It must be greater than -0.5.
#
#    Input, real X(N), the evaluation points.
#
#    Output, real C(1:M+1,N), the values of Gegenbauer polynomials 0 through M
#    at the N points X.  
#
  import numpy as np
  from gegenbauer_alpha_check import gegenbauer_alpha_check
  from sys import exit

  check = gegenbauer_alpha_check ( alpha )

  if ( not check ):
    print ( '' )
    print ( 'GEGENBAUER_POLYNOMIAL_VALUE - Fatal error!' )
    print ( '  GEGENBAUER_ALPHA_CHECK failed.' )
    exit ( 'GEGENBAUER_POLYNOMIAL_VALUE - Fatal error!' )

  c = np.zeros ( [ m + 1, n ] )

  if ( m < 0 ):
    return c

  for j in range ( 0, n ):
    c[0,j] = 1.0

  if ( n == 0 ):
    return c

  if ( m < 1 ):
    return c

  for j in range ( 0, n ):
    c[1,j] = 2.0 * alpha * x[j]

  for i in range ( 2, m + 1 ):
    for j in range ( 0, n ):
      c[i,j] = (  (     2 * i - 2  + 2.0 * alpha ) * x[j] * c[i-1,j]   \
               +  (       - i + 2  - 2.0 * alpha ) *        c[i-2,j] ) \
               /            i 

  return c

def gegenbauer_polynomial_value_test ( ):

#*****************************************************************************80
#
## GEGENBAUER_POLYNOMIAL_VALUE_TEST tests GEGENBAUER_POLYNOMIAL_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 November 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from gegenbauer_polynomial_values import gegenbauer_polynomial_values

  print ( '' )
  print ( 'GEGENBAUER_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GEGENBAUER_POLYNOMIAL_VALUE evaluates the Gegenbauer polynomial.' )
  print ( '' )
  print ( '       M     ALPHA         X           GPV    GEGENBAUER' )
  print ( '' )

  n_data = 0
  x = np.zeros ( 1 )

  while ( True ):

    n_data, m, alpha, xscalar, fx = gegenbauer_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break
#
#  Since GEGENBAUER_POLYNOMIAL_VALUE expects a vector input X, we have to
#  do a little "rewrapping" of the input.
#
    n = 1
    x[0] = xscalar
    c = gegenbauer_polynomial_value ( m, n, alpha, x )
    print ( '  %6d  %8.2f  %8.2f  %12f  %12f' % ( m, alpha, x[0], fx, c[m,0] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEGENBAUER_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  gegenbauer_polynomial_value_test ( )
  timestamp ( )

