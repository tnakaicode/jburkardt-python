#! /usr/bin/env python3
#
def hypercube01_monomial_integral ( m, e ):

#*****************************************************************************80
#
## hypercube01_monomial_integral(): integrals over the unit hypercube in M dimensions.
#
#  Discussion:
#
#    The integration region is 
#
#      0 <= X(1:M) <= 1,
#
#    The monomial is F(X) = product ( 1 <= I <= M ) X(I)^E(I).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 June 2015
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
#    integer M, the spatial dimension.
#
#    integer E(M), the exponents.  Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  for i in range ( 0, m ):
    if ( e[i] < 0 ):
      print ( '' )
      print ( 'hypercube01_monomial_integral(): Fatal error!' )
      print ( '  All exponents must be nonnegative.' )
      raise Exception ( 'hypercube01_monomial_integral(): Fatal error!' )

  integral = 1.0
  for i in range ( 0, m ):
    integral = integral / float ( e[i] + 1 )

  return integral

def hypercube01_monomial_integral_test ( rng ):

#*****************************************************************************80
#
## hypercube01_monomial_integral_test() tests hypercube01_monomial_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#    rng(): the current random number generator.
#
  import numpy as np

  m = 3
  n = 4192
  test_num = 20

  print ( '' )
  print ( 'hypercube01_monomial_integral_test():' )
  print ( '  hypercube01_monomial_integral() returns the integral of a monomial' )
  print ( '  over the interior of the unit hypercube in 3D.' )
  print ( '  Compare with a Monte Carlo estimate.' )
  print ( '' )
  print ( '  Using M = ', m )
#
#  Get sample points.
#
  x = hypercube01_sample ( m, n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose exponents.
#
  print ( '' )
  print ( '  Ex  Ey  Ez     MC-Estimate           Exact      Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = rng.integers ( low = 0, high = 4, size = m, endpoint = True )

    value = monomial_value ( m, n, e, x )

    result = hypercube01_volume ( m ) * np.sum ( value ) / float ( n )
    exact = hypercube01_monomial_integral ( m, e )
    error = abs ( result - exact )

    for i in range ( 0, m ):
      print ( '  %2d' % ( e[i] ), end = '' )
    print ( '  %14.6g  %14.6g  %10.2g' % ( result, exact, error ) )

  return

def hypercube01_monte_carlo_test01 ( rng ):

#*****************************************************************************80
#
## hypercube01_monte_carlo_test01() estimates integrals over the unit hypercube in 3D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
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

  m = 3

  e_test = np.array ( [ \
    [ 0, 0, 0 ], \
    [ 1, 0, 0 ], \
    [ 0, 1, 0 ], \
    [ 0, 0, 1 ], \
    [ 2, 0, 0 ], \
    [ 1, 1, 0 ], \
    [ 1, 0, 1 ], \
    [ 0, 2, 0 ], \
    [ 0, 1, 1 ], \
    [ 0, 0, 2 ] ] )

  print ( '' )
  print ( 'hypercube01_monte_carlo_test01():' )
  print ( '  hypercube01_sample() estimates integrals ' )
  print ( '  along the interior of the unit hypercube in 3D.' )
  print ( '' )
  print ( '         N', end = '' )
  print ( '        1', end = '' )
  print ( '               X', end = '' )
  print ( '               Y ', end = '' )
  print ( '              Z', end = '' )
  print ( '               X^2', end = '' )
  print ( '              XY', end = '' )
  print ( '             XZ', end = '' )
  print ( '              Y^2', end = '' )
  print ( '             YZ', end = '' )
  print ( '               Z^2' )
  print ( '' )

  n = 1
  e = np.zeros ( m, dtype = np.int32 )

  while ( n <= 65536 ):

    x = hypercube01_sample ( m, n, rng )
    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 10 ):

      e[0:m] = e_test[j,0:m]

      value = monomial_value ( m, n, e, x )

      result = hypercube01_volume ( m ) * np.sum ( value[0:n] ) / float ( n )

      print ( '  %14.6g' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  print ( '' )
  print ( '     Exact', end = '' )

  for j in range ( 0, 10 ):

    e[0:m] = e_test[j,0:m]

    result = hypercube01_monomial_integral ( m, e )
    print ( '  %14.6g' % ( result ), end = '' )

  print ( '' )

  return

def hypercube01_monte_carlo_test02 ( rng ):

#*****************************************************************************80
#
## hypercube01_monte_carlo_test02() estimates integrals over the unit hypercube in 6D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2016
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

  m = 6

  e_test = np.array ( [ \
    [ 0, 0, 0, 0, 0, 0 ], \
    [ 1, 0, 0, 0, 0, 0 ], \
    [ 0, 2, 0, 0, 0, 0 ], \
    [ 0, 2, 2, 0, 0, 0 ], \
    [ 0, 0, 0, 4, 0, 0 ], \
    [ 2, 0, 0, 0, 2, 2 ], \
    [ 0, 0, 0, 0, 0, 6 ] ] )

  print ( '' )
  print ( 'hypercube01_monte_carlo_test02():' )
  print ( '  hypercube01_sample() estimates integrals ' )
  print ( '  along the interior of the unit hypercube in 6D.' )
  print ( '' )
  print ( '         N', end = '' )
  print ( '        1      ', end = '' )
  print ( '        U      ', end = '' )
  print ( '         V^2   ', end = '' )
  print ( '         V^2W^2', end = '' )
  print ( '         X^4   ', end = '' )
  print ( '         Y^2Z^2', end = '' )
  print ( '         Z^6' )
  print ( '' )

  n = 1
  e = np.zeros ( m, dtype = np.int32 )

  while ( n <= 65536 ):

    x = hypercube01_sample ( m, n, rng )
    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 7 ):

      e[0:m] = e_test[j,0:m]

      value = monomial_value ( m, n, e, x )

      result = hypercube01_volume ( m ) * np.sum ( value[0:n] ) / float ( n )

      print ( '  %14.6g' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  print ( '' )
  print ( '     Exact', end = '' )

  for j in range ( 0, 7 ):

    e[0:m] = e_test[j,0:m]

    result = hypercube01_monomial_integral ( m, e )
    print ( '  %14.6g' % ( result ), end = '' )

  print ( '' )

  return

def hypercube01_sample ( m, n, rng ):

#*****************************************************************************80
#
## hypercube01_sample() samples points in the unit hypercube in M dimensions.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of points.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(M,N), the points.
#
  import numpy as np

  x = rng.random ( size = [ m, n ] )

  return x

def hypercube01_sample_test ( rng ):

#*****************************************************************************80
#
## hypercube01_sample_test() tests hypercube01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'hypercube01_sample_test():' )
  print ( '  hypercube01_sample() samples the unit hypercube' )
  print ( '  in M dimensions.' )

  m = 3
  n = 10

  x = hypercube01_sample ( m, n, rng )

  r8mat_transpose_print ( m, n, x, '  Sample points in the unit hypercube.' )

  return

def hypercube01_volume ( m ):

#*****************************************************************************80
#
## hypercube01_volume() returns the volume of the unit hypercube in M dimensions.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real VALUE, the volume.
#
  value = 1.0

  return value

def hypercube01_volume_test ( ) :

#*****************************************************************************80
#
## hypercube01_volume() tests hypercube01_volume().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hypercube01_volume_test():' )
  print ( '  hypercube01_volume() returns the volume of the unit hypercube' )
  print ( '  in M dimensions.' )

  m = 3

  value = hypercube01_volume ( m )

  print ( '' )
  print ( '  hypercube01_volume(%d) = %g' % ( m, value ) )

  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_print() prints an I4VEC.
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
#    integer N, the dimension of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_transpose_print() prints an I4VEC "transposed".
#
#  Example:
#
#    A = (/ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 /)
#    TITLE = 'My vector:  '
#
#    My vector:
#
#       1    2    3    4    5
#       6    7    8    9   10
#      11
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  if ( 0 < n ):
    for i in range ( 0, n ):
      print ( '%8d' % ( a[i] ), end = '' )
      if ( ( i + 1 ) % 10 == 0 or i == n - 1 ):
        print ( '' )
  else:
    print ( '  (empty vector)' )

  return

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

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
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
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
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

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row', end = '' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

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
    print ( '  Col', end = '' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

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

def hypercube_monte_carlo_test ( ):

#*****************************************************************************80
#
## hypercube_monte_carlo_test() tests hypercube_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 November 2016
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'hypercube_monte_carlo_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hypercube_monte_carlo().' )

  rng = default_rng ( )

  hypercube01_monomial_integral_test ( rng )
  hypercube01_monte_carlo_test01 ( rng )
  hypercube01_monte_carlo_test02 ( rng )
  hypercube01_sample_test ( rng )
  hypercube01_volume_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hypercube_monte_carlo_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  hypercube_monte_carlo_test ( )
  timestamp ( )

