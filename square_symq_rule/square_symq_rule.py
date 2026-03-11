#! /usr/bin/env python3
#
def square_symq_rule_test ( ):

#*****************************************************************************80
#
## square_symq_rule_test() tests square_symq_rule().
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    16 July 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'square_symq_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test square_symq_rule().' )

  p = 5
  square_symq_rule_test01 ( p )

  p = 5
  square_symq_rule_test02 ( p )

  p_lo = 0
  p_hi = 20
  square_symq_rule_test03 ( p_lo, p_hi )
#
#  Terminate.
#
  print ( '' )
  print ( 'square_symq_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def square_symq_rule_test01 ( p ):

#*****************************************************************************80
#
## square_symq_rule_test01() prints a rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    16 July 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer p: the precision of the rule.
#
  import numpy as np

  print ( '' )
  print ( 'square_symq_rule_test01():' )
  print ( '  Symmetric quadrature rule for a square.' )
  print ( '  precision = ', p )

  n = rule_order ( p )
  x, y, w = square_symq ( p, n )

  print ( '' )
  print ( '     J  W       X       Y' )
  print ( '' )
  for j in range ( 0, n ):
    print ( '  %4d  %14.6g  %14.6g  %14.6g' % ( j, w[j], x[j], y[j] ) )

  w_sum = np.sum ( w )

  print ( '  Weight sum', w_sum )

  return

def square_symq_rule_test02 ( p ):

#*****************************************************************************80
#
## square_symq_rule_test02() tests a rule of precision P.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    16 July 2023
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer p: the precision of the rule.
#
  import numpy as np

  print ( '' )
  print ( 'square_symq_rule_test02():' )
  print ( '  Test the precision of a quadrature rule for the square.' )

  dim_num = 2
#
#  Retrieve the rule.
#
  n = rule_order ( p )
  x, y, w = square_symq ( p, n )
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

def square_symq_rule_test03 ( p_lo, p_hi ):

#*****************************************************************************80
#
## square_symq_rule_test03() tests absolute and relative precision.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    16 July 2023
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
  print ( 'square_symq_rule_test02():' )
  print ( '  Test the precision of a quadrature rule for the square.' )
  print ( '  Check rules of precision p =', p_lo, 'through', p_hi )
  print ( '  for error in approximating integrals of monomials.' )

  dim_num = 2

  print ( '' )
  print ( '              maximum                   maximum' )
  print ( '   p          absolute                  relative' )
  print ( '              error                     error' )
  print ( '' )

  for p in range ( p_lo, p_hi + 1 ):

    n = rule_order ( p )
    x, y, w = square_symq ( p, n )
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
#    with MORE = FALSE, set A = np.array ( [] ).  Thereafter, A should be the 
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
    a = np.array ( [] )
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

def rule00 ( n ):

#*****************************************************************************80
#
## rule00() returns the rule of degree 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
       0.00000000000000000E+00 ] )
  ys = np.array ( [ \
       0.00000000000000000E+00 ] )
  ws = np.array ( [ \
       0.28284271247461904E+01 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule01 ( n ):

#*****************************************************************************80
#
## rule01() returns the rule of degree 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
       0.00000000000000000E+00 ] )
  ys = np.array ( [ \
       0.00000000000000000E+00 ] )
  ws = np.array ( [ \
       0.28284271247461904E+01 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule02 ( n ):

#*****************************************************************************80
#
## rule02() returns the rule of degree 2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
   -0.5773502691896256E+00, \
    0.5773502691896260E+00, \
    0.5773502691896256E+00, \
   -0.5773502691896260E+00 ] )
  ys = np.array ( [ \
   -0.5773502691896260E+00, \
   -0.5773502691896256E+00, \
    0.5773502691896260E+00, \
    0.5773502691896256E+00 ] )
  ws = np.array ( [ \
    0.7071067811865476E+00, \
    0.7071067811865476E+00, \
    0.7071067811865476E+00, \
    0.7071067811865476E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule03 ( n ):

#*****************************************************************************80
#
## rule03() returns the rule of degree 3.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
   -0.5773502691896256E+00, \
    0.5773502691896260E+00, \
    0.5773502691896256E+00, \
   -0.5773502691896260E+00 ] )
  ys = np.array ( [ \
   -0.5773502691896260E+00, \
   -0.5773502691896256E+00, \
    0.5773502691896260E+00, \
    0.5773502691896256E+00 ] )
  ws = np.array ( [ \
    0.7071067811865476E+00, \
    0.7071067811865476E+00, \
    0.7071067811865476E+00, \
    0.7071067811865476E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule04 ( n ):

#*****************************************************************************80
#
## rule04() returns the rule of degree 4.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.3683480503448356E+00, \
   -0.3683480503448355E+00, \
    0.8881837963234579E+00, \
   -0.8881837963234579E+00, \
   -0.6849278434806340E+00, \
    0.6849278434806340E+00, \
    0.1035042199756803E-32 ] )
  ys = np.array ( [ \
   -0.8931142408116063E+00, \
    0.8931142408116063E+00, \
   -0.3800827242611582E+00, \
    0.3800827242611583E+00, \
   -0.6813275148988932E+00, \
    0.6813275148988932E+00, \
   -0.4874534345070689E-33 ] )
  ws = np.array ( [ \
    0.2922561796990344E+00, \
    0.2922561796990344E+00, \
    0.2970097006317383E+00, \
    0.2970097006317383E+00, \
    0.4208866642214383E+00, \
    0.4208866642214383E+00, \
    0.8081220356417685E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule05 ( n ):

#*****************************************************************************80
#
## rule05() returns the rule of degree 5.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.1775868202077551E-01, \
   -0.1775868202077539E-01, \
    0.7788710544649639E+00, \
   -0.7788710544649639E+00, \
   -0.7703781288541645E+00, \
    0.7703781288541645E+00, \
   -0.7490353914168658E-33 ] )
  ys = np.array ( [ \
   -0.9659285494001192E+00, \
    0.9659285494001192E+00, \
   -0.5715708301251639E+00, \
    0.5715708301251639E+00, \
   -0.5829672991828014E+00, \
    0.5829672991828014E+00, \
    0.1356144833394667E-33 ] )
  ws = np.array ( [ \
    0.2246199725165690E+00, \
    0.2246199725165690E+00, \
    0.3901817339168917E+00, \
    0.3901817339168917E+00, \
    0.3953508381187504E+00, \
    0.3953508381187504E+00, \
    0.8081220356417684E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule06 ( n ):

#*****************************************************************************80
#
## rule06() returns the rule of degree 6.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.4595981103653579E-16, \
    0.9258200997725515E+00, \
    0.6742045114073804E-16, \
   -0.9258200997725515E+00, \
   -0.3805544332083157E+00, \
    0.3805544332083157E+00, \
    0.3805544332083157E+00, \
   -0.3805544332083157E+00, \
   -0.8059797829185990E+00, \
    0.8059797829185988E+00, \
    0.8059797829185990E+00, \
   -0.8059797829185988E+00 ] )
  ys = np.array ( [ \
   -0.9258200997725515E+00, \
   -0.1073032005210112E-16, \
    0.9258200997725515E+00, \
    0.1241105822293750E-15, \
   -0.3805544332083157E+00, \
   -0.3805544332083157E+00, \
    0.3805544332083157E+00, \
    0.3805544332083157E+00, \
   -0.8059797829185988E+00, \
   -0.8059797829185990E+00, \
    0.8059797829185988E+00, \
    0.8059797829185990E+00 ] )
  ws = np.array ( [ \
    0.1711023816204485E+00, \
    0.1711023816204485E+00, \
    0.1711023816204485E+00, \
    0.1711023816204485E+00, \
    0.3681147816131979E+00, \
    0.3681147816131979E+00, \
    0.3681147816131979E+00, \
    0.3681147816131979E+00, \
    0.1678896179529011E+00, \
    0.1678896179529011E+00, \
    0.1678896179529011E+00, \
    0.1678896179529011E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule07 ( n ):

#*****************************************************************************80
#
## rule07() returns the rule of degree 7.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.4595981103653579E-16, \
    0.9258200997725515E+00, \
    0.6742045114073804E-16, \
   -0.9258200997725515E+00, \
   -0.3805544332083157E+00, \
    0.3805544332083157E+00, \
    0.3805544332083157E+00, \
   -0.3805544332083157E+00, \
   -0.8059797829185990E+00, \
    0.8059797829185988E+00, \
    0.8059797829185990E+00, \
   -0.8059797829185988E+00 ] )
  ys = np.array ( [ \
   -0.9258200997725515E+00, \
   -0.1073032005210112E-16, \
    0.9258200997725515E+00, \
    0.1241105822293750E-15, \
   -0.3805544332083157E+00, \
   -0.3805544332083157E+00, \
    0.3805544332083157E+00, \
    0.3805544332083157E+00, \
   -0.8059797829185988E+00, \
   -0.8059797829185990E+00, \
    0.8059797829185988E+00, \
    0.8059797829185990E+00 ] )
  ws = np.array ( [ \
    0.1711023816204485E+00, \
    0.1711023816204485E+00, \
    0.1711023816204485E+00, \
    0.1711023816204485E+00, \
    0.3681147816131979E+00, \
    0.3681147816131979E+00, \
    0.3681147816131979E+00, \
    0.3681147816131979E+00, \
    0.1678896179529011E+00, \
    0.1678896179529011E+00, \
    0.1678896179529011E+00, \
    0.1678896179529011E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule08 ( n ):

#*****************************************************************************80
#
## rule08() returns the rule of degree 8.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.6306801197316689E+00, \
    0.9688499663619776E+00, \
   -0.6306801197316687E+00, \
   -0.9688499663619776E+00, \
   -0.7502770999789002E+00, \
    0.9279616459595696E+00, \
    0.7502770999789005E+00, \
   -0.9279616459595696E+00, \
   -0.7620832819261708E-01, \
    0.8526157293336623E+00, \
    0.7620832819261719E-01, \
   -0.8526157293336623E+00, \
   -0.5237358202144292E+00, \
    0.4533398211356472E+00, \
    0.5237358202144292E+00, \
   -0.4533398211356471E+00, \
    0.1018964154952896E-32 ] )
  ys = np.array ( [ \
   -0.9688499663619776E+00, \
    0.6306801197316688E+00, \
    0.9688499663619776E+00, \
   -0.6306801197316686E+00, \
   -0.9279616459595696E+00, \
   -0.7502770999789004E+00, \
    0.9279616459595696E+00, \
    0.7502770999789006E+00, \
   -0.8526157293336623E+00, \
   -0.7620832819261714E-01, \
    0.8526157293336623E+00, \
    0.7620832819261725E-01, \
   -0.4533398211356472E+00, \
   -0.5237358202144292E+00, \
    0.4533398211356471E+00, \
    0.5237358202144292E+00, \
   -0.7403196379681869E-32 ] )
  ws = np.array ( [ \
    0.6284721101179121E-01, \
    0.6284721101179121E-01, \
    0.6284721101179121E-01, \
    0.6284721101179121E-01, \
    0.7926638883415160E-01, \
    0.7926638883415160E-01, \
    0.7926638883415160E-01, \
    0.7926638883415160E-01, \
    0.1902480253324004E+00, \
    0.1902480253324004E+00, \
    0.1902480253324004E+00, \
    0.1902480253324004E+00, \
    0.2816282136297291E+00, \
    0.2816282136297291E+00, \
    0.2816282136297291E+00, \
    0.2816282136297291E+00, \
    0.3724677695139019E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule09 ( n ):

#*****************************************************************************80
#
## rule09() returns the rule of degree 9.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.6306801197316689E+00, \
    0.9688499663619776E+00, \
   -0.6306801197316687E+00, \
   -0.9688499663619776E+00, \
   -0.7502770999789002E+00, \
    0.9279616459595696E+00, \
    0.7502770999789005E+00, \
   -0.9279616459595696E+00, \
   -0.7620832819261708E-01, \
    0.8526157293336623E+00, \
    0.7620832819261719E-01, \
   -0.8526157293336623E+00, \
   -0.5237358202144292E+00, \
    0.4533398211356472E+00, \
    0.5237358202144292E+00, \
   -0.4533398211356471E+00, \
    0.1018964154952896E-32 ] )
  ys = np.array ( [ \
   -0.9688499663619776E+00, \
    0.6306801197316688E+00, \
    0.9688499663619776E+00, \
   -0.6306801197316686E+00, \
   -0.9279616459595696E+00, \
   -0.7502770999789004E+00, \
    0.9279616459595696E+00, \
    0.7502770999789006E+00, \
   -0.8526157293336623E+00, \
   -0.7620832819261714E-01, \
    0.8526157293336623E+00, \
    0.7620832819261725E-01, \
   -0.4533398211356472E+00, \
   -0.5237358202144292E+00, \
    0.4533398211356471E+00, \
    0.5237358202144292E+00, \
   -0.7403196379681869E-32 ] )
  ws = np.array ( [ \
    0.6284721101179121E-01, \
    0.6284721101179121E-01, \
    0.6284721101179121E-01, \
    0.6284721101179121E-01, \
    0.7926638883415160E-01, \
    0.7926638883415160E-01, \
    0.7926638883415160E-01, \
    0.7926638883415160E-01, \
    0.1902480253324004E+00, \
    0.1902480253324004E+00, \
    0.1902480253324004E+00, \
    0.1902480253324004E+00, \
    0.2816282136297291E+00, \
    0.2816282136297291E+00, \
    0.2816282136297291E+00, \
    0.2816282136297291E+00, \
    0.3724677695139019E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule10 ( n ):

#*****************************************************************************80
#
## rule10() returns the rule of degree 10.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
   -0.6980761045495689E+00, \
    0.9826392235408554E+00, \
    0.6980761045495691E+00, \
   -0.9826392235408554E+00, \
    0.8257758359029634E+00, \
    0.9394863828167371E+00, \
   -0.8257758359029632E+00, \
   -0.9394863828167371E+00, \
    0.1885861387186400E+00, \
    0.9535395282015321E+00, \
   -0.1885861387186399E+00, \
   -0.9535395282015321E+00, \
   -0.7120019130753369E+00, \
    0.5253202503645465E+00, \
    0.7120019130753369E+00, \
   -0.5253202503645465E+00, \
   -0.3156234329152560E+00, \
    0.8125205483048131E+00, \
    0.3156234329152561E+00, \
   -0.8125205483048131E+00, \
   -0.4248472488486695E+00, \
    0.4165807191202114E-01, \
    0.4248472488486695E+00, \
   -0.4165807191202109E-01 ] )
  ys = np.array ( [ \
   -0.9826392235408554E+00, \
   -0.6980761045495690E+00, \
    0.9826392235408554E+00, \
    0.6980761045495693E+00, \
   -0.9394863828167371E+00, \
    0.8257758359029633E+00, \
    0.9394863828167371E+00, \
   -0.8257758359029631E+00, \
   -0.9535395282015321E+00, \
    0.1885861387186400E+00, \
    0.9535395282015321E+00, \
   -0.1885861387186399E+00, \
   -0.5253202503645465E+00, \
   -0.7120019130753369E+00, \
    0.5253202503645465E+00, \
    0.7120019130753369E+00, \
   -0.8125205483048131E+00, \
   -0.3156234329152560E+00, \
    0.8125205483048131E+00, \
    0.3156234329152561E+00, \
   -0.4165807191202117E-01, \
   -0.4248472488486695E+00, \
    0.4165807191202112E-01, \
    0.4248472488486695E+00 ] )
  ws = np.array ( [ \
    0.3395580740305119E-01, \
    0.3395580740305119E-01, \
    0.3395580740305119E-01, \
    0.3395580740305119E-01, \
    0.4671948489426219E-01, \
    0.4671948489426219E-01, \
    0.4671948489426219E-01, \
    0.4671948489426219E-01, \
    0.6886285066821875E-01, \
    0.6886285066821875E-01, \
    0.6886285066821875E-01, \
    0.6886285066821875E-01, \
    0.1595417182608940E+00, \
    0.1595417182608940E+00, \
    0.1595417182608940E+00, \
    0.1595417182608940E+00, \
    0.1497202089079447E+00, \
    0.1497202089079447E+00, \
    0.1497202089079447E+00, \
    0.1497202089079447E+00, \
    0.2483067110521768E+00, \
    0.2483067110521768E+00, \
    0.2483067110521768E+00, \
    0.2483067110521768E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule11 ( n ):

#*****************************************************************************80
#
## rule11() returns the rule of degree 11.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.1885861387186414E+00, \
    0.9535395282015320E+00, \
   -0.1885861387186413E+00, \
   -0.9535395282015320E+00, \
   -0.6980761045495679E+00, \
    0.9826392235408555E+00, \
    0.6980761045495681E+00, \
   -0.9826392235408555E+00, \
   -0.9394863828167370E+00, \
    0.8257758359029639E+00, \
    0.9394863828167370E+00, \
   -0.8257758359029637E+00, \
   -0.7120019130753364E+00, \
    0.5253202503645475E+00, \
    0.7120019130753364E+00, \
   -0.5253202503645475E+00, \
   -0.3156234329152547E+00, \
    0.8125205483048131E+00, \
    0.3156234329152548E+00, \
   -0.8125205483048131E+00, \
   -0.4248472488486694E+00, \
    0.4165807191202203E-01, \
    0.4248472488486694E+00, \
   -0.4165807191202197E-01 ] )
  ys = np.array ( [ \
   -0.9535395282015320E+00, \
    0.1885861387186414E+00, \
    0.9535395282015320E+00, \
   -0.1885861387186413E+00, \
   -0.9826392235408555E+00, \
   -0.6980761045495680E+00, \
    0.9826392235408555E+00, \
    0.6980761045495683E+00, \
   -0.8257758359029640E+00, \
   -0.9394863828167370E+00, \
    0.8257758359029638E+00, \
    0.9394863828167370E+00, \
   -0.5253202503645475E+00, \
   -0.7120019130753364E+00, \
    0.5253202503645475E+00, \
    0.7120019130753364E+00, \
   -0.8125205483048131E+00, \
   -0.3156234329152547E+00, \
    0.8125205483048131E+00, \
    0.3156234329152549E+00, \
   -0.4165807191202205E-01, \
   -0.4248472488486694E+00, \
    0.4165807191202200E-01, \
    0.4248472488486694E+00 ] )
  ws = np.array ( [ \
    0.6886285066821880E-01, \
    0.6886285066821880E-01, \
    0.6886285066821880E-01, \
    0.6886285066821880E-01, \
    0.3395580740305121E-01, \
    0.3395580740305121E-01, \
    0.3395580740305121E-01, \
    0.3395580740305121E-01, \
    0.4671948489426224E-01, \
    0.4671948489426224E-01, \
    0.4671948489426224E-01, \
    0.4671948489426224E-01, \
    0.1595417182608939E+00, \
    0.1595417182608939E+00, \
    0.1595417182608939E+00, \
    0.1595417182608939E+00, \
    0.1497202089079448E+00, \
    0.1497202089079448E+00, \
    0.1497202089079448E+00, \
    0.1497202089079448E+00, \
    0.2483067110521767E+00, \
    0.2483067110521767E+00, \
    0.2483067110521767E+00, \
    0.2483067110521767E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule12 ( n ):

#*****************************************************************************80
#
## rule12() returns the rule of degree 12.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
   -0.9572976997863073E+00, \
    0.8595560056416388E+00, \
    0.9572976997863073E+00, \
   -0.8595560056416386E+00, \
   -0.7788097115544194E+00, \
    0.9834866824398721E+00, \
    0.7788097115544196E+00, \
   -0.9834866824398721E+00, \
   -0.4758086252182758E+00, \
    0.8500766736997486E+00, \
    0.4758086252182759E+00, \
   -0.8500766736997486E+00, \
   -0.7558053565720815E+00, \
    0.6478216371870107E+00, \
    0.7558053565720815E+00, \
   -0.6478216371870107E+00, \
   -0.3427165560404068E+00, \
    0.4093045616940387E+00, \
    0.3427165560404068E+00, \
   -0.4093045616940387E+00, \
   -0.1381834598624653E+00, \
    0.9589251702875349E+00, \
    0.1381834598624654E+00, \
   -0.9589251702875349E+00, \
    0.7074150899644485E-01, \
    0.6962500784917494E+00, \
   -0.7074150899644477E-01, \
   -0.6962500784917494E+00, \
    0.3907362161294610E+00, \
    0.9413272258729252E+00, \
   -0.3907362161294609E+00, \
   -0.9413272258729252E+00, \
   -0.3126032252245169E-31 ] )
  ys = np.array ( [ \
   -0.8595560056416389E+00, \
   -0.9572976997863073E+00, \
    0.8595560056416387E+00, \
    0.9572976997863073E+00, \
   -0.9834866824398721E+00, \
   -0.7788097115544195E+00, \
    0.9834866824398721E+00, \
    0.7788097115544197E+00, \
   -0.8500766736997486E+00, \
   -0.4758086252182758E+00, \
    0.8500766736997486E+00, \
    0.4758086252182759E+00, \
   -0.6478216371870107E+00, \
   -0.7558053565720815E+00, \
    0.6478216371870107E+00, \
    0.7558053565720815E+00, \
   -0.4093045616940387E+00, \
   -0.3427165560404068E+00, \
    0.4093045616940387E+00, \
    0.3427165560404068E+00, \
   -0.9589251702875349E+00, \
   -0.1381834598624653E+00, \
    0.9589251702875349E+00, \
    0.1381834598624654E+00, \
   -0.6962500784917494E+00, \
    0.7074150899644481E-01, \
    0.6962500784917494E+00, \
   -0.7074150899644473E-01, \
   -0.9413272258729252E+00, \
    0.3907362161294610E+00, \
    0.9413272258729252E+00, \
   -0.3907362161294609E+00, \
   -0.1114446878059780E-31 ] )
  ws = np.array ( [ \
    0.2699339218118220E-01, \
    0.2699339218118220E-01, \
    0.2699339218118220E-01, \
    0.2699339218118220E-01, \
    0.2120743264134161E-01, \
    0.2120743264134161E-01, \
    0.2120743264134161E-01, \
    0.2120743264134161E-01, \
    0.8403587015611028E-01, \
    0.8403587015611028E-01, \
    0.8403587015611028E-01, \
    0.8403587015611028E-01, \
    0.9175668641747105E-01, \
    0.9175668641747105E-01, \
    0.9175668641747105E-01, \
    0.9175668641747105E-01, \
    0.1816350488471703E+00, \
    0.1816350488471703E+00, \
    0.1816350488471703E+00, \
    0.1816350488471703E+00, \
    0.4272687338421145E-01, \
    0.4272687338421145E-01, \
    0.4272687338421145E-01, \
    0.4272687338421145E-01, \
    0.1508552789574408E+00, \
    0.1508552789574408E+00, \
    0.1508552789574408E+00, \
    0.1508552789574408E+00, \
    0.5479564090947486E-01, \
    0.5479564090947486E-01, \
    0.5479564090947486E-01, \
    0.5479564090947486E-01, \
    0.2124022307685798E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule13 ( n ):

#*****************************************************************************80
#
## rule13() returns the rule of degree 13.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
   -0.9572976997863074E+00, \
    0.8595560056416388E+00, \
    0.9572976997863074E+00, \
   -0.8595560056416386E+00, \
   -0.7788097115544195E+00, \
    0.9834866824398722E+00, \
    0.7788097115544197E+00, \
   -0.9834866824398722E+00, \
   -0.4758086252182752E+00, \
    0.8500766736997490E+00, \
    0.4758086252182753E+00, \
   -0.8500766736997490E+00, \
    0.3907362161294613E+00, \
    0.9413272258729251E+00, \
   -0.3907362161294612E+00, \
   -0.9413272258729251E+00, \
   -0.1381834598624646E+00, \
    0.9589251702875351E+00, \
    0.1381834598624647E+00, \
   -0.9589251702875351E+00, \
    0.6478216371870111E+00, \
    0.7558053565720809E+00, \
   -0.6478216371870111E+00, \
   -0.7558053565720809E+00, \
    0.7074150899644462E-01, \
    0.6962500784917495E+00, \
   -0.7074150899644453E-01, \
   -0.6962500784917495E+00, \
   -0.3427165560404070E+00, \
    0.4093045616940387E+00, \
    0.3427165560404070E+00, \
   -0.4093045616940387E+00, \
   -0.7375869198366919E-30 ] )
  ys = np.array ( [ \
   -0.8595560056416389E+00, \
   -0.9572976997863074E+00, \
    0.8595560056416387E+00, \
    0.9572976997863074E+00, \
   -0.9834866824398722E+00, \
   -0.7788097115544196E+00, \
    0.9834866824398722E+00, \
    0.7788097115544198E+00, \
   -0.8500766736997490E+00, \
   -0.4758086252182752E+00, \
    0.8500766736997490E+00, \
    0.4758086252182753E+00, \
   -0.9413272258729251E+00, \
    0.3907362161294612E+00, \
    0.9413272258729251E+00, \
   -0.3907362161294611E+00, \
   -0.9589251702875351E+00, \
   -0.1381834598624647E+00, \
    0.9589251702875351E+00, \
    0.1381834598624648E+00, \
   -0.7558053565720809E+00, \
    0.6478216371870111E+00, \
    0.7558053565720809E+00, \
   -0.6478216371870111E+00, \
   -0.6962500784917495E+00, \
    0.7074150899644457E-01, \
    0.6962500784917495E+00, \
   -0.7074150899644449E-01, \
   -0.4093045616940387E+00, \
   -0.3427165560404070E+00, \
    0.4093045616940387E+00, \
    0.3427165560404070E+00, \
   -0.6522588594679827E-30 ] )
  ws = np.array ( [ \
    0.2699339218118215E-01, \
    0.2699339218118215E-01, \
    0.2699339218118215E-01, \
    0.2699339218118215E-01, \
    0.2120743264134157E-01, \
    0.2120743264134157E-01, \
    0.2120743264134157E-01, \
    0.2120743264134157E-01, \
    0.8403587015611026E-01, \
    0.8403587015611026E-01, \
    0.8403587015611026E-01, \
    0.8403587015611026E-01, \
    0.5479564090947502E-01, \
    0.5479564090947502E-01, \
    0.5479564090947502E-01, \
    0.5479564090947502E-01, \
    0.4272687338421139E-01, \
    0.4272687338421139E-01, \
    0.4272687338421139E-01, \
    0.4272687338421139E-01, \
    0.9175668641747110E-01, \
    0.9175668641747110E-01, \
    0.9175668641747110E-01, \
    0.9175668641747110E-01, \
    0.1508552789574409E+00, \
    0.1508552789574409E+00, \
    0.1508552789574409E+00, \
    0.1508552789574409E+00, \
    0.1816350488471704E+00, \
    0.1816350488471704E+00, \
    0.1816350488471704E+00, \
    0.1816350488471704E+00, \
    0.2124022307685795E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule14 ( n ):

#*****************************************************************************80
#
## rule14() returns the rule of degree 14.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
   -0.6714783701550190E+00, \
    0.9859876542016408E+00, \
    0.6714783701550192E+00, \
   -0.9859876542016408E+00, \
   -0.9318844245957986E+00, \
    0.9382770335701854E+00, \
    0.9318844245957988E+00, \
   -0.9382770335701852E+00, \
    0.6776977793098985E+00, \
    0.9773357693271729E+00, \
   -0.6776977793098983E+00, \
   -0.9773357693271729E+00, \
    0.4073679548284153E+00, \
    0.8648066658739809E+00, \
   -0.4073679548284151E+00, \
   -0.8648066658739809E+00, \
    0.6518175069036650E-01, \
    0.9759935658724420E+00, \
   -0.6518175069036639E-01, \
   -0.9759935658724420E+00, \
   -0.7473119631960774E+00, \
    0.7834652444128232E+00, \
    0.7473119631960774E+00, \
   -0.7834652444128232E+00, \
    0.1328305205898269E+00, \
    0.6241210323620054E+00, \
   -0.1328305205898269E+00, \
   -0.6241210323620054E+00, \
   -0.4781379108769722E+00, \
    0.5501448214169192E+00, \
    0.4781379108769723E+00, \
   -0.5501448214169192E+00, \
   -0.1803286643164523E+00, \
    0.8053335984690123E+00, \
    0.1803286643164524E+00, \
   -0.8053335984690123E+00, \
   -0.4134760830488010E+00, \
    0.9261965849285028E+00, \
    0.4134760830488011E+00, \
   -0.9261965849285028E+00, \
   -0.1307639250027494E+00, \
    0.2910908755606336E+00, \
    0.1307639250027494E+00, \
   -0.2910908755606336E+00 ] )
  ys = np.array ( [ \
   -0.9859876542016408E+00, \
   -0.6714783701550191E+00, \
    0.9859876542016408E+00, \
    0.6714783701550193E+00, \
   -0.9382770335701855E+00, \
   -0.9318844245957987E+00, \
    0.9382770335701853E+00, \
    0.9318844245957989E+00, \
   -0.9773357693271729E+00, \
    0.6776977793098984E+00, \
    0.9773357693271729E+00, \
   -0.6776977793098982E+00, \
   -0.8648066658739809E+00, \
    0.4073679548284152E+00, \
    0.8648066658739809E+00, \
   -0.4073679548284151E+00, \
   -0.9759935658724420E+00, \
    0.6518175069036644E-01, \
    0.9759935658724420E+00, \
   -0.6518175069036633E-01, \
   -0.7834652444128232E+00, \
   -0.7473119631960774E+00, \
    0.7834652444128232E+00, \
    0.7473119631960774E+00, \
   -0.6241210323620054E+00, \
    0.1328305205898269E+00, \
    0.6241210323620054E+00, \
   -0.1328305205898269E+00, \
   -0.5501448214169192E+00, \
   -0.4781379108769723E+00, \
    0.5501448214169192E+00, \
    0.4781379108769724E+00, \
   -0.8053335984690123E+00, \
   -0.1803286643164524E+00, \
    0.8053335984690123E+00, \
    0.1803286643164525E+00, \
   -0.9261965849285028E+00, \
   -0.4134760830488011E+00, \
    0.9261965849285028E+00, \
    0.4134760830488012E+00, \
   -0.2910908755606336E+00, \
   -0.1307639250027494E+00, \
    0.2910908755606336E+00, \
    0.1307639250027494E+00 ] )
  ws = np.array ( [ \
    0.1410384661573933E-01, \
    0.1410384661573933E-01, \
    0.1410384661573933E-01, \
    0.1410384661573933E-01, \
    0.1896652423210582E-01, \
    0.1896652423210582E-01, \
    0.1896652423210582E-01, \
    0.1896652423210582E-01, \
    0.2088141025507279E-01, \
    0.2088141025507279E-01, \
    0.2088141025507279E-01, \
    0.2088141025507279E-01, \
    0.7331394692154988E-01, \
    0.7331394692154988E-01, \
    0.7331394692154988E-01, \
    0.7331394692154988E-01, \
    0.3078002143226069E-01, \
    0.3078002143226069E-01, \
    0.3078002143226069E-01, \
    0.3078002143226069E-01, \
    0.6693059666394105E-01, \
    0.6693059666394105E-01, \
    0.6693059666394105E-01, \
    0.6693059666394105E-01, \
    0.1122840307920054E+00, \
    0.1122840307920054E+00, \
    0.1122840307920054E+00, \
    0.1122840307920054E+00, \
    0.1159261595200915E+00, \
    0.1159261595200915E+00, \
    0.1159261595200915E+00, \
    0.1159261595200915E+00, \
    0.7346051498025349E-01, \
    0.7346051498025349E-01, \
    0.7346051498025349E-01, \
    0.7346051498025349E-01, \
    0.4099703937729331E-01, \
    0.4099703937729331E-01, \
    0.4099703937729331E-01, \
    0.4099703937729331E-01, \
    0.1394626903962344E+00, \
    0.1394626903962344E+00, \
    0.1394626903962344E+00, \
    0.1394626903962344E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule15 ( n ):

#*****************************************************************************80
#
## rule15() returns the rule of degree 15.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 July 2014
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.7749527857778351E+00, \
    0.9885448991378063E+00, \
   -0.7749527857778349E+00, \
   -0.9885448991378063E+00, \
   -0.9070374303651182E+00, \
    0.9571446613308432E+00, \
    0.9070374303651184E+00, \
   -0.9571446613308430E+00, \
   -0.4303978306869286E+00, \
    0.9769578054468787E+00, \
    0.4303978306869287E+00, \
   -0.9769578054468787E+00, \
   -0.9756646723906326E+00, \
    0.1107064048513496E+00, \
    0.9756646723906326E+00, \
   -0.1107064048513495E+00, \
   -0.7388921437312957E+00, \
    0.7868610204187212E+00, \
    0.7388921437312957E+00, \
   -0.7868610204187212E+00, \
    0.1995220876718269E+00, \
    0.6659287668239546E+00, \
   -0.1995220876718268E+00, \
   -0.6659287668239546E+00, \
   -0.1934983412061240E+00, \
    0.8412271039808018E+00, \
    0.1934983412061241E+00, \
   -0.8412271039808018E+00, \
    0.4882189227791580E+00, \
    0.8922368778153702E+00, \
   -0.4882189227791579E+00, \
   -0.8922368778153702E+00, \
   -0.5772265461040059E+00, \
    0.9526539504944950E+00, \
    0.5772265461040061E+00, \
   -0.9526539504944950E+00, \
   -0.4474426063114782E+00, \
    0.5675455860909890E+00, \
    0.4474426063114783E+00, \
   -0.5675455860909890E+00, \
   -0.7044956995149931E-01, \
    0.3256679896817100E+00, \
    0.7044956995149934E-01, \
   -0.3256679896817100E+00 ] )
  ys = np.array ( [ \
   -0.9885448991378063E+00, \
    0.7749527857778350E+00, \
    0.9885448991378063E+00, \
   -0.7749527857778348E+00, \
   -0.9571446613308433E+00, \
   -0.9070374303651183E+00, \
    0.9571446613308431E+00, \
    0.9070374303651185E+00, \
   -0.9769578054468787E+00, \
   -0.4303978306869286E+00, \
    0.9769578054468787E+00, \
    0.4303978306869287E+00, \
   -0.1107064048513496E+00, \
   -0.9756646723906326E+00, \
    0.1107064048513495E+00, \
    0.9756646723906326E+00, \
   -0.7868610204187212E+00, \
   -0.7388921437312957E+00, \
    0.7868610204187212E+00, \
    0.7388921437312957E+00, \
   -0.6659287668239546E+00, \
    0.1995220876718268E+00, \
    0.6659287668239546E+00, \
   -0.1995220876718268E+00, \
   -0.8412271039808018E+00, \
   -0.1934983412061240E+00, \
    0.8412271039808018E+00, \
    0.1934983412061241E+00, \
   -0.8922368778153702E+00, \
    0.4882189227791580E+00, \
    0.8922368778153702E+00, \
   -0.4882189227791578E+00, \
   -0.9526539504944950E+00, \
   -0.5772265461040060E+00, \
    0.9526539504944950E+00, \
    0.5772265461040063E+00, \
   -0.5675455860909890E+00, \
   -0.4474426063114783E+00, \
    0.5675455860909890E+00, \
    0.4474426063114784E+00, \
   -0.3256679896817100E+00, \
   -0.7044956995149933E-01, \
    0.3256679896817100E+00, \
    0.7044956995149936E-01 ] )
  ws = np.array ( [ \
    0.1443015463807196E-01, \
    0.1443015463807196E-01, \
    0.1443015463807196E-01, \
    0.1443015463807196E-01, \
    0.1816242330920956E-01, \
    0.1816242330920956E-01, \
    0.1816242330920956E-01, \
    0.1816242330920956E-01, \
    0.1290815898308381E-01, \
    0.1290815898308381E-01, \
    0.1290815898308381E-01, \
    0.1290815898308381E-01, \
    0.3010764365372140E-01, \
    0.3010764365372140E-01, \
    0.3010764365372140E-01, \
    0.3010764365372140E-01, \
    0.6540469907131932E-01, \
    0.6540469907131932E-01, \
    0.6540469907131932E-01, \
    0.6540469907131932E-01, \
    0.1197895531736646E+00, \
    0.1197895531736646E+00, \
    0.1197895531736646E+00, \
    0.1197895531736646E+00, \
    0.8473841548096289E-01, \
    0.8473841548096289E-01, \
    0.8473841548096289E-01, \
    0.8473841548096289E-01, \
    0.6453833756714425E-01, \
    0.6453833756714425E-01, \
    0.6453833756714425E-01, \
    0.6453833756714425E-01, \
    0.2403055376316494E-01, \
    0.2403055376316494E-01, \
    0.2403055376316494E-01, \
    0.2403055376316494E-01, \
    0.1196130510491228E+00, \
    0.1196130510491228E+00, \
    0.1196130510491228E+00, \
    0.1196130510491228E+00, \
    0.1533837904970821E+00, \
    0.1533837904970821E+00, \
    0.1533837904970821E+00, \
    0.1533837904970821E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule16 ( n ):

#*****************************************************************************80
#
## rule16() returns the rule of degree 16.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
    0.7331873192446229E+00, \
   -0.7331873192446227E+00, \
   -0.9811278880414770E+00, \
    0.9811278880414772E+00, \
   -0.8004995596996590E+00, \
    0.8004995596996592E+00, \
    0.2935594202060772E+00, \
   -0.2935594202060772E+00, \
    0.5019013651861420E+00, \
   -0.5019013651861418E+00, \
   -0.9240427888147712E+00, \
    0.9240427888147712E+00, \
   -0.7321159842417640E+00, \
    0.7321159842417640E+00, \
    0.9107218705094187E+00, \
   -0.9107218705094184E+00, \
    0.9799531606782582E+00, \
   -0.9799531606782582E+00, \
   -0.2536359436096021E+00, \
    0.2536359436096021E+00, \
    0.8800049697526030E+00, \
   -0.8800049697526030E+00, \
    0.7136219272623606E+00, \
   -0.7136219272623606E+00, \
    0.5185051092186185E+00, \
   -0.5185051092186185E+00, \
    0.9890262305049052E+00, \
   -0.9890262305049052E+00, \
    0.9865971248382277E+00, \
   -0.9865971248382277E+00, \
    0.4087785918187709E-01, \
   -0.4087785918187702E-01, \
    0.9650604144351506E+00, \
   -0.9650604144351506E+00, \
   -0.5228670170578392E+00, \
    0.5228670170578394E+00, \
   -0.2304316370092423E+00, \
    0.2304316370092424E+00, \
    0.7381821882135022E+00, \
   -0.7381821882135022E+00, \
   -0.4979206093242921E+00, \
    0.4979206093242922E+00, \
    0.8494669121845019E+00, \
   -0.8494669121845019E+00, \
    0.4390176422841324E+00, \
   -0.4390176422841323E+00, \
    0.1590601194183188E+00, \
   -0.1590601194183187E+00, \
    0.8973818517920210E+00, \
   -0.8973818517920210E+00, \
    0.6726312443333152E+00, \
   -0.6726312443333152E+00, \
   -0.1686064273871127E+00, \
    0.1686064273871128E+00, \
   -0.3548241530243386E-18 ] )
  ys = np.array ( [ \
   -0.9711078221435576E+00, \
    0.9711078221435576E+00, \
   -0.9668551959097115E+00, \
    0.9668551959097113E+00, \
   -0.9746926011666336E+00, \
    0.9746926011666336E+00, \
   -0.3231309208576288E+00, \
    0.3231309208576288E+00, \
   -0.9765444785368099E+00, \
    0.9765444785368099E+00, \
   -0.8490306235166675E+00, \
    0.8490306235166672E+00, \
   -0.7537198042004623E+00, \
    0.7537198042004623E+00, \
   -0.9737587969123404E+00, \
    0.9737587969123406E+00, \
   -0.3822148312292263E+00, \
    0.3822148312292264E+00, \
   -0.2988363050086515E+00, \
    0.2988363050086515E+00, \
    0.4849608774128832E+00, \
   -0.4849608774128831E+00, \
    0.2492237020321146E+00, \
   -0.2492237020321144E+00, \
   -0.3504141436316342E-01, \
    0.3504141436316349E-01, \
    0.6278936489285102E+00, \
   -0.6278936489285100E+00, \
   -0.8591476119499135E+00, \
    0.8591476119499137E+00, \
   -0.5892598635566724E+00, \
    0.5892598635566724E+00, \
    0.1438346146728415E+00, \
   -0.1438346146728414E+00, \
   -0.9289486752701194E+00, \
    0.9289486752701194E+00, \
   -0.8028060773786958E+00, \
    0.8028060773786958E+00, \
   -0.8651144139342870E+00, \
    0.8651144139342870E+00, \
   -0.5653829126627348E+00, \
    0.5653829126627348E+00, \
   -0.1574661586091270E+00, \
    0.1574661586091272E+00, \
   -0.7312745784466166E+00, \
    0.7312745784466166E+00, \
   -0.9115177107109407E+00, \
    0.9115177107109407E+00, \
   -0.6626783799774586E+00, \
    0.6626783799774586E+00, \
   -0.4696061222418765E+00, \
    0.4696061222418766E+00, \
   -0.9939228673343959E+00, \
    0.9939228673343959E+00, \
    0.3228625474392587E-19 ] )
  ws = np.array ( [ \
    0.3224472434909546E-02, \
    0.3224472434909546E-02, \
    0.4080157527921578E-02, \
    0.4080157527921578E-02, \
    0.1406321867924724E-01, \
    0.1406321867924724E-01, \
    0.1094478053582958E+00, \
    0.1094478053582958E+00, \
    0.2046021623250057E-01, \
    0.2046021623250057E-01, \
    0.2244481290183435E-01, \
    0.2244481290183435E-01, \
    0.5310357585578484E-01, \
    0.5310357585578484E-01, \
    0.1049750419840204E-01, \
    0.1049750419840204E-01, \
    0.2100735514277743E-01, \
    0.2100735514277743E-01, \
    0.1140510361065565E+00, \
    0.1140510361065565E+00, \
    0.4811709451294231E-01, \
    0.4811709451294231E-01, \
    0.7994419804097108E-01, \
    0.7994419804097108E-01, \
    0.1010005451633049E+00, \
    0.1010005451633049E+00, \
    0.1204195881877324E-01, \
    0.1204195881877324E-01, \
    0.9474459024829298E-02, \
    0.9474459024829298E-02, \
    0.1005514424347678E+00, \
    0.1005514424347678E+00, \
    0.3161642787539286E-01, \
    0.3161642787539286E-01, \
    0.3963833050663004E-01, \
    0.3963833050663004E-01, \
    0.7350586661049985E-01, \
    0.7350586661049985E-01, \
    0.4319417861510279E-01, \
    0.4319417861510279E-01, \
    0.8810251098693814E-01, \
    0.8810251098693814E-01, \
    0.6864316028539075E-01, \
    0.6864316028539075E-01, \
    0.8257746135731812E-01, \
    0.8257746135731812E-01, \
    0.5439632620644287E-01, \
    0.5439632620644287E-01, \
    0.4386704732153978E-01, \
    0.4386704732153978E-01, \
    0.8808225769982879E-01, \
    0.8808225769982879E-01, \
    0.1534893259270625E-01, \
    0.1534893259270625E-01, \
    0.1234624197629746E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule17 ( n ):

#*****************************************************************************80
#
## rule17() returns the rule of degree 17.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
   -0.7710386602263628E+00, \
    0.7710386602263630E+00, \
    0.9803457456469387E+00, \
   -0.9803457456469384E+00, \
   -0.2292639639675523E+00, \
    0.2292639639675524E+00, \
    0.4847176019505991E-03, \
   -0.4847176019504780E-03, \
   -0.6189416389750175E+00, \
    0.6189416389750177E+00, \
    0.9587315519802511E+00, \
   -0.9587315519802511E+00, \
    0.8409306922533750E+00, \
   -0.8409306922533748E+00, \
   -0.4308042054877432E+00, \
    0.4308042054877433E+00, \
    0.4761431266211590E+00, \
   -0.4761431266211589E+00, \
    0.8651144531733139E+00, \
   -0.8651144531733139E+00, \
    0.9846617345267017E+00, \
   -0.9846617345267017E+00, \
   -0.7981639404863030E+00, \
    0.7981639404863030E+00, \
    0.6877591943414725E+00, \
   -0.6877591943414725E+00, \
   -0.3038305486106544E+00, \
    0.3038305486106544E+00, \
    0.9852576255116258E+00, \
   -0.9852576255116258E+00, \
    0.9853756930046446E+00, \
   -0.9853756930046446E+00, \
    0.7024672194580522E+00, \
   -0.7024672194580522E+00, \
    0.4589513024499020E+00, \
   -0.4589513024499019E+00, \
   -0.5838938372432102E+00, \
    0.5838938372432102E+00, \
    0.4855363777625971E+00, \
   -0.4855363777625971E+00, \
    0.1909552287968119E+00, \
   -0.1909552287968118E+00, \
    0.1970910744873101E+00, \
   -0.1970910744873101E+00, \
    0.9070140000742543E+00, \
   -0.9070140000742543E+00, \
   -0.9370706813548184E+00, \
    0.9370706813548186E+00, \
   -0.1024098809482286E+00, \
    0.1024098809482287E+00, \
    0.9018657853563646E+00, \
   -0.9018657853563646E+00, \
    0.7422255782894629E+00, \
   -0.7422255782894629E+00, \
   -0.1975779250586182E-19 ] )
  ys = np.array ( [ \
   -0.9187170657318696E+00, \
    0.9187170657318696E+00, \
   -0.9679135253250817E+00, \
    0.9679135253250819E+00, \
   -0.9437800394025085E+00, \
    0.9437800394025085E+00, \
   -0.9886578344699537E+00, \
    0.9886578344699537E+00, \
   -0.9803491213417113E+00, \
    0.9803491213417113E+00, \
   -0.8226737868824753E+00, \
    0.8226737868824755E+00, \
   -0.9649601466712245E+00, \
    0.9649601466712245E+00, \
   -0.8370492275539414E+00, \
    0.8370492275539414E+00, \
   -0.9716943047473653E+00, \
    0.9716943047473653E+00, \
   -0.6326447362896030E+00, \
    0.6326447362896030E+00, \
    0.2029425559112923E+00, \
   -0.2029425559112922E+00, \
   -0.7906135688735062E+00, \
    0.7906135688735062E+00, \
   -0.8442560578129694E+00, \
    0.8442560578129694E+00, \
   -0.3117615836793495E+00, \
    0.3117615836793495E+00, \
    0.7701659795648228E+00, \
   -0.7701659795648226E+00, \
   -0.4379432170880169E+00, \
    0.4379432170880170E+00, \
   -0.3820619012323893E+00, \
    0.3820619012323894E+00, \
   -0.6514286057161101E+00, \
    0.6514286057161101E+00, \
   -0.5711068454496305E+00, \
    0.5711068454496305E+00, \
   -0.8072896746317025E-01, \
    0.8072896746317031E-01, \
   -0.8630149364726712E+00, \
    0.8630149364726712E+00, \
   -0.3872678175415290E+00, \
    0.3872678175415290E+00, \
    0.5103334842355030E+00, \
   -0.5103334842355027E+00, \
   -0.9584329986119476E+00, \
    0.9584329986119474E+00, \
   -0.6619201369182062E+00, \
    0.6619201369182062E+00, \
   -0.1238115372273944E+00, \
    0.1238115372273945E+00, \
    0.2071876599633523E+00, \
   -0.2071876599633522E+00, \
    0.5346688849930886E-20 ] )
  ws = np.array ( [ \
    0.1261638293838951E-01, \
    0.1261638293838951E-01, \
    0.3408339905429266E-02, \
    0.3408339905429266E-02, \
    0.2796862081921473E-01, \
    0.2796862081921473E-01, \
    0.1252812914329644E-01, \
    0.1252812914329644E-01, \
    0.1635296523785200E-01, \
    0.1635296523785200E-01, \
    0.1720881227455075E-01, \
    0.1720881227455075E-01, \
    0.1523407270818440E-01, \
    0.1523407270818440E-01, \
    0.5600796522816800E-01, \
    0.5600796522816800E-01, \
    0.2382823797668716E-01, \
    0.2382823797668716E-01, \
    0.4513279974663867E-01, \
    0.4513279974663867E-01, \
    0.1931215256841166E-01, \
    0.1931215256841166E-01, \
    0.4158804216001467E-01, \
    0.4158804216001467E-01, \
    0.4685849665862760E-01, \
    0.4685849665862760E-01, \
    0.1200522449400290E+00, \
    0.1200522449400290E+00, \
    0.1238565802221201E-01, \
    0.1238565802221201E-01, \
    0.1760077392303538E-01, \
    0.1760077392303538E-01, \
    0.8264937698824523E-01, \
    0.8264937698824523E-01, \
    0.8629133710270168E-01, \
    0.8629133710270168E-01, \
    0.8660536182880048E-01, \
    0.8660536182880048E-01, \
    0.1134857467272575E+00, \
    0.1134857467272575E+00, \
    0.6518861145910534E-01, \
    0.6518861145910534E-01, \
    0.1184802238173896E+00, \
    0.1184802238173896E+00, \
    0.4767526390300979E-01, \
    0.4767526390300979E-01, \
    0.1203076112968188E-01, \
    0.1203076112968188E-01, \
    0.1010849820160845E+00, \
    0.1010849820160845E+00, \
    0.5753445241741756E-01, \
    0.5753445241741756E-01, \
    0.8946701652955226E-01, \
    0.8946701652955226E-01, \
    0.1312734684062163E+00 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule18 ( n ):

#*****************************************************************************80
#
## rule18() returns the rule of degree 18.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
   -0.9669786385710223E+00, \
    0.9737001842077581E+00, \
    0.9669786385710225E+00, \
   -0.9737001842077578E+00, \
   -0.2156318842512505E+00, \
    0.9910931195695962E+00, \
    0.2156318842512506E+00, \
   -0.9910931195695962E+00, \
   -0.7389660590011030E+00, \
    0.9797385272966153E+00, \
    0.7389660590011032E+00, \
   -0.9797385272966153E+00, \
    0.7689094060317012E+00, \
    0.9882749272572955E+00, \
   -0.7689094060317010E+00, \
   -0.9882749272572955E+00, \
   -0.8922402234413791E+00, \
    0.8925564983087213E+00, \
    0.8922402234413791E+00, \
   -0.8925564983087213E+00, \
    0.2617471442719549E+00, \
    0.9844702542794935E+00, \
   -0.2617471442719548E+00, \
   -0.9844702542794935E+00, \
   -0.7742833119206508E+00, \
    0.7411227454690407E+00, \
    0.7742833119206508E+00, \
   -0.7411227454690407E+00, \
   -0.5506736485553229E+00, \
    0.8796491853095826E+00, \
    0.5506736485553229E+00, \
   -0.8796491853095826E+00, \
   -0.5792562772184127E+00, \
    0.5652337954199163E+00, \
    0.5792562772184127E+00, \
   -0.5652337954199163E+00, \
   -0.1014796206724937E-01, \
    0.9024857168797702E+00, \
    0.1014796206724948E-01, \
   -0.9024857168797702E+00, \
    0.5420066475220151E+00, \
    0.9210890053684702E+00, \
   -0.5420066475220149E+00, \
   -0.9210890053684702E+00, \
    0.2943587054075071E+00, \
    0.7683262972049428E+00, \
   -0.2943587054075070E+00, \
   -0.7683262972049428E+00, \
   -0.3513695172888806E+00, \
    0.3692629613410464E+00, \
    0.3513695172888806E+00, \
   -0.3692629613410464E+00, \
   -0.3707443881794703E+00, \
    0.9667097045148131E+00, \
    0.3707443881794704E+00, \
   -0.9667097045148131E+00, \
   -0.2686897439986438E+00, \
    0.7370294813846769E+00, \
    0.2686897439986439E+00, \
   -0.7370294813846769E+00, \
   -0.1140106895094741E+00, \
    0.1969733705383891E+00, \
    0.1140106895094742E+00, \
   -0.1969733705383891E+00, \
    0.3612358695381902E-01, \
    0.5430113079937613E+00, \
   -0.3612358695381895E-01, \
   -0.5430113079937613E+00 ] )
  ys = np.array ( [ \
   -0.9737001842077582E+00, \
   -0.9669786385710224E+00, \
    0.9737001842077579E+00, \
    0.9669786385710226E+00, \
   -0.9910931195695962E+00, \
   -0.2156318842512506E+00, \
    0.9910931195695962E+00, \
    0.2156318842512507E+00, \
   -0.9797385272966153E+00, \
   -0.7389660590011031E+00, \
    0.9797385272966153E+00, \
    0.7389660590011033E+00, \
   -0.9882749272572955E+00, \
    0.7689094060317011E+00, \
    0.9882749272572955E+00, \
   -0.7689094060317009E+00, \
   -0.8925564983087213E+00, \
   -0.8922402234413791E+00, \
    0.8925564983087213E+00, \
    0.8922402234413791E+00, \
   -0.9844702542794935E+00, \
    0.2617471442719548E+00, \
    0.9844702542794935E+00, \
   -0.2617471442719547E+00, \
   -0.7411227454690407E+00, \
   -0.7742833119206508E+00, \
    0.7411227454690407E+00, \
    0.7742833119206508E+00, \
   -0.8796491853095826E+00, \
   -0.5506736485553229E+00, \
    0.8796491853095826E+00, \
    0.5506736485553229E+00, \
   -0.5652337954199163E+00, \
   -0.5792562772184127E+00, \
    0.5652337954199163E+00, \
    0.5792562772184127E+00, \
   -0.9024857168797702E+00, \
   -0.1014796206724942E-01, \
    0.9024857168797702E+00, \
    0.1014796206724953E-01, \
   -0.9210890053684702E+00, \
    0.5420066475220150E+00, \
    0.9210890053684702E+00, \
   -0.5420066475220148E+00, \
   -0.7683262972049428E+00, \
    0.2943587054075071E+00, \
    0.7683262972049428E+00, \
   -0.2943587054075070E+00, \
   -0.3692629613410464E+00, \
   -0.3513695172888806E+00, \
    0.3692629613410464E+00, \
    0.3513695172888806E+00, \
   -0.9667097045148131E+00, \
   -0.3707443881794704E+00, \
    0.9667097045148131E+00, \
    0.3707443881794705E+00, \
   -0.7370294813846769E+00, \
   -0.2686897439986438E+00, \
    0.7370294813846769E+00, \
    0.2686897439986439E+00, \
   -0.1969733705383891E+00, \
   -0.1140106895094741E+00, \
    0.1969733705383891E+00, \
    0.1140106895094742E+00, \
   -0.5430113079937613E+00, \
    0.3612358695381898E-01, \
    0.5430113079937613E+00, \
   -0.3612358695381891E-01 ] )
  ws = np.array ( [ \
    0.4697922862445027E-02, \
    0.4697922862445027E-02, \
    0.4697922862445027E-02, \
    0.4697922862445027E-02, \
    0.7136263254607511E-02, \
    0.7136263254607511E-02, \
    0.7136263254607511E-02, \
    0.7136263254607511E-02, \
    0.1293239065568239E-01, \
    0.1293239065568239E-01, \
    0.1293239065568239E-01, \
    0.1293239065568239E-01, \
    0.9398347568166604E-02, \
    0.9398347568166604E-02, \
    0.9398347568166604E-02, \
    0.9398347568166604E-02, \
    0.1884626577476044E-01, \
    0.1884626577476044E-01, \
    0.1884626577476044E-01, \
    0.1884626577476044E-01, \
    0.1572887987347023E-01, \
    0.1572887987347023E-01, \
    0.1572887987347023E-01, \
    0.1572887987347023E-01, \
    0.4107161379502558E-01, \
    0.4107161379502558E-01, \
    0.4107161379502558E-01, \
    0.4107161379502558E-01, \
    0.4035221395931435E-01, \
    0.4035221395931435E-01, \
    0.4035221395931435E-01, \
    0.4035221395931435E-01, \
    0.6647952625116643E-01, \
    0.6647952625116643E-01, \
    0.6647952625116643E-01, \
    0.6647952625116643E-01, \
    0.4719480581715914E-01, \
    0.4719480581715914E-01, \
    0.4719480581715914E-01, \
    0.4719480581715914E-01, \
    0.3594938959356454E-01, \
    0.3594938959356454E-01, \
    0.3594938959356454E-01, \
    0.3594938959356454E-01, \
    0.6892712069447091E-01, \
    0.6892712069447091E-01, \
    0.6892712069447091E-01, \
    0.6892712069447091E-01, \
    0.8060688072749707E-01, \
    0.8060688072749707E-01, \
    0.8060688072749707E-01, \
    0.8060688072749707E-01, \
    0.1530603725863855E-01, \
    0.1530603725863855E-01, \
    0.1530603725863855E-01, \
    0.1530603725863855E-01, \
    0.7313001882369689E-01, \
    0.7313001882369689E-01, \
    0.7313001882369689E-01, \
    0.7313001882369689E-01, \
    0.7447739831288605E-01, \
    0.7447739831288605E-01, \
    0.7447739831288605E-01, \
    0.7447739831288605E-01, \
    0.9487170596399580E-01, \
    0.9487170596399580E-01, \
    0.9487170596399580E-01, \
    0.9487170596399580E-01 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule19 ( n ):

#*****************************************************************************80
#
## rule19() returns the rule of degree 19.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
   -0.9734386316165470E+00, \
    0.9744990929036832E+00, \
    0.9734386316165472E+00, \
   -0.9744990929036830E+00, \
   -0.3841574585766744E+00, \
    0.9670641778942685E+00, \
    0.3841574585766745E+00, \
   -0.9670641778942685E+00, \
    0.2986734938364671E+00, \
    0.9905525689050123E+00, \
   -0.2986734938364670E+00, \
   -0.9905525689050123E+00, \
   -0.7396581737067777E+00, \
    0.9869464369033261E+00, \
    0.7396581737067779E+00, \
   -0.9869464369033261E+00, \
   -0.1425244970455050E+00, \
    0.9733021904515969E+00, \
    0.1425244970455051E+00, \
   -0.9733021904515969E+00, \
    0.7650240374639232E+00, \
    0.9804863471920530E+00, \
   -0.7650240374639230E+00, \
   -0.9804863471920530E+00, \
   -0.7599006633708002E+00, \
    0.7279453517455540E+00, \
    0.7599006633708002E+00, \
   -0.7279453517455540E+00, \
   -0.1192987760526789E+00, \
   -0.2637912058730560E-02, \
    0.1192987760526789E+00, \
    0.2637912058730575E-02, \
   -0.8850504442537889E+00, \
    0.9022234232868145E+00, \
    0.8850504442537889E+00, \
   -0.9022234232868145E+00, \
    0.5304174652462883E+00, \
    0.9125489607085608E+00, \
   -0.5304174652462881E+00, \
   -0.9125489607085608E+00, \
   -0.2858528945041368E+00, \
    0.2941600854694212E+00, \
    0.2858528945041368E+00, \
   -0.2941600854694212E+00, \
   -0.5671850101113227E+00, \
    0.8836081660895880E+00, \
    0.5671850101113227E+00, \
   -0.8836081660895880E+00, \
    0.3174295148500719E+00, \
    0.7293427112089215E+00, \
   -0.3174295148500718E+00, \
   -0.7293427112089215E+00, \
   -0.2492430513869149E+00, \
    0.7672563284436533E+00, \
    0.2492430513869150E+00, \
   -0.7672563284436533E+00, \
   -0.5087793568494521E+00, \
    0.5623738439118215E+00, \
    0.5087793568494521E+00, \
   -0.5623738439118215E+00, \
    0.7335719396414396E-01, \
    0.8930925855397183E+00, \
   -0.7335719396414385E-01, \
   -0.8930925855397183E+00, \
    0.8350775723842838E-02, \
    0.5392457387102469E+00, \
   -0.8350775723842772E-02, \
   -0.5392457387102469E+00 ] )
  ys = np.array ( [ \
   -0.9744990929036833E+00, \
   -0.9734386316165471E+00, \
    0.9744990929036831E+00, \
    0.9734386316165473E+00, \
   -0.9670641778942685E+00, \
   -0.3841574585766744E+00, \
    0.9670641778942685E+00, \
    0.3841574585766745E+00, \
   -0.9905525689050123E+00, \
    0.2986734938364670E+00, \
    0.9905525689050123E+00, \
   -0.2986734938364669E+00, \
   -0.9869464369033261E+00, \
   -0.7396581737067778E+00, \
    0.9869464369033261E+00, \
    0.7396581737067780E+00, \
   -0.9733021904515969E+00, \
   -0.1425244970455050E+00, \
    0.9733021904515969E+00, \
    0.1425244970455051E+00, \
   -0.9804863471920530E+00, \
    0.7650240374639231E+00, \
    0.9804863471920530E+00, \
   -0.7650240374639229E+00, \
   -0.7279453517455540E+00, \
   -0.7599006633708002E+00, \
    0.7279453517455540E+00, \
    0.7599006633708002E+00, \
    0.2637912058730553E-02, \
   -0.1192987760526789E+00, \
   -0.2637912058730568E-02, \
    0.1192987760526789E+00, \
   -0.9022234232868145E+00, \
   -0.8850504442537889E+00, \
    0.9022234232868145E+00, \
    0.8850504442537889E+00, \
   -0.9125489607085608E+00, \
    0.5304174652462882E+00, \
    0.9125489607085608E+00, \
   -0.5304174652462880E+00, \
   -0.2941600854694212E+00, \
   -0.2858528945041368E+00, \
    0.2941600854694212E+00, \
    0.2858528945041368E+00, \
   -0.8836081660895880E+00, \
   -0.5671850101113227E+00, \
    0.8836081660895880E+00, \
    0.5671850101113227E+00, \
   -0.7293427112089215E+00, \
    0.3174295148500719E+00, \
    0.7293427112089215E+00, \
   -0.3174295148500718E+00, \
   -0.7672563284436533E+00, \
   -0.2492430513869149E+00, \
    0.7672563284436533E+00, \
    0.2492430513869150E+00, \
   -0.5623738439118215E+00, \
   -0.5087793568494521E+00, \
    0.5623738439118215E+00, \
    0.5087793568494521E+00, \
   -0.8930925855397183E+00, \
    0.7335719396414390E-01, \
    0.8930925855397183E+00, \
   -0.7335719396414379E-01, \
   -0.5392457387102469E+00, \
    0.8350775723842805E-02, \
    0.5392457387102469E+00, \
   -0.8350775723842739E-02 ] )
  ws = np.array ( [ \
    0.4076118519980060E-02, \
    0.4076118519980060E-02, \
    0.4076118519980060E-02, \
    0.4076118519980060E-02, \
    0.1627326938099484E-01, \
    0.1627326938099484E-01, \
    0.1627326938099484E-01, \
    0.1627326938099484E-01, \
    0.1254157952509427E-01, \
    0.1254157952509427E-01, \
    0.1254157952509427E-01, \
    0.1254157952509427E-01, \
    0.1028929333936017E-01, \
    0.1028929333936017E-01, \
    0.1028929333936017E-01, \
    0.1028929333936017E-01, \
    0.1475928282295525E-01, \
    0.1475928282295525E-01, \
    0.1475928282295525E-01, \
    0.1475928282295525E-01, \
    0.1207323692393111E-01, \
    0.1207323692393111E-01, \
    0.1207323692393111E-01, \
    0.1207323692393111E-01, \
    0.4619184040692218E-01, \
    0.4619184040692218E-01, \
    0.4619184040692218E-01, \
    0.4619184040692218E-01, \
    0.3696173437828049E-01, \
    0.3696173437828049E-01, \
    0.3696173437828049E-01, \
    0.3696173437828049E-01, \
    0.2018069481193246E-01, \
    0.2018069481193246E-01, \
    0.2018069481193246E-01, \
    0.2018069481193246E-01, \
    0.3738944032940469E-01, \
    0.3738944032940469E-01, \
    0.3738944032940469E-01, \
    0.3738944032940469E-01, \
    0.9821701539315209E-01, \
    0.9821701539315209E-01, \
    0.9821701539315209E-01, \
    0.9821701539315209E-01, \
    0.3844110871724747E-01, \
    0.3844110871724747E-01, \
    0.3844110871724747E-01, \
    0.3844110871724747E-01, \
    0.7127049386881731E-01, \
    0.7127049386881731E-01, \
    0.7127049386881731E-01, \
    0.7127049386881731E-01, \
    0.6966749913838975E-01, \
    0.6966749913838975E-01, \
    0.6966749913838975E-01, \
    0.6966749913838975E-01, \
    0.7715964130310782E-01, \
    0.7715964130310782E-01, \
    0.7715964130310782E-01, \
    0.7715964130310782E-01, \
    0.4598470092336809E-01, \
    0.4598470092336809E-01, \
    0.4598470092336809E-01, \
    0.4598470092336809E-01, \
    0.9562983140360957E-01, \
    0.9562983140360957E-01, \
    0.9562983140360957E-01, \
    0.9562983140360957E-01 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule20 ( n ):

#*****************************************************************************80
#
## rule20() returns the rule of degree 20.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer N, the number of nodes.
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  import numpy as np

  xs = np.array ( [ \
   -0.9795110740034025E+00, \
    0.9831906073122737E+00, \
    0.9795110740034028E+00, \
   -0.9831906073122735E+00, \
   -0.7431761069248197E+00, \
    0.9923743096061538E+00, \
    0.7431761069248199E+00, \
   -0.9923743096061538E+00, \
   -0.4283144128355606E+00, \
    0.9641460474769801E+00, \
    0.4283144128355607E+00, \
   -0.9641460474769801E+00, \
    0.2195391124808899E+00, \
    0.9631697483532271E+00, \
   -0.2195391124808898E+00, \
   -0.9631697483532271E+00, \
    0.6056140907858303E+00, \
    0.9331619907848750E+00, \
   -0.6056140907858301E+00, \
   -0.9331619907848750E+00, \
    0.4538625783394974E+00, \
    0.9980174969022684E+00, \
   -0.4538625783394973E+00, \
   -0.9980174969022684E+00, \
   -0.8095537467004988E+00, \
    0.7623591488515665E+00, \
    0.8095537467004988E+00, \
   -0.7623591488515665E+00, \
   -0.1187579119827596E+00, \
    0.9879801664420653E+00, \
    0.1187579119827597E+00, \
   -0.9879801664420653E+00, \
   -0.8923235157505165E+00, \
    0.9333621871500086E+00, \
    0.8923235157505167E+00, \
   -0.9333621871500086E+00, \
    0.8231553038658227E+00, \
    0.9792360167943942E+00, \
   -0.8231553038658225E+00, \
   -0.9792360167943942E+00, \
   -0.2288711050959638E+00, \
    0.8448136056975591E+00, \
    0.2288711050959640E+00, \
   -0.8448136056975591E+00, \
   -0.6414644180013116E+00, \
    0.8887383480333905E+00, \
    0.6414644180013116E+00, \
   -0.8887383480333905E+00, \
    0.2100118285690190E-01, \
    0.9154636292013463E+00, \
   -0.2100118285690179E-01, \
   -0.9154636292013463E+00, \
    0.2939039049089534E+00, \
    0.4700673563865673E+00, \
   -0.2939039049089532E+00, \
   -0.4700673563865673E+00, \
   -0.4701209495753256E+00, \
    0.7110849452816542E+00, \
    0.4701209495753257E+00, \
   -0.7110849452816542E+00, \
   -0.2561845423520469E+00, \
    0.1372468757285573E-01, \
    0.2561845423520469E+00, \
   -0.1372468757285570E-01, \
    0.5331634078426070E+00, \
    0.6746722584255035E+00, \
   -0.5331634078426070E+00, \
   -0.6746722584255035E+00, \
    0.3458330575650539E+00, \
    0.8408056203362516E+00, \
   -0.3458330575650538E+00, \
   -0.8408056203362516E+00, \
    0.6630732857737233E-01, \
    0.6973527543224615E+00, \
   -0.6630732857737225E-01, \
   -0.6973527543224615E+00, \
   -0.2157929992274237E+00, \
    0.5168584327986239E+00, \
    0.2157929992274237E+00, \
   -0.5168584327986239E+00, \
   -0.1195405968452537E-31 ] )
  ys = np.array ( [ \
   -0.9831906073122738E+00, \
   -0.9795110740034026E+00, \
    0.9831906073122736E+00, \
    0.9795110740034029E+00, \
   -0.9923743096061538E+00, \
   -0.7431761069248198E+00, \
    0.9923743096061538E+00, \
    0.7431761069248201E+00, \
   -0.9641460474769801E+00, \
   -0.4283144128355607E+00, \
    0.9641460474769801E+00, \
    0.4283144128355608E+00, \
   -0.9631697483532271E+00, \
    0.2195391124808899E+00, \
    0.9631697483532271E+00, \
   -0.2195391124808898E+00, \
   -0.9331619907848750E+00, \
    0.6056140907858302E+00, \
    0.9331619907848750E+00, \
   -0.6056140907858300E+00, \
   -0.9980174969022684E+00, \
    0.4538625783394974E+00, \
    0.9980174969022684E+00, \
   -0.4538625783394973E+00, \
   -0.7623591488515665E+00, \
   -0.8095537467004988E+00, \
    0.7623591488515665E+00, \
    0.8095537467004988E+00, \
   -0.9879801664420653E+00, \
   -0.1187579119827596E+00, \
    0.9879801664420653E+00, \
    0.1187579119827597E+00, \
   -0.9333621871500086E+00, \
   -0.8923235157505166E+00, \
    0.9333621871500086E+00, \
    0.8923235157505168E+00, \
   -0.9792360167943942E+00, \
    0.8231553038658226E+00, \
    0.9792360167943942E+00, \
   -0.8231553038658224E+00, \
   -0.8448136056975591E+00, \
   -0.2288711050959639E+00, \
    0.8448136056975591E+00, \
    0.2288711050959640E+00, \
   -0.8887383480333905E+00, \
   -0.6414644180013116E+00, \
    0.8887383480333905E+00, \
    0.6414644180013116E+00, \
   -0.9154636292013463E+00, \
    0.2100118285690184E-01, \
    0.9154636292013463E+00, \
   -0.2100118285690173E-01, \
   -0.4700673563865673E+00, \
    0.2939039049089533E+00, \
    0.4700673563865673E+00, \
   -0.2939039049089532E+00, \
   -0.7110849452816542E+00, \
   -0.4701209495753256E+00, \
    0.7110849452816542E+00, \
    0.4701209495753257E+00, \
   -0.1372468757285574E-01, \
   -0.2561845423520469E+00, \
    0.1372468757285571E-01, \
    0.2561845423520469E+00, \
   -0.6746722584255035E+00, \
    0.5331634078426070E+00, \
    0.6746722584255035E+00, \
   -0.5331634078426070E+00, \
   -0.8408056203362516E+00, \
    0.3458330575650538E+00, \
    0.8408056203362516E+00, \
   -0.3458330575650537E+00, \
   -0.6973527543224615E+00, \
    0.6630732857737229E-01, \
    0.6973527543224615E+00, \
   -0.6630732857737220E-01, \
   -0.5168584327986239E+00, \
   -0.2157929992274237E+00, \
    0.5168584327986239E+00, \
    0.2157929992274238E+00, \
    0.3240416764471269E-32 ] )
  ws = np.array ( [ \
    0.2403280128020245E-02, \
    0.2403280128020245E-02, \
    0.2403280128020245E-02, \
    0.2403280128020245E-02, \
    0.6918304937846545E-02, \
    0.6918304937846545E-02, \
    0.6918304937846545E-02, \
    0.6918304937846545E-02, \
    0.1998132824455828E-01, \
    0.1998132824455828E-01, \
    0.1998132824455828E-01, \
    0.1998132824455828E-01, \
    0.1612406542082527E-01, \
    0.1612406542082527E-01, \
    0.1612406542082527E-01, \
    0.1612406542082527E-01, \
    0.2451719014395468E-01, \
    0.2451719014395468E-01, \
    0.2451719014395468E-01, \
    0.2451719014395468E-01, \
    0.5618083393401648E-02, \
    0.5618083393401648E-02, \
    0.5618083393401648E-02, \
    0.5618083393401648E-02, \
    0.3267989661107104E-01, \
    0.3267989661107104E-01, \
    0.3267989661107104E-01, \
    0.3267989661107104E-01, \
    0.9643554633385169E-02, \
    0.9643554633385169E-02, \
    0.9643554633385169E-02, \
    0.9643554633385169E-02, \
    0.1438022637487432E-01, \
    0.1438022637487432E-01, \
    0.1438022637487432E-01, \
    0.1438022637487432E-01, \
    0.9462403050575163E-02, \
    0.9462403050575163E-02, \
    0.9462403050575163E-02, \
    0.9462403050575163E-02, \
    0.4414700234043260E-01, \
    0.4414700234043260E-01, \
    0.4414700234043260E-01, \
    0.4414700234043260E-01, \
    0.2997776103642255E-01, \
    0.2997776103642255E-01, \
    0.2997776103642255E-01, \
    0.2997776103642255E-01, \
    0.2217921802120890E-01, \
    0.2217921802120890E-01, \
    0.2217921802120890E-01, \
    0.2217921802120890E-01, \
    0.7979169324002153E-01, \
    0.7979169324002153E-01, \
    0.7979169324002153E-01, \
    0.7979169324002153E-01, \
    0.5450753416951606E-01, \
    0.5450753416951606E-01, \
    0.5450753416951606E-01, \
    0.5450753416951606E-01, \
    0.9164051342923195E-01, \
    0.9164051342923195E-01, \
    0.9164051342923195E-01, \
    0.9164051342923195E-01, \
    0.5417703706712328E-01, \
    0.5417703706712328E-01, \
    0.5417703706712328E-01, \
    0.5417703706712328E-01, \
    0.4265496337854927E-01, \
    0.4265496337854927E-01, \
    0.4265496337854927E-01, \
    0.4265496337854927E-01, \
    0.6713307669025259E-01, \
    0.6713307669025259E-01, \
    0.6713307669025259E-01, \
    0.6713307669025259E-01, \
    0.7903551107191877E-01, \
    0.7903551107191877E-01, \
    0.7903551107191877E-01, \
    0.7903551107191877E-01, \
    0.5365512134302086E-03 ] )

  x = 0.5 * ( xs + 1.0 )
  y = 0.5 * ( ys + 1.0 )
  w = ws / np.sqrt ( 8.0 )

  return x, y, w

def rule_order ( degree ):

#*****************************************************************************80
#
## rule_order() returns the full size of the requested quadrature rule.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    10 June 2023
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer DEGREE, the degree of the quadrature (the 
#    maximum degree of the polynomials of two variables that are integrated
#    exactly.  0 <= DEGREE <= 20.
#
#  Output:
#
#    integer N, the number of nodes in the full rule.
#
  import numpy as np

  n_save = np.array ( [ \
      0, \
      1,   4,   4,   7,   7,  12,  12,  17,  17,  24, \
     24,  33,  33,  44,  44,  55,  55,  68,  68,  81 ] )

  if ( 0 <= degree and degree <= 20 ):
    n = n_save[degree]
  else:
    print ( '' )
    print ( 'rule_order(): Fatal error!' )
    print ( '  Degree must be between 0 and 20.' )
    raise Exception ( 'rule_order(): Fatal error!' )

  return n

def square_symq ( degree, n ):

#*****************************************************************************80
#
## square_symq() returns a symmetric quadrature rule for the square.
#
#  Discussion:
#
#    This procedure returns a quadrature rule for smooth functions
#    on the unit square [-1,1] )^2.
#
#    All quadratures are accurate to 15 digits
#    All weights are positive and inside the square
#
#    The nodes are symmetrically arranged.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    Original FORTRAN77 version by Hong Xiao, Zydrunas Gimbutas.
#    This version by John Burkardt.
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    integer DEGREE, the degree of the quadrature rule.
#    0 <= DEGREE <= 20.
#
#    integer N, the number of nodes.
#    This can be determined by a call to rule_order(degree).
#
#  Output:
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    real w(n): the weights.
#
  if ( degree == 0 ):
    x, y, w = rule00 ( n )
  elif ( degree == 1 ):
    x, y, w = rule01 ( n )
  elif ( degree == 2 ):
    x, y, w = rule02 ( n )
  elif ( degree == 3 ):
    x, y, w = rule03 ( n )
  elif ( degree == 4 ):
    x, y, w = rule04 ( n )
  elif ( degree == 5 ):
    x, y, w = rule05 ( n )
  elif ( degree == 6 ):
    x, y, w = rule06 ( n )
  elif ( degree == 7 ):
    x, y, w = rule07 ( n )
  elif ( degree == 8 ):
    x, y, w = rule08 ( n )
  elif ( degree == 9 ):
    x, y, w = rule09 ( n )
  elif ( degree == 10 ):
    x, y, w = rule10 ( n )
  elif ( degree == 11 ):
    x, y, w = rule11 ( n )
  elif ( degree == 12 ):
    x, y, w = rule12 ( n )
  elif ( degree == 13 ):
    x, y, w = rule13 ( n )
  elif ( degree == 14 ):
    x, y, w = rule14 ( n )
  elif ( degree == 15 ):
    x, y, w = rule15 ( n )
  elif ( degree == 16 ):
    x, y, w = rule16 ( n )
  elif ( degree == 17 ):
    x, y, w = rule17 ( n )
  elif ( degree == 18 ):
    x, y, w = rule18 ( n )
  elif ( degree == 19 ):
    x, y, w = rule19 ( n )
  elif ( degree == 20 ):
    x, y, w = rule20 ( n )
  else:
    print ( '' )
    print ( 'square_symq(): Fatal error!' )
    print ( '  Illegal value of DEGREE.' )
    raise Exception ( 'square_symq(): Fatal error!' )

  return x, y, w

def square_symq_plot ( n, x, y, filename ):

#*****************************************************************************80
#
## square_symq_plot() plots a symmetric square quadrature rule.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    08 June 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Hong Xiao, Zydrunas Gimbutas,
#    A numerical algorithm for the construction of efficient quadrature
#    rules in two and higher dimensions,
#    Computers and Mathematics with Applications,
#    Volume 59, 2010, pages 663-676.
#
#  Input:
#
#    real N, the number of nodes.
#
#    real x(n), y(n): the coordinates of the nodes.
#
#    string filename: a filename for the plot.
#
  import matplotlib.pyplot as plt
  import numpy as np

  plt.clf ( )
  plt.plot ( [ 0.0, 1.0, 1.0, 0.0, 0.0 ], [ 0.0, 0.0, 1.0, 1.0, 0.0 ], \
    'r-', linewidth = 2 )
  plt.plot ( x, y, 'b.', markersize = 25 )
  plt.xlabel ( "<--- X --->" )
  plt.ylabel ( "<--- Y --->" )
  plt.title ( filename )
  plt.grid ( True )
  plt.axis ( 'equal' )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

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
  square_symq_rule_test ( )
  timestamp ( )

