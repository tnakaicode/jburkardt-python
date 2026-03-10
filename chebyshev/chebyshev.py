#! /usr/bin/env python3
#
def chebyshev_coefficients ( a, b, n, f ):

#*****************************************************************************80
#
## chebyshev_coefficients() determines Chebyshev interpolation coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Roger Broucke,
#    Algorithm 446:
#    Ten Subroutines for the Manipulation of Chebyshev Series,
#    Communications of the ACM,
#    Volume 16, Number 4, April 1973, pages 254-256.
#
#  Input:
#
#    real A, B, the domain of definition.
#
#    integer N, the order of the interpolant.
#
#    real F ( X ), a function handle.
#
#  Output:
#
#    real C(N), the Chebyshev coefficients.
#
  import numpy as np

  angle = np.linspace ( 1.0, 2.0 * n - 1, n )
  angle = angle * np.pi / ( 2.0 * n )
  x = np.cos ( angle )
  x = 0.5 * ( a + b ) + x * 0.5 * ( b - a )
  fx = f ( x )

  c = np.zeros ( n )
  for j in range ( 0, n ):
    for k in range ( 0, n ):
      c[j] = c[j] + fx[k] * np.cos ( np.pi * j * ( 2 * k + 1 ) / 2.0 / n )

  c = 2.0 * c / n

  return c

def chebyshev_interpolant ( a, b, n, c, m, x ):

#*****************************************************************************80
#
## chebyshev_interpolant() evaluates a Chebyshev interpolant.
#
#  Discussion:
#
#    For n = 0, ..., define T(n,x) = cos ( n * arccos ( x ) ).
#
#    The polynomial T(n,x) has n zeros in [-1,+1].
#
#    For a given value n, the zeros of T(n,x) are
#
#      x(j,n) = cos ( pi * ( 2 * j - 1 ) / ( 2 * n ) ), for j = 1 to n.
#
#    For a given n, define the Chebyshev coefficients by
#
#      c(i) = (2/n) * sum ( 0 <= j < n ) f(x(j,n)) * T(i-1,x(j,n))
#
#    Now define the Chebyshev interpolant C(f) by:
#
#      C(f)(x) = sum ( 1 <= i <= n ) c(i) T(i-1,x) - 0.5 * c(1)
#
#    Then it is the case that
#
#      C(f)(x(j,n)) = f(x(j,n)) for j = 1 to n.
#
#    This function accepts the Chebyshev coefficients c(), and evaluates
#    the Chebyshev interpolant C(f)(x).
#      
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Roger Broucke,
#    Algorithm 446:
#    Ten Subroutines for the Manipulation of Chebyshev Series,
#    Communications of the ACM,
#    Volume 16, Number 4, April 1973, pages 254-256.
#
#  Input:
#
#    real A, B, the domain of definition.
#
#    integer N, the order of the interpolant.
#
#    real C(N), the Chebyshev coefficients.
#
#    integer M, the number of points.
#
#    real X(M), the points at which the polynomial is
#    to be evaluated.
#
#  Output:
#
#    real VALUE(M), the value of the Chebyshev interpolant at X.
#
  import numpy as np

  dip1 = np.zeros ( m )
  di = np.zeros ( m )
  y = ( 2.0 * x - a - b ) / ( b - a )

  for i in range ( n - 1, 0, -1 ):
    dip2 = dip1
    dip1 = di
    di = 2.0 * y * dip1 - dip2 + c[i]

  value = y * di - dip1 + 0.5 * c[0]

  return value

def chebyshev_test01 ( ):

#*****************************************************************************80
#
## chebyshev_test01() tests chebyshev_coefficients() and chebyshev_interpolant().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev_test01():' )
  print ( '  chebyshev_coefficients() computes the coefficients of the' )
  print ( '  Chebyshev interpolant.' )
  print ( '  chebyshev_interpolant() evaluates the interpolant.' )

  n = 5
  a = -1.0
  b = +1.0

  c = chebyshev_coefficients ( a, b, n, f1 )

  x = chebyshev_zeros ( n )
  x = 0.5 * ( a + b ) + x * 0.5 * ( b - a )

  fx = f1 ( x )
  m = n
  fc = chebyshev_interpolant ( a, b, n, c, m, x )

  print ( '' )
  print ( '  F(X) is a trig function:' )
  print ( '' )
  print ( '      X           C(I)        F(X)       C(F)(X)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %10f  %10f  %10f  %10f' % ( x[i], c[i], fx[i], fc[i] ) )

  return

def chebyshev_test02 ( ):

#*****************************************************************************80
#
## chebyshev_test02() tests chebyshev_coefficients() and chebyshev_interpolant().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev_test02():' )
  print ( '  Try the same function, but a variant interval.' )
#
#  Try a variant interval.
#
  n = 5
  a = 0.0
  b = +3.0

  c = chebyshev_coefficients ( a, b, n, f1 )

  x = chebyshev_zeros ( n )
  x = 0.5 * ( a + b ) + x * 0.5 * ( b - a )

  fx = f1 ( x )
  m = n
  fc = chebyshev_interpolant ( a, b, n, c, m, x )

  print ( '' )
  print ( '  Consider the same F(X), but now over [0,3]:' )
  print ( '' )
  print ( '      X           C(I)        F(X)       C(F)(X)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %10f  %10f  %10f  %10f' % ( x[i], c[i], fx[i], fc[i] ) )

  return

def chebyshev_test03 ( ):

#*****************************************************************************80
#
## chebyshev_test03() tests chebyshev_coefficients() and chebyshev_interpolant().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev_test03():' )
  print ( '  Try the same function, but a higher order.' )

  n = 10
  a = -1.0
  b = +1.0

  c = chebyshev_coefficients ( a, b, n, f1 )

  x = chebyshev_zeros ( n )
  x = 0.5 * ( a + b ) + x * 0.5 * ( b - a )

  fx = f1 ( x )
  m = n
  fc = chebyshev_interpolant ( a, b, n, c, m, x )

  print ( '' )
  print ( '  Consider the same F(X), but now with higher order:' )
  print ( '' )
  print ( '      X           C(I)        F(X)       C(F)(X)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %10f  %10f  %10f  %10f' % ( x[i], c[i], fx[i], fc[i] ) )

  return

def chebyshev_test04 ( ):

#*****************************************************************************80
#
## chebyshev_test04() tests chebyshev_coefficients() and chebyshev_interpolant().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev_test04():' )
  print ( '  Try a polynomial.' )

  n = 10
  a = -1.0
  b = +1.0

  c = chebyshev_coefficients ( a, b, n, f3 )

  x = chebyshev_zeros ( n )
  x = 0.5 * ( a + b ) + x * 0.5 * ( b - a )

  fx = f3 ( x )
  m = n
  fc = chebyshev_interpolant ( a, b, n, c, m, x )

  print ( '' )
  print ( '  F(X) is a degree 4 polynomial:' )
  print ( '' )
  print ( '      X           C(I)        F(X)       C(F)(X)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %10f  %10f  %10f  %10f' % ( x[i], c[i], fx[i], fc[i] ) )

  return

def chebyshev_test05 ( ):

#*****************************************************************************80
#
## chebyshev_test05() tests chebyshev_coefficients() and chebyshev_interpolant().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'chebyshev_test05():' )
  print ( '  Try a function with decaying behavior.' )

  n = 10
  a = -1.0
  b = +1.0

  c = chebyshev_coefficients ( a, b, n, f2 )

  x = chebyshev_zeros ( n )
  x = 0.5 * ( a + b ) + x * 0.5 * ( b - a )

  fx = f2 ( x )
  m = n
  fc = chebyshev_interpolant ( a, b, n, c, m, x )

  print ( '' )
  print ( '  The polynomial approximation to F(X) decays:' )
  print ( '' )
  print ( '      X           C(I)        F(X)       C(F)(X)' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %10f  %10f  %10f  %10f' % ( x[i], c[i], fx[i], fc[i] ) )

  return

def chebyshev_test ( ):

#*****************************************************************************80
#
## chebyshev_test() tests chebyshev().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'chebyshev_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test chebyshev().' )

  chebyshev_test01 ( )
  chebyshev_test02 ( )
  chebyshev_test03 ( )
  chebyshev_test04 ( )
  chebyshev_test05 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'chebyshev_test():' )
  print ( '  Normal end of execution.' )

  return

def chebyshev_zeros ( n ):

#*****************************************************************************80
#
## chebyshev_zeros() returns zeroes of the Chebyshev polynomial T(N)(X).
#
#  Discussion:
#
#    We produce the Chebyshev zeros in ascending order.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#  Output:
#
#    real X(N), the zeroes of T(N)(X).
#
  import numpy as np

  angle = np.linspace ( 2 * n - 1, 1.0, n )
  angle = angle * np.pi / ( 2.0 * n )
  x = np.cos ( angle )

  return x

def f1 ( x ):

#*****************************************************************************80
#
## f1() evaluates a function that can be used for Chebyshev interpolation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(), the evaluation points.
#
#  Output:
#
#    real VALUE(), the function values.
#
  import numpy as np

  value = np.cos ( 2.0 * np.pi * x ) * np.sin ( 3.0 * np.pi * x )

  return value

def f2 ( x ):

#*****************************************************************************80
#
## f2() evaluates a function that can be used for Chebyshev interpolation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(), the evaluation points.
#
#  Output:
#
#    real VALUE(), the function values.
#
  import numpy as np

  value = np.exp ( x )

  return value

def f3 ( x ):

#*****************************************************************************80
#
## f3() evaluates a function that can be used for Chebyshev interpolation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X(), the evaluation points.
#
#  Output:
#
#    real VALUE(), the function values.
#
  value = ( x - 3.0 ) * ( x - 1.0 ) * ( x - 1.0 ) * ( x + 2.0 )

  return value

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  chebyshev_test ( )
  timestamp ( )

