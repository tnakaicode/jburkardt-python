#! /usr/bin/env python3
#
def hyperball_monte_carlo_test01 ( rng ):

#*****************************************************************************80
#
## hyperball_monte_carlo_test01() tests hyperball01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2016
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
  print ( 'hyperball_monte_carlo_test01():' )
  print ( '  Use the Monte Carlo method to estimate integrals' )
  print ( '  over the interior of the unit hyperball in M dimensions.' )
  print ( '' )
  print ( '  Spatial dimension M = %d' % ( m ) )
  print ( '' )
  print ( '         N        1              X^2             Y^2', end = '' )
  print ( '             Z^2             X^4           X^2Y^2           Z^4' )
  print ( '' )

  n = 1

  e = np.zeros ( 7 )

  while ( n <= 65536 ):

    x = hyperball01_sample ( m, n, rng )

    print ( '  %8d' % ( n ), end = '' )
    for j in range ( 0, 7 ):
      e[0:m] = e_test[j,0:m]
      value = monomial_value ( m, n, e, x )
      result = hyperball01_volume ( m ) * np.sum ( value[0:n] ) / float ( n )
      print ( '  %14.6g' % ( result ), end = '' )
    print ( '' )

    n = 2 * n

  print ( '' )
  print ( '     Exact', end = '' )
  for j in range ( 0, 7 ):
    e[0:m] = e_test[j,0:m]
    result = hyperball01_monomial_integral ( m, e )
    print ( '  %14.6g' % ( result ), end = '' )

  print ( '' )

  return

def hyperball_monte_carlo_test02 ( rng ):

#*****************************************************************************80
#
## hyperball_monte_carlo_test02() uses hyperball01_sample() in 6D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 November 2016
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
  import platform

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
  print ( 'hyperball_monte_carlo_test02():' )
  print ( '  Use the Monte Carlo method to estimate integrals' )
  print ( '  over the interior of the unit hyperball in M dimensions.' )
  print ( '' )
  print ( '  Spatial dimension M = %d' % ( m ) )
  print ( '' )
  print ( '         N', end = '' )
  print ( '        1      ', end = '' )
  print ( '        U      ', end = '' )
  print ( '         V^2   ', end = '' )
  print ( '         V^2W^2', end = '' )
  print ( '         X^4   ', end = '' )
  print ( '         Y^2Z^2', end = '' )
  print ( '         Z^6', end = '' )
  print ( '' )

  n = 1
  e = np.zeros ( m )

  while ( n <= 65536 ):

    x = hyperball01_sample ( m, n, rng )

    print ( '  %8d' % ( n ), end = '' )
    for j in range ( 0, 7 ):
      e[0:m] = e_test[j,0:m]
      value = monomial_value ( m, n, e, x )
      result = hyperball01_volume ( m ) * np.sum ( value[0:n] ) / float ( n )
      print ( '  %14.6g' % ( result ), end = '' )
    print ( '' )

    n = 2 * n

  print ( '' )
  print ( '     Exact', end = '' )
  for j in range ( 0, 7 ):
    e[0:m] = e_test[j,0:m]
    result = hyperball01_monomial_integral ( m, e )
    print ( '  %14.6g' % ( result ), end = '' )
  print ( '' )

  return

def hyperball01_monomial_integral ( m, e ):

#*****************************************************************************80
#
## hyperball01_monomial_integral(): integrals in unit hyperball in M dimensions.
#
#  Discussion:
#
#    The integration region is 
#
#      sum ( 1 <= I <= M ) X(I)^2 <= 1.
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
#  Reference:
#
#    Gerald Folland,
#    How to Integrate a Polynomial Over a Sphere,
#    American Mathematical Monthly,
#    Volume 108, Number 5, May 2001, pages 446-448.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer E(M): the exponents.  Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  from scipy.special import gamma

  for i in range ( 0, m ):
    if ( e[i] < 0 ):
      print ( '' )
      print ( 'hyperball01_monomial_integral(): Fatal error!' )
      print ( '  All exponents must be nonnegative.' )
      raise Exception ( 'hyperball01_monomial_integral(): Fatal error!' )
#
#  Integrate over the surface.
#
  for i in range ( 0, m ):
    if ( ( e[i] % 2 ) == 1 ):
      integral = 0.0
      return integral

  integral = 2.0

  for i in range ( 0, m ):
    integral = integral * gamma ( 0.5 * float ( e[i] + 1 ) )
 
  s = 0
  for i in range ( 0, m ):
   s = s + e[i] + 1

  integral = integral / gamma ( 0.5 * float ( s ) )
#
#  The surface integral is now adjusted to give the volume integral.
#
  r = 1.0

  integral = integral * r ** s / float ( s )

  return integral

def hyperball01_monomial_integral_test ( rng ):

#*****************************************************************************80
#
## hyperball01_monomial_integral_test() tests hyperball01_monomial_integral().
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
  import numpy as np

  m = 3
  n = 4192
  test_num = 20

  print ( '' )
  print ( 'hyperball01_monomial_integral_test():' )
  print ( '  hyperball01_monomial_integral() computes the integral of a monomial' )
  print ( '  over the interior of the unit hyperball in M dimensions.' )
  print ( '  Compare with a Monte Carlo estimate.' )
  print ( '' )
  print ( '  Spatial dimension M = %d' % ( m ) )
#
#  Get sample points.
#
  x = hyperball01_sample ( m, n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose exponents between 0 and 8.
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

    result = hyperball01_volume ( m ) * np.sum ( value ) / float ( n )
    exact = hyperball01_monomial_integral ( m, e )
    error = abs ( result - exact )

    for i in range ( 0, m ):
      print ( '  %2d' % ( e[i] ), end = '' )
    print ( '  %14.6g  %14.6g  %10.2g' % ( result, exact, error ) )

  return

def hyperball01_sample ( m, n, rng ):

#*****************************************************************************80
#
## hyperball01_sample() uniformly samples the unit hyperball in M dimensions.
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
#    Russell Cheng,
#    Random Variate Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998, pages 168.
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation, and Sensitivity 
#    of Queueing Networks,
#    Krieger, 1992,
#    ISBN: 0894647644,
#    LC: QA298.R79.
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
#    real X(M,N): the points.
#
  import numpy as np

  x = np.zeros ( [ m, n ] )

  exponent = 1.0 / float ( m )

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
      v[i] = v[i] / norm
#
#  Now compute a value to map the point ON the sphere INTO the sphere.
#
    r = rng.random ( )

    for i in range ( 0, m ):
      x[i,j] = r ** exponent * v[i]

  return x

def hyperball01_sample_test ( rng ):

#*****************************************************************************80
#
## hyperball01_sample_test() tests hyperball01_sample().
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
  import platform

  print ( '' )
  print ( 'hyperball01_sample_test():' )
  print ( '  hyperball01_sample() samples the unit hyperball.' )

  m = 3
  n = 10

  x = hyperball01_sample ( m, n, rng )

  r8mat_transpose_print ( m, n, x, '  Sample points in the unit hyperball.' )

  return

def hyperball01_volume ( m ):

#*****************************************************************************80
#
## hyperball01_volume() returns the volume of the unit hyperball in M dimensions.
#
#  Discussion:
#
#     M  Volume
#
#     1    2
#     2    1        * PI
#     3  ( 4 /   3) * PI
#     4  ( 1 /   2) * PI^2
#     5  ( 8 /  15) * PI^2
#     6  ( 1 /   6) * PI^3
#     7  (16 / 105) * PI^3
#     8  ( 1 /  24) * PI^4
#     9  (32 / 945) * PI^4
#    10  ( 1 / 120) * PI^5
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
#    real VOLUME, the volume of the unit ball.
#
  import numpy as np

  if ( ( m % 2 ) == 0 ):
    m_half = ( m // 2 );
    volume = np.pi ** m_half
    for i in range ( 1, m_half + 1 ):
      volume = volume / float ( i )
  else:
    m_half = ( ( m - 1 ) // 2 )
    volume = np.pi ** m_half * 2.0 ** m
    for i in range ( m_half + 1, 2 * m_half + 2 ):
      volume = volume / float ( i )

  return volume

def hyperball01_volume_test ( ):

#*****************************************************************************80
#
## hyperball01_volume_test() tests hyperball01_volume().
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
  print ( 'hyperball01_volume_test():' )
  print ( '  hyperball01_volume() returns the volume of the unit hyperball' )
  print ( '  in M dimensions.' )
  print ( '' )
  print ( '   M  Volume' )
  print ( '' )

  for m in range ( 1, 11 ):
    value = hyperball01_volume ( m )
    print ( '  %2d  %g' % ( m, value ) )

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
#    integer A(N): the vector to be printed.
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
#    integer A(N): the vector to be printed.
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
#    integer E(M): the exponents.
#
#    real X(M,N): the point coordinates.
#
#  Output:
#
#    real V(N): the monomial values.
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
#    real A(M,N): the matrix.
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
#    real A(M,N): an M by N matrix to be printed.
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
#    real A(N): the vector to be printed.
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

def hyperball_monte_carlo_test ( ):

#*****************************************************************************80
#
## hyperball_monte_carlo_test tests the hyperball_monte_carlo library.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2014
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'hyperball_monte_carlo_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hyperball_monte_carlo().' )

  rng = default_rng ( )

  hyperball_monte_carlo_test01 ( rng )
  hyperball_monte_carlo_test02 ( rng )
  hyperball01_monomial_integral_test ( rng )
  hyperball01_sample_test ( rng )
  hyperball01_volume_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hyperball_monte_carlo_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  hyperball_monte_carlo_test ( )
  timestamp ( )

