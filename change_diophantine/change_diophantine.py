#! /usr/bin/env python3
#
def change_diophantine_test01 ( ):

#*****************************************************************************80
#
## change_diophantine_test01() tests change_diophantine().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'change_diophantine_test01():' )
  print ( '  change_diophantine() solves a change-making problem.' )

  test_num = 7

  for test in range ( 0, test_num ):

    if ( test == 0 ):
      value = np.array ( [  5,  9, 13 ] )
      target = 19
    elif ( test == 1 ):
      value = np.array ( [  1,  4,  5,  8, 11 ] )
      target = 29
    elif ( test == 2 ):
      value = np.array ( [  1,  5, 10, 25, 50, 100 ] )
      target = 96
    elif ( test == 3 ):
      value = np.array ( [  1,  2,  6, 12, 24,  48,  60 ] )
      target = 96
    elif ( test == 4 ):
      value = np.array ( [  1,  3,  4 ] )
      target = 6
    elif ( test == 5 ):
      value = np.array ( [ 16, 17, 23, 24, 39,  40 ] )
      target = 100
    elif ( test == 6 ):
      value = np.array ( [  6,  9, 20 ] )
      target = 43

    print ( '' )
    print ( '  Test:', test )

    if ( diophantine_nd_check ( value, target ) ):

      diophantine_equation_print ( value, target )
  
      x = diophantine_nd_nonnegative ( value, target )

      x_num = x.shape[0]
      print ( '    ', x_num, ' solutions found.' )
      if ( 0 < x_num ):
        x_min = np.min ( np.sum ( x, axis = 1 ) )
        print ( '    ', x_min, ' coins in minimal solution.' )

      if ( x_num <= 50 ):
        diophantine_solution_print ( value, target, x )
      else:
        print ( '    Too many solutions to print.' )

    else:
      fprintf ( '  Test rejected.' )

  return

def change_diophantine_test ( ):

#*****************************************************************************80
#
## change_diophantine_test() tests change_diophantine().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'change_diophantine_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  change_diophantine() solves a Diophantine equation' )
  print ( '  to determine how to make a sum using a given set of coins.' )

  change_diophantine_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'change_diophantine_test():' )
  print ( '  Normal end of execution.' )

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
  change_diophantine_test ( )
  timestamp ( )


