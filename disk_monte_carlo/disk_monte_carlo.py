#! /usr/bin/env python3
#
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
#    22 June 2015
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

def disk_area ( center, r ):

#*****************************************************************************80
#
## disk_area() returns the area of a general disk.
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
#    real CENTER(2), the center of the disk. 
#    This information is not needed for the area calculation.
#
#    real R, the radius of the disk.
#
#  Output:
#
#    real AREA, the area of the unit disk.
#
  import numpy as np

  value = np.pi * r * r

  return value

def disk_area_test ( rng ):

#*****************************************************************************80
#
## disk_area_test() tests disk_area().
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
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'disk_area_test():' )
  print ( '  disk_area() returns the area of the unit disk.' )

  center = np.zeros ( 2 )

  print ( '' )
  print ( '  (   CX        CY     )    R          Area' )
  print ( '' )

  for i in range ( 0, 10 ):
    data = rng.random ( size = 3 )
    center[0] = 10.0 * data[0] - 5.0
    center[1] = 10.0 * data[1] - 5.0
    r = data[2]
    area = disk_area ( center, r )
    print ( '  (%9.6f,%9.6f)  %9.6f  %9.6f' \
      % ( center[0], center[1], r, area ) )

  return

def disk_monte_carlo_test ( ):

#*****************************************************************************80
#
## disk_monte_carlo_test() tests disk_monte_carlo().
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
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'disk_monte_carlo_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test disk_monte_carlo().' )

  rng = default_rng ( )

  disk_area_test ( rng )

  center = np.zeros ( 2 )
  center = np.array ( [ 0.0, 0.0 ] )
  r = 1.0
  disk_sample_test ( center, r, rng )

  center = np.zeros ( 2 )
  center = np.array ( [ 1.0, 0.0 ] )
  r = 1.0
  disk_sample_test ( center, r, rng )

  center = np.zeros ( 2 )
  center = np.array ( [ 1.0, 2.0 ] )
  r = 3.0
  disk_sample_test ( center, r, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'disk_monte_carlo_test():' )
  print ( '  Normal end of execution.' )
  return

def disk_sample ( center, r, n, rng ):

#*****************************************************************************80
#
## disk_sample() uniformly samples the unit disk.
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
#    real CENTER(2), the center of the disk. 
#
#    real R, the radius of the disk.
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
    r2 = rng.random ( )

    x[0,j] = center[0] + r * np.sqrt ( r2 ) * v[0]
    x[1,j] = center[1] + r * np.sqrt ( r2 ) * v[1]

  return x

def disk_sample_test ( center, r, rng ):

#*****************************************************************************80
#
## disk_sample_test() tests disk_sample().
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
#    real CENTER(2), the center of the disk. 
#
#    real R, the radius of the disk.
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'disk_sample_test():' )
  print ( '  disk_sample() estimates integrals in the disk' )
  print ( '  with center (%g,%g) and radius %g' \
    % ( center[0], center[1], r ) )

  e_test = np.array ( [ \
    [ 0, 0 ], \
    [ 2, 0 ], \
    [ 0, 2 ], \
    [ 4, 0 ], \
    [ 2, 2 ], \
    [ 0, 4 ], \
    [ 6, 0 ] ] )

  print ( '' )
  print ( '         N        1              X^2             Y^2             X^4             X^2Y^2           Y^4             X^6' )
  print ( '' )

  n = 1

  while ( n <= 65536 ):

    x = disk_sample ( center, r, n, rng )

    print ( '  %8d' % ( n ), end = '' )

    for i in range ( 0, 7 ):

      e = e_test[i,:]

      value = monomial_value ( 2, n, e, x )

      result = disk_area ( center, r ) * np.sum ( value[:] ) / n
      print ( '  %14.6g' %  ( result ), end = '' )

    print ( '' )

    n = 2 * n

  if ( \
    center[0] == 0.0 and \
    center[1] == 0.0 and \
    r == 1.0 ):
    print ( '' )
    print ( '     Exact', end = '' )
    for i in range ( 0, 7 ):
      e = e_test[i,:]
      result = disk01_monomial_integral ( e )
      print ( '  %14.6g' % ( result ), end = '' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  disk_monte_carlo_test ( )
  timestamp ( )

