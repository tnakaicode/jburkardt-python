#! /usr/bin/env python3
#
def tetrahedron_witherden_rule_test ( ):

#*****************************************************************************80
#
## tetrahedron_witherden_rule_test() tests tetrahedron_witherden_rule().
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    12 July 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'tetrahedron_witherden_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test tetrahedron_witherden_rule().' )

  p = 5
  tetrahedron_witherden_rule_test01 ( p )

  p = 5
  tetrahedron_witherden_rule_test02 ( p )

  p_lo = 0
  p_hi = 10
  tetrahedron_witherden_rule_test03 ( p_lo, p_hi )

  tetrahedron_witherden_rule_test04 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'tetrahedron_witherden_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def tetrahedron_witherden_rule_test01 ( p ):

#*****************************************************************************80
#
## tetrahedron_witherden_rule_test01() computes a quadrature rule of precision P.
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
  print ( 'tetrahedron_witherden_rule_test01():' )
  print ( '  Quadrature rule for the tetrahedron,' )
  print ( '  given in barycentric coordinates.' )
  print ( '  Precision p = ', p )
#
#  Retrieve the rule.
#
  n, a, b, c, d, w = tetrahedron_witherden_rule ( p )
#
#  Print the rule.
#
  print ( '' )
  print ( '     I      W          A           B           C           D' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %10.6g  %10.6g  %10.6g  %10.6g  %10.6g' \
      % ( i, w[i], a[i], b[i], c[i], d[i] ) )
#
#  Verify weights sum to 1.
#
  w_sum = np.sum ( w )

  print ( '' )
  print ( '  Weight Sum ', w_sum )

  return

def tetrahedron_witherden_rule_test02 ( p ):

#*****************************************************************************80
#
## tetrahedron_witherden_rule_test02() tests a rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    23 May 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'tetrahedron_witherden_rule_test02():' )
  print ( '  Test the precision of a quadrature rule for the unit tetrahedron.' )

  dim_num = 3
#
#  Retrieve the rule.
#
  n, a, b, c, d, w = tetrahedron_witherden_rule ( p )
#
#  Pack the x, y, z vectors as rows of an array.
#
  xyz = np.transpose ( np.array ( [ a, b, c ] ) )

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

      quad = tetrahedron_unit_volume ( ) * np.dot ( w, v )

      exact = tetrahedron_unit_monomial_integral ( expon )

      quad_error = np.abs ( quad - exact )

      max_error = max ( max_error, quad_error )

      if ( not more ):
        break

    print ( '  %2d  %24.16g' % ( degree, max_error ) )

  return

def tetrahedron_witherden_rule_test03 ( p_lo, p_hi ):

#*****************************************************************************80
#
## tetrahedron_witherden_rule_test03() tests absolute and relative precision.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    12 July 2023
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
  print ( 'tetrahedron_witherden_rule_test03():' )
  print ( '  Test the precision of quadrature rules for the unit tetrahedron.' )
  print ( '  Check rules of precision p =', p_lo, 'through', p_hi )
  print ( '  for error in approximating integrals of monomials.' )

  dim_num = 3

  print ( '' )
  print ( '              maximum                   maximum' )
  print ( '   p          absolute                  relative' )
  print ( '              error                     error' )
  print ( '' )

  for p in range ( p_lo, p_hi + 1 ):

    n, a, b, c, d, w = tetrahedron_witherden_rule ( p )
#
#  Pack the x, y, z vectors as rows of an array.
#
    xyz = np.transpose ( np.array ( [ a, b, c ] ) )

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

        quad = tetrahedron_unit_volume ( ) * np.dot ( w, v )

        exact = tetrahedron_unit_monomial_integral ( expon )

        quad_error = np.abs ( quad - exact )

        max_abs = max ( max_abs, quad_error )
        max_rel = max ( max_rel, quad_error / abs ( exact ) )

        if ( not more ):
          break

    print ( '  %2d  %24.16g  %24.16g' % ( p, max_abs, max_rel ) )

  return

def tetrahedron_witherden_rule_test04 ( ):

#*****************************************************************************80
#
## tetrahedron_witherden_rule_test04() integrates 1/sqrt(r).
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    07 May 2023
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Jan Jaskowiec, Natarajan Sukumar,
#    High order symmetric cubature rules for tetrahedra and pyramids,
#    International Journal of Numerical Methods in Engineering,
#    Volume 122, Number 1, pages 148-171, 24 August 2020.
#
  import numpy as np

  print ( '' )
  print ( 'tetrahedron_witherden_rule_test04():' )
  print ( '  Integrate 1/sqrt(r) over the reference tetrahedron.' )
  print ( '  Witherden rule #9 fails because a quadrature point is' )
  print ( '  very near the singularity at the origin.' )

  exact = 163.0 / 679.0
  print ( '  Exact integral value is', exact )

  tetra = np.array ( [ \
    [ 0.0, 0.0, 0.0 ], \
    [ 1.0, 0.0, 0.0 ], \
    [ 0.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0 ] ] )
  volume = tetrahedron_volume ( tetra )
  print ( '  Volume of tetrahedron is', volume )

  print ( '' )
  print ( '   P    N     Q     |Q-Exact]' )
  print ( '' )

  for p in range ( 0, 11 ):

    n, a, b, c, d, w = tetrahedron_witherden_rule ( p )
    r = np.sqrt ( a**2 + b**2 + c**2 )
    f = 1.0 / np.sqrt ( r )
    q = volume * np.dot ( w, f )
    e = np.abs ( q - exact )
    print ( '  %2d  %3d  %20.16g  %20.16g' % ( p, n, q, e ) )

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

def rule_order ( p ):

#*****************************************************************************80
#
## rule_order() returns the order of a tetrahedron quadrature rule of given precision.
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
#    24 April 2023
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
      1,   4,   8,  14,  14, \
     24,  35,  46,  59,  81 ] )

  order = order_vec[p]

  return order

def rule00 ( ):

#*****************************************************************************80
#
## rule00() returns the rule of precision 0.
#
#  Discussion:
#
#    The data is given for the reference tetrahedron
#    with vertices (0,0,0), (1,0,0), (0,1,0), (0,0,1).
#
#    We suppose we are given a tetrahedron T with vertices A, B, C, D.
#    We call a rule with n points, returning barycentric coordinates
#    a, b, c, d, and weights w.  Then the integral I of f(x,y,z) over T is 
#    approximated by Q as follows:
#
#    (x,y,z) = a(1:n) * A + b(1:n) * B + c(1:n) * C + d(1:n * D
#    Q = area(T) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2023
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
#    a(n), b(n), c(n), d(n): the barycentric coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  a = np.array ( [ \
      0.25000000000000000000 ] )

  b = np.array ( [ \
      0.25000000000000000000 ] )

  c = np.array ( [ \
      0.25000000000000000000 ] )

  d = np.array ( [ \
      0.25000000000000000000 ] )

  w = np.array ( [ \
      1.00000000000000000000 ] )

  return a, b, c, d, w

def rule01 ( ):

#*****************************************************************************80
#
## rule01() returns the rule of precision 1.
#
#  Discussion:
#
#    The data is given for the reference tetrahedron
#    with vertices (0,0,0), (1,0,0), (0,1,0), (0,0,1).
#
#    We suppose we are given a tetrahedron T with vertices A, B, C, D.
#    We call a rule with n points, returning barycentric coordinates
#    a, b, c, d, and weights w.  Then the integral I of f(x,y,z) over T is 
#    approximated by Q as follows:
#
#    (x,y,z) = a(1:n) * A + b(1:n) * B + c(1:n) * C + d(1:n * D
#    Q = area(T) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2023
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
#    a(n), b(n), c(n), d(n): the barycentric coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  a = np.array ( [ \
      0.25000000000000000000 ] )

  b = np.array ( [ \
      0.25000000000000000000 ] )

  c = np.array ( [ \
      0.25000000000000000000 ] )

  d = np.array ( [ \
      0.25000000000000000000 ] )

  w = np.array ( [ \
      1.00000000000000000000 ] )

  return a, b, c, d, w

def rule02 ( ):

#*****************************************************************************80
#
## rule02() returns the rule of precision 2.
#
#  Discussion:
#
#    The data is given for the reference tetrahedron
#    with vertices (0,0,0), (1,0,0), (0,1,0), (0,0,1).
#
#    We suppose we are given a tetrahedron T with vertices A, B, C, D.
#    We call a rule with n points, returning barycentric coordinates
#    a, b, c, d, and weights w.  Then the integral I of f(x,y,z) over T is 
#    approximated by Q as follows:
#
#    (x,y,z) = a(1:n) * A + b(1:n) * B + c(1:n) * C + d(1:n * D
#    Q = area(T) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2023
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
#    a(n), b(n), c(n), d(n): the barycentric coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  a = np.array ( [ \
      0.13819660112501053195, \
      0.13819660112501053195, \
      0.58541019662496851517, \
      0.13819660112501053195 ] )

  b = np.array ( [ \
      0.13819660112501053195, \
      0.58541019662496851517, \
      0.13819660112501053195, \
      0.13819660112501053195 ] )

  c = np.array ( [ \
      0.58541019662496851517, \
      0.13819660112501053195, \
      0.13819660112501053195, \
      0.13819660112501053195 ] )

  d = np.array ( [ \
      0.13819660112501042093, \
      0.13819660112501042093, \
      0.13819660112501042093, \
      0.58541019662496840414 ] )

  w = np.array ( [ \
      0.25000000000000000000, \
      0.25000000000000000000, \
      0.25000000000000000000, \
      0.25000000000000000000 ] )

  return a, b, c, d, w

def rule03 ( ):

#*****************************************************************************80
#
## rule03() returns the rule of precision 3.
#
#  Discussion:
#
#    The data is given for the reference tetrahedron
#    with vertices (0,0,0), (1,0,0), (0,1,0), (0,0,1).
#
#    We suppose we are given a tetrahedron T with vertices A, B, C, D.
#    We call a rule with n points, returning barycentric coordinates
#    a, b, c, d, and weights w.  Then the integral I of f(x,y,z) over T is 
#    approximated by Q as follows:
#
#    (x,y,z) = a(1:n) * A + b(1:n) * B + c(1:n) * C + d(1:n * D
#    Q = area(T) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2023
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
#    a(n), b(n), c(n), d(n): the barycentric coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  a = np.array ( [ \
      0.32816330251638170523, \
      0.32816330251638170523, \
      0.01551009245085493982, \
      0.32816330251638170523, \
      0.10804724989842862115, \
      0.10804724989842862115, \
      0.67585825030471413655, \
      0.10804724989842862115 ] )

  b = np.array ( [ \
      0.32816330251638170523, \
      0.01551009245085493982, \
      0.32816330251638170523, \
      0.32816330251638170523, \
      0.10804724989842862115, \
      0.67585825030471413655, \
      0.10804724989842862115, \
      0.10804724989842862115 ] )

  c = np.array ( [ \
      0.01551009245085493982, \
      0.32816330251638170523, \
      0.32816330251638170523, \
      0.32816330251638170523, \
      0.67585825030471413655, \
      0.10804724989842862115, \
      0.10804724989842862115, \
      0.10804724989842862115 ] )

  d = np.array ( [ \
      0.32816330251638164972, \
      0.32816330251638170523, \
      0.32816330251638170523, \
      0.01551009245085488431, \
      0.10804724989842862115, \
      0.10804724989842862115, \
      0.10804724989842862115, \
      0.67585825030471413655 ] )

  w = np.array ( [ \
      0.13621784253708735246, \
      0.13621784253708735246, \
      0.13621784253708735246, \
      0.13621784253708735246, \
      0.11378215746291264754, \
      0.11378215746291264754, \
      0.11378215746291264754, \
      0.11378215746291264754 ] )

  return a, b, c, d, w

def rule04 ( ):

#*****************************************************************************80
#
## rule04() returns the rule of precision 4.
#
#  Discussion:
#
#    The data is given for the reference tetrahedron
#    with vertices (0,0,0), (1,0,0), (0,1,0), (0,0,1).
#
#    We suppose we are given a tetrahedron T with vertices A, B, C, D.
#    We call a rule with n points, returning barycentric coordinates
#    a, b, c, d, and weights w.  Then the integral I of f(x,y,z) over T is 
#    approximated by Q as follows:
#
#    (x,y,z) = a(1:n) * A + b(1:n) * B + c(1:n) * C + d(1:n * D
#    Q = area(T) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2023
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
#    a(n), b(n), c(n), d(n): the barycentric coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  a = np.array ( [ \
      0.31088591926330061410, \
      0.31088591926330061410, \
      0.06734224221009815770, \
      0.31088591926330061410, \
      0.09273525031089124848, \
      0.09273525031089124848, \
      0.72179424906732636558, \
      0.09273525031089124848, \
      0.04550370412564963551, \
      0.45449629587435036449, \
      0.04550370412564963551, \
      0.04550370412564963551, \
      0.45449629587435036449, \
      0.45449629587435036449 ] )

  b = np.array ( [ \
      0.31088591926330061410, \
      0.06734224221009815770, \
      0.31088591926330061410, \
      0.31088591926330061410, \
      0.09273525031089124848, \
      0.72179424906732636558, \
      0.09273525031089124848, \
      0.09273525031089124848, \
      0.45449629587435036449, \
      0.04550370412564963551, \
      0.04550370412564963551, \
      0.45449629587435036449, \
      0.04550370412564963551, \
      0.45449629587435036449 ] )

  c = np.array ( [ \
      0.06734224221009815770, \
      0.31088591926330061410, \
      0.31088591926330061410, \
      0.31088591926330061410, \
      0.72179424906732636558, \
      0.09273525031089124848, \
      0.09273525031089124848, \
      0.09273525031089124848, \
      0.45449629587435036449, \
      0.45449629587435036449, \
      0.45449629587435036449, \
      0.04550370412564963551, \
      0.04550370412564963551, \
      0.04550370412564963551 ] )

  d = np.array ( [ \
      0.31088591926330055859, \
      0.31088591926330050308, \
      0.31088591926330050308, \
      0.06734224221009810218, \
      0.09273525031089113746, \
      0.09273525031089113746, \
      0.09273525031089113746, \
      0.72179424906732625455, \
      0.04550370412564963551, \
      0.04550370412564963551, \
      0.45449629587435036449, \
      0.45449629587435036449, \
      0.45449629587435036449, \
      0.04550370412564963551 ] )

  w = np.array ( [ \
      0.11268792571801586333, \
      0.11268792571801586333, \
      0.11268792571801586333, \
      0.11268792571801586333, \
      0.07349304311636195575, \
      0.07349304311636195575, \
      0.07349304311636195575, \
      0.07349304311636195575, \
      0.04254602077708146551, \
      0.04254602077708146551, \
      0.04254602077708146551, \
      0.04254602077708146551, \
      0.04254602077708146551, \
      0.04254602077708146551 ] )

  return a, b, c, d, w

def rule05 ( ):

#*****************************************************************************80
#
## rule05() returns the rule of precision 5.
#
#  Discussion:
#
#    The data is given for the reference tetrahedron
#    with vertices (0,0,0), (1,0,0), (0,1,0), (0,0,1).
#
#    We suppose we are given a tetrahedron T with vertices A, B, C, D.
#    We call a rule with n points, returning barycentric coordinates
#    a, b, c, d, and weights w.  Then the integral I of f(x,y,z) over T is 
#    approximated by Q as follows:
#
#    (x,y,z) = a(1:n) * A + b(1:n) * B + c(1:n) * C + d(1:n * D
#    Q = area(T) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2023
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
#    a(n), b(n), c(n), d(n): the barycentric coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  a = np.array ( [ \
      0.31088591926330061410, \
      0.31088591926330061410, \
      0.06734224221009815770, \
      0.31088591926330061410, \
      0.09273525031089124848, \
      0.09273525031089124848, \
      0.72179424906732636558, \
      0.09273525031089124848, \
      0.04550370412564963551, \
      0.45449629587435036449, \
      0.04550370412564963551, \
      0.04550370412564963551, \
      0.45449629587435036449, \
      0.45449629587435036449 ] )

  b = np.array ( [ \
      0.31088591926330061410, \
      0.06734224221009815770, \
      0.31088591926330061410, \
      0.31088591926330061410, \
      0.09273525031089124848, \
      0.72179424906732636558, \
      0.09273525031089124848, \
      0.09273525031089124848, \
      0.45449629587435036449, \
      0.04550370412564963551, \
      0.04550370412564963551, \
      0.45449629587435036449, \
      0.04550370412564963551, \
      0.45449629587435036449 ] )

  c = np.array ( [ \
      0.06734224221009815770, \
      0.31088591926330061410, \
      0.31088591926330061410, \
      0.31088591926330061410, \
      0.72179424906732636558, \
      0.09273525031089124848, \
      0.09273525031089124848, \
      0.09273525031089124848, \
      0.45449629587435036449, \
      0.45449629587435036449, \
      0.45449629587435036449, \
      0.04550370412564963551, \
      0.04550370412564963551, \
      0.04550370412564963551 ] )

  d = np.array ( [ \
      0.31088591926330055859, \
      0.31088591926330050308, \
      0.31088591926330050308, \
      0.06734224221009810218, \
      0.09273525031089113746, \
      0.09273525031089113746, \
      0.09273525031089113746, \
      0.72179424906732625455, \
      0.04550370412564963551, \
      0.04550370412564963551, \
      0.45449629587435036449, \
      0.45449629587435036449, \
      0.45449629587435036449, \
      0.04550370412564963551 ] )

  w = np.array ( [ \
      0.11268792571801586333, \
      0.11268792571801586333, \
      0.11268792571801586333, \
      0.11268792571801586333, \
      0.07349304311636195575, \
      0.07349304311636195575, \
      0.07349304311636195575, \
      0.07349304311636195575, \
      0.04254602077708146551, \
      0.04254602077708146551, \
      0.04254602077708146551, \
      0.04254602077708146551, \
      0.04254602077708146551, \
      0.04254602077708146551 ] )

  return a, b, c, d, w

def rule06 ( ):

#*****************************************************************************80
#
## rule06() returns the rule of precision 6.
#
#  Discussion:
#
#    The data is given for the reference tetrahedron
#    with vertices (0,0,0), (1,0,0), (0,1,0), (0,0,1).
#
#    We suppose we are given a tetrahedron T with vertices A, B, C, D.
#    We call a rule with n points, returning barycentric coordinates
#    a, b, c, d, and weights w.  Then the integral I of f(x,y,z) over T is 
#    approximated by Q as follows:
#
#    (x,y,z) = a(1:n) * A + b(1:n) * B + c(1:n) * C + d(1:n * D
#    Q = area(T) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2023
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
#    a(n), b(n), c(n), d(n): the barycentric coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  a = np.array ( [ \
      0.04067395853461136523, \
      0.04067395853461136523, \
      0.87797812439616595981, \
      0.04067395853461136523, \
      0.32233789014227554048, \
      0.32233789014227554048, \
      0.03298632957317348957, \
      0.32233789014227554048, \
      0.21460287125915200601, \
      0.21460287125915200601, \
      0.35619138622254387094, \
      0.21460287125915200601, \
      0.60300566479164918743, \
      0.60300566479164918743, \
      0.06366100187501749774, \
      0.26967233145831581709, \
      0.06366100187501749774, \
      0.06366100187501749774, \
      0.26967233145831581709, \
      0.06366100187501749774, \
      0.06366100187501749774, \
      0.06366100187501749774, \
      0.26967233145831581709, \
      0.60300566479164918743 ] )

  b = np.array ( [ \
      0.04067395853461136523, \
      0.87797812439616595981, \
      0.04067395853461136523, \
      0.04067395853461136523, \
      0.32233789014227554048, \
      0.03298632957317348957, \
      0.32233789014227554048, \
      0.32233789014227554048, \
      0.21460287125915200601, \
      0.35619138622254387094, \
      0.21460287125915200601, \
      0.21460287125915200601, \
      0.06366100187501749774, \
      0.06366100187501749774, \
      0.06366100187501749774, \
      0.60300566479164918743, \
      0.26967233145831581709, \
      0.60300566479164918743, \
      0.06366100187501749774, \
      0.26967233145831581709, \
      0.06366100187501749774, \
      0.60300566479164918743, \
      0.06366100187501749774, \
      0.26967233145831581709 ] )

  c = np.array ( [ \
      0.87797812439616595981, \
      0.04067395853461136523, \
      0.04067395853461136523, \
      0.04067395853461136523, \
      0.03298632957317348957, \
      0.32233789014227554048, \
      0.32233789014227554048, \
      0.32233789014227554048, \
      0.35619138622254387094, \
      0.21460287125915200601, \
      0.21460287125915200601, \
      0.21460287125915200601, \
      0.26967233145831581709, \
      0.06366100187501749774, \
      0.60300566479164918743, \
      0.06366100187501749774, \
      0.60300566479164918743, \
      0.06366100187501749774, \
      0.60300566479164918743, \
      0.06366100187501749774, \
      0.26967233145831581709, \
      0.26967233145831581709, \
      0.06366100187501749774, \
      0.06366100187501749774 ] )

  d = np.array ( [ \
      0.04067395853461119870, \
      0.04067395853461125421, \
      0.04067395853461130972, \
      0.87797812439616573776, \
      0.32233789014227542946, \
      0.32233789014227542946, \
      0.32233789014227542946, \
      0.03298632957317337855, \
      0.21460287125915211703, \
      0.21460287125915211703, \
      0.21460287125915211703, \
      0.35619138622254398197, \
      0.06366100187501749774, \
      0.26967233145831581709, \
      0.26967233145831592811, \
      0.06366100187501749774, \
      0.06366100187501755325, \
      0.26967233145831587260, \
      0.06366100187501755325, \
      0.60300566479164929845, \
      0.60300566479164929845, \
      0.06366100187501755325, \
      0.60300566479164929845, \
      0.06366100187501749774 ] )

  w = np.array ( [ \
      0.01007721105532064301, \
      0.01007721105532064301, \
      0.01007721105532064301, \
      0.01007721105532064301, \
      0.05535718154365472377, \
      0.05535718154365472377, \
      0.05535718154365472377, \
      0.05535718154365472377, \
      0.03992275025816749423, \
      0.03992275025816749423, \
      0.03992275025816749423, \
      0.03992275025816749423, \
      0.04821428571428570953, \
      0.04821428571428570953, \
      0.04821428571428570953, \
      0.04821428571428570953, \
      0.04821428571428570953, \
      0.04821428571428570953, \
      0.04821428571428570953, \
      0.04821428571428570953, \
      0.04821428571428570953, \
      0.04821428571428570953, \
      0.04821428571428570953, \
      0.04821428571428570953 ] )

  return a, b, c, d, w

def rule07 ( ):

#*****************************************************************************80
#
## rule07() returns the rule of precision 7.
#
#  Discussion:
#
#    The data is given for the reference tetrahedron
#    with vertices (0,0,0), (1,0,0), (0,1,0), (0,0,1).
#
#    We suppose we are given a tetrahedron T with vertices A, B, C, D.
#    We call a rule with n points, returning barycentric coordinates
#    a, b, c, d, and weights w.  Then the integral I of f(x,y,z) over T is 
#    approximated by Q as follows:
#
#    (x,y,z) = a(1:n) * A + b(1:n) * B + c(1:n) * C + d(1:n * D
#    Q = area(T) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2023
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
#    a(n), b(n), c(n), d(n): the barycentric coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  a = np.array ( [ \
      0.25000000000000000000, \
      0.31570114977820279423, \
      0.31570114977820279423, \
      0.05289655066539161732, \
      0.31570114977820279423, \
      0.05048982259839635001, \
      0.44951017740160364999, \
      0.05048982259839635001, \
      0.05048982259839635001, \
      0.44951017740160364999, \
      0.44951017740160364999, \
      0.57517163758699996201, \
      0.57517163758699996201, \
      0.18883383102600104220, \
      0.04716070036099789808, \
      0.18883383102600104220, \
      0.18883383102600104220, \
      0.04716070036099789808, \
      0.18883383102600104220, \
      0.18883383102600104220, \
      0.18883383102600104220, \
      0.04716070036099789808, \
      0.57517163758699996201, \
      0.81083024109854862083, \
      0.81083024109854862083, \
      0.02126547254148325461, \
      0.14663881381848492547, \
      0.02126547254148325461, \
      0.02126547254148325461, \
      0.14663881381848492547, \
      0.02126547254148325461, \
      0.02126547254148325461, \
      0.02126547254148325461, \
      0.14663881381848492547, \
      0.81083024109854862083 ] )

  b = np.array ( [ \
      0.25000000000000000000, \
      0.31570114977820279423, \
      0.05289655066539161732, \
      0.31570114977820279423, \
      0.31570114977820279423, \
      0.44951017740160364999, \
      0.05048982259839635001, \
      0.05048982259839635001, \
      0.44951017740160364999, \
      0.05048982259839635001, \
      0.44951017740160364999, \
      0.18883383102600104220, \
      0.18883383102600104220, \
      0.18883383102600104220, \
      0.57517163758699996201, \
      0.04716070036099789808, \
      0.57517163758699996201, \
      0.18883383102600104220, \
      0.04716070036099789808, \
      0.18883383102600104220, \
      0.57517163758699996201, \
      0.18883383102600104220, \
      0.04716070036099789808, \
      0.02126547254148325461, \
      0.02126547254148325461, \
      0.02126547254148325461, \
      0.81083024109854862083, \
      0.14663881381848492547, \
      0.81083024109854862083, \
      0.02126547254148325461, \
      0.14663881381848492547, \
      0.02126547254148325461, \
      0.81083024109854862083, \
      0.02126547254148325461, \
      0.14663881381848492547 ] )

  c = np.array ( [ \
      0.25000000000000000000, \
      0.05289655066539161732, \
      0.31570114977820279423, \
      0.31570114977820279423, \
      0.31570114977820279423, \
      0.44951017740160364999, \
      0.44951017740160364999, \
      0.44951017740160364999, \
      0.05048982259839635001, \
      0.05048982259839635001, \
      0.05048982259839635001, \
      0.04716070036099789808, \
      0.18883383102600104220, \
      0.57517163758699996201, \
      0.18883383102600104220, \
      0.57517163758699996201, \
      0.18883383102600104220, \
      0.57517163758699996201, \
      0.18883383102600104220, \
      0.04716070036099789808, \
      0.04716070036099789808, \
      0.18883383102600104220, \
      0.18883383102600104220, \
      0.14663881381848492547, \
      0.02126547254148325461, \
      0.81083024109854862083, \
      0.02126547254148325461, \
      0.81083024109854862083, \
      0.02126547254148325461, \
      0.81083024109854862083, \
      0.02126547254148325461, \
      0.14663881381848492547, \
      0.14663881381848492547, \
      0.02126547254148325461, \
      0.02126547254148325461 ] )

  d = np.array ( [ \
      0.25000000000000000000, \
      0.31570114977820284974, \
      0.31570114977820290525, \
      0.31570114977820290525, \
      0.05289655066539167283, \
      0.05048982259839635001, \
      0.05048982259839629450, \
      0.44951017740160376102, \
      0.44951017740160364999, \
      0.44951017740160359448, \
      0.05048982259839629450, \
      0.18883383102600109771, \
      0.04716070036099795360, \
      0.04716070036099795360, \
      0.18883383102600104220, \
      0.18883383102600115322, \
      0.04716070036099795360, \
      0.18883383102600104220, \
      0.57517163758700007303, \
      0.57517163758699996201, \
      0.18883383102600109771, \
      0.57517163758699996201, \
      0.18883383102600109771, \
      0.02126547254148319910, \
      0.14663881381848486996, \
      0.14663881381848486996, \
      0.02126547254148325461, \
      0.02126547254148314359, \
      0.14663881381848486996, \
      0.02126547254148325461, \
      0.81083024109854850980, \
      0.81083024109854862083, \
      0.02126547254148319910, \
      0.81083024109854862083, \
      0.02126547254148319910 ] )

  w = np.array ( [ \
      0.09548528946413084584, \
      0.04232958120996702794, \
      0.04232958120996702794, \
      0.04232958120996702794, \
      0.04232958120996702794, \
      0.03189692783285758004, \
      0.03189692783285758004, \
      0.03189692783285758004, \
      0.03189692783285758004, \
      0.03189692783285758004, \
      0.03189692783285758004, \
      0.03720713072833461976, \
      0.03720713072833461976, \
      0.03720713072833461976, \
      0.03720713072833461976, \
      0.03720713072833461976, \
      0.03720713072833461976, \
      0.03720713072833461976, \
      0.03720713072833461976, \
      0.03720713072833461976, \
      0.03720713072833461976, \
      0.03720713072833461976, \
      0.03720713072833461976, \
      0.00811077082990334201, \
      0.00811077082990334201, \
      0.00811077082990334201, \
      0.00811077082990334201, \
      0.00811077082990334201, \
      0.00811077082990334201, \
      0.00811077082990334201, \
      0.00811077082990334201, \
      0.00811077082990334201, \
      0.00811077082990334201, \
      0.00811077082990334201, \
      0.00811077082990334201 ] )

  return a, b, c, d, w

def rule08 ( ):

#*****************************************************************************80
#
## rule08() returns the rule of precision 8.
#
#  Discussion:
#
#    The data is given for the reference tetrahedron
#    with vertices (0,0,0), (1,0,0), (0,1,0), (0,0,1).
#
#    We suppose we are given a tetrahedron T with vertices A, B, C, D.
#    We call a rule with n points, returning barycentric coordinates
#    a, b, c, d, and weights w.  Then the integral I of f(x,y,z) over T is 
#    approximated by Q as follows:
#
#    (x,y,z) = a(1:n) * A + b(1:n) * B + c(1:n) * C + d(1:n * D
#    Q = area(T) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2023
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
#    a(n), b(n), c(n), d(n): the barycentric coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  a = np.array ( [ \
      0.10795272496221086644, \
      0.10795272496221086644, \
      0.67614182511336751169, \
      0.10795272496221086644, \
      0.18510948778258656811, \
      0.18510948778258656811, \
      0.44467153665224029568, \
      0.18510948778258656811, \
      0.04231654368476728267, \
      0.04231654368476728267, \
      0.87305036894569809647, \
      0.04231654368476728267, \
      0.31418170912403897699, \
      0.31418170912403897699, \
      0.05745487262788301353, \
      0.31418170912403897699, \
      0.43559132858383020626, \
      0.06440867141616979374, \
      0.43559132858383020626, \
      0.43559132858383020626, \
      0.06440867141616979374, \
      0.06440867141616979374, \
      0.71746406342630830721, \
      0.71746406342630830721, \
      0.02143393012713057377, \
      0.23966807631943054524, \
      0.02143393012713057377, \
      0.02143393012713057377, \
      0.23966807631943054524, \
      0.02143393012713057377, \
      0.02143393012713057377, \
      0.02143393012713057377, \
      0.23966807631943054524, \
      0.71746406342630830721, \
      0.58379737830214439853, \
      0.58379737830214439853, \
      0.20413933387602911651, \
      0.00792395394579736845, \
      0.20413933387602911651, \
      0.20413933387602911651, \
      0.00792395394579736845, \
      0.20413933387602911651, \
      0.20413933387602911651, \
      0.20413933387602911651, \
      0.00792395394579736845, \
      0.58379737830214439853 ] )

  b = np.array ( [ \
      0.10795272496221086644, \
      0.67614182511336751169, \
      0.10795272496221086644, \
      0.10795272496221086644, \
      0.18510948778258656811, \
      0.44467153665224029568, \
      0.18510948778258656811, \
      0.18510948778258656811, \
      0.04231654368476728267, \
      0.87305036894569809647, \
      0.04231654368476728267, \
      0.04231654368476728267, \
      0.31418170912403897699, \
      0.05745487262788301353, \
      0.31418170912403897699, \
      0.31418170912403897699, \
      0.06440867141616979374, \
      0.43559132858383020626, \
      0.43559132858383020626, \
      0.06440867141616979374, \
      0.43559132858383020626, \
      0.06440867141616979374, \
      0.02143393012713057377, \
      0.02143393012713057377, \
      0.02143393012713057377, \
      0.71746406342630830721, \
      0.23966807631943054524, \
      0.71746406342630830721, \
      0.02143393012713057377, \
      0.23966807631943054524, \
      0.02143393012713057377, \
      0.71746406342630830721, \
      0.02143393012713057377, \
      0.23966807631943054524, \
      0.20413933387602911651, \
      0.20413933387602911651, \
      0.20413933387602911651, \
      0.58379737830214439853, \
      0.00792395394579736845, \
      0.58379737830214439853, \
      0.20413933387602911651, \
      0.00792395394579736845, \
      0.20413933387602911651, \
      0.58379737830214439853, \
      0.20413933387602911651, \
      0.00792395394579736845 ] )

  c = np.array ( [ \
      0.67614182511336751169, \
      0.10795272496221086644, \
      0.10795272496221086644, \
      0.10795272496221086644, \
      0.44467153665224029568, \
      0.18510948778258656811, \
      0.18510948778258656811, \
      0.18510948778258656811, \
      0.87305036894569809647, \
      0.04231654368476728267, \
      0.04231654368476728267, \
      0.04231654368476728267, \
      0.05745487262788301353, \
      0.31418170912403897699, \
      0.31418170912403897699, \
      0.31418170912403897699, \
      0.06440867141616979374, \
      0.06440867141616979374, \
      0.06440867141616979374, \
      0.43559132858383020626, \
      0.43559132858383020626, \
      0.43559132858383020626, \
      0.23966807631943054524, \
      0.02143393012713057377, \
      0.71746406342630830721, \
      0.02143393012713057377, \
      0.71746406342630830721, \
      0.02143393012713057377, \
      0.71746406342630830721, \
      0.02143393012713057377, \
      0.23966807631943054524, \
      0.23966807631943054524, \
      0.02143393012713057377, \
      0.02143393012713057377, \
      0.00792395394579736845, \
      0.20413933387602911651, \
      0.58379737830214439853, \
      0.20413933387602911651, \
      0.58379737830214439853, \
      0.20413933387602911651, \
      0.58379737830214439853, \
      0.20413933387602911651, \
      0.00792395394579736845, \
      0.00792395394579736845, \
      0.20413933387602911651, \
      0.20413933387602911651 ] )

  d = np.array ( [ \
      0.10795272496221075542, \
      0.10795272496221075542, \
      0.10795272496221075542, \
      0.67614182511336740067, \
      0.18510948778258667913, \
      0.18510948778258662362, \
      0.18510948778258662362, \
      0.44467153665224040671, \
      0.04231654368476744921, \
      0.04231654368476739370, \
      0.04231654368476733818, \
      0.87305036894569831851, \
      0.31418170912403903250, \
      0.31418170912403897699, \
      0.31418170912403908801, \
      0.05745487262788306904, \
      0.43559132858383020626, \
      0.43559132858383020626, \
      0.06440867141616979374, \
      0.06440867141616979374, \
      0.06440867141616979374, \
      0.43559132858383020626, \
      0.02143393012713057377, \
      0.23966807631943054524, \
      0.23966807631943054524, \
      0.02143393012713057377, \
      0.02143393012713057377, \
      0.23966807631943054524, \
      0.02143393012713057377, \
      0.71746406342630830721, \
      0.71746406342630830721, \
      0.02143393012713057377, \
      0.71746406342630830721, \
      0.02143393012713057377, \
      0.20413933387602911651, \
      0.00792395394579736845, \
      0.00792395394579736845, \
      0.20413933387602911651, \
      0.20413933387602911651, \
      0.00792395394579736845, \
      0.20413933387602911651, \
      0.58379737830214439853, \
      0.58379737830214439853, \
      0.20413933387602911651, \
      0.58379737830214439853, \
      0.20413933387602911651 ] )

  w = np.array ( [ \
      0.02642665090840883024, \
      0.02642665090840883024, \
      0.02642665090840883024, \
      0.02642665090840883024, \
      0.05203174756373853127, \
      0.05203174756373853127, \
      0.05203174756373853127, \
      0.05203174756373853127, \
      0.00752525615354019892, \
      0.00752525615354019892, \
      0.00752525615354019892, \
      0.00752525615354019892, \
      0.04176378285693489734, \
      0.04176378285693489734, \
      0.04176378285693489734, \
      0.04176378285693489734, \
      0.03628093026130882470, \
      0.03628093026130882470, \
      0.03628093026130882470, \
      0.03628093026130882470, \
      0.03628093026130882470, \
      0.03628093026130882470, \
      0.00715690289084443265, \
      0.00715690289084443265, \
      0.00715690289084443265, \
      0.00715690289084443265, \
      0.00715690289084443265, \
      0.00715690289084443265, \
      0.00715690289084443265, \
      0.00715690289084443265, \
      0.00715690289084443265, \
      0.00715690289084443265, \
      0.00715690289084443265, \
      0.00715690289084443265, \
      0.01545348615096033516, \
      0.01545348615096033516, \
      0.01545348615096033516, \
      0.01545348615096033516, \
      0.01545348615096033516, \
      0.01545348615096033516, \
      0.01545348615096033516, \
      0.01545348615096033516, \
      0.01545348615096033516, \
      0.01545348615096033516, \
      0.01545348615096033516, \
      0.01545348615096033516 ] )

  return a, b, c, d, w

def rule09 ( ):

#*****************************************************************************80
#
## rule09() returns the rule of precision 9.
#
#  Discussion:
#
#    The data is given for the reference tetrahedron
#    with vertices (0,0,0), (1,0,0), (0,1,0), (0,0,1).
#
#    We suppose we are given a tetrahedron T with vertices A, B, C, D.
#    We call a rule with n points, returning barycentric coordinates
#    a, b, c, d, and weights w.  Then the integral I of f(x,y,z) over T is 
#    approximated by Q as follows:
#
#    (x,y,z) = a(1:n) * A + b(1:n) * B + c(1:n) * C + d(1:n * D
#    Q = area(T) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2023
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
#    a(n), b(n), c(n), d(n): the barycentric coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  a = np.array ( [ \
      0.25000000000000000000, \
      0.00000000061981697552, \
      0.00000000061981697552, \
      0.99999999814054896241, \
      0.00000000061981697552, \
      0.16077453539526159743, \
      0.16077453539526159743, \
      0.51767639381421526323, \
      0.16077453539526159743, \
      0.32227652182142096926, \
      0.32227652182142096926, \
      0.03317043453573709222, \
      0.32227652182142096926, \
      0.04510891834541358447, \
      0.04510891834541358447, \
      0.86467324496375930210, \
      0.04510891834541358447, \
      0.11229654600437605216, \
      0.38770345399562394784, \
      0.11229654600437605216, \
      0.11229654600437605216, \
      0.38770345399562394784, \
      0.38770345399562394784, \
      0.00255457923304130974, \
      0.00255457923304130974, \
      0.45887144875245927667, \
      0.07970252326204013693, \
      0.45887144875245927667, \
      0.45887144875245927667, \
      0.07970252326204013693, \
      0.45887144875245927667, \
      0.45887144875245927667, \
      0.45887144875245927667, \
      0.07970252326204013693, \
      0.00255457923304130974, \
      0.71835032644207452712, \
      0.71835032644207452712, \
      0.03377587068533860482, \
      0.21409793218724831876, \
      0.03377587068533860482, \
      0.03377587068533860482, \
      0.21409793218724831876, \
      0.03377587068533860482, \
      0.03377587068533860482, \
      0.03377587068533860482, \
      0.21409793218724831876, \
      0.71835032644207452712, \
      0.03441591057817527943, \
      0.03441591057817527943, \
      0.18364136980992790127, \
      0.59830134980196891803, \
      0.18364136980992790127, \
      0.18364136980992790127, \
      0.59830134980196891803, \
      0.18364136980992790127, \
      0.18364136980992790127, \
      0.18364136980992790127, \
      0.59830134980196891803, \
      0.03441591057817527943 ] )

  b = np.array ( [ \
      0.25000000000000000000, \
      0.00000000061981697552, \
      0.99999999814054896241, \
      0.00000000061981697552, \
      0.00000000061981697552, \
      0.16077453539526159743, \
      0.51767639381421526323, \
      0.16077453539526159743, \
      0.16077453539526159743, \
      0.32227652182142096926, \
      0.03317043453573709222, \
      0.32227652182142096926, \
      0.32227652182142096926, \
      0.04510891834541358447, \
      0.86467324496375930210, \
      0.04510891834541358447, \
      0.04510891834541358447, \
      0.38770345399562394784, \
      0.11229654600437605216, \
      0.11229654600437605216, \
      0.38770345399562394784, \
      0.11229654600437605216, \
      0.38770345399562394784, \
      0.45887144875245927667, \
      0.45887144875245927667, \
      0.45887144875245927667, \
      0.00255457923304130974, \
      0.07970252326204013693, \
      0.00255457923304130974, \
      0.45887144875245927667, \
      0.07970252326204013693, \
      0.45887144875245927667, \
      0.00255457923304130974, \
      0.45887144875245927667, \
      0.07970252326204013693, \
      0.03377587068533860482, \
      0.03377587068533860482, \
      0.03377587068533860482, \
      0.71835032644207452712, \
      0.21409793218724831876, \
      0.71835032644207452712, \
      0.03377587068533860482, \
      0.21409793218724831876, \
      0.03377587068533860482, \
      0.71835032644207452712, \
      0.03377587068533860482, \
      0.21409793218724831876, \
      0.18364136980992790127, \
      0.18364136980992790127, \
      0.18364136980992790127, \
      0.03441591057817527943, \
      0.59830134980196891803, \
      0.03441591057817527943, \
      0.18364136980992790127, \
      0.59830134980196891803, \
      0.18364136980992790127, \
      0.03441591057817527943, \
      0.18364136980992790127, \
      0.59830134980196891803 ] )

  c = np.array ( [ \
      0.25000000000000000000, \
      0.99999999814054896241, \
      0.00000000061981697552, \
      0.00000000061981697552, \
      0.00000000061981697552, \
      0.51767639381421526323, \
      0.16077453539526159743, \
      0.16077453539526159743, \
      0.16077453539526159743, \
      0.03317043453573709222, \
      0.32227652182142096926, \
      0.32227652182142096926, \
      0.32227652182142096926, \
      0.86467324496375930210, \
      0.04510891834541358447, \
      0.04510891834541358447, \
      0.04510891834541358447, \
      0.38770345399562394784, \
      0.38770345399562394784, \
      0.38770345399562394784, \
      0.11229654600437605216, \
      0.11229654600437605216, \
      0.11229654600437605216, \
      0.07970252326204013693, \
      0.45887144875245927667, \
      0.00255457923304130974, \
      0.45887144875245927667, \
      0.00255457923304130974, \
      0.45887144875245927667, \
      0.00255457923304130974, \
      0.45887144875245927667, \
      0.07970252326204013693, \
      0.07970252326204013693, \
      0.45887144875245927667, \
      0.45887144875245927667, \
      0.21409793218724831876, \
      0.03377587068533860482, \
      0.71835032644207452712, \
      0.03377587068533860482, \
      0.71835032644207452712, \
      0.03377587068533860482, \
      0.71835032644207452712, \
      0.03377587068533860482, \
      0.21409793218724831876, \
      0.21409793218724831876, \
      0.03377587068533860482, \
      0.03377587068533860482, \
      0.59830134980196891803, \
      0.18364136980992790127, \
      0.03441591057817527943, \
      0.18364136980992790127, \
      0.03441591057817527943, \
      0.18364136980992790127, \
      0.03441591057817527943, \
      0.18364136980992790127, \
      0.59830134980196891803, \
      0.59830134980196891803, \
      0.18364136980992790127, \
      0.18364136980992790127 ] )

  d = np.array ( [ \
      0.25000000000000000000, \
      0.00000000061981708654, \
      0.00000000061981708654, \
      0.00000000061981708654, \
      0.99999999814054907343, \
      0.16077453539526143089, \
      0.16077453539526148640, \
      0.16077453539526154191, \
      0.51767639381421504119, \
      0.32227652182142096926, \
      0.32227652182142096926, \
      0.32227652182142096926, \
      0.03317043453573709222, \
      0.04510891834541341794, \
      0.04510891834541347345, \
      0.04510891834541352896, \
      0.86467324496375908005, \
      0.11229654600437599665, \
      0.11229654600437605216, \
      0.38770345399562383681, \
      0.38770345399562389233, \
      0.38770345399562394784, \
      0.11229654600437610767, \
      0.45887144875245938769, \
      0.07970252326204024795, \
      0.07970252326204019244, \
      0.45887144875245938769, \
      0.45887144875245933218, \
      0.07970252326204024795, \
      0.45887144875245933218, \
      0.00255457923304136525, \
      0.00255457923304136525, \
      0.45887144875245938769, \
      0.00255457923304136525, \
      0.45887144875245938769, \
      0.03377587068533854930, \
      0.21409793218724826325, \
      0.21409793218724826325, \
      0.03377587068533860482, \
      0.03377587068533860482, \
      0.21409793218724826325, \
      0.03377587068533860482, \
      0.71835032644207452712, \
      0.71835032644207452712, \
      0.03377587068533854930, \
      0.71835032644207452712, \
      0.03377587068533854930, \
      0.18364136980992795678, \
      0.59830134980196891803, \
      0.59830134980196880701, \
      0.18364136980992790127, \
      0.18364136980992784576, \
      0.59830134980196891803, \
      0.18364136980992790127, \
      0.03441591057817522392, \
      0.03441591057817516841, \
      0.18364136980992784576, \
      0.03441591057817527943, \
      0.18364136980992790127 ] )

  w = np.array ( [ \
      0.05801054891248025314, \
      0.00006431928175925639, \
      0.00006431928175925639, \
      0.00006431928175925639, \
      0.00006431928175925639, \
      0.02317333846242545722, \
      0.02317333846242545722, \
      0.02317333846242545722, \
      0.02317333846242545722, \
      0.02956291233542928526, \
      0.02956291233542928526, \
      0.02956291233542928526, \
      0.02956291233542928526, \
      0.00806397997961618221, \
      0.00806397997961618221, \
      0.00806397997961618221, \
      0.00806397997961618221, \
      0.03813408010370246404, \
      0.03813408010370246404, \
      0.03813408010370246404, \
      0.03813408010370246404, \
      0.03813408010370246404, \
      0.03813408010370246404, \
      0.00838442219829855194, \
      0.00838442219829855194, \
      0.00838442219829855194, \
      0.00838442219829855194, \
      0.00838442219829855194, \
      0.00838442219829855194, \
      0.00838442219829855194, \
      0.00838442219829855194, \
      0.00838442219829855194, \
      0.00838442219829855194, \
      0.00838442219829855194, \
      0.00838442219829855194, \
      0.01023455935274532845, \
      0.01023455935274532845, \
      0.01023455935274532845, \
      0.01023455935274532845, \
      0.01023455935274532845, \
      0.01023455935274532845, \
      0.01023455935274532845, \
      0.01023455935274532845, \
      0.01023455935274532845, \
      0.01023455935274532845, \
      0.01023455935274532845, \
      0.01023455935274532845, \
      0.02052491596798813878, \
      0.02052491596798813878, \
      0.02052491596798813878, \
      0.02052491596798813878, \
      0.02052491596798813878, \
      0.02052491596798813878, \
      0.02052491596798813878, \
      0.02052491596798813878, \
      0.02052491596798813878, \
      0.02052491596798813878, \
      0.02052491596798813878, \
      0.02052491596798813878 ] )

  return a, b, c, d, w

def rule10 ( ):

#*****************************************************************************80
#
## rule10() returns the rule of precision 10.
#
#  Discussion:
#
#    The data is given for the reference tetrahedron
#    with vertices (0,0,0), (1,0,0), (0,1,0), (0,0,1).
#
#    We suppose we are given a tetrahedron T with vertices A, B, C, D.
#    We call a rule with n points, returning barycentric coordinates
#    a, b, c, d, and weights w.  Then the integral I of f(x,y,z) over T is 
#    approximated by Q as follows:
#
#    (x,y,z) = a(1:n) * A + b(1:n) * B + c(1:n) * C + d(1:n * D
#    Q = area(T) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2023
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
#    a(n), b(n), c(n), d(n): the barycentric coordinates of quadrature points.
#
#    w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  a = np.array ( [ \
      0.25000000000000000000, \
      0.31225006869518867614, \
      0.31225006869518867614, \
      0.06324979391443408261, \
      0.31225006869518867614, \
      0.11430965385734614959, \
      0.11430965385734614959, \
      0.65707103842796155124, \
      0.11430965385734614959, \
      0.16548602561961106572, \
      0.16548602561961106572, \
      0.41043073921896550127, \
      0.01365249594245798725, \
      0.41043073921896550127, \
      0.41043073921896550127, \
      0.01365249594245798725, \
      0.41043073921896550127, \
      0.41043073921896550127, \
      0.41043073921896550127, \
      0.01365249594245798725, \
      0.16548602561961106572, \
      0.94298876734520487020, \
      0.94298876734520487020, \
      0.00613800882479076382, \
      0.04473521500521365768, \
      0.00613800882479076382, \
      0.00613800882479076382, \
      0.04473521500521365768, \
      0.00613800882479076382, \
      0.00613800882479076382, \
      0.00613800882479076382, \
      0.04473521500521365768, \
      0.94298876734520487020, \
      0.47719037990428037066, \
      0.47719037990428037066, \
      0.12105018114558940834, \
      0.28070925780454081266, \
      0.12105018114558940834, \
      0.12105018114558940834, \
      0.28070925780454081266, \
      0.12105018114558940834, \
      0.12105018114558940834, \
      0.12105018114558940834, \
      0.28070925780454081266, \
      0.47719037990428037066, \
      0.59425626948000698224, \
      0.59425626948000698224, \
      0.03277946821644267539, \
      0.34018479408710766698, \
      0.03277946821644267539, \
      0.03277946821644267539, \
      0.34018479408710766698, \
      0.03277946821644267539, \
      0.03277946821644267539, \
      0.03277946821644267539, \
      0.34018479408710766698, \
      0.59425626948000698224, \
      0.80117728465834436857, \
      0.80117728465834436857, \
      0.03248528156482305418, \
      0.13385215221200952307, \
      0.03248528156482305418, \
      0.03248528156482305418, \
      0.13385215221200952307, \
      0.03248528156482305418, \
      0.03248528156482305418, \
      0.03248528156482305418, \
      0.13385215221200952307, \
      0.80117728465834436857, \
      0.62807184547536598629, \
      0.62807184547536598629, \
      0.17497934218393901284, \
      0.02196947015675593251, \
      0.17497934218393901284, \
      0.17497934218393901284, \
      0.02196947015675593251, \
      0.17497934218393901284, \
      0.17497934218393901284, \
      0.17497934218393901284, \
      0.02196947015675593251, \
      0.62807184547536598629 ] )

  b = np.array ( [ \
      0.25000000000000000000, \
      0.31225006869518867614, \
      0.06324979391443408261, \
      0.31225006869518867614, \
      0.31225006869518867614, \
      0.11430965385734614959, \
      0.65707103842796155124, \
      0.11430965385734614959, \
      0.11430965385734614959, \
      0.41043073921896550127, \
      0.41043073921896550127, \
      0.41043073921896550127, \
      0.16548602561961106572, \
      0.01365249594245798725, \
      0.16548602561961106572, \
      0.41043073921896550127, \
      0.01365249594245798725, \
      0.41043073921896550127, \
      0.16548602561961106572, \
      0.41043073921896550127, \
      0.01365249594245798725, \
      0.00613800882479076382, \
      0.00613800882479076382, \
      0.00613800882479076382, \
      0.94298876734520487020, \
      0.04473521500521365768, \
      0.94298876734520487020, \
      0.00613800882479076382, \
      0.04473521500521365768, \
      0.00613800882479076382, \
      0.94298876734520487020, \
      0.00613800882479076382, \
      0.04473521500521365768, \
      0.12105018114558940834, \
      0.12105018114558940834, \
      0.12105018114558940834, \
      0.47719037990428037066, \
      0.28070925780454081266, \
      0.47719037990428037066, \
      0.12105018114558940834, \
      0.28070925780454081266, \
      0.12105018114558940834, \
      0.47719037990428037066, \
      0.12105018114558940834, \
      0.28070925780454081266, \
      0.03277946821644267539, \
      0.03277946821644267539, \
      0.03277946821644267539, \
      0.59425626948000698224, \
      0.34018479408710766698, \
      0.59425626948000698224, \
      0.03277946821644267539, \
      0.34018479408710766698, \
      0.03277946821644267539, \
      0.59425626948000698224, \
      0.03277946821644267539, \
      0.34018479408710766698, \
      0.03248528156482305418, \
      0.03248528156482305418, \
      0.03248528156482305418, \
      0.80117728465834436857, \
      0.13385215221200952307, \
      0.80117728465834436857, \
      0.03248528156482305418, \
      0.13385215221200952307, \
      0.03248528156482305418, \
      0.80117728465834436857, \
      0.03248528156482305418, \
      0.13385215221200952307, \
      0.17497934218393901284, \
      0.17497934218393901284, \
      0.17497934218393901284, \
      0.62807184547536598629, \
      0.02196947015675593251, \
      0.62807184547536598629, \
      0.17497934218393901284, \
      0.02196947015675593251, \
      0.17497934218393901284, \
      0.62807184547536598629, \
      0.17497934218393901284, \
      0.02196947015675593251 ] )

  c = np.array ( [ \
      0.25000000000000000000, \
      0.06324979391443408261, \
      0.31225006869518867614, \
      0.31225006869518867614, \
      0.31225006869518867614, \
      0.65707103842796155124, \
      0.11430965385734614959, \
      0.11430965385734614959, \
      0.11430965385734614959, \
      0.01365249594245798725, \
      0.41043073921896550127, \
      0.16548602561961106572, \
      0.41043073921896550127, \
      0.16548602561961106572, \
      0.41043073921896550127, \
      0.16548602561961106572, \
      0.41043073921896550127, \
      0.01365249594245798725, \
      0.01365249594245798725, \
      0.41043073921896550127, \
      0.41043073921896550127, \
      0.04473521500521365768, \
      0.00613800882479076382, \
      0.94298876734520487020, \
      0.00613800882479076382, \
      0.94298876734520487020, \
      0.00613800882479076382, \
      0.94298876734520487020, \
      0.00613800882479076382, \
      0.04473521500521365768, \
      0.04473521500521365768, \
      0.00613800882479076382, \
      0.00613800882479076382, \
      0.28070925780454081266, \
      0.12105018114558940834, \
      0.47719037990428037066, \
      0.12105018114558940834, \
      0.47719037990428037066, \
      0.12105018114558940834, \
      0.47719037990428037066, \
      0.12105018114558940834, \
      0.28070925780454081266, \
      0.28070925780454081266, \
      0.12105018114558940834, \
      0.12105018114558940834, \
      0.34018479408710766698, \
      0.03277946821644267539, \
      0.59425626948000698224, \
      0.03277946821644267539, \
      0.59425626948000698224, \
      0.03277946821644267539, \
      0.59425626948000698224, \
      0.03277946821644267539, \
      0.34018479408710766698, \
      0.34018479408710766698, \
      0.03277946821644267539, \
      0.03277946821644267539, \
      0.13385215221200952307, \
      0.03248528156482305418, \
      0.80117728465834436857, \
      0.03248528156482305418, \
      0.80117728465834436857, \
      0.03248528156482305418, \
      0.80117728465834436857, \
      0.03248528156482305418, \
      0.13385215221200952307, \
      0.13385215221200952307, \
      0.03248528156482305418, \
      0.03248528156482305418, \
      0.02196947015675593251, \
      0.17497934218393901284, \
      0.62807184547536598629, \
      0.17497934218393901284, \
      0.62807184547536598629, \
      0.17497934218393901284, \
      0.62807184547536598629, \
      0.17497934218393901284, \
      0.02196947015675593251, \
      0.02196947015675593251, \
      0.17497934218393901284, \
      0.17497934218393901284 ] )

  d = np.array ( [ \
      0.25000000000000000000, \
      0.31225006869518856512, \
      0.31225006869518856512, \
      0.31225006869518856512, \
      0.06324979391443397159, \
      0.11430965385734614959, \
      0.11430965385734614959, \
      0.11430965385734614959, \
      0.65707103842796155124, \
      0.41043073921896539025, \
      0.01365249594245787623, \
      0.01365249594245798725, \
      0.41043073921896539025, \
      0.41043073921896550127, \
      0.01365249594245798725, \
      0.41043073921896550127, \
      0.16548602561961106572, \
      0.16548602561961106572, \
      0.41043073921896550127, \
      0.16548602561961106572, \
      0.41043073921896539025, \
      0.00613800882479070831, \
      0.04473521500521360217, \
      0.04473521500521360217, \
      0.00613800882479076382, \
      0.00613800882479065280, \
      0.04473521500521360217, \
      0.00613800882479076382, \
      0.94298876734520475917, \
      0.94298876734520487020, \
      0.00613800882479070831, \
      0.94298876734520487020, \
      0.00613800882479070831, \
      0.12105018114558940834, \
      0.28070925780454081266, \
      0.28070925780454081266, \
      0.12105018114558940834, \
      0.12105018114558940834, \
      0.28070925780454081266, \
      0.12105018114558940834, \
      0.47719037990428037066, \
      0.47719037990428037066, \
      0.12105018114558940834, \
      0.47719037990428037066, \
      0.12105018114558940834, \
      0.03277946821644267539, \
      0.34018479408710766698, \
      0.34018479408710777800, \
      0.03277946821644267539, \
      0.03277946821644273090, \
      0.34018479408710772249, \
      0.03277946821644273090, \
      0.59425626948000709326, \
      0.59425626948000709326, \
      0.03277946821644273090, \
      0.59425626948000709326, \
      0.03277946821644267539, \
      0.03248528156482305418, \
      0.13385215221200952307, \
      0.13385215221200941205, \
      0.03248528156482305418, \
      0.03248528156482299867, \
      0.13385215221200946756, \
      0.03248528156482299867, \
      0.80117728465834425755, \
      0.80117728465834425755, \
      0.03248528156482299867, \
      0.80117728465834425755, \
      0.03248528156482305418, \
      0.17497934218393906836, \
      0.02196947015675598802, \
      0.02196947015675609904, \
      0.17497934218393912387, \
      0.17497934218393917938, \
      0.02196947015675604353, \
      0.17497934218393917938, \
      0.62807184547536620833, \
      0.62807184547536620833, \
      0.17497934218393912387, \
      0.62807184547536620833, \
      0.17497934218393906836 ] )

  w = np.array ( [ \
      0.04739977355602073561, \
      0.02693705999226870401, \
      0.02693705999226870401, \
      0.02693705999226870401, \
      0.02693705999226870401, \
      0.00986915971679338221, \
      0.00986915971679338221, \
      0.00986915971679338221, \
      0.00986915971679338221, \
      0.01139388122019523164, \
      0.01139388122019523164, \
      0.01139388122019523164, \
      0.01139388122019523164, \
      0.01139388122019523164, \
      0.01139388122019523164, \
      0.01139388122019523164, \
      0.01139388122019523164, \
      0.01139388122019523164, \
      0.01139388122019523164, \
      0.01139388122019523164, \
      0.01139388122019523164, \
      0.00036194434433925362, \
      0.00036194434433925362, \
      0.00036194434433925362, \
      0.00036194434433925362, \
      0.00036194434433925362, \
      0.00036194434433925362, \
      0.00036194434433925362, \
      0.00036194434433925362, \
      0.00036194434433925362, \
      0.00036194434433925362, \
      0.00036194434433925362, \
      0.00036194434433925362, \
      0.02573973198045606883, \
      0.02573973198045606883, \
      0.02573973198045606883, \
      0.02573973198045606883, \
      0.02573973198045606883, \
      0.02573973198045606883, \
      0.02573973198045606883, \
      0.02573973198045606883, \
      0.02573973198045606883, \
      0.02573973198045606883, \
      0.02573973198045606883, \
      0.02573973198045606883, \
      0.01013587167975579274, \
      0.01013587167975579274, \
      0.01013587167975579274, \
      0.01013587167975579274, \
      0.01013587167975579274, \
      0.01013587167975579274, \
      0.01013587167975579274, \
      0.01013587167975579274, \
      0.01013587167975579274, \
      0.01013587167975579274, \
      0.01013587167975579274, \
      0.01013587167975579274, \
      0.00657614727703590383, \
      0.00657614727703590383, \
      0.00657614727703590383, \
      0.00657614727703590383, \
      0.00657614727703590383, \
      0.00657614727703590383, \
      0.00657614727703590383, \
      0.00657614727703590383, \
      0.00657614727703590383, \
      0.00657614727703590383, \
      0.00657614727703590383, \
      0.00657614727703590383, \
      0.01290703579886198944, \
      0.01290703579886198944, \
      0.01290703579886198944, \
      0.01290703579886198944, \
      0.01290703579886198944, \
      0.01290703579886198944, \
      0.01290703579886198944, \
      0.01290703579886198944, \
      0.01290703579886198944, \
      0.01290703579886198944, \
      0.01290703579886198944, \
      0.01290703579886198944 ] )

  return a, b, c, d, w

def tetrahedron_unit_monomial_integral ( e ):

#*****************************************************************************80
#
## tetrahedron_unit_monomial_integral(): integrals in the unit tetrahedron.
#
#  Discussion:
#
#    The monomial is F(X,Y,Z) = X^E(1) * Y^E(2) * Z^E(3).
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
#    integer E(3), the exponents.  
#    Each exponent must be nonnegative.
#
#  Output:
#
#    real integral, the integral.
#
  m = 3

  for i in range ( 0, m ):
    if ( e[i] < 0 ):
      print ( '' )
      print ( 'tetrahedron_unit_monomial_integral(): Fatal error!' )
      print ( '  All exponents must be nonnegative.' )
      raise Exception ( 'tetrahedron01_monomial_integral(): Fatal error!' )

  k = 0
  integral = 1.0

  for i in range ( 0, m ):

    for j in range ( 1, e[i] + 1 ):
      k = k + 1
      integral = integral * float ( j ) / float ( k )

  for i in range ( 0, m ):
    k = k + 1
    integral = integral / float ( k )

  return integral

def tetrahedron_unit_volume ( ):

#*****************************************************************************80
#
## tetrahedron_unit_volume() computes the volume of a unit tetrahedron.
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
#  Output:
#
#    real volume: the volume of the unit tetrahedron.
#
  volume = 1.0 / 6.0

  return volume

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
#    13 April 2023
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

def tetrahedron_witherden_rule ( p ):

#*****************************************************************************80
#
## tetrahedron_witherden_rule() returns a tetrahedron quadrature rule of given precision.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 May 2023
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
#    real a(n), b(n), c(n), d(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  if ( p < 0 ): 
    raise Exception ( 'tetrahedron_witherden_rule(): Input p < 0.' )

  if ( 10 < p ):
    raise Exception ( 'tetrahedron_witherden_rule(): Input 10 < p.' )

  n = rule_order ( p )

  if ( p == 0 ):
    a, b, c, d, w = rule00 ( )
  elif ( p == 1 ):
    a, b, c, d, w = rule01 ( )
  elif ( p == 2 ):
    a, b, c, d, w = rule02 ( )
  elif ( p == 3 ):
    a, b, c, d, w = rule03 ( )
  elif ( p == 4 ):
    a, b, c, d, w = rule04 ( )
  elif ( p == 5 ):
    a, b, c, d, w = rule05 ( )
  elif ( p == 6 ):
    a, b, c, d, w = rule06 ( )
  elif ( p == 7 ):
    a, b, c, d, w = rule07 ( )
  elif ( p == 8 ):
    a, b, c, d, w = rule08 ( )
  elif ( p == 9 ):
    a, b, c, d, w = rule09 ( )
  elif ( p == 10 ):
    a, b, c, d, w = rule10 ( )

  return n, a, b, c, d, w

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
  tetrahedron_witherden_rule_test ( )
  timestamp ( )

