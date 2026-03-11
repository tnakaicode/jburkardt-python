#! /usr/bin/env python3
#
def wedge_felippa_rule_test ( ):

#*****************************************************************************80
#
## wedge_felippa_rule_test() tests wedge_felippa_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'wedge_felippa_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test wedge_felippa_rule()' )

  max_degree = 4

  wedge_felippa_rule_test01 ( max_degree )
  wedge_felippa_rule_test02 ( max_degree )
  wedge_felippa_rule_test03 ( max_degree )
#
#  Terminate.
#
  print ( '' )
  print ( 'wedge_felippa_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def wedge_felippa_rule_test01 ( degree_max ):

#*****************************************************************************80
#
## wedge_felippa_rule_test01() tests wedge_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DEGREE_MAX, the maximum total degree of the
#    monomials to check.
#
  import numpy as np

  print ( '' )
  print ( 'wedge_felippa_rule_test01():' )
  print ( '  wedge_integral() returns the exact value of the' )
  print ( '  integral of X^ALPHA Y^BETA Z^GAMMA' )
  print ( '' )
  print ( '  Volume = ', wedge01_volume ( ) )
  print ( '' )
  print ( '     ALPHA      BETA     GAMMA      INTEGRAL' )
  print ( '' )

  expon = np.zeros ( 3, dtype = int )

  for alpha in range ( 0, degree_max + 1 ):
    expon[0] = alpha
    for beta in range ( 0, degree_max + 1 - alpha ):
      expon[1] = beta
      for gamma in range ( 0, degree_max + 1 - alpha - beta ):
        expon[2] = gamma
        value = wedge01_monomial_integral ( expon )
        print ( '  %8d  %8d  %8d  %14.6e' % ( expon[0], expon[1], expon[2], value ) )

  return

def wedge_felippa_rule_test02 ( degree_max ):

#*****************************************************************************80
#
## wedge_felippa_rule_test01() tests the rules for the unit wedge.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DEGREE_MAX, the maximum total degree of the
#    monomials to check.
#
  import numpy as np

  dim_num = 3
  test_num = 7
  line_order_array = np.array ( [ 1, 2, 2, 3, 2, 3, 4 ] )
  triangle_order_array = np.array ( [ 1, 3, -3, 6, -6, 7, 12 ] )

  print ( '' )
  print ( 'wedge_felippa_rule_test02():' )
  print ( '  wedge_rule() approximates monomial integrals.' )

  expon = np.zeros ( 3, dtype = int )
  more = False
  h = 0
  t = 0
  n2 = 0
  more2 = False

  while ( True ):

    expon, more, h, t, n2, more2 = subcomp_next ( degree_max, dim_num, \
      expon, more, h, t, n2, more2 )

    if ( ( expon[2] % 2 ) == 1 ):
      if ( not more ):
        break
      else:
        continue

    print ( '' )
    print ( '  Monomial exponents: ' )
    for dim in range ( 0, dim_num ):
      print ( '  %2d' % ( expon[dim] ), end = '' )
    print ( '' )
    print ( '' )

    for test in range ( 0, test_num ):

      line_order = line_order_array[test]
      triangle_order = triangle_order_array[test]

      order = line_order * abs ( triangle_order )

      w, xyz = wedge_rule ( line_order, triangle_order )
      v = monomial_value ( expon, xyz )
      quad = wedge01_volume ( ) * np.dot ( w, v )
      print ( '  %6d  %6d  %6d  %14f' \
        % ( triangle_order, line_order, order, quad ) )

    print ( '' )
    quad = wedge01_monomial_integral ( expon )
    print ( '  Exact                   %14f' % ( quad ) )

    if ( not more ):
      break

  return

def wedge_felippa_rule_test03 ( degree_max ):

#*****************************************************************************80
#
## wedge_felippa_rule_test03() tests some wedge quadrature rules to files.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  rule_num = 7
  line_order_array = np.array ( [ 1, 2, 2, 3, 2, 3, 4 ] )
  trig_order_array = np.array ( [ 1, 3, -3, 6, -6, 7, 12 ] )

  print ( '' )
  print ( 'wedge_felippa_rule_test03():' )
  print ( '  For the unit wedge, write quadrature rules to a file' )
  print ( '' )
  print ( '   Rule  Trig    Line   Total  W_File X_File' )
  print ( '         Order   Order  Order' )
  print ( '' )

  for rule in range ( 0, rule_num ):

    if ( rule == 0 ):
      w_filename = 'wedge_felippa_1x1_w.txt'
      x_filename = 'wedge_felippa_1x1_x.txt'
    elif ( rule == 1 ):
      w_filename = 'wedge_felippa_3x2_w.txt'
      x_filename = 'wedge_felippa_3x2_x.txt'
    elif ( rule == 2 ):
      w_filename = 'wedge_felippa_3bx2_w.txt'
      x_filename = 'wedge_felippa_3bx2_x.txt'
    elif ( rule == 3 ):
      w_filename = 'wedge_felippa_6x3_w.txt'
      x_filename = 'wedge_felippa_6x3_x.txt'
    elif ( rule == 4 ):
      w_filename = 'wedge_felippa_6bx2_w.txt'
      x_filename = 'wedge_felippa_6bx2_x.txt'
    elif ( rule == 5 ):
      w_filename = 'wedge_felippa_7x3_w.txt'
      x_filename = 'wedge_felippa_7x3_x.txt'
    elif ( rule == 6 ):
      w_filename = 'wedge_felippa_12x4_w.txt'
      x_filename = 'wedge_felippa_12x4_x.txt'

    line_order = line_order_array[rule]
    trig_order = trig_order_array[rule]

    order = line_order * abs ( trig_order )

    w, x = wedge_rule ( line_order, trig_order )
    np.savetxt ( w_filename, w )
    np.savetxt ( x_filename, x )
    print ( '  %6d  %6d  %6d  %6d  %s  %s'  \
      % ( rule, trig_order, line_order, order, w_filename, x_filename ) )

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

def line_o01 ( ):

#*****************************************************************************80
#
## line_o01() returns a 1 point quadrature rule for the unit line.
#
#  Discussion:
#
#    The integration region is:
#
#    - 1.0 <= X <= 1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(1), the weights.
#
#    real X(1), the abscissas.
#
  import numpy as np

  w = np.array ( [ 1.0 ] )

  x = np.array ( [ 0.0 ] )

  return w, x

def line_o02 ( ):

#*****************************************************************************80
#
## line_o02() returns a 2 point quadrature rule for the unit line.
#
#  Discussion:
#
#    The integration region is:
#
#    - 1.0 <= X <= 1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(2), the weights.
#
#    real X(2), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.5, \
    0.5 ] )

  x = np.array ( [ \
    -0.57735026918962576451, \
     0.57735026918962576451 ] )

  return w, x

def line_o03 ( ):

#*****************************************************************************80
#
## line_o03() returns a 3 point quadrature rule for the unit line.
#
#  Discussion:
#
#    The integration region is:
#
#    - 1.0 <= X <= 1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(3), the weights.
#
#    real X(3), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.27777777777777777778, \
    0.44444444444444444444, \
    0.27777777777777777778 ] )

  x = np.array ( [ \
    -0.77459666924148337704, \
     0.00000000000000000000, \
     0.77459666924148337704 ] )

  return w, x

def line_o04 ( ):

#*****************************************************************************80
#
## line_o04() returns a 4 point quadrature rule for the unit line.
#
#  Discussion:
#
#    The integration region is:
#
#    - 1.0 <= X <= 1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(4), the weights.
#
#    real X(4), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.173927422568727, \
    0.326072577431273, \
    0.326072577431273, \
    0.173927422568727 ] )

  x = np.array ( [ \
    -0.86113631159405257522, \
    -0.33998104358485626480, \
     0.33998104358485626480, \
     0.86113631159405257522 ] )

  return w, x

def line_o05 ( ):

#*****************************************************************************80
#
## line_o05() returns a 5 point quadrature rule for the unit line.
#
#  Discussion:
#
#    The integration region is:
#
#    - 1.0 <= X <= 1.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(5), the weights.
#
#    real X(5), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.118463442528095, \
    0.239314335249683, \
    0.284444444444444, \
    0.239314335249683, \
    0.118463442528095 ] )

  x = np.array ( [ \
    -0.90617984593866399280, \
    -0.53846931010568309104, \
     0.00000000000000000000, \
     0.53846931010568309104, \
     0.90617984593866399280 ] )

  return w, x

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

def subcomp_next ( n, k, a, more, h, t, n2, more2 ):

#*****************************************************************************80
#
## subcomp_next() computes the next subcomposition of N into K parts.
#
#  Discussion:
#
#    A composition of the integer N into K parts is an ordered sequence
#    of K nonnegative integers which sum to a value of N.
#
#    A subcomposition of the integer N into K parts is a composition
#    of M into K parts, where 0 <= M <= N.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the integer whose subcompositions are desired.
#
#    integer K, the number of parts in the subcomposition.
#
#    integer A(K), the parts of the subcomposition.
#
#    bool MORE, set to FALSE by the user to start the computation.
#
#    integer H, T, N2, internal parameters needed for the
#    computation.  The user may need to initialize these before the
#    very first call, but these initial values are not important.
#    The user should not alter these parameters once the computation
#    begins.
#
#    bool MORE2, an internal parameter needed for the
#    computation.  The user may need to initialize this before the
#    very first call, but the initial value is not important.
#    The user should not alter this parameter once the computation
#    begins.
#
#  Output:
#
#    integer A(K), the parts of the subcomposition.
#
#    bool MORE, set to FALSE by the routine to end the computation.
#
#    integer H, T, N2, updated values.
#
#    bool MORE2, an updated value.
#

#
#  The first computation.
#
  if ( not more ):

    for i in range ( 0, k ):
      a[i] = 0
    more = True
    h = 0
    t = 0
    n2 = 0
    more2 = False
#
#  Do the next element at the current value of N.
#
  elif ( more2 ):

    a, more2, h, t = comp_next ( n2, k, a, more2, h, t )

  else:

    more2 = False
    n2 = n2 + 1

    a, more2, h, t = comp_next ( n2, k, a, more2, h, t )
#
#  Termination occurs if MORE2 = FALSE and N2 = N.
#
  if ( not more2 and n2 == n ):
    more = False

  return a, more, h, t, n2, more2

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
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

def triangle_o01 ( ):

#*****************************************************************************80
#
## triangle_o01() returns a 1 point quadrature rule for the unit triangle.
#
#  Discussion:
#
#    This rule is precise for monomials through degree 1.
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(1), the weights.
#
#    real XY(2,1), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    1.0 ] )

  xy = np.array ( [ \
    [ 0.33333333333333333333,  0.33333333333333333333 ] ] )

  return w, xy

def triangle_o03b ( ):

#*****************************************************************************80
#
## triangle_o03b() returns a 3 point quadrature rule for the unit triangle.
#
#  Discussion:
#
#    This rule is precise for monomials through degree 2.
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(3), the weights.
#
#    real XY(2,3), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.33333333333333333333, \
    0.33333333333333333333, \
    0.33333333333333333333 ] )

  xy = np.array ( [ \
    [ 0.0,  0.5 ], \
    [ 0.5,  0.0 ], \
    [ 0.5,  0.5 ] ] )

  return w, xy

def triangle_o03 ( ):

#*****************************************************************************80
#
## triangle_o03() returns a 3 point quadrature rule for the unit triangle.
#
#  Discussion:
#
#    This rule is precise for monomials through degree 2.
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(3), the weights.
#
#    real XY(2,3), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.33333333333333333333, \
    0.33333333333333333333, \
    0.33333333333333333333 ] )

  xy = np.array ( [ \
    [ 0.66666666666666666667,  0.16666666666666666667 ], \
    [ 0.16666666666666666667,  0.66666666666666666667 ], \
    [ 0.16666666666666666667,  0.16666666666666666667 ] ] )

  return w, xy

def triangle_o06b ( ):

#*****************************************************************************80
#
## triangle_o06b() returns a 6 point quadrature rule for the unit triangle.
#
#  Discussion:
#
#    This rule is precise for monomials through degree 3.
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(6), the weights.
#
#    real XY(2,6), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.30000000000000000000, \
    0.30000000000000000000, \
    0.30000000000000000000, \
    0.033333333333333333333, \
    0.033333333333333333333, \
    0.033333333333333333333 ] )

  xy = np.array ( [ \
    [ 0.66666666666666666667,  0.16666666666666666667 ], \
    [ 0.16666666666666666667,  0.66666666666666666667 ], \
    [ 0.16666666666666666667,  0.16666666666666666667 ], \
    [ 0.0,  0.5 ], \
    [ 0.5,  0.0 ], \
    [ 0.5,  0.5 ] ] )

  return w, xy

def triangle_o06 ( ):

#*****************************************************************************80
#
## triangle_o06() returns a 6 point quadrature rule for the unit triangle.
#
#  Discussion:
#
#    This rule is precise for monomials through degree 4.
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(6), the weights.
#
#    real XY(2,6), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.22338158967801146570, \
    0.22338158967801146570, \
    0.22338158967801146570, \
    0.10995174365532186764, \
    0.10995174365532186764, \
    0.10995174365532186764 ] )

  xy = np.array ( [ \
    [ 0.10810301816807022736,  0.44594849091596488632 ], \
    [ 0.44594849091596488632,  0.10810301816807022736 ], \
    [ 0.44594849091596488632,  0.44594849091596488632 ], \
    [ 0.81684757298045851308,  0.091576213509770743460 ], \
    [ 0.091576213509770743460,  0.81684757298045851308 ], \
    [ 0.091576213509770743460,  0.091576213509770743460 ] ] )

  return w, xy

def triangle_o07 ( ):

#*****************************************************************************80
#
## triangle_o07() returns a 7 point quadrature rule for the unit triangle.
#
#  Discussion:
#
#    This rule is precise for monomials through degree 5.
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(7), the weights.
#
#    real XY(2,7), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
    0.12593918054482715260, \
    0.12593918054482715260, \
    0.12593918054482715260, \
    0.13239415278850618074, \
    0.13239415278850618074, \
    0.13239415278850618074, \
    0.22500000000000000000 ] )

  xy = np.array ( [ \
    [ 0.79742698535308732240,  0.10128650732345633880 ], \
    [ 0.10128650732345633880,  0.79742698535308732240 ], \
    [ 0.10128650732345633880,  0.10128650732345633880 ], \
    [ 0.059715871789769820459,  0.47014206410511508977 ], \
    [ 0.47014206410511508977,  0.059715871789769820459 ], \
    [ 0.47014206410511508977,  0.47014206410511508977 ], \
    [ 0.33333333333333333333,  0.33333333333333333333 ] ] )

  return w, xy

def triangle_o12 ( ):

#*****************************************************************************80
#
## triangle_o12() returns a 12 point quadrature rule for the unit triangle.
#
#  Discussion:
#
#    This rule is precise for monomials through degree 6.
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Output:
#
#    real W(12), the weights.
#
#    real XY(2,12), the abscissas.
#
  import numpy as np

  w = np.array ( [ \
     0.050844906370206816921, \
     0.050844906370206816921, \
     0.050844906370206816921, \
     0.11678627572637936603, \
     0.11678627572637936603, \
     0.11678627572637936603, \
     0.082851075618373575194, \
     0.082851075618373575194, \
     0.082851075618373575194, \
     0.082851075618373575194, \
     0.082851075618373575194, \
     0.082851075618373575194 ] )

  xy = np.array ( [ \
    [ 0.87382197101699554332,  0.063089014491502228340 ], \
    [ 0.063089014491502228340,  0.87382197101699554332 ], \
    [ 0.063089014491502228340,  0.063089014491502228340 ], \
    [ 0.50142650965817915742,  0.24928674517091042129 ], \
    [ 0.24928674517091042129,  0.50142650965817915742 ], \
    [ 0.24928674517091042129,  0.24928674517091042129 ], \
    [ 0.053145049844816947353,  0.31035245103378440542 ], \
    [ 0.31035245103378440542,  0.053145049844816947353 ], \
    [ 0.053145049844816947353,  0.63650249912139864723 ], \
    [ 0.31035245103378440542,  0.63650249912139864723 ], \
    [ 0.63650249912139864723,  0.053145049844816947353 ], \
    [ 0.63650249912139864723,  0.31035245103378440542 ] ] )

  return w, xy

def wedge01_monomial_integral ( e ):

#*****************************************************************************80
#
## wedge01_monomial_integral(): integral of a monomial in the unit wedge in 3D.
#
#  Discussion:
#
#    This routine returns the integral of
#
#      product ( 1 <= I <= 3 ) X(I)^E(I)
#
#    over the unit wedge.
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1
#      -1 <= Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Arthur Stroud,
#    Approximate Calculation of Multiple integrals,
#    Prentice Hall, 1971,
#    ISBN: 0130438936,
#    LC: QA311.S85.
#
#  Input:
#
#    integer E(3), the exponents.
#
#  Output:
#
#    real VALUE, the integral of the monomial.
#
  value = 1.0

  k = e[0]

  for i in range ( 1, e[1] + 1 ):
    k = k + 1
    value = value * float ( i ) / float ( k )

  k = k + 1
  value = value / float ( k )

  k = k + 1
  value = value / float ( k )
#
#  Now account for integration in Z.
#
  if ( e[2] == - 1 ):
    print ( '' )
    print ( 'wedge01_monomial_integral(): Fatal error!' )
    print ( '  E(3) = -1 is not a legal input.' )
    raise Exception ( 'wedge01_monomial_integral(): Fatal error!' )
  elif ( ( e[2] % 2 ) == 1 ):
    value = 0.0
  else:
    value = value * 2.0 / float ( e[2] + 1 )

  return value

def wedge_rule ( line_order, triangle_order ):

#*****************************************************************************80
#
## wedge_rule() returns a quadrature rule for the unit wedge in 3D.
#
#  Discussion:
#
#    It is usually sensible to take LINE_ORDER and TRIANGLE_ORDER so that
#    the line and triangle rules are roughly the same precision.  For that
#    criterion, we recommend the following combinations:
#
#      TRIANGLE_ORDER  LINE_ORDER  Precision
#      ----------      ----------  ---------
#          1               1       1 x 1 
#          3               2       2 x 3
#         -3               2       2 x 3
#          6               3       4 x 5
#         -6               2       3 x 3
#          7               3       5 x 5
#         12               4       6 x 7
#
#    The integration region is:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1
#      -1 <= Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Carlos Felippa,
#    A compendium of FEM integration formulas for symbolic work,
#    Engineering Computation,
#    Volume 21, Number 8, 2004, pages 867-890.
#
#  Input:
#
#    integer LINE_ORDER, the index of the line rule.
#    The index of the rule is equal to the order of the rule.
#    1 <= LINE_ORDER <= 5.
#
#    integer TRIANGLE_ORDER, the index of the triangle rule.
#    The index of the rule is 1, 3, -3, 6, -6, 7 or 12.
#
#  Output:
#
#    real W(LINE_ORDER*abs(TRIANGLE_ORDER)), the weights.
#
#    real XYZ(3,LINE_ORDER*abs(TRIANGLE_ORDER)), the abscissas.
#
  import numpy as np

  order = line_order * abs ( triangle_order )

  if ( line_order == 1 ):
    line_w, line_x = line_o01 ( )
  elif ( line_order == 2 ):
    line_w, line_x = line_o02 ( )
  elif ( line_order == 3 ):
    line_w, line_x = line_o03 ( )
  elif ( line_order == 4 ):
    line_w, line_x = line_o04 ( )
  elif ( line_order == 5 ):
    line_w, line_x = line_o05 ( )
  else:
    print ( '' )
    print ( 'wedge_rule(): Fatal error!' )
    print ( '  Illegal value of LINE_ORDER.' )
    raise Exception ( 'wedge_rule(): Fatal error!' )

  if ( triangle_order == 1 ):
    triangle_w, triangle_xy = triangle_o01 ( )
  elif ( triangle_order == 3 ):
    triangle_w, triangle_xy = triangle_o03 ( )
  elif ( triangle_order == - 3 ):
    triangle_w, triangle_xy = triangle_o03b ( )
  elif ( triangle_order == 6 ):
   triangle_w, triangle_xy = triangle_o06 ( )
  elif ( triangle_order == - 6 ):
    triangle_w, triangle_xy = triangle_o06b ( )
  elif ( triangle_order == 7 ):
    triangle_w, triangle_xy = triangle_o07 ( )
  elif ( triangle_order == 12 ):
    triangle_w, triangle_xy = triangle_o12 ( )
  else:
    print ( '' )
    print ( 'wedge_rule(): Fatal error!' )
    print ( '  Illegal value of TRIANGLE_ORDER.' )
    raise Exception ( 'wedge_rule(): Fatal error!' )

  w = np.zeros ( order )
  xyz = np.zeros ( [ order, 3 ] )

  k = 0
  for i in range ( 0, line_order ):
    for j in range ( 0, abs ( triangle_order ) ):
      w[k] = line_w[i] * triangle_w[j]
      xyz[k,0] = triangle_xy[j,0]
      xyz[k,1] = triangle_xy[j,1]
      xyz[k,2] = line_x[i]
      k = k + 1

  return w, xyz

def wedge01_volume ( ):

#*****************************************************************************80
#
## wedge01_volume(): volume of the unit wedge in 3D.
#
#  Discussion:
#
#    The integration region is defined as:
#
#      0 <= X
#      0 <= Y
#      X + Y <= 1
#      -1 <= Z <= 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2023
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

if ( __name__ == '__main__' ):
  timestamp ( )
  wedge_felippa_rule_test ( )
  timestamp ( )

