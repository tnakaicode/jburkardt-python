#! /usr/bin/env python
#
def cardinal_cos ( j, m, n, t ):

#*****************************************************************************80
#
## CARDINAL_COS evaluates the J-th cardinal cosine basis function.
#
#  Discussion:
#
#    The base points are T(I) = pi * I / ( M + 1 ), 0 <= I <= M + 1.
#    Basis function J is 1 at T(J), and 0 at T(I) for I /= J
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
#    John Boyd,
#    Exponentially convergent Fourier-Chebyshev quadrature schemes on
#    bounded and infinite intervals,
#    Journal of Scientific Computing,
#    Volume 2, Number 2, 1987, pages 99-109.
#
#  Parameters:
#
#    Input, integer J, the index of the basis function.
#    0 <= J <= M + 1.
#
#    Input, integer M, indicates the size of the basis set.
#
#    Input, integer N, the number of sample points.
#
#    Input, real T(N), one or more points in [0,pi] where the
#    basis function is to be evaluated.
#
#    Output, real C(N), the value of the function at T.
#
  import numpy as np
  from r8_mop import r8_mop

  r8_epsilon = 2.220446049250313E-16

  if ( ( j % ( m + 1 ) ) == 0 ):
    cj = 2.0
  else:
    cj = 1.0

  tj = np.pi * float ( j ) / float ( m + 1 )

  c = np.zeros ( n )

  for i in range ( 0, n ):
    if ( abs ( t[i] - tj ) < 5.0 * r8_epsilon ):
      c[i] = 1.0
    else:
      c[i] = r8_mop ( ( j + 1 ) % 2 ) * np.sin ( t[i] ) * np.sin ( ( m + 1 ) * t[i] ) \
        / cj / ( m + 1 ) / ( np.cos ( t[i] ) - np.cos ( tj ) )

  return c

def cardinal_cos_test ( ):

#*****************************************************************************80
#
## CARDINAL_COS_TEST tests CARDINAL_COS.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'CARDINAL_COS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CARDINAL_COS evaluates cardinal cosine functions.' )
  print ( '  Ci(Tj) = Delta(i,j), where Tj = cos(pi*i/(n+1)).' )
  print ( '  A simple check of all pairs should form the identity matrix.' )

  print ( '' )
  print ( '  The CARDINAL_COS test matrix:' )
  print ( '' )

  m = 11
  n = m + 2
  c = np.zeros ( [ m + 2, n ] )
  t_lo = 0.0
  t_hi = np.pi
  t = np.linspace ( t_lo, t_hi, n )
 
  for j in range ( 0, m + 2 ):
    v = cardinal_cos ( j, m, n, t )
    for i in range ( 0, n ):
      c[i,j] = v[i]

  for i in range ( 0, n ):
    for j in range ( 0, m + 2 ):
      print ( '  %5.2f' % ( c[i,j] ) ),
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'CARDINAL_COS_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  cardinal_cos_test ( )
  timestamp ( )
