#! /usr/bin/env python3
#
def hexagon_stroud_rule_test ( ):

#*****************************************************************************80
#
## hexagon_stroud_rule_test() tests hexagon_stroud_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hexagon_stroud_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hexagon_stroud().' )

  hexagon_quadrature_test ( hexagon_stroud_rule1, 'Stroud rule #1' )
  hexagon_quadrature_test ( hexagon_stroud_rule2, 'Stroud rule #2' )
  hexagon_quadrature_test ( hexagon_stroud_rule3, 'Stroud rule #3' )
  hexagon_quadrature_test ( hexagon_stroud_rule4, 'Stroud rule #4' )
#
#  Terminate.
#
  print ( '' )
  print ( 'hexagon_stroud_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def comp_next ( n, k, a, more, h, t ):

#*****************************************************************************80
#
## comp_next() computes the compositions of the integer N into K parts.
#
#  Discussion:
#
#    A composition of the integer N into K parts is an ordered sequence
#    of K nonnegative integers which sum to N.  The compositions (1,2,1)
#    and (1,1,2) are considered to be distinct.
#
#    The routine computes one composition on each call until there are no more.
#    For instance, one composition of 6 into 3 parts is
#    3+2+1, another would be 6+0+0.
#
#    On the first call to this routine, set MORE = FALSE.  The routine
#    will compute the first element in the sequence of compositions, and
#    return it, as well as setting MORE = TRUE.  If more compositions
#    are desired, call again, and again.  Each time, the routine will
#    return with a new composition.
#
#    However, when the LAST composition in the sequence is computed 
#    and returned, the routine will reset MORE to FALSE, signaling that
#    the end of the sequence has been reached.
#
#    This routine originally used a SAVE statement to maintain the
#    variables H and T.  I have decided that it is safer
#    to pass these variables as arguments, even though the user should
#    never alter them.  This allows this routine to safely shuffle
#    between several ongoing calculations.
#
#    There are 28 compositions of 6 into three parts.  This routine will
#    produce those compositions in the following order:
#
#     I         A
#     -     ---------
#     1     6   0   0
#     2     5   1   0
#     3     4   2   0
#     4     3   3   0
#     5     2   4   0
#     6     1   5   0
#     7     0   6   0
#     8     5   0   1
#     9     4   1   1
#    10     3   2   1
#    11     2   3   1
#    12     1   4   1
#    13     0   5   1
#    14     4   0   2
#    15     3   1   2
#    16     2   2   2
#    17     1   3   2
#    18     0   4   2
#    19     3   0   3
#    20     2   1   3
#    21     1   2   3
#    22     0   3   3
#    23     2   0   4
#    24     1   1   4
#    25     0   2   4
#    26     1   0   5
#    27     0   1   5
#    28     0   0   6
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 May 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms for Computers and Calculators,
#    Second Edition,
#    Academic Press, 1978,
#    ISBN: 0-12-519260-6,
#    LC: QA164.N54.
#
#  Input:
#
#    integer N, the integer whose compositions are desired.
#
#    integer K, the number of parts in the composition.
#
#    integer A(K), the previous composition.  On the first call,
#    with MORE = FALSE, set A = [].  Thereafter, A should be the 
#    value of A output from the previous call.
#
#    bool MORE.  The input value of MORE on the first
#    call should be FALSE, which tells the program to initialize.
#    On subsequent calls, MORE should be TRUE, or simply the
#    output value of MORE from the previous call.
#
#    integer H, T, two internal parameters needed for the
#    computation.  The user may need to initialize these before the
#    very first call, but these initial values are not important.
#    The user should not alter these parameters once the computation
#    begins.
#
#  Output:
#
#    integer A(K), the next composition.
#
#    bool MORE, will be TRUE unless the composition 
#    that is being returned is the final one in the sequence.
#
#    integer H, T, the updated values of the two internal 
#    variables.
#
  if ( not more ):

    t = n
    h = 0
    a[0] = n
    for i in range ( 1, k ):
      a[i] = 0

  else:
      
    if ( 1 < t ):
      h = 0

    t = a[h]
    a[h] = 0
    a[0] = t - 1
    a[h+1] = a[h+1] + 1
    h = h + 1

  more = ( a[k-1] != n )

  return a, more, h, t

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
#    30 May 2023
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

def hexagon01_monomial_integral ( p, q ):

#*****************************************************************************80
#
## hexagon01_monomial_integral() evaluates a monomial integral in the unit hexagon.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, Q, the indices of the moment.
#
#  Output:
#
#    real VALUE, the integral of x^p y^q.
#
  import numpy as np

  if ( ( p % 2 ) == 1 or ( q % 2 ) == 1 ):
    value = 0.0
  else:
    n = 6
    x, y = hexagon_unit_vertices ( )
    value = moment_unnormalized ( n, x, y, p, q )

  return value

def hexagon_quadrature_test ( rule, rule_name ):

#*****************************************************************************80
#
## hexagon_quadrature_test() tests a hexagon quadrature rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rule, a pointer to the rule function.
#
#    string rule_name, a name for the rule.
#
  import numpy as np

  print ( '' )
  print ( 'hexagon_quadrature_test():' )
  print ( '  Test' + rule_name )

  n, p, x, y, w = rule ( )

  degree_max = p + 2

  print ( '' )
  print ( 'Degree  Exponents      Exact       Estimate    Error' )
  print ( '' )

  dim_num = 2

  for degree in range ( 0, degree_max + 1 ):

    expon = np.zeros ( dim_num, dtype = int )
    more = False
    h = 0
    t = 0

    while ( True ):

      expon, more, h, t = comp_next ( degree, dim_num, expon, more, h, t )

      xy = np.stack ( [ x, y ], axis = 1 )
      v = monomial_value ( expon, xy )
      q = hexagon01_area ( ) * np.dot ( w, v )
      exact = hexagon01_monomial_integral ( expon[0], expon[1] )

      quad_error = np.abs ( exact - q )

      print ( '  %2d  %2d  %2d  %14.6g  %14.6g  %14.6g' \
        % ( degree, expon[0], expon[1], exact, q, quad_error ) )

      if ( not more ):
        break

    print ( '' )

  return

def hexagon_stroud_rule1 ( ):

#*****************************************************************************80
#
## hexagon_stroud_rule1() sets the Stroud hexagon quadrature rule #1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Arthur Stroud,
#    Approximate Calculation of Multiple Integrals,
#    Prentice Hall, 1971.
#
#  Output:
#
#    integer n, the number of points.
#
#    integer p: the precision.
#
#    real x(n), y(n), the points.
#
#    real w(n), the weights.
#
  import numpy as np

  n = 1
  p = 1
  x = np.array ( [ 0.0 ] )
  y = np.array ( [ 0.0 ] )
  w = np.array ( [ 1.0 ] )

  return n, p, x, y, w

def hexagon_stroud_rule2 ( ):

#*****************************************************************************80
#
## hexagon_stroud_rule2() sets the Stroud hexagon quadrature rule #2.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Arthur Stroud,
#    Approximate Calculation of Multiple Integrals,
#    Prentice Hall, 1971.
#
#  Output:
#
#    integer n, the number of points.
#
#    integer p: the precision.
#
#    real x(n), y(n), the points.
#
#    real w(n), the weights.
#
  import numpy as np

  a = np.sqrt ( 5.0 / 12.0 )
  b = 1.0 / 4.0
  z = 0.0

  n = 4
  p = 3
  x = np.array ( [  a, -a,  z,  z ] )
  y = np.array ( [  z,  z,  a, -a ] )
  w = np.array ( [  b,  b,  b,  b ] )

  return n, p, x, y, w

def hexagon_stroud_rule3 ( ):

#*****************************************************************************80
#
## hexagon_stroud_rule3() sets the Stroud hexagon quadrature rule #3.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Arthur Stroud,
#    Approximate Calculation of Multiple Integrals,
#    Prentice Hall, 1971.
#
#  Output:
#
#    integer n, the number of points.
#
#    integer p: the precision.
#
#    real x(n), y(n), the points.
#
#    real w(n), the weights.
#
  import numpy as np

  a = np.sqrt ( 3.0 ) / 2.0
  b =  0.5
  c =  1.0
  d =  5.0 / 72.0
  e = 42.0 / 72.0
  z =  0.0

  n = 7
  p = 3
  x = np.array ( [  z,  c, -c,  b, -b,  b, -b ] )
  y = np.array ( [  z,  z,  z,  a,  a, -a, -a ] )
  w = np.array ( [  e,  d,  d,  d,  d,  d,  d ] )

  return n, p, x, y, w

def hexagon_stroud_rule4 ( ):

#*****************************************************************************80
#
## hexagon_stroud_rule4() sets the Stroud hexagon quadrature rule #4.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Arthur Stroud,
#    Approximate Calculation of Multiple Integrals,
#    Prentice Hall, 1971.
#
#  Output:
#
#    integer n, the number of points.
#
#    integer p: the precision.
#
#    real x(n), y(n), the points.
#
#    real w(n), the weights.
#
  import numpy as np

  a = np.sqrt ( 14.0 ) / 5.0
  b = np.sqrt ( 14.0 ) / 10.0
  c = np.sqrt ( 42.0 ) / 10.0
  d = 125.0 / 1008.0
  e = 258.0 / 1008.0
  z = 0.0

  n = 7
  p = 5
  x = np.array ( [ z,  a, -a,  b, -b,  b, -b ] )
  y = np.array ( [ z,  z,  z,  c,  c, -c, -c ] )
  w = np.array ( [ e,  d,  d,  d,  d,  d,  d ] )

  return n, p, x, y, w

def hexagon_unit_vertices ( ):

#*****************************************************************************80
#
## hexagon_unit_vertices() returns the vertices of a unit hexagon.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real x(6), y(6): the coordinates of the vertices.
#
  import numpy as np

  a = np.sqrt ( 3.0 ) / 2.0
  x = np.array ( [ 1.0, 0.5, -0.5, -1.0, -0.5,  0.5 ] )
  y = np.array ( [ 0.0, a,    a,    0.0, -a,   -a ] )

  return x, y

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
#    30 May 2023
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

  nu_pq = nu_pq / ( p + q + 2 ) / ( p + q + 1 ) / comb ( p + q, p )

  return nu_pq

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
#    15 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer E(D): the exponents.
#
#    real X(N,D): the point coordinates.
#
#  Output:
#
#    real V(N): the monomial values.
#
  import numpy as np

  n, d = x.shape

  v = np.ones ( n )

  for j in range ( 0, d ):
    if ( 0 != e[j] ):
      v[0:n] = v[0:n] * x[0:n,j] ** e[j]

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
  hexagon_stroud_rule_test ( )
  timestamp ( )


