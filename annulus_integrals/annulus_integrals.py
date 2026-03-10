#! /usr/bin/env python3
#
def annulus_area ( r1, r2 ):

#*****************************************************************************80
#
## annulus_area() computes the area of a annulus centered at the origin.
#
#  Discussion:
#
#    A circular annulus centered at the origin, with inner radius R1 and
#    outer radius R2, is the set of points (X,Y) so that
#
#      R1^2 <= X^2 + Y^2 <= R2^2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real r1, r2: the inner and outer radii.
#    0.0 <= R1, and normally R1 <= R2.
#
#  Output:
#
#    real area: the area of the annulus.
#
  import numpy as np

  if ( r1 < 0.0 ):
    print ( '' )
    print ( 'annulus_area(): Fatal error!' )
    print ( '  Inner radius R1 < 0.0.' )
    raise Exception ( 'annulus_area(): Fatal error!' )

  area = np.pi * ( r2 + r1 ) * ( r2 - r1 )

  return area

def annulus_integrals_test01 ( r1, r2, n ):

#*****************************************************************************80
#
## annulus_integrals_test01() compares exact and Monte Carlo integral estimates.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 November 2002
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real r1, r2: the inner and outer radius.
#
#    integer n: the number of sample points.
#
  import numpy as np

  m = 2
  test_num = 20

  print ( '' )
  print ( 'annulus_integrals_test01():' )
  print ( '  Estimate monomial integrals using Monte Carlo method' )
  print ( '  over the interior of an annulus centered at the origin.' )
#
#  Get sample points.
#
  x = annulus_sample ( r1, r2, n )

  print ( '' )
  print ( '  Inner radius is', r1 )
  print ( '  Outer radius is', r2 )
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

  for e1 in range ( 0, 10, 2 ):

    for e2 in range ( 0, 10, 2 ):

      e = np.array ( [ e1, e2 ] )

      value = monomial_value ( m, n, e, x )

      result = annulus_area ( r1, r2 ) * np.sum ( value ) / n
      exact = annulus_monomial_integral ( r1, r2, e )
      error = np.abs ( result - exact )

      print ( '  %2d  %2d  %14.6g  %14.6g  %10.2e' \
        % ( e[0], e[1], result, exact, error ) )

  return

def annulus_integrals_test ( ):

#*****************************************************************************80
#
## annulus_integrals_test() tests annulus_integrals().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'annulus_integrals_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test annulus_integrals().' )

  r1 = 0.0
  r2 = 1.0
  n = 4192
  annulus_integrals_test01 ( r1, r2, n )

  r1 = 1.0
  r2 = 2.0
  n = 4192
  annulus_integrals_test01 ( r1, r2, n )

  r1 = 1.0
  r2 = 2.0
  n = n * 16
  annulus_integrals_test01 ( r1, r2, n )
#
#  Terminate.
#
  print ( '' )
  print ( 'annulus_integrals_test():' )
  print ( '  Normal end of execution.' )

  return

def annulus_monomial_integral ( r1, r2, e ):

#*****************************************************************************80
#
## annulus_monomial_integral() returns monomial integrals over an annulus.
#
#  Discussion:
#
#    A circular annulus centered at the origin, with inner radius R1 and
#    outer radius R2, is the set of points (X,Y) so that
#
#      R1^2 <= X^2 + Y^2 <= R2^2
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
#    real r1, r2: the inner and outer radii.
#    0.0 <= R1, and normally R1 <= R2.
#
#    integer e(2): the nonnegative exponents of X and Y.
#
#  Output:
#
#    real integral: the integral.
#
  from scipy.special import gamma
  import numpy as np

  if ( np.any ( e < 0 ) ):
    print ( '' )
    print ( 'disk01_monomial_integral(): Fatal error!' )
    print ( '  All exponents must be nonnegative.' )
    raise Exception ( 'disk01_monomial_integral(): Fatal error!' )

  if ( np.any ( ( e % 2 ) == 1 ) ):
    integral = 0.0
    return integral

  integral = 2.0
  for i in range ( 0, 2 ):
    arg = 0.5 * ( e[i] + 1 )
    integral = integral * gamma ( arg )

  arg = 0.5 * ( np.sum ( e + 1 ) )
  integral = integral / gamma ( arg )
#
#  The surface integral is now adjusted to give the volume integral.
#
  s = np.sum ( e ) + 2

  integral = integral * ( r2**s - r1**s ) / s

  return integral

def annulus_sample ( r1, r2, n ):

#*****************************************************************************80
#
## annulus_sample() samples a circular annulus.
#
#  Discussion:
#
#    A circular annulus with center at the origin, inner radius R1 and
#    outer radius R2, is the set of points P so that
#
#      R1^2 <= P(1)^2 + P(2)^2 <= R2^2
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
#  Reference:
#
#    Peter Shirley,
#    Nonuniform Random Point Sets Via Warping,
#    Graphics Gems, Volume III,
#    edited by David Kirk,
#    AP Professional, 1992, 
#    ISBN: 0122861663,
#    LC: T385.G6973.
#
#  Input:
#
#    real R1, R2, the inner and outer radii.
#    0.0 <= R1 <= R2.
#
#    integer N, the number of points to generate.
#
#  Output:
#
#    real P(2,N), sample points.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  if ( r1 < 0.0 ):
    print ( '' )
    print ( 'annulus_sample(): Fatal error!' )
    print ( '  Inner radius R1 < 0.0.' )
    raise Exception ( 'annulus_sample(): Fatal error!' )

  if ( r2 < r1 ):
    print ( '' )
    print ( 'annulus_sample(): Fatal error!' )
    print ( '  Outer radius R1 < R1 = inner radius.' )
    raise Exception ( 'annulus_sample(): Fatal error!' )

  theta = 2.0 * np.pi * rng.random ( size = n )

  v = rng.random ( size = n )

  r = np.sqrt ( ( 1.0 - v[:] ) * r1 * r1 \
    +                   v[:]   * r2 * r2 )

  p = np.zeros ( [ 2, n ] )

  p[0,:] = r[:] * np.cos ( theta[:] )
  p[1,:] = r[:] * np.sin ( theta[:] )

  return p

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
  annulus_integrals_test ( )
  timestamp ( )

