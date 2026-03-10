#! /usr/bin/env python3
#
def hypersphere01_area ( m ):

#*****************************************************************************80
#
## hypersphere01_area() returns the surface area of the unit hypersphere.
#
#  Discussion:
#
#     M   Area
#
#     2    2        * PI
#     3    4        * PI
#     4  ( 2 /   1) * PI^2
#     5  ( 8 /   3) * PI^2
#     6  ( 1 /   1) * PI^3
#     7  (16 /  15) * PI^3
#     8  ( 1 /   3) * PI^4
#     9  (32 / 105) * PI^4
#    10  ( 1 /  12) * PI^5
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 January 2014
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
#    real VALUE, the area of the unit hypersphere.
#
  import numpy as np

  if ( ( m % 2 ) == 0 ):
    m_half = ( m // 2 )
    value = 2.0 * np.pi ** m_half
    for i in range (  1, m_half ):
      value = value / float ( i )
  else:
    m_half = ( ( m - 1 ) // 2 )
    value = np.pi ** m_half * 2.0 ** m
    for i in range ( m_half + 1, 2 * m_half + 1 ):
      value = value / float ( i )

  return value

def hypersphere01_area_test ( ) :

#*****************************************************************************80
#
## hypersphere01_area_test() tests hypersphere01_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'hypersphere01_area_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  hypersphere01_area returns the area of the unit hypersphere.' )
  print ( '' )
  print ( '   M  Area' )
  print ( '' )

  for m in range ( 1, 11 ):
    value = hypersphere01_area ( m )
    print ( '  %2d  %g' % ( m, value ) )

  return

def hypersphere01_monomial_integral ( m, e ):

#*****************************************************************************80
#
## hypersphere01_monomial_integral(): monomial integrals on the unit hypersphere.
#
#  Discussion:
#
#    The integration region is 
#
#      sum ( 1 <= I <= M ) X(I)^2 = 1.
#
#    The monomial is F(X) = product ( 1 <= I <= M ) X(I)^E(I)
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
#    integer E(M), the exponents of X(1) through X(M). 
#    Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  from scipy.special import gamma

  for i in range ( 0, m ):
    if ( e[i] < 0 ):
      print ( '' )
      print ( 'hypersphere01_monomial_integral(): Fatal error!' )
      print ( '  All exponents must be nonnegative.' )
      raise Exception ( 'hypersphere01_monomial_integral - Fatal error!' )

  for i in range ( 0, m ):
    if ( ( e[i] % 2 ) == 1 ):
      integral = 0.0
      return integral

  integral = 2.0

  for i in range ( 0, m ):
    arg = 0.5 * float ( e[i] + 1 )
    integral = integral * gamma ( arg )

  s = 0
  for i in range ( 0, m ):
    s = s + float ( e[i] + 1 )

  arg = 0.5 * float ( s )
  integral = integral / gamma ( arg )

  return integral

def hypersphere01_monomial_integral_test ( rng ):

#*****************************************************************************80
#
## hypersphere01_monomial_integral_test() tests hypersphere01_monomial_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 January 2014
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
  n = 4192
  test_num = 20

  print ( '' )
  print ( 'hypersphere01_monomial_integral_test():' )
  print ( '  hypersphere01_monomial_integral() returns the integral of' )
  print ( '  a monomial over the surface of the unit hypersphere in 3D.' )
  print ( '  Compare with a Monte Carlo estimate.' )
#
#  Get sample points.
#
  x = hypersphere01_sample ( m, n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose X,Y,Z exponents between (0,0,0) and (8,8,8).
#
  print ( '' )
  print ( '  If any exponent is odd, the integral is zero.' )
  print ( '  We will restrict this test to randomly chosen even exponents.' )
  print ( '' )
  print ( '  Ex  Ey  Ez     MC-Estimate           Exact      Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = rng.integers ( low = 0, high = 4, size = m, endpoint = True )

    for i in range ( 0, m ):
      e[i] = e[i] * 2

    value = monomial_value ( m, n, e, x )

    result = hypersphere01_area ( m ) * np.sum ( value ) / float ( n )
    exact = hypersphere01_monomial_integral ( m, e )
    error = abs ( result - exact )

    for i in range ( 0, m ):
      print ( '  %2d' % ( e[i] ), end = '' )
    print ( '  %14.6g  %14.6g  %10.2g' % ( result, exact, error ) )

  return

def hypersphere01_monte_carlo_test01 ( rng ):

#*****************************************************************************80
#
## hypersphere01_monte_carlo_test01() tests hypersphere01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2016
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
    [ 2, 0, 0 ], \
    [ 0, 2, 0 ], \
    [ 0, 0, 2 ], \
    [ 4, 0, 0 ], \
    [ 2, 2, 0 ], \
    [ 0, 0, 4 ] ] )

  print ( '' )
  print ( 'hypersphere01_monte_carlo_test01():' )
  print ( '  hypersphere01_sample() estimates integrals over ' )
  print ( '  the surface of the unit hypersphere in M dimensions.' )
  print ( '' )
  print ( '  Spatial dimension M = %d' % ( m ) )
  print ( '' )
  print ( '         N        1              X^2             Y^2', end = '' )
  print ( '             Z^2             X^4           X^2Y^2           Z^4' )
  print ( '' )

  n = 1

  e = np.zeros ( m, dtype = np.int32 )

  while ( n <= 65536 ):

    x = hypersphere01_sample ( m, n, rng )

    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 7 ):

      e[0:m] = e_test[j,0:m]

      value = monomial_value ( m, n, e, x )

      result = hypersphere01_area ( m ) * np.sum ( value[0:n] ) / float ( n )

      print ( '  %14f' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  print ( '' )
  print ( '     Exact', end = '' )

  for j in range ( 0, 7 ):

    e[0:m] = e_test[j,0:m]

    result = hypersphere01_monomial_integral ( m, e )

    print ( '  %14f' % ( result ), end = '' )

  print ( '' )

  return

def hypersphere01_monte_carlo_test02 ( rng ):

#*****************************************************************************80
#
## hypersphere01_monte_carlo_test02() tests hypersphere01_sample() in dimension 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 November 2016
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
  print ( 'hypersphere01_monte_carlo_test02():' )
  print ( '  hypersphere01_sample() estimates integrals over ' )
  print ( '  the surface of the unit hypersphere in M dimensions.' )
  print ( '' )
  print ( '  Spatial dimension M = %d' % ( m  ) )
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

    x = hypersphere01_sample ( m, n, rng )

    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 7 ):

      e[0:m] = e_test[j,0:m]

      value = monomial_value ( m, n, e, x )

      result = hypersphere01_area ( m ) * np.sum ( value[0:n] ) / float ( n )

      print ( '  %14f' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  print ( '' )
  print ( '     Exact', end = '' )

  for j in range ( 0, 7 ):

    e[0:m] = e_test[j,0:m]

    result = hypersphere01_monomial_integral ( m, e )

    print ( '  %14f' % ( result ), end = '' )

  print ( '' )

  return

def hypersphere01_sample ( m, n, rng ):

#*****************************************************************************80
#
## hypersphere01_sample() uniformly samples the surface of the unit hypersphere.
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

  x = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
#
#  Fill a vector with normally distributed values.
#
    v = rng.standard_normal ( size = m )
#
#  Compute the length of the vector.
#
    norm = np.linalg.norm ( v )
#
#  Normalize the vector.
#
    for i in range ( 0, m ):
      x[i,j] = v[i] / norm

  return x

def hypersphere01_sample_test ( rng ):

#*****************************************************************************80
#
## hypersphere01_sample_test() tests hypersphere01_sample().
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
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'hypersphere01_sample_test()' )
  print ( '  hypersphere01_sample() samples the unit hypersphere' )
  print ( '  in M dimensions.' )

  m = 3
  n = 10

  x = hypersphere01_sample ( m, n, rng )

  r8mat_transpose_print ( m, n, x, '  Sample points on the unit hypersphere.' )

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

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
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
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

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

def hypersphere_monte_carlo_test ( ):

#*****************************************************************************80
#
## hypersphere_monte_carlo_test() tests hypersphere_monte_carlo().
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
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'hypersphere_monte_carlo_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hypersphere_monte_carlo().' )

  rng = default_rng ( )

  hypersphere01_area_test ( )
  hypersphere01_monomial_integral_test ( rng )
  hypersphere01_monte_carlo_test01 ( rng )
  hypersphere01_monte_carlo_test02 ( rng )
  hypersphere01_sample_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'hypersphere_monte_carlo_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  hypersphere_monte_carlo_test ( )
  timestamp ( )

