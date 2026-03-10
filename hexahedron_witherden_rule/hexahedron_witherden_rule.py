#! /usr/bin/env python3
#
def hexahedron_witherden_rule_test ( ):

#*****************************************************************************80
#
## hexahedron_witherden_rule_test() tests hexahedron_witherden_rule().
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    17 July 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'hexahedron_witherden_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hexahedron_witherden_rule().' )

  p = 5
  hexahedron_witherden_rule_test01 ( p )

  p = 5
  hexahedron_witherden_rule_test02 ( p )

  p_lo = 0
  p_hi = 11
  hexahedron_witherden_rule_test03 ( p_lo, p_hi )
#
#  Terminate.
#
  print ( '' )
  print ( 'hexahedron_witherden_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def hexahedron_witherden_rule_test01 ( p ):

#*****************************************************************************80
#
## hexahedron_witherden_rule_test01() prints a rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    25 May 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'hexahedron_witherden_rule_test01():' )
  print ( '  Quadrature rule for the unit hexahedron,' )
  print ( '  Precision p =', p )
#
#  Retrieve the rule.
#
  n, x, y, z, w = hexahedron_witherden_rule ( p )
#
#  Print the rule.
#
  print ( '' )
  print ( '     I      W          X           Y           Z' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %10.6g  %10.6g  %10.6g  %10.6g' \
      % ( i, w[i], x[i], y[i], z[i] ) )
#
#  Verify that the weights sum to 1.
#
  w_sum = np.sum ( w )

  print ( '' )
  print ( '  Weight Sum ', w_sum )

  return

def hexahedron_witherden_rule_test02 ( p ):

#*****************************************************************************80
#
## hexahedron_witherden_rule_test02() tests a rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    21 May 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'hexahedron_witherden_rule_test02():' )
  print ( '  Test the precision of a quadrature rule for the unit hexahedron.' )

  dim_num = 3
#
#  Retrieve the rule.
#
  n, x, y, z, w = hexahedron_witherden_rule ( p )
#
#  Pack the x, y, z vectors as rows of an array.
#
  xyz = np.transpose ( np.array ( [ x, y, z ] ) )

  print ( '' )
  print ( '  Stated precision of rule    = ', p )
  print ( '  Number of quadrature points = ', n )
  print ( '' )
  print ( '  Degree  Maximum error' )
  print ( '' )

  for degree in range ( 0, p + 3 ):

    expon = np.zeros ( dim_num, dtype = int )
    more = False
    h = 0
    t = 0
    max_error = 0.0

    while ( True ):

      expon, more, h, t = comp_next ( degree, dim_num, expon, more, h, t )

      v = monomial_value ( expon, xyz )

      quad = hexahedron_unit_volume ( ) * np.dot ( w, v )

      exact = hexahedron_unit_monomial_integral ( expon )

      quad_error = np.abs ( quad - exact )

      max_error = max ( max_error, quad_error )

      if ( not more ):
        break

    print ( '  %2d  %24.16g' % ( degree, max_error ) )

  return

def hexahedron_witherden_rule_test03 ( p_lo, p_hi ):

#*****************************************************************************80
#
## hexahedron_witherden_rule_test03() tests absolute and relative precision.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    17 July 2023
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer p_lo, p_hi: the range of precisions.
#
  import numpy as np

  print ( '' )
  print ( 'hexahedron_witherden_rule_test03():' )
  print ( '  Test the precision of quadrature rules for the unit hexahedron.' )
  print ( '  Check rules of precision p =', p_lo, 'through', p_hi )
  print ( '  for error in approximating integrals of monomials.' )

  dim_num = 3

  print ( '' )
  print ( '              maximum                   maximum' )
  print ( '   p          absolute                  relative' )
  print ( '              error                     error' )
  print ( '' )

  for p in range ( p_lo, p_hi + 1 ):

    n, x, y, z, w = hexahedron_witherden_rule ( p )
#
#  Pack the x, y, z vectors as rows of an array.
#
    xyz = np.transpose ( np.array ( [ x, y, z ] ) )

    max_abs = 0.0
    max_rel = 0.0

    for degree in range ( 0, p + 1 ):

      expon = np.zeros ( dim_num, dtype = int )
      more = False
      h = 0
      t = 0

      while ( True ):

        expon, more, h, t = comp_next ( degree, dim_num, expon, more, h, t )

        v = monomial_value ( expon, xyz )

        quad = hexahedron_unit_volume ( ) * np.dot ( w, v )

        exact = hexahedron_unit_monomial_integral ( expon )

        quad_error = np.abs ( quad - exact )

        max_abs = max ( max_abs, quad_error )
        max_rel = max ( max_rel, quad_error / abs ( exact ) )

        if ( not more ):
          break

    print ( '  %2d  %24.16g  %24.16g' % ( p, max_abs, max_rel ) )

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
  if ( k == 0 ):
    a = []
    more = False
    t = n
    h = 0
    return a, more, h, t

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

def hexahedron_unit_monomial_integral ( expon ):

#*****************************************************************************80
#
## hexahedron_unit_monomial_integral(): monomial integral in a unit hexahedron.
#
#  Discussion:
#
#    This routine returns the integral of
#
#      product ( 1 <= I <= 3 ) X(I)^EXPON(I)
#
#    over the unit hexahedron.
#
#    The unit hexahedron H is bounded by the vertices
#    (0,0,0), (1,0,0), (1,1,0), (0,1,0), (0,0,1), (1,0,1), (1,1,1), (0,1,1).
# 
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON(3): the exponents.
#
#  Output:
#
#    real VALUE: the integral of the monomial.
#
  value = 1.0 / ( expon[0] + 1 ) \
        * 1.0 / ( expon[1] + 1 ) \
        * 1.0 / ( expon[2] + 1 )

  return value

def hexahedron_unit_volume ( ):

#*****************************************************************************80
#
## hexahedron_unit_volume() returns the volume of a unit hexahedron.
#
#  Discussion:
#
#    The unit hexahedron has vertices 
#    (0,0,0), (1,0,0), (1,1,0), (0,1,0), (0,0,1), (1,0,1), (1,1,1), (0,1,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real value: the volume.
#
  value = 1.0

  return value

def hexahedron_witherden_rule ( p ):

#*****************************************************************************80
#
## hexahedron_witherden_rule() returns a hexahedron quadrature rule of given precision.
#
#  Discussion:
#
#    The unit hexahedron is defined as:
#
#    0 <= X <= 1
#    0 <= Y <= 1
#    0 <= Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Freddie Witherden, Peter Vincent,
#    On the identification of symmetric quadrature rules for finite element methods,
#    Computers and Mathematics with Applications,
#    Volume 69, pages 1232-1241, 2015.
#
#  Input:
#
#    integer p: the precision, 0 <= p <= 11.
#
#  Output:
#
#    integer n: the order of the rule.
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  if ( p < 0 ):
    raise Exception ( 'hexahedron_witherden_rule(): Input p < 0.' )
 
  if ( 11 < p ):
    raise Exception ( 'hexahedron_witherden_rule(): Input 11 < p.' )

  n = rule_order ( p )

  if ( p <= 1 ):
    x, y, z, w = rule01 ( )
  elif ( p <= 3 ):
    x, y, z, w = rule03 ( )
  elif ( p <= 5 ):
    x, y, z, w = rule05 ( )
  elif ( p <= 7 ):
    x, y, z, w = rule07 ( )
  elif ( p <= 9 ):
    x, y, z, w = rule09 ( )
  elif ( p <= 11 ):
    x, y, z, w = rule11 ( )

  return n, x, y, z, w

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

def rule_order ( p ):

#*****************************************************************************80
#
## rule_order() returns the order of a hexahedron quadrature rule of given precision.
#
#  Discussion:
#
#    The "order" of a quadrature rule is the number of points involved.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Freddie Witherden, Peter Vincent,
#    On the identification of symmetric quadrature rules for finite element methods,
#    Computers and Mathematics with Applications,
#    Volume 69, pages 1232-1241, 2015.
#
#  Input:
#
#    integer p: the precision, 0 <= p <= 11.
#
#  Output:
#
#    integer order: the order of the rule.
#
  import numpy as np

  if ( p < 0 ):
    raise Exception ( 'rule_order(): Input p < 0.' )

  if ( 11 < p ):
    raise Exception ( 'rule_order(): Input 11 < p.' )

  order_vec = np.array ( [ \
       1,  \
       1,  6,  6, 14, 14, 34, 34, 58, 58, 90, \
      90 ] )

  order = order_vec[p]

  return order

def rule01 ( ):

#*****************************************************************************80
#
## rule01() returns the hexahedron rule of precision 1.
#
#  Discussion:
#
#    We suppose we are given a hexahedron H with vertices
#    (0,0,0), (1,0,0), (1,1,0), (0,1,0), (0,0,1), (1,0,1), (1,1,1), (0,1,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over H is 
#    approximated by Q as follows:
#
#    Q = volume(H) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Freddie Witherden, Peter Vincent,
#    On the identification of symmetric quadrature rules for finite element methods,
#    Computers and Mathematics with Applications,
#    Volume 69, pages 1232-1241, 2015.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  import numpy as np

  x = np.array ( [ \
          0.5000000000000000 ] )

  y = np.array ( [ \
          0.5000000000000000 ] )

  z = np.array ( [ \
          0.5000000000000000 ] )

  w = np.array ( [ \
          1.0000000000000000 ] )

  return x, y, z, w

def rule03 ( ):

#*****************************************************************************80
#
## rule03() returns the hexahedron rule of precision 3.
#
#  Discussion:
#
#    We suppose we are given a hexahedron H with vertices
#    (0,0,0), (1,0,0), (1,1,0), (0,1,0), (0,0,1), (1,0,1), (1,1,1), (0,1,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over H is 
#    approximated by Q as follows:
#
#    Q = volume(H) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Freddie Witherden, Peter Vincent,
#    On the identification of symmetric quadrature rules for finite element methods,
#    Computers and Mathematics with Applications,
#    Volume 69, pages 1232-1241, 2015.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.0000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          1.0000000000000000, \
          0.5000000000000000 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          1.0000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0000000000000000 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          1.0000000000000000, \
          0.5000000000000000, \
          0.0000000000000000, \
          0.5000000000000000, \
          0.5000000000000000 ] )

  w = np.array ( [ \
          0.1666666666666667, \
          0.1666666666666667, \
          0.1666666666666667, \
          0.1666666666666667, \
          0.1666666666666667, \
          0.1666666666666667 ] )

  return x, y, z, w

def rule05 ( ):

#*****************************************************************************80
#
## rule05() returns the hexahedron rule of precision 5.
#
#  Discussion:
#
#    We suppose we are given a hexahedron H with vertices
#    (0,0,0), (1,0,0), (1,1,0), (0,1,0), (0,0,1), (1,0,1), (1,1,1), (0,1,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over H is 
#    approximated by Q as follows:
#
#    Q = volume(H) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Freddie Witherden, Peter Vincent,
#    On the identification of symmetric quadrature rules for finite element methods,
#    Computers and Mathematics with Applications,
#    Volume 69, pages 1232-1241, 2015.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.1020887871228893, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8979112128771107, \
          0.5000000000000000, \
          0.8793934553196641, \
          0.1206065446803359, \
          0.1206065446803359, \
          0.1206065446803359, \
          0.1206065446803359, \
          0.8793934553196641, \
          0.8793934553196641, \
          0.8793934553196641 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8979112128771107, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1020887871228893, \
          0.1206065446803359, \
          0.8793934553196641, \
          0.8793934553196641, \
          0.1206065446803359, \
          0.1206065446803359, \
          0.8793934553196641, \
          0.8793934553196641, \
          0.1206065446803359 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.8979112128771107, \
          0.5000000000000000, \
          0.1020887871228893, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1206065446803359, \
          0.8793934553196641, \
          0.1206065446803359, \
          0.1206065446803359, \
          0.8793934553196641, \
          0.1206065446803359, \
          0.8793934553196641, \
          0.8793934553196641 ] )

  w = np.array ( [ \
          0.1108033240997230, \
          0.1108033240997230, \
          0.1108033240997230, \
          0.1108033240997230, \
          0.1108033240997230, \
          0.1108033240997230, \
          0.0418975069252078, \
          0.0418975069252078, \
          0.0418975069252078, \
          0.0418975069252078, \
          0.0418975069252078, \
          0.0418975069252078, \
          0.0418975069252078, \
          0.0418975069252078 ] )

  return x, y, z, w

def rule07 ( ):

#*****************************************************************************80
#
## rule07() returns the hexahedron rule of precision 7.
#
#  Discussion:
#
#    We suppose we are given a hexahedron H with vertices
#    (0,0,0), (1,0,0), (1,1,0), (0,1,0), (0,0,1), (1,0,1), (1,1,1), (0,1,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over H is 
#    approximated by Q as follows:
#
#    Q = volume(H) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Freddie Witherden, Peter Vincent,
#    On the identification of symmetric quadrature rules for finite element methods,
#    Computers and Mathematics with Applications,
#    Volume 69, pages 1232-1241, 2015.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.0059569194056617, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9940430805943383, \
          0.5000000000000000, \
          0.7039775836791597, \
          0.2960224163208403, \
          0.2960224163208403, \
          0.2960224163208403, \
          0.2960224163208403, \
          0.7039775836791597, \
          0.7039775836791597, \
          0.7039775836791597, \
          0.8905514105020593, \
          0.1094485894979407, \
          0.1094485894979407, \
          0.1094485894979407, \
          0.1094485894979407, \
          0.8905514105020593, \
          0.8905514105020593, \
          0.8905514105020593, \
          0.0759738621579806, \
          0.9240261378420194, \
          0.5000000000000000, \
          0.9240261378420194, \
          0.9240261378420194, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0759738621579806, \
          0.0759738621579806, \
          0.9240261378420194, \
          0.5000000000000000, \
          0.0759738621579806 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9940430805943383, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0059569194056617, \
          0.2960224163208403, \
          0.7039775836791597, \
          0.7039775836791597, \
          0.2960224163208403, \
          0.2960224163208403, \
          0.7039775836791597, \
          0.7039775836791597, \
          0.2960224163208403, \
          0.1094485894979407, \
          0.8905514105020593, \
          0.8905514105020593, \
          0.1094485894979407, \
          0.1094485894979407, \
          0.8905514105020593, \
          0.8905514105020593, \
          0.1094485894979407, \
          0.0759738621579806, \
          0.5000000000000000, \
          0.9240261378420194, \
          0.9240261378420194, \
          0.5000000000000000, \
          0.0759738621579806, \
          0.0759738621579806, \
          0.5000000000000000, \
          0.9240261378420194, \
          0.0759738621579806, \
          0.9240261378420194, \
          0.5000000000000000 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.9940430805943383, \
          0.5000000000000000, \
          0.0059569194056617, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.2960224163208403, \
          0.7039775836791597, \
          0.2960224163208403, \
          0.2960224163208403, \
          0.7039775836791597, \
          0.2960224163208403, \
          0.7039775836791597, \
          0.7039775836791597, \
          0.1094485894979407, \
          0.8905514105020593, \
          0.1094485894979407, \
          0.1094485894979407, \
          0.8905514105020593, \
          0.1094485894979407, \
          0.8905514105020593, \
          0.8905514105020593, \
          0.5000000000000000, \
          0.0759738621579806, \
          0.0759738621579806, \
          0.5000000000000000, \
          0.9240261378420194, \
          0.9240261378420194, \
          0.0759738621579806, \
          0.9240261378420194, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9240261378420194, \
          0.0759738621579806 ] )

  w = np.array ( [ \
          0.0250162363729459, \
          0.0250162363729459, \
          0.0250162363729459, \
          0.0250162363729459, \
          0.0250162363729459, \
          0.0250162363729459, \
          0.0571442320087316, \
          0.0571442320087316, \
          0.0571442320087316, \
          0.0571442320087316, \
          0.0571442320087316, \
          0.0571442320087316, \
          0.0571442320087316, \
          0.0571442320087316, \
          0.0192245175082448, \
          0.0192245175082448, \
          0.0192245175082448, \
          0.0192245175082448, \
          0.0192245175082448, \
          0.0192245175082448, \
          0.0192245175082448, \
          0.0192245175082448, \
          0.0199127154688761, \
          0.0199127154688761, \
          0.0199127154688761, \
          0.0199127154688761, \
          0.0199127154688761, \
          0.0199127154688761, \
          0.0199127154688761, \
          0.0199127154688761, \
          0.0199127154688761, \
          0.0199127154688761, \
          0.0199127154688761, \
          0.0199127154688761 ] )

  return x, y, z, w

def rule09 ( ):

#*****************************************************************************80
#
## rule09() returns the hexahedron rule of precision 9.
#
#  Discussion:
#
#    We suppose we are given a hexahedron H with vertices
#    (0,0,0), (1,0,0), (1,1,0), (0,1,0), (0,0,1), (1,0,1), (1,1,1), (0,1,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over H is 
#    approximated by Q as follows:
#
#    Q = volume(H) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Freddie Witherden, Peter Vincent,
#    On the identification of symmetric quadrature rules for finite element methods,
#    Computers and Mathematics with Applications,
#    Volume 69, pages 1232-1241, 2015.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.1931592652041455, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8068407347958545, \
          0.5000000000000000, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.0649501076690120, \
          0.0649501076690120, \
          0.0649501076690120, \
          0.9350498923309880, \
          0.9350498923309880, \
          0.9350498923309880, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.2179445964899850, \
          0.2179445964899850, \
          0.2179445964899850, \
          0.7820554035100150, \
          0.7820554035100150, \
          0.7820554035100150, \
          0.0611564383711609, \
          0.9388435616288391, \
          0.5000000000000000, \
          0.9388435616288391, \
          0.9388435616288391, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0611564383711609, \
          0.0611564383711609, \
          0.9388435616288391, \
          0.5000000000000000, \
          0.0611564383711609, \
          0.7161339513154311, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.0307347890676641, \
          0.2838660486845689, \
          0.9692652109323359, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.2838660486845689, \
          0.7161339513154311, \
          0.0307347890676641, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.7161339513154311, \
          0.9692652109323359, \
          0.7161339513154311, \
          0.9692652109323359, \
          0.9692652109323359, \
          0.0307347890676641, \
          0.7161339513154311, \
          0.2838660486845689, \
          0.7161339513154311, \
          0.0307347890676641 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8068407347958545, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1931592652041455, \
          0.0649501076690120, \
          0.9350498923309880, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.0649501076690120, \
          0.9350498923309880, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.2179445964899850, \
          0.7820554035100150, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.2179445964899850, \
          0.7820554035100150, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.0611564383711609, \
          0.5000000000000000, \
          0.9388435616288391, \
          0.9388435616288391, \
          0.5000000000000000, \
          0.0611564383711609, \
          0.0611564383711609, \
          0.5000000000000000, \
          0.9388435616288391, \
          0.0611564383711609, \
          0.9388435616288391, \
          0.5000000000000000, \
          0.9692652109323359, \
          0.0307347890676641, \
          0.9692652109323359, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.7161339513154311, \
          0.0307347890676641, \
          0.0307347890676641, \
          0.0307347890676641, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.9692652109323359, \
          0.7161339513154311, \
          0.2838660486845689, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.9692652109323359, \
          0.2838660486845689, \
          0.2838660486845689 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.8068407347958545, \
          0.5000000000000000, \
          0.1931592652041455, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0649501076690120, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.0649501076690120, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.9350498923309880, \
          0.9350498923309880, \
          0.2179445964899850, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.2179445964899850, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.7820554035100150, \
          0.7820554035100150, \
          0.5000000000000000, \
          0.0611564383711609, \
          0.0611564383711609, \
          0.5000000000000000, \
          0.9388435616288391, \
          0.9388435616288391, \
          0.0611564383711609, \
          0.9388435616288391, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9388435616288391, \
          0.0611564383711609, \
          0.2838660486845689, \
          0.7161339513154311, \
          0.2838660486845689, \
          0.7161339513154311, \
          0.9692652109323359, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.7161339513154311, \
          0.2838660486845689, \
          0.0307347890676641, \
          0.2838660486845689, \
          0.0307347890676641, \
          0.9692652109323359, \
          0.0307347890676641, \
          0.9692652109323359, \
          0.2838660486845689, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.9692652109323359, \
          0.7161339513154311, \
          0.0307347890676641, \
          0.2838660486845689 ] )

  w = np.array ( [ \
          0.0541593744687068, \
          0.0541593744687068, \
          0.0541593744687068, \
          0.0541593744687068, \
          0.0541593744687068, \
          0.0541593744687068, \
          0.0062685994124186, \
          0.0062685994124186, \
          0.0062685994124186, \
          0.0062685994124186, \
          0.0062685994124186, \
          0.0062685994124186, \
          0.0062685994124186, \
          0.0062685994124186, \
          0.0248574797680029, \
          0.0248574797680029, \
          0.0248574797680029, \
          0.0248574797680029, \
          0.0248574797680029, \
          0.0248574797680029, \
          0.0248574797680029, \
          0.0248574797680029, \
          0.0114737257670222, \
          0.0114737257670222, \
          0.0114737257670222, \
          0.0114737257670222, \
          0.0114737257670222, \
          0.0114737257670222, \
          0.0114737257670222, \
          0.0114737257670222, \
          0.0114737257670222, \
          0.0114737257670222, \
          0.0114737257670222, \
          0.0114737257670222, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717, \
          0.0120146004391717 ] )

  return x, y, z, w

def rule11 ( ):

#*****************************************************************************80
#
## rule11() returns the hexahedron rule of precision 11.
#
#  Discussion:
#
#    We suppose we are given a hexahedron H with vertices
#    (0,0,0), (1,0,0), (1,1,0), (0,1,0), (0,0,1), (1,0,1), (1,1,1), (0,1,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over H is 
#    approximated by Q as follows:
#
#    Q = volume(H) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Freddie Witherden, Peter Vincent,
#    On the identification of symmetric quadrature rules for finite element methods,
#    Computers and Mathematics with Applications,
#    Volume 69, pages 1232-1241, 2015.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.0936928329501868, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9063071670498133, \
          0.5000000000000000, \
          0.8008376320991313, \
          0.1991623679008687, \
          0.1991623679008687, \
          0.1991623679008687, \
          0.1991623679008687, \
          0.8008376320991313, \
          0.8008376320991313, \
          0.8008376320991313, \
          0.9277278805088800, \
          0.0722721194911200, \
          0.0722721194911200, \
          0.0722721194911200, \
          0.0722721194911200, \
          0.9277278805088800, \
          0.9277278805088800, \
          0.9277278805088800, \
          0.6566967022580273, \
          0.3433032977419727, \
          0.3433032977419727, \
          0.3433032977419727, \
          0.3433032977419727, \
          0.6566967022580273, \
          0.6566967022580273, \
          0.6566967022580273, \
          0.1326658565014960, \
          0.8673341434985040, \
          0.5000000000000000, \
          0.8673341434985040, \
          0.8673341434985040, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1326658565014960, \
          0.1326658565014960, \
          0.8673341434985040, \
          0.5000000000000000, \
          0.1326658565014960, \
          0.7253999675572547, \
          0.2746000324427453, \
          0.2746000324427453, \
          0.0174501672436448, \
          0.2746000324427453, \
          0.9825498327563551, \
          0.7253999675572547, \
          0.7253999675572547, \
          0.2746000324427453, \
          0.7253999675572547, \
          0.0174501672436448, \
          0.2746000324427453, \
          0.2746000324427453, \
          0.2746000324427453, \
          0.7253999675572547, \
          0.9825498327563551, \
          0.7253999675572547, \
          0.9825498327563551, \
          0.9825498327563551, \
          0.0174501672436448, \
          0.7253999675572547, \
          0.2746000324427453, \
          0.7253999675572547, \
          0.0174501672436448, \
          0.9706224286053016, \
          0.0293775713946984, \
          0.0293775713946984, \
          0.3230485927016850, \
          0.0293775713946984, \
          0.6769514072983150, \
          0.9706224286053016, \
          0.9706224286053016, \
          0.0293775713946984, \
          0.9706224286053016, \
          0.3230485927016850, \
          0.0293775713946984, \
          0.0293775713946984, \
          0.0293775713946984, \
          0.9706224286053016, \
          0.6769514072983150, \
          0.9706224286053016, \
          0.6769514072983150, \
          0.6769514072983150, \
          0.3230485927016850, \
          0.9706224286053016, \
          0.0293775713946984, \
          0.9706224286053016, \
          0.3230485927016850 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9063071670498133, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0936928329501868, \
          0.1991623679008687, \
          0.8008376320991313, \
          0.8008376320991313, \
          0.1991623679008687, \
          0.1991623679008687, \
          0.8008376320991313, \
          0.8008376320991313, \
          0.1991623679008687, \
          0.0722721194911200, \
          0.9277278805088800, \
          0.9277278805088800, \
          0.0722721194911200, \
          0.0722721194911200, \
          0.9277278805088800, \
          0.9277278805088800, \
          0.0722721194911200, \
          0.3433032977419727, \
          0.6566967022580273, \
          0.6566967022580273, \
          0.3433032977419727, \
          0.3433032977419727, \
          0.6566967022580273, \
          0.6566967022580273, \
          0.3433032977419727, \
          0.1326658565014960, \
          0.5000000000000000, \
          0.8673341434985040, \
          0.8673341434985040, \
          0.5000000000000000, \
          0.1326658565014960, \
          0.1326658565014960, \
          0.5000000000000000, \
          0.8673341434985040, \
          0.1326658565014960, \
          0.8673341434985040, \
          0.5000000000000000, \
          0.9825498327563551, \
          0.0174501672436448, \
          0.9825498327563551, \
          0.2746000324427453, \
          0.2746000324427453, \
          0.7253999675572547, \
          0.0174501672436448, \
          0.0174501672436448, \
          0.0174501672436448, \
          0.7253999675572547, \
          0.7253999675572547, \
          0.7253999675572547, \
          0.7253999675572547, \
          0.2746000324427453, \
          0.2746000324427453, \
          0.2746000324427453, \
          0.9825498327563551, \
          0.7253999675572547, \
          0.2746000324427453, \
          0.7253999675572547, \
          0.7253999675572547, \
          0.9825498327563551, \
          0.2746000324427453, \
          0.2746000324427453, \
          0.6769514072983150, \
          0.3230485927016850, \
          0.6769514072983150, \
          0.0293775713946984, \
          0.0293775713946984, \
          0.9706224286053016, \
          0.3230485927016850, \
          0.3230485927016850, \
          0.3230485927016850, \
          0.9706224286053016, \
          0.9706224286053016, \
          0.9706224286053016, \
          0.9706224286053016, \
          0.0293775713946984, \
          0.0293775713946984, \
          0.0293775713946984, \
          0.6769514072983150, \
          0.9706224286053016, \
          0.0293775713946984, \
          0.9706224286053016, \
          0.9706224286053016, \
          0.6769514072983150, \
          0.0293775713946984, \
          0.0293775713946984 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.9063071670498133, \
          0.5000000000000000, \
          0.0936928329501868, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1991623679008687, \
          0.8008376320991313, \
          0.1991623679008687, \
          0.1991623679008687, \
          0.8008376320991313, \
          0.1991623679008687, \
          0.8008376320991313, \
          0.8008376320991313, \
          0.0722721194911200, \
          0.9277278805088800, \
          0.0722721194911200, \
          0.0722721194911200, \
          0.9277278805088800, \
          0.0722721194911200, \
          0.9277278805088800, \
          0.9277278805088800, \
          0.3433032977419727, \
          0.6566967022580273, \
          0.3433032977419727, \
          0.3433032977419727, \
          0.6566967022580273, \
          0.3433032977419727, \
          0.6566967022580273, \
          0.6566967022580273, \
          0.5000000000000000, \
          0.1326658565014960, \
          0.1326658565014960, \
          0.5000000000000000, \
          0.8673341434985040, \
          0.8673341434985040, \
          0.1326658565014960, \
          0.8673341434985040, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8673341434985040, \
          0.1326658565014960, \
          0.2746000324427453, \
          0.7253999675572547, \
          0.2746000324427453, \
          0.7253999675572547, \
          0.9825498327563551, \
          0.2746000324427453, \
          0.2746000324427453, \
          0.7253999675572547, \
          0.2746000324427453, \
          0.0174501672436448, \
          0.2746000324427453, \
          0.0174501672436448, \
          0.9825498327563551, \
          0.0174501672436448, \
          0.9825498327563551, \
          0.2746000324427453, \
          0.7253999675572547, \
          0.7253999675572547, \
          0.7253999675572547, \
          0.7253999675572547, \
          0.9825498327563551, \
          0.7253999675572547, \
          0.0174501672436448, \
          0.2746000324427453, \
          0.0293775713946984, \
          0.9706224286053016, \
          0.0293775713946984, \
          0.9706224286053016, \
          0.6769514072983150, \
          0.0293775713946984, \
          0.0293775713946984, \
          0.9706224286053016, \
          0.0293775713946984, \
          0.3230485927016850, \
          0.0293775713946984, \
          0.3230485927016850, \
          0.6769514072983150, \
          0.3230485927016850, \
          0.6769514072983150, \
          0.0293775713946984, \
          0.9706224286053016, \
          0.9706224286053016, \
          0.9706224286053016, \
          0.9706224286053016, \
          0.6769514072983150, \
          0.9706224286053016, \
          0.3230485927016850, \
          0.0293775713946984 ] )

  w = np.array ( [ \
          0.0253096342016000, \
          0.0253096342016000, \
          0.0253096342016000, \
          0.0253096342016000, \
          0.0253096342016000, \
          0.0253096342016000, \
          0.0146922934945570, \
          0.0146922934945570, \
          0.0146922934945570, \
          0.0146922934945570, \
          0.0146922934945570, \
          0.0146922934945570, \
          0.0146922934945570, \
          0.0146922934945570, \
          0.0055804890098537, \
          0.0055804890098537, \
          0.0055804890098537, \
          0.0055804890098537, \
          0.0055804890098537, \
          0.0055804890098537, \
          0.0055804890098537, \
          0.0055804890098537, \
          0.0269990056568711, \
          0.0269990056568711, \
          0.0269990056568711, \
          0.0269990056568711, \
          0.0269990056568711, \
          0.0269990056568711, \
          0.0269990056568711, \
          0.0269990056568711, \
          0.0181499182325145, \
          0.0181499182325145, \
          0.0181499182325145, \
          0.0181499182325145, \
          0.0181499182325145, \
          0.0181499182325145, \
          0.0181499182325145, \
          0.0181499182325145, \
          0.0181499182325145, \
          0.0181499182325145, \
          0.0181499182325145, \
          0.0181499182325145, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0076802492622294, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527, \
          0.0028267870173527 ] )

  return x, y, z, w

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
  hexahedron_witherden_rule_test ( )
  timestamp ( )

