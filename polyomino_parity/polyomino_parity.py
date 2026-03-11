#! /usr/bin/env python3
#
def addmultisteps ( p, ns, steps ):

#*****************************************************************************80
#
## addmultisteps() computes all possible sums from a set.
#
#  Discussion:
#
#    This function calculates all possible sums of N1 elements from the set
#    {+Q1,-Q1}, N2 elements from {+Q2,-Q2}, N3 elements from {+Q3,-Q3}, etc., 
#    and then checks to see how many of these sums equals P
#
#  Modified:
#
#    22 Jan 2019
#
#  Author:
#
#    Marcus Garvie
#
#  Input:
#
#    integer P, the target sum.
#
#    integer NS(): a row vector of positive integers, corresponding to the
#    number of steps N1, N2, etc we take with the step-magnitudes in STEPS
#
#    integer STEPS(): a row vector of distinct positive integers, corresponding
#    to the step-magnitudes Q1, Q2, etc 
#
#  Output:
#
#    integer S(): a row vector of integers corresponding to all possible sums 
#    of N1, N2, etc  choices from the sets {+Q1,-Q1}, {+Q2,-Q2}, etc
#    respectively
#
#    integer NO_SUMS: the total number of sums in S
#
#    integer NUM: a non-negative integer, yielding the number of sums in S
#    that equal P
#
  import numpy as np

  col = len ( ns )
#
#  Recursively call sumallsteps() to calculate all possible sums.
#
  s = np.array ( [ 0 ] )
  for i in range ( 0, col ):
    s = sumallsteps ( s, ns[i], steps[i] )
# 
#  Determine how many sums equal P.
#
  np.sort ( s )
  no_sums = len ( s )
  num = np.count_nonzero ( s == p )

  return num, no_sums, s

def addmultisteps_test ( ):

#*****************************************************************************80
#
## addmultisteps_test() tests addmultisteps().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2020
#
#  Author:
#
#    Marcus Garvie,
#    John Burkardt
#
#  Reference:
#
#    Marcus Garvie, John Burkardt,
#    Checkerboard Colouring Arguments For Impossible Polyomino 
#    Tiling Problems,
#    In preparation.
#
  import numpy as np

  print ( '' )
  print ( 'addmultisteps_test():' )
  print ( '  [ num, no_sums, s ] = addmultisteps ( p, ns, steps )' )
  print ( '  input:' )
  print ( '    P is the parity of the region.' )
  print ( '    NS is a vector of step counts.' )
  print ( '    STEPS is a vector of step sizes.' )   
  print ( '  output:' )
  print ( '    NUM is the number of sums equal to P.' )
  print ( '    NO_SUMS is the number of sums generated.' )
  print ( '    S, contains every sum computed.' )

  for test in range ( 0, 3 ):

    if ( test == 0 ):
      p = 0
      ns = np.array ( [ 2, 5, 3, 6, 7 ] )
      steps = np.array ( [ 1, 3, 2, 5, 9 ] )
      correct = 56
    elif ( test == 1 ):
      p = 4
      ns = np.array ( [ 1, 1, 3 ] )
      steps = np.array ( [ 1, 3, 4 ] )
      correct = 0
    elif ( test == 2 ):
      p = 4
      ns = np.array ( [ 3, 1, 1 ] )
      steps = np.array ( [ 1, 3, 4 ] )
      correct = 2

    n = len ( ns )

    print ( '' )
    print ( '  For this example:' )
    print ( '    P =', p )
    print ( '    NS = [', end = '' )
    for i in range ( 0, n ):
      print ( ns[i], end = '' )
      if ( i < n - 1 ):
        print ( ',', end = '' )
      else:
        print ( ' ]' )

    print ( '    STEPS = [', end = '' )
    for i in range ( 0, n ):
      print ( steps[i], end = '' )
      if ( i < n - 1 ):
        print ( ',', end = '' )
      else:
        print ( ' ]' )

    num, no_sums, s = addmultisteps ( p, ns, steps )

    print ( '' )
    print ( ' ', num, 'sums equal to P were found:' )
    print ( '  Correct number of such sums is', correct )
    print ( ' ', no_sums, 'sums were generated:' )

  return

def diophantine_equation_print ( a, b ):

#*****************************************************************************80
#
## diophantine_equation_print() prints a Diophantine equation.
#
#  Discussion:
#
#     A Diophantine equation has the form:
#
#       a1 x1 + a2 x2 + ... + an xn = b
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer a(n): the coefficients of the Diophantine equation.
#
#    integer b: the right hand side of the Diophantine equation.
#
  n = len ( a )

  for i in range ( 0, n ):
    if ( i == 0 ):
      print ( '    ', a[i], '* x', i+1, end = '' )
    else:
      print ( ' +', a[i], '* x', i+1, end = '' )
  print ( ' =', b )

  return

def diophantine_nd_check ( a, b ):

#*****************************************************************************80
#
## diophantine_nd_check() checks a proposed Diophantine problem.
#
#  Discussion:
#
#     We are given a Diophantine equation 
#
#       a1 x1 + a2 x2 + ... + an * xn = b
#
#     for which all positive or nonnegative solutions are sought.
#
#     For this problem to be well posed, we require:
#     *) All coefficients A are positive.
#     *) All coefficients A are integers.
#     *) At least one coefficient A must be positive.
#     *) The right hand side B must be nonnegative.
#     *) The right hand side B must be an integer.
#     *) If G is the greatest common divisor of A,
#        then B must be divisible by G.
#
#     If any of these requirements fails, the problem is not suitable for
#     treatment by diophantine_nd_nonnegative() or diophantine_nd_positive().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer a(n): the coefficients of the Diophantine equation.
#
#    integer b: the right hand side.
#
#  Output:
#
#    logical check: true if this problem is well posed.
#
  import numpy as np

  check = False

  if ( np.any ( a <= 0 ) ):
    print ( 'diophantine_nd_check(): a has a nonpositive entry.' )
    return check

  if ( not i4vec_is_integer ( a ) ):
    print ( 'diophantine_nd_check(): some a is not an integer.' )
    return check

  if ( np.sum ( a ) <= 0 ):
    print ( 'diophantine_nd_check(): a does not have a positive entry.' )
    return check

  if ( b < 0 ):
    print ( 'diophantine_nd_check(): b is negative.' )
    return check

  d = i4vec_gcd ( a )
  if ( np.mod ( b, d ) != 0 ):
    print ( 'diophantine_nd_check(): b is not divisible by gcd ( a ).' )
    return check

  check = True
 
  return check

def diophantine_nd_nonnegative ( a, b ):

#*****************************************************************************80
#
## diophantine_nd_nonnegative() finds nonnegative diophantine solutions.
#
#  Discussion:
#
#     We are given a Diophantine equation 
#
#       a1 x1 + a2 x2 + ... + an * xn = b
#
#     for which the coefficients a are positive integers, and
#     the right hand side b is a nonnegative integer.
#
#     We are seeking all nonnegative integer solutions x.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer a(n): the coefficients of the Diophantine equation.
#
#    integer b: the right hand side.
#
#  Output:
#
#    integer x(k,n): solutions to the equation.
#
  import numpy as np
#
#  Initialize.
#
  n = len ( a )
  x = np.empty ( [ 0, n ] )
  j = 0
  k = 0
  r = b
  y = np.zeros ( [ 1, n ] )
#
#  Construct a vector Y that is a possible solution.
#
  while ( True ):

    r = b - sum ( a[0:j] * y[0,0:j] )
#
#  We have a partial vector Y.  Get next component.
#
    if ( j < n ):
      y[0,j] = np.floor ( r / a[j] )
      j = j + 1
#
#  We have a full vector Y.
#
    else:
#
#  Is it a solution?
#
      if ( r == 0 ):

        x = np.append ( x, y, axis = 0 )
#  
#  Find last nonzero Y entry, decrease by 1 and resume search.
#
      while ( 0 < j ):

        if ( 0 < y[0,j-1] ):
          y[0,j-1] = y[0,j-1] - 1
          break
        j = j - 1
#
#  End the search.
#
      if ( j == 0 ):
        break

  return x

def diophantine_nd_nonnegative_test ( ):

#*****************************************************************************80
#
## diophantine_nd_nonnegative_test() tests diophantine_nd_nonnegative().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'diophantine_nd_nonnegative_test():' )
  print ( '  diophantine_nd_nonnegative() returns nonnegative solutions' )
  print ( '  of a Diophantine equation in N variables.' )

  a = np.array ( [ 2, 3 ] )
  b = 18
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    x = diophantine_nd_nonnegative ( a, b )
    diophantine_solution_print ( a, b, x )

  a = np.array ( [ 6, 3, 13 ] )
  b = 16
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    x = diophantine_nd_nonnegative ( a, b )
    diophantine_solution_print ( a, b, x )

  a = np.array ( [ 12, 9, 7 ] )
  b = 60
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    x = diophantine_nd_nonnegative ( a, b )
    diophantine_solution_print ( a, b, x )

  a = np.array ( [ 2, 3, 5, 6 ] )
  b = 24
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    x = diophantine_nd_nonnegative ( a, b )
    diophantine_solution_print ( a, b, x )

  a = np.array ( [ 2, 3, 5, 6, 7 ] )
  b = 35
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    x = diophantine_nd_nonnegative ( a, b )
    diophantine_solution_print ( a, b, x )

  return

def diophantine_nd_positive ( a, b ):

#*****************************************************************************80
#
## diophantine_nd_positive() finds positive diophantine solutions.
#
#  Discussion:
#
#     We are given a Diophantine equation 
#
#       a1 x1 + a2 x2 + ... + an * xn = b
#
#     for which the coefficients a are positive integers, and
#     the right hand side b is a nonnegative integer.
#
#     We are seeking all strictly positive integer solutions x.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer a(n): the coefficients of the Diophantine equation.
#
#    integer b: the right hand side.
#
#  Output:
#
#    integer x(k,n): solutions to the equation.
#
  import numpy as np

  beta = b - sum ( a )

  if ( beta < 0 ):
    n = len ( a )
    x = np.empty ( [ 0, n ] )
    return x

  x = diophantine_nd_nonnegative ( a, beta )
#
#  Increase every component by 1.
#
  x = x + 1

  return x

def diophantine_nd_positive_test ( ):

#*****************************************************************************80
#
## diophantine_nd_positive_test() tests diophantine_nd_positive().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'diophantine_nd_positive_test():' )
  print ( '  diophantine_nd_positive() returns the positive solutions' )
  print ( '  of a Diophantine equation in N variables.' )

  a = np.array ( [ 2, 3 ] )
  b = 18
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    x = diophantine_nd_positive ( a, b )
    diophantine_solution_print ( a, b, x )

  a = np.array ( [ 6, 3, 13 ] )
  b = 16
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    x = diophantine_nd_positive ( a, b )
    diophantine_solution_print ( a, b, x )

  a = np.array ( [ 12, 9, 7 ] )
  b = 60
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    x = diophantine_nd_positive ( a, b )
    diophantine_solution_print ( a, b, x )

  a = np.array ( [ 2, 3, 5, 6 ] )
  b = 24
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    x = diophantine_nd_positive ( a, b )
    diophantine_solution_print ( a, b, x )

  a = np.array ( [ 2, 3, 5, 6, 7 ] )
  b = 35
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    x = diophantine_nd_positive ( a, b )
    diophantine_solution_print ( a, b, x )

  return

def diophantine_solution_print ( a, b, x ):

#*****************************************************************************80
#
## diophantine_solution_print() prints a Diophantine solution.
#
#  Discussion:
#
#     A Diophantine equation has the form:
#
#       a1 x1 + a2 x2 + ... + an xn = b
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer a(n): the coefficients of the Diophantine equation.
#
#    integer b: the right hand side of the Diophantine equation.
#
#    integer x(x_num,n): the solutions.
#
  n = len ( a )
  x_num = len ( x )

  print ( '' )
  print ( '  ', x_num, 'solutions found.' )
  if ( 0 < x_num ):
    print ( '' )

  for i in range ( 0, x_num ):

    b2 = sum ( a[0:n] * x[i,0:n] )

    if ( b2 != b ):
      print ( 'BOGUS', i, ':', end = '' )
    else:
      print ( '     ', i, ':', end = '' )

    for j in range ( 0, n ):
      if ( j == 0 ):
        print ( ' ', a[j], '*', x[i,j], end = '' )
      else:
        print ( ' +', a[j], '*', x[i,j], end = '' )

    print ( ' =', b2 )

  return

def is_integer_test ( ) :

#*****************************************************************************80
#
## is_integer_test() tests is_integer().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'is_integer_test():' )
  print ( '  arg.is_integer is True if arg has an integer value.' )
  print ( ' ' )
  print ( '         arg  arg.is_integer' )
  print ( ' ' )
  arg = np.pi
  print ( '  ', arg, '  ', arg.is_integer )
  arg = 1+2j
  print ( '  ', arg, '  ', arg.is_integer )
  arg = 3+0j
  print ( '  ', arg, '  ', arg.is_integer )
  arg = np.finfo(float).eps
  print ( '  ', arg, '  ', arg.is_integer )
  arg = 3.0
  print ( '  ', arg, '  ', arg.is_integer )
  arg = 0
  print ( '  ', arg, '  ', arg.is_integer )
  arg = -17
  print ( '  ', arg, '  ', arg.is_integer )
  arg = np.Inf
  print ( '  ', arg, '  ', arg.is_integer )
  arg = np.NAN
  print ( '  ', arg, '  ', arg.is_integer )

  return

def i4vec_gcd ( v ):

#*****************************************************************************80
#
## i4vec_gcd() returns the greatest common divisor of an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#    The value GCD returned has the property that it is the greatest integer
#    which evenly divides every entry of V.
#
#    The entries in V may be negative.
#
#    Any zero entries in V are ignored.  If all entries of V are zero,
#    GCD is returned as 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer V(:), the vector.
#
#  Output:
#
#    integer VALUE, the greatest common divisor of V.
#
  import numpy as np

  n = len ( v )

  value = abs ( v[0] )

  for i in range ( 1, n ):
    value = np.gcd ( value, v[i] )

  return value

def i4vec_gcd_test ( ):

#*****************************************************************************80
#
## i4vec_gcd_test() tests i4vec_gcd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
  from i4vec_print import i4vec_print
  import numpy as np

  n = 4;
  i4vec = np.array ( [ \
    2**3*3   *5   *7*11   *13, \
    2   *3**2*5   *7*11   *13, \
    2   *3   *5**3*7*11   *13, \
    2   *3   *5   *7*11**2*13 ] )

  print ( '' );
  print ( 'i4vec_gcd_test():' )
  print ( '  i4vec_gcd() computes the greatest common divisor of the' )
  print ( '  entries in an I4VEC.' )

  i4vec_print ( n, i4vec, '  The I4VEC:' )

  value = i4vec_gcd ( i4vec )

  print ( '' )
  print ( '  GCD = ', value )

  return

def i4vec_is_integer ( a ):

#*****************************************************************************80
#
## i4vec_is_integer() is TRUE if all entries of an I4VEC are integer.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    type A(:), the array.
#
#  Output:
#
#    logical VALUE, is true if all entries are integer.
#
  value = True

  for i in range ( 0, len ( a ) ):
    if ( not a[i].is_integer ):
      value = False
      break

  return value

def polyomino_parity_test ( ):

#*****************************************************************************80
#
## polyomino_parity_test() tests polyomino_parity().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'polyomino_parity_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test polyomino_parity().' )

  addmultisteps_test ( )
  diophantine_nd_nonnegative_test ( )
  diophantine_nd_positive_test ( )
  pv_search_test ( )
  sumallsteps_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'polyomino_parity_test():' )
  print ( '  Normal end of execution.' )
  return

def pv_search ( parities, orders, p, c ):

#*****************************************************************************80
#
## pv_search() searches for parity violations.
#
#  Discussion:
#
#    This function considers possible tilings of a region by polyominoes.
#
#    It first determines all combinations of the polyominoes which 
#    have the same total area as the region.
#
#    Then it uses parity arguments to reject certain solutions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2020
#
#  Author:
#
#    Marcus Garvie,
#    John Burkardt
#
#  Input:
#
#    integer parities(nf): the parity of each polyomino.
#
#    integer orders(nf): the area each polyomino.
#
#    integer p: the parity of the region to be tiled.
#
#    integer c: the area of the region to be tiled.
#
#  Output:
#
#    integer S1(k1,nf): k1 solutions to the area equation for which
#    a trivial parity violation was found.
#
#    integer S2(k2,nf): k2 solutions to the area equation for which
#    a serious parity violation was found.
#
  import numpy as np

  nf = len ( parities )
  s1 = np.zeros ( [ 0, nf ] )
  s2 = np.zeros ( [ 0, nf ] )
#
#  Seek solutions of the area equation, { (n1, n2, ..., nF) }
#
  s = diophantine_nd_positive ( orders, c ) 
# ns, ks = s.shape
  ns = len ( s )

  if ( ns == 0 ):
    print ( 'pv_search():' )
    print ( '  No solutions to area equation found.' )
    return s1, s2

  flags = np.zeros ( ns )
#
#  Remove the r zero parities.
#
  pnz = np.nonzero ( parities )
  pos_parities = parities[pnz]
#
#  Check for parity violations in each area equation solution.
# 
  for i in range ( 0, ns ):
#
#  Remove any n_i values corresponding to parities p_i = 0, 
#  i.e.,  [n_{r+1}, n_{r+2}, ..., n_F].
#
    sp = s[i,pnz]
#   sp = np.nonzeros ( ( parities > 0 ) * s[i,:] )
#
#  Flag trivial parity violations.
#
    ps = np.sum ( pos_parities * sp )

    if ( ps < p ):
      flags[i] = 1
      continue
#
#  pos_parities*Sp = p_{r+1}*n_{r+1} + ... + p_F*n_F
#
    k = ( p + ps ) / 2  
#
#  Solve for solutions { (a_{r+1}, a_{r+2}, ..., a_F) }
#
    t = diophantine_nd_nonnegative ( pos_parities, k )
    nt = len ( t )
#   nt, kt = t.shape
#
#  There is a serious parity violation, unless at least one of the T 
#  solutions satisfies the parity condition.
# 
    flags[i] = 2
#
#  If, for any T, we have all a_k <= n_k, then S(i) does not violate parity.
#
    for j in range ( 0, nt ):

      if ( np.all ( t[j,:] <= sp ) ):
        flags[i] = 0
        break
#
#  Use the flag array to gather the trivial and serious parity violations.
#
#  S1 = rows of S with iflag = 1 (trivial parity violation).
#  S2 = rows of S with iflag = 2 (serious parity violation).
#
  i1 = np.nonzero ( flags == 1 )
  s1 = s[i1]

  i2 = np.nonzero ( flags == 2 )
  s2 = s[i2]

  return s1, s2

def pv_search_post ( s1, s2 ):

#*****************************************************************************80
#
## pv_search_post() reports the results of a search for parity violations.
#
#  Discussion:
#
#    Call this function with the results from pv_search().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2020
#
#  Author:
#
#    Marcus Garvie,
#    John Burkardt
#
#  Input:
#
#    integer S1(k1,nf): k1 solutions to the area equation for which
#    a trivial parity violation was found.
#
#    integer S2(k2,nf): k2 solutions to the area equation for which
#    a serious parity violation was found.
#
  k1, nf = s1.shape
  print ( '' )
  print ( ' ', k1, 'trivial parity violations were found:' )
  if ( 0 < k1 ):
    print ( '' )
    for i in range ( 0, k1 ):
      print ( ' ', i, ': [', end = '' )
      for j in range ( 0, nf ):
        print ( s1[i,j], end = '' )
        if ( j < nf - 1 ):
          print ( ',', end = '' )
        else:
          print ( ' ]' )

  k2, nf = s2.shape
  print ( '' )
  print ( ' ', k2, 'strong parity violations were found:' )
  if ( 0 < k2 ):
    print ( '' )
    for i in range ( 0, k2 ):
      print ( ' ', i, ': [', end = '' )
      for j in range ( 0, nf ):
        print ( s2[i,j], end = '' )
        if ( j < nf - 1 ):
          print ( ',', end = '' )
        else:
          print ( ' ]' )

  return

def pv_search_test ( ):

#*****************************************************************************80
#
## pv_search_test() tests pv_search().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2020
#
#  Author:
#
#    Marcus Garvie,
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'pv_search_test():' )
  print ( '  pv_search() applies parity arguments to potential' )
  print ( '  solutions of a polyomino tiling problem.' )

  for test in range ( 0, 3 ):

    if ( test == 0 ):
      label = '  Example 6'
      parities = np.array ( [ 0, 1 ] )
      orders = np.array ( [ 4, 3 ] )
      p = 9
      c = 41
    elif ( test == 1 ):
      label = '  Example 8'
      parities = np.array ( [ 0, 2, 3, 5 ] )
      orders = np.array ( [ 2, 4, 5, 9 ] )
      p = 0
      c = 156
    elif ( test == 2 ):
      label = '  Example 9'
      parities = np.array ( [ 0, 1, 2, 5 ] )
      orders = np.array ( [ 4, 3, 6, 13 ] )
      p = 0
      c = 320

    n = len ( parities )

    print ( '' )
    print ( label )

    print ( '  parities = [', end = '' )
    for i in range ( 0, n ):
      print ( parities[i], end = '' )
      if ( i < n - 1 ):
        print ( ',', end = '' )
      else:
        print ( ']' )

    print ( '  orders = [', end = '' )
    for i in range ( 0, n ):
      print ( orders[i], end = '' )
      if ( i < n - 1 ):
        print ( ',', end = '' )
      else:
        print ( ']' )

    print ( '  p =', p )

    print ( '  c =', c )
#
#  Search for parity violations.
#
    S1, S2 = pv_search ( parities, orders, p, c )
#
#  Report results.
#
    pv_search_post ( S1, S2 )

  return

def sumallsteps ( a, n, q ):

#*****************************************************************************80
#
## sumallsteps() finds all sums of A + N signed copies of Q.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 June 2020
#
#  Author:
#
#    Marcus Garvie
#    John Burkardt
#
#  Input:
#
#    integer A(na): the vector to be incremented.
#
#    integer N: the number of steps to take.
#
#    integer Q: the magnitude of the steps.
#
#  Output:
#
#    integer S(na*(n+1)): all sums of an entry of A and N signed copies of Q.
#
  import numpy as np

  na = len ( a )
  nb = n + 1

  b = np.arange ( -n, n+2, 2 ) * q

  x, y = np.meshgrid ( a, b )
  s = x + y
  s = np.reshape ( s, na * nb )
  s.flatten ( )
  np.sort ( s )

  return s

def sumallsteps_test ( ):

#*****************************************************************************80
#
## sumallsteps_test() tests sumallsteps().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 June 2020
#
#  Author:
#
#    Marcus Garvie,
#    John Burkardt
#
#  Reference:
#
#    Marcus Garvie, John Burkardt,
#    Checkerboard Colouring Arguments For Impossible Polyomino 
#    Tiling Problems,
#    In preparation.
#
  import numpy as np

  print ( '' )
  print ( 'sumallsteps_test:' )
  print ( '  sumallsteps() finds all possible sums, of the form' )
  print ( '    S = Ai + N * ( +/- Q )' )
  print ( '  where:' )
  print ( '    Ai is any single entry of the vector A' )
  print ( '    N counts the number of +/- Q values to be added.' )
  print ( '    Q is the magnitude of the increments or steps.' )
#
#  Example from paper.
#  Correct result:
#    S_num = 18
#    S = [ -15, -14, -11, -10, -7, -6, -3, -2, 1, 2, 5, 6, 9, 10, 13, 14, 17, 18 ].
#
  A = np.array ( [ 1, 2 ] )
  N = 8
  Q = 2

  print ( '' )
  print ( '  For this example:' )
  print ( '    A = [', end = '' )
  for i in range ( 0, len ( A ) ):
    print ( ' %d' % ( A[i] ), end = '' )
    if ( i < len ( A ) - 1 ):
      print ( ',', end = '' )
    else:
      print ( ' ]' )
  print ( '    N =', N )
  print ( '    Q =', Q )

  S = sumallsteps ( A, N, Q )

  S_num = len ( S )
  print ( '' )
  print ( ' ', S_num, 'distinct sums were found:' )
  print ( '' )
  for i in range ( 0, S_num ):
    print ( '  %2d: %3d' % ( i, S[i] ) )

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
  polyomino_parity_test ( )
  timestamp ( )

