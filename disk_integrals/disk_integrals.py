#! /usr/bin/env python3
#
def disk_area ( r ):

#*****************************************************************************80
#
## disk_area() returns the area of a disk of radius R.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real r: the radius of the disk.
#
#  Output:
#
#    real area: the area of the disk.
#
  import numpy as np

  area = np.pi * r * r

  return area

def disk_integrals_test01 ( n, rng ):

#*****************************************************************************80
#
## disk_integrals_test01() compares exact and Monte Carlo integral estimates.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 November 2002
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the number of sample points to use.
#
#    rng(): the current random number generator.
#
  import numpy as np

  m = 2
  test_num = 20

  print ( '' )
  print ( 'disk_integrals_test01():' )
  print ( '  Estimate monomial integrals using Monte Carlo' )
  print ( '  over the interior of the unit disk in 2D.' )
#
#  Get sample points.
#
  r = 2.0
  x = disk_sample ( r, n, rng )

  print ( '' )
  print ( '  Disk radius is', r )
  print ( '  Number of sample points is', n )
#
#  Randomly choose X,Y exponents between 0 and 8.
#
  print ( '' )
  print ( '  If any exponent is odd, the integral is zero.' )
  print ( '  We will restrict this test to randomly chosen even exponents.' )
  print ( '' )
  print ( '  Ex  Ey     MC-Estimate           Exact      Error' )
  print ( '' )

  for e1 in range ( 0, 8, 2 ):

    for e2 in range ( 0, 8, 2 ):

      e = [ e1, e2 ]

      value = monomial_value ( m, n, e, x )

      result = disk_area ( r ) * np.sum ( value ) / n
      exact = disk_monomial_integral ( r, e )
      error = np.abs ( result - exact )

      print ( '  %2d  %2d  %14.6g  %14.6g  %10.2e' \
        % ( e[0], e[1], result, exact, error ) )

  return

def disk_integrals_test ( ):

#*****************************************************************************80
#
## disk_integrals_test() tests disk_integrals().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'disk_integrals_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test disk_integrals().' )

  rng = default_rng ( )

  n = 4192
  disk_integrals_test01 ( n, rng )

  n = n * 16
  disk_integrals_test01 ( n, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'disk_integrals_test():' )
  print ( '  Normal end of execution.' )

  return

def disk_monomial_integral ( r, e ):

#*****************************************************************************80
#
## disk_monomial_integral() returns monomial integrals in disk of radius R.
#
#  Discussion:
#
#    The integration region is 
#
#      X^2 + Y^2 <= R^2.
#
#    The monomial is F(X,Y) = X^E(1) * Y^E(2).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real r: the radius of the disk.
#
#    integer e(2): the nonnegative exponents of X and Y.
#
#  Output:
#
#    real integral: the integral.
#
  from scipy.special import gamma

  if ( e[0] < 0 or e[1] < 0 ):
    print ( '' )
    print ( 'disk_monomial_integral() - Fatal error!' )
    print ( '  All exponents must be nonnegative.' )
    raise Exception ( 'disk_monomial_integral() - Fatal error!' )

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

  return

def disk_sample ( r, n, rng ):

#*****************************************************************************80
#
## disk_sample() uniformly samples a disk centered at the origin.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real r: the radius of the disk.
#
#    integer n: the number of sample points.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real x(n,2): the points.
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
    s = rng.random ( )

    x[0,j] = r * np.sqrt ( s ) * v[0]
    x[1,j] = r * np.sqrt ( s ) * v[1]

  return x

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
  disk_integrals_test ( )
  timestamp ( )

