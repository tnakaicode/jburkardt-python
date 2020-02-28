#! /usr/bin/env python
#
def legendre_dr_compute ( n ):

#*****************************************************************************80
#
## LEGENDRE_DR_COMPUTE: Gauss-Legendre quadrature by Davis-Rabinowitz method.
#
#  Discussion:
#
#    The integral:
#
#      Integral ( -1 <= X <= 1 ) F(X) dX
#
#    The quadrature rule:
#
#      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Dover, 2007,
#    ISBN: 0486453391,
#    LC: QA299.3.D28.
#
#  Parameters:
#
#    Input, integer N, the order.
#    N must be greater than 0.
#
#    Output, real X(N), the abscissas.
#
#    Output, real W(N), the weights.
#
  import numpy as np
  from sys import exit

  x = np.zeros ( n )
  w = np.zeros ( n )

  if ( n < 1 ):
    print ( '' )
    print ( 'LEGENDRE_DR_COMPUTE - Fatal error!' )
    print ( '  Illegal value of N = %d' % ( n ) )
    exit ( 'LEGENDRE_DR_COMPUTE - Fatal error!' )

  e1 = n * ( n + 1 )

  m = ( ( n + 1 ) // 2 )

  for i in range ( 1, m + 1 ):

    mp1mi = m + 1 - i

    t = float ( 4 * i - 1 ) * np.pi / float ( 4 * n + 2 )

    x0 = np.cos ( t ) \
      * ( 1.0 - ( 1.0 - 1.0 / float ( n ) ) / float ( 8 * n * n ) )

    pkm1 = 1.0
    pk = x0

    for k in range ( 2, n + 1 ):
      pkp1 = 2.0 * x0 * pk - pkm1 - ( x0 * pk - pkm1 ) / float ( k )
      pkm1 = pk
      pk = pkp1

    d1 = float ( n ) * ( pkm1 - x0 * pk )

    dpn = d1 / ( 1.0 - x0 * x0 )

    d2pn = ( 2.0 * x0 * dpn - e1 * pk ) / ( 1.0 - x0 * x0 )

    d3pn = ( 4.0 * x0 * d2pn + ( 2.0 - e1 ) * dpn ) / ( 1.0 - x0 * x0 )

    d4pn = ( 6.0 * x0 * d3pn + ( 6.0 - e1 ) * d2pn ) / ( 1.0 - x0 * x0 )

    u = pk / dpn
    v = d2pn / dpn
#
#  Initial approximation H:
#
    h = - u * ( 1.0 + 0.5 * u * ( v + u * ( v * v - d3pn / ( 3.0 * dpn ) ) ) )
#
#  Refine H using one step of Newton's method:
#
    p = pk + h * ( dpn + 0.5 * h * ( d2pn + h / 3.0 \
      * ( d3pn + 0.25 * h * d4pn ) ) )

    dp = dpn + h * ( d2pn + 0.5 * h * ( d3pn + h * d4pn / 3.0 ) )

    h = h - p / dp

    xtemp = x0 + h

    x[mp1mi-1] = xtemp

    fx = d1 - h * e1 * ( pk + 0.5 * h * ( dpn + h / 3.0 \
      * ( d2pn + 0.25 * h * ( d3pn + 0.2 * h * d4pn ) ) ) )

    w[mp1mi-1] = 2.0 * ( 1.0 - xtemp * xtemp ) / fx / fx

  if ( ( n % 2 ) == 1 ):
    x[0] = 0.0
#
#  Shift the data up.
#
  nmove = ( ( n + 1 ) // 2 )
  ncopy = n - nmove

  for i in range ( 1, nmove + 1 ):
    iback = n + 1 - i
    x[iback-1] = x[iback-ncopy-1]
    w[iback-1] = w[iback-ncopy-1]
#
#  Reflect values for the negative abscissas.
#
  for i in range ( 1, n - nmove + 1 ):
    x[i-1] = - x[n-i]
    w[i-1] =   w[n-i]

  return x, w

def legendre_dr_compute_test ( ):

#*****************************************************************************80
#
## LEGENDRE_DR_COMPUTE_TEST tests LEGENDRE_DR_COMPUTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LEGENDRE_DR_COMPUTE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LEGENDRE_DR_COMPUTE computes a Legendre quadrature rule' )
  print ( '  using the Davis-Rabinowitz algorithm.' )
  print ( '' )
  print ( '  Index       X             W' )

  for n in range ( 1, 11 ):

    x, w = legendre_dr_compute ( n )

    print ( '' )

    for i in range ( 0, n ):
      print ( '  %2d  %24.16g  %24.16g' % ( i, x[i], w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LEGENDRE_DR_COMPUTE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  legendre_dr_compute_test ( )
  timestamp ( )

