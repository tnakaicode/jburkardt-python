#! /usr/bin/env python3
#
def polygon_monte_carlo_tests ( ):

#*****************************************************************************80
#
## polygon_monte_carlo_tests() tests polygon_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'polygon_monte_carlo_tests():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polygon_monte_carlo().' )

  polygon_area_test ( )
  polygon_monomial_integral_test ( )
  polygon_monte_carlo_test ( )
  polygon_sample_test ( )
  triangle_area_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_monte_carlo_tests():' )
  print ( '  Normal end of execution.' )
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
      print ( '%8d' % ( a[i] ) ),
      if ( ( i + 1 ) % 10 == 0 or i == n - 1 ):
        print ( '' )
  else:
    print ( '  (empty vector)' )

  return

def monomial_value ( n, m, e, x ):

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
#    real X(N,M), the point coordinates.
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
        v[j] = v[j] * x[j,i] ** e[i]

  return v

def polygon_area ( n, v ):

#*****************************************************************************80
#
## polygon_area() computes the area of a polygon.
#
#  Discussion:
#
#    AREA = 1/2 * abs ( sum ( 1 <= I <= N ) X(I) * ( Y(I+1) - Y(I-1) ) )
#    where Y(0) should be replaced by Y(N), and Y(N+1) by Y(1).
#
#    If the vertices are given in counterclockwise order, the area
#    will be positive.  If the vertices are given in clockwise order,
#    the area will be negative.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#
#    real V(N,2), the vertices.
#
#  Output:
#
#    real AREA, the area of the polygon.
#
  area = 0.0

  for i in range ( 0, n ):

    if ( i == 0 ):
      im1 = n - 1
    else:
      im1 = i - 1

    if ( i == n - 1 ):
      ip1 = 0
    else:
      ip1 = i + 1

    area = area + v[i,0] * ( v[ip1,1] - v[im1,1] )

  area = 0.5 * area

  return area

def polygon_area_test ( ):

#*****************************************************************************80
#
## polygon_area_test() tests polygon_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 2
  area_exact_test = np.array ( [ 2.0, 6.0 ] )
  n_test = np.array ( [ 4, 8 ] )

  print ( '' )
  print ( 'polygon_area_test():' )
  print ( '  polygon_area() computes the area of a polygon.' )

  for test in range ( 0, test_num ):

    n = n_test[test]
    area_exact = area_exact_test[test]

    if ( test == 0 ):

      v = np.array ( [ \
        [ 1.0, 0.0 ], \
        [ 2.0, 1.0 ], \
        [ 1.0, 2.0 ], \
        [ 0.0, 1.0 ] ] )

    elif ( test == 1 ):

      v = np.array ( [ \
        [ 0.0, 0.0 ], \
        [ 3.0, 0.0 ], \
        [ 3.0, 3.0 ], \
        [ 2.0, 3.0 ], \
        [ 2.0, 1.0 ], \
        [ 1.0, 1.0 ], \
        [ 1.0, 2.0 ], \
        [ 0.0, 2.0 ] ] )

    print ( '' )
    print ( '  Number of polygonal vertices = %d' % ( n ) )

    r8mat_print ( n, 2, v, '  The polygon vertices:' )

    area = polygon_area ( n, v )

    print ( '' )
    print ( '  Exact area is        %g' % ( area_exact ) )
    print ( '  The computed area is %g' % ( area ) )

  return

def polygon_monomial_integral ( nv, v, e ):

#*****************************************************************************80
#
## polygon_monomial_integral() integrates a monomial over a polygon.
#
#  Discussion:
#
#    Nu(P,Q) = Integral ( x, y in polygon ) x^p y^q dx dy
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carsten Steger,
#    On the calculation of arbitrary moments of polygons,
#    Technical Report FGBV-96-05,
#    Forschungsgruppe Bildverstehen, Informatik IX,
#    Technische Universitaet Muenchen, October 1996.
#
#  Input:
#
#    integer NV, the number of vertices of the polygon.
#
#    real V(NV,2), the vertex coordinates.
#
#    integer E(2), the exponents of the monomial.
#
#  Output:
#
#    real NU_PQ, the unnormalized moment Nu(P,Q).
#
  from scipy.special import comb

  p = e[0]
  q = e[1]

  nu_pq = 0.0

  xj = v[nv-1,0]
  yj = v[nv-1,1]

  for i in range ( 0, nv ):

    xi = v[i,0]
    yi = v[i,1]

    s_pq = 0.0

    for k in range( 0, p + 1 ):
      for l in range ( 0, q + 1 ):
        s_pq = s_pq \
          + comb ( k + l, l ) * comb ( p + q - k - l, q - l ) \
          * xi ** k * xj ** ( p - k ) \
          * yi ** l * yj ** ( q - l )

    nu_pq = nu_pq + ( xj * yi - xi * yj ) * s_pq

    xj = xi
    yj = yi

  nu_pq = nu_pq / float ( p + q + 2 ) / float ( p + q + 1 ) \
    / comb ( p + q, p )

  return nu_pq

def polygon_monomial_integral_test ( ):

#*****************************************************************************80
#
## polygon_monomial_integral_test() tests polygon_monomial_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nv = 3

  v = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 1.0, 0.0 ], \
    [ 0.0, 1.0 ] ] ) 

  print ( '' )
  print ( 'polygon_monomial_integral_test():' )
  print ( '  polygon_monomial_integral() evaluates the integral of a monomial' )
  print ( '  x^p y^q over the interior of a polygon in 2D.' )

  r8mat_print ( nv, 2, v, '  Polygon vertices:' )

  print ( '' )
  print ( '   P   Q       Integral' )
  print ( '' )

  e = np.zeros ( 2, dtype = np.int32 )

  for pq in range ( 0, 5 ):
    for p in range ( 0, pq + 1 ):
      q = pq - p
      e[0] = p
      e[1] = q

      result = polygon_monomial_integral ( nv, v, e )
      print ( '  %2d  %2d  %14.6g' % ( p, q, result ) )

  return

def polygon_monte_carlo_test ( ):

#*****************************************************************************80
#
## polygon_monte_carlo_test() estimates integrals over a polygon in 2D.
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
  import numpy as np

  nv = 4

  v = np.array ( [ \
    [ -1.0, -1.0 ], \
    [  1.0, -1.0 ], \
    [  1.0,  1.0 ], \
    [ -1.0,  1.0 ] ] )

  e_test = np.array ( [ \
    [ 0, 0 ], \
    [ 2, 0 ], \
    [ 0, 2 ], \
    [ 4, 0 ], \
    [ 2, 2 ], \
    [ 0, 4 ], \
    [ 6, 0 ] ] )

  print ( '' )
  print ( 'polygon_monte_carlo_test():' )
  print ( '  polygon_sample() estimates integrals' )
  print ( '  over the interior of a polygon in 2D.' )
  print ( '' )
  print ( '         N' ),
  print ( '        1' ),
  print ( '              X^2 ' ),
  print ( '             Y^2' ),
  print ( '             X^4' ),
  print ( '           X^2Y^2' ),
  print ( '             Y^4' ),
  print ( '           X^6' )
  print ( '' )

  n = 1

  e = np.zeros ( 2, dtype = np.int32 )

  while ( n <= 65536 ):

    x = polygon_sample ( nv, v, n )

    print ( '  %8d' % ( n ) ),

    for j in range ( 0, 7 ):

      e[0:2] = e_test[j,0:2]

      value = monomial_value ( n, 2, e, x )

      result = polygon_area ( nv, v ) * np.sum ( value[0:n] ) / float ( n )

      print ( '  %14.6g' % ( result ) ),

    print ( '' )

    n = 2 * n

  print ( '     Exact' ),

  for j in range ( 0, 7 ):

    e[0:2] = e_test[j,0:2]

    result = polygon_monomial_integral ( nv, v, e )
    print ( '  %14.6g' % ( result ) ),

  print ( '' )

  return

def polygon_sample ( nv, v, n ):

#*****************************************************************************80
#
## polygon_sample() uniformly samples a polygon.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NV, the number of vertices.
#
#    real V(NV,2), the vertices of the polygon, listed in
#    counterclockwise order.
#
#    integer N, the number of points to create.
#
#  Output:
#
#    real S(2,N), the points.
#
  from numpy.random import default_rng
  from polygon_triangulate import polygon_triangulate
  import numpy as np

  rng = default_rng ( )
#
#  Triangulate the polygon.
#
  x = np.zeros ( nv )
  y = np.zeros ( nv )
  for j in range ( 0, nv ):
    x[j] = v[j,0]
    y[j] = v[j,1]

  triangles = polygon_triangulate ( nv, x, y )
#
#  Determine the areas of each triangle.
#
  area_triangle = np.zeros ( nv - 2 )

  area_polygon = 0.0
  for i in range ( 0, nv - 2 ):
    area_triangle[i] = triangle_area ( \
      v[triangles[i,0],0], v[triangles[i,0],1], \
      v[triangles[i,1],0], v[triangles[i,1],1], \
      v[triangles[i,2],0], v[triangles[i,2],1] )
    area_polygon = area_polygon + area_triangle[i]
#
#  Normalize the areas.
#
  area_relative = np.zeros ( nv - 1 )

  for i in range ( 0, nv - 2 ):
    area_relative[i] = area_triangle[i] / area_polygon
#
#  Replace each area by the sum of itself and all previous ones.
#
  area_cumulative = np.zeros ( nv - 2 )

  area_cumulative[0] = area_relative[0]
  for i in range ( 1, nv - 2 ):
    area_cumulative[i] = area_relative[i] + area_cumulative[i-1]

  s = np.zeros ( [ n, 2 ] )

  for j in range ( 0, n ):
#
#  Choose triangle I at random, based on areas.
#
    area_percent = rng.random ( )

    for k in range ( 0, nv - 2 ):

      i = k

      if ( area_percent <= area_cumulative[k] ):
        break
#
#  Now choose a point at random in triangle I.
#
    r = rng.random ( size = 2 )

    if ( 1.0 < r[0] + r[1] ):
      r[0] = 1.0 - r[0]
      r[1] = 1.0 - r[1]

    s[j,0] = ( 1.0 - r[0] - r[1] ) * v[triangles[i,0],0] \
                   + r[0]          * v[triangles[i,1],0] \
                          + r[1]   * v[triangles[i,2],0]

    s[j,1] = ( 1.0 - r[0] - r[1] ) * v[triangles[i,0],1] \
                   + r[0]          * v[triangles[i,1],1] \
                          + r[1]   * v[triangles[i,2],1]

  return s

def polygon_sample_test ( ):

#*****************************************************************************80
#
## polygon_sample_test() tests polygon_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 20
  nv = 6
  v = np.array ( [ \
    [ 0.0, 0.0 ], \
    [ 2.0, 0.0 ], \
    [ 2.0, 1.0 ], \
    [ 1.0, 1.0 ], \
    [ 1.0, 2.0 ], \
    [ 0.0, 1.0 ] ] )

  print ( '' )
  print ( 'polygon_sample_test():' )
  print ( '  polygon_sample() samples a polygon.' )

  x = polygon_sample ( nv, v, n )

  r8mat_print ( n, 2, x, '  Sample points:' )

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

  print ( '' )
  print ( 'r8mat_transpose_print_test()' )
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

def triangle_area ( xa, ya, xb, yb, xc, yc ):

#*****************************************************************************80
#
## triangle_area() computes the signed area of a triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real XA, YA, XB, YB, XC, YC, the vertices.
#
#  Output:
#
#    real AREA, the signed area of the triangle.
#
  area = 0.5 * ( ( xb - xa ) * ( yc - ya ) \
               - ( xc - xa ) * ( yb - ya ) )

  return area

def triangle_area_test ( ):

#*****************************************************************************80
#
## triangle_area_test() tests triangle_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  xa = 0.0
  ya = 1.0
  xb = 0.0
  yb = 0.0
  xc = 1.0
  yc = 0.0

  print ( '' )
  print ( 'triangle_area_test():' )
  print ( '  triangle_area() computes the area of a triangle.' )

  print ( '' )
  print ( '  (XA,YA) = (%g,%g)' % ( xa, ya ) )
  print ( '  (XB,YB) = (%g,%g)' % ( xb, yb ) )
  print ( '  (XC,YC) = (%g,%g)' % ( xc, yc ) )

  area = triangle_area ( xa, ya, xb, yb, xc, yc )

  print ( '' )
  print ( '  Triangle area is %g' % ( area ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  polygon_monte_carlo_tests ( )
  timestamp ( )

