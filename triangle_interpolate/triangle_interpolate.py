#! /usr/bin/env python3
#
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

def r8mat_transpose_write ( filename, m, n, a ):

#*****************************************************************************80
#
## r8mat_transpose_write() writes the transpose of an R8MAT to a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the output file.
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      s = '  %g' % ( a[i,j] )
      output.write ( s )
    output.write ( '\n' )

  output.close ( )

  return

def r8mat_transpose_write_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_write_test() tests r8mat_transpose_write().
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
  print ( 'r8mat_transpose_write_test:' )
  print ( '  Test r8mat_transpose_write, which writes the transpose of an R8MAT to a file.' )

  filename = 'r8mat_transpose_write_test.txt'
  m = 5
  n = 3
  a = np.array ( (  \
    ( 1.1, 1.2, 1.3 ), \
    ( 2.1, 2.2, 2.3 ), \
    ( 3.1, 3.2, 3.3 ), \
    ( 4.1, 4.2, 4.3 ), \
    ( 5.1, 5.2, 5.3 ) ) )
  r8mat_transpose_write ( filename, m, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )

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

def triangle_area ( t ):

#*****************************************************************************80
#
## triangle_area() computes the area of a triangle in 2D.
#
#  Discussion:
#
#    If the triangle's vertices are given in counterclockwise order,
#    the area will be positive.  If the triangle's vertices are given
#    in clockwise order, the area will be negative!
#
#    An earlier version of this routine always returned the absolute
#    value of the computed area.  I am convinced now that that is
#    a less useful result!  For instance, by returning the signed 
#    area of a triangle, it is possible to easily compute the area 
#    of a nonconvex polygon as the sum of the (possibly negative) 
#    areas of triangles formed by node 1 and successive pairs of vertices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(2,3), the triangle vertices.
#
#  Output:
#
#    real AREA, the area of the triangle.
#
  area = 0.5 * ( \
      t[0,0] * ( t[1,1] - t[1,2] ) \
    + t[0,1] * ( t[1,2] - t[1,0] ) \
    + t[0,2] * ( t[1,0] - t[1,1] ) )

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
#    23 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  print ( '' )
  print ( 'triangle_area_test' )
  print ( '  triangle_area computes the area of a triangle.' )

  r8mat_print ( 2, 3, t, '  Triangle vertices (columns)' )

  area = triangle_area ( t )

  print ( '' )
  print ( '  Triangle area is %g' % ( area ) )

  return

def triangle_interpolate_linear ( m, n, p1, p2, p3, p, v1, v2, v3 ):

#*****************************************************************************80
#
## triangle_interpolate_linear() interpolates data given on a triangle's vertices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the dimension of the quantity.
#
#    integer N, the number of points.
#
#    real P1(2), P2(2), P3(2), the vertices of the triangle,
#    in counterclockwise order.
#
#    real P(2,N), the point at which the interpolant is desired.
#
#    real V1(M), V2(M), V3(M), the value of some quantity at the vertices.
#
#  Output:
#
#    real V(M,N), the interpolated value of the quantity at P.
#
  import numpy as np

  v = np.zeros ( [ m, n ] )

  abc = triangle_area ( np.array ( [ [ p1[0], p2[0], p3[0] ], [ p1[1], p2[1], p3[1] ] ] ) )

  for j in range ( 0, n ):
    pj = np.array ( [ p[0,j], p[1,j] ] )
    pbc = triangle_area ( np.array ( [ [ pj[0], p2[0], p3[0] ], [ pj[1], p2[1], p3[1] ] ] ) )
    apc = triangle_area ( np.array ( [ [ p1[0], pj[0], p3[0] ], [ p1[1], pj[1], p3[1] ] ] ) )
    abp = triangle_area ( np.array ( [ [ p1[0], p2[0], pj[0] ], [ p1[1], p2[1], pj[1] ] ] ) )
    for i in range ( 0, m ):
      v[i,j] =        \
        ( pbc * v1[i]   \
        + apc * v2[i]   \
        + abp * v3[i] ) \
        / abc

  return v

def triangle_interpolate_linear_test ( ):

#*****************************************************************************80
#
## triangle_interpolate_linear_test() tests triangle_interpolate_linear().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'triangle_interpolate_linear_test' )
  print ( '  triangle_interpolate_linear uses linear interpolation' )
  print ( '  on vertex data to estimate values in the interior.' )
#
#  Define the triangle corners.
#
  p1 = np.array ( [ 0.0, 1.0 ] )
  p2 = np.array ( [ 5.0, 0.0 ] )
  p3 = np.array ( [ 4.0, 4.0 ] )
#
#  Get N sample points inside the triangle.
#
  n = 10
  p = uniform_in_triangle_map1 ( p1, p2, p3, n )
#
#  Set the corner colors to R, G and B.
#
  v1 = np.array ( [ 1.0, 0.0, 0.0 ] )
  v2 = np.array ( [ 0.0, 1.0, 0.0 ] )
  v3 = np.array ( [ 0.0, 0.0, 1.0 ] )
#
#  Request an intepolated value for R, G and B at each point.
#
  m = 3
  v = triangle_interpolate_linear ( m, n, p1, p2, p3, p, v1, v2, v3 )
#
#  Report the data.
#
  print ( '' )
  print ( '       X               Y               V(1)            V(2)            V(3)' )
  print ( '' )
  print ( '  %14.6g  %14.6g  %14.6g  %14.6g  %14.6g' \
    % ( p1[0], p1[1], v1[0], v1[1], v1[2] ) )
  print ( '  %14.6g  %14.6g  %14.6g  %14.6g  %14.6g' \
    % ( p2[0], p2[1], v2[0], v2[1], v2[2] ) )
  print ( '  %14.6g  %14.6g  %14.6g  %14.6g  %14.6g' \
    % ( p3[0], p3[1], v3[0], v3[1], v3[2] ) )
  print ( '' )
  for j in range ( 0, n ):
    print ( '  %14.6g  %14.6g' % ( p[0,j], p[1,j] ) ),
    for i in range ( 0, m ):
      print ( '  %14.6g' % ( v[i,j] ) ),
    print ( '' )

  return

def triangle_interpolate_test ( ):

#*****************************************************************************80
#
## triangle_interpolate_test() tests triangle_interpolate().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'triangle_interpolate_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test triangle_interpolate()' )

  r8mat_transpose_write_test ( )
  triangle_interpolate_linear_test ( )
  uniform_in_triangle_map1_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'triangle_interpolate_test():' )
  print ( '  Normal end of execution.' )
  return

def uniform_in_triangle_map1 ( v1, v2, v3, n ):

#*****************************************************************************80
#
## uniform_in_triangle_map1() maps uniform points into a triangle.
#
#  Discussion:
#
#    The triangle is defined by three vertices.  This routine
#    uses Turk's rule #1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Greg Turk,
#    Generating Random Points in a Triangle,
#    in Graphics Gems,
#    edited by Andrew Glassner,
#    AP Professional, 1990, pages 24-28.
#
#  Input:
#
#    real V1(2), V2(2), V3(2), the vertices.
#
#    integer N, the number of points.
#
#  Output:
#
#    real X(2,N), the points.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  x = np.zeros ( [ 2, n ] )
#
#  Generate the points using Turk's rule 1.
#
  for j in range ( 0, n ):

    r = rng.random ( size = 2 )

    a = 1.0 - np.sqrt ( r[1] )
    b = ( 1.0 - r[0] ) * np.sqrt ( r[1] )
    c = r[0] * np.sqrt ( r[1] )

    for i in range ( 0, 2 ):
      x[i,j] = ( a * v1[i] \
               + b * v2[i] \
               + c * v3[i] )

  return x

def uniform_in_triangle_map1_test ( ):

#*****************************************************************************80
#
## uniform_in_triangle_map1_test() tests uniform_in_triangle_map1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 1000
  v1 = np.array ( [ 0.75, 0.90 ] )
  v2 = np.array ( [ 0.00, 0.20 ] )
  v3 = np.array ( [ 0.95, 0.65 ] )

  print ( '' )
  print ( 'uniform_in_triangle_map1_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  uniform_in_triangle_map1() maps uniform' )
  print ( '  points into a triangle.' )
  print ( '' )
  print ( '  Number of points N =          %d' % ( n ) )

  print ( '' )
  print ( '  V1 = %12f  %12f' % ( v1[0], v1[1] ) )
  print ( '  V2 = %12f  %12f' % ( v2[0], v2[1] ) )
  print ( '  V3 = %12f  %12f' % ( v3[0], v3[1] ) )

  x = uniform_in_triangle_map1 ( v1, v2, v3, n )

  filename = 'uniform_in_triangle_map1.txt'
  r8mat_transpose_write ( filename, 2, n, x )

  print ( '' )
  print ( '  Data written to "%s".' % ( filename ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  triangle_interpolate_test ( )
  timestamp ( )

