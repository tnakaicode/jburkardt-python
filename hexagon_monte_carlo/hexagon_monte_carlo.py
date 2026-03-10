#! /usr/bin/env python3
#
def hexagon01_area ( ):

#*****************************************************************************80
#
## hexagon01_area() returns the area of a unit regular hexagon in 2D.
#
#  Integration region:
#
#    The definition is given in terms of THETA, the angle in degrees of the
#    vector (X,Y).  The following six conditions apply, respectively,
#    between the bracketing values of THETA of 0, 60, 120, 180, 240,
#    300, and 360.
#
#                              0 <= Y <= - SQRT(3) * X + SQRT(3)
#                              0 <= Y <=                 SQRT(3)/2
#                              0 <= Y <=   SQRT(3) * X + SQRT(3)
#      - SQRT(3) * X - SQRT(3)   <= Y <= 0
#                    - SQRT(3)/2 <= Y <= 0
#        SQRT(3) * X - SQRT(3)   <= Y <= 0
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real value, the area of the hexagon.
#
  import numpy as np

  value = 3.0 * np.sqrt ( 3.0 ) / 2.0

  return value

def hexagon01_integral ( p, q ):

#*****************************************************************************80
#
## hexagon01_integral() evaluates a monomial integral in the unit hexagon.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#
#    real X(N), Y(N), the vertex coordinates.
#
#    integer P, Q, the indices of the moment.
#
#  Output:
#
#    real VALUE, the integral of x^p y^q.
#
  import numpy as np

  if ( ( ( p % 2 ) == 1 ) or ( ( q % 2 ) == 1 ) ):
    value = 0.0
  else:
    n = 6
    a = np.sqrt ( 3.0 ) / 2.0
    x = np.array ( [ 1.0, 0.5, -0.5, -1.0, -0.5,  0.5 ] )
    y = np.array ( [ 0.0, a,    a,    0.0, -a,   -a ] )
    value = moment_polygon ( n, x, y, p, q )

  return value

def hexagon01_monte_carlo ( n, f ):

#*****************************************************************************80
#
## hexagon01_monte_carlo(): Monte Carlo estimate of integral over unit hexagon.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n, the number of sample points.
#
#    pointer f, the name of the function.
#
#  Output:
#
#    real result, the approximate integrals.
#
  import numpy as np

  area = hexagon01_area ( )

  x, y = hexagon01_sample ( n )

  result = ( area / n ) * np.sum ( f ( x, y ) )
  
  return result

def hexagon01_monte_carlo_test01 ( ):

#*****************************************************************************80
#
## hexagon01_monte_carlo_test01() requests integrals over the unit hexagon.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  area = hexagon01_area ( )

  print ( '' )
  print ( 'hexagon01_monte_carlo_test01():' )
  print ( '  hexagon01_monte_carlo() estimates' )
  print ( '  monomial integrals x^p y^q over the unit hexagon.' )
  print ( '' )
  print ( '   N  P   Q             Nu(P,Q)' )
  for s in range ( 0, 11 ):
    for p in range ( s, -1, -1 ):

      q = s - p

      if ( ( ( p % 2 ) == 0 ) and ( ( q % 2 ) == 0 ) ):

        print ( '' )
        n = 1
        for log2n in range ( 0, 16 ):
          x, y = hexagon01_sample ( n )
          v = monomial_value_2d ( n, p, q, x, y )
          nu_pq = ( area / n ) * np.sum ( v )
          print ( '  %6d  %2d  %2d  %14.6g' % ( n, p, q, nu_pq ) )
          n = n * 2

        nu_pq = hexagon01_integral ( p, q )
        print ( '   Exact  %2d  %2d  %14.6g' % ( p, q, nu_pq ) )

  return

def hexagon01_sample ( n ):

#*****************************************************************************80
#
## hexagon01_sample() samples uniformly from the regular unit hexagon.
#
#  Discussion:
#
#    The unit hexagon has center (0,0) and "radius" 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of points.
#
#  Output:
#
#    real X(N), Y(N), the points.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )
#
#  Set basis vectors for each rhombus.
#
  vx = np.array ( [ -1.0, 0.5,               0.5,              -1.0 ] )
  vy = np.array ( [  0.0, np.sqrt(3.0)/2.0, -np.sqrt(3.0)/2.0,  0.0 ] )
#
#  Assign each point randomly to one of the rhombuses.
#
  rh = rng.integers ( low = 0, high = 2, size = n, endpoint = True )
#
#  You don't want to know why I use this as a substitute for MATLAB's find().
#
  i = np.flatnonzero ( rh == 0 )
  j = np.flatnonzero ( rh == 1 )
  k = np.flatnonzero ( rh == 2 )
#
#  Set barycentric coordinates of each point in its rhombus.
#
  xy = rng.random ( [ 2, n ] )
#
#  Convert to physical coordinates.
#
  x = np.zeros ( n )
  x[i] = np.dot ( vx[0:2], xy[:,i] )
  x[j] = np.dot ( vx[1:3], xy[:,j] )
  x[k] = np.dot ( vx[2:4], xy[:,k] )

  y = np.zeros ( n )
  y[i] = np.dot ( vy[0:2], xy[:,i] )
  y[j] = np.dot ( vy[1:3], xy[:,j] )
  y[k] = np.dot ( vy[2:4], xy[:,k] )

  return x, y

def hexagon_monte_carlo_test ( ):

#*****************************************************************************80
#
## hexagon_monte_carlo_test() tests hexagon_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hexagon_monte_carlo_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hexagon_monte_carlo().' )

  hexagon01_monte_carlo_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hexagon_monte_carlo_test():' )
  print ( '  Normal end of execution.' )

  return

def moment_polygon ( n, x, y, p, q ):

#*****************************************************************************80
#
## moment_polygon() computes an unnormalized moment of a polygon.
#
#  Discussion:
#
#    Nu(P,Q) = Integral ( x, y in polygon ) x^p y^q dx dy
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carsten Steger,
#    On the calculation of arbitrary moments of polygons,
#    Technical Report FGBV-96-05,
#    Forschungsgruppe Bildverstehen, Informatik IX,
#    Technische Universitaet Muenchen, October 1996.
#
#  Input:
#
#    integer N, the number of vertices of the polygon.
#
#    real X(N), Y(N), the vertex coordinates.
#
#    integer P, Q, the indices of the moment.
#
#  Output:
#
#    real NU_PQ, the unnormalized moment Nu(P,Q).
#
  from scipy.special import comb

  nu_pq = 0.0

  xj = x[n-1]
  yj = y[n-1]

  for i in range ( 0, n ):

    xi = x[i]
    yi = y[i]

    s_pq = 0.0

    for k in range ( 0, p + 1 ):
      for l in range ( 0, q + 1 ):
        s_pq = s_pq \
          + comb ( k + l, l ) * comb ( p + q - k - l, q - l ) \
          * xi ** k * xj ** ( p - k ) \
          * yi ** l * yj ** ( q - l )

    nu_pq = nu_pq + ( xj * yi - xi * yj ) * s_pq

    xj = xi
    yj = yi

  nu_pq = nu_pq / float ( p + q + 2 ) / float ( p + q + 1 ) \
    / comb ( p + q, p )

  return nu_pq

def monomial_value_2d ( n, ex, ey, x, y ):

#*****************************************************************************80
#
## monomial_value_2d() evaluates a monomial in x and y.
#
#  Discussion:
#
#    This routine evaluates a monomial of the form
#
#      x^ex * y^ey
#
#    The combination 0.0^0 is encountered is treated as 1.0.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 November 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of evaluation points.
#
#    integer EX, EY, the exponents.
#
#    real X(N), Y(N), the point coordinates.
#
#  Output:
#
#    real V(N), the monomial values.
#
  import numpy as np

  v = np.ones ( n )

  if ( 0 != ex ):
    v = v * x ** ex

  if ( 0 != ey ):
    v = v * y ** ey

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
#    21 August 2019
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
  hexagon_monte_carlo_test ( )
  timestamp ( )

