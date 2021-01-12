#! /usr/bin/env python
#
def r8poly_pval ( n, a, x ):

#*****************************************************************************80
#
## R8POLY_PVAL evaluates a real polynomial in power sum form.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(n-1) * x^(n-1) + a(n) * x^(n)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of A.
#
#    Input, real A(1:N+1), the coefficients of the polynomial.
#    A(1) is the constant term.
#
#    Input, real X, the point at which the polynomial is to be evaluated.
#
#    Output, real VALUE, the value of the polynomial at X.
#
  value = 0.0
  for i in range ( n, -1, -1 ):
    value = value * x + a[i]

  return value

def r8poly_pval_test ( ):

#*****************************************************************************80
#
## R8POLY_PVAL_TEST tests R8POLY_PVAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8poly_print import r8poly_print

  n = 4

  a = np.zeros ( n + 1 )
  for i in range ( 0, n + 1 ):
    a[i] = float ( i + 1 )

  print ( '' )
  print ( 'R8POLY_PVAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_PVAL evaluates a polynomial' )
  print ( '  in power sum form.' )

  r8poly_print ( n, a, '  The polynomial to be evaluated:' )

  x = 2.0
 
  val = r8poly_pval ( n, a, x )

  print ( '' )
  print ( '  At X = %f' % ( x ) )
  print ( '  Computed polynomial value is %f' % ( val ) )
  print ( '  Correct value is 129.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_PVAL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_pval_test ( )
  timestamp ( )
