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
    print ( '  Row: ' ),

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

def triangle01_area ( ):

#*****************************************************************************80
#
## triangle01_area() computes the area of the unit triangle in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 January 2014
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real AREA, the area.
#
  area = 0.5

  return area

def triangle01_area_test ( ):

#*****************************************************************************80
#
## triangle01_area_test() tests triangle01_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 November 2016
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
  print ( 'triangle01_area_test' )
  print ( '  triangle01_area computes the area of the unit triangle.' )

  r8mat_print ( 2, 3, t, '  Triangle vertices (columns)' )

  area = triangle01_area ( )

  print ( '' )
  print ( '  Triangle area is %g' % ( area ) )

  return

def triangle01_monomial_integral ( i, j ):

#*****************************************************************************80
#
## triangle01_monomial_integral(): monomial integrals in the unit triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the exponents.  
#    Each exponent must be nonnegative.
#
#  Output:
#
#    real Q, the integral.
#
  k = 0
  q = 1.0

  for l in range ( 1, i + 1 ):
    k = k + 1
    q = q * float ( l ) / float ( k )

  for l in range ( 1, j + 1 ):
    k = k + 1
    q = q * float ( l ) / float ( k )

  for l in range ( 1, 3 ):
    k = k + 1
    q = q / float ( k )

  return q

def triangle01_monomial_integral_test ( ):

#*****************************************************************************80
#
## triangle01_monomial_integral_test() estimates integrals over the unit triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'triangle01_monomial_integral_test' )
  print ( '  triangle01_monomial_integral returns the integral Q of' )
  print ( '  a monomial X^I Y^J over the interior of the unit triangle.' )

  print ( '' )
  print ( '   I   J         Q(I,J)' )

  for d in range ( 0, 6 ):
    print ( '' )
    for i in range ( 0, d + 1 ):
      j = d - i
      q = triangle01_monomial_integral ( i, j )
      print ( '  %2d  %2d  %14.6g' % ( i, j, q ) )

  return

def triangle01_monte_carlo ( xy_num, triangle01_integrand ):

#*****************************************************************************80
#
## triangle01_monte_carlo() applies the Monte Carlo rule to integrate a function.
#
#  Discussion:
#
#    The function f(x,y) is to be integrated over the unit triangle.
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
#    integer XY_NUM, the number of sample points.
#
#    external triangle01_integrand, the integrand routine.
#
#  Output:
#
#    real RESULT(F_NUM), the approximate integrals.
#
  import numpy as np

  area = 0.5

  xy = triangle01_sample ( xy_num )

  fxy = triangle01_integrand ( xy )
 
  result = area * np.sum ( fxy ) / float ( xy_num )

  return result

def triangle01_monte_carlo_test ( ):

#*****************************************************************************80
#
## triangle01_monte_carlo_test() estimates integrals over the unit triangle.
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
  print ( 'triangle01_monte_carlo_test01' )
  print ( '  triangle01_monte_carlo estimates an integral over' )
  print ( '  the unit triangle using the Monte Carlo method.' )
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

      result = triangle01_monte_carlo ( n, triangle01_integrand )

      print ( '  %14.6g' % ( result ) ),

    print ( '' )

    n = 2 * n

  print ( '' )
  print ( '     Exact' ),

  for j in range ( 0, 7 ):

    e[0:m] = e_test[j,0:m]

    result = triangle01_monomial_integral ( e[0], e[1] )

    print ( '  %14.6g' % ( result ) ),

  print ( '' )

  return

def triangle01_integrand ( xy ):

#*****************************************************************************80
#
## triangle01_integrand() is a sample integrand function.
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

def triangle01_monte_carlo_tests ( ):

#*****************************************************************************80
#
## triangle01_monte_carlo_tests() tests triangle01_monte_carlo().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'triangle01_monte_carlo_tests():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test triangle01_monte_carlo().' )

  triangle01_area_test ( )
  triangle01_monomial_integral_test ( )
  triangle01_monte_carlo_test ( )
  triangle01_sample_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'triangle01_monte_carlo_tests():' )
  print ( '  Normal end of execution.' )
  return

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
  print ( 'triangle01_sample_test():' )
  print ( '  triangle01_sample() samples the unit triangle.' )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  print ( '' )
  print ( '  Sample points (X,Y):' )
  print ( '' )

  n = 10
  xy = triangle01_sample ( n )
  r8mat_transpose_print ( 2, n, xy, '  Sample points:' )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  triangle01_monte_carlo_tests ( )
  timestamp ( )

