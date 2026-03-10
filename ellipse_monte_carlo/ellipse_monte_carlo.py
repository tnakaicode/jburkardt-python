#! /usr/bin/env python3
#
def ellipse_area1 ( a, r ):

#*****************************************************************************80
#
## ellipse_area1() returns the area of an ellipse defined by a matrix.
#
#  Discussion:
#
#    The points X in the ellipse are described by a 2 by 2
#    positive definite symmetric matrix A, and a "radius" R, such that
#      X' * A * X <= R * R
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(2,2), the matrix that describes
#    the ellipsoid.  A must be symmetric and positive definite.
#
#    real R, the "radius" of the ellipse.
#
#  Output:
#
#    real VALUE, the area of the ellipse.
#
  import numpy as np

  value = r * r * np.pi / np.sqrt ( a[0,0] * a[1,1] - a[1,0] * a[0,1] )

  return value

def ellipse_area1_test ( ):

#*****************************************************************************80
#
## ellipse_area1_test() tests ellipse_area1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ellipse_area1_test():' )
  print ( '  ellipse_area1() computes the area of an ellipse.' )

  r = 10.0
  a = np.array ( [ [ 5.0, 1.0 ], [ 1.0, 2.0 ] ] )
  area = ellipse_area1 ( a, r )
  print ( '' )
  print ( '  R = %g' % ( r ) )
  r8mat_print ( 2, 2, a, '  Matrix A in ellipse definition x*A*x=r^2' )
  print ( '  Area = %g' % ( area ) )

  return

def ellipse_area2 ( a, b, c, d ):

#*****************************************************************************80
#
## ellipse_area2() returns the area of an ellipse defined by an equation.
#
#  Discussion:
#
#    The ellipse is described by the formula
#      a x^2 + b xy + c y^2 = d
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, coefficients on the left hand side.
#
#    real D, the right hand side.
#
#  Output:
#
#    real VALUE, the area of the ellipse.
#
  import numpy as np

  value = 2.0 * d * d * np.pi / np.sqrt ( 4.0 * a * c - b * b )

  return value

def ellipse_area2_test ( ):

#*****************************************************************************80
#
## ellipse_area2_test() tests ellipse_area2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'ellipse_area2_test():' )
  print ( '  ellipse_area2() computes the area of an ellipse.' )

  a = 5.0
  b = 2.0
  c = 2.0
  d = 10.0

  area = ellipse_area2 ( a, b, c, d )
  print ( '' )
  print ( '  Ellipse: %g * x^2 + %g * xy + %g * y^2 = %g' % ( a, b, c, d ) )
  print ( '  Area = %g' % ( area ) )

  return

def ellipse_monte_carlo_test ( ):

#*****************************************************************************80
#
## ellipse_monte_carlo_test() tests ellipse_monte_carlo library().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ellipse_monte_carlo_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ellipse_monte_carlo().' )

  ellipse_area1_test ( )
  ellipse_area2_test ( )
  ellipse_sample_test ( )
  ellipse_sample2_test ( )
  r8po_fa_test ( )
  r8po_sl_test ( )
  uniform_in_sphere01_map_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ellipse_monte_carlo_test():' ) 
  print ( '  Normal end of execution.' )
  return

def ellipse_sample ( n, a, r, rng ):

#*****************************************************************************80
#
## ellipse_sample() samples points in an ellipse.
#
#  Discussion:
#
#    The points X in the ellipse are described by a 2 by 2
#    positive definite symmetric matrix A, and a "radius" R, such that
#      X' * A * X <= R * R
#
#    If the ellipse is described by the formula
#      a x^2 + b xy + c y^2 = d
#    then
#      A = (  a  b/2 )
#          ( b/2  c  )
#      R = sqrt ( d )
#
#    The algorithm computes the Cholesky factorization of A:
#      A = U' * U.
#    A set of uniformly random points Y is generated, satisfying:
#      Y' * Y <= R * R.
#    The appropriate points in the ellipsoid are found by solving
#      U * X = Y
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
#    Wiley, 1986.
#
#  Input:
#
#    integer N, the number of points.
#
#    real A(2,2), the matrix that describes the ellipse.
#
#    real R, the right hand side of the ellipse equation.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(2,N), the points.
#
  import numpy as np
#
#  Get the factor U such that U' * U = A.
#
  u_fa = r8po_fa ( 2, a )
#
#  Get the points Y that satisfy Y' * Y = R * R.
#
  x = uniform_in_sphere01_map ( 2, n, rng )

  x = r * x
#
#  Solve U * X = Y.
#
  s = np.zeros ( 2 )
  t = np.zeros ( 2 )
  
  for j in range ( 0, n ):
    t[0:2] = x[0:2,j]
    s[0:2] = r8po_sl ( 2, u_fa, t )
    x[0:2,j] = s[0:2]

  return x

def ellipse_sample_test ( ):

#*****************************************************************************80
#
## ellipse_sample_test() tests ellipse_sample().
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

  print ( '' )
  print ( 'ellipse_sample_test():' )
  print ( '  ellipse_sample() computes points uniformly distributed' )
  print ( '  inside an ellipse x\'*A*x=r^2.' )

  rng = default_rng ( )
  n = 10
  a = np.array ( [ [ 5.0, 1.0 ], [ 1.0, 2.0 ] ] )
  r = 10.0

  x = ellipse_sample ( n, a, r, rng )

  r8mat_transpose_print ( 2, n, x, '  Random points inside ellipse' )

  return

def ellipse_sample2_test ( ):

#*****************************************************************************80
#
## ellipse_sample2_test() tests ellipse_sample() to estimate an integral.
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

  print ( '' )
  print ( 'ellipse_sample2_test():' )
  print ( '  ellipse_sample() estimates integrals' )
  print ( '  in the ellipse x'' * A * x <= r^2.' )
  print ( '' )
  print ( '         N        1              X               Y               X^2               XY             Y^2             X^3' )
  print ( '' )

  n = 1
  e = np.zeros ( 2 )

  while ( n <= 65536 ):

    x = ellipse_sample ( n, a, r, rng )

    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 7 ):

      e[0:2] = e_test[j,0:2]

      value = monomial_value ( 2, n, e, x )

      result = ellipse_area1 ( a, r ) * np.sum ( value[0:n] ) / float ( n )
      print ( '  %14.6g' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

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
  print ( 'i4vec_print_test():' )
  print ( '  i4vec_print() prints an I4VEC.' )

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
      print ( '%8d' % ( a[i] ), end = '' )
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
  print ( 'i4vec_transpose_print_test():' )
  print ( '  i4vec_transpose_print() prints an I4VEC' )
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
#    r8po_fa, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
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
## r8po_fa_test() tests r8po_fa().
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
## r8po_sl() solves a R8PO system factored by r8po_fa.
#
#  Discussion:
#
#    The R8PO storage format is appropriate for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of a R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    r8po_fa, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
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
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  uniform_in_sphere01_map() computes points uniformly distributed' )
  print ( '  inside the M-dimensional unit sphere.' )

  m = 3
  n = 10
  rng = default_rng ( )

  x = uniform_in_sphere01_map ( m, n, rng )

  r8mat_transpose_print ( m, n, x, '  Random points inside unit 3-sphere' )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  ellipse_monte_carlo_test ( )
  timestamp ( )

