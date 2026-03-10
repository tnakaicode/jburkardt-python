#! /usr/bin/env python3
#
def cube01_monomial_integral ( e ):

#*****************************************************************************80
#
## cube01_monomial_integral(): integrals over the unit cube in 3D.
#
#  Discussion:
#
#    The integration region is 
#
#      0 <= X <= 1,
#      0 <= Y <= 1,
#      0 <= Z <= 1.
#
#    The monomial is F(X,Y,Z) = X^E(1) * Y^E(2) * Z^E(3).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 January 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Academic Press, 1984, page 263.
#
#  Input:
#
#    integer E(3), the exponents.  Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  m = 3

  if ( e[0] < 0 or e[1] < 0 or e[2] < 0 ):
    print ( '' )
    print ( 'cube01_monomial_integral - Fatal error!' )
    print ( '  All exponents must be nonnegative.' )
    raise Exception ( 'cube01_monomial_integral - Fatal error!' )

  integral = 1.0
  for i in range ( 0, m ):
    integral = integral / float ( e[i] + 1 )

  return integral

def cube01_monomial_integral_test ( ):

#*****************************************************************************80
#
## cube01_monomial_integral_test() tests cube01_monomial_integral().
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
  from numpy.random import default_rng
  import numpy as np
  import platform

  rng = default_rng ( )

  m = 3
  n = 4192
  test_num = 20

  print ( '' )
  print ( 'cube01_monomial_integral_test():' )
  print ( '  cube01_monomial_integral() computes the integral of a monomial' )
  print ( '  within the interior of the unit cube in 3D.' )
  print ( '  Compare with a Monte Carlo estimate.' )
#
#  Get sample points.
#
  x = cube01_sample ( n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose exponents.
#
  print ( '' )
  print ( '  Ex  Ey  Ez     MC-Estimate           Exact      Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = rng.integers ( low = 0, high = 7, size = m, endpoint = True )

    value = monomial_value ( m, n, e, x )

    result = cube01_volume ( ) * np.sum ( value ) / float ( n )
    exact = cube01_monomial_integral ( e )
    error = abs ( result - exact )

    print ( '  %2d  %2d  %2d  %14.6g  %14.6g  %10.2g' \
      % ( e[0], e[1], e[2], result, exact, error ) )

  return

def cube01_monte_carlo_test ( ):

#*****************************************************************************80
#
## cube01_monte_carlo_test() tests cube01_monte_carlo().
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

  m = 3

  e_test = np.array ( [ \
    [ 0, 0, 0 ], \
    [ 1, 0, 0 ], \
    [ 0, 1, 0 ], \
    [ 0, 0, 1 ], \
    [ 2, 0, 0 ], \
    [ 1, 1, 0 ], \
    [ 1, 0, 1 ], \
    [ 0, 2, 0 ], \
    [ 0, 1, 1 ], \
    [ 0, 0, 2 ] ] )

  print ( '' )
  print ( 'cube01_monte_carlo_test()' )
  print ( '  cube01_sample() estimates integrals' )
  print ( '  along the interior of the unit cube in 3D.' )
  print ( '' )
  print ( '         N', end = '' )
  print ( '        1', end = '' )
  print ( '               X', end = '' )
  print ( '               Y ', end = '' )
  print ( '              Z', end = '' )
  print ( '               X^2', end = '' )
  print ( '              XY', end = '' )
  print ( '             XZ', end = '' )
  print ( '              Y^2', end = '' )
  print ( '             YZ', end = '' )
  print ( '               Z^2', end = '' )
  print ( '' )

  n = 1

  e = np.zeros ( m )

  while ( n <= 65536 ):

    x = cube01_sample ( n, rng )
    print ( '  %8d' % ( n ), end = '' )

    for j in range ( 0, 10 ):

      e[0:m] = e_test[j,0:m]

      value = monomial_value ( m, n, e, x )

      result = cube01_volume ( ) * np.sum ( value[0:n] ) / float ( n )

      print ( '  %14.6g' % ( result ), end = '' )

    print ( '' )

    n = 2 * n

  print ( '' )
  print ( '     Exact', end = '' )

  for j in range ( 0, 10 ):

    e[0:m] = e_test[j,0:m]

    result = cube01_monomial_integral ( e )
    print ( '  %14.6g' % ( result ), end = '' )

  print ( '' )

  return

def cube01_sample ( n, rng ):

#*****************************************************************************80
#
## cube01_sample() samples points in the unit cube in 3D.
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
#  Input:
#
#    integer N, the number of points.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(3,N), the points.
#
  import numpy as np

  x = rng.random ( size = [ 3, n ] )

  return x

def cube01_sample_test ( ):

#*****************************************************************************80
#
## cube01_sample_test() tests cube01_sample().
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
  from numpy.random import default_rng

  rng = default_rng ( )

  print ( '' )
  print ( 'cube01_sample_test():' )
  print ( '  cube01_sample() samples the unit cube.' )

  n = 10
  x = cube01_sample ( n, rng )

  r8mat_transpose_print ( 3, n, x, '  Sample points in the unit cube.' )

  return

def cube01_volume ( ):

#*****************************************************************************80
#
## cube01_volume() returns the volume of the unit cube in 3D.
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
#  Output:
#
#    real VALUE, the volume.
#
  value = 1.0

  return value

def cube01_volume_test ( ) :

#*****************************************************************************80
#
## cube01_volume() tests cube01_volume().
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
  print ( 'cube01_volume_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  cube01_volume() returns the volume of the unit cube.' )

  value = cube01_volume ( )

  print ( '' )
  print ( '  Volume = %g' % ( value ) )

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
        if ( x[i,j] == 0.0 ):
          v[j] = 0.0
        else:
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

  return

def cube_monte_carlo_test ( ):

#*****************************************************************************80
#
## cube_monte_carlo_test() tests cube_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    07 November 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'cube_monte_carlo_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test cube_monte_carlo().' )

  cube01_monomial_integral_test ( )
  cube01_monte_carlo_test ( )
  cube01_sample_test ( )
  cube01_volume_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'cube_monte_carlo_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  cube_monte_carlo_test ( )
  timestamp ( )
 
