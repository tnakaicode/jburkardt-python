#! /usr/bin/env python3
#
def disk01_monte_carlo_test ( ):

#*****************************************************************************80
#
## disk01_monte_carlo_test() tests disk01_monte_carlo().
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
  print ( 'disk01_monte_carlo_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test disk01_monte_carlo().' )

  rng = default_rng ( )

  disk01_area_test ( )
  disk01_monomial_integral_test ( rng )
  disk01_sample_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'disk01_monte_carlo_test():' )
  print ( '  Normal end of execution.' )
  return

def disk01_area ( ):

#*****************************************************************************80
#
## disk01_area() returns the area of the unit disk.
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
#  Output:
#
#    real AREA, the area of the unit disk.
#
  import numpy as np

  r = 1.0
  value = np.pi * r * r

  return value

def disk01_area_test ( ) :

#*****************************************************************************80
#
## disk01_area_test() tests disk01_area().
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
  print ( 'disk01_area_test():' )
  print ( '  disk01_area() returns the area of the unit disk.' )

  value = disk01_area ( )

  print ( '' )
  print ( '  disk01_area() = %g' % ( value ) )

  return

def disk01_monomial_integral ( e ):

#*****************************************************************************80
#
## disk01_monomial_integral() returns monomial integrals in the unit disk.
#
#  Discussion:
#
#    The integration region is 
#
#      X^2 + Y^2 <= 1.
#
#    The monomial is F(X,Y) = X^E(1) * Y^E(2).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 July 2018
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

  r = 1.0

  if ( e[0] < 0 or e[1] < 0 ):
    print ( '' )
    print ( 'disk01_monomial_integral(): Fatal error!' )
    print ( '  All exponents must be nonnegative.' )
    raise Exception ( 'disk01_monomial_integral(): Fatal error!' )

  if ( ( ( e[0] % 2 ) == 1 ) or ( ( e[1] % 2 ) == 1 ) ):

    integral = 0.0

  else:

    integral = 2.0

    for i in range ( 0, 2 ):
      arg = 0.5 * float ( e[i] + 1 )
      integral = integral * gamma ( arg )

    arg = 0.5 * float ( e[0] + e[1] + 2 )
    integral = integral / gamma ( arg )
#
#  The surface integral is now adjusted to give the volume integral.
#
  s = e[0] + e[1] + 2

  integral = integral * r ** s / float ( s )

  return integral

def disk01_monomial_integral_test ( rng ):

#*****************************************************************************80
#
## disk01_monomial_integral_test() tests disk01_monomial_integral().
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
  import platform

  m = 2
  n = 4192
  test_num = 20

  print ( '' )
  print ( 'disk01_monomial_integral_test():' )
  print ( '  disk01_monomial_integral() computes monomial integrals' )
  print ( '  over the interior of the unit disk in 2D.' )
  print ( '  Compare with a Monte Carlo value.' )
#
#  Get sample points.
#
  x = disk01_sample ( n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose X,Y exponents between 0 and 8.
#
  print ( '' )
  print ( '  If any exponent is odd, the integral is zero.' )
  print ( '  We will restrict this test to randomly chosen even exponents.' )
  print ( '' )
  print ( '  Ex  Ey     MC-Estimate           Exact      Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = rng.integers ( low = 0, high = 4, size = m, endpoint = True )

    e[0] = e[0] * 2
    e[1] = e[1] * 2

    value = monomial_value ( m, n, e, x )

    result = disk01_area ( ) * np.sum ( value ) / float ( n )
    exact = disk01_monomial_integral ( e )
    error = abs ( result - exact )

    print ( '  %2d  %2d  %14.6g  %14.6g  %10.2g' \
      % ( e[0], e[1], result, exact, error ) )

  return

def disk01_sample ( n, rng ):

#*****************************************************************************80
#
## disk01_sample() uniformly samples the unit disk.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 January 2014
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
#    real X(2,N), the points.
#
  import numpy as np

  x = np.zeros ( [ 2, n ] )

  for j in range ( 0, n ):
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

    x[0,j] = np.sqrt ( r ) * v[0]
    x[1,j] = np.sqrt ( r ) * v[1]

  return x

def disk01_sample_test ( rng ):

#*****************************************************************************80
#
## disk01_sample_test() tests disk01_sample().
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
#    rng(): the current random number generator.
#
  import platform

  print ( '' )
  print ( 'disk01_sample_test():' )
  print ( '  disk01_sample() samples the unit disk.' )

  n = 10
  x = disk01_sample ( n, rng )

  print ( '' )
  print ( '  Sample points in the unit disk.' )
  print ( x )

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
  disk01_monte_carlo_test ( )
  timestamp ( )

