#! /usr/bin/env python3
#
def ellipsoid_monte_carlo_test ( ):

#*****************************************************************************80
#
## ellipsoid_monte_carlo_test() tests ellipsoid_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ellipsoid_monte_carlo_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ellipsoid_monte_carlo().' )

  ellipsoid_monte_carlo_test01 ( )
  ellipsoid_monte_carlo_test02 ( )
  ellipsoid_monte_carlo_test03 ( )
  ellipsoid_sample_test ( )
  ellipsoid_volume_test ( )
  hypersphere_unit_volume_test ( )
  r8po_fa_test ( )
  r8po_sl_test ( )
  uniform_in_sphere01_map_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ellipsoid_monte_carlo_test():' ) 
  print ( '  Normal end of execution.' )
  return

def ellipsoid_monte_carlo_test01 ( ):

#*****************************************************************************80
#
## ellipsoid_monte_carlo_test01() uses ellipsoid_sample() on a 2D ellipse centered at (0,0).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  m = 2

  a = np.array ( [ \
    [ 9.0, 1.0 ], \
    [ 1.0, 4.0 ] ] )

  e_test = np.array ( [ \
    [ 0, 0 ], \
    [ 1, 0 ], \
    [ 0, 1 ], \
    [ 2, 0 ], \
    [ 1, 1 ], \
    [ 0, 2 ], \
    [ 3, 0 ] ] )

  r = 2.0
  v = np.array ( [ 0.0, 0.0 ] )

  print ( '' )
  print ( 'ellipsoid_monte_carlo_test01()' )
  print ( '  ellipsoid_sample() estimates integrals' )
  print ( '  in a 2D ellipse x'' * A * x <= r^2.' )

  print ( '' )
  print ( '  Ellipsoid radius R = %g' % ( r ) )
  r8vec_print ( m, v, '  Ellipsoid center V:' )
  r8mat_print ( m, m, a, '  Ellipsoid matrix A:' )

  volume = ellipsoid_volume ( m, a, v, r )
  print ( '' )
  print ( '  Ellipsoid volume = %g' % ( volume ) )
  print ( '' )
  print ( '         N        1              X               Y               X^2               XY             Y^2             X^3' )
  print ( '' )

  e = np.zeros ( m )

  n = 1

  while ( n <= 65536 ):

    x = ellipsoid_sample ( m, n, a, v, r, rng )

    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 7 ):

      e[0:m] = e_test[j,0:m]

      value = monomial_value ( m, n, e, x )

      result = volume * np.sum ( value[0:n] ) / float ( n )

      print ( '  %14.6g' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  return

def ellipsoid_monte_carlo_test02 ( ):

#*****************************************************************************80
#
## ellipsoid_monte_carlo_test02() uses ellipsoid_sample() on a 2D ellipse centered at (2,3).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )
  m = 2

  a = np.array ( [ \
    [ 9.0, 1.0 ], \
    [ 1.0, 4.0 ] ] )

  e_test = np.array ( [ \
    [ 0, 0 ], \
    [ 1, 0 ], \
    [ 0, 1 ], \
    [ 2, 0 ], \
    [ 1, 1 ], \
    [ 0, 2 ], \
    [ 3, 0 ] ] )

  r = 0.5

  v = np.array ( [ 2.0, 3.0 ] )

  print ( '' )
  print ( 'ellipsoid_monte_carlo_test02():' )
  print ( '  ellipsoid_sample() estimates integrals' )
  print ( '  in a 2D ellipse (x-v)'' * A * (x-v) <= r^2.' )

  print ( '' )
  print ( '  Ellipsoid radius R = %g' % ( r ) )
  r8vec_print ( m, v, '  Ellipsoid center V:' )
  r8mat_print ( m, m, a, '  Ellipsoid matrix A:' )

  volume = ellipsoid_volume ( m, a, v, r )
  print ( '' )
  print ( '  Ellipsoid volume = %g' % ( volume ) )
  print ( '' )
  print ( '         N        1              X               Y               X^2               XY             Y^2             X^3' )
  print ( '' )

  n = 1

  e = np.zeros ( 2 )

  while ( n <= 65536 ):

    x = ellipsoid_sample ( m, n, a, v, r, rng )

    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 7 ):

      e[0:m] = e_test[j,0:m]

      value = monomial_value ( m, n, e, x )

      result = volume * np.sum ( value[0:n] ) / float ( n )

      print ( '  %14.6g' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  return

def ellipsoid_monte_carlo_test03 ( ):

#*****************************************************************************80
#
## ellipsoid_monte_carlo_test03() uses ellipsoid_sample() on a 3D ellipse centered at (1,2,3).
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
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )
  m = 3

  a = np.array ( [ \
    [ 9.0, 6.0, 3.0 ], \
    [ 6.0, 5.0, 4.0 ], \
    [ 3.0, 4.0, 9.0 ] ] )

  e_test = np.array ( [ \
    [ 0, 0, 0 ], \
    [ 1, 0, 0 ], \
    [ 0, 1, 0 ], \
    [ 0, 0, 1 ], \
    [ 2, 0, 0 ], \
    [ 0, 2, 2 ], \
    [ 0, 0, 3 ] ] )

  r = 0.5

  v = np.array ( [ 1.0, 2.0, 3.0 ] )

  print ( '' )
  print ( 'ellipsoid_monte_carlo_test03():' )
  print ( '  ellipsoid_sample() estimates integrals' )
  print ( '  in a 3D ellipse (x-v)'' * A * (x-v) <= r^2.' )

  print ( '' )
  print ( '  Ellipsoid radius R = %g' % ( r ) )
  r8vec_print ( m, v, '  Ellipsoid center V:' )
  r8mat_print ( m, m, a, '  Ellipsoid matrix A:' )

  volume = ellipsoid_volume ( m, a, v, r )
  print ( '' )
  print ( '  Ellipsoid volume = %g' % ( volume ) )
  print ( '' )
  print ( '         N        1              X               Y                Z                X^2            YZ              Z^3' )
  print ( '' )

  n = 1

  e = np.zeros ( 3 )

  while ( n <= 65536 ):

    x = ellipsoid_sample ( m, n, a, v, r, rng )

    print ( '  %8d' % ( n ) )

    for j in range ( 0, 7 ):

      e[0:m] = e_test[j,0:m]

      value = monomial_value ( m, n, e, x )

      result = volume * np.sum ( value[0:n] ) / float ( n )

      print ( '  %14.6g' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  return

def ellipsoid_sample ( m, n, a, v, r, rng ):

#*****************************************************************************80
#
## ellipsoid_sample() samples points uniformly from an ellipsoid.
#
#  Discussion:
#
#    The points X in the ellipsoid are described by a M by M
#    positive definite symmetric matrix A, a "center" V, and 
#    a "radius" R, such that
#
#      (X-V)' * A * (X-V) <= R * R
#
#    The algorithm computes the Cholesky factorization of A:
#
#      A = U' * U.
#
#    A set of uniformly random points Y is generated, satisfying:
#
#      Y' * Y <= R * R.
#
#    The appropriate points in the ellipsoid are found by solving
#
#      U * X = Y
#      X = X + V
#
#    Thanks to Dr Karl-Heinz Keil for pointing out that the original
#    coding was actually correct only if A was replaced by its inverse.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Reference:
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
#    integer M, the dimension of the space.
#
#    integer N, the number of points.
#
#    real A(M,M), the matrix that describes
#    the ellipsoid.
#
#    real V(M), the "center" of the ellipsoid.
#
#    real R, the "radius" of the ellipsoid.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(M,N), the points.
#
  import numpy as np
#
#  Get the Cholesky factor U.
#
  u = r8po_fa ( m, a )
#
#  Get the points Y that satisfy Y' * Y <= 1.
#
  y = uniform_in_sphere01_map ( m, n, rng )
#
#  Get the points Y that satisfy Y' * Y <= R * R.
#
  y = r * y
#
#  Solve U * X = Y.
#
  x = np.zeros ( [ m, n ] )
  sol = np.zeros ( m )
  rhs = np.zeros ( m )

  for j in range ( 0, n ):
    rhs[0:m] = y[0:m,j]
    sol = r8po_sl ( m, u, rhs )
    x[0:m,j] = sol[0:m]
#
#  X = X + V.
#
  for i in range ( 0, m ):
    x[i,0:n] = x[i,0:n] + v[i]

  return x

def ellipsoid_sample_test ( ):

#*****************************************************************************80
#
## ellipsoid_sample_test() tests ellipsoid_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'ellipsoid_sample_test():' )
  print ( '  ellipsoid_sample() samples the ellipsoid' )
  print ( '    (X-V)\' * A * (X-V) <= R * R.' )

  m = 3
  n = 20
  a = np.array ( [ \
    [ 9.0, 3.0, 3.0 ], \
    [ 3.0, 5.0, 3.0 ], \
    [ 3.0, 3.0, 3.0 ] ] )
  v = np.array ( [ 2.0, 3.0, 1.0 ] )
  r = 1.0

  print ( '' )
  print ( '  M = %d' % ( m ) )
  r8mat_print ( m, m, a, '  A:' )
  r8vec_print ( m, v, '  V:' )

  x = ellipsoid_sample ( m, n, a, v, r, rng )

  r8mat_transpose_print ( m, n, x, '  Ellipsoid sample points:' )

  return

def ellipsoid_volume ( m, a, v, r ):

#*****************************************************************************80
#
## ellipsoid_volume() returns the volume of an ellipsoid.
#
#  Discussion:
#
#    The points X in the ellipsoid are described by an M by M
#    positive definite symmetric matrix A, an M-dimensional point V,
#    and a "radius" R, such that
#      (X-V)' * A * (X-V) <= R * R
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    real A(M,M), the matrix that describes
#    the ellipsoid.  A must be symmetric and positive definite.
#
#    real V(M), the "center" of the ellipse.
#    The value of V is not actually needed by this function.
#
#    real R, the "radius" of the ellipse.
#
#  Output:
#
#    real VOLUME, the volume of the ellipsoid.
#
  u = r8po_fa ( m, a )
 
  sqrt_det = 1.0
  for i in range ( 0, m ):
    sqrt_det = sqrt_det * u[i,i]

  volume = r ** m * hypersphere_unit_volume ( m ) / sqrt_det

  return volume

def ellipsoid_volume_test ( ):

#*****************************************************************************80
#
## ellipsoid_volume_test() tests ellipsoid_volume().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ellipsoid_volume_test():' )
  print ( '  ellipsoid_volume() computes the volume of the ellipsoid' )
  print ( '    (X-V)\' * A * (X-V) <= R * R.' )

  m = 3;
  a = np.array ( [ \
    [ 9.0, 3.0, 3.0 ], \
    [ 3.0, 5.0, 3.0 ], \
    [ 3.0, 3.0, 3.0 ] ] )
  v = np.array ( [ 2.0, 3.0, 1.0 ] )
  r = 1.0

  print ( '' )
  print ( '  M = %d' % ( m ) )
  r8mat_print ( m, m, a, '  A:' )
  r8vec_print ( m, v, '  V:' )

  volume = ellipsoid_volume ( m, a, v, r )

  print ( '' )
  print ( '  Volume = %14.6g' % ( volume ) )

  return

def hypersphere_unit_volume ( m ):

#*****************************************************************************80
#
## hypersphere_unit_volume(): volume of a unit hypersphere in M dimensions.
#
#  Discussion:
#
#    The unit sphere in ND satisfies:
#
#      sum ( 1 <= I <= M ) X(I) * X(I) = 1
#
#    Results for the first few values of M are:
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
#    For the unit sphere, Volume(M) = 2 * PI * Volume(M-2) / M
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2005
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the dimension of the space.
#
#  Output:
#
#    real VOLUME, the volume of the sphere.
#
  import numpy as np

  if ( ( m % 2 ) == 0 ):
    m2 = m // 2
    volume = np.pi ** m2
    for i in range ( 1, m2 + 1 ):
      volume = volume / float ( i )
  else:
    m2 = ( m - 1 ) // 2
    volume = np.pi ** m2 * 2.0 ** m
    for i in range ( m2 + 1, 2 * m2 + 2 ):
      volume = volume / float ( i )

  return volume

def hypersphere_unit_volume_test ( ):

#*****************************************************************************80
#
## hypersphere_unit_volume_test() tests hypersphere_unit_volume().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hypersphere_unit_volume_test():' )
  print ( '  hypersphere_unit_volume() computes the volume of the unit' )
  print ( '  hypersphere in M dimensions.' )
  print ( '' )
  print ( '   M        Volume' )
  print ( '' )

  for m in range ( 1, 11 ):
    volume = hypersphere_unit_volume ( m )
    print ( '  %2d  %14.6g' % ( m, volume ) )

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

def r83col_print_part ( n, a, max_print, title ):

#*****************************************************************************80
#
## r83col_print_part() prints "part" of an R83COL.
#
#  Discussion:
#
#    An R83COL is a (3,N) array of R8's.
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_print, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vector.
#
#    real A(N,3), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines
#    to print.
#
#    string TITLE, a title.
#
  if ( 0 < max_print ):

    if ( 0 < n ):

      if ( 0 < len ( title ) ):
        print ( '' )
        print ( title )

      print ( '' )

      if ( n <= max_print ):

        for i in range ( 0, n ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )
 
      elif ( 3 <= max_print ):

        for i in range ( 0, max_print - 2 ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )
        print ( '  ....  ..............  ..............  ..............' )
        i = n - 1
        print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )

      else:

        for i in range ( 0, max_print - 1 ):
          print ( '  %4d  %14g  %14g  %14g' % ( i, a[i,0], a[i,1], a[i,2] ) )
        i = max_print - 1
        print ( '  %4d  %14g  %14g  %14g  ...more entries...' \
          % ( i, a[i,0], a[i,1], a[i,2] ) )

  return

def r83col_print_part_test ( ):

#*****************************************************************************80
#
## r83col_print_part_test() tests r83col_print_part().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r83col_print_part_test():' )
  print ( '  r83col_print_part() prints part of an R83COL.' )

  n = 10

  v = np.array ( [ \
    [  11,  12,  13 ], \
    [  21,  22,  23 ], \
    [  31,  32,  33 ], \
    [  41,  42,  43 ], \
    [  51,  52,  53 ], \
    [  61,  62,  63 ], \
    [  71,  72,  73 ], \
    [  81,  82,  83 ], \
    [  91,  92,  93 ], \
    [ 101, 102, 103 ] ] )

  max_print = 2
  r83col_print_part ( n, v, max_print, '  Output with MAX_print = 2' )

  max_print = 5
  r83col_print_part ( n, v, max_print, '  Output with MAX_print = 5' )

  max_print = 25
  r83col_print_part ( n, v, max_print, '  Output with MAX_print = 25' )

  return

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
    print ( '  Row' )

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

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_test() tests r8mat_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_transpose_print_test():' )
  print ( '  r8mat_transpose_print() prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )

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

def r8mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_some_test() tests r8mat_transpose_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8mat_transpose_print_some_test():' )
  print ( '  r8mat_transpose_print_some() prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )

  return

def r8po_fa ( n, a ):

#*****************************************************************************80
#
## r8po_fa() factors a R8PO matrix.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_INVERSE.  For clarity, the lower triangle
#    is set to zero.
#
#    The positive definite symmetric matrix A has a Cholesky factorization
#    of the form:
#
#      A = R' * R
#
#    where R is an upper triangular matrix with positive elements on
#    its diagonal.  This routine overwrites the matrix A with its
#    factor R.
#
#    This function failed miserably when I wrote "r = a", because of a
#    disastrously misconceived feature of Python, which does not copy
#    one matrix to another, but makes them both point to the same object.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the matrix in R8PO storage.
#
#  Output:
#
#    real R(N,N), the Cholesky factor R in R8GE storage.
#
#    integer INFO, error flag.
#    0, normal return.
#    K, error condition.  The principal minor of order K is not
#    positive definite, and the factorization was not completed.
#
  import numpy as np

  r = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      r[i,j] = a[i,j]

  for j in range ( 0, n ):

    for k in range ( 0, j ):
      t = 0.0
      for i in range ( 0, k ):
        t = t + r[i,k] * r[i,j]
      r[k,j] = ( r[k,j] - t ) / r[k,k]

    t = 0.0
    for i in range ( 0, j ):
      t = t + r[i,j] ** 2

    s = r[j,j] - t

    if ( s <= 0.0 ):
      print ( '' )
      print ( 'r8po_fa(): Fatal error!' )
      print ( '  Factorization fails on column %d.' % ( j ) )
      raise Exception ( 'r8po_fa(): Fatal error!' )

    r[j,j] = np.sqrt ( s )
#
#  Since the Cholesky factor is stored in R8GE format, be sure to
#  zero out the lower triangle.
#
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      r[i,j] = 0.0

  return r

def r8po_fa_test ( ):

#*****************************************************************************80
#
## r8po_fa_test() tests r8po_fa();
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'r8po_fa_test():' )
  print ( '  r8po_fa() factors a positive definite symmetric' )
  print ( '  linear system,' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = min ( i, j ) + 1

  r8mat_print ( n, n, a, '  The matrix A:' )
#
#  Factor the matrix.
#
  r = r8po_fa ( n, a )

  r8mat_print ( n, n, r, '  The factor R (a R8UT matrix):' )
#
#  Compute the product R' * R.
#
  rtr = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      k_hi = min ( i + 1, j + 1 )
      for k in range ( 0, k_hi ):
        rtr[i,j] = rtr[i,j] + r[k,i] * r[k,j]

  r8mat_print ( n, n, rtr, '  The product R\' * R:' )

  return

def r8po_sl ( n, r, b ):

#*****************************************************************************80
#
## r8po_sl() solves a R8PO system factored by r8po_fa().
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by r8po_INVERSE.  For clarity, the lower triangle
#    is set to zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real R(N,N), the Cholesky factor, in R8GE storage, 
#    returned by r8po_fa.
#
#    real B(N), the right hand side.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]
#
#  Solve R' * y = b.
#
  for k in range ( 0, n ):
    t = 0.0
    for i in range ( 0, k ):
      t = t + x[i] * r[i,k]
    x[k] = ( x[k] - t ) / r[k,k]
#
#  Solve R * x = y.
#
  for k in range ( n - 1, -1, -1 ):
    x[k] = x[k] / r[k,k]
    for i in range ( 0, k ):
      x[i] = x[i] - r[i,k] * x[k]

  return x

def r8po_sl_test ( ):

#*****************************************************************************80
#
## r8po_sl_test() tests r8po_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'r8po_sl_test():' )
  print ( '  r8po_sl() solves a linear system with an R8PO matrix' )
  print ( '  after it has been factored by r8po_fa.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set (the upper half of) matrix A.
#
  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    a[i,i] = 2.0
  for i in range ( 0, n - 1 ):
    a[i,i+1] = -1.0

  r8mat_print ( n, n, a, '  Matrix A:' )
#
#  Factor the matrix.
#
  r = r8po_fa ( n, a )
#
#  Set the right hand side.
#
  b = np.zeros ( n )
  b[n-1] = float ( n + 1 )
  r8vec_print ( n, b, '  Right hand side b:' )
#
#  Solve the linear system.
#
  x = r8po_sl ( n, r, b )
  r8vec_print ( n, x, '  Solution x:' )

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

def uniform_in_sphere01_map ( m, n, rng ):

#*****************************************************************************80
#
## uniform_in_sphere01_map() maps uniform points in the unit M-dimensional sphere.
#
#  Discussion:
#
#    The sphere has center 0 and radius 1.
#
#    We first generate a point ON the sphere, and then distribute it
#    IN the sphere.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 January 2024
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
#    Wiley, 1986, page 232.
#
#  Input:
#
#    integer M, the dimension of the space.
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

  exponent = 1.0 / float ( m )

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
    v[0:m] = v[0:m] / norm
#
#  Now compute a value to map the point ON the sphere INTO the sphere.
#
    r = rng.random ( )

    x[0:m,j] = r ** exponent * v[0:m]
  
  return x

def uniform_in_sphere01_map_test ( ):

#*****************************************************************************80
#
## uniform_in_sphere01_map_test() tests uniform_in_sphere01_map().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import platform

  print ( '' )
  print ( 'uniform_in_sphere01_map_test():' )
  print ( '  uniform_in_sphere01_map() computes points uniformly distributed' )
  print ( '  inside the M-dimensional unit sphere.' )

  rng = default_rng ( )
  m = 3
  n = 10

  x = uniform_in_sphere01_map ( m, n, rng )

  r8mat_transpose_print ( m, n, x, '  Random points inside unit 3-sphere' )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  ellipsoid_monte_carlo_test ( )
  timestamp ( )

