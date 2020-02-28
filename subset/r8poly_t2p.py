#! /usr/bin/env python
#
def r8poly_t2p ( n, a1, x ):

#*****************************************************************************80
#
## R8POLY_T2P converts a real polynomial from Taylor form to power sum form.
#
#  Discussion:
#
#    The Taylor form of a polynomial based at X0 is
#
#      p(x) =   a(1)
#             + a(2) * (x-x0)
#             + a(3) * (x-x0)^2
#             ...
#             + a(n) * (x-x0)^(n-1)
#
#    The power sum form is
#
#      p(x) = a(1) + a(2)*x + a(3)*x^2 + ... + a(n)*x^(n-1)
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
#    Input, real A1(N), the coefficients in Taylor form.
#
#    Input, real X, the point at which the Taylor form polynomial is based.
#
#    Output, real A2(N), the coefficients in power sum form.
#
  import numpy as np

  a2 = np.zeros ( n )

  for i in range ( 0, n ):
    a2[i] = a1[i]

  for i in range ( n - 1, -1, -1 ):
    for j in range ( i, n - 1 ):
      a2[j] = a2[j] - a2[j+1] * x

  return a2

def r8poly_t2p_test ( ):

#*****************************************************************************80
#
## R8POLY_T2P_TEST tests R8POLY_T2P.
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
  from r8poly_p2t import r8poly_p2t
  from r8poly_print import r8poly_print
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  n = 4
  a = r8vec_indicator1 ( n )
  x = 2.0

  print ( '' )
  print ( 'R8POLY_T2P_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_T2P: Taylor => Power sum' )
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
  print ( 'R8POLY_T2P_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_t2p_test ( )
  timestamp ( )

