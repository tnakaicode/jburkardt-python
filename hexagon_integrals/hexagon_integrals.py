#! /usr/bin/env python3
#
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
#    05 November 2022
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
    value = moment_unnormalized ( n, x, y, p, q )

  return value

def hexagon_integrals_test ( ):

#*****************************************************************************80
#
## hexagon_integrals_test() tests hexagon_integrals().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'hexagon_integrals_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  hexagon01_integral() computes' )
  print ( '  monomial integrals x^p y^q over the unit hexagon.' )
  print ( '' )
  print ( '   P   Q             Nu(P,Q)' )
  print ( '' )
  k = 0
  for s in range ( 0, 11 ):
    for p in range ( s, -1, -1 ):
      q = s - p
      if ( ( ( p % 2 ) == 0 ) and ( ( q % 2 ) == 0 ) ):
        k = k + 1
        nu_pq = hexagon01_integral ( p, q )
        print ( '  %2d  %2d  %14.6g' % ( p, q, nu_pq ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'hexagon_integrals_test():' )
  print ( '  Normal end of execution.' )

  return

def moment_central ( n, x, y, p, q ):

#*****************************************************************************80
#
## moment_central() computes central moments of a polygon.
#
#  Discussion:
#
#    The central moment Mu(P,Q) is defined by
#
#      Mu(P,Q) = Integral ( polygon ) (x-Alpha(1,0))^p (y-Alpha(0,1))^q dx dy
#              / Area ( polygon )
#
#    where
#
#      Alpha(1,0) = Integral ( polygon ) x dx dy / Area ( polygon )
#      Alpha(0,1) = Integral ( polygon ) y dx dy / Area ( polygon )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
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
#    real MU_PQ, the uncentral moment Mu(P,Q).
#
  from scipy.special import comb

  alpha_10 = moment_normalized ( n, x, y, 1, 0 )
  alpha_01 = moment_normalized ( n, x, y, 0, 1 )

  mu_pq = 0.0

  for i in range ( 0, p + 1 ):
    for j in range ( 0, q + 1 ):

      alpha_ij = moment_normalized ( n, x, y, i, j )

      mu_pq = mu_pq + r8_mop ( p + q - i - j ) \
        * comb ( p, i ) * comb ( q, j ) \
        * alpha_10 ** ( p - i ) * alpha_01 ** ( q - j ) * alpha_ij

  return mu_pq

def moment_normalized ( n, x, y, p, q ):

#*****************************************************************************80
#
## moment_normalized() computes a normalized moment of a polygon.
#
#  Discussion:
#
#    Alpha(P,Q) = Integral ( x, y in polygon ) x^p y^q dx dy / Area ( polygon )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
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
#    real ALPHA_PQ, the normalized moment Alpha(P,Q).
#
  nu_pq = moment_unnormalized ( n, x, y, p, q )
  nu_00 = moment_unnormalized ( n, x, y, 0, 0 )

  alpha_pq = nu_pq / nu_00

  return alpha_pq

def moment_unnormalized ( n, x, y, p, q ):

#*****************************************************************************80
#
## moment_unnormalized() computes an unnormalized moment of a polygon.
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
#    23 June 2015
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

def r8_mop ( i ):

#*****************************************************************************80
#
## r8_mop() returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the power of -1.
#
#  Output:
#
#    real VALUE, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

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
  hexagon_integrals_test ( )
  timestamp ( )

