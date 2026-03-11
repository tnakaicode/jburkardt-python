#! /usr/bin/env python3
#
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
#    parameters.
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

def comp_next_test ( ):

#*****************************************************************************80
#
## comp_next_test() tests comp_next().
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
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'comp_next_test():' )
  print ( '  comp_next() generates compositions.' )
  print ( '' )

  n = 6
  k = 3
  a = np.zeros ( k )
  more = False
  h = 0
  t = 0

  print ( '  Seeking all compositions of N = %d' % ( n ) )
  print ( '  using %d parts.' % ( k ) )
  print ( '' )

  while ( True ):

    a, more, h, t = comp_next ( n, k, a, more, h, t )
    
    print ( '  ', end = "" ),
    for i in range ( 0, k ):
      print ( '%2d  ' % ( a[i] ), end = "" )
    print ( '' )

    if ( not more ):
      break

  return

def gm_general_rule_set ( rule, m, n, t ):

#*****************************************************************************80
#
## gm_general_rule_set() sets a Grundmann-Moeller rule for a general simplex.
#
#  Discussion:
#
#    The vertices of the simplex are given by the array T.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 March 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Axel Grundmann, Michael Moeller,
#    Invariant Integration Formulas for the N-Simplex 
#    by Combinatorial Methods,
#    SIAM Journal on Numerical Analysis,
#    Volume 15, Number 2, April 1978, pages 282-290.
#
#  Input:
#
#    integer RULE, the index of the rule.
#    0 <= RULE.
#
#    integer M, the spatial dimension.
#    1 <= M.
#
#    integer N, the number of points in the rule.
#
#    real T(M,M+1), the vertices of the simplex.
#
#  Output:
#
#    real W(N), the weights.
#
#    real X(M,N), the abscissas.
#
  import numpy as np
#
#  Get the unit rule.
#
  w1, x1 = gm_unit_rule_set ( rule, m, n )
#
#  Compute the volume of the unit simplex.
#
  volume1 = simplex_unit_volume ( m )
#
#  Compute the volume of the general simplex.
#
  volume = simplex_general_volume ( m, t )
#
#  Convert the points.
#
  x = simplex_unit_to_general ( m, n, t, x1 )
#
#  Convert the weights.
#
  w = np.zeros ( n )
  w[0:n] = w1[0:n] * volume / volume1

  return w, x

def gm_general_rule_set_test01 ( ):

#*****************************************************************************80
#
## gm_general_rule_set_test01() tests gm_general_rule_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t = np.array ( [ \
    [ 1.0, 2.0, 1.0, 1.0 ], \
    [ 0.0, 0.0, 2.0, 0.0 ], \
    [ 0.0, 0.0, 0.0, 3.0 ] ] )

  print ( '' )
  print ( 'gm_general_rule_set_test01' )
  print ( '  gm_general_rule_set determines the weights and abscissas' )
  print ( '  of a Grundmann-Moeller quadrature rule for' )
  print ( '  the M dimensional general simplex,' )
  print ( '  using a rule of in index RULE,' )
  print ( '  which will have degree of exactness 2*RULE+1.' )

  m = 3
  rule = 2

  print ( '' )
  print ( '  Here we use M = %d' % ( m ) )
  print ( '  RULE = %d' % ( rule ) )
  print ( '  DEGREE = %d' % ( 2 * rule + 1 ) )

  print ( '' )
  print ( '  Simplex vertices:' )
  print ( '' )
  for j in range ( 0, 4 ):
    for i in range ( 0, 3 ):
      print ( '%14.6g' % ( t[i,j] ), end = '' )
    print ( '' )

  n = gm_rule_size ( rule, m )

  w, x = gm_general_rule_set ( rule, m, n, t )

  print ( '' )
  print ( '     POINT        W             X             Y             Z' )
  print ( '' )

  for j in range ( 0, n ):
    print ( '  %8d  %12f' % ( j, w[j] ), end = "" )
    for i in range ( 0, m ):
      print ( '  %12f' % ( x[i,j] ), end = "" )
    print ( '' )

  return

def gm_general_rule_set_test02 ( ):

#*****************************************************************************80
#
## gm_general_rule_set_test02() tests gm_general_rule_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  e_test = np.array ( [ \
    [ 0, 1, 0, 0, 2, 1, 1, 0, 0, 0 ], \
    [ 0, 0, 1, 0, 0, 1, 0, 2, 1, 0 ], \
    [ 0, 0, 0, 1, 0, 0, 1, 0, 1, 2 ] ] )

  t = np.array ( [ \
    [ 1.0, 2.0, 1.0, 1.0 ], \
    [ 0.0, 0.0, 2.0, 0.0 ], \
    [ 0.0, 0.0, 0.0, 3.0 ] ] )

  print ( '' )
  print ( 'gm_general_rule_set_test02' )
  print ( '  gm_general_rule_set determines the weights and abscissas' )
  print ( '  of a Grundmann-Moeller quadrature rule for' )
  print ( '  the M dimensional general simplex,' )
  print ( '  using a rule of index RULE,' )
  print ( '  which will have degree of exactness 2*RULE+1.' )

  print ( '  In this test, look at all the monomials up to' )
  print ( '  some maximum degree, choose a few low order rules' )
  print ( '  and determine the quadrature error for each.' )

  print ( '' )
  print ( '  Simplex vertices:' )
  print ( '' )
  for j in range ( 0, 4 ):
    for i in range ( 0, 3 ):
      print ( '%14.6g' % ( t[i,j] ), end = '' )
    print ( '' )

  m = 3
  volume = simplex_general_volume ( m, t )
  print ( '' )
  print ( '  Simplex volume = %g' % ( volume ) )

  print ( '' )
  print ( '         N        1               X               Y ', end = '' )
  print ( '              Z               X^2              XY             XZ', end = '' )
  print ( '              Y^2             YZ               Z^2' )
  print ( '' )

  e = np.zeros ( m )

  for rule in range ( 0, 6 ):

    n = gm_rule_size ( rule, m )

    w, x = gm_general_rule_set ( rule, m, n, t )

    print ( '  %8d' % ( n ), end = '' )

    for k in range ( 0, 10 ):

      e[0:m] = e_test[0:m,k]

      value = monomial_value ( m, n, e, x  )

      result = np.dot ( w, value )

      print ( '  %14.6g' % ( result ), end ='' )

    print ( '' )

  return

def gm_rule_size ( rule, m ):

#*****************************************************************************80
#
## gm_rule_size() determines the size of a Grundmann-Moeller rule.
#
#  Discussion:
#
#    This rule returns the value of N, the number of points associated
#    with a GM rule of given index.
#
#    After calling this rule, the user can use the value of N to
#    allocate space for the weight vector as W(N) and the abscissa
#    vector as X(M,N), and then call GM_RULE_SET.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 July 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Axel Grundmann, Michael Moeller,
#    Invariant Integration Formulas for the N-Simplex
#    by Combinatorial Methods,
#    SIAM Journal on Numerical Analysis,
#    Volume 15, Number 2, April 1978, pages 282-290.
#
#  Input:
#
#    integer RULE, the index of the rule.
#    0 <= RULE.
#
#    integer M, the spatial dimension.
#    1 <= M.
#
#  Output:
#
#    integer N, the number of points in the rule.
#
  from scipy.special import comb

  arg1 = m + rule + 1

  n = int ( comb ( arg1, rule ) )

  return n

def gm_rule_size_test ( ):

#*****************************************************************************80
#
## gm_rule_size_test() tests gm_rule_size().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 March 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 4

  m_test = np.array ( [ 2, 3, 5, 10 ] )

  print ( '' )
  print ( 'gm_rule_size_test():' )
  print ( '  gm_rule_size returns N, the number of points' )
  print ( '  associated with a Grundmann-Moeller quadrature rule' )
  print ( '  for the unit simplex of dimension M' )
  print ( '  with rule index RULE' )
  print ( '  and degree of exactness DEGREE = 2*RULE+1.' )

  print ( '' )
  print ( '         M      RULE    DEGREE N' )

  for test in range ( 0, test_num ):

    m = m_test[test]

    print ( '' )

    for rule in range ( 0, 6 ):

      n = gm_rule_size ( rule, m )
      degree = 2 * rule + 1

      print ( '  %8d  %8d  %8d  %8d' % ( m, rule, degree, n ) )

  return

def gm_unit_rule_set ( rule, m, n ):

#*****************************************************************************80
#
## gm_unit_rule_set() sets a Grundmann-Moeller rule for a unit simplex.
#
#  Discussion:
#
#    This is a revised version of the calculation which seeks to compute
#    the value of the weight in a cautious way that avoids intermediate
#    overflow.  Thanks to John Peterson for pointing out the problem on
#    26 June 2008.
#
#    This rule returns weights and abscissas of a Grundmann-Moeller
#    quadrature rule for the M-dimensional unit simplex.
#
#    The dimension N can be determined by calling gm_rule_size.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Axel Grundmann, Michael Moeller,
#    Invariant Integration Formulas for the N-Simplex
#    by Combinatorial Methods,
#    SIAM Journal on Numerical Analysis,
#    Volume 15, Number 2, April 1978, pages 282-290.
#
#  Input:
#
#    integer RULE, the index of the rule.
#    0 <= RULE.
#
#    integer M, the spatial dimension.
#    1 <= M.
#
#    integer N, the number of points in the rule.
#
#  Output:
#
#    real W(N), the weights.
#
#    real X(M,N), the abscissas.
#
  import numpy as np

  w = np.zeros ( n )
  x = np.zeros ( [ m, n ] )

  s = rule
  d = 2 * s + 1
  k = 0
  one_pm = 1

  for i in range ( 0, s + 1 ):

    weight = one_pm

    for j in range (  1, max ( m, max ( d, d + m - i ) ) + 1 ):

      if ( j <= m ):
        weight = weight *  float ( j )

      if ( j <= d ):
        weight = weight * float ( d + m - 2 * i )

      if ( j <= 2 * s ):
        weight = weight / 2.0

      if ( j <= i ):
        weight = weight / float ( j )

      if ( j <= d + m - i ):
        weight = weight / float ( j )

    one_pm = - one_pm

    beta_sum = s - i
    more = False
    beta = np.zeros ( m + 1 )
    h = 0
    t = 0

    while ( True ):

      beta, more, h, t = comp_next ( beta_sum, m + 1, beta, more, h, t )

      w[k] = weight
      
      x[0:m,k] = ( 2.0 * beta[1:m+1] + 1.0 ) / float ( d + m - 2 * i )

      k = k + 1

      if ( not more ):
        break

  volume1 = simplex_unit_volume ( m )
  w[0:n] = w[0:n] * volume1

  return w, x

def gm_unit_rule_set_test01 ( ):

#*****************************************************************************80
#
## gm_unit_rule_set_test01() tests gm_unit_rule_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'gm_unit_rule_set_test01' )
  print ( '  gm_unit_rule_set determines the weights and abscissas' )
  print ( '  of a Grundmann-Moeller quadrature rule for' )
  print ( '  the M dimensional unit simplex,' )
  print ( '  using a rule of in index RULE,' )
  print ( '  which will have degree of exactness 2*RULE+1.' )

  m = 3
  rule = 2

  print ( '' )
  print ( '  Here we use M = %d' % ( m ) )
  print ( '  RULE = %d' % ( rule ) )
  print ( '  DEGREE = %d' % ( 2 * rule + 1 ) )

  n = gm_rule_size ( rule, m )

  w, x = gm_unit_rule_set ( rule, m, n )

  print ( '' )
  print ( '     POINT        W             X             Y             Z' )
  print ( '' )

  for j in range ( 0, n ):
    print ( '  %8d  %12f' % ( j, w[j] ), end = "" )
    for i in range ( 0, m ):
      print ( '  %12f' % ( x[i,j] ), end = "" )
    print ( '' )

  return

def gm_unit_rule_set_test02 ( ):

#*****************************************************************************80
#
## gm_unit_rule_set_test02() tests gm_unit_rule_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 4

  m_test = np.array ( [ 2, 3, 5, 10 ] )

  print ( '' )
  print ( 'gm_unit_rule_set_test02' )
  print ( '  gm_unit_rule_set determines the weights and abscissas' )
  print ( '  of a Grundmann-Moeller quadrature rule for' )
  print ( '  the M dimensional unit simplex,' )
  print ( '  using a rule of in index RULE,' )
  print ( '  which will have degree of exactness 2*RULE+1.' )
  print ( '' )
  print ( '  In this test, we compute various rules, and simply' )
  print ( '  report the number of points, and the sum of weights.' )

  print ( '' )
  print ( '   M            RULE    N  WEIGHT SUM' )

  for test in range ( 0, test_num ):

    m = m_test[test]

    print ( '' )

    for rule in range ( 0, 6 ):

      n = gm_rule_size ( rule, m )

      w, x = gm_unit_rule_set ( rule, m, n )

      w_sum = np.sum ( w )

      print ( '  %8d  %8d  %8d  %24.16f' % ( m, rule, n, w_sum ) )

  return

def gm_unit_rule_set_test03 ( ):

#*****************************************************************************80
#
## gm_unit_rule_set_test03() tests gm_unit_rule_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2017
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'gm_unit_rule_set_test03' )
  print ( '  gm_unit_rule_set determines the weights and abscissas' )
  print ( '  of a Grundmann-Moeller quadrature rule for' )
  print ( '  the M dimensional unit simplex,' )
  print ( '  using a rule of index RULE,' )
  print ( '  which will have degree of exactness 2*RULE+1.' )
  print ( '' )
  print ( '  In this test, we write a rule to a file.' )
  print ( '' )

  m = 3
  rule = 2

  print ( '' )
  print ( '  Here we use M = %d' % ( m ) )
  print ( '  RULE = %d' % ( rule ) )
  print ( '  DEGREE = %d' % ( 2 * rule + 1 ) )

  n = gm_rule_size ( rule, m )

  w, x = gm_unit_rule_set ( rule, m, n )

  w_file = 'gm' + str ( rule ) + '_' + str ( m ) + 'd_w.txt'

  w_unit = open ( w_file, 'wt' )

  for j in range ( 0, n ):
    st = '  %g' % ( w[j] )
    w_unit.write ( st )
    w_unit.write ( '\n' )

  w_unit.close ( )

  x_file = 'gm' + str ( rule ) + '_' + str ( m ) + 'd_x.txt'

  x_unit = open ( x_file, 'wt' )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      st = '  %g' % ( x[i,j] )
      x_unit.write ( st )
    x_unit.write ( '\n' )

  x_unit.close ( )

  print ( '' )
  print ( '  Wrote rule %d to "%s" and "%s".' % ( rule, w_file, x_file ) )

  return

def gm_unit_rule_set_test04 ( ):

#*****************************************************************************80
#
## gm_unit_rule_set_test04() tests gm_unit_rule_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  degree_max = 4
  rule_max = 3

  print ( '' )
  print ( 'gm_unit_rule_set_test04' )
  print ( '  gm_unit_rule_set determines the weights and abscissas' )
  print ( '  of a Grundmann-Moeller quadrature rule for' )
  print ( '  the M dimensional unit simplex,' )
  print ( '  using a rule of index RULE,' )
  print ( '  which will have degree of exactness 2*RULE+1.' )
  print ( '' )
  print ( '  In this test, look at all the monomials up to' )
  print ( '  some maximum degree, choose a few low order rules' )
  print ( '  and determine the quadrature error for each.' )
  print ( '' )
  print ( '  Here we use M = %d' % ( m ) )

  print ( '' )
  print ( '      Rule     Order     Quad_Error' )
  print ( '' )

  expon = np.zeros ( m, dtype = np.int32 )

  for degree in range ( 0, degree_max + 1 ):

    more = False
    h = 0
    t = 0

    while ( True ):

      expon, more, h, t = comp_next ( degree, m, expon, more, h, t )

      print ( '' )
      print ( '  F(X) = X1^%d * X2^%d * X3^%d * X4^%d * X5^%d' \
        % ( expon[0], expon[1], expon[2], expon[3], expon[4] ) )

      print ( '' )

      for rule in range ( 0, rule_max + 1 ):
        n = gm_rule_size ( rule, m )
        w, x = gm_unit_rule_set ( rule, m, n )
        quad_error = simplex_unit_monomial_quadrature ( m, expon, n, x, w )
        print ( '  %8d  %8d  %14.6e' % ( rule, n, quad_error ) )

      if ( not more ):
        break

  return

def gm_unit_rule_set_test05 ( ):

#*****************************************************************************80
#
## gm_unit_rule_set_test05() tests gm_unit_rule_set().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  e_test = np.array ( [ \
    [ 0, 1, 0, 0, 2, 1, 1, 0, 0, 0 ], \
    [ 0, 0, 1, 0, 0, 1, 0, 2, 1, 0 ], \
    [ 0, 0, 0, 1, 0, 0, 1, 0, 1, 2 ] ] )

  print ( '' )
  print ( 'gm_unit_rule_set_test05' )
  print ( '  gm_unit_rule_set determines the weights and abscissas' )
  print ( '  of a Grundmann-Moeller quadrature rule for' )
  print ( '  the M dimensional unit simplex,' )
  print ( '  using a rule of index RULE,' )
  print ( '  which will have degree of exactness 2*RULE+1.' )

  print ( '  In this test, look at all the monomials up to' )
  print ( '  some maximum degree, choose a few low order rules' )
  print ( '  and determine the quadrature error for each.' )

  m = 3
  volume = simplex_unit_volume ( m )
  print ( '' )
  print ( '  Simplex volume = %g' % ( volume ) )

  print ( '' )
  print ( '         N        1               X               Y ', end = '' )
  print ( '              Z               X^2              XY             XZ', end = '' )
  print ( '              Y^2             YZ               Z^2' )
  print ( '' )

  e = np.zeros ( m )

  for rule in range ( 0, 6 ):

    n = gm_rule_size ( rule, m )

    w, x = gm_unit_rule_set ( rule, m, n )

    print ( '  %8d' % ( n ), end = '' )

    for k in range ( 0, 10 ):

      e[0:m] = e_test[0:m,k]

      value = monomial_value ( m, n, e, x  )

      result = np.dot ( w, value )

      print ( '  %14.6g' % ( result ), end ='' )

    print ( '' )

  return

def i4vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_transpose_print() prints an I4VEC "transposed".
#
#  Example:
#
#    A = (/ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 /)
#    TITLE = 'My vector:  '
#
#    My vector:
#
#       1    2    3    4    5
#       6    7    8    9   10
#      11
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  if ( 0 < n ):
    for i in range ( 0, n ):
      print ( '%8d' % ( a[i] ), end = "" )
      if ( ( i + 1 ) % 10 == 0 or i == n - 1 ):
        print ( '' )
  else:
    print ( '  (empty vector)' )

  return

def i4vec_transpose_print_test ( ):

#*****************************************************************************80
#
## i4vec_transpose_print_test() tests i4vec_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'i4vec_transpose_print_test():' )
  print ( '  i4vec_transpose_print() prints an I4VEC' )
  print ( '  with 5 entries to a row, and an optional title.' )

  n = 12
  a = np.zeros ( n, dtype = np.int32 )
  
  for i in range ( 0, n ):
    a[i] = i + 1

  i4vec_transpose_print ( n, a, '  My array:  ' )

  return

def monomial_value ( m, n, e, x ):

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
#    07 April 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of evaluation points.
#
#    integer E(M), the exponents.
#
#    real X(M,N), the point coordinates.
#
#  Output:
#
#    real V(N), the monomial values.
#
  import numpy as np

  v = np.ones ( n )

  for i in range ( 0, m ):
    if ( 0 != e[i] ):
      for j in range ( 0, n ):
        v[j] = v[j] * x[i,j] ** e[i]

  return v

def r8mat_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_transpose_print() prints an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_transpose_print_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_test() tests r8mat_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_transpose_print_test():' )
  print ( '  r8mat_transpose_print() prints an R8MAT.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8mat_transpose_print ( m, n, v, '  Here is an R8MAT, transposed:' )

  return

def r8mat_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_transpose_print_some() prints a portion of an R8MAT, transposed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ' ),

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ), end = "" )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ), end = "" )
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = "" )

      print ( '' )

  return

def r8mat_transpose_print_some_test ( ):

#*****************************************************************************80
#
## r8mat_transpose_print_some_test() tests r8mat_transpose_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8mat_transpose_print_some_test():' )
  print ( '  r8mat_transpose_print_some() prints some of an R8MAT, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:' )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def simplex_general_volume ( m, t ):

#*****************************************************************************80
#
## simplex_general_volume() computes the volume of a simplex in N dimensions.
#
#  Discussion:
#
#    The formula is: 
#
#      volume = 1/M! * det ( B )
#
#    where B is the M by M matrix obtained by subtracting one
#    vector from all the others.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 March 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the dimension of the space.
#
#    real T(M,M+1), the vertices.
#
#  Output:
#
#    real VOLUME, the volume of the simplex.
#
  import numpy as np

  b = np.zeros ( [ m, m ] )

  b[0:m,0:m] = t[0:m,0:m]
  for j in range ( 0, m ):
    b[0:m,j] = b[0:m,j] - t[0:m,m]

  volume = abs ( np.linalg.det ( b ) )

  for i in range ( 1, m + 1 ):
    volume = volume / float ( i )
  
  return volume

def simplex_unit_monomial_integral ( m, e ):

#*****************************************************************************80
#
## simplex_unit_monomial_integral(): integrals in the unit simplex in M dimensions.
#
#  Discussion:
#
#    The monomial is F(X) = product ( 1 <= I <= M ) X(I)^E(I).
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
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer E(M), the exponents.  
#    Each exponent must be nonnegative.
#
#  Output:
#
#    real INTEGRAL, the integral.
#
  for i in range ( 0, m ):
    if ( e[i] < 0 ):
      print ( '' )
      print ( 'simplex_unit_monomial_integral - Fatal error!' )
      print ( '  All exponents must be nonnegative.' )
      raise Exception ( 'simplex_unit_monomial_integral - Fatal error!' )

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

def simplex_unit_monomial_integral_test ( rng ):

#*****************************************************************************80
#
## simplex_unit_monomial_integral_test() tests simplex_unit_monomial_integral().
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
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  m = 3
  n = 4192
  test_num = 20

  print ( '' )
  print ( 'simplex_unit_monomial_integral_test():' )
  print ( '  Estimate monomial integrals using Monte Carlo' )
  print ( '  over the interior of the unit simplex in M dimensions.' )
#
#  Get sample points.
#
  x = simplex_unit_sample ( m, n, rng )

  print ( '' )
  print ( '  Number of sample points used is %d' % ( n ) )
#
#  Randomly choose exponents.
#
  print ( '' )
  print ( '  We randomly choose the exponents.' )
  print ( '' )
  print ( '  Ex  Ey  Ez     MC-Estimate      Exact           Error' )
  print ( '' )

  for test in range ( 0, test_num ):

    e = rng.integers ( low = 0, high = 4, size = m, endpoint = True )

    value = monomial_value ( m, n, e, x )

    result = simplex_unit_volume ( m ) * np.sum ( value ) / float ( n )
    exact = simplex_unit_monomial_integral ( m, e )
    error = abs ( result - exact )

    for i in range ( 0, m ):
      print ( '  %2d' % ( e[i] ), end = "" )
    print ( '  %14.6g  %14.6g  %10.2g' % ( result, exact, error ) )

  return

def simplex_unit_monomial_quadrature ( m, expon, n, x, w ):

#*****************************************************************************80
#
## simplex_unit_monomial_quadrature(): quadrature of monomials in a unit simplex.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 March 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer EXPON(M), the exponents.
#
#    integer N, the number of points in the rule.
#
#    real X(M,N), the quadrature points.
#
#    real W(N), the quadrature weights.
#
#  Output:
#
#    real QUAD_ERROR, the quadrature error.
#
  import numpy as np
#
#  Get the exact value of the integral of the unscaled monomial.
#
  scale = simplex_unit_monomial_integral ( m, expon )
#
#  Evaluate the monomial at the quadrature points.
#
  value = monomial_value ( m, n, expon, x )
#
#  Compute the weighted sum and divide by the exact value.
#
  quad = np.dot ( w, value ) / scale
#
#  Error:
#
  exact = 1.0
  quad_error = abs ( quad - exact )

  return quad_error

def simplex_unit_sample ( m, n, rng ):

#*****************************************************************************80
#
## simplex_unit_sample() samples the unit simplex in M dimensions.
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
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation, and Sensitivity
#    of Queueing Networks,
#    Krieger, 1992,
#    ISBN: 0894647644,
#    LC: QA298.R79.
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of points.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real X(M,N), the points.
#
  import numpy as np

  x = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):

    e = rng.random ( size = m + 1 )

    e_sum = 0.0
    for i in range ( 0, m + 1 ):
      e[i] = - np.log ( e[i] )
      e_sum = e_sum + e[i]

    for i in range ( 0, m ):
      x[i,j] = e[i] / e_sum

  return x

def simplex_unit_sample_test ( rng ):

#*****************************************************************************80
#
## simplex_unit_sample_test() tests simplex_unit_sample().
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
 #  Input:
#
#    rng(): the current random number generator.
#
  print ( '' )
  print ( 'simplex_unit_sample_test():' )
  print ( '  simplex_unit_sample() samples the unit simplex in M dimensions.' )

  m = 3
  n = 10
  x = simplex_unit_sample ( m, n, rng )

  r8mat_transpose_print ( m, n, x, '  Sample points in the unit simplex.' )

  return

def simplex_unit_to_general ( m, n, t, ref ):

#*****************************************************************************80
#
## simplex_unit_to_general() maps the unit simplex to a general simplex.
#
#  Discussion:
#
#    Given that the unit simplex has been mapped to a general simplex
#    with vertices T, compute the images in T, under the same linear
#    mapping, of points whose coordinates in the unit simplex are REF.
#
#    The vertices of the unit simplex are listed as suggested in the
#    following:
#
#      (0,0,0,...,0)
#      (1,0,0,...,0)
#      (0,1,0,...,0)
#      (0,0,1,...,0)
#      (...........)
#      (0,0,0,...,1)
#
#    Thanks to Andrei ("spiritualworlds") for pointing out a mistake in the
#    previous implementation of this routine, 02 March 2008.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 March 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer N, the number of points to transform.
#
#    real T(M,M+1), the vertices of the
#    general simplex.  
#
#    real REF(M,N), points in the 
#    reference triangle.
#
#  Output:
#
#    real PHY(M,N), corresponding points 
#    in the physical triangle.
#
  import numpy as np
#
#  The image of each point is initially the image of the origin.
#
#  Insofar as the pre-image differs from the origin in a given vertex
#  direction, add that proportion of the difference between the images
#  of the origin and the vertex.
#
  phy = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):

    for j in range ( 0, n ):

      phy[i,j] = t[i,0]

      for vertex in range ( 1, m + 1 ):

        phy[i,j] = phy[i,j] + ( t[i,vertex] - t[i,0] ) * ref[vertex-1,j]

  return phy

def simplex_unit_to_general_test01 ( rng ):

#*****************************************************************************80
#
## simplex_unit_to_general_test01() tests simplex_unit_to_general().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  m = 2
  n = 10

  t = np.array ( [ \
    [ 1.0, 3.0, 2.0 ], \
    [ 1.0, 1.0, 5.0 ] ] )

  t_unit = np.array ( [ \
    [ 0.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0 ] ] )

  print ( '' )
  print ( 'simplex_unit_to_general_test01' )
  print ( '  simplex_unit_to_general' )
  print ( '  maps points in the unit simplex to a general simplex.' )
  print ( '' )
  print ( '  Here we consider a simplex in 2D, a triangle.' )
  print ( ''  )
  print ( '  The vertices of the general triangle are:' )
  print ( '' )
  for j in range ( 0, m + 1 ):
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( t[i,j] ), end = "" )
    print ( '' )

  print ( '' )
  print ( '   (  XSI     ETA )   ( X       Y  )' )
  print ( '' )

  phy_unit = simplex_unit_to_general ( m, m+1, t, t_unit )

  for j in range ( 0, m + 1 ):
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( t_unit[i,j] ), end = "" )
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( phy_unit[i,j] ), end = "" )
    print ( '' )

  ref = simplex_unit_sample ( m, n, rng )

  phy = simplex_unit_to_general ( m, n, t, ref )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( ref[i,j] ), end = "" )
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( phy[i,j] ), end = "" )
    print ( '' )

  return

def simplex_unit_to_general_test02 ( rng ):

#*****************************************************************************80
#
## simplex_unit_to_general_test02() tests simplex_unit_to_general().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2008
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  m = 3
  n = 10

  t = np.array ( [ \
    [ 1.0, 3.0, 1.0, 1.0 ], \
    [ 1.0, 1.0, 4.0, 1.0 ], \
    [ 1.0, 1.0, 1.0, 5.0 ] ] )

  t_unit = np.array ( [ \
    [ 0.0, 1.0, 0.0, 0.0 ], \
    [ 0.0, 0.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 0.0, 1.0 ] ] )

  print ( '' )
  print ( 'simplex_unit_to_general_test02' )
  print ( '  simplex_unit_to_general' )
  print ( '  maps points in the unit simplex to a general simplex.' )
  print ( '' )
  print ( '  Here we consider a simplex in 3D, a tetrahedron.' )
  print ( '' )
  print ( '  The vertices of the general tetrahedron are:' )
  print ( '' )
  for j in range ( 0, m + 1 ):
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( t[i,j] ), end = "" )
    print ( '' )

  print ( '' )
  print ( '   (  XSI     ETA )   ( X       Y  )' )
  print ( '' )

  phy_unit = simplex_unit_to_general ( m, m+1, t, t_unit )

  for j in range ( 0, m + 1 ):
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( t_unit[i,j] ), end = "" )
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( phy_unit[i,j] ), end = "" )
    print ( '' )

  ref = simplex_unit_sample ( m, n, rng )

  phy = simplex_unit_to_general ( m, n, t, ref )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( ref[i,j] ), end = "" )
    for i in range ( 0, m ):
      print ( '  %8.4f' % ( phy[i,j] ), end = "" )
    print ( '' )

  return

def simplex_unit_volume ( m ):

#*****************************************************************************80
#
## simplex_unit_volume() returns the volume of the unit simplex in M dimensions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 January 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#  Output:
#
#    real VALUE, the volume.
#
  value = 1.0
  for i in range ( 1, m + 1 ):
    value = value / float ( i )

  return value

def simplex_unit_volume_test ( ) :

#*****************************************************************************80
#
## simplex_unit_volume_test() tests simplex_unit_volume().
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
  print ( '' )
  print ( 'simplex_unit_volume_test():' )
  print ( '  simplex_unit_volume() returns the volume of the unit simplex' )
  print ( '  in M dimensions.' )
  print ( '' )
  print ( '   M   Volume' )
  print ( '' )

  for m in range ( 1, 10 ):
    value = simplex_unit_volume ( m )
    print ( '  %2d  %g' % ( m, value ) )

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def simplex_gm_rule_test ( ):

#*****************************************************************************80
#
## simplex_gm_rule_test() tests simplex_gm_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'simplex_gm_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test simplex_gm_rule().' )

  rng = default_rng ( )

  comp_next_test ( )
  gm_general_rule_set_test01 ( )
  gm_general_rule_set_test02 ( )
  gm_rule_size_test ( )
  gm_unit_rule_set_test01 ( )
  gm_unit_rule_set_test02 ( )
  gm_unit_rule_set_test03 ( )
  gm_unit_rule_set_test04 ( )
  gm_unit_rule_set_test05 ( )
  simplex_unit_monomial_integral_test ( rng )
  simplex_unit_to_general_test01 ( rng )
  simplex_unit_to_general_test02 ( rng )
  simplex_unit_sample_test ( rng )
  simplex_unit_volume_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'simplex_gm_rule_test():' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  simplex_gm_rule_test ( )
  timestamp ( )
