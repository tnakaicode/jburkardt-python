#! /usr/bin/env python3
#
def mcnuggets_diophantine_test ( ):

#*****************************************************************************80
#
## mcnuggets_diophantine_test() tests mcnuggets_diophantine().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 November 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'mcnuggets_diophantine_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  mcnuggets_diophantine() finds the ways that you can' )
  print ( '  get exact N chicken McNuggets when they only come in packages' )
  print ( '  of 6, 9, and 20.' )

  a = np.array ( [ 6, 9, 20 ] )

  for b in range ( 0, 101 ):
    x = mcnuggets_diophantine ( a, b )
    m = x.shape[0]
    print ( '' )
    print ( '  %3d  %2d' % ( b, m ) )
    if ( 0 < m ):
      print ( x )
#
#  Terminate.
#
  print ( '' )
  print ( 'mcnuggets_diophantine_test():' )
  print ( '  Normal end of execution.' )

  return

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
#  End search.
#
      if ( j == 0 ):
        break

  return x

def mcnuggets_diophantine ( a, b ):

#*****************************************************************************80
#
## mcnuggets_diophantine() counts solutions to a McNuggets problem.
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
#     In general, a = [ 6, 9, 20 ] and b is the desired number of 
#     Chicken McNuggets.
#
#     We are seeking to count all nonnegative integer solutions x, that is,
#     the number of different ways in which a total of b Chicken McNuggets
#     can be assembled by various choices of the packages of 6, 9, and 20.
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
#  Reference:
#
#    Scott Chapman, Chris O’Neill,
#    Factoring in the Chicken McNugget Monoid,
#    Mathematics Magazine, 
#    Volume 91, Number 5, 2018, pages 323-336.
#
#  Input:
#
#    integer a(n): the number of McNuggets in each package size.
#
#    integer b: the total number of McNuggets desired.
#
#  Output:
#
#    integer x[m,n]: the different ways of getting b McNuggets.
#

#
#  Find all nonnegative integer solutions X of A*X = B.
#
  x = diophantine_nd_nonnegative ( a, b )

  return x

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

if ( __name__ == "__main__" ):
  timestamp ( )
  mcnuggets_diophantine_test ( )
  timestamp ( )

