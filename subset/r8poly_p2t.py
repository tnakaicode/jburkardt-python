#! /usr/bin/env python
#
def r8poly_p2t ( n, a1, x ):

#*****************************************************************************80
#
## RPPOLY_P2T converts a real polynomial from power sum form to Taylor form.
#
#  Discussion:
#
#    The power sum form is
#
#      p(x) = a(1) + a(2)*x + a(3)*x^2 + ... + a(n)*x^(n-1)
#
#    The Taylor form of a polynomial based at X0 is
#
#      p(x) =   a(1)
#             + a(2) * (x-x0)
#             + a(3) * (x-x0)^2
#             ...
#             + a(n) * (x-x0)^(n-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of A.
#
#    Input, real A1(N), on input, the coefficients in power sum form.
#
#    Input, real X, the point at which the Taylor form of the
#    polynomial is to be based.
#
#    Output, real A2(N), the coefficients in Taylor form.
#
  import numpy as np

  a2 = np.zeros ( n )

  for i in range ( 0, n ):
    a2[i] = a1[i]

  for m in range ( 1, n + 1 ):
    value = 0.0
    for i in range ( m, n + 1 ):
      value = a2[n+m-i-1] + x * value
      a2[n+m-i-1] = value

  return a2

def r8poly_p2t_test ( ):

#*****************************************************************************80
#
## R8POLY_P2T_TEST tests R8POLY_P2T.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8poly_print import r8poly_print
  from r8poly_t2p import r8poly_t2p
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  n = 4
  a = r8vec_indicator1 ( n )
  x = 2.0

  print ( '' )
  print ( 'R8POLY_P2T_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_P2T: Power sum => Taylor.' )
  print ( '' )
  print ( '  Taylor expansion point is X = %g' % ( x ) )

  r8vec_print ( n, a, '  The Taylor coefficients:' )

  a2 = r8poly_t2p ( n, a, x )

  r8poly_print ( n-1, a2, '  The power sum polynomial:' )

  a3 = r8poly_p2t ( n, a2, x )
 
  r8vec_print ( n, a3, '  The recovered Taylor coefficients:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_P2T_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_p2t_test ( )
  timestamp ( )

