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

def reference_to_physical_t3 ( t, n, ref ):

#*****************************************************************************80
#
## reference_to_physical_t3() maps a reference point to a physical point.
#
#  Discussion:
#
#    Given the vertices of an order 3 physical triangle and a point
#    (XSI,ETA) in the reference triangle, the routine computes the value
#    of the corresponding image point (X,Y) in physical space.
#
#    Note that this routine may also be appropriate for an order 6
#    triangle, if the mapping between reference and physical space
#    is linear.  This implies, in particular, that the sides of the
#    image triangle are straight and that the "midside" nodes in the
#    physical triangle are halfway along the sides of
#    the physical triangle.
#
#  Reference Element T3:
#
#    |
#    1  3
#    |  |\
#    |  | \
#    S  |  \
#    |  |   \
#    |  |    \
#    0  1-----2
#    |
#    +--0--R--1-->
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(2,3), the coordinates of the vertices.  The vertices are assumed 
#    to be the images of (0,0), (1,0) and (0,1) respectively.
#
#    integer N, the number of points to transform.
#
#    real REF(2,N), the coordinates of points in the reference space.
#
#  Output:
#
#    real PHY(2,N), the coordinates of the corresponding points in the 
#    physical space.
#
  import numpy as np

  phy = np.zeros ( [ 2, n ] )

  for i in range ( 0, 2 ):

    phy[i,:] = t[i,0] * ( 1.0 - ref[0,:] - ref[1,:] ) \
             + t[i,1] *         ref[0,:]              \
             + t[i,2] *                    ref[1,:]

  return phy

def reference_to_physical_t3_test ( ):

#*****************************************************************************80
#
## reference_to_physical_t3_test() tests reference_to_physical_t3().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'reference_to_physical_t3_test:' )
  print ( '  reference_to_physical_t3 maps points in a reference triangle' )
  print ( '  to points in a physical triangle.' )
 
  t = np.array ( [ \
    [ 2.0, 3.0, 0.0 ], \
    [ 0.0, 4.0, 3.0 ] ] )

  n = 3

  ref = np.array ( [ \
    [ 0.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0 ] ] )

  r8mat_transpose_print ( 2, 3, t, '  XY triangle vertices:' )

  phy = reference_to_physical_t3 ( t, n, ref )

  print ( '' )
  print ( '  Apply map to RS triangle vertices.' )
  print ( '  Recover XY vertices (2,0), (3,4) and (0,3).' )
  print ( '' )

  for j in range ( 0, 3 ):
    print ( '  V(%d) = ( %g, %g )' % ( j, phy[0,j], phy[1,j] ) )

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

def triangle01_sample ( n ):

#*****************************************************************************80
#
## triangle01_sample() samples the interior of the unit triangle in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2016
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
#    integer N, the number of points.
#
#  Output:
#
#    real XY(2,N), the points.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  m = 2

  xy = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):

    e = rng.random ( size = m + 1 )

    e = - np.log ( e )

    d = np.sum ( e )

    xy[0:2,j] = e[0:2] / d

  return xy

def triangle01_sample_test ( ):

#*****************************************************************************80
#
## triangle01_sample_test() tests triangle01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 October 2015
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
  print ( 'triangle01_sample_test' )
  print ( '  triangle01_sample samples the unit triangle.' )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  n = 10
  xy = triangle01_sample ( n )
  r8mat_transpose_print ( 2, n, xy, '  Sample points:' )

  return

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

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices (columns)' )

  area = triangle_area ( t )

  print ( '' )
  print ( '  Triangle area is %g' % ( area ) )

  return

def triangle_monte_carlo ( t, n, triangle_integrand ):

#*****************************************************************************80
#
## triangle_monte_carlo() applies the Monte Carlo rule to integrate a function.
#
#  Discussion:
#
#    The function f(x,y) is to be integrated over a triangle T.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2010
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(2,3), the triangle vertices.
#
#    integer N, the number of sample points.
#
#    external triangle_integrand, the integrand routine.
#
#  Output:
#
#    real RESULT, the approximate integral.
#
  import numpy as np

  area = triangle_area ( t )

  p = triangle01_sample ( n )

  p2 = reference_to_physical_t3 ( t, n, p )

  fp = triangle_integrand ( p2 )
  
  result = area * np.sum ( fp[:] ) / float ( n )

  return result

def triangle_monte_carlo_test ( ):

#*****************************************************************************80
#
## triangle_monte_carlo_test() estimates integrals over a general triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  global e

  m = 2

  e_test = np.array ( [ \
    [ 0, 0 ], \
    [ 1, 0 ], \
    [ 0, 1 ], \
    [ 2, 0 ], \
    [ 1, 1 ], \
    [ 0, 2 ], \
    [ 3, 0 ] ] )

  print ( '' )
  print ( 'triangle_monte_carlo_test' )
  print ( '  triangle_monte_carlo estimates an integral over' )
  print ( '  a general triangle using the Monte Carlo method.' )

  t = np.array ( [ \
    [ 2.0, 3.0, 0.0 ], \
    [ 0.0, 4.0, 3.0 ] ] )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  print ( '' )
  print ( '         N        1               X               Y ' ),
  print ( '             X^2               XY             Y^2             X^3' )
  print ( '' )

  n = 1
  e = np.zeros ( m, dtype = np.int32 )

  while ( n <= 65536 ):

    print ( '  %8d' % ( n ) ),

    for j in range ( 0, 7 ):

      e[0:m] = e_test[j,0:m]

      result = triangle_monte_carlo ( t, n, triangle_integrand )

      print ( '  %14.6g' % ( result ) ),

    print ( '' )

    n = 2 * n

  return

def triangle_integrand ( xy ):

#*****************************************************************************80
#
## triangle_integrand() is a sample integrand function.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real XY(XY_NUM), the number of evaluation points.
#
#  Output:
#
#    real FXY(XY_NUM), the function values.
#
  m = 2
  n = xy.shape[1]

  fxy = monomial_value ( m, n, e, xy )

  return fxy

def triangle_monte_carlo_test01 ( ):

#*****************************************************************************80
#
## triangle_monte_carlo_test01() samples the unit triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 August 2009
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t = np.array ( [ \
    [ 1.0, 0.0, 0.0 ], \
    [ 0.0, 1.0, 0.0 ] ] )

  print ( '' )
  print ( 'triangle_monte_carlo_test01' )
  print ( '  Integrate xy^3' )
  print ( '  Integration region is the unit triangle.' )
  print ( '  Use an increasing number of points N.' )
  print ( '' )
  print ( '     N          XY^3' )
  print ( '' )

  n = 1

  while ( n <= 65536 ):

    result = triangle_monte_carlo ( t, n, triangle_integrand )

    print ( '  %8d  %14f' % ( n, result ) )

    n = 2 * n

  return

def triangle_integrand ( p ):

#*****************************************************************************80
#
## triangle_integrand() evaluates xy^3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 August 2009
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P(2,P_NUM), the evaluation points.
#
#  Output:
#
#    real FP(P_NUM), the integrand values.
#
  fp = p[0,:] * p[1,:] ** 3

  return fp

def triangle_monte_carlo_test02 ( ):

#*****************************************************************************80
#
## triangle_monte_carlo_test02() samples a general triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  t = np.array ( [ \
    [ 2.0, 3.0, 0.0 ], \
    [ 0.0, 4.0, 3.0 ] ] )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  print ( '' )
  print ( 'triangle_monte_carlo_test02' )
  print ( '  Integrate xy^3' )
  print ( '  Integration region is a general triangle.' )
  print ( '  Use an increasing number of points N.' )
  print ( '' )
  print ( '     N          XY^3' )
  print ( '' )

  n = 1

  while ( n <= 65536 ):

    result = triangle_monte_carlo ( t, n, triangle_integrand )

    print ( '  %8d  %14f' % ( n, result ) )

    n = 2 * n

  return

def triangle_integrand ( p ):

#*****************************************************************************80
#
## triangle_integrand() evaluates xy^3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 August 2009
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real P(2,P_NUM), the evaluation points.
#
#  Output:
#
#    real FP(P_NUM), the integrand values.
#
  fp = p[0,:] * p[1,:] ** 3

  return fp

def triangle_monte_carlo_tests ( ):

#*****************************************************************************80
#
## triangle_monte_carlo_tests() tests triangle_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'triangle_monte_carlo_tests()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test triangle_monte_carlo().' )

  triangle_area_test
  reference_to_physical_t3_test ( )
  triangle01_sample_test ( )
  triangle_monte_carlo_test ( )
#
#  Sample on the unit triangle, integrating XY^3.
#
  triangle_monte_carlo_test01 ( )
#
#  Sample on a general triangle, integrating X*Y^3.
#
  triangle_monte_carlo_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'triangle_monte_carlo_tests():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  triangle_monte_carlo_tests ( )
  timestamp ( )

