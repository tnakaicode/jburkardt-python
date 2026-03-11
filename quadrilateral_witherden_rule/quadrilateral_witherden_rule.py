#! /usr/bin/env python3
#
def quadrilateral_witherden_rule_test ( ):

#*****************************************************************************80
#
## quadrilateral_witherden_rule_test() tests quadrilateral_witherden_rule().
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    27 May 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'quadrilateral_witherden_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test quadrilateral_witherden_rule().' )

  p = 5
  quadrilateral_witherden_rule_test01 ( p )

  p = 5
  quadrilateral_witherden_rule_test02 ( p )

  p_lo = 0
  p_hi = 21
  quadrilateral_witherden_rule_test03 ( p_lo, p_hi )
#
#  Terminate.
#
  print ( '' )
  print ( 'quadrilateral_witherden_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def quadrilateral_witherden_rule_test01 ( p ):

#*****************************************************************************80
#
## quadrilateral_witherden_rule_test01() computes a quadrature rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    27 May 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'quadrilateral_witherden_rule_test01():' )
  print ( '  Quadrature rule for the unit quadrilateral,' )
  print ( '  Precision p =', p )
#
#  Retrieve the rule.
#
  n, x, y, w = quadrilateral_witherden_rule ( p )
#
#  Print the rule.
#
  print ( '' )
  print ( '     I      W          X           Y' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %10.6g  %10.6g  %10.6g' \
      % ( i, w[i], x[i], y[i] ) )
#
#  Verify weights sum to 1.
#
  w_sum = np.sum ( w )

  print ( '' )
  print ( '  Weight Sum ', w_sum )

  return

def quadrilateral_witherden_rule_test02 ( p ):

#*****************************************************************************80
#
## quadrilateral_witherden_rule_test02() tests a rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    15 July 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'quadrilateral_witherden_rule_test02():' )
  print ( '  Test the precision of a quadrature rule for the unit quadrilateral.' )

  dim_num = 2
#
#  Retrieve the rule.
#
  n, x, y, w = quadrilateral_witherden_rule ( p )
#
#  Pack the x, y vectors as rows of an array.
#
  xy = np.transpose ( np.array ( [ x, y ] ) )

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

      v = monomial_value ( expon, xy )

      quad = quadrilateral_unit_area ( ) * np.dot ( w, v )

      exact = quadrilateral_unit_monomial_integral ( expon )

      quad_error = np.abs ( quad - exact )

      max_error = max ( max_error, quad_error )

      if ( not more ):
        break

    print ( '  %2d  %24.16g' % ( degree, max_error ) )

  return

def quadrilateral_witherden_rule_test03 ( p_lo, p_hi ):

#*****************************************************************************80
#
## quadrilateral_witherden_rule_test03() tests absolute and relative precision.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    15 July 2023
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
  print ( 'quadrilateral_witherden_rule_test03():' )
  print ( '  Test the precision of quadrature rules for the unit quadrilateral.' )
  print ( '  Check rules of precision p =', p_lo, 'through', p_hi )
  print ( '  for error in approximating integrals of monomials.' )

  dim_num = 2

  print ( '' )
  print ( '              maximum                   maximum' )
  print ( '   p          absolute                  relative' )
  print ( '              error                     error' )
  print ( '' )

  for p in range ( p_lo, p_hi + 1 ):

    n, x, y, w = quadrilateral_witherden_rule ( p )
#
#  Pack the x, y vectors as rows of an array.
#
    xy = np.transpose ( np.array ( [ x, y ] ) )

    max_abs = 0.0
    max_rel = 0.0

    for degree in range ( 0, p + 1 ):

      expon = np.zeros ( dim_num, dtype = int )
      more = False
      h = 0
      t = 0

      while ( True ):

        expon, more, h, t = comp_next ( degree, dim_num, expon, more, h, t )

        v = monomial_value ( expon, xy )

        quad = quadrilateral_unit_area ( ) * np.dot ( w, v )

        exact = quadrilateral_unit_monomial_integral ( expon )

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

def quadrilateral_unit_area ( ):

#*****************************************************************************80
#
## quadrilateral_unit_area() returns the area of a unit quadrilateral.
#
#  Discussion:
#
#    The unit quadrilateral has vertices (0,0), (1,0), (1,1), (0,1).
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
#    real value: the area.
#
  value = 1.0

  return value

def quadrilateral_unit_monomial_integral ( expon ):

#*****************************************************************************80
#
## quadrilateral_unit_monomial_integral(): monomial integral in a unit quadrilateral.
#
#  Discussion:
#
#    This routine returns the integral of
#
#      product ( 1 <= I <= 2 ) X(I)^EXPON(I)
#
#    over the unit quadrilateral.
#
#    The unit quadrilateral is bounded by the vertices
#    (0,0), (1,0), (1,1), (0,1).
# 
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer EXPON(2): the exponents.
#
#  Output:
#
#    real VALUE: the integral of the monomial.
#
  value = 1.0 / ( expon[0] + 1 ) \
        * 1.0 / ( expon[1] + 1 )

  return value

def quadrilateral_witherden_rule ( p ):

#*****************************************************************************80
#
## quadrilateral_witherden_rule() returns a quadrilateral quadrature rule of given precision.
#
#  Discussion:
#
#    The unit quadrilateral is defined as:
#
#    0 <= X <= 1
#    0 <= Y <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2023
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
#    integer p: the precision, 0 <= p <= 21.
#
#  Output:
#
#    integer n: the order of the rule.
#
#    real x(n), y(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  if ( p < 0 ):
    raise Exception ( 'quadrilateral_witherden_rule(): Input p < 0.' )
 
  if ( 21 < p ):
    raise Exception ( 'quadrilateral_witherden_rule(): Input 21 < p.' )

  n = rule_order ( p )

  if ( p <= 1 ):
    x, y, w = rule01 ( )
  elif ( p <= 3 ):
    x, y, w = rule03 ( )
  elif ( p <= 5 ):
    x, y, w = rule05 ( )
  elif ( p <= 7 ):
    x, y, w = rule07 ( )
  elif ( p <= 9 ):
    x, y, w = rule09 ( )
  elif ( p <= 11 ):
    x, y, w = rule11 ( )
  elif ( p <= 13 ):
    x, y, w = rule13 ( )
  elif ( p <= 15 ):
    x, y, w = rule15 ( )
  elif ( p <= 17 ):
    x, y, w = rule17 ( )
  elif ( p <= 19 ):
    x, y, w = rule19 ( )
  elif ( p <= 21 ):
    x, y, w = rule21 ( )

  return n, x, y, w

def rule_order ( p ):

#*****************************************************************************80
#
## rule_order() returns the order of a quadrilateral quadrature rule of given precision.
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
       1,  1,  4,  4,  8,  8, \
      12, 12, 20, 20, 28, 28, \
      37, 37, 48, 48, 60, 60, \
      72, 72, 85, 85 ] )

  order = order_vec[p]

  return order

def rule01 ( ):

#*****************************************************************************80
#
## rule01() returns the quadrilateral rule of precision 1.
#
#  Discussion:
#
#    We suppose we are given a quadrilateral Quad with vertices
#    (0,0), (1,0), (1,1), (0,1),
#    We call a rule with n points, returning coordinates
#    x, y, and weights w.  Then the integral I of f(x,y,z) over Quad is 
#    approximated by Q as follows:
#
#    Q = area(Quad) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i)) 
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
#    real x(n), y(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.5000000000000000 ] )

  y = np.array ( [ \
          0.5000000000000000 ] )

  w = np.array ( [ \
          1.0000000000000000 ] )

  return x, y, w

def rule03 ( ):

#*****************************************************************************80
#
## rule03() returns the quadrilateral rule of precision 3.
#
#  Discussion:
#
#    We suppose we are given a quadrilateral Quad with vertices
#    (0,0), (1,0), (1,1), (0,1),
#    We call a rule with n points, returning coordinates
#    x, y, and weights w.  Then the integral I of f(x,y,z) over Quad is 
#    approximated by Q as follows:
#
#    Q = area(Quad) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i)) 
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
#    real x(n), y(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.7886751345948129, \
          0.7886751345948129, \
          0.2113248654051871, \
          0.2113248654051871 ] )

  y = np.array ( [ \
          0.7886751345948129, \
          0.2113248654051871, \
          0.7886751345948129, \
          0.2113248654051871 ] )

  w = np.array ( [ \
          0.2500000000000000, \
          0.2500000000000000, \
          0.2500000000000000, \
          0.2500000000000000 ] )

  return x, y, w

def rule05 ( ):

#*****************************************************************************80
#
## rule05() returns the quadrilateral rule of precision 5.
#
#  Discussion:
#
#    We suppose we are given a quadrilateral Quad with vertices
#    (0,0), (1,0), (1,1), (0,1),
#    We call a rule with n points, returning coordinates
#    x, y, and weights w.  Then the integral I of f(x,y,z) over Quad is 
#    approximated by Q as follows:
#
#    Q = area(Quad) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i)) 
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
#    real x(n), y(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.8415650255319866, \
          0.5000000000000000, \
          0.1584349744680134, \
          0.5000000000000000, \
          0.9409585518440984, \
          0.9409585518440984, \
          0.0590414481559016, \
          0.0590414481559016 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.8415650255319866, \
          0.5000000000000000, \
          0.1584349744680134, \
          0.9409585518440984, \
          0.0590414481559016, \
          0.9409585518440984, \
          0.0590414481559016 ] )

  w = np.array ( [ \
          0.2040816326530612, \
          0.2040816326530612, \
          0.2040816326530612, \
          0.2040816326530612, \
          0.0459183673469388, \
          0.0459183673469388, \
          0.0459183673469388, \
          0.0459183673469388 ] )

  return x, y, w

def rule07 ( ):

#*****************************************************************************80
#
## rule07() returns the quadrilateral rule of precision 7.
#
#  Discussion:
#
#    We suppose we are given a quadrilateral Quad with vertices
#    (0,0), (1,0), (1,1), (0,1),
#    We call a rule with n points, returning coordinates
#    x, y, and weights w.  Then the integral I of f(x,y,z) over Quad is 
#    approximated by Q as follows:
#
#    Q = area(Quad) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i)) 
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
#    real x(n), y(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.9629100498862757, \
          0.5000000000000000, \
          0.0370899501137243, \
          0.5000000000000000, \
          0.9029898914592993, \
          0.9029898914592993, \
          0.0970101085407006, \
          0.0970101085407006, \
          0.6902772166041579, \
          0.6902772166041579, \
          0.3097227833958421, \
          0.3097227833958421 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.9629100498862757, \
          0.5000000000000000, \
          0.0370899501137243, \
          0.9029898914592993, \
          0.0970101085407006, \
          0.9029898914592993, \
          0.0970101085407006, \
          0.6902772166041579, \
          0.3097227833958421, \
          0.6902772166041579, \
          0.3097227833958421 ] )

  w = np.array ( [ \
          0.0604938271604938, \
          0.0604938271604938, \
          0.0604938271604938, \
          0.0604938271604938, \
          0.0593579436726576, \
          0.0593579436726576, \
          0.0593579436726576, \
          0.0593579436726576, \
          0.1301482291668486, \
          0.1301482291668486, \
          0.1301482291668486, \
          0.1301482291668486 ] )

  return x, y, w

def rule09 ( ):

#*****************************************************************************80
#
## rule09() returns the quadrilateral rule of precision 9.
#
#  Discussion:
#
#    We suppose we are given a quadrilateral Quad with vertices
#    (0,0), (1,0), (1,1), (0,1),
#    We call a rule with n points, returning coordinates
#    x, y, and weights w.  Then the integral I of f(x,y,z) over Quad is 
#    approximated by Q as follows:
#
#    Q = area(Quad) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i)) 
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
#    real x(n), y(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.7444634284871845, \
          0.5000000000000000, \
          0.2555365715128155, \
          0.5000000000000000, \
          0.9698276290484189, \
          0.9698276290484189, \
          0.0301723709515812, \
          0.0301723709515812, \
          0.8454402752431720, \
          0.8454402752431720, \
          0.1545597247568281, \
          0.1545597247568281, \
          0.9593102205283611, \
          0.6724360126822018, \
          0.9593102205283611, \
          0.3275639873177982, \
          0.0406897794716389, \
          0.6724360126822018, \
          0.0406897794716389, \
          0.3275639873177982 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.7444634284871845, \
          0.5000000000000000, \
          0.2555365715128155, \
          0.9698276290484189, \
          0.0301723709515812, \
          0.9698276290484189, \
          0.0301723709515812, \
          0.8454402752431720, \
          0.1545597247568281, \
          0.8454402752431720, \
          0.1545597247568281, \
          0.6724360126822018, \
          0.9593102205283611, \
          0.3275639873177982, \
          0.9593102205283611, \
          0.6724360126822018, \
          0.0406897794716389, \
          0.3275639873177982, \
          0.0406897794716389 ] )

  w = np.array ( [ \
          0.1135409901716873, \
          0.1135409901716873, \
          0.1135409901716873, \
          0.1135409901716873, \
          0.0106828079664439, \
          0.0106828079664439, \
          0.0106828079664439, \
          0.0106828079664439, \
          0.0535500902317154, \
          0.0535500902317154, \
          0.0535500902317154, \
          0.0535500902317154, \
          0.0361130558150767, \
          0.0361130558150767, \
          0.0361130558150767, \
          0.0361130558150767, \
          0.0361130558150767, \
          0.0361130558150767, \
          0.0361130558150767, \
          0.0361130558150767 ] )

  return x, y, w

def rule11 ( ):

#*****************************************************************************80
#
## rule11() returns the quadrilateral rule of precision 11.
#
#  Discussion:
#
#    We suppose we are given a quadrilateral Quad with vertices
#    (0,0), (1,0), (1,1), (0,1),
#    We call a rule with n points, returning coordinates
#    x, y, and weights w.  Then the integral I of f(x,y,z) over Quad is 
#    approximated by Q as follows:
#
#    Q = area(Quad) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i)) 
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
#    real x(n), y(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.8573089148323030, \
          0.5000000000000000, \
          0.1426910851676970, \
          0.5000000000000000, \
          0.6368286050857298, \
          0.6368286050857298, \
          0.3631713949142702, \
          0.3631713949142702, \
          0.8183019661061506, \
          0.8183019661061506, \
          0.1816980338938495, \
          0.1816980338938495, \
          0.9758151943920168, \
          0.9077827168448191, \
          0.9758151943920168, \
          0.0922172831551808, \
          0.0241848056079833, \
          0.9077827168448191, \
          0.0241848056079833, \
          0.0922172831551808, \
          0.6731036000238227, \
          0.9677839357437956, \
          0.6731036000238227, \
          0.0322160642562044, \
          0.3268963999761773, \
          0.9677839357437956, \
          0.3268963999761773, \
          0.0322160642562044 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.8573089148323030, \
          0.5000000000000000, \
          0.1426910851676970, \
          0.6368286050857298, \
          0.3631713949142702, \
          0.6368286050857298, \
          0.3631713949142702, \
          0.8183019661061506, \
          0.1816980338938495, \
          0.8183019661061506, \
          0.1816980338938495, \
          0.9077827168448191, \
          0.9758151943920168, \
          0.0922172831551808, \
          0.9758151943920168, \
          0.9077827168448191, \
          0.0241848056079833, \
          0.0922172831551808, \
          0.0241848056079833, \
          0.9677839357437956, \
          0.6731036000238227, \
          0.0322160642562044, \
          0.6731036000238227, \
          0.9677839357437956, \
          0.3268963999761773, \
          0.0322160642562044, \
          0.3268963999761773 ] )

  w = np.array ( [ \
          0.0543501099671780, \
          0.0543501099671780, \
          0.0543501099671780, \
          0.0543501099671780, \
          0.0693185257459628, \
          0.0693185257459628, \
          0.0693185257459628, \
          0.0693185257459628, \
          0.0534834094695620, \
          0.0534834094695620, \
          0.0534834094695620, \
          0.0534834094695620, \
          0.0110186422787458, \
          0.0110186422787458, \
          0.0110186422787458, \
          0.0110186422787458, \
          0.0110186422787458, \
          0.0110186422787458, \
          0.0110186422787458, \
          0.0110186422787458, \
          0.0254053351299028, \
          0.0254053351299028, \
          0.0254053351299028, \
          0.0254053351299028, \
          0.0254053351299028, \
          0.0254053351299028, \
          0.0254053351299028, \
          0.0254053351299028 ] )

  return x, y, w

def rule13 ( ):

#*****************************************************************************80
#
## rule13() returns the quadrilateral rule of precision 13.
#
#  Discussion:
#
#    We suppose we are given a quadrilateral Quad with vertices
#    (0,0), (1,0), (1,1), (0,1),
#    We call a rule with n points, returning coordinates
#    x, y, and weights w.  Then the integral I of f(x,y,z) over Quad is 
#    approximated by Q as follows:
#
#    Q = area(Quad) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i)) 
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
#    real x(n), y(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.5000000000000000, \
          0.9917306663066228, \
          0.5000000000000000, \
          0.0082693336933772, \
          0.5000000000000000, \
          0.8199307091835548, \
          0.5000000000000000, \
          0.1800692908164451, \
          0.5000000000000000, \
          0.9593892440398557, \
          0.9593892440398557, \
          0.0406107559601443, \
          0.0406107559601443, \
          0.6898142525933719, \
          0.6898142525933719, \
          0.3101857474066281, \
          0.3101857474066281, \
          0.8497771082566756, \
          0.8497771082566756, \
          0.1502228917433244, \
          0.1502228917433244, \
          0.8217986874983090, \
          0.9875344419529918, \
          0.8217986874983090, \
          0.0124655580470082, \
          0.1782013125016910, \
          0.9875344419529918, \
          0.1782013125016910, \
          0.0124655580470082, \
          0.6667699405823916, \
          0.9322138046335309, \
          0.6667699405823916, \
          0.0677861953664691, \
          0.3332300594176084, \
          0.9322138046335309, \
          0.3332300594176084, \
          0.0677861953664691 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9917306663066228, \
          0.5000000000000000, \
          0.0082693336933772, \
          0.5000000000000000, \
          0.8199307091835548, \
          0.5000000000000000, \
          0.1800692908164451, \
          0.9593892440398557, \
          0.0406107559601443, \
          0.9593892440398557, \
          0.0406107559601443, \
          0.6898142525933719, \
          0.3101857474066281, \
          0.6898142525933719, \
          0.3101857474066281, \
          0.8497771082566756, \
          0.1502228917433244, \
          0.8497771082566756, \
          0.1502228917433244, \
          0.9875344419529918, \
          0.8217986874983090, \
          0.0124655580470082, \
          0.8217986874983090, \
          0.9875344419529918, \
          0.1782013125016910, \
          0.0124655580470082, \
          0.1782013125016910, \
          0.9322138046335309, \
          0.6667699405823916, \
          0.0677861953664691, \
          0.6667699405823916, \
          0.9322138046335309, \
          0.3332300594176084, \
          0.0677861953664691, \
          0.3332300594176084 ] )

  w = np.array ( [ \
          0.0749983360897274, \
          0.0095321563374632, \
          0.0095321563374632, \
          0.0095321563374632, \
          0.0095321563374632, \
          0.0461338672424518, \
          0.0461338672424518, \
          0.0461338672424518, \
          0.0461338672424518, \
          0.0098767851618631, \
          0.0098767851618631, \
          0.0098767851618631, \
          0.0098767851618631, \
          0.0578496298501713, \
          0.0578496298501713, \
          0.0578496298501713, \
          0.0578496298501713, \
          0.0343105241782509, \
          0.0343105241782509, \
          0.0343105241782509, \
          0.0343105241782509, \
          0.0083799450125954, \
          0.0083799450125954, \
          0.0083799450125954, \
          0.0083799450125954, \
          0.0083799450125954, \
          0.0083799450125954, \
          0.0083799450125954, \
          0.0083799450125954, \
          0.0283937815910886, \
          0.0283937815910886, \
          0.0283937815910886, \
          0.0283937815910886, \
          0.0283937815910886, \
          0.0283937815910886, \
          0.0283937815910886, \
          0.0283937815910886 ] )

  return x, y, w

def rule15 ( ):

#*****************************************************************************80
#
## rule15() returns the quadrilateral rule of precision 15.
#
#  Discussion:
#
#    We suppose we are given a quadrilateral Quad with vertices
#    (0,0), (1,0), (1,1), (0,1),
#    We call a rule with n points, returning coordinates
#    x, y, and weights w.  Then the integral I of f(x,y,z) over Quad is 
#    approximated by Q as follows:
#
#    Q = area(Quad) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i)) 
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
#    real x(n), y(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.8990494939485035, \
          0.5000000000000000, \
          0.1009505060514965, \
          0.5000000000000000, \
          0.6519265131992299, \
          0.5000000000000000, \
          0.3480734868007701, \
          0.5000000000000000, \
          0.9412111350534427, \
          0.9412111350534427, \
          0.0587888649465573, \
          0.0587888649465573, \
          0.9888948997699514, \
          0.9888948997699514, \
          0.0111051002300486, \
          0.0111051002300486, \
          0.9043560679097518, \
          0.7836067866982954, \
          0.9043560679097518, \
          0.2163932133017046, \
          0.0956439320902482, \
          0.7836067866982954, \
          0.0956439320902482, \
          0.2163932133017046, \
          0.6523273995185263, \
          0.7893680970179033, \
          0.6523273995185263, \
          0.2106319029820967, \
          0.3476726004814737, \
          0.7893680970179033, \
          0.3476726004814737, \
          0.2106319029820967, \
          0.9902524218622659, \
          0.8487318159954835, \
          0.9902524218622659, \
          0.1512681840045165, \
          0.0097475781377340, \
          0.8487318159954835, \
          0.0097475781377340, \
          0.1512681840045165, \
          0.6324220779361581, \
          0.9778712599047559, \
          0.6324220779361581, \
          0.0221287400952441, \
          0.3675779220638419, \
          0.9778712599047559, \
          0.3675779220638419, \
          0.0221287400952441 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.8990494939485035, \
          0.5000000000000000, \
          0.1009505060514965, \
          0.5000000000000000, \
          0.6519265131992299, \
          0.5000000000000000, \
          0.3480734868007701, \
          0.9412111350534427, \
          0.0587888649465573, \
          0.9412111350534427, \
          0.0587888649465573, \
          0.9888948997699514, \
          0.0111051002300486, \
          0.9888948997699514, \
          0.0111051002300486, \
          0.7836067866982954, \
          0.9043560679097518, \
          0.2163932133017046, \
          0.9043560679097518, \
          0.7836067866982954, \
          0.0956439320902482, \
          0.2163932133017046, \
          0.0956439320902482, \
          0.7893680970179033, \
          0.6523273995185263, \
          0.2106319029820967, \
          0.6523273995185263, \
          0.7893680970179033, \
          0.3476726004814737, \
          0.2106319029820967, \
          0.3476726004814737, \
          0.8487318159954835, \
          0.9902524218622659, \
          0.1512681840045165, \
          0.9902524218622659, \
          0.8487318159954835, \
          0.0097475781377340, \
          0.1512681840045165, \
          0.0097475781377340, \
          0.9778712599047559, \
          0.6324220779361581, \
          0.0221287400952441, \
          0.6324220779361581, \
          0.9778712599047559, \
          0.3675779220638419, \
          0.0221287400952441, \
          0.3675779220638419 ] )

  w = np.array ( [ \
          0.0287332318158813, \
          0.0287332318158813, \
          0.0287332318158813, \
          0.0287332318158813, \
          0.0454214397418180, \
          0.0454214397418180, \
          0.0454214397418180, \
          0.0454214397418180, \
          0.0103096209471915, \
          0.0103096209471915, \
          0.0103096209471915, \
          0.0103096209471915, \
          0.0014834366214598, \
          0.0014834366214598, \
          0.0014834366214598, \
          0.0014834366214598, \
          0.0252872858693581, \
          0.0252872858693581, \
          0.0252872858693581, \
          0.0252872858693581, \
          0.0252872858693581, \
          0.0252872858693581, \
          0.0252872858693581, \
          0.0252872858693581, \
          0.0369591804082203, \
          0.0369591804082203, \
          0.0369591804082203, \
          0.0369591804082203, \
          0.0369591804082203, \
          0.0369591804082203, \
          0.0369591804082203, \
          0.0369591804082203, \
          0.0058182985361683, \
          0.0058182985361683, \
          0.0058182985361683, \
          0.0058182985361683, \
          0.0058182985361683, \
          0.0058182985361683, \
          0.0058182985361683, \
          0.0058182985361683, \
          0.0139613706230780, \
          0.0139613706230780, \
          0.0139613706230780, \
          0.0139613706230780, \
          0.0139613706230780, \
          0.0139613706230780, \
          0.0139613706230780, \
          0.0139613706230780 ] )

  return x, y, w

def rule17 ( ):

#*****************************************************************************80
#
## rule17() returns the quadrilateral rule of precision 17.
#
#  Discussion:
#
#    We suppose we are given a quadrilateral Quad with vertices
#    (0,0), (1,0), (1,1), (0,1),
#    We call a rule with n points, returning coordinates
#    x, y, and weights w.  Then the integral I of f(x,y,z) over Quad is 
#    approximated by Q as follows:
#
#    Q = area(Quad) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i)) 
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
#    real x(n), y(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.7725214936045741, \
          0.5000000000000000, \
          0.2274785063954258, \
          0.5000000000000000, \
          0.9587485941095766, \
          0.5000000000000000, \
          0.0412514058904234, \
          0.5000000000000000, \
          0.5962771213070235, \
          0.5962771213070235, \
          0.4037228786929766, \
          0.4037228786929766, \
          0.9356643423477216, \
          0.9356643423477216, \
          0.0643356576522784, \
          0.0643356576522784, \
          0.8471940450447754, \
          0.8471940450447754, \
          0.1528059549552246, \
          0.1528059549552246, \
          0.7288414964415777, \
          0.7288414964415777, \
          0.2711585035584222, \
          0.2711585035584222, \
          0.9846021280457544, \
          0.9846021280457544, \
          0.0153978719542456, \
          0.0153978719542456, \
          0.8810441380400991, \
          0.6397388833575961, \
          0.8810441380400991, \
          0.3602611166424039, \
          0.1189558619599009, \
          0.6397388833575961, \
          0.1189558619599009, \
          0.3602611166424039, \
          0.9536971760991118, \
          0.7734493352071550, \
          0.9536971760991118, \
          0.2265506647928450, \
          0.0463028239008882, \
          0.7734493352071550, \
          0.0463028239008882, \
          0.2265506647928450, \
          0.8806243332195414, \
          0.9918939857507747, \
          0.8806243332195414, \
          0.0081060142492252, \
          0.1193756667804586, \
          0.9918939857507747, \
          0.1193756667804586, \
          0.0081060142492252, \
          0.9935473535223840, \
          0.6514037408944306, \
          0.9935473535223840, \
          0.3485962591055693, \
          0.0064526464776161, \
          0.6514037408944306, \
          0.0064526464776161, \
          0.3485962591055693 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.7725214936045741, \
          0.5000000000000000, \
          0.2274785063954258, \
          0.5000000000000000, \
          0.9587485941095766, \
          0.5000000000000000, \
          0.0412514058904234, \
          0.5962771213070235, \
          0.4037228786929766, \
          0.5962771213070235, \
          0.4037228786929766, \
          0.9356643423477216, \
          0.0643356576522784, \
          0.9356643423477216, \
          0.0643356576522784, \
          0.8471940450447754, \
          0.1528059549552246, \
          0.8471940450447754, \
          0.1528059549552246, \
          0.7288414964415777, \
          0.2711585035584222, \
          0.7288414964415777, \
          0.2711585035584222, \
          0.9846021280457544, \
          0.0153978719542456, \
          0.9846021280457544, \
          0.0153978719542456, \
          0.6397388833575961, \
          0.8810441380400991, \
          0.3602611166424039, \
          0.8810441380400991, \
          0.6397388833575961, \
          0.1189558619599009, \
          0.3602611166424039, \
          0.1189558619599009, \
          0.7734493352071550, \
          0.9536971760991118, \
          0.2265506647928450, \
          0.9536971760991118, \
          0.7734493352071550, \
          0.0463028239008882, \
          0.2265506647928450, \
          0.0463028239008882, \
          0.9918939857507747, \
          0.8806243332195414, \
          0.0081060142492252, \
          0.8806243332195414, \
          0.9918939857507747, \
          0.1193756667804586, \
          0.0081060142492252, \
          0.1193756667804586, \
          0.6514037408944306, \
          0.9935473535223840, \
          0.3485962591055693, \
          0.9935473535223840, \
          0.6514037408944306, \
          0.0064526464776161, \
          0.3485962591055693, \
          0.0064526464776161 ] )

  w = np.array ( [ \
          0.0347010944218050, \
          0.0347010944218050, \
          0.0347010944218050, \
          0.0347010944218050, \
          0.0163369559518662, \
          0.0163369559518662, \
          0.0163369559518662, \
          0.0163369559518662, \
          0.0357141049055499, \
          0.0357141049055499, \
          0.0357141049055499, \
          0.0357141049055499, \
          0.0091789771213129, \
          0.0091789771213129, \
          0.0091789771213129, \
          0.0091789771213129, \
          0.0215639249095360, \
          0.0215639249095360, \
          0.0215639249095360, \
          0.0215639249095360, \
          0.0336390683029792, \
          0.0336390683029792, \
          0.0336390683029792, \
          0.0336390683029792, \
          0.0019139083537275, \
          0.0019139083537275, \
          0.0019139083537275, \
          0.0019139083537275, \
          0.0257941811962338, \
          0.0257941811962338, \
          0.0257941811962338, \
          0.0257941811962338, \
          0.0257941811962338, \
          0.0257941811962338, \
          0.0257941811962338, \
          0.0257941811962338, \
          0.0137066000593229, \
          0.0137066000593229, \
          0.0137066000593229, \
          0.0137066000593229, \
          0.0137066000593229, \
          0.0137066000593229, \
          0.0137066000593229, \
          0.0137066000593229, \
          0.0037799525970642, \
          0.0037799525970642, \
          0.0037799525970642, \
          0.0037799525970642, \
          0.0037799525970642, \
          0.0037799525970642, \
          0.0037799525970642, \
          0.0037799525970642, \
          0.0051952491639908, \
          0.0051952491639908, \
          0.0051952491639908, \
          0.0051952491639908, \
          0.0051952491639908, \
          0.0051952491639908, \
          0.0051952491639908, \
          0.0051952491639908 ] )

  return x, y, w

def rule19 ( ):

#*****************************************************************************80
#
## rule19() returns the quadrilateral rule of precision 19.
#
#  Discussion:
#
#    We suppose we are given a quadrilateral Quad with vertices
#    (0,0), (1,0), (1,1), (0,1),
#    We call a rule with n points, returning coordinates
#    x, y, and weights w.  Then the integral I of f(x,y,z) over Quad is 
#    approximated by Q as follows:
#
#    Q = area(Quad) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i)) 
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
#    real x(n), y(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.8571721297863971, \
          0.5000000000000000, \
          0.1428278702136029, \
          0.5000000000000000, \
          0.6328360260604818, \
          0.5000000000000000, \
          0.3671639739395182, \
          0.5000000000000000, \
          0.9822171346289836, \
          0.5000000000000000, \
          0.0177828653710164, \
          0.5000000000000000, \
          0.9016898647338425, \
          0.9016898647338425, \
          0.0983101352661575, \
          0.0983101352661575, \
          0.9960827029485674, \
          0.9960827029485674, \
          0.0039172970514326, \
          0.0039172970514326, \
          0.9647248013998047, \
          0.9647248013998047, \
          0.0352751986001953, \
          0.0352751986001953, \
          0.7551391286846717, \
          0.6333201572972811, \
          0.7551391286846717, \
          0.3666798427027189, \
          0.2448608713153283, \
          0.6333201572972811, \
          0.2448608713153283, \
          0.3666798427027189, \
          0.6953671028876249, \
          0.9939464665708677, \
          0.6953671028876249, \
          0.0060535334291323, \
          0.3046328971123751, \
          0.9939464665708677, \
          0.3046328971123751, \
          0.0060535334291323, \
          0.8585839606548726, \
          0.7562459386080489, \
          0.8585839606548726, \
          0.2437540613919512, \
          0.1414160393451274, \
          0.7562459386080489, \
          0.1414160393451274, \
          0.2437540613919512, \
          0.6327200039056480, \
          0.9344512170772521, \
          0.6327200039056480, \
          0.0655487829227479, \
          0.3672799960943520, \
          0.9344512170772521, \
          0.3672799960943520, \
          0.0655487829227479, \
          0.8100176993466282, \
          0.9631514779035646, \
          0.8100176993466282, \
          0.0368485220964354, \
          0.1899823006533718, \
          0.9631514779035646, \
          0.1899823006533718, \
          0.0368485220964354, \
          0.9008357923592984, \
          0.9942232653419869, \
          0.9008357923592984, \
          0.0057767346580131, \
          0.0991642076407016, \
          0.9942232653419869, \
          0.0991642076407016, \
          0.0057767346580131 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.8571721297863971, \
          0.5000000000000000, \
          0.1428278702136029, \
          0.5000000000000000, \
          0.6328360260604818, \
          0.5000000000000000, \
          0.3671639739395182, \
          0.5000000000000000, \
          0.9822171346289836, \
          0.5000000000000000, \
          0.0177828653710164, \
          0.9016898647338425, \
          0.0983101352661575, \
          0.9016898647338425, \
          0.0983101352661575, \
          0.9960827029485674, \
          0.0039172970514326, \
          0.9960827029485674, \
          0.0039172970514326, \
          0.9647248013998047, \
          0.0352751986001953, \
          0.9647248013998047, \
          0.0352751986001953, \
          0.6333201572972811, \
          0.7551391286846717, \
          0.3666798427027189, \
          0.7551391286846717, \
          0.6333201572972811, \
          0.2448608713153283, \
          0.3666798427027189, \
          0.2448608713153283, \
          0.9939464665708677, \
          0.6953671028876249, \
          0.0060535334291323, \
          0.6953671028876249, \
          0.9939464665708677, \
          0.3046328971123751, \
          0.0060535334291323, \
          0.3046328971123751, \
          0.7562459386080489, \
          0.8585839606548726, \
          0.2437540613919512, \
          0.8585839606548726, \
          0.7562459386080489, \
          0.1414160393451274, \
          0.2437540613919512, \
          0.1414160393451274, \
          0.9344512170772521, \
          0.6327200039056480, \
          0.0655487829227479, \
          0.6327200039056480, \
          0.9344512170772521, \
          0.3672799960943520, \
          0.0655487829227479, \
          0.3672799960943520, \
          0.9631514779035646, \
          0.8100176993466282, \
          0.0368485220964354, \
          0.8100176993466282, \
          0.9631514779035646, \
          0.1899823006533718, \
          0.0368485220964354, \
          0.1899823006533718, \
          0.9942232653419869, \
          0.9008357923592984, \
          0.0057767346580131, \
          0.9008357923592984, \
          0.9942232653419869, \
          0.0991642076407016, \
          0.0057767346580131, \
          0.0991642076407016 ] )

  w = np.array ( [ \
          0.0244343411732072, \
          0.0244343411732072, \
          0.0244343411732072, \
          0.0244343411732072, \
          0.0348269032306206, \
          0.0348269032306206, \
          0.0348269032306206, \
          0.0348269032306206, \
          0.0087173958729720, \
          0.0087173958729720, \
          0.0087173958729720, \
          0.0087173958729720, \
          0.0119511367906989, \
          0.0119511367906989, \
          0.0119511367906989, \
          0.0119511367906989, \
          0.0004044287944779, \
          0.0004044287944779, \
          0.0004044287944779, \
          0.0004044287944779, \
          0.0043602620085889, \
          0.0043602620085889, \
          0.0043602620085889, \
          0.0043602620085889, \
          0.0294314582100140, \
          0.0294314582100140, \
          0.0294314582100140, \
          0.0294314582100140, \
          0.0294314582100140, \
          0.0294314582100140, \
          0.0294314582100140, \
          0.0294314582100140, \
          0.0040448944029145, \
          0.0040448944029145, \
          0.0040448944029145, \
          0.0040448944029145, \
          0.0040448944029145, \
          0.0040448944029145, \
          0.0040448944029145, \
          0.0040448944029145, \
          0.0207116547458512, \
          0.0207116547458512, \
          0.0207116547458512, \
          0.0207116547458512, \
          0.0207116547458512, \
          0.0207116547458512, \
          0.0207116547458512, \
          0.0207116547458512, \
          0.0162472703731490, \
          0.0162472703731490, \
          0.0162472703731490, \
          0.0162472703731490, \
          0.0162472703731490, \
          0.0162472703731490, \
          0.0162472703731490, \
          0.0162472703731490, \
          0.0097451380991026, \
          0.0097451380991026, \
          0.0097451380991026, \
          0.0097451380991026, \
          0.0097451380991026, \
          0.0097451380991026, \
          0.0097451380991026, \
          0.0097451380991026, \
          0.0024723502336859, \
          0.0024723502336859, \
          0.0024723502336859, \
          0.0024723502336859, \
          0.0024723502336859, \
          0.0024723502336859, \
          0.0024723502336859, \
          0.0024723502336859 ] )

  return x, y, w

def rule21 ( ):

#*****************************************************************************80
#
## rule21() returns the quadrilateral rule of precision 21.
#
#  Discussion:
#
#    We suppose we are given a quadrilateral Quad with vertices
#    (0,0), (1,0), (1,1), (0,1),
#    We call a rule with n points, returning coordinates
#    x, y, and weights w.  Then the integral I of f(x,y,z) over Quad is 
#    approximated by Q as follows:
#
#    Q = area(Quad) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 April 2023
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
#    real x(n), y(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.5000000000000000, \
          0.7366755371791120, \
          0.5000000000000000, \
          0.2633244628208880, \
          0.5000000000000000, \
          0.9176392148779342, \
          0.5000000000000000, \
          0.0823607851220658, \
          0.5000000000000000, \
          0.6286859503036145, \
          0.6286859503036145, \
          0.3713140496963855, \
          0.3713140496963855, \
          0.9816689160578117, \
          0.9816689160578117, \
          0.0183310839421883, \
          0.0183310839421883, \
          0.9312259626898258, \
          0.9312259626898258, \
          0.0687740373101742, \
          0.0687740373101742, \
          0.7484489812596729, \
          0.7484489812596729, \
          0.2515510187403271, \
          0.2515510187403271, \
          0.8521660875977003, \
          0.8521660875977003, \
          0.1478339124022997, \
          0.1478339124022997, \
          0.6209390927383510, \
          0.8370731099776589, \
          0.6209390927383510, \
          0.1629268900223411, \
          0.3790609072616490, \
          0.8370731099776589, \
          0.3790609072616490, \
          0.1629268900223411, \
          0.7400784831563976, \
          0.9123236876354603, \
          0.7400784831563976, \
          0.0876763123645397, \
          0.2599215168436024, \
          0.9123236876354603, \
          0.2599215168436024, \
          0.0876763123645397, \
          0.9661209679608770, \
          0.6353495920508325, \
          0.9661209679608770, \
          0.3646504079491675, \
          0.0338790320391230, \
          0.6353495920508325, \
          0.0338790320391230, \
          0.3646504079491675, \
          0.9674511629120053, \
          0.8375197837185376, \
          0.9674511629120053, \
          0.1624802162814624, \
          0.0325488370879947, \
          0.8375197837185376, \
          0.0325488370879947, \
          0.1624802162814624, \
          0.9952277337647621, \
          0.7444581255885834, \
          0.9952277337647621, \
          0.2555418744114166, \
          0.0047722662352379, \
          0.7444581255885834, \
          0.0047722662352379, \
          0.2555418744114166, \
          0.9155676229879507, \
          0.9944803056932863, \
          0.9155676229879507, \
          0.0055196943067138, \
          0.0844323770120493, \
          0.9944803056932863, \
          0.0844323770120493, \
          0.0055196943067138, \
          0.5457348004611456, \
          0.9920085742447995, \
          0.5457348004611456, \
          0.0079914257552005, \
          0.4542651995388544, \
          0.9920085742447995, \
          0.4542651995388544, \
          0.0079914257552005 ] )

  y = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.7366755371791120, \
          0.5000000000000000, \
          0.2633244628208880, \
          0.5000000000000000, \
          0.9176392148779342, \
          0.5000000000000000, \
          0.0823607851220658, \
          0.6286859503036145, \
          0.3713140496963855, \
          0.6286859503036145, \
          0.3713140496963855, \
          0.9816689160578117, \
          0.0183310839421883, \
          0.9816689160578117, \
          0.0183310839421883, \
          0.9312259626898258, \
          0.0687740373101742, \
          0.9312259626898258, \
          0.0687740373101742, \
          0.7484489812596729, \
          0.2515510187403271, \
          0.7484489812596729, \
          0.2515510187403271, \
          0.8521660875977003, \
          0.1478339124022997, \
          0.8521660875977003, \
          0.1478339124022997, \
          0.8370731099776589, \
          0.6209390927383510, \
          0.1629268900223411, \
          0.6209390927383510, \
          0.8370731099776589, \
          0.3790609072616490, \
          0.1629268900223411, \
          0.3790609072616490, \
          0.9123236876354603, \
          0.7400784831563976, \
          0.0876763123645397, \
          0.7400784831563976, \
          0.9123236876354603, \
          0.2599215168436024, \
          0.0876763123645397, \
          0.2599215168436024, \
          0.6353495920508325, \
          0.9661209679608770, \
          0.3646504079491675, \
          0.9661209679608770, \
          0.6353495920508325, \
          0.0338790320391230, \
          0.3646504079491675, \
          0.0338790320391230, \
          0.8375197837185376, \
          0.9674511629120053, \
          0.1624802162814624, \
          0.9674511629120053, \
          0.8375197837185376, \
          0.0325488370879947, \
          0.1624802162814624, \
          0.0325488370879947, \
          0.7444581255885834, \
          0.9952277337647621, \
          0.2555418744114166, \
          0.9952277337647621, \
          0.7444581255885834, \
          0.0047722662352379, \
          0.2555418744114166, \
          0.0047722662352379, \
          0.9944803056932863, \
          0.9155676229879507, \
          0.0055196943067138, \
          0.9155676229879507, \
          0.9944803056932863, \
          0.0844323770120493, \
          0.0055196943067138, \
          0.0844323770120493, \
          0.9920085742447995, \
          0.5457348004611456, \
          0.0079914257552005, \
          0.5457348004611456, \
          0.9920085742447995, \
          0.4542651995388544, \
          0.0079914257552005, \
          0.4542651995388544 ] )

  w = np.array ( [ \
          0.0337982100890357, \
          0.0266985396964851, \
          0.0266985396964851, \
          0.0266985396964851, \
          0.0266985396964851, \
          0.0165643020012361, \
          0.0165643020012361, \
          0.0165643020012361, \
          0.0165643020012361, \
          0.0299711209115851, \
          0.0299711209115851, \
          0.0299711209115851, \
          0.0299711209115851, \
          0.0020573653223050, \
          0.0020573653223050, \
          0.0020573653223050, \
          0.0020573653223050, \
          0.0076509102321939, \
          0.0076509102321939, \
          0.0076509102321939, \
          0.0076509102321939, \
          0.0241979479733988, \
          0.0241979479733988, \
          0.0241979479733988, \
          0.0241979479733988, \
          0.0153790853703291, \
          0.0153790853703291, \
          0.0153790853703291, \
          0.0153790853703291, \
          0.0216821248783021, \
          0.0216821248783021, \
          0.0216821248783021, \
          0.0216821248783021, \
          0.0216821248783021, \
          0.0216821248783021, \
          0.0216821248783021, \
          0.0216821248783021, \
          0.0139697793510318, \
          0.0139697793510318, \
          0.0139697793510318, \
          0.0139697793510318, \
          0.0139697793510318, \
          0.0139697793510318, \
          0.0139697793510318, \
          0.0139697793510318, \
          0.0092822068602285, \
          0.0092822068602285, \
          0.0092822068602285, \
          0.0092822068602285, \
          0.0092822068602285, \
          0.0092822068602285, \
          0.0092822068602285, \
          0.0092822068602285, \
          0.0071939002127551, \
          0.0071939002127551, \
          0.0071939002127551, \
          0.0071939002127551, \
          0.0071939002127551, \
          0.0071939002127551, \
          0.0071939002127551, \
          0.0071939002127551, \
          0.0028773801106233, \
          0.0028773801106233, \
          0.0028773801106233, \
          0.0028773801106233, \
          0.0028773801106233, \
          0.0028773801106233, \
          0.0028773801106233, \
          0.0028773801106233, \
          0.0018821205326004, \
          0.0018821205326004, \
          0.0018821205326004, \
          0.0018821205326004, \
          0.0018821205326004, \
          0.0018821205326004, \
          0.0018821205326004, \
          0.0018821205326004, \
          0.0026280760395628, \
          0.0026280760395628, \
          0.0026280760395628, \
          0.0026280760395628, \
          0.0026280760395628, \
          0.0026280760395628, \
          0.0026280760395628, \
          0.0026280760395628 ] )

  return x, y, w

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
  quadrilateral_witherden_rule_test ( )
  timestamp ( )

