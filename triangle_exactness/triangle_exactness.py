#! /usr/bin/env python3
#
def triangle_exactness_test ( ):

#*****************************************************************************80
#
## triangle_exactness_test() tests triangle_exactness().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'triangle_exactness_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test triangle_exactness().' )

  triangle_exactness ( 'strang5', 5 )
#
#  Terminate.
#
  print ( '' )
  print ( 'triangle_exactness_test():' )
  print ( '  Normal end of execution.' )

  return

def triangle_exactness ( quad_filename, degree_max ):

#*****************************************************************************80
#
## triangle_exactness() investigates the exactness of a quadrature rule.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character QUAD_FILENAME, the common filename prefix for the quadrature files.
#
#    integer DEGREE_MAX, the maximum degree to check.
#
  import numpy as np

  print ( '' )
  print ( 'triangle_exactness():' )
  print ( '  Investigate the polynomial exactness of a quadrature' )
  print ( '  rule for the triangle by integrating all monomials' )
  print ( '  up to a given degree.' )
  print ( '  The rule will be adjusted to the unit triangle.' )
#
#  Create the names of:
#    the quadrature X file
#    the quadrature W file
#    the quadrature R file
#
  quad_x_filename = quad_filename + '_x.txt'
  quad_w_filename = quad_filename + '_w.txt'
  quad_r_filename = quad_filename + '_r.txt'
#
#  Summarize the input.
#
  print ( '' )
  print ( 'User input:' )
  print ( '  Quadrature rule X file = "' + quad_x_filename + '".' )
  print ( '  Quadrature rule W file = "' + quad_w_filename + '".' )
  print ( '  Quadrature rule R file = "' + quad_r_filename + '".' )
  print ( '  Maximum total degree to check = ', degree_max )
#
#  Read the X file.
#
  x = np.loadtxt ( quad_x_filename )
  point_num = x.shape[0]
#
#  Read the W file.
#
  w = np.loadtxt ( quad_w_filename )
#
#  Read the R file.
#
  r = np.loadtxt ( quad_r_filename )
#
#  Rescale the weights.
#
  area = triangle_area ( r )
  w = 0.5 * w / area
#
#  Translate the abscissas.
#
  x_ref = triangle_order3_physical_to_reference ( r, point_num, x )
#
#  Explore the monomials.
#
  print ( '' )
  print ( '  Degree  Exponents  Error' )
  print ( '' )

  dim_num = 2
  expon = np.zeros ( dim_num, dtype = int )

  for degree in range ( 0, degree_max + 1 ):

    more = False
    h = 0
    t = 0

    while ( True ):

      expon, more, h, t = comp_next ( degree, dim_num, expon, more, h, t )

      quad_error = triangle01_monomial_quadrature ( dim_num, expon, \
        point_num, x_ref, w )

      print ( '  %2d  (%2d,%2d)  %24.16f' \
        % ( degree, expon[0], expon[1], quad_error ) )

      if ( not more ):
        break

    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'triangle_exactness():' )
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

def monomial_value ( d, n, e, x ):

#*****************************************************************************80
#
## monomial_value() evaluates a monomial.
#
#  Discussion:
#
#    This routine evaluates a monomial of the form
#
#      product ( 1 <= i <= d ) x(i)^e(i)
#
#    The combination 0.0^0, if encountered, is treated as 1.0.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 October 2021
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer D, the spatial dimension.
#
#    integer N, the number of evaluation points.
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

  v = np.ones ( n )

  for j in range ( 0, d ):
    if ( 0 != e[j] ):
      for i in range ( 0, n ):
        if ( x[i,j] == 0.0 ):
          v[i] = 0.0
        elif ( e[j] != 0 ):
          v[i] = v[i] * x[i,j] ** e[j]

  return v

def triangle_area ( t ):

#*****************************************************************************80
#
## triangle_area() computes the area of a triangle in 2D.
#
#  Discussion:
#
#    If the triangle's vertices are given in counterclockwise order,
#    the area will be positive.  If the triangle's vertices are given
#    in clockwise order, the area will be negative!
#
#    An earlier version of this routine always returned the absolute
#    value of the computed area.  I am convinced now that that is
#    a less useful result!  For instance, by returning the signed 
#    area of a triangle, it is possible to easily compute the area 
#    of a nonconvex polygon as the sum of the (possibly negative) 
#    areas of triangles formed by node 1 and successive pairs of vertices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(3,2), the triangle vertices.
#
#  Output:
#
#    real AREA, the area of the triangle.
#
  area = 0.5 * ( \
      t[0,0] * ( t[1,1] - t[2,1] ) \
    + t[1,0] * ( t[2,1] - t[0,1] ) \
    + t[2,0] * ( t[0,1] - t[1,1] ) )

  return area

def triangle_order3_physical_to_reference ( t, n, phy ):

#*****************************************************************************80
#
## triangle_order3_physical_to_reference() maps a physical point to a reference point.
#
#  Discussion:
#
#    Given the vertices of an order 3 physical triangle and a point
#    (X,Y) in the physical triangle, the routine computes the value
#    of the corresponding image point (XSI,ETA) in reference space.
#
#    Note that this routine may also be appropriate for an order 6
#    triangle, if the mapping between reference and physical space
#    is linear.  This implies, in particular, that the sides of the
#    image triangle are straight and that the "midside" nodes in the
#    physical triangle are halfway along the sides of
#    the physical triangle.
#
#  Reference Element T3:
#
#    |
#    1  3
#    |  |\
#    |  | \
#    S  |  \
#    |  |   \
#    |  |    \
#    0  1-----2
#    |
#    +--0--R--1-->
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 December 2006
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(3,2), the X and Y coordinates
#    of the vertices.  The vertices are assumed to be the images of
#    (0,0), (1,0) and (0,1) respectively.
#
#    integer N, the number of points to transform.
#
#    real PHY(N,2), the coordinates of points in the physical space.
#
#  Output:
#
#    real REF(N,2), the coordinates of the corresponding
#    points in the reference space.
#
  import numpy as np

  ref = np.zeros ( [ n, 2 ] )

  ref[0:n,0] = ( ( t[2,1] - t[0,1] ) * ( phy[0:n,0] - t[0,0] )   \
               - ( t[2,0] - t[0,0] ) * ( phy[0:n,1] - t[0,1] ) ) \
             / ( ( t[2,1] - t[0,1] ) * ( t[1,0]     - t[0,0] )   \
               - ( t[2,0] - t[0,0] ) * ( t[1,1]     - t[0,1] ) )

  ref[0:n,1] = ( ( t[1,0] - t[0,0] ) * ( phy[0:n,1] - t[0,1] )   \
               - ( t[1,1] - t[0,1] ) * ( phy[0:n,0] - t[0,0] ) ) \
             / ( ( t[2,1] - t[0,1] ) * ( t[1,0]     - t[0,0] )   \
               - ( t[2,0] - t[0,0] ) * ( t[1,1]     - t[0,1] ) )

  return ref

def triangle_unit_monomial_integral ( expon ):

#*****************************************************************************80
#
## triangle_unit_monomial_integral(): integral of a monomial over unit triangle.
#
#  Discussion:
#
#    This routine evaluates a monomial of the form
#
#      product ( 1 <= dim <= dim_num ) x(dim)^expon(dim)
#
#    where the exponents are nonnegative integers.  Note that
#    if the combination 0^0 is encountered, it should be treated
#    as 1.
#
#    Integral ( over unit triangle ) x^m y^n dx dy = m! * n! / ( m + n + 2 )!
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 July 2007
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIM_NUM, the spatial dimension.
#
#    integer EXPON(DIM_NUM), the exponents.
#
#  Output:
#
#    real VALUE, the value of the integral of the monomial.
#

#
#  The first computation ends with VALUE = 1.0
#
  value = 1.0

  k = 0

  for i in range ( 1, expon[0] + 1 ):
    k = k + 1
#   value = value * i / k

  for i in range ( 1, expon[1] + 1 ):
    k = k + 1
    value = value * i / k

  k = k + 1
  value = value / k

  k = k + 1
  value = value / k

  return value

def triangle01_monomial_quadrature ( dim_num, expon, point_num, x, weight ):

#*****************************************************************************80
#
## triangle01_monomial_quadrature(): quadrature of monomial in unit triangle.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIM_NUM, the spatial dimension.
#
#    integer EXPON(DIM_NUM), the exponents.
#
#    integer POINT_NUM, the number of points in the rule.
#
#    real X(DIM_NUM,POINT_NUM), the quadrature points.
#
#    real WEIGHT(POINT_NUM), the quadrature weights.
#
#  Output:
#
#    real QUAD_ERROR, the quadrature error.
#
  import numpy as np
#
#  Get the exact value of the integral of the unscaled monomial.
#
  scale = triangle_unit_monomial_integral ( expon )
#
#  Evaluate the monomial at the quadrature points.
#
  value = monomial_value ( dim_num, point_num, expon, x )
#
#  Compute the weighted sum and divide by the exact value.
#
  area = 0.5
  quad = area * np.dot ( weight, value ) / scale
#
#  Error:
#
  exact = 1.0
  quad_error = np.abs ( quad - exact )

  return quad_error

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
  triangle_exactness_test ( )
  timestamp ( )


