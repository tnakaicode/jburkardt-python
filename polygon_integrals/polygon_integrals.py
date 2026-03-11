#! /usr/bin/env python3
#
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

def moment_central_test ( ):

#*****************************************************************************80
#
## moment_central_test() tests moment_central().
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
  import numpy as np

  n = 4

  mu_exact = np.array ( [ \
    1.0, 0.0, 0.0, 5.666666666666667, 2.0, 2.666666666666667 ] )

  x = np.array ( [ 2.0, 10.0, 8.0, 0.0 ] )
  y = np.array ( [ 0.0,  4.0, 8.0, 4.0 ] )

  print ( '' )
  print ( 'moment_central_test():' )
  print ( '  moment_central() computes central moments of a polygon.' )
  print ( '  Here, we test the code using a rectangle with known moments.' )
  print ( '' )
  print ( '   P   Q             Mu(P,Q)' )
  print ( '            Computed         Exact' )
  print ( '' )
  k = 0
  for s in range ( 0, 3 ):
    for p in range ( s, -1, -1 ):
      q = s - p
      mu_pq = moment_central ( n, x, y, p, q )
      print ( '  %2d  %2d  %14.6g  %14.6g' % ( p, q, mu_pq, mu_exact[k] ) )
      k = k + 1

  return

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
  nu_pq = moment ( n, x, y, p, q )
  nu_00 = moment ( n, x, y, 0, 0 )

  alpha_pq = nu_pq / nu_00

  return alpha_pq

def moment_normalized_test ( ):

#*****************************************************************************80
#
## moment_normalized_test() tests moment_normalized().
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
  import numpy as np

  n = 4

  alpha_exact = np.array ( [ \
    1.0, 5.0, 4.0, 30.66666666666667, 22.0, 18.66666666666666 ] )

  x = np.array ( [ 2.0, 10.0, 8.0, 0.0 ] )
  y = np.array ( [ 0.0,  4.0, 8.0, 4.0 ] )

  print ( '' )
  print ( 'moment_normalized_test():' )
  print ( '  moment_normalized() computes normalized moments of a polygon.' )
  print ( '  Here, we test the code using a rectangle with known moments.' )
  print ( '' )
  print ( '   P   Q          Alpha(P,Q)' )
  print ( '            Computed         Exact' )
  print ( '' )
  k = 0
  for s in range ( 0, 3 ):
    for p in range ( s, -1, -1 ):
      q = s - p
      alpha_pq = moment_normalized ( n, x, y, p, q )
      print ( '  %2d  %2d  %14.6g  %14.6g' % ( p, q, alpha_pq, alpha_exact[k] ) )
      k = k + 1

  return

def moment ( n, x, y, p, q ):

#*****************************************************************************80
#
## moment() computes an unnormalized moment of a polygon.
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

def moment_test ( ):

#*****************************************************************************80
#
## moment_test() tests moment().
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
  import numpy as np

  n = 4

  nu_exact = np.array ( [ \
    40.0, 200.0, 160.0, 1226.66666666666667, 880.0, 746.66666666666666 ] )

  x = np.array ( [ 2.0, 10.0, 8.0, 0.0 ] )
  y = np.array ( [ 0.0,  4.0, 8.0, 4.0 ] )

  print ( '' )
  print ( 'moment_test():' )
  print ( '  moment() computes moments of a polygon.' )
  print ( '  Here, we test the code using a rectangle with known moments.' )
  print ( '' )
  print ( '   P   Q             Nu(P,Q)' )
  print ( '            Computed         Exact' )
  print ( '' )
  k = 0
  for s in range ( 0, 3 ):
    for p in range ( s, -1, -1 ):
      q = s - p
      nu_pq = moment ( n, x, y, p, q )
      print ( '  %2d  %2d  %14.6g  %14.6g' % ( p, q, nu_pq, nu_exact[k] ) )
      k = k + 1

  return

def polygon_integrals_test ( ):

#*****************************************************************************80
#
## polygon_integrals_test() tests polygon_integrals().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'polygon_integrals_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polygon_integrals().' )
#
#  Utilities:
#
  r8_mop_test ( )
#
#  Library functions:
#
  moment_test ( )
  moment_central_test ( )
  moment_normalized_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polygon_integrals_test():' )
  print ( '  Normal end of execution.' )
  return

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

def r8_mop_test ( ):

#*****************************************************************************80
#
## r8_mop_test() tests r8_mop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'r8_mop_test():' )
  print ( '  r8_mop() evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  r8_mop(I4)' )
  print ( '' )

  i4_min = -100
  i4_max = +100

  for test in range ( 0, 10 ):
    i4 = rng.integers ( low = -100, high = +100, endpoint = True )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )

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
  polygon_integrals_test ( )
  timestamp ( )

