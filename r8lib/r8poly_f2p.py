#! /usr/bin/env python
#
def r8poly_f2p ( n, a ):

#*****************************************************************************80
#
## R8POLY_F2P converts a real polynomial from factorial form to power sum form.
#
#  Discussion:
#
#    The (falling) factorial form is
#
#      p(x) =   a(1)
#             + a(2) * x
#             + a(3) * x*(x-1)
#             ...
#             + a(n) * x*(x-1)*...*(x-(n-2))
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
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of A.
#
#    Input, real A(N), the polynomial coefficients in factorial form.
#
#    Output, real B(N),  the polynomial coefficients in power sum form.
#
  import numpy as np

  b = np.zeros ( n )
  for i in range ( 0, n ):
    b[i] = a[i]

  w = - float ( n )

  for m in range ( 0, n ):

    val = 0.0
    z = w

    for i in range ( m, n ):
      z = z + 1.0
      val = b[n-1+m-i] + z * val
      b[n-1+m-i] = val

    w = w + 1.0

  return b

def r8poly_f2p_test ( ):

#*****************************************************************************80
#
## R8POLY_F2P_TEST tests R8POLY_F2P.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8poly_print import r8poly_print
  from r8poly_p2f import r8poly_p2f
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  n = 4
  a = r8vec_indicator1 ( n )
 
  print ( '' )
  print ( 'R8POLY_F2P_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_F2P: factorial => power sum.' )

  r8poly_print ( n - 1, a, '  The power sum polynomial:' )
 
  b = r8poly_p2f ( n, a )
 
  r8vec_print ( n, b, '  The factorial polynomial coefficients:' )
 
  c = r8poly_f2p ( n, b )
 
  r8poly_print ( n - 1, c, '  The recovered power sum polynomial:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_F2P_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_f2p_test ( )
  timestamp ( )

