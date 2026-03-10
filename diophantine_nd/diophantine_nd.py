#! /usr/bin/env python3
#
def diophantine_bounds_print ( lo, hi ):

#*****************************************************************************80
#
## diophantine_bounds_print() prints bounds on solutions of a Diophantine equation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer lo(n), hi(n): the lower and upper bounds for each component.
#    Any component of lo() can be -Inf, and any component of hi() can be +Inf.
#
  import numpy as np

  n = len ( lo )

  print ( '' )
  print ( '  Bounds imposed on Diophantine equation solutions:' )
  print ( '' )
  for i in range ( 0, n ):
    if ( np.isinf ( lo[i] ) and np.isinf ( hi[i] ) ):
      print ( '  x(%d) is free' % ( i ) )
    elif ( np.isinf ( lo[i] ) ):
      print ( '  x(%d) <= %d' % ( i, hi[i] ) )
    elif ( np.isinf ( hi[i] ) ):
      print ( '  %d <= x(%d)' % ( lo[i], i ) )
    else:
      print ( '  %d <= x(%d) <= %d' % ( lo[i], i, hi[i] ) )

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
    print ( 'diophantine_nd_check: a has a nonpositive entry.' )
    return check

  if ( not i4vec_is_integer ( a ) ):
    print ( 'diophantine_nd_check: some a is not an integer.' )
    return check

  if ( np.sum ( a ) <= 0 ):
    print ( 'diophantine_nd_check: a does not have a positive entry.' )
    return check

  if ( b < 0 ):
    print ( 'diophantine_nd_check: b is negative.' )
    return check

  d = i4vec_gcd ( a )
  if ( np.mod ( b, d ) != 0 ):
    print ( 'diophantine_nd_check: b is not divisible by gcd ( a ).' )
    return check

  check = True
 
  return check

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
  x = np.empty ( [ 0, n ], dtype = int )
  j = 0
  k = 0
  r = b
  y = np.zeros ( [ 1, n ], dtype = int )
#
#  Construct a vector Y that is a possible solution.
#
  while ( True ):

    r = b - sum ( a[0:j] * y[0,0:j] )
#
#  We have a partial vector Y.  Get next component.
#
    if ( j < n ):
      y[0,j] = int ( np.floor ( r / a[j] ) )
      j = j + 1
#
#  We have a full vector Y.
#
    else:
#
#  If Y is a solution, add it to our list.
#
      if ( r == 0 ):

        x = np.append ( x, y, axis = 0 )
#  
#  Find last nonzero Y entry, decrease it by 1 and resume search.
#
      while ( 0 < j ):

        if ( 0 < y[0,j-1] ):
          y[0,j-1] = y[0,j-1] - 1
          break
        j = j - 1
#
#  End search.
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
#    21 October 2022
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

  for test in range ( 0, 6 ):

    if ( test == 0 ):
      a = np.array ( [ 2, 3 ] )
      b = 18
    elif ( test == 1 ):
      a = np.array ( [ 6, 3, 13 ] )
      b = 16
    elif ( test == 2 ):
      a = np.array ( [ 12, 9, 7 ] )
      b = 60
    elif ( test == 3 ):
      a = np.array ( [ 2, 3, 5, 6 ] )
      b = 24
    elif ( test == 4 ):
      a = np.array ( [ 2, 3, 5, 6, 7 ] )
      b = 35
    elif ( test == 5 ):
      a = np.array ( [ 1, 5, 10, 25 ] )
      b = 46

    print ( '' )
    print ( '  Test ', test )
    diophantine_equation_print ( a, b )
    if ( diophantine_nd_check ( a, b ) ):
      x = diophantine_nd_nonnegative ( a, b )
      print ( '    Number of solutions = ', x.shape[0] )
      diophantine_solution_print ( a, b, x )

  return

def diophantine_nd_nonnegative_bounded ( a, b, m ):

#*****************************************************************************80
#
## diophantine_nd_nonnegative_bounded(): bounded nonnegative diophantine solutions.
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
#     We are seeking all integer solutions x such that
#       0 <= xi <= mi
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2020
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
#    integer m(n): the upper bounds for each component.
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
  x = np.empty ( [ 0, n ], dtype = int )
  j = 0
  k = 0
  r = b
  y = np.zeros ( [ 1, n ], dtype = int )
#
#  Determine the current residual for the tentative partial solution Y(0:J)
#
  while ( True ):

    r = b - sum ( a[0:j] * y[0,0:j] )
#
#  If the vector is still incomplete, get the next component.
#
    if ( j < n ):
      y[0,j] = int ( np.floor ( r / a[j] ) )
#
#  Impose the upper bound.
#
      y[0,j] = min ( y[0,j], m[j] )
      j = j + 1
#
#  If the vector is complete, analyze it.
#
    else:
#
#  Is it a solution?
#
      if ( r == 0 ):

        x = np.append ( x, y, axis = 0 )
#  
#  Now try to modify the complete vector to determine another candidate.
#  Find last nonzero Y entry, decrease by 1 and resume search.
#
      while ( 0 < j ):

        if ( 0 < y[0,j-1] ):
          y[0,j-1] = y[0,j-1] - 1
          break
        j = j - 1
#
#  End search.
#
      if ( j == 0 ):
        break

  return x

def diophantine_nd_nonnegative_bounded_test ( ):

#*****************************************************************************80
#
## diophantine_nd_nonnegative_bounded_test() tests diophantine_nd_nonnegative_bounded().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'diophantine_nd_nonnegative_bounded_test():' )
  print ( '  diophantine_nd_nonnegative_bounded() returns solutions' )
  print ( '  of a Diophantine equation in N variables which are' )
  print ( '  nonnegative, and bounded by x(i) <= m(i).' )

  a = np.array ( [ 2, 3 ] )
  b = 18
  m = np.array ( [ 10, 10 ] )
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    diophantine_bounds_print ( np.zeros ( 2 ), m )
    x = diophantine_nd_nonnegative_bounded ( a, b, m )
    diophantine_solution_print ( a, b, x )

  a = np.array ( [ 2, 3 ] )
  b = 18
  m = np.array ( [ 5, 4 ] )
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    diophantine_bounds_print ( np.zeros ( 2 ), m )
    x = diophantine_nd_nonnegative_bounded ( a, b, m )
    diophantine_solution_print ( a, b, x )

  a = np.array ( [ 2, 3 ] )
  b = 18
  m = np.array ( [ 1, 1 ] )
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    diophantine_bounds_print ( np.zeros ( 2 ), m )
    x = diophantine_nd_nonnegative_bounded ( a, b, m )
    diophantine_solution_print ( a, b, x )

  a = np.array ( [ 2, 3, 5, 6 ] )
  b = 24
  m = np.array ( [ 6, 6, 3, 3 ] )
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    diophantine_bounds_print ( np.zeros ( 4 ), m )
    x = diophantine_nd_nonnegative_bounded ( a, b, m )
    diophantine_solution_print ( a, b, x )

  a = np.array ( [ 2, 3, 5, 6, 7 ] )
  b = 35
  m = np.array ( [ 6, 2, 2, 2, 2 ] )
  print ( '' )
  if ( diophantine_nd_check ( a, b ) ):
    diophantine_equation_print ( a, b )
    diophantine_bounds_print ( np.zeros ( 5 ), m )
    x = diophantine_nd_nonnegative_bounded ( a, b, m )
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
    x = np.empty ( [ 0, n ], dtype = int )
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

def diophantine_nd_test ( ):

#*****************************************************************************80
#
## diophantine_nd_test() tests diophantine_nd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'diophantine_nd_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test diophantine_nd()' )

  diophantine_nd_nonnegative_test ( )
  diophantine_nd_nonnegative_bounded_test ( )
  diophantine_nd_positive_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'diophantine_nd_test():' )
  print ( '  Normal end of execution.' )

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
  diophantine_nd_test ( )
  timestamp ( )

