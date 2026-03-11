#! /usr/bin/env python3
#
def triangle_witherden_rule_test ( ):

#*****************************************************************************80
#
## triangle_witherden_rule_test() tests triangle_witherden_rule().
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    10 July 2023
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'triangle_witherden_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test triangle_witherden_rule().' )

  p = 5
  triangle_witherden_rule_test01 ( p )

  p = 5
  triangle_witherden_rule_test02 ( p )

  p_lo = 0
  p_hi = 20
  triangle_witherden_rule_test03 ( p_lo, p_hi )
#
#  Terminate.
#
  print ( '' )
  print ( 'triangle_witherden_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def triangle_witherden_rule_test01 ( p ):

#*****************************************************************************80
#
## triangle_witherden_rule_test01() computes a quadrature rule of order P.
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
  print ( 'triangle_witherden_rule_test01():' )
  print ( '  Quadrature rule for the triangle,' )
  print ( '  given in barycentric coordinates.' )
  print ( '  Precision p = ', p )
#
#  Retrieve the rule.
#
  n, a, b, c, w = triangle_witherden_rule ( p )
#
#  Print the rule.
#
  print ( '' )
  print ( '     I      W          A           B           C' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %4d  %10.6g  %10.6g  %10.6g  %10.6g' \
      % ( i, w[i], a[i], b[i], c[i] ) )
#
#  Verify weights sum to 1.
#
  w_sum = np.sum ( w )

  print ( '' )
  print ( '  Weight Sum    ', w_sum )

  return

def triangle_witherden_rule_test02 ( p ):

#*****************************************************************************80
#
## triangle_witherden_rule_test02() tests a triangle quadrature rule of order P.
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
  print ( 'triangle_witherden_rule_test02():' )
  print ( '  Test the precision of a quadrature rule for the unit triangle.' )

  dim_num = 2
#
#  Retrieve the rule.
#
  n, a, b, c, w = triangle_witherden_rule ( p )
#
#  Pack the x, y, z vectors as rows of an array.
#
  xy = np.transpose ( np.array ( [ a, b ] ) )

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

      quad = triangle_unit_area ( ) * np.dot ( w, v )

      exact = triangle_unit_monomial_integral ( expon )

      quad_error = np.abs ( quad - exact )

      max_error = max ( max_error, quad_error )

      if ( not more ):
        break

    print ( '  %2d  %24.16g' % ( degree, max_error ) )

  return

def triangle_witherden_rule_test03 ( p_lo, p_hi ):

#*****************************************************************************80
#
## triangle_witherden_rule_test03() tests absolute and relative precision.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    10 July 2023
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
  print ( 'triangle_witherden_rule_test03():' )
  print ( '  Test the precision of quadrature rules for the unit triangle.' )
  print ( '  Check rules of precision p =', p_lo, 'through', p_hi )
  print ( '  for error in approximating integrals of monomials.' )

  dim_num = 2

  print ( '' )
  print ( '              maximum                   maximum' )
  print ( '   p          absolute                  relative' )
  print ( '              error                     error' )
  print ( '' )

  for p in range ( p_lo, p_hi + 1 ):

    n, a, b, c, w = triangle_witherden_rule ( p )
#
#  Pack the x, y, z vectors as rows of an array.
#
    xy = np.transpose ( np.array ( [ a, b ] ) )

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

        quad = triangle_unit_area ( ) * np.dot ( w, v )

        exact = triangle_unit_monomial_integral ( expon )

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

def rule00 ( ):

#*****************************************************************************80
#
## rule00() returns the rule of precision 0.
#
#  Discussion:
#
#    This is simply a copy of rule01.m.
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.3333333333333334 ] )

  y = np.array ( [ \
      0.3333333333333334 ] )

  z = np.array ( [ \
      0.3333333333333333 ] )

  w = np.array ( [ \
      0.5000000000000000 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule01 ( ):

#*****************************************************************************80
#
## rule01() returns the rule of precision 1.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.3333333333333334 ] )

  y = np.array ( [ \
      0.3333333333333334 ] )

  z = np.array ( [ \
      0.3333333333333333 ] )

  w = np.array ( [ \
      0.5000000000000000 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule02 ( ):

#*****************************************************************************80
#
## rule02() returns the rule of precision 2.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.1666666666666667, \
      0.6666666666666666, \
      0.1666666666666667 ] )

  y = np.array ( [ \
      0.6666666666666666, \
      0.1666666666666667, \
      0.1666666666666667 ] )

  z = np.array ( [ \
      0.1666666666666666, \
      0.1666666666666667, \
      0.6666666666666665 ] )

  w = np.array ( [ \
      0.1666666666666667, \
      0.1666666666666667, \
      0.1666666666666667 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule03 ( ):

#*****************************************************************************80
#
## rule03() returns the rule of precision 3.
#
#  Discussion:
#
#    This is a copy of rule04.m.
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.4459484909159649, \
      0.1081030181680702, \
      0.4459484909159649, \
      0.0915762135097707, \
      0.8168475729804585, \
      0.0915762135097707 ] )

  y = np.array ( [ \
      0.1081030181680702, \
      0.4459484909159649, \
      0.4459484909159649, \
      0.8168475729804585, \
      0.0915762135097707, \
      0.0915762135097707 ] )

  z = np.array ( [ \
      0.4459484909159649, \
      0.4459484909159649, \
      0.1081030181680702, \
      0.0915762135097707, \
      0.0915762135097707, \
      0.8168475729804585 ] )

  w = np.array ( [ \
      0.1116907948390057, \
      0.1116907948390057, \
      0.1116907948390057, \
      0.0549758718276609, \
      0.0549758718276609, \
      0.0549758718276609 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule04 ( ):

#*****************************************************************************80
#
## rule04() returns the rule of precision 4.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.4459484909159649, \
      0.1081030181680702, \
      0.4459484909159649, \
      0.0915762135097707, \
      0.8168475729804585, \
      0.0915762135097707 ] )

  y = np.array ( [ \
      0.1081030181680702, \
      0.4459484909159649, \
      0.4459484909159649, \
      0.8168475729804585, \
      0.0915762135097707, \
      0.0915762135097707 ] )

  z = np.array ( [ \
      0.4459484909159649, \
      0.4459484909159649, \
      0.1081030181680702, \
      0.0915762135097707, \
      0.0915762135097707, \
      0.8168475729804585 ] )

  w = np.array ( [ \
      0.1116907948390057, \
      0.1116907948390057, \
      0.1116907948390057, \
      0.0549758718276609, \
      0.0549758718276609, \
      0.0549758718276609 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule05 ( ):

#*****************************************************************************80
#
## rule05() returns the rule of precision 5.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.3333333333333334, \
      0.1012865073234563, \
      0.7974269853530873, \
      0.1012865073234563, \
      0.4701420641051151, \
      0.0597158717897698, \
      0.4701420641051151 ] )

  y = np.array ( [ \
      0.3333333333333334, \
      0.7974269853530873, \
      0.1012865073234563, \
      0.1012865073234563, \
      0.0597158717897698, \
      0.4701420641051151, \
      0.4701420641051151 ] )

  z = np.array ( [ \
      0.3333333333333333, \
      0.1012865073234563, \
      0.1012865073234563, \
      0.7974269853530873, \
      0.4701420641051151, \
      0.4701420641051150, \
      0.0597158717897698 ] )

  w = np.array ( [ \
      0.1125000000000000, \
      0.0629695902724136, \
      0.0629695902724136, \
      0.0629695902724136, \
      0.0661970763942531, \
      0.0661970763942531, \
      0.0661970763942531 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule06 ( ):

#*****************************************************************************80
#
## rule06() returns the rule of precision 6.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.0630890144915022, \
      0.8738219710169955, \
      0.0630890144915022, \
      0.2492867451709104, \
      0.5014265096581791, \
      0.2492867451709104, \
      0.0531450498448169, \
      0.6365024991213987, \
      0.3103524510337844, \
      0.6365024991213987, \
      0.3103524510337844, \
      0.0531450498448169 ] )

  y = np.array ( [ \
      0.8738219710169955, \
      0.0630890144915022, \
      0.0630890144915022, \
      0.5014265096581791, \
      0.2492867451709104, \
      0.2492867451709104, \
      0.6365024991213987, \
      0.0531450498448169, \
      0.6365024991213987, \
      0.3103524510337844, \
      0.0531450498448169, \
      0.3103524510337844 ] )

  z = np.array ( [ \
      0.0630890144915023, \
      0.0630890144915022, \
      0.8738219710169957, \
      0.2492867451709104, \
      0.2492867451709104, \
      0.5014265096581791, \
      0.3103524510337844, \
      0.3103524510337844, \
      0.0531450498448169, \
      0.0531450498448169, \
      0.6365024991213987, \
      0.6365024991213987 ] )

  w = np.array ( [ \
      0.0254224531851034, \
      0.0254224531851034, \
      0.0254224531851034, \
      0.0583931378631897, \
      0.0583931378631897, \
      0.0583931378631897, \
      0.0414255378091868, \
      0.0414255378091868, \
      0.0414255378091868, \
      0.0414255378091868, \
      0.0414255378091868, \
      0.0414255378091868 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule07 ( ):

#*****************************************************************************80
#
## rule07() returns the rule of precision 7.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.0337306485545878, \
      0.9325387028908243, \
      0.0337306485545878, \
      0.2415773825954036, \
      0.5168452348091929, \
      0.2415773825954036, \
      0.4743096925047182, \
      0.0513806149905635, \
      0.4743096925047182, \
      0.0470366446525952, \
      0.7542800405500532, \
      0.1986833147973516, \
      0.7542800405500532, \
      0.1986833147973516, \
      0.0470366446525952 ] )

  y = np.array ( [ \
      0.9325387028908243, \
      0.0337306485545878, \
      0.0337306485545878, \
      0.5168452348091929, \
      0.2415773825954036, \
      0.2415773825954036, \
      0.0513806149905635, \
      0.4743096925047182, \
      0.4743096925047182, \
      0.7542800405500532, \
      0.0470366446525952, \
      0.7542800405500532, \
      0.1986833147973516, \
      0.0470366446525952, \
      0.1986833147973516 ] )

  z = np.array ( [ \
      0.0337306485545878, \
      0.0337306485545878, \
      0.9325387028908243, \
      0.2415773825954036, \
      0.2415773825954036, \
      0.5168452348091930, \
      0.4743096925047183, \
      0.4743096925047182, \
      0.0513806149905636, \
      0.1986833147973517, \
      0.1986833147973516, \
      0.0470366446525953, \
      0.0470366446525953, \
      0.7542800405500532, \
      0.7542800405500533 ] )

  w = np.array ( [ \
      0.0082725250553961, \
      0.0082725250553961, \
      0.0082725250553961, \
      0.0639720856150778, \
      0.0639720856150778, \
      0.0639720856150778, \
      0.0385433230929930, \
      0.0385433230929930, \
      0.0385433230929930, \
      0.0279393664515999, \
      0.0279393664515999, \
      0.0279393664515999, \
      0.0279393664515999, \
      0.0279393664515999, \
      0.0279393664515999 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule08 ( ):

#*****************************************************************************80
#
## rule08() returns the rule of precision 8.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.3333333333333334, \
      0.4592925882927231, \
      0.0814148234145537, \
      0.4592925882927231, \
      0.1705693077517602, \
      0.6588613844964796, \
      0.1705693077517602, \
      0.0505472283170310, \
      0.8989055433659381, \
      0.0505472283170310, \
      0.0083947774099576, \
      0.7284923929554042, \
      0.2631128296346381, \
      0.7284923929554042, \
      0.2631128296346381, \
      0.0083947774099576 ] )

  y = np.array ( [ \
      0.3333333333333334, \
      0.0814148234145537, \
      0.4592925882927231, \
      0.4592925882927231, \
      0.6588613844964796, \
      0.1705693077517602, \
      0.1705693077517602, \
      0.8989055433659381, \
      0.0505472283170310, \
      0.0505472283170310, \
      0.7284923929554042, \
      0.0083947774099576, \
      0.7284923929554042, \
      0.2631128296346381, \
      0.0083947774099576, \
      0.2631128296346381 ] )

  z = np.array ( [ \
      0.3333333333333333, \
      0.4592925882927232, \
      0.4592925882927231, \
      0.0814148234145537, \
      0.1705693077517602, \
      0.1705693077517602, \
      0.6588613844964795, \
      0.0505472283170310, \
      0.0505472283170310, \
      0.8989055433659381, \
      0.2631128296346382, \
      0.2631128296346382, \
      0.0083947774099576, \
      0.0083947774099576, \
      0.7284923929554044, \
      0.7284923929554044 ] )

  w = np.array ( [ \
      0.0721578038388936, \
      0.0475458171336423, \
      0.0475458171336423, \
      0.0475458171336423, \
      0.0516086852673591, \
      0.0516086852673591, \
      0.0516086852673591, \
      0.0162292488115990, \
      0.0162292488115990, \
      0.0162292488115990, \
      0.0136151570872175, \
      0.0136151570872175, \
      0.0136151570872175, \
      0.0136151570872175, \
      0.0136151570872175, \
      0.0136151570872175 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule09 ( ):

#*****************************************************************************80
#
## rule09() returns the rule of precision 9.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.3333333333333334, \
      0.4370895914929366, \
      0.1258208170141267, \
      0.4370895914929366, \
      0.1882035356190327, \
      0.6235929287619345, \
      0.1882035356190327, \
      0.4896825191987376, \
      0.0206349616025248, \
      0.4896825191987376, \
      0.0447295133944527, \
      0.9105409732110945, \
      0.0447295133944527, \
      0.0368384120547363, \
      0.7411985987844980, \
      0.2219629891607657, \
      0.7411985987844980, \
      0.2219629891607657, \
      0.0368384120547363 ] )

  y = np.array ( [ \
      0.3333333333333334, \
      0.1258208170141267, \
      0.4370895914929366, \
      0.4370895914929366, \
      0.6235929287619345, \
      0.1882035356190327, \
      0.1882035356190327, \
      0.0206349616025248, \
      0.4896825191987376, \
      0.4896825191987376, \
      0.9105409732110945, \
      0.0447295133944527, \
      0.0447295133944527, \
      0.7411985987844980, \
      0.0368384120547363, \
      0.7411985987844980, \
      0.2219629891607657, \
      0.0368384120547363, \
      0.2219629891607657 ] )

  z = np.array ( [ \
      0.3333333333333333, \
      0.4370895914929366, \
      0.4370895914929366, \
      0.1258208170141267, \
      0.1882035356190327, \
      0.1882035356190327, \
      0.6235929287619344, \
      0.4896825191987376, \
      0.4896825191987376, \
      0.0206349616025248, \
      0.0447295133944527, \
      0.0447295133944528, \
      0.9105409732110945, \
      0.2219629891607657, \
      0.2219629891607657, \
      0.0368384120547363, \
      0.0368384120547363, \
      0.7411985987844980, \
      0.7411985987844980 ] )

  w = np.array ( [ \
      0.0485678981413994, \
      0.0389137705023871, \
      0.0389137705023871, \
      0.0389137705023871, \
      0.0398238694636051, \
      0.0398238694636051, \
      0.0398238694636051, \
      0.0156673501135695, \
      0.0156673501135695, \
      0.0156673501135695, \
      0.0127888378293490, \
      0.0127888378293490, \
      0.0127888378293490, \
      0.0216417696886447, \
      0.0216417696886447, \
      0.0216417696886447, \
      0.0216417696886447, \
      0.0216417696886447, \
      0.0216417696886447 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule10 ( ):

#*****************************************************************************80
#
## rule10() returns the rule of precision 10.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.3333333333333334, \
      0.0320553732169435, \
      0.9358892535661130, \
      0.0320553732169435, \
      0.1421611010565644, \
      0.7156777978868712, \
      0.1421611010565644, \
      0.3218129952888354, \
      0.5300541189273440, \
      0.1481328857838206, \
      0.5300541189273440, \
      0.1481328857838206, \
      0.3218129952888354, \
      0.0296198894887298, \
      0.6012333286834592, \
      0.3691467818278110, \
      0.6012333286834592, \
      0.3691467818278110, \
      0.0296198894887298, \
      0.0283676653399385, \
      0.8079306009228790, \
      0.1637017337371825, \
      0.8079306009228790, \
      0.1637017337371825, \
      0.0283676653399385 ] )

  y = np.array ( [ \
      0.3333333333333334, \
      0.9358892535661130, \
      0.0320553732169435, \
      0.0320553732169435, \
      0.7156777978868712, \
      0.1421611010565644, \
      0.1421611010565644, \
      0.5300541189273440, \
      0.3218129952888354, \
      0.5300541189273440, \
      0.1481328857838206, \
      0.3218129952888354, \
      0.1481328857838206, \
      0.6012333286834592, \
      0.0296198894887298, \
      0.6012333286834592, \
      0.3691467818278110, \
      0.0296198894887298, \
      0.3691467818278110, \
      0.8079306009228790, \
      0.0283676653399385, \
      0.8079306009228790, \
      0.1637017337371825, \
      0.0283676653399385, \
      0.1637017337371825 ] )

  z = np.array ( [ \
      0.3333333333333333, \
      0.0320553732169435, \
      0.0320553732169435, \
      0.9358892535661130, \
      0.1421611010565643, \
      0.1421611010565644, \
      0.7156777978868711, \
      0.1481328857838206, \
      0.1481328857838206, \
      0.3218129952888354, \
      0.3218129952888354, \
      0.5300541189273440, \
      0.5300541189273440, \
      0.3691467818278109, \
      0.3691467818278110, \
      0.0296198894887297, \
      0.0296198894887297, \
      0.6012333286834592, \
      0.6012333286834591, \
      0.1637017337371824, \
      0.1637017337371825, \
      0.0283676653399385, \
      0.0283676653399385, \
      0.8079306009228790, \
      0.8079306009228790 ] )

  w = np.array ( [ \
      0.0408716645731430, \
      0.0066764844065748, \
      0.0066764844065748, \
      0.0066764844065748, \
      0.0229789818023724, \
      0.0229789818023724, \
      0.0229789818023724, \
      0.0319524531982120, \
      0.0319524531982120, \
      0.0319524531982120, \
      0.0319524531982120, \
      0.0319524531982120, \
      0.0319524531982120, \
      0.0170923240814797, \
      0.0170923240814797, \
      0.0170923240814797, \
      0.0170923240814797, \
      0.0170923240814797, \
      0.0170923240814797, \
      0.0126488788536442, \
      0.0126488788536442, \
      0.0126488788536442, \
      0.0126488788536442, \
      0.0126488788536442, \
      0.0126488788536442 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule11 ( ):

#*****************************************************************************80
#
## rule11() returns the rule of precision 11.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.3333333333333334, \
      0.0284854176143719, \
      0.9430291647712562, \
      0.0284854176143719, \
      0.2102199567031783, \
      0.5795600865936434, \
      0.2102199567031783, \
      0.1026354827122464, \
      0.7947290345755071, \
      0.1026354827122464, \
      0.4958919009658909, \
      0.0082161980682182, \
      0.4958919009658909, \
      0.4384659267643522, \
      0.1230681464712956, \
      0.4384659267643522, \
      0.1493247886520824, \
      0.8433497836618531, \
      0.0073254276860645, \
      0.8433497836618531, \
      0.0073254276860645, \
      0.1493247886520824, \
      0.0460105001654300, \
      0.6644083741968642, \
      0.2895811256377059, \
      0.6644083741968642, \
      0.2895811256377059, \
      0.0460105001654300 ] )

  y = np.array ( [ \
      0.3333333333333334, \
      0.9430291647712562, \
      0.0284854176143719, \
      0.0284854176143719, \
      0.5795600865936434, \
      0.2102199567031783, \
      0.2102199567031783, \
      0.7947290345755071, \
      0.1026354827122464, \
      0.1026354827122464, \
      0.0082161980682182, \
      0.4958919009658909, \
      0.4958919009658909, \
      0.1230681464712956, \
      0.4384659267643522, \
      0.4384659267643522, \
      0.8433497836618531, \
      0.1493247886520824, \
      0.8433497836618531, \
      0.0073254276860645, \
      0.1493247886520824, \
      0.0073254276860645, \
      0.6644083741968642, \
      0.0460105001654300, \
      0.6644083741968642, \
      0.2895811256377059, \
      0.0460105001654300, \
      0.2895811256377059 ] )

  z = np.array ( [ \
      0.3333333333333333, \
      0.0284854176143720, \
      0.0284854176143719, \
      0.9430291647712563, \
      0.2102199567031783, \
      0.2102199567031783, \
      0.5795600865936434, \
      0.1026354827122464, \
      0.1026354827122464, \
      0.7947290345755071, \
      0.4958919009658910, \
      0.4958919009658909, \
      0.0082161980682182, \
      0.4384659267643521, \
      0.4384659267643522, \
      0.1230681464712955, \
      0.0073254276860646, \
      0.0073254276860645, \
      0.1493247886520824, \
      0.1493247886520824, \
      0.8433497836618531, \
      0.8433497836618532, \
      0.2895811256377059, \
      0.2895811256377059, \
      0.0460105001654300, \
      0.0460105001654300, \
      0.6644083741968642, \
      0.6644083741968642 ] )

  w = np.array ( [ \
      0.0428805898661121, \
      0.0052159352564473, \
      0.0052159352564473, \
      0.0052159352564473, \
      0.0352578420558583, \
      0.0352578420558583, \
      0.0352578420558583, \
      0.0193153796185097, \
      0.0193153796185097, \
      0.0193153796185097, \
      0.0083031365272927, \
      0.0083031365272927, \
      0.0083031365272927, \
      0.0336580770397341, \
      0.0336580770397341, \
      0.0336580770397341, \
      0.0051451447864766, \
      0.0051451447864766, \
      0.0051451447864766, \
      0.0051451447864766, \
      0.0051451447864766, \
      0.0051451447864766, \
      0.0201662383202503, \
      0.0201662383202503, \
      0.0201662383202503, \
      0.0201662383202503, \
      0.0201662383202503, \
      0.0201662383202503 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule12 ( ):

#*****************************************************************************80
#
## rule12() returns the rule of precision 12.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.4882037509455415, \
      0.0235924981089169, \
      0.4882037509455415, \
      0.1092578276593543, \
      0.7814843446812914, \
      0.1092578276593543, \
      0.2714625070149261, \
      0.4570749859701478, \
      0.2714625070149261, \
      0.0246463634363356, \
      0.9507072731273288, \
      0.0246463634363356, \
      0.4401116486585931, \
      0.1197767026828138, \
      0.4401116486585931, \
      0.2916556797383409, \
      0.6853101639063919, \
      0.0230341563552671, \
      0.6853101639063919, \
      0.0230341563552671, \
      0.2916556797383409, \
      0.1162960196779266, \
      0.6282497516835561, \
      0.2554542286385174, \
      0.6282497516835561, \
      0.2554542286385174, \
      0.1162960196779266, \
      0.8513377925102401, \
      0.1272797172335894, \
      0.0213824902561706, \
      0.1272797172335894, \
      0.0213824902561706, \
      0.8513377925102401 ] )

  y = np.array ( [ \
      0.0235924981089169, \
      0.4882037509455415, \
      0.4882037509455415, \
      0.7814843446812914, \
      0.1092578276593543, \
      0.1092578276593543, \
      0.4570749859701478, \
      0.2714625070149261, \
      0.2714625070149261, \
      0.9507072731273288, \
      0.0246463634363356, \
      0.0246463634363356, \
      0.1197767026828138, \
      0.4401116486585931, \
      0.4401116486585931, \
      0.6853101639063919, \
      0.2916556797383409, \
      0.6853101639063919, \
      0.0230341563552671, \
      0.2916556797383409, \
      0.0230341563552671, \
      0.6282497516835561, \
      0.1162960196779266, \
      0.6282497516835561, \
      0.2554542286385174, \
      0.1162960196779266, \
      0.2554542286385174, \
      0.1272797172335894, \
      0.8513377925102401, \
      0.1272797172335894, \
      0.0213824902561706, \
      0.8513377925102401, \
      0.0213824902561706 ] )

  z = np.array ( [ \
      0.4882037509455416, \
      0.4882037509455416, \
      0.0235924981089170, \
      0.1092578276593543, \
      0.1092578276593544, \
      0.7814843446812914, \
      0.2714625070149260, \
      0.2714625070149261, \
      0.4570749859701478, \
      0.0246463634363355, \
      0.0246463634363356, \
      0.9507072731273287, \
      0.4401116486585931, \
      0.4401116486585931, \
      0.1197767026828138, \
      0.0230341563552672, \
      0.0230341563552672, \
      0.2916556797383409, \
      0.2916556797383410, \
      0.6853101639063919, \
      0.6853101639063919, \
      0.2554542286385173, \
      0.2554542286385173, \
      0.1162960196779266, \
      0.1162960196779265, \
      0.6282497516835561, \
      0.6282497516835561, \
      0.0213824902561705, \
      0.0213824902561706, \
      0.8513377925102401, \
      0.8513377925102401, \
      0.1272797172335893, \
      0.1272797172335893 ] )

  w = np.array ( [ \
      0.0121334190407260, \
      0.0121334190407260, \
      0.0121334190407260, \
      0.0142430260344388, \
      0.0142430260344388, \
      0.0142430260344388, \
      0.0312706065979514, \
      0.0312706065979514, \
      0.0312706065979514, \
      0.0039658212549868, \
      0.0039658212549868, \
      0.0039658212549868, \
      0.0249591674640305, \
      0.0249591674640305, \
      0.0249591674640305, \
      0.0108917925193038, \
      0.0108917925193038, \
      0.0108917925193038, \
      0.0108917925193038, \
      0.0108917925193038, \
      0.0108917925193038, \
      0.0216136818297071, \
      0.0216136818297071, \
      0.0216136818297071, \
      0.0216136818297071, \
      0.0216136818297071, \
      0.0216136818297071, \
      0.0075418387882557, \
      0.0075418387882557, \
      0.0075418387882557, \
      0.0075418387882557, \
      0.0075418387882557, \
      0.0075418387882557 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule13 ( ):

#*****************************************************************************80
#
## rule13() returns the rule of precision 13.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.3333333333333334, \
      0.4890769464525394, \
      0.0218461070949213, \
      0.4890769464525394, \
      0.2213722862918329, \
      0.5572554274163342, \
      0.2213722862918329, \
      0.4269414142598004, \
      0.1461171714803992, \
      0.4269414142598004, \
      0.0215096811088432, \
      0.9569806377823136, \
      0.0215096811088432, \
      0.0878954830321973, \
      0.7485071158999522, \
      0.1635974010678505, \
      0.7485071158999522, \
      0.1635974010678505, \
      0.0878954830321973, \
      0.1109220428034634, \
      0.8647077702954428, \
      0.0243701869010938, \
      0.8647077702954428, \
      0.0243701869010938, \
      0.1109220428034634, \
      0.3084417608921178, \
      0.6235459955536755, \
      0.0680122435542067, \
      0.6235459955536755, \
      0.0680122435542067, \
      0.3084417608921178, \
      0.0051263891023824, \
      0.7223577931241880, \
      0.2725158177734297, \
      0.7223577931241880, \
      0.2725158177734297, \
      0.0051263891023824 ] )

  y = np.array ( [ \
      0.3333333333333334, \
      0.0218461070949213, \
      0.4890769464525394, \
      0.4890769464525394, \
      0.5572554274163342, \
      0.2213722862918329, \
      0.2213722862918329, \
      0.1461171714803992, \
      0.4269414142598004, \
      0.4269414142598004, \
      0.9569806377823136, \
      0.0215096811088432, \
      0.0215096811088432, \
      0.7485071158999522, \
      0.0878954830321973, \
      0.7485071158999522, \
      0.1635974010678505, \
      0.0878954830321973, \
      0.1635974010678505, \
      0.8647077702954428, \
      0.1109220428034634, \
      0.8647077702954428, \
      0.0243701869010938, \
      0.1109220428034634, \
      0.0243701869010938, \
      0.6235459955536755, \
      0.3084417608921178, \
      0.6235459955536755, \
      0.0680122435542067, \
      0.3084417608921178, \
      0.0680122435542067, \
      0.7223577931241880, \
      0.0051263891023824, \
      0.7223577931241880, \
      0.2725158177734297, \
      0.0051263891023824, \
      0.2725158177734297 ] )

  z = np.array ( [ \
      0.3333333333333333, \
      0.4890769464525394, \
      0.4890769464525394, \
      0.0218461070949214, \
      0.2213722862918329, \
      0.2213722862918329, \
      0.5572554274163342, \
      0.4269414142598003, \
      0.4269414142598003, \
      0.1461171714803991, \
      0.0215096811088433, \
      0.0215096811088433, \
      0.9569806377823138, \
      0.1635974010678505, \
      0.1635974010678505, \
      0.0878954830321973, \
      0.0878954830321973, \
      0.7485071158999522, \
      0.7485071158999522, \
      0.0243701869010938, \
      0.0243701869010938, \
      0.1109220428034634, \
      0.1109220428034634, \
      0.8647077702954428, \
      0.8647077702954428, \
      0.0680122435542068, \
      0.0680122435542067, \
      0.3084417608921178, \
      0.3084417608921178, \
      0.6235459955536755, \
      0.6235459955536756, \
      0.2725158177734296, \
      0.2725158177734296, \
      0.0051263891023823, \
      0.0051263891023823, \
      0.7223577931241879, \
      0.7223577931241879 ] )

  w = np.array ( [ \
      0.0339800182934158, \
      0.0119972009644474, \
      0.0119972009644474, \
      0.0119972009644474, \
      0.0291392425596000, \
      0.0291392425596000, \
      0.0291392425596000, \
      0.0278009837652267, \
      0.0278009837652267, \
      0.0278009837652267, \
      0.0030261685517696, \
      0.0030261685517696, \
      0.0030261685517696, \
      0.0120895199057969, \
      0.0120895199057969, \
      0.0120895199057969, \
      0.0120895199057969, \
      0.0120895199057969, \
      0.0120895199057969, \
      0.0074827005525828, \
      0.0074827005525828, \
      0.0074827005525828, \
      0.0074827005525828, \
      0.0074827005525828, \
      0.0074827005525828, \
      0.0173206380704242, \
      0.0173206380704242, \
      0.0173206380704242, \
      0.0173206380704242, \
      0.0173206380704242, \
      0.0173206380704242, \
      0.0047953405017716, \
      0.0047953405017716, \
      0.0047953405017716, \
      0.0047953405017716, \
      0.0047953405017716, \
      0.0047953405017716 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule14 ( ):

#*****************************************************************************80
#
## rule14() returns the rule of precision 14.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.1772055324125434, \
      0.6455889351749131, \
      0.1772055324125434, \
      0.4176447193404539, \
      0.1647105613190922, \
      0.4176447193404539, \
      0.0617998830908726, \
      0.8764002338182548, \
      0.0617998830908726, \
      0.4889639103621786, \
      0.0220721792756427, \
      0.4889639103621786, \
      0.2734775283088386, \
      0.4530449433823227, \
      0.2734775283088386, \
      0.0193909612487010, \
      0.9612180775025979, \
      0.0193909612487010, \
      0.2983728821362578, \
      0.6869801678080878, \
      0.0146469500556544, \
      0.6869801678080878, \
      0.0146469500556544, \
      0.2983728821362578, \
      0.0571247574036479, \
      0.7706085547749965, \
      0.1722666878213556, \
      0.7706085547749965, \
      0.1722666878213556, \
      0.0571247574036479, \
      0.3368614597963450, \
      0.5702222908466832, \
      0.0929162493569718, \
      0.5702222908466832, \
      0.0929162493569718, \
      0.3368614597963450, \
      0.0012683309328720, \
      0.8797571713701711, \
      0.1189744976969568, \
      0.8797571713701711, \
      0.1189744976969568, \
      0.0012683309328720 ] )

  y = np.array ( [ \
      0.6455889351749131, \
      0.1772055324125434, \
      0.1772055324125434, \
      0.1647105613190922, \
      0.4176447193404539, \
      0.4176447193404539, \
      0.8764002338182548, \
      0.0617998830908726, \
      0.0617998830908726, \
      0.0220721792756427, \
      0.4889639103621786, \
      0.4889639103621786, \
      0.4530449433823227, \
      0.2734775283088386, \
      0.2734775283088386, \
      0.9612180775025979, \
      0.0193909612487010, \
      0.0193909612487010, \
      0.6869801678080878, \
      0.2983728821362578, \
      0.6869801678080878, \
      0.0146469500556544, \
      0.2983728821362578, \
      0.0146469500556544, \
      0.7706085547749965, \
      0.0571247574036479, \
      0.7706085547749965, \
      0.1722666878213556, \
      0.0571247574036479, \
      0.1722666878213556, \
      0.5702222908466832, \
      0.3368614597963450, \
      0.5702222908466832, \
      0.0929162493569718, \
      0.3368614597963450, \
      0.0929162493569718, \
      0.8797571713701711, \
      0.0012683309328720, \
      0.8797571713701711, \
      0.1189744976969568, \
      0.0012683309328720, \
      0.1189744976969568 ] )

  z = np.array ( [ \
      0.1772055324125434, \
      0.1772055324125434, \
      0.6455889351749131, \
      0.4176447193404538, \
      0.4176447193404538, \
      0.1647105613190921, \
      0.0617998830908726, \
      0.0617998830908726, \
      0.8764002338182548, \
      0.4889639103621787, \
      0.4889639103621787, \
      0.0220721792756428, \
      0.2734775283088386, \
      0.2734775283088386, \
      0.4530449433823227, \
      0.0193909612487010, \
      0.0193909612487010, \
      0.9612180775025978, \
      0.0146469500556544, \
      0.0146469500556544, \
      0.2983728821362578, \
      0.2983728821362578, \
      0.6869801678080878, \
      0.6869801678080878, \
      0.1722666878213556, \
      0.1722666878213556, \
      0.0571247574036480, \
      0.0571247574036480, \
      0.7706085547749966, \
      0.7706085547749965, \
      0.0929162493569718, \
      0.0929162493569718, \
      0.3368614597963450, \
      0.3368614597963450, \
      0.5702222908466832, \
      0.5702222908466832, \
      0.1189744976969569, \
      0.1189744976969569, \
      0.0012683309328720, \
      0.0012683309328721, \
      0.8797571713701711, \
      0.8797571713701711 ] )

  w = np.array ( [ \
      0.0210812943684965, \
      0.0210812943684965, \
      0.0210812943684965, \
      0.0163941767720627, \
      0.0163941767720627, \
      0.0163941767720627, \
      0.0072168498348883, \
      0.0072168498348883, \
      0.0072168498348883, \
      0.0109417906847144, \
      0.0109417906847144, \
      0.0109417906847144, \
      0.0258870522536458, \
      0.0258870522536458, \
      0.0258870522536458, \
      0.0024617018012000, \
      0.0024617018012000, \
      0.0024617018012000, \
      0.0072181540567669, \
      0.0072181540567669, \
      0.0072181540567669, \
      0.0072181540567669, \
      0.0072181540567669, \
      0.0072181540567669, \
      0.0123328766062818, \
      0.0123328766062818, \
      0.0123328766062818, \
      0.0123328766062818, \
      0.0123328766062818, \
      0.0123328766062818, \
      0.0192857553935303, \
      0.0192857553935303, \
      0.0192857553935303, \
      0.0192857553935303, \
      0.0192857553935303, \
      0.0192857553935303, \
      0.0025051144192503, \
      0.0025051144192503, \
      0.0025051144192503, \
      0.0025051144192503, \
      0.0025051144192503, \
      0.0025051144192503 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule15 ( ):

#*****************************************************************************80
#
## rule15() returns the rule of precision 15.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#    We suppose we are given a triangle T with vertices A, B, C.
#    We call a rule with n points, returning barycentric coordinates
#    a, b, c, and weights w.  Then the integral I of f(x,y) over T is 
#    approximated by Q as follows:
#
#    (x,y) = a(1:n) * A + b(1:n) * B + c(1:n) * C
#    Q = area(T) * sum ( 1 <= i <= n ) w(i) * f(x(i),y(i)) 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real a(n), b(n), c(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights, which sum to 1.
#
  import numpy as np

  a = np.array ( [ \
      0.3333333333333334, \
      0.4053622141339755, \
      0.1892755717320491, \
      0.4053622141339755, \
      0.0701735528999860, \
      0.8596528942000279, \
      0.0701735528999860, \
      0.4741706814380198, \
      0.0516586371239604, \
      0.4741706814380198, \
      0.2263787134203496, \
      0.5472425731593008, \
      0.2263787134203496, \
      0.4949969567691262, \
      0.0100060864617476, \
      0.4949969567691262, \
      0.0158117262509886, \
      0.9683765474980227, \
      0.0158117262509886, \
      0.0183761123856811, \
      0.6669756448018681, \
      0.3146482428124509, \
      0.6669756448018681, \
      0.3146482428124509, \
      0.0183761123856811, \
      0.0091392370373084, \
      0.9199121577262361, \
      0.0709486052364555, \
      0.9199121577262361, \
      0.0709486052364555, \
      0.0091392370373084, \
      0.1905355894763939, \
      0.7152223569314506, \
      0.0942420535921554, \
      0.7152223569314506, \
      0.0942420535921554, \
      0.1905355894763939, \
      0.1680686452224144, \
      0.8132926410494192, \
      0.0186387137281664, \
      0.8132926410494192, \
      0.0186387137281664, \
      0.1680686452224144, \
      0.3389506114752772, \
      0.5652526648771142, \
      0.0957967236476086, \
      0.5652526648771142, \
      0.0957967236476086, \
      0.3389506114752772 ] )

  b = np.array ( [ \
      0.3333333333333334, \
      0.1892755717320491, \
      0.4053622141339755, \
      0.4053622141339755, \
      0.8596528942000279, \
      0.0701735528999860, \
      0.0701735528999860, \
      0.0516586371239604, \
      0.4741706814380198, \
      0.4741706814380198, \
      0.5472425731593008, \
      0.2263787134203496, \
      0.2263787134203496, \
      0.0100060864617476, \
      0.4949969567691262, \
      0.4949969567691262, \
      0.9683765474980227, \
      0.0158117262509886, \
      0.0158117262509886, \
      0.6669756448018681, \
      0.0183761123856811, \
      0.6669756448018681, \
      0.3146482428124509, \
      0.0183761123856811, \
      0.3146482428124509, \
      0.9199121577262361, \
      0.0091392370373084, \
      0.9199121577262361, \
      0.0709486052364555, \
      0.0091392370373084, \
      0.0709486052364555, \
      0.7152223569314506, \
      0.1905355894763939, \
      0.7152223569314506, \
      0.0942420535921554, \
      0.1905355894763939, \
      0.0942420535921554, \
      0.8132926410494192, \
      0.1680686452224144, \
      0.8132926410494192, \
      0.0186387137281664, \
      0.1680686452224144, \
      0.0186387137281664, \
      0.5652526648771142, \
      0.3389506114752772, \
      0.5652526648771142, \
      0.0957967236476086, \
      0.3389506114752772, \
      0.0957967236476086 ] )

  c = np.array ( [ \
      0.3333333333333333, \
      0.4053622141339755, \
      0.4053622141339754, \
      0.1892755717320491, \
      0.0701735528999861, \
      0.0701735528999861, \
      0.8596528942000279, \
      0.4741706814380198, \
      0.4741706814380198, \
      0.0516586371239605, \
      0.2263787134203495, \
      0.2263787134203496, \
      0.5472425731593007, \
      0.4949969567691263, \
      0.4949969567691262, \
      0.0100060864617477, \
      0.0158117262509886, \
      0.0158117262509886, \
      0.9683765474980226, \
      0.3146482428124507, \
      0.3146482428124508, \
      0.0183761123856810, \
      0.0183761123856810, \
      0.6669756448018680, \
      0.6669756448018680, \
      0.0709486052364554, \
      0.0709486052364555, \
      0.0091392370373083, \
      0.0091392370373083, \
      0.9199121577262361, \
      0.9199121577262360, \
      0.0942420535921554, \
      0.0942420535921554, \
      0.1905355894763940, \
      0.1905355894763940, \
      0.7152223569314508, \
      0.7152223569314506, \
      0.0186387137281664, \
      0.0186387137281664, \
      0.1680686452224144, \
      0.1680686452224144, \
      0.8132926410494192, \
      0.8132926410494192, \
      0.0957967236476086, \
      0.0957967236476086, \
      0.3389506114752772, \
      0.3389506114752772, \
      0.5652526648771142, \
      0.5652526648771142 ] )

  w = np.array ( [ \
      0.0443353873821841, \
      0.0427137815714606, \
      0.0427137815714606, \
      0.0427137815714606, \
      0.0164447375626252, \
      0.0164447375626252, \
      0.0164447375626252, \
      0.0173961480007634, \
      0.0173961480007634, \
      0.0173961480007634, \
      0.0467833617287096, \
      0.0467833617287096, \
      0.0467833617287096, \
      0.0095738461824601, \
      0.0095738461824601, \
      0.0095738461824601, \
      0.0029607746379054, \
      0.0029607746379054, \
      0.0029607746379054, \
      0.0156025728305760, \
      0.0156025728305760, \
      0.0156025728305760, \
      0.0156025728305760, \
      0.0156025728305760, \
      0.0156025728305760, \
      0.0040298533720181, \
      0.0040298533720181, \
      0.0040298533720181, \
      0.0040298533720181, \
      0.0040298533720181, \
      0.0040298533720181, \
      0.0287205869252013, \
      0.0287205869252013, \
      0.0287205869252013, \
      0.0287205869252013, \
      0.0287205869252013, \
      0.0287205869252013, \
      0.0116726211815758, \
      0.0116726211815758, \
      0.0116726211815758, \
      0.0116726211815758, \
      0.0116726211815758, \
      0.0116726211815758, \
      0.0313154762849693, \
      0.0313154762849693, \
      0.0313154762849693, \
      0.0313154762849693, \
      0.0313154762849693, \
      0.0313154762849693 ] )

  return a, b, c, w

def rule16 ( ):

#*****************************************************************************80
#
## rule16() returns the rule of precision 16.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.3333333333333334, \
      0.2459900704671417, \
      0.5080198590657166, \
      0.2459900704671417, \
      0.4155848968854205, \
      0.1688302062291590, \
      0.4155848968854205, \
      0.0853555665867003, \
      0.8292888668265994, \
      0.0853555665867003, \
      0.1619186441912712, \
      0.6761627116174576, \
      0.1619186441912712, \
      0.5000000000000000, \
      0.0000000000000000, \
      0.5000000000000000, \
      0.4752807275459421, \
      0.0494385449081158, \
      0.4752807275459421, \
      0.0547551749147031, \
      0.7541700614447677, \
      0.1910747636405291, \
      0.7541700614447677, \
      0.1910747636405291, \
      0.0547551749147031, \
      0.0232034277688137, \
      0.9682443680309587, \
      0.0085522042002276, \
      0.9682443680309587, \
      0.0085522042002276, \
      0.0232034277688137, \
      0.0189317782804059, \
      0.6493036982454464, \
      0.3317645234741476, \
      0.6493036982454464, \
      0.3317645234741476, \
      0.0189317782804059, \
      0.0190301297436974, \
      0.9002737032704295, \
      0.0806961669858730, \
      0.9002737032704295, \
      0.0806961669858730, \
      0.0190301297436974, \
      0.1026061902393981, \
      0.5891488405642479, \
      0.3082449691963540, \
      0.5891488405642479, \
      0.3082449691963540, \
      0.1026061902393981, \
      0.0059363500168222, \
      0.8066218674993957, \
      0.1874417824837821, \
      0.8066218674993957, \
      0.1874417824837821, \
      0.0059363500168222 ] )

  y = np.array ( [ \
      0.3333333333333334, \
      0.5080198590657166, \
      0.2459900704671417, \
      0.2459900704671417, \
      0.1688302062291590, \
      0.4155848968854205, \
      0.4155848968854205, \
      0.8292888668265994, \
      0.0853555665867003, \
      0.0853555665867003, \
      0.6761627116174576, \
      0.1619186441912712, \
      0.1619186441912712, \
      0.0000000000000000, \
      0.5000000000000000, \
      0.5000000000000000, \
      0.0494385449081158, \
      0.4752807275459421, \
      0.4752807275459421, \
      0.7541700614447677, \
      0.0547551749147031, \
      0.7541700614447677, \
      0.1910747636405291, \
      0.0547551749147031, \
      0.1910747636405291, \
      0.9682443680309587, \
      0.0232034277688137, \
      0.9682443680309587, \
      0.0085522042002276, \
      0.0232034277688137, \
      0.0085522042002276, \
      0.6493036982454464, \
      0.0189317782804059, \
      0.6493036982454464, \
      0.3317645234741476, \
      0.0189317782804059, \
      0.3317645234741476, \
      0.9002737032704295, \
      0.0190301297436974, \
      0.9002737032704295, \
      0.0806961669858730, \
      0.0190301297436974, \
      0.0806961669858730, \
      0.5891488405642479, \
      0.1026061902393981, \
      0.5891488405642479, \
      0.3082449691963540, \
      0.1026061902393981, \
      0.3082449691963540, \
      0.8066218674993957, \
      0.0059363500168222, \
      0.8066218674993957, \
      0.1874417824837821, \
      0.0059363500168222, \
      0.1874417824837821 ] )

  z = np.array ( [ \
      0.3333333333333333, \
      0.2459900704671417, \
      0.2459900704671417, \
      0.5080198590657166, \
      0.4155848968854205, \
      0.4155848968854206, \
      0.1688302062291590, \
      0.0853555665867003, \
      0.0853555665867002, \
      0.8292888668265994, \
      0.1619186441912712, \
      0.1619186441912712, \
      0.6761627116174576, \
      0.5000000000000000, \
      0.5000000000000000, \
      0.0000000000000000, \
      0.4752807275459421, \
      0.4752807275459421, \
      0.0494385449081158, \
      0.1910747636405292, \
      0.1910747636405292, \
      0.0547551749147033, \
      0.0547551749147032, \
      0.7541700614447679, \
      0.7541700614447679, \
      0.0085522042002275, \
      0.0085522042002276, \
      0.0232034277688137, \
      0.0232034277688137, \
      0.9682443680309587, \
      0.9682443680309586, \
      0.3317645234741476, \
      0.3317645234741476, \
      0.0189317782804059, \
      0.0189317782804059, \
      0.6493036982454464, \
      0.6493036982454464, \
      0.0806961669858730, \
      0.0806961669858730, \
      0.0190301297436974, \
      0.0190301297436975, \
      0.9002737032704295, \
      0.9002737032704295, \
      0.3082449691963540, \
      0.3082449691963540, \
      0.1026061902393981, \
      0.1026061902393981, \
      0.5891488405642479, \
      0.5891488405642479, \
      0.1874417824837821, \
      0.1874417824837821, \
      0.0059363500168222, \
      0.0059363500168222, \
      0.8066218674993957, \
      0.8066218674993957 ] )

  w = np.array ( [ \
      0.0226322830369094, \
      0.0205464615718495, \
      0.0205464615718495, \
      0.0205464615718495, \
      0.0203559166562127, \
      0.0203559166562127, \
      0.0203559166562127, \
      0.0073908173451122, \
      0.0073908173451122, \
      0.0073908173451122, \
      0.0147092048494940, \
      0.0147092048494940, \
      0.0147092048494940, \
      0.0022092731560753, \
      0.0022092731560753, \
      0.0022092731560753, \
      0.0129871666491386, \
      0.0129871666491386, \
      0.0129871666491386, \
      0.0094691362322078, \
      0.0094691362322078, \
      0.0094691362322078, \
      0.0094691362322078, \
      0.0094691362322078, \
      0.0094691362322078, \
      0.0008272333574175, \
      0.0008272333574175, \
      0.0008272333574175, \
      0.0008272333574175, \
      0.0008272333574175, \
      0.0008272333574175, \
      0.0075043008921429, \
      0.0075043008921429, \
      0.0075043008921429, \
      0.0075043008921429, \
      0.0075043008921429, \
      0.0075043008921429, \
      0.0039737969666962, \
      0.0039737969666962, \
      0.0039737969666962, \
      0.0039737969666962, \
      0.0039737969666962, \
      0.0039737969666962, \
      0.0159918050396850, \
      0.0159918050396850, \
      0.0159918050396850, \
      0.0159918050396850, \
      0.0159918050396850, \
      0.0159918050396850, \
      0.0026955935584244, \
      0.0026955935584244, \
      0.0026955935584244, \
      0.0026955935584244, \
      0.0026955935584244, \
      0.0026955935584244 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule17 ( ):

#*****************************************************************************80
#
## rule17() returns the rule of precision 17.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.4171034443615992, \
      0.1657931112768016, \
      0.4171034443615992, \
      0.0147554916607540, \
      0.9704890166784921, \
      0.0147554916607540, \
      0.4655978716188903, \
      0.0688042567622194, \
      0.4655978716188903, \
      0.1803581162663706, \
      0.6392837674672588, \
      0.1803581162663706, \
      0.0666540634795969, \
      0.8666918730408062, \
      0.0666540634795969, \
      0.2857065024365866, \
      0.4285869951268267, \
      0.2857065024365866, \
      0.0160176423621193, \
      0.8247900701650881, \
      0.1591922874727927, \
      0.8247900701650881, \
      0.1591922874727927, \
      0.0160176423621193, \
      0.3062815917461865, \
      0.6263690303864522, \
      0.0673493778673612, \
      0.6263690303864522, \
      0.0673493778673612, \
      0.3062815917461865, \
      0.0132296727600869, \
      0.5712948679446841, \
      0.4154754592952291, \
      0.5712948679446841, \
      0.4154754592952291, \
      0.0132296727600869, \
      0.0780423405682824, \
      0.7532351459364581, \
      0.1687225134952595, \
      0.7532351459364581, \
      0.1687225134952595, \
      0.0780423405682824, \
      0.0131358708340027, \
      0.7150722591106424, \
      0.2717918700553549, \
      0.7150722591106424, \
      0.2717918700553549, \
      0.0131358708340027, \
      0.0115751759031806, \
      0.9159193532978169, \
      0.0725054707990024, \
      0.9159193532978169, \
      0.0725054707990024, \
      0.0115751759031806, \
      0.1575054779268699, \
      0.5432755795961598, \
      0.2992189424769703, \
      0.5432755795961598, \
      0.2992189424769703, \
      0.1575054779268699 ] )

  y = np.array ( [ \
      0.1657931112768016, \
      0.4171034443615992, \
      0.4171034443615992, \
      0.9704890166784921, \
      0.0147554916607540, \
      0.0147554916607540, \
      0.0688042567622194, \
      0.4655978716188903, \
      0.4655978716188903, \
      0.6392837674672588, \
      0.1803581162663706, \
      0.1803581162663706, \
      0.8666918730408062, \
      0.0666540634795969, \
      0.0666540634795969, \
      0.4285869951268267, \
      0.2857065024365866, \
      0.2857065024365866, \
      0.8247900701650881, \
      0.0160176423621193, \
      0.8247900701650881, \
      0.1591922874727927, \
      0.0160176423621193, \
      0.1591922874727927, \
      0.6263690303864522, \
      0.3062815917461865, \
      0.6263690303864522, \
      0.0673493778673612, \
      0.3062815917461865, \
      0.0673493778673612, \
      0.5712948679446841, \
      0.0132296727600869, \
      0.5712948679446841, \
      0.4154754592952291, \
      0.0132296727600869, \
      0.4154754592952291, \
      0.7532351459364581, \
      0.0780423405682824, \
      0.7532351459364581, \
      0.1687225134952595, \
      0.0780423405682824, \
      0.1687225134952595, \
      0.7150722591106424, \
      0.0131358708340027, \
      0.7150722591106424, \
      0.2717918700553549, \
      0.0131358708340027, \
      0.2717918700553549, \
      0.9159193532978169, \
      0.0115751759031806, \
      0.9159193532978169, \
      0.0725054707990024, \
      0.0115751759031806, \
      0.0725054707990024, \
      0.5432755795961598, \
      0.1575054779268699, \
      0.5432755795961598, \
      0.2992189424769703, \
      0.1575054779268699, \
      0.2992189424769703 ] )

  z = np.array ( [ \
      0.4171034443615992, \
      0.4171034443615992, \
      0.1657931112768016, \
      0.0147554916607540, \
      0.0147554916607540, \
      0.9704890166784921, \
      0.4655978716188903, \
      0.4655978716188903, \
      0.0688042567622194, \
      0.1803581162663707, \
      0.1803581162663706, \
      0.6392837674672589, \
      0.0666540634795969, \
      0.0666540634795969, \
      0.8666918730408062, \
      0.2857065024365867, \
      0.2857065024365866, \
      0.4285869951268268, \
      0.1591922874727927, \
      0.1591922874727926, \
      0.0160176423621192, \
      0.0160176423621192, \
      0.8247900701650881, \
      0.8247900701650881, \
      0.0673493778673613, \
      0.0673493778673613, \
      0.3062815917461866, \
      0.3062815917461866, \
      0.6263690303864523, \
      0.6263690303864523, \
      0.4154754592952290, \
      0.4154754592952290, \
      0.0132296727600869, \
      0.0132296727600869, \
      0.5712948679446841, \
      0.5712948679446841, \
      0.1687225134952595, \
      0.1687225134952595, \
      0.0780423405682824, \
      0.0780423405682824, \
      0.7532351459364581, \
      0.7532351459364581, \
      0.2717918700553549, \
      0.2717918700553549, \
      0.0131358708340027, \
      0.0131358708340027, \
      0.7150722591106424, \
      0.7150722591106424, \
      0.0725054707990025, \
      0.0725054707990024, \
      0.0115751759031806, \
      0.0115751759031806, \
      0.9159193532978169, \
      0.9159193532978169, \
      0.2992189424769703, \
      0.2992189424769703, \
      0.1575054779268699, \
      0.1575054779268699, \
      0.5432755795961597, \
      0.5432755795961598 ] )

  w = np.array ( [ \
      0.0136554632640511, \
      0.0136554632640511, \
      0.0136554632640511, \
      0.0013869437888188, \
      0.0013869437888188, \
      0.0013869437888188, \
      0.0125097254752487, \
      0.0125097254752487, \
      0.0125097254752487, \
      0.0131563152940090, \
      0.0131563152940090, \
      0.0131563152940090, \
      0.0062295004011527, \
      0.0062295004011527, \
      0.0062295004011527, \
      0.0188581185763976, \
      0.0188581185763976, \
      0.0188581185763976, \
      0.0039891501029648, \
      0.0039891501029648, \
      0.0039891501029648, \
      0.0039891501029648, \
      0.0039891501029648, \
      0.0039891501029648, \
      0.0112438862733455, \
      0.0112438862733455, \
      0.0112438862733455, \
      0.0112438862733455, \
      0.0112438862733455, \
      0.0112438862733455, \
      0.0051992199779198, \
      0.0051992199779198, \
      0.0051992199779198, \
      0.0051992199779198, \
      0.0051992199779198, \
      0.0051992199779198, \
      0.0102789491602273, \
      0.0102789491602273, \
      0.0102789491602273, \
      0.0102789491602273, \
      0.0102789491602273, \
      0.0102789491602273, \
      0.0043461072505006, \
      0.0043461072505006, \
      0.0043461072505006, \
      0.0043461072505006, \
      0.0043461072505006, \
      0.0043461072505006, \
      0.0022921742008679, \
      0.0022921742008679, \
      0.0022921742008679, \
      0.0022921742008679, \
      0.0022921742008679, \
      0.0022921742008679, \
      0.0130858129676685, \
      0.0130858129676685, \
      0.0130858129676685, \
      0.0130858129676685, \
      0.0130858129676685, \
      0.0130858129676685 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule18 ( ):

#*****************************************************************************80
#
## rule18() returns the rule of precision 18.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.3333333333333334, \
      0.3999556280675762, \
      0.2000887438648475, \
      0.3999556280675762, \
      0.4875803015748695, \
      0.0248393968502609, \
      0.4875803015748695, \
      0.4618095064064492, \
      0.0763809871871015, \
      0.4618095064064492, \
      0.2422647025142720, \
      0.5154705949714561, \
      0.2422647025142720, \
      0.0388302560886856, \
      0.9223394878226288, \
      0.0388302560886856, \
      0.0919477421216432, \
      0.8161045157567136, \
      0.0919477421216432, \
      0.0458049158598608, \
      0.7703723762146752, \
      0.1838227079254640, \
      0.7703723762146752, \
      0.1838227079254640, \
      0.0458049158598608, \
      0.2063492574338379, \
      0.6709539851942345, \
      0.1226967573719275, \
      0.6709539851942345, \
      0.1226967573719275, \
      0.2063492574338379, \
      0.0038976110334734, \
      0.6004189546342569, \
      0.3956834343322697, \
      0.6004189546342569, \
      0.3956834343322697, \
      0.0038976110334734, \
      0.0134620167414450, \
      0.8783421894675217, \
      0.1081957937910333, \
      0.8783421894675217, \
      0.1081957937910333, \
      0.0134620167414450, \
      0.0402602834699081, \
      0.6399880920047146, \
      0.3197516245253773, \
      0.6399880920047146, \
      0.3197516245253773, \
      0.0402602834699081, \
      0.0052983351866098, \
      0.7589294798551984, \
      0.2357721849581917, \
      0.7589294798551984, \
      0.2357721849581917, \
      0.0052983351866098, \
      0.0005483600420423, \
      0.9723607289627957, \
      0.0270909109951620, \
      0.9723607289627957, \
      0.0270909109951620, \
      0.0005483600420423, \
      0.1205876951639246, \
      0.5459187753861946, \
      0.3334935294498808, \
      0.5459187753861946, \
      0.3334935294498808, \
      0.1205876951639246 ] )

  y = np.array ( [ \
      0.3333333333333334, \
      0.2000887438648475, \
      0.3999556280675762, \
      0.3999556280675762, \
      0.0248393968502609, \
      0.4875803015748695, \
      0.4875803015748695, \
      0.0763809871871015, \
      0.4618095064064492, \
      0.4618095064064492, \
      0.5154705949714561, \
      0.2422647025142720, \
      0.2422647025142720, \
      0.9223394878226288, \
      0.0388302560886856, \
      0.0388302560886856, \
      0.8161045157567136, \
      0.0919477421216432, \
      0.0919477421216432, \
      0.7703723762146752, \
      0.0458049158598608, \
      0.7703723762146752, \
      0.1838227079254640, \
      0.0458049158598608, \
      0.1838227079254640, \
      0.6709539851942345, \
      0.2063492574338379, \
      0.6709539851942345, \
      0.1226967573719275, \
      0.2063492574338379, \
      0.1226967573719275, \
      0.6004189546342569, \
      0.0038976110334734, \
      0.6004189546342569, \
      0.3956834343322697, \
      0.0038976110334734, \
      0.3956834343322697, \
      0.8783421894675217, \
      0.0134620167414450, \
      0.8783421894675217, \
      0.1081957937910333, \
      0.0134620167414450, \
      0.1081957937910333, \
      0.6399880920047146, \
      0.0402602834699081, \
      0.6399880920047146, \
      0.3197516245253773, \
      0.0402602834699081, \
      0.3197516245253773, \
      0.7589294798551984, \
      0.0052983351866098, \
      0.7589294798551984, \
      0.2357721849581917, \
      0.0052983351866098, \
      0.2357721849581917, \
      0.9723607289627957, \
      0.0005483600420423, \
      0.9723607289627957, \
      0.0270909109951620, \
      0.0005483600420423, \
      0.0270909109951620, \
      0.5459187753861946, \
      0.1205876951639246, \
      0.5459187753861946, \
      0.3334935294498808, \
      0.1205876951639246, \
      0.3334935294498808 ] )

  z = np.array ( [ \
      0.3333333333333333, \
      0.3999556280675762, \
      0.3999556280675762, \
      0.2000887438648475, \
      0.4875803015748696, \
      0.4875803015748695, \
      0.0248393968502609, \
      0.4618095064064492, \
      0.4618095064064492, \
      0.0763809871871015, \
      0.2422647025142720, \
      0.2422647025142720, \
      0.5154705949714562, \
      0.0388302560886856, \
      0.0388302560886856, \
      0.9223394878226288, \
      0.0919477421216431, \
      0.0919477421216432, \
      0.8161045157567135, \
      0.1838227079254640, \
      0.1838227079254640, \
      0.0458049158598608, \
      0.0458049158598607, \
      0.7703723762146752, \
      0.7703723762146752, \
      0.1226967573719275, \
      0.1226967573719275, \
      0.2063492574338379, \
      0.2063492574338379, \
      0.6709539851942345, \
      0.6709539851942345, \
      0.3956834343322697, \
      0.3956834343322698, \
      0.0038976110334734, \
      0.0038976110334734, \
      0.6004189546342569, \
      0.6004189546342569, \
      0.1081957937910333, \
      0.1081957937910333, \
      0.0134620167414450, \
      0.0134620167414450, \
      0.8783421894675217, \
      0.8783421894675217, \
      0.3197516245253773, \
      0.3197516245253773, \
      0.0402602834699081, \
      0.0402602834699081, \
      0.6399880920047146, \
      0.6399880920047146, \
      0.2357721849581917, \
      0.2357721849581918, \
      0.0052983351866098, \
      0.0052983351866098, \
      0.7589294798551984, \
      0.7589294798551984, \
      0.0270909109951619, \
      0.0270909109951620, \
      0.0005483600420423, \
      0.0005483600420423, \
      0.9723607289627956, \
      0.9723607289627956, \
      0.3334935294498808, \
      0.3334935294498808, \
      0.1205876951639246, \
      0.1205876951639246, \
      0.5459187753861946, \
      0.5459187753861946 ] )

  w = np.array ( [ \
      0.0181778676507133, \
      0.0166522350166951, \
      0.0166522350166951, \
      0.0166522350166951, \
      0.0060233238169999, \
      0.0060233238169999, \
      0.0060233238169999, \
      0.0094745857533894, \
      0.0094745857533894, \
      0.0094745857533894, \
      0.0182375447044718, \
      0.0182375447044718, \
      0.0182375447044718, \
      0.0035646630098595, \
      0.0035646630098595, \
      0.0035646630098595, \
      0.0082795799760016, \
      0.0082795799760016, \
      0.0082795799760016, \
      0.0068798081174711, \
      0.0068798081174711, \
      0.0068798081174711, \
      0.0068798081174711, \
      0.0068798081174711, \
      0.0068798081174711, \
      0.0118909554500764, \
      0.0118909554500764, \
      0.0118909554500764, \
      0.0118909554500764, \
      0.0118909554500764, \
      0.0118909554500764, \
      0.0022652672511285, \
      0.0022652672511285, \
      0.0022652672511285, \
      0.0022652672511285, \
      0.0022652672511285, \
      0.0022652672511285, \
      0.0034200550598036, \
      0.0034200550598036, \
      0.0034200550598036, \
      0.0034200550598036, \
      0.0034200550598036, \
      0.0034200550598036, \
      0.0088737445510102, \
      0.0088737445510102, \
      0.0088737445510102, \
      0.0088737445510102, \
      0.0088737445510102, \
      0.0088737445510102, \
      0.0025053304372899, \
      0.0025053304372899, \
      0.0025053304372899, \
      0.0025053304372899, \
      0.0025053304372899, \
      0.0025053304372899, \
      0.0006114740634805, \
      0.0006114740634805, \
      0.0006114740634805, \
      0.0006114740634805, \
      0.0006114740634805, \
      0.0006114740634805, \
      0.0127410876559122, \
      0.0127410876559122, \
      0.0127410876559122, \
      0.0127410876559122, \
      0.0127410876559122, \
      0.0127410876559122 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule19 ( ):

#*****************************************************************************80
#
## rule19() returns the rule of precision 19.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.3333333333333334, \
      0.0525238903512090, \
      0.8949522192975821, \
      0.0525238903512090, \
      0.4925126750413369, \
      0.0149746499173263, \
      0.4925126750413369, \
      0.1114488733230214, \
      0.7771022533539573, \
      0.1114488733230214, \
      0.4591942010395437, \
      0.0816115979209127, \
      0.4591942010395437, \
      0.4039697225519012, \
      0.1920605548961976, \
      0.4039697225519012, \
      0.1781701047817643, \
      0.6436597904364714, \
      0.1781701047817643, \
      0.0116394611837894, \
      0.9767210776324211, \
      0.0116394611837894, \
      0.2551616329136077, \
      0.4896767341727846, \
      0.2551616329136077, \
      0.1306976762680324, \
      0.8301564644002754, \
      0.0391458593316922, \
      0.8301564644002754, \
      0.0391458593316922, \
      0.1306976762680324, \
      0.3113176298095413, \
      0.5593698057203009, \
      0.1293125644701578, \
      0.5593698057203009, \
      0.1293125644701578, \
      0.3113176298095413, \
      0.0020689258966048, \
      0.6333132931287841, \
      0.3646177809746111, \
      0.6333132931287841, \
      0.3646177809746111, \
      0.0020689258966048, \
      0.0745602946016267, \
      0.7040048199660421, \
      0.2214348854323312, \
      0.7040048199660421, \
      0.2214348854323312, \
      0.0745602946016267, \
      0.0050072882573545, \
      0.8525669543768892, \
      0.1424257573657563, \
      0.8525669543768892, \
      0.1424257573657563, \
      0.0050072882573545, \
      0.0408880111960169, \
      0.6050839790687079, \
      0.3540280097352752, \
      0.6050839790687079, \
      0.3540280097352752, \
      0.0408880111960169, \
      0.2418945789605796, \
      0.7431813689574364, \
      0.0149240520819841, \
      0.7431813689574364, \
      0.0149240520819841, \
      0.2418945789605796, \
      0.0600862753223067, \
      0.9301376988768051, \
      0.0097760258008882, \
      0.9301376988768051, \
      0.0097760258008882, \
      0.0600862753223067 ] )

  y = np.array ( [ \
      0.3333333333333334, \
      0.8949522192975821, \
      0.0525238903512090, \
      0.0525238903512090, \
      0.0149746499173263, \
      0.4925126750413369, \
      0.4925126750413369, \
      0.7771022533539573, \
      0.1114488733230214, \
      0.1114488733230214, \
      0.0816115979209127, \
      0.4591942010395437, \
      0.4591942010395437, \
      0.1920605548961976, \
      0.4039697225519012, \
      0.4039697225519012, \
      0.6436597904364714, \
      0.1781701047817643, \
      0.1781701047817643, \
      0.9767210776324211, \
      0.0116394611837894, \
      0.0116394611837894, \
      0.4896767341727846, \
      0.2551616329136077, \
      0.2551616329136077, \
      0.8301564644002754, \
      0.1306976762680324, \
      0.8301564644002754, \
      0.0391458593316922, \
      0.1306976762680324, \
      0.0391458593316922, \
      0.5593698057203009, \
      0.3113176298095413, \
      0.5593698057203009, \
      0.1293125644701578, \
      0.3113176298095413, \
      0.1293125644701578, \
      0.6333132931287841, \
      0.0020689258966048, \
      0.6333132931287841, \
      0.3646177809746111, \
      0.0020689258966048, \
      0.3646177809746111, \
      0.7040048199660421, \
      0.0745602946016267, \
      0.7040048199660421, \
      0.2214348854323312, \
      0.0745602946016267, \
      0.2214348854323312, \
      0.8525669543768892, \
      0.0050072882573545, \
      0.8525669543768892, \
      0.1424257573657563, \
      0.0050072882573545, \
      0.1424257573657563, \
      0.6050839790687079, \
      0.0408880111960169, \
      0.6050839790687079, \
      0.3540280097352752, \
      0.0408880111960169, \
      0.3540280097352752, \
      0.7431813689574364, \
      0.2418945789605796, \
      0.7431813689574364, \
      0.0149240520819841, \
      0.2418945789605796, \
      0.0149240520819841, \
      0.9301376988768051, \
      0.0600862753223067, \
      0.9301376988768051, \
      0.0097760258008882, \
      0.0600862753223067, \
      0.0097760258008882 ] )

  z = np.array ( [ \
      0.3333333333333333, \
      0.0525238903512090, \
      0.0525238903512090, \
      0.8949522192975821, \
      0.4925126750413368, \
      0.4925126750413369, \
      0.0149746499173262, \
      0.1114488733230212, \
      0.1114488733230213, \
      0.7771022533539571, \
      0.4591942010395437, \
      0.4591942010395437, \
      0.0816115979209127, \
      0.4039697225519012, \
      0.4039697225519012, \
      0.1920605548961976, \
      0.1781701047817643, \
      0.1781701047817643, \
      0.6436597904364714, \
      0.0116394611837894, \
      0.0116394611837894, \
      0.9767210776324211, \
      0.2551616329136077, \
      0.2551616329136077, \
      0.4896767341727846, \
      0.0391458593316922, \
      0.0391458593316922, \
      0.1306976762680324, \
      0.1306976762680324, \
      0.8301564644002754, \
      0.8301564644002754, \
      0.1293125644701578, \
      0.1293125644701578, \
      0.3113176298095413, \
      0.3113176298095413, \
      0.5593698057203009, \
      0.5593698057203009, \
      0.3646177809746111, \
      0.3646177809746111, \
      0.0020689258966048, \
      0.0020689258966048, \
      0.6333132931287841, \
      0.6333132931287841, \
      0.2214348854323313, \
      0.2214348854323312, \
      0.0745602946016267, \
      0.0745602946016267, \
      0.7040048199660423, \
      0.7040048199660423, \
      0.1424257573657564, \
      0.1424257573657563, \
      0.0050072882573544, \
      0.0050072882573545, \
      0.8525669543768892, \
      0.8525669543768892, \
      0.3540280097352753, \
      0.3540280097352752, \
      0.0408880111960169, \
      0.0408880111960169, \
      0.6050839790687079, \
      0.6050839790687080, \
      0.0149240520819841, \
      0.0149240520819841, \
      0.2418945789605796, \
      0.2418945789605796, \
      0.7431813689574365, \
      0.7431813689574365, \
      0.0097760258008882, \
      0.0097760258008882, \
      0.0600862753223068, \
      0.0600862753223068, \
      0.9301376988768052, \
      0.9301376988768051 ] )

  w = np.array ( [ \
      0.0172346988520062, \
      0.0035546282988991, \
      0.0035546282988991, \
      0.0035546282988991, \
      0.0051608775714721, \
      0.0051608775714721, \
      0.0051608775714721, \
      0.0076171755465091, \
      0.0076171755465091, \
      0.0076171755465091, \
      0.0114917950133708, \
      0.0114917950133708, \
      0.0114917950133708, \
      0.0157687674465775, \
      0.0157687674465775, \
      0.0157687674465775, \
      0.0123259574240954, \
      0.0123259574240954, \
      0.0123259574240954, \
      0.0008826613882214, \
      0.0008826613882214, \
      0.0008826613882214, \
      0.0158765096830015, \
      0.0158765096830015, \
      0.0158765096830015, \
      0.0048477422434275, \
      0.0048477422434275, \
      0.0048477422434275, \
      0.0048477422434275, \
      0.0048477422434275, \
      0.0048477422434275, \
      0.0131731609886954, \
      0.0131731609886954, \
      0.0131731609886954, \
      0.0131731609886954, \
      0.0131731609886954, \
      0.0131731609886954, \
      0.0016410382759179, \
      0.0016410382759179, \
      0.0016410382759179, \
      0.0016410382759179, \
      0.0016410382759179, \
      0.0016410382759179, \
      0.0090539724656062, \
      0.0090539724656062, \
      0.0090539724656062, \
      0.0090539724656062, \
      0.0090539724656062, \
      0.0090539724656062, \
      0.0014631575517351, \
      0.0014631575517351, \
      0.0014631575517351, \
      0.0014631575517351, \
      0.0014631575517351, \
      0.0014631575517351, \
      0.0080510813820121, \
      0.0080510813820121, \
      0.0080510813820121, \
      0.0080510813820121, \
      0.0080510813820121, \
      0.0080510813820121, \
      0.0042279437497682, \
      0.0042279437497682, \
      0.0042279437497682, \
      0.0042279437497682, \
      0.0042279437497682, \
      0.0042279437497682, \
      0.0016636006814297, \
      0.0016636006814297, \
      0.0016636006814297, \
      0.0016636006814297, \
      0.0016636006814297, \
      0.0016636006814297 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule20 ( ):

#*****************************************************************************80
#
## rule20() returns the rule of precision 20.
#
#  Discussion:
#
#    The data is given for the following triangle:
#
#     (0,1) 
#       |   \ 
#       |    \ 
#       |     \ 
#       |      \ 
#     (0,0)----(1,0)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 April 2023
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
#    real x(n), y(n), z(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  import numpy as np

  x = np.array ( [ \
      0.3333333333333334, \
      0.2545792676733391, \
      0.4908414646533218, \
      0.2545792676733391, \
      0.0109761410283978, \
      0.9780477179432046, \
      0.0109761410283978, \
      0.1093835967117146, \
      0.7812328065765708, \
      0.1093835967117146, \
      0.1862949977445409, \
      0.6274100045109181, \
      0.1862949977445409, \
      0.4455510569559248, \
      0.1088978860881504, \
      0.4455510569559248, \
      0.0373108805988847, \
      0.9253782388022307, \
      0.0373108805988847, \
      0.3934253478170999, \
      0.2131493043658003, \
      0.3934253478170999, \
      0.4762456115404990, \
      0.0475087769190020, \
      0.4762456115404990, \
      0.0075707805046965, \
      0.8332955118382362, \
      0.1591337076570672, \
      0.8332955118382362, \
      0.1591337076570672, \
      0.0075707805046965, \
      0.0465603649076643, \
      0.7549215028635474, \
      0.1985181322287882, \
      0.7549215028635474, \
      0.1985181322287882, \
      0.0465603649076643, \
      0.0640905856084341, \
      0.9310544767839422, \
      0.0048549376076237, \
      0.9310544767839422, \
      0.0048549376076237, \
      0.0640905856084341, \
      0.0549874791429868, \
      0.6118777035474257, \
      0.3331348173095875, \
      0.6118777035474257, \
      0.3331348173095875, \
      0.0549874791429868, \
      0.0999522962881387, \
      0.8616840189364867, \
      0.0383636847753746, \
      0.8616840189364867, \
      0.0383636847753746, \
      0.0999522962881387, \
      0.1062272047202700, \
      0.6781657378896355, \
      0.2156070573900944, \
      0.6781657378896355, \
      0.2156070573900944, \
      0.1062272047202700, \
      0.4200237588162241, \
      0.5701446928909734, \
      0.0098315482928026, \
      0.5701446928909734, \
      0.0098315482928026, \
      0.4200237588162241, \
      0.3178601238357720, \
      0.5423318041724281, \
      0.1398080719917999, \
      0.5423318041724281, \
      0.1398080719917999, \
      0.3178601238357720, \
      0.0107372128560111, \
      0.7086813757203236, \
      0.2805814114236652, \
      0.7086813757203236, \
      0.2805814114236652, \
      0.0107372128560111 ] )

  y = np.array ( [ \
      0.3333333333333334, \
      0.4908414646533218, \
      0.2545792676733391, \
      0.2545792676733391, \
      0.9780477179432046, \
      0.0109761410283978, \
      0.0109761410283978, \
      0.7812328065765708, \
      0.1093835967117146, \
      0.1093835967117146, \
      0.6274100045109181, \
      0.1862949977445409, \
      0.1862949977445409, \
      0.1088978860881504, \
      0.4455510569559248, \
      0.4455510569559248, \
      0.9253782388022307, \
      0.0373108805988847, \
      0.0373108805988847, \
      0.2131493043658003, \
      0.3934253478170999, \
      0.3934253478170999, \
      0.0475087769190020, \
      0.4762456115404990, \
      0.4762456115404990, \
      0.8332955118382362, \
      0.0075707805046965, \
      0.8332955118382362, \
      0.1591337076570672, \
      0.0075707805046965, \
      0.1591337076570672, \
      0.7549215028635474, \
      0.0465603649076643, \
      0.7549215028635474, \
      0.1985181322287882, \
      0.0465603649076643, \
      0.1985181322287882, \
      0.9310544767839422, \
      0.0640905856084341, \
      0.9310544767839422, \
      0.0048549376076237, \
      0.0640905856084341, \
      0.0048549376076237, \
      0.6118777035474257, \
      0.0549874791429868, \
      0.6118777035474257, \
      0.3331348173095875, \
      0.0549874791429868, \
      0.3331348173095875, \
      0.8616840189364867, \
      0.0999522962881387, \
      0.8616840189364867, \
      0.0383636847753746, \
      0.0999522962881387, \
      0.0383636847753746, \
      0.6781657378896355, \
      0.1062272047202700, \
      0.6781657378896355, \
      0.2156070573900944, \
      0.1062272047202700, \
      0.2156070573900944, \
      0.5701446928909734, \
      0.4200237588162241, \
      0.5701446928909734, \
      0.0098315482928026, \
      0.4200237588162241, \
      0.0098315482928026, \
      0.5423318041724281, \
      0.3178601238357720, \
      0.5423318041724281, \
      0.1398080719917999, \
      0.3178601238357720, \
      0.1398080719917999, \
      0.7086813757203236, \
      0.0107372128560111, \
      0.7086813757203236, \
      0.2805814114236652, \
      0.0107372128560111, \
      0.2805814114236652 ] )

  z = np.array ( [ \
      0.3333333333333333, \
      0.2545792676733390, \
      0.2545792676733391, \
      0.4908414646533217, \
      0.0109761410283977, \
      0.0109761410283977, \
      0.9780477179432046, \
      0.1093835967117146, \
      0.1093835967117146, \
      0.7812328065765708, \
      0.1862949977445409, \
      0.1862949977445409, \
      0.6274100045109181, \
      0.4455510569559248, \
      0.4455510569559248, \
      0.1088978860881504, \
      0.0373108805988847, \
      0.0373108805988846, \
      0.9253782388022307, \
      0.3934253478170998, \
      0.3934253478170999, \
      0.2131493043658002, \
      0.4762456115404991, \
      0.4762456115404991, \
      0.0475087769190021, \
      0.1591337076570672, \
      0.1591337076570672, \
      0.0075707805046965, \
      0.0075707805046965, \
      0.8332955118382362, \
      0.8332955118382362, \
      0.1985181322287883, \
      0.1985181322287883, \
      0.0465603649076645, \
      0.0465603649076644, \
      0.7549215028635476, \
      0.7549215028635476, \
      0.0048549376076238, \
      0.0048549376076238, \
      0.0640905856084342, \
      0.0640905856084341, \
      0.9310544767839423, \
      0.9310544767839422, \
      0.3331348173095876, \
      0.3331348173095875, \
      0.0549874791429869, \
      0.0549874791429869, \
      0.6118777035474257, \
      0.6118777035474258, \
      0.0383636847753746, \
      0.0383636847753746, \
      0.0999522962881387, \
      0.0999522962881387, \
      0.8616840189364867, \
      0.8616840189364867, \
      0.2156070573900944, \
      0.2156070573900944, \
      0.1062272047202701, \
      0.1062272047202701, \
      0.6781657378896356, \
      0.6781657378896355, \
      0.0098315482928025, \
      0.0098315482928025, \
      0.4200237588162240, \
      0.4200237588162241, \
      0.5701446928909732, \
      0.5701446928909732, \
      0.1398080719917999, \
      0.1398080719917999, \
      0.3178601238357720, \
      0.3178601238357720, \
      0.5423318041724281, \
      0.5423318041724281, \
      0.2805814114236653, \
      0.2805814114236653, \
      0.0107372128560111, \
      0.0107372128560111, \
      0.7086813757203236, \
      0.7086813757203237 ] )

  w = np.array ( [ \
      0.0139101107014531, \
      0.0140832013075202, \
      0.0140832013075202, \
      0.0140832013075202, \
      0.0007988407910666, \
      0.0007988407910666, \
      0.0007988407910666, \
      0.0078302307760745, \
      0.0078302307760745, \
      0.0078302307760745, \
      0.0091734629742529, \
      0.0091734629742529, \
      0.0091734629742529, \
      0.0094523999332324, \
      0.0094523999332324, \
      0.0094523999332324, \
      0.0021612754106656, \
      0.0021612754106656, \
      0.0021612754106656, \
      0.0137880506290705, \
      0.0137880506290705, \
      0.0137880506290705, \
      0.0071018253034084, \
      0.0071018253034084, \
      0.0071018253034084, \
      0.0022028974185585, \
      0.0022028974185585, \
      0.0022028974185585, \
      0.0022028974185585, \
      0.0022028974185585, \
      0.0022028974185585, \
      0.0059863985789547, \
      0.0059863985789547, \
      0.0059863985789547, \
      0.0059863985789547, \
      0.0059863985789547, \
      0.0059863985789547, \
      0.0011298696021259, \
      0.0011298696021259, \
      0.0011298696021259, \
      0.0011298696021259, \
      0.0011298696021259, \
      0.0011298696021259, \
      0.0086672255672193, \
      0.0086672255672193, \
      0.0086672255672193, \
      0.0086672255672193, \
      0.0086672255672193, \
      0.0086672255672193, \
      0.0041457115276139, \
      0.0041457115276139, \
      0.0041457115276139, \
      0.0041457115276139, \
      0.0041457115276139, \
      0.0041457115276139, \
      0.0077226078220992, \
      0.0077226078220992, \
      0.0077226078220992, \
      0.0077226078220992, \
      0.0077226078220992, \
      0.0077226078220992, \
      0.0036956815002553, \
      0.0036956815002553, \
      0.0036956815002553, \
      0.0036956815002553, \
      0.0036956815002553, \
      0.0036956815002553, \
      0.0116917457318277, \
      0.0116917457318277, \
      0.0116917457318277, \
      0.0116917457318277, \
      0.0116917457318277, \
      0.0116917457318277, \
      0.0035782002384577, \
      0.0035782002384577, \
      0.0035782002384577, \
      0.0035782002384577, \
      0.0035782002384577, \
      0.0035782002384577 ] )
#
#  The weights should sum to 1, not 1/2!
#
  w = w * 2.0

  return x, y, z, w

def rule_order ( p ):

#*****************************************************************************80
#
## rule_order() returns the order of a quadrature rule of given precision.
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
#    23 April 2023
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
#    integer order: the order of the rule.
#
  import numpy as np

  if ( p < 0 ):
    raise Exception ( 'rule_order(): Input "p" < 0.' )

  if ( 20 < p ):
    raise Exception ( 'rule_order(): Input 20 < "p".' )
 
  order_vec = np.array ( [ \
      1, \
      1,   3,   6,   6,   7, \
     12,  15,  16,  19,  25, \
     28,  33,  37,  42,  49, \
     55,  60,  67,  73,  79 ] )

  order = order_vec[p]

  return order

def triangle_area ( vert1, vert2, vert3 ):

#*****************************************************************************80
#
## triangle_area() returns the area of a triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU GPL license.
#
#  Modified:
#
#    22 April 2023
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    real vert1(2), vert2(2), vert3(2): the vertex coordinates.
#
#  Output:
#
#    real area: the area of the triangle.
#
  area = 0.5 * \
    ( \
        ( vert2[0] - vert1[0] ) * ( vert3[1] - vert1[1] ) \
      - ( vert3[0] - vert1[0] ) * ( vert2[1] - vert1[1] ) \
    )

  return area

def triangle_unit_area ( ):

#*****************************************************************************80
#
## triangle_unit_area() returns the area of a unit triangle.
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
#  Output:
#
#    real area: the area of the unit triangle.
#
  area = 0.5

  return area

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

def triangle_witherden_rule ( p ):

#*****************************************************************************80
#
## triangle_witherden_rule() returns a triangle quadrature rule of given precision.
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
#    integer p: the precision, 0 <= p <= 20.
#
#  Output:
#
#    integer n: the order of the rule.
#
#    real a(n), b(n), c(n): the barycentric coordinates of quadrature points.
#
#    real w(n): the quadrature weights.
#
  if ( p < 0 ): 
    raise Exception ( 'triangle_witherden_rule(): Input p < 0.' )

  if ( 20 < p ):
    raise Exception ( 'triangle_witherden_rule(): Input 20 < p.' )

  n = rule_order ( p )

  if ( p == 0 ):
    a, b, c, w = rule00 ( )
  elif ( p == 1 ):
    a, b, c, w = rule01 ( )
  elif ( p == 2 ):
    a, b, c, w = rule02 ( )
  elif ( p == 3 ):
    a, b, c, w = rule03 ( )
  elif ( p == 4 ):
    a, b, c, w = rule04 ( )
  elif ( p == 5 ):
    a, b, c, w = rule05 ( )
  elif ( p == 6 ):
    a, b, c, w = rule06 ( )
  elif ( p == 7 ):
    a, b, c, w = rule07 ( )
  elif ( p == 8 ):
    a, b, c, w = rule08 ( )
  elif ( p == 9 ):
    a, b, c, w = rule09 ( )
  elif ( p == 10 ):
    a, b, c, w = rule10 ( )
  elif ( p == 11 ):
    a, b, c, w = rule11 ( )
  elif ( p == 12 ):
    a, b, c, w = rule12 ( )
  elif ( p == 13 ):
    a, b, c, w = rule13 ( )
  elif ( p == 14 ):
    a, b, c, w = rule14 ( )
  elif ( p == 15 ):
    a, b, c, w = rule15 ( )
  elif ( p == 16 ):
    a, b, c, w = rule16 ( )
  elif ( p == 17 ):
    a, b, c, w = rule17 ( )
  elif ( p == 18 ):
    a, b, c, w = rule18 ( )
  elif ( p == 19 ):
    a, b, c, w = rule19 ( )
  elif ( p == 20 ):
    a, b, c, w = rule20 ( )

  return n, a, b, c, w

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
  triangle_witherden_rule_test ( )
  timestamp ( )

