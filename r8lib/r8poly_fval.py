#! /usr/bin/env python
#
def r8poly_fval ( n, a, x ):

#*****************************************************************************80
#
## R8POLY_FVAL evaluates a real polynomial in factorial form.
#
#  Discussion:
#
#    The (falling) factorial form of a polynomial is:
#
#      p(x) = a(1)
#           + a(2)  *x
#           + a(3)  *x*(x-1)
#           +...
#           + a(n-1)*x*(x-1)*(x-2)...*(x-(n-3))
#           + a(n)  *x*(x-1)*(x-2)...*(x-(n-3))*(x-(n-2))
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of A.
#
#    Input, real A(N), the coefficients of the polynomial.
#    A(1) is the constant term.
#
#    Input, real X, the point at which the polynomial is to be evaluated.
#
#    Output, real VALUE, the value of the polynomial at X.
#
  value = 0.0
  for i in range ( 0, n ):
    value = a[n-1-i] + ( x - n + 1 + i ) * value

  return value

def r8poly_fval_test ( ):

#*****************************************************************************80
#
## R8POLY_FVAL_TEST tests R8POLY_FVAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  n = 5

  print ( '' )
  print ( 'R8POLY_FVAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_FVAL evaluates a polynomial in factorial form.' )

  a = r8vec_indicator1 ( n )
 
  r8vec_print ( n, a, '  The factorial polynomial coefficients:' )

  x = 2.0

  val = r8poly_fval ( n, a, x )

  print ( '' )
  print ( '  R8POLY(%g) = %g' % ( x, val ) )
  print ( '  The correct value is 11.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_NVAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_nval_test ( )
  timestamp ( )

