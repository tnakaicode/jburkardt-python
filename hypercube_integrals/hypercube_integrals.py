#! /usr/bin/env python3
#
def hypercube01_monomial_integral ( m, e ):

#*****************************************************************************80
#
## hypercube01_monomial_integral(): integrals over the unit hypercube in M dimensions.
#
#  Discussion:
#
#    The integration region is 
#
#      0 <= X(1:M) <= 1,
#
#    The monomial is F(X) = product ( 1 <= I <= M ) X(I)^E(I).
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
#    Philip Davis, Philip Rabinowitz,
#    Methods of Numerical Integration,
#    Second Edition,
#    Academic Press, 1984, page 263.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer E(M), the exponents.  Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  for i in range ( 0, m ):
    if ( e[i] < 0 ):
      print ( '' )
      print ( 'hypercube01_monomial_integral - Fatal error!' )
      print ( '  All exponents must be nonnegative.' )
      raise Exception ( 'hypercube01_monomial_integral - Fatal error!' )

  integral = 1.0
  for i in range ( 0, m ):
    integral = integral / float ( e[i] + 1 )

  return integral

def hypercube01_monomial_integral_test ( rng ):

#*****************************************************************************80
#
## hypercube01_monomial_integral_test() tests hypercube01_monomial_integral().
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
#    rng(): the current random number generator.
#
  import numpy as np

  m = 3
  n = 4192
  test_num = 20

  print ( '' )
  print ( 'hypercube01_monomial_integral_test():' )
  print ( '  hypercube01_monomial_integral() returns the integral of a monomial' )
  print ( '  over the interior of the unit hypercube in 3D.' )
  print ( '  Compare with a Monte Carlo estimate.' )
  print ( '' )
  print ( '  Using M = ', m )
#
#  Get sample points.
#
  x = hypercube01_sample ( m, n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose exponents.
#
  print ( '' )
  print ( '  Ex  Ey  Ez     MC-Estimate           Exact      Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = rng.integers ( low = 0, high = 4, size = m, endpoint = False )

    value = monomial_value ( m, n, e, x )

    result = hypercube01_volume ( m ) * np.sum ( value ) / float ( n )
    exact = hypercube01_monomial_integral ( m, e )
    error = abs ( result - exact )

    for i in range ( 0, m ):
      print ( '  %2d' % ( e[i] ) ),
    print ( '  %14.6g  %14.6g  %10.2g' % ( result, exact, error ) )

  return

def hypercube01_sample ( m, n, rng ):

#*****************************************************************************80
#
## hypercube01_sample() samples points in the unit hypercube in M dimensions.
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

  x = rng.random ( size = [ m, n ] )

  return x

def hypercube01_sample_test ( rng ):

#*****************************************************************************80
#
## hypercube01_sample_test() tests hypercube01_sample().
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
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'hypercube01_sample_test():' )
  print ( '  hypercube01_sample() samples the unit hypercube' )
  print ( '  in M dimensions.' )

  m = 3
  n = 10

  x = hypercube01_sample ( m, n, rng )

  r8mat_transpose_print ( m, n, x, '  Sample points in the unit hypercube.' )

  return

def hypercube01_volume ( m ):

#*****************************************************************************80
#
## hypercube01_volume() returns the volume of the unit hypercube in M dimensions.
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
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real VALUE, the volume.
#
  value = 1.0

  return value

def hypercube01_volume_test ( ) :

#*****************************************************************************80
#
## hypercube01_volume_test() tests hypercube01_volume().
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
  import platform

  print ( '' )
  print ( 'hypercube01_volume_test():' )
  print ( '  hypercube01_volume() returns the volume of the unit hypercube' )
  print ( '  in M dimensions.' )

  m = 3

  value = hypercube01_volume ( m )

  print ( '' )
  print ( '  hypercube01_volume(%d) = %g' % ( m, value ) )

  return

def hypercube_integrals_test ( ):

#*****************************************************************************80
#
## hypercube_integrals_test() tests hypercube_integrals().
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
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'hypercube_integrals_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hypercube_integrals().' )

  rng = default_rng ( )

  hypercube01_monomial_integral_test ( rng )
  hypercube01_sample_test ( rng )
  hypercube01_volume_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hypercube_integrals_test():' )
  print ( '  Normal end of execution.' )
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

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  hypercube_integrals_test ( )
  timestamp ( )

