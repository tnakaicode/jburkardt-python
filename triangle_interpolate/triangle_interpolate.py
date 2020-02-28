#! /usr/bin/env python3
#
def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_PRINT prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_TEST tests R8MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
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

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT_SOME prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT prints an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_TEST tests R8MAT_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8MAT_TRANSPOSE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_TRANSPOSE_PRINT prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_PRINT_SOME prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
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
## R8MAT_TRANSPOSE_PRINT_SOME_TEST tests R8MAT_TRANSPOSE_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8MAT_TRANSPOSE_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_TRANSPOSE_PRINT_SOME prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_TRANSPOSE_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_transpose_write ( filename, m, n, a ):

#*****************************************************************************80
#
## R8MAT_TRANSPOSE_WRITE writes the transpose of an R8MAT to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
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
## R8MAT_TRANSPOSE_WRITE_TEST tests R8MAT_TRANSPOSE_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8MAT_TRANSPOSE_WRITE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test R8MAT_TRANSPOSE_WRITE, which writes the transpose of an R8MAT to a file.' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_TRANSPOSE_WRITE_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_01 - Fatal error!' )

  x = np.zeros ( n );

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_01 computes a random R8VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_01 ( n, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def triangle_area ( t ):

#*****************************************************************************80
#
## TRIANGLE_AREA computes the area of a triangle in 2D.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T(2,3), the triangle vertices.
#
#    Output, real AREA, the area of the triangle.
#
  area = 0.5 * ( \
      t[0,0] * ( t[1,1] - t[1,2] ) \
    + t[0,1] * ( t[1,2] - t[1,0] ) \
    + t[0,2] * ( t[1,0] - t[1,1] ) )

  return area

def triangle_area_test ( ):

#*****************************************************************************80
#
## TRIANGLE_AREA_TEST tests TRIANGLE_AREA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'TRIANGLE_AREA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_AREA computes the area of a triangle.' )

  r8mat_print ( 2, 3, t, '  Triangle vertices (columns)' )

  area = triangle_area ( t )

  print ( '' )
  print ( '  Triangle area is %g' % ( area ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_AREA_TEST' )
  print ( '  Normal end of execution.' )
  return

def triangle_interpolate_linear ( m, n, p1, p2, p3, p, v1, v2, v3 ):

#*****************************************************************************80
#
## TRIANGLE_INTERPOLATE_LINEAR interpolates data given on a triangle's vertices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the dimension of the quantity.
#
#    Input, integer N, the number of points.
#
#    Input, real P1(2), P2(2), P3(2), the vertices of the triangle,
#    in counterclockwise order.
#
#    Input, real P(2,N), the point at which the interpolant is desired.
#
#    Input, real V1(M), V2(M), V3(M), the value of some quantity at the vertices.
#
#    Output, real V(M,N), the interpolated value of the quantity at P.
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
## TRIANGLE_INTERPOLATE_LINEAR_TEST tests TRIANGLE_INTERPOLATE_LINEAR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'TRIANGLE_INTERPOLATE_LINEAR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_INTERPOLATE_LINEAR uses linear interpolation' )
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
  seed = 123456789
  p, seed = uniform_in_triangle_map1 ( p1, p2, p3, n, seed )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_INTERPOLATE_LINEAR_TEST:' )
  print ( '  Normal end of execution.' )
  return

def triangle_interpolate_test ( ):

#*****************************************************************************80
#
## TRIANGLE_INTERPOLATE_TEST tests the TRIANGLE_INTERPOLATE library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 January 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRIANGLE_INTERPOLATE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the TRIANGLE_INTERPOLATE library.' )

  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_transpose_write_test ( )
  r8vec_print_test ( )
  r8vec_uniform_01_test ( )
  triangle_interpolate_linear_test ( )
  uniform_in_triangle_map1_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_INTERPOLATE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def uniform_in_triangle_map1 ( v1, v2, v3, n, seed ):

#*****************************************************************************80
#
## UNIFORM_IN_TRIANGLE_MAP1 maps uniform points into a triangle.
#
#  Discussion:
#
#    The triangle is defined by three vertices.  This routine
#    uses Turk's rule #1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
#  Parameters:
#
#    Input, real V1(2), V2(2), V3(2), the vertices.
#
#    Input, integer N, the number of points.
#
#    Input/output, integer SEED, a seed for the random number generator.
#
#    Output, real X(2,N), the points.
#
  import numpy as np
  import platform

  x = np.zeros ( [ 2, n ] )
#
#  Generate the points using Turk's rule 1.
#
  for j in range ( 0, n ):

    r, seed = r8vec_uniform_01 ( 2, seed )

    a = 1.0 - np.sqrt ( r[1] )
    b = ( 1.0 - r[0] ) * np.sqrt ( r[1] )
    c = r[0] * np.sqrt ( r[1] )

    for i in range ( 0, 2 ):
      x[i,j] = ( a * v1[i] \
               + b * v2[i] \
               + c * v3[i] )

  return x, seed

def uniform_in_triangle_map1_test ( ):

#*****************************************************************************80
#
#% UNIFORM_IN_TRIANGLE_MAP1_TEST tests UNIFORM_IN_TRIANGLE_MAP1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  seed = 123456789
  v1 = np.array ( [ 0.75, 0.90 ] )
  v2 = np.array ( [ 0.00, 0.20 ] )
  v3 = np.array ( [ 0.95, 0.65 ] )

  print ( '' )
  print ( 'UNIFORM_IN_TRIANGLE_MAP1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNIFORM_IN_TRIANGLE_MAP1 maps uniform' )
  print ( '  points into a triangle.' )
  print ( '' )
  print ( '  Number of points N =          %d' % ( n ) )
  print ( '  Initial random number SEED =  %d' % ( seed ) )

  print ( '' )
  print ( '  V1 = %12f  %12f' % ( v1[0], v1[1] ) )
  print ( '  V2 = %12f  %12f' % ( v2[0], v2[1] ) )
  print ( '  V3 = %12f  %12f' % ( v3[0], v3[1] ) )

  x, seed = uniform_in_triangle_map1 ( v1, v2, v3, n, seed )

  print ( '  Final random number SEED =    %d' % ( seed ) )

  filename = 'uniform_in_triangle_map1.txt'
  r8mat_transpose_write ( filename, 2, n, x )

  print ( '' )
  print ( '  Data written to "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNIFORM_IN_TRIANGLE_MAP1_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  triangle_interpolate_test ( )
  timestamp ( )

