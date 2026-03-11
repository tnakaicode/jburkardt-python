#! /usr/bin/env python3
#
def pyramid_witherden_rule_test ( ):

#*****************************************************************************80
#
## pyramid_witherden_rule_test() tests pyramid_witherden_rule().
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    13 July 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'pyramid_witherden_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test pyramid_witherden_rule().' )

  p = 5
  pyramid_witherden_rule_test01 ( p )

  p = 5
  pyramid_witherden_rule_test02 ( p )

  p_lo = 0
  p_hi = 10
  pyramid_witherden_rule_test03 ( p_lo, p_hi )
#
#  Terminate.
#
  print ( '' )
  print ( 'pyramid_witherden_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def pyramid_witherden_rule_test01 ( p ):

#*****************************************************************************80
#
## pyramid_witherden_rule_test01() computes a quadrature rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    26 May 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'pyramid_witherden_rule_test01():' )
  print ( '  Quadrature rule for the unit pyramid,' )
  print ( '  Precision p =', p )
#
#  Retrieve a rule
#
  n, x, y, z, w = pyramid_witherden_rule ( p )
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
#  Verify weights sum to 1.
#
  w_sum = np.sum ( w )

  print ( '' )
  print ( '  Weight Sum', w_sum )

  return

def pyramid_witherden_rule_test02 ( p ):

#*****************************************************************************80
#
## pyramid_witherden_rule_test02() tests a quadrature rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    15 May 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'pyramid_witherden_rule_test02():' )
  print ( '  Test the precision of a quadrature rule for the unit pyramid.' )

  dim_num = 3
#
#  Retrieve the rule.
#
  n, x, y, z, w = pyramid_witherden_rule ( p )
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

      quad = pyramid_unit_volume ( ) * np.dot ( w, v )

      exact = pyramid_unit_monomial_integral ( expon )

      quad_error = np.abs ( quad - exact )

      max_error = max ( max_error, quad_error )

      if ( not more ):
        break

    print ( '  %2d  %24.16g' % ( degree, max_error ) )

  return

def pyramid_witherden_rule_test03 ( p_lo, p_hi ):

#*****************************************************************************80
#
## pyramid_witherden_rule_test03() tests absolute and relative precision.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    13 July 2023
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer p_lo, p_hi: the lowest and highest rules to check.
# 
  import numpy as np

  print ( '' )
  print ( 'pyramid_witherden_rule_test03():' )
  print ( '  Test the precision of quadrature rules for the unit pyramid.' )
  print ( '  Check rules of precision p =', p_lo, 'through', p_hi )
  print ( '  for error in approximating integrals of monomials.' )

  dim_num = 3

  print ( '' )
  print ( '              maximum                   maximum' )
  print ( '   p          absolute                  relative' )
  print ( '              error                     error' )
  print ( '' )

  for p in range ( p_lo, p_hi + 1 ):

    n, x, y, z, w = pyramid_witherden_rule ( p )
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

        quad = pyramid_unit_volume ( ) * np.dot ( w, v )

        exact = pyramid_unit_monomial_integral ( expon )

        quad_error = np.abs ( quad - exact )

        max_abs = max ( max_abs, quad_error )

        if ( exact != 0.0 ):
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

def pyramid_unit_monomial_integral ( expon ):

#*****************************************************************************80
#
## pyramid_unit_monomial_integral(): monomial integral in a unit pyramid.
#
#  Discussion:
#
#    This routine returns the integral of
#
#      product ( 1 <= I <= 3 ) X(I)^EXPON(I)
#
#    over the unit pyramid.
#
#    The unit pyramid is defined as:
#
#    - ( 1 - Z ) <= X <= 1 - Z
#    - ( 1 - Z ) <= Y <= 1 - Z
#              0 <= Z <= 1.
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
#  Reference:
#
#    Arthur Stroud,
#    Approximate Calculation of Multiple Integrals,
#    Prentice Hall, 1971,
#    ISBN: 0130438936,
#    LC: QA311.S85.
#
#  Input:
#
#    integer EXPON(3): the exponents.
#
#  Output:
#
#    real VALUE: the integral of the monomial.
#
  from scipy.special import comb

  if ( ( ( expon[0] % 2 ) == 0 ) and ( ( expon[1] % 2 ) == 0 ) ):

    i_hi = 2 + expon[0] + expon[1]

    value = 0.0
    mop = 1.0
    for i in range ( 0, i_hi + 1 ):
      value = value + mop * comb ( i_hi, i ) / float ( i + expon[2] + 1 )
      mop = - mop

    value = value * 2.0 / float ( expon[0] + 1 ) * 2.0 / float ( expon[1] + 1 )

  else:

    value = 0.0

  return value

def pyramid_witherden_rule ( p ):

#*****************************************************************************80
#
## pyramid_witherden_rule() returns a pyramid quadrature rule of given precision.
#
#  Discussion:
#
#    The unit pyramid with square base is the region
#
#      -1 <= X <= 1
#      -1 <= Y <= 1
#       0 <= Z <= 1.
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
#  Reference:
#
#    Freddie Witherden, Peter Vincent,
#    On the identification of symmetric quadrature rules for finite element methods,
#    Computers and Mathematics with Applications,
#    Volume 69, pages 1232-1241, 2015.
#
#  Input:
#
#    integer p: the precision, 0 <= p <= 10.
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
    raise Exception ( 'pyramid_witherden_rule(): Input p < 0.' )
 
  if ( 10 < p ):
    raise Exception ( 'pyramid_witherden_rule(): Input 10 < p.' )

  n = rule_order ( p )

  if ( p == 0 ):
    x, y, z, w = rule00 ( )
  elif ( p == 1 ):
    x, y, z, w = rule01 ( )
  elif ( p == 2 ):
    x, y, z, w = rule02 ( )
  elif ( p == 3 ):
    x, y, z, w = rule03 ( )
  elif ( p == 4 ):
    x, y, z, w = rule04 ( )
  elif ( p == 5 ):
    x, y, z, w = rule05 ( )
  elif ( p == 6 ):
    x, y, z, w = rule06 ( )
  elif ( p == 7 ):
    x, y, z, w = rule07 ( )
  elif ( p == 8 ):
    x, y, z, w = rule08 ( )
  elif ( p == 9 ):
    x, y, z, w = rule09 ( )
  elif ( p == 10 ):
    x, y, z, w = rule10 ( )

  return n, x, y, z, w

def pyramid_unit_volume ( ):

#*****************************************************************************80
#
## pyramid_unit_volume() returns the volume of a unit pyramid.
#
#  Discussion:
#
#    A pyramid with square base can be regarded as the upper half of a
#    3D octahedron.
#
#    The integration region:
#
#      - ( 1 - Z ) <= X <= 1 - Z
#      - ( 1 - Z ) <= Y <= 1 - Z
#                0 <= Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    31 March 2008
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real VALUE, the volume of the pyramid.
#
  value = 4.0 / 3.0

  return value

def pyramid_volume ( r, h ):

#*****************************************************************************80
#
## pyramid_volume() returns the volume of a pyramid with square base in 3D.
#
#  Discussion:
#
#    A pyramid with square base can be regarded as the upper half of a
#    3D octahedron.
#
#    Z - R <= X <= R - Z
#    Z - R <= Y <= R - Z
#    0 <= Z <= H.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real R, the "radius" of the pyramid, that is, half the
#    length of one of the sides of the square base.
#
#    real H, the height of the pyramid.
#
#  Output:
#
#    real VALUE, the volume of the pyramid.
#
  value = ( 4.0 / 3.0 ) * h * r * r

  return value

def rule_order ( p ):

#*****************************************************************************80
#
## rule_order() returns the order of a pyramid quadrature rule of given precision.
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
#    26 April 2023
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
#    integer p: the precision, 0 <= p <= 10.
#
#  Output:
#
#    integer order: the order of the rule.
#
  import numpy as np

  if ( p < 0 ):
    raise Exception ( 'rule_order(): Input p < 0.' )

  if ( 10 < p ):
    raise Exception ( 'rule_order(): Input 10 < p.' )

  order_vec = np.array ( [ \
      1, \
      1,   5,   6,  10,  15, \
     24,  31,  47,  62,  83 ] )

  order = order_vec[p]

  return order

def rule00 ( ):

#*****************************************************************************80
#
## rule00() returns the pyramid quadrature rule of precision 0.
#
#  Discussion:
#
#    We suppose we are given a pyramid P with vertices
#      (-1,-1,0), (-1,+1,0), (+1,+1,0), (+1,-1,0), (0,0,1).
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over
#    P is approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2023
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
          0.0000000000000000 ] )

  y = np.array ( [ \
          0.0000000000000000 ] )

  z = np.array ( [ \
          0.2500000000000000 ] )

  w = np.array ( [ \
          1.0000000000000000 ] )

  return x, y, z, w

def rule01 ( ):

#*****************************************************************************80
#
## rule01() returns the pyramid quadrature rule of precision 1.
#
#  Discussion:
#
#    We suppose we are given a pyramid P with vertices
#      (-1,-1,0), (-1,+1,0), (+1,+1,0), (+1,-1,0), (0,0,1).
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over
#    P is approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2023
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
          0.0000000000000000 ] )

  y = np.array ( [ \
          0.0000000000000000 ] )

  z = np.array ( [ \
          0.2500000000000000 ] )

  w = np.array ( [ \
          1.0000000000000000 ] )

  return x, y, z, w

def rule02 ( ):

#*****************************************************************************80
#
## rule02() returns the pyramid quadrature rule of precision 2.
#
#  Discussion:
#
#    We suppose we are given a pyramid P with vertices
#      (-1,-1,0), (-1,+1,0), (+1,+1,0), (+1,-1,0), (0,0,1).
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over
#    P is approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2023
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
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.0000000000000000, \
          0.7189210558117962, \
          0.0000000000000000, \
         -0.7189210558117962, \
          0.0000000000000000 ] )

  y = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.7189210558117962, \
          0.0000000000000000, \
         -0.7189210558117962 ] )

  z = np.array ( [ \
          0.6082910385597788, \
          0.1453364835728557, \
          0.1453364835728557, \
          0.1453364835728557, \
          0.1453364835728557 ] )

  w = np.array ( [ \
          0.2260773013241023, \
          0.1934806746689745, \
          0.1934806746689745, \
          0.1934806746689745, \
          0.1934806746689745 ] )

  return x, y, z, w

def rule03 ( ):

#*****************************************************************************80
#
## rule03() returns the pyramid quadrature rule of precision 3.
#
#  Discussion:
#
#    We suppose we are given a pyramid P with vertices
#      (-1,-1,0), (-1,+1,0), (+1,+1,0), (+1,-1,0), (0,0,1).
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over
#    P is approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2023
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
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.5610836110587396, \
          0.5610836110587396, \
         -0.5610836110587396, \
         -0.5610836110587396 ] )

  y = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.5610836110587396, \
         -0.5610836110587396, \
          0.5610836110587396, \
         -0.5610836110587396 ] )

  z = np.array ( [ \
          0.5714285703860683, \
          0.0000000056758500, \
          0.1666666666666667, \
          0.1666666666666667, \
          0.1666666666666667, \
          0.1666666666666667 ] )

  w = np.array ( [ \
          0.2522058839227606, \
          0.1125000060660650, \
          0.1588235275027936, \
          0.1588235275027936, \
          0.1588235275027936, \
          0.1588235275027936 ] )

  return x, y, z, w

def rule04 ( ):

#*****************************************************************************80
#
## rule04() returns the pyramid quadrature rule of precision 4.
#
#  Discussion:
#
#    We suppose we are given a pyramid P with vertices
#      (-1,-1,0), (-1,+1,0), (+1,+1,0), (+1,-1,0), (0,0,1).
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over
#    P is approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2023
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
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.6505815563982326, \
          0.0000000000000000, \
         -0.6505815563982326, \
          0.0000000000000000, \
          0.6579669971216900, \
          0.6579669971216900, \
         -0.6579669971216900, \
         -0.6579669971216900 ] )

  y = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.6505815563982326, \
          0.0000000000000000, \
         -0.6505815563982326, \
          0.6579669971216900, \
         -0.6579669971216900, \
          0.6579669971216900, \
         -0.6579669971216900 ] )

  z = np.array ( [ \
          0.6772327888861374, \
          0.1251369531087465, \
          0.3223841495782137, \
          0.3223841495782137, \
          0.3223841495782137, \
          0.3223841495782137, \
          0.0392482838988154, \
          0.0392482838988154, \
          0.0392482838988154, \
          0.0392482838988154 ] )

  w = np.array ( [ \
          0.1137418831706419, \
          0.2068834025895523, \
          0.1063245878893255, \
          0.1063245878893255, \
          0.1063245878893255, \
          0.1063245878893255, \
          0.0635190906706259, \
          0.0635190906706259, \
          0.0635190906706259, \
          0.0635190906706259 ] )

  return x, y, z, w

def rule05 ( ):

#*****************************************************************************80
#
## rule05() returns the pyramid quadrature rule of precision 5.
#
#  Discussion:
#
#    We suppose we are given a pyramid P with vertices
#      (-1,-1,0), (-1,+1,0), (+1,+1,0), (+1,-1,0), (0,0,1).
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over
#    P is approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2023
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
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.7065260315463245, \
          0.0000000000000000, \
         -0.7065260315463245, \
          0.0000000000000000, \
          0.7051171227788277, \
          0.7051171227788277, \
         -0.7051171227788277, \
         -0.7051171227788277, \
          0.4328828641035410, \
          0.4328828641035410, \
         -0.4328828641035410, \
         -0.4328828641035410 ] )

  y = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.7065260315463245, \
          0.0000000000000000, \
         -0.7065260315463245, \
          0.7051171227788277, \
         -0.7051171227788277, \
          0.7051171227788277, \
         -0.7051171227788277, \
          0.4328828641035410, \
         -0.4328828641035410, \
          0.4328828641035410, \
         -0.4328828641035410 ] )

  z = np.array ( [ \
          0.7298578807825067, \
          0.3004010208137690, \
          0.0000000064917722, \
          0.1250000000000000, \
          0.1250000000000000, \
          0.1250000000000000, \
          0.1250000000000000, \
          0.0611119070620230, \
          0.0611119070620230, \
          0.0611119070620230, \
          0.0611119070620230, \
          0.4236013371197248, \
          0.4236013371197248, \
          0.4236013371197248, \
          0.4236013371197248 ] )

  w = np.array ( [ \
          0.0684353699091401, \
          0.1693971144927240, \
          0.0587045358285745, \
          0.0764412931481202, \
          0.0764412931481202, \
          0.0764412931481202, \
          0.0764412931481202, \
          0.0396709015796455, \
          0.0396709015796455, \
          0.0396709015796455, \
          0.0396709015796455, \
          0.0597535502146247, \
          0.0597535502146247, \
          0.0597535502146247, \
          0.0597535502146247 ] )

  return x, y, z, w

def rule06 ( ):

#*****************************************************************************80
#
## rule06() returns the pyramid quadrature rule of precision 6.
#
#  Discussion:
#
#    We suppose we are given a pyramid P with vertices
#      (-1,-1,0), (-1,+1,0), (+1,+1,0), (+1,-1,0), (0,0,1).
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over
#    P is approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2023
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
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.8345953511147084, \
          0.0000000000000000, \
         -0.8345953511147084, \
          0.0000000000000000, \
          0.4339254093766991, \
          0.0000000000000000, \
         -0.4339254093766991, \
          0.0000000000000000, \
          0.5656808544256755, \
          0.5656808544256755, \
         -0.5656808544256755, \
         -0.5656808544256755, \
          0.4980790917807059, \
          0.4980790917807059, \
         -0.4980790917807059, \
         -0.4980790917807059, \
          0.9508994872144825, \
          0.9508994872144825, \
         -0.9508994872144825, \
         -0.9508994872144825 ] )

  y = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.8345953511147084, \
          0.0000000000000000, \
         -0.8345953511147084, \
          0.0000000000000000, \
          0.4339254093766991, \
          0.0000000000000000, \
         -0.4339254093766991, \
          0.5656808544256755, \
         -0.5656808544256755, \
          0.5656808544256755, \
         -0.5656808544256755, \
          0.4980790917807059, \
         -0.4980790917807059, \
          0.4980790917807059, \
         -0.4980790917807059, \
          0.9508994872144825, \
         -0.9508994872144825, \
          0.9508994872144825, \
         -0.9508994872144825 ] )

  z = np.array ( [ \
          0.8076457976939595, \
          0.0017638088528196, \
          0.1382628064637306, \
          0.4214239119356371, \
          0.0974473410254620, \
          0.0974473410254620, \
          0.0974473410254620, \
          0.0974473410254620, \
          0.5660745906233009, \
          0.5660745906233009, \
          0.5660745906233009, \
          0.5660745906233009, \
          0.0294777308457207, \
          0.0294777308457207, \
          0.0294777308457207, \
          0.0294777308457207, \
          0.2649158632121295, \
          0.2649158632121295, \
          0.2649158632121295, \
          0.2649158632121295, \
          0.0482490706319360, \
          0.0482490706319360, \
          0.0482490706319360, \
          0.0482490706319360 ] )

  w = np.array ( [ \
          0.0254628936626420, \
          0.0160535131751913, \
          0.1195795544525238, \
          0.1030606701991518, \
          0.0369505879363295, \
          0.0369505879363295, \
          0.0369505879363295, \
          0.0369505879363295, \
          0.0315875794881733, \
          0.0315875794881733, \
          0.0315875794881733, \
          0.0315875794881733, \
          0.0372001293894483, \
          0.0372001293894483, \
          0.0372001293894483, \
          0.0372001293894483, \
          0.0738823846769269, \
          0.0738823846769269, \
          0.0738823846769269, \
          0.0738823846769269, \
          0.0043401606367449, \
          0.0043401606367449, \
          0.0043401606367449, \
          0.0043401606367449 ] )

  return x, y, z, w

def rule07 ( ):

#*****************************************************************************80
#
## rule07() returns the pyramid quadrature rule of precision 7.
#
#  Discussion:
#
#    We suppose we are given a pyramid P with vertices
#      (-1,-1,0), (-1,+1,0), (+1,+1,0), (+1,-1,0), (0,0,1).
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over
#    P is approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2023
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
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.8640987597877147, \
          0.0000000000000000, \
         -0.8640987597877147, \
          0.0000000000000000, \
          0.6172133998483676, \
          0.0000000000000000, \
         -0.6172133998483676, \
          0.0000000000000000, \
          0.3541523808681161, \
          0.3541523808681161, \
         -0.3541523808681161, \
         -0.3541523808681161, \
          0.8027258501000878, \
          0.8027258501000878, \
         -0.8027258501000878, \
         -0.8027258501000878, \
          0.2541353468618572, \
          0.2541353468618572, \
         -0.2541353468618572, \
         -0.2541353468618572, \
          0.6143051077207853, \
          0.6143051077207853, \
         -0.6143051077207853, \
         -0.6143051077207853, \
          0.5248326982543755, \
          0.5248326982543755, \
         -0.5248326982543755, \
         -0.5248326982543755 ] )

  y = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.8640987597877147, \
          0.0000000000000000, \
         -0.8640987597877147, \
          0.0000000000000000, \
          0.6172133998483676, \
          0.0000000000000000, \
         -0.6172133998483676, \
          0.3541523808681161, \
         -0.3541523808681161, \
          0.3541523808681161, \
         -0.3541523808681161, \
          0.8027258501000878, \
         -0.8027258501000878, \
          0.8027258501000878, \
         -0.8027258501000878, \
          0.2541353468618572, \
         -0.2541353468618572, \
          0.2541353468618572, \
         -0.2541353468618572, \
          0.6143051077207853, \
         -0.6143051077207853, \
          0.6143051077207853, \
         -0.6143051077207853, \
          0.5248326982543755, \
         -0.5248326982543755, \
          0.5248326982543755, \
         -0.5248326982543755 ] )

  z = np.array ( [ \
          0.0000454802082028, \
          0.3935828767576542, \
          0.8386827828168515, \
          0.0666666666666667, \
          0.0666666666666667, \
          0.0666666666666667, \
          0.0666666666666667, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.1292864095395495, \
          0.1292864095395495, \
          0.1292864095395495, \
          0.1292864095395495, \
          0.0801385301797781, \
          0.0801385301797781, \
          0.0801385301797781, \
          0.0801385301797781, \
          0.6055199301105999, \
          0.6055199301105999, \
          0.6055199301105999, \
          0.6055199301105999, \
          0.0000000000897583, \
          0.0000000000897583, \
          0.0000000000897583, \
          0.0000000000897583, \
          0.2905430754945976, \
          0.2905430754945976, \
          0.2905430754945976, \
          0.2905430754945976 ] )

  w = np.array ( [ \
          0.0250005770341970, \
          0.1005301826998931, \
          0.0157071744270173, \
          0.0266917592930029, \
          0.0266917592930029, \
          0.0266917592930029, \
          0.0266917592930029, \
          0.0287109375000000, \
          0.0287109375000000, \
          0.0287109375000000, \
          0.0287109375000000, \
          0.0659601871499773, \
          0.0659601871499773, \
          0.0659601871499773, \
          0.0659601871499773, \
          0.0147861379562357, \
          0.0147861379562357, \
          0.0147861379562357, \
          0.0147861379562357, \
          0.0295191096942239, \
          0.0295191096942239, \
          0.0295191096942239, \
          0.0295191096942239, \
          0.0133038449696241, \
          0.0133038449696241, \
          0.0133038449696241, \
          0.0133038449696241, \
          0.0357185398966593, \
          0.0357185398966593, \
          0.0357185398966593, \
          0.0357185398966593 ] )

  return x, y, z, w

def rule08 ( ):

#*****************************************************************************80
#
## rule08() returns the pyramid quadrature rule of precision 8.
#
#  Discussion:
#
#    We suppose we are given a pyramid P with vertices
#      (-1,-1,0), (-1,+1,0), (+1,+1,0), (+1,-1,0), (0,0,1).
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over
#    P is approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2023
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
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.7960960887742582, \
          0.0000000000000000, \
         -0.7960960887742582, \
          0.0000000000000000, \
          0.5648889587418399, \
          0.0000000000000000, \
         -0.5648889587418399, \
          0.0000000000000000, \
          0.7530226935489476, \
          0.0000000000000000, \
         -0.7530226935489476, \
          0.0000000000000000, \
          0.2465779424622870, \
          0.2465779424622870, \
         -0.2465779424622870, \
         -0.2465779424622870, \
          0.7338895325467361, \
          0.7338895325467361, \
         -0.7338895325467361, \
         -0.7338895325467361, \
          0.0000826826715128, \
          0.0000826826715128, \
         -0.0000826826715128, \
         -0.0000826826715128, \
          0.3989965570952277, \
          0.3989965570952277, \
         -0.3989965570952277, \
         -0.3989965570952277, \
          0.3653124144795900, \
          0.3653124144795900, \
         -0.3653124144795900, \
         -0.3653124144795900, \
          0.4834252440408382, \
          0.4834252440408382, \
         -0.4834252440408382, \
         -0.4834252440408382, \
          0.6314047976005609, \
          0.8948561964915306, \
          0.6314047976005609, \
         -0.8948561964915306, \
         -0.6314047976005609, \
          0.8948561964915306, \
         -0.6314047976005609, \
         -0.8948561964915306 ] )

  y = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.7960960887742582, \
          0.0000000000000000, \
         -0.7960960887742582, \
          0.0000000000000000, \
          0.5648889587418399, \
          0.0000000000000000, \
         -0.5648889587418399, \
          0.0000000000000000, \
          0.7530226935489476, \
          0.0000000000000000, \
         -0.7530226935489476, \
          0.2465779424622870, \
         -0.2465779424622870, \
          0.2465779424622870, \
         -0.2465779424622870, \
          0.7338895325467361, \
         -0.7338895325467361, \
          0.7338895325467361, \
         -0.7338895325467361, \
          0.0000826826715128, \
         -0.0000826826715128, \
          0.0000826826715128, \
         -0.0000826826715128, \
          0.3989965570952277, \
         -0.3989965570952277, \
          0.3989965570952277, \
         -0.3989965570952277, \
          0.3653124144795900, \
         -0.3653124144795900, \
          0.3653124144795900, \
         -0.3653124144795900, \
          0.4834252440408382, \
         -0.4834252440408382, \
          0.4834252440408382, \
         -0.4834252440408382, \
          0.8948561964915306, \
          0.6314047976005609, \
         -0.8948561964915306, \
          0.6314047976005609, \
          0.8948561964915306, \
         -0.6314047976005609, \
         -0.8948561964915306, \
         -0.6314047976005609 ] )

  z = np.array ( [ \
          0.5848054341081260, \
          0.2714503954191895, \
          0.0714404302154540, \
          0.0000000073236390, \
          0.0000000073236390, \
          0.0000000073236390, \
          0.0000000073236390, \
          0.4221837006010586, \
          0.4221837006010586, \
          0.4221837006010586, \
          0.4221837006010586, \
          0.1477639972965497, \
          0.1477639972965497, \
          0.1477639972965497, \
          0.1477639972965497, \
          0.6734528479254847, \
          0.6734528479254847, \
          0.6734528479254847, \
          0.6734528479254847, \
          0.2455708050362506, \
          0.2455708050362506, \
          0.2455708050362506, \
          0.2455708050362506, \
          0.8582503626505816, \
          0.8582503626505816, \
          0.8582503626505816, \
          0.8582503626505816, \
          0.0474032316194875, \
          0.0474032316194875, \
          0.0474032316194875, \
          0.0474032316194875, \
          0.4021857062205061, \
          0.4021857062205061, \
          0.4021857062205061, \
          0.4021857062205061, \
          0.1903148210864091, \
          0.1903148210864091, \
          0.1903148210864091, \
          0.1903148210864091, \
          0.0454758042237511, \
          0.0454758042237511, \
          0.0454758042237511, \
          0.0454758042237511, \
          0.0454758042237511, \
          0.0454758042237511, \
          0.0454758042237511, \
          0.0454758042237511 ] )

  w = np.array ( [ \
          0.0494409951557794, \
          0.0873546894411460, \
          0.0384605774968570, \
          0.0093760594001275, \
          0.0093760594001275, \
          0.0093760594001275, \
          0.0093760594001275, \
          0.0163110192164366, \
          0.0163110192164366, \
          0.0163110192164366, \
          0.0163110192164366, \
          0.0322397220710709, \
          0.0322397220710709, \
          0.0322397220710709, \
          0.0322397220710709, \
          0.0126350996218853, \
          0.0126350996218853, \
          0.0126350996218853, \
          0.0126350996218853, \
          0.0062155450261151, \
          0.0062155450261151, \
          0.0062155450261151, \
          0.0062155450261151, \
          0.0026132528336493, \
          0.0026132528336493, \
          0.0026132528336493, \
          0.0026132528336493, \
          0.0293249681950410, \
          0.0293249681950410, \
          0.0293249681950410, \
          0.0293249681950410, \
          0.0363593842641747, \
          0.0363593842641747, \
          0.0363593842641747, \
          0.0363593842641747, \
          0.0409820609459212, \
          0.0409820609459212, \
          0.0409820609459212, \
          0.0409820609459212, \
          0.0100644114510665, \
          0.0100644114510665, \
          0.0100644114510665, \
          0.0100644114510665, \
          0.0100644114510665, \
          0.0100644114510665, \
          0.0100644114510665, \
          0.0100644114510665 ] )

  return x, y, z, w

def rule09 ( ):

#*****************************************************************************80
#
## rule09() returns the pyramid quadrature rule of precision 9.
#
#  Discussion:
#
#    We suppose we are given a pyramid P with vertices
#      (-1,-1,0), (-1,+1,0), (+1,+1,0), (+1,-1,0), (0,0,1).
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over
#    P is approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2023
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
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.9258200958608426, \
          0.0000000000000000, \
         -0.9258200958608426, \
          0.0000000000000000, \
          0.6760969921163639, \
          0.0000000000000000, \
         -0.6760969921163639, \
          0.0000000000000000, \
          0.6163321778509252, \
          0.0000000000000000, \
         -0.6163321778509252, \
          0.0000000000000000, \
          0.4319711692851803, \
          0.0000000000000000, \
         -0.4319711692851803, \
          0.0000000000000000, \
          0.2418018136307699, \
          0.2418018136307699, \
         -0.2418018136307699, \
         -0.2418018136307699, \
          0.8440791629031899, \
          0.8440791629031899, \
         -0.8440791629031899, \
         -0.8440791629031899, \
          0.2279669387608253, \
          0.2279669387608253, \
         -0.2279669387608253, \
         -0.2279669387608253, \
          0.5027849771350101, \
          0.5027849771350101, \
         -0.5027849771350101, \
         -0.5027849771350101, \
          0.2605010749834311, \
          0.2605010749834311, \
         -0.2605010749834311, \
         -0.2605010749834311, \
          0.0926958730867243, \
          0.0926958730867243, \
         -0.0926958730867243, \
         -0.0926958730867243, \
          0.4832161680706445, \
          0.4832161680706445, \
         -0.4832161680706445, \
         -0.4832161680706445, \
          0.5671855056082324, \
          0.5671855056082324, \
         -0.5671855056082324, \
         -0.5671855056082324, \
          0.8463949915138761, \
          0.8463949915138761, \
         -0.8463949915138761, \
         -0.8463949915138761, \
          0.8471778681177453, \
          0.4641907129661463, \
          0.8471778681177453, \
         -0.4641907129661463, \
         -0.8471778681177453, \
          0.4641907129661463, \
         -0.8471778681177453, \
         -0.4641907129661463 ] )

  y = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.9258200958608426, \
          0.0000000000000000, \
         -0.9258200958608426, \
          0.0000000000000000, \
          0.6760969921163639, \
          0.0000000000000000, \
         -0.6760969921163639, \
          0.0000000000000000, \
          0.6163321778509252, \
          0.0000000000000000, \
         -0.6163321778509252, \
          0.0000000000000000, \
          0.4319711692851803, \
          0.0000000000000000, \
         -0.4319711692851803, \
          0.2418018136307699, \
         -0.2418018136307699, \
          0.2418018136307699, \
         -0.2418018136307699, \
          0.8440791629031899, \
         -0.8440791629031899, \
          0.8440791629031899, \
         -0.8440791629031899, \
          0.2279669387608253, \
         -0.2279669387608253, \
          0.2279669387608253, \
         -0.2279669387608253, \
          0.5027849771350101, \
         -0.5027849771350101, \
          0.5027849771350101, \
         -0.5027849771350101, \
          0.2605010749834311, \
         -0.2605010749834311, \
          0.2605010749834311, \
         -0.2605010749834311, \
          0.0926958730867243, \
         -0.0926958730867243, \
          0.0926958730867243, \
         -0.0926958730867243, \
          0.4832161680706445, \
         -0.4832161680706445, \
          0.4832161680706445, \
         -0.4832161680706445, \
          0.5671855056082324, \
         -0.5671855056082324, \
          0.5671855056082324, \
         -0.5671855056082324, \
          0.8463949915138761, \
         -0.8463949915138761, \
          0.8463949915138761, \
         -0.8463949915138761, \
          0.4641907129661463, \
          0.8471778681177453, \
         -0.4641907129661463, \
          0.8471778681177453, \
          0.4641907129661463, \
         -0.8471778681177453, \
         -0.4641907129661463, \
         -0.8471778681177453 ] )

  z = np.array ( [ \
          0.0371459309315055, \
          0.6942002631703261, \
          0.0000000042251285, \
          0.0000000042251285, \
          0.0000000042251285, \
          0.0000000042251285, \
          0.2697317845200571, \
          0.2697317845200571, \
          0.2697317845200571, \
          0.2697317845200571, \
          0.0833333333333333, \
          0.0833333333333333, \
          0.0833333333333333, \
          0.0833333333333333, \
          0.5334178104457834, \
          0.5334178104457834, \
          0.5334178104457834, \
          0.5334178104457834, \
          0.6619880087153507, \
          0.6619880087153507, \
          0.6619880087153507, \
          0.6619880087153507, \
          0.1522047098054636, \
          0.1522047098054636, \
          0.1522047098054636, \
          0.1522047098054636, \
          0.4222655365894455, \
          0.4222655365894455, \
          0.4222655365894455, \
          0.4222655365894455, \
          0.3967643698988902, \
          0.3967643698988902, \
          0.3967643698988902, \
          0.3967643698988902, \
          0.2008207219371707, \
          0.2008207219371707, \
          0.2008207219371707, \
          0.2008207219371707, \
          0.8661453707796378, \
          0.8661453707796378, \
          0.8661453707796378, \
          0.8661453707796378, \
          0.0195040124924115, \
          0.0195040124924115, \
          0.0195040124924115, \
          0.0195040124924115, \
          0.2131686017065601, \
          0.2131686017065601, \
          0.2131686017065601, \
          0.2131686017065601, \
          0.0153477972480097, \
          0.0153477972480097, \
          0.0153477972480097, \
          0.0153477972480097, \
          0.0833333333333333, \
          0.0833333333333333, \
          0.0833333333333333, \
          0.0833333333333333, \
          0.0833333333333333, \
          0.0833333333333333, \
          0.0833333333333333, \
          0.0833333333333333 ] )

  w = np.array ( [ \
          0.0320478691353425, \
          0.0237932209450781, \
          0.0041733723029944, \
          0.0041733723029944, \
          0.0041733723029944, \
          0.0041733723029944, \
          0.0222937913596180, \
          0.0222937913596180, \
          0.0222937913596180, \
          0.0222937913596180, \
          0.0291280227779532, \
          0.0291280227779532, \
          0.0291280227779532, \
          0.0291280227779532, \
          0.0115418065483010, \
          0.0115418065483010, \
          0.0115418065483010, \
          0.0115418065483010, \
          0.0101005748273597, \
          0.0101005748273597, \
          0.0101005748273597, \
          0.0101005748273597, \
          0.0020589782014206, \
          0.0020589782014206, \
          0.0020589782014206, \
          0.0020589782014206, \
          0.0342456887657178, \
          0.0342456887657178, \
          0.0342456887657178, \
          0.0342456887657178, \
          0.0129094136418972, \
          0.0129094136418972, \
          0.0129094136418972, \
          0.0129094136418972, \
          0.0371122811478335, \
          0.0371122811478335, \
          0.0371122811478335, \
          0.0371122811478335, \
          0.0022186981787511, \
          0.0022186981787511, \
          0.0022186981787511, \
          0.0022186981787511, \
          0.0159562091361951, \
          0.0159562091361951, \
          0.0159562091361951, \
          0.0159562091361951, \
          0.0230673181273276, \
          0.0230673181273276, \
          0.0230673181273276, \
          0.0230673181273276, \
          0.0045994005726981, \
          0.0045994005726981, \
          0.0045994005726981, \
          0.0045994005726981, \
          0.0133170859459138, \
          0.0133170859459138, \
          0.0133170859459138, \
          0.0133170859459138, \
          0.0133170859459138, \
          0.0133170859459138, \
          0.0133170859459138, \
          0.0133170859459138 ] )

  return x, y, z, w

def rule10 ( ):

#*****************************************************************************80
#
## rule10() returns the pyramid quadrature rule of precision 10.
#
#  Discussion:
#
#    We suppose we are given a pyramid P with vertices
#      (-1,-1,0), (-1,+1,0), (+1,+1,0), (+1,-1,0), (0,0,1).
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over
#    P is approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 April 2023
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
#    x(n), y(n), z(n): the coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.9211301560146403, \
          0.0000000000000000, \
         -0.9211301560146403, \
          0.0000000000000000, \
          0.4546948844252537, \
          0.0000000000000000, \
         -0.4546948844252537, \
          0.0000000000000000, \
          0.3495469844967067, \
          0.0000000000000000, \
         -0.3495469844967067, \
          0.0000000000000000, \
          0.4036909359989291, \
          0.4036909359989291, \
         -0.4036909359989291, \
         -0.4036909359989291, \
          0.3714608909064742, \
          0.3714608909064742, \
         -0.3714608909064742, \
         -0.3714608909064742, \
          0.2995979966434122, \
          0.2995979966434122, \
         -0.2995979966434122, \
         -0.2995979966434122, \
          0.1582262545541785, \
          0.1582262545541785, \
         -0.1582262545541785, \
         -0.1582262545541785, \
          0.1819979349519966, \
          0.1819979349519966, \
         -0.1819979349519966, \
         -0.1819979349519966, \
          0.8455841498012413, \
          0.8455841498012413, \
         -0.8455841498012413, \
         -0.8455841498012413, \
          0.6468694059373429, \
          0.6468694059373429, \
         -0.6468694059373429, \
         -0.6468694059373429, \
          0.5875870294087208, \
          0.5875870294087208, \
         -0.5875870294087208, \
         -0.5875870294087208, \
          0.2237620599838161, \
          0.2237620599838161, \
         -0.2237620599838161, \
         -0.2237620599838161, \
          0.7455657084697210, \
          0.2247174318849062, \
          0.7455657084697210, \
         -0.2247174318849062, \
         -0.7455657084697210, \
          0.2247174318849062, \
         -0.7455657084697210, \
         -0.2247174318849062, \
          0.4056619527318771, \
          0.7487267628018788, \
          0.4056619527318771, \
         -0.7487267628018788, \
         -0.4056619527318771, \
          0.7487267628018788, \
         -0.4056619527318771, \
         -0.7487267628018788, \
          0.0707425682812096, \
          0.6004569111268736, \
          0.0707425682812096, \
         -0.6004569111268736, \
         -0.0707425682812096, \
          0.6004569111268736, \
         -0.0707425682812096, \
         -0.6004569111268736, \
          0.9422191470796681, \
          0.6375631040785387, \
          0.9422191470796681, \
         -0.6375631040785387, \
         -0.9422191470796681, \
          0.6375631040785387, \
         -0.9422191470796681, \
         -0.6375631040785387 ] )

  y = np.array ( [ \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.0000000000000000, \
          0.9211301560146403, \
          0.0000000000000000, \
         -0.9211301560146403, \
          0.0000000000000000, \
          0.4546948844252537, \
          0.0000000000000000, \
         -0.4546948844252537, \
          0.0000000000000000, \
          0.3495469844967067, \
          0.0000000000000000, \
         -0.3495469844967067, \
          0.4036909359989291, \
         -0.4036909359989291, \
          0.4036909359989291, \
         -0.4036909359989291, \
          0.3714608909064742, \
         -0.3714608909064742, \
          0.3714608909064742, \
         -0.3714608909064742, \
          0.2995979966434122, \
         -0.2995979966434122, \
          0.2995979966434122, \
         -0.2995979966434122, \
          0.1582262545541785, \
         -0.1582262545541785, \
          0.1582262545541785, \
         -0.1582262545541785, \
          0.1819979349519966, \
         -0.1819979349519966, \
          0.1819979349519966, \
         -0.1819979349519966, \
          0.8455841498012413, \
         -0.8455841498012413, \
          0.8455841498012413, \
         -0.8455841498012413, \
          0.6468694059373429, \
         -0.6468694059373429, \
          0.6468694059373429, \
         -0.6468694059373429, \
          0.5875870294087208, \
         -0.5875870294087208, \
          0.5875870294087208, \
         -0.5875870294087208, \
          0.2237620599838161, \
         -0.2237620599838161, \
          0.2237620599838161, \
         -0.2237620599838161, \
          0.2247174318849062, \
          0.7455657084697210, \
         -0.2247174318849062, \
          0.7455657084697210, \
          0.2247174318849062, \
         -0.7455657084697210, \
         -0.2247174318849062, \
         -0.7455657084697210, \
          0.7487267628018788, \
          0.4056619527318771, \
         -0.7487267628018788, \
          0.4056619527318771, \
          0.7487267628018788, \
         -0.4056619527318771, \
         -0.7487267628018788, \
         -0.4056619527318771, \
          0.6004569111268736, \
          0.0707425682812096, \
         -0.6004569111268736, \
          0.0707425682812096, \
          0.6004569111268736, \
         -0.0707425682812096, \
         -0.6004569111268736, \
         -0.0707425682812096, \
          0.6375631040785387, \
          0.9422191470796681, \
         -0.6375631040785387, \
          0.9422191470796681, \
          0.6375631040785387, \
         -0.9422191470796681, \
         -0.6375631040785387, \
         -0.9422191470796681 ] )

  z = np.array ( [ \
          0.9167957817791272, \
          0.3511368063403526, \
          0.7419135679633000, \
          0.0631615972799145, \
          0.0631615972799145, \
          0.0631615972799145, \
          0.0631615972799145, \
          0.1767304111617324, \
          0.1767304111617324, \
          0.1767304111617324, \
          0.1767304111617324, \
          0.6020938107079140, \
          0.6020938107079140, \
          0.6020938107079140, \
          0.6020938107079140, \
          0.5270494697681531, \
          0.5270494697681531, \
          0.5270494697681531, \
          0.5270494697681531, \
          0.3491104418985491, \
          0.3491104418985491, \
          0.3491104418985491, \
          0.3491104418985491, \
          0.0069339728754634, \
          0.0069339728754634, \
          0.0069339728754634, \
          0.0069339728754634, \
          0.7752643179331966, \
          0.7752643179331966, \
          0.7752643179331966, \
          0.7752643179331966, \
          0.5470650181463391, \
          0.5470650181463391, \
          0.5470650181463391, \
          0.5470650181463391, \
          0.0728984114756605, \
          0.0728984114756605, \
          0.0728984114756605, \
          0.0728984114756605, \
          0.2836223397977548, \
          0.2836223397977548, \
          0.2836223397977548, \
          0.2836223397977548, \
          0.0598130217927265, \
          0.0598130217927265, \
          0.0598130217927265, \
          0.0598130217927265, \
          0.0658308799806233, \
          0.0658308799806233, \
          0.0658308799806233, \
          0.0658308799806233, \
          0.0272502552746740, \
          0.0272502552746740, \
          0.0272502552746740, \
          0.0272502552746740, \
          0.0272502552746740, \
          0.0272502552746740, \
          0.0272502552746740, \
          0.0272502552746740, \
          0.1618000129270508, \
          0.1618000129270508, \
          0.1618000129270508, \
          0.1618000129270508, \
          0.1618000129270508, \
          0.1618000129270508, \
          0.1618000129270508, \
          0.1618000129270508, \
          0.3584705635890507, \
          0.3584705635890507, \
          0.3584705635890507, \
          0.3584705635890507, \
          0.3584705635890507, \
          0.3584705635890507, \
          0.3584705635890507, \
          0.3584705635890507, \
          0.0074406410768847, \
          0.0074406410768847, \
          0.0074406410768847, \
          0.0074406410768847, \
          0.0074406410768847, \
          0.0074406410768847, \
          0.0074406410768847, \
          0.0074406410768847 ] )

  w = np.array ( [ \
          0.0024012267625214, \
          0.0469159279097637, \
          0.0098466607485292, \
          0.0056773923179313, \
          0.0056773923179313, \
          0.0056773923179313, \
          0.0056773923179313, \
          0.0412212597418143, \
          0.0412212597418143, \
          0.0412212597418143, \
          0.0412212597418143, \
          0.0092087532680317, \
          0.0092087532680317, \
          0.0092087532680317, \
          0.0092087532680317, \
          0.0070683961650691, \
          0.0070683961650691, \
          0.0070683961650691, \
          0.0070683961650691, \
          0.0298306858263750, \
          0.0298306858263750, \
          0.0298306858263750, \
          0.0298306858263750, \
          0.0058699928018168, \
          0.0058699928018168, \
          0.0058699928018168, \
          0.0058699928018168, \
          0.0049543654347689, \
          0.0049543654347689, \
          0.0049543654347689, \
          0.0049543654347689, \
          0.0159309372716684, \
          0.0159309372716684, \
          0.0159309372716684, \
          0.0159309372716684, \
          0.0050915274851829, \
          0.0050915274851829, \
          0.0050915274851829, \
          0.0050915274851829, \
          0.0068457933453088, \
          0.0068457933453088, \
          0.0068457933453088, \
          0.0068457933453088, \
          0.0150380203803664, \
          0.0150380203803664, \
          0.0150380203803664, \
          0.0150380203803664, \
          0.0156151631237942, \
          0.0156151631237942, \
          0.0156151631237942, \
          0.0156151631237942, \
          0.0089093600668980, \
          0.0089093600668980, \
          0.0089093600668980, \
          0.0089093600668980, \
          0.0089093600668980, \
          0.0089093600668980, \
          0.0089093600668980, \
          0.0089093600668980, \
          0.0167917214598521, \
          0.0167917214598521, \
          0.0167917214598521, \
          0.0167917214598521, \
          0.0167917214598521, \
          0.0167917214598521, \
          0.0167917214598521, \
          0.0167917214598521, \
          0.0082057491053038, \
          0.0082057491053038, \
          0.0082057491053038, \
          0.0082057491053038, \
          0.0082057491053038, \
          0.0082057491053038, \
          0.0082057491053038, \
          0.0082057491053038, \
          0.0025215488592804, \
          0.0025215488592804, \
          0.0025215488592804, \
          0.0025215488592804, \
          0.0025215488592804, \
          0.0025215488592804, \
          0.0025215488592804, \
          0.0025215488592804 ] )

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
  pyramid_witherden_rule_test ( )
  timestamp ( )



