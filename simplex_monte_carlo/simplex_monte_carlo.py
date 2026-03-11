#! /usr/bin/env python3
#
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

def i4vec_print_test ( ):

#*****************************************************************************80
#
## i4vec_print_test() tests i4vec_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4vec_print_test' )
  print ( '  i4vec_print prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )

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
      print ( '%8d' % ( a[i] ) ),
      if ( ( i + 1 ) % 10 == 0 or i == n - 1 ):
        print ( '' )
  else:
    print ( '  (empty vector)' )

  return

def i4vec_transpose_print_test ( ):

#*****************************************************************************80
#
## i4vec_transpose_print_test() tests i4vec_transpose_print().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'i4vec_transpose_print_test' )
  print ( '  i4vec_transpose_print prints an I4VEC' )
  print ( '  with 5 entries to a row, and an optional title.' )

  n = 12
  a = np.zeros ( n, dtype = np.int32 )
  
  for i in range ( 0, n ):
    a[i] = i + 1

  i4vec_transpose_print ( n, a, '  My array:  ' )

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
    print ( '  Col: ' ),

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ) ),

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ) ),

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
  print ( 'r8mat_transpose_print_test' )
  print ( '  r8mat_transpose_print prints an R8MAT.' )

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
    print ( '  Row: ' ),

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ) ),

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ) ),
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ) ),

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
  print ( 'r8mat_transpose_print_some_test' )
  print ( '  r8mat_transpose_print_some prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )

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

def simplex_general_sample ( m, n, t, rng ):

#*****************************************************************************80
#
## simplex_general_sample() samples a general simplex in M dimensions.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 March 2017
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
#    integer M, the spatial dimension.
#
#    integer N, the number of points.
#
#    real T(M,M+1), the simplex vertices.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(M,N), the points.
#
  x1 = simplex_unit_sample ( m, n, rng )

  x = simplex_unit_to_general ( m, n, t, x1 )

  return x

def simplex_general_sample_test ( rng ):

#*****************************************************************************80
#
## simplex_general_sample_test() estimates integrals in 3D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2017
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
    [ 0, 1, 0, 0, 2, 1, 1, 0, 0, 0 ], \
    [ 0, 0, 1, 0, 0, 1, 0, 2, 1, 0 ], \
    [ 0, 0, 0, 1, 0, 0, 1, 0, 1, 2 ] ], dtype = np.int32 )

  e = np.zeros ( m, dtype = np.int32 )

  t = np.array ( [ \
    [ 1.0, 2.0, 1.0, 1.0 ], \
    [ 0.0, 0.0, 2.0, 0.0 ], \
    [ 0.0, 0.0, 0.0, 3.0 ] ] )

  print ( '' )
  print ( 'simplex_general_sample_test' )
  print ( '  simplex_general_sample computes a Monte Carlo estimate of an' )
  print ( '  integral over the interior of a general simplex in 3D.' )

  print ( '' )
  print ( '  Simplex vertices:' )
  print ( '' )
  for j in range ( 0, 4 ):
    for i in range ( 0, 3 ):
      print ( '%14.6g' % ( t[i,j] ), end = '' )
    print ( '' )
  print ( '' )
  print ( '         N        1               X               Y ', end = '' )
  print ( '              Z               X^2              XY             XZ', end = '' )
  print ( '              Y^2             YZ               Z^2' )
  print ( '' )

  n = 1

  while ( n <= 65536 ):

    x = simplex_general_sample ( m, n, t, rng )

    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 10 ):

      e[0:m] = e_test[0:m,j]

      value = monomial_value ( m, n, e, x )

      result = simplex_general_volume ( m, t ) * np.sum ( value[0:n] ) / n
      print ( '  %14.6g' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  return

def simplex_general_volume ( m, t ):

#*****************************************************************************80
#
## simplex_general_volume() computes the volume of a simplex in N dimensions.
#
#  Discussion:
#
#    The formula is: 
#
#      volume = 1/M! * det ( B )
#
#    where B is the M by M matrix obtained by subtracting one
#    vector from all the others.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 March 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the dimension of the space.
#
#    real T(M,M+1), the vertices.
#
#  Output:
#
#    real VOLUME, the volume of the simplex.
#
  import numpy as np

  b = np.zeros ( [ m, m ] )

  b[0:m,0:m] = t[0:m,0:m]
  for j in range ( 0, m ):
    b[0:m,j] = b[0:m,j] - t[0:m,m]

  volume = abs ( np.linalg.det ( b ) )

  for i in range ( 1, m + 1 ):
    volume = volume / float ( i )
  
  return volume

def simplex_unit_monomial_integral ( m, e ):

#*****************************************************************************80
#
## simplex_unit_monomial_integral(): integrals in the unit simplex in M dimensions.
#
#  Discussion:
#
#    The monomial is F(X) = product ( 1 <= I <= M ) X(I)^E(I).
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
#    integer M, the spatial dimension.
#
#    integer E(M), the exponents.  
#    Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  for i in range ( 0, m ):
    if ( e[i] < 0 ):
      print ( '' )
      print ( 'simplex_unit_monomial_integral - Fatal error!' )
      print ( '  All exponents must be nonnegative.' )
      raise Exception ( 'simplex_unit_monomial_integral - Fatal error!' )

  k = 0
  integral = 1.0

  for i in range ( 0, m ):

    for j in range ( 1, e[i] + 1 ):
      k = k + 1
      integral = integral * float ( j ) / float ( k )

  for i in range ( 0, m ):
    k = k + 1
    integral = integral / float ( k )

  return integral

def simplex_unit_monomial_integral_test ( rng ):

#*****************************************************************************80
#
## simplex_unit_monomial_integral_test() compares exact and estimated integrals in 3D.
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

  m = 3
  n = 4192
  test_num = 20

  print ( '' )
  print ( 'simplex_unit_monomial_integral_test():' )
  print ( '  Estimate monomial integrals using Monte Carlo' )
  print ( '  over the interior of the unit simplex in M dimensions.' )
#
#  Get sample points.
#
  x = simplex_unit_sample ( m, n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose exponents.
#
  print ( '' )
  print ( '  We randomly choose the exponents.' )
  print ( '' )
  print ( '  Ex  Ey  Ez     MC-Estimate      Exact           Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = rng.integers ( low = 0, high = 4, size = m, endpoint = True )

    value = monomial_value ( m, n, e, x )

    result = simplex_unit_volume ( m ) * np.sum ( value ) / float ( n )
    exact = simplex_unit_monomial_integral ( m, e )
    error = abs ( result - exact )

    for i in range ( 0, m ):
      print ( '  %2d' % ( e[i] ) ),
    print ( '  %14.6g  %14.6g  %10.2g' % ( result, exact, error ) )

  return

def simplex_unit_sample ( m, n, rng ):

#*****************************************************************************80
#
## simplex_unit_sample() samples the unit simplex in M dimensions.
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
#    real X(M,N), the points.
#
  import numpy as np

  x = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):

    e = rng.random ( size = m + 1 )

    e_sum = 0.0
    for i in range ( 0, m + 1 ):
      e[i] = - np.log ( e[i] )
      e_sum = e_sum + e[i]

    for i in range ( 0, m ):
      x[i,j] = e[i] / e_sum

  return x

def simplex_unit_sample_test00 ( rng ):

#*****************************************************************************80
#
## simplex_unit_sample_test00() tests simplex_unit_sample().
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
  print ( 'simplex_unit_sample_test00' )
  print ( '  simplex_unit_sample samples the unit simplex in M dimensions.' )

  m = 3
  n = 10
  x = simplex_unit_sample ( m, n, rng )

  r8mat_transpose_print ( m, n, x, '  Sample points in the unit simplex.' )

  return

def simplex_unit_sample_test01 ( rng ):

#*****************************************************************************80
#
## simplex_unit_sample_test01() estimates integrals in 3D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2017
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
    [ 0, 1, 0, 0, 2, 1, 1, 0, 0, 0 ], \
    [ 0, 0, 1, 0, 0, 1, 0, 2, 1, 0 ], \
    [ 0, 0, 0, 1, 0, 0, 1, 0, 1, 2 ] ], dtype = np.int32 )

  e = np.zeros ( m, dtype = np.int32 )

  print ( '' )
  print ( 'simplex_unit_sample_test01' )
  print ( '  simplex_unit_sample computes a Monte Carlo estimate of an' )
  print ( '  integral over the interior of the unit simplex in 3D.' )
  print ( '' )
  print ( '         N        1               X               Y ', end = '' )
  print ( '              Z               X^2              XY             XZ', end = '' )
  print ( '              Y^2             YZ               Z^2' )
  print ( '' )

  n = 1

  while ( n <= 65536 ):

    x = simplex_unit_sample ( m, n, rng )

    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 10 ):

      e[0:m] = e_test[0:m,j]

      value = monomial_value ( m, n, e, x )

      result = simplex_unit_volume ( m ) * np.sum ( value[0:n] ) / n
      print ( '  %14.6g' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  print ( '' )
  print ( '     Exact' )
  for j in range ( 0, 10 ):

    e[0:m] = e_test[0:m,j]

    result = simplex_unit_monomial_integral ( m, e )
    print ( '  %14.6g' % ( result ), end = '' )

  print ( '' )

  return

def simplex_unit_sample_test02 ( rng ):

#*****************************************************************************80
#
## simplex_unit_sample_test02() estimates integrals in 6D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2017
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
    [ 0, 1, 0, 0, 0, 2, 0 ], \
    [ 0, 0, 2, 2, 0, 0, 0 ], \
    [ 0, 0, 0, 2, 0, 0, 0 ], \
    [ 0, 0, 0, 0, 4, 0, 0 ], \
    [ 0, 0, 0, 0, 0, 2, 0 ], \
    [ 0, 0, 0, 0, 0, 2, 6 ] ], dtype = np.int32 )

  e = np.zeros ( m, dtype = np.int32 )

  print ( '' )
  print ( 'simplex_unit_sample_test02' )
  print ( '  simplex_unit_sample computes a Monte Carlo estimate of an' )
  print ( '  integral over the interior of the unit simplex in 6D.' )
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

  while ( n <= 65536 ):

    x = simplex_unit_sample ( m, n, rng )

    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 7 ):

      e[0:m] = e_test[0:m,j]

      value = monomial_value ( m, n, e, x )

      result = simplex_unit_volume ( m ) * np.sum ( value[0:n] ) / n
      print ( '  %14.6g' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  print ( '' )
  print ( '     Exact' )
  for j in range ( 0, 7 ):

    e[0:m] = e_test[0:m,j]

    result = simplex_unit_monomial_integral ( m, e )
    print ( '  %14.6g' % ( result ), end = '' )

  print ( '' )

  return

def simplex_unit_to_general ( m, n, t, ref ):

#*****************************************************************************80
#
## simplex_unit_to_general() maps the unit simplex to a general simplex.
#
#  Discussion:
#
#    Given that the unit simplex has been mapped to a general simplex
#    with vertices T, compute the images in T, under the same linear
#    mapping, of points whose coordinates in the unit simplex are REF.
#
#    The vertices of the unit simplex are listed as suggested in the
#    following:
#
#      (0,0,0,...,0)
#      (1,0,0,...,0)
#      (0,1,0,...,0)
#      (0,0,1,...,0)
#      (...........)
#      (0,0,0,...,1)
#
#    Thanks to Andrei ("spiritualworlds") for pointing out a mistake in the
#    previous implementation of this routine, 02 March 2008.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 March 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of points to transform.
#
#    real T(M,M+1), the vertices of the
#    general simplex.  
#
#    real REF(M,N), points in the 
#    reference triangle.
#
#  Output:
#
#    real PHY(M,N), corresponding points 
#    in the physical triangle.
#
  import numpy as np
#
#  The image of each point is initially the image of the origin.
#
#  Insofar as the pre-image differs from the origin in a given vertex
#  direction, add that proportion of the difference between the images
#  of the origin and the vertex.
#
  phy = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):

    for j in range ( 0, n ):

      phy[i,j] = t[i,0]

      for vertex in range ( 1, m + 1 ):

        phy[i,j] = phy[i,j] + ( t[i,vertex] - t[i,0] ) * ref[vertex-1,j]

  return phy

def simplex_unit_to_general_test01 ( rng ):

#*****************************************************************************80
#
## simplex_unit_to_general_test01() tests simplex_unit_to_general().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2017
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
  n = 10

  t = np.array ( [ \
    [ 1.0, 3.0, 2.0 ], \
    [ 1.0, 1.0, 5.0 ] ] )

  t_unit = np.array ( [ \
    [ 0.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0 ] ] )

  print ( '' )
  print ( 'simplex_unit_to_general_test01' )
  print ( '  simplex_unit_to_general' )
  print ( '  maps points in the unit simplex to a general simplex.' )
  print ( '' )
  print ( '  Here we consider a simplex in 2D, a triangle.' )
  print ( ''  )
  print ( '  The vertices of the general triangle are:' )
  print ( '' )
  for j in range ( 0, m + 1 ):
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( t[i,j] ), end = "" )
    print ( '' )

  print ( '' )
  print ( '   (  XSI     ETA )   ( X       Y  )' )
  print ( '' )

  phy_unit = simplex_unit_to_general ( m, m+1, t, t_unit )

  for j in range ( 0, m + 1 ):
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( t_unit[i,j] ), end = "" )
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( phy_unit[i,j] ), end = "" )
    print ( '' )

  ref = simplex_unit_sample ( m, n, rng )

  phy = simplex_unit_to_general ( m, n, t, ref )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( ref[i,j] ), end = "" )
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( phy[i,j] ), end = "" )
    print ( '' )

  return

def simplex_unit_to_general_test02 ( rng ):

#*****************************************************************************80
#
## simplex_unit_to_general_test02() tests simplex_unit_to_general().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2008
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
  n = 10

  t = np.array ( [ \
    [ 1.0, 3.0, 1.0, 1.0 ], \
    [ 1.0, 1.0, 4.0, 1.0 ], \
    [ 1.0, 1.0, 1.0, 5.0 ] ] )

  t_unit = np.array ( [ \
    [ 0.0, 1.0, 0.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 0.0, 1.0 ] ] )

  print ( '' )
  print ( 'simplex_unit_to_general_test02' )
  print ( '  simplex_unit_to_general' )
  print ( '  maps points in the unit simplex to a general simplex.' )
  print ( '' )
  print ( '  Here we consider a simplex in 3D, a tetrahedron.' )
  print ( '' )
  print ( '  The vertices of the general tetrahedron are:' )
  print ( '' )
  for j in range ( 0, m + 1 ):
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( t[i,j] ), end = "" )
    print ( '' )

  print ( '' )
  print ( '   (  XSI     ETA )   ( X       Y  )' )
  print ( '' )

  phy_unit = simplex_unit_to_general ( m, m+1, t, t_unit )

  for j in range ( 0, m + 1 ):
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( t_unit[i,j] ), end = "" )
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( phy_unit[i,j] ), end = "" )
    print ( '' )

  ref = simplex_unit_sample ( m, n, rng )

  phy = simplex_unit_to_general ( m, n, t, ref )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( ref[i,j] ), end = "" )
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( phy[i,j] ), end = "" )
    print ( '' )

  return

def simplex_unit_volume ( m ):

#*****************************************************************************80
#
## simplex_unit_volume() returns the volume of the unit simplex in M dimensions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2014
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
  for i in range ( 1, m + 1 ):
    value = value / float ( i )

  return value

def simplex_unit_volume_test ( ) :

#*****************************************************************************80
#
## simplex_unit_volume_test() tests simplex_unit_volume().
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
  print ( 'simplex_unit_volume_test' )
  print ( '  simplex_unit_volume returns the volume of the unit simplex' )
  print ( '  in M dimensions.' )
  print ( '' )
  print ( '   M   Volume' )
  print ( '' )

  for m in range ( 1, 10 ):
    value = simplex_unit_volume ( m )
    print ( '  %2d  %g' % ( m, value ) )

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

def simplex_monte_carlo_test ( ):

#*****************************************************************************80
#
## simplex_monte_carlo_test() tests simplex_monte_carlo().
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
  print ( 'simplex_monte_carlo_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test simplex_monte_carlo().' )

  rng = default_rng ( )

  simplex_general_sample_test ( rng )
  simplex_unit_monomial_integral_test ( rng )
  simplex_unit_sample_test00 ( rng )
  simplex_unit_sample_test01 ( rng )
  simplex_unit_sample_test02 ( rng )
  simplex_unit_to_general_test01 ( rng )
  simplex_unit_to_general_test02 ( rng )
  simplex_unit_volume_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'simplex_monte_carlo_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  simplex_monte_carlo_test ( )
  timestamp ( )

