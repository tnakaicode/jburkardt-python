#! /usr/bin/env python3
#
def prism_jaskowiec_rule_test ( ):

#*****************************************************************************80
#
## prism_jaskowiec_rule_test() tests prism_jaskowiec_rule().
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    14 July 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'prism_jaskowiec_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test prism_jaskowiec_rule().' )

  p = 5
  prism_jaskowiec_rule_test01 ( p )

  p = 5
  prism_jaskowiec_rule_test02 ( p )

  p_lo = 0
  p_hi = 20
  prism_jaskowiec_rule_test03 ( p_lo, p_hi )
#
#  Terminate.
#
  print ( '' )
  print ( 'prism_jaskowiec_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def prism_jaskowiec_rule_test01 ( p ):

#*****************************************************************************80
#
## prism_jaskowiec_rule_test01() computes a quadrature rule of precision P.
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
  print ( 'prism_jaskowiec_rule_test01():' )
  print ( '  Quadrature rule for the unit prism,' )
  print ( '  Precision p =', p )
#
#  Retrieve a rule.
#
  n, x, y, z, w = prism_jaskowiec_rule ( p )
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

def prism_jaskowiec_rule_test02 ( p ):

#*****************************************************************************80
#
## prism_jaskowiec_rule_test02() tests a quadrature rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    17 May 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np

  print ( '' )
  print ( 'prism_jaskowiec_rule_test02():' )
  print ( '  Test the precision of a quadrature rule for the unit prism.' )

  dim_num = 3
#
#  Retrieve the rule.
#
  n, x, y, z, w = prism_jaskowiec_rule ( p )
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

      quad = prism_unit_volume ( ) * np.dot ( w, v )

      exact = prism_unit_monomial_integral ( expon )

      quad_error = np.abs ( quad - exact )

      max_error = max ( max_error, quad_error )

      if ( not more ):
        break

    print ( '  %2d  %24.16g' % ( degree, max_error ) )

  return

def prism_jaskowiec_rule_test03 ( p_lo, p_hi ):

#*****************************************************************************80
#
## prism_jaskowiec_rule_test03() tests absolute and relative precision.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    14 July 2023
#
#  Author:
#
#    John Burkardt.
#
#    integer p_lo, p_hi: the lowest and highest rules to check.
#
  import numpy as np

  print ( '' )
  print ( 'prism_jaskowiec_rule_test03():' )
  print ( '  Test the precision of quadrature rules for the unit prism.' )
  print ( '  Check rules of precision p =', p_lo, 'through', p_hi )
  print ( '  for error in approximating integrals of monomials.' )

  dim_num = 3

  print ( '' )
  print ( '              maximum                   maximum' )
  print ( '   p          absolute                  relative' )
  print ( '              error                     error' )
  print ( '' )

  for p in range ( p_lo, p_hi + 1 ):

    n, x, y, z, w = prism_jaskowiec_rule ( p )
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

        quad = prism_unit_volume ( ) * np.dot ( w, v )

        exact = prism_unit_monomial_integral ( expon )

        quad_error = np.abs ( quad - exact )

        max_abs = max ( max_abs, quad_error )

        if ( exact != 0 ):
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

def prism_jaskowiec_rule ( p ):

#*****************************************************************************80
#
## prism_jaskowiec_rule() returns a prism quadrature rule of given precision.
#
#  Discussion:
#
#    The unit prism is defined as:
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
#    17 May 2023
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
#    integer p: the precision, 0 <= p <= 20.
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
 
  if ( 20 < p ):
    raise Exception ( 'prism_jaskowiec_rule(): Input 20 < p.' )

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
  elif ( p == 11 ):
    x, y, z, w = rule11 ( )
  elif ( p == 12 ):
    x, y, z, w = rule12 ( )
  elif ( p == 13 ):
    x, y, z, w = rule13 ( )
  elif ( p == 14 ):
    x, y, z, w = rule14 ( )
  elif ( p == 15 ):
    x, y, z, w = rule15 ( )
  elif ( p == 16 ):
    x, y, z, w = rule16 ( )
  elif ( p == 17 ):
    x, y, z, w = rule17 ( )
  elif ( p == 18 ):
    x, y, z, w = rule18 ( )
  elif ( p == 19 ):
    x, y, z, w = rule19 ( )
  elif ( p == 20 ):
    x, y, z, w = rule20 ( )

  return n, x, y, z, w

def prism_unit_monomial_integral ( expon ):

#*****************************************************************************80
#
## prism_unit_monomial_integral(): monomial integral in a unit prism.
#
#  Discussion:
#
#    This routine returns the integral of
#
#      product ( 1 <= I <= 3 ) X(I)^EXPON(I)
#
#    over the unit prism.
#
#    The unit prism is defined as:
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
  from scipy.special import factorial

  value = factorial ( expon[0] ) \
        * factorial ( expon[1] ) \
        / ( expon[2] + 1 ) \
        / factorial ( expon[0] + expon[1] + 2 )

  return value

def prism_unit_volume ( ):

#*****************************************************************************80
#
## prism_unit_volume() returns the volume of a unit prism.
#
#  Discussion:
#
#    A unit triangular prism has a triangular base in the (x,y) plane,
#    projected vertically one unit in the z direction.  
#
#    The vertices are 
#      (1,0,0), (0,1,0), (0,0,0), 
#      (1,0,1), (0,1,1), (0,0,1), 
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    27 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Output:
#
#    real value: the volume.
#
  value = 0.5

  return value

def rule_order ( p ):

#*****************************************************************************80
#
## rule_order() returns the order of a prism quadrature rule of given precision.
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
#    27 April 2023
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
#    integer p: the precision, 0 <= p <= 20.
#
#  Output:
#
#    integer order: the order of the rule.
#
  import numpy as np

  if ( p < 0 ): 
    raise Exception ( 'rule_order(): Input p < 0.' )

  if ( 20 < p ):
    raise Exception ( 'rule_order(): Input 20 < p.' )

  order_vec = np.array ( [ \
      1, \
      1,   5,   8,  11,  16,  28,  35,  46,  59,  84, \
     99, 136, 162, 194, 238, 287, 338, 396, 420, 518 ] )

  order = order_vec[p]

  return order

def rule00 ( ):

#*****************************************************************************80
#
## rule00() returns the prism rule of precision 0.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333 ] )

  y = np.array ( [ \
          0.3333333333333333 ] )

  z = np.array ( [ \
          0.5000000000000000 ] )

  w = np.array ( [ \
          1.0000000000000000 ] )

  return x, y, z, w

def rule01 ( ):

#*****************************************************************************80
#
## rule01() returns the prism rule of precision 1.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333 ] )

  y = np.array ( [ \
          0.3333333333333333 ] )

  z = np.array ( [ \
          0.5000000000000000 ] )

  w = np.array ( [ \
          1.0000000000000000 ] )

  return x, y, z, w

def rule02 ( ):

#*****************************************************************************80
#
## rule02() returns the prism rule of precision 2.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.1046424703769979, \
          0.1046424703769979, \
          0.7907150592460042 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.1046424703769979, \
          0.7907150592460042, \
          0.1046424703769979 ] )

  z = np.array ( [ \
          0.0784174655667168, \
          0.9215825344332832, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000 ] )

  w = np.array ( [ \
          0.2344355869392759, \
          0.2344355869392759, \
          0.1770429420404827, \
          0.1770429420404827, \
          0.1770429420404827 ] )

  return x, y, z, w

def rule03 ( ):

#*****************************************************************************80
#
## rule03() returns the prism rule of precision 3.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4890588576053607, \
          0.4890588576053607, \
          0.0218822847892786, \
          0.0778317780273062, \
          0.0778317780273062, \
          0.8443364439453875 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4890588576053607, \
          0.0218822847892786, \
          0.4890588576053607, \
          0.0778317780273062, \
          0.8443364439453875, \
          0.0778317780273062 ] )

  z = np.array ( [ \
          0.0192797910055989, \
          0.9807202089944012, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000 ] )

  w = np.array ( [ \
          0.1803034341765672, \
          0.1803034341765672, \
          0.1134313729984015, \
          0.1134313729984015, \
          0.1134313729984015, \
          0.0996996708838870, \
          0.0996996708838870, \
          0.0996996708838870 ] )

  return x, y, z, w

def rule04 ( ):

#*****************************************************************************80
#
## rule04() returns the prism rule of precision 4.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4686558098619952, \
          0.4686558098619952, \
          0.0626883802760096, \
          0.1007404057989106, \
          0.1007404057989106, \
          0.7985191884021787, \
          0.1007404057989106, \
          0.1007404057989106, \
          0.7985191884021787 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4686558098619952, \
          0.0626883802760096, \
          0.4686558098619952, \
          0.1007404057989106, \
          0.7985191884021787, \
          0.1007404057989106, \
          0.1007404057989106, \
          0.7985191884021787, \
          0.1007404057989106 ] )

  z = np.array ( [ \
          0.0665690129954826, \
          0.9334309870045174, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8378199118411298, \
          0.8378199118411298, \
          0.8378199118411298, \
          0.1621800881588701, \
          0.1621800881588701, \
          0.1621800881588701 ] )

  w = np.array ( [ \
          0.1079119748155355, \
          0.1079119748155355, \
          0.1364146126054776, \
          0.1364146126054776, \
          0.1364146126054776, \
          0.0624887020920827, \
          0.0624887020920827, \
          0.0624887020920827, \
          0.0624887020920827, \
          0.0624887020920827, \
          0.0624887020920827 ] )

  return x, y, z, w

def rule05 ( ):

#*****************************************************************************80
#
## rule05() returns the prism rule of precision 5.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.0517646178271648, \
          0.0517646178271648, \
          0.8964707643456705, \
          0.1663967696311171, \
          0.1663967696311171, \
          0.6672064607377658, \
          0.1663967696311171, \
          0.1663967696311171, \
          0.6672064607377658, \
          0.4976649895838920, \
          0.4976649895838920, \
          0.0046700208322159, \
          0.4976649895838920, \
          0.4976649895838920, \
          0.0046700208322159 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.0517646178271648, \
          0.8964707643456705, \
          0.0517646178271648, \
          0.1663967696311171, \
          0.6672064607377658, \
          0.1663967696311171, \
          0.1663967696311171, \
          0.6672064607377658, \
          0.1663967696311171, \
          0.4976649895838920, \
          0.0046700208322159, \
          0.4976649895838920, \
          0.4976649895838920, \
          0.0046700208322159, \
          0.4976649895838920 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9035817431942219, \
          0.9035817431942219, \
          0.9035817431942219, \
          0.0964182568057780, \
          0.0964182568057780, \
          0.0964182568057780, \
          0.3013691627751696, \
          0.3013691627751696, \
          0.3013691627751696, \
          0.6986308372248304, \
          0.6986308372248304, \
          0.6986308372248304 ] )

  w = np.array ( [ \
          0.2071428343483058, \
          0.0380755890309976, \
          0.0380755890309976, \
          0.0380755890309976, \
          0.0763742613922619, \
          0.0763742613922619, \
          0.0763742613922619, \
          0.0763742613922619, \
          0.0763742613922619, \
          0.0763742613922619, \
          0.0367308050341883, \
          0.0367308050341883, \
          0.0367308050341883, \
          0.0367308050341883, \
          0.0367308050341883, \
          0.0367308050341883 ] )

  return x, y, z, w

def rule06 ( ):

#*****************************************************************************80
#
## rule06() returns the prism rule of precision 6.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.0175042446586512, \
          0.0175042446586512, \
          0.9649915106826975, \
          0.1617417813899514, \
          0.1617417813899514, \
          0.6765164372200974, \
          0.4656535513495914, \
          0.4656535513495914, \
          0.0686928973008173, \
          0.4656535513495914, \
          0.4656535513495914, \
          0.0686928973008173, \
          0.0345948698524570, \
          0.2025039451729335, \
          0.0345948698524570, \
          0.7629011849746096, \
          0.2025039451729335, \
          0.7629011849746096, \
          0.0345948698524570, \
          0.2025039451729335, \
          0.0345948698524570, \
          0.7629011849746096, \
          0.2025039451729335, \
          0.7629011849746096 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.0175042446586512, \
          0.9649915106826975, \
          0.0175042446586512, \
          0.1617417813899514, \
          0.6765164372200974, \
          0.1617417813899514, \
          0.4656535513495914, \
          0.0686928973008173, \
          0.4656535513495914, \
          0.4656535513495914, \
          0.0686928973008173, \
          0.4656535513495914, \
          0.2025039451729335, \
          0.0345948698524570, \
          0.7629011849746096, \
          0.0345948698524570, \
          0.7629011849746096, \
          0.2025039451729335, \
          0.2025039451729335, \
          0.0345948698524570, \
          0.7629011849746096, \
          0.0345948698524570, \
          0.7629011849746096, \
          0.2025039451729335 ] )

  z = np.array ( [ \
          0.9925192962207799, \
          0.0074807037792201, \
          0.2480010523941030, \
          0.7519989476058970, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.7405713004233492, \
          0.7405713004233492, \
          0.7405713004233492, \
          0.2594286995766508, \
          0.2594286995766508, \
          0.2594286995766508, \
          0.0952682547954233, \
          0.0952682547954233, \
          0.0952682547954233, \
          0.0952682547954233, \
          0.0952682547954233, \
          0.0952682547954233, \
          0.9047317452045767, \
          0.9047317452045767, \
          0.9047317452045767, \
          0.9047317452045767, \
          0.9047317452045767, \
          0.9047317452045767 ] )

  w = np.array ( [ \
          0.0361446293820950, \
          0.0361446293820950, \
          0.0554469020242208, \
          0.0554469020242208, \
          0.0116429635765844, \
          0.0116429635765844, \
          0.0116429635765844, \
          0.0768806419265571, \
          0.0768806419265571, \
          0.0768806419265571, \
          0.0496268551496232, \
          0.0496268551496232, \
          0.0496268551496232, \
          0.0496268551496232, \
          0.0496268551496232, \
          0.0496268551496232, \
          0.0211237491483504, \
          0.0211237491483504, \
          0.0211237491483504, \
          0.0211237491483504, \
          0.0211237491483504, \
          0.0211237491483504, \
          0.0211237491483504, \
          0.0211237491483504, \
          0.0211237491483504, \
          0.0211237491483504, \
          0.0211237491483504, \
          0.0211237491483504 ] )

  return x, y, z, w

def rule07 ( ):

#*****************************************************************************80
#
## rule07() returns the prism rule of precision 7.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.0083375954660215, \
          0.0083375954660215, \
          0.9833248090679571, \
          0.4815219753291366, \
          0.4815219753291366, \
          0.0369560493417268, \
          0.4815219753291366, \
          0.4815219753291366, \
          0.0369560493417268, \
          0.0954832483714894, \
          0.0954832483714894, \
          0.8090335032570213, \
          0.0954832483714894, \
          0.0954832483714894, \
          0.8090335032570213, \
          0.7429966820728956, \
          0.0121491315983783, \
          0.7429966820728956, \
          0.2448541863287261, \
          0.0121491315983783, \
          0.2448541863287261, \
          0.1529845984247976, \
          0.3051562164322261, \
          0.1529845984247976, \
          0.5418591851429763, \
          0.3051562164322261, \
          0.5418591851429763, \
          0.1529845984247976, \
          0.3051562164322261, \
          0.1529845984247976, \
          0.5418591851429763, \
          0.3051562164322261, \
          0.5418591851429763 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.0083375954660215, \
          0.9833248090679571, \
          0.0083375954660215, \
          0.4815219753291366, \
          0.0369560493417268, \
          0.4815219753291366, \
          0.4815219753291366, \
          0.0369560493417268, \
          0.4815219753291366, \
          0.0954832483714894, \
          0.8090335032570213, \
          0.0954832483714894, \
          0.0954832483714894, \
          0.8090335032570213, \
          0.0954832483714894, \
          0.0121491315983783, \
          0.7429966820728956, \
          0.2448541863287261, \
          0.7429966820728956, \
          0.2448541863287261, \
          0.0121491315983783, \
          0.3051562164322261, \
          0.1529845984247976, \
          0.5418591851429763, \
          0.1529845984247976, \
          0.5418591851429763, \
          0.3051562164322261, \
          0.3051562164322261, \
          0.1529845984247976, \
          0.5418591851429763, \
          0.1529845984247976, \
          0.5418591851429763, \
          0.3051562164322261 ] )

  z = np.array ( [ \
          0.9901140347954458, \
          0.0098859652045542, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0793063228967370, \
          0.0793063228967370, \
          0.0793063228967370, \
          0.9206936771032630, \
          0.9206936771032630, \
          0.9206936771032630, \
          0.1020754547065085, \
          0.1020754547065085, \
          0.1020754547065085, \
          0.8979245452934915, \
          0.8979245452934915, \
          0.8979245452934915, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.7019672802660549, \
          0.7019672802660549, \
          0.7019672802660549, \
          0.7019672802660549, \
          0.7019672802660549, \
          0.7019672802660549, \
          0.2980327197339451, \
          0.2980327197339451, \
          0.2980327197339451, \
          0.2980327197339451, \
          0.2980327197339451, \
          0.2980327197339451 ] )

  w = np.array ( [ \
          0.0284456811126893, \
          0.0284456811126893, \
          0.0061182421730950, \
          0.0061182421730950, \
          0.0061182421730950, \
          0.0215508640862265, \
          0.0215508640862265, \
          0.0215508640862265, \
          0.0215508640862265, \
          0.0215508640862265, \
          0.0215508640862265, \
          0.0291785249020985, \
          0.0291785249020985, \
          0.0291785249020985, \
          0.0291785249020985, \
          0.0291785249020985, \
          0.0291785249020985, \
          0.0255148563351493, \
          0.0255148563351493, \
          0.0255148563351493, \
          0.0255148563351493, \
          0.0255148563351493, \
          0.0255148563351493, \
          0.0389407032762076, \
          0.0389407032762076, \
          0.0389407032762076, \
          0.0389407032762076, \
          0.0389407032762076, \
          0.0389407032762076, \
          0.0389407032762076, \
          0.0389407032762076, \
          0.0389407032762076, \
          0.0389407032762076, \
          0.0389407032762076, \
          0.0389407032762076 ] )

  return x, y, z, w

def rule08 ( ):

#*****************************************************************************80
#
## rule08() returns the prism rule of precision 8.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4600889628137106, \
          0.4600889628137106, \
          0.0798220743725788, \
          0.0534123509369071, \
          0.0534123509369071, \
          0.8931752981261857, \
          0.0472387858397694, \
          0.0472387858397694, \
          0.9055224283204613, \
          0.0472387858397694, \
          0.0472387858397694, \
          0.9055224283204613, \
          0.1740616079243704, \
          0.1740616079243704, \
          0.6518767841512593, \
          0.1740616079243704, \
          0.1740616079243704, \
          0.6518767841512593, \
          0.1597492639425890, \
          0.1597492639425890, \
          0.6805014721148220, \
          0.1597492639425890, \
          0.1597492639425890, \
          0.6805014721148220, \
          0.4585690687909513, \
          0.4585690687909513, \
          0.0828618624180973, \
          0.4585690687909513, \
          0.4585690687909513, \
          0.0828618624180973, \
          0.0085881275077590, \
          0.7285980718010000, \
          0.0085881275077590, \
          0.2628138006912410, \
          0.7285980718010000, \
          0.2628138006912410, \
          0.0085881275077590, \
          0.7285980718010000, \
          0.0085881275077590, \
          0.2628138006912410, \
          0.7285980718010000, \
          0.2628138006912410 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4600889628137106, \
          0.0798220743725788, \
          0.4600889628137106, \
          0.0534123509369071, \
          0.8931752981261857, \
          0.0534123509369071, \
          0.0472387858397694, \
          0.9055224283204613, \
          0.0472387858397694, \
          0.0472387858397694, \
          0.9055224283204613, \
          0.0472387858397694, \
          0.1740616079243704, \
          0.6518767841512593, \
          0.1740616079243704, \
          0.1740616079243704, \
          0.6518767841512593, \
          0.1740616079243704, \
          0.1597492639425890, \
          0.6805014721148220, \
          0.1597492639425890, \
          0.1597492639425890, \
          0.6805014721148220, \
          0.1597492639425890, \
          0.4585690687909513, \
          0.0828618624180973, \
          0.4585690687909513, \
          0.4585690687909513, \
          0.0828618624180973, \
          0.4585690687909513, \
          0.7285980718010000, \
          0.0085881275077590, \
          0.2628138006912410, \
          0.0085881275077590, \
          0.2628138006912410, \
          0.7285980718010000, \
          0.7285980718010000, \
          0.0085881275077590, \
          0.2628138006912410, \
          0.0085881275077590, \
          0.2628138006912410, \
          0.7285980718010000 ] )

  z = np.array ( [ \
          0.6122169330529953, \
          0.3877830669470047, \
          0.1590872792145671, \
          0.8409127207854329, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9144077215293400, \
          0.9144077215293400, \
          0.9144077215293400, \
          0.0855922784706599, \
          0.0855922784706599, \
          0.0855922784706599, \
          0.7030421146772952, \
          0.7030421146772952, \
          0.7030421146772952, \
          0.2969578853227048, \
          0.2969578853227048, \
          0.2969578853227048, \
          0.9829325832703272, \
          0.9829325832703272, \
          0.9829325832703272, \
          0.0170674167296728, \
          0.0170674167296728, \
          0.0170674167296728, \
          0.9380979550001272, \
          0.9380979550001272, \
          0.9380979550001272, \
          0.0619020449998729, \
          0.0619020449998729, \
          0.0619020449998729, \
          0.7886751345948129, \
          0.7886751345948129, \
          0.7886751345948129, \
          0.7886751345948129, \
          0.7886751345948129, \
          0.7886751345948129, \
          0.2113248654051871, \
          0.2113248654051871, \
          0.2113248654051871, \
          0.2113248654051871, \
          0.2113248654051871, \
          0.2113248654051871 ] )

  w = np.array ( [ \
          0.0207349366428555, \
          0.0207349366428555, \
          0.0510894271121815, \
          0.0510894271121815, \
          0.0526997449065072, \
          0.0526997449065072, \
          0.0526997449065072, \
          0.0181522487841497, \
          0.0181522487841497, \
          0.0181522487841497, \
          0.0071453577535386, \
          0.0071453577535386, \
          0.0071453577535386, \
          0.0071453577535386, \
          0.0071453577535386, \
          0.0071453577535386, \
          0.0406292626589893, \
          0.0406292626589893, \
          0.0406292626589893, \
          0.0406292626589893, \
          0.0406292626589893, \
          0.0406292626589893, \
          0.0111430273484653, \
          0.0111430273484653, \
          0.0111430273484653, \
          0.0111430273484653, \
          0.0111430273484653, \
          0.0111430273484653, \
          0.0210865092935865, \
          0.0210865092935865, \
          0.0210865092935865, \
          0.0210865092935865, \
          0.0210865092935865, \
          0.0210865092935865, \
          0.0136475290908731, \
          0.0136475290908731, \
          0.0136475290908731, \
          0.0136475290908731, \
          0.0136475290908731, \
          0.0136475290908731, \
          0.0136475290908731, \
          0.0136475290908731, \
          0.0136475290908731, \
          0.0136475290908731, \
          0.0136475290908731, \
          0.0136475290908731 ] )

  return x, y, z, w

def rule09 ( ):

#*****************************************************************************80
#
## rule09() returns the prism rule of precision 9.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4938630638969568, \
          0.4938630638969568, \
          0.0122738722060863, \
          0.2362540169543293, \
          0.2362540169543293, \
          0.5274919660913414, \
          0.2362540169543293, \
          0.2362540169543293, \
          0.5274919660913414, \
          0.0722383394163824, \
          0.0722383394163824, \
          0.8555233211672353, \
          0.0722383394163824, \
          0.0722383394163824, \
          0.8555233211672353, \
          0.4383137607101617, \
          0.4383137607101617, \
          0.1233724785796766, \
          0.4383137607101617, \
          0.4383137607101617, \
          0.1233724785796766, \
          0.0364340164940779, \
          0.0364340164940779, \
          0.9271319670118442, \
          0.0364340164940779, \
          0.0364340164940779, \
          0.9271319670118442, \
          0.4828779929693860, \
          0.4828779929693860, \
          0.0342440140612279, \
          0.4828779929693860, \
          0.4828779929693860, \
          0.0342440140612279, \
          0.1628698857202373, \
          0.1628698857202373, \
          0.6742602285595254, \
          0.1628698857202373, \
          0.1628698857202373, \
          0.6742602285595254, \
          0.8213377527237301, \
          0.1626087609745086, \
          0.8213377527237301, \
          0.0160534863017613, \
          0.1626087609745086, \
          0.0160534863017613, \
          0.0424944495063928, \
          0.2561926710584905, \
          0.0424944495063928, \
          0.7013128794351167, \
          0.2561926710584905, \
          0.7013128794351167, \
          0.0424944495063928, \
          0.2561926710584905, \
          0.0424944495063928, \
          0.7013128794351167, \
          0.2561926710584905, \
          0.7013128794351167 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4938630638969568, \
          0.0122738722060863, \
          0.4938630638969568, \
          0.2362540169543293, \
          0.5274919660913414, \
          0.2362540169543293, \
          0.2362540169543293, \
          0.5274919660913414, \
          0.2362540169543293, \
          0.0722383394163824, \
          0.8555233211672353, \
          0.0722383394163824, \
          0.0722383394163824, \
          0.8555233211672353, \
          0.0722383394163824, \
          0.4383137607101617, \
          0.1233724785796766, \
          0.4383137607101617, \
          0.4383137607101617, \
          0.1233724785796766, \
          0.4383137607101617, \
          0.0364340164940779, \
          0.9271319670118442, \
          0.0364340164940779, \
          0.0364340164940779, \
          0.9271319670118442, \
          0.0364340164940779, \
          0.4828779929693860, \
          0.0342440140612279, \
          0.4828779929693860, \
          0.4828779929693860, \
          0.0342440140612279, \
          0.4828779929693860, \
          0.1628698857202373, \
          0.6742602285595254, \
          0.1628698857202373, \
          0.1628698857202373, \
          0.6742602285595254, \
          0.1628698857202373, \
          0.1626087609745086, \
          0.8213377527237301, \
          0.0160534863017613, \
          0.8213377527237301, \
          0.0160534863017613, \
          0.1626087609745086, \
          0.2561926710584905, \
          0.0424944495063928, \
          0.7013128794351167, \
          0.0424944495063928, \
          0.7013128794351167, \
          0.2561926710584905, \
          0.2561926710584905, \
          0.0424944495063928, \
          0.7013128794351167, \
          0.0424944495063928, \
          0.7013128794351167, \
          0.2561926710584905 ] )

  z = np.array ( [ \
          0.3624907904961116, \
          0.6375092095038883, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9356193788144789, \
          0.9356193788144789, \
          0.9356193788144789, \
          0.0643806211855212, \
          0.0643806211855212, \
          0.0643806211855212, \
          0.9775968701180802, \
          0.9775968701180802, \
          0.9775968701180802, \
          0.0224031298819198, \
          0.0224031298819198, \
          0.0224031298819198, \
          0.7182058908565040, \
          0.7182058908565040, \
          0.7182058908565040, \
          0.2817941091434960, \
          0.2817941091434960, \
          0.2817941091434960, \
          0.7515028180283210, \
          0.7515028180283210, \
          0.7515028180283210, \
          0.2484971819716791, \
          0.2484971819716791, \
          0.2484971819716791, \
          0.0091271384992068, \
          0.0091271384992068, \
          0.0091271384992068, \
          0.9908728615007932, \
          0.9908728615007932, \
          0.9908728615007932, \
          0.4125665631901645, \
          0.4125665631901645, \
          0.4125665631901645, \
          0.5874334368098355, \
          0.5874334368098355, \
          0.5874334368098355, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8418079279883068, \
          0.8418079279883068, \
          0.8418079279883068, \
          0.8418079279883068, \
          0.8418079279883068, \
          0.8418079279883068, \
          0.1581920720116932, \
          0.1581920720116932, \
          0.1581920720116932, \
          0.1581920720116932, \
          0.1581920720116932, \
          0.1581920720116932 ] )

  w = np.array ( [ \
          0.0342834712909237, \
          0.0342834712909237, \
          0.0163927977044536, \
          0.0163927977044536, \
          0.0163927977044536, \
          0.0234717806987032, \
          0.0234717806987032, \
          0.0234717806987032, \
          0.0234717806987032, \
          0.0234717806987032, \
          0.0234717806987032, \
          0.0057618481582789, \
          0.0057618481582789, \
          0.0057618481582789, \
          0.0057618481582789, \
          0.0057618481582789, \
          0.0057618481582789, \
          0.0349247930577802, \
          0.0349247930577802, \
          0.0349247930577802, \
          0.0349247930577802, \
          0.0349247930577802, \
          0.0349247930577802, \
          0.0073738996232123, \
          0.0073738996232123, \
          0.0073738996232123, \
          0.0073738996232123, \
          0.0073738996232123, \
          0.0073738996232123, \
          0.0057224608464489, \
          0.0057224608464489, \
          0.0057224608464489, \
          0.0057224608464489, \
          0.0057224608464489, \
          0.0057224608464489, \
          0.0243387430144453, \
          0.0243387430144453, \
          0.0243387430144453, \
          0.0243387430144453, \
          0.0243387430144453, \
          0.0243387430144453, \
          0.0094129636631352, \
          0.0094129636631352, \
          0.0094129636631352, \
          0.0094129636631352, \
          0.0094129636631352, \
          0.0094129636631352, \
          0.0180179774943973, \
          0.0180179774943973, \
          0.0180179774943973, \
          0.0180179774943973, \
          0.0180179774943973, \
          0.0180179774943973, \
          0.0180179774943973, \
          0.0180179774943973, \
          0.0180179774943973, \
          0.0180179774943973, \
          0.0180179774943973, \
          0.0180179774943973 ] )

  return x, y, z, w

def rule10 ( ):

#*****************************************************************************80
#
## rule10() returns the prism rule of precision 10.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4300104731739727, \
          0.4300104731739727, \
          0.1399790536520547, \
          0.1095696683547513, \
          0.1095696683547513, \
          0.7808606632904974, \
          0.0158148366313868, \
          0.0158148366313868, \
          0.9683703267372263, \
          0.4356018236697312, \
          0.4356018236697312, \
          0.1287963526605377, \
          0.4356018236697312, \
          0.4356018236697312, \
          0.1287963526605377, \
          0.1485976165307029, \
          0.1485976165307029, \
          0.7028047669385943, \
          0.1485976165307029, \
          0.1485976165307029, \
          0.7028047669385943, \
          0.0519664835822357, \
          0.0519664835822357, \
          0.8960670328355285, \
          0.0519664835822357, \
          0.0519664835822357, \
          0.8960670328355285, \
          0.4990219694442680, \
          0.4990219694442680, \
          0.0019560611114641, \
          0.4990219694442680, \
          0.4990219694442680, \
          0.0019560611114641, \
          0.0415525016027702, \
          0.0415525016027702, \
          0.9168949967944596, \
          0.0415525016027702, \
          0.0415525016027702, \
          0.9168949967944596, \
          0.2343945196820784, \
          0.2343945196820784, \
          0.5312109606358433, \
          0.2343945196820784, \
          0.2343945196820784, \
          0.5312109606358433, \
          0.0528115168465621, \
          0.2716521744885937, \
          0.0528115168465621, \
          0.6755363086648442, \
          0.2716521744885937, \
          0.6755363086648442, \
          0.0528115168465621, \
          0.2716521744885937, \
          0.0528115168465621, \
          0.6755363086648442, \
          0.2716521744885937, \
          0.6755363086648442, \
          0.1675738337212976, \
          0.0101912520986929, \
          0.1675738337212976, \
          0.8222349141800095, \
          0.0101912520986929, \
          0.8222349141800095, \
          0.1675738337212976, \
          0.0101912520986929, \
          0.1675738337212976, \
          0.8222349141800095, \
          0.0101912520986929, \
          0.8222349141800095, \
          0.3291869417398026, \
          0.0509081627669518, \
          0.3291869417398026, \
          0.6199048954932456, \
          0.0509081627669518, \
          0.6199048954932456, \
          0.3291869417398026, \
          0.0509081627669518, \
          0.3291869417398026, \
          0.6199048954932456, \
          0.0509081627669518, \
          0.6199048954932456 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4300104731739727, \
          0.1399790536520547, \
          0.4300104731739727, \
          0.1095696683547513, \
          0.7808606632904974, \
          0.1095696683547513, \
          0.0158148366313868, \
          0.9683703267372263, \
          0.0158148366313868, \
          0.4356018236697312, \
          0.1287963526605377, \
          0.4356018236697312, \
          0.4356018236697312, \
          0.1287963526605377, \
          0.4356018236697312, \
          0.1485976165307029, \
          0.7028047669385943, \
          0.1485976165307029, \
          0.1485976165307029, \
          0.7028047669385943, \
          0.1485976165307029, \
          0.0519664835822357, \
          0.8960670328355285, \
          0.0519664835822357, \
          0.0519664835822357, \
          0.8960670328355285, \
          0.0519664835822357, \
          0.4990219694442680, \
          0.0019560611114641, \
          0.4990219694442680, \
          0.4990219694442680, \
          0.0019560611114641, \
          0.4990219694442680, \
          0.0415525016027702, \
          0.9168949967944596, \
          0.0415525016027702, \
          0.0415525016027702, \
          0.9168949967944596, \
          0.0415525016027702, \
          0.2343945196820784, \
          0.5312109606358433, \
          0.2343945196820784, \
          0.2343945196820784, \
          0.5312109606358433, \
          0.2343945196820784, \
          0.2716521744885937, \
          0.0528115168465621, \
          0.6755363086648442, \
          0.0528115168465621, \
          0.6755363086648442, \
          0.2716521744885937, \
          0.2716521744885937, \
          0.0528115168465621, \
          0.6755363086648442, \
          0.0528115168465621, \
          0.6755363086648442, \
          0.2716521744885937, \
          0.0101912520986929, \
          0.1675738337212976, \
          0.8222349141800095, \
          0.1675738337212976, \
          0.8222349141800095, \
          0.0101912520986929, \
          0.0101912520986929, \
          0.1675738337212976, \
          0.8222349141800095, \
          0.1675738337212976, \
          0.8222349141800095, \
          0.0101912520986929, \
          0.0509081627669518, \
          0.3291869417398026, \
          0.6199048954932456, \
          0.3291869417398026, \
          0.6199048954932456, \
          0.0509081627669518, \
          0.0509081627669518, \
          0.3291869417398026, \
          0.6199048954932456, \
          0.3291869417398026, \
          0.6199048954932456, \
          0.0509081627669518 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.9825433408084738, \
          0.0174566591915262, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8914517952143866, \
          0.8914517952143866, \
          0.8914517952143866, \
          0.1085482047856134, \
          0.1085482047856134, \
          0.1085482047856134, \
          0.8836628766030707, \
          0.8836628766030707, \
          0.8836628766030707, \
          0.1163371233969292, \
          0.1163371233969292, \
          0.1163371233969292, \
          0.7446456974623019, \
          0.7446456974623019, \
          0.7446456974623019, \
          0.2553543025376981, \
          0.2553543025376981, \
          0.2553543025376981, \
          0.8458358146384862, \
          0.8458358146384862, \
          0.8458358146384862, \
          0.1541641853615138, \
          0.1541641853615138, \
          0.1541641853615138, \
          0.9455005421560339, \
          0.9455005421560339, \
          0.9455005421560339, \
          0.0544994578439661, \
          0.0544994578439661, \
          0.0544994578439661, \
          0.7325671383641421, \
          0.7325671383641421, \
          0.7325671383641421, \
          0.2674328616358579, \
          0.2674328616358579, \
          0.2674328616358579, \
          0.9783107845287782, \
          0.9783107845287782, \
          0.9783107845287782, \
          0.9783107845287782, \
          0.9783107845287782, \
          0.9783107845287782, \
          0.0216892154712218, \
          0.0216892154712218, \
          0.0216892154712218, \
          0.0216892154712218, \
          0.0216892154712218, \
          0.0216892154712218, \
          0.7695898729425880, \
          0.7695898729425880, \
          0.7695898729425880, \
          0.7695898729425880, \
          0.7695898729425880, \
          0.7695898729425880, \
          0.2304101270574120, \
          0.2304101270574120, \
          0.2304101270574120, \
          0.2304101270574120, \
          0.2304101270574120, \
          0.2304101270574120, \
          0.3678576424324543, \
          0.3678576424324543, \
          0.3678576424324543, \
          0.3678576424324543, \
          0.3678576424324543, \
          0.3678576424324543, \
          0.6321423575675457, \
          0.6321423575675457, \
          0.6321423575675457, \
          0.6321423575675457, \
          0.6321423575675457, \
          0.6321423575675457 ] )

  w = np.array ( [ \
          0.0321960882383680, \
          0.0132395953233874, \
          0.0132395953233874, \
          0.0166307172641394, \
          0.0166307172641394, \
          0.0166307172641394, \
          0.0223711737567938, \
          0.0223711737567938, \
          0.0223711737567938, \
          0.0029651442680284, \
          0.0029651442680284, \
          0.0029651442680284, \
          0.0204122071267436, \
          0.0204122071267436, \
          0.0204122071267436, \
          0.0204122071267436, \
          0.0204122071267436, \
          0.0204122071267436, \
          0.0141443496976585, \
          0.0141443496976585, \
          0.0141443496976585, \
          0.0141443496976585, \
          0.0141443496976585, \
          0.0141443496976585, \
          0.0035457088242710, \
          0.0035457088242710, \
          0.0035457088242710, \
          0.0035457088242710, \
          0.0035457088242710, \
          0.0035457088242710, \
          0.0060580804829928, \
          0.0060580804829928, \
          0.0060580804829928, \
          0.0060580804829928, \
          0.0060580804829928, \
          0.0060580804829928, \
          0.0035558880399586, \
          0.0035558880399586, \
          0.0035558880399586, \
          0.0035558880399586, \
          0.0035558880399586, \
          0.0035558880399586, \
          0.0303810246652175, \
          0.0303810246652175, \
          0.0303810246652175, \
          0.0303810246652175, \
          0.0303810246652175, \
          0.0303810246652175, \
          0.0062118567570921, \
          0.0062118567570921, \
          0.0062118567570921, \
          0.0062118567570921, \
          0.0062118567570921, \
          0.0062118567570921, \
          0.0062118567570921, \
          0.0062118567570921, \
          0.0062118567570921, \
          0.0062118567570921, \
          0.0062118567570921, \
          0.0062118567570921, \
          0.0066184191661461, \
          0.0066184191661461, \
          0.0066184191661461, \
          0.0066184191661461, \
          0.0066184191661461, \
          0.0066184191661461, \
          0.0066184191661461, \
          0.0066184191661461, \
          0.0066184191661461, \
          0.0066184191661461, \
          0.0066184191661461, \
          0.0066184191661461, \
          0.0160730625956718, \
          0.0160730625956718, \
          0.0160730625956718, \
          0.0160730625956718, \
          0.0160730625956718, \
          0.0160730625956718, \
          0.0160730625956718, \
          0.0160730625956718, \
          0.0160730625956718, \
          0.0160730625956718, \
          0.0160730625956718, \
          0.0160730625956718 ] )

  return x, y, z, w

def rule11 ( ):

#*****************************************************************************80
#
## rule11() returns the prism rule of precision 11.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4269221881685347, \
          0.4269221881685347, \
          0.1461556236629306, \
          0.4396327659106838, \
          0.4396327659106838, \
          0.1207344681786323, \
          0.4396327659106838, \
          0.4396327659106838, \
          0.1207344681786323, \
          0.2009128761138035, \
          0.2009128761138035, \
          0.5981742477723929, \
          0.2009128761138035, \
          0.2009128761138035, \
          0.5981742477723929, \
          0.0215850980431769, \
          0.0215850980431769, \
          0.9568298039136461, \
          0.0215850980431769, \
          0.0215850980431769, \
          0.9568298039136461, \
          0.4941546402080231, \
          0.4941546402080231, \
          0.0116907195839538, \
          0.4941546402080231, \
          0.4941546402080231, \
          0.0116907195839538, \
          0.0599602772654436, \
          0.0599602772654436, \
          0.8800794454691128, \
          0.0599602772654436, \
          0.0599602772654436, \
          0.8800794454691128, \
          0.2328102236807494, \
          0.2328102236807494, \
          0.5343795526385012, \
          0.2328102236807494, \
          0.2328102236807494, \
          0.5343795526385012, \
          0.1213201391549184, \
          0.1213201391549184, \
          0.7573597216901632, \
          0.1213201391549184, \
          0.1213201391549184, \
          0.7573597216901632, \
          0.4987543911906001, \
          0.4987543911906001, \
          0.0024912176187997, \
          0.4987543911906001, \
          0.4987543911906001, \
          0.0024912176187997, \
          0.1046140524481813, \
          0.0165184963342511, \
          0.1046140524481813, \
          0.8788674512175675, \
          0.0165184963342511, \
          0.8788674512175675, \
          0.0719632569755848, \
          0.2979854667459965, \
          0.0719632569755848, \
          0.6300512762784186, \
          0.2979854667459965, \
          0.6300512762784186, \
          0.0719632569755848, \
          0.2979854667459965, \
          0.0719632569755848, \
          0.6300512762784186, \
          0.2979854667459965, \
          0.6300512762784186, \
          0.1998026706474004, \
          0.0172094825510263, \
          0.1998026706474004, \
          0.7829878468015733, \
          0.0172094825510263, \
          0.7829878468015733, \
          0.1998026706474004, \
          0.0172094825510263, \
          0.1998026706474004, \
          0.7829878468015733, \
          0.0172094825510263, \
          0.7829878468015733, \
          0.3197359768880742, \
          0.0462852386525127, \
          0.3197359768880742, \
          0.6339787844594131, \
          0.0462852386525127, \
          0.6339787844594131, \
          0.3197359768880742, \
          0.0462852386525127, \
          0.3197359768880742, \
          0.6339787844594131, \
          0.0462852386525127, \
          0.6339787844594131 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4269221881685347, \
          0.1461556236629306, \
          0.4269221881685347, \
          0.4396327659106838, \
          0.1207344681786323, \
          0.4396327659106838, \
          0.4396327659106838, \
          0.1207344681786323, \
          0.4396327659106838, \
          0.2009128761138035, \
          0.5981742477723929, \
          0.2009128761138035, \
          0.2009128761138035, \
          0.5981742477723929, \
          0.2009128761138035, \
          0.0215850980431769, \
          0.9568298039136461, \
          0.0215850980431769, \
          0.0215850980431769, \
          0.9568298039136461, \
          0.0215850980431769, \
          0.4941546402080231, \
          0.0116907195839538, \
          0.4941546402080231, \
          0.4941546402080231, \
          0.0116907195839538, \
          0.4941546402080231, \
          0.0599602772654436, \
          0.8800794454691128, \
          0.0599602772654436, \
          0.0599602772654436, \
          0.8800794454691128, \
          0.0599602772654436, \
          0.2328102236807494, \
          0.5343795526385012, \
          0.2328102236807494, \
          0.2328102236807494, \
          0.5343795526385012, \
          0.2328102236807494, \
          0.1213201391549184, \
          0.7573597216901632, \
          0.1213201391549184, \
          0.1213201391549184, \
          0.7573597216901632, \
          0.1213201391549184, \
          0.4987543911906001, \
          0.0024912176187997, \
          0.4987543911906001, \
          0.4987543911906001, \
          0.0024912176187997, \
          0.4987543911906001, \
          0.0165184963342511, \
          0.1046140524481813, \
          0.8788674512175675, \
          0.1046140524481813, \
          0.8788674512175675, \
          0.0165184963342511, \
          0.2979854667459965, \
          0.0719632569755848, \
          0.6300512762784186, \
          0.0719632569755848, \
          0.6300512762784186, \
          0.2979854667459965, \
          0.2979854667459965, \
          0.0719632569755848, \
          0.6300512762784186, \
          0.0719632569755848, \
          0.6300512762784186, \
          0.2979854667459965, \
          0.0172094825510263, \
          0.1998026706474004, \
          0.7829878468015733, \
          0.1998026706474004, \
          0.7829878468015733, \
          0.0172094825510263, \
          0.0172094825510263, \
          0.1998026706474004, \
          0.7829878468015733, \
          0.1998026706474004, \
          0.7829878468015733, \
          0.0172094825510263, \
          0.0462852386525127, \
          0.3197359768880742, \
          0.6339787844594131, \
          0.3197359768880742, \
          0.6339787844594131, \
          0.0462852386525127, \
          0.0462852386525127, \
          0.3197359768880742, \
          0.6339787844594131, \
          0.3197359768880742, \
          0.6339787844594131, \
          0.0462852386525127 ] )

  z = np.array ( [ \
          0.2225225095750167, \
          0.7774774904249833, \
          0.9852161050240122, \
          0.0147838949759878, \
          0.4588747274117720, \
          0.5411252725882280, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8379989630425995, \
          0.8379989630425995, \
          0.8379989630425995, \
          0.1620010369574005, \
          0.1620010369574005, \
          0.1620010369574005, \
          0.9180267718000730, \
          0.9180267718000730, \
          0.9180267718000730, \
          0.0819732281999270, \
          0.0819732281999270, \
          0.0819732281999270, \
          0.7930952762440336, \
          0.7930952762440336, \
          0.7930952762440336, \
          0.2069047237559664, \
          0.2069047237559664, \
          0.2069047237559664, \
          0.9873500827745887, \
          0.9873500827745887, \
          0.9873500827745887, \
          0.0126499172254113, \
          0.0126499172254113, \
          0.0126499172254113, \
          0.9725136338749176, \
          0.9725136338749176, \
          0.9725136338749176, \
          0.0274863661250824, \
          0.0274863661250824, \
          0.0274863661250824, \
          0.6317612421960503, \
          0.6317612421960503, \
          0.6317612421960503, \
          0.3682387578039497, \
          0.3682387578039497, \
          0.3682387578039497, \
          0.7219895510260312, \
          0.7219895510260312, \
          0.7219895510260312, \
          0.2780104489739688, \
          0.2780104489739688, \
          0.2780104489739688, \
          0.7875076710403349, \
          0.7875076710403349, \
          0.7875076710403349, \
          0.2124923289596651, \
          0.2124923289596651, \
          0.2124923289596651, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9685666190309952, \
          0.9685666190309952, \
          0.9685666190309952, \
          0.9685666190309952, \
          0.9685666190309952, \
          0.9685666190309952, \
          0.0314333809690049, \
          0.0314333809690049, \
          0.0314333809690049, \
          0.0314333809690049, \
          0.0314333809690049, \
          0.0314333809690049, \
          0.8651322718570146, \
          0.8651322718570146, \
          0.8651322718570146, \
          0.8651322718570146, \
          0.8651322718570146, \
          0.8651322718570146, \
          0.1348677281429854, \
          0.1348677281429854, \
          0.1348677281429854, \
          0.1348677281429854, \
          0.1348677281429854, \
          0.1348677281429854, \
          0.3827016872275200, \
          0.3827016872275200, \
          0.3827016872275200, \
          0.3827016872275200, \
          0.3827016872275200, \
          0.3827016872275200, \
          0.6172983127724800, \
          0.6172983127724800, \
          0.6172983127724800, \
          0.6172983127724800, \
          0.6172983127724800, \
          0.6172983127724800 ] )

  w = np.array ( [ \
          0.0216801440673047, \
          0.0216801440673047, \
          0.0104576079858723, \
          0.0104576079858723, \
          0.0034934625077134, \
          0.0034934625077134, \
          0.0161061041817141, \
          0.0161061041817141, \
          0.0161061041817141, \
          0.0220331028546643, \
          0.0220331028546643, \
          0.0220331028546643, \
          0.0220331028546643, \
          0.0220331028546643, \
          0.0220331028546643, \
          0.0127441869618096, \
          0.0127441869618096, \
          0.0127441869618096, \
          0.0127441869618096, \
          0.0127441869618096, \
          0.0127441869618096, \
          0.0028425261018310, \
          0.0028425261018310, \
          0.0028425261018310, \
          0.0028425261018310, \
          0.0028425261018310, \
          0.0028425261018310, \
          0.0015098577228106, \
          0.0015098577228106, \
          0.0015098577228106, \
          0.0015098577228106, \
          0.0015098577228106, \
          0.0015098577228106, \
          0.0036504270647864, \
          0.0036504270647864, \
          0.0036504270647864, \
          0.0036504270647864, \
          0.0036504270647864, \
          0.0036504270647864, \
          0.0210029067169834, \
          0.0210029067169834, \
          0.0210029067169834, \
          0.0210029067169834, \
          0.0210029067169834, \
          0.0210029067169834, \
          0.0187619585366729, \
          0.0187619585366729, \
          0.0187619585366729, \
          0.0187619585366729, \
          0.0187619585366729, \
          0.0187619585366729, \
          0.0051948191291646, \
          0.0051948191291646, \
          0.0051948191291646, \
          0.0051948191291646, \
          0.0051948191291646, \
          0.0051948191291646, \
          0.0070505879387705, \
          0.0070505879387705, \
          0.0070505879387705, \
          0.0070505879387705, \
          0.0070505879387705, \
          0.0070505879387705, \
          0.0059012699482948, \
          0.0059012699482948, \
          0.0059012699482948, \
          0.0059012699482948, \
          0.0059012699482948, \
          0.0059012699482948, \
          0.0059012699482948, \
          0.0059012699482948, \
          0.0059012699482948, \
          0.0059012699482948, \
          0.0059012699482948, \
          0.0059012699482948, \
          0.0062126654655306, \
          0.0062126654655306, \
          0.0062126654655306, \
          0.0062126654655306, \
          0.0062126654655306, \
          0.0062126654655306, \
          0.0062126654655306, \
          0.0062126654655306, \
          0.0062126654655306, \
          0.0062126654655306, \
          0.0062126654655306, \
          0.0062126654655306, \
          0.0138591496001844, \
          0.0138591496001844, \
          0.0138591496001844, \
          0.0138591496001844, \
          0.0138591496001844, \
          0.0138591496001844, \
          0.0138591496001844, \
          0.0138591496001844, \
          0.0138591496001844, \
          0.0138591496001844, \
          0.0138591496001844, \
          0.0138591496001844 ] )

  return x, y, z, w

def rule12 ( ):

#*****************************************************************************80
#
## rule12() returns the prism rule of precision 12.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.0485337200788840, \
          0.0485337200788840, \
          0.9029325598422321, \
          0.0003340541016131, \
          0.0003340541016131, \
          0.9993318917967738, \
          0.4849074297077183, \
          0.4849074297077183, \
          0.0301851405845634, \
          0.4849074297077183, \
          0.4849074297077183, \
          0.0301851405845634, \
          0.1497566246841529, \
          0.1497566246841529, \
          0.7004867506316943, \
          0.1497566246841529, \
          0.1497566246841529, \
          0.7004867506316943, \
          0.2344536517846724, \
          0.2344536517846724, \
          0.5310926964306552, \
          0.2344536517846724, \
          0.2344536517846724, \
          0.5310926964306552, \
          0.4409030162469282, \
          0.4409030162469282, \
          0.1181939675061436, \
          0.4409030162469282, \
          0.4409030162469282, \
          0.1181939675061436, \
          0.4870412467653055, \
          0.4870412467653055, \
          0.0259175064693890, \
          0.4870412467653055, \
          0.4870412467653055, \
          0.0259175064693890, \
          0.0248638193002129, \
          0.0248638193002129, \
          0.9502723613995742, \
          0.0248638193002129, \
          0.0248638193002129, \
          0.9502723613995742, \
          0.1118542147928236, \
          0.1118542147928236, \
          0.7762915704143528, \
          0.1118542147928236, \
          0.1118542147928236, \
          0.7762915704143528, \
          0.1207867185816364, \
          0.7097236881695401, \
          0.1207867185816364, \
          0.1694895932488235, \
          0.7097236881695401, \
          0.1694895932488235, \
          0.6481099336610571, \
          0.3419306029008594, \
          0.6481099336610571, \
          0.0099594634380836, \
          0.3419306029008594, \
          0.0099594634380836, \
          0.0200903650277176, \
          0.1335404714654308, \
          0.0200903650277176, \
          0.8463691635068515, \
          0.1335404714654308, \
          0.8463691635068515, \
          0.0200903650277176, \
          0.1335404714654308, \
          0.0200903650277176, \
          0.8463691635068515, \
          0.1335404714654308, \
          0.8463691635068515, \
          0.3214917379706315, \
          0.1648190492804087, \
          0.3214917379706315, \
          0.5136892127489598, \
          0.1648190492804087, \
          0.5136892127489598, \
          0.3214917379706315, \
          0.1648190492804087, \
          0.3214917379706315, \
          0.5136892127489598, \
          0.1648190492804087, \
          0.5136892127489598, \
          0.0689956505491457, \
          0.6636404691861656, \
          0.0689956505491457, \
          0.2673638802646887, \
          0.6636404691861656, \
          0.2673638802646887, \
          0.0689956505491457, \
          0.6636404691861656, \
          0.0689956505491457, \
          0.2673638802646887, \
          0.6636404691861656, \
          0.2673638802646887, \
          0.0199626366433414, \
          0.2615529990296567, \
          0.0199626366433414, \
          0.7184843643270019, \
          0.2615529990296567, \
          0.7184843643270019, \
          0.0199626366433414, \
          0.2615529990296567, \
          0.0199626366433414, \
          0.7184843643270019, \
          0.2615529990296567, \
          0.7184843643270019, \
          0.0900297723891655, \
          0.0155218563345725, \
          0.0900297723891655, \
          0.8944483712762620, \
          0.0155218563345725, \
          0.8944483712762620, \
          0.0900297723891655, \
          0.0155218563345725, \
          0.0900297723891655, \
          0.8944483712762620, \
          0.0155218563345725, \
          0.8944483712762620, \
          0.1172214513692467, \
          0.5641016399337317, \
          0.1172214513692467, \
          0.3186769086970216, \
          0.5641016399337317, \
          0.3186769086970216, \
          0.1172214513692467, \
          0.5641016399337317, \
          0.1172214513692467, \
          0.3186769086970216, \
          0.5641016399337317, \
          0.3186769086970216 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.0485337200788840, \
          0.9029325598422321, \
          0.0485337200788840, \
          0.0003340541016131, \
          0.9993318917967738, \
          0.0003340541016131, \
          0.4849074297077183, \
          0.0301851405845634, \
          0.4849074297077183, \
          0.4849074297077183, \
          0.0301851405845634, \
          0.4849074297077183, \
          0.1497566246841529, \
          0.7004867506316943, \
          0.1497566246841529, \
          0.1497566246841529, \
          0.7004867506316943, \
          0.1497566246841529, \
          0.2344536517846724, \
          0.5310926964306552, \
          0.2344536517846724, \
          0.2344536517846724, \
          0.5310926964306552, \
          0.2344536517846724, \
          0.4409030162469282, \
          0.1181939675061436, \
          0.4409030162469282, \
          0.4409030162469282, \
          0.1181939675061436, \
          0.4409030162469282, \
          0.4870412467653055, \
          0.0259175064693890, \
          0.4870412467653055, \
          0.4870412467653055, \
          0.0259175064693890, \
          0.4870412467653055, \
          0.0248638193002129, \
          0.9502723613995742, \
          0.0248638193002129, \
          0.0248638193002129, \
          0.9502723613995742, \
          0.0248638193002129, \
          0.1118542147928236, \
          0.7762915704143528, \
          0.1118542147928236, \
          0.1118542147928236, \
          0.7762915704143528, \
          0.1118542147928236, \
          0.7097236881695401, \
          0.1207867185816364, \
          0.1694895932488235, \
          0.1207867185816364, \
          0.1694895932488235, \
          0.7097236881695401, \
          0.3419306029008594, \
          0.6481099336610571, \
          0.0099594634380836, \
          0.6481099336610571, \
          0.0099594634380836, \
          0.3419306029008594, \
          0.1335404714654308, \
          0.0200903650277176, \
          0.8463691635068515, \
          0.0200903650277176, \
          0.8463691635068515, \
          0.1335404714654308, \
          0.1335404714654308, \
          0.0200903650277176, \
          0.8463691635068515, \
          0.0200903650277176, \
          0.8463691635068515, \
          0.1335404714654308, \
          0.1648190492804087, \
          0.3214917379706315, \
          0.5136892127489598, \
          0.3214917379706315, \
          0.5136892127489598, \
          0.1648190492804087, \
          0.1648190492804087, \
          0.3214917379706315, \
          0.5136892127489598, \
          0.3214917379706315, \
          0.5136892127489598, \
          0.1648190492804087, \
          0.6636404691861656, \
          0.0689956505491457, \
          0.2673638802646887, \
          0.0689956505491457, \
          0.2673638802646887, \
          0.6636404691861656, \
          0.6636404691861656, \
          0.0689956505491457, \
          0.2673638802646887, \
          0.0689956505491457, \
          0.2673638802646887, \
          0.6636404691861656, \
          0.2615529990296567, \
          0.0199626366433414, \
          0.7184843643270019, \
          0.0199626366433414, \
          0.7184843643270019, \
          0.2615529990296567, \
          0.2615529990296567, \
          0.0199626366433414, \
          0.7184843643270019, \
          0.0199626366433414, \
          0.7184843643270019, \
          0.2615529990296567, \
          0.0155218563345725, \
          0.0900297723891655, \
          0.8944483712762620, \
          0.0900297723891655, \
          0.8944483712762620, \
          0.0155218563345725, \
          0.0155218563345725, \
          0.0900297723891655, \
          0.8944483712762620, \
          0.0900297723891655, \
          0.8944483712762620, \
          0.0155218563345725, \
          0.5641016399337317, \
          0.1172214513692467, \
          0.3186769086970216, \
          0.1172214513692467, \
          0.3186769086970216, \
          0.5641016399337317, \
          0.5641016399337317, \
          0.1172214513692467, \
          0.3186769086970216, \
          0.1172214513692467, \
          0.3186769086970216, \
          0.5641016399337317 ] )

  z = np.array ( [ \
          0.9624802640887508, \
          0.0375197359112492, \
          0.6587282524060957, \
          0.3412717475939043, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.7793516203235177, \
          0.7793516203235177, \
          0.7793516203235177, \
          0.2206483796764823, \
          0.2206483796764823, \
          0.2206483796764823, \
          0.0004872322680031, \
          0.0004872322680031, \
          0.0004872322680031, \
          0.9995127677319969, \
          0.9995127677319969, \
          0.9995127677319969, \
          0.6654124101220354, \
          0.6654124101220354, \
          0.6654124101220354, \
          0.3345875898779646, \
          0.3345875898779646, \
          0.3345875898779646, \
          0.4636840317697777, \
          0.4636840317697777, \
          0.4636840317697777, \
          0.5363159682302223, \
          0.5363159682302223, \
          0.5363159682302223, \
          0.9686710476965903, \
          0.9686710476965903, \
          0.9686710476965903, \
          0.0313289523034098, \
          0.0313289523034098, \
          0.0313289523034098, \
          0.8407183935395043, \
          0.8407183935395043, \
          0.8407183935395043, \
          0.1592816064604957, \
          0.1592816064604957, \
          0.1592816064604957, \
          0.8773254399543938, \
          0.8773254399543938, \
          0.8773254399543938, \
          0.1226745600456062, \
          0.1226745600456062, \
          0.1226745600456062, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6944689221677809, \
          0.6944689221677809, \
          0.6944689221677809, \
          0.6944689221677809, \
          0.6944689221677809, \
          0.6944689221677809, \
          0.3055310778322191, \
          0.3055310778322191, \
          0.3055310778322191, \
          0.3055310778322191, \
          0.3055310778322191, \
          0.3055310778322191, \
          0.8559006310012134, \
          0.8559006310012134, \
          0.8559006310012134, \
          0.8559006310012134, \
          0.8559006310012134, \
          0.8559006310012134, \
          0.1440993689987866, \
          0.1440993689987866, \
          0.1440993689987866, \
          0.1440993689987866, \
          0.1440993689987866, \
          0.1440993689987866, \
          0.2888455393681256, \
          0.2888455393681256, \
          0.2888455393681256, \
          0.2888455393681256, \
          0.2888455393681256, \
          0.2888455393681256, \
          0.7111544606318744, \
          0.7111544606318744, \
          0.7111544606318744, \
          0.7111544606318744, \
          0.7111544606318744, \
          0.7111544606318744, \
          0.9221446748533075, \
          0.9221446748533075, \
          0.9221446748533075, \
          0.9221446748533075, \
          0.9221446748533075, \
          0.9221446748533075, \
          0.0778553251466925, \
          0.0778553251466925, \
          0.0778553251466925, \
          0.0778553251466925, \
          0.0778553251466925, \
          0.0778553251466925, \
          0.9762657414250897, \
          0.9762657414250897, \
          0.9762657414250897, \
          0.9762657414250897, \
          0.9762657414250897, \
          0.9762657414250897, \
          0.0237342585749103, \
          0.0237342585749103, \
          0.0237342585749103, \
          0.0237342585749103, \
          0.0237342585749103, \
          0.0237342585749103, \
          0.0278439909861404, \
          0.0278439909861404, \
          0.0278439909861404, \
          0.0278439909861404, \
          0.0278439909861404, \
          0.0278439909861404, \
          0.9721560090138596, \
          0.9721560090138596, \
          0.9721560090138596, \
          0.9721560090138596, \
          0.9721560090138596, \
          0.9721560090138596 ] )

  w = np.array ( [ \
          0.0112254009526498, \
          0.0112254009526498, \
          0.0225097870163436, \
          0.0225097870163436, \
          0.0054894240839370, \
          0.0054894240839370, \
          0.0054894240839370, \
          0.0004964406537954, \
          0.0004964406537954, \
          0.0004964406537954, \
          0.0102090400109948, \
          0.0102090400109948, \
          0.0102090400109948, \
          0.0102090400109948, \
          0.0102090400109948, \
          0.0102090400109948, \
          0.0021006495508094, \
          0.0021006495508094, \
          0.0021006495508094, \
          0.0021006495508094, \
          0.0021006495508094, \
          0.0021006495508094, \
          0.0152094206670507, \
          0.0152094206670507, \
          0.0152094206670507, \
          0.0152094206670507, \
          0.0152094206670507, \
          0.0152094206670507, \
          0.0136582892001806, \
          0.0136582892001806, \
          0.0136582892001806, \
          0.0136582892001806, \
          0.0136582892001806, \
          0.0136582892001806, \
          0.0027887393220490, \
          0.0027887393220490, \
          0.0027887393220490, \
          0.0027887393220490, \
          0.0027887393220490, \
          0.0027887393220490, \
          0.0022520950855930, \
          0.0022520950855930, \
          0.0022520950855930, \
          0.0022520950855930, \
          0.0022520950855930, \
          0.0022520950855930, \
          0.0099174482589678, \
          0.0099174482589678, \
          0.0099174482589678, \
          0.0099174482589678, \
          0.0099174482589678, \
          0.0099174482589678, \
          0.0095245941038326, \
          0.0095245941038326, \
          0.0095245941038326, \
          0.0095245941038326, \
          0.0095245941038326, \
          0.0095245941038326, \
          0.0066881354290901, \
          0.0066881354290901, \
          0.0066881354290901, \
          0.0066881354290901, \
          0.0066881354290901, \
          0.0066881354290901, \
          0.0056673224713314, \
          0.0056673224713314, \
          0.0056673224713314, \
          0.0056673224713314, \
          0.0056673224713314, \
          0.0056673224713314, \
          0.0056673224713314, \
          0.0056673224713314, \
          0.0056673224713314, \
          0.0056673224713314, \
          0.0056673224713314, \
          0.0056673224713314, \
          0.0125866454585098, \
          0.0125866454585098, \
          0.0125866454585098, \
          0.0125866454585098, \
          0.0125866454585098, \
          0.0125866454585098, \
          0.0125866454585098, \
          0.0125866454585098, \
          0.0125866454585098, \
          0.0125866454585098, \
          0.0125866454585098, \
          0.0125866454585098, \
          0.0114370118000321, \
          0.0114370118000321, \
          0.0114370118000321, \
          0.0114370118000321, \
          0.0114370118000321, \
          0.0114370118000321, \
          0.0114370118000321, \
          0.0114370118000321, \
          0.0114370118000321, \
          0.0114370118000321, \
          0.0114370118000321, \
          0.0114370118000321, \
          0.0044955975561441, \
          0.0044955975561441, \
          0.0044955975561441, \
          0.0044955975561441, \
          0.0044955975561441, \
          0.0044955975561441, \
          0.0044955975561441, \
          0.0044955975561441, \
          0.0044955975561441, \
          0.0044955975561441, \
          0.0044955975561441, \
          0.0044955975561441, \
          0.0011897740209102, \
          0.0011897740209102, \
          0.0011897740209102, \
          0.0011897740209102, \
          0.0011897740209102, \
          0.0011897740209102, \
          0.0011897740209102, \
          0.0011897740209102, \
          0.0011897740209102, \
          0.0011897740209102, \
          0.0011897740209102, \
          0.0011897740209102, \
          0.0046637786995230, \
          0.0046637786995230, \
          0.0046637786995230, \
          0.0046637786995230, \
          0.0046637786995230, \
          0.0046637786995230, \
          0.0046637786995230, \
          0.0046637786995230, \
          0.0046637786995230, \
          0.0046637786995230, \
          0.0046637786995230, \
          0.0046637786995230 ] )

  return x, y, z, w

def rule13 ( ):

#*****************************************************************************80
#
## rule13() returns the prism rule of precision 13.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.4898439392870481, \
          0.4898439392870481, \
          0.0203121214259039, \
          0.4898439392870481, \
          0.4898439392870481, \
          0.0203121214259039, \
          0.4652402431593082, \
          0.4652402431593082, \
          0.0695195136813836, \
          0.4652402431593082, \
          0.4652402431593082, \
          0.0695195136813836, \
          0.1189161740974999, \
          0.1189161740974999, \
          0.7621676518050002, \
          0.1189161740974999, \
          0.1189161740974999, \
          0.7621676518050002, \
          0.4065656818638698, \
          0.4065656818638698, \
          0.1868686362722604, \
          0.4065656818638698, \
          0.4065656818638698, \
          0.1868686362722604, \
          0.3731243598486834, \
          0.3731243598486834, \
          0.2537512803026333, \
          0.3731243598486834, \
          0.3731243598486834, \
          0.2537512803026333, \
          0.0222257711836755, \
          0.0222257711836755, \
          0.9555484576326490, \
          0.0222257711836755, \
          0.0222257711836755, \
          0.9555484576326490, \
          0.4252710267490136, \
          0.4252710267490136, \
          0.1494579465019728, \
          0.4252710267490136, \
          0.4252710267490136, \
          0.1494579465019728, \
          0.2896929731593648, \
          0.2896929731593648, \
          0.4206140536812703, \
          0.2896929731593648, \
          0.2896929731593648, \
          0.4206140536812703, \
          0.1072868932263340, \
          0.1072868932263340, \
          0.7854262135473320, \
          0.1072868932263340, \
          0.1072868932263340, \
          0.7854262135473320, \
          0.2080125480772502, \
          0.2080125480772502, \
          0.5839749038454997, \
          0.2080125480772502, \
          0.2080125480772502, \
          0.5839749038454997, \
          0.2230030950549982, \
          0.2230030950549982, \
          0.5539938098900037, \
          0.2230030950549982, \
          0.2230030950549982, \
          0.5539938098900037, \
          0.0261743916084927, \
          0.0261743916084927, \
          0.9476512167830147, \
          0.0261743916084927, \
          0.0261743916084927, \
          0.9476512167830147, \
          0.0069141701592508, \
          0.2742659465495736, \
          0.0069141701592508, \
          0.7188198832911755, \
          0.2742659465495736, \
          0.7188198832911755, \
          0.1210652398684976, \
          0.0234237758449634, \
          0.1210652398684976, \
          0.8555109842865389, \
          0.0234237758449634, \
          0.8555109842865389, \
          0.0935360177546358, \
          0.5415308571572887, \
          0.0935360177546358, \
          0.3649331250880756, \
          0.5415308571572887, \
          0.3649331250880756, \
          0.0190809537819619, \
          0.4425451813256520, \
          0.0190809537819619, \
          0.5383738648923861, \
          0.4425451813256520, \
          0.5383738648923861, \
          0.0190809537819619, \
          0.4425451813256520, \
          0.0190809537819619, \
          0.5383738648923861, \
          0.4425451813256520, \
          0.5383738648923861, \
          0.2923396969545124, \
          0.0181776522602859, \
          0.2923396969545124, \
          0.6894826507852017, \
          0.0181776522602859, \
          0.6894826507852017, \
          0.2923396969545124, \
          0.0181776522602859, \
          0.2923396969545124, \
          0.6894826507852017, \
          0.0181776522602859, \
          0.6894826507852017, \
          0.0212309381671597, \
          0.8615902483468726, \
          0.0212309381671597, \
          0.1171788134859677, \
          0.8615902483468726, \
          0.1171788134859677, \
          0.0212309381671597, \
          0.8615902483468726, \
          0.0212309381671597, \
          0.1171788134859677, \
          0.8615902483468726, \
          0.1171788134859677, \
          0.2541452627735283, \
          0.0752550719401233, \
          0.2541452627735283, \
          0.6705996652863484, \
          0.0752550719401233, \
          0.6705996652863484, \
          0.2541452627735283, \
          0.0752550719401233, \
          0.2541452627735283, \
          0.6705996652863484, \
          0.0752550719401233, \
          0.6705996652863484, \
          0.1414034499801619, \
          0.0248530932165772, \
          0.1414034499801619, \
          0.8337434568032609, \
          0.0248530932165772, \
          0.8337434568032609, \
          0.1414034499801619, \
          0.0248530932165772, \
          0.1414034499801619, \
          0.8337434568032609, \
          0.0248530932165772, \
          0.8337434568032609, \
          0.5920519581168684, \
          0.1079442302776815, \
          0.5920519581168684, \
          0.3000038116054501, \
          0.1079442302776815, \
          0.3000038116054501, \
          0.5920519581168684, \
          0.1079442302776815, \
          0.5920519581168684, \
          0.3000038116054501, \
          0.1079442302776815, \
          0.3000038116054501 ] )

  y = np.array ( [ \
          0.4898439392870481, \
          0.0203121214259039, \
          0.4898439392870481, \
          0.4898439392870481, \
          0.0203121214259039, \
          0.4898439392870481, \
          0.4652402431593082, \
          0.0695195136813836, \
          0.4652402431593082, \
          0.4652402431593082, \
          0.0695195136813836, \
          0.4652402431593082, \
          0.1189161740974999, \
          0.7621676518050002, \
          0.1189161740974999, \
          0.1189161740974999, \
          0.7621676518050002, \
          0.1189161740974999, \
          0.4065656818638698, \
          0.1868686362722604, \
          0.4065656818638698, \
          0.4065656818638698, \
          0.1868686362722604, \
          0.4065656818638698, \
          0.3731243598486834, \
          0.2537512803026333, \
          0.3731243598486834, \
          0.3731243598486834, \
          0.2537512803026333, \
          0.3731243598486834, \
          0.0222257711836755, \
          0.9555484576326490, \
          0.0222257711836755, \
          0.0222257711836755, \
          0.9555484576326490, \
          0.0222257711836755, \
          0.4252710267490136, \
          0.1494579465019728, \
          0.4252710267490136, \
          0.4252710267490136, \
          0.1494579465019728, \
          0.4252710267490136, \
          0.2896929731593648, \
          0.4206140536812703, \
          0.2896929731593648, \
          0.2896929731593648, \
          0.4206140536812703, \
          0.2896929731593648, \
          0.1072868932263340, \
          0.7854262135473320, \
          0.1072868932263340, \
          0.1072868932263340, \
          0.7854262135473320, \
          0.1072868932263340, \
          0.2080125480772502, \
          0.5839749038454997, \
          0.2080125480772502, \
          0.2080125480772502, \
          0.5839749038454997, \
          0.2080125480772502, \
          0.2230030950549982, \
          0.5539938098900037, \
          0.2230030950549982, \
          0.2230030950549982, \
          0.5539938098900037, \
          0.2230030950549982, \
          0.0261743916084927, \
          0.9476512167830147, \
          0.0261743916084927, \
          0.0261743916084927, \
          0.9476512167830147, \
          0.0261743916084927, \
          0.2742659465495736, \
          0.0069141701592508, \
          0.7188198832911755, \
          0.0069141701592508, \
          0.7188198832911755, \
          0.2742659465495736, \
          0.0234237758449634, \
          0.1210652398684976, \
          0.8555109842865389, \
          0.1210652398684976, \
          0.8555109842865389, \
          0.0234237758449634, \
          0.5415308571572887, \
          0.0935360177546358, \
          0.3649331250880756, \
          0.0935360177546358, \
          0.3649331250880756, \
          0.5415308571572887, \
          0.4425451813256520, \
          0.0190809537819619, \
          0.5383738648923861, \
          0.0190809537819619, \
          0.5383738648923861, \
          0.4425451813256520, \
          0.4425451813256520, \
          0.0190809537819619, \
          0.5383738648923861, \
          0.0190809537819619, \
          0.5383738648923861, \
          0.4425451813256520, \
          0.0181776522602859, \
          0.2923396969545124, \
          0.6894826507852017, \
          0.2923396969545124, \
          0.6894826507852017, \
          0.0181776522602859, \
          0.0181776522602859, \
          0.2923396969545124, \
          0.6894826507852017, \
          0.2923396969545124, \
          0.6894826507852017, \
          0.0181776522602859, \
          0.8615902483468726, \
          0.0212309381671597, \
          0.1171788134859677, \
          0.0212309381671597, \
          0.1171788134859677, \
          0.8615902483468726, \
          0.8615902483468726, \
          0.0212309381671597, \
          0.1171788134859677, \
          0.0212309381671597, \
          0.1171788134859677, \
          0.8615902483468726, \
          0.0752550719401233, \
          0.2541452627735283, \
          0.6705996652863484, \
          0.2541452627735283, \
          0.6705996652863484, \
          0.0752550719401233, \
          0.0752550719401233, \
          0.2541452627735283, \
          0.6705996652863484, \
          0.2541452627735283, \
          0.6705996652863484, \
          0.0752550719401233, \
          0.0248530932165772, \
          0.1414034499801619, \
          0.8337434568032609, \
          0.1414034499801619, \
          0.8337434568032609, \
          0.0248530932165772, \
          0.0248530932165772, \
          0.1414034499801619, \
          0.8337434568032609, \
          0.1414034499801619, \
          0.8337434568032609, \
          0.0248530932165772, \
          0.1079442302776815, \
          0.5920519581168684, \
          0.3000038116054501, \
          0.5920519581168684, \
          0.3000038116054501, \
          0.1079442302776815, \
          0.1079442302776815, \
          0.5920519581168684, \
          0.3000038116054501, \
          0.5920519581168684, \
          0.3000038116054501, \
          0.1079442302776815 ] )

  z = np.array ( [ \
          0.9628749136752521, \
          0.9628749136752521, \
          0.9628749136752521, \
          0.0371250863247479, \
          0.0371250863247479, \
          0.0371250863247479, \
          0.1596095438845206, \
          0.1596095438845206, \
          0.1596095438845206, \
          0.8403904561154794, \
          0.8403904561154794, \
          0.8403904561154794, \
          0.9056527042389668, \
          0.9056527042389668, \
          0.9056527042389668, \
          0.0943472957610332, \
          0.0943472957610332, \
          0.0943472957610332, \
          0.5096252745686303, \
          0.5096252745686303, \
          0.5096252745686303, \
          0.4903747254313698, \
          0.4903747254313698, \
          0.4903747254313698, \
          0.9622105990610692, \
          0.9622105990610692, \
          0.9622105990610692, \
          0.0377894009389309, \
          0.0377894009389309, \
          0.0377894009389309, \
          0.6451848165106220, \
          0.6451848165106220, \
          0.6451848165106220, \
          0.3548151834893781, \
          0.3548151834893781, \
          0.3548151834893781, \
          0.8358323923694781, \
          0.8358323923694781, \
          0.8358323923694781, \
          0.1641676076305219, \
          0.1641676076305219, \
          0.1641676076305219, \
          0.6970082735594627, \
          0.6970082735594627, \
          0.6970082735594627, \
          0.3029917264405373, \
          0.3029917264405373, \
          0.3029917264405373, \
          0.5806209783551364, \
          0.5806209783551364, \
          0.5806209783551364, \
          0.4193790216448636, \
          0.4193790216448636, \
          0.4193790216448636, \
          0.6310517191712730, \
          0.6310517191712730, \
          0.6310517191712730, \
          0.3689482808287270, \
          0.3689482808287270, \
          0.3689482808287270, \
          0.8758646517044397, \
          0.8758646517044397, \
          0.8758646517044397, \
          0.1241353482955603, \
          0.1241353482955603, \
          0.1241353482955603, \
          0.9265272967069804, \
          0.9265272967069804, \
          0.9265272967069804, \
          0.0734727032930196, \
          0.0734727032930196, \
          0.0734727032930196, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.6831055612129073, \
          0.6831055612129073, \
          0.6831055612129073, \
          0.6831055612129073, \
          0.6831055612129073, \
          0.6831055612129073, \
          0.3168944387870927, \
          0.3168944387870927, \
          0.3168944387870927, \
          0.3168944387870927, \
          0.3168944387870927, \
          0.3168944387870927, \
          0.8946991133344783, \
          0.8946991133344783, \
          0.8946991133344783, \
          0.8946991133344783, \
          0.8946991133344783, \
          0.8946991133344783, \
          0.1053008866655217, \
          0.1053008866655217, \
          0.1053008866655217, \
          0.1053008866655217, \
          0.1053008866655217, \
          0.1053008866655217, \
          0.7783161730088111, \
          0.7783161730088111, \
          0.7783161730088111, \
          0.7783161730088111, \
          0.7783161730088111, \
          0.7783161730088111, \
          0.2216838269911889, \
          0.2216838269911889, \
          0.2216838269911889, \
          0.2216838269911889, \
          0.2216838269911889, \
          0.2216838269911889, \
          0.2838393063545257, \
          0.2838393063545257, \
          0.2838393063545257, \
          0.2838393063545257, \
          0.2838393063545257, \
          0.2838393063545257, \
          0.7161606936454743, \
          0.7161606936454743, \
          0.7161606936454743, \
          0.7161606936454743, \
          0.7161606936454743, \
          0.7161606936454743, \
          0.9877489005025584, \
          0.9877489005025584, \
          0.9877489005025584, \
          0.9877489005025584, \
          0.9877489005025584, \
          0.9877489005025584, \
          0.0122510994974416, \
          0.0122510994974416, \
          0.0122510994974416, \
          0.0122510994974416, \
          0.0122510994974416, \
          0.0122510994974416, \
          0.9801022671238835, \
          0.9801022671238835, \
          0.9801022671238835, \
          0.9801022671238835, \
          0.9801022671238835, \
          0.9801022671238835, \
          0.0198977328761166, \
          0.0198977328761166, \
          0.0198977328761166, \
          0.0198977328761166, \
          0.0198977328761166, \
          0.0198977328761166 ] )

  w = np.array ( [ \
          0.0026290597067936, \
          0.0026290597067936, \
          0.0026290597067936, \
          0.0026290597067936, \
          0.0026290597067936, \
          0.0026290597067936, \
          0.0059734237493126, \
          0.0059734237493126, \
          0.0059734237493126, \
          0.0059734237493126, \
          0.0059734237493126, \
          0.0059734237493126, \
          0.0080935494241557, \
          0.0080935494241557, \
          0.0080935494241557, \
          0.0080935494241557, \
          0.0080935494241557, \
          0.0080935494241557, \
          0.0068191162590357, \
          0.0068191162590357, \
          0.0068191162590357, \
          0.0068191162590357, \
          0.0068191162590357, \
          0.0068191162590357, \
          0.0049334513687730, \
          0.0049334513687730, \
          0.0049334513687730, \
          0.0049334513687730, \
          0.0049334513687730, \
          0.0049334513687730, \
          0.0020147080132884, \
          0.0020147080132884, \
          0.0020147080132884, \
          0.0020147080132884, \
          0.0020147080132884, \
          0.0020147080132884, \
          0.0123357707370753, \
          0.0123357707370753, \
          0.0123357707370753, \
          0.0123357707370753, \
          0.0123357707370753, \
          0.0123357707370753, \
          0.0113647943376711, \
          0.0113647943376711, \
          0.0113647943376711, \
          0.0113647943376711, \
          0.0113647943376711, \
          0.0113647943376711, \
          0.0066668649606825, \
          0.0066668649606825, \
          0.0066668649606825, \
          0.0066668649606825, \
          0.0066668649606825, \
          0.0066668649606825, \
          0.0119452201363976, \
          0.0119452201363976, \
          0.0119452201363976, \
          0.0119452201363976, \
          0.0119452201363976, \
          0.0119452201363976, \
          0.0106878809406112, \
          0.0106878809406112, \
          0.0106878809406112, \
          0.0106878809406112, \
          0.0106878809406112, \
          0.0106878809406112, \
          0.0016663443274632, \
          0.0016663443274632, \
          0.0016663443274632, \
          0.0016663443274632, \
          0.0016663443274632, \
          0.0016663443274632, \
          0.0045120516170652, \
          0.0045120516170652, \
          0.0045120516170652, \
          0.0045120516170652, \
          0.0045120516170652, \
          0.0045120516170652, \
          0.0034887068394433, \
          0.0034887068394433, \
          0.0034887068394433, \
          0.0034887068394433, \
          0.0034887068394433, \
          0.0034887068394433, \
          0.0111803506944158, \
          0.0111803506944158, \
          0.0111803506944158, \
          0.0111803506944158, \
          0.0111803506944158, \
          0.0111803506944158, \
          0.0042052602324505, \
          0.0042052602324505, \
          0.0042052602324505, \
          0.0042052602324505, \
          0.0042052602324505, \
          0.0042052602324505, \
          0.0042052602324505, \
          0.0042052602324505, \
          0.0042052602324505, \
          0.0042052602324505, \
          0.0042052602324505, \
          0.0042052602324505, \
          0.0043767917497427, \
          0.0043767917497427, \
          0.0043767917497427, \
          0.0043767917497427, \
          0.0043767917497427, \
          0.0043767917497427, \
          0.0043767917497427, \
          0.0043767917497427, \
          0.0043767917497427, \
          0.0043767917497427, \
          0.0043767917497427, \
          0.0043767917497427, \
          0.0044067550419370, \
          0.0044067550419370, \
          0.0044067550419370, \
          0.0044067550419370, \
          0.0044067550419370, \
          0.0044067550419370, \
          0.0044067550419370, \
          0.0044067550419370, \
          0.0044067550419370, \
          0.0044067550419370, \
          0.0044067550419370, \
          0.0044067550419370, \
          0.0120350326772681, \
          0.0120350326772681, \
          0.0120350326772681, \
          0.0120350326772681, \
          0.0120350326772681, \
          0.0120350326772681, \
          0.0120350326772681, \
          0.0120350326772681, \
          0.0120350326772681, \
          0.0120350326772681, \
          0.0120350326772681, \
          0.0120350326772681, \
          0.0013986921884649, \
          0.0013986921884649, \
          0.0013986921884649, \
          0.0013986921884649, \
          0.0013986921884649, \
          0.0013986921884649, \
          0.0013986921884649, \
          0.0013986921884649, \
          0.0013986921884649, \
          0.0013986921884649, \
          0.0013986921884649, \
          0.0013986921884649, \
          0.0047551548873781, \
          0.0047551548873781, \
          0.0047551548873781, \
          0.0047551548873781, \
          0.0047551548873781, \
          0.0047551548873781, \
          0.0047551548873781, \
          0.0047551548873781, \
          0.0047551548873781, \
          0.0047551548873781, \
          0.0047551548873781, \
          0.0047551548873781 ] )

  return x, y, z, w

def rule14 ( ):

#*****************************************************************************80
#
## rule14() returns the prism rule of precision 14.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.1531409494078462, \
          0.1531409494078462, \
          0.6937181011843075, \
          0.1094642266754876, \
          0.1094642266754876, \
          0.7810715466490248, \
          0.4852139749601931, \
          0.4852139749601931, \
          0.0295720500796137, \
          0.4852139749601931, \
          0.4852139749601931, \
          0.0295720500796137, \
          0.4811857851081537, \
          0.4811857851081537, \
          0.0376284297836926, \
          0.4811857851081537, \
          0.4811857851081537, \
          0.0376284297836926, \
          0.0854252549169795, \
          0.0854252549169795, \
          0.8291494901660410, \
          0.0854252549169795, \
          0.0854252549169795, \
          0.8291494901660410, \
          0.4949498254464672, \
          0.4949498254464672, \
          0.0101003491070657, \
          0.4949498254464672, \
          0.4949498254464672, \
          0.0101003491070657, \
          0.2006722689888837, \
          0.2006722689888837, \
          0.5986554620222326, \
          0.2006722689888837, \
          0.2006722689888837, \
          0.5986554620222326, \
          0.0134631402389198, \
          0.0134631402389198, \
          0.9730737195221603, \
          0.0134631402389198, \
          0.0134631402389198, \
          0.9730737195221603, \
          0.3888073656098609, \
          0.3888073656098609, \
          0.2223852687802782, \
          0.3888073656098609, \
          0.3888073656098609, \
          0.2223852687802782, \
          0.2589597694248802, \
          0.2589597694248802, \
          0.4820804611502396, \
          0.2589597694248802, \
          0.2589597694248802, \
          0.4820804611502396, \
          0.0656674639158517, \
          0.0656674639158517, \
          0.8686650721682967, \
          0.0656674639158517, \
          0.0656674639158517, \
          0.8686650721682967, \
          0.4462504387663027, \
          0.4462504387663027, \
          0.1074991224673947, \
          0.4462504387663027, \
          0.4462504387663027, \
          0.1074991224673947, \
          0.1155506883468244, \
          0.1155506883468244, \
          0.7688986233063512, \
          0.1155506883468244, \
          0.1155506883468244, \
          0.7688986233063512, \
          0.0257939798379175, \
          0.0257939798379175, \
          0.9484120403241649, \
          0.0257939798379175, \
          0.0257939798379175, \
          0.9484120403241649, \
          0.0231313365079955, \
          0.3737411598567404, \
          0.0231313365079955, \
          0.6031275036352640, \
          0.3737411598567404, \
          0.6031275036352640, \
          0.0780837656724579, \
          0.0087167837437324, \
          0.0780837656724579, \
          0.9131994505838098, \
          0.0087167837437324, \
          0.9131994505838098, \
          0.1932090397525293, \
          0.4408189862889988, \
          0.1932090397525293, \
          0.3659719739584719, \
          0.4408189862889988, \
          0.3659719739584719, \
          0.0110695610243579, \
          0.3495104935335414, \
          0.0110695610243579, \
          0.6394199454421007, \
          0.3495104935335414, \
          0.6394199454421007, \
          0.0110695610243579, \
          0.3495104935335414, \
          0.0110695610243579, \
          0.6394199454421007, \
          0.3495104935335414, \
          0.6394199454421007, \
          0.2813786819004687, \
          0.0725240717490409, \
          0.2813786819004687, \
          0.6460972463504904, \
          0.0725240717490409, \
          0.6460972463504904, \
          0.2813786819004687, \
          0.0725240717490409, \
          0.2813786819004687, \
          0.6460972463504904, \
          0.0725240717490409, \
          0.6460972463504904, \
          0.0136067459730556, \
          0.7694543610610796, \
          0.0136067459730556, \
          0.2169388929658648, \
          0.7694543610610796, \
          0.2169388929658648, \
          0.0136067459730556, \
          0.7694543610610796, \
          0.0136067459730556, \
          0.2169388929658648, \
          0.7694543610610796, \
          0.2169388929658648, \
          0.3160642637515643, \
          0.0980612921350026, \
          0.3160642637515643, \
          0.5858744441134331, \
          0.0980612921350026, \
          0.5858744441134331, \
          0.3160642637515643, \
          0.0980612921350026, \
          0.3160642637515643, \
          0.5858744441134331, \
          0.0980612921350026, \
          0.5858744441134331, \
          0.2010219519914552, \
          0.0101533805746944, \
          0.2010219519914552, \
          0.7888246674338504, \
          0.0101533805746944, \
          0.7888246674338504, \
          0.2010219519914552, \
          0.0101533805746944, \
          0.2010219519914552, \
          0.7888246674338504, \
          0.0101533805746944, \
          0.7888246674338504, \
          0.5404862370418329, \
          0.1675040220811526, \
          0.5404862370418329, \
          0.2920097408770145, \
          0.1675040220811526, \
          0.2920097408770145, \
          0.5404862370418329, \
          0.1675040220811526, \
          0.5404862370418329, \
          0.2920097408770145, \
          0.1675040220811526, \
          0.2920097408770145, \
          0.1016331118955575, \
          0.0168250918958854, \
          0.1016331118955575, \
          0.8815417962085570, \
          0.0168250918958854, \
          0.8815417962085570, \
          0.1016331118955575, \
          0.0168250918958854, \
          0.1016331118955575, \
          0.8815417962085570, \
          0.0168250918958854, \
          0.8815417962085570, \
          0.7553391402298588, \
          0.0552850680433709, \
          0.7553391402298588, \
          0.1893757917267703, \
          0.0552850680433709, \
          0.1893757917267703, \
          0.7553391402298588, \
          0.0552850680433709, \
          0.7553391402298588, \
          0.1893757917267703, \
          0.0552850680433709, \
          0.1893757917267703 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.1531409494078462, \
          0.6937181011843075, \
          0.1531409494078462, \
          0.1094642266754876, \
          0.7810715466490248, \
          0.1094642266754876, \
          0.4852139749601931, \
          0.0295720500796137, \
          0.4852139749601931, \
          0.4852139749601931, \
          0.0295720500796137, \
          0.4852139749601931, \
          0.4811857851081537, \
          0.0376284297836926, \
          0.4811857851081537, \
          0.4811857851081537, \
          0.0376284297836926, \
          0.4811857851081537, \
          0.0854252549169795, \
          0.8291494901660410, \
          0.0854252549169795, \
          0.0854252549169795, \
          0.8291494901660410, \
          0.0854252549169795, \
          0.4949498254464672, \
          0.0101003491070657, \
          0.4949498254464672, \
          0.4949498254464672, \
          0.0101003491070657, \
          0.4949498254464672, \
          0.2006722689888837, \
          0.5986554620222326, \
          0.2006722689888837, \
          0.2006722689888837, \
          0.5986554620222326, \
          0.2006722689888837, \
          0.0134631402389198, \
          0.9730737195221603, \
          0.0134631402389198, \
          0.0134631402389198, \
          0.9730737195221603, \
          0.0134631402389198, \
          0.3888073656098609, \
          0.2223852687802782, \
          0.3888073656098609, \
          0.3888073656098609, \
          0.2223852687802782, \
          0.3888073656098609, \
          0.2589597694248802, \
          0.4820804611502396, \
          0.2589597694248802, \
          0.2589597694248802, \
          0.4820804611502396, \
          0.2589597694248802, \
          0.0656674639158517, \
          0.8686650721682967, \
          0.0656674639158517, \
          0.0656674639158517, \
          0.8686650721682967, \
          0.0656674639158517, \
          0.4462504387663027, \
          0.1074991224673947, \
          0.4462504387663027, \
          0.4462504387663027, \
          0.1074991224673947, \
          0.4462504387663027, \
          0.1155506883468244, \
          0.7688986233063512, \
          0.1155506883468244, \
          0.1155506883468244, \
          0.7688986233063512, \
          0.1155506883468244, \
          0.0257939798379175, \
          0.9484120403241649, \
          0.0257939798379175, \
          0.0257939798379175, \
          0.9484120403241649, \
          0.0257939798379175, \
          0.3737411598567404, \
          0.0231313365079955, \
          0.6031275036352640, \
          0.0231313365079955, \
          0.6031275036352640, \
          0.3737411598567404, \
          0.0087167837437324, \
          0.0780837656724579, \
          0.9131994505838098, \
          0.0780837656724579, \
          0.9131994505838098, \
          0.0087167837437324, \
          0.4408189862889988, \
          0.1932090397525293, \
          0.3659719739584719, \
          0.1932090397525293, \
          0.3659719739584719, \
          0.4408189862889988, \
          0.3495104935335414, \
          0.0110695610243579, \
          0.6394199454421007, \
          0.0110695610243579, \
          0.6394199454421007, \
          0.3495104935335414, \
          0.3495104935335414, \
          0.0110695610243579, \
          0.6394199454421007, \
          0.0110695610243579, \
          0.6394199454421007, \
          0.3495104935335414, \
          0.0725240717490409, \
          0.2813786819004687, \
          0.6460972463504904, \
          0.2813786819004687, \
          0.6460972463504904, \
          0.0725240717490409, \
          0.0725240717490409, \
          0.2813786819004687, \
          0.6460972463504904, \
          0.2813786819004687, \
          0.6460972463504904, \
          0.0725240717490409, \
          0.7694543610610796, \
          0.0136067459730556, \
          0.2169388929658648, \
          0.0136067459730556, \
          0.2169388929658648, \
          0.7694543610610796, \
          0.7694543610610796, \
          0.0136067459730556, \
          0.2169388929658648, \
          0.0136067459730556, \
          0.2169388929658648, \
          0.7694543610610796, \
          0.0980612921350026, \
          0.3160642637515643, \
          0.5858744441134331, \
          0.3160642637515643, \
          0.5858744441134331, \
          0.0980612921350026, \
          0.0980612921350026, \
          0.3160642637515643, \
          0.5858744441134331, \
          0.3160642637515643, \
          0.5858744441134331, \
          0.0980612921350026, \
          0.0101533805746944, \
          0.2010219519914552, \
          0.7888246674338504, \
          0.2010219519914552, \
          0.7888246674338504, \
          0.0101533805746944, \
          0.0101533805746944, \
          0.2010219519914552, \
          0.7888246674338504, \
          0.2010219519914552, \
          0.7888246674338504, \
          0.0101533805746944, \
          0.1675040220811526, \
          0.5404862370418329, \
          0.2920097408770145, \
          0.5404862370418329, \
          0.2920097408770145, \
          0.1675040220811526, \
          0.1675040220811526, \
          0.5404862370418329, \
          0.2920097408770145, \
          0.5404862370418329, \
          0.2920097408770145, \
          0.1675040220811526, \
          0.0168250918958854, \
          0.1016331118955575, \
          0.8815417962085570, \
          0.1016331118955575, \
          0.8815417962085570, \
          0.0168250918958854, \
          0.0168250918958854, \
          0.1016331118955575, \
          0.8815417962085570, \
          0.1016331118955575, \
          0.8815417962085570, \
          0.0168250918958854, \
          0.0552850680433709, \
          0.7553391402298588, \
          0.1893757917267703, \
          0.7553391402298588, \
          0.1893757917267703, \
          0.0552850680433709, \
          0.0552850680433709, \
          0.7553391402298588, \
          0.1893757917267703, \
          0.7553391402298588, \
          0.1893757917267703, \
          0.0552850680433709 ] )

  z = np.array ( [ \
          0.2284245901167349, \
          0.7715754098832651, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9749706927792001, \
          0.9749706927792001, \
          0.9749706927792001, \
          0.0250293072207999, \
          0.0250293072207999, \
          0.0250293072207999, \
          0.3291597905587964, \
          0.3291597905587964, \
          0.3291597905587964, \
          0.6708402094412036, \
          0.6708402094412036, \
          0.6708402094412036, \
          0.9996712623901741, \
          0.9996712623901741, \
          0.9996712623901741, \
          0.0003287376098259, \
          0.0003287376098259, \
          0.0003287376098259, \
          0.7021882096439400, \
          0.7021882096439400, \
          0.7021882096439400, \
          0.2978117903560600, \
          0.2978117903560600, \
          0.2978117903560600, \
          0.8352161845608261, \
          0.8352161845608261, \
          0.8352161845608261, \
          0.1647838154391739, \
          0.1647838154391739, \
          0.1647838154391739, \
          0.7201109571464277, \
          0.7201109571464277, \
          0.7201109571464277, \
          0.2798890428535724, \
          0.2798890428535724, \
          0.2798890428535724, \
          0.9332471062622827, \
          0.9332471062622827, \
          0.9332471062622827, \
          0.0667528937377173, \
          0.0667528937377173, \
          0.0667528937377173, \
          0.3097333917149071, \
          0.3097333917149071, \
          0.3097333917149071, \
          0.6902666082850929, \
          0.6902666082850929, \
          0.6902666082850929, \
          0.6590250213320482, \
          0.6590250213320482, \
          0.6590250213320482, \
          0.3409749786679518, \
          0.3409749786679518, \
          0.3409749786679518, \
          0.8368689390766315, \
          0.8368689390766315, \
          0.8368689390766315, \
          0.1631310609233684, \
          0.1631310609233684, \
          0.1631310609233684, \
          0.9263853262636454, \
          0.9263853262636454, \
          0.9263853262636454, \
          0.0736146737363546, \
          0.0736146737363546, \
          0.0736146737363546, \
          0.9586297434779142, \
          0.9586297434779142, \
          0.9586297434779142, \
          0.0413702565220858, \
          0.0413702565220858, \
          0.0413702565220858, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8444056700436123, \
          0.8444056700436123, \
          0.8444056700436123, \
          0.8444056700436123, \
          0.8444056700436123, \
          0.8444056700436123, \
          0.1555943299563877, \
          0.1555943299563877, \
          0.1555943299563877, \
          0.1555943299563877, \
          0.1555943299563877, \
          0.1555943299563877, \
          0.9409140558660263, \
          0.9409140558660263, \
          0.9409140558660263, \
          0.9409140558660263, \
          0.9409140558660263, \
          0.9409140558660263, \
          0.0590859441339738, \
          0.0590859441339738, \
          0.0590859441339738, \
          0.0590859441339738, \
          0.0590859441339738, \
          0.0590859441339738, \
          0.6041114898852048, \
          0.6041114898852048, \
          0.6041114898852048, \
          0.6041114898852048, \
          0.6041114898852048, \
          0.6041114898852048, \
          0.3958885101147953, \
          0.3958885101147953, \
          0.3958885101147953, \
          0.3958885101147953, \
          0.3958885101147953, \
          0.3958885101147953, \
          0.3519734130158997, \
          0.3519734130158997, \
          0.3519734130158997, \
          0.3519734130158997, \
          0.3519734130158997, \
          0.3519734130158997, \
          0.6480265869841003, \
          0.6480265869841003, \
          0.6480265869841003, \
          0.6480265869841003, \
          0.6480265869841003, \
          0.6480265869841003, \
          0.9783845500663495, \
          0.9783845500663495, \
          0.9783845500663495, \
          0.9783845500663495, \
          0.9783845500663495, \
          0.9783845500663495, \
          0.0216154499336504, \
          0.0216154499336504, \
          0.0216154499336504, \
          0.0216154499336504, \
          0.0216154499336504, \
          0.0216154499336504, \
          0.9921911717290701, \
          0.9921911717290701, \
          0.9921911717290701, \
          0.9921911717290701, \
          0.9921911717290701, \
          0.9921911717290701, \
          0.0078088282709299, \
          0.0078088282709299, \
          0.0078088282709299, \
          0.0078088282709299, \
          0.0078088282709299, \
          0.0078088282709299, \
          0.8588015965488265, \
          0.8588015965488265, \
          0.8588015965488265, \
          0.8588015965488265, \
          0.8588015965488265, \
          0.8588015965488265, \
          0.1411984034511735, \
          0.1411984034511735, \
          0.1411984034511735, \
          0.1411984034511735, \
          0.1411984034511735, \
          0.1411984034511735, \
          0.2510713639088549, \
          0.2510713639088549, \
          0.2510713639088549, \
          0.2510713639088549, \
          0.2510713639088549, \
          0.2510713639088549, \
          0.7489286360911451, \
          0.7489286360911451, \
          0.7489286360911451, \
          0.7489286360911451, \
          0.7489286360911451, \
          0.7489286360911451 ] )

  w = np.array ( [ \
          0.0117723371203579, \
          0.0117723371203579, \
          0.0135361913058678, \
          0.0135361913058678, \
          0.0135361913058678, \
          0.0028636244590190, \
          0.0028636244590190, \
          0.0028636244590190, \
          0.0028317101953144, \
          0.0028317101953144, \
          0.0028317101953144, \
          0.0028317101953144, \
          0.0028317101953144, \
          0.0028317101953144, \
          0.0043546495593520, \
          0.0043546495593520, \
          0.0043546495593520, \
          0.0043546495593520, \
          0.0043546495593520, \
          0.0043546495593520, \
          0.0009145278212111, \
          0.0009145278212111, \
          0.0009145278212111, \
          0.0009145278212111, \
          0.0009145278212111, \
          0.0009145278212111, \
          0.0016406658653518, \
          0.0016406658653518, \
          0.0016406658653518, \
          0.0016406658653518, \
          0.0016406658653518, \
          0.0016406658653518, \
          0.0121732957893404, \
          0.0121732957893404, \
          0.0121732957893404, \
          0.0121732957893404, \
          0.0121732957893404, \
          0.0121732957893404, \
          0.0010621280231715, \
          0.0010621280231715, \
          0.0010621280231715, \
          0.0010621280231715, \
          0.0010621280231715, \
          0.0010621280231715, \
          0.0081462190313536, \
          0.0081462190313536, \
          0.0081462190313536, \
          0.0081462190313536, \
          0.0081462190313536, \
          0.0081462190313536, \
          0.0118819825086521, \
          0.0118819825086521, \
          0.0118819825086521, \
          0.0118819825086521, \
          0.0118819825086521, \
          0.0118819825086521, \
          0.0045106060735437, \
          0.0045106060735437, \
          0.0045106060735437, \
          0.0045106060735437, \
          0.0045106060735437, \
          0.0045106060735437, \
          0.0120105850348785, \
          0.0120105850348785, \
          0.0120105850348785, \
          0.0120105850348785, \
          0.0120105850348785, \
          0.0120105850348785, \
          0.0047664383021567, \
          0.0047664383021567, \
          0.0047664383021567, \
          0.0047664383021567, \
          0.0047664383021567, \
          0.0047664383021567, \
          0.0009777024948606, \
          0.0009777024948606, \
          0.0009777024948606, \
          0.0009777024948606, \
          0.0009777024948606, \
          0.0009777024948606, \
          0.0051118807026059, \
          0.0051118807026059, \
          0.0051118807026059, \
          0.0051118807026059, \
          0.0051118807026059, \
          0.0051118807026059, \
          0.0021717621070222, \
          0.0021717621070222, \
          0.0021717621070222, \
          0.0021717621070222, \
          0.0021717621070222, \
          0.0021717621070222, \
          0.0104022745738753, \
          0.0104022745738753, \
          0.0104022745738753, \
          0.0104022745738753, \
          0.0104022745738753, \
          0.0104022745738753, \
          0.0035903626892995, \
          0.0035903626892995, \
          0.0035903626892995, \
          0.0035903626892995, \
          0.0035903626892995, \
          0.0035903626892995, \
          0.0035903626892995, \
          0.0035903626892995, \
          0.0035903626892995, \
          0.0035903626892995, \
          0.0035903626892995, \
          0.0035903626892995, \
          0.0052108482781140, \
          0.0052108482781140, \
          0.0052108482781140, \
          0.0052108482781140, \
          0.0052108482781140, \
          0.0052108482781140, \
          0.0052108482781140, \
          0.0052108482781140, \
          0.0052108482781140, \
          0.0052108482781140, \
          0.0052108482781140, \
          0.0052108482781140, \
          0.0029024210927214, \
          0.0029024210927214, \
          0.0029024210927214, \
          0.0029024210927214, \
          0.0029024210927214, \
          0.0029024210927214, \
          0.0029024210927214, \
          0.0029024210927214, \
          0.0029024210927214, \
          0.0029024210927214, \
          0.0029024210927214, \
          0.0029024210927214, \
          0.0109370973987031, \
          0.0109370973987031, \
          0.0109370973987031, \
          0.0109370973987031, \
          0.0109370973987031, \
          0.0109370973987031, \
          0.0109370973987031, \
          0.0109370973987031, \
          0.0109370973987031, \
          0.0109370973987031, \
          0.0109370973987031, \
          0.0109370973987031, \
          0.0010706231542004, \
          0.0010706231542004, \
          0.0010706231542004, \
          0.0010706231542004, \
          0.0010706231542004, \
          0.0010706231542004, \
          0.0010706231542004, \
          0.0010706231542004, \
          0.0010706231542004, \
          0.0010706231542004, \
          0.0010706231542004, \
          0.0010706231542004, \
          0.0023660542319623, \
          0.0023660542319623, \
          0.0023660542319623, \
          0.0023660542319623, \
          0.0023660542319623, \
          0.0023660542319623, \
          0.0023660542319623, \
          0.0023660542319623, \
          0.0023660542319623, \
          0.0023660542319623, \
          0.0023660542319623, \
          0.0023660542319623, \
          0.0026196720900109, \
          0.0026196720900109, \
          0.0026196720900109, \
          0.0026196720900109, \
          0.0026196720900109, \
          0.0026196720900109, \
          0.0026196720900109, \
          0.0026196720900109, \
          0.0026196720900109, \
          0.0026196720900109, \
          0.0026196720900109, \
          0.0026196720900109, \
          0.0070960302290289, \
          0.0070960302290289, \
          0.0070960302290289, \
          0.0070960302290289, \
          0.0070960302290289, \
          0.0070960302290289, \
          0.0070960302290289, \
          0.0070960302290289, \
          0.0070960302290289, \
          0.0070960302290289, \
          0.0070960302290289, \
          0.0070960302290289 ] )

  return x, y, z, w

def rule15 ( ):

#*****************************************************************************80
#
## rule15() returns the prism rule of precision 15.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.2180179116942069, \
          0.2180179116942069, \
          0.5639641766115862, \
          0.1819996803717089, \
          0.1819996803717089, \
          0.6360006392565821, \
          0.0174014011631261, \
          0.0174014011631261, \
          0.9651971976737478, \
          0.0542711501859966, \
          0.0542711501859966, \
          0.8914576996280067, \
          0.3702896314191779, \
          0.3702896314191779, \
          0.2594207371616443, \
          0.3702896314191779, \
          0.3702896314191779, \
          0.2594207371616443, \
          0.0683792324219036, \
          0.0683792324219036, \
          0.8632415351561927, \
          0.0683792324219036, \
          0.0683792324219036, \
          0.8632415351561927, \
          0.4041029865296590, \
          0.4041029865296590, \
          0.1917940269406819, \
          0.4041029865296590, \
          0.4041029865296590, \
          0.1917940269406819, \
          0.4924009437532922, \
          0.4924009437532922, \
          0.0151981124934156, \
          0.4924009437532922, \
          0.4924009437532922, \
          0.0151981124934156, \
          0.4679592294726652, \
          0.4679592294726652, \
          0.0640815410546695, \
          0.4679592294726652, \
          0.4679592294726652, \
          0.0640815410546695, \
          0.2538613877625208, \
          0.2538613877625208, \
          0.4922772244749584, \
          0.2538613877625208, \
          0.2538613877625208, \
          0.4922772244749584, \
          0.1490233678882002, \
          0.1490233678882002, \
          0.7019532642235996, \
          0.1490233678882002, \
          0.1490233678882002, \
          0.7019532642235996, \
          0.4943016520035221, \
          0.4943016520035221, \
          0.0113966959929558, \
          0.4943016520035221, \
          0.4943016520035221, \
          0.0113966959929558, \
          0.2380227290434666, \
          0.0191912097570085, \
          0.2380227290434666, \
          0.7427860611995248, \
          0.0191912097570085, \
          0.7427860611995248, \
          0.2658819381343187, \
          0.0947024276247834, \
          0.2658819381343187, \
          0.6394156342408979, \
          0.0947024276247834, \
          0.6394156342408979, \
          0.2658819381343187, \
          0.0947024276247834, \
          0.2658819381343187, \
          0.6394156342408979, \
          0.0947024276247834, \
          0.6394156342408979, \
          0.0282488031371648, \
          0.0067976462534296, \
          0.0282488031371648, \
          0.9649535506094056, \
          0.0067976462534296, \
          0.9649535506094056, \
          0.0282488031371648, \
          0.0067976462534296, \
          0.0282488031371648, \
          0.9649535506094056, \
          0.0067976462534296, \
          0.9649535506094056, \
          0.6410939576871652, \
          0.0151121945323486, \
          0.6410939576871652, \
          0.3437938477804863, \
          0.0151121945323486, \
          0.3437938477804863, \
          0.6410939576871652, \
          0.0151121945323486, \
          0.6410939576871652, \
          0.3437938477804863, \
          0.0151121945323486, \
          0.3437938477804863, \
          0.1570345607673937, \
          0.0792048851268470, \
          0.1570345607673937, \
          0.7637605541057593, \
          0.0792048851268470, \
          0.7637605541057593, \
          0.1570345607673937, \
          0.0792048851268470, \
          0.1570345607673937, \
          0.7637605541057593, \
          0.0792048851268470, \
          0.7637605541057593, \
          0.2618681572601245, \
          0.1978262294209248, \
          0.2618681572601245, \
          0.5403056133189508, \
          0.1978262294209248, \
          0.5403056133189508, \
          0.2618681572601245, \
          0.1978262294209248, \
          0.2618681572601245, \
          0.5403056133189508, \
          0.1978262294209248, \
          0.5403056133189508, \
          0.0065324588746805, \
          0.0486805622526683, \
          0.0065324588746805, \
          0.9447869788726512, \
          0.0486805622526683, \
          0.9447869788726512, \
          0.0065324588746805, \
          0.0486805622526683, \
          0.0065324588746805, \
          0.9447869788726512, \
          0.0486805622526683, \
          0.9447869788726512, \
          0.3702624031957258, \
          0.0912977133028943, \
          0.3702624031957258, \
          0.5384398835013798, \
          0.0912977133028943, \
          0.5384398835013798, \
          0.3702624031957258, \
          0.0912977133028943, \
          0.3702624031957258, \
          0.5384398835013798, \
          0.0912977133028943, \
          0.5384398835013798, \
          0.1377079768509805, \
          0.0373008369533812, \
          0.1377079768509805, \
          0.8249911861956383, \
          0.0373008369533812, \
          0.8249911861956383, \
          0.1377079768509805, \
          0.0373008369533812, \
          0.1377079768509805, \
          0.8249911861956383, \
          0.0373008369533812, \
          0.8249911861956383, \
          0.4784950101267365, \
          0.1635654688089934, \
          0.4784950101267365, \
          0.3579395210642701, \
          0.1635654688089934, \
          0.3579395210642701, \
          0.4784950101267365, \
          0.1635654688089934, \
          0.4784950101267365, \
          0.3579395210642701, \
          0.1635654688089934, \
          0.3579395210642701, \
          0.3278240979071815, \
          0.0249615816629217, \
          0.3278240979071815, \
          0.6472143204298968, \
          0.0249615816629217, \
          0.6472143204298968, \
          0.3278240979071815, \
          0.0249615816629217, \
          0.3278240979071815, \
          0.6472143204298968, \
          0.0249615816629217, \
          0.6472143204298968, \
          0.3475735063324100, \
          0.0871302288391398, \
          0.3475735063324100, \
          0.5652962648284502, \
          0.0871302288391398, \
          0.5652962648284502, \
          0.3475735063324100, \
          0.0871302288391398, \
          0.3475735063324100, \
          0.5652962648284502, \
          0.0871302288391398, \
          0.5652962648284502, \
          0.1096327891311607, \
          0.0128395677390919, \
          0.1096327891311607, \
          0.8775276431297473, \
          0.0128395677390919, \
          0.8775276431297473, \
          0.1096327891311607, \
          0.0128395677390919, \
          0.1096327891311607, \
          0.8775276431297473, \
          0.0128395677390919, \
          0.8775276431297473, \
          0.2078784801536998, \
          0.0849045675529205, \
          0.2078784801536998, \
          0.7072169522933797, \
          0.0849045675529205, \
          0.7072169522933797, \
          0.2078784801536998, \
          0.0849045675529205, \
          0.2078784801536998, \
          0.7072169522933797, \
          0.0849045675529205, \
          0.7072169522933797, \
          0.1953330193360589, \
          0.0143045787175747, \
          0.1953330193360589, \
          0.7903624019463664, \
          0.0143045787175747, \
          0.7903624019463664, \
          0.1953330193360589, \
          0.0143045787175747, \
          0.1953330193360589, \
          0.7903624019463664, \
          0.0143045787175747, \
          0.7903624019463664 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.2180179116942069, \
          0.5639641766115862, \
          0.2180179116942069, \
          0.1819996803717089, \
          0.6360006392565821, \
          0.1819996803717089, \
          0.0174014011631261, \
          0.9651971976737478, \
          0.0174014011631261, \
          0.0542711501859966, \
          0.8914576996280067, \
          0.0542711501859966, \
          0.3702896314191779, \
          0.2594207371616443, \
          0.3702896314191779, \
          0.3702896314191779, \
          0.2594207371616443, \
          0.3702896314191779, \
          0.0683792324219036, \
          0.8632415351561927, \
          0.0683792324219036, \
          0.0683792324219036, \
          0.8632415351561927, \
          0.0683792324219036, \
          0.4041029865296590, \
          0.1917940269406819, \
          0.4041029865296590, \
          0.4041029865296590, \
          0.1917940269406819, \
          0.4041029865296590, \
          0.4924009437532922, \
          0.0151981124934156, \
          0.4924009437532922, \
          0.4924009437532922, \
          0.0151981124934156, \
          0.4924009437532922, \
          0.4679592294726652, \
          0.0640815410546695, \
          0.4679592294726652, \
          0.4679592294726652, \
          0.0640815410546695, \
          0.4679592294726652, \
          0.2538613877625208, \
          0.4922772244749584, \
          0.2538613877625208, \
          0.2538613877625208, \
          0.4922772244749584, \
          0.2538613877625208, \
          0.1490233678882002, \
          0.7019532642235996, \
          0.1490233678882002, \
          0.1490233678882002, \
          0.7019532642235996, \
          0.1490233678882002, \
          0.4943016520035221, \
          0.0113966959929558, \
          0.4943016520035221, \
          0.4943016520035221, \
          0.0113966959929558, \
          0.4943016520035221, \
          0.0191912097570085, \
          0.2380227290434666, \
          0.7427860611995248, \
          0.2380227290434666, \
          0.7427860611995248, \
          0.0191912097570085, \
          0.0947024276247834, \
          0.2658819381343187, \
          0.6394156342408979, \
          0.2658819381343187, \
          0.6394156342408979, \
          0.0947024276247834, \
          0.0947024276247834, \
          0.2658819381343187, \
          0.6394156342408979, \
          0.2658819381343187, \
          0.6394156342408979, \
          0.0947024276247834, \
          0.0067976462534296, \
          0.0282488031371648, \
          0.9649535506094056, \
          0.0282488031371648, \
          0.9649535506094056, \
          0.0067976462534296, \
          0.0067976462534296, \
          0.0282488031371648, \
          0.9649535506094056, \
          0.0282488031371648, \
          0.9649535506094056, \
          0.0067976462534296, \
          0.0151121945323486, \
          0.6410939576871652, \
          0.3437938477804863, \
          0.6410939576871652, \
          0.3437938477804863, \
          0.0151121945323486, \
          0.0151121945323486, \
          0.6410939576871652, \
          0.3437938477804863, \
          0.6410939576871652, \
          0.3437938477804863, \
          0.0151121945323486, \
          0.0792048851268470, \
          0.1570345607673937, \
          0.7637605541057593, \
          0.1570345607673937, \
          0.7637605541057593, \
          0.0792048851268470, \
          0.0792048851268470, \
          0.1570345607673937, \
          0.7637605541057593, \
          0.1570345607673937, \
          0.7637605541057593, \
          0.0792048851268470, \
          0.1978262294209248, \
          0.2618681572601245, \
          0.5403056133189508, \
          0.2618681572601245, \
          0.5403056133189508, \
          0.1978262294209248, \
          0.1978262294209248, \
          0.2618681572601245, \
          0.5403056133189508, \
          0.2618681572601245, \
          0.5403056133189508, \
          0.1978262294209248, \
          0.0486805622526683, \
          0.0065324588746805, \
          0.9447869788726512, \
          0.0065324588746805, \
          0.9447869788726512, \
          0.0486805622526683, \
          0.0486805622526683, \
          0.0065324588746805, \
          0.9447869788726512, \
          0.0065324588746805, \
          0.9447869788726512, \
          0.0486805622526683, \
          0.0912977133028943, \
          0.3702624031957258, \
          0.5384398835013798, \
          0.3702624031957258, \
          0.5384398835013798, \
          0.0912977133028943, \
          0.0912977133028943, \
          0.3702624031957258, \
          0.5384398835013798, \
          0.3702624031957258, \
          0.5384398835013798, \
          0.0912977133028943, \
          0.0373008369533812, \
          0.1377079768509805, \
          0.8249911861956383, \
          0.1377079768509805, \
          0.8249911861956383, \
          0.0373008369533812, \
          0.0373008369533812, \
          0.1377079768509805, \
          0.8249911861956383, \
          0.1377079768509805, \
          0.8249911861956383, \
          0.0373008369533812, \
          0.1635654688089934, \
          0.4784950101267365, \
          0.3579395210642701, \
          0.4784950101267365, \
          0.3579395210642701, \
          0.1635654688089934, \
          0.1635654688089934, \
          0.4784950101267365, \
          0.3579395210642701, \
          0.4784950101267365, \
          0.3579395210642701, \
          0.1635654688089934, \
          0.0249615816629217, \
          0.3278240979071815, \
          0.6472143204298968, \
          0.3278240979071815, \
          0.6472143204298968, \
          0.0249615816629217, \
          0.0249615816629217, \
          0.3278240979071815, \
          0.6472143204298968, \
          0.3278240979071815, \
          0.6472143204298968, \
          0.0249615816629217, \
          0.0871302288391398, \
          0.3475735063324100, \
          0.5652962648284502, \
          0.3475735063324100, \
          0.5652962648284502, \
          0.0871302288391398, \
          0.0871302288391398, \
          0.3475735063324100, \
          0.5652962648284502, \
          0.3475735063324100, \
          0.5652962648284502, \
          0.0871302288391398, \
          0.0128395677390919, \
          0.1096327891311607, \
          0.8775276431297473, \
          0.1096327891311607, \
          0.8775276431297473, \
          0.0128395677390919, \
          0.0128395677390919, \
          0.1096327891311607, \
          0.8775276431297473, \
          0.1096327891311607, \
          0.8775276431297473, \
          0.0128395677390919, \
          0.0849045675529205, \
          0.2078784801536998, \
          0.7072169522933797, \
          0.2078784801536998, \
          0.7072169522933797, \
          0.0849045675529205, \
          0.0849045675529205, \
          0.2078784801536998, \
          0.7072169522933797, \
          0.2078784801536998, \
          0.7072169522933797, \
          0.0849045675529205, \
          0.0143045787175747, \
          0.1953330193360589, \
          0.7903624019463664, \
          0.1953330193360589, \
          0.7903624019463664, \
          0.0143045787175747, \
          0.0143045787175747, \
          0.1953330193360589, \
          0.7903624019463664, \
          0.1953330193360589, \
          0.7903624019463664, \
          0.0143045787175747 ] )

  z = np.array ( [ \
          0.8401109114804578, \
          0.1598890885195422, \
          0.9524833096339549, \
          0.0475166903660451, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5508863349912149, \
          0.5508863349912149, \
          0.5508863349912149, \
          0.4491136650087851, \
          0.4491136650087851, \
          0.4491136650087851, \
          0.8664406024867690, \
          0.8664406024867690, \
          0.8664406024867690, \
          0.1335593975132310, \
          0.1335593975132310, \
          0.1335593975132310, \
          0.3291089745865182, \
          0.3291089745865182, \
          0.3291089745865182, \
          0.6708910254134818, \
          0.6708910254134818, \
          0.6708910254134818, \
          0.4287046442912852, \
          0.4287046442912852, \
          0.4287046442912852, \
          0.5712953557087147, \
          0.5712953557087147, \
          0.5712953557087147, \
          0.8306396134186287, \
          0.8306396134186287, \
          0.8306396134186287, \
          0.1693603865813713, \
          0.1693603865813713, \
          0.1693603865813713, \
          0.9826991514876333, \
          0.9826991514876333, \
          0.9826991514876333, \
          0.0173008485123666, \
          0.0173008485123666, \
          0.0173008485123666, \
          0.9603593395589844, \
          0.9603593395589844, \
          0.9603593395589844, \
          0.0396406604410156, \
          0.0396406604410156, \
          0.0396406604410156, \
          0.9264398795821308, \
          0.9264398795821308, \
          0.9264398795821308, \
          0.0735601204178692, \
          0.0735601204178692, \
          0.0735601204178692, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9025925504145782, \
          0.9025925504145782, \
          0.9025925504145782, \
          0.9025925504145782, \
          0.9025925504145782, \
          0.9025925504145782, \
          0.0974074495854217, \
          0.0974074495854217, \
          0.0974074495854217, \
          0.0974074495854217, \
          0.0974074495854217, \
          0.0974074495854217, \
          0.7775063050268207, \
          0.7775063050268207, \
          0.7775063050268207, \
          0.7775063050268207, \
          0.7775063050268207, \
          0.7775063050268207, \
          0.2224936949731793, \
          0.2224936949731793, \
          0.2224936949731793, \
          0.2224936949731793, \
          0.2224936949731793, \
          0.2224936949731793, \
          0.7482800508722226, \
          0.7482800508722226, \
          0.7482800508722226, \
          0.7482800508722226, \
          0.7482800508722226, \
          0.7482800508722226, \
          0.2517199491277774, \
          0.2517199491277774, \
          0.2517199491277774, \
          0.2517199491277774, \
          0.2517199491277774, \
          0.2517199491277774, \
          0.6403701196964353, \
          0.6403701196964353, \
          0.6403701196964353, \
          0.6403701196964353, \
          0.6403701196964353, \
          0.6403701196964353, \
          0.3596298803035647, \
          0.3596298803035647, \
          0.3596298803035647, \
          0.3596298803035647, \
          0.3596298803035647, \
          0.3596298803035647, \
          0.7769630399535563, \
          0.7769630399535563, \
          0.7769630399535563, \
          0.7769630399535563, \
          0.7769630399535563, \
          0.7769630399535563, \
          0.2230369600464437, \
          0.2230369600464437, \
          0.2230369600464437, \
          0.2230369600464437, \
          0.2230369600464437, \
          0.2230369600464437, \
          0.9565498865251021, \
          0.9565498865251021, \
          0.9565498865251021, \
          0.9565498865251021, \
          0.9565498865251021, \
          0.9565498865251021, \
          0.0434501134748980, \
          0.0434501134748980, \
          0.0434501134748980, \
          0.0434501134748980, \
          0.0434501134748980, \
          0.0434501134748980, \
          0.9928793309605464, \
          0.9928793309605464, \
          0.9928793309605464, \
          0.9928793309605464, \
          0.9928793309605464, \
          0.9928793309605464, \
          0.0071206690394536, \
          0.0071206690394536, \
          0.0071206690394536, \
          0.0071206690394536, \
          0.0071206690394536, \
          0.0071206690394536, \
          0.9880631245383409, \
          0.9880631245383409, \
          0.9880631245383409, \
          0.9880631245383409, \
          0.9880631245383409, \
          0.9880631245383409, \
          0.0119368754616592, \
          0.0119368754616592, \
          0.0119368754616592, \
          0.0119368754616592, \
          0.0119368754616592, \
          0.0119368754616592, \
          0.9154311485206492, \
          0.9154311485206492, \
          0.9154311485206492, \
          0.9154311485206492, \
          0.9154311485206492, \
          0.9154311485206492, \
          0.0845688514793507, \
          0.0845688514793507, \
          0.0845688514793507, \
          0.0845688514793507, \
          0.0845688514793507, \
          0.0845688514793507, \
          0.9705250000766562, \
          0.9705250000766562, \
          0.9705250000766562, \
          0.9705250000766562, \
          0.9705250000766562, \
          0.9705250000766562, \
          0.0294749999233438, \
          0.0294749999233438, \
          0.0294749999233438, \
          0.0294749999233438, \
          0.0294749999233438, \
          0.0294749999233438, \
          0.3853017195325944, \
          0.3853017195325944, \
          0.3853017195325944, \
          0.3853017195325944, \
          0.3853017195325944, \
          0.3853017195325944, \
          0.6146982804674056, \
          0.6146982804674056, \
          0.6146982804674056, \
          0.6146982804674056, \
          0.6146982804674056, \
          0.6146982804674056, \
          0.6900924303976952, \
          0.6900924303976952, \
          0.6900924303976952, \
          0.6900924303976952, \
          0.6900924303976952, \
          0.6900924303976952, \
          0.3099075696023049, \
          0.3099075696023049, \
          0.3099075696023049, \
          0.3099075696023049, \
          0.3099075696023049, \
          0.3099075696023049, \
          0.7816502945768592, \
          0.7816502945768592, \
          0.7816502945768592, \
          0.7816502945768592, \
          0.7816502945768592, \
          0.7816502945768592, \
          0.2183497054231408, \
          0.2183497054231408, \
          0.2183497054231408, \
          0.2183497054231408, \
          0.2183497054231408, \
          0.2183497054231408, \
          0.8883851866879513, \
          0.8883851866879513, \
          0.8883851866879513, \
          0.8883851866879513, \
          0.8883851866879513, \
          0.8883851866879513, \
          0.1116148133120487, \
          0.1116148133120487, \
          0.1116148133120487, \
          0.1116148133120487, \
          0.1116148133120487, \
          0.1116148133120487 ] )

  w = np.array ( [ \
          0.0109734885358618, \
          0.0109734885358618, \
          0.0032613958307349, \
          0.0032613958307349, \
          0.0093941405464380, \
          0.0093941405464380, \
          0.0093941405464380, \
          0.0074721925384407, \
          0.0074721925384407, \
          0.0074721925384407, \
          0.0011251486610045, \
          0.0011251486610045, \
          0.0011251486610045, \
          0.0040278942594456, \
          0.0040278942594456, \
          0.0040278942594456, \
          0.0046987405274126, \
          0.0046987405274126, \
          0.0046987405274126, \
          0.0046987405274126, \
          0.0046987405274126, \
          0.0046987405274126, \
          0.0044231068731859, \
          0.0044231068731859, \
          0.0044231068731859, \
          0.0044231068731859, \
          0.0044231068731859, \
          0.0044231068731859, \
          0.0119087119167916, \
          0.0119087119167916, \
          0.0119087119167916, \
          0.0119087119167916, \
          0.0119087119167916, \
          0.0119087119167916, \
          0.0034190583552652, \
          0.0034190583552652, \
          0.0034190583552652, \
          0.0034190583552652, \
          0.0034190583552652, \
          0.0034190583552652, \
          0.0076078695830692, \
          0.0076078695830692, \
          0.0076078695830692, \
          0.0076078695830692, \
          0.0076078695830692, \
          0.0076078695830692, \
          0.0034877218143443, \
          0.0034877218143443, \
          0.0034877218143443, \
          0.0034877218143443, \
          0.0034877218143443, \
          0.0034877218143443, \
          0.0041265711237682, \
          0.0041265711237682, \
          0.0041265711237682, \
          0.0041265711237682, \
          0.0041265711237682, \
          0.0041265711237682, \
          0.0020552290439392, \
          0.0020552290439392, \
          0.0020552290439392, \
          0.0020552290439392, \
          0.0020552290439392, \
          0.0020552290439392, \
          0.0053334369811175, \
          0.0053334369811175, \
          0.0053334369811175, \
          0.0053334369811175, \
          0.0053334369811175, \
          0.0053334369811175, \
          0.0045658362940629, \
          0.0045658362940629, \
          0.0045658362940629, \
          0.0045658362940629, \
          0.0045658362940629, \
          0.0045658362940629, \
          0.0045658362940629, \
          0.0045658362940629, \
          0.0045658362940629, \
          0.0045658362940629, \
          0.0045658362940629, \
          0.0045658362940629, \
          0.0005459132755231, \
          0.0005459132755231, \
          0.0005459132755231, \
          0.0005459132755231, \
          0.0005459132755231, \
          0.0005459132755231, \
          0.0005459132755231, \
          0.0005459132755231, \
          0.0005459132755231, \
          0.0005459132755231, \
          0.0005459132755231, \
          0.0005459132755231, \
          0.0043191948291063, \
          0.0043191948291063, \
          0.0043191948291063, \
          0.0043191948291063, \
          0.0043191948291063, \
          0.0043191948291063, \
          0.0043191948291063, \
          0.0043191948291063, \
          0.0043191948291063, \
          0.0043191948291063, \
          0.0043191948291063, \
          0.0043191948291063, \
          0.0053774143502532, \
          0.0053774143502532, \
          0.0053774143502532, \
          0.0053774143502532, \
          0.0053774143502532, \
          0.0053774143502532, \
          0.0053774143502532, \
          0.0053774143502532, \
          0.0053774143502532, \
          0.0053774143502532, \
          0.0053774143502532, \
          0.0053774143502532, \
          0.0071616945998409, \
          0.0071616945998409, \
          0.0071616945998409, \
          0.0071616945998409, \
          0.0071616945998409, \
          0.0071616945998409, \
          0.0071616945998409, \
          0.0071616945998409, \
          0.0071616945998409, \
          0.0071616945998409, \
          0.0071616945998409, \
          0.0071616945998409, \
          0.0005425741614460, \
          0.0005425741614460, \
          0.0005425741614460, \
          0.0005425741614460, \
          0.0005425741614460, \
          0.0005425741614460, \
          0.0005425741614460, \
          0.0005425741614460, \
          0.0005425741614460, \
          0.0005425741614460, \
          0.0005425741614460, \
          0.0005425741614460, \
          0.0014376691849096, \
          0.0014376691849096, \
          0.0014376691849096, \
          0.0014376691849096, \
          0.0014376691849096, \
          0.0014376691849096, \
          0.0014376691849096, \
          0.0014376691849096, \
          0.0014376691849096, \
          0.0014376691849096, \
          0.0014376691849096, \
          0.0014376691849096, \
          0.0011160390387250, \
          0.0011160390387250, \
          0.0011160390387250, \
          0.0011160390387250, \
          0.0011160390387250, \
          0.0011160390387250, \
          0.0011160390387250, \
          0.0011160390387250, \
          0.0011160390387250, \
          0.0011160390387250, \
          0.0011160390387250, \
          0.0011160390387250, \
          0.0048559812857500, \
          0.0048559812857500, \
          0.0048559812857500, \
          0.0048559812857500, \
          0.0048559812857500, \
          0.0048559812857500, \
          0.0048559812857500, \
          0.0048559812857500, \
          0.0048559812857500, \
          0.0048559812857500, \
          0.0048559812857500, \
          0.0048559812857500, \
          0.0017971531168555, \
          0.0017971531168555, \
          0.0017971531168555, \
          0.0017971531168555, \
          0.0017971531168555, \
          0.0017971531168555, \
          0.0017971531168555, \
          0.0017971531168555, \
          0.0017971531168555, \
          0.0017971531168555, \
          0.0017971531168555, \
          0.0017971531168555, \
          0.0096050585986694, \
          0.0096050585986694, \
          0.0096050585986694, \
          0.0096050585986694, \
          0.0096050585986694, \
          0.0096050585986694, \
          0.0096050585986694, \
          0.0096050585986694, \
          0.0096050585986694, \
          0.0096050585986694, \
          0.0096050585986694, \
          0.0096050585986694, \
          0.0027021277312842, \
          0.0027021277312842, \
          0.0027021277312842, \
          0.0027021277312842, \
          0.0027021277312842, \
          0.0027021277312842, \
          0.0027021277312842, \
          0.0027021277312842, \
          0.0027021277312842, \
          0.0027021277312842, \
          0.0027021277312842, \
          0.0027021277312842, \
          0.0055044460347859, \
          0.0055044460347859, \
          0.0055044460347859, \
          0.0055044460347859, \
          0.0055044460347859, \
          0.0055044460347859, \
          0.0055044460347859, \
          0.0055044460347859, \
          0.0055044460347859, \
          0.0055044460347859, \
          0.0055044460347859, \
          0.0055044460347859, \
          0.0023946829935762, \
          0.0023946829935762, \
          0.0023946829935762, \
          0.0023946829935762, \
          0.0023946829935762, \
          0.0023946829935762, \
          0.0023946829935762, \
          0.0023946829935762, \
          0.0023946829935762, \
          0.0023946829935762, \
          0.0023946829935762, \
          0.0023946829935762 ] )

  return x, y, z, w

def rule16 ( ):

#*****************************************************************************80
#
## rule16() returns the prism rule of precision 16.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.0089540840312146, \
          0.0089540840312146, \
          0.9820918319375707, \
          0.0553908100440216, \
          0.0553908100440216, \
          0.8892183799119567, \
          0.3916317627335951, \
          0.3916317627335951, \
          0.2167364745328097, \
          0.0561000778858347, \
          0.0561000778858347, \
          0.8877998442283307, \
          0.0561000778858347, \
          0.0561000778858347, \
          0.8877998442283307, \
          0.2669967593271997, \
          0.2669967593271997, \
          0.4660064813456005, \
          0.2669967593271997, \
          0.2669967593271997, \
          0.4660064813456005, \
          0.1619375672046858, \
          0.1619375672046858, \
          0.6761248655906285, \
          0.1619375672046858, \
          0.1619375672046858, \
          0.6761248655906285, \
          0.4259891438745869, \
          0.4259891438745869, \
          0.1480217122508263, \
          0.4259891438745869, \
          0.4259891438745869, \
          0.1480217122508263, \
          0.4943682456985981, \
          0.4943682456985981, \
          0.0112635086028039, \
          0.4943682456985981, \
          0.4943682456985981, \
          0.0112635086028039, \
          0.4745817664118026, \
          0.4745817664118026, \
          0.0508364671763949, \
          0.4745817664118026, \
          0.4745817664118026, \
          0.0508364671763949, \
          0.2785739189962955, \
          0.2785739189962955, \
          0.4428521620074090, \
          0.2785739189962955, \
          0.2785739189962955, \
          0.4428521620074090, \
          0.1564426776295505, \
          0.1564426776295505, \
          0.6871146447408989, \
          0.1564426776295505, \
          0.1564426776295505, \
          0.6871146447408989, \
          0.4933597406415689, \
          0.4933597406415689, \
          0.0132805187168622, \
          0.4933597406415689, \
          0.4933597406415689, \
          0.0132805187168622, \
          0.5254267651000835, \
          0.0993149454903146, \
          0.5254267651000835, \
          0.3752582894096019, \
          0.0993149454903146, \
          0.3752582894096019, \
          0.3482743570815052, \
          0.0212715561472286, \
          0.3482743570815052, \
          0.6304540867712661, \
          0.0212715561472286, \
          0.6304540867712661, \
          0.1654756461617898, \
          0.0860850979983652, \
          0.1654756461617898, \
          0.7484392558398449, \
          0.0860850979983652, \
          0.7484392558398449, \
          0.1639763763638563, \
          0.0551722290870520, \
          0.1639763763638563, \
          0.7808513945490917, \
          0.0551722290870520, \
          0.7808513945490917, \
          0.1639763763638563, \
          0.0551722290870520, \
          0.1639763763638563, \
          0.7808513945490917, \
          0.0551722290870520, \
          0.7808513945490917, \
          0.0370382522819345, \
          0.0105036665914126, \
          0.0370382522819345, \
          0.9524580811266530, \
          0.0105036665914126, \
          0.9524580811266530, \
          0.0370382522819345, \
          0.0105036665914126, \
          0.0370382522819345, \
          0.9524580811266530, \
          0.0105036665914126, \
          0.9524580811266530, \
          0.6350080118967869, \
          0.0055639594221052, \
          0.6350080118967869, \
          0.3594280286811078, \
          0.0055639594221052, \
          0.3594280286811078, \
          0.6350080118967869, \
          0.0055639594221052, \
          0.6350080118967869, \
          0.3594280286811078, \
          0.0055639594221052, \
          0.3594280286811078, \
          0.1297894012222233, \
          0.0724868197207572, \
          0.1297894012222233, \
          0.7977237790570195, \
          0.0724868197207572, \
          0.7977237790570195, \
          0.1297894012222233, \
          0.0724868197207572, \
          0.1297894012222233, \
          0.7977237790570195, \
          0.0724868197207572, \
          0.7977237790570195, \
          0.3059321030072774, \
          0.0621201882612809, \
          0.3059321030072774, \
          0.6319477087314417, \
          0.0621201882612809, \
          0.6319477087314417, \
          0.3059321030072774, \
          0.0621201882612809, \
          0.3059321030072774, \
          0.6319477087314417, \
          0.0621201882612809, \
          0.6319477087314417, \
          0.1677554820715698, \
          0.2612303617350463, \
          0.1677554820715698, \
          0.5710141561933839, \
          0.2612303617350463, \
          0.5710141561933839, \
          0.1677554820715698, \
          0.2612303617350463, \
          0.1677554820715698, \
          0.5710141561933839, \
          0.2612303617350463, \
          0.5710141561933839, \
          0.0015296219296330, \
          0.0337686922990924, \
          0.0015296219296330, \
          0.9647016857712746, \
          0.0337686922990924, \
          0.9647016857712746, \
          0.0015296219296330, \
          0.0337686922990924, \
          0.0015296219296330, \
          0.9647016857712746, \
          0.0337686922990924, \
          0.9647016857712746, \
          0.3532796606132861, \
          0.0949242221588698, \
          0.3532796606132861, \
          0.5517961172278441, \
          0.0949242221588698, \
          0.5517961172278441, \
          0.3532796606132861, \
          0.0949242221588698, \
          0.3532796606132861, \
          0.5517961172278441, \
          0.0949242221588698, \
          0.5517961172278441, \
          0.0959262325920420, \
          0.0248817170289358, \
          0.0959262325920420, \
          0.8791920503790223, \
          0.0248817170289358, \
          0.8791920503790223, \
          0.0959262325920420, \
          0.0248817170289358, \
          0.0959262325920420, \
          0.8791920503790223, \
          0.0248817170289358, \
          0.8791920503790223, \
          0.4963305263335406, \
          0.1757029526928022, \
          0.4963305263335406, \
          0.3279665209736572, \
          0.1757029526928022, \
          0.3279665209736572, \
          0.4963305263335406, \
          0.1757029526928022, \
          0.4963305263335406, \
          0.3279665209736572, \
          0.1757029526928022, \
          0.3279665209736572, \
          0.2738501035919119, \
          0.0140786122092260, \
          0.2738501035919119, \
          0.7120712841988621, \
          0.0140786122092260, \
          0.7120712841988621, \
          0.2738501035919119, \
          0.0140786122092260, \
          0.2738501035919119, \
          0.7120712841988621, \
          0.0140786122092260, \
          0.7120712841988621, \
          0.3828844998895772, \
          0.0565171623200343, \
          0.3828844998895772, \
          0.5605983377903885, \
          0.0565171623200343, \
          0.5605983377903885, \
          0.3828844998895772, \
          0.0565171623200343, \
          0.3828844998895772, \
          0.5605983377903885, \
          0.0565171623200343, \
          0.5605983377903885, \
          0.0899365323953004, \
          0.0192412570201629, \
          0.0899365323953004, \
          0.8908222105845367, \
          0.0192412570201629, \
          0.8908222105845367, \
          0.0899365323953004, \
          0.0192412570201629, \
          0.0899365323953004, \
          0.8908222105845367, \
          0.0192412570201629, \
          0.8908222105845367, \
          0.2516074150213084, \
          0.0611370184542401, \
          0.2516074150213084, \
          0.6872555665244514, \
          0.0611370184542401, \
          0.6872555665244514, \
          0.2516074150213084, \
          0.0611370184542401, \
          0.2516074150213084, \
          0.6872555665244514, \
          0.0611370184542401, \
          0.6872555665244514, \
          0.1524244609819593, \
          0.0050182699561948, \
          0.1524244609819593, \
          0.8425572690618459, \
          0.0050182699561948, \
          0.8425572690618459, \
          0.1524244609819593, \
          0.0050182699561948, \
          0.1524244609819593, \
          0.8425572690618459, \
          0.0050182699561948, \
          0.8425572690618459, \
          0.2475011786624472, \
          0.1365910574355268, \
          0.2475011786624472, \
          0.6159077639020261, \
          0.1365910574355268, \
          0.6159077639020261, \
          0.2475011786624472, \
          0.1365910574355268, \
          0.2475011786624472, \
          0.6159077639020261, \
          0.1365910574355268, \
          0.6159077639020261, \
          0.7591852986956938, \
          0.0173543718109579, \
          0.7591852986956938, \
          0.2234603294933483, \
          0.0173543718109579, \
          0.2234603294933483, \
          0.7591852986956938, \
          0.0173543718109579, \
          0.7591852986956938, \
          0.2234603294933483, \
          0.0173543718109579, \
          0.2234603294933483 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.0089540840312146, \
          0.9820918319375707, \
          0.0089540840312146, \
          0.0553908100440216, \
          0.8892183799119567, \
          0.0553908100440216, \
          0.3916317627335951, \
          0.2167364745328097, \
          0.3916317627335951, \
          0.0561000778858347, \
          0.8877998442283307, \
          0.0561000778858347, \
          0.0561000778858347, \
          0.8877998442283307, \
          0.0561000778858347, \
          0.2669967593271997, \
          0.4660064813456005, \
          0.2669967593271997, \
          0.2669967593271997, \
          0.4660064813456005, \
          0.2669967593271997, \
          0.1619375672046858, \
          0.6761248655906285, \
          0.1619375672046858, \
          0.1619375672046858, \
          0.6761248655906285, \
          0.1619375672046858, \
          0.4259891438745869, \
          0.1480217122508263, \
          0.4259891438745869, \
          0.4259891438745869, \
          0.1480217122508263, \
          0.4259891438745869, \
          0.4943682456985981, \
          0.0112635086028039, \
          0.4943682456985981, \
          0.4943682456985981, \
          0.0112635086028039, \
          0.4943682456985981, \
          0.4745817664118026, \
          0.0508364671763949, \
          0.4745817664118026, \
          0.4745817664118026, \
          0.0508364671763949, \
          0.4745817664118026, \
          0.2785739189962955, \
          0.4428521620074090, \
          0.2785739189962955, \
          0.2785739189962955, \
          0.4428521620074090, \
          0.2785739189962955, \
          0.1564426776295505, \
          0.6871146447408989, \
          0.1564426776295505, \
          0.1564426776295505, \
          0.6871146447408989, \
          0.1564426776295505, \
          0.4933597406415689, \
          0.0132805187168622, \
          0.4933597406415689, \
          0.4933597406415689, \
          0.0132805187168622, \
          0.4933597406415689, \
          0.0993149454903146, \
          0.5254267651000835, \
          0.3752582894096019, \
          0.5254267651000835, \
          0.3752582894096019, \
          0.0993149454903146, \
          0.0212715561472286, \
          0.3482743570815052, \
          0.6304540867712661, \
          0.3482743570815052, \
          0.6304540867712661, \
          0.0212715561472286, \
          0.0860850979983652, \
          0.1654756461617898, \
          0.7484392558398449, \
          0.1654756461617898, \
          0.7484392558398449, \
          0.0860850979983652, \
          0.0551722290870520, \
          0.1639763763638563, \
          0.7808513945490917, \
          0.1639763763638563, \
          0.7808513945490917, \
          0.0551722290870520, \
          0.0551722290870520, \
          0.1639763763638563, \
          0.7808513945490917, \
          0.1639763763638563, \
          0.7808513945490917, \
          0.0551722290870520, \
          0.0105036665914126, \
          0.0370382522819345, \
          0.9524580811266530, \
          0.0370382522819345, \
          0.9524580811266530, \
          0.0105036665914126, \
          0.0105036665914126, \
          0.0370382522819345, \
          0.9524580811266530, \
          0.0370382522819345, \
          0.9524580811266530, \
          0.0105036665914126, \
          0.0055639594221052, \
          0.6350080118967869, \
          0.3594280286811078, \
          0.6350080118967869, \
          0.3594280286811078, \
          0.0055639594221052, \
          0.0055639594221052, \
          0.6350080118967869, \
          0.3594280286811078, \
          0.6350080118967869, \
          0.3594280286811078, \
          0.0055639594221052, \
          0.0724868197207572, \
          0.1297894012222233, \
          0.7977237790570195, \
          0.1297894012222233, \
          0.7977237790570195, \
          0.0724868197207572, \
          0.0724868197207572, \
          0.1297894012222233, \
          0.7977237790570195, \
          0.1297894012222233, \
          0.7977237790570195, \
          0.0724868197207572, \
          0.0621201882612809, \
          0.3059321030072774, \
          0.6319477087314417, \
          0.3059321030072774, \
          0.6319477087314417, \
          0.0621201882612809, \
          0.0621201882612809, \
          0.3059321030072774, \
          0.6319477087314417, \
          0.3059321030072774, \
          0.6319477087314417, \
          0.0621201882612809, \
          0.2612303617350463, \
          0.1677554820715698, \
          0.5710141561933839, \
          0.1677554820715698, \
          0.5710141561933839, \
          0.2612303617350463, \
          0.2612303617350463, \
          0.1677554820715698, \
          0.5710141561933839, \
          0.1677554820715698, \
          0.5710141561933839, \
          0.2612303617350463, \
          0.0337686922990924, \
          0.0015296219296330, \
          0.9647016857712746, \
          0.0015296219296330, \
          0.9647016857712746, \
          0.0337686922990924, \
          0.0337686922990924, \
          0.0015296219296330, \
          0.9647016857712746, \
          0.0015296219296330, \
          0.9647016857712746, \
          0.0337686922990924, \
          0.0949242221588698, \
          0.3532796606132861, \
          0.5517961172278441, \
          0.3532796606132861, \
          0.5517961172278441, \
          0.0949242221588698, \
          0.0949242221588698, \
          0.3532796606132861, \
          0.5517961172278441, \
          0.3532796606132861, \
          0.5517961172278441, \
          0.0949242221588698, \
          0.0248817170289358, \
          0.0959262325920420, \
          0.8791920503790223, \
          0.0959262325920420, \
          0.8791920503790223, \
          0.0248817170289358, \
          0.0248817170289358, \
          0.0959262325920420, \
          0.8791920503790223, \
          0.0959262325920420, \
          0.8791920503790223, \
          0.0248817170289358, \
          0.1757029526928022, \
          0.4963305263335406, \
          0.3279665209736572, \
          0.4963305263335406, \
          0.3279665209736572, \
          0.1757029526928022, \
          0.1757029526928022, \
          0.4963305263335406, \
          0.3279665209736572, \
          0.4963305263335406, \
          0.3279665209736572, \
          0.1757029526928022, \
          0.0140786122092260, \
          0.2738501035919119, \
          0.7120712841988621, \
          0.2738501035919119, \
          0.7120712841988621, \
          0.0140786122092260, \
          0.0140786122092260, \
          0.2738501035919119, \
          0.7120712841988621, \
          0.2738501035919119, \
          0.7120712841988621, \
          0.0140786122092260, \
          0.0565171623200343, \
          0.3828844998895772, \
          0.5605983377903885, \
          0.3828844998895772, \
          0.5605983377903885, \
          0.0565171623200343, \
          0.0565171623200343, \
          0.3828844998895772, \
          0.5605983377903885, \
          0.3828844998895772, \
          0.5605983377903885, \
          0.0565171623200343, \
          0.0192412570201629, \
          0.0899365323953004, \
          0.8908222105845367, \
          0.0899365323953004, \
          0.8908222105845367, \
          0.0192412570201629, \
          0.0192412570201629, \
          0.0899365323953004, \
          0.8908222105845367, \
          0.0899365323953004, \
          0.8908222105845367, \
          0.0192412570201629, \
          0.0611370184542401, \
          0.2516074150213084, \
          0.6872555665244514, \
          0.2516074150213084, \
          0.6872555665244514, \
          0.0611370184542401, \
          0.0611370184542401, \
          0.2516074150213084, \
          0.6872555665244514, \
          0.2516074150213084, \
          0.6872555665244514, \
          0.0611370184542401, \
          0.0050182699561948, \
          0.1524244609819593, \
          0.8425572690618459, \
          0.1524244609819593, \
          0.8425572690618459, \
          0.0050182699561948, \
          0.0050182699561948, \
          0.1524244609819593, \
          0.8425572690618459, \
          0.1524244609819593, \
          0.8425572690618459, \
          0.0050182699561948, \
          0.1365910574355268, \
          0.2475011786624472, \
          0.6159077639020261, \
          0.2475011786624472, \
          0.6159077639020261, \
          0.1365910574355268, \
          0.1365910574355268, \
          0.2475011786624472, \
          0.6159077639020261, \
          0.2475011786624472, \
          0.6159077639020261, \
          0.1365910574355268, \
          0.0173543718109579, \
          0.7591852986956938, \
          0.2234603294933483, \
          0.7591852986956938, \
          0.2234603294933483, \
          0.0173543718109579, \
          0.0173543718109579, \
          0.7591852986956938, \
          0.2234603294933483, \
          0.7591852986956938, \
          0.2234603294933483, \
          0.0173543718109579 ] )

  z = np.array ( [ \
          0.8403117926958672, \
          0.1596882073041329, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8842725336194912, \
          0.8842725336194912, \
          0.8842725336194912, \
          0.1157274663805087, \
          0.1157274663805087, \
          0.1157274663805087, \
          0.6593583359504520, \
          0.6593583359504520, \
          0.6593583359504520, \
          0.3406416640495479, \
          0.3406416640495479, \
          0.3406416640495479, \
          0.8712606670369063, \
          0.8712606670369063, \
          0.8712606670369063, \
          0.1287393329630936, \
          0.1287393329630936, \
          0.1287393329630936, \
          0.2304229580101690, \
          0.2304229580101690, \
          0.2304229580101690, \
          0.7695770419898310, \
          0.7695770419898310, \
          0.7695770419898310, \
          0.6455038513606328, \
          0.6455038513606328, \
          0.6455038513606328, \
          0.3544961486393671, \
          0.3544961486393671, \
          0.3544961486393671, \
          0.8851421910096543, \
          0.8851421910096543, \
          0.8851421910096543, \
          0.1148578089903457, \
          0.1148578089903457, \
          0.1148578089903457, \
          0.9818829756657210, \
          0.9818829756657210, \
          0.9818829756657210, \
          0.0181170243342790, \
          0.0181170243342790, \
          0.0181170243342790, \
          0.9850118189004804, \
          0.9850118189004804, \
          0.9850118189004804, \
          0.0149881810995195, \
          0.0149881810995195, \
          0.0149881810995195, \
          0.9701315317214787, \
          0.9701315317214787, \
          0.9701315317214787, \
          0.0298684682785212, \
          0.0298684682785212, \
          0.0298684682785212, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9387595239709540, \
          0.9387595239709540, \
          0.9387595239709540, \
          0.9387595239709540, \
          0.9387595239709540, \
          0.9387595239709540, \
          0.0612404760290460, \
          0.0612404760290460, \
          0.0612404760290460, \
          0.0612404760290460, \
          0.0612404760290460, \
          0.0612404760290460, \
          0.7620680922209941, \
          0.7620680922209941, \
          0.7620680922209941, \
          0.7620680922209941, \
          0.7620680922209941, \
          0.7620680922209941, \
          0.2379319077790059, \
          0.2379319077790059, \
          0.2379319077790059, \
          0.2379319077790059, \
          0.2379319077790059, \
          0.2379319077790059, \
          0.8273450356745347, \
          0.8273450356745347, \
          0.8273450356745347, \
          0.8273450356745347, \
          0.8273450356745347, \
          0.8273450356745347, \
          0.1726549643254653, \
          0.1726549643254653, \
          0.1726549643254653, \
          0.1726549643254653, \
          0.1726549643254653, \
          0.1726549643254653, \
          0.7401886228316812, \
          0.7401886228316812, \
          0.7401886228316812, \
          0.7401886228316812, \
          0.7401886228316812, \
          0.7401886228316812, \
          0.2598113771683188, \
          0.2598113771683188, \
          0.2598113771683188, \
          0.2598113771683188, \
          0.2598113771683188, \
          0.2598113771683188, \
          0.9210357305129615, \
          0.9210357305129615, \
          0.9210357305129615, \
          0.9210357305129615, \
          0.9210357305129615, \
          0.9210357305129615, \
          0.0789642694870386, \
          0.0789642694870386, \
          0.0789642694870386, \
          0.0789642694870386, \
          0.0789642694870386, \
          0.0789642694870386, \
          0.8233326926574609, \
          0.8233326926574609, \
          0.8233326926574609, \
          0.8233326926574609, \
          0.8233326926574609, \
          0.8233326926574609, \
          0.1766673073425390, \
          0.1766673073425390, \
          0.1766673073425390, \
          0.1766673073425390, \
          0.1766673073425390, \
          0.1766673073425390, \
          0.9478854137232893, \
          0.9478854137232893, \
          0.9478854137232893, \
          0.9478854137232893, \
          0.9478854137232893, \
          0.9478854137232893, \
          0.0521145862767107, \
          0.0521145862767107, \
          0.0521145862767107, \
          0.0521145862767107, \
          0.0521145862767107, \
          0.0521145862767107, \
          0.9916391512107949, \
          0.9916391512107949, \
          0.9916391512107949, \
          0.9916391512107949, \
          0.9916391512107949, \
          0.9916391512107949, \
          0.0083608487892050, \
          0.0083608487892050, \
          0.0083608487892050, \
          0.0083608487892050, \
          0.0083608487892050, \
          0.0083608487892050, \
          0.9898679390727328, \
          0.9898679390727328, \
          0.9898679390727328, \
          0.9898679390727328, \
          0.9898679390727328, \
          0.9898679390727328, \
          0.0101320609272672, \
          0.0101320609272672, \
          0.0101320609272672, \
          0.0101320609272672, \
          0.0101320609272672, \
          0.0101320609272672, \
          0.9305712292308971, \
          0.9305712292308971, \
          0.9305712292308971, \
          0.9305712292308971, \
          0.9305712292308971, \
          0.9305712292308971, \
          0.0694287707691029, \
          0.0694287707691029, \
          0.0694287707691029, \
          0.0694287707691029, \
          0.0694287707691029, \
          0.0694287707691029, \
          0.9758011913142881, \
          0.9758011913142881, \
          0.9758011913142881, \
          0.9758011913142881, \
          0.9758011913142881, \
          0.9758011913142881, \
          0.0241988086857118, \
          0.0241988086857118, \
          0.0241988086857118, \
          0.0241988086857118, \
          0.0241988086857118, \
          0.0241988086857118, \
          0.3036894659036268, \
          0.3036894659036268, \
          0.3036894659036268, \
          0.3036894659036268, \
          0.3036894659036268, \
          0.3036894659036268, \
          0.6963105340963731, \
          0.6963105340963731, \
          0.6963105340963731, \
          0.6963105340963731, \
          0.6963105340963731, \
          0.6963105340963731, \
          0.6138684175664644, \
          0.6138684175664644, \
          0.6138684175664644, \
          0.6138684175664644, \
          0.6138684175664644, \
          0.6138684175664644, \
          0.3861315824335356, \
          0.3861315824335356, \
          0.3861315824335356, \
          0.3861315824335356, \
          0.3861315824335356, \
          0.3861315824335356, \
          0.7885638236910046, \
          0.7885638236910046, \
          0.7885638236910046, \
          0.7885638236910046, \
          0.7885638236910046, \
          0.7885638236910046, \
          0.2114361763089954, \
          0.2114361763089954, \
          0.2114361763089954, \
          0.2114361763089954, \
          0.2114361763089954, \
          0.2114361763089954, \
          0.8514618541948253, \
          0.8514618541948253, \
          0.8514618541948253, \
          0.8514618541948253, \
          0.8514618541948253, \
          0.8514618541948253, \
          0.1485381458051747, \
          0.1485381458051747, \
          0.1485381458051747, \
          0.1485381458051747, \
          0.1485381458051747, \
          0.1485381458051747, \
          0.3722497735842279, \
          0.3722497735842279, \
          0.3722497735842279, \
          0.3722497735842279, \
          0.3722497735842279, \
          0.3722497735842279, \
          0.6277502264157721, \
          0.6277502264157721, \
          0.6277502264157721, \
          0.6277502264157721, \
          0.6277502264157721, \
          0.6277502264157721, \
          0.6329858368666343, \
          0.6329858368666343, \
          0.6329858368666343, \
          0.6329858368666343, \
          0.6329858368666343, \
          0.6329858368666343, \
          0.3670141631333657, \
          0.3670141631333657, \
          0.3670141631333657, \
          0.3670141631333657, \
          0.3670141631333657, \
          0.3670141631333657 ] )

  w = np.array ( [ \
          0.0126082800938750, \
          0.0126082800938750, \
          0.0005804416586274, \
          0.0005804416586274, \
          0.0005804416586274, \
          0.0014515275277035, \
          0.0014515275277035, \
          0.0014515275277035, \
          0.0110392519457591, \
          0.0110392519457591, \
          0.0110392519457591, \
          0.0023896607884456, \
          0.0023896607884456, \
          0.0023896607884456, \
          0.0023896607884456, \
          0.0023896607884456, \
          0.0023896607884456, \
          0.0111852959227564, \
          0.0111852959227564, \
          0.0111852959227564, \
          0.0111852959227564, \
          0.0111852959227564, \
          0.0111852959227564, \
          0.0044527106261489, \
          0.0044527106261489, \
          0.0044527106261489, \
          0.0044527106261489, \
          0.0044527106261489, \
          0.0044527106261489, \
          0.0099310429205233, \
          0.0099310429205233, \
          0.0099310429205233, \
          0.0099310429205233, \
          0.0099310429205233, \
          0.0099310429205233, \
          0.0027983315098658, \
          0.0027983315098658, \
          0.0027983315098658, \
          0.0027983315098658, \
          0.0027983315098658, \
          0.0027983315098658, \
          0.0045950791440008, \
          0.0045950791440008, \
          0.0045950791440008, \
          0.0045950791440008, \
          0.0045950791440008, \
          0.0045950791440008, \
          0.0026497419827358, \
          0.0026497419827358, \
          0.0026497419827358, \
          0.0026497419827358, \
          0.0026497419827358, \
          0.0026497419827358, \
          0.0023791749450044, \
          0.0023791749450044, \
          0.0023791749450044, \
          0.0023791749450044, \
          0.0023791749450044, \
          0.0023791749450044, \
          0.0012902115379941, \
          0.0012902115379941, \
          0.0012902115379941, \
          0.0012902115379941, \
          0.0012902115379941, \
          0.0012902115379941, \
          0.0071749704457678, \
          0.0071749704457678, \
          0.0071749704457678, \
          0.0071749704457678, \
          0.0071749704457678, \
          0.0071749704457678, \
          0.0039041969129065, \
          0.0039041969129065, \
          0.0039041969129065, \
          0.0039041969129065, \
          0.0039041969129065, \
          0.0039041969129065, \
          0.0058968479213494, \
          0.0058968479213494, \
          0.0058968479213494, \
          0.0058968479213494, \
          0.0058968479213494, \
          0.0058968479213494, \
          0.0024349402323106, \
          0.0024349402323106, \
          0.0024349402323106, \
          0.0024349402323106, \
          0.0024349402323106, \
          0.0024349402323106, \
          0.0024349402323106, \
          0.0024349402323106, \
          0.0024349402323106, \
          0.0024349402323106, \
          0.0024349402323106, \
          0.0024349402323106, \
          0.0007867926281754, \
          0.0007867926281754, \
          0.0007867926281754, \
          0.0007867926281754, \
          0.0007867926281754, \
          0.0007867926281754, \
          0.0007867926281754, \
          0.0007867926281754, \
          0.0007867926281754, \
          0.0007867926281754, \
          0.0007867926281754, \
          0.0007867926281754, \
          0.0019733458950933, \
          0.0019733458950933, \
          0.0019733458950933, \
          0.0019733458950933, \
          0.0019733458950933, \
          0.0019733458950933, \
          0.0019733458950933, \
          0.0019733458950933, \
          0.0019733458950933, \
          0.0019733458950933, \
          0.0019733458950933, \
          0.0019733458950933, \
          0.0039028044764867, \
          0.0039028044764867, \
          0.0039028044764867, \
          0.0039028044764867, \
          0.0039028044764867, \
          0.0039028044764867, \
          0.0039028044764867, \
          0.0039028044764867, \
          0.0039028044764867, \
          0.0039028044764867, \
          0.0039028044764867, \
          0.0039028044764867, \
          0.0028651948489933, \
          0.0028651948489933, \
          0.0028651948489933, \
          0.0028651948489933, \
          0.0028651948489933, \
          0.0028651948489933, \
          0.0028651948489933, \
          0.0028651948489933, \
          0.0028651948489933, \
          0.0028651948489933, \
          0.0028651948489933, \
          0.0028651948489933, \
          0.0042658629737291, \
          0.0042658629737291, \
          0.0042658629737291, \
          0.0042658629737291, \
          0.0042658629737291, \
          0.0042658629737291, \
          0.0042658629737291, \
          0.0042658629737291, \
          0.0042658629737291, \
          0.0042658629737291, \
          0.0042658629737291, \
          0.0042658629737291, \
          0.0002763846307136, \
          0.0002763846307136, \
          0.0002763846307136, \
          0.0002763846307136, \
          0.0002763846307136, \
          0.0002763846307136, \
          0.0002763846307136, \
          0.0002763846307136, \
          0.0002763846307136, \
          0.0002763846307136, \
          0.0002763846307136, \
          0.0002763846307136, \
          0.0015947204945141, \
          0.0015947204945141, \
          0.0015947204945141, \
          0.0015947204945141, \
          0.0015947204945141, \
          0.0015947204945141, \
          0.0015947204945141, \
          0.0015947204945141, \
          0.0015947204945141, \
          0.0015947204945141, \
          0.0015947204945141, \
          0.0015947204945141, \
          0.0005967018601525, \
          0.0005967018601525, \
          0.0005967018601525, \
          0.0005967018601525, \
          0.0005967018601525, \
          0.0005967018601525, \
          0.0005967018601525, \
          0.0005967018601525, \
          0.0005967018601525, \
          0.0005967018601525, \
          0.0005967018601525, \
          0.0005967018601525, \
          0.0050890108573681, \
          0.0050890108573681, \
          0.0050890108573681, \
          0.0050890108573681, \
          0.0050890108573681, \
          0.0050890108573681, \
          0.0050890108573681, \
          0.0050890108573681, \
          0.0050890108573681, \
          0.0050890108573681, \
          0.0050890108573681, \
          0.0050890108573681, \
          0.0010232527285653, \
          0.0010232527285653, \
          0.0010232527285653, \
          0.0010232527285653, \
          0.0010232527285653, \
          0.0010232527285653, \
          0.0010232527285653, \
          0.0010232527285653, \
          0.0010232527285653, \
          0.0010232527285653, \
          0.0010232527285653, \
          0.0010232527285653, \
          0.0048336118379361, \
          0.0048336118379361, \
          0.0048336118379361, \
          0.0048336118379361, \
          0.0048336118379361, \
          0.0048336118379361, \
          0.0048336118379361, \
          0.0048336118379361, \
          0.0048336118379361, \
          0.0048336118379361, \
          0.0048336118379361, \
          0.0048336118379361, \
          0.0022565704494986, \
          0.0022565704494986, \
          0.0022565704494986, \
          0.0022565704494986, \
          0.0022565704494986, \
          0.0022565704494986, \
          0.0022565704494986, \
          0.0022565704494986, \
          0.0022565704494986, \
          0.0022565704494986, \
          0.0022565704494986, \
          0.0022565704494986, \
          0.0043942174418955, \
          0.0043942174418955, \
          0.0043942174418955, \
          0.0043942174418955, \
          0.0043942174418955, \
          0.0043942174418955, \
          0.0043942174418955, \
          0.0043942174418955, \
          0.0043942174418955, \
          0.0043942174418955, \
          0.0043942174418955, \
          0.0043942174418955, \
          0.0014412804208529, \
          0.0014412804208529, \
          0.0014412804208529, \
          0.0014412804208529, \
          0.0014412804208529, \
          0.0014412804208529, \
          0.0014412804208529, \
          0.0014412804208529, \
          0.0014412804208529, \
          0.0014412804208529, \
          0.0014412804208529, \
          0.0014412804208529, \
          0.0076389038664824, \
          0.0076389038664824, \
          0.0076389038664824, \
          0.0076389038664824, \
          0.0076389038664824, \
          0.0076389038664824, \
          0.0076389038664824, \
          0.0076389038664824, \
          0.0076389038664824, \
          0.0076389038664824, \
          0.0076389038664824, \
          0.0076389038664824, \
          0.0032669200631480, \
          0.0032669200631480, \
          0.0032669200631480, \
          0.0032669200631480, \
          0.0032669200631480, \
          0.0032669200631480, \
          0.0032669200631480, \
          0.0032669200631480, \
          0.0032669200631480, \
          0.0032669200631480, \
          0.0032669200631480, \
          0.0032669200631480 ] )

  return x, y, z, w

def rule17 ( ):

#*****************************************************************************80
#
## rule17() returns the prism rule of precision 17.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4665556153120432, \
          0.4665556153120432, \
          0.0668887693759136, \
          0.4665556153120432, \
          0.4665556153120432, \
          0.0668887693759136, \
          0.4923809674098066, \
          0.4923809674098066, \
          0.0152380651803867, \
          0.4923809674098066, \
          0.4923809674098066, \
          0.0152380651803867, \
          0.4466963397682847, \
          0.4466963397682847, \
          0.1066073204634306, \
          0.4466963397682847, \
          0.4466963397682847, \
          0.1066073204634306, \
          0.2058899494758731, \
          0.2058899494758731, \
          0.5882201010482538, \
          0.2058899494758731, \
          0.2058899494758731, \
          0.5882201010482538, \
          0.2305779360323416, \
          0.2305779360323416, \
          0.5388441279353168, \
          0.2305779360323416, \
          0.2305779360323416, \
          0.5388441279353168, \
          0.0070726502342596, \
          0.0070726502342596, \
          0.9858546995314807, \
          0.0070726502342596, \
          0.0070726502342596, \
          0.9858546995314807, \
          0.0524838545504923, \
          0.0524838545504923, \
          0.8950322908990154, \
          0.0524838545504923, \
          0.0524838545504923, \
          0.8950322908990154, \
          0.2780743897936196, \
          0.2780743897936196, \
          0.4438512204127608, \
          0.2780743897936196, \
          0.2780743897936196, \
          0.4438512204127608, \
          0.3893995813144771, \
          0.3893995813144771, \
          0.2212008373710459, \
          0.3893995813144771, \
          0.3893995813144771, \
          0.2212008373710459, \
          0.1132999955833483, \
          0.1132999955833483, \
          0.7734000088333033, \
          0.1132999955833483, \
          0.1132999955833483, \
          0.7734000088333033, \
          0.4687774749283292, \
          0.4687774749283292, \
          0.0624450501433417, \
          0.4687774749283292, \
          0.4687774749283292, \
          0.0624450501433417, \
          0.4942337889964747, \
          0.4942337889964747, \
          0.0115324220070506, \
          0.4942337889964747, \
          0.4942337889964747, \
          0.0115324220070506, \
          0.2906999098818323, \
          0.2906999098818323, \
          0.4186001802363355, \
          0.2906999098818323, \
          0.2906999098818323, \
          0.4186001802363355, \
          0.0937693039918497, \
          0.0937693039918497, \
          0.8124613920163005, \
          0.0937693039918497, \
          0.0937693039918497, \
          0.8124613920163005, \
          0.1632812980104028, \
          0.1632812980104028, \
          0.6734374039791945, \
          0.1632812980104028, \
          0.1632812980104028, \
          0.6734374039791945, \
          0.1774626418569745, \
          0.1774626418569745, \
          0.6450747162860511, \
          0.1774626418569745, \
          0.1774626418569745, \
          0.6450747162860511, \
          0.3930786561208929, \
          0.3930786561208929, \
          0.2138426877582142, \
          0.3930786561208929, \
          0.3930786561208929, \
          0.2138426877582142, \
          0.2711153947647855, \
          0.2711153947647855, \
          0.4577692104704291, \
          0.2711153947647855, \
          0.2711153947647855, \
          0.4577692104704291, \
          0.0243062210015648, \
          0.0243062210015648, \
          0.9513875579968704, \
          0.0243062210015648, \
          0.0243062210015648, \
          0.9513875579968704, \
          0.1273859447314594, \
          0.2765687474993688, \
          0.1273859447314594, \
          0.5960453077691718, \
          0.2765687474993688, \
          0.5960453077691718, \
          0.2450510833431427, \
          0.0852468501828055, \
          0.2450510833431427, \
          0.6697020664740517, \
          0.0852468501828055, \
          0.6697020664740517, \
          0.2450510833431427, \
          0.0852468501828055, \
          0.2450510833431427, \
          0.6697020664740517, \
          0.0852468501828055, \
          0.6697020664740517, \
          0.3192911229101512, \
          0.0276449852112552, \
          0.3192911229101512, \
          0.6530638918785936, \
          0.0276449852112552, \
          0.6530638918785936, \
          0.3192911229101512, \
          0.0276449852112552, \
          0.3192911229101512, \
          0.6530638918785936, \
          0.0276449852112552, \
          0.6530638918785936, \
          0.4577741357714497, \
          0.1385428807092584, \
          0.4577741357714497, \
          0.4036829835192919, \
          0.1385428807092584, \
          0.4036829835192919, \
          0.4577741357714497, \
          0.1385428807092584, \
          0.4577741357714497, \
          0.4036829835192919, \
          0.1385428807092584, \
          0.4036829835192919, \
          0.2421105196372634, \
          0.0124568391026713, \
          0.2421105196372634, \
          0.7454326412600653, \
          0.0124568391026713, \
          0.7454326412600653, \
          0.2421105196372634, \
          0.0124568391026713, \
          0.2421105196372634, \
          0.7454326412600653, \
          0.0124568391026713, \
          0.7454326412600653, \
          0.7269945541994681, \
          0.0888093024099239, \
          0.7269945541994681, \
          0.1841961433906080, \
          0.0888093024099239, \
          0.1841961433906080, \
          0.7269945541994681, \
          0.0888093024099239, \
          0.7269945541994681, \
          0.1841961433906080, \
          0.0888093024099239, \
          0.1841961433906080, \
          0.4870517086755036, \
          0.1725779658472295, \
          0.4870517086755036, \
          0.3403703254772670, \
          0.1725779658472295, \
          0.3403703254772670, \
          0.4870517086755036, \
          0.1725779658472295, \
          0.4870517086755036, \
          0.3403703254772670, \
          0.1725779658472295, \
          0.3403703254772670, \
          0.1582123188291182, \
          0.3108975273704328, \
          0.1582123188291182, \
          0.5308901538004490, \
          0.3108975273704328, \
          0.5308901538004490, \
          0.1582123188291182, \
          0.3108975273704328, \
          0.1582123188291182, \
          0.5308901538004490, \
          0.3108975273704328, \
          0.5308901538004490, \
          0.5973833093262283, \
          0.0432967856355362, \
          0.5973833093262283, \
          0.3593199050382355, \
          0.0432967856355362, \
          0.3593199050382355, \
          0.5973833093262283, \
          0.0432967856355362, \
          0.5973833093262283, \
          0.3593199050382355, \
          0.0432967856355362, \
          0.3593199050382355, \
          0.1111929938785087, \
          0.0368260832055792, \
          0.1111929938785087, \
          0.8519809229159122, \
          0.0368260832055792, \
          0.8519809229159122, \
          0.1111929938785087, \
          0.0368260832055792, \
          0.1111929938785087, \
          0.8519809229159122, \
          0.0368260832055792, \
          0.8519809229159122, \
          0.0387865006290567, \
          0.0070454102530681, \
          0.0387865006290567, \
          0.9541680891178752, \
          0.0070454102530681, \
          0.9541680891178752, \
          0.0387865006290567, \
          0.0070454102530681, \
          0.0387865006290567, \
          0.9541680891178752, \
          0.0070454102530681, \
          0.9541680891178752, \
          0.1417441449927015, \
          0.0066561350058640, \
          0.1417441449927015, \
          0.8515997200014345, \
          0.0066561350058640, \
          0.8515997200014345, \
          0.1417441449927015, \
          0.0066561350058640, \
          0.1417441449927015, \
          0.8515997200014345, \
          0.0066561350058640, \
          0.8515997200014345, \
          0.1343472140817544, \
          0.0269814183822196, \
          0.1343472140817544, \
          0.8386713675360260, \
          0.0269814183822196, \
          0.8386713675360260, \
          0.1343472140817544, \
          0.0269814183822196, \
          0.1343472140817544, \
          0.8386713675360260, \
          0.0269814183822196, \
          0.8386713675360260, \
          0.3195031824862086, \
          0.0813440561372205, \
          0.3195031824862086, \
          0.5991527613765709, \
          0.0813440561372205, \
          0.5991527613765709, \
          0.3195031824862086, \
          0.0813440561372205, \
          0.3195031824862086, \
          0.5991527613765709, \
          0.0813440561372205, \
          0.5991527613765709, \
          0.0826308438588340, \
          0.0102635465039764, \
          0.0826308438588340, \
          0.9071056096371896, \
          0.0102635465039764, \
          0.9071056096371896, \
          0.0826308438588340, \
          0.0102635465039764, \
          0.0826308438588340, \
          0.9071056096371896, \
          0.0102635465039764, \
          0.9071056096371896, \
          0.3827807429336583, \
          0.0067490134150570, \
          0.3827807429336583, \
          0.6104702436512848, \
          0.0067490134150570, \
          0.6104702436512848, \
          0.3827807429336583, \
          0.0067490134150570, \
          0.3827807429336583, \
          0.6104702436512848, \
          0.0067490134150570, \
          0.6104702436512848, \
          0.2446543644502634, \
          0.0056501992086932, \
          0.2446543644502634, \
          0.7496954363410434, \
          0.0056501992086932, \
          0.7496954363410434, \
          0.2446543644502634, \
          0.0056501992086932, \
          0.2446543644502634, \
          0.7496954363410434, \
          0.0056501992086932, \
          0.7496954363410434, \
          0.0263707136798594, \
          0.6264598409479015, \
          0.0263707136798594, \
          0.3471694453722390, \
          0.6264598409479015, \
          0.3471694453722390, \
          0.0263707136798594, \
          0.6264598409479015, \
          0.0263707136798594, \
          0.3471694453722390, \
          0.6264598409479015, \
          0.3471694453722390, \
          0.0434074542015924, \
          0.1947680793017931, \
          0.0434074542015924, \
          0.7618244664966145, \
          0.1947680793017931, \
          0.7618244664966145, \
          0.0434074542015924, \
          0.1947680793017931, \
          0.0434074542015924, \
          0.7618244664966145, \
          0.1947680793017931, \
          0.7618244664966145 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4665556153120432, \
          0.0668887693759136, \
          0.4665556153120432, \
          0.4665556153120432, \
          0.0668887693759136, \
          0.4665556153120432, \
          0.4923809674098066, \
          0.0152380651803867, \
          0.4923809674098066, \
          0.4923809674098066, \
          0.0152380651803867, \
          0.4923809674098066, \
          0.4466963397682847, \
          0.1066073204634306, \
          0.4466963397682847, \
          0.4466963397682847, \
          0.1066073204634306, \
          0.4466963397682847, \
          0.2058899494758731, \
          0.5882201010482538, \
          0.2058899494758731, \
          0.2058899494758731, \
          0.5882201010482538, \
          0.2058899494758731, \
          0.2305779360323416, \
          0.5388441279353168, \
          0.2305779360323416, \
          0.2305779360323416, \
          0.5388441279353168, \
          0.2305779360323416, \
          0.0070726502342596, \
          0.9858546995314807, \
          0.0070726502342596, \
          0.0070726502342596, \
          0.9858546995314807, \
          0.0070726502342596, \
          0.0524838545504923, \
          0.8950322908990154, \
          0.0524838545504923, \
          0.0524838545504923, \
          0.8950322908990154, \
          0.0524838545504923, \
          0.2780743897936196, \
          0.4438512204127608, \
          0.2780743897936196, \
          0.2780743897936196, \
          0.4438512204127608, \
          0.2780743897936196, \
          0.3893995813144771, \
          0.2212008373710459, \
          0.3893995813144771, \
          0.3893995813144771, \
          0.2212008373710459, \
          0.3893995813144771, \
          0.1132999955833483, \
          0.7734000088333033, \
          0.1132999955833483, \
          0.1132999955833483, \
          0.7734000088333033, \
          0.1132999955833483, \
          0.4687774749283292, \
          0.0624450501433417, \
          0.4687774749283292, \
          0.4687774749283292, \
          0.0624450501433417, \
          0.4687774749283292, \
          0.4942337889964747, \
          0.0115324220070506, \
          0.4942337889964747, \
          0.4942337889964747, \
          0.0115324220070506, \
          0.4942337889964747, \
          0.2906999098818323, \
          0.4186001802363355, \
          0.2906999098818323, \
          0.2906999098818323, \
          0.4186001802363355, \
          0.2906999098818323, \
          0.0937693039918497, \
          0.8124613920163005, \
          0.0937693039918497, \
          0.0937693039918497, \
          0.8124613920163005, \
          0.0937693039918497, \
          0.1632812980104028, \
          0.6734374039791945, \
          0.1632812980104028, \
          0.1632812980104028, \
          0.6734374039791945, \
          0.1632812980104028, \
          0.1774626418569745, \
          0.6450747162860511, \
          0.1774626418569745, \
          0.1774626418569745, \
          0.6450747162860511, \
          0.1774626418569745, \
          0.3930786561208929, \
          0.2138426877582142, \
          0.3930786561208929, \
          0.3930786561208929, \
          0.2138426877582142, \
          0.3930786561208929, \
          0.2711153947647855, \
          0.4577692104704291, \
          0.2711153947647855, \
          0.2711153947647855, \
          0.4577692104704291, \
          0.2711153947647855, \
          0.0243062210015648, \
          0.9513875579968704, \
          0.0243062210015648, \
          0.0243062210015648, \
          0.9513875579968704, \
          0.0243062210015648, \
          0.2765687474993688, \
          0.1273859447314594, \
          0.5960453077691718, \
          0.1273859447314594, \
          0.5960453077691718, \
          0.2765687474993688, \
          0.0852468501828055, \
          0.2450510833431427, \
          0.6697020664740517, \
          0.2450510833431427, \
          0.6697020664740517, \
          0.0852468501828055, \
          0.0852468501828055, \
          0.2450510833431427, \
          0.6697020664740517, \
          0.2450510833431427, \
          0.6697020664740517, \
          0.0852468501828055, \
          0.0276449852112552, \
          0.3192911229101512, \
          0.6530638918785936, \
          0.3192911229101512, \
          0.6530638918785936, \
          0.0276449852112552, \
          0.0276449852112552, \
          0.3192911229101512, \
          0.6530638918785936, \
          0.3192911229101512, \
          0.6530638918785936, \
          0.0276449852112552, \
          0.1385428807092584, \
          0.4577741357714497, \
          0.4036829835192919, \
          0.4577741357714497, \
          0.4036829835192919, \
          0.1385428807092584, \
          0.1385428807092584, \
          0.4577741357714497, \
          0.4036829835192919, \
          0.4577741357714497, \
          0.4036829835192919, \
          0.1385428807092584, \
          0.0124568391026713, \
          0.2421105196372634, \
          0.7454326412600653, \
          0.2421105196372634, \
          0.7454326412600653, \
          0.0124568391026713, \
          0.0124568391026713, \
          0.2421105196372634, \
          0.7454326412600653, \
          0.2421105196372634, \
          0.7454326412600653, \
          0.0124568391026713, \
          0.0888093024099239, \
          0.7269945541994681, \
          0.1841961433906080, \
          0.7269945541994681, \
          0.1841961433906080, \
          0.0888093024099239, \
          0.0888093024099239, \
          0.7269945541994681, \
          0.1841961433906080, \
          0.7269945541994681, \
          0.1841961433906080, \
          0.0888093024099239, \
          0.1725779658472295, \
          0.4870517086755036, \
          0.3403703254772670, \
          0.4870517086755036, \
          0.3403703254772670, \
          0.1725779658472295, \
          0.1725779658472295, \
          0.4870517086755036, \
          0.3403703254772670, \
          0.4870517086755036, \
          0.3403703254772670, \
          0.1725779658472295, \
          0.3108975273704328, \
          0.1582123188291182, \
          0.5308901538004490, \
          0.1582123188291182, \
          0.5308901538004490, \
          0.3108975273704328, \
          0.3108975273704328, \
          0.1582123188291182, \
          0.5308901538004490, \
          0.1582123188291182, \
          0.5308901538004490, \
          0.3108975273704328, \
          0.0432967856355362, \
          0.5973833093262283, \
          0.3593199050382355, \
          0.5973833093262283, \
          0.3593199050382355, \
          0.0432967856355362, \
          0.0432967856355362, \
          0.5973833093262283, \
          0.3593199050382355, \
          0.5973833093262283, \
          0.3593199050382355, \
          0.0432967856355362, \
          0.0368260832055792, \
          0.1111929938785087, \
          0.8519809229159122, \
          0.1111929938785087, \
          0.8519809229159122, \
          0.0368260832055792, \
          0.0368260832055792, \
          0.1111929938785087, \
          0.8519809229159122, \
          0.1111929938785087, \
          0.8519809229159122, \
          0.0368260832055792, \
          0.0070454102530681, \
          0.0387865006290567, \
          0.9541680891178752, \
          0.0387865006290567, \
          0.9541680891178752, \
          0.0070454102530681, \
          0.0070454102530681, \
          0.0387865006290567, \
          0.9541680891178752, \
          0.0387865006290567, \
          0.9541680891178752, \
          0.0070454102530681, \
          0.0066561350058640, \
          0.1417441449927015, \
          0.8515997200014345, \
          0.1417441449927015, \
          0.8515997200014345, \
          0.0066561350058640, \
          0.0066561350058640, \
          0.1417441449927015, \
          0.8515997200014345, \
          0.1417441449927015, \
          0.8515997200014345, \
          0.0066561350058640, \
          0.0269814183822196, \
          0.1343472140817544, \
          0.8386713675360260, \
          0.1343472140817544, \
          0.8386713675360260, \
          0.0269814183822196, \
          0.0269814183822196, \
          0.1343472140817544, \
          0.8386713675360260, \
          0.1343472140817544, \
          0.8386713675360260, \
          0.0269814183822196, \
          0.0813440561372205, \
          0.3195031824862086, \
          0.5991527613765709, \
          0.3195031824862086, \
          0.5991527613765709, \
          0.0813440561372205, \
          0.0813440561372205, \
          0.3195031824862086, \
          0.5991527613765709, \
          0.3195031824862086, \
          0.5991527613765709, \
          0.0813440561372205, \
          0.0102635465039764, \
          0.0826308438588340, \
          0.9071056096371896, \
          0.0826308438588340, \
          0.9071056096371896, \
          0.0102635465039764, \
          0.0102635465039764, \
          0.0826308438588340, \
          0.9071056096371896, \
          0.0826308438588340, \
          0.9071056096371896, \
          0.0102635465039764, \
          0.0067490134150570, \
          0.3827807429336583, \
          0.6104702436512848, \
          0.3827807429336583, \
          0.6104702436512848, \
          0.0067490134150570, \
          0.0067490134150570, \
          0.3827807429336583, \
          0.6104702436512848, \
          0.3827807429336583, \
          0.6104702436512848, \
          0.0067490134150570, \
          0.0056501992086932, \
          0.2446543644502634, \
          0.7496954363410434, \
          0.2446543644502634, \
          0.7496954363410434, \
          0.0056501992086932, \
          0.0056501992086932, \
          0.2446543644502634, \
          0.7496954363410434, \
          0.2446543644502634, \
          0.7496954363410434, \
          0.0056501992086932, \
          0.6264598409479015, \
          0.0263707136798594, \
          0.3471694453722390, \
          0.0263707136798594, \
          0.3471694453722390, \
          0.6264598409479015, \
          0.6264598409479015, \
          0.0263707136798594, \
          0.3471694453722390, \
          0.0263707136798594, \
          0.3471694453722390, \
          0.6264598409479015, \
          0.1947680793017931, \
          0.0434074542015924, \
          0.7618244664966145, \
          0.0434074542015924, \
          0.7618244664966145, \
          0.1947680793017931, \
          0.1947680793017931, \
          0.0434074542015924, \
          0.7618244664966145, \
          0.0434074542015924, \
          0.7618244664966145, \
          0.1947680793017931 ] )

  z = np.array ( [ \
          0.8666490488529237, \
          0.1333509511470762, \
          0.8703524297116281, \
          0.8703524297116281, \
          0.8703524297116281, \
          0.1296475702883719, \
          0.1296475702883719, \
          0.1296475702883719, \
          0.5962892344246855, \
          0.5962892344246855, \
          0.5962892344246855, \
          0.4037107655753145, \
          0.4037107655753145, \
          0.4037107655753145, \
          0.9862457308604132, \
          0.9862457308604132, \
          0.9862457308604132, \
          0.0137542691395868, \
          0.0137542691395868, \
          0.0137542691395868, \
          0.6193405024389006, \
          0.6193405024389006, \
          0.6193405024389006, \
          0.3806594975610994, \
          0.3806594975610994, \
          0.3806594975610994, \
          0.6506114926978297, \
          0.6506114926978297, \
          0.6506114926978297, \
          0.3493885073021704, \
          0.3493885073021704, \
          0.3493885073021704, \
          0.8258627018814777, \
          0.8258627018814777, \
          0.8258627018814777, \
          0.1741372981185223, \
          0.1741372981185223, \
          0.1741372981185223, \
          0.2477808238551293, \
          0.2477808238551293, \
          0.2477808238551293, \
          0.7522191761448707, \
          0.7522191761448707, \
          0.7522191761448707, \
          0.2921358009316097, \
          0.2921358009316097, \
          0.2921358009316097, \
          0.7078641990683903, \
          0.7078641990683903, \
          0.7078641990683903, \
          0.0981873258283363, \
          0.0981873258283363, \
          0.0981873258283363, \
          0.9018126741716637, \
          0.9018126741716637, \
          0.9018126741716637, \
          0.7125198639059245, \
          0.7125198639059245, \
          0.7125198639059245, \
          0.2874801360940755, \
          0.2874801360940755, \
          0.2874801360940755, \
          0.3516395946331653, \
          0.3516395946331653, \
          0.3516395946331653, \
          0.6483604053668347, \
          0.6483604053668347, \
          0.6483604053668347, \
          0.9459742145088597, \
          0.9459742145088597, \
          0.9459742145088597, \
          0.0540257854911404, \
          0.0540257854911404, \
          0.0540257854911404, \
          0.5658612299497008, \
          0.5658612299497008, \
          0.5658612299497008, \
          0.4341387700502993, \
          0.4341387700502993, \
          0.4341387700502993, \
          0.9273724754855923, \
          0.9273724754855923, \
          0.9273724754855923, \
          0.0726275245144077, \
          0.0726275245144077, \
          0.0726275245144077, \
          0.9989623565279326, \
          0.9989623565279326, \
          0.9989623565279326, \
          0.0010376434720673, \
          0.0010376434720673, \
          0.0010376434720673, \
          0.1604307070751930, \
          0.1604307070751930, \
          0.1604307070751930, \
          0.8395692929248070, \
          0.8395692929248070, \
          0.8395692929248070, \
          0.6345291354152611, \
          0.6345291354152611, \
          0.6345291354152611, \
          0.3654708645847389, \
          0.3654708645847389, \
          0.3654708645847389, \
          0.9811993443803730, \
          0.9811993443803730, \
          0.9811993443803730, \
          0.0188006556196270, \
          0.0188006556196270, \
          0.0188006556196270, \
          0.9712793580501632, \
          0.9712793580501632, \
          0.9712793580501632, \
          0.0287206419498368, \
          0.0287206419498368, \
          0.0287206419498368, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9553022983267381, \
          0.9553022983267381, \
          0.9553022983267381, \
          0.9553022983267381, \
          0.9553022983267381, \
          0.9553022983267381, \
          0.0446977016732619, \
          0.0446977016732619, \
          0.0446977016732619, \
          0.0446977016732619, \
          0.0446977016732619, \
          0.0446977016732619, \
          0.5287768623754378, \
          0.5287768623754378, \
          0.5287768623754378, \
          0.5287768623754378, \
          0.5287768623754378, \
          0.5287768623754378, \
          0.4712231376245622, \
          0.4712231376245622, \
          0.4712231376245622, \
          0.4712231376245622, \
          0.4712231376245622, \
          0.4712231376245622, \
          0.4538216112941401, \
          0.4538216112941401, \
          0.4538216112941401, \
          0.4538216112941401, \
          0.4538216112941401, \
          0.4538216112941401, \
          0.5461783887058599, \
          0.5461783887058599, \
          0.5461783887058599, \
          0.5461783887058599, \
          0.5461783887058599, \
          0.5461783887058599, \
          0.3624591754389214, \
          0.3624591754389214, \
          0.3624591754389214, \
          0.3624591754389214, \
          0.3624591754389214, \
          0.3624591754389214, \
          0.6375408245610786, \
          0.6375408245610786, \
          0.6375408245610786, \
          0.6375408245610786, \
          0.6375408245610786, \
          0.6375408245610786, \
          0.6176517353683332, \
          0.6176517353683332, \
          0.6176517353683332, \
          0.6176517353683332, \
          0.6176517353683332, \
          0.6176517353683332, \
          0.3823482646316668, \
          0.3823482646316668, \
          0.3823482646316668, \
          0.3823482646316668, \
          0.3823482646316668, \
          0.3823482646316668, \
          0.2130333812420883, \
          0.2130333812420883, \
          0.2130333812420883, \
          0.2130333812420883, \
          0.2130333812420883, \
          0.2130333812420883, \
          0.7869666187579117, \
          0.7869666187579117, \
          0.7869666187579117, \
          0.7869666187579117, \
          0.7869666187579117, \
          0.7869666187579117, \
          0.9281160730015593, \
          0.9281160730015593, \
          0.9281160730015593, \
          0.9281160730015593, \
          0.9281160730015593, \
          0.9281160730015593, \
          0.0718839269984407, \
          0.0718839269984407, \
          0.0718839269984407, \
          0.0718839269984407, \
          0.0718839269984407, \
          0.0718839269984407, \
          0.8760469217983575, \
          0.8760469217983575, \
          0.8760469217983575, \
          0.8760469217983575, \
          0.8760469217983575, \
          0.8760469217983575, \
          0.1239530782016424, \
          0.1239530782016424, \
          0.1239530782016424, \
          0.1239530782016424, \
          0.1239530782016424, \
          0.1239530782016424, \
          0.5105770631364416, \
          0.5105770631364416, \
          0.5105770631364416, \
          0.5105770631364416, \
          0.5105770631364416, \
          0.5105770631364416, \
          0.4894229368635584, \
          0.4894229368635584, \
          0.4894229368635584, \
          0.4894229368635584, \
          0.4894229368635584, \
          0.4894229368635584, \
          0.6124742043718856, \
          0.6124742043718856, \
          0.6124742043718856, \
          0.6124742043718856, \
          0.6124742043718856, \
          0.6124742043718856, \
          0.3875257956281143, \
          0.3875257956281143, \
          0.3875257956281143, \
          0.3875257956281143, \
          0.3875257956281143, \
          0.3875257956281143, \
          0.6912097488491545, \
          0.6912097488491545, \
          0.6912097488491545, \
          0.6912097488491545, \
          0.6912097488491545, \
          0.6912097488491545, \
          0.3087902511508455, \
          0.3087902511508455, \
          0.3087902511508455, \
          0.3087902511508455, \
          0.3087902511508455, \
          0.3087902511508455, \
          0.9870924037489929, \
          0.9870924037489929, \
          0.9870924037489929, \
          0.9870924037489929, \
          0.9870924037489929, \
          0.9870924037489929, \
          0.0129075962510071, \
          0.0129075962510071, \
          0.0129075962510071, \
          0.0129075962510071, \
          0.0129075962510071, \
          0.0129075962510071, \
          0.7190879938703654, \
          0.7190879938703654, \
          0.7190879938703654, \
          0.7190879938703654, \
          0.7190879938703654, \
          0.7190879938703654, \
          0.2809120061296346, \
          0.2809120061296346, \
          0.2809120061296346, \
          0.2809120061296346, \
          0.2809120061296346, \
          0.2809120061296346, \
          0.8842315513280089, \
          0.8842315513280089, \
          0.8842315513280089, \
          0.8842315513280089, \
          0.8842315513280089, \
          0.8842315513280089, \
          0.1157684486719911, \
          0.1157684486719911, \
          0.1157684486719911, \
          0.1157684486719911, \
          0.1157684486719911, \
          0.1157684486719911, \
          0.7732864296384829, \
          0.7732864296384829, \
          0.7732864296384829, \
          0.7732864296384829, \
          0.7732864296384829, \
          0.7732864296384829, \
          0.2267135703615171, \
          0.2267135703615171, \
          0.2267135703615171, \
          0.2267135703615171, \
          0.2267135703615171, \
          0.2267135703615171, \
          0.9276833503490310, \
          0.9276833503490310, \
          0.9276833503490310, \
          0.9276833503490310, \
          0.9276833503490310, \
          0.9276833503490310, \
          0.0723166496509690, \
          0.0723166496509690, \
          0.0723166496509690, \
          0.0723166496509690, \
          0.0723166496509690, \
          0.0723166496509690, \
          0.9877761641032086, \
          0.9877761641032086, \
          0.9877761641032086, \
          0.9877761641032086, \
          0.9877761641032086, \
          0.9877761641032086, \
          0.0122238358967914, \
          0.0122238358967914, \
          0.0122238358967914, \
          0.0122238358967914, \
          0.0122238358967914, \
          0.0122238358967914, \
          0.8232871808501311, \
          0.8232871808501311, \
          0.8232871808501311, \
          0.8232871808501311, \
          0.8232871808501311, \
          0.8232871808501311, \
          0.1767128191498689, \
          0.1767128191498689, \
          0.1767128191498689, \
          0.1767128191498689, \
          0.1767128191498689, \
          0.1767128191498689 ] )

  w = np.array ( [ \
          0.0075216525929737, \
          0.0075216525929737, \
          0.0039523401420815, \
          0.0039523401420815, \
          0.0039523401420815, \
          0.0039523401420815, \
          0.0039523401420815, \
          0.0039523401420815, \
          0.0026587971023890, \
          0.0026587971023890, \
          0.0026587971023890, \
          0.0026587971023890, \
          0.0026587971023890, \
          0.0026587971023890, \
          0.0023032616801324, \
          0.0023032616801324, \
          0.0023032616801324, \
          0.0023032616801324, \
          0.0023032616801324, \
          0.0023032616801324, \
          0.0043006096205643, \
          0.0043006096205643, \
          0.0043006096205643, \
          0.0043006096205643, \
          0.0043006096205643, \
          0.0043006096205643, \
          0.0030221060153018, \
          0.0030221060153018, \
          0.0030221060153018, \
          0.0030221060153018, \
          0.0030221060153018, \
          0.0030221060153018, \
          0.0003076949950084, \
          0.0003076949950084, \
          0.0003076949950084, \
          0.0003076949950084, \
          0.0003076949950084, \
          0.0003076949950084, \
          0.0030734403191510, \
          0.0030734403191510, \
          0.0030734403191510, \
          0.0030734403191510, \
          0.0030734403191510, \
          0.0030734403191510, \
          0.0049055295500793, \
          0.0049055295500793, \
          0.0049055295500793, \
          0.0049055295500793, \
          0.0049055295500793, \
          0.0049055295500793, \
          0.0027066696484092, \
          0.0027066696484092, \
          0.0027066696484092, \
          0.0027066696484092, \
          0.0027066696484092, \
          0.0027066696484092, \
          0.0034577749276135, \
          0.0034577749276135, \
          0.0034577749276135, \
          0.0034577749276135, \
          0.0034577749276135, \
          0.0034577749276135, \
          0.0051705174541971, \
          0.0051705174541971, \
          0.0051705174541971, \
          0.0051705174541971, \
          0.0051705174541971, \
          0.0051705174541971, \
          0.0014022583115306, \
          0.0014022583115306, \
          0.0014022583115306, \
          0.0014022583115306, \
          0.0014022583115306, \
          0.0014022583115306, \
          0.0042401026043811, \
          0.0042401026043811, \
          0.0042401026043811, \
          0.0042401026043811, \
          0.0042401026043811, \
          0.0042401026043811, \
          0.0032841487411702, \
          0.0032841487411702, \
          0.0032841487411702, \
          0.0032841487411702, \
          0.0032841487411702, \
          0.0032841487411702, \
          0.0011342259853124, \
          0.0011342259853124, \
          0.0011342259853124, \
          0.0011342259853124, \
          0.0011342259853124, \
          0.0011342259853124, \
          0.0074708548163608, \
          0.0074708548163608, \
          0.0074708548163608, \
          0.0074708548163608, \
          0.0074708548163608, \
          0.0074708548163608, \
          0.0034340384613521, \
          0.0034340384613521, \
          0.0034340384613521, \
          0.0034340384613521, \
          0.0034340384613521, \
          0.0034340384613521, \
          0.0031462609694126, \
          0.0031462609694126, \
          0.0031462609694126, \
          0.0031462609694126, \
          0.0031462609694126, \
          0.0031462609694126, \
          0.0005752613942102, \
          0.0005752613942102, \
          0.0005752613942102, \
          0.0005752613942102, \
          0.0005752613942102, \
          0.0005752613942102, \
          0.0065552795530324, \
          0.0065552795530324, \
          0.0065552795530324, \
          0.0065552795530324, \
          0.0065552795530324, \
          0.0065552795530324, \
          0.0029454095619872, \
          0.0029454095619872, \
          0.0029454095619872, \
          0.0029454095619872, \
          0.0029454095619872, \
          0.0029454095619872, \
          0.0029454095619872, \
          0.0029454095619872, \
          0.0029454095619872, \
          0.0029454095619872, \
          0.0029454095619872, \
          0.0029454095619872, \
          0.0024530630415632, \
          0.0024530630415632, \
          0.0024530630415632, \
          0.0024530630415632, \
          0.0024530630415632, \
          0.0024530630415632, \
          0.0024530630415632, \
          0.0024530630415632, \
          0.0024530630415632, \
          0.0024530630415632, \
          0.0024530630415632, \
          0.0024530630415632, \
          0.0028703966404990, \
          0.0028703966404990, \
          0.0028703966404990, \
          0.0028703966404990, \
          0.0028703966404990, \
          0.0028703966404990, \
          0.0028703966404990, \
          0.0028703966404990, \
          0.0028703966404990, \
          0.0028703966404990, \
          0.0028703966404990, \
          0.0028703966404990, \
          0.0018268277900660, \
          0.0018268277900660, \
          0.0018268277900660, \
          0.0018268277900660, \
          0.0018268277900660, \
          0.0018268277900660, \
          0.0018268277900660, \
          0.0018268277900660, \
          0.0018268277900660, \
          0.0018268277900660, \
          0.0018268277900660, \
          0.0018268277900660, \
          0.0046842877207978, \
          0.0046842877207978, \
          0.0046842877207978, \
          0.0046842877207978, \
          0.0046842877207978, \
          0.0046842877207978, \
          0.0046842877207978, \
          0.0046842877207978, \
          0.0046842877207978, \
          0.0046842877207978, \
          0.0046842877207978, \
          0.0046842877207978, \
          0.0061987832367774, \
          0.0061987832367774, \
          0.0061987832367774, \
          0.0061987832367774, \
          0.0061987832367774, \
          0.0061987832367774, \
          0.0061987832367774, \
          0.0061987832367774, \
          0.0061987832367774, \
          0.0061987832367774, \
          0.0061987832367774, \
          0.0061987832367774, \
          0.0041978630490507, \
          0.0041978630490507, \
          0.0041978630490507, \
          0.0041978630490507, \
          0.0041978630490507, \
          0.0041978630490507, \
          0.0041978630490507, \
          0.0041978630490507, \
          0.0041978630490507, \
          0.0041978630490507, \
          0.0041978630490507, \
          0.0041978630490507, \
          0.0025528142014630, \
          0.0025528142014630, \
          0.0025528142014630, \
          0.0025528142014630, \
          0.0025528142014630, \
          0.0025528142014630, \
          0.0025528142014630, \
          0.0025528142014630, \
          0.0025528142014630, \
          0.0025528142014630, \
          0.0025528142014630, \
          0.0025528142014630, \
          0.0020901151709172, \
          0.0020901151709172, \
          0.0020901151709172, \
          0.0020901151709172, \
          0.0020901151709172, \
          0.0020901151709172, \
          0.0020901151709172, \
          0.0020901151709172, \
          0.0020901151709172, \
          0.0020901151709172, \
          0.0020901151709172, \
          0.0020901151709172, \
          0.0007568671403396, \
          0.0007568671403396, \
          0.0007568671403396, \
          0.0007568671403396, \
          0.0007568671403396, \
          0.0007568671403396, \
          0.0007568671403396, \
          0.0007568671403396, \
          0.0007568671403396, \
          0.0007568671403396, \
          0.0007568671403396, \
          0.0007568671403396, \
          0.0013000657288395, \
          0.0013000657288395, \
          0.0013000657288395, \
          0.0013000657288395, \
          0.0013000657288395, \
          0.0013000657288395, \
          0.0013000657288395, \
          0.0013000657288395, \
          0.0013000657288395, \
          0.0013000657288395, \
          0.0013000657288395, \
          0.0013000657288395, \
          0.0008479873802968, \
          0.0008479873802968, \
          0.0008479873802968, \
          0.0008479873802968, \
          0.0008479873802968, \
          0.0008479873802968, \
          0.0008479873802968, \
          0.0008479873802968, \
          0.0008479873802968, \
          0.0008479873802968, \
          0.0008479873802968, \
          0.0008479873802968, \
          0.0064046130401019, \
          0.0064046130401019, \
          0.0064046130401019, \
          0.0064046130401019, \
          0.0064046130401019, \
          0.0064046130401019, \
          0.0064046130401019, \
          0.0064046130401019, \
          0.0064046130401019, \
          0.0064046130401019, \
          0.0064046130401019, \
          0.0064046130401019, \
          0.0011323520941966, \
          0.0011323520941966, \
          0.0011323520941966, \
          0.0011323520941966, \
          0.0011323520941966, \
          0.0011323520941966, \
          0.0011323520941966, \
          0.0011323520941966, \
          0.0011323520941966, \
          0.0011323520941966, \
          0.0011323520941966, \
          0.0011323520941966, \
          0.0020644102531444, \
          0.0020644102531444, \
          0.0020644102531444, \
          0.0020644102531444, \
          0.0020644102531444, \
          0.0020644102531444, \
          0.0020644102531444, \
          0.0020644102531444, \
          0.0020644102531444, \
          0.0020644102531444, \
          0.0020644102531444, \
          0.0020644102531444, \
          0.0010481934583324, \
          0.0010481934583324, \
          0.0010481934583324, \
          0.0010481934583324, \
          0.0010481934583324, \
          0.0010481934583324, \
          0.0010481934583324, \
          0.0010481934583324, \
          0.0010481934583324, \
          0.0010481934583324, \
          0.0010481934583324, \
          0.0010481934583324, \
          0.0009390285812953, \
          0.0009390285812953, \
          0.0009390285812953, \
          0.0009390285812953, \
          0.0009390285812953, \
          0.0009390285812953, \
          0.0009390285812953, \
          0.0009390285812953, \
          0.0009390285812953, \
          0.0009390285812953, \
          0.0009390285812953, \
          0.0009390285812953, \
          0.0042160603323249, \
          0.0042160603323249, \
          0.0042160603323249, \
          0.0042160603323249, \
          0.0042160603323249, \
          0.0042160603323249, \
          0.0042160603323249, \
          0.0042160603323249, \
          0.0042160603323249, \
          0.0042160603323249, \
          0.0042160603323249, \
          0.0042160603323249 ] )

  return x, y, z, w

def rule18 ( ):

#*****************************************************************************80
#
## rule18() returns the prism rule of precision 18.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.4728631477307805, \
          0.4728631477307805, \
          0.0542737045384390, \
          0.4728631477307805, \
          0.4728631477307805, \
          0.0542737045384390, \
          0.1090318158369727, \
          0.1090318158369727, \
          0.7819363683260546, \
          0.1090318158369727, \
          0.1090318158369727, \
          0.7819363683260546, \
          0.2141954002982068, \
          0.2141954002982068, \
          0.5716091994035865, \
          0.2141954002982068, \
          0.2141954002982068, \
          0.5716091994035865, \
          0.0084150887533426, \
          0.0084150887533426, \
          0.9831698224933149, \
          0.0084150887533426, \
          0.0084150887533426, \
          0.9831698224933149, \
          0.0494156440294096, \
          0.0494156440294096, \
          0.9011687119411808, \
          0.0494156440294096, \
          0.0494156440294096, \
          0.9011687119411808, \
          0.4574258170355346, \
          0.4574258170355346, \
          0.0851483659289308, \
          0.4574258170355346, \
          0.4574258170355346, \
          0.0851483659289308, \
          0.2945570490820424, \
          0.2945570490820424, \
          0.4108859018359152, \
          0.2945570490820424, \
          0.2945570490820424, \
          0.4108859018359152, \
          0.4148583469418042, \
          0.4148583469418042, \
          0.1702833061163916, \
          0.4148583469418042, \
          0.4148583469418042, \
          0.1702833061163916, \
          0.1801567120271234, \
          0.1801567120271234, \
          0.6396865759457532, \
          0.1801567120271234, \
          0.1801567120271234, \
          0.6396865759457532, \
          0.4092592655375933, \
          0.4092592655375933, \
          0.1814814689248134, \
          0.4092592655375933, \
          0.4092592655375933, \
          0.1814814689248134, \
          0.4106876572727113, \
          0.4106876572727113, \
          0.1786246854545774, \
          0.4106876572727113, \
          0.4106876572727113, \
          0.1786246854545774, \
          0.4942616172602019, \
          0.4942616172602019, \
          0.0114767654795962, \
          0.4942616172602019, \
          0.4942616172602019, \
          0.0114767654795962, \
          0.1455821883151533, \
          0.1455821883151533, \
          0.7088356233696933, \
          0.1455821883151533, \
          0.1455821883151533, \
          0.7088356233696933, \
          0.0775928696462990, \
          0.0775928696462990, \
          0.8448142607074021, \
          0.0775928696462990, \
          0.0775928696462990, \
          0.8448142607074021, \
          0.1688466480848478, \
          0.1688466480848478, \
          0.6623067038303044, \
          0.1688466480848478, \
          0.1688466480848478, \
          0.6623067038303044, \
          0.2737821968608845, \
          0.2737821968608845, \
          0.4524356062782311, \
          0.2737821968608845, \
          0.2737821968608845, \
          0.4524356062782311, \
          0.3193703110432156, \
          0.3193703110432156, \
          0.3612593779135688, \
          0.3193703110432156, \
          0.3193703110432156, \
          0.3612593779135688, \
          0.2789278090499041, \
          0.2789278090499041, \
          0.4421443819001918, \
          0.2789278090499041, \
          0.2789278090499041, \
          0.4421443819001918, \
          0.0147343308678136, \
          0.0147343308678136, \
          0.9705313382643729, \
          0.0147343308678136, \
          0.0147343308678136, \
          0.9705313382643729, \
          0.2803931989784251, \
          0.1730708483947652, \
          0.2803931989784251, \
          0.5465359526268097, \
          0.1730708483947652, \
          0.5465359526268097, \
          0.3067402740370590, \
          0.0472583316199373, \
          0.3067402740370590, \
          0.6460013943430037, \
          0.0472583316199373, \
          0.6460013943430037, \
          0.3067402740370590, \
          0.0472583316199373, \
          0.3067402740370590, \
          0.6460013943430037, \
          0.0472583316199373, \
          0.6460013943430037, \
          0.5587472044782793, \
          0.0637486493547561, \
          0.5587472044782793, \
          0.3775041461669645, \
          0.0637486493547561, \
          0.3775041461669645, \
          0.5587472044782793, \
          0.0637486493547561, \
          0.5587472044782793, \
          0.3775041461669645, \
          0.0637486493547561, \
          0.3775041461669645, \
          0.1295467219204834, \
          0.2834002542935580, \
          0.1295467219204834, \
          0.5870530237859586, \
          0.2834002542935580, \
          0.5870530237859586, \
          0.1295467219204834, \
          0.2834002542935580, \
          0.1295467219204834, \
          0.5870530237859586, \
          0.2834002542935580, \
          0.5870530237859586, \
          0.2943165499688927, \
          0.0323606160924521, \
          0.2943165499688927, \
          0.6733228339386552, \
          0.0323606160924521, \
          0.6733228339386552, \
          0.2943165499688927, \
          0.0323606160924521, \
          0.2943165499688927, \
          0.6733228339386552, \
          0.0323606160924521, \
          0.6733228339386552, \
          0.7045618883179275, \
          0.0682727115900655, \
          0.7045618883179275, \
          0.2271654000920070, \
          0.0682727115900655, \
          0.2271654000920070, \
          0.7045618883179275, \
          0.0682727115900655, \
          0.7045618883179275, \
          0.2271654000920070, \
          0.0682727115900655, \
          0.2271654000920070, \
          0.5336092397180819, \
          0.0823227847933820, \
          0.5336092397180819, \
          0.3840679754885361, \
          0.0823227847933820, \
          0.3840679754885361, \
          0.5336092397180819, \
          0.0823227847933820, \
          0.5336092397180819, \
          0.3840679754885361, \
          0.0823227847933820, \
          0.3840679754885361, \
          0.1659343236267790, \
          0.2958566157742775, \
          0.1659343236267790, \
          0.5382090605989435, \
          0.2958566157742775, \
          0.5382090605989435, \
          0.1659343236267790, \
          0.2958566157742775, \
          0.1659343236267790, \
          0.5382090605989435, \
          0.2958566157742775, \
          0.5382090605989435, \
          0.5873912217089957, \
          0.0091538552254334, \
          0.5873912217089957, \
          0.4034549230655710, \
          0.0091538552254334, \
          0.4034549230655710, \
          0.5873912217089957, \
          0.0091538552254334, \
          0.5873912217089957, \
          0.4034549230655710, \
          0.0091538552254334, \
          0.4034549230655710, \
          0.1216404492275597, \
          0.0492455683577680, \
          0.1216404492275597, \
          0.8291139824146723, \
          0.0492455683577680, \
          0.8291139824146723, \
          0.1216404492275597, \
          0.0492455683577680, \
          0.1216404492275597, \
          0.8291139824146723, \
          0.0492455683577680, \
          0.8291139824146723, \
          0.0420809533226036, \
          0.0077537345196640, \
          0.0420809533226036, \
          0.9501653121577324, \
          0.0077537345196640, \
          0.9501653121577324, \
          0.0420809533226036, \
          0.0077537345196640, \
          0.0420809533226036, \
          0.9501653121577324, \
          0.0077537345196640, \
          0.9501653121577324, \
          0.4516351625773616, \
          0.0228219169717125, \
          0.4516351625773616, \
          0.5255429204509259, \
          0.0228219169717125, \
          0.5255429204509259, \
          0.4516351625773616, \
          0.0228219169717125, \
          0.4516351625773616, \
          0.5255429204509259, \
          0.0228219169717125, \
          0.5255429204509259, \
          0.1252580641579170, \
          0.0073963274047276, \
          0.1252580641579170, \
          0.8673456084373554, \
          0.0073963274047276, \
          0.8673456084373554, \
          0.1252580641579170, \
          0.0073963274047276, \
          0.1252580641579170, \
          0.8673456084373554, \
          0.0073963274047276, \
          0.8673456084373554, \
          0.1765722195894258, \
          0.0653002115725378, \
          0.1765722195894258, \
          0.7581275688380364, \
          0.0653002115725378, \
          0.7581275688380364, \
          0.1765722195894258, \
          0.0653002115725378, \
          0.1765722195894258, \
          0.7581275688380364, \
          0.0653002115725378, \
          0.7581275688380364, \
          0.2404267015692479, \
          0.0085879015506819, \
          0.2404267015692479, \
          0.7509853968800702, \
          0.0085879015506819, \
          0.7509853968800702, \
          0.2404267015692479, \
          0.0085879015506819, \
          0.2404267015692479, \
          0.7509853968800702, \
          0.0085879015506819, \
          0.7509853968800702, \
          0.0644058552263157, \
          0.0122678034366560, \
          0.0644058552263157, \
          0.9233263413370284, \
          0.0122678034366560, \
          0.9233263413370284, \
          0.0644058552263157, \
          0.0122678034366560, \
          0.0644058552263157, \
          0.9233263413370284, \
          0.0122678034366560, \
          0.9233263413370284, \
          0.2681069831840066, \
          0.0044793265613672, \
          0.2681069831840066, \
          0.7274136902546262, \
          0.0044793265613672, \
          0.7274136902546262, \
          0.2681069831840066, \
          0.0044793265613672, \
          0.2681069831840066, \
          0.7274136902546262, \
          0.0044793265613672, \
          0.7274136902546262, \
          0.1727205252244992, \
          0.0117334535244670, \
          0.1727205252244992, \
          0.8155460212510338, \
          0.0117334535244670, \
          0.8155460212510338, \
          0.1727205252244992, \
          0.0117334535244670, \
          0.1727205252244992, \
          0.8155460212510338, \
          0.0117334535244670, \
          0.8155460212510338, \
          0.1118329953359960, \
          0.5446775610503505, \
          0.1118329953359960, \
          0.3434894436136536, \
          0.5446775610503505, \
          0.3434894436136536, \
          0.1118329953359960, \
          0.5446775610503505, \
          0.1118329953359960, \
          0.3434894436136536, \
          0.5446775610503505, \
          0.3434894436136536, \
          0.5899536365475773, \
          0.0080175874177025, \
          0.5899536365475773, \
          0.4020287760347202, \
          0.0080175874177025, \
          0.4020287760347202, \
          0.5899536365475773, \
          0.0080175874177025, \
          0.5899536365475773, \
          0.4020287760347202, \
          0.0080175874177025, \
          0.4020287760347202, \
          0.0961540597861764, \
          0.2067498834662211, \
          0.0961540597861764, \
          0.6970960567476024, \
          0.2067498834662211, \
          0.6970960567476024, \
          0.0961540597861764, \
          0.2067498834662211, \
          0.0961540597861764, \
          0.6970960567476024, \
          0.2067498834662211, \
          0.6970960567476024, \
          0.3068968355307726, \
          0.0117746553239110, \
          0.3068968355307726, \
          0.6813285091453164, \
          0.0117746553239110, \
          0.6813285091453164, \
          0.3068968355307726, \
          0.0117746553239110, \
          0.3068968355307726, \
          0.6813285091453164, \
          0.0117746553239110, \
          0.6813285091453164, \
          0.0798486447852760, \
          0.0174063356195718, \
          0.0798486447852760, \
          0.9027450195951523, \
          0.0174063356195718, \
          0.9027450195951523, \
          0.0798486447852760, \
          0.0174063356195718, \
          0.0798486447852760, \
          0.9027450195951523, \
          0.0174063356195718, \
          0.9027450195951523, \
          0.0360777790627768, \
          0.1618562004775664, \
          0.0360777790627768, \
          0.8020660204596567, \
          0.1618562004775664, \
          0.8020660204596567, \
          0.0360777790627768, \
          0.1618562004775664, \
          0.0360777790627768, \
          0.8020660204596567, \
          0.1618562004775664, \
          0.8020660204596567 ] )

  y = np.array ( [ \
          0.4728631477307805, \
          0.0542737045384390, \
          0.4728631477307805, \
          0.4728631477307805, \
          0.0542737045384390, \
          0.4728631477307805, \
          0.1090318158369727, \
          0.7819363683260546, \
          0.1090318158369727, \
          0.1090318158369727, \
          0.7819363683260546, \
          0.1090318158369727, \
          0.2141954002982068, \
          0.5716091994035865, \
          0.2141954002982068, \
          0.2141954002982068, \
          0.5716091994035865, \
          0.2141954002982068, \
          0.0084150887533426, \
          0.9831698224933149, \
          0.0084150887533426, \
          0.0084150887533426, \
          0.9831698224933149, \
          0.0084150887533426, \
          0.0494156440294096, \
          0.9011687119411808, \
          0.0494156440294096, \
          0.0494156440294096, \
          0.9011687119411808, \
          0.0494156440294096, \
          0.4574258170355346, \
          0.0851483659289308, \
          0.4574258170355346, \
          0.4574258170355346, \
          0.0851483659289308, \
          0.4574258170355346, \
          0.2945570490820424, \
          0.4108859018359152, \
          0.2945570490820424, \
          0.2945570490820424, \
          0.4108859018359152, \
          0.2945570490820424, \
          0.4148583469418042, \
          0.1702833061163916, \
          0.4148583469418042, \
          0.4148583469418042, \
          0.1702833061163916, \
          0.4148583469418042, \
          0.1801567120271234, \
          0.6396865759457532, \
          0.1801567120271234, \
          0.1801567120271234, \
          0.6396865759457532, \
          0.1801567120271234, \
          0.4092592655375933, \
          0.1814814689248134, \
          0.4092592655375933, \
          0.4092592655375933, \
          0.1814814689248134, \
          0.4092592655375933, \
          0.4106876572727113, \
          0.1786246854545774, \
          0.4106876572727113, \
          0.4106876572727113, \
          0.1786246854545774, \
          0.4106876572727113, \
          0.4942616172602019, \
          0.0114767654795962, \
          0.4942616172602019, \
          0.4942616172602019, \
          0.0114767654795962, \
          0.4942616172602019, \
          0.1455821883151533, \
          0.7088356233696933, \
          0.1455821883151533, \
          0.1455821883151533, \
          0.7088356233696933, \
          0.1455821883151533, \
          0.0775928696462990, \
          0.8448142607074021, \
          0.0775928696462990, \
          0.0775928696462990, \
          0.8448142607074021, \
          0.0775928696462990, \
          0.1688466480848478, \
          0.6623067038303044, \
          0.1688466480848478, \
          0.1688466480848478, \
          0.6623067038303044, \
          0.1688466480848478, \
          0.2737821968608845, \
          0.4524356062782311, \
          0.2737821968608845, \
          0.2737821968608845, \
          0.4524356062782311, \
          0.2737821968608845, \
          0.3193703110432156, \
          0.3612593779135688, \
          0.3193703110432156, \
          0.3193703110432156, \
          0.3612593779135688, \
          0.3193703110432156, \
          0.2789278090499041, \
          0.4421443819001918, \
          0.2789278090499041, \
          0.2789278090499041, \
          0.4421443819001918, \
          0.2789278090499041, \
          0.0147343308678136, \
          0.9705313382643729, \
          0.0147343308678136, \
          0.0147343308678136, \
          0.9705313382643729, \
          0.0147343308678136, \
          0.1730708483947652, \
          0.2803931989784251, \
          0.5465359526268097, \
          0.2803931989784251, \
          0.5465359526268097, \
          0.1730708483947652, \
          0.0472583316199373, \
          0.3067402740370590, \
          0.6460013943430037, \
          0.3067402740370590, \
          0.6460013943430037, \
          0.0472583316199373, \
          0.0472583316199373, \
          0.3067402740370590, \
          0.6460013943430037, \
          0.3067402740370590, \
          0.6460013943430037, \
          0.0472583316199373, \
          0.0637486493547561, \
          0.5587472044782793, \
          0.3775041461669645, \
          0.5587472044782793, \
          0.3775041461669645, \
          0.0637486493547561, \
          0.0637486493547561, \
          0.5587472044782793, \
          0.3775041461669645, \
          0.5587472044782793, \
          0.3775041461669645, \
          0.0637486493547561, \
          0.2834002542935580, \
          0.1295467219204834, \
          0.5870530237859586, \
          0.1295467219204834, \
          0.5870530237859586, \
          0.2834002542935580, \
          0.2834002542935580, \
          0.1295467219204834, \
          0.5870530237859586, \
          0.1295467219204834, \
          0.5870530237859586, \
          0.2834002542935580, \
          0.0323606160924521, \
          0.2943165499688927, \
          0.6733228339386552, \
          0.2943165499688927, \
          0.6733228339386552, \
          0.0323606160924521, \
          0.0323606160924521, \
          0.2943165499688927, \
          0.6733228339386552, \
          0.2943165499688927, \
          0.6733228339386552, \
          0.0323606160924521, \
          0.0682727115900655, \
          0.7045618883179275, \
          0.2271654000920070, \
          0.7045618883179275, \
          0.2271654000920070, \
          0.0682727115900655, \
          0.0682727115900655, \
          0.7045618883179275, \
          0.2271654000920070, \
          0.7045618883179275, \
          0.2271654000920070, \
          0.0682727115900655, \
          0.0823227847933820, \
          0.5336092397180819, \
          0.3840679754885361, \
          0.5336092397180819, \
          0.3840679754885361, \
          0.0823227847933820, \
          0.0823227847933820, \
          0.5336092397180819, \
          0.3840679754885361, \
          0.5336092397180819, \
          0.3840679754885361, \
          0.0823227847933820, \
          0.2958566157742775, \
          0.1659343236267790, \
          0.5382090605989435, \
          0.1659343236267790, \
          0.5382090605989435, \
          0.2958566157742775, \
          0.2958566157742775, \
          0.1659343236267790, \
          0.5382090605989435, \
          0.1659343236267790, \
          0.5382090605989435, \
          0.2958566157742775, \
          0.0091538552254334, \
          0.5873912217089957, \
          0.4034549230655710, \
          0.5873912217089957, \
          0.4034549230655710, \
          0.0091538552254334, \
          0.0091538552254334, \
          0.5873912217089957, \
          0.4034549230655710, \
          0.5873912217089957, \
          0.4034549230655710, \
          0.0091538552254334, \
          0.0492455683577680, \
          0.1216404492275597, \
          0.8291139824146723, \
          0.1216404492275597, \
          0.8291139824146723, \
          0.0492455683577680, \
          0.0492455683577680, \
          0.1216404492275597, \
          0.8291139824146723, \
          0.1216404492275597, \
          0.8291139824146723, \
          0.0492455683577680, \
          0.0077537345196640, \
          0.0420809533226036, \
          0.9501653121577324, \
          0.0420809533226036, \
          0.9501653121577324, \
          0.0077537345196640, \
          0.0077537345196640, \
          0.0420809533226036, \
          0.9501653121577324, \
          0.0420809533226036, \
          0.9501653121577324, \
          0.0077537345196640, \
          0.0228219169717125, \
          0.4516351625773616, \
          0.5255429204509259, \
          0.4516351625773616, \
          0.5255429204509259, \
          0.0228219169717125, \
          0.0228219169717125, \
          0.4516351625773616, \
          0.5255429204509259, \
          0.4516351625773616, \
          0.5255429204509259, \
          0.0228219169717125, \
          0.0073963274047276, \
          0.1252580641579170, \
          0.8673456084373554, \
          0.1252580641579170, \
          0.8673456084373554, \
          0.0073963274047276, \
          0.0073963274047276, \
          0.1252580641579170, \
          0.8673456084373554, \
          0.1252580641579170, \
          0.8673456084373554, \
          0.0073963274047276, \
          0.0653002115725378, \
          0.1765722195894258, \
          0.7581275688380364, \
          0.1765722195894258, \
          0.7581275688380364, \
          0.0653002115725378, \
          0.0653002115725378, \
          0.1765722195894258, \
          0.7581275688380364, \
          0.1765722195894258, \
          0.7581275688380364, \
          0.0653002115725378, \
          0.0085879015506819, \
          0.2404267015692479, \
          0.7509853968800702, \
          0.2404267015692479, \
          0.7509853968800702, \
          0.0085879015506819, \
          0.0085879015506819, \
          0.2404267015692479, \
          0.7509853968800702, \
          0.2404267015692479, \
          0.7509853968800702, \
          0.0085879015506819, \
          0.0122678034366560, \
          0.0644058552263157, \
          0.9233263413370284, \
          0.0644058552263157, \
          0.9233263413370284, \
          0.0122678034366560, \
          0.0122678034366560, \
          0.0644058552263157, \
          0.9233263413370284, \
          0.0644058552263157, \
          0.9233263413370284, \
          0.0122678034366560, \
          0.0044793265613672, \
          0.2681069831840066, \
          0.7274136902546262, \
          0.2681069831840066, \
          0.7274136902546262, \
          0.0044793265613672, \
          0.0044793265613672, \
          0.2681069831840066, \
          0.7274136902546262, \
          0.2681069831840066, \
          0.7274136902546262, \
          0.0044793265613672, \
          0.0117334535244670, \
          0.1727205252244992, \
          0.8155460212510338, \
          0.1727205252244992, \
          0.8155460212510338, \
          0.0117334535244670, \
          0.0117334535244670, \
          0.1727205252244992, \
          0.8155460212510338, \
          0.1727205252244992, \
          0.8155460212510338, \
          0.0117334535244670, \
          0.5446775610503505, \
          0.1118329953359960, \
          0.3434894436136536, \
          0.1118329953359960, \
          0.3434894436136536, \
          0.5446775610503505, \
          0.5446775610503505, \
          0.1118329953359960, \
          0.3434894436136536, \
          0.1118329953359960, \
          0.3434894436136536, \
          0.5446775610503505, \
          0.0080175874177025, \
          0.5899536365475773, \
          0.4020287760347202, \
          0.5899536365475773, \
          0.4020287760347202, \
          0.0080175874177025, \
          0.0080175874177025, \
          0.5899536365475773, \
          0.4020287760347202, \
          0.5899536365475773, \
          0.4020287760347202, \
          0.0080175874177025, \
          0.2067498834662211, \
          0.0961540597861764, \
          0.6970960567476024, \
          0.0961540597861764, \
          0.6970960567476024, \
          0.2067498834662211, \
          0.2067498834662211, \
          0.0961540597861764, \
          0.6970960567476024, \
          0.0961540597861764, \
          0.6970960567476024, \
          0.2067498834662211, \
          0.0117746553239110, \
          0.3068968355307726, \
          0.6813285091453164, \
          0.3068968355307726, \
          0.6813285091453164, \
          0.0117746553239110, \
          0.0117746553239110, \
          0.3068968355307726, \
          0.6813285091453164, \
          0.3068968355307726, \
          0.6813285091453164, \
          0.0117746553239110, \
          0.0174063356195718, \
          0.0798486447852760, \
          0.9027450195951523, \
          0.0798486447852760, \
          0.9027450195951523, \
          0.0174063356195718, \
          0.0174063356195718, \
          0.0798486447852760, \
          0.9027450195951523, \
          0.0798486447852760, \
          0.9027450195951523, \
          0.0174063356195718, \
          0.1618562004775664, \
          0.0360777790627768, \
          0.8020660204596567, \
          0.0360777790627768, \
          0.8020660204596567, \
          0.1618562004775664, \
          0.1618562004775664, \
          0.0360777790627768, \
          0.8020660204596567, \
          0.0360777790627768, \
          0.8020660204596567, \
          0.1618562004775664 ] )

  z = np.array ( [ \
          0.9534387216382612, \
          0.9534387216382612, \
          0.9534387216382612, \
          0.0465612783617388, \
          0.0465612783617388, \
          0.0465612783617388, \
          0.7595655027404185, \
          0.7595655027404185, \
          0.7595655027404185, \
          0.2404344972595815, \
          0.2404344972595815, \
          0.2404344972595815, \
          0.8487633516520783, \
          0.8487633516520783, \
          0.8487633516520783, \
          0.1512366483479217, \
          0.1512366483479217, \
          0.1512366483479217, \
          0.7352481798898231, \
          0.7352481798898231, \
          0.7352481798898231, \
          0.2647518201101769, \
          0.2647518201101769, \
          0.2647518201101769, \
          0.3114476852954629, \
          0.3114476852954629, \
          0.3114476852954629, \
          0.6885523147045371, \
          0.6885523147045371, \
          0.6885523147045371, \
          0.3645354584203186, \
          0.3645354584203186, \
          0.3645354584203186, \
          0.6354645415796814, \
          0.6354645415796814, \
          0.6354645415796814, \
          0.4121101005024969, \
          0.4121101005024969, \
          0.4121101005024969, \
          0.5878898994975031, \
          0.5878898994975031, \
          0.5878898994975031, \
          0.3548440062961510, \
          0.3548440062961510, \
          0.3548440062961510, \
          0.6451559937038489, \
          0.6451559937038489, \
          0.6451559937038489, \
          0.3501843143023031, \
          0.3501843143023031, \
          0.3501843143023031, \
          0.6498156856976969, \
          0.6498156856976969, \
          0.6498156856976969, \
          0.0656042965456428, \
          0.0656042965456428, \
          0.0656042965456428, \
          0.9343957034543572, \
          0.9343957034543572, \
          0.9343957034543572, \
          0.1448541902653249, \
          0.1448541902653249, \
          0.1448541902653249, \
          0.8551458097346751, \
          0.8551458097346751, \
          0.8551458097346751, \
          0.9806685335400167, \
          0.9806685335400167, \
          0.9806685335400167, \
          0.0193314664599833, \
          0.0193314664599833, \
          0.0193314664599833, \
          0.6290398587069839, \
          0.6290398587069839, \
          0.6290398587069839, \
          0.3709601412930161, \
          0.3709601412930161, \
          0.3709601412930161, \
          0.9287263768670988, \
          0.9287263768670988, \
          0.9287263768670988, \
          0.0712736231329013, \
          0.0712736231329013, \
          0.0712736231329013, \
          0.9721416113157295, \
          0.9721416113157295, \
          0.9721416113157295, \
          0.0278583886842705, \
          0.0278583886842705, \
          0.0278583886842705, \
          0.2369147251638602, \
          0.2369147251638602, \
          0.2369147251638602, \
          0.7630852748361399, \
          0.7630852748361399, \
          0.7630852748361399, \
          0.8919378093663139, \
          0.8919378093663139, \
          0.8919378093663139, \
          0.1080621906336861, \
          0.1080621906336861, \
          0.1080621906336861, \
          0.9842060169219227, \
          0.9842060169219227, \
          0.9842060169219227, \
          0.0157939830780774, \
          0.0157939830780774, \
          0.0157939830780774, \
          0.9527746747185892, \
          0.9527746747185892, \
          0.9527746747185892, \
          0.0472253252814108, \
          0.0472253252814108, \
          0.0472253252814108, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9343231379314123, \
          0.9343231379314123, \
          0.9343231379314123, \
          0.9343231379314123, \
          0.9343231379314123, \
          0.9343231379314123, \
          0.0656768620685876, \
          0.0656768620685876, \
          0.0656768620685876, \
          0.0656768620685876, \
          0.0656768620685876, \
          0.0656768620685876, \
          0.5513722678894569, \
          0.5513722678894569, \
          0.5513722678894569, \
          0.5513722678894569, \
          0.5513722678894569, \
          0.5513722678894569, \
          0.4486277321105431, \
          0.4486277321105431, \
          0.4486277321105431, \
          0.4486277321105431, \
          0.4486277321105431, \
          0.4486277321105431, \
          0.2743627864784612, \
          0.2743627864784612, \
          0.2743627864784612, \
          0.2743627864784612, \
          0.2743627864784612, \
          0.2743627864784612, \
          0.7256372135215388, \
          0.7256372135215388, \
          0.7256372135215388, \
          0.7256372135215388, \
          0.7256372135215388, \
          0.7256372135215388, \
          0.2817575164863711, \
          0.2817575164863711, \
          0.2817575164863711, \
          0.2817575164863711, \
          0.2817575164863711, \
          0.2817575164863711, \
          0.7182424835136290, \
          0.7182424835136290, \
          0.7182424835136290, \
          0.7182424835136290, \
          0.7182424835136290, \
          0.7182424835136290, \
          0.5891160926744499, \
          0.5891160926744499, \
          0.5891160926744499, \
          0.5891160926744499, \
          0.5891160926744499, \
          0.5891160926744499, \
          0.4108839073255501, \
          0.4108839073255501, \
          0.4108839073255501, \
          0.4108839073255501, \
          0.4108839073255501, \
          0.4108839073255501, \
          0.1714235980915265, \
          0.1714235980915265, \
          0.1714235980915265, \
          0.1714235980915265, \
          0.1714235980915265, \
          0.1714235980915265, \
          0.8285764019084735, \
          0.8285764019084735, \
          0.8285764019084735, \
          0.8285764019084735, \
          0.8285764019084735, \
          0.8285764019084735, \
          0.9394301860037320, \
          0.9394301860037320, \
          0.9394301860037320, \
          0.9394301860037320, \
          0.9394301860037320, \
          0.9394301860037320, \
          0.0605698139962680, \
          0.0605698139962680, \
          0.0605698139962680, \
          0.0605698139962680, \
          0.0605698139962680, \
          0.0605698139962680, \
          0.8744417684033916, \
          0.8744417684033916, \
          0.8744417684033916, \
          0.8744417684033916, \
          0.8744417684033916, \
          0.8744417684033916, \
          0.1255582315966083, \
          0.1255582315966083, \
          0.1255582315966083, \
          0.1255582315966083, \
          0.1255582315966083, \
          0.1255582315966083, \
          0.4576004985221995, \
          0.4576004985221995, \
          0.4576004985221995, \
          0.4576004985221995, \
          0.4576004985221995, \
          0.4576004985221995, \
          0.5423995014778005, \
          0.5423995014778005, \
          0.5423995014778005, \
          0.5423995014778005, \
          0.5423995014778005, \
          0.5423995014778005, \
          0.5469802767947162, \
          0.5469802767947162, \
          0.5469802767947162, \
          0.5469802767947162, \
          0.5469802767947162, \
          0.5469802767947162, \
          0.4530197232052838, \
          0.4530197232052838, \
          0.4530197232052838, \
          0.4530197232052838, \
          0.4530197232052838, \
          0.4530197232052838, \
          0.7227042014132130, \
          0.7227042014132130, \
          0.7227042014132130, \
          0.7227042014132130, \
          0.7227042014132130, \
          0.7227042014132130, \
          0.2772957985867870, \
          0.2772957985867870, \
          0.2772957985867870, \
          0.2772957985867870, \
          0.2772957985867870, \
          0.2772957985867870, \
          0.6586462869796975, \
          0.6586462869796975, \
          0.6586462869796975, \
          0.6586462869796975, \
          0.6586462869796975, \
          0.6586462869796975, \
          0.3413537130203025, \
          0.3413537130203025, \
          0.3413537130203025, \
          0.3413537130203025, \
          0.3413537130203025, \
          0.3413537130203025, \
          0.9865056469526946, \
          0.9865056469526946, \
          0.9865056469526946, \
          0.9865056469526946, \
          0.9865056469526946, \
          0.9865056469526946, \
          0.0134943530473054, \
          0.0134943530473054, \
          0.0134943530473054, \
          0.0134943530473054, \
          0.0134943530473054, \
          0.0134943530473054, \
          0.5827285974639408, \
          0.5827285974639408, \
          0.5827285974639408, \
          0.5827285974639408, \
          0.5827285974639408, \
          0.5827285974639408, \
          0.4172714025360593, \
          0.4172714025360593, \
          0.4172714025360593, \
          0.4172714025360593, \
          0.4172714025360593, \
          0.4172714025360593, \
          0.8529096418585074, \
          0.8529096418585074, \
          0.8529096418585074, \
          0.8529096418585074, \
          0.8529096418585074, \
          0.8529096418585074, \
          0.1470903581414927, \
          0.1470903581414927, \
          0.1470903581414927, \
          0.1470903581414927, \
          0.1470903581414927, \
          0.1470903581414927, \
          0.8283291277845266, \
          0.8283291277845266, \
          0.8283291277845266, \
          0.8283291277845266, \
          0.8283291277845266, \
          0.8283291277845266, \
          0.1716708722154733, \
          0.1716708722154733, \
          0.1716708722154733, \
          0.1716708722154733, \
          0.1716708722154733, \
          0.1716708722154733, \
          0.9370173839969559, \
          0.9370173839969559, \
          0.9370173839969559, \
          0.9370173839969559, \
          0.9370173839969559, \
          0.9370173839969559, \
          0.0629826160030441, \
          0.0629826160030441, \
          0.0629826160030441, \
          0.0629826160030441, \
          0.0629826160030441, \
          0.0629826160030441, \
          0.9939758307965130, \
          0.9939758307965130, \
          0.9939758307965130, \
          0.9939758307965130, \
          0.9939758307965130, \
          0.9939758307965130, \
          0.0060241692034870, \
          0.0060241692034870, \
          0.0060241692034870, \
          0.0060241692034870, \
          0.0060241692034870, \
          0.0060241692034870, \
          0.5786001946994722, \
          0.5786001946994722, \
          0.5786001946994722, \
          0.5786001946994722, \
          0.5786001946994722, \
          0.5786001946994722, \
          0.4213998053005278, \
          0.4213998053005278, \
          0.4213998053005278, \
          0.4213998053005278, \
          0.4213998053005278, \
          0.4213998053005278, \
          0.8755215159278712, \
          0.8755215159278712, \
          0.8755215159278712, \
          0.8755215159278712, \
          0.8755215159278712, \
          0.8755215159278712, \
          0.1244784840721288, \
          0.1244784840721288, \
          0.1244784840721288, \
          0.1244784840721288, \
          0.1244784840721288, \
          0.1244784840721288, \
          0.9893261490512200, \
          0.9893261490512200, \
          0.9893261490512200, \
          0.9893261490512200, \
          0.9893261490512200, \
          0.9893261490512200, \
          0.0106738509487800, \
          0.0106738509487800, \
          0.0106738509487800, \
          0.0106738509487800, \
          0.0106738509487800, \
          0.0106738509487800, \
          0.9893821585030006, \
          0.9893821585030006, \
          0.9893821585030006, \
          0.9893821585030006, \
          0.9893821585030006, \
          0.9893821585030006, \
          0.0106178414969994, \
          0.0106178414969994, \
          0.0106178414969994, \
          0.0106178414969994, \
          0.0106178414969994, \
          0.0106178414969994, \
          0.7966282776345323, \
          0.7966282776345323, \
          0.7966282776345323, \
          0.7966282776345323, \
          0.7966282776345323, \
          0.7966282776345323, \
          0.2033717223654677, \
          0.2033717223654677, \
          0.2033717223654677, \
          0.2033717223654677, \
          0.2033717223654677, \
          0.2033717223654677 ] )

  w = np.array ( [ \
          0.0022576928480960, \
          0.0022576928480960, \
          0.0022576928480960, \
          0.0022576928480960, \
          0.0022576928480960, \
          0.0022576928480960, \
          0.0035220009936119, \
          0.0035220009936119, \
          0.0035220009936119, \
          0.0035220009936119, \
          0.0035220009936119, \
          0.0035220009936119, \
          0.0044617234977870, \
          0.0044617234977870, \
          0.0044617234977870, \
          0.0044617234977870, \
          0.0044617234977870, \
          0.0044617234977870, \
          0.0003707999359392, \
          0.0003707999359392, \
          0.0003707999359392, \
          0.0003707999359392, \
          0.0003707999359392, \
          0.0003707999359392, \
          0.0024236611427218, \
          0.0024236611427218, \
          0.0024236611427218, \
          0.0024236611427218, \
          0.0024236611427218, \
          0.0024236611427218, \
          0.0028149967000162, \
          0.0028149967000162, \
          0.0028149967000162, \
          0.0028149967000162, \
          0.0028149967000162, \
          0.0028149967000162, \
          0.0053376421669576, \
          0.0053376421669576, \
          0.0053376421669576, \
          0.0053376421669576, \
          0.0053376421669576, \
          0.0053376421669576, \
          0.0085742666644647, \
          0.0085742666644647, \
          0.0085742666644647, \
          0.0085742666644647, \
          0.0085742666644647, \
          0.0085742666644647, \
          0.0022657258714867, \
          0.0022657258714867, \
          0.0022657258714867, \
          0.0022657258714867, \
          0.0022657258714867, \
          0.0022657258714867, \
          0.0029551579597074, \
          0.0029551579597074, \
          0.0029551579597074, \
          0.0029551579597074, \
          0.0029551579597074, \
          0.0029551579597074, \
          0.0039194664968460, \
          0.0039194664968460, \
          0.0039194664968460, \
          0.0039194664968460, \
          0.0039194664968460, \
          0.0039194664968460, \
          0.0006030674708196, \
          0.0006030674708196, \
          0.0006030674708196, \
          0.0006030674708196, \
          0.0006030674708196, \
          0.0006030674708196, \
          0.0045779809945426, \
          0.0045779809945426, \
          0.0045779809945426, \
          0.0045779809945426, \
          0.0045779809945426, \
          0.0045779809945426, \
          0.0024306636423047, \
          0.0024306636423047, \
          0.0024306636423047, \
          0.0024306636423047, \
          0.0024306636423047, \
          0.0024306636423047, \
          0.0021599699258395, \
          0.0021599699258395, \
          0.0021599699258395, \
          0.0021599699258395, \
          0.0021599699258395, \
          0.0021599699258395, \
          0.0079010510892335, \
          0.0079010510892335, \
          0.0079010510892335, \
          0.0079010510892335, \
          0.0079010510892335, \
          0.0079010510892335, \
          0.0021738453915315, \
          0.0021738453915315, \
          0.0021738453915315, \
          0.0021738453915315, \
          0.0021738453915315, \
          0.0021738453915315, \
          0.0022486463151748, \
          0.0022486463151748, \
          0.0022486463151748, \
          0.0022486463151748, \
          0.0022486463151748, \
          0.0022486463151748, \
          0.0003442548195872, \
          0.0003442548195872, \
          0.0003442548195872, \
          0.0003442548195872, \
          0.0003442548195872, \
          0.0003442548195872, \
          0.0080699355816128, \
          0.0080699355816128, \
          0.0080699355816128, \
          0.0080699355816128, \
          0.0080699355816128, \
          0.0080699355816128, \
          0.0023877231635901, \
          0.0023877231635901, \
          0.0023877231635901, \
          0.0023877231635901, \
          0.0023877231635901, \
          0.0023877231635901, \
          0.0023877231635901, \
          0.0023877231635901, \
          0.0023877231635901, \
          0.0023877231635901, \
          0.0023877231635901, \
          0.0023877231635901, \
          0.0034305282210409, \
          0.0034305282210409, \
          0.0034305282210409, \
          0.0034305282210409, \
          0.0034305282210409, \
          0.0034305282210409, \
          0.0034305282210409, \
          0.0034305282210409, \
          0.0034305282210409, \
          0.0034305282210409, \
          0.0034305282210409, \
          0.0034305282210409, \
          0.0060295453672165, \
          0.0060295453672165, \
          0.0060295453672165, \
          0.0060295453672165, \
          0.0060295453672165, \
          0.0060295453672165, \
          0.0060295453672165, \
          0.0060295453672165, \
          0.0060295453672165, \
          0.0060295453672165, \
          0.0060295453672165, \
          0.0060295453672165, \
          0.0032768238791581, \
          0.0032768238791581, \
          0.0032768238791581, \
          0.0032768238791581, \
          0.0032768238791581, \
          0.0032768238791581, \
          0.0032768238791581, \
          0.0032768238791581, \
          0.0032768238791581, \
          0.0032768238791581, \
          0.0032768238791581, \
          0.0032768238791581, \
          0.0036635492105407, \
          0.0036635492105407, \
          0.0036635492105407, \
          0.0036635492105407, \
          0.0036635492105407, \
          0.0036635492105407, \
          0.0036635492105407, \
          0.0036635492105407, \
          0.0036635492105407, \
          0.0036635492105407, \
          0.0036635492105407, \
          0.0036635492105407, \
          0.0044244882628077, \
          0.0044244882628077, \
          0.0044244882628077, \
          0.0044244882628077, \
          0.0044244882628077, \
          0.0044244882628077, \
          0.0044244882628077, \
          0.0044244882628077, \
          0.0044244882628077, \
          0.0044244882628077, \
          0.0044244882628077, \
          0.0044244882628077, \
          0.0027600635232146, \
          0.0027600635232146, \
          0.0027600635232146, \
          0.0027600635232146, \
          0.0027600635232146, \
          0.0027600635232146, \
          0.0027600635232146, \
          0.0027600635232146, \
          0.0027600635232146, \
          0.0027600635232146, \
          0.0027600635232146, \
          0.0027600635232146, \
          0.0013921098894439, \
          0.0013921098894439, \
          0.0013921098894439, \
          0.0013921098894439, \
          0.0013921098894439, \
          0.0013921098894439, \
          0.0013921098894439, \
          0.0013921098894439, \
          0.0013921098894439, \
          0.0013921098894439, \
          0.0013921098894439, \
          0.0013921098894439, \
          0.0021384358726425, \
          0.0021384358726425, \
          0.0021384358726425, \
          0.0021384358726425, \
          0.0021384358726425, \
          0.0021384358726425, \
          0.0021384358726425, \
          0.0021384358726425, \
          0.0021384358726425, \
          0.0021384358726425, \
          0.0021384358726425, \
          0.0021384358726425, \
          0.0005166067073489, \
          0.0005166067073489, \
          0.0005166067073489, \
          0.0005166067073489, \
          0.0005166067073489, \
          0.0005166067073489, \
          0.0005166067073489, \
          0.0005166067073489, \
          0.0005166067073489, \
          0.0005166067073489, \
          0.0005166067073489, \
          0.0005166067073489, \
          0.0019539531411333, \
          0.0019539531411333, \
          0.0019539531411333, \
          0.0019539531411333, \
          0.0019539531411333, \
          0.0019539531411333, \
          0.0019539531411333, \
          0.0019539531411333, \
          0.0019539531411333, \
          0.0019539531411333, \
          0.0019539531411333, \
          0.0019539531411333, \
          0.0012550085983638, \
          0.0012550085983638, \
          0.0012550085983638, \
          0.0012550085983638, \
          0.0012550085983638, \
          0.0012550085983638, \
          0.0012550085983638, \
          0.0012550085983638, \
          0.0012550085983638, \
          0.0012550085983638, \
          0.0012550085983638, \
          0.0012550085983638, \
          0.0010423341141818, \
          0.0010423341141818, \
          0.0010423341141818, \
          0.0010423341141818, \
          0.0010423341141818, \
          0.0010423341141818, \
          0.0010423341141818, \
          0.0010423341141818, \
          0.0010423341141818, \
          0.0010423341141818, \
          0.0010423341141818, \
          0.0010423341141818, \
          0.0012793420418862, \
          0.0012793420418862, \
          0.0012793420418862, \
          0.0012793420418862, \
          0.0012793420418862, \
          0.0012793420418862, \
          0.0012793420418862, \
          0.0012793420418862, \
          0.0012793420418862, \
          0.0012793420418862, \
          0.0012793420418862, \
          0.0012793420418862, \
          0.0010877722341374, \
          0.0010877722341374, \
          0.0010877722341374, \
          0.0010877722341374, \
          0.0010877722341374, \
          0.0010877722341374, \
          0.0010877722341374, \
          0.0010877722341374, \
          0.0010877722341374, \
          0.0010877722341374, \
          0.0010877722341374, \
          0.0010877722341374, \
          0.0008506443220554, \
          0.0008506443220554, \
          0.0008506443220554, \
          0.0008506443220554, \
          0.0008506443220554, \
          0.0008506443220554, \
          0.0008506443220554, \
          0.0008506443220554, \
          0.0008506443220554, \
          0.0008506443220554, \
          0.0008506443220554, \
          0.0008506443220554, \
          0.0010717384362760, \
          0.0010717384362760, \
          0.0010717384362760, \
          0.0010717384362760, \
          0.0010717384362760, \
          0.0010717384362760, \
          0.0010717384362760, \
          0.0010717384362760, \
          0.0010717384362760, \
          0.0010717384362760, \
          0.0010717384362760, \
          0.0010717384362760, \
          0.0012223898383723, \
          0.0012223898383723, \
          0.0012223898383723, \
          0.0012223898383723, \
          0.0012223898383723, \
          0.0012223898383723, \
          0.0012223898383723, \
          0.0012223898383723, \
          0.0012223898383723, \
          0.0012223898383723, \
          0.0012223898383723, \
          0.0012223898383723, \
          0.0014264821649004, \
          0.0014264821649004, \
          0.0014264821649004, \
          0.0014264821649004, \
          0.0014264821649004, \
          0.0014264821649004, \
          0.0014264821649004, \
          0.0014264821649004, \
          0.0014264821649004, \
          0.0014264821649004, \
          0.0014264821649004, \
          0.0014264821649004, \
          0.0038341778997734, \
          0.0038341778997734, \
          0.0038341778997734, \
          0.0038341778997734, \
          0.0038341778997734, \
          0.0038341778997734, \
          0.0038341778997734, \
          0.0038341778997734, \
          0.0038341778997734, \
          0.0038341778997734, \
          0.0038341778997734, \
          0.0038341778997734, \
          0.0004758021594541, \
          0.0004758021594541, \
          0.0004758021594541, \
          0.0004758021594541, \
          0.0004758021594541, \
          0.0004758021594541, \
          0.0004758021594541, \
          0.0004758021594541, \
          0.0004758021594541, \
          0.0004758021594541, \
          0.0004758021594541, \
          0.0004758021594541, \
          0.0003711298716255, \
          0.0003711298716255, \
          0.0003711298716255, \
          0.0003711298716255, \
          0.0003711298716255, \
          0.0003711298716255, \
          0.0003711298716255, \
          0.0003711298716255, \
          0.0003711298716255, \
          0.0003711298716255, \
          0.0003711298716255, \
          0.0003711298716255, \
          0.0027364096600290, \
          0.0027364096600290, \
          0.0027364096600290, \
          0.0027364096600290, \
          0.0027364096600290, \
          0.0027364096600290, \
          0.0027364096600290, \
          0.0027364096600290, \
          0.0027364096600290, \
          0.0027364096600290, \
          0.0027364096600290, \
          0.0027364096600290 ] )

  return x, y, z, w

def rule19 ( ):

#*****************************************************************************80
#
## rule19() returns the prism rule of precision 19.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4935398626809867, \
          0.4935398626809867, \
          0.0129202746380266, \
          0.2767659367008514, \
          0.2767659367008514, \
          0.4464681265982973, \
          0.0545777948502843, \
          0.0545777948502843, \
          0.8908444102994315, \
          0.0139969735218886, \
          0.0139969735218886, \
          0.9720060529562228, \
          0.1418740786751734, \
          0.1418740786751734, \
          0.7162518426496531, \
          0.1418740786751734, \
          0.1418740786751734, \
          0.7162518426496531, \
          0.0083955990101041, \
          0.0083955990101041, \
          0.9832088019797917, \
          0.0083955990101041, \
          0.0083955990101041, \
          0.9832088019797917, \
          0.1035973359771996, \
          0.1035973359771996, \
          0.7928053280456009, \
          0.1035973359771996, \
          0.1035973359771996, \
          0.7928053280456009, \
          0.3956080996828434, \
          0.3956080996828434, \
          0.2087838006343133, \
          0.3956080996828434, \
          0.3956080996828434, \
          0.2087838006343133, \
          0.0140019311977436, \
          0.0140019311977436, \
          0.9719961376045129, \
          0.0140019311977436, \
          0.0140019311977436, \
          0.9719961376045129, \
          0.4801897764603656, \
          0.4801897764603656, \
          0.0396204470792688, \
          0.4801897764603656, \
          0.4801897764603656, \
          0.0396204470792688, \
          0.1623484102426076, \
          0.1623484102426076, \
          0.6753031795147848, \
          0.1623484102426076, \
          0.1623484102426076, \
          0.6753031795147848, \
          0.4972236736522475, \
          0.4972236736522475, \
          0.0055526526955051, \
          0.4972236736522475, \
          0.4972236736522475, \
          0.0055526526955051, \
          0.1990216655966096, \
          0.1990216655966096, \
          0.6019566688067807, \
          0.1990216655966096, \
          0.1990216655966096, \
          0.6019566688067807, \
          0.1202889101503504, \
          0.1202889101503504, \
          0.7594221796992991, \
          0.1202889101503504, \
          0.1202889101503504, \
          0.7594221796992991, \
          0.0532191526098831, \
          0.0532191526098831, \
          0.8935616947802337, \
          0.0532191526098831, \
          0.0532191526098831, \
          0.8935616947802337, \
          0.4012796612843944, \
          0.4012796612843944, \
          0.1974406774312114, \
          0.4012796612843944, \
          0.4012796612843944, \
          0.1974406774312114, \
          0.1089883669604236, \
          0.1089883669604236, \
          0.7820232660791528, \
          0.1089883669604236, \
          0.1089883669604236, \
          0.7820232660791528, \
          0.4472748897677901, \
          0.4472748897677901, \
          0.1054502204644198, \
          0.4472748897677901, \
          0.4472748897677901, \
          0.1054502204644198, \
          0.0692335448571578, \
          0.0692335448571578, \
          0.8615329102856844, \
          0.0692335448571578, \
          0.0692335448571578, \
          0.8615329102856844, \
          0.2475145234973103, \
          0.2475145234973103, \
          0.5049709530053793, \
          0.2475145234973103, \
          0.2475145234973103, \
          0.5049709530053793, \
          0.4533377451558121, \
          0.4533377451558121, \
          0.0933245096883758, \
          0.4533377451558121, \
          0.4533377451558121, \
          0.0933245096883758, \
          0.0180837411268107, \
          0.0180837411268107, \
          0.9638325177463786, \
          0.0180837411268107, \
          0.0180837411268107, \
          0.9638325177463786, \
          0.1297897131077726, \
          0.0069174965695053, \
          0.1297897131077726, \
          0.8632927903227221, \
          0.0069174965695053, \
          0.8632927903227221, \
          0.3779418721990778, \
          0.0310061742359910, \
          0.3779418721990778, \
          0.5910519535649312, \
          0.0310061742359910, \
          0.5910519535649312, \
          0.0644631311955231, \
          0.2203251202566757, \
          0.0644631311955231, \
          0.7152117485478011, \
          0.2203251202566757, \
          0.7152117485478011, \
          0.1625899734623090, \
          0.2824754920851798, \
          0.1625899734623090, \
          0.5549345344525113, \
          0.2824754920851798, \
          0.5549345344525113, \
          0.1625899734623090, \
          0.2824754920851798, \
          0.1625899734623090, \
          0.5549345344525113, \
          0.2824754920851798, \
          0.5549345344525113, \
          0.0081184148094398, \
          0.0547883511283449, \
          0.0081184148094398, \
          0.9370932340622153, \
          0.0547883511283449, \
          0.9370932340622153, \
          0.0081184148094398, \
          0.0547883511283449, \
          0.0081184148094398, \
          0.9370932340622153, \
          0.0547883511283449, \
          0.9370932340622153, \
          0.6582273496659641, \
          0.1178005364736766, \
          0.6582273496659641, \
          0.2239721138603593, \
          0.1178005364736766, \
          0.2239721138603593, \
          0.6582273496659641, \
          0.1178005364736766, \
          0.6582273496659641, \
          0.2239721138603593, \
          0.1178005364736766, \
          0.2239721138603593, \
          0.2876874815978630, \
          0.0355268541454468, \
          0.2876874815978630, \
          0.6767856642566902, \
          0.0355268541454468, \
          0.6767856642566902, \
          0.2876874815978630, \
          0.0355268541454468, \
          0.2876874815978630, \
          0.6767856642566902, \
          0.0355268541454468, \
          0.6767856642566902, \
          0.2839484400308330, \
          0.2073917255967352, \
          0.2839484400308330, \
          0.5086598343724318, \
          0.2073917255967352, \
          0.5086598343724318, \
          0.2839484400308330, \
          0.2073917255967352, \
          0.2839484400308330, \
          0.5086598343724318, \
          0.2073917255967352, \
          0.5086598343724318, \
          0.0282457003834953, \
          0.0862230026956853, \
          0.0282457003834953, \
          0.8855312969208194, \
          0.0862230026956853, \
          0.8855312969208194, \
          0.0282457003834953, \
          0.0862230026956853, \
          0.0282457003834953, \
          0.8855312969208194, \
          0.0862230026956853, \
          0.8855312969208194, \
          0.3915043117238656, \
          0.0056196516036861, \
          0.3915043117238656, \
          0.6028760366724483, \
          0.0056196516036861, \
          0.6028760366724483, \
          0.3915043117238656, \
          0.0056196516036861, \
          0.3915043117238656, \
          0.6028760366724483, \
          0.0056196516036861, \
          0.6028760366724483, \
          0.0737667613724345, \
          0.3389265718024346, \
          0.0737667613724345, \
          0.5873066668251310, \
          0.3389265718024346, \
          0.5873066668251310, \
          0.0737667613724345, \
          0.3389265718024346, \
          0.0737667613724345, \
          0.5873066668251310, \
          0.3389265718024346, \
          0.5873066668251310, \
          0.1582419524500696, \
          0.0080205188978798, \
          0.1582419524500696, \
          0.8337375286520506, \
          0.0080205188978798, \
          0.8337375286520506, \
          0.1582419524500696, \
          0.0080205188978798, \
          0.1582419524500696, \
          0.8337375286520506, \
          0.0080205188978798, \
          0.8337375286520506, \
          0.2270465393157224, \
          0.0761183063986999, \
          0.2270465393157224, \
          0.6968351542855776, \
          0.0761183063986999, \
          0.6968351542855776, \
          0.2270465393157224, \
          0.0761183063986999, \
          0.2270465393157224, \
          0.6968351542855776, \
          0.0761183063986999, \
          0.6968351542855776, \
          0.0107402320272877, \
          0.0674860196923538, \
          0.0107402320272877, \
          0.9217737482803585, \
          0.0674860196923538, \
          0.9217737482803585, \
          0.0107402320272877, \
          0.0674860196923538, \
          0.0107402320272877, \
          0.9217737482803585, \
          0.0674860196923538, \
          0.9217737482803585, \
          0.0450629754431290, \
          0.1495289831435912, \
          0.0450629754431290, \
          0.8054080414132798, \
          0.1495289831435912, \
          0.8054080414132798, \
          0.0450629754431290, \
          0.1495289831435912, \
          0.0450629754431290, \
          0.8054080414132798, \
          0.1495289831435912, \
          0.8054080414132798, \
          0.3899263834124326, \
          0.0536599901206231, \
          0.3899263834124326, \
          0.5564136264669443, \
          0.0536599901206231, \
          0.5564136264669443, \
          0.3899263834124326, \
          0.0536599901206231, \
          0.3899263834124326, \
          0.5564136264669443, \
          0.0536599901206231, \
          0.5564136264669443, \
          0.0142616821078597, \
          0.4039638109964547, \
          0.0142616821078597, \
          0.5817745068956857, \
          0.4039638109964547, \
          0.5817745068956857, \
          0.0142616821078597, \
          0.4039638109964547, \
          0.0142616821078597, \
          0.5817745068956857, \
          0.4039638109964547, \
          0.5817745068956857, \
          0.3314062155351160, \
          0.0088330831166114, \
          0.3314062155351160, \
          0.6597607013482726, \
          0.0088330831166114, \
          0.6597607013482726, \
          0.3314062155351160, \
          0.0088330831166114, \
          0.3314062155351160, \
          0.6597607013482726, \
          0.0088330831166114, \
          0.6597607013482726, \
          0.1223644156202090, \
          0.0103923793593637, \
          0.1223644156202090, \
          0.8672432050204273, \
          0.0103923793593637, \
          0.8672432050204273, \
          0.1223644156202090, \
          0.0103923793593637, \
          0.1223644156202090, \
          0.8672432050204273, \
          0.0103923793593637, \
          0.8672432050204273, \
          0.2929652829983945, \
          0.1324448044285512, \
          0.2929652829983945, \
          0.5745899125730543, \
          0.1324448044285512, \
          0.5745899125730543, \
          0.2929652829983945, \
          0.1324448044285512, \
          0.2929652829983945, \
          0.5745899125730543, \
          0.1324448044285512, \
          0.5745899125730543, \
          0.2534748953911949, \
          0.0535147091599154, \
          0.2534748953911949, \
          0.6930103954488898, \
          0.0535147091599154, \
          0.6930103954488898, \
          0.2534748953911949, \
          0.0535147091599154, \
          0.2534748953911949, \
          0.6930103954488898, \
          0.0535147091599154, \
          0.6930103954488898, \
          0.0440785872085001, \
          0.1461188761758480, \
          0.0440785872085001, \
          0.8098025366156519, \
          0.1461188761758480, \
          0.8098025366156519, \
          0.0440785872085001, \
          0.1461188761758480, \
          0.0440785872085001, \
          0.8098025366156519, \
          0.1461188761758480, \
          0.8098025366156519, \
          0.5031457633505478, \
          0.1264604222462178, \
          0.5031457633505478, \
          0.3703938144032344, \
          0.1264604222462178, \
          0.3703938144032344, \
          0.5031457633505478, \
          0.1264604222462178, \
          0.5031457633505478, \
          0.3703938144032344, \
          0.1264604222462178, \
          0.3703938144032344, \
          0.0087499979841172, \
          0.2433623618774898, \
          0.0087499979841172, \
          0.7478876401383930, \
          0.2433623618774898, \
          0.7478876401383930, \
          0.0087499979841172, \
          0.2433623618774898, \
          0.0087499979841172, \
          0.7478876401383930, \
          0.2433623618774898, \
          0.7478876401383930, \
          0.4433279475253553, \
          0.2569581578007861, \
          0.4433279475253553, \
          0.2997138946738586, \
          0.2569581578007861, \
          0.2997138946738586, \
          0.4433279475253553, \
          0.2569581578007861, \
          0.4433279475253553, \
          0.2997138946738586, \
          0.2569581578007861, \
          0.2997138946738586, \
          0.2485412372956145, \
          0.0112771540337380, \
          0.2485412372956145, \
          0.7401816086706475, \
          0.0112771540337380, \
          0.7401816086706475, \
          0.2485412372956145, \
          0.0112771540337380, \
          0.2485412372956145, \
          0.7401816086706475, \
          0.0112771540337380, \
          0.7401816086706475 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.3333333333333333, \
          0.4935398626809867, \
          0.0129202746380266, \
          0.4935398626809867, \
          0.2767659367008514, \
          0.4464681265982973, \
          0.2767659367008514, \
          0.0545777948502843, \
          0.8908444102994315, \
          0.0545777948502843, \
          0.0139969735218886, \
          0.9720060529562228, \
          0.0139969735218886, \
          0.1418740786751734, \
          0.7162518426496531, \
          0.1418740786751734, \
          0.1418740786751734, \
          0.7162518426496531, \
          0.1418740786751734, \
          0.0083955990101041, \
          0.9832088019797917, \
          0.0083955990101041, \
          0.0083955990101041, \
          0.9832088019797917, \
          0.0083955990101041, \
          0.1035973359771996, \
          0.7928053280456009, \
          0.1035973359771996, \
          0.1035973359771996, \
          0.7928053280456009, \
          0.1035973359771996, \
          0.3956080996828434, \
          0.2087838006343133, \
          0.3956080996828434, \
          0.3956080996828434, \
          0.2087838006343133, \
          0.3956080996828434, \
          0.0140019311977436, \
          0.9719961376045129, \
          0.0140019311977436, \
          0.0140019311977436, \
          0.9719961376045129, \
          0.0140019311977436, \
          0.4801897764603656, \
          0.0396204470792688, \
          0.4801897764603656, \
          0.4801897764603656, \
          0.0396204470792688, \
          0.4801897764603656, \
          0.1623484102426076, \
          0.6753031795147848, \
          0.1623484102426076, \
          0.1623484102426076, \
          0.6753031795147848, \
          0.1623484102426076, \
          0.4972236736522475, \
          0.0055526526955051, \
          0.4972236736522475, \
          0.4972236736522475, \
          0.0055526526955051, \
          0.4972236736522475, \
          0.1990216655966096, \
          0.6019566688067807, \
          0.1990216655966096, \
          0.1990216655966096, \
          0.6019566688067807, \
          0.1990216655966096, \
          0.1202889101503504, \
          0.7594221796992991, \
          0.1202889101503504, \
          0.1202889101503504, \
          0.7594221796992991, \
          0.1202889101503504, \
          0.0532191526098831, \
          0.8935616947802337, \
          0.0532191526098831, \
          0.0532191526098831, \
          0.8935616947802337, \
          0.0532191526098831, \
          0.4012796612843944, \
          0.1974406774312114, \
          0.4012796612843944, \
          0.4012796612843944, \
          0.1974406774312114, \
          0.4012796612843944, \
          0.1089883669604236, \
          0.7820232660791528, \
          0.1089883669604236, \
          0.1089883669604236, \
          0.7820232660791528, \
          0.1089883669604236, \
          0.4472748897677901, \
          0.1054502204644198, \
          0.4472748897677901, \
          0.4472748897677901, \
          0.1054502204644198, \
          0.4472748897677901, \
          0.0692335448571578, \
          0.8615329102856844, \
          0.0692335448571578, \
          0.0692335448571578, \
          0.8615329102856844, \
          0.0692335448571578, \
          0.2475145234973103, \
          0.5049709530053793, \
          0.2475145234973103, \
          0.2475145234973103, \
          0.5049709530053793, \
          0.2475145234973103, \
          0.4533377451558121, \
          0.0933245096883758, \
          0.4533377451558121, \
          0.4533377451558121, \
          0.0933245096883758, \
          0.4533377451558121, \
          0.0180837411268107, \
          0.9638325177463786, \
          0.0180837411268107, \
          0.0180837411268107, \
          0.9638325177463786, \
          0.0180837411268107, \
          0.0069174965695053, \
          0.1297897131077726, \
          0.8632927903227221, \
          0.1297897131077726, \
          0.8632927903227221, \
          0.0069174965695053, \
          0.0310061742359910, \
          0.3779418721990778, \
          0.5910519535649312, \
          0.3779418721990778, \
          0.5910519535649312, \
          0.0310061742359910, \
          0.2203251202566757, \
          0.0644631311955231, \
          0.7152117485478011, \
          0.0644631311955231, \
          0.7152117485478011, \
          0.2203251202566757, \
          0.2824754920851798, \
          0.1625899734623090, \
          0.5549345344525113, \
          0.1625899734623090, \
          0.5549345344525113, \
          0.2824754920851798, \
          0.2824754920851798, \
          0.1625899734623090, \
          0.5549345344525113, \
          0.1625899734623090, \
          0.5549345344525113, \
          0.2824754920851798, \
          0.0547883511283449, \
          0.0081184148094398, \
          0.9370932340622153, \
          0.0081184148094398, \
          0.9370932340622153, \
          0.0547883511283449, \
          0.0547883511283449, \
          0.0081184148094398, \
          0.9370932340622153, \
          0.0081184148094398, \
          0.9370932340622153, \
          0.0547883511283449, \
          0.1178005364736766, \
          0.6582273496659641, \
          0.2239721138603593, \
          0.6582273496659641, \
          0.2239721138603593, \
          0.1178005364736766, \
          0.1178005364736766, \
          0.6582273496659641, \
          0.2239721138603593, \
          0.6582273496659641, \
          0.2239721138603593, \
          0.1178005364736766, \
          0.0355268541454468, \
          0.2876874815978630, \
          0.6767856642566902, \
          0.2876874815978630, \
          0.6767856642566902, \
          0.0355268541454468, \
          0.0355268541454468, \
          0.2876874815978630, \
          0.6767856642566902, \
          0.2876874815978630, \
          0.6767856642566902, \
          0.0355268541454468, \
          0.2073917255967352, \
          0.2839484400308330, \
          0.5086598343724318, \
          0.2839484400308330, \
          0.5086598343724318, \
          0.2073917255967352, \
          0.2073917255967352, \
          0.2839484400308330, \
          0.5086598343724318, \
          0.2839484400308330, \
          0.5086598343724318, \
          0.2073917255967352, \
          0.0862230026956853, \
          0.0282457003834953, \
          0.8855312969208194, \
          0.0282457003834953, \
          0.8855312969208194, \
          0.0862230026956853, \
          0.0862230026956853, \
          0.0282457003834953, \
          0.8855312969208194, \
          0.0282457003834953, \
          0.8855312969208194, \
          0.0862230026956853, \
          0.0056196516036861, \
          0.3915043117238656, \
          0.6028760366724483, \
          0.3915043117238656, \
          0.6028760366724483, \
          0.0056196516036861, \
          0.0056196516036861, \
          0.3915043117238656, \
          0.6028760366724483, \
          0.3915043117238656, \
          0.6028760366724483, \
          0.0056196516036861, \
          0.3389265718024346, \
          0.0737667613724345, \
          0.5873066668251310, \
          0.0737667613724345, \
          0.5873066668251310, \
          0.3389265718024346, \
          0.3389265718024346, \
          0.0737667613724345, \
          0.5873066668251310, \
          0.0737667613724345, \
          0.5873066668251310, \
          0.3389265718024346, \
          0.0080205188978798, \
          0.1582419524500696, \
          0.8337375286520506, \
          0.1582419524500696, \
          0.8337375286520506, \
          0.0080205188978798, \
          0.0080205188978798, \
          0.1582419524500696, \
          0.8337375286520506, \
          0.1582419524500696, \
          0.8337375286520506, \
          0.0080205188978798, \
          0.0761183063986999, \
          0.2270465393157224, \
          0.6968351542855776, \
          0.2270465393157224, \
          0.6968351542855776, \
          0.0761183063986999, \
          0.0761183063986999, \
          0.2270465393157224, \
          0.6968351542855776, \
          0.2270465393157224, \
          0.6968351542855776, \
          0.0761183063986999, \
          0.0674860196923538, \
          0.0107402320272877, \
          0.9217737482803585, \
          0.0107402320272877, \
          0.9217737482803585, \
          0.0674860196923538, \
          0.0674860196923538, \
          0.0107402320272877, \
          0.9217737482803585, \
          0.0107402320272877, \
          0.9217737482803585, \
          0.0674860196923538, \
          0.1495289831435912, \
          0.0450629754431290, \
          0.8054080414132798, \
          0.0450629754431290, \
          0.8054080414132798, \
          0.1495289831435912, \
          0.1495289831435912, \
          0.0450629754431290, \
          0.8054080414132798, \
          0.0450629754431290, \
          0.8054080414132798, \
          0.1495289831435912, \
          0.0536599901206231, \
          0.3899263834124326, \
          0.5564136264669443, \
          0.3899263834124326, \
          0.5564136264669443, \
          0.0536599901206231, \
          0.0536599901206231, \
          0.3899263834124326, \
          0.5564136264669443, \
          0.3899263834124326, \
          0.5564136264669443, \
          0.0536599901206231, \
          0.4039638109964547, \
          0.0142616821078597, \
          0.5817745068956857, \
          0.0142616821078597, \
          0.5817745068956857, \
          0.4039638109964547, \
          0.4039638109964547, \
          0.0142616821078597, \
          0.5817745068956857, \
          0.0142616821078597, \
          0.5817745068956857, \
          0.4039638109964547, \
          0.0088330831166114, \
          0.3314062155351160, \
          0.6597607013482726, \
          0.3314062155351160, \
          0.6597607013482726, \
          0.0088330831166114, \
          0.0088330831166114, \
          0.3314062155351160, \
          0.6597607013482726, \
          0.3314062155351160, \
          0.6597607013482726, \
          0.0088330831166114, \
          0.0103923793593637, \
          0.1223644156202090, \
          0.8672432050204273, \
          0.1223644156202090, \
          0.8672432050204273, \
          0.0103923793593637, \
          0.0103923793593637, \
          0.1223644156202090, \
          0.8672432050204273, \
          0.1223644156202090, \
          0.8672432050204273, \
          0.0103923793593637, \
          0.1324448044285512, \
          0.2929652829983945, \
          0.5745899125730543, \
          0.2929652829983945, \
          0.5745899125730543, \
          0.1324448044285512, \
          0.1324448044285512, \
          0.2929652829983945, \
          0.5745899125730543, \
          0.2929652829983945, \
          0.5745899125730543, \
          0.1324448044285512, \
          0.0535147091599154, \
          0.2534748953911949, \
          0.6930103954488898, \
          0.2534748953911949, \
          0.6930103954488898, \
          0.0535147091599154, \
          0.0535147091599154, \
          0.2534748953911949, \
          0.6930103954488898, \
          0.2534748953911949, \
          0.6930103954488898, \
          0.0535147091599154, \
          0.1461188761758480, \
          0.0440785872085001, \
          0.8098025366156519, \
          0.0440785872085001, \
          0.8098025366156519, \
          0.1461188761758480, \
          0.1461188761758480, \
          0.0440785872085001, \
          0.8098025366156519, \
          0.0440785872085001, \
          0.8098025366156519, \
          0.1461188761758480, \
          0.1264604222462178, \
          0.5031457633505478, \
          0.3703938144032344, \
          0.5031457633505478, \
          0.3703938144032344, \
          0.1264604222462178, \
          0.1264604222462178, \
          0.5031457633505478, \
          0.3703938144032344, \
          0.5031457633505478, \
          0.3703938144032344, \
          0.1264604222462178, \
          0.2433623618774898, \
          0.0087499979841172, \
          0.7478876401383930, \
          0.0087499979841172, \
          0.7478876401383930, \
          0.2433623618774898, \
          0.2433623618774898, \
          0.0087499979841172, \
          0.7478876401383930, \
          0.0087499979841172, \
          0.7478876401383930, \
          0.2433623618774898, \
          0.2569581578007861, \
          0.4433279475253553, \
          0.2997138946738586, \
          0.4433279475253553, \
          0.2997138946738586, \
          0.2569581578007861, \
          0.2569581578007861, \
          0.4433279475253553, \
          0.2997138946738586, \
          0.4433279475253553, \
          0.2997138946738586, \
          0.2569581578007861, \
          0.0112771540337380, \
          0.2485412372956145, \
          0.7401816086706475, \
          0.2485412372956145, \
          0.7401816086706475, \
          0.0112771540337380, \
          0.0112771540337380, \
          0.2485412372956145, \
          0.7401816086706475, \
          0.2485412372956145, \
          0.7401816086706475, \
          0.0112771540337380 ] )

  z = np.array ( [ \
          0.7622415410729753, \
          0.2377584589270247, \
          0.5372666694077471, \
          0.4627333305922529, \
          0.9783048646074941, \
          0.0216951353925058, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9776297496930976, \
          0.9776297496930976, \
          0.9776297496930976, \
          0.0223702503069024, \
          0.0223702503069024, \
          0.0223702503069024, \
          0.8365993771201422, \
          0.8365993771201422, \
          0.8365993771201422, \
          0.1634006228798578, \
          0.1634006228798578, \
          0.1634006228798578, \
          0.3997141071880904, \
          0.3997141071880904, \
          0.3997141071880904, \
          0.6002858928119097, \
          0.6002858928119097, \
          0.6002858928119097, \
          0.6540149239138839, \
          0.6540149239138839, \
          0.6540149239138839, \
          0.3459850760861161, \
          0.3459850760861161, \
          0.3459850760861161, \
          0.6177200943808741, \
          0.6177200943808741, \
          0.6177200943808741, \
          0.3822799056191259, \
          0.3822799056191259, \
          0.3822799056191259, \
          0.7414020374054957, \
          0.7414020374054957, \
          0.7414020374054957, \
          0.2585979625945043, \
          0.2585979625945043, \
          0.2585979625945043, \
          0.3998937993818196, \
          0.3998937993818196, \
          0.3998937993818196, \
          0.6001062006181804, \
          0.6001062006181804, \
          0.6001062006181804, \
          0.8605804354127558, \
          0.8605804354127558, \
          0.8605804354127558, \
          0.1394195645872443, \
          0.1394195645872443, \
          0.1394195645872443, \
          0.8884925585076502, \
          0.8884925585076502, \
          0.8884925585076502, \
          0.1115074414923499, \
          0.1115074414923499, \
          0.1115074414923499, \
          0.1501005238707534, \
          0.1501005238707534, \
          0.1501005238707534, \
          0.8498994761292467, \
          0.8498994761292467, \
          0.8498994761292467, \
          0.8161162302018612, \
          0.8161162302018612, \
          0.8161162302018612, \
          0.1838837697981388, \
          0.1838837697981388, \
          0.1838837697981388, \
          0.9492984016563156, \
          0.9492984016563156, \
          0.9492984016563156, \
          0.0507015983436844, \
          0.0507015983436844, \
          0.0507015983436844, \
          0.8207059136960952, \
          0.8207059136960952, \
          0.8207059136960952, \
          0.1792940863039048, \
          0.1792940863039048, \
          0.1792940863039048, \
          0.5709032950041624, \
          0.5709032950041624, \
          0.5709032950041624, \
          0.4290967049958376, \
          0.4290967049958376, \
          0.4290967049958376, \
          0.9796258147828216, \
          0.9796258147828216, \
          0.9796258147828216, \
          0.0203741852171783, \
          0.0203741852171783, \
          0.0203741852171783, \
          0.9955700370275176, \
          0.9955700370275176, \
          0.9955700370275176, \
          0.0044299629724824, \
          0.0044299629724824, \
          0.0044299629724824, \
          0.9940911680624349, \
          0.9940911680624349, \
          0.9940911680624349, \
          0.0059088319375651, \
          0.0059088319375651, \
          0.0059088319375651, \
          0.9768533807402040, \
          0.9768533807402040, \
          0.9768533807402040, \
          0.0231466192597961, \
          0.0231466192597961, \
          0.0231466192597961, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5784175741511786, \
          0.5784175741511786, \
          0.5784175741511786, \
          0.5784175741511786, \
          0.5784175741511786, \
          0.5784175741511786, \
          0.4215824258488214, \
          0.4215824258488214, \
          0.4215824258488214, \
          0.4215824258488214, \
          0.4215824258488214, \
          0.4215824258488214, \
          0.3016244371993055, \
          0.3016244371993055, \
          0.3016244371993055, \
          0.3016244371993055, \
          0.3016244371993055, \
          0.3016244371993055, \
          0.6983755628006945, \
          0.6983755628006945, \
          0.6983755628006945, \
          0.6983755628006945, \
          0.6983755628006945, \
          0.6983755628006945, \
          0.2557424176244907, \
          0.2557424176244907, \
          0.2557424176244907, \
          0.2557424176244907, \
          0.2557424176244907, \
          0.2557424176244907, \
          0.7442575823755093, \
          0.7442575823755093, \
          0.7442575823755093, \
          0.7442575823755093, \
          0.7442575823755093, \
          0.7442575823755093, \
          0.7933947373630322, \
          0.7933947373630322, \
          0.7933947373630322, \
          0.7933947373630322, \
          0.7933947373630322, \
          0.7933947373630322, \
          0.2066052626369678, \
          0.2066052626369678, \
          0.2066052626369678, \
          0.2066052626369678, \
          0.2066052626369678, \
          0.2066052626369678, \
          0.7415891076871005, \
          0.7415891076871005, \
          0.7415891076871005, \
          0.7415891076871005, \
          0.7415891076871005, \
          0.7415891076871005, \
          0.2584108923128995, \
          0.2584108923128995, \
          0.2584108923128995, \
          0.2584108923128995, \
          0.2584108923128995, \
          0.2584108923128995, \
          0.3990327902043654, \
          0.3990327902043654, \
          0.3990327902043654, \
          0.3990327902043654, \
          0.3990327902043654, \
          0.3990327902043654, \
          0.6009672097956347, \
          0.6009672097956347, \
          0.6009672097956347, \
          0.6009672097956347, \
          0.6009672097956347, \
          0.6009672097956347, \
          0.6658797023892886, \
          0.6658797023892886, \
          0.6658797023892886, \
          0.6658797023892886, \
          0.6658797023892886, \
          0.6658797023892886, \
          0.3341202976107114, \
          0.3341202976107114, \
          0.3341202976107114, \
          0.3341202976107114, \
          0.3341202976107114, \
          0.3341202976107114, \
          0.3477027664621174, \
          0.3477027664621174, \
          0.3477027664621174, \
          0.3477027664621174, \
          0.3477027664621174, \
          0.3477027664621174, \
          0.6522972335378826, \
          0.6522972335378826, \
          0.6522972335378826, \
          0.6522972335378826, \
          0.6522972335378826, \
          0.6522972335378826, \
          0.8121138484281050, \
          0.8121138484281050, \
          0.8121138484281050, \
          0.8121138484281050, \
          0.8121138484281050, \
          0.8121138484281050, \
          0.1878861515718951, \
          0.1878861515718951, \
          0.1878861515718951, \
          0.1878861515718951, \
          0.1878861515718951, \
          0.1878861515718951, \
          0.8889931649237686, \
          0.8889931649237686, \
          0.8889931649237686, \
          0.8889931649237686, \
          0.8889931649237686, \
          0.8889931649237686, \
          0.1110068350762314, \
          0.1110068350762314, \
          0.1110068350762314, \
          0.1110068350762314, \
          0.1110068350762314, \
          0.1110068350762314, \
          0.9152677185839518, \
          0.9152677185839518, \
          0.9152677185839518, \
          0.9152677185839518, \
          0.9152677185839518, \
          0.9152677185839518, \
          0.0847322814160482, \
          0.0847322814160482, \
          0.0847322814160482, \
          0.0847322814160482, \
          0.0847322814160482, \
          0.0847322814160482, \
          0.6968471564249525, \
          0.6968471564249525, \
          0.6968471564249525, \
          0.6968471564249525, \
          0.6968471564249525, \
          0.6968471564249525, \
          0.3031528435750474, \
          0.3031528435750474, \
          0.3031528435750474, \
          0.3031528435750474, \
          0.3031528435750474, \
          0.3031528435750474, \
          0.9181070186825648, \
          0.9181070186825648, \
          0.9181070186825648, \
          0.9181070186825648, \
          0.9181070186825648, \
          0.9181070186825648, \
          0.0818929813174352, \
          0.0818929813174352, \
          0.0818929813174352, \
          0.0818929813174352, \
          0.0818929813174352, \
          0.0818929813174352, \
          0.9772924850792593, \
          0.9772924850792593, \
          0.9772924850792593, \
          0.9772924850792593, \
          0.9772924850792593, \
          0.9772924850792593, \
          0.0227075149207407, \
          0.0227075149207407, \
          0.0227075149207407, \
          0.0227075149207407, \
          0.0227075149207407, \
          0.0227075149207407, \
          0.8548397574539421, \
          0.8548397574539421, \
          0.8548397574539421, \
          0.8548397574539421, \
          0.8548397574539421, \
          0.8548397574539421, \
          0.1451602425460579, \
          0.1451602425460579, \
          0.1451602425460579, \
          0.1451602425460579, \
          0.1451602425460579, \
          0.1451602425460579, \
          0.9950140347594980, \
          0.9950140347594980, \
          0.9950140347594980, \
          0.9950140347594980, \
          0.9950140347594980, \
          0.9950140347594980, \
          0.0049859652405020, \
          0.0049859652405020, \
          0.0049859652405020, \
          0.0049859652405020, \
          0.0049859652405020, \
          0.0049859652405020, \
          0.9589371765386895, \
          0.9589371765386895, \
          0.9589371765386895, \
          0.9589371765386895, \
          0.9589371765386895, \
          0.9589371765386895, \
          0.0410628234613105, \
          0.0410628234613105, \
          0.0410628234613105, \
          0.0410628234613105, \
          0.0410628234613105, \
          0.0410628234613105, \
          0.9922849190190410, \
          0.9922849190190410, \
          0.9922849190190410, \
          0.9922849190190410, \
          0.9922849190190410, \
          0.9922849190190410, \
          0.0077150809809589, \
          0.0077150809809589, \
          0.0077150809809589, \
          0.0077150809809589, \
          0.0077150809809589, \
          0.0077150809809589, \
          0.9284954503109000, \
          0.9284954503109000, \
          0.9284954503109000, \
          0.9284954503109000, \
          0.9284954503109000, \
          0.9284954503109000, \
          0.0715045496891001, \
          0.0715045496891001, \
          0.0715045496891001, \
          0.0715045496891001, \
          0.0715045496891001, \
          0.0715045496891001, \
          0.8243592634966279, \
          0.8243592634966279, \
          0.8243592634966279, \
          0.8243592634966279, \
          0.8243592634966279, \
          0.8243592634966279, \
          0.1756407365033721, \
          0.1756407365033721, \
          0.1756407365033721, \
          0.1756407365033721, \
          0.1756407365033721, \
          0.1756407365033721, \
          0.9514300035294792, \
          0.9514300035294792, \
          0.9514300035294792, \
          0.9514300035294792, \
          0.9514300035294792, \
          0.9514300035294792, \
          0.0485699964705208, \
          0.0485699964705208, \
          0.0485699964705208, \
          0.0485699964705208, \
          0.0485699964705208, \
          0.0485699964705208, \
          0.8768250142401974, \
          0.8768250142401974, \
          0.8768250142401974, \
          0.8768250142401974, \
          0.8768250142401974, \
          0.8768250142401974, \
          0.1231749857598025, \
          0.1231749857598025, \
          0.1231749857598025, \
          0.1231749857598025, \
          0.1231749857598025, \
          0.1231749857598025, \
          0.6209054808190849, \
          0.6209054808190849, \
          0.6209054808190849, \
          0.6209054808190849, \
          0.6209054808190849, \
          0.6209054808190849, \
          0.3790945191809150, \
          0.3790945191809150, \
          0.3790945191809150, \
          0.3790945191809150, \
          0.3790945191809150, \
          0.3790945191809150 ] )

  w = np.array ( [ \
          0.0067665109724298, \
          0.0067665109724298, \
          0.0026669976869157, \
          0.0026669976869157, \
          0.0021982966836122, \
          0.0021982966836122, \
          0.0018035576610240, \
          0.0018035576610240, \
          0.0018035576610240, \
          0.0063544305083746, \
          0.0063544305083746, \
          0.0063544305083746, \
          0.0016368347217208, \
          0.0016368347217208, \
          0.0016368347217208, \
          0.0004893654007837, \
          0.0004893654007837, \
          0.0004893654007837, \
          0.0018464185130403, \
          0.0018464185130403, \
          0.0018464185130403, \
          0.0018464185130403, \
          0.0018464185130403, \
          0.0018464185130403, \
          0.0002773402798746, \
          0.0002773402798746, \
          0.0002773402798746, \
          0.0002773402798746, \
          0.0002773402798746, \
          0.0002773402798746, \
          0.0028236344372154, \
          0.0028236344372154, \
          0.0028236344372154, \
          0.0028236344372154, \
          0.0028236344372154, \
          0.0028236344372154, \
          0.0077260759989331, \
          0.0077260759989331, \
          0.0077260759989331, \
          0.0077260759989331, \
          0.0077260759989331, \
          0.0077260759989331, \
          0.0002193983773241, \
          0.0002193983773241, \
          0.0002193983773241, \
          0.0002193983773241, \
          0.0002193983773241, \
          0.0002193983773241, \
          0.0043666503668884, \
          0.0043666503668884, \
          0.0043666503668884, \
          0.0043666503668884, \
          0.0043666503668884, \
          0.0043666503668884, \
          0.0040292939228197, \
          0.0040292939228197, \
          0.0040292939228197, \
          0.0040292939228197, \
          0.0040292939228197, \
          0.0040292939228197, \
          0.0011307686923958, \
          0.0011307686923958, \
          0.0011307686923958, \
          0.0011307686923958, \
          0.0011307686923958, \
          0.0011307686923958, \
          0.0042878636066862, \
          0.0042878636066862, \
          0.0042878636066862, \
          0.0042878636066862, \
          0.0042878636066862, \
          0.0042878636066862, \
          0.0015922560724046, \
          0.0015922560724046, \
          0.0015922560724046, \
          0.0015922560724046, \
          0.0015922560724046, \
          0.0015922560724046, \
          0.0020526689955830, \
          0.0020526689955830, \
          0.0020526689955830, \
          0.0020526689955830, \
          0.0020526689955830, \
          0.0020526689955830, \
          0.0038947953255298, \
          0.0038947953255298, \
          0.0038947953255298, \
          0.0038947953255298, \
          0.0038947953255298, \
          0.0038947953255298, \
          0.0018034020896591, \
          0.0018034020896591, \
          0.0018034020896591, \
          0.0018034020896591, \
          0.0018034020896591, \
          0.0018034020896591, \
          0.0049066738140960, \
          0.0049066738140960, \
          0.0049066738140960, \
          0.0049066738140960, \
          0.0049066738140960, \
          0.0049066738140960, \
          0.0008385245625735, \
          0.0008385245625735, \
          0.0008385245625735, \
          0.0008385245625735, \
          0.0008385245625735, \
          0.0008385245625735, \
          0.0013444227016777, \
          0.0013444227016777, \
          0.0013444227016777, \
          0.0013444227016777, \
          0.0013444227016777, \
          0.0013444227016777, \
          0.0012123512024300, \
          0.0012123512024300, \
          0.0012123512024300, \
          0.0012123512024300, \
          0.0012123512024300, \
          0.0012123512024300, \
          0.0002704967330299, \
          0.0002704967330299, \
          0.0002704967330299, \
          0.0002704967330299, \
          0.0002704967330299, \
          0.0002704967330299, \
          0.0011944957381629, \
          0.0011944957381629, \
          0.0011944957381629, \
          0.0011944957381629, \
          0.0011944957381629, \
          0.0011944957381629, \
          0.0031031422250087, \
          0.0031031422250087, \
          0.0031031422250087, \
          0.0031031422250087, \
          0.0031031422250087, \
          0.0031031422250087, \
          0.0051316606545523, \
          0.0051316606545523, \
          0.0051316606545523, \
          0.0051316606545523, \
          0.0051316606545523, \
          0.0051316606545523, \
          0.0048030743388154, \
          0.0048030743388154, \
          0.0048030743388154, \
          0.0048030743388154, \
          0.0048030743388154, \
          0.0048030743388154, \
          0.0048030743388154, \
          0.0048030743388154, \
          0.0048030743388154, \
          0.0048030743388154, \
          0.0048030743388154, \
          0.0048030743388154, \
          0.0008150376242850, \
          0.0008150376242850, \
          0.0008150376242850, \
          0.0008150376242850, \
          0.0008150376242850, \
          0.0008150376242850, \
          0.0008150376242850, \
          0.0008150376242850, \
          0.0008150376242850, \
          0.0008150376242850, \
          0.0008150376242850, \
          0.0008150376242850, \
          0.0044984898722334, \
          0.0044984898722334, \
          0.0044984898722334, \
          0.0044984898722334, \
          0.0044984898722334, \
          0.0044984898722334, \
          0.0044984898722334, \
          0.0044984898722334, \
          0.0044984898722334, \
          0.0044984898722334, \
          0.0044984898722334, \
          0.0044984898722334, \
          0.0027317773513874, \
          0.0027317773513874, \
          0.0027317773513874, \
          0.0027317773513874, \
          0.0027317773513874, \
          0.0027317773513874, \
          0.0027317773513874, \
          0.0027317773513874, \
          0.0027317773513874, \
          0.0027317773513874, \
          0.0027317773513874, \
          0.0027317773513874, \
          0.0039179954921652, \
          0.0039179954921652, \
          0.0039179954921652, \
          0.0039179954921652, \
          0.0039179954921652, \
          0.0039179954921652, \
          0.0039179954921652, \
          0.0039179954921652, \
          0.0039179954921652, \
          0.0039179954921652, \
          0.0039179954921652, \
          0.0039179954921652, \
          0.0008946420147168, \
          0.0008946420147168, \
          0.0008946420147168, \
          0.0008946420147168, \
          0.0008946420147168, \
          0.0008946420147168, \
          0.0008946420147168, \
          0.0008946420147168, \
          0.0008946420147168, \
          0.0008946420147168, \
          0.0008946420147168, \
          0.0008946420147168, \
          0.0012726195819812, \
          0.0012726195819812, \
          0.0012726195819812, \
          0.0012726195819812, \
          0.0012726195819812, \
          0.0012726195819812, \
          0.0012726195819812, \
          0.0012726195819812, \
          0.0012726195819812, \
          0.0012726195819812, \
          0.0012726195819812, \
          0.0012726195819812, \
          0.0045391175168163, \
          0.0045391175168163, \
          0.0045391175168163, \
          0.0045391175168163, \
          0.0045391175168163, \
          0.0045391175168163, \
          0.0045391175168163, \
          0.0045391175168163, \
          0.0045391175168163, \
          0.0045391175168163, \
          0.0045391175168163, \
          0.0045391175168163, \
          0.0012280771399416, \
          0.0012280771399416, \
          0.0012280771399416, \
          0.0012280771399416, \
          0.0012280771399416, \
          0.0012280771399416, \
          0.0012280771399416, \
          0.0012280771399416, \
          0.0012280771399416, \
          0.0012280771399416, \
          0.0012280771399416, \
          0.0012280771399416, \
          0.0024813526864083, \
          0.0024813526864083, \
          0.0024813526864083, \
          0.0024813526864083, \
          0.0024813526864083, \
          0.0024813526864083, \
          0.0024813526864083, \
          0.0024813526864083, \
          0.0024813526864083, \
          0.0024813526864083, \
          0.0024813526864083, \
          0.0024813526864083, \
          0.0006742435916066, \
          0.0006742435916066, \
          0.0006742435916066, \
          0.0006742435916066, \
          0.0006742435916066, \
          0.0006742435916066, \
          0.0006742435916066, \
          0.0006742435916066, \
          0.0006742435916066, \
          0.0006742435916066, \
          0.0006742435916066, \
          0.0006742435916066, \
          0.0030856887684142, \
          0.0030856887684142, \
          0.0030856887684142, \
          0.0030856887684142, \
          0.0030856887684142, \
          0.0030856887684142, \
          0.0030856887684142, \
          0.0030856887684142, \
          0.0030856887684142, \
          0.0030856887684142, \
          0.0030856887684142, \
          0.0030856887684142, \
          0.0028277448828289, \
          0.0028277448828289, \
          0.0028277448828289, \
          0.0028277448828289, \
          0.0028277448828289, \
          0.0028277448828289, \
          0.0028277448828289, \
          0.0028277448828289, \
          0.0028277448828289, \
          0.0028277448828289, \
          0.0028277448828289, \
          0.0028277448828289, \
          0.0007880156766982, \
          0.0007880156766982, \
          0.0007880156766982, \
          0.0007880156766982, \
          0.0007880156766982, \
          0.0007880156766982, \
          0.0007880156766982, \
          0.0007880156766982, \
          0.0007880156766982, \
          0.0007880156766982, \
          0.0007880156766982, \
          0.0007880156766982, \
          0.0009734356783438, \
          0.0009734356783438, \
          0.0009734356783438, \
          0.0009734356783438, \
          0.0009734356783438, \
          0.0009734356783438, \
          0.0009734356783438, \
          0.0009734356783438, \
          0.0009734356783438, \
          0.0009734356783438, \
          0.0009734356783438, \
          0.0009734356783438, \
          0.0002344473397349, \
          0.0002344473397349, \
          0.0002344473397349, \
          0.0002344473397349, \
          0.0002344473397349, \
          0.0002344473397349, \
          0.0002344473397349, \
          0.0002344473397349, \
          0.0002344473397349, \
          0.0002344473397349, \
          0.0002344473397349, \
          0.0002344473397349, \
          0.0027549281349627, \
          0.0027549281349627, \
          0.0027549281349627, \
          0.0027549281349627, \
          0.0027549281349627, \
          0.0027549281349627, \
          0.0027549281349627, \
          0.0027549281349627, \
          0.0027549281349627, \
          0.0027549281349627, \
          0.0027549281349627, \
          0.0027549281349627, \
          0.0008530955496580, \
          0.0008530955496580, \
          0.0008530955496580, \
          0.0008530955496580, \
          0.0008530955496580, \
          0.0008530955496580, \
          0.0008530955496580, \
          0.0008530955496580, \
          0.0008530955496580, \
          0.0008530955496580, \
          0.0008530955496580, \
          0.0008530955496580, \
          0.0017207910666049, \
          0.0017207910666049, \
          0.0017207910666049, \
          0.0017207910666049, \
          0.0017207910666049, \
          0.0017207910666049, \
          0.0017207910666049, \
          0.0017207910666049, \
          0.0017207910666049, \
          0.0017207910666049, \
          0.0017207910666049, \
          0.0017207910666049, \
          0.0052380601608220, \
          0.0052380601608220, \
          0.0052380601608220, \
          0.0052380601608220, \
          0.0052380601608220, \
          0.0052380601608220, \
          0.0052380601608220, \
          0.0052380601608220, \
          0.0052380601608220, \
          0.0052380601608220, \
          0.0052380601608220, \
          0.0052380601608220, \
          0.0007780035531901, \
          0.0007780035531901, \
          0.0007780035531901, \
          0.0007780035531901, \
          0.0007780035531901, \
          0.0007780035531901, \
          0.0007780035531901, \
          0.0007780035531901, \
          0.0007780035531901, \
          0.0007780035531901, \
          0.0007780035531901, \
          0.0007780035531901, \
          0.0027997199341340, \
          0.0027997199341340, \
          0.0027997199341340, \
          0.0027997199341340, \
          0.0027997199341340, \
          0.0027997199341340, \
          0.0027997199341340, \
          0.0027997199341340, \
          0.0027997199341340, \
          0.0027997199341340, \
          0.0027997199341340, \
          0.0027997199341340, \
          0.0018871269258399, \
          0.0018871269258399, \
          0.0018871269258399, \
          0.0018871269258399, \
          0.0018871269258399, \
          0.0018871269258399, \
          0.0018871269258399, \
          0.0018871269258399, \
          0.0018871269258399, \
          0.0018871269258399, \
          0.0018871269258399, \
          0.0018871269258399 ] )

  return x, y, z, w

def rule20 ( ):

#*****************************************************************************80
#
## rule20() returns the prism rule of precision 20.
#
#  Discussion:
#
#    We suppose we are given a triangular prism P with vertices
#    (1,0,0), (0,1,0), (0,0,0),
#    (1,0,1), (0,1,1), (0,0,1),
#    We call a rule with n points, returning coordinates
#    x, y, z, and weights w.  Then the integral I of f(x,y,z) over P is 
#    approximated by Q as follows:
#
#    Q = volume(P) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i),z(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 May 2023
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
#  Output:
#
#    real x(n), y(n), z(n): the coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  x = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.0144110873698983, \
          0.0144110873698983, \
          0.9711778252602034, \
          0.0594974134225245, \
          0.0594974134225245, \
          0.8810051731549510, \
          0.4716249531173324, \
          0.4716249531173324, \
          0.0567500937653351, \
          0.4716249531173324, \
          0.4716249531173324, \
          0.0567500937653351, \
          0.4084460043805324, \
          0.4084460043805324, \
          0.1831079912389352, \
          0.4084460043805324, \
          0.4084460043805324, \
          0.1831079912389352, \
          0.2544280410411358, \
          0.2544280410411358, \
          0.4911439179177284, \
          0.2544280410411358, \
          0.2544280410411358, \
          0.4911439179177284, \
          0.4774877095488475, \
          0.4774877095488475, \
          0.0450245809023050, \
          0.4774877095488475, \
          0.4774877095488475, \
          0.0450245809023050, \
          0.0080292636682187, \
          0.0080292636682187, \
          0.9839414726635627, \
          0.0080292636682187, \
          0.0080292636682187, \
          0.9839414726635627, \
          0.4968613511179721, \
          0.4968613511179721, \
          0.0062772977640557, \
          0.4968613511179721, \
          0.4968613511179721, \
          0.0062772977640557, \
          0.4952615769053836, \
          0.4952615769053836, \
          0.0094768461892327, \
          0.4952615769053836, \
          0.4952615769053836, \
          0.0094768461892327, \
          0.0353578097171312, \
          0.0353578097171312, \
          0.9292843805657376, \
          0.0353578097171312, \
          0.0353578097171312, \
          0.9292843805657376, \
          0.2045970282680664, \
          0.2045970282680664, \
          0.5908059434638671, \
          0.2045970282680664, \
          0.2045970282680664, \
          0.5908059434638671, \
          0.1406131665045265, \
          0.1406131665045265, \
          0.7187736669909469, \
          0.1406131665045265, \
          0.1406131665045265, \
          0.7187736669909469, \
          0.0982561053377771, \
          0.0982561053377771, \
          0.8034877893244458, \
          0.0982561053377771, \
          0.0982561053377771, \
          0.8034877893244458, \
          0.0505951664588140, \
          0.0505951664588140, \
          0.8988096670823720, \
          0.0505951664588140, \
          0.0505951664588140, \
          0.8988096670823720, \
          0.4494558038329708, \
          0.4494558038329708, \
          0.1010883923340583, \
          0.4494558038329708, \
          0.4494558038329708, \
          0.1010883923340583, \
          0.2188296334498393, \
          0.2188296334498393, \
          0.5623407331003214, \
          0.2188296334498393, \
          0.2188296334498393, \
          0.5623407331003214, \
          0.3839280551265914, \
          0.3839280551265914, \
          0.2321438897468171, \
          0.3839280551265914, \
          0.3839280551265914, \
          0.2321438897468171, \
          0.0599706591707595, \
          0.0599706591707595, \
          0.8800586816584810, \
          0.0599706591707595, \
          0.0599706591707595, \
          0.8800586816584810, \
          0.2735494152095392, \
          0.2735494152095392, \
          0.4529011695809215, \
          0.2735494152095392, \
          0.2735494152095392, \
          0.4529011695809215, \
          0.4907393281824849, \
          0.4907393281824849, \
          0.0185213436350301, \
          0.4907393281824849, \
          0.4907393281824849, \
          0.0185213436350301, \
          0.0114930108302544, \
          0.0114930108302544, \
          0.9770139783394911, \
          0.0114930108302544, \
          0.0114930108302544, \
          0.9770139783394911, \
          0.4048678509173179, \
          0.4048678509173179, \
          0.1902642981653643, \
          0.4048678509173179, \
          0.4048678509173179, \
          0.1902642981653643, \
          0.2917111538437177, \
          0.2917111538437177, \
          0.4165776923125646, \
          0.2917111538437177, \
          0.2917111538437177, \
          0.4165776923125646, \
          0.4459340787080981, \
          0.4459340787080981, \
          0.1081318425838039, \
          0.4459340787080981, \
          0.4459340787080981, \
          0.1081318425838039, \
          0.2107382124681030, \
          0.0313712403793080, \
          0.2107382124681030, \
          0.7578905471525890, \
          0.0313712403793080, \
          0.7578905471525890, \
          0.2031438036613264, \
          0.1114400380412596, \
          0.2031438036613264, \
          0.6854161582974140, \
          0.1114400380412596, \
          0.6854161582974140, \
          0.3734168270486775, \
          0.0362901207122587, \
          0.3734168270486775, \
          0.5902930522390638, \
          0.0362901207122587, \
          0.5902930522390638, \
          0.5331515253263366, \
          0.1335223252058013, \
          0.5331515253263366, \
          0.3333261494678621, \
          0.1335223252058013, \
          0.3333261494678621, \
          0.5331515253263366, \
          0.1335223252058013, \
          0.5331515253263366, \
          0.3333261494678621, \
          0.1335223252058013, \
          0.3333261494678621, \
          0.0031052202964266, \
          0.0650661770452139, \
          0.0031052202964266, \
          0.9318286026583595, \
          0.0650661770452139, \
          0.9318286026583595, \
          0.0031052202964266, \
          0.0650661770452139, \
          0.0031052202964266, \
          0.9318286026583595, \
          0.0650661770452139, \
          0.9318286026583595, \
          0.7387825606686489, \
          0.0932063677657537, \
          0.7387825606686489, \
          0.1680110715655975, \
          0.0932063677657537, \
          0.1680110715655975, \
          0.7387825606686489, \
          0.0932063677657537, \
          0.7387825606686489, \
          0.1680110715655975, \
          0.0932063677657537, \
          0.1680110715655975, \
          0.2402209181076414, \
          0.0342816904321169, \
          0.2402209181076414, \
          0.7254973914602417, \
          0.0342816904321169, \
          0.7254973914602417, \
          0.2402209181076414, \
          0.0342816904321169, \
          0.2402209181076414, \
          0.7254973914602417, \
          0.0342816904321169, \
          0.7254973914602417, \
          0.0816129838618181, \
          0.3087274419444517, \
          0.0816129838618181, \
          0.6096595741937303, \
          0.3087274419444517, \
          0.6096595741937303, \
          0.0816129838618181, \
          0.3087274419444517, \
          0.0816129838618181, \
          0.6096595741937303, \
          0.3087274419444517, \
          0.6096595741937303, \
          0.1728159430622389, \
          0.3228866908185781, \
          0.1728159430622389, \
          0.5042973661191831, \
          0.3228866908185781, \
          0.5042973661191831, \
          0.1728159430622389, \
          0.3228866908185781, \
          0.1728159430622389, \
          0.5042973661191831, \
          0.3228866908185781, \
          0.5042973661191831, \
          0.2247127800382396, \
          0.1327427633967232, \
          0.2247127800382396, \
          0.6425444565650372, \
          0.1327427633967232, \
          0.6425444565650372, \
          0.2247127800382396, \
          0.1327427633967232, \
          0.2247127800382396, \
          0.6425444565650372, \
          0.1327427633967232, \
          0.6425444565650372, \
          0.0285010351208627, \
          0.1058138309132070, \
          0.0285010351208627, \
          0.8656851339659303, \
          0.1058138309132070, \
          0.8656851339659303, \
          0.0285010351208627, \
          0.1058138309132070, \
          0.0285010351208627, \
          0.8656851339659303, \
          0.1058138309132070, \
          0.8656851339659303, \
          0.3896100790636586, \
          0.0109712296494740, \
          0.3896100790636586, \
          0.5994186912868675, \
          0.0109712296494740, \
          0.5994186912868675, \
          0.3896100790636586, \
          0.0109712296494740, \
          0.3896100790636586, \
          0.5994186912868675, \
          0.0109712296494740, \
          0.5994186912868675, \
          0.2493335646225524, \
          0.3397868885786173, \
          0.2493335646225524, \
          0.4108795467988303, \
          0.3397868885786173, \
          0.4108795467988303, \
          0.2493335646225524, \
          0.3397868885786173, \
          0.2493335646225524, \
          0.4108795467988303, \
          0.3397868885786173, \
          0.4108795467988303, \
          0.0070420236000393, \
          0.3177207979690921, \
          0.0070420236000393, \
          0.6752371784308686, \
          0.3177207979690921, \
          0.6752371784308686, \
          0.0070420236000393, \
          0.3177207979690921, \
          0.0070420236000393, \
          0.6752371784308686, \
          0.3177207979690921, \
          0.6752371784308686, \
          0.1229469656661441, \
          0.0156675786078851, \
          0.1229469656661441, \
          0.8613854557259707, \
          0.0156675786078851, \
          0.8613854557259707, \
          0.1229469656661441, \
          0.0156675786078851, \
          0.1229469656661441, \
          0.8613854557259707, \
          0.0156675786078851, \
          0.8613854557259707, \
          0.2259160262165568, \
          0.0521518846441873, \
          0.2259160262165568, \
          0.7219320891392559, \
          0.0521518846441873, \
          0.7219320891392559, \
          0.2259160262165568, \
          0.0521518846441873, \
          0.2259160262165568, \
          0.7219320891392559, \
          0.0521518846441873, \
          0.7219320891392559, \
          0.0094714933266370, \
          0.0496441415264223, \
          0.0094714933266370, \
          0.9408843651469406, \
          0.0496441415264223, \
          0.9408843651469406, \
          0.0094714933266370, \
          0.0496441415264223, \
          0.0094714933266370, \
          0.9408843651469406, \
          0.0496441415264223, \
          0.9408843651469406, \
          0.0524311424127234, \
          0.1452721772236918, \
          0.0524311424127234, \
          0.8022966803635848, \
          0.1452721772236918, \
          0.8022966803635848, \
          0.0524311424127234, \
          0.1452721772236918, \
          0.0524311424127234, \
          0.8022966803635848, \
          0.1452721772236918, \
          0.8022966803635848, \
          0.0088722025555106, \
          0.3816302433543118, \
          0.0088722025555106, \
          0.6094975540901776, \
          0.3816302433543118, \
          0.6094975540901776, \
          0.0088722025555106, \
          0.3816302433543118, \
          0.0088722025555106, \
          0.6094975540901776, \
          0.3816302433543118, \
          0.6094975540901776, \
          0.2592518129005248, \
          0.5551397100853696, \
          0.2592518129005248, \
          0.1856084770141057, \
          0.5551397100853696, \
          0.1856084770141057, \
          0.2592518129005248, \
          0.5551397100853696, \
          0.2592518129005248, \
          0.1856084770141057, \
          0.5551397100853696, \
          0.1856084770141057, \
          0.3527097683072426, \
          0.0454609714340920, \
          0.3527097683072426, \
          0.6018292602586655, \
          0.0454609714340920, \
          0.6018292602586655, \
          0.3527097683072426, \
          0.0454609714340920, \
          0.3527097683072426, \
          0.6018292602586655, \
          0.0454609714340920, \
          0.6018292602586655, \
          0.1450709676542589, \
          0.0118170254385161, \
          0.1450709676542589, \
          0.8431120069072251, \
          0.0118170254385161, \
          0.8431120069072251, \
          0.1450709676542589, \
          0.0118170254385161, \
          0.1450709676542589, \
          0.8431120069072251, \
          0.0118170254385161, \
          0.8431120069072251, \
          0.1874143309040665, \
          0.1371981166173774, \
          0.1874143309040665, \
          0.6753875524785560, \
          0.1371981166173774, \
          0.6753875524785560, \
          0.1874143309040665, \
          0.1371981166173774, \
          0.1874143309040665, \
          0.6753875524785560, \
          0.1371981166173774, \
          0.6753875524785560, \
          0.0681401608659605, \
          0.1498311852045099, \
          0.0681401608659605, \
          0.7820286539295297, \
          0.1498311852045099, \
          0.7820286539295297, \
          0.0681401608659605, \
          0.1498311852045099, \
          0.0681401608659605, \
          0.7820286539295297, \
          0.1498311852045099, \
          0.7820286539295297, \
          0.3340585216441213, \
          0.0549696286134690, \
          0.3340585216441213, \
          0.6109718497424097, \
          0.0549696286134690, \
          0.6109718497424097, \
          0.3340585216441213, \
          0.0549696286134690, \
          0.3340585216441213, \
          0.6109718497424097, \
          0.0549696286134690, \
          0.6109718497424097, \
          0.0678515797670052, \
          0.1205147270278029, \
          0.0678515797670052, \
          0.8116336932051920, \
          0.1205147270278029, \
          0.8116336932051920, \
          0.0678515797670052, \
          0.1205147270278029, \
          0.0678515797670052, \
          0.8116336932051920, \
          0.1205147270278029, \
          0.8116336932051920, \
          0.5023136055537912, \
          0.1076311573233394, \
          0.5023136055537912, \
          0.3900552371228693, \
          0.1076311573233394, \
          0.3900552371228693, \
          0.5023136055537912, \
          0.1076311573233394, \
          0.5023136055537912, \
          0.3900552371228693, \
          0.1076311573233394, \
          0.3900552371228693, \
          0.0078193997434242, \
          0.2556542053755758, \
          0.0078193997434242, \
          0.7365263948810000, \
          0.2556542053755758, \
          0.7365263948810000, \
          0.0078193997434242, \
          0.2556542053755758, \
          0.0078193997434242, \
          0.7365263948810000, \
          0.2556542053755758, \
          0.7365263948810000, \
          0.6609230621965876, \
          0.0983956958507364, \
          0.6609230621965876, \
          0.2406812419526760, \
          0.0983956958507364, \
          0.2406812419526760, \
          0.6609230621965876, \
          0.0983956958507364, \
          0.6609230621965876, \
          0.2406812419526760, \
          0.0983956958507364, \
          0.2406812419526760, \
          0.1784736485903538, \
          0.0017965399943124, \
          0.1784736485903538, \
          0.8197298114153339, \
          0.0017965399943124, \
          0.8197298114153339, \
          0.1784736485903538, \
          0.0017965399943124, \
          0.1784736485903538, \
          0.8197298114153339, \
          0.0017965399943124, \
          0.8197298114153339, \
          0.2532227359651285, \
          0.0131217590858908, \
          0.2532227359651285, \
          0.7336555049489807, \
          0.0131217590858908, \
          0.7336555049489807, \
          0.2532227359651285, \
          0.0131217590858908, \
          0.2532227359651285, \
          0.7336555049489807, \
          0.0131217590858908, \
          0.7336555049489807, \
          0.0144350536713311, \
          0.0686738759058901, \
          0.0144350536713311, \
          0.9168910704227788, \
          0.0686738759058901, \
          0.9168910704227788, \
          0.0144350536713311, \
          0.0686738759058901, \
          0.0144350536713311, \
          0.9168910704227788, \
          0.0686738759058901, \
          0.9168910704227788, \
          0.2794904874495157, \
          0.1274003485132245, \
          0.2794904874495157, \
          0.5931091640372598, \
          0.1274003485132245, \
          0.5931091640372598, \
          0.2794904874495157, \
          0.1274003485132245, \
          0.2794904874495157, \
          0.5931091640372598, \
          0.1274003485132245, \
          0.5931091640372598 ] )

  y = np.array ( [ \
          0.3333333333333333, \
          0.3333333333333333, \
          0.0144110873698983, \
          0.9711778252602034, \
          0.0144110873698983, \
          0.0594974134225245, \
          0.8810051731549510, \
          0.0594974134225245, \
          0.4716249531173324, \
          0.0567500937653351, \
          0.4716249531173324, \
          0.4716249531173324, \
          0.0567500937653351, \
          0.4716249531173324, \
          0.4084460043805324, \
          0.1831079912389352, \
          0.4084460043805324, \
          0.4084460043805324, \
          0.1831079912389352, \
          0.4084460043805324, \
          0.2544280410411358, \
          0.4911439179177284, \
          0.2544280410411358, \
          0.2544280410411358, \
          0.4911439179177284, \
          0.2544280410411358, \
          0.4774877095488475, \
          0.0450245809023050, \
          0.4774877095488475, \
          0.4774877095488475, \
          0.0450245809023050, \
          0.4774877095488475, \
          0.0080292636682187, \
          0.9839414726635627, \
          0.0080292636682187, \
          0.0080292636682187, \
          0.9839414726635627, \
          0.0080292636682187, \
          0.4968613511179721, \
          0.0062772977640557, \
          0.4968613511179721, \
          0.4968613511179721, \
          0.0062772977640557, \
          0.4968613511179721, \
          0.4952615769053836, \
          0.0094768461892327, \
          0.4952615769053836, \
          0.4952615769053836, \
          0.0094768461892327, \
          0.4952615769053836, \
          0.0353578097171312, \
          0.9292843805657376, \
          0.0353578097171312, \
          0.0353578097171312, \
          0.9292843805657376, \
          0.0353578097171312, \
          0.2045970282680664, \
          0.5908059434638671, \
          0.2045970282680664, \
          0.2045970282680664, \
          0.5908059434638671, \
          0.2045970282680664, \
          0.1406131665045265, \
          0.7187736669909469, \
          0.1406131665045265, \
          0.1406131665045265, \
          0.7187736669909469, \
          0.1406131665045265, \
          0.0982561053377771, \
          0.8034877893244458, \
          0.0982561053377771, \
          0.0982561053377771, \
          0.8034877893244458, \
          0.0982561053377771, \
          0.0505951664588140, \
          0.8988096670823720, \
          0.0505951664588140, \
          0.0505951664588140, \
          0.8988096670823720, \
          0.0505951664588140, \
          0.4494558038329708, \
          0.1010883923340583, \
          0.4494558038329708, \
          0.4494558038329708, \
          0.1010883923340583, \
          0.4494558038329708, \
          0.2188296334498393, \
          0.5623407331003214, \
          0.2188296334498393, \
          0.2188296334498393, \
          0.5623407331003214, \
          0.2188296334498393, \
          0.3839280551265914, \
          0.2321438897468171, \
          0.3839280551265914, \
          0.3839280551265914, \
          0.2321438897468171, \
          0.3839280551265914, \
          0.0599706591707595, \
          0.8800586816584810, \
          0.0599706591707595, \
          0.0599706591707595, \
          0.8800586816584810, \
          0.0599706591707595, \
          0.2735494152095392, \
          0.4529011695809215, \
          0.2735494152095392, \
          0.2735494152095392, \
          0.4529011695809215, \
          0.2735494152095392, \
          0.4907393281824849, \
          0.0185213436350301, \
          0.4907393281824849, \
          0.4907393281824849, \
          0.0185213436350301, \
          0.4907393281824849, \
          0.0114930108302544, \
          0.9770139783394911, \
          0.0114930108302544, \
          0.0114930108302544, \
          0.9770139783394911, \
          0.0114930108302544, \
          0.4048678509173179, \
          0.1902642981653643, \
          0.4048678509173179, \
          0.4048678509173179, \
          0.1902642981653643, \
          0.4048678509173179, \
          0.2917111538437177, \
          0.4165776923125646, \
          0.2917111538437177, \
          0.2917111538437177, \
          0.4165776923125646, \
          0.2917111538437177, \
          0.4459340787080981, \
          0.1081318425838039, \
          0.4459340787080981, \
          0.4459340787080981, \
          0.1081318425838039, \
          0.4459340787080981, \
          0.0313712403793080, \
          0.2107382124681030, \
          0.7578905471525890, \
          0.2107382124681030, \
          0.7578905471525890, \
          0.0313712403793080, \
          0.1114400380412596, \
          0.2031438036613264, \
          0.6854161582974140, \
          0.2031438036613264, \
          0.6854161582974140, \
          0.1114400380412596, \
          0.0362901207122587, \
          0.3734168270486775, \
          0.5902930522390638, \
          0.3734168270486775, \
          0.5902930522390638, \
          0.0362901207122587, \
          0.1335223252058013, \
          0.5331515253263366, \
          0.3333261494678621, \
          0.5331515253263366, \
          0.3333261494678621, \
          0.1335223252058013, \
          0.1335223252058013, \
          0.5331515253263366, \
          0.3333261494678621, \
          0.5331515253263366, \
          0.3333261494678621, \
          0.1335223252058013, \
          0.0650661770452139, \
          0.0031052202964266, \
          0.9318286026583595, \
          0.0031052202964266, \
          0.9318286026583595, \
          0.0650661770452139, \
          0.0650661770452139, \
          0.0031052202964266, \
          0.9318286026583595, \
          0.0031052202964266, \
          0.9318286026583595, \
          0.0650661770452139, \
          0.0932063677657537, \
          0.7387825606686489, \
          0.1680110715655975, \
          0.7387825606686489, \
          0.1680110715655975, \
          0.0932063677657537, \
          0.0932063677657537, \
          0.7387825606686489, \
          0.1680110715655975, \
          0.7387825606686489, \
          0.1680110715655975, \
          0.0932063677657537, \
          0.0342816904321169, \
          0.2402209181076414, \
          0.7254973914602417, \
          0.2402209181076414, \
          0.7254973914602417, \
          0.0342816904321169, \
          0.0342816904321169, \
          0.2402209181076414, \
          0.7254973914602417, \
          0.2402209181076414, \
          0.7254973914602417, \
          0.0342816904321169, \
          0.3087274419444517, \
          0.0816129838618181, \
          0.6096595741937303, \
          0.0816129838618181, \
          0.6096595741937303, \
          0.3087274419444517, \
          0.3087274419444517, \
          0.0816129838618181, \
          0.6096595741937303, \
          0.0816129838618181, \
          0.6096595741937303, \
          0.3087274419444517, \
          0.3228866908185781, \
          0.1728159430622389, \
          0.5042973661191831, \
          0.1728159430622389, \
          0.5042973661191831, \
          0.3228866908185781, \
          0.3228866908185781, \
          0.1728159430622389, \
          0.5042973661191831, \
          0.1728159430622389, \
          0.5042973661191831, \
          0.3228866908185781, \
          0.1327427633967232, \
          0.2247127800382396, \
          0.6425444565650372, \
          0.2247127800382396, \
          0.6425444565650372, \
          0.1327427633967232, \
          0.1327427633967232, \
          0.2247127800382396, \
          0.6425444565650372, \
          0.2247127800382396, \
          0.6425444565650372, \
          0.1327427633967232, \
          0.1058138309132070, \
          0.0285010351208627, \
          0.8656851339659303, \
          0.0285010351208627, \
          0.8656851339659303, \
          0.1058138309132070, \
          0.1058138309132070, \
          0.0285010351208627, \
          0.8656851339659303, \
          0.0285010351208627, \
          0.8656851339659303, \
          0.1058138309132070, \
          0.0109712296494740, \
          0.3896100790636586, \
          0.5994186912868675, \
          0.3896100790636586, \
          0.5994186912868675, \
          0.0109712296494740, \
          0.0109712296494740, \
          0.3896100790636586, \
          0.5994186912868675, \
          0.3896100790636586, \
          0.5994186912868675, \
          0.0109712296494740, \
          0.3397868885786173, \
          0.2493335646225524, \
          0.4108795467988303, \
          0.2493335646225524, \
          0.4108795467988303, \
          0.3397868885786173, \
          0.3397868885786173, \
          0.2493335646225524, \
          0.4108795467988303, \
          0.2493335646225524, \
          0.4108795467988303, \
          0.3397868885786173, \
          0.3177207979690921, \
          0.0070420236000393, \
          0.6752371784308686, \
          0.0070420236000393, \
          0.6752371784308686, \
          0.3177207979690921, \
          0.3177207979690921, \
          0.0070420236000393, \
          0.6752371784308686, \
          0.0070420236000393, \
          0.6752371784308686, \
          0.3177207979690921, \
          0.0156675786078851, \
          0.1229469656661441, \
          0.8613854557259707, \
          0.1229469656661441, \
          0.8613854557259707, \
          0.0156675786078851, \
          0.0156675786078851, \
          0.1229469656661441, \
          0.8613854557259707, \
          0.1229469656661441, \
          0.8613854557259707, \
          0.0156675786078851, \
          0.0521518846441873, \
          0.2259160262165568, \
          0.7219320891392559, \
          0.2259160262165568, \
          0.7219320891392559, \
          0.0521518846441873, \
          0.0521518846441873, \
          0.2259160262165568, \
          0.7219320891392559, \
          0.2259160262165568, \
          0.7219320891392559, \
          0.0521518846441873, \
          0.0496441415264223, \
          0.0094714933266370, \
          0.9408843651469406, \
          0.0094714933266370, \
          0.9408843651469406, \
          0.0496441415264223, \
          0.0496441415264223, \
          0.0094714933266370, \
          0.9408843651469406, \
          0.0094714933266370, \
          0.9408843651469406, \
          0.0496441415264223, \
          0.1452721772236918, \
          0.0524311424127234, \
          0.8022966803635848, \
          0.0524311424127234, \
          0.8022966803635848, \
          0.1452721772236918, \
          0.1452721772236918, \
          0.0524311424127234, \
          0.8022966803635848, \
          0.0524311424127234, \
          0.8022966803635848, \
          0.1452721772236918, \
          0.3816302433543118, \
          0.0088722025555106, \
          0.6094975540901776, \
          0.0088722025555106, \
          0.6094975540901776, \
          0.3816302433543118, \
          0.3816302433543118, \
          0.0088722025555106, \
          0.6094975540901776, \
          0.0088722025555106, \
          0.6094975540901776, \
          0.3816302433543118, \
          0.5551397100853696, \
          0.2592518129005248, \
          0.1856084770141057, \
          0.2592518129005248, \
          0.1856084770141057, \
          0.5551397100853696, \
          0.5551397100853696, \
          0.2592518129005248, \
          0.1856084770141057, \
          0.2592518129005248, \
          0.1856084770141057, \
          0.5551397100853696, \
          0.0454609714340920, \
          0.3527097683072426, \
          0.6018292602586655, \
          0.3527097683072426, \
          0.6018292602586655, \
          0.0454609714340920, \
          0.0454609714340920, \
          0.3527097683072426, \
          0.6018292602586655, \
          0.3527097683072426, \
          0.6018292602586655, \
          0.0454609714340920, \
          0.0118170254385161, \
          0.1450709676542589, \
          0.8431120069072251, \
          0.1450709676542589, \
          0.8431120069072251, \
          0.0118170254385161, \
          0.0118170254385161, \
          0.1450709676542589, \
          0.8431120069072251, \
          0.1450709676542589, \
          0.8431120069072251, \
          0.0118170254385161, \
          0.1371981166173774, \
          0.1874143309040665, \
          0.6753875524785560, \
          0.1874143309040665, \
          0.6753875524785560, \
          0.1371981166173774, \
          0.1371981166173774, \
          0.1874143309040665, \
          0.6753875524785560, \
          0.1874143309040665, \
          0.6753875524785560, \
          0.1371981166173774, \
          0.1498311852045099, \
          0.0681401608659605, \
          0.7820286539295297, \
          0.0681401608659605, \
          0.7820286539295297, \
          0.1498311852045099, \
          0.1498311852045099, \
          0.0681401608659605, \
          0.7820286539295297, \
          0.0681401608659605, \
          0.7820286539295297, \
          0.1498311852045099, \
          0.0549696286134690, \
          0.3340585216441213, \
          0.6109718497424097, \
          0.3340585216441213, \
          0.6109718497424097, \
          0.0549696286134690, \
          0.0549696286134690, \
          0.3340585216441213, \
          0.6109718497424097, \
          0.3340585216441213, \
          0.6109718497424097, \
          0.0549696286134690, \
          0.1205147270278029, \
          0.0678515797670052, \
          0.8116336932051920, \
          0.0678515797670052, \
          0.8116336932051920, \
          0.1205147270278029, \
          0.1205147270278029, \
          0.0678515797670052, \
          0.8116336932051920, \
          0.0678515797670052, \
          0.8116336932051920, \
          0.1205147270278029, \
          0.1076311573233394, \
          0.5023136055537912, \
          0.3900552371228693, \
          0.5023136055537912, \
          0.3900552371228693, \
          0.1076311573233394, \
          0.1076311573233394, \
          0.5023136055537912, \
          0.3900552371228693, \
          0.5023136055537912, \
          0.3900552371228693, \
          0.1076311573233394, \
          0.2556542053755758, \
          0.0078193997434242, \
          0.7365263948810000, \
          0.0078193997434242, \
          0.7365263948810000, \
          0.2556542053755758, \
          0.2556542053755758, \
          0.0078193997434242, \
          0.7365263948810000, \
          0.0078193997434242, \
          0.7365263948810000, \
          0.2556542053755758, \
          0.0983956958507364, \
          0.6609230621965876, \
          0.2406812419526760, \
          0.6609230621965876, \
          0.2406812419526760, \
          0.0983956958507364, \
          0.0983956958507364, \
          0.6609230621965876, \
          0.2406812419526760, \
          0.6609230621965876, \
          0.2406812419526760, \
          0.0983956958507364, \
          0.0017965399943124, \
          0.1784736485903538, \
          0.8197298114153339, \
          0.1784736485903538, \
          0.8197298114153339, \
          0.0017965399943124, \
          0.0017965399943124, \
          0.1784736485903538, \
          0.8197298114153339, \
          0.1784736485903538, \
          0.8197298114153339, \
          0.0017965399943124, \
          0.0131217590858908, \
          0.2532227359651285, \
          0.7336555049489807, \
          0.2532227359651285, \
          0.7336555049489807, \
          0.0131217590858908, \
          0.0131217590858908, \
          0.2532227359651285, \
          0.7336555049489807, \
          0.2532227359651285, \
          0.7336555049489807, \
          0.0131217590858908, \
          0.0686738759058901, \
          0.0144350536713311, \
          0.9168910704227788, \
          0.0144350536713311, \
          0.9168910704227788, \
          0.0686738759058901, \
          0.0686738759058901, \
          0.0144350536713311, \
          0.9168910704227788, \
          0.0144350536713311, \
          0.9168910704227788, \
          0.0686738759058901, \
          0.1274003485132245, \
          0.2794904874495157, \
          0.5931091640372598, \
          0.2794904874495157, \
          0.5931091640372598, \
          0.1274003485132245, \
          0.1274003485132245, \
          0.2794904874495157, \
          0.5931091640372598, \
          0.2794904874495157, \
          0.5931091640372598, \
          0.1274003485132245 ] )

  z = np.array ( [ \
          0.9210083004731364, \
          0.0789916995268636, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.9076441430436997, \
          0.9076441430436997, \
          0.9076441430436997, \
          0.0923558569563003, \
          0.0923558569563003, \
          0.0923558569563003, \
          0.7654479960865263, \
          0.7654479960865263, \
          0.7654479960865263, \
          0.2345520039134737, \
          0.2345520039134737, \
          0.2345520039134737, \
          0.8572582404180138, \
          0.8572582404180138, \
          0.8572582404180138, \
          0.1427417595819861, \
          0.1427417595819861, \
          0.1427417595819861, \
          0.6651011543921541, \
          0.6651011543921541, \
          0.6651011543921541, \
          0.3348988456078459, \
          0.3348988456078459, \
          0.3348988456078459, \
          0.7626983072263107, \
          0.7626983072263107, \
          0.7626983072263107, \
          0.2373016927736893, \
          0.2373016927736893, \
          0.2373016927736893, \
          0.5839411665251317, \
          0.5839411665251317, \
          0.5839411665251317, \
          0.4160588334748682, \
          0.4160588334748682, \
          0.4160588334748682, \
          0.8529900626158916, \
          0.8529900626158916, \
          0.8529900626158916, \
          0.1470099373841084, \
          0.1470099373841084, \
          0.1470099373841084, \
          0.6690062435950173, \
          0.6690062435950173, \
          0.6690062435950173, \
          0.3309937564049827, \
          0.3309937564049827, \
          0.3309937564049827, \
          0.4508779258616127, \
          0.4508779258616127, \
          0.4508779258616127, \
          0.5491220741383873, \
          0.5491220741383873, \
          0.5491220741383873, \
          0.8420489345379816, \
          0.8420489345379816, \
          0.8420489345379816, \
          0.1579510654620185, \
          0.1579510654620185, \
          0.1579510654620185, \
          0.3603208005838872, \
          0.3603208005838872, \
          0.3603208005838872, \
          0.6396791994161128, \
          0.6396791994161128, \
          0.6396791994161128, \
          0.7720261679832757, \
          0.7720261679832757, \
          0.7720261679832757, \
          0.2279738320167243, \
          0.2279738320167243, \
          0.2279738320167243, \
          0.9830894614249917, \
          0.9830894614249917, \
          0.9830894614249917, \
          0.0169105385750084, \
          0.0169105385750084, \
          0.0169105385750084, \
          0.7580515195220092, \
          0.7580515195220092, \
          0.7580515195220092, \
          0.2419484804779908, \
          0.2419484804779908, \
          0.2419484804779908, \
          0.8207076808620348, \
          0.8207076808620348, \
          0.8207076808620348, \
          0.1792923191379651, \
          0.1792923191379651, \
          0.1792923191379651, \
          0.9471959220764619, \
          0.9471959220764619, \
          0.9471959220764619, \
          0.0528040779235381, \
          0.0528040779235381, \
          0.0528040779235381, \
          0.9896592480532946, \
          0.9896592480532946, \
          0.9896592480532946, \
          0.0103407519467054, \
          0.0103407519467054, \
          0.0103407519467054, \
          0.9943125669152897, \
          0.9943125669152897, \
          0.9943125669152897, \
          0.0056874330847103, \
          0.0056874330847103, \
          0.0056874330847103, \
          0.9633861983838395, \
          0.9633861983838395, \
          0.9633861983838395, \
          0.0366138016161605, \
          0.0366138016161605, \
          0.0366138016161605, \
          0.9582038855682118, \
          0.9582038855682118, \
          0.9582038855682118, \
          0.0417961144317883, \
          0.0417961144317883, \
          0.0417961144317883, \
          0.3139113946603033, \
          0.3139113946603033, \
          0.3139113946603033, \
          0.6860886053396967, \
          0.6860886053396967, \
          0.6860886053396967, \
          0.5189148057278750, \
          0.5189148057278750, \
          0.5189148057278750, \
          0.4810851942721250, \
          0.4810851942721250, \
          0.4810851942721250, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.8901251913253538, \
          0.8901251913253538, \
          0.8901251913253538, \
          0.8901251913253538, \
          0.8901251913253538, \
          0.8901251913253538, \
          0.1098748086746462, \
          0.1098748086746462, \
          0.1098748086746462, \
          0.1098748086746462, \
          0.1098748086746462, \
          0.1098748086746462, \
          0.3557614873681827, \
          0.3557614873681827, \
          0.3557614873681827, \
          0.3557614873681827, \
          0.3557614873681827, \
          0.3557614873681827, \
          0.6442385126318173, \
          0.6442385126318173, \
          0.6442385126318173, \
          0.6442385126318173, \
          0.6442385126318173, \
          0.6442385126318173, \
          0.3778572463523129, \
          0.3778572463523129, \
          0.3778572463523129, \
          0.3778572463523129, \
          0.3778572463523129, \
          0.3778572463523129, \
          0.6221427536476871, \
          0.6221427536476871, \
          0.6221427536476871, \
          0.6221427536476871, \
          0.6221427536476871, \
          0.6221427536476871, \
          0.7130345491338336, \
          0.7130345491338336, \
          0.7130345491338336, \
          0.7130345491338336, \
          0.7130345491338336, \
          0.7130345491338336, \
          0.2869654508661664, \
          0.2869654508661664, \
          0.2869654508661664, \
          0.2869654508661664, \
          0.2869654508661664, \
          0.2869654508661664, \
          0.6210154934017852, \
          0.6210154934017852, \
          0.6210154934017852, \
          0.6210154934017852, \
          0.6210154934017852, \
          0.6210154934017852, \
          0.3789845065982148, \
          0.3789845065982148, \
          0.3789845065982148, \
          0.3789845065982148, \
          0.3789845065982148, \
          0.3789845065982148, \
          0.3811077243266478, \
          0.3811077243266478, \
          0.3811077243266478, \
          0.3811077243266478, \
          0.3811077243266478, \
          0.3811077243266478, \
          0.6188922756733521, \
          0.6188922756733521, \
          0.6188922756733521, \
          0.6188922756733521, \
          0.6188922756733521, \
          0.6188922756733521, \
          0.7341832387945393, \
          0.7341832387945393, \
          0.7341832387945393, \
          0.7341832387945393, \
          0.7341832387945393, \
          0.7341832387945393, \
          0.2658167612054607, \
          0.2658167612054607, \
          0.2658167612054607, \
          0.2658167612054607, \
          0.2658167612054607, \
          0.2658167612054607, \
          0.4405032526890183, \
          0.4405032526890183, \
          0.4405032526890183, \
          0.4405032526890183, \
          0.4405032526890183, \
          0.4405032526890183, \
          0.5594967473109818, \
          0.5594967473109818, \
          0.5594967473109818, \
          0.5594967473109818, \
          0.5594967473109818, \
          0.5594967473109818, \
          0.7406281263771474, \
          0.7406281263771474, \
          0.7406281263771474, \
          0.7406281263771474, \
          0.7406281263771474, \
          0.7406281263771474, \
          0.2593718736228526, \
          0.2593718736228526, \
          0.2593718736228526, \
          0.2593718736228526, \
          0.2593718736228526, \
          0.2593718736228526, \
          0.4825288515428756, \
          0.4825288515428756, \
          0.4825288515428756, \
          0.4825288515428756, \
          0.4825288515428756, \
          0.4825288515428756, \
          0.5174711484571244, \
          0.5174711484571244, \
          0.5174711484571244, \
          0.5174711484571244, \
          0.5174711484571244, \
          0.5174711484571244, \
          0.6039123747541559, \
          0.6039123747541559, \
          0.6039123747541559, \
          0.6039123747541559, \
          0.6039123747541559, \
          0.6039123747541559, \
          0.3960876252458441, \
          0.3960876252458441, \
          0.3960876252458441, \
          0.3960876252458441, \
          0.3960876252458441, \
          0.3960876252458441, \
          0.8047375675549896, \
          0.8047375675549896, \
          0.8047375675549896, \
          0.8047375675549896, \
          0.8047375675549896, \
          0.8047375675549896, \
          0.1952624324450104, \
          0.1952624324450104, \
          0.1952624324450104, \
          0.1952624324450104, \
          0.1952624324450104, \
          0.1952624324450104, \
          0.9180415438599450, \
          0.9180415438599450, \
          0.9180415438599450, \
          0.9180415438599450, \
          0.9180415438599450, \
          0.9180415438599450, \
          0.0819584561400550, \
          0.0819584561400550, \
          0.0819584561400550, \
          0.0819584561400550, \
          0.0819584561400550, \
          0.0819584561400550, \
          0.8806920867999144, \
          0.8806920867999144, \
          0.8806920867999144, \
          0.8806920867999144, \
          0.8806920867999144, \
          0.8806920867999144, \
          0.1193079132000855, \
          0.1193079132000855, \
          0.1193079132000855, \
          0.1193079132000855, \
          0.1193079132000855, \
          0.1193079132000855, \
          0.7498396447851496, \
          0.7498396447851496, \
          0.7498396447851496, \
          0.7498396447851496, \
          0.7498396447851496, \
          0.7498396447851496, \
          0.2501603552148504, \
          0.2501603552148504, \
          0.2501603552148504, \
          0.2501603552148504, \
          0.2501603552148504, \
          0.2501603552148504, \
          0.9438500554714535, \
          0.9438500554714535, \
          0.9438500554714535, \
          0.9438500554714535, \
          0.9438500554714535, \
          0.9438500554714535, \
          0.0561499445285465, \
          0.0561499445285465, \
          0.0561499445285465, \
          0.0561499445285465, \
          0.0561499445285465, \
          0.0561499445285465, \
          0.9395243139937932, \
          0.9395243139937932, \
          0.9395243139937932, \
          0.9395243139937932, \
          0.9395243139937932, \
          0.9395243139937932, \
          0.0604756860062068, \
          0.0604756860062068, \
          0.0604756860062068, \
          0.0604756860062068, \
          0.0604756860062068, \
          0.0604756860062068, \
          0.8184995763288090, \
          0.8184995763288090, \
          0.8184995763288090, \
          0.8184995763288090, \
          0.8184995763288090, \
          0.8184995763288090, \
          0.1815004236711910, \
          0.1815004236711910, \
          0.1815004236711910, \
          0.1815004236711910, \
          0.1815004236711910, \
          0.1815004236711910, \
          0.9476062382889998, \
          0.9476062382889998, \
          0.9476062382889998, \
          0.9476062382889998, \
          0.9476062382889998, \
          0.9476062382889998, \
          0.0523937617110002, \
          0.0523937617110002, \
          0.0523937617110002, \
          0.0523937617110002, \
          0.0523937617110002, \
          0.0523937617110002, \
          0.9567123523504457, \
          0.9567123523504457, \
          0.9567123523504457, \
          0.9567123523504457, \
          0.9567123523504457, \
          0.9567123523504457, \
          0.0432876476495543, \
          0.0432876476495543, \
          0.0432876476495543, \
          0.0432876476495543, \
          0.0432876476495543, \
          0.0432876476495543, \
          0.9875892078343605, \
          0.9875892078343605, \
          0.9875892078343605, \
          0.9875892078343605, \
          0.9875892078343605, \
          0.9875892078343605, \
          0.0124107921656395, \
          0.0124107921656395, \
          0.0124107921656395, \
          0.0124107921656395, \
          0.0124107921656395, \
          0.0124107921656395, \
          0.9678315615098414, \
          0.9678315615098414, \
          0.9678315615098414, \
          0.9678315615098414, \
          0.9678315615098414, \
          0.9678315615098414, \
          0.0321684384901587, \
          0.0321684384901587, \
          0.0321684384901587, \
          0.0321684384901587, \
          0.0321684384901587, \
          0.0321684384901587, \
          0.8827873971246739, \
          0.8827873971246739, \
          0.8827873971246739, \
          0.8827873971246739, \
          0.8827873971246739, \
          0.8827873971246739, \
          0.1172126028753261, \
          0.1172126028753261, \
          0.1172126028753261, \
          0.1172126028753261, \
          0.1172126028753261, \
          0.1172126028753261, \
          0.7591086801871259, \
          0.7591086801871259, \
          0.7591086801871259, \
          0.7591086801871259, \
          0.7591086801871259, \
          0.7591086801871259, \
          0.2408913198128742, \
          0.2408913198128742, \
          0.2408913198128742, \
          0.2408913198128742, \
          0.2408913198128742, \
          0.2408913198128742, \
          0.8583410425577678, \
          0.8583410425577678, \
          0.8583410425577678, \
          0.8583410425577678, \
          0.8583410425577678, \
          0.8583410425577678, \
          0.1416589574422322, \
          0.1416589574422322, \
          0.1416589574422322, \
          0.1416589574422322, \
          0.1416589574422322, \
          0.1416589574422322, \
          0.8401797426849694, \
          0.8401797426849694, \
          0.8401797426849694, \
          0.8401797426849694, \
          0.8401797426849694, \
          0.8401797426849694, \
          0.1598202573150306, \
          0.1598202573150306, \
          0.1598202573150306, \
          0.1598202573150306, \
          0.1598202573150306, \
          0.1598202573150306, \
          0.6433267612797380, \
          0.6433267612797380, \
          0.6433267612797380, \
          0.6433267612797380, \
          0.6433267612797380, \
          0.6433267612797380, \
          0.3566732387202620, \
          0.3566732387202620, \
          0.3566732387202620, \
          0.3566732387202620, \
          0.3566732387202620, \
          0.3566732387202620, \
          0.9914944215982142, \
          0.9914944215982142, \
          0.9914944215982142, \
          0.9914944215982142, \
          0.9914944215982142, \
          0.9914944215982142, \
          0.0085055784017858, \
          0.0085055784017858, \
          0.0085055784017858, \
          0.0085055784017858, \
          0.0085055784017858, \
          0.0085055784017858, \
          0.9917464272284122, \
          0.9917464272284122, \
          0.9917464272284122, \
          0.9917464272284122, \
          0.9917464272284122, \
          0.9917464272284122, \
          0.0082535727715877, \
          0.0082535727715877, \
          0.0082535727715877, \
          0.0082535727715877, \
          0.0082535727715877, \
          0.0082535727715877, \
          0.9953960310331887, \
          0.9953960310331887, \
          0.9953960310331887, \
          0.9953960310331887, \
          0.9953960310331887, \
          0.9953960310331887, \
          0.0046039689668113, \
          0.0046039689668113, \
          0.0046039689668113, \
          0.0046039689668113, \
          0.0046039689668113, \
          0.0046039689668113 ] )

  w = np.array ( [ \
          0.0047470442329770, \
          0.0047470442329770, \
          0.0006640322548036, \
          0.0006640322548036, \
          0.0006640322548036, \
          0.0009620914054916, \
          0.0009620914054916, \
          0.0009620914054916, \
          0.0027421731795808, \
          0.0027421731795808, \
          0.0027421731795808, \
          0.0027421731795808, \
          0.0027421731795808, \
          0.0027421731795808, \
          0.0028143241025262, \
          0.0028143241025262, \
          0.0028143241025262, \
          0.0028143241025262, \
          0.0028143241025262, \
          0.0028143241025262, \
          0.0038647591741263, \
          0.0038647591741263, \
          0.0038647591741263, \
          0.0038647591741263, \
          0.0038647591741263, \
          0.0038647591741263, \
          0.0037745380549365, \
          0.0037745380549365, \
          0.0037745380549365, \
          0.0037745380549365, \
          0.0037745380549365, \
          0.0037745380549365, \
          0.0002695893315348, \
          0.0002695893315348, \
          0.0002695893315348, \
          0.0002695893315348, \
          0.0002695893315348, \
          0.0002695893315348, \
          0.0011175414425365, \
          0.0011175414425365, \
          0.0011175414425365, \
          0.0011175414425365, \
          0.0011175414425365, \
          0.0011175414425365, \
          0.0011681839673208, \
          0.0011681839673208, \
          0.0011681839673208, \
          0.0011681839673208, \
          0.0011681839673208, \
          0.0011681839673208, \
          0.0009039109611475, \
          0.0009039109611475, \
          0.0009039109611475, \
          0.0009039109611475, \
          0.0009039109611475, \
          0.0009039109611475, \
          0.0033698332015479, \
          0.0033698332015479, \
          0.0033698332015479, \
          0.0033698332015479, \
          0.0033698332015479, \
          0.0033698332015479, \
          0.0026397641711200, \
          0.0026397641711200, \
          0.0026397641711200, \
          0.0026397641711200, \
          0.0026397641711200, \
          0.0026397641711200, \
          0.0025993019789248, \
          0.0025993019789248, \
          0.0025993019789248, \
          0.0025993019789248, \
          0.0025993019789248, \
          0.0025993019789248, \
          0.0012822330144373, \
          0.0012822330144373, \
          0.0012822330144373, \
          0.0012822330144373, \
          0.0012822330144373, \
          0.0012822330144373, \
          0.0012901963397495, \
          0.0012901963397495, \
          0.0012901963397495, \
          0.0012901963397495, \
          0.0012901963397495, \
          0.0012901963397495, \
          0.0036340343281761, \
          0.0036340343281761, \
          0.0036340343281761, \
          0.0036340343281761, \
          0.0036340343281761, \
          0.0036340343281761, \
          0.0038655552411094, \
          0.0038655552411094, \
          0.0038655552411094, \
          0.0038655552411094, \
          0.0038655552411094, \
          0.0038655552411094, \
          0.0010549067548651, \
          0.0010549067548651, \
          0.0010549067548651, \
          0.0010549067548651, \
          0.0010549067548651, \
          0.0010549067548651, \
          0.0015623117217385, \
          0.0015623117217385, \
          0.0015623117217385, \
          0.0015623117217385, \
          0.0015623117217385, \
          0.0015623117217385, \
          0.0004729101647326, \
          0.0004729101647326, \
          0.0004729101647326, \
          0.0004729101647326, \
          0.0004729101647326, \
          0.0004729101647326, \
          0.0001740638131578, \
          0.0001740638131578, \
          0.0001740638131578, \
          0.0001740638131578, \
          0.0001740638131578, \
          0.0001740638131578, \
          0.0028959599653198, \
          0.0028959599653198, \
          0.0028959599653198, \
          0.0028959599653198, \
          0.0028959599653198, \
          0.0028959599653198, \
          0.0052347442788098, \
          0.0052347442788098, \
          0.0052347442788098, \
          0.0052347442788098, \
          0.0052347442788098, \
          0.0052347442788098, \
          0.0031766394449831, \
          0.0031766394449831, \
          0.0031766394449831, \
          0.0031766394449831, \
          0.0031766394449831, \
          0.0031766394449831, \
          0.0027162231233183, \
          0.0027162231233183, \
          0.0027162231233183, \
          0.0027162231233183, \
          0.0027162231233183, \
          0.0027162231233183, \
          0.0032818257977382, \
          0.0032818257977382, \
          0.0032818257977382, \
          0.0032818257977382, \
          0.0032818257977382, \
          0.0032818257977382, \
          0.0031878946984893, \
          0.0031878946984893, \
          0.0031878946984893, \
          0.0031878946984893, \
          0.0031878946984893, \
          0.0031878946984893, \
          0.0035903411322359, \
          0.0035903411322359, \
          0.0035903411322359, \
          0.0035903411322359, \
          0.0035903411322359, \
          0.0035903411322359, \
          0.0035903411322359, \
          0.0035903411322359, \
          0.0035903411322359, \
          0.0035903411322359, \
          0.0035903411322359, \
          0.0035903411322359, \
          0.0005184823629820, \
          0.0005184823629820, \
          0.0005184823629820, \
          0.0005184823629820, \
          0.0005184823629820, \
          0.0005184823629820, \
          0.0005184823629820, \
          0.0005184823629820, \
          0.0005184823629820, \
          0.0005184823629820, \
          0.0005184823629820, \
          0.0005184823629820, \
          0.0020440538003019, \
          0.0020440538003019, \
          0.0020440538003019, \
          0.0020440538003019, \
          0.0020440538003019, \
          0.0020440538003019, \
          0.0020440538003019, \
          0.0020440538003019, \
          0.0020440538003019, \
          0.0020440538003019, \
          0.0020440538003019, \
          0.0020440538003019, \
          0.0024543847025850, \
          0.0024543847025850, \
          0.0024543847025850, \
          0.0024543847025850, \
          0.0024543847025850, \
          0.0024543847025850, \
          0.0024543847025850, \
          0.0024543847025850, \
          0.0024543847025850, \
          0.0024543847025850, \
          0.0024543847025850, \
          0.0024543847025850, \
          0.0041194067328505, \
          0.0041194067328505, \
          0.0041194067328505, \
          0.0041194067328505, \
          0.0041194067328505, \
          0.0041194067328505, \
          0.0041194067328505, \
          0.0041194067328505, \
          0.0041194067328505, \
          0.0041194067328505, \
          0.0041194067328505, \
          0.0041194067328505, \
          0.0057629469800418, \
          0.0057629469800418, \
          0.0057629469800418, \
          0.0057629469800418, \
          0.0057629469800418, \
          0.0057629469800418, \
          0.0057629469800418, \
          0.0057629469800418, \
          0.0057629469800418, \
          0.0057629469800418, \
          0.0057629469800418, \
          0.0057629469800418, \
          0.0032546495070173, \
          0.0032546495070173, \
          0.0032546495070173, \
          0.0032546495070173, \
          0.0032546495070173, \
          0.0032546495070173, \
          0.0032546495070173, \
          0.0032546495070173, \
          0.0032546495070173, \
          0.0032546495070173, \
          0.0032546495070173, \
          0.0032546495070173, \
          0.0013769528611881, \
          0.0013769528611881, \
          0.0013769528611881, \
          0.0013769528611881, \
          0.0013769528611881, \
          0.0013769528611881, \
          0.0013769528611881, \
          0.0013769528611881, \
          0.0013769528611881, \
          0.0013769528611881, \
          0.0013769528611881, \
          0.0013769528611881, \
          0.0013901442662305, \
          0.0013901442662305, \
          0.0013901442662305, \
          0.0013901442662305, \
          0.0013901442662305, \
          0.0013901442662305, \
          0.0013901442662305, \
          0.0013901442662305, \
          0.0013901442662305, \
          0.0013901442662305, \
          0.0013901442662305, \
          0.0013901442662305, \
          0.0019734826201223, \
          0.0019734826201223, \
          0.0019734826201223, \
          0.0019734826201223, \
          0.0019734826201223, \
          0.0019734826201223, \
          0.0019734826201223, \
          0.0019734826201223, \
          0.0019734826201223, \
          0.0019734826201223, \
          0.0019734826201223, \
          0.0019734826201223, \
          0.0011120290537863, \
          0.0011120290537863, \
          0.0011120290537863, \
          0.0011120290537863, \
          0.0011120290537863, \
          0.0011120290537863, \
          0.0011120290537863, \
          0.0011120290537863, \
          0.0011120290537863, \
          0.0011120290537863, \
          0.0011120290537863, \
          0.0011120290537863, \
          0.0011961101336802, \
          0.0011961101336802, \
          0.0011961101336802, \
          0.0011961101336802, \
          0.0011961101336802, \
          0.0011961101336802, \
          0.0011961101336802, \
          0.0011961101336802, \
          0.0011961101336802, \
          0.0011961101336802, \
          0.0011961101336802, \
          0.0011961101336802, \
          0.0018889821414862, \
          0.0018889821414862, \
          0.0018889821414862, \
          0.0018889821414862, \
          0.0018889821414862, \
          0.0018889821414862, \
          0.0018889821414862, \
          0.0018889821414862, \
          0.0018889821414862, \
          0.0018889821414862, \
          0.0018889821414862, \
          0.0018889821414862, \
          0.0005659037184544, \
          0.0005659037184544, \
          0.0005659037184544, \
          0.0005659037184544, \
          0.0005659037184544, \
          0.0005659037184544, \
          0.0005659037184544, \
          0.0005659037184544, \
          0.0005659037184544, \
          0.0005659037184544, \
          0.0005659037184544, \
          0.0005659037184544, \
          0.0018321887972236, \
          0.0018321887972236, \
          0.0018321887972236, \
          0.0018321887972236, \
          0.0018321887972236, \
          0.0018321887972236, \
          0.0018321887972236, \
          0.0018321887972236, \
          0.0018321887972236, \
          0.0018321887972236, \
          0.0018321887972236, \
          0.0018321887972236, \
          0.0008460253945738, \
          0.0008460253945738, \
          0.0008460253945738, \
          0.0008460253945738, \
          0.0008460253945738, \
          0.0008460253945738, \
          0.0008460253945738, \
          0.0008460253945738, \
          0.0008460253945738, \
          0.0008460253945738, \
          0.0008460253945738, \
          0.0008460253945738, \
          0.0015975131973438, \
          0.0015975131973438, \
          0.0015975131973438, \
          0.0015975131973438, \
          0.0015975131973438, \
          0.0015975131973438, \
          0.0015975131973438, \
          0.0015975131973438, \
          0.0015975131973438, \
          0.0015975131973438, \
          0.0015975131973438, \
          0.0015975131973438, \
          0.0026781578703448, \
          0.0026781578703448, \
          0.0026781578703448, \
          0.0026781578703448, \
          0.0026781578703448, \
          0.0026781578703448, \
          0.0026781578703448, \
          0.0026781578703448, \
          0.0026781578703448, \
          0.0026781578703448, \
          0.0026781578703448, \
          0.0026781578703448, \
          0.0007373212126546, \
          0.0007373212126546, \
          0.0007373212126546, \
          0.0007373212126546, \
          0.0007373212126546, \
          0.0007373212126546, \
          0.0007373212126546, \
          0.0007373212126546, \
          0.0007373212126546, \
          0.0007373212126546, \
          0.0007373212126546, \
          0.0007373212126546, \
          0.0013900594133789, \
          0.0013900594133789, \
          0.0013900594133789, \
          0.0013900594133789, \
          0.0013900594133789, \
          0.0013900594133789, \
          0.0013900594133789, \
          0.0013900594133789, \
          0.0013900594133789, \
          0.0013900594133789, \
          0.0013900594133789, \
          0.0013900594133789, \
          0.0007964285504550, \
          0.0007964285504550, \
          0.0007964285504550, \
          0.0007964285504550, \
          0.0007964285504550, \
          0.0007964285504550, \
          0.0007964285504550, \
          0.0007964285504550, \
          0.0007964285504550, \
          0.0007964285504550, \
          0.0007964285504550, \
          0.0007964285504550, \
          0.0014601164425740, \
          0.0014601164425740, \
          0.0014601164425740, \
          0.0014601164425740, \
          0.0014601164425740, \
          0.0014601164425740, \
          0.0014601164425740, \
          0.0014601164425740, \
          0.0014601164425740, \
          0.0014601164425740, \
          0.0014601164425740, \
          0.0014601164425740, \
          0.0013483736840244, \
          0.0013483736840244, \
          0.0013483736840244, \
          0.0013483736840244, \
          0.0013483736840244, \
          0.0013483736840244, \
          0.0013483736840244, \
          0.0013483736840244, \
          0.0013483736840244, \
          0.0013483736840244, \
          0.0013483736840244, \
          0.0013483736840244, \
          0.0032860508781285, \
          0.0032860508781285, \
          0.0032860508781285, \
          0.0032860508781285, \
          0.0032860508781285, \
          0.0032860508781285, \
          0.0032860508781285, \
          0.0032860508781285, \
          0.0032860508781285, \
          0.0032860508781285, \
          0.0032860508781285, \
          0.0032860508781285, \
          0.0011247201187777, \
          0.0011247201187777, \
          0.0011247201187777, \
          0.0011247201187777, \
          0.0011247201187777, \
          0.0011247201187777, \
          0.0011247201187777, \
          0.0011247201187777, \
          0.0011247201187777, \
          0.0011247201187777, \
          0.0011247201187777, \
          0.0011247201187777, \
          0.0021271072748908, \
          0.0021271072748908, \
          0.0021271072748908, \
          0.0021271072748908, \
          0.0021271072748908, \
          0.0021271072748908, \
          0.0021271072748908, \
          0.0021271072748908, \
          0.0021271072748908, \
          0.0021271072748908, \
          0.0021271072748908, \
          0.0021271072748908, \
          0.0007135219223491, \
          0.0007135219223491, \
          0.0007135219223491, \
          0.0007135219223491, \
          0.0007135219223491, \
          0.0007135219223491, \
          0.0007135219223491, \
          0.0007135219223491, \
          0.0007135219223491, \
          0.0007135219223491, \
          0.0007135219223491, \
          0.0007135219223491, \
          0.0003719588400836, \
          0.0003719588400836, \
          0.0003719588400836, \
          0.0003719588400836, \
          0.0003719588400836, \
          0.0003719588400836, \
          0.0003719588400836, \
          0.0003719588400836, \
          0.0003719588400836, \
          0.0003719588400836, \
          0.0003719588400836, \
          0.0003719588400836, \
          0.0002151829924432, \
          0.0002151829924432, \
          0.0002151829924432, \
          0.0002151829924432, \
          0.0002151829924432, \
          0.0002151829924432, \
          0.0002151829924432, \
          0.0002151829924432, \
          0.0002151829924432, \
          0.0002151829924432, \
          0.0002151829924432, \
          0.0002151829924432, \
          0.0008163226512583, \
          0.0008163226512583, \
          0.0008163226512583, \
          0.0008163226512583, \
          0.0008163226512583, \
          0.0008163226512583, \
          0.0008163226512583, \
          0.0008163226512583, \
          0.0008163226512583, \
          0.0008163226512583, \
          0.0008163226512583, \
          0.0008163226512583 ] )

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
  prism_jaskowiec_rule_test ( )
  timestamp ( )



