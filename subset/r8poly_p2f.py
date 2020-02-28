#! /usr/bin/env python
#
def r8poly_p2f ( n, a ):

#*****************************************************************************80
#
## R8POLY_P2F converts a real polynomial from power sum form to factorial form.
#
#  Discussion:
#
#    The power sum form is
#
#      p(x) = a(1) + a(2) * x + a(3) * x^2 + ... + a(n) * x^(n-1)
#
#    The (falling) factorial form is
#
#      p(x) =   a(1)
#             + a(2) * x
#             + a(3) * x * (x-1)
#             ...
#             + a(n) * x * (x-1) *...* (x-(n-2))
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
#    Input, real A(N), on input, the polynomial coefficients in power sum form.
#
#    Output, real B(N), the polynomial coefficients in factorial form.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    b[i] = a[i]

  for m in range ( 0, n ):
    value = 0.0;
    for i in range ( m, n ):
      value = b[n-1+m-i] + float ( m ) * value
      b[n-1+m-i] = value

  return b

def r8poly_p2f_test ( ):

#*****************************************************************************80
#
## R8POLY_P2F_TEST tests R8POLY_P2F.
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
  from r8poly_f2p import r8poly_f2p
  from r8poly_print import r8poly_print
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  n = 4
  a = r8vec_indicator1 ( n )
 
  print ( '' )
  print ( 'R8POLY_P2F_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_P2F: power sum => factorial;' )

  r8poly_print ( n - 1, a, '  The power sum polynomial:' )
 
  b = r8poly_p2f ( n, a )
 
  r8vec_print ( n, b, '  The factorial polynomial coefficients:' )
 
  c = r8poly_f2p ( n, b )
 
  r8poly_print ( n - 1, c, '  The recovered power sum polynomial:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_P2F_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_p2f_test ( )
  timestamp ( )

