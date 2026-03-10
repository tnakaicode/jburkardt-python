#! /usr/bin/env python3
#
def ball01_monomial_integral ( e ):

#*****************************************************************************80
#
## ball01_monomial_integral() returns monomial integrals in the unit ball.
#
#  Discussion:
#
#    The integration region is 
#
#      X^2 + Y^2 + Z^2 <= 1.
#
#    The monomial is F(X,Y,Z) = X^E(1) * Y^E(2) * Z^E(3).
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
#  Reference:
#
#    Gerald Folland,
#    How to Integrate a Polynomial Over a Sphere,
#    American Mathematical Monthly,
#    Volume 108, Number 5, May 2001, pages 446-448.
#
#  Input:
#
#    integer E(3), the exponents of X, Y and Z in the 
#    monomial.  Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  from scipy.special import gamma
  import numpy as np

  if ( e[0] < 0 or e[1] < 0 or e[2] < 0 ):
    print ( '' )
    print ( 'ball01_monomial_integral - Fatal error!' )
    print ( '  All exponents must be nonnegative.' )
    raise Exception ( 'ball01_monomial_integral - Fatal error!' )
#
#  Integrate over the surface.
#
  if ( e[0] == 0 and e[1] == 0 and e[2] == 0 ):

    integral = 2.0 * np.sqrt ( np.pi ** 3 ) / gamma ( 1.5 )

  elif ( ( e[0] % 2 ) == 1 or ( e[1] % 2 ) == 1 or ( e[2] % 2 ) == 1 ):

    integral = 0.0

  else:

    integral = 2.0

    for i in range ( 0, 3 ):
      integral = integral * gamma ( 0.5 * float ( e[i] + 1 ) )

    integral = integral / gamma ( 0.5 * float ( e[0] + e[1] + e[2] + 3 ) )
#
#  The surface integral is now adjusted to give the volume integral.
#
  r = 1.0
  s = e[0] + e[1] + e[2] + 3

  integral = integral * r ** s / float ( s )

  return integral

def ball01_monomial_integral_test ( ):

#*****************************************************************************80
#
## ball01_monomial_integral_test() tests ball01_monomial_integral().
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
  print ( 'ball01_monomial_integral_test():' )
  print ( '  ball01_monomial_integral() returns the integral of a monomial' )
  print ( '  over the interior of the unit ball in 3D.' )
  print ( '  Compate against Monte Carlo estimates.' )
#
#  Get sample points.
#
  x = ball01_sample ( n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose X,Y exponents between 0 and 8.
#
  print ( '' )
  print ( '  If any exponent is odd, the integral is zero.' )
  print ( '  We will restrict this test to randomly chosen even exponents.' )
  print ( '' )
  print ( '  Ex  Ey  Ez     MC-Estimate           Exact      Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = rng.integers ( low = 0, high = 4, size = m, endpoint = True )

    for i in range ( 0, 3 ):
      e[i] = e[i] * 2

    value = monomial_value ( m, n, e, x )

    result = ball01_volume ( ) * np.sum ( value ) / float ( n )
    exact = ball01_monomial_integral ( e )
    error = abs ( result - exact )

    print ( '  %2d  %2d  %2d  %14.6g  %14.6g  %10.2e' \
      % ( e[0], e[1], e[1], result, exact, error ) )

  return

def ball01_sample ( n, rng ):

#*****************************************************************************80
#
## ball01_sample() uniformly samples the unit ball.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 January 2023
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
#    integer N, the number of points.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(3,N), the points.
#
  import numpy as np

  x = np.zeros ( [ 3, n ] )

  for j in range ( 0, n ):
#
#  Fill a vector with normally distributed values.
#
    v = rng.standard_normal ( size = 3 )
#
#  Compute the length of the vector.
#
    norm = np.sqrt ( v[0] ** 2 + v[1] ** 2 + v[2] ** 2 )
#
#  Normalize the vector.
#
    for i in range ( 0, 3 ):
      v[i] = v[i] / norm
#
#  Transfer the point from the surface to the interior.
#
    r = rng.random ( )

    r = r ** ( 1.0 / 3.0 )
    for i in range ( 0, 3 ):
      x[i,j] = r * v[i]

  return x

def ball01_sample_test ( ):

#*****************************************************************************80
#
## ball01_sample_test() tests ball01_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2023
#
#  Author:
#
#    John Burkardt
#
  import platform
  from numpy.random import default_rng

  print ( '' )
  print ( 'ball01_sample_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ball01_sample() samples the unit ball.' )

  rng = default_rng ( )

  n = 10

  x = ball01_sample ( n, rng )

  r8mat_transpose_print ( 3, n, x, '  Sample points in the unit ball.' )

  return

def ball01_volume ( ):

#*****************************************************************************80
#
## ball01_volume() returns the volume of the unit ball.
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
#    real VALUE, the volume of the unit ball.
#
  import numpy as np

  r = 1.0
  value = 4.0 * np.pi * r ** 3 / 3.0

  return value

def ball01_volume_test ( ) :

#*****************************************************************************80
#
## ball01_volume_test() tests ball01_volume().
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
  print ( 'ball01_volume_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ball01_volume() returns the volume of the unit ball.' )

  value = ball01_volume ( )

  print ( '' )
  print ( '  ball01_volume() = %g' % ( value ) )

  return

def ball_integrals_test ( ):

#*****************************************************************************80
#
## ball_integrals_test() tests ball_integrals().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'ball_integrals_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ball_integrals().' )

  ball01_monomial_integral_test ( )
  ball01_sample_test ( )
  ball01_volume_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ball_integrals_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )
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
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8mat_transpose_print() prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )

  print ( '' )
  print ( 'r8mat_transpose_print_test():' )
  print ( '  Normal end of execution.' )

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
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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
    print ( '%6d  %12g' % ( i, a[i] ) )

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

if ( __name__ == '__main__' ):
  timestamp ( )
  ball_integrals_test ( )
  timestamp ( )

