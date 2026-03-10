#! /usr/bin/env python3
#
def disk01_positive_monte_carlo_test ( ):

#*****************************************************************************80
#
## disk01_positive_monte_carlo_test() tests disk01_positive_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'disk01_positive_monte_carlo_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test disk01_positive_monte_carlo().' )

  rng = default_rng ( )

  disk01_positive_area_test ( )
  disk01_positive_monomial_integral_test ( rng )
  disk01_positive_sample_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'disk01_positive_monte_carlo_test():' )
  print ( '  Normal end of execution.' )
  return

def disk01_positive_area ( ):

#*****************************************************************************80
#
## disk01_positive_area() returns the area of the unit positive_disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real AREA, the area.
#
  import numpy as np

  value = np.pi / 4.0

  return value

def disk01_positive_area_test ( ) :

#*****************************************************************************80
#
## disk01_positive_area_test() tests disk01_positive_area().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'disk01_positive_area_test():' )
  print ( '  disk01_positive_area returns the area of the unit positive disk.' )

  value = disk01_positive_area ( )

  print ( '' )
  print ( '  disk01_positive_area() = %g' % ( value ) )

  return

def disk01_positive_monomial_integral ( e ):

#*****************************************************************************80
#
## disk01_positive_monomial_integral(): monomial integrals in unit positive disk.
#
#  Discussion:
#
#    The integration region is 
#
#      X^2 + Y^2 <= 1.
#      0 <= X, 0 <= Y.
#
#    The monomial is F(X,Y) = X^E(1) * Y^E(2).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer E(2), the exponents of X and Y in the 
#    monomial.  Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  from scipy.special import gamma

  f1 = gamma ( ( e[0]        + 3 ) / 2.0 )
  f2 = gamma ( (        e[1] + 1 ) / 2.0 )
  f3 = gamma ( ( e[0] + e[1] + 4 ) / 2.0 )

  integral = f1 * f2 / f3 / 2.0 / ( 1.0 + e[0] )

  return integral

def disk01_positive_monomial_integral_test ( rng ):

#*****************************************************************************80
#
## disk01_positive_monomial_integral_test() tests disk01_positive_monomial_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 May 2016
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
  n = 4192
  test_num = 20

  print ( '' )
  print ( 'disk01_positive_monomial_integral_test():' )
  print ( '  disk01_positive_monomial_integral computes monomial integrals' )
  print ( '  over the interior of the unit disk in 2D.' )
  print ( '  Compare with a Monte Carlo value.' )
#
#  Get sample points.
#
  x = disk01_positive_sample ( n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose X,Y exponents.
#
  print ( '' )
  print ( '  We will restrict this test to randomly chosen even exponents.' )
  print ( '' )
  print ( '  Ex  Ey     MC-Estimate           Exact      Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = rng.integers ( low = 0, high = 4, size = m, endpoint = True )

    value = monomial_value ( e, x )

    result = disk01_positive_area ( ) * np.sum ( value ) / float ( n )
    exact = disk01_positive_monomial_integral ( e )
    error = abs ( result - exact )

    print ( '  %2d  %2d  %14.6g  %14.6g  %10.2g' \
      % ( e[0], e[1], result, exact, error ) )

  return

def disk01_positive_sample ( n, rng ):

#*****************************************************************************80
#
## disk01_positive_sample() uniformly samples the unit positive disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 August 2023
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
#    real x(n,2): the points.
#
  import numpy as np

  x = np.zeros ( [ n, 2 ] )

  for i in range ( 0, n ):
#
#  Fill a vector with normally distributed values.
#
    v = rng.standard_normal ( size = 2 )
#
#  Compute the length of the vector.
#
    norm = np.sqrt ( v[0] ** 2 + v[1] ** 2 )
#
#  Normalize the vector.
#
    v[0] = v[0] / norm
    v[1] = v[1] / norm
#
#  Now compute a value to map the point ON the disk INTO the disk.
#
    r = rng.random ( )

    x[i,0] = np.sqrt ( r ) * np.abs ( v[0] )
    x[i,1] = np.sqrt ( r ) * np.abs ( v[1] )

  return x

def disk01_positive_sample_test ( rng ):

#*****************************************************************************80
#
## disk01_positive_sample_test() tests disk01_positive_sample().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import platform

  print ( '' )
  print ( 'disk01_positive_sample_test():' )
  print ( '  disk01_positive_sample() samples the unit positive disk.' )

  n = 10
  x = disk01_positive_sample ( n, rng )

  print ( '' )
  print ( '  Sample points in the unit positive disk.' )
  print ( x )

  return

def monomial_value ( e, x ):

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
#    10 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer E(D), the exponents.
#
#    real X(N,D), the point coordinates.
#
#  Output:
#
#    real V(N), the monomial values.
#
  import numpy as np

  n, d = x.shape

  v = np.ones ( n )

  for j in range ( 0, d ):
    if ( 0 != e[j] ):
      for i in range ( 0, n ):
        v[i] = v[i] * x[i,j] ** e[j]

  return v

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
  disk01_positive_monte_carlo_test ( )
  timestamp ( )

