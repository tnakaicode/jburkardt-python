#! /usr/bin/env python
#
def r8poly_nval ( n, a, xarray, x ):

#*****************************************************************************80
#
## R8POLY_NVAL evaluates a real polynomial in Newton form.
#
#  Definition:
#
#    The Newton form of a polynomial is
#
#      p(x) = a(1)
#           + a(2)  *(x-x1)
#           + a(3)  *(x-x1)*(x-x2)
#           +...
#           + a(n-1)*(x-x1)*(x-x2)*(x-x3)...*(x-x(n-2))
#           + a(n)  *(x-x1)*(x-x2)*(x-x3)...*(x-x(n-2))*(x-x(n-1))
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
#    Input, real XARRAY(N-1), the N-1 points X which are part
#    of the definition of the polynomial.
#
#    Input, real X, the point at which the polynomial is to be evaluated.
#
#    Output, real VALUE, the value of the polynomial at X.
#
  value = a[n-1]
  for i in range ( n - 2, -1, -1 ):
    value = a[i] + ( x - xarray[i] ) * value

  return value

def r8poly_nval_test ( ):

#*****************************************************************************80
#
## R8POLY_NVAL_TEST tests R8POLY_NVAL.
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
  import numpy as np
  import platform
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  n = 5

  print ( '' )
  print ( 'R8POLY_NVAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_NVAL evaluates a Newton polynomial.' )

  a = r8vec_indicator1 ( n )

  x = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    x[i] = a[i] - 1.0
 
  r8vec_print ( n, a, '  Newton polynomial coefficients:' )
  r8vec_print ( n - 1, x, '  Newton polynomial abscissas:' )

  xval = 2.0
 
  aval = r8poly_nval ( n, a, x, xval )
 
  print ( '' )
  print ( '  R8POLY(%g) = %g' % ( xval, aval ) )
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

