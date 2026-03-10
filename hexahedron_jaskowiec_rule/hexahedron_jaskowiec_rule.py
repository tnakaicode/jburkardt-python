#! /usr/bin/env python3
#
def hexahedron_jaskowiec_rule_test ( ):

#*****************************************************************************80
#
## hexahedron_jaskowiec_rule_test() tests hexahedron_jaskowiec_rule().
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
  print ( 'hexahedron_jaskowiec_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hexahedron_jaskowiec_rule().' )

  p = 5
  hexahedron_jaskowiec_rule_test01 ( p )

  p = 5
  hexahedron_jaskowiec_rule_test02 ( p )

  p_lo = 0
  p_hi = 21
  hexahedron_jaskowiec_rule_test03 ( p_lo, p_hi )
#
#  Terminate.
#
  print ( '' )
  print ( 'hexahedron_jaskowiec_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def hexahedron_jaskowiec_rule_test01 ( p ):

#*****************************************************************************80
#
## hexahedron_jaskowiec_rule_test01() prints a rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    24 May 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'hexahedron_jaskowiec_rule_test01():' )
  print ( '  Quadrature rule for the unit hexahedron,' )
  print ( '  Precision p =', p )
#
#  Retrieve the rule.
#
  n, x, y, z, w = hexahedron_jaskowiec_rule ( p )
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
#  Verify that weights sum to 1.
#
  w_sum = np.sum ( w )

  print ( '' )
  print ( '  Weight Sum ', w_sum )

  return

def hexahedron_jaskowiec_rule_test02 ( p ):

#*****************************************************************************80
#
## hexahedron_jaskowiec_rule_test02() tests a rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    19 May 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'hexahedron_jaskowiec_rule_test02():' )
  print ( '  Test the precision of a quadrature rule for the unit hexahedron.' )

  dim_num = 3
#
#  Retrieve the rule.
#
  n, x, y, z, w = hexahedron_jaskowiec_rule ( p )
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

def hexahedron_jaskowiec_rule_test03 ( p_lo, p_hi ):

#*****************************************************************************80
#
## hexahedron_jaskowiec_rule_test03() tests absolute and relative precision.
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

  print ( '' )
  print ( 'hexahedron_jaskowiec_rule_test03():' )
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

    n, x, y, z, w = hexahedron_jaskowiec_rule ( p )
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

def hexahedron_jaskowiec_rule ( p ):

#*****************************************************************************80
#
## hexahedron_jaskowiec_rule() returns a hexahedron quadrature rule of given precision.
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
#    19 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and prisms,
#    International Journal of Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Input:
#
#    integer p: the precision, 0 <= p <= 21.
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
    raise Exception ( 'prism_jaskowiec_rule(): Input p < 0.' )
 
  if ( 21 < p ):
    raise Exception ( 'prism_jaskowiec_rule(): Input 21 < p.' )

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
  elif ( p <= 13 ):
    x, y, z, w = rule13 ( )
  elif ( p <= 15 ):
    x, y, z, w = rule15 ( )
  elif ( p <= 17 ):
    x, y, z, w = rule17 ( )
  elif ( p <= 19 ):
    x, y, z, w = rule19 ( )
  elif ( p <= 21 ):
    x, y, z, w = rule21 ( )

  return n, x, y, z, w

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
#    05 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Input:
#
#    integer p: the precision, 0 <= p <= 21.
#
#  Output:
#
#    integer order: the order of the rule.
#
  import numpy as np

  if ( p < 0 ):
    raise Exception ( 'rule_order(): Input p < 0.' )

  if ( 21 < p ):
    raise Exception ( 'rule_order(): Input 21 < p.' )

  order_vec = np.array ( [ \
        1,  \
        1,   6,   6,  14,  14,  34,  34,  58,  58,  90, \
       90, 154, 154, 256, 256, 346, 346, 454, 454, 580, \
      580 ] )

  order = order_vec[p]

  return order

def rule01 ( ):

#*****************************************************************************80
#
## rule01() returns the hexahedron quadrature rule of precision 1.
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
#    05 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which add to 1.
#
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
## rule03() returns the hexahedron quadrature rule of precision 3.
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
#    05 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which add to 1.
#
  import numpy as np

  x = np.array ( [ \
          1.0000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0000000000000000, \
          0.5000000000000000, \
          0.5000000000000000 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          1.0000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0000000000000000, \
          0.5000000000000000 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          1.0000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0000000000000000 ] )

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
## rule05() returns the hexahedron quadrature rule of precision 5.
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
#    05 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which add to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.1020887871228893, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8979112128771107, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8793934553196641, \
          0.1206065446803359, \
          0.1206065446803359, \
          0.8793934553196641, \
          0.8793934553196641, \
          0.1206065446803359, \
          0.8793934553196641, \
          0.1206065446803359 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.1020887871228893, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8979112128771107, \
          0.5000000000000000, \
          0.8793934553196641, \
          0.1206065446803359, \
          0.8793934553196641, \
          0.1206065446803359, \
          0.8793934553196641, \
          0.1206065446803359, \
          0.1206065446803359, \
          0.8793934553196641 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1020887871228893, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8979112128771107, \
          0.8793934553196641, \
          0.1206065446803359, \
          0.8793934553196641, \
          0.8793934553196641, \
          0.1206065446803359, \
          0.8793934553196641, \
          0.1206065446803359, \
          0.1206065446803359 ] )

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
## rule07() returns the hexahedron quadrature rule of precision 7.
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
#    05 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which add to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.0305973139469912, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9694026860530087, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8731668050064080, \
          0.1268331949935920, \
          0.1268331949935920, \
          0.8731668050064080, \
          0.8731668050064080, \
          0.1268331949935920, \
          0.8731668050064080, \
          0.1268331949935920, \
          0.7050654491660072, \
          0.2949345508339928, \
          0.2949345508339928, \
          0.7050654491660072, \
          0.7050654491660072, \
          0.2949345508339928, \
          0.7050654491660072, \
          0.2949345508339928, \
          0.9532303450614186, \
          0.5000000000000000, \
          0.9532303450614186, \
          0.0467696549385814, \
          0.5000000000000000, \
          0.0467696549385814, \
          0.9532303450614186, \
          0.5000000000000000, \
          0.9532303450614186, \
          0.0467696549385814, \
          0.5000000000000000, \
          0.0467696549385814 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.0305973139469912, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9694026860530087, \
          0.5000000000000000, \
          0.8731668050064080, \
          0.1268331949935920, \
          0.8731668050064080, \
          0.1268331949935920, \
          0.8731668050064080, \
          0.1268331949935920, \
          0.1268331949935920, \
          0.8731668050064080, \
          0.7050654491660072, \
          0.2949345508339928, \
          0.7050654491660072, \
          0.2949345508339928, \
          0.7050654491660072, \
          0.2949345508339928, \
          0.2949345508339928, \
          0.7050654491660072, \
          0.9532303450614186, \
          0.9532303450614186, \
          0.5000000000000000, \
          0.9532303450614186, \
          0.0467696549385814, \
          0.5000000000000000, \
          0.0467696549385814, \
          0.9532303450614186, \
          0.5000000000000000, \
          0.0467696549385814, \
          0.0467696549385814, \
          0.5000000000000000 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0305973139469912, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9694026860530087, \
          0.8731668050064080, \
          0.1268331949935920, \
          0.8731668050064080, \
          0.8731668050064080, \
          0.1268331949935920, \
          0.8731668050064080, \
          0.1268331949935920, \
          0.1268331949935920, \
          0.7050654491660072, \
          0.2949345508339928, \
          0.7050654491660072, \
          0.7050654491660072, \
          0.2949345508339928, \
          0.7050654491660072, \
          0.2949345508339928, \
          0.2949345508339928, \
          0.5000000000000000, \
          0.9532303450614186, \
          0.9532303450614186, \
          0.5000000000000000, \
          0.9532303450614186, \
          0.9532303450614186, \
          0.5000000000000000, \
          0.0467696549385814, \
          0.0467696549385814, \
          0.5000000000000000, \
          0.0467696549385814, \
          0.0467696549385814 ] )

  w = np.array ( [ \
          0.0340045847498003, \
          0.0340045847498003, \
          0.0340045847498003, \
          0.0340045847498003, \
          0.0340045847498003, \
          0.0340045847498003, \
          0.0252967244013519, \
          0.0252967244013519, \
          0.0252967244013519, \
          0.0252967244013519, \
          0.0252967244013519, \
          0.0252967244013519, \
          0.0252967244013519, \
          0.0252967244013519, \
          0.0541706353348564, \
          0.0541706353348564, \
          0.0541706353348564, \
          0.0541706353348564, \
          0.0541706353348564, \
          0.0541706353348564, \
          0.0541706353348564, \
          0.0541706353348564, \
          0.0133528011342943, \
          0.0133528011342943, \
          0.0133528011342943, \
          0.0133528011342943, \
          0.0133528011342943, \
          0.0133528011342943, \
          0.0133528011342943, \
          0.0133528011342943, \
          0.0133528011342943, \
          0.0133528011342943, \
          0.0133528011342943, \
          0.0133528011342943 ] )

  return x, y, z, w

def rule09 ( ):

#*****************************************************************************80
#
## rule09() returns the hexahedron quadrature rule of precision 9.
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
#    05 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which add to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.1931592652041455, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8068407347958545, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.0649501076690120, \
          0.9350498923309880, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.2179445964899850, \
          0.7820554035100150, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.9388435616288391, \
          0.5000000000000000, \
          0.9388435616288391, \
          0.0611564383711609, \
          0.5000000000000000, \
          0.0611564383711609, \
          0.9388435616288391, \
          0.5000000000000000, \
          0.9388435616288391, \
          0.0611564383711609, \
          0.5000000000000000, \
          0.0611564383711609, \
          0.7161339513154311, \
          0.9692652109323359, \
          0.7161339513154311, \
          0.2838660486845689, \
          0.9692652109323359, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.9692652109323359, \
          0.2838660486845689, \
          0.7161339513154311, \
          0.9692652109323359, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.0307347890676641, \
          0.7161339513154311, \
          0.2838660486845689, \
          0.0307347890676641, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.0307347890676641, \
          0.2838660486845689, \
          0.7161339513154311, \
          0.0307347890676641, \
          0.7161339513154311 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.1931592652041455, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8068407347958545, \
          0.5000000000000000, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.0649501076690120, \
          0.9350498923309880, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.2179445964899850, \
          0.7820554035100150, \
          0.9388435616288391, \
          0.9388435616288391, \
          0.5000000000000000, \
          0.9388435616288391, \
          0.0611564383711609, \
          0.5000000000000000, \
          0.0611564383711609, \
          0.9388435616288391, \
          0.5000000000000000, \
          0.0611564383711609, \
          0.0611564383711609, \
          0.5000000000000000, \
          0.9692652109323359, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.9692652109323359, \
          0.2838660486845689, \
          0.7161339513154311, \
          0.9692652109323359, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.9692652109323359, \
          0.7161339513154311, \
          0.2838660486845689, \
          0.0307347890676641, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.0307347890676641, \
          0.2838660486845689, \
          0.7161339513154311, \
          0.0307347890676641, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.0307347890676641, \
          0.7161339513154311, \
          0.2838660486845689 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1931592652041455, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8068407347958545, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.9350498923309880, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.9350498923309880, \
          0.0649501076690120, \
          0.0649501076690120, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.7820554035100150, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.7820554035100150, \
          0.2179445964899850, \
          0.2179445964899850, \
          0.5000000000000000, \
          0.9388435616288391, \
          0.9388435616288391, \
          0.5000000000000000, \
          0.9388435616288391, \
          0.9388435616288391, \
          0.5000000000000000, \
          0.0611564383711609, \
          0.0611564383711609, \
          0.5000000000000000, \
          0.0611564383711609, \
          0.0611564383711609, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.9692652109323359, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.9692652109323359, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.9692652109323359, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.9692652109323359, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.0307347890676641, \
          0.7161339513154311, \
          0.7161339513154311, \
          0.0307347890676641, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.0307347890676641, \
          0.2838660486845689, \
          0.2838660486845689, \
          0.0307347890676641 ] )

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
## rule11() returns the hexahedron quadrature rule of precision 11.
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
#    05 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which add to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.8610665194372092, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1389334805627908, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9047441009815494, \
          0.0952558990184506, \
          0.0952558990184506, \
          0.9047441009815494, \
          0.9047441009815494, \
          0.0952558990184506, \
          0.9047441009815494, \
          0.0952558990184506, \
          0.2331729955597515, \
          0.7668270044402485, \
          0.7668270044402485, \
          0.2331729955597515, \
          0.2331729955597515, \
          0.7668270044402485, \
          0.2331729955597515, \
          0.7668270044402485, \
          0.6403862933256372, \
          0.3596137066743628, \
          0.3596137066743628, \
          0.6403862933256372, \
          0.6403862933256372, \
          0.3596137066743628, \
          0.6403862933256372, \
          0.3596137066743628, \
          0.9019667336076422, \
          0.5000000000000000, \
          0.9019667336076422, \
          0.0980332663923578, \
          0.5000000000000000, \
          0.0980332663923578, \
          0.9019667336076422, \
          0.5000000000000000, \
          0.9019667336076422, \
          0.0980332663923578, \
          0.5000000000000000, \
          0.0980332663923578, \
          0.9900497455045357, \
          0.2346080844030868, \
          0.9900497455045357, \
          0.0099502544954643, \
          0.2346080844030868, \
          0.0099502544954643, \
          0.0099502544954643, \
          0.2346080844030868, \
          0.0099502544954643, \
          0.9900497455045357, \
          0.2346080844030868, \
          0.9900497455045357, \
          0.9900497455045357, \
          0.7653919155969132, \
          0.9900497455045357, \
          0.0099502544954643, \
          0.7653919155969132, \
          0.0099502544954643, \
          0.0099502544954643, \
          0.7653919155969132, \
          0.0099502544954643, \
          0.9900497455045357, \
          0.7653919155969132, \
          0.9900497455045357, \
          0.7028429900975481, \
          0.9772916094647830, \
          0.7028429900975481, \
          0.2971570099024518, \
          0.9772916094647830, \
          0.2971570099024518, \
          0.2971570099024518, \
          0.9772916094647830, \
          0.2971570099024518, \
          0.7028429900975481, \
          0.9772916094647830, \
          0.7028429900975481, \
          0.7028429900975481, \
          0.0227083905352169, \
          0.7028429900975481, \
          0.2971570099024518, \
          0.0227083905352169, \
          0.2971570099024518, \
          0.2971570099024518, \
          0.0227083905352169, \
          0.2971570099024518, \
          0.7028429900975481, \
          0.0227083905352169, \
          0.7028429900975481 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.8610665194372092, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1389334805627908, \
          0.5000000000000000, \
          0.9047441009815494, \
          0.0952558990184506, \
          0.9047441009815494, \
          0.0952558990184506, \
          0.9047441009815494, \
          0.0952558990184506, \
          0.0952558990184506, \
          0.9047441009815494, \
          0.2331729955597515, \
          0.7668270044402485, \
          0.2331729955597515, \
          0.7668270044402485, \
          0.2331729955597515, \
          0.7668270044402485, \
          0.7668270044402485, \
          0.2331729955597515, \
          0.6403862933256372, \
          0.3596137066743628, \
          0.6403862933256372, \
          0.3596137066743628, \
          0.6403862933256372, \
          0.3596137066743628, \
          0.3596137066743628, \
          0.6403862933256372, \
          0.9019667336076422, \
          0.9019667336076422, \
          0.5000000000000000, \
          0.9019667336076422, \
          0.0980332663923578, \
          0.5000000000000000, \
          0.0980332663923578, \
          0.9019667336076422, \
          0.5000000000000000, \
          0.0980332663923578, \
          0.0980332663923578, \
          0.5000000000000000, \
          0.2346080844030868, \
          0.9900497455045357, \
          0.9900497455045357, \
          0.2346080844030868, \
          0.0099502544954643, \
          0.9900497455045357, \
          0.2346080844030868, \
          0.0099502544954643, \
          0.0099502544954643, \
          0.2346080844030868, \
          0.9900497455045357, \
          0.0099502544954643, \
          0.7653919155969132, \
          0.9900497455045357, \
          0.9900497455045357, \
          0.7653919155969132, \
          0.0099502544954643, \
          0.9900497455045357, \
          0.7653919155969132, \
          0.0099502544954643, \
          0.0099502544954643, \
          0.7653919155969132, \
          0.9900497455045357, \
          0.0099502544954643, \
          0.9772916094647830, \
          0.7028429900975481, \
          0.7028429900975481, \
          0.9772916094647830, \
          0.2971570099024518, \
          0.7028429900975481, \
          0.9772916094647830, \
          0.2971570099024518, \
          0.2971570099024518, \
          0.9772916094647830, \
          0.7028429900975481, \
          0.2971570099024518, \
          0.0227083905352169, \
          0.7028429900975481, \
          0.7028429900975481, \
          0.0227083905352169, \
          0.2971570099024518, \
          0.7028429900975481, \
          0.0227083905352169, \
          0.2971570099024518, \
          0.2971570099024518, \
          0.0227083905352169, \
          0.7028429900975481, \
          0.2971570099024518 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8610665194372092, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1389334805627908, \
          0.9047441009815494, \
          0.0952558990184506, \
          0.9047441009815494, \
          0.9047441009815494, \
          0.0952558990184506, \
          0.9047441009815494, \
          0.0952558990184506, \
          0.0952558990184506, \
          0.2331729955597515, \
          0.7668270044402485, \
          0.2331729955597515, \
          0.2331729955597515, \
          0.7668270044402485, \
          0.2331729955597515, \
          0.7668270044402485, \
          0.7668270044402485, \
          0.6403862933256372, \
          0.3596137066743628, \
          0.6403862933256372, \
          0.6403862933256372, \
          0.3596137066743628, \
          0.6403862933256372, \
          0.3596137066743628, \
          0.3596137066743628, \
          0.5000000000000000, \
          0.9019667336076422, \
          0.9019667336076422, \
          0.5000000000000000, \
          0.9019667336076422, \
          0.9019667336076422, \
          0.5000000000000000, \
          0.0980332663923578, \
          0.0980332663923578, \
          0.5000000000000000, \
          0.0980332663923578, \
          0.0980332663923578, \
          0.9900497455045357, \
          0.9900497455045357, \
          0.2346080844030868, \
          0.9900497455045357, \
          0.9900497455045357, \
          0.2346080844030868, \
          0.0099502544954643, \
          0.0099502544954643, \
          0.2346080844030868, \
          0.0099502544954643, \
          0.0099502544954643, \
          0.2346080844030868, \
          0.9900497455045357, \
          0.9900497455045357, \
          0.7653919155969132, \
          0.9900497455045357, \
          0.9900497455045357, \
          0.7653919155969132, \
          0.0099502544954643, \
          0.0099502544954643, \
          0.7653919155969132, \
          0.0099502544954643, \
          0.0099502544954643, \
          0.7653919155969132, \
          0.7028429900975481, \
          0.7028429900975481, \
          0.9772916094647830, \
          0.7028429900975481, \
          0.7028429900975481, \
          0.9772916094647830, \
          0.2971570099024518, \
          0.2971570099024518, \
          0.9772916094647830, \
          0.2971570099024518, \
          0.2971570099024518, \
          0.9772916094647830, \
          0.7028429900975481, \
          0.7028429900975481, \
          0.0227083905352169, \
          0.7028429900975481, \
          0.7028429900975481, \
          0.0227083905352169, \
          0.2971570099024518, \
          0.2971570099024518, \
          0.0227083905352169, \
          0.2971570099024518, \
          0.2971570099024518, \
          0.0227083905352169 ] )

  w = np.array ( [ \
          0.0296169245240206, \
          0.0296169245240206, \
          0.0296169245240206, \
          0.0296169245240206, \
          0.0296169245240206, \
          0.0296169245240206, \
          0.0077511837875231, \
          0.0077511837875231, \
          0.0077511837875231, \
          0.0077511837875231, \
          0.0077511837875231, \
          0.0077511837875231, \
          0.0077511837875231, \
          0.0077511837875231, \
          0.0222210081090505, \
          0.0222210081090505, \
          0.0222210081090505, \
          0.0222210081090505, \
          0.0222210081090505, \
          0.0222210081090505, \
          0.0222210081090505, \
          0.0222210081090505, \
          0.0169887021445520, \
          0.0169887021445520, \
          0.0169887021445520, \
          0.0169887021445520, \
          0.0169887021445520, \
          0.0169887021445520, \
          0.0169887021445520, \
          0.0169887021445520, \
          0.0160272817769356, \
          0.0160272817769356, \
          0.0160272817769356, \
          0.0160272817769356, \
          0.0160272817769356, \
          0.0160272817769356, \
          0.0160272817769356, \
          0.0160272817769356, \
          0.0160272817769356, \
          0.0160272817769356, \
          0.0160272817769356, \
          0.0160272817769356, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0016188211900323, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196, \
          0.0089763421101196 ] )

  return x, y, z, w

def rule13 ( ):

#*****************************************************************************80
#
## rule13() returns the hexahedron quadrature rule of precision 13.
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
#    05 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which add to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.1827950053146007, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8172049946853993, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9539270239814177, \
          0.0460729760185823, \
          0.0460729760185823, \
          0.9539270239814177, \
          0.9539270239814177, \
          0.0460729760185823, \
          0.9539270239814177, \
          0.0460729760185823, \
          0.3818973707741769, \
          0.6181026292258232, \
          0.6181026292258232, \
          0.3818973707741769, \
          0.3818973707741769, \
          0.6181026292258232, \
          0.3818973707741769, \
          0.6181026292258232, \
          0.8687873171566183, \
          0.5000000000000000, \
          0.8687873171566183, \
          0.1312126828433817, \
          0.5000000000000000, \
          0.1312126828433817, \
          0.8687873171566183, \
          0.5000000000000000, \
          0.8687873171566183, \
          0.1312126828433817, \
          0.5000000000000000, \
          0.1312126828433817, \
          0.7303580738482240, \
          0.2696419261517760, \
          0.7303580738482240, \
          0.2696419261517760, \
          0.7303580738482240, \
          0.2696419261517760, \
          0.7303580738482240, \
          0.2696419261517760, \
          0.9666726015054183, \
          0.0333273984945817, \
          0.0333273984945817, \
          0.9666726015054183, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9666726015054183, \
          0.0333273984945817, \
          0.0333273984945817, \
          0.9666726015054183, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6866920757899998, \
          0.8321081947965769, \
          0.6866920757899998, \
          0.3133079242100002, \
          0.8321081947965769, \
          0.3133079242100002, \
          0.3133079242100002, \
          0.8321081947965769, \
          0.3133079242100002, \
          0.6866920757899998, \
          0.8321081947965769, \
          0.6866920757899998, \
          0.6866920757899998, \
          0.1678918052034231, \
          0.6866920757899998, \
          0.3133079242100002, \
          0.1678918052034231, \
          0.3133079242100002, \
          0.3133079242100002, \
          0.1678918052034231, \
          0.3133079242100002, \
          0.6866920757899998, \
          0.1678918052034231, \
          0.6866920757899998, \
          0.9747555407321407, \
          0.6288381939284606, \
          0.9747555407321407, \
          0.0252444592678593, \
          0.6288381939284606, \
          0.0252444592678593, \
          0.0252444592678593, \
          0.6288381939284606, \
          0.0252444592678593, \
          0.9747555407321407, \
          0.6288381939284606, \
          0.9747555407321407, \
          0.9747555407321407, \
          0.3711618060715394, \
          0.9747555407321407, \
          0.0252444592678593, \
          0.3711618060715394, \
          0.0252444592678593, \
          0.0252444592678593, \
          0.3711618060715394, \
          0.0252444592678593, \
          0.9747555407321407, \
          0.3711618060715394, \
          0.9747555407321407, \
          0.8328347413800889, \
          0.9974350214009486, \
          0.8328347413800889, \
          0.1671652586199110, \
          0.9974350214009486, \
          0.1671652586199110, \
          0.1671652586199110, \
          0.9974350214009486, \
          0.1671652586199110, \
          0.8328347413800889, \
          0.9974350214009486, \
          0.8328347413800889, \
          0.8328347413800889, \
          0.0025649785990514, \
          0.8328347413800889, \
          0.1671652586199110, \
          0.0025649785990514, \
          0.1671652586199110, \
          0.1671652586199110, \
          0.0025649785990514, \
          0.1671652586199110, \
          0.8328347413800889, \
          0.0025649785990514, \
          0.8328347413800889, \
          0.0974495447483840, \
          0.2739297470225850, \
          0.0974495447483840, \
          0.9025504552516159, \
          0.2739297470225850, \
          0.9025504552516159, \
          0.9025504552516159, \
          0.2739297470225850, \
          0.9025504552516159, \
          0.0974495447483840, \
          0.2739297470225850, \
          0.0974495447483840, \
          0.0974495447483840, \
          0.7260702529774150, \
          0.0974495447483840, \
          0.9025504552516159, \
          0.7260702529774150, \
          0.9025504552516159, \
          0.9025504552516159, \
          0.7260702529774150, \
          0.9025504552516159, \
          0.0974495447483840, \
          0.7260702529774150, \
          0.0974495447483840 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.1827950053146007, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8172049946853993, \
          0.5000000000000000, \
          0.9539270239814177, \
          0.0460729760185823, \
          0.9539270239814177, \
          0.0460729760185823, \
          0.9539270239814177, \
          0.0460729760185823, \
          0.0460729760185823, \
          0.9539270239814177, \
          0.3818973707741769, \
          0.6181026292258232, \
          0.3818973707741769, \
          0.6181026292258232, \
          0.3818973707741769, \
          0.6181026292258232, \
          0.6181026292258232, \
          0.3818973707741769, \
          0.8687873171566183, \
          0.8687873171566183, \
          0.5000000000000000, \
          0.8687873171566183, \
          0.1312126828433817, \
          0.5000000000000000, \
          0.1312126828433817, \
          0.8687873171566183, \
          0.5000000000000000, \
          0.1312126828433817, \
          0.1312126828433817, \
          0.5000000000000000, \
          0.9666726015054183, \
          0.0333273984945817, \
          0.0333273984945817, \
          0.9666726015054183, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.7303580738482240, \
          0.2696419261517760, \
          0.7303580738482240, \
          0.2696419261517760, \
          0.7303580738482240, \
          0.2696419261517760, \
          0.7303580738482240, \
          0.2696419261517760, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9666726015054183, \
          0.0333273984945817, \
          0.0333273984945817, \
          0.9666726015054183, \
          0.8321081947965769, \
          0.6866920757899998, \
          0.6866920757899998, \
          0.8321081947965769, \
          0.3133079242100002, \
          0.6866920757899998, \
          0.8321081947965769, \
          0.3133079242100002, \
          0.3133079242100002, \
          0.8321081947965769, \
          0.6866920757899998, \
          0.3133079242100002, \
          0.1678918052034231, \
          0.6866920757899998, \
          0.6866920757899998, \
          0.1678918052034231, \
          0.3133079242100002, \
          0.6866920757899998, \
          0.1678918052034231, \
          0.3133079242100002, \
          0.3133079242100002, \
          0.1678918052034231, \
          0.6866920757899998, \
          0.3133079242100002, \
          0.6288381939284606, \
          0.9747555407321407, \
          0.9747555407321407, \
          0.6288381939284606, \
          0.0252444592678593, \
          0.9747555407321407, \
          0.6288381939284606, \
          0.0252444592678593, \
          0.0252444592678593, \
          0.6288381939284606, \
          0.9747555407321407, \
          0.0252444592678593, \
          0.3711618060715394, \
          0.9747555407321407, \
          0.9747555407321407, \
          0.3711618060715394, \
          0.0252444592678593, \
          0.9747555407321407, \
          0.3711618060715394, \
          0.0252444592678593, \
          0.0252444592678593, \
          0.3711618060715394, \
          0.9747555407321407, \
          0.0252444592678593, \
          0.9974350214009486, \
          0.8328347413800889, \
          0.8328347413800889, \
          0.9974350214009486, \
          0.1671652586199110, \
          0.8328347413800889, \
          0.9974350214009486, \
          0.1671652586199110, \
          0.1671652586199110, \
          0.9974350214009486, \
          0.8328347413800889, \
          0.1671652586199110, \
          0.0025649785990514, \
          0.8328347413800889, \
          0.8328347413800889, \
          0.0025649785990514, \
          0.1671652586199110, \
          0.8328347413800889, \
          0.0025649785990514, \
          0.1671652586199110, \
          0.1671652586199110, \
          0.0025649785990514, \
          0.8328347413800889, \
          0.1671652586199110, \
          0.2739297470225850, \
          0.0974495447483840, \
          0.0974495447483840, \
          0.2739297470225850, \
          0.9025504552516159, \
          0.0974495447483840, \
          0.2739297470225850, \
          0.9025504552516159, \
          0.9025504552516159, \
          0.2739297470225850, \
          0.0974495447483840, \
          0.9025504552516159, \
          0.7260702529774150, \
          0.0974495447483840, \
          0.0974495447483840, \
          0.7260702529774150, \
          0.9025504552516159, \
          0.0974495447483840, \
          0.7260702529774150, \
          0.9025504552516159, \
          0.9025504552516159, \
          0.7260702529774150, \
          0.0974495447483840, \
          0.9025504552516159 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1827950053146007, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8172049946853993, \
          0.9539270239814177, \
          0.0460729760185823, \
          0.9539270239814177, \
          0.9539270239814177, \
          0.0460729760185823, \
          0.9539270239814177, \
          0.0460729760185823, \
          0.0460729760185823, \
          0.3818973707741769, \
          0.6181026292258232, \
          0.3818973707741769, \
          0.3818973707741769, \
          0.6181026292258232, \
          0.3818973707741769, \
          0.6181026292258232, \
          0.6181026292258232, \
          0.5000000000000000, \
          0.8687873171566183, \
          0.8687873171566183, \
          0.5000000000000000, \
          0.8687873171566183, \
          0.8687873171566183, \
          0.5000000000000000, \
          0.1312126828433817, \
          0.1312126828433817, \
          0.5000000000000000, \
          0.1312126828433817, \
          0.1312126828433817, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9666726015054183, \
          0.0333273984945817, \
          0.0333273984945817, \
          0.9666726015054183, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9666726015054183, \
          0.0333273984945817, \
          0.0333273984945817, \
          0.9666726015054183, \
          0.7303580738482240, \
          0.2696419261517760, \
          0.7303580738482240, \
          0.2696419261517760, \
          0.7303580738482240, \
          0.2696419261517760, \
          0.7303580738482240, \
          0.2696419261517760, \
          0.6866920757899998, \
          0.6866920757899998, \
          0.8321081947965769, \
          0.6866920757899998, \
          0.6866920757899998, \
          0.8321081947965769, \
          0.3133079242100002, \
          0.3133079242100002, \
          0.8321081947965769, \
          0.3133079242100002, \
          0.3133079242100002, \
          0.8321081947965769, \
          0.6866920757899998, \
          0.6866920757899998, \
          0.1678918052034231, \
          0.6866920757899998, \
          0.6866920757899998, \
          0.1678918052034231, \
          0.3133079242100002, \
          0.3133079242100002, \
          0.1678918052034231, \
          0.3133079242100002, \
          0.3133079242100002, \
          0.1678918052034231, \
          0.9747555407321407, \
          0.9747555407321407, \
          0.6288381939284606, \
          0.9747555407321407, \
          0.9747555407321407, \
          0.6288381939284606, \
          0.0252444592678593, \
          0.0252444592678593, \
          0.6288381939284606, \
          0.0252444592678593, \
          0.0252444592678593, \
          0.6288381939284606, \
          0.9747555407321407, \
          0.9747555407321407, \
          0.3711618060715394, \
          0.9747555407321407, \
          0.9747555407321407, \
          0.3711618060715394, \
          0.0252444592678593, \
          0.0252444592678593, \
          0.3711618060715394, \
          0.0252444592678593, \
          0.0252444592678593, \
          0.3711618060715394, \
          0.8328347413800889, \
          0.8328347413800889, \
          0.9974350214009486, \
          0.8328347413800889, \
          0.8328347413800889, \
          0.9974350214009486, \
          0.1671652586199110, \
          0.1671652586199110, \
          0.9974350214009486, \
          0.1671652586199110, \
          0.1671652586199110, \
          0.9974350214009486, \
          0.8328347413800889, \
          0.8328347413800889, \
          0.0025649785990514, \
          0.8328347413800889, \
          0.8328347413800889, \
          0.0025649785990514, \
          0.1671652586199110, \
          0.1671652586199110, \
          0.0025649785990514, \
          0.1671652586199110, \
          0.1671652586199110, \
          0.0025649785990514, \
          0.0974495447483840, \
          0.0974495447483840, \
          0.2739297470225850, \
          0.0974495447483840, \
          0.0974495447483840, \
          0.2739297470225850, \
          0.9025504552516159, \
          0.9025504552516159, \
          0.2739297470225850, \
          0.9025504552516159, \
          0.9025504552516159, \
          0.2739297470225850, \
          0.0974495447483840, \
          0.0974495447483840, \
          0.7260702529774150, \
          0.0974495447483840, \
          0.0974495447483840, \
          0.7260702529774150, \
          0.9025504552516159, \
          0.9025504552516159, \
          0.7260702529774150, \
          0.9025504552516159, \
          0.9025504552516159, \
          0.7260702529774150 ] )

  w = np.array ( [ \
          0.0173912824874704, \
          0.0173912824874704, \
          0.0173912824874704, \
          0.0173912824874704, \
          0.0173912824874704, \
          0.0173912824874704, \
          0.0018386577800611, \
          0.0018386577800611, \
          0.0018386577800611, \
          0.0018386577800611, \
          0.0018386577800611, \
          0.0018386577800611, \
          0.0018386577800611, \
          0.0018386577800611, \
          0.0112910248314292, \
          0.0112910248314292, \
          0.0112910248314292, \
          0.0112910248314292, \
          0.0112910248314292, \
          0.0112910248314292, \
          0.0112910248314292, \
          0.0112910248314292, \
          0.0059757596352895, \
          0.0059757596352895, \
          0.0059757596352895, \
          0.0059757596352895, \
          0.0059757596352895, \
          0.0059757596352895, \
          0.0059757596352895, \
          0.0059757596352895, \
          0.0059757596352895, \
          0.0059757596352895, \
          0.0059757596352895, \
          0.0059757596352895, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0086912315244171, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0106145587103426, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0016903589166661, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0022842405528399, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919, \
          0.0066740156523919 ] )

  return x, y, z, w

def rule15 ( ):

#*****************************************************************************80
#
## rule15() returns the hexahedron quadrature rule of precision 15.
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
#    05 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which add to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.9619577574752056, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0380422425247944, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.3913025693166751, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6086974306833248, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6692365934747126, \
          0.3307634065252874, \
          0.3307634065252874, \
          0.6692365934747126, \
          0.6692365934747126, \
          0.3307634065252874, \
          0.6692365934747126, \
          0.3307634065252874, \
          0.8965445655196689, \
          0.1034554344803311, \
          0.1034554344803311, \
          0.8965445655196689, \
          0.8965445655196689, \
          0.1034554344803311, \
          0.8965445655196689, \
          0.1034554344803311, \
          0.8482759513633358, \
          0.5000000000000000, \
          0.8482759513633358, \
          0.1517240486366642, \
          0.5000000000000000, \
          0.1517240486366642, \
          0.8482759513633358, \
          0.5000000000000000, \
          0.8482759513633358, \
          0.1517240486366642, \
          0.5000000000000000, \
          0.1517240486366642, \
          0.6321333796314236, \
          0.3678666203685764, \
          0.6321333796314236, \
          0.3678666203685764, \
          0.6321333796314236, \
          0.3678666203685764, \
          0.6321333796314236, \
          0.3678666203685764, \
          0.7924949743436622, \
          0.2075050256563378, \
          0.2075050256563378, \
          0.7924949743436622, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.7924949743436622, \
          0.2075050256563378, \
          0.2075050256563378, \
          0.7924949743436622, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.7764752956685337, \
          0.2235247043314663, \
          0.7764752956685337, \
          0.2235247043314663, \
          0.7764752956685337, \
          0.2235247043314663, \
          0.7764752956685337, \
          0.2235247043314663, \
          0.9914024363900886, \
          0.0085975636099114, \
          0.0085975636099114, \
          0.9914024363900886, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9914024363900886, \
          0.0085975636099114, \
          0.0085975636099114, \
          0.9914024363900886, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6360162945430453, \
          0.9390447038366581, \
          0.6360162945430453, \
          0.3639837054569547, \
          0.9390447038366581, \
          0.3639837054569547, \
          0.3639837054569547, \
          0.9390447038366581, \
          0.3639837054569547, \
          0.6360162945430453, \
          0.9390447038366581, \
          0.6360162945430453, \
          0.6360162945430453, \
          0.0609552961633420, \
          0.6360162945430453, \
          0.3639837054569547, \
          0.0609552961633420, \
          0.3639837054569547, \
          0.3639837054569547, \
          0.0609552961633420, \
          0.3639837054569547, \
          0.6360162945430453, \
          0.0609552961633420, \
          0.6360162945430453, \
          0.8093239300427761, \
          0.9699906676537717, \
          0.8093239300427761, \
          0.1906760699572239, \
          0.9699906676537717, \
          0.1906760699572239, \
          0.1906760699572239, \
          0.9699906676537717, \
          0.1906760699572239, \
          0.8093239300427761, \
          0.9699906676537717, \
          0.8093239300427761, \
          0.8093239300427761, \
          0.0300093323462282, \
          0.8093239300427761, \
          0.1906760699572239, \
          0.0300093323462282, \
          0.1906760699572239, \
          0.1906760699572239, \
          0.0300093323462282, \
          0.1906760699572239, \
          0.8093239300427761, \
          0.0300093323462282, \
          0.8093239300427761, \
          0.9315772312765189, \
          0.6521112975876302, \
          0.9315772312765189, \
          0.0684227687234810, \
          0.6521112975876302, \
          0.0684227687234810, \
          0.0684227687234810, \
          0.6521112975876302, \
          0.0684227687234810, \
          0.9315772312765189, \
          0.6521112975876302, \
          0.9315772312765189, \
          0.9315772312765189, \
          0.3478887024123698, \
          0.9315772312765189, \
          0.0684227687234810, \
          0.3478887024123698, \
          0.0684227687234810, \
          0.0684227687234810, \
          0.3478887024123698, \
          0.0684227687234810, \
          0.9315772312765189, \
          0.3478887024123698, \
          0.9315772312765189, \
          0.7308028863234025, \
          0.8685680591748091, \
          0.7308028863234025, \
          0.2691971136765975, \
          0.8685680591748091, \
          0.2691971136765975, \
          0.2691971136765975, \
          0.8685680591748091, \
          0.2691971136765975, \
          0.7308028863234025, \
          0.8685680591748091, \
          0.7308028863234025, \
          0.7308028863234025, \
          0.1314319408251909, \
          0.7308028863234025, \
          0.2691971136765975, \
          0.1314319408251909, \
          0.2691971136765975, \
          0.2691971136765975, \
          0.1314319408251909, \
          0.2691971136765975, \
          0.7308028863234025, \
          0.1314319408251909, \
          0.7308028863234025, \
          0.9801570902708128, \
          0.8835073040170505, \
          0.9801570902708128, \
          0.0198429097291872, \
          0.8835073040170505, \
          0.0198429097291872, \
          0.0198429097291872, \
          0.8835073040170505, \
          0.0198429097291872, \
          0.9801570902708128, \
          0.8835073040170505, \
          0.9801570902708128, \
          0.9801570902708128, \
          0.1164926959829496, \
          0.9801570902708128, \
          0.0198429097291872, \
          0.1164926959829496, \
          0.0198429097291872, \
          0.0198429097291872, \
          0.1164926959829496, \
          0.0198429097291872, \
          0.9801570902708128, \
          0.1164926959829496, \
          0.9801570902708128, \
          0.6401259198958773, \
          0.6401259198958773, \
          0.9442969164789898, \
          0.9971300972924322, \
          0.9442969164789898, \
          0.9971300972924322, \
          0.3598740801041227, \
          0.3598740801041227, \
          0.9442969164789898, \
          0.9971300972924322, \
          0.9442969164789898, \
          0.9971300972924322, \
          0.6401259198958773, \
          0.6401259198958773, \
          0.0557030835210102, \
          0.9971300972924322, \
          0.0557030835210102, \
          0.9971300972924322, \
          0.6401259198958773, \
          0.6401259198958773, \
          0.9442969164789898, \
          0.0028699027075679, \
          0.9442969164789898, \
          0.0028699027075679, \
          0.3598740801041227, \
          0.3598740801041227, \
          0.0557030835210102, \
          0.9971300972924322, \
          0.0557030835210102, \
          0.9971300972924322, \
          0.3598740801041227, \
          0.3598740801041227, \
          0.9442969164789898, \
          0.0028699027075679, \
          0.9442969164789898, \
          0.0028699027075679, \
          0.6401259198958773, \
          0.6401259198958773, \
          0.0557030835210102, \
          0.0028699027075679, \
          0.0557030835210102, \
          0.0028699027075679, \
          0.3598740801041227, \
          0.3598740801041227, \
          0.0557030835210102, \
          0.0028699027075679, \
          0.0557030835210102, \
          0.0028699027075679 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.9619577574752056, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0380422425247944, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.3913025693166751, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6086974306833248, \
          0.5000000000000000, \
          0.6692365934747126, \
          0.3307634065252874, \
          0.6692365934747126, \
          0.3307634065252874, \
          0.6692365934747126, \
          0.3307634065252874, \
          0.3307634065252874, \
          0.6692365934747126, \
          0.8965445655196689, \
          0.1034554344803311, \
          0.8965445655196689, \
          0.1034554344803311, \
          0.8965445655196689, \
          0.1034554344803311, \
          0.1034554344803311, \
          0.8965445655196689, \
          0.8482759513633358, \
          0.8482759513633358, \
          0.5000000000000000, \
          0.8482759513633358, \
          0.1517240486366642, \
          0.5000000000000000, \
          0.1517240486366642, \
          0.8482759513633358, \
          0.5000000000000000, \
          0.1517240486366642, \
          0.1517240486366642, \
          0.5000000000000000, \
          0.7924949743436622, \
          0.2075050256563378, \
          0.2075050256563378, \
          0.7924949743436622, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6321333796314236, \
          0.3678666203685764, \
          0.6321333796314236, \
          0.3678666203685764, \
          0.6321333796314236, \
          0.3678666203685764, \
          0.6321333796314236, \
          0.3678666203685764, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.7924949743436622, \
          0.2075050256563378, \
          0.2075050256563378, \
          0.7924949743436622, \
          0.9914024363900886, \
          0.0085975636099114, \
          0.0085975636099114, \
          0.9914024363900886, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.7764752956685337, \
          0.2235247043314663, \
          0.7764752956685337, \
          0.2235247043314663, \
          0.7764752956685337, \
          0.2235247043314663, \
          0.7764752956685337, \
          0.2235247043314663, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9914024363900886, \
          0.0085975636099114, \
          0.0085975636099114, \
          0.9914024363900886, \
          0.9390447038366581, \
          0.6360162945430453, \
          0.6360162945430453, \
          0.9390447038366581, \
          0.3639837054569547, \
          0.6360162945430453, \
          0.9390447038366581, \
          0.3639837054569547, \
          0.3639837054569547, \
          0.9390447038366581, \
          0.6360162945430453, \
          0.3639837054569547, \
          0.0609552961633420, \
          0.6360162945430453, \
          0.6360162945430453, \
          0.0609552961633420, \
          0.3639837054569547, \
          0.6360162945430453, \
          0.0609552961633420, \
          0.3639837054569547, \
          0.3639837054569547, \
          0.0609552961633420, \
          0.6360162945430453, \
          0.3639837054569547, \
          0.9699906676537717, \
          0.8093239300427761, \
          0.8093239300427761, \
          0.9699906676537717, \
          0.1906760699572239, \
          0.8093239300427761, \
          0.9699906676537717, \
          0.1906760699572239, \
          0.1906760699572239, \
          0.9699906676537717, \
          0.8093239300427761, \
          0.1906760699572239, \
          0.0300093323462282, \
          0.8093239300427761, \
          0.8093239300427761, \
          0.0300093323462282, \
          0.1906760699572239, \
          0.8093239300427761, \
          0.0300093323462282, \
          0.1906760699572239, \
          0.1906760699572239, \
          0.0300093323462282, \
          0.8093239300427761, \
          0.1906760699572239, \
          0.6521112975876302, \
          0.9315772312765189, \
          0.9315772312765189, \
          0.6521112975876302, \
          0.0684227687234810, \
          0.9315772312765189, \
          0.6521112975876302, \
          0.0684227687234810, \
          0.0684227687234810, \
          0.6521112975876302, \
          0.9315772312765189, \
          0.0684227687234810, \
          0.3478887024123698, \
          0.9315772312765189, \
          0.9315772312765189, \
          0.3478887024123698, \
          0.0684227687234810, \
          0.9315772312765189, \
          0.3478887024123698, \
          0.0684227687234810, \
          0.0684227687234810, \
          0.3478887024123698, \
          0.9315772312765189, \
          0.0684227687234810, \
          0.8685680591748091, \
          0.7308028863234025, \
          0.7308028863234025, \
          0.8685680591748091, \
          0.2691971136765975, \
          0.7308028863234025, \
          0.8685680591748091, \
          0.2691971136765975, \
          0.2691971136765975, \
          0.8685680591748091, \
          0.7308028863234025, \
          0.2691971136765975, \
          0.1314319408251909, \
          0.7308028863234025, \
          0.7308028863234025, \
          0.1314319408251909, \
          0.2691971136765975, \
          0.7308028863234025, \
          0.1314319408251909, \
          0.2691971136765975, \
          0.2691971136765975, \
          0.1314319408251909, \
          0.7308028863234025, \
          0.2691971136765975, \
          0.8835073040170505, \
          0.9801570902708128, \
          0.9801570902708128, \
          0.8835073040170505, \
          0.0198429097291872, \
          0.9801570902708128, \
          0.8835073040170505, \
          0.0198429097291872, \
          0.0198429097291872, \
          0.8835073040170505, \
          0.9801570902708128, \
          0.0198429097291872, \
          0.1164926959829496, \
          0.9801570902708128, \
          0.9801570902708128, \
          0.1164926959829496, \
          0.0198429097291872, \
          0.9801570902708128, \
          0.1164926959829496, \
          0.0198429097291872, \
          0.0198429097291872, \
          0.1164926959829496, \
          0.9801570902708128, \
          0.0198429097291872, \
          0.9442969164789898, \
          0.9971300972924322, \
          0.6401259198958773, \
          0.6401259198958773, \
          0.9971300972924322, \
          0.9442969164789898, \
          0.9442969164789898, \
          0.9971300972924322, \
          0.3598740801041227, \
          0.3598740801041227, \
          0.9971300972924322, \
          0.9442969164789898, \
          0.0557030835210102, \
          0.9971300972924322, \
          0.6401259198958773, \
          0.6401259198958773, \
          0.9971300972924322, \
          0.0557030835210102, \
          0.9442969164789898, \
          0.0028699027075679, \
          0.6401259198958773, \
          0.6401259198958773, \
          0.0028699027075679, \
          0.9442969164789898, \
          0.0557030835210102, \
          0.9971300972924322, \
          0.3598740801041227, \
          0.3598740801041227, \
          0.9971300972924322, \
          0.0557030835210102, \
          0.9442969164789898, \
          0.0028699027075679, \
          0.3598740801041227, \
          0.3598740801041227, \
          0.0028699027075679, \
          0.9442969164789898, \
          0.0557030835210102, \
          0.0028699027075679, \
          0.6401259198958773, \
          0.6401259198958773, \
          0.0028699027075679, \
          0.0557030835210102, \
          0.0557030835210102, \
          0.0028699027075679, \
          0.3598740801041227, \
          0.3598740801041227, \
          0.0028699027075679, \
          0.0557030835210102 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9619577574752056, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0380422425247944, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.3913025693166751, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6086974306833248, \
          0.6692365934747126, \
          0.3307634065252874, \
          0.6692365934747126, \
          0.6692365934747126, \
          0.3307634065252874, \
          0.6692365934747126, \
          0.3307634065252874, \
          0.3307634065252874, \
          0.8965445655196689, \
          0.1034554344803311, \
          0.8965445655196689, \
          0.8965445655196689, \
          0.1034554344803311, \
          0.8965445655196689, \
          0.1034554344803311, \
          0.1034554344803311, \
          0.5000000000000000, \
          0.8482759513633358, \
          0.8482759513633358, \
          0.5000000000000000, \
          0.8482759513633358, \
          0.8482759513633358, \
          0.5000000000000000, \
          0.1517240486366642, \
          0.1517240486366642, \
          0.5000000000000000, \
          0.1517240486366642, \
          0.1517240486366642, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.7924949743436622, \
          0.2075050256563378, \
          0.2075050256563378, \
          0.7924949743436622, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.7924949743436622, \
          0.2075050256563378, \
          0.2075050256563378, \
          0.7924949743436622, \
          0.6321333796314236, \
          0.3678666203685764, \
          0.6321333796314236, \
          0.3678666203685764, \
          0.6321333796314236, \
          0.3678666203685764, \
          0.6321333796314236, \
          0.3678666203685764, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9914024363900886, \
          0.0085975636099114, \
          0.0085975636099114, \
          0.9914024363900886, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9914024363900886, \
          0.0085975636099114, \
          0.0085975636099114, \
          0.9914024363900886, \
          0.7764752956685337, \
          0.2235247043314663, \
          0.7764752956685337, \
          0.2235247043314663, \
          0.7764752956685337, \
          0.2235247043314663, \
          0.7764752956685337, \
          0.2235247043314663, \
          0.6360162945430453, \
          0.6360162945430453, \
          0.9390447038366581, \
          0.6360162945430453, \
          0.6360162945430453, \
          0.9390447038366581, \
          0.3639837054569547, \
          0.3639837054569547, \
          0.9390447038366581, \
          0.3639837054569547, \
          0.3639837054569547, \
          0.9390447038366581, \
          0.6360162945430453, \
          0.6360162945430453, \
          0.0609552961633420, \
          0.6360162945430453, \
          0.6360162945430453, \
          0.0609552961633420, \
          0.3639837054569547, \
          0.3639837054569547, \
          0.0609552961633420, \
          0.3639837054569547, \
          0.3639837054569547, \
          0.0609552961633420, \
          0.8093239300427761, \
          0.8093239300427761, \
          0.9699906676537717, \
          0.8093239300427761, \
          0.8093239300427761, \
          0.9699906676537717, \
          0.1906760699572239, \
          0.1906760699572239, \
          0.9699906676537717, \
          0.1906760699572239, \
          0.1906760699572239, \
          0.9699906676537717, \
          0.8093239300427761, \
          0.8093239300427761, \
          0.0300093323462282, \
          0.8093239300427761, \
          0.8093239300427761, \
          0.0300093323462282, \
          0.1906760699572239, \
          0.1906760699572239, \
          0.0300093323462282, \
          0.1906760699572239, \
          0.1906760699572239, \
          0.0300093323462282, \
          0.9315772312765189, \
          0.9315772312765189, \
          0.6521112975876302, \
          0.9315772312765189, \
          0.9315772312765189, \
          0.6521112975876302, \
          0.0684227687234810, \
          0.0684227687234810, \
          0.6521112975876302, \
          0.0684227687234810, \
          0.0684227687234810, \
          0.6521112975876302, \
          0.9315772312765189, \
          0.9315772312765189, \
          0.3478887024123698, \
          0.9315772312765189, \
          0.9315772312765189, \
          0.3478887024123698, \
          0.0684227687234810, \
          0.0684227687234810, \
          0.3478887024123698, \
          0.0684227687234810, \
          0.0684227687234810, \
          0.3478887024123698, \
          0.7308028863234025, \
          0.7308028863234025, \
          0.8685680591748091, \
          0.7308028863234025, \
          0.7308028863234025, \
          0.8685680591748091, \
          0.2691971136765975, \
          0.2691971136765975, \
          0.8685680591748091, \
          0.2691971136765975, \
          0.2691971136765975, \
          0.8685680591748091, \
          0.7308028863234025, \
          0.7308028863234025, \
          0.1314319408251909, \
          0.7308028863234025, \
          0.7308028863234025, \
          0.1314319408251909, \
          0.2691971136765975, \
          0.2691971136765975, \
          0.1314319408251909, \
          0.2691971136765975, \
          0.2691971136765975, \
          0.1314319408251909, \
          0.9801570902708128, \
          0.9801570902708128, \
          0.8835073040170505, \
          0.9801570902708128, \
          0.9801570902708128, \
          0.8835073040170505, \
          0.0198429097291872, \
          0.0198429097291872, \
          0.8835073040170505, \
          0.0198429097291872, \
          0.0198429097291872, \
          0.8835073040170505, \
          0.9801570902708128, \
          0.9801570902708128, \
          0.1164926959829496, \
          0.9801570902708128, \
          0.9801570902708128, \
          0.1164926959829496, \
          0.0198429097291872, \
          0.0198429097291872, \
          0.1164926959829496, \
          0.0198429097291872, \
          0.0198429097291872, \
          0.1164926959829496, \
          0.9971300972924322, \
          0.9442969164789898, \
          0.9971300972924322, \
          0.9442969164789898, \
          0.6401259198958773, \
          0.6401259198958773, \
          0.9971300972924322, \
          0.9442969164789898, \
          0.9971300972924322, \
          0.9442969164789898, \
          0.3598740801041227, \
          0.3598740801041227, \
          0.9971300972924322, \
          0.0557030835210102, \
          0.9971300972924322, \
          0.0557030835210102, \
          0.6401259198958773, \
          0.6401259198958773, \
          0.0028699027075679, \
          0.9442969164789898, \
          0.0028699027075679, \
          0.9442969164789898, \
          0.6401259198958773, \
          0.6401259198958773, \
          0.9971300972924322, \
          0.0557030835210102, \
          0.9971300972924322, \
          0.0557030835210102, \
          0.3598740801041227, \
          0.3598740801041227, \
          0.0028699027075679, \
          0.9442969164789898, \
          0.0028699027075679, \
          0.9442969164789898, \
          0.3598740801041227, \
          0.3598740801041227, \
          0.0028699027075679, \
          0.0557030835210102, \
          0.0028699027075679, \
          0.0557030835210102, \
          0.6401259198958773, \
          0.6401259198958773, \
          0.0028699027075679, \
          0.0557030835210102, \
          0.0028699027075679, \
          0.0557030835210102, \
          0.3598740801041227, \
          0.3598740801041227 ] )

  w = np.array ( [ \
          0.0033403050106945, \
          0.0033403050106945, \
          0.0033403050106945, \
          0.0033403050106945, \
          0.0033403050106945, \
          0.0033403050106945, \
          0.0050185523378773, \
          0.0050185523378773, \
          0.0050185523378773, \
          0.0050185523378773, \
          0.0050185523378773, \
          0.0050185523378773, \
          0.0090827588172248, \
          0.0090827588172248, \
          0.0090827588172248, \
          0.0090827588172248, \
          0.0090827588172248, \
          0.0090827588172248, \
          0.0090827588172248, \
          0.0090827588172248, \
          0.0029364087383876, \
          0.0029364087383876, \
          0.0029364087383876, \
          0.0029364087383876, \
          0.0029364087383876, \
          0.0029364087383876, \
          0.0029364087383876, \
          0.0029364087383876, \
          0.0093182386470488, \
          0.0093182386470488, \
          0.0093182386470488, \
          0.0093182386470488, \
          0.0093182386470488, \
          0.0093182386470488, \
          0.0093182386470488, \
          0.0093182386470488, \
          0.0093182386470488, \
          0.0093182386470488, \
          0.0093182386470488, \
          0.0093182386470488, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0069907862357511, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0028410057474906, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0053095740723308, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035708945365673, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0035058721795857, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0066651990511383, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0007781518386120, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597, \
          0.0006249800796597 ] )

  return x, y, z, w

def rule17 ( ):

#*****************************************************************************80
#
## rule17() returns the hexahedron quadrature rule of precision 17.
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
#    05 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which add to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.7426575151151338, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.2573424848848662, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8703394079370492, \
          0.1296605920629508, \
          0.1296605920629508, \
          0.8703394079370492, \
          0.8703394079370492, \
          0.1296605920629508, \
          0.8703394079370492, \
          0.1296605920629508, \
          0.9999997917911259, \
          0.0000002082088741, \
          0.0000002082088741, \
          0.9999997917911259, \
          0.9999997917911259, \
          0.0000002082088741, \
          0.9999997917911259, \
          0.0000002082088741, \
          0.8773134026065881, \
          0.5000000000000000, \
          0.8773134026065881, \
          0.1226865973934119, \
          0.5000000000000000, \
          0.1226865973934119, \
          0.8773134026065881, \
          0.5000000000000000, \
          0.8773134026065881, \
          0.1226865973934119, \
          0.5000000000000000, \
          0.1226865973934119, \
          0.7748409070843456, \
          0.5000000000000000, \
          0.7748409070843456, \
          0.2251590929156544, \
          0.5000000000000000, \
          0.2251590929156544, \
          0.7748409070843456, \
          0.5000000000000000, \
          0.7748409070843456, \
          0.2251590929156544, \
          0.5000000000000000, \
          0.2251590929156544, \
          0.9998342518711405, \
          0.5000000000000000, \
          0.9998342518711405, \
          0.0001657481288594, \
          0.5000000000000000, \
          0.0001657481288594, \
          0.9998342518711405, \
          0.5000000000000000, \
          0.9998342518711405, \
          0.0001657481288594, \
          0.5000000000000000, \
          0.0001657481288594, \
          0.8078645495842367, \
          0.1921354504157633, \
          0.8078645495842367, \
          0.1921354504157633, \
          0.8078645495842367, \
          0.1921354504157633, \
          0.8078645495842367, \
          0.1921354504157633, \
          0.9765209703524975, \
          0.0234790296475025, \
          0.0234790296475025, \
          0.9765209703524975, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9765209703524975, \
          0.0234790296475025, \
          0.0234790296475025, \
          0.9765209703524975, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6378406365996775, \
          0.3621593634003225, \
          0.6378406365996775, \
          0.3621593634003225, \
          0.6378406365996775, \
          0.3621593634003225, \
          0.6378406365996775, \
          0.3621593634003225, \
          0.9085620340535459, \
          0.0914379659464542, \
          0.0914379659464542, \
          0.9085620340535459, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9085620340535459, \
          0.0914379659464542, \
          0.0914379659464542, \
          0.9085620340535459, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6276714770186411, \
          0.9848870223309694, \
          0.6276714770186411, \
          0.3723285229813589, \
          0.9848870223309694, \
          0.3723285229813589, \
          0.3723285229813589, \
          0.9848870223309694, \
          0.3723285229813589, \
          0.6276714770186411, \
          0.9848870223309694, \
          0.6276714770186411, \
          0.6276714770186411, \
          0.0151129776690307, \
          0.6276714770186411, \
          0.3723285229813589, \
          0.0151129776690307, \
          0.3723285229813589, \
          0.3723285229813589, \
          0.0151129776690307, \
          0.3723285229813589, \
          0.6276714770186411, \
          0.0151129776690307, \
          0.6276714770186411, \
          0.9676181924490221, \
          0.8733616537091691, \
          0.9676181924490221, \
          0.0323818075509779, \
          0.8733616537091691, \
          0.0323818075509779, \
          0.0323818075509779, \
          0.8733616537091691, \
          0.0323818075509779, \
          0.9676181924490221, \
          0.8733616537091691, \
          0.9676181924490221, \
          0.9676181924490221, \
          0.1266383462908310, \
          0.9676181924490221, \
          0.0323818075509779, \
          0.1266383462908310, \
          0.0323818075509779, \
          0.0323818075509779, \
          0.1266383462908310, \
          0.0323818075509779, \
          0.9676181924490221, \
          0.1266383462908310, \
          0.9676181924490221, \
          0.6715295730694326, \
          0.8093319789042792, \
          0.6715295730694326, \
          0.3284704269305673, \
          0.8093319789042792, \
          0.3284704269305673, \
          0.3284704269305673, \
          0.8093319789042792, \
          0.3284704269305673, \
          0.6715295730694326, \
          0.8093319789042792, \
          0.6715295730694326, \
          0.6715295730694326, \
          0.1906680210957207, \
          0.6715295730694326, \
          0.3284704269305673, \
          0.1906680210957207, \
          0.3284704269305673, \
          0.3284704269305673, \
          0.1906680210957207, \
          0.3284704269305673, \
          0.6715295730694326, \
          0.1906680210957207, \
          0.6715295730694326, \
          0.6277920800575361, \
          0.4229648752978111, \
          0.6277920800575361, \
          0.3722079199424639, \
          0.4229648752978111, \
          0.3722079199424639, \
          0.3722079199424639, \
          0.4229648752978111, \
          0.3722079199424639, \
          0.6277920800575361, \
          0.4229648752978111, \
          0.6277920800575361, \
          0.6277920800575361, \
          0.5770351247021889, \
          0.6277920800575361, \
          0.3722079199424639, \
          0.5770351247021889, \
          0.3722079199424639, \
          0.3722079199424639, \
          0.5770351247021889, \
          0.3722079199424639, \
          0.6277920800575361, \
          0.5770351247021889, \
          0.6277920800575361, \
          0.7708105708234440, \
          0.9478284758927406, \
          0.7708105708234440, \
          0.2291894291765560, \
          0.9478284758927406, \
          0.2291894291765560, \
          0.2291894291765560, \
          0.9478284758927406, \
          0.2291894291765560, \
          0.7708105708234440, \
          0.9478284758927406, \
          0.7708105708234440, \
          0.7708105708234440, \
          0.0521715241072594, \
          0.7708105708234440, \
          0.2291894291765560, \
          0.0521715241072594, \
          0.2291894291765560, \
          0.2291894291765560, \
          0.0521715241072594, \
          0.2291894291765560, \
          0.7708105708234440, \
          0.0521715241072594, \
          0.7708105708234440, \
          0.9437280545720244, \
          0.6207324889467394, \
          0.9437280545720244, \
          0.0562719454279757, \
          0.6207324889467394, \
          0.0562719454279757, \
          0.0562719454279757, \
          0.6207324889467394, \
          0.0562719454279757, \
          0.9437280545720244, \
          0.6207324889467394, \
          0.9437280545720244, \
          0.9437280545720244, \
          0.3792675110532606, \
          0.9437280545720244, \
          0.0562719454279757, \
          0.3792675110532606, \
          0.0562719454279757, \
          0.0562719454279757, \
          0.3792675110532606, \
          0.0562719454279757, \
          0.9437280545720244, \
          0.3792675110532606, \
          0.9437280545720244, \
          0.9007366871015028, \
          0.9007366871015028, \
          0.9943923590724830, \
          0.7341796540172194, \
          0.9943923590724830, \
          0.7341796540172194, \
          0.0992633128984972, \
          0.0992633128984972, \
          0.9943923590724830, \
          0.7341796540172194, \
          0.9943923590724830, \
          0.7341796540172194, \
          0.9007366871015028, \
          0.9007366871015028, \
          0.0056076409275170, \
          0.7341796540172194, \
          0.0056076409275170, \
          0.7341796540172194, \
          0.9007366871015028, \
          0.9007366871015028, \
          0.9943923590724830, \
          0.2658203459827806, \
          0.9943923590724830, \
          0.2658203459827806, \
          0.0992633128984972, \
          0.0992633128984972, \
          0.0056076409275170, \
          0.7341796540172194, \
          0.0056076409275170, \
          0.7341796540172194, \
          0.0992633128984972, \
          0.0992633128984972, \
          0.9943923590724830, \
          0.2658203459827806, \
          0.9943923590724830, \
          0.2658203459827806, \
          0.9007366871015028, \
          0.9007366871015028, \
          0.0056076409275170, \
          0.2658203459827806, \
          0.0056076409275170, \
          0.2658203459827806, \
          0.0992633128984972, \
          0.0992633128984972, \
          0.0056076409275170, \
          0.2658203459827806, \
          0.0056076409275170, \
          0.2658203459827806, \
          0.8049570330025153, \
          0.8049570330025153, \
          0.8934115499715557, \
          0.6602554101905883, \
          0.8934115499715557, \
          0.6602554101905883, \
          0.1950429669974847, \
          0.1950429669974847, \
          0.8934115499715557, \
          0.6602554101905883, \
          0.8934115499715557, \
          0.6602554101905883, \
          0.8049570330025153, \
          0.8049570330025153, \
          0.1065884500284443, \
          0.6602554101905883, \
          0.1065884500284443, \
          0.6602554101905883, \
          0.8049570330025153, \
          0.8049570330025153, \
          0.8934115499715557, \
          0.3397445898094117, \
          0.8934115499715557, \
          0.3397445898094117, \
          0.1950429669974847, \
          0.1950429669974847, \
          0.1065884500284443, \
          0.6602554101905883, \
          0.1065884500284443, \
          0.6602554101905883, \
          0.1950429669974847, \
          0.1950429669974847, \
          0.8934115499715557, \
          0.3397445898094117, \
          0.8934115499715557, \
          0.3397445898094117, \
          0.8049570330025153, \
          0.8049570330025153, \
          0.1065884500284443, \
          0.3397445898094117, \
          0.1065884500284443, \
          0.3397445898094117, \
          0.1950429669974847, \
          0.1950429669974847, \
          0.1065884500284443, \
          0.3397445898094117, \
          0.1065884500284443, \
          0.3397445898094117 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.7426575151151338, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.2573424848848662, \
          0.5000000000000000, \
          0.8703394079370492, \
          0.1296605920629508, \
          0.8703394079370492, \
          0.1296605920629508, \
          0.8703394079370492, \
          0.1296605920629508, \
          0.1296605920629508, \
          0.8703394079370492, \
          0.9999997917911259, \
          0.0000002082088741, \
          0.9999997917911259, \
          0.0000002082088741, \
          0.9999997917911259, \
          0.0000002082088741, \
          0.0000002082088741, \
          0.9999997917911259, \
          0.8773134026065881, \
          0.8773134026065881, \
          0.5000000000000000, \
          0.8773134026065881, \
          0.1226865973934119, \
          0.5000000000000000, \
          0.1226865973934119, \
          0.8773134026065881, \
          0.5000000000000000, \
          0.1226865973934119, \
          0.1226865973934119, \
          0.5000000000000000, \
          0.7748409070843456, \
          0.7748409070843456, \
          0.5000000000000000, \
          0.7748409070843456, \
          0.2251590929156544, \
          0.5000000000000000, \
          0.2251590929156544, \
          0.7748409070843456, \
          0.5000000000000000, \
          0.2251590929156544, \
          0.2251590929156544, \
          0.5000000000000000, \
          0.9998342518711405, \
          0.9998342518711405, \
          0.5000000000000000, \
          0.9998342518711405, \
          0.0001657481288594, \
          0.5000000000000000, \
          0.0001657481288594, \
          0.9998342518711405, \
          0.5000000000000000, \
          0.0001657481288594, \
          0.0001657481288594, \
          0.5000000000000000, \
          0.9765209703524975, \
          0.0234790296475025, \
          0.0234790296475025, \
          0.9765209703524975, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8078645495842367, \
          0.1921354504157633, \
          0.8078645495842367, \
          0.1921354504157633, \
          0.8078645495842367, \
          0.1921354504157633, \
          0.8078645495842367, \
          0.1921354504157633, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9765209703524975, \
          0.0234790296475025, \
          0.0234790296475025, \
          0.9765209703524975, \
          0.9085620340535459, \
          0.0914379659464542, \
          0.0914379659464542, \
          0.9085620340535459, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6378406365996775, \
          0.3621593634003225, \
          0.6378406365996775, \
          0.3621593634003225, \
          0.6378406365996775, \
          0.3621593634003225, \
          0.6378406365996775, \
          0.3621593634003225, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9085620340535459, \
          0.0914379659464542, \
          0.0914379659464542, \
          0.9085620340535459, \
          0.9848870223309694, \
          0.6276714770186411, \
          0.6276714770186411, \
          0.9848870223309694, \
          0.3723285229813589, \
          0.6276714770186411, \
          0.9848870223309694, \
          0.3723285229813589, \
          0.3723285229813589, \
          0.9848870223309694, \
          0.6276714770186411, \
          0.3723285229813589, \
          0.0151129776690307, \
          0.6276714770186411, \
          0.6276714770186411, \
          0.0151129776690307, \
          0.3723285229813589, \
          0.6276714770186411, \
          0.0151129776690307, \
          0.3723285229813589, \
          0.3723285229813589, \
          0.0151129776690307, \
          0.6276714770186411, \
          0.3723285229813589, \
          0.8733616537091691, \
          0.9676181924490221, \
          0.9676181924490221, \
          0.8733616537091691, \
          0.0323818075509779, \
          0.9676181924490221, \
          0.8733616537091691, \
          0.0323818075509779, \
          0.0323818075509779, \
          0.8733616537091691, \
          0.9676181924490221, \
          0.0323818075509779, \
          0.1266383462908310, \
          0.9676181924490221, \
          0.9676181924490221, \
          0.1266383462908310, \
          0.0323818075509779, \
          0.9676181924490221, \
          0.1266383462908310, \
          0.0323818075509779, \
          0.0323818075509779, \
          0.1266383462908310, \
          0.9676181924490221, \
          0.0323818075509779, \
          0.8093319789042792, \
          0.6715295730694326, \
          0.6715295730694326, \
          0.8093319789042792, \
          0.3284704269305673, \
          0.6715295730694326, \
          0.8093319789042792, \
          0.3284704269305673, \
          0.3284704269305673, \
          0.8093319789042792, \
          0.6715295730694326, \
          0.3284704269305673, \
          0.1906680210957207, \
          0.6715295730694326, \
          0.6715295730694326, \
          0.1906680210957207, \
          0.3284704269305673, \
          0.6715295730694326, \
          0.1906680210957207, \
          0.3284704269305673, \
          0.3284704269305673, \
          0.1906680210957207, \
          0.6715295730694326, \
          0.3284704269305673, \
          0.4229648752978111, \
          0.6277920800575361, \
          0.6277920800575361, \
          0.4229648752978111, \
          0.3722079199424639, \
          0.6277920800575361, \
          0.4229648752978111, \
          0.3722079199424639, \
          0.3722079199424639, \
          0.4229648752978111, \
          0.6277920800575361, \
          0.3722079199424639, \
          0.5770351247021889, \
          0.6277920800575361, \
          0.6277920800575361, \
          0.5770351247021889, \
          0.3722079199424639, \
          0.6277920800575361, \
          0.5770351247021889, \
          0.3722079199424639, \
          0.3722079199424639, \
          0.5770351247021889, \
          0.6277920800575361, \
          0.3722079199424639, \
          0.9478284758927406, \
          0.7708105708234440, \
          0.7708105708234440, \
          0.9478284758927406, \
          0.2291894291765560, \
          0.7708105708234440, \
          0.9478284758927406, \
          0.2291894291765560, \
          0.2291894291765560, \
          0.9478284758927406, \
          0.7708105708234440, \
          0.2291894291765560, \
          0.0521715241072594, \
          0.7708105708234440, \
          0.7708105708234440, \
          0.0521715241072594, \
          0.2291894291765560, \
          0.7708105708234440, \
          0.0521715241072594, \
          0.2291894291765560, \
          0.2291894291765560, \
          0.0521715241072594, \
          0.7708105708234440, \
          0.2291894291765560, \
          0.6207324889467394, \
          0.9437280545720244, \
          0.9437280545720244, \
          0.6207324889467394, \
          0.0562719454279757, \
          0.9437280545720244, \
          0.6207324889467394, \
          0.0562719454279757, \
          0.0562719454279757, \
          0.6207324889467394, \
          0.9437280545720244, \
          0.0562719454279757, \
          0.3792675110532606, \
          0.9437280545720244, \
          0.9437280545720244, \
          0.3792675110532606, \
          0.0562719454279757, \
          0.9437280545720244, \
          0.3792675110532606, \
          0.0562719454279757, \
          0.0562719454279757, \
          0.3792675110532606, \
          0.9437280545720244, \
          0.0562719454279757, \
          0.9943923590724830, \
          0.7341796540172194, \
          0.9007366871015028, \
          0.9007366871015028, \
          0.7341796540172194, \
          0.9943923590724830, \
          0.9943923590724830, \
          0.7341796540172194, \
          0.0992633128984972, \
          0.0992633128984972, \
          0.7341796540172194, \
          0.9943923590724830, \
          0.0056076409275170, \
          0.7341796540172194, \
          0.9007366871015028, \
          0.9007366871015028, \
          0.7341796540172194, \
          0.0056076409275170, \
          0.9943923590724830, \
          0.2658203459827806, \
          0.9007366871015028, \
          0.9007366871015028, \
          0.2658203459827806, \
          0.9943923590724830, \
          0.0056076409275170, \
          0.7341796540172194, \
          0.0992633128984972, \
          0.0992633128984972, \
          0.7341796540172194, \
          0.0056076409275170, \
          0.9943923590724830, \
          0.2658203459827806, \
          0.0992633128984972, \
          0.0992633128984972, \
          0.2658203459827806, \
          0.9943923590724830, \
          0.0056076409275170, \
          0.2658203459827806, \
          0.9007366871015028, \
          0.9007366871015028, \
          0.2658203459827806, \
          0.0056076409275170, \
          0.0056076409275170, \
          0.2658203459827806, \
          0.0992633128984972, \
          0.0992633128984972, \
          0.2658203459827806, \
          0.0056076409275170, \
          0.8934115499715557, \
          0.6602554101905883, \
          0.8049570330025153, \
          0.8049570330025153, \
          0.6602554101905883, \
          0.8934115499715557, \
          0.8934115499715557, \
          0.6602554101905883, \
          0.1950429669974847, \
          0.1950429669974847, \
          0.6602554101905883, \
          0.8934115499715557, \
          0.1065884500284443, \
          0.6602554101905883, \
          0.8049570330025153, \
          0.8049570330025153, \
          0.6602554101905883, \
          0.1065884500284443, \
          0.8934115499715557, \
          0.3397445898094117, \
          0.8049570330025153, \
          0.8049570330025153, \
          0.3397445898094117, \
          0.8934115499715557, \
          0.1065884500284443, \
          0.6602554101905883, \
          0.1950429669974847, \
          0.1950429669974847, \
          0.6602554101905883, \
          0.1065884500284443, \
          0.8934115499715557, \
          0.3397445898094117, \
          0.1950429669974847, \
          0.1950429669974847, \
          0.3397445898094117, \
          0.8934115499715557, \
          0.1065884500284443, \
          0.3397445898094117, \
          0.8049570330025153, \
          0.8049570330025153, \
          0.3397445898094117, \
          0.1065884500284443, \
          0.1065884500284443, \
          0.3397445898094117, \
          0.1950429669974847, \
          0.1950429669974847, \
          0.3397445898094117, \
          0.1065884500284443 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.7426575151151338, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.2573424848848662, \
          0.8703394079370492, \
          0.1296605920629508, \
          0.8703394079370492, \
          0.8703394079370492, \
          0.1296605920629508, \
          0.8703394079370492, \
          0.1296605920629508, \
          0.1296605920629508, \
          0.9999997917911259, \
          0.0000002082088741, \
          0.9999997917911259, \
          0.9999997917911259, \
          0.0000002082088741, \
          0.9999997917911259, \
          0.0000002082088741, \
          0.0000002082088741, \
          0.5000000000000000, \
          0.8773134026065881, \
          0.8773134026065881, \
          0.5000000000000000, \
          0.8773134026065881, \
          0.8773134026065881, \
          0.5000000000000000, \
          0.1226865973934119, \
          0.1226865973934119, \
          0.5000000000000000, \
          0.1226865973934119, \
          0.1226865973934119, \
          0.5000000000000000, \
          0.7748409070843456, \
          0.7748409070843456, \
          0.5000000000000000, \
          0.7748409070843456, \
          0.7748409070843456, \
          0.5000000000000000, \
          0.2251590929156544, \
          0.2251590929156544, \
          0.5000000000000000, \
          0.2251590929156544, \
          0.2251590929156544, \
          0.5000000000000000, \
          0.9998342518711405, \
          0.9998342518711405, \
          0.5000000000000000, \
          0.9998342518711405, \
          0.9998342518711405, \
          0.5000000000000000, \
          0.0001657481288594, \
          0.0001657481288594, \
          0.5000000000000000, \
          0.0001657481288594, \
          0.0001657481288594, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9765209703524975, \
          0.0234790296475025, \
          0.0234790296475025, \
          0.9765209703524975, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9765209703524975, \
          0.0234790296475025, \
          0.0234790296475025, \
          0.9765209703524975, \
          0.8078645495842367, \
          0.1921354504157633, \
          0.8078645495842367, \
          0.1921354504157633, \
          0.8078645495842367, \
          0.1921354504157633, \
          0.8078645495842367, \
          0.1921354504157633, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9085620340535459, \
          0.0914379659464542, \
          0.0914379659464542, \
          0.9085620340535459, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9085620340535459, \
          0.0914379659464542, \
          0.0914379659464542, \
          0.9085620340535459, \
          0.6378406365996775, \
          0.3621593634003225, \
          0.6378406365996775, \
          0.3621593634003225, \
          0.6378406365996775, \
          0.3621593634003225, \
          0.6378406365996775, \
          0.3621593634003225, \
          0.6276714770186411, \
          0.6276714770186411, \
          0.9848870223309694, \
          0.6276714770186411, \
          0.6276714770186411, \
          0.9848870223309694, \
          0.3723285229813589, \
          0.3723285229813589, \
          0.9848870223309694, \
          0.3723285229813589, \
          0.3723285229813589, \
          0.9848870223309694, \
          0.6276714770186411, \
          0.6276714770186411, \
          0.0151129776690307, \
          0.6276714770186411, \
          0.6276714770186411, \
          0.0151129776690307, \
          0.3723285229813589, \
          0.3723285229813589, \
          0.0151129776690307, \
          0.3723285229813589, \
          0.3723285229813589, \
          0.0151129776690307, \
          0.9676181924490221, \
          0.9676181924490221, \
          0.8733616537091691, \
          0.9676181924490221, \
          0.9676181924490221, \
          0.8733616537091691, \
          0.0323818075509779, \
          0.0323818075509779, \
          0.8733616537091691, \
          0.0323818075509779, \
          0.0323818075509779, \
          0.8733616537091691, \
          0.9676181924490221, \
          0.9676181924490221, \
          0.1266383462908310, \
          0.9676181924490221, \
          0.9676181924490221, \
          0.1266383462908310, \
          0.0323818075509779, \
          0.0323818075509779, \
          0.1266383462908310, \
          0.0323818075509779, \
          0.0323818075509779, \
          0.1266383462908310, \
          0.6715295730694326, \
          0.6715295730694326, \
          0.8093319789042792, \
          0.6715295730694326, \
          0.6715295730694326, \
          0.8093319789042792, \
          0.3284704269305673, \
          0.3284704269305673, \
          0.8093319789042792, \
          0.3284704269305673, \
          0.3284704269305673, \
          0.8093319789042792, \
          0.6715295730694326, \
          0.6715295730694326, \
          0.1906680210957207, \
          0.6715295730694326, \
          0.6715295730694326, \
          0.1906680210957207, \
          0.3284704269305673, \
          0.3284704269305673, \
          0.1906680210957207, \
          0.3284704269305673, \
          0.3284704269305673, \
          0.1906680210957207, \
          0.6277920800575361, \
          0.6277920800575361, \
          0.4229648752978111, \
          0.6277920800575361, \
          0.6277920800575361, \
          0.4229648752978111, \
          0.3722079199424639, \
          0.3722079199424639, \
          0.4229648752978111, \
          0.3722079199424639, \
          0.3722079199424639, \
          0.4229648752978111, \
          0.6277920800575361, \
          0.6277920800575361, \
          0.5770351247021889, \
          0.6277920800575361, \
          0.6277920800575361, \
          0.5770351247021889, \
          0.3722079199424639, \
          0.3722079199424639, \
          0.5770351247021889, \
          0.3722079199424639, \
          0.3722079199424639, \
          0.5770351247021889, \
          0.7708105708234440, \
          0.7708105708234440, \
          0.9478284758927406, \
          0.7708105708234440, \
          0.7708105708234440, \
          0.9478284758927406, \
          0.2291894291765560, \
          0.2291894291765560, \
          0.9478284758927406, \
          0.2291894291765560, \
          0.2291894291765560, \
          0.9478284758927406, \
          0.7708105708234440, \
          0.7708105708234440, \
          0.0521715241072594, \
          0.7708105708234440, \
          0.7708105708234440, \
          0.0521715241072594, \
          0.2291894291765560, \
          0.2291894291765560, \
          0.0521715241072594, \
          0.2291894291765560, \
          0.2291894291765560, \
          0.0521715241072594, \
          0.9437280545720244, \
          0.9437280545720244, \
          0.6207324889467394, \
          0.9437280545720244, \
          0.9437280545720244, \
          0.6207324889467394, \
          0.0562719454279757, \
          0.0562719454279757, \
          0.6207324889467394, \
          0.0562719454279757, \
          0.0562719454279757, \
          0.6207324889467394, \
          0.9437280545720244, \
          0.9437280545720244, \
          0.3792675110532606, \
          0.9437280545720244, \
          0.9437280545720244, \
          0.3792675110532606, \
          0.0562719454279757, \
          0.0562719454279757, \
          0.3792675110532606, \
          0.0562719454279757, \
          0.0562719454279757, \
          0.3792675110532606, \
          0.7341796540172194, \
          0.9943923590724830, \
          0.7341796540172194, \
          0.9943923590724830, \
          0.9007366871015028, \
          0.9007366871015028, \
          0.7341796540172194, \
          0.9943923590724830, \
          0.7341796540172194, \
          0.9943923590724830, \
          0.0992633128984972, \
          0.0992633128984972, \
          0.7341796540172194, \
          0.0056076409275170, \
          0.7341796540172194, \
          0.0056076409275170, \
          0.9007366871015028, \
          0.9007366871015028, \
          0.2658203459827806, \
          0.9943923590724830, \
          0.2658203459827806, \
          0.9943923590724830, \
          0.9007366871015028, \
          0.9007366871015028, \
          0.7341796540172194, \
          0.0056076409275170, \
          0.7341796540172194, \
          0.0056076409275170, \
          0.0992633128984972, \
          0.0992633128984972, \
          0.2658203459827806, \
          0.9943923590724830, \
          0.2658203459827806, \
          0.9943923590724830, \
          0.0992633128984972, \
          0.0992633128984972, \
          0.2658203459827806, \
          0.0056076409275170, \
          0.2658203459827806, \
          0.0056076409275170, \
          0.9007366871015028, \
          0.9007366871015028, \
          0.2658203459827806, \
          0.0056076409275170, \
          0.2658203459827806, \
          0.0056076409275170, \
          0.0992633128984972, \
          0.0992633128984972, \
          0.6602554101905883, \
          0.8934115499715557, \
          0.6602554101905883, \
          0.8934115499715557, \
          0.8049570330025153, \
          0.8049570330025153, \
          0.6602554101905883, \
          0.8934115499715557, \
          0.6602554101905883, \
          0.8934115499715557, \
          0.1950429669974847, \
          0.1950429669974847, \
          0.6602554101905883, \
          0.1065884500284443, \
          0.6602554101905883, \
          0.1065884500284443, \
          0.8049570330025153, \
          0.8049570330025153, \
          0.3397445898094117, \
          0.8934115499715557, \
          0.3397445898094117, \
          0.8934115499715557, \
          0.8049570330025153, \
          0.8049570330025153, \
          0.6602554101905883, \
          0.1065884500284443, \
          0.6602554101905883, \
          0.1065884500284443, \
          0.1950429669974847, \
          0.1950429669974847, \
          0.3397445898094117, \
          0.8934115499715557, \
          0.3397445898094117, \
          0.8934115499715557, \
          0.1950429669974847, \
          0.1950429669974847, \
          0.3397445898094117, \
          0.1065884500284443, \
          0.3397445898094117, \
          0.1065884500284443, \
          0.8049570330025153, \
          0.8049570330025153, \
          0.3397445898094117, \
          0.1065884500284443, \
          0.3397445898094117, \
          0.1065884500284443, \
          0.1950429669974847, \
          0.1950429669974847 ] )

  w = np.array ( [ \
          0.0096145921289297, \
          0.0096145921289297, \
          0.0096145921289297, \
          0.0096145921289297, \
          0.0096145921289297, \
          0.0096145921289297, \
          0.0043938276021590, \
          0.0043938276021590, \
          0.0043938276021590, \
          0.0043938276021590, \
          0.0043938276021590, \
          0.0043938276021590, \
          0.0043938276021590, \
          0.0043938276021590, \
          0.0000496472519452, \
          0.0000496472519452, \
          0.0000496472519452, \
          0.0000496472519452, \
          0.0000496472519452, \
          0.0000496472519452, \
          0.0000496472519452, \
          0.0000496472519452, \
          0.0025062844648325, \
          0.0025062844648325, \
          0.0025062844648325, \
          0.0025062844648325, \
          0.0025062844648325, \
          0.0025062844648325, \
          0.0025062844648325, \
          0.0025062844648325, \
          0.0025062844648325, \
          0.0025062844648325, \
          0.0025062844648325, \
          0.0025062844648325, \
          0.0061332324820703, \
          0.0061332324820703, \
          0.0061332324820703, \
          0.0061332324820703, \
          0.0061332324820703, \
          0.0061332324820703, \
          0.0061332324820703, \
          0.0061332324820703, \
          0.0061332324820703, \
          0.0061332324820703, \
          0.0061332324820703, \
          0.0061332324820703, \
          0.0003052513689971, \
          0.0003052513689971, \
          0.0003052513689971, \
          0.0003052513689971, \
          0.0003052513689971, \
          0.0003052513689971, \
          0.0003052513689971, \
          0.0003052513689971, \
          0.0003052513689971, \
          0.0003052513689971, \
          0.0003052513689971, \
          0.0003052513689971, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0028254377330331, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0048177045987999, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0022831423389536, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0011774374872787, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0061840607506279, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0026746558375937, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0034191776775788, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0023346175566150, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0010527901648871, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639, \
          0.0027438309407639 ] )

  return x, y, z, w

def rule19 ( ):

#*****************************************************************************80
#
## rule19() returns the hexahedron quadrature rule of precision 19.
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
#    05 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which add to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.6178975194487687, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.3821024805512313, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9442475200220319, \
          0.0557524799779681, \
          0.0557524799779681, \
          0.9442475200220319, \
          0.9442475200220319, \
          0.0557524799779681, \
          0.9442475200220319, \
          0.0557524799779681, \
          0.8345909234965025, \
          0.1654090765034974, \
          0.1654090765034974, \
          0.8345909234965025, \
          0.8345909234965025, \
          0.1654090765034974, \
          0.8345909234965025, \
          0.1654090765034974, \
          0.8561550198509273, \
          0.1438449801490727, \
          0.8561550198509273, \
          0.1438449801490727, \
          0.8561550198509273, \
          0.1438449801490727, \
          0.8561550198509273, \
          0.1438449801490727, \
          0.9991488896425311, \
          0.0008511103574689, \
          0.0008511103574689, \
          0.9991488896425311, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9991488896425311, \
          0.0008511103574689, \
          0.0008511103574689, \
          0.9991488896425311, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6998570581371140, \
          0.3001429418628860, \
          0.6998570581371140, \
          0.3001429418628860, \
          0.6998570581371140, \
          0.3001429418628860, \
          0.6998570581371140, \
          0.3001429418628860, \
          0.5860120647237821, \
          0.4139879352762179, \
          0.4139879352762179, \
          0.5860120647237821, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5860120647237821, \
          0.4139879352762179, \
          0.4139879352762179, \
          0.5860120647237821, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9382902632360840, \
          0.0617097367639160, \
          0.9382902632360840, \
          0.0617097367639160, \
          0.9382902632360840, \
          0.0617097367639160, \
          0.9382902632360840, \
          0.0617097367639160, \
          0.2840454955532042, \
          0.7159545044467958, \
          0.7159545044467958, \
          0.2840454955532042, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.2840454955532042, \
          0.7159545044467958, \
          0.7159545044467958, \
          0.2840454955532042, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.3449134012977228, \
          0.7705521820675761, \
          0.3449134012977228, \
          0.6550865987022771, \
          0.7705521820675761, \
          0.6550865987022771, \
          0.6550865987022771, \
          0.7705521820675761, \
          0.6550865987022771, \
          0.3449134012977228, \
          0.7705521820675761, \
          0.3449134012977228, \
          0.3449134012977228, \
          0.2294478179324239, \
          0.3449134012977228, \
          0.6550865987022771, \
          0.2294478179324239, \
          0.6550865987022771, \
          0.6550865987022771, \
          0.2294478179324239, \
          0.6550865987022771, \
          0.3449134012977228, \
          0.2294478179324239, \
          0.3449134012977228, \
          0.9920926274878630, \
          0.9103324974446185, \
          0.9920926274878630, \
          0.0079073725121370, \
          0.9103324974446185, \
          0.0079073725121370, \
          0.0079073725121370, \
          0.9103324974446185, \
          0.0079073725121370, \
          0.9920926274878630, \
          0.9103324974446185, \
          0.9920926274878630, \
          0.9920926274878630, \
          0.0896675025553814, \
          0.9920926274878630, \
          0.0079073725121370, \
          0.0896675025553814, \
          0.0079073725121370, \
          0.0079073725121370, \
          0.0896675025553814, \
          0.0079073725121370, \
          0.9920926274878630, \
          0.0896675025553814, \
          0.9920926274878630, \
          0.9221936167657927, \
          0.4263116836838957, \
          0.9221936167657927, \
          0.0778063832342073, \
          0.4263116836838957, \
          0.0778063832342073, \
          0.0778063832342073, \
          0.4263116836838957, \
          0.0778063832342073, \
          0.9221936167657927, \
          0.4263116836838957, \
          0.9221936167657927, \
          0.9221936167657927, \
          0.5736883163161043, \
          0.9221936167657927, \
          0.0778063832342073, \
          0.5736883163161043, \
          0.0778063832342073, \
          0.0778063832342073, \
          0.5736883163161043, \
          0.0778063832342073, \
          0.9221936167657927, \
          0.5736883163161043, \
          0.9221936167657927, \
          0.7437996999426106, \
          0.8837457372516819, \
          0.7437996999426106, \
          0.2562003000573894, \
          0.8837457372516819, \
          0.2562003000573894, \
          0.2562003000573894, \
          0.8837457372516819, \
          0.2562003000573894, \
          0.7437996999426106, \
          0.8837457372516819, \
          0.7437996999426106, \
          0.7437996999426106, \
          0.1162542627483181, \
          0.7437996999426106, \
          0.2562003000573894, \
          0.1162542627483181, \
          0.2562003000573894, \
          0.2562003000573894, \
          0.1162542627483181, \
          0.2562003000573894, \
          0.7437996999426106, \
          0.1162542627483181, \
          0.7437996999426106, \
          0.8820659248983722, \
          0.6931955182506035, \
          0.8820659248983722, \
          0.1179340751016278, \
          0.6931955182506035, \
          0.1179340751016278, \
          0.1179340751016278, \
          0.6931955182506035, \
          0.1179340751016278, \
          0.8820659248983722, \
          0.6931955182506035, \
          0.8820659248983722, \
          0.8820659248983722, \
          0.3068044817493964, \
          0.8820659248983722, \
          0.1179340751016278, \
          0.3068044817493964, \
          0.1179340751016278, \
          0.1179340751016278, \
          0.3068044817493964, \
          0.1179340751016278, \
          0.8820659248983722, \
          0.3068044817493964, \
          0.8820659248983722, \
          0.8556268694112152, \
          0.9516006474964566, \
          0.8556268694112152, \
          0.1443731305887847, \
          0.9516006474964566, \
          0.1443731305887847, \
          0.1443731305887847, \
          0.9516006474964566, \
          0.1443731305887847, \
          0.8556268694112152, \
          0.9516006474964566, \
          0.8556268694112152, \
          0.8556268694112152, \
          0.0483993525035434, \
          0.8556268694112152, \
          0.1443731305887847, \
          0.0483993525035434, \
          0.1443731305887847, \
          0.1443731305887847, \
          0.0483993525035434, \
          0.1443731305887847, \
          0.8556268694112152, \
          0.0483993525035434, \
          0.8556268694112152, \
          0.9775744747969544, \
          0.6113080322285057, \
          0.9775744747969544, \
          0.0224255252030456, \
          0.6113080322285057, \
          0.0224255252030456, \
          0.0224255252030456, \
          0.6113080322285057, \
          0.0224255252030456, \
          0.9775744747969544, \
          0.6113080322285057, \
          0.9775744747969544, \
          0.9775744747969544, \
          0.3886919677714943, \
          0.9775744747969544, \
          0.0224255252030456, \
          0.3886919677714943, \
          0.0224255252030456, \
          0.0224255252030456, \
          0.3886919677714943, \
          0.0224255252030456, \
          0.9775744747969544, \
          0.3886919677714943, \
          0.9775744747969544, \
          0.5848459901934986, \
          0.9825814337796190, \
          0.5848459901934986, \
          0.4151540098065015, \
          0.9825814337796190, \
          0.4151540098065015, \
          0.4151540098065015, \
          0.9825814337796190, \
          0.4151540098065015, \
          0.5848459901934986, \
          0.9825814337796190, \
          0.5848459901934986, \
          0.5848459901934986, \
          0.0174185662203810, \
          0.5848459901934986, \
          0.4151540098065015, \
          0.0174185662203810, \
          0.4151540098065015, \
          0.4151540098065015, \
          0.0174185662203810, \
          0.4151540098065015, \
          0.5848459901934986, \
          0.0174185662203810, \
          0.5848459901934986, \
          0.8042667629417029, \
          0.5470636340177077, \
          0.8042667629417029, \
          0.1957332370582971, \
          0.5470636340177077, \
          0.1957332370582971, \
          0.1957332370582971, \
          0.5470636340177077, \
          0.1957332370582971, \
          0.8042667629417029, \
          0.5470636340177077, \
          0.8042667629417029, \
          0.8042667629417029, \
          0.4529363659822923, \
          0.8042667629417029, \
          0.1957332370582971, \
          0.4529363659822923, \
          0.1957332370582971, \
          0.1957332370582971, \
          0.4529363659822923, \
          0.1957332370582971, \
          0.8042667629417029, \
          0.4529363659822923, \
          0.8042667629417029, \
          0.7132758893843609, \
          0.9892390565548020, \
          0.7132758893843609, \
          0.2867241106156391, \
          0.9892390565548020, \
          0.2867241106156391, \
          0.2867241106156391, \
          0.9892390565548020, \
          0.2867241106156391, \
          0.7132758893843609, \
          0.9892390565548020, \
          0.7132758893843609, \
          0.7132758893843609, \
          0.0107609434451980, \
          0.7132758893843609, \
          0.2867241106156391, \
          0.0107609434451980, \
          0.2867241106156391, \
          0.2867241106156391, \
          0.0107609434451980, \
          0.2867241106156391, \
          0.7132758893843609, \
          0.0107609434451980, \
          0.7132758893843609, \
          0.5918460351304471, \
          0.8728877113378553, \
          0.5918460351304471, \
          0.4081539648695529, \
          0.8728877113378553, \
          0.4081539648695529, \
          0.4081539648695529, \
          0.8728877113378553, \
          0.4081539648695529, \
          0.5918460351304471, \
          0.8728877113378553, \
          0.5918460351304471, \
          0.5918460351304471, \
          0.1271122886621447, \
          0.5918460351304471, \
          0.4081539648695529, \
          0.1271122886621447, \
          0.4081539648695529, \
          0.4081539648695529, \
          0.1271122886621447, \
          0.4081539648695529, \
          0.5918460351304471, \
          0.1271122886621447, \
          0.5918460351304471, \
          0.8267665443298317, \
          0.8267665443298317, \
          0.9566761563025079, \
          0.6444314510393020, \
          0.9566761563025079, \
          0.6444314510393020, \
          0.1732334556701683, \
          0.1732334556701683, \
          0.9566761563025079, \
          0.6444314510393020, \
          0.9566761563025079, \
          0.6444314510393020, \
          0.8267665443298317, \
          0.8267665443298317, \
          0.0433238436974921, \
          0.6444314510393020, \
          0.0433238436974921, \
          0.6444314510393020, \
          0.8267665443298317, \
          0.8267665443298317, \
          0.9566761563025079, \
          0.3555685489606980, \
          0.9566761563025079, \
          0.3555685489606980, \
          0.1732334556701683, \
          0.1732334556701683, \
          0.0433238436974921, \
          0.6444314510393020, \
          0.0433238436974921, \
          0.6444314510393020, \
          0.1732334556701683, \
          0.1732334556701683, \
          0.9566761563025079, \
          0.3555685489606980, \
          0.9566761563025079, \
          0.3555685489606980, \
          0.8267665443298317, \
          0.8267665443298317, \
          0.0433238436974921, \
          0.3555685489606980, \
          0.0433238436974921, \
          0.3555685489606980, \
          0.1732334556701683, \
          0.1732334556701683, \
          0.0433238436974921, \
          0.3555685489606980, \
          0.0433238436974921, \
          0.3555685489606980, \
          0.9237817545492393, \
          0.9237817545492393, \
          0.9874241069713281, \
          0.7767138770406730, \
          0.9874241069713281, \
          0.7767138770406730, \
          0.0762182454507607, \
          0.0762182454507607, \
          0.9874241069713281, \
          0.7767138770406730, \
          0.9874241069713281, \
          0.7767138770406730, \
          0.9237817545492393, \
          0.9237817545492393, \
          0.0125758930286720, \
          0.7767138770406730, \
          0.0125758930286720, \
          0.7767138770406730, \
          0.9237817545492393, \
          0.9237817545492393, \
          0.9874241069713281, \
          0.2232861229593271, \
          0.9874241069713281, \
          0.2232861229593271, \
          0.0762182454507607, \
          0.0762182454507607, \
          0.0125758930286720, \
          0.7767138770406730, \
          0.0125758930286720, \
          0.7767138770406730, \
          0.0762182454507607, \
          0.0762182454507607, \
          0.9874241069713281, \
          0.2232861229593271, \
          0.9874241069713281, \
          0.2232861229593271, \
          0.9237817545492393, \
          0.9237817545492393, \
          0.0125758930286720, \
          0.2232861229593271, \
          0.0125758930286720, \
          0.2232861229593271, \
          0.0762182454507607, \
          0.0762182454507607, \
          0.0125758930286720, \
          0.2232861229593271, \
          0.0125758930286720, \
          0.2232861229593271 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.6178975194487687, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.3821024805512313, \
          0.5000000000000000, \
          0.9442475200220319, \
          0.0557524799779681, \
          0.9442475200220319, \
          0.0557524799779681, \
          0.9442475200220319, \
          0.0557524799779681, \
          0.0557524799779681, \
          0.9442475200220319, \
          0.8345909234965025, \
          0.1654090765034974, \
          0.8345909234965025, \
          0.1654090765034974, \
          0.8345909234965025, \
          0.1654090765034974, \
          0.1654090765034974, \
          0.8345909234965025, \
          0.9991488896425311, \
          0.0008511103574689, \
          0.0008511103574689, \
          0.9991488896425311, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8561550198509273, \
          0.1438449801490727, \
          0.8561550198509273, \
          0.1438449801490727, \
          0.8561550198509273, \
          0.1438449801490727, \
          0.8561550198509273, \
          0.1438449801490727, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9991488896425311, \
          0.0008511103574689, \
          0.0008511103574689, \
          0.9991488896425311, \
          0.5860120647237821, \
          0.4139879352762179, \
          0.4139879352762179, \
          0.5860120647237821, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6998570581371140, \
          0.3001429418628860, \
          0.6998570581371140, \
          0.3001429418628860, \
          0.6998570581371140, \
          0.3001429418628860, \
          0.6998570581371140, \
          0.3001429418628860, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5860120647237821, \
          0.4139879352762179, \
          0.4139879352762179, \
          0.5860120647237821, \
          0.2840454955532042, \
          0.7159545044467958, \
          0.7159545044467958, \
          0.2840454955532042, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9382902632360840, \
          0.0617097367639160, \
          0.9382902632360840, \
          0.0617097367639160, \
          0.9382902632360840, \
          0.0617097367639160, \
          0.9382902632360840, \
          0.0617097367639160, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.2840454955532042, \
          0.7159545044467958, \
          0.7159545044467958, \
          0.2840454955532042, \
          0.7705521820675761, \
          0.3449134012977228, \
          0.3449134012977228, \
          0.7705521820675761, \
          0.6550865987022771, \
          0.3449134012977228, \
          0.7705521820675761, \
          0.6550865987022771, \
          0.6550865987022771, \
          0.7705521820675761, \
          0.3449134012977228, \
          0.6550865987022771, \
          0.2294478179324239, \
          0.3449134012977228, \
          0.3449134012977228, \
          0.2294478179324239, \
          0.6550865987022771, \
          0.3449134012977228, \
          0.2294478179324239, \
          0.6550865987022771, \
          0.6550865987022771, \
          0.2294478179324239, \
          0.3449134012977228, \
          0.6550865987022771, \
          0.9103324974446185, \
          0.9920926274878630, \
          0.9920926274878630, \
          0.9103324974446185, \
          0.0079073725121370, \
          0.9920926274878630, \
          0.9103324974446185, \
          0.0079073725121370, \
          0.0079073725121370, \
          0.9103324974446185, \
          0.9920926274878630, \
          0.0079073725121370, \
          0.0896675025553814, \
          0.9920926274878630, \
          0.9920926274878630, \
          0.0896675025553814, \
          0.0079073725121370, \
          0.9920926274878630, \
          0.0896675025553814, \
          0.0079073725121370, \
          0.0079073725121370, \
          0.0896675025553814, \
          0.9920926274878630, \
          0.0079073725121370, \
          0.4263116836838957, \
          0.9221936167657927, \
          0.9221936167657927, \
          0.4263116836838957, \
          0.0778063832342073, \
          0.9221936167657927, \
          0.4263116836838957, \
          0.0778063832342073, \
          0.0778063832342073, \
          0.4263116836838957, \
          0.9221936167657927, \
          0.0778063832342073, \
          0.5736883163161043, \
          0.9221936167657927, \
          0.9221936167657927, \
          0.5736883163161043, \
          0.0778063832342073, \
          0.9221936167657927, \
          0.5736883163161043, \
          0.0778063832342073, \
          0.0778063832342073, \
          0.5736883163161043, \
          0.9221936167657927, \
          0.0778063832342073, \
          0.8837457372516819, \
          0.7437996999426106, \
          0.7437996999426106, \
          0.8837457372516819, \
          0.2562003000573894, \
          0.7437996999426106, \
          0.8837457372516819, \
          0.2562003000573894, \
          0.2562003000573894, \
          0.8837457372516819, \
          0.7437996999426106, \
          0.2562003000573894, \
          0.1162542627483181, \
          0.7437996999426106, \
          0.7437996999426106, \
          0.1162542627483181, \
          0.2562003000573894, \
          0.7437996999426106, \
          0.1162542627483181, \
          0.2562003000573894, \
          0.2562003000573894, \
          0.1162542627483181, \
          0.7437996999426106, \
          0.2562003000573894, \
          0.6931955182506035, \
          0.8820659248983722, \
          0.8820659248983722, \
          0.6931955182506035, \
          0.1179340751016278, \
          0.8820659248983722, \
          0.6931955182506035, \
          0.1179340751016278, \
          0.1179340751016278, \
          0.6931955182506035, \
          0.8820659248983722, \
          0.1179340751016278, \
          0.3068044817493964, \
          0.8820659248983722, \
          0.8820659248983722, \
          0.3068044817493964, \
          0.1179340751016278, \
          0.8820659248983722, \
          0.3068044817493964, \
          0.1179340751016278, \
          0.1179340751016278, \
          0.3068044817493964, \
          0.8820659248983722, \
          0.1179340751016278, \
          0.9516006474964566, \
          0.8556268694112152, \
          0.8556268694112152, \
          0.9516006474964566, \
          0.1443731305887847, \
          0.8556268694112152, \
          0.9516006474964566, \
          0.1443731305887847, \
          0.1443731305887847, \
          0.9516006474964566, \
          0.8556268694112152, \
          0.1443731305887847, \
          0.0483993525035434, \
          0.8556268694112152, \
          0.8556268694112152, \
          0.0483993525035434, \
          0.1443731305887847, \
          0.8556268694112152, \
          0.0483993525035434, \
          0.1443731305887847, \
          0.1443731305887847, \
          0.0483993525035434, \
          0.8556268694112152, \
          0.1443731305887847, \
          0.6113080322285057, \
          0.9775744747969544, \
          0.9775744747969544, \
          0.6113080322285057, \
          0.0224255252030456, \
          0.9775744747969544, \
          0.6113080322285057, \
          0.0224255252030456, \
          0.0224255252030456, \
          0.6113080322285057, \
          0.9775744747969544, \
          0.0224255252030456, \
          0.3886919677714943, \
          0.9775744747969544, \
          0.9775744747969544, \
          0.3886919677714943, \
          0.0224255252030456, \
          0.9775744747969544, \
          0.3886919677714943, \
          0.0224255252030456, \
          0.0224255252030456, \
          0.3886919677714943, \
          0.9775744747969544, \
          0.0224255252030456, \
          0.9825814337796190, \
          0.5848459901934986, \
          0.5848459901934986, \
          0.9825814337796190, \
          0.4151540098065015, \
          0.5848459901934986, \
          0.9825814337796190, \
          0.4151540098065015, \
          0.4151540098065015, \
          0.9825814337796190, \
          0.5848459901934986, \
          0.4151540098065015, \
          0.0174185662203810, \
          0.5848459901934986, \
          0.5848459901934986, \
          0.0174185662203810, \
          0.4151540098065015, \
          0.5848459901934986, \
          0.0174185662203810, \
          0.4151540098065015, \
          0.4151540098065015, \
          0.0174185662203810, \
          0.5848459901934986, \
          0.4151540098065015, \
          0.5470636340177077, \
          0.8042667629417029, \
          0.8042667629417029, \
          0.5470636340177077, \
          0.1957332370582971, \
          0.8042667629417029, \
          0.5470636340177077, \
          0.1957332370582971, \
          0.1957332370582971, \
          0.5470636340177077, \
          0.8042667629417029, \
          0.1957332370582971, \
          0.4529363659822923, \
          0.8042667629417029, \
          0.8042667629417029, \
          0.4529363659822923, \
          0.1957332370582971, \
          0.8042667629417029, \
          0.4529363659822923, \
          0.1957332370582971, \
          0.1957332370582971, \
          0.4529363659822923, \
          0.8042667629417029, \
          0.1957332370582971, \
          0.9892390565548020, \
          0.7132758893843609, \
          0.7132758893843609, \
          0.9892390565548020, \
          0.2867241106156391, \
          0.7132758893843609, \
          0.9892390565548020, \
          0.2867241106156391, \
          0.2867241106156391, \
          0.9892390565548020, \
          0.7132758893843609, \
          0.2867241106156391, \
          0.0107609434451980, \
          0.7132758893843609, \
          0.7132758893843609, \
          0.0107609434451980, \
          0.2867241106156391, \
          0.7132758893843609, \
          0.0107609434451980, \
          0.2867241106156391, \
          0.2867241106156391, \
          0.0107609434451980, \
          0.7132758893843609, \
          0.2867241106156391, \
          0.8728877113378553, \
          0.5918460351304471, \
          0.5918460351304471, \
          0.8728877113378553, \
          0.4081539648695529, \
          0.5918460351304471, \
          0.8728877113378553, \
          0.4081539648695529, \
          0.4081539648695529, \
          0.8728877113378553, \
          0.5918460351304471, \
          0.4081539648695529, \
          0.1271122886621447, \
          0.5918460351304471, \
          0.5918460351304471, \
          0.1271122886621447, \
          0.4081539648695529, \
          0.5918460351304471, \
          0.1271122886621447, \
          0.4081539648695529, \
          0.4081539648695529, \
          0.1271122886621447, \
          0.5918460351304471, \
          0.4081539648695529, \
          0.9566761563025079, \
          0.6444314510393020, \
          0.8267665443298317, \
          0.8267665443298317, \
          0.6444314510393020, \
          0.9566761563025079, \
          0.9566761563025079, \
          0.6444314510393020, \
          0.1732334556701683, \
          0.1732334556701683, \
          0.6444314510393020, \
          0.9566761563025079, \
          0.0433238436974921, \
          0.6444314510393020, \
          0.8267665443298317, \
          0.8267665443298317, \
          0.6444314510393020, \
          0.0433238436974921, \
          0.9566761563025079, \
          0.3555685489606980, \
          0.8267665443298317, \
          0.8267665443298317, \
          0.3555685489606980, \
          0.9566761563025079, \
          0.0433238436974921, \
          0.6444314510393020, \
          0.1732334556701683, \
          0.1732334556701683, \
          0.6444314510393020, \
          0.0433238436974921, \
          0.9566761563025079, \
          0.3555685489606980, \
          0.1732334556701683, \
          0.1732334556701683, \
          0.3555685489606980, \
          0.9566761563025079, \
          0.0433238436974921, \
          0.3555685489606980, \
          0.8267665443298317, \
          0.8267665443298317, \
          0.3555685489606980, \
          0.0433238436974921, \
          0.0433238436974921, \
          0.3555685489606980, \
          0.1732334556701683, \
          0.1732334556701683, \
          0.3555685489606980, \
          0.0433238436974921, \
          0.9874241069713281, \
          0.7767138770406730, \
          0.9237817545492393, \
          0.9237817545492393, \
          0.7767138770406730, \
          0.9874241069713281, \
          0.9874241069713281, \
          0.7767138770406730, \
          0.0762182454507607, \
          0.0762182454507607, \
          0.7767138770406730, \
          0.9874241069713281, \
          0.0125758930286720, \
          0.7767138770406730, \
          0.9237817545492393, \
          0.9237817545492393, \
          0.7767138770406730, \
          0.0125758930286720, \
          0.9874241069713281, \
          0.2232861229593271, \
          0.9237817545492393, \
          0.9237817545492393, \
          0.2232861229593271, \
          0.9874241069713281, \
          0.0125758930286720, \
          0.7767138770406730, \
          0.0762182454507607, \
          0.0762182454507607, \
          0.7767138770406730, \
          0.0125758930286720, \
          0.9874241069713281, \
          0.2232861229593271, \
          0.0762182454507607, \
          0.0762182454507607, \
          0.2232861229593271, \
          0.9874241069713281, \
          0.0125758930286720, \
          0.2232861229593271, \
          0.9237817545492393, \
          0.9237817545492393, \
          0.2232861229593271, \
          0.0125758930286720, \
          0.0125758930286720, \
          0.2232861229593271, \
          0.0762182454507607, \
          0.0762182454507607, \
          0.2232861229593271, \
          0.0125758930286720 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6178975194487687, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.3821024805512313, \
          0.9442475200220319, \
          0.0557524799779681, \
          0.9442475200220319, \
          0.9442475200220319, \
          0.0557524799779681, \
          0.9442475200220319, \
          0.0557524799779681, \
          0.0557524799779681, \
          0.8345909234965025, \
          0.1654090765034974, \
          0.8345909234965025, \
          0.8345909234965025, \
          0.1654090765034974, \
          0.8345909234965025, \
          0.1654090765034974, \
          0.1654090765034974, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9991488896425311, \
          0.0008511103574689, \
          0.0008511103574689, \
          0.9991488896425311, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9991488896425311, \
          0.0008511103574689, \
          0.0008511103574689, \
          0.9991488896425311, \
          0.8561550198509273, \
          0.1438449801490727, \
          0.8561550198509273, \
          0.1438449801490727, \
          0.8561550198509273, \
          0.1438449801490727, \
          0.8561550198509273, \
          0.1438449801490727, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5860120647237821, \
          0.4139879352762179, \
          0.4139879352762179, \
          0.5860120647237821, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5860120647237821, \
          0.4139879352762179, \
          0.4139879352762179, \
          0.5860120647237821, \
          0.6998570581371140, \
          0.3001429418628860, \
          0.6998570581371140, \
          0.3001429418628860, \
          0.6998570581371140, \
          0.3001429418628860, \
          0.6998570581371140, \
          0.3001429418628860, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.2840454955532042, \
          0.7159545044467958, \
          0.7159545044467958, \
          0.2840454955532042, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.2840454955532042, \
          0.7159545044467958, \
          0.7159545044467958, \
          0.2840454955532042, \
          0.9382902632360840, \
          0.0617097367639160, \
          0.9382902632360840, \
          0.0617097367639160, \
          0.9382902632360840, \
          0.0617097367639160, \
          0.9382902632360840, \
          0.0617097367639160, \
          0.3449134012977228, \
          0.3449134012977228, \
          0.7705521820675761, \
          0.3449134012977228, \
          0.3449134012977228, \
          0.7705521820675761, \
          0.6550865987022771, \
          0.6550865987022771, \
          0.7705521820675761, \
          0.6550865987022771, \
          0.6550865987022771, \
          0.7705521820675761, \
          0.3449134012977228, \
          0.3449134012977228, \
          0.2294478179324239, \
          0.3449134012977228, \
          0.3449134012977228, \
          0.2294478179324239, \
          0.6550865987022771, \
          0.6550865987022771, \
          0.2294478179324239, \
          0.6550865987022771, \
          0.6550865987022771, \
          0.2294478179324239, \
          0.9920926274878630, \
          0.9920926274878630, \
          0.9103324974446185, \
          0.9920926274878630, \
          0.9920926274878630, \
          0.9103324974446185, \
          0.0079073725121370, \
          0.0079073725121370, \
          0.9103324974446185, \
          0.0079073725121370, \
          0.0079073725121370, \
          0.9103324974446185, \
          0.9920926274878630, \
          0.9920926274878630, \
          0.0896675025553814, \
          0.9920926274878630, \
          0.9920926274878630, \
          0.0896675025553814, \
          0.0079073725121370, \
          0.0079073725121370, \
          0.0896675025553814, \
          0.0079073725121370, \
          0.0079073725121370, \
          0.0896675025553814, \
          0.9221936167657927, \
          0.9221936167657927, \
          0.4263116836838957, \
          0.9221936167657927, \
          0.9221936167657927, \
          0.4263116836838957, \
          0.0778063832342073, \
          0.0778063832342073, \
          0.4263116836838957, \
          0.0778063832342073, \
          0.0778063832342073, \
          0.4263116836838957, \
          0.9221936167657927, \
          0.9221936167657927, \
          0.5736883163161043, \
          0.9221936167657927, \
          0.9221936167657927, \
          0.5736883163161043, \
          0.0778063832342073, \
          0.0778063832342073, \
          0.5736883163161043, \
          0.0778063832342073, \
          0.0778063832342073, \
          0.5736883163161043, \
          0.7437996999426106, \
          0.7437996999426106, \
          0.8837457372516819, \
          0.7437996999426106, \
          0.7437996999426106, \
          0.8837457372516819, \
          0.2562003000573894, \
          0.2562003000573894, \
          0.8837457372516819, \
          0.2562003000573894, \
          0.2562003000573894, \
          0.8837457372516819, \
          0.7437996999426106, \
          0.7437996999426106, \
          0.1162542627483181, \
          0.7437996999426106, \
          0.7437996999426106, \
          0.1162542627483181, \
          0.2562003000573894, \
          0.2562003000573894, \
          0.1162542627483181, \
          0.2562003000573894, \
          0.2562003000573894, \
          0.1162542627483181, \
          0.8820659248983722, \
          0.8820659248983722, \
          0.6931955182506035, \
          0.8820659248983722, \
          0.8820659248983722, \
          0.6931955182506035, \
          0.1179340751016278, \
          0.1179340751016278, \
          0.6931955182506035, \
          0.1179340751016278, \
          0.1179340751016278, \
          0.6931955182506035, \
          0.8820659248983722, \
          0.8820659248983722, \
          0.3068044817493964, \
          0.8820659248983722, \
          0.8820659248983722, \
          0.3068044817493964, \
          0.1179340751016278, \
          0.1179340751016278, \
          0.3068044817493964, \
          0.1179340751016278, \
          0.1179340751016278, \
          0.3068044817493964, \
          0.8556268694112152, \
          0.8556268694112152, \
          0.9516006474964566, \
          0.8556268694112152, \
          0.8556268694112152, \
          0.9516006474964566, \
          0.1443731305887847, \
          0.1443731305887847, \
          0.9516006474964566, \
          0.1443731305887847, \
          0.1443731305887847, \
          0.9516006474964566, \
          0.8556268694112152, \
          0.8556268694112152, \
          0.0483993525035434, \
          0.8556268694112152, \
          0.8556268694112152, \
          0.0483993525035434, \
          0.1443731305887847, \
          0.1443731305887847, \
          0.0483993525035434, \
          0.1443731305887847, \
          0.1443731305887847, \
          0.0483993525035434, \
          0.9775744747969544, \
          0.9775744747969544, \
          0.6113080322285057, \
          0.9775744747969544, \
          0.9775744747969544, \
          0.6113080322285057, \
          0.0224255252030456, \
          0.0224255252030456, \
          0.6113080322285057, \
          0.0224255252030456, \
          0.0224255252030456, \
          0.6113080322285057, \
          0.9775744747969544, \
          0.9775744747969544, \
          0.3886919677714943, \
          0.9775744747969544, \
          0.9775744747969544, \
          0.3886919677714943, \
          0.0224255252030456, \
          0.0224255252030456, \
          0.3886919677714943, \
          0.0224255252030456, \
          0.0224255252030456, \
          0.3886919677714943, \
          0.5848459901934986, \
          0.5848459901934986, \
          0.9825814337796190, \
          0.5848459901934986, \
          0.5848459901934986, \
          0.9825814337796190, \
          0.4151540098065015, \
          0.4151540098065015, \
          0.9825814337796190, \
          0.4151540098065015, \
          0.4151540098065015, \
          0.9825814337796190, \
          0.5848459901934986, \
          0.5848459901934986, \
          0.0174185662203810, \
          0.5848459901934986, \
          0.5848459901934986, \
          0.0174185662203810, \
          0.4151540098065015, \
          0.4151540098065015, \
          0.0174185662203810, \
          0.4151540098065015, \
          0.4151540098065015, \
          0.0174185662203810, \
          0.8042667629417029, \
          0.8042667629417029, \
          0.5470636340177077, \
          0.8042667629417029, \
          0.8042667629417029, \
          0.5470636340177077, \
          0.1957332370582971, \
          0.1957332370582971, \
          0.5470636340177077, \
          0.1957332370582971, \
          0.1957332370582971, \
          0.5470636340177077, \
          0.8042667629417029, \
          0.8042667629417029, \
          0.4529363659822923, \
          0.8042667629417029, \
          0.8042667629417029, \
          0.4529363659822923, \
          0.1957332370582971, \
          0.1957332370582971, \
          0.4529363659822923, \
          0.1957332370582971, \
          0.1957332370582971, \
          0.4529363659822923, \
          0.7132758893843609, \
          0.7132758893843609, \
          0.9892390565548020, \
          0.7132758893843609, \
          0.7132758893843609, \
          0.9892390565548020, \
          0.2867241106156391, \
          0.2867241106156391, \
          0.9892390565548020, \
          0.2867241106156391, \
          0.2867241106156391, \
          0.9892390565548020, \
          0.7132758893843609, \
          0.7132758893843609, \
          0.0107609434451980, \
          0.7132758893843609, \
          0.7132758893843609, \
          0.0107609434451980, \
          0.2867241106156391, \
          0.2867241106156391, \
          0.0107609434451980, \
          0.2867241106156391, \
          0.2867241106156391, \
          0.0107609434451980, \
          0.5918460351304471, \
          0.5918460351304471, \
          0.8728877113378553, \
          0.5918460351304471, \
          0.5918460351304471, \
          0.8728877113378553, \
          0.4081539648695529, \
          0.4081539648695529, \
          0.8728877113378553, \
          0.4081539648695529, \
          0.4081539648695529, \
          0.8728877113378553, \
          0.5918460351304471, \
          0.5918460351304471, \
          0.1271122886621447, \
          0.5918460351304471, \
          0.5918460351304471, \
          0.1271122886621447, \
          0.4081539648695529, \
          0.4081539648695529, \
          0.1271122886621447, \
          0.4081539648695529, \
          0.4081539648695529, \
          0.1271122886621447, \
          0.6444314510393020, \
          0.9566761563025079, \
          0.6444314510393020, \
          0.9566761563025079, \
          0.8267665443298317, \
          0.8267665443298317, \
          0.6444314510393020, \
          0.9566761563025079, \
          0.6444314510393020, \
          0.9566761563025079, \
          0.1732334556701683, \
          0.1732334556701683, \
          0.6444314510393020, \
          0.0433238436974921, \
          0.6444314510393020, \
          0.0433238436974921, \
          0.8267665443298317, \
          0.8267665443298317, \
          0.3555685489606980, \
          0.9566761563025079, \
          0.3555685489606980, \
          0.9566761563025079, \
          0.8267665443298317, \
          0.8267665443298317, \
          0.6444314510393020, \
          0.0433238436974921, \
          0.6444314510393020, \
          0.0433238436974921, \
          0.1732334556701683, \
          0.1732334556701683, \
          0.3555685489606980, \
          0.9566761563025079, \
          0.3555685489606980, \
          0.9566761563025079, \
          0.1732334556701683, \
          0.1732334556701683, \
          0.3555685489606980, \
          0.0433238436974921, \
          0.3555685489606980, \
          0.0433238436974921, \
          0.8267665443298317, \
          0.8267665443298317, \
          0.3555685489606980, \
          0.0433238436974921, \
          0.3555685489606980, \
          0.0433238436974921, \
          0.1732334556701683, \
          0.1732334556701683, \
          0.7767138770406730, \
          0.9874241069713281, \
          0.7767138770406730, \
          0.9874241069713281, \
          0.9237817545492393, \
          0.9237817545492393, \
          0.7767138770406730, \
          0.9874241069713281, \
          0.7767138770406730, \
          0.9874241069713281, \
          0.0762182454507607, \
          0.0762182454507607, \
          0.7767138770406730, \
          0.0125758930286720, \
          0.7767138770406730, \
          0.0125758930286720, \
          0.9237817545492393, \
          0.9237817545492393, \
          0.2232861229593271, \
          0.9874241069713281, \
          0.2232861229593271, \
          0.9874241069713281, \
          0.9237817545492393, \
          0.9237817545492393, \
          0.7767138770406730, \
          0.0125758930286720, \
          0.7767138770406730, \
          0.0125758930286720, \
          0.0762182454507607, \
          0.0762182454507607, \
          0.2232861229593271, \
          0.9874241069713281, \
          0.2232861229593271, \
          0.9874241069713281, \
          0.0762182454507607, \
          0.0762182454507607, \
          0.2232861229593271, \
          0.0125758930286720, \
          0.2232861229593271, \
          0.0125758930286720, \
          0.9237817545492393, \
          0.9237817545492393, \
          0.2232861229593271, \
          0.0125758930286720, \
          0.2232861229593271, \
          0.0125758930286720, \
          0.0762182454507607, \
          0.0762182454507607 ] )

  w = np.array ( [ \
          0.0020573710057311, \
          0.0020573710057311, \
          0.0020573710057311, \
          0.0020573710057311, \
          0.0020573710057311, \
          0.0020573710057311, \
          0.0009660877915728, \
          0.0009660877915728, \
          0.0009660877915728, \
          0.0009660877915728, \
          0.0009660877915728, \
          0.0009660877915728, \
          0.0009660877915728, \
          0.0009660877915728, \
          0.0016359014467992, \
          0.0016359014467992, \
          0.0016359014467992, \
          0.0016359014467992, \
          0.0016359014467992, \
          0.0016359014467992, \
          0.0016359014467992, \
          0.0016359014467992, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0008499912813105, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0035950037217364, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0038360634296226, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0050441284857989, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0001951830532879, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0017584548406612, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0038873202629322, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0018874010836757, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0016991651835215, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0007588378288378, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0014557629541032, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0040079050757571, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0013991860755843, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0040992807889267, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0019518612573850, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919, \
          0.0009537937942919 ] )

  return x, y, z, w

def rule21 ( ):

#*****************************************************************************80
#
## rule21() returns the hexahedron quadrature rule of precision 21.
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
#    06 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal for Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which add to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.1912521437383576, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8087478562616424, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.3543162299281049, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6456837700718951, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9311291591147122, \
          0.0688708408852879, \
          0.0688708408852879, \
          0.9311291591147122, \
          0.9311291591147122, \
          0.0688708408852879, \
          0.9311291591147122, \
          0.0688708408852879, \
          0.7833399058047521, \
          0.2166600941952480, \
          0.2166600941952480, \
          0.7833399058047521, \
          0.7833399058047521, \
          0.2166600941952480, \
          0.7833399058047521, \
          0.2166600941952480, \
          0.8981144288438190, \
          0.1018855711561810, \
          0.8981144288438190, \
          0.1018855711561810, \
          0.8981144288438190, \
          0.1018855711561810, \
          0.8981144288438190, \
          0.1018855711561810, \
          0.9999999935557286, \
          0.0000000064442714, \
          0.0000000064442714, \
          0.9999999935557286, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9999999935557286, \
          0.0000000064442714, \
          0.0000000064442714, \
          0.9999999935557286, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8467830886160004, \
          0.1532169113839996, \
          0.8467830886160004, \
          0.1532169113839996, \
          0.8467830886160004, \
          0.1532169113839996, \
          0.8467830886160004, \
          0.1532169113839996, \
          0.6731903387258514, \
          0.3268096612741486, \
          0.3268096612741486, \
          0.6731903387258514, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6731903387258514, \
          0.3268096612741486, \
          0.3268096612741486, \
          0.6731903387258514, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9359181010210101, \
          0.0640818989789899, \
          0.9359181010210101, \
          0.0640818989789899, \
          0.9359181010210101, \
          0.0640818989789899, \
          0.9359181010210101, \
          0.0640818989789899, \
          0.1873892499846415, \
          0.8126107500153585, \
          0.8126107500153585, \
          0.1873892499846415, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1873892499846415, \
          0.8126107500153585, \
          0.8126107500153585, \
          0.1873892499846415, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.2917727295202502, \
          0.9026740712514576, \
          0.2917727295202502, \
          0.7082272704797498, \
          0.9026740712514576, \
          0.7082272704797498, \
          0.7082272704797498, \
          0.9026740712514576, \
          0.7082272704797498, \
          0.2917727295202502, \
          0.9026740712514576, \
          0.2917727295202502, \
          0.2917727295202502, \
          0.0973259287485423, \
          0.2917727295202502, \
          0.7082272704797498, \
          0.0973259287485423, \
          0.7082272704797498, \
          0.7082272704797498, \
          0.0973259287485423, \
          0.7082272704797498, \
          0.2917727295202502, \
          0.0973259287485423, \
          0.2917727295202502, \
          0.9869259796545771, \
          0.9372501994187228, \
          0.9869259796545771, \
          0.0130740203454229, \
          0.9372501994187228, \
          0.0130740203454229, \
          0.0130740203454229, \
          0.9372501994187228, \
          0.0130740203454229, \
          0.9869259796545771, \
          0.9372501994187228, \
          0.9869259796545771, \
          0.9869259796545771, \
          0.0627498005812772, \
          0.9869259796545771, \
          0.0130740203454229, \
          0.0627498005812772, \
          0.0130740203454229, \
          0.0130740203454229, \
          0.0627498005812772, \
          0.0130740203454229, \
          0.9869259796545771, \
          0.0627498005812772, \
          0.9869259796545771, \
          0.8645117252804405, \
          0.6225837716647646, \
          0.8645117252804405, \
          0.1354882747195595, \
          0.6225837716647646, \
          0.1354882747195595, \
          0.1354882747195595, \
          0.6225837716647646, \
          0.1354882747195595, \
          0.8645117252804405, \
          0.6225837716647646, \
          0.8645117252804405, \
          0.8645117252804405, \
          0.3774162283352354, \
          0.8645117252804405, \
          0.1354882747195595, \
          0.3774162283352354, \
          0.1354882747195595, \
          0.1354882747195595, \
          0.3774162283352354, \
          0.1354882747195595, \
          0.8645117252804405, \
          0.3774162283352354, \
          0.8645117252804405, \
          0.8248058551406905, \
          0.9220515632141263, \
          0.8248058551406905, \
          0.1751941448593096, \
          0.9220515632141263, \
          0.1751941448593096, \
          0.1751941448593096, \
          0.9220515632141263, \
          0.1751941448593096, \
          0.8248058551406905, \
          0.9220515632141263, \
          0.8248058551406905, \
          0.8248058551406905, \
          0.0779484367858737, \
          0.8248058551406905, \
          0.1751941448593096, \
          0.0779484367858737, \
          0.1751941448593096, \
          0.1751941448593096, \
          0.0779484367858737, \
          0.1751941448593096, \
          0.8248058551406905, \
          0.0779484367858737, \
          0.8248058551406905, \
          0.9459853758476011, \
          0.5650967942783419, \
          0.9459853758476011, \
          0.0540146241523989, \
          0.5650967942783419, \
          0.0540146241523989, \
          0.0540146241523989, \
          0.5650967942783419, \
          0.0540146241523989, \
          0.9459853758476011, \
          0.5650967942783419, \
          0.9459853758476011, \
          0.9459853758476011, \
          0.4349032057216580, \
          0.9459853758476011, \
          0.0540146241523989, \
          0.4349032057216580, \
          0.0540146241523989, \
          0.0540146241523989, \
          0.4349032057216580, \
          0.0540146241523989, \
          0.9459853758476011, \
          0.4349032057216580, \
          0.9459853758476011, \
          0.8916635718645309, \
          0.9766093536267083, \
          0.8916635718645309, \
          0.1083364281354691, \
          0.9766093536267083, \
          0.1083364281354691, \
          0.1083364281354691, \
          0.9766093536267083, \
          0.1083364281354691, \
          0.8916635718645309, \
          0.9766093536267083, \
          0.8916635718645309, \
          0.8916635718645309, \
          0.0233906463732917, \
          0.8916635718645309, \
          0.1083364281354691, \
          0.0233906463732917, \
          0.1083364281354691, \
          0.1083364281354691, \
          0.0233906463732917, \
          0.1083364281354691, \
          0.8916635718645309, \
          0.0233906463732917, \
          0.8916635718645309, \
          0.9849705936644424, \
          0.6355079664366210, \
          0.9849705936644424, \
          0.0150294063355575, \
          0.6355079664366210, \
          0.0150294063355575, \
          0.0150294063355575, \
          0.6355079664366210, \
          0.0150294063355575, \
          0.9849705936644424, \
          0.6355079664366210, \
          0.9849705936644424, \
          0.9849705936644424, \
          0.3644920335633790, \
          0.9849705936644424, \
          0.0150294063355575, \
          0.3644920335633790, \
          0.0150294063355575, \
          0.0150294063355575, \
          0.3644920335633790, \
          0.0150294063355575, \
          0.9849705936644424, \
          0.3644920335633790, \
          0.9849705936644424, \
          0.5860169886103869, \
          0.9923845018898745, \
          0.5860169886103869, \
          0.4139830113896131, \
          0.9923845018898745, \
          0.4139830113896131, \
          0.4139830113896131, \
          0.9923845018898745, \
          0.4139830113896131, \
          0.5860169886103869, \
          0.9923845018898745, \
          0.5860169886103869, \
          0.5860169886103869, \
          0.0076154981101255, \
          0.5860169886103869, \
          0.4139830113896131, \
          0.0076154981101255, \
          0.4139830113896131, \
          0.4139830113896131, \
          0.0076154981101255, \
          0.4139830113896131, \
          0.5860169886103869, \
          0.0076154981101255, \
          0.5860169886103869, \
          0.7690492963095925, \
          0.3896184326892077, \
          0.7690492963095925, \
          0.2309507036904074, \
          0.3896184326892077, \
          0.2309507036904074, \
          0.2309507036904074, \
          0.3896184326892077, \
          0.2309507036904074, \
          0.7690492963095925, \
          0.3896184326892077, \
          0.7690492963095925, \
          0.7690492963095925, \
          0.6103815673107923, \
          0.7690492963095925, \
          0.2309507036904074, \
          0.6103815673107923, \
          0.2309507036904074, \
          0.2309507036904074, \
          0.6103815673107923, \
          0.2309507036904074, \
          0.7690492963095925, \
          0.6103815673107923, \
          0.7690492963095925, \
          0.7768424517946938, \
          0.9994864489115713, \
          0.7768424517946938, \
          0.2231575482053062, \
          0.9994864489115713, \
          0.2231575482053062, \
          0.2231575482053062, \
          0.9994864489115713, \
          0.2231575482053062, \
          0.7768424517946938, \
          0.9994864489115713, \
          0.7768424517946938, \
          0.7768424517946938, \
          0.0005135510884287, \
          0.7768424517946938, \
          0.2231575482053062, \
          0.0005135510884287, \
          0.2231575482053062, \
          0.2231575482053062, \
          0.0005135510884287, \
          0.2231575482053062, \
          0.7768424517946938, \
          0.0005135510884287, \
          0.7768424517946938, \
          0.6117790069755276, \
          0.7209288728023533, \
          0.6117790069755276, \
          0.3882209930244724, \
          0.7209288728023533, \
          0.3882209930244724, \
          0.3882209930244724, \
          0.7209288728023533, \
          0.3882209930244724, \
          0.6117790069755276, \
          0.7209288728023533, \
          0.6117790069755276, \
          0.6117790069755276, \
          0.2790711271976467, \
          0.6117790069755276, \
          0.3882209930244724, \
          0.2790711271976467, \
          0.3882209930244724, \
          0.3882209930244724, \
          0.2790711271976467, \
          0.3882209930244724, \
          0.6117790069755276, \
          0.2790711271976467, \
          0.6117790069755276, \
          0.9350312907963207, \
          0.7494073604468848, \
          0.9350312907963207, \
          0.0649687092036792, \
          0.7494073604468848, \
          0.0649687092036792, \
          0.0649687092036792, \
          0.7494073604468848, \
          0.0649687092036792, \
          0.9350312907963207, \
          0.7494073604468848, \
          0.9350312907963207, \
          0.9350312907963207, \
          0.2505926395531152, \
          0.9350312907963207, \
          0.0649687092036792, \
          0.2505926395531152, \
          0.0649687092036792, \
          0.0649687092036792, \
          0.2505926395531152, \
          0.0649687092036792, \
          0.9350312907963207, \
          0.2505926395531152, \
          0.9350312907963207, \
          0.8750719993006615, \
          0.8750719993006615, \
          0.9719926774632096, \
          0.6986057011288138, \
          0.9719926774632096, \
          0.6986057011288138, \
          0.1249280006993386, \
          0.1249280006993386, \
          0.9719926774632096, \
          0.6986057011288138, \
          0.9719926774632096, \
          0.6986057011288138, \
          0.8750719993006615, \
          0.8750719993006615, \
          0.0280073225367904, \
          0.6986057011288138, \
          0.0280073225367904, \
          0.6986057011288138, \
          0.8750719993006615, \
          0.8750719993006615, \
          0.9719926774632096, \
          0.3013942988711862, \
          0.9719926774632096, \
          0.3013942988711862, \
          0.1249280006993386, \
          0.1249280006993386, \
          0.0280073225367904, \
          0.6986057011288138, \
          0.0280073225367904, \
          0.6986057011288138, \
          0.1249280006993386, \
          0.1249280006993386, \
          0.9719926774632096, \
          0.3013942988711862, \
          0.9719926774632096, \
          0.3013942988711862, \
          0.8750719993006615, \
          0.8750719993006615, \
          0.0280073225367904, \
          0.3013942988711862, \
          0.0280073225367904, \
          0.3013942988711862, \
          0.1249280006993386, \
          0.1249280006993386, \
          0.0280073225367904, \
          0.3013942988711862, \
          0.0280073225367904, \
          0.3013942988711862, \
          0.9512929061479376, \
          0.9512929061479376, \
          0.9923118941018740, \
          0.8153563222457214, \
          0.9923118941018740, \
          0.8153563222457214, \
          0.0487070938520624, \
          0.0487070938520624, \
          0.9923118941018740, \
          0.8153563222457214, \
          0.9923118941018740, \
          0.8153563222457214, \
          0.9512929061479376, \
          0.9512929061479376, \
          0.0076881058981259, \
          0.8153563222457214, \
          0.0076881058981259, \
          0.8153563222457214, \
          0.9512929061479376, \
          0.9512929061479376, \
          0.9923118941018740, \
          0.1846436777542786, \
          0.9923118941018740, \
          0.1846436777542786, \
          0.0487070938520624, \
          0.0487070938520624, \
          0.0076881058981259, \
          0.8153563222457214, \
          0.0076881058981259, \
          0.8153563222457214, \
          0.0487070938520624, \
          0.0487070938520624, \
          0.9923118941018740, \
          0.1846436777542786, \
          0.9923118941018740, \
          0.1846436777542786, \
          0.9512929061479376, \
          0.9512929061479376, \
          0.0076881058981259, \
          0.1846436777542786, \
          0.0076881058981259, \
          0.1846436777542786, \
          0.0487070938520624, \
          0.0487070938520624, \
          0.0076881058981259, \
          0.1846436777542786, \
          0.0076881058981259, \
          0.1846436777542786, \
          0.6108897298239304, \
          0.6108897298239304, \
          0.5491142465864416, \
          0.9360994289291793, \
          0.5491142465864416, \
          0.9360994289291793, \
          0.3891102701760696, \
          0.3891102701760696, \
          0.5491142465864416, \
          0.9360994289291793, \
          0.5491142465864416, \
          0.9360994289291793, \
          0.6108897298239304, \
          0.6108897298239304, \
          0.4508857534135584, \
          0.9360994289291793, \
          0.4508857534135584, \
          0.9360994289291793, \
          0.6108897298239304, \
          0.6108897298239304, \
          0.5491142465864416, \
          0.0639005710708208, \
          0.5491142465864416, \
          0.0639005710708208, \
          0.3891102701760696, \
          0.3891102701760696, \
          0.4508857534135584, \
          0.9360994289291793, \
          0.4508857534135584, \
          0.9360994289291793, \
          0.3891102701760696, \
          0.3891102701760696, \
          0.5491142465864416, \
          0.0639005710708208, \
          0.5491142465864416, \
          0.0639005710708208, \
          0.6108897298239304, \
          0.6108897298239304, \
          0.4508857534135584, \
          0.0639005710708208, \
          0.4508857534135584, \
          0.0639005710708208, \
          0.3891102701760696, \
          0.3891102701760696, \
          0.4508857534135584, \
          0.0639005710708208, \
          0.4508857534135584, \
          0.0639005710708208, \
          0.9784211281771267, \
          0.9784211281771267, \
          0.6040696445748173, \
          0.7479204633014319, \
          0.6040696445748173, \
          0.7479204633014319, \
          0.0215788718228733, \
          0.0215788718228733, \
          0.6040696445748173, \
          0.7479204633014319, \
          0.6040696445748173, \
          0.7479204633014319, \
          0.9784211281771267, \
          0.9784211281771267, \
          0.3959303554251827, \
          0.7479204633014319, \
          0.3959303554251827, \
          0.7479204633014319, \
          0.9784211281771267, \
          0.9784211281771267, \
          0.6040696445748173, \
          0.2520795366985681, \
          0.6040696445748173, \
          0.2520795366985681, \
          0.0215788718228733, \
          0.0215788718228733, \
          0.3959303554251827, \
          0.7479204633014319, \
          0.3959303554251827, \
          0.7479204633014319, \
          0.0215788718228733, \
          0.0215788718228733, \
          0.6040696445748173, \
          0.2520795366985681, \
          0.6040696445748173, \
          0.2520795366985681, \
          0.9784211281771267, \
          0.9784211281771267, \
          0.3959303554251827, \
          0.2520795366985681, \
          0.3959303554251827, \
          0.2520795366985681, \
          0.0215788718228733, \
          0.0215788718228733, \
          0.3959303554251827, \
          0.2520795366985681, \
          0.3959303554251827, \
          0.2520795366985681 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.1912521437383576, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8087478562616424, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.3543162299281049, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6456837700718951, \
          0.5000000000000000, \
          0.9311291591147122, \
          0.0688708408852879, \
          0.9311291591147122, \
          0.0688708408852879, \
          0.9311291591147122, \
          0.0688708408852879, \
          0.0688708408852879, \
          0.9311291591147122, \
          0.7833399058047521, \
          0.2166600941952480, \
          0.7833399058047521, \
          0.2166600941952480, \
          0.7833399058047521, \
          0.2166600941952480, \
          0.2166600941952480, \
          0.7833399058047521, \
          0.9999999935557286, \
          0.0000000064442714, \
          0.0000000064442714, \
          0.9999999935557286, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8981144288438190, \
          0.1018855711561810, \
          0.8981144288438190, \
          0.1018855711561810, \
          0.8981144288438190, \
          0.1018855711561810, \
          0.8981144288438190, \
          0.1018855711561810, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9999999935557286, \
          0.0000000064442714, \
          0.0000000064442714, \
          0.9999999935557286, \
          0.6731903387258514, \
          0.3268096612741486, \
          0.3268096612741486, \
          0.6731903387258514, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8467830886160004, \
          0.1532169113839996, \
          0.8467830886160004, \
          0.1532169113839996, \
          0.8467830886160004, \
          0.1532169113839996, \
          0.8467830886160004, \
          0.1532169113839996, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6731903387258514, \
          0.3268096612741486, \
          0.3268096612741486, \
          0.6731903387258514, \
          0.1873892499846415, \
          0.8126107500153585, \
          0.8126107500153585, \
          0.1873892499846415, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9359181010210101, \
          0.0640818989789899, \
          0.9359181010210101, \
          0.0640818989789899, \
          0.9359181010210101, \
          0.0640818989789899, \
          0.9359181010210101, \
          0.0640818989789899, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1873892499846415, \
          0.8126107500153585, \
          0.8126107500153585, \
          0.1873892499846415, \
          0.9026740712514576, \
          0.2917727295202502, \
          0.2917727295202502, \
          0.9026740712514576, \
          0.7082272704797498, \
          0.2917727295202502, \
          0.9026740712514576, \
          0.7082272704797498, \
          0.7082272704797498, \
          0.9026740712514576, \
          0.2917727295202502, \
          0.7082272704797498, \
          0.0973259287485423, \
          0.2917727295202502, \
          0.2917727295202502, \
          0.0973259287485423, \
          0.7082272704797498, \
          0.2917727295202502, \
          0.0973259287485423, \
          0.7082272704797498, \
          0.7082272704797498, \
          0.0973259287485423, \
          0.2917727295202502, \
          0.7082272704797498, \
          0.9372501994187228, \
          0.9869259796545771, \
          0.9869259796545771, \
          0.9372501994187228, \
          0.0130740203454229, \
          0.9869259796545771, \
          0.9372501994187228, \
          0.0130740203454229, \
          0.0130740203454229, \
          0.9372501994187228, \
          0.9869259796545771, \
          0.0130740203454229, \
          0.0627498005812772, \
          0.9869259796545771, \
          0.9869259796545771, \
          0.0627498005812772, \
          0.0130740203454229, \
          0.9869259796545771, \
          0.0627498005812772, \
          0.0130740203454229, \
          0.0130740203454229, \
          0.0627498005812772, \
          0.9869259796545771, \
          0.0130740203454229, \
          0.6225837716647646, \
          0.8645117252804405, \
          0.8645117252804405, \
          0.6225837716647646, \
          0.1354882747195595, \
          0.8645117252804405, \
          0.6225837716647646, \
          0.1354882747195595, \
          0.1354882747195595, \
          0.6225837716647646, \
          0.8645117252804405, \
          0.1354882747195595, \
          0.3774162283352354, \
          0.8645117252804405, \
          0.8645117252804405, \
          0.3774162283352354, \
          0.1354882747195595, \
          0.8645117252804405, \
          0.3774162283352354, \
          0.1354882747195595, \
          0.1354882747195595, \
          0.3774162283352354, \
          0.8645117252804405, \
          0.1354882747195595, \
          0.9220515632141263, \
          0.8248058551406905, \
          0.8248058551406905, \
          0.9220515632141263, \
          0.1751941448593096, \
          0.8248058551406905, \
          0.9220515632141263, \
          0.1751941448593096, \
          0.1751941448593096, \
          0.9220515632141263, \
          0.8248058551406905, \
          0.1751941448593096, \
          0.0779484367858737, \
          0.8248058551406905, \
          0.8248058551406905, \
          0.0779484367858737, \
          0.1751941448593096, \
          0.8248058551406905, \
          0.0779484367858737, \
          0.1751941448593096, \
          0.1751941448593096, \
          0.0779484367858737, \
          0.8248058551406905, \
          0.1751941448593096, \
          0.5650967942783419, \
          0.9459853758476011, \
          0.9459853758476011, \
          0.5650967942783419, \
          0.0540146241523989, \
          0.9459853758476011, \
          0.5650967942783419, \
          0.0540146241523989, \
          0.0540146241523989, \
          0.5650967942783419, \
          0.9459853758476011, \
          0.0540146241523989, \
          0.4349032057216580, \
          0.9459853758476011, \
          0.9459853758476011, \
          0.4349032057216580, \
          0.0540146241523989, \
          0.9459853758476011, \
          0.4349032057216580, \
          0.0540146241523989, \
          0.0540146241523989, \
          0.4349032057216580, \
          0.9459853758476011, \
          0.0540146241523989, \
          0.9766093536267083, \
          0.8916635718645309, \
          0.8916635718645309, \
          0.9766093536267083, \
          0.1083364281354691, \
          0.8916635718645309, \
          0.9766093536267083, \
          0.1083364281354691, \
          0.1083364281354691, \
          0.9766093536267083, \
          0.8916635718645309, \
          0.1083364281354691, \
          0.0233906463732917, \
          0.8916635718645309, \
          0.8916635718645309, \
          0.0233906463732917, \
          0.1083364281354691, \
          0.8916635718645309, \
          0.0233906463732917, \
          0.1083364281354691, \
          0.1083364281354691, \
          0.0233906463732917, \
          0.8916635718645309, \
          0.1083364281354691, \
          0.6355079664366210, \
          0.9849705936644424, \
          0.9849705936644424, \
          0.6355079664366210, \
          0.0150294063355575, \
          0.9849705936644424, \
          0.6355079664366210, \
          0.0150294063355575, \
          0.0150294063355575, \
          0.6355079664366210, \
          0.9849705936644424, \
          0.0150294063355575, \
          0.3644920335633790, \
          0.9849705936644424, \
          0.9849705936644424, \
          0.3644920335633790, \
          0.0150294063355575, \
          0.9849705936644424, \
          0.3644920335633790, \
          0.0150294063355575, \
          0.0150294063355575, \
          0.3644920335633790, \
          0.9849705936644424, \
          0.0150294063355575, \
          0.9923845018898745, \
          0.5860169886103869, \
          0.5860169886103869, \
          0.9923845018898745, \
          0.4139830113896131, \
          0.5860169886103869, \
          0.9923845018898745, \
          0.4139830113896131, \
          0.4139830113896131, \
          0.9923845018898745, \
          0.5860169886103869, \
          0.4139830113896131, \
          0.0076154981101255, \
          0.5860169886103869, \
          0.5860169886103869, \
          0.0076154981101255, \
          0.4139830113896131, \
          0.5860169886103869, \
          0.0076154981101255, \
          0.4139830113896131, \
          0.4139830113896131, \
          0.0076154981101255, \
          0.5860169886103869, \
          0.4139830113896131, \
          0.3896184326892077, \
          0.7690492963095925, \
          0.7690492963095925, \
          0.3896184326892077, \
          0.2309507036904074, \
          0.7690492963095925, \
          0.3896184326892077, \
          0.2309507036904074, \
          0.2309507036904074, \
          0.3896184326892077, \
          0.7690492963095925, \
          0.2309507036904074, \
          0.6103815673107923, \
          0.7690492963095925, \
          0.7690492963095925, \
          0.6103815673107923, \
          0.2309507036904074, \
          0.7690492963095925, \
          0.6103815673107923, \
          0.2309507036904074, \
          0.2309507036904074, \
          0.6103815673107923, \
          0.7690492963095925, \
          0.2309507036904074, \
          0.9994864489115713, \
          0.7768424517946938, \
          0.7768424517946938, \
          0.9994864489115713, \
          0.2231575482053062, \
          0.7768424517946938, \
          0.9994864489115713, \
          0.2231575482053062, \
          0.2231575482053062, \
          0.9994864489115713, \
          0.7768424517946938, \
          0.2231575482053062, \
          0.0005135510884287, \
          0.7768424517946938, \
          0.7768424517946938, \
          0.0005135510884287, \
          0.2231575482053062, \
          0.7768424517946938, \
          0.0005135510884287, \
          0.2231575482053062, \
          0.2231575482053062, \
          0.0005135510884287, \
          0.7768424517946938, \
          0.2231575482053062, \
          0.7209288728023533, \
          0.6117790069755276, \
          0.6117790069755276, \
          0.7209288728023533, \
          0.3882209930244724, \
          0.6117790069755276, \
          0.7209288728023533, \
          0.3882209930244724, \
          0.3882209930244724, \
          0.7209288728023533, \
          0.6117790069755276, \
          0.3882209930244724, \
          0.2790711271976467, \
          0.6117790069755276, \
          0.6117790069755276, \
          0.2790711271976467, \
          0.3882209930244724, \
          0.6117790069755276, \
          0.2790711271976467, \
          0.3882209930244724, \
          0.3882209930244724, \
          0.2790711271976467, \
          0.6117790069755276, \
          0.3882209930244724, \
          0.7494073604468848, \
          0.9350312907963207, \
          0.9350312907963207, \
          0.7494073604468848, \
          0.0649687092036792, \
          0.9350312907963207, \
          0.7494073604468848, \
          0.0649687092036792, \
          0.0649687092036792, \
          0.7494073604468848, \
          0.9350312907963207, \
          0.0649687092036792, \
          0.2505926395531152, \
          0.9350312907963207, \
          0.9350312907963207, \
          0.2505926395531152, \
          0.0649687092036792, \
          0.9350312907963207, \
          0.2505926395531152, \
          0.0649687092036792, \
          0.0649687092036792, \
          0.2505926395531152, \
          0.9350312907963207, \
          0.0649687092036792, \
          0.9719926774632096, \
          0.6986057011288138, \
          0.8750719993006615, \
          0.8750719993006615, \
          0.6986057011288138, \
          0.9719926774632096, \
          0.9719926774632096, \
          0.6986057011288138, \
          0.1249280006993386, \
          0.1249280006993386, \
          0.6986057011288138, \
          0.9719926774632096, \
          0.0280073225367904, \
          0.6986057011288138, \
          0.8750719993006615, \
          0.8750719993006615, \
          0.6986057011288138, \
          0.0280073225367904, \
          0.9719926774632096, \
          0.3013942988711862, \
          0.8750719993006615, \
          0.8750719993006615, \
          0.3013942988711862, \
          0.9719926774632096, \
          0.0280073225367904, \
          0.6986057011288138, \
          0.1249280006993386, \
          0.1249280006993386, \
          0.6986057011288138, \
          0.0280073225367904, \
          0.9719926774632096, \
          0.3013942988711862, \
          0.1249280006993386, \
          0.1249280006993386, \
          0.3013942988711862, \
          0.9719926774632096, \
          0.0280073225367904, \
          0.3013942988711862, \
          0.8750719993006615, \
          0.8750719993006615, \
          0.3013942988711862, \
          0.0280073225367904, \
          0.0280073225367904, \
          0.3013942988711862, \
          0.1249280006993386, \
          0.1249280006993386, \
          0.3013942988711862, \
          0.0280073225367904, \
          0.9923118941018740, \
          0.8153563222457214, \
          0.9512929061479376, \
          0.9512929061479376, \
          0.8153563222457214, \
          0.9923118941018740, \
          0.9923118941018740, \
          0.8153563222457214, \
          0.0487070938520624, \
          0.0487070938520624, \
          0.8153563222457214, \
          0.9923118941018740, \
          0.0076881058981259, \
          0.8153563222457214, \
          0.9512929061479376, \
          0.9512929061479376, \
          0.8153563222457214, \
          0.0076881058981259, \
          0.9923118941018740, \
          0.1846436777542786, \
          0.9512929061479376, \
          0.9512929061479376, \
          0.1846436777542786, \
          0.9923118941018740, \
          0.0076881058981259, \
          0.8153563222457214, \
          0.0487070938520624, \
          0.0487070938520624, \
          0.8153563222457214, \
          0.0076881058981259, \
          0.9923118941018740, \
          0.1846436777542786, \
          0.0487070938520624, \
          0.0487070938520624, \
          0.1846436777542786, \
          0.9923118941018740, \
          0.0076881058981259, \
          0.1846436777542786, \
          0.9512929061479376, \
          0.9512929061479376, \
          0.1846436777542786, \
          0.0076881058981259, \
          0.0076881058981259, \
          0.1846436777542786, \
          0.0487070938520624, \
          0.0487070938520624, \
          0.1846436777542786, \
          0.0076881058981259, \
          0.5491142465864416, \
          0.9360994289291793, \
          0.6108897298239304, \
          0.6108897298239304, \
          0.9360994289291793, \
          0.5491142465864416, \
          0.5491142465864416, \
          0.9360994289291793, \
          0.3891102701760696, \
          0.3891102701760696, \
          0.9360994289291793, \
          0.5491142465864416, \
          0.4508857534135584, \
          0.9360994289291793, \
          0.6108897298239304, \
          0.6108897298239304, \
          0.9360994289291793, \
          0.4508857534135584, \
          0.5491142465864416, \
          0.0639005710708208, \
          0.6108897298239304, \
          0.6108897298239304, \
          0.0639005710708208, \
          0.5491142465864416, \
          0.4508857534135584, \
          0.9360994289291793, \
          0.3891102701760696, \
          0.3891102701760696, \
          0.9360994289291793, \
          0.4508857534135584, \
          0.5491142465864416, \
          0.0639005710708208, \
          0.3891102701760696, \
          0.3891102701760696, \
          0.0639005710708208, \
          0.5491142465864416, \
          0.4508857534135584, \
          0.0639005710708208, \
          0.6108897298239304, \
          0.6108897298239304, \
          0.0639005710708208, \
          0.4508857534135584, \
          0.4508857534135584, \
          0.0639005710708208, \
          0.3891102701760696, \
          0.3891102701760696, \
          0.0639005710708208, \
          0.4508857534135584, \
          0.6040696445748173, \
          0.7479204633014319, \
          0.9784211281771267, \
          0.9784211281771267, \
          0.7479204633014319, \
          0.6040696445748173, \
          0.6040696445748173, \
          0.7479204633014319, \
          0.0215788718228733, \
          0.0215788718228733, \
          0.7479204633014319, \
          0.6040696445748173, \
          0.3959303554251827, \
          0.7479204633014319, \
          0.9784211281771267, \
          0.9784211281771267, \
          0.7479204633014319, \
          0.3959303554251827, \
          0.6040696445748173, \
          0.2520795366985681, \
          0.9784211281771267, \
          0.9784211281771267, \
          0.2520795366985681, \
          0.6040696445748173, \
          0.3959303554251827, \
          0.7479204633014319, \
          0.0215788718228733, \
          0.0215788718228733, \
          0.7479204633014319, \
          0.3959303554251827, \
          0.6040696445748173, \
          0.2520795366985681, \
          0.0215788718228733, \
          0.0215788718228733, \
          0.2520795366985681, \
          0.6040696445748173, \
          0.3959303554251827, \
          0.2520795366985681, \
          0.9784211281771267, \
          0.9784211281771267, \
          0.2520795366985681, \
          0.3959303554251827, \
          0.3959303554251827, \
          0.2520795366985681, \
          0.0215788718228733, \
          0.0215788718228733, \
          0.2520795366985681, \
          0.3959303554251827 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1912521437383576, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8087478562616424, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.3543162299281049, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6456837700718951, \
          0.9311291591147122, \
          0.0688708408852879, \
          0.9311291591147122, \
          0.9311291591147122, \
          0.0688708408852879, \
          0.9311291591147122, \
          0.0688708408852879, \
          0.0688708408852879, \
          0.7833399058047521, \
          0.2166600941952480, \
          0.7833399058047521, \
          0.7833399058047521, \
          0.2166600941952480, \
          0.7833399058047521, \
          0.2166600941952480, \
          0.2166600941952480, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9999999935557286, \
          0.0000000064442714, \
          0.0000000064442714, \
          0.9999999935557286, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9999999935557286, \
          0.0000000064442714, \
          0.0000000064442714, \
          0.9999999935557286, \
          0.8981144288438190, \
          0.1018855711561810, \
          0.8981144288438190, \
          0.1018855711561810, \
          0.8981144288438190, \
          0.1018855711561810, \
          0.8981144288438190, \
          0.1018855711561810, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6731903387258514, \
          0.3268096612741486, \
          0.3268096612741486, \
          0.6731903387258514, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6731903387258514, \
          0.3268096612741486, \
          0.3268096612741486, \
          0.6731903387258514, \
          0.8467830886160004, \
          0.1532169113839996, \
          0.8467830886160004, \
          0.1532169113839996, \
          0.8467830886160004, \
          0.1532169113839996, \
          0.8467830886160004, \
          0.1532169113839996, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1873892499846415, \
          0.8126107500153585, \
          0.8126107500153585, \
          0.1873892499846415, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1873892499846415, \
          0.8126107500153585, \
          0.8126107500153585, \
          0.1873892499846415, \
          0.9359181010210101, \
          0.0640818989789899, \
          0.9359181010210101, \
          0.0640818989789899, \
          0.9359181010210101, \
          0.0640818989789899, \
          0.9359181010210101, \
          0.0640818989789899, \
          0.2917727295202502, \
          0.2917727295202502, \
          0.9026740712514576, \
          0.2917727295202502, \
          0.2917727295202502, \
          0.9026740712514576, \
          0.7082272704797498, \
          0.7082272704797498, \
          0.9026740712514576, \
          0.7082272704797498, \
          0.7082272704797498, \
          0.9026740712514576, \
          0.2917727295202502, \
          0.2917727295202502, \
          0.0973259287485423, \
          0.2917727295202502, \
          0.2917727295202502, \
          0.0973259287485423, \
          0.7082272704797498, \
          0.7082272704797498, \
          0.0973259287485423, \
          0.7082272704797498, \
          0.7082272704797498, \
          0.0973259287485423, \
          0.9869259796545771, \
          0.9869259796545771, \
          0.9372501994187228, \
          0.9869259796545771, \
          0.9869259796545771, \
          0.9372501994187228, \
          0.0130740203454229, \
          0.0130740203454229, \
          0.9372501994187228, \
          0.0130740203454229, \
          0.0130740203454229, \
          0.9372501994187228, \
          0.9869259796545771, \
          0.9869259796545771, \
          0.0627498005812772, \
          0.9869259796545771, \
          0.9869259796545771, \
          0.0627498005812772, \
          0.0130740203454229, \
          0.0130740203454229, \
          0.0627498005812772, \
          0.0130740203454229, \
          0.0130740203454229, \
          0.0627498005812772, \
          0.8645117252804405, \
          0.8645117252804405, \
          0.6225837716647646, \
          0.8645117252804405, \
          0.8645117252804405, \
          0.6225837716647646, \
          0.1354882747195595, \
          0.1354882747195595, \
          0.6225837716647646, \
          0.1354882747195595, \
          0.1354882747195595, \
          0.6225837716647646, \
          0.8645117252804405, \
          0.8645117252804405, \
          0.3774162283352354, \
          0.8645117252804405, \
          0.8645117252804405, \
          0.3774162283352354, \
          0.1354882747195595, \
          0.1354882747195595, \
          0.3774162283352354, \
          0.1354882747195595, \
          0.1354882747195595, \
          0.3774162283352354, \
          0.8248058551406905, \
          0.8248058551406905, \
          0.9220515632141263, \
          0.8248058551406905, \
          0.8248058551406905, \
          0.9220515632141263, \
          0.1751941448593096, \
          0.1751941448593096, \
          0.9220515632141263, \
          0.1751941448593096, \
          0.1751941448593096, \
          0.9220515632141263, \
          0.8248058551406905, \
          0.8248058551406905, \
          0.0779484367858737, \
          0.8248058551406905, \
          0.8248058551406905, \
          0.0779484367858737, \
          0.1751941448593096, \
          0.1751941448593096, \
          0.0779484367858737, \
          0.1751941448593096, \
          0.1751941448593096, \
          0.0779484367858737, \
          0.9459853758476011, \
          0.9459853758476011, \
          0.5650967942783419, \
          0.9459853758476011, \
          0.9459853758476011, \
          0.5650967942783419, \
          0.0540146241523989, \
          0.0540146241523989, \
          0.5650967942783419, \
          0.0540146241523989, \
          0.0540146241523989, \
          0.5650967942783419, \
          0.9459853758476011, \
          0.9459853758476011, \
          0.4349032057216580, \
          0.9459853758476011, \
          0.9459853758476011, \
          0.4349032057216580, \
          0.0540146241523989, \
          0.0540146241523989, \
          0.4349032057216580, \
          0.0540146241523989, \
          0.0540146241523989, \
          0.4349032057216580, \
          0.8916635718645309, \
          0.8916635718645309, \
          0.9766093536267083, \
          0.8916635718645309, \
          0.8916635718645309, \
          0.9766093536267083, \
          0.1083364281354691, \
          0.1083364281354691, \
          0.9766093536267083, \
          0.1083364281354691, \
          0.1083364281354691, \
          0.9766093536267083, \
          0.8916635718645309, \
          0.8916635718645309, \
          0.0233906463732917, \
          0.8916635718645309, \
          0.8916635718645309, \
          0.0233906463732917, \
          0.1083364281354691, \
          0.1083364281354691, \
          0.0233906463732917, \
          0.1083364281354691, \
          0.1083364281354691, \
          0.0233906463732917, \
          0.9849705936644424, \
          0.9849705936644424, \
          0.6355079664366210, \
          0.9849705936644424, \
          0.9849705936644424, \
          0.6355079664366210, \
          0.0150294063355575, \
          0.0150294063355575, \
          0.6355079664366210, \
          0.0150294063355575, \
          0.0150294063355575, \
          0.6355079664366210, \
          0.9849705936644424, \
          0.9849705936644424, \
          0.3644920335633790, \
          0.9849705936644424, \
          0.9849705936644424, \
          0.3644920335633790, \
          0.0150294063355575, \
          0.0150294063355575, \
          0.3644920335633790, \
          0.0150294063355575, \
          0.0150294063355575, \
          0.3644920335633790, \
          0.5860169886103869, \
          0.5860169886103869, \
          0.9923845018898745, \
          0.5860169886103869, \
          0.5860169886103869, \
          0.9923845018898745, \
          0.4139830113896131, \
          0.4139830113896131, \
          0.9923845018898745, \
          0.4139830113896131, \
          0.4139830113896131, \
          0.9923845018898745, \
          0.5860169886103869, \
          0.5860169886103869, \
          0.0076154981101255, \
          0.5860169886103869, \
          0.5860169886103869, \
          0.0076154981101255, \
          0.4139830113896131, \
          0.4139830113896131, \
          0.0076154981101255, \
          0.4139830113896131, \
          0.4139830113896131, \
          0.0076154981101255, \
          0.7690492963095925, \
          0.7690492963095925, \
          0.3896184326892077, \
          0.7690492963095925, \
          0.7690492963095925, \
          0.3896184326892077, \
          0.2309507036904074, \
          0.2309507036904074, \
          0.3896184326892077, \
          0.2309507036904074, \
          0.2309507036904074, \
          0.3896184326892077, \
          0.7690492963095925, \
          0.7690492963095925, \
          0.6103815673107923, \
          0.7690492963095925, \
          0.7690492963095925, \
          0.6103815673107923, \
          0.2309507036904074, \
          0.2309507036904074, \
          0.6103815673107923, \
          0.2309507036904074, \
          0.2309507036904074, \
          0.6103815673107923, \
          0.7768424517946938, \
          0.7768424517946938, \
          0.9994864489115713, \
          0.7768424517946938, \
          0.7768424517946938, \
          0.9994864489115713, \
          0.2231575482053062, \
          0.2231575482053062, \
          0.9994864489115713, \
          0.2231575482053062, \
          0.2231575482053062, \
          0.9994864489115713, \
          0.7768424517946938, \
          0.7768424517946938, \
          0.0005135510884287, \
          0.7768424517946938, \
          0.7768424517946938, \
          0.0005135510884287, \
          0.2231575482053062, \
          0.2231575482053062, \
          0.0005135510884287, \
          0.2231575482053062, \
          0.2231575482053062, \
          0.0005135510884287, \
          0.6117790069755276, \
          0.6117790069755276, \
          0.7209288728023533, \
          0.6117790069755276, \
          0.6117790069755276, \
          0.7209288728023533, \
          0.3882209930244724, \
          0.3882209930244724, \
          0.7209288728023533, \
          0.3882209930244724, \
          0.3882209930244724, \
          0.7209288728023533, \
          0.6117790069755276, \
          0.6117790069755276, \
          0.2790711271976467, \
          0.6117790069755276, \
          0.6117790069755276, \
          0.2790711271976467, \
          0.3882209930244724, \
          0.3882209930244724, \
          0.2790711271976467, \
          0.3882209930244724, \
          0.3882209930244724, \
          0.2790711271976467, \
          0.9350312907963207, \
          0.9350312907963207, \
          0.7494073604468848, \
          0.9350312907963207, \
          0.9350312907963207, \
          0.7494073604468848, \
          0.0649687092036792, \
          0.0649687092036792, \
          0.7494073604468848, \
          0.0649687092036792, \
          0.0649687092036792, \
          0.7494073604468848, \
          0.9350312907963207, \
          0.9350312907963207, \
          0.2505926395531152, \
          0.9350312907963207, \
          0.9350312907963207, \
          0.2505926395531152, \
          0.0649687092036792, \
          0.0649687092036792, \
          0.2505926395531152, \
          0.0649687092036792, \
          0.0649687092036792, \
          0.2505926395531152, \
          0.6986057011288138, \
          0.9719926774632096, \
          0.6986057011288138, \
          0.9719926774632096, \
          0.8750719993006615, \
          0.8750719993006615, \
          0.6986057011288138, \
          0.9719926774632096, \
          0.6986057011288138, \
          0.9719926774632096, \
          0.1249280006993386, \
          0.1249280006993386, \
          0.6986057011288138, \
          0.0280073225367904, \
          0.6986057011288138, \
          0.0280073225367904, \
          0.8750719993006615, \
          0.8750719993006615, \
          0.3013942988711862, \
          0.9719926774632096, \
          0.3013942988711862, \
          0.9719926774632096, \
          0.8750719993006615, \
          0.8750719993006615, \
          0.6986057011288138, \
          0.0280073225367904, \
          0.6986057011288138, \
          0.0280073225367904, \
          0.1249280006993386, \
          0.1249280006993386, \
          0.3013942988711862, \
          0.9719926774632096, \
          0.3013942988711862, \
          0.9719926774632096, \
          0.1249280006993386, \
          0.1249280006993386, \
          0.3013942988711862, \
          0.0280073225367904, \
          0.3013942988711862, \
          0.0280073225367904, \
          0.8750719993006615, \
          0.8750719993006615, \
          0.3013942988711862, \
          0.0280073225367904, \
          0.3013942988711862, \
          0.0280073225367904, \
          0.1249280006993386, \
          0.1249280006993386, \
          0.8153563222457214, \
          0.9923118941018740, \
          0.8153563222457214, \
          0.9923118941018740, \
          0.9512929061479376, \
          0.9512929061479376, \
          0.8153563222457214, \
          0.9923118941018740, \
          0.8153563222457214, \
          0.9923118941018740, \
          0.0487070938520624, \
          0.0487070938520624, \
          0.8153563222457214, \
          0.0076881058981259, \
          0.8153563222457214, \
          0.0076881058981259, \
          0.9512929061479376, \
          0.9512929061479376, \
          0.1846436777542786, \
          0.9923118941018740, \
          0.1846436777542786, \
          0.9923118941018740, \
          0.9512929061479376, \
          0.9512929061479376, \
          0.8153563222457214, \
          0.0076881058981259, \
          0.8153563222457214, \
          0.0076881058981259, \
          0.0487070938520624, \
          0.0487070938520624, \
          0.1846436777542786, \
          0.9923118941018740, \
          0.1846436777542786, \
          0.9923118941018740, \
          0.0487070938520624, \
          0.0487070938520624, \
          0.1846436777542786, \
          0.0076881058981259, \
          0.1846436777542786, \
          0.0076881058981259, \
          0.9512929061479376, \
          0.9512929061479376, \
          0.1846436777542786, \
          0.0076881058981259, \
          0.1846436777542786, \
          0.0076881058981259, \
          0.0487070938520624, \
          0.0487070938520624, \
          0.9360994289291793, \
          0.5491142465864416, \
          0.9360994289291793, \
          0.5491142465864416, \
          0.6108897298239304, \
          0.6108897298239304, \
          0.9360994289291793, \
          0.5491142465864416, \
          0.9360994289291793, \
          0.5491142465864416, \
          0.3891102701760696, \
          0.3891102701760696, \
          0.9360994289291793, \
          0.4508857534135584, \
          0.9360994289291793, \
          0.4508857534135584, \
          0.6108897298239304, \
          0.6108897298239304, \
          0.0639005710708208, \
          0.5491142465864416, \
          0.0639005710708208, \
          0.5491142465864416, \
          0.6108897298239304, \
          0.6108897298239304, \
          0.9360994289291793, \
          0.4508857534135584, \
          0.9360994289291793, \
          0.4508857534135584, \
          0.3891102701760696, \
          0.3891102701760696, \
          0.0639005710708208, \
          0.5491142465864416, \
          0.0639005710708208, \
          0.5491142465864416, \
          0.3891102701760696, \
          0.3891102701760696, \
          0.0639005710708208, \
          0.4508857534135584, \
          0.0639005710708208, \
          0.4508857534135584, \
          0.6108897298239304, \
          0.6108897298239304, \
          0.0639005710708208, \
          0.4508857534135584, \
          0.0639005710708208, \
          0.4508857534135584, \
          0.3891102701760696, \
          0.3891102701760696, \
          0.7479204633014319, \
          0.6040696445748173, \
          0.7479204633014319, \
          0.6040696445748173, \
          0.9784211281771267, \
          0.9784211281771267, \
          0.7479204633014319, \
          0.6040696445748173, \
          0.7479204633014319, \
          0.6040696445748173, \
          0.0215788718228733, \
          0.0215788718228733, \
          0.7479204633014319, \
          0.3959303554251827, \
          0.7479204633014319, \
          0.3959303554251827, \
          0.9784211281771267, \
          0.9784211281771267, \
          0.2520795366985681, \
          0.6040696445748173, \
          0.2520795366985681, \
          0.6040696445748173, \
          0.9784211281771267, \
          0.9784211281771267, \
          0.7479204633014319, \
          0.3959303554251827, \
          0.7479204633014319, \
          0.3959303554251827, \
          0.0215788718228733, \
          0.0215788718228733, \
          0.2520795366985681, \
          0.6040696445748173, \
          0.2520795366985681, \
          0.6040696445748173, \
          0.0215788718228733, \
          0.0215788718228733, \
          0.2520795366985681, \
          0.3959303554251827, \
          0.2520795366985681, \
          0.3959303554251827, \
          0.9784211281771267, \
          0.9784211281771267, \
          0.2520795366985681, \
          0.3959303554251827, \
          0.2520795366985681, \
          0.3959303554251827, \
          0.0215788718228733, \
          0.0215788718228733 ] )

  w = np.array ( [ \
          0.0030079175616226, \
          0.0030079175616226, \
          0.0030079175616226, \
          0.0030079175616226, \
          0.0030079175616226, \
          0.0030079175616226, \
          0.0061575518559863, \
          0.0061575518559863, \
          0.0061575518559863, \
          0.0061575518559863, \
          0.0061575518559863, \
          0.0061575518559863, \
          0.0007451864938265, \
          0.0007451864938265, \
          0.0007451864938265, \
          0.0007451864938265, \
          0.0007451864938265, \
          0.0007451864938265, \
          0.0007451864938265, \
          0.0007451864938265, \
          0.0034736498758246, \
          0.0034736498758246, \
          0.0034736498758246, \
          0.0034736498758246, \
          0.0034736498758246, \
          0.0034736498758246, \
          0.0034736498758246, \
          0.0034736498758246, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0005231065457280, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0047212614224319, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0023372223737635, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0038417548985660, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0001507767719634, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0032140794095183, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0022454466226130, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0010413676731518, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0005920000965024, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0004100172337698, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0007465850926621, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0037432896839704, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0004534357504253, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0041828675781781, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0007389797381823, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0013712825533878, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0003675472168789, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0012580194835158, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946, \
          0.0015165655616946 ] )


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
  hexahedron_jaskowiec_rule_test ( )
  timestamp ( )

