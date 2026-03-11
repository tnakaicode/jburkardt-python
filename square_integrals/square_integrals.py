#! /usr/bin/env python3
#
def monomial_value ( m, n, e, x ):

#*****************************************************************************80
#
## monomial_value() evaluates a monomial.
#
#  Discussion:
#
#    This routine evaluates a monomial of the form
#
#      product ( 1 <= i <= m ) x(i)^e(i)
#
#    The combination 0.0^0, if encountered, is treated as 1.0.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of evaluation points.
#
#    integer E(M), the exponents.
#
#    real X(M,N), the point coordinates.
#
#  Output:
#
#    real V(N), the monomial values.
#
  import numpy as np

  v = np.ones ( n )

  for i in range ( 0, m ):
    if ( 0 != e[i] ):
      for j in range ( 0, n ):
        v[j] = v[j] * x[i,j] ** e[i]

  return v

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_transpose_print() prints an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_transpose_print_some() prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ', end = '' )

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ), end = '' )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def square01_area ( ):

#*****************************************************************************80
#
## square01_area() returns the area of the unit square in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the area.
#
  value = 1.0

  return value

def square01_area_test ( ) :

#*****************************************************************************80
#
## square01_area_test() tests square01_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'square01_area_test():' )
  print ( '  square01_area returns the area of the unit square.' )

  value = square01_area ( )

  print ( '' )
  print ( '  square01_area() = %g' % ( value ) )

  return

def square01_monomial_integral ( e ):

#*****************************************************************************80
#
## square01_monomial_integral(): integrals over the unit square in 2D.
#
#  Discussion:
#
#    The integration region is 
#
#      0 <= X <= 1,
#      0 <= Y <= 1.
#
#    The monomial is F(X,Y) = X^E(1) * Y^E(2).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Academic Press, 1984, page 263.
#
#  Input:
#
#    integer E(2), the exponents.  Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  m = 2

  if ( e[0] < 0 or e[1] < 0 ):
    print ( '' )
    print ( 'square01_monomial_integral - Fatal error!' )
    print ( '  All exponents must be nonnegative.' )
    raise Exception ( 'square01_monomial_integral - Fatal error!' )

  integral = 1.0
  for i in range ( 0, m ):
    integral = integral / float ( e[i] + 1 )

  return integral

def square01_monomial_integral_test ( rng ):

#*****************************************************************************80
#
## square01_monomial_integral_test() tests square01_monomial_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  m = 2
  n = 4192
  test_num = 20

  print ( '' )
  print ( 'square01_monomial_integral_test():' )
  print ( '  square01_monomial_integral() returns the integral of a monomial' )
  print ( '  over the interior of the unit square in 2D.' )
  print ( '  Compare with a Monte Carlo estimate.' )
#
#  Get sample points.
#
  x = square01_sample ( n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose exponents.
#
  print ( '' )
  print ( '  Ex  Ey     MC-Estimate           Exact      Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e  = rng.integers ( low = 0, high = 7, size = m, endpoint = True )

    value = monomial_value ( m, n, e, x )

    result = square01_area ( ) * np.sum ( value ) / float ( n )
    exact = square01_monomial_integral ( e )
    error = abs ( result - exact )

    print ( '  %2d  %2d  %14.6g  %14.6g  %10.2g' \
      % ( e[0], e[1], result, exact, error ) )

  return

def square01_sample ( n, rng ):

#*****************************************************************************80
#
## square01_sample() samples points in the unit square in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(2,N), the points.
#
  import numpy as np

  x = rng.random ( size = [ 2, n ] )

  return x

def square01_sample_test ( rng ):

#*****************************************************************************80
#
## square01_sample_test() tests square01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'square01_sample_test():' )
  print ( '  square01_sample() samples the unit square.' )

  m = 2
  n = 10
 
  x = square01_sample ( n, rng )

  r8mat_transpose_print ( m, n, x, '  Sample points in the unit square.' )

  return

def square_integrals_test ( ):

#*****************************************************************************80
#
## square_integrals_test() tests square_integrals().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'square_integrals_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test square_integrals().' )

  rng = default_rng ( )
#
#  Library functions.
#
  square01_area_test ( )
  square01_monomial_integral_test ( rng )
  square01_sample_test ( rng )
  squaresym_area_test ( )
  squaresym_monomial_integral_test ( rng )
  squaresym_sample_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'square_integrals_test():' )
  print ( '  Normal end of execution.' )
  return

def squaresym_area ( ):

#*****************************************************************************80
#
## squaresym_area() returns the area of the symmetric unit square in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 February 2018
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the area.
#
  value = 4.0;

  return value

def squaresym_area_test ( ) :

#*****************************************************************************80
#
## squaresym_area_test() tests squaresym_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'squaresym_area_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  squaresym_area returns the area of the symmetric unit square.' )

  value = squaresym_area ( )

  print ( '' )
  print ( '  squaresym_area() = %g' % ( value ) )

  return

def squaresym_monomial_integral ( e ):

#*****************************************************************************80
#
## squaresym_monomial_integral(): integrals over the symmetric unit square in 2D.
#
#  Discussion:
#
#    The integration region is 
#
#      -1 <= X <= 1,
#      -1 <= Y <= 1.
#
#    The monomial is F(X,Y) = X^E(1) * Y^E(2).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 February 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Academic Press, 1984, page 263.
#
#  Input:
#
#    integer E(2), the exponents.  Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  m = 2

  if ( e[0] < 0 or e[1] < 0 ):
    print ( '' )
    print ( 'squaresym_monomial_integral - Fatal error!' )
    print ( '  All exponents must be nonnegative.' )
    raise Exception ( 'squaresym_monomial_integral - Fatal error!' )

  if ( e[0] % 2 == 1 or e[1] % 2 == 1 ):
    integral = 0.0
  else:
    integral = 4.0 / float ( e[0] + 1 ) / float ( e[1] + 1 )

  return integral

def squaresym_monomial_integral_test ( rng ):

#*****************************************************************************80
#
## squaresym_monomial_integral_test() tests squaresym_monomial_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  m = 2
  n = 4192
  test_num = 20

  print ( '' )
  print ( 'squaresym_monomial_integral_test():' )
  print ( '  squaresym_monomial_integral() returns the integral of a monomial' )
  print ( '  over the interior of the unit square in 2D.' )
  print ( '  Compare with a Monte Carlo estimate.' )
#
#  Get sample points.
#
  x = squaresym_sample ( n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose exponents.
#
  print ( '' )
  print ( '  Ex  Ey     MC-Estimate           Exact      Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = rng.integers ( low = 0, high = 7, size = m, endpoint = True )

    value = monomial_value ( m, n, e, x )

    result = squaresym_area ( ) * np.sum ( value ) / float ( n )
    exact = squaresym_monomial_integral ( e )
    error = abs ( result - exact )

    print ( '  %2d  %2d  %14.6g  %14.6g  %10.2g' \
      % ( e[0], e[1], result, exact, error ) )

  return

def squaresym_sample ( n, rng ):

#*****************************************************************************80
#
## squaresym_sample() samples points in the symmetric unit square in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 February 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(2,N), the points.
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  x = -1.0 + 2.0 * rng.random ( size = [ 2, n ] )

  return x

def squaresym_sample_test ( rng ):

#*****************************************************************************80
#
## squaresym_sample_test() tests squaresym_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'squaresym_sample_test():' )
  print ( '  squaresym_sample samples the symmeric unit square.' )

  m = 2
  n = 10
  x = squaresym_sample ( n, rng )

  r8mat_transpose_print ( m, n, x, '  Sample points in the symmetric unit square.' )

  return

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  square_integrals_test ( )
  timestamp ( )

