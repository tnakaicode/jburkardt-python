#! /usr/bin/env python3
#
def diophantine_test ( ):

#*****************************************************************************80
#
## diophantine_test() tests diophantine().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'diophantine_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test diophantine().' )

  diophantine_test01 ( )
  diophantine_test02 ( )
  diophantine_test03 ( )
  diophantine_test04 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'diophantine_test():' )
  print ( '  Normal end of execution.' )

  return

def diophantine_test01 ( ):

#*****************************************************************************80
#
## diophantine_test01() tests diophantine() on a small problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'diophantine_test01():' )
  print ( '  Solve one Diophantine equation in two variables.' )

  a = np.array ( [ 91, 21 ] )
  b = 7
  diophantine_equation_print ( a, b )

  d, v, B = diophantine_basis ( a, b )

  diophantine_basis_print ( d, v, B )

  r = diophantine_residual ( a, b, v )

  print ( '' )
  print ( '  The residual for the particular solution with c=0 is', r )

  return

def diophantine_test02 ( ):

#*****************************************************************************80
#
## diophantine_test02() tests diophantine on a three-variable problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'diophantine_test02():' )
  print ( '  Solve one Diophantine equation in three variables.' )

  a = np.array ( [ 6, -14, 21 ] )
  b = 11
  diophantine_equation_print ( a, b )

  d, v, B = diophantine_basis ( a, b )

  diophantine_basis_print ( d, v, B )

  r = diophantine_residual ( a, b, v )

  print ( '' )
  print ( '  The residual for the particular solution with c=0 is', r )

  return

def diophantine_test03 ( ):

#*****************************************************************************80
#
## diophantine_test03() tests diophantine on a three-variable problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'diophantine_test03()' )
  print ( '  Solve one Diophantine equation in three variables.' )

  a = np.array ( [ 12, 9, 7 ] )
  b = 60
  diophantine_equation_print ( a, b )

  d, v, B = diophantine_basis ( a, b )

  diophantine_basis_print ( d, v, B )

  r = diophantine_residual ( a, b, v )

  print ( '' )
  print ( '  The residual for the particular solution with c=0 is', r )

  return

def diophantine_test04 ( ):

#*****************************************************************************80
#
## diophantine_test04() tests diophantine() on a three-variable problem.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np 

  print ( '' )
  print ( 'diophantine_test04():' )
  print ( '  Solve one Diophantine equation in three variables.' )

  a = np.array ( [ 6, 15, 10 ] )
  b = 60
  diophantine_equation_print ( a, b )

  d, v, B = diophantine_basis ( a, b )

  diophantine_basis_print ( d, v, B )

  r = diophantine_residual ( a, b, v )

  print ( '' )
  print ( '  The residual for the particular solution with c=0 is ', r )

  for k1 in range ( 28, 31 ):
    for k2 in range ( 40 - k1, 13 ):
      w = np.array ( [ [ k1 ], [ k2 ] ] )
      Bw = np.dot ( B, w )
      u = v + Bw[0]
      print ( '(%d,%d): %d %d + %d %d + %d %d = %d' \
        % ( k1, k2, a[0], u[0], a[1], u[1], a[2], u[2], b ) )

  return

def diophantine_basis ( a, b ):

#*****************************************************************************80
#
## diophantine_basis() finds a basis for the solution space.
#
#  Discussion:
#
#     Given the Diophantine equation 
#
#       a1 x1 + a2 x2 + ... + an xn = b
#
#     we are seeking all possible integer solutions x.
#
#     This function analyzes the coefficient vector a, and returns
#     a value d, an n vector v, and an n x n-1 matrix W so that:
#     * The value b must be divisible by d
#     * v is a solution
#     * General solutions have the form x = v + W * c
#       where c is a set of n-1 arbitrary integer coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 September 2022
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
#    integer d: a value that must be a factor of the right hand side.
#
#    integer v(n): a particular solution for c = 0.
#
#    integer W(n,n-1): the basis vectors for the general solution.
#
  import numpy as np

  if ( any ( a == 0 ) ):
    raise Exception ( 'diophantine_basis(): a has a zero entry.' )
#
#  Dimension the matrix.
#
  n = len ( a )
#
#  Form the matrix: 
#
  A = np.zeros ( [ n, n + 1 ] )
  A[:,0] = a
  for i in range ( 0, n ):
    A[i,i+1] = 1
#
#  Perform repeated row reduction.
#
  while ( 1 < np.count_nonzero ( A[:,0] ) ):
#
#  Locate row containing nonzero entry of smallest magnitude.
#
    t = np.inf
    p = -1
    for i in range ( 0, n ):
      s = np.abs ( A[i,0] )
      if ( s != 0 ):
        if ( s < t ):
          p = i
#
#  Swap row 0 and row p.
#
    T      = A[0,:].copy()
    A[0,:] = A[p,:].copy()
    A[p,:] = T.copy ( )
#
#  fix(r) rounds towards zero.
#
    for i in range ( 1, n ):
      s = np.fix ( A[i,0] / A[0,0] )
      A[i,:] = A[i,:] - s * A[0,:]

  d = A[0,0]
  f = b / d

  if ( f * d != b ):
    print ( '' )
    print ( 'diophantine_basis(): Fatal error!' )
    print ( '  b = ', b, ' is not a multiple of d = ', d )
    print ( '  There are no integer solutions to this equation.' )
    raise Exception ( 'diophantine_basis(): Fatal error!' )

  v = A[0,1:n+1] * f

  W = A[1:n,1:n+1].T

  return d, v, W

def diophantine_basis_print ( d, v, W ):

#*****************************************************************************80
#
## diophantine_basis_print() prints the Diophantine solution space basis.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer d: a value that must be a factor of the right hand side.
#
#    integer v(n): the solution for c = 0.
#
#    integer W(n,n-1): the basis vectors.
#
  print ( '' )
  print ( '  Any right hand side must be a multiple of d =', d )
  print ( '' )
  print ( '  A particular solution v:' )
  print ( v )
  print ( '' )
  print ( '  General solution x = v + W*c, where W is:' )
  print ( W )

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
#    22 September 2022
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

def diophantine_nonnegative ( a, b ):

#*****************************************************************************80
#
## diophantine_nonnegative() finds nonnegative diophantine solutions.
#
#  Discussion:
#
#     We are given a Diophantine equation 
#
#       a1 x1 + a2 x2 + ... + an xn = b
#
#     for which the coefficients a and right hand side b are nonnegative,
#     and for which at least one coefficient is strictly positive.
#
#     We are seeking all possible integer solutions x.
#
#     This function analyzes the coefficient vector a, and returns
#     a value d, an n vector v, and an n x n-1 matrix B so that:
#     * The value b must be divisible by d
#     * v is a solution
#     * General solutions have the form x = v + B * c
#       where c is a set of n-1 arbitrary integer coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 September 2022
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
#    integer d: a value that must be a factor of the right hand side.
#
#    integer v(n): the solution for c = 0.
#
#    integer B(n,n-1): the basis vectors.
#
  import numpy as np

  if ( any ( a < 0 ) ):
    raise Exception ( 'diophantine_nonnegative(): a has a negative entry.' )

  if ( not i4vec_is_integer ( a ) ):
    raise Exception ( 'diophantine_nonnegative(): some a is not an integer.' )

  if ( np.sum ( a ) <= 0 ):
    raise Exception ( 'diophantine_nonnegative(): a does not have a positive entry.' )

  if ( b < 0 ):
    raise Exception ( 'diophantine_nonnegative(): b is negative.' )

  d = i4vec_gcd ( a )
  if ( ( b % d ) != 0 ):
    raise Exception ( 'diophantine_nonnegative(): b is not divisible by gcd ( a ).' )
#
#  Dimension the matrix.
#
  n = len ( a )
#
#  Form the matrix: 
#
  A = np.zeros ( [ n, n + 1 ] )
  A[:,0] = a
  for j in range ( 0, n ):
    A[j,j+1] = 1
#
#  Perform repeated row reduction.
#
  while ( 1 < np.count_nonzero ( A[:,0] ) ):
#
#  Locate row containing nonzero entry of smallest magnitude.
#
    t = np.inf
    p = 0
    for i in range ( 0, n ):
      s = np.abs ( A[i,0] )
      if ( s != 0 ):
        if ( s < t ):
          p = i
#
#  Swap row 1 and row p.
#
    T      = A[0,:]
    A[0,:] = A[p,:]
    A[p,:] = T.copy ( )
#
#  fix(r) rounds towards zero.
#
    for i in range ( 1, n ):
      s = np.fix ( A[i,0] / A[0,0] )
      A[i,:] = A[i,:] - s * A[1,:]

  d = A[0,0]
  f = b / d

  if ( f * d != b ):
    print ( '' )
    print ( 'diophantine_nonnegative(): Fatal error!' )
    print ( '  b = ', b, ' is not a multiple of d =', d )
    print ( '  There are no integer solutions to this equation.' )
    raise Exception ( 'diophantine_nonnegative(): Fatal error!' )


  v = A[0,1:n+1] * f

  B = A[1:n,1:n+1].T

  kmin = - np.nf * np.ones ( n - 1 )
  kmax =   np.nf * np.ones ( n - 1 )

  for j in range ( 0, n - 1 ):
    for i in range ( 0, n ):
      if ( B[i,j] < 0 ):
        kmax[j] = min ( kmax[j], - v[i] / B[i,j] )
      elif ( 0 < B(i,j) ):
        kmin[j] = max ( kmin[j], - v[i] / B[i,j] )

  return d, v, B, kmin, kmax

def diophantine_residual ( a, b, x ):

#*****************************************************************************80
#
## diophantine_residual() returns the residual for a Diophantine equation.
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
#    22 September 2022
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
#    integer x(n): a proposed solution to the equation.
#
#  Output:
#
#    integer r: the solution b - a' * x.
#
  import numpy as np

  r = b - np.dot ( a, x )

  return r

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
#    22 September 2022
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
#    22 September 2022
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
#    22 September 2022
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
#    22 September 2022
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == "__main__" ):
  timestamp ( )
  diophantine_test ( )
  timestamp ( )

