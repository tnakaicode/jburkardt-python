#! /usr/bin/env python
#
def r8poly_nx ( n, a, xarray, x ):

#*****************************************************************************80
#
## R8POLY_NX replaces one of the base points in a polynomial in Newton form.
#
#  Discussion:
#
#    The Newton form of a polynomial is described by an array of N coefficients
#    A and N abscissas X:
#
#      p(x) =   a(1)
#             + a(2) * (x-x(1))
#             + a(3) * (x-x(1)) * (x-x(2))
#             ...
#             + a(n) * (x-x(1)) * (x-x(2)) * ... * (x-x(n-1))
#
#    X(N) does not occur explicitly in the formula for the evaluation of p(x),
#    although it is used in deriving the coefficients A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of A.
#
#    Input, real A(N), the polynomial coefficients of the Newton form.
#
#    Input, real XARRAY(N), the set of abscissas that
#    are part of the Newton form of the polynomial.  #
#    Input, real X, the new point to be shifted into XARRAY.
#
#    Output, real A(N), the updated polynomial coefficients
#    of the Newton form.
#
#    Output, real XARRAY(N), the shifted abscissas.  The first
#    entry is now equal to X.
#
  for i in range ( n - 2, -1, -1 ):
    a[i] = a[i] + ( x - xarray[i] ) * a[i+1]

  for i in range ( n - 1, 0, -1 ):
    xarray[i] = xarray[i-1]
  xarray[0] = x

  return a, xarray

def r8poly_nx_test ( ):

#*****************************************************************************80
#
## R8POLY_NX_TEST tests R8POLY_NX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_indicator1 import r8vec_indicator1
  from r8vec_print import r8vec_print

  n = 3

  print ( '' )
  print ( 'R8POLY_NX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_NX replaces one abscissa in a Newton polynomial.' )

  a = r8vec_indicator1 ( n )
  xarray = r8vec_indicator1 ( n )
 
  r8vec_print ( n, a, '  Newton polynomial coefficients:' )
  r8vec_print ( n, xarray, '  Newton polynomial abscissas:' )
#
#  Shift the X array by inserting X=0.
#
  x = 0.0

  print ( '' )
  print ( '  Replace one abscissa by X = %g' % ( x ) )

  a, xarray = r8poly_nx ( n, a, xarray, x )
#
#  Report the new polynomial form.
#
  r8vec_print ( n, a, '  Newton polynomial coefficients:' )
  r8vec_print ( n, xarray, '  Newton polynomial abscissas:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_NX_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8poly_nx_test ( )
  timestamp ( )

