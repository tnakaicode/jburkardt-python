#! /usr/bin/env python3
#
def prism_witherden_rule_test ( ):

#*****************************************************************************80
#
## prism_witherden_rule_test() tests prism_witherden_rule().
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
  print ( 'prism_witherden_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test prism_witherden_rule().' )

  p = 5
  prism_witherden_rule_test01 ( p )

  p = 5
  prism_witherden_rule_test02 ( p )

  p_lo = 0
  p_hi = 10
  prism_witherden_rule_test03 ( p_lo, p_hi )
#
#  Terminate.
#
  print ( '' )
  print ( 'prism_witherden_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def prism_witherden_rule_test01 ( p ):

#*****************************************************************************80
#
## prism_witherden_rule_test01() computes a quadrature rule of precision P.
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
  print ( 'prism_witherden_rule_test01():' )
  print ( '  Quadrature rule for the unit prism,' )
  print ( '  Precision p = ', p )
#
#  Retrieve the rule.
#
  n, x, y, z, w = prism_witherden_rule ( p )
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

def prism_witherden_rule_test02 ( p ):

#*****************************************************************************80
#
## prism_witherden_rule_test02() tests a rule of precision P.
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
  print ( 'prism_witherden_rule_test02():' )
  print ( '  Test the precision of a quadrature rule for the unit prism.' )

  dim_num = 3
#
#  Retrieve the rule.
#
  n, x, y, z, w = prism_witherden_rule ( p )
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

def prism_witherden_rule_test03 ( p_lo, p_hi ):

#*****************************************************************************80
#
## prism_witherden_rule_test03() tests absolute and relative precision.
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
#  Input:
#
#    integer p_lo, p_hi: the lowest and highest rules to check.
# 
  import numpy as np

  print ( '' )
  print ( 'prism_witherden_rule_test03():' )
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

    n, x, y, z, w = prism_witherden_rule ( p )
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

def prism_witherden_rule ( p ):

#*****************************************************************************80
#
## prism_witherden_rule() returns a prism quadrature rule of given precision.
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
#    Freddie Witherden, Peter Vincent,
#    On the identification of symmetric quadrature rules for finite element methods,
#    Computers and Mathematics with Applications,
#    Volume 69, pages 1232-1241, 2015.
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
    raise Exception ( 'prism_witherden_rule(): Input p < 0.' )
 
  if ( 20 < p ):
    raise Exception ( 'prism_witherden_rule(): Input 20 < p.' )

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
#    27 April 2023
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
          0.3333333333333334 ] )

  y = np.array ( [ \
          0.3333333333333334 ] )

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
#    27 April 2023
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
          0.3333333333333334 ] )

  y = np.array ( [ \
          0.3333333333333334 ] )

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
#    27 April 2023
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
          0.3333333333333334, \
          0.3333333333333334, \
          0.1292091881014018, \
          0.7415816237971964, \
          0.1292091881014018 ] )

  y = np.array ( [ \
          0.3333333333333334, \
          0.3333333333333334, \
          0.7415816237971964, \
          0.1292091881014018, \
          0.1292091881014018 ] )

  z = np.array ( [ \
          0.0000000000000001, \
          1.0000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000 ] )

  w = np.array ( [ \
          0.1666666666666667, \
          0.1666666666666667, \
          0.2222222222222222, \
          0.2222222222222222, \
          0.2222222222222222 ] )

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
#    27 April 2023
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
          0.3333333333333334, \
          0.3333333333333334, \
          0.2388834359565783, \
          0.7611141478748917, \
          0.0000024161685299, \
          0.7611141478748917, \
          0.0000024161685299, \
          0.2388834359565783 ] )

  y = np.array ( [ \
          0.3333333333333334, \
          0.3333333333333334, \
          0.7611141478748917, \
          0.2388834359565783, \
          0.7611141478748917, \
          0.0000024161685299, \
          0.2388834359565783, \
          0.0000024161685299 ] )

  z = np.array ( [ \
          0.0696653977676110, \
          0.9303346022323890, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000 ] )

  w = np.array ( [ \
          0.2249967381449005, \
          0.2249967381449005, \
          0.0916677539516998, \
          0.0916677539516998, \
          0.0916677539516998, \
          0.0916677539516998, \
          0.0916677539516998, \
          0.0916677539516998 ] )

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
#    27 April 2023
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
          0.3333333333333334, \
          0.3333333333333334, \
          0.4686558098619952, \
          0.0626883802760096, \
          0.4686558098619952, \
          0.1007404057989106, \
          0.7985191884021787, \
          0.1007404057989106, \
          0.1007404057989106, \
          0.7985191884021787, \
          0.1007404057989106 ] )

  y = np.array ( [ \
          0.3333333333333334, \
          0.3333333333333334, \
          0.0626883802760096, \
          0.4686558098619952, \
          0.4686558098619952, \
          0.7985191884021787, \
          0.1007404057989106, \
          0.1007404057989106, \
          0.7985191884021787, \
          0.1007404057989106, \
          0.1007404057989106 ] )

  z = np.array ( [ \
          0.0665690129954826, \
          0.9334309870045174, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1621800881588701, \
          0.1621800881588701, \
          0.1621800881588701, \
          0.8378199118411298, \
          0.8378199118411298, \
          0.8378199118411298 ] )

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
#    27 April 2023
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
          0.3333333333333334, \
          0.4872999645502457, \
          0.0254000708995087, \
          0.4872999645502457, \
          0.4455981046703720, \
          0.1088037906592560, \
          0.4455981046703720, \
          0.4455981046703720, \
          0.1088037906592560, \
          0.4455981046703720, \
          0.1008589459827085, \
          0.7982821080345830, \
          0.1008589459827085, \
          0.1008589459827085, \
          0.7982821080345830, \
          0.1008589459827085 ] )

  y = np.array ( [ \
          0.3333333333333334, \
          0.0254000708995087, \
          0.4872999645502457, \
          0.4872999645502457, \
          0.1088037906592560, \
          0.4455981046703720, \
          0.4455981046703720, \
          0.1088037906592560, \
          0.4455981046703720, \
          0.4455981046703720, \
          0.7982821080345830, \
          0.1008589459827085, \
          0.1008589459827085, \
          0.7982821080345830, \
          0.1008589459827085, \
          0.1008589459827085 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0644985325672780, \
          0.0644985325672780, \
          0.0644985325672780, \
          0.9355014674327220, \
          0.9355014674327220, \
          0.9355014674327220, \
          0.2147865096474204, \
          0.2147865096474204, \
          0.2147865096474204, \
          0.7852134903525796, \
          0.7852134903525796, \
          0.7852134903525796 ] )

  w = np.array ( [ \
          0.1778638889828717, \
          0.0561775168070667, \
          0.0561775168070667, \
          0.0561775168070667, \
          0.0464153553290395, \
          0.0464153553290395, \
          0.0464153553290395, \
          0.0464153553290395, \
          0.0464153553290395, \
          0.0464153553290395, \
          0.0625185714369485, \
          0.0625185714369485, \
          0.0625185714369485, \
          0.0625185714369485, \
          0.0625185714369485, \
          0.0625185714369485 ] )

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
#    27 April 2023
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
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.1652032650280925, \
          0.6695934699438151, \
          0.1652032650280925, \
          0.0204732696122569, \
          0.9590534607754861, \
          0.0204732696122569, \
          0.4661116655901595, \
          0.0677766688196810, \
          0.4661116655901595, \
          0.4661116655901595, \
          0.0677766688196810, \
          0.4661116655901595, \
          0.2025738967252308, \
          0.7627467408337223, \
          0.0346793624410470, \
          0.7627467408337223, \
          0.0346793624410470, \
          0.2025738967252308, \
          0.2025738967252308, \
          0.7627467408337223, \
          0.0346793624410470, \
          0.7627467408337223, \
          0.0346793624410470, \
          0.2025738967252308 ] )

  y = np.array ( [ \
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.6695934699438151, \
          0.1652032650280925, \
          0.1652032650280925, \
          0.9590534607754861, \
          0.0204732696122569, \
          0.0204732696122569, \
          0.0677766688196810, \
          0.4661116655901595, \
          0.4661116655901595, \
          0.0677766688196810, \
          0.4661116655901595, \
          0.4661116655901595, \
          0.7627467408337223, \
          0.2025738967252308, \
          0.7627467408337223, \
          0.0346793624410470, \
          0.2025738967252308, \
          0.0346793624410470, \
          0.7627467408337223, \
          0.2025738967252308, \
          0.7627467408337223, \
          0.0346793624410470, \
          0.2025738967252308, \
          0.0346793624410470 ] )

  z = np.array ( [ \
          0.2366886475975126, \
          0.7633113524024874, \
          0.0045818495903776, \
          0.9954181504096224, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.2591629325578062, \
          0.2591629325578062, \
          0.2591629325578062, \
          0.7408370674421938, \
          0.7408370674421938, \
          0.7408370674421938, \
          0.0953571033720836, \
          0.0953571033720836, \
          0.0953571033720836, \
          0.0953571033720836, \
          0.0953571033720836, \
          0.0953571033720836, \
          0.9046428966279163, \
          0.9046428966279163, \
          0.9046428966279163, \
          0.9046428966279163, \
          0.9046428966279163, \
          0.9046428966279163 ] )

  w = np.array ( [ \
          0.0556732835230563, \
          0.0556732835230563, \
          0.0345990273435311, \
          0.0345990273435311, \
          0.0779570037033338, \
          0.0779570037033338, \
          0.0779570037033338, \
          0.0125366338096741, \
          0.0125366338096741, \
          0.0125366338096741, \
          0.0490126400515205, \
          0.0490126400515205, \
          0.0490126400515205, \
          0.0490126400515205, \
          0.0490126400515205, \
          0.0490126400515205, \
          0.0211582187848898, \
          0.0211582187848898, \
          0.0211582187848898, \
          0.0211582187848898, \
          0.0211582187848898, \
          0.0211582187848898, \
          0.0211582187848898, \
          0.0211582187848898, \
          0.0211582187848898, \
          0.0211582187848898, \
          0.0211582187848898, \
          0.0211582187848898 ] )

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
#    27 April 2023
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
          0.3333333333333334, \
          0.3333333333333334, \
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

  y = np.array ( [ \
          0.3333333333333334, \
          0.3333333333333334, \
          0.9833248090679571, \
          0.0083375954660215, \
          0.0083375954660215, \
          0.0369560493417268, \
          0.4815219753291366, \
          0.4815219753291366, \
          0.0369560493417268, \
          0.4815219753291366, \
          0.4815219753291366, \
          0.8090335032570213, \
          0.0954832483714894, \
          0.0954832483714894, \
          0.8090335032570213, \
          0.0954832483714894, \
          0.0954832483714894, \
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

  z = np.array ( [ \
          0.0098859652045542, \
          0.9901140347954458, \
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
          0.2980327197339451, \
          0.2980327197339451, \
          0.2980327197339451, \
          0.2980327197339451, \
          0.2980327197339451, \
          0.2980327197339451, \
          0.7019672802660549, \
          0.7019672802660549, \
          0.7019672802660549, \
          0.7019672802660549, \
          0.7019672802660549, \
          0.7019672802660549 ] )

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
#    27 April 2023
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
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.0534123509369072, \
          0.8931752981261858, \
          0.0534123509369072, \
          0.4600889628137106, \
          0.0798220743725788, \
          0.4600889628137106, \
          0.4585690687909513, \
          0.0828618624180973, \
          0.4585690687909513, \
          0.4585690687909513, \
          0.0828618624180973, \
          0.4585690687909513, \
          0.1740616079243704, \
          0.6518767841512592, \
          0.1740616079243704, \
          0.1740616079243704, \
          0.6518767841512592, \
          0.1740616079243704, \
          0.0472387858397694, \
          0.9055224283204613, \
          0.0472387858397694, \
          0.0472387858397694, \
          0.9055224283204613, \
          0.0472387858397694, \
          0.1597492639425890, \
          0.6805014721148220, \
          0.1597492639425890, \
          0.1597492639425890, \
          0.6805014721148220, \
          0.1597492639425890, \
          0.2628138006912410, \
          0.7285980718010000, \
          0.0085881275077590, \
          0.7285980718010000, \
          0.0085881275077590, \
          0.2628138006912410, \
          0.2628138006912410, \
          0.7285980718010000, \
          0.0085881275077590, \
          0.7285980718010000, \
          0.0085881275077590, \
          0.2628138006912410 ] )

  y = np.array ( [ \
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.8931752981261858, \
          0.0534123509369072, \
          0.0534123509369072, \
          0.0798220743725788, \
          0.4600889628137106, \
          0.4600889628137106, \
          0.0828618624180973, \
          0.4585690687909513, \
          0.4585690687909513, \
          0.0828618624180973, \
          0.4585690687909513, \
          0.4585690687909513, \
          0.6518767841512592, \
          0.1740616079243704, \
          0.1740616079243704, \
          0.6518767841512592, \
          0.1740616079243704, \
          0.1740616079243704, \
          0.9055224283204613, \
          0.0472387858397694, \
          0.0472387858397694, \
          0.9055224283204613, \
          0.0472387858397694, \
          0.0472387858397694, \
          0.6805014721148220, \
          0.1597492639425890, \
          0.1597492639425890, \
          0.6805014721148220, \
          0.1597492639425890, \
          0.1597492639425890, \
          0.7285980718010000, \
          0.2628138006912410, \
          0.7285980718010000, \
          0.0085881275077590, \
          0.2628138006912410, \
          0.0085881275077590, \
          0.7285980718010000, \
          0.2628138006912410, \
          0.7285980718010000, \
          0.0085881275077590, \
          0.2628138006912410, \
          0.0085881275077590 ] )

  z = np.array ( [ \
          0.3877830669470047, \
          0.6122169330529953, \
          0.1590872792145671, \
          0.8409127207854329, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0619020449998729, \
          0.0619020449998729, \
          0.0619020449998729, \
          0.9380979550001272, \
          0.9380979550001272, \
          0.9380979550001272, \
          0.2969578853227048, \
          0.2969578853227048, \
          0.2969578853227048, \
          0.7030421146772952, \
          0.7030421146772952, \
          0.7030421146772952, \
          0.0855922784706599, \
          0.0855922784706599, \
          0.0855922784706599, \
          0.9144077215293400, \
          0.9144077215293400, \
          0.9144077215293400, \
          0.0170674167296728, \
          0.0170674167296728, \
          0.0170674167296728, \
          0.9829325832703272, \
          0.9829325832703272, \
          0.9829325832703272, \
          0.2113248654051871, \
          0.2113248654051871, \
          0.2113248654051871, \
          0.2113248654051871, \
          0.2113248654051871, \
          0.2113248654051871, \
          0.7886751345948129, \
          0.7886751345948129, \
          0.7886751345948129, \
          0.7886751345948129, \
          0.7886751345948129, \
          0.7886751345948129 ] )

  w = np.array ( [ \
          0.0207349366428555, \
          0.0207349366428555, \
          0.0510894271121815, \
          0.0510894271121815, \
          0.0181522487841497, \
          0.0181522487841497, \
          0.0181522487841497, \
          0.0526997449065072, \
          0.0526997449065072, \
          0.0526997449065072, \
          0.0210865092935865, \
          0.0210865092935865, \
          0.0210865092935865, \
          0.0210865092935865, \
          0.0210865092935865, \
          0.0210865092935865, \
          0.0406292626589893, \
          0.0406292626589893, \
          0.0406292626589893, \
          0.0406292626589893, \
          0.0406292626589893, \
          0.0406292626589893, \
          0.0071453577535386, \
          0.0071453577535386, \
          0.0071453577535386, \
          0.0071453577535386, \
          0.0071453577535386, \
          0.0071453577535386, \
          0.0111430273484653, \
          0.0111430273484653, \
          0.0111430273484653, \
          0.0111430273484653, \
          0.0111430273484653, \
          0.0111430273484653, \
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
#    27 April 2023
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
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.4994650351706859, \
          0.0010699296586282, \
          0.4994650351706859, \
          0.4450675000425037, \
          0.1098649999149927, \
          0.4450675000425037, \
          0.4450675000425037, \
          0.1098649999149927, \
          0.4450675000425037, \
          0.2111544337105105, \
          0.5776911325789790, \
          0.2111544337105105, \
          0.2111544337105105, \
          0.5776911325789790, \
          0.2111544337105105, \
          0.0438424814414928, \
          0.9123150371170143, \
          0.0438424814414928, \
          0.0438424814414928, \
          0.9123150371170143, \
          0.0438424814414928, \
          0.4827499316708669, \
          0.0345001366582662, \
          0.4827499316708669, \
          0.4827499316708669, \
          0.0345001366582662, \
          0.4827499316708669, \
          0.1771782441116773, \
          0.6456435117766455, \
          0.1771782441116773, \
          0.1771782441116773, \
          0.6456435117766455, \
          0.1771782441116773, \
          0.0462311804109438, \
          0.9075376391781124, \
          0.0462311804109438, \
          0.0462311804109438, \
          0.9075376391781124, \
          0.0462311804109438, \
          0.0593670097433656, \
          0.7246952695529995, \
          0.2159377207036349, \
          0.7246952695529995, \
          0.2159377207036349, \
          0.0593670097433656, \
          0.2241275457533561, \
          0.7484054595660388, \
          0.0274669946806053, \
          0.7484054595660388, \
          0.0274669946806053, \
          0.2241275457533561, \
          0.2241275457533561, \
          0.7484054595660388, \
          0.0274669946806053, \
          0.7484054595660388, \
          0.0274669946806053, \
          0.2241275457533561 ] )

  y = np.array ( [ \
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.0010699296586282, \
          0.4994650351706859, \
          0.4994650351706859, \
          0.1098649999149927, \
          0.4450675000425037, \
          0.4450675000425037, \
          0.1098649999149927, \
          0.4450675000425037, \
          0.4450675000425037, \
          0.5776911325789790, \
          0.2111544337105105, \
          0.2111544337105105, \
          0.5776911325789790, \
          0.2111544337105105, \
          0.2111544337105105, \
          0.9123150371170143, \
          0.0438424814414928, \
          0.0438424814414928, \
          0.9123150371170143, \
          0.0438424814414928, \
          0.0438424814414928, \
          0.0345001366582662, \
          0.4827499316708669, \
          0.4827499316708669, \
          0.0345001366582662, \
          0.4827499316708669, \
          0.4827499316708669, \
          0.6456435117766455, \
          0.1771782441116773, \
          0.1771782441116773, \
          0.6456435117766455, \
          0.1771782441116773, \
          0.1771782441116773, \
          0.9075376391781124, \
          0.0462311804109438, \
          0.0462311804109438, \
          0.9075376391781124, \
          0.0462311804109438, \
          0.0462311804109438, \
          0.7246952695529995, \
          0.0593670097433656, \
          0.7246952695529995, \
          0.2159377207036349, \
          0.0593670097433656, \
          0.2159377207036349, \
          0.7484054595660388, \
          0.2241275457533561, \
          0.7484054595660388, \
          0.0274669946806053, \
          0.2241275457533561, \
          0.0274669946806053, \
          0.7484054595660388, \
          0.2241275457533561, \
          0.7484054595660388, \
          0.0274669946806053, \
          0.2241275457533561, \
          0.0274669946806053 ] )

  z = np.array ( [ \
          0.5000000000000000, \
          0.0620804206000612, \
          0.9379195793999389, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.2351832223969616, \
          0.2351832223969616, \
          0.2351832223969616, \
          0.7648167776030383, \
          0.7648167776030383, \
          0.7648167776030383, \
          0.3380115589156150, \
          0.3380115589156150, \
          0.3380115589156150, \
          0.6619884410843850, \
          0.6619884410843850, \
          0.6619884410843850, \
          0.2991741657146056, \
          0.2991741657146056, \
          0.2991741657146056, \
          0.7008258342853944, \
          0.7008258342853944, \
          0.7008258342853944, \
          0.0161039372678948, \
          0.0161039372678948, \
          0.0161039372678948, \
          0.9838960627321052, \
          0.9838960627321052, \
          0.9838960627321052, \
          0.0546091297715147, \
          0.0546091297715147, \
          0.0546091297715147, \
          0.9453908702284853, \
          0.9453908702284853, \
          0.9453908702284853, \
          0.0211468980535365, \
          0.0211468980535365, \
          0.0211468980535365, \
          0.9788531019464635, \
          0.9788531019464635, \
          0.9788531019464635, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.1523897230641826, \
          0.1523897230641826, \
          0.1523897230641826, \
          0.1523897230641826, \
          0.1523897230641826, \
          0.1523897230641826, \
          0.8476102769358174, \
          0.8476102769358174, \
          0.8476102769358174, \
          0.8476102769358174, \
          0.8476102769358174, \
          0.8476102769358174 ] )

  w = np.array ( [ \
          0.0477869971115503, \
          0.0265242298973318, \
          0.0265242298973318, \
          0.0123656013604738, \
          0.0123656013604738, \
          0.0123656013604738, \
          0.0377019831531896, \
          0.0377019831531896, \
          0.0377019831531896, \
          0.0377019831531896, \
          0.0377019831531896, \
          0.0377019831531896, \
          0.0233456174363846, \
          0.0233456174363846, \
          0.0233456174363846, \
          0.0233456174363846, \
          0.0233456174363846, \
          0.0233456174363846, \
          0.0095970715963016, \
          0.0095970715963016, \
          0.0095970715963016, \
          0.0095970715963016, \
          0.0095970715963016, \
          0.0095970715963016, \
          0.0066321078005801, \
          0.0066321078005801, \
          0.0066321078005801, \
          0.0066321078005801, \
          0.0066321078005801, \
          0.0066321078005801, \
          0.0166799856433621, \
          0.0166799856433621, \
          0.0166799856433621, \
          0.0166799856433621, \
          0.0166799856433621, \
          0.0166799856433621, \
          0.0030327934591018, \
          0.0030327934591018, \
          0.0030327934591018, \
          0.0030327934591018, \
          0.0030327934591018, \
          0.0030327934591018, \
          0.0219227903282098, \
          0.0219227903282098, \
          0.0219227903282098, \
          0.0219227903282098, \
          0.0219227903282098, \
          0.0219227903282098, \
          0.0123828035424656, \
          0.0123828035424656, \
          0.0123828035424656, \
          0.0123828035424656, \
          0.0123828035424656, \
          0.0123828035424656, \
          0.0123828035424656, \
          0.0123828035424656, \
          0.0123828035424656, \
          0.0123828035424656, \
          0.0123828035424656, \
          0.0123828035424656 ] )

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
#    27 April 2023
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
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.2074503749892171, \
          0.5850992500215657, \
          0.2074503749892171, \
          0.4561273628680818, \
          0.0877452742638365, \
          0.4561273628680818, \
          0.0833192521500528, \
          0.8333614956998945, \
          0.0833192521500528, \
          0.2071663521398311, \
          0.5856672957203378, \
          0.2071663521398311, \
          0.2071663521398311, \
          0.5856672957203378, \
          0.2071663521398311, \
          0.1429911965428408, \
          0.7140176069143184, \
          0.1429911965428408, \
          0.1429911965428408, \
          0.7140176069143184, \
          0.1429911965428408, \
          0.4970408872397459, \
          0.0059182255205082, \
          0.4970408872397459, \
          0.4970408872397459, \
          0.0059182255205082, \
          0.4970408872397459, \
          0.4277824598534921, \
          0.1444350802930158, \
          0.4277824598534921, \
          0.4277824598534921, \
          0.1444350802930158, \
          0.4277824598534921, \
          0.0367246894695538, \
          0.9265506210608924, \
          0.0367246894695538, \
          0.0367246894695538, \
          0.9265506210608924, \
          0.0367246894695538, \
          0.0018926195990494, \
          0.9979100409523263, \
          0.0001973394486243, \
          0.9979100409523263, \
          0.0001973394486243, \
          0.0018926195990494, \
          0.0432896837794919, \
          0.6627532432395955, \
          0.2939570729809126, \
          0.6627532432395955, \
          0.2939570729809126, \
          0.0432896837794919, \
          0.0432896837794919, \
          0.6627532432395955, \
          0.2939570729809126, \
          0.6627532432395955, \
          0.2939570729809126, \
          0.0432896837794919, \
          0.0382915191722036, \
          0.6875657341783573, \
          0.2741427466494392, \
          0.6875657341783573, \
          0.2741427466494392, \
          0.0382915191722036, \
          0.0382915191722036, \
          0.6875657341783573, \
          0.2741427466494392, \
          0.6875657341783573, \
          0.2741427466494392, \
          0.0382915191722036, \
          0.0160393936272334, \
          0.8702636086393689, \
          0.1136969977333976, \
          0.8702636086393689, \
          0.1136969977333976, \
          0.0160393936272334, \
          0.0160393936272334, \
          0.8702636086393689, \
          0.1136969977333976, \
          0.8702636086393689, \
          0.1136969977333976, \
          0.0160393936272334 ] )

  y = np.array ( [ \
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.3333333333333334, \
          0.5850992500215657, \
          0.2074503749892171, \
          0.2074503749892171, \
          0.0877452742638365, \
          0.4561273628680818, \
          0.4561273628680818, \
          0.8333614956998945, \
          0.0833192521500528, \
          0.0833192521500528, \
          0.5856672957203378, \
          0.2071663521398311, \
          0.2071663521398311, \
          0.5856672957203378, \
          0.2071663521398311, \
          0.2071663521398311, \
          0.7140176069143184, \
          0.1429911965428408, \
          0.1429911965428408, \
          0.7140176069143184, \
          0.1429911965428408, \
          0.1429911965428408, \
          0.0059182255205082, \
          0.4970408872397459, \
          0.4970408872397459, \
          0.0059182255205082, \
          0.4970408872397459, \
          0.4970408872397459, \
          0.1444350802930158, \
          0.4277824598534921, \
          0.4277824598534921, \
          0.1444350802930158, \
          0.4277824598534921, \
          0.4277824598534921, \
          0.9265506210608924, \
          0.0367246894695538, \
          0.0367246894695538, \
          0.9265506210608924, \
          0.0367246894695538, \
          0.0367246894695538, \
          0.9979100409523263, \
          0.0018926195990494, \
          0.9979100409523263, \
          0.0001973394486243, \
          0.0018926195990494, \
          0.0001973394486243, \
          0.6627532432395955, \
          0.0432896837794919, \
          0.6627532432395955, \
          0.2939570729809126, \
          0.0432896837794919, \
          0.2939570729809126, \
          0.6627532432395955, \
          0.0432896837794919, \
          0.6627532432395955, \
          0.2939570729809126, \
          0.0432896837794919, \
          0.2939570729809126, \
          0.6875657341783573, \
          0.0382915191722036, \
          0.6875657341783573, \
          0.2741427466494392, \
          0.0382915191722036, \
          0.2741427466494392, \
          0.6875657341783573, \
          0.0382915191722036, \
          0.6875657341783573, \
          0.2741427466494392, \
          0.0382915191722036, \
          0.2741427466494392, \
          0.8702636086393689, \
          0.0160393936272334, \
          0.8702636086393689, \
          0.1136969977333976, \
          0.0160393936272334, \
          0.1136969977333976, \
          0.8702636086393689, \
          0.0160393936272334, \
          0.8702636086393689, \
          0.1136969977333976, \
          0.0160393936272334, \
          0.1136969977333976 ] )

  z = np.array ( [ \
          0.0000000000000000, \
          1.0000000000000000, \
          0.3580817993007142, \
          0.6419182006992858, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.2608548695498160, \
          0.2608548695498160, \
          0.2608548695498160, \
          0.7391451304501840, \
          0.7391451304501840, \
          0.7391451304501840, \
          0.0739666680004302, \
          0.0739666680004302, \
          0.0739666680004302, \
          0.9260333319995698, \
          0.9260333319995698, \
          0.9260333319995698, \
          0.1862549441760233, \
          0.1862549441760233, \
          0.1862549441760233, \
          0.8137450558239767, \
          0.8137450558239767, \
          0.8137450558239767, \
          0.1155140587235295, \
          0.1155140587235295, \
          0.1155140587235295, \
          0.8844859412764705, \
          0.8844859412764705, \
          0.8844859412764705, \
          0.0273190720391215, \
          0.0273190720391215, \
          0.0273190720391215, \
          0.9726809279608786, \
          0.9726809279608786, \
          0.9726809279608786, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.5000000000000000, \
          0.0288182662745812, \
          0.0288182662745812, \
          0.0288182662745812, \
          0.0288182662745812, \
          0.0288182662745812, \
          0.0288182662745812, \
          0.9711817337254187, \
          0.9711817337254187, \
          0.9711817337254187, \
          0.9711817337254187, \
          0.9711817337254187, \
          0.9711817337254187, \
          0.3323319456663029, \
          0.3323319456663029, \
          0.3323319456663029, \
          0.3323319456663029, \
          0.3323319456663029, \
          0.3323319456663029, \
          0.6676680543336971, \
          0.6676680543336971, \
          0.6676680543336971, \
          0.6676680543336971, \
          0.6676680543336971, \
          0.6676680543336971, \
          0.1928382490614613, \
          0.1928382490614613, \
          0.1928382490614613, \
          0.1928382490614613, \
          0.1928382490614613, \
          0.1928382490614613, \
          0.8071617509385387, \
          0.8071617509385387, \
          0.8071617509385387, \
          0.8071617509385387, \
          0.8071617509385387, \
          0.8071617509385387 ] )

  w = np.array ( [ \
          0.0095107770210602, \
          0.0095107770210602, \
          0.0320123016081395, \
          0.0320123016081395, \
          0.0113557896200342, \
          0.0113557896200342, \
          0.0113557896200342, \
          0.0301966545250866, \
          0.0301966545250866, \
          0.0301966545250866, \
          0.0176309095004028, \
          0.0176309095004028, \
          0.0176309095004028, \
          0.0260882953260851, \
          0.0260882953260851, \
          0.0260882953260851, \
          0.0260882953260851, \
          0.0260882953260851, \
          0.0260882953260851, \
          0.0113382624425785, \
          0.0113382624425785, \
          0.0113382624425785, \
          0.0113382624425785, \
          0.0113382624425785, \
          0.0113382624425785, \
          0.0070316434137385, \
          0.0070316434137385, \
          0.0070316434137385, \
          0.0070316434137385, \
          0.0070316434137385, \
          0.0070316434137385, \
          0.0243250168786856, \
          0.0243250168786856, \
          0.0243250168786856, \
          0.0243250168786856, \
          0.0243250168786856, \
          0.0243250168786856, \
          0.0018924357100839, \
          0.0018924357100839, \
          0.0018924357100839, \
          0.0018924357100839, \
          0.0018924357100839, \
          0.0018924357100839, \
          0.0007802159100457, \
          0.0007802159100457, \
          0.0007802159100457, \
          0.0007802159100457, \
          0.0007802159100457, \
          0.0007802159100457, \
          0.0060458851624517, \
          0.0060458851624517, \
          0.0060458851624517, \
          0.0060458851624517, \
          0.0060458851624517, \
          0.0060458851624517, \
          0.0060458851624517, \
          0.0060458851624517, \
          0.0060458851624517, \
          0.0060458851624517, \
          0.0060458851624517, \
          0.0060458851624517, \
          0.0136507771841729, \
          0.0136507771841729, \
          0.0136507771841729, \
          0.0136507771841729, \
          0.0136507771841729, \
          0.0136507771841729, \
          0.0136507771841729, \
          0.0136507771841729, \
          0.0136507771841729, \
          0.0136507771841729, \
          0.0136507771841729, \
          0.0136507771841729, \
          0.0061923846298526, \
          0.0061923846298526, \
          0.0061923846298526, \
          0.0061923846298526, \
          0.0061923846298526, \
          0.0061923846298526, \
          0.0061923846298526, \
          0.0061923846298526, \
          0.0061923846298526, \
          0.0061923846298526, \
          0.0061923846298526, \
          0.0061923846298526 ] )

  return x, y, z, w

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
      1,   5,   8,  11,  16, \
     28,  35,  46,  60,  85 ] )

  order = order_vec[p]

  return order

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
  prism_witherden_rule_test ( )
  timestamp ( )



