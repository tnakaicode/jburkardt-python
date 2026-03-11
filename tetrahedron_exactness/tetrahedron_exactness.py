#! /usr/bin/env python3
#
def tetrahedron_exactness_test ( ):

#*****************************************************************************80
#
## tetrahedron_exactness_test() tests tetrahedron_exactness().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'tetrahedron_exactness_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test tetrahedron_exactness().' )

  tetrahedron_exactness ( 'keast7', 7 )
#
#  Terminate.
#
  print ( '' )
  print ( 'tetrahedron_exactness_test():' )
  print ( '  Normal end of execution.' )

  return

def tetrahedron_exactness ( quad_filename, degree_max ):

#*****************************************************************************80
#
## tetrahedron_exactness() investigates the exactness of a tetrahedron quadrature.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    character QUAD_FILENAME, the common filename prefix for the quadrature rule.
#
#    integer DEGREE_MAX, the maximum degree to check.
#
  import numpy as np

  print ( '' )
  print ( 'tetrahedron_exactness():' )
  print ( '  Investigate the polynomial exactness of a quadrature' )
  print ( '  rule for the tetrahedron by integrating all monomials' )
  print ( '  of a given degree.' )
  print ( '' )
  print ( '  The rule will be adjusted to the unit tetrahedron.' )
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
  print ( 'tetrahedron_exactness: User input:' )
  print ( '  Quadrature rule X file = "' + quad_x_filename + '".' )
  print ( '  Quadrature rule W file = "' + quad_w_filename + '".' )
  print ( '  Quadrature rule R file = "' + quad_r_filename + '".' )
  print ( '  Maximum total degree to check =', degree_max )
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
#  Rescale the weights for the unit tetrahedron.
#
  volume = tetrahedron_volume ( r )
  w = ( 1.0 / 6.0 ) * w / volume
#
#  Translate the abscissas to the unit tetrahedron.
#
  x_ref = tetrahedron_physical_to_reference ( r, point_num, x )
#
#  Explore the monomials.
#
  print ( '' )
  print ( '      Degree  Error' )
  print ( '' )

  dim_num = 3
  expon = np.zeros ( 3, dtype = int )

  for degree in range ( 0, degree_max + 1 ):

    more = False
    h = 0
    t = 0

    while ( True ):

      expon, more, h, t = comp_next ( degree, dim_num, expon, more, h, t )

      quad_error = tetrahedron_unit_monomial_quadrature ( dim_num, expon, \
        point_num, x_ref, w )

      print ( '  %2d    %24.16f %2d  %2d  %2d' \
        % ( degree, quad_error, expon[0], expon[1], expon[2] ) )

      if ( not more ):
        break

    print ( '' )

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
        v[i] = v[i] * x[i,j] ** e[j]

  return v

def tetrahedron_unit_monomial_integral ( expon ):

#*****************************************************************************80
#
## tetrahedron_unit_monomial_integral() integrates a monomial over the unit tetrahedron.
#
#  Discussion:
#
#    This routine integrates a monomial of the form
#
#      product ( 1 <= dim <= 3 ) x(dim)^expon(dim)
#
#    where the exponents are nonnegative integers.  Note that
#    if the combination 0^0 is encountered, it should be treated
#    as 1.
#
#    Integral ( over unit tetrahedron ) x^l y^m z^n dx dy =
#    l! * m! * n! / ( m + n + 3 )!
#
#    The integration region is defined as:
#
#      0 <= X
#      0 <= Y
#      0 <= Z
#      0 <= X + Y + Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON(3), the exponents.
#
#  Output:
#
#    real VALUE, the integral of the monomial.
#

#
#  The first computation ends with VALUE = 1.0
#
  value = 1.0
#
#  The first loop simply calculates 1, so we short circuit it.
#
# k = 0
#
# for i = 1 : expon(1)
#   k = k + 1
#   value = value * i / k
# end

  k = expon[0]
  for i in range ( 0, expon[1] ):
    k = k + 1
    value = value * ( i + 1 ) / k

  for i in range ( 0, expon[2] ):
    k = k + 1
    value = value * ( i + 1 ) / k

  k = k + 1
  value = value / k

  k = k + 1
  value = value / k

  k = k + 1
  value = value / k

  return value

def tetrahedron_unit_monomial_quadrature ( dim_num, expon, point_num, x, weight ):

#*****************************************************************************80
#
## tetrahedron_unit_monomial_quadrature() applies quadrature to a monomial in a tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 May 2023
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
  scale = tetrahedron_unit_monomial_integral ( expon )
#
#  Evaluate the monomial at the quadrature points.
#
  value = monomial_value ( dim_num, point_num, expon, x )
#
#  Compute the weighted sum and divide by the exact value.
#
  volume = 1.0 / 6.0
  quad = volume * np.dot ( weight, value ) / scale
#
#  Error:
#
  exact = 1.0
  quad_error = abs ( quad - exact )

  return quad_error

def tetrahedron_physical_to_reference ( t, n, phy ):

#*****************************************************************************80
#
## tetrahedron_physical_to_reference() maps physical points to reference points.
#
#  Discussion:
#
#    Given the vertices of an order 4 physical tetrahedron and a point
#    (X,Y,Z) in the physical tetrahedron, the routine computes the value
#    of the corresponding image point (R,S,T) in reference space.
#
#    This routine may be appropriate for an order 10 tetrahedron,
#    if the mapping between reference and physical space is linear.
#    This implies, in particular, that the edges of the image tetrahedron
#    are straight, the faces are flat, and the "midside" nodes in the
#    physical tetrahedron are halfway along the sides of the physical
#    tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2006
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(4,3), the X, Y, Z coordinates of the vertices.  
#
#    integer N, the number of points to transform.
#
#    real PHY(N,3), the coordinates of physical points
#    to be transformed.
#
#  Output:
#
#    real REF[N,3], the coordinates of the corresponding reference points.
#
  import numpy as np
#
#  Set up the matrix.
#
  A = np.zeros ( [ 3, 3 ] )

  A[0,0:3] = t[1,0:3] - t[0,0:3]
  A[1,0:3] = t[2,0:3] - t[0,0:3]
  A[2,0:3] = t[3,0:3] - t[0,0:3]
#
#  If the determinant is zero, bail out.
#
  if ( np.linalg.det ( A ) == 0.0 ):
    raise Exception ( 'Singular matrix.' )
    return []
#
#  Compute the right hand side.
#
  rhs = np.zeros ( [ n, 3 ] )

  rhs[0:n,0] = phy[0:n,0] - t[0,0]
  rhs[0:n,1] = phy[0:n,1] - t[0,1]
  rhs[0:n,2] = phy[0:n,2] - t[0,2]
#
#  Compute the solution.
#
  ref = np.linalg.solve ( A, rhs.T )
  ref = ref.T

  return ref

def tetrahedron_volume ( tetra ):

#*****************************************************************************80
#
## tetrahedron_volume() computes the volume of a tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real tetra(4,3): the vertices of the tetrahedron.
#
#  Output:
#
#    real volume: the volume of the tetrahedron.
#
  import numpy as np

  a = np.zeros ( [ 4, 4 ] )
  a[0:4,0:3] = tetra[0:4,0:3]
  a[0:4,3] = 1.0

  volume = np.abs ( np.linalg.det ( a ) ) / 6.0

  return volume

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
  tetrahedron_exactness_test ( )
  timestamp ( )

