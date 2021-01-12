#! /usr/bin/env python
#
def i4poly ( n, a, x0, iopt ):

#*****************************************************************************80
#
## I4POLY performs operations on integer polynomials in power or factorial form.
#
#  Discussion:
#
#    The power sum form of a polynomial is
#
#      P(X) = A1 + A2*X + A3*X^2 + ... + (AN+1)*X^N
#
#    The Taylor expansion at C has the form
#
#      P(X) = A1 + A2*(X-C) + A3*(X-C)^2 + ... + (AN+1)*(X-C)^N
#
#    The factorial form of a polynomial is
#
#      P(X) = A1 + A2*X + A3*(X)*(X-1) + A4*(X)*(X-1)*(X-2)+...
#        + (AN+1)*(X)*(X-1)*...*(X-N+1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuism, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Parameters:
#
#    Input, integer N, the number of coefficients in the polynomial
#    (in other words, the polynomial degree + 1)
#
#    Input, integer A(N), the coefficients of the polynomial.
#
#    Input, integer X0, for IOPT = -1, 0, or positive, the value of the
#    argument at which the polynomial is to be evaluated, or the
#    Taylor expansion is to be carried out.
#
#    Input, integer IOPT, a flag describing which algorithm is to
#    be carried out:
#
#    -3: Reverse Stirling.  Input the coefficients of the polynomial in
#    factorial form, output them in power sum form.
#
#    -2: Stirling.  Input the coefficients in power sum form, output them
#    in factorial form.
#
#    -1: Evaluate a polynomial which has been input in factorial form.
#
#    0:  Evaluate a polynomial input in power sum form.
#
#    1 or more:  Given the coefficients of a polynomial in
#    power sum form, compute the first IOPT coefficients of
#    the polynomial in Taylor expansion form.
#
#    Output, integer A(N), the coefficients of the output polynomial.
#    Depending on the option chosen, these coefficients are the input values,
#    or those of a different form of the polynomial.
#
#    Output, integer VAL, for IOPT = -1 or 0, the value of the
#    polynomial at the point X0.
#
  val = 0

  n1 = min ( n, iopt )
  n1 = max ( 1, n1 )

  if ( iopt < -1 ):
    n1 = n

  delta = ( max ( -iopt, 0 ) % 2 )

  w = -n * delta

  if ( -2 < iopt ):
    w = w + x0

  for m in range ( 1, n1 + 1 ):

    val = 0
    z = w

    for i in range ( m, n + 1 ):
      z = z + delta
      val = a[n+m-i-1] + z * val
      if ( iopt != 0 and iopt != -1 ):
        a[n+m-i-1] = val

    if ( iopt < 0 ):
      w = w + 1

  return a, val

def i4poly_test ( ):

#*****************************************************************************80
#
## I4POLY_TEST test I4POLY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 6

  print ( '' )
  print ( 'I4POLY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4POLY converts between power sum, factorial' )
  print ( '  and Taylor forms, and can evaluate a polynomial' )
  print ( '' )
 
  for test in range ( 1, 7 ):

    if ( test == 1 ):
      iopt = -3
      x0 = 0
    elif ( test == 2 ):
      iopt = -2
      x0 = 0
    elif ( test == 3 ):
      iopt = -1
      x0 = 2
    elif ( test == 4 ):
      iopt = 0
      x0 = 2
    elif ( test == 5 ):
      iopt = 6
      x0 = 2
    elif ( test == 6 ):
      iopt = 6
      x0 = -2

    a = np.array ( [ 0, 0, 0, 0, 0, 1 ] )

    if ( test == 1 ):
      print ( '' )
      print ( '  All calls have input A as follows:' )
      for i in range ( 0, n ):
        print ( '  %2d' % ( a[i] ) )
      print ( '' )
 
    a, val = i4poly ( n, a, x0, iopt )
 
    print ( '' )
    print ( '  Option IOPT = %d' % ( iopt ) )

    if ( -1 <= iopt ):
      print ( '  X0 = %d' % ( x0 ) )

    if ( iopt == -3 or iopt == -2 or 0 < iopt ):
      print ( '  Output array:' )
      for i in range ( 0, n ):
        print ( '  %2d' % ( a[i] ) ),
      print ( '' )

    if ( iopt == -1 or iopt == 0 ):
      print ( '  Value = %d' % ( val ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4POLY_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4poly_test ( )
  timestamp ( )
