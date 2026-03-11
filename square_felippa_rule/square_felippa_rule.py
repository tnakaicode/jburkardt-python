#! /usr/bin/env python3
#
def square_felippa_rule_test ( ):

#*****************************************************************************80
#
## square_felippa_rule_test() tests square_felippa_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'square_felippa_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test square_felippa_rule().' )

  degree_max = 4
  square_monomial_test ( degree_max )

  degree_max = 5
  square_quad_test ( degree_max )
#
#  Terminate.
#
  print ( '' )
  print ( 'square_felippa_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def square_monomial_test ( degree_max ):

#*****************************************************************************80
#
## square_monomial_test() tests square_monomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    04 February 2026
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

  a = - np.ones ( 2 )
  b =   np.ones ( 2 )

  print ( '' )
  print ( 'square_monomial_test():' )
  print ( '  square_monomial() returns the exact value of the' )
  print ( '  integral of X^ALPHA Y^BETA' )
  print ( '' )
  print ( '  Volume = ', square_volume ( a, b ) )
  print ( '' )
  print ( '     ALPHA      BETA      INTEGRAL' )
  print ( '' )

  expon = np.zeros ( 2 )

  for alpha in range ( 0, degree_max + 1 ):
    expon[0] = alpha
    for beta in range ( 0, degree_max - alpha + 1 ):
      expon[1] = beta
      value = square_monomial_integral ( a, b, expon )
      print ( '  %8d  %8d  %14.6e' \
        % ( expon[0], expon[1], value ) )

  return

def square_quad_test ( degree_max ):

#*****************************************************************************80
#
## square_quad_test() tests the rules for a square in 2D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
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
  import pprint

  a = - np.ones ( 2 )
  b =   np.ones ( 2 )

  print ( '' )
  print ( 'square_quad_test():' )
  print ( '  we approximate monomial integrals with' )
  print ( '  square_rule(), which returns M by N point rules..' )

  expon = np.zeros ( 2 )
  more = False
  h = 0
  t = 0
  n2 = 0
  more2 = False

  while ( True ):

    expon, more, h, t, n2, more2 = \
      subcomp_next ( degree_max, 2, expon, more, h, t, n2, more2 )

    if ( not more ):
      break

    if ( np.any ( ( expon % 2 ) == 1 ) ):
      continue

    print ( '' )
    print ( '  Monomial exponents: ' )
    pprint.pprint ( expon )
    print ( '' )
    print ( '' )

    order_1d = np.zeros ( 2, dtype = int )

    for k in range ( 1, 6 ):

      order_1d[:] = k
      order = int ( np.prod ( order_1d ) )
      w, xyz = square_rule ( a, b, order_1d )
      v = monomial_value ( expon, xyz )
      quad = square_volume ( a, b ) * np.dot ( w, v )
      print ( '  %6d  %6d  %14f' \
        % ( order_1d[0], order_1d[1], quad ) )
#
#  Try a rule of mixed orders.
#
    order_1d[0] = 3
    order_1d[1] = 5
    order = int ( np.prod ( order_1d ) )
    w, xyz = square_rule ( a, b, order_1d )
    v = monomial_value ( expon, xyz )
    quad = square_volume ( a, b ) * np.dot ( w, v )
    print ( '  %6d  %6d  %14f' \
      % ( order_1d[0], order_1d[1], quad ) )

    print ( '' )
    quad = square_monomial_integral ( a, b, expon )
    print ( '   Exact          %14f' % ( quad ) )

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

def line_unit_o01 ( ):

#*****************************************************************************80
#
## line_unit_o01() returns a 1 point quadrature rule for the unit line.
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

def line_unit_o02 ( ):

#*****************************************************************************80
#
## line_unit_o02() returns a 2 point quadrature rule for the unit line.
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

def line_unit_o03 ( ):

#*****************************************************************************80
#
## line_unit_o03() returns a 3 point quadrature rule for the unit line.
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

def line_unit_o04 ( ):

#*****************************************************************************80
#
## line_unit_o04() returns a 4 point quadrature rule for the unit line.
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

def line_unit_o05 ( ):

#*****************************************************************************80
#
## line_unit_o05() returns a 5 point quadrature rule for the unit line.
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

def r8vec_direct_product ( factor_index, factor_order, \
  factor_value, factor_num, point_num, x, contig, rep, skip ):

#*****************************************************************************80
#
## r8vec_direct_product() creates a direct product of R8VEC's.
#
#  Discussion:
#
#    To explain what is going on here, suppose we had to construct
#    a multidimensional quadrature rule as the product of K rules
#    for 1D quadrature.
#
#    The product rule will be represented as a list of points and weights.
#
#    The J-th item in the product rule will be associated with
#      item J1 of 1D rule 1,
#      item J2 of 1D rule 2, 
#      ..., 
#      item JK of 1D rule K.
#
#    In particular, 
#      X(J) = ( X(1,J1), X(2,J2), ..., X(K,JK))
#    and
#      W(J) = W(1,J1) * W(2,J2) * ... * W(K,JK)
#
#    So we can construct the quadrature rule if we can properly
#    distribute the information in the 1D quadrature rules.
#
#    This routine carries out that task.
#
#    Another way to do this would be to compute, one by one, the
#    set of all possible indices (J1,J2,...,JK), and then index
#    the appropriate information.  An advantage of the method shown
#    here is that you can process the K-th set of information and
#    then discard it.
#
#  Example:
#
#    Rule 1: 
#      Order = 4
#      X(1:4) = ( 1, 2, 3, 4 )
#
#    Rule 2:
#      Order = 3
#      X(1:3) = ( 10, 20, 30 )
#
#    Rule 3:
#      Order = 2
#      X(1:2) = ( 100, 200 )
#
#    Product Rule:
#      Order = 24
#      X(1:24) = 
#        ( 1, 10, 100 )
#        ( 2, 10, 100 )
#        ( 3, 10, 100 )
#        ( 4, 10, 100 )
#        ( 1, 20, 100 )
#        ( 2, 20, 100 )
#        ( 3, 20, 100 )
#        ( 4, 20, 100 )
#        ( 1, 30, 100 )
#        ( 2, 30, 100 )
#        ( 3, 30, 100 )
#        ( 4, 30, 100 )
#        ( 1, 10, 200 )
#        ( 2, 10, 200 )
#        ( 3, 10, 200 )
#        ( 4, 10, 200 )
#        ( 1, 20, 200 )
#        ( 2, 20, 200 )
#        ( 3, 20, 200 )
#        ( 4, 20, 200 )
#        ( 1, 30, 200 )
#        ( 2, 30, 200 )
#        ( 3, 30, 200 )
#        ( 4, 30, 200 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer FACTOR_index, the index of the factor being processed.
#    The first factor processed must be factor 1#
#
#    integer FACTOR_ORDER, the order of the factor.
#
#    real FACTOR_VALUE(FACTOR_ORDER), the factor values
#    for factor FACTOR_index.
#
#    integer FACTOR_NUM, the number of factors.
#
#    integer POINT_NUM, the number of elements in the direct product.
#
#    real X(FACTOR_NUM,POINT_NUM), the elements of the
#    direct product.  
#
#    integer CONTIG, the number of consecutive values to set.
#    The user should not set or alter this value.
#
#    integer REP, the number of blocks of values to set.
#    The user should not set or alter this value.
#
#    integer SKIP, the distance from the current value of START
#    to the next location of a block of values to set.
#    The user should not set or alter this value.
#
#  Output:
#
#    real X(FACTOR_NUM,POINT_NUM), the updated elements of the
#    direct product.  
#
#    integer CONTIG, the number of consecutive values to set.
#
#    integer REP, the number of blocks of values to set.
#
#    integer SKIP, the distance from the current value of START
#    to the next location of a block of values to set.
#
#  Local:
#
#    integer START, the first location of a block of values to set.
#
  import numpy as np

  if ( factor_index == 0 ):
    contig = 1
    skip = 1
    rep = point_num

  rep = ( rep // factor_order )
  skip = skip * factor_order

  for j in range ( 0, factor_order ):

    start = j * contig

    for k in range ( 0, rep ):
      for l in range ( start, start + contig ):
        x[l,factor_index] = factor_value[j]
      start = start + skip

  contig = contig * factor_order

  return x, contig, rep, skip

def r8vec_direct_product2 ( factor_index, factor_order, \
  factor_value, factor_num, point_num, w, contig, rep, skip ):

#*****************************************************************************80
#
## r8vec_direct_product2() creates a direct product of R8VEC's.
#
#  Discussion:
#
#    To explain what is going on here, suppose we had to construct
#    a multidimensional quadrature rule as the product of K rules
#    for 1D quadrature.
#
#    The product rule will be represented as a list of points and weights.
#
#    The J-th item in the product rule will be associated with
#      item J1 of 1D rule 1,
#      item J2 of 1D rule 2, 
#      ..., 
#      item JK of 1D rule K.
#
#    In particular, 
#      X(J) = ( X(1,J1), X(2,J2), ..., X(K,JK))
#    and
#      W(J) = W(1,J1) * W(2,J2) * ... * W(K,JK)
#
#    So we can construct the quadrature rule if we can properly
#    distribute the information in the 1D quadrature rules.
#
#    This routine carries out that task for the weights W.
#
#    Another way to do this would be to compute, one by one, the
#    set of all possible indices (J1,J2,...,JK), and then index
#    the appropriate information.  An advantage of the method shown
#    here is that you can process the K-th set of information and
#    then discard it.
#
#  Example:
#
#    Rule 1: 
#      Order = 4
#      W(1:4) = ( 2, 3, 5, 7 )
#
#    Rule 2:
#      Order = 3
#      W(1:3) = ( 11, 13, 17 )
#
#    Rule 3:
#      Order = 2
#      W(1:2) = ( 19, 23 )
#
#    Product Rule:
#      Order = 24
#      W(1:24) =
#        ( 2 * 11 * 19 )
#        ( 3 * 11 * 19 )
#        ( 4 * 11 * 19 )
#        ( 7 * 11 * 19 )
#        ( 2 * 13 * 19 )
#        ( 3 * 13 * 19 )
#        ( 5 * 13 * 19 )
#        ( 7 * 13 * 19 )
#        ( 2 * 17 * 19 )
#        ( 3 * 17 * 19 )
#        ( 5 * 17 * 19 )
#        ( 7 * 17 * 19 )
#        ( 2 * 11 * 23 )
#        ( 3 * 11 * 23 )
#        ( 5 * 11 * 23 )
#        ( 7 * 11 * 23 )
#        ( 2 * 13 * 23 )
#        ( 3 * 13 * 23 )
#        ( 5 * 13 * 23 )
#        ( 7 * 13 * 23 )
#        ( 2 * 17 * 23 )
#        ( 3 * 17 * 23 )
#        ( 5 * 17 * 23 )
#        ( 7 * 17 * 23 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer FACTOR_INDEX, the index of the factor being processed.
#    The first factor processed must be factor 0.
#
#    integer FACTOR_ORDER, the order of the factor.
#
#    real FACTOR_VALUE(FACTOR_ORDER), the factor values for
#    factor FACTOR_INDEX.
#
#    integer FACTOR_NUM, the number of factors.
#
#    integer POINT_NUM, the number of elements in the direct product.
#
#    real W(POINT_NUM), the elements of the
#    direct product.
#
#    integer CONTIG, the number of consecutive values to set.
#    The user should not set or alter this value.
#
#    integer REP, the number of blocks of values to set.
#    The user should not set or alter this value.
#
#    integer SKIP, the distance from the current value of START
#    to the next location of a block of values to set.
#    The user should not set or alter this value.
#
#  Output:
#
#    real W(POINT_NUM), the elements of the
#    direct product, updated by the latest factor.
#
#    integer CONTIG, the number of consecutive values to set.
#
#    integer REP, the number of blocks of values to set.
#
#    integer SKIP, the distance from the current value of START
#    to the next location of a block of values to set.
#
#  Local:
#
#    integer START, the first location of a block of values to set.
#
  import numpy as np

  if ( factor_index == 0 ):
    contig = 1
    skip = 1
    rep = point_num
    w = np.ones ( point_num )

  rep = rep // factor_order
  skip = skip * factor_order

  for j in range ( 0, factor_order ):

    start = j * contig

    for k in range ( 0, rep ):
      w[start:start+contig] = w[start:start+contig] * factor_value[j]
      start = start + skip

  contig = contig * factor_order

  return w, contig, rep, skip

def square_monomial_integral ( a, b, expon ):

#*****************************************************************************80
#
## square_monomial_integral() integrates a monomial over a square in 2D.
#
#  Discussion:
#
#    This routine integrates a monomial of the form
#
#      product ( 1 <= dim <= 2 ) x(dim)^expon(dim)
#
#    where the exponents are nonnegative integers.  Note that
#    if the combination 0^0 is encountered, it should be treated
#    as 1.
#
#    The integration region is defined as:
#      A(1) <= X <= B(1)
#      A(2) <= Y <= B(2)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(2), B(2), the lower and upper limits.
#
#    integer EXPON(2), the exponents.
#
#  Output:
#
#    real VALUE, the integral of the monomial.
#
  for i in range ( 0, 2 ):

    if ( expon[i] == -1 ):
      print ( '' )
      print ( 'square_monomial_integral(): Fatal error!' )
      print ( '  Exponent of -1 encountered.' )
      raise Exception ( 'square_monomial_integral(): Fatal error!' )

  value = 1.0

  for i in range ( 0, 2 ):

    value = value * ( b[i] ** ( expon[i] + 1 ) - a[i] ** ( expon[i] + 1 ) ) \
      / ( expon[i] + 1 )

  return value

def square_rule ( a, b, order_1d ):

#*****************************************************************************80
#
## square_rule() returns a quadrature rule for a square in 2D.
#
#  Discussion:
#
#    The integration region is defined as:
#      A(1) <= X <= B(1)
#      A(2) <= Y <= B(2)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
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
#    real A(2), B(2), the lower and upper limits.
#
#    integer ORDER_1D(2), the order of the rule in
#    each dimension.  1 <= ORDER_1D(I) <= 5.
#
#  Output:
#
#    real W(ORDER_1D(1)*ORDER_1D(2),1), the weights.
#
#    real XY(ORDER_1D(1)*ORDER_1D(2),2), the abscissas.
#
  import numpy as np

  order = order_1d[0] * order_1d[1]

  xy = np.zeros ( [ order, 2 ] )
  w = np.zeros ( order )

  contig = 1
  rep = 1
  skip = order

  contig2 = 1
  rep2 = 1
  skip2 = order

  for i in range ( 0, 2 ):

    o = order_1d[i]

    if ( o == 1 ):
      w_1d, x_1d = line_unit_o01 ( )
    elif ( o == 2 ):
      w_1d, x_1d = line_unit_o02 ( )
    elif ( o == 3 ):
      w_1d, x_1d = line_unit_o03 ( )
    elif ( o == 4 ):
      w_1d, x_1d = line_unit_o04 ( )
    elif ( o == 5 ):
      w_1d, x_1d = line_unit_o05 ( )
    else:
      print ( '' )
      print ( 'square_rule(): Fatal error!' )
      print ( '  Illegal value of ORDER_1D(*).' )
      raise Exception ( 'square_rule(): Fatal error!' )
#
#  Transform from [-1,+1] to [Ai,Bi]
#
    for j in range ( 0, o ):
      w_1d[j] = w_1d[j] * ( b[i] - a[i] ) / 2.0
      x_1d[j] = ( ( 1.0 - x_1d[j] ) * a[i]   \
                + ( 1.0 + x_1d[j] ) * b[i] ) \
                /   2.0
#
#  Add this information to the rule.
#
    xy, contig, rep, skip = \
      r8vec_direct_product ( i, o, x_1d, 2, order, xy, contig, rep, skip )

    w, contig2, rep2, skip2 = \
      r8vec_direct_product2 ( i, o, w_1d, 2, order, w, contig2, rep2, skip2 )

  return w, xy

def square_volume ( a, b ):

#*****************************************************************************80
#
## square_volume(): volume of a square in 2D.
#
#  Discussion:
#
#    The integration region is defined as:
#      A(1) <= X <= B(1)
#      A(2) <= Y <= B(2)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(2), B(2), the lower and upper limits.
#
#  Output:
#
#    real VALUE, the volume.
#
  value = ( b[0] - a[0] ) * ( b[1] - a[1] )

  return value

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

if ( __name__ == '__main__' ):
  timestamp ( )
  square_felippa_rule_test ( )
  timestamp ( )

