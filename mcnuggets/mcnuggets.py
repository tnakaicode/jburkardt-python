#! /usr/bin/env python3
#
def mcnuggets_test ( ):

#*****************************************************************************80
#
## mcnuggets_test() tests mcnuggets().
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
  print ( 'mcnuggets_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test mcnuggets()' )

  mcnugget_solvable_test ( )
  mcnugget_ways_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'mcnuggets_test():' )
  print ( '  Normal end of execution.' )

  return

def mcnugget_number_values ( n_data ):

#*****************************************************************************80
#
## mcnugget_number_values() returns McNugget numbers.
#
#  Discussion:
#
#    A restaurant offers Chicken McNuggets, but only in packages of 6, 9 or 20.
#
#    A customer wishes to buy exactly N McNuggets.
#
#    Presumably, there are M distinct ways to do this.  M is known as the
#    McNugget number of N.
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
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#    Thereafter, it should simply be the value returned by the previous call.
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N: the number of McNuggets desired.
#
#    integer M: the number of different ways of getting N McNuggets.
#
  import numpy as np

  n_max = 101

  n_vec = np.array ( [ \
     0,  1,  2,  3,  4,  5,  6,  7,  8,  9, \
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19, \
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, \
    30, 31, 32, 33, 34, 35, 36, 37, 38, 39, \
    40, 41, 42, 43, 44, 45, 46, 47, 48, 49, \
    50, 51, 52, 53, 54, 55, 56, 57, 58, 59, \
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69, \
    70, 71, 72, 73, 74, 75, 76, 77, 78, 79, \
    80, 81, 82, 83, 84, 85, 86, 87, 88, 89, \
    90, 91, 92, 93, 94, 95, 96, 97, 98, 99, \
   100 \
  ] )

  m_vec = np.array ( [ \
    1,  0,  0,  0,  0,  0,  1,  0,  0,  1, \
    0,  0,  1,  0,  0,  1,  0,  0,  2,  0, \
    1,  1,  0,  0,  2,  0,  1,  2,  0,  1, \
    2,  0,  1,  2,  0,  1,  3,  0,  2,  2, \
    1,  1,  3,  0,  2,  3,  1,  2,  3,  1, \
    2,  3,  1,  2,  4,  1,  3,  3,  2,  2, \
    5,  1,  3,  4,  2,  3,  5,  2,  3,  5, \
    2,  3,  6,  2,  4,  5,  3,  3,  7,  2, \
    5,  6,  3,  4,  7,  3,  5,  7,  3,  5, \
    8,  3,  6,  7,  4,  5,  9,  3,  7,  8, \
    5 \
  ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    m = 0
  else:
    n = n_vec[n_data]
    m = m_vec[n_data]
    n_data = n_data + 1

  return n_data, n, m

def mcnugget_solvable ( a, b ):

#*****************************************************************************80
#
## mcnugget_solvable() determines whether a McNuggets problem is solvable.
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
#     We want to know whether there are nonnegative integers x which
#     satisfy this equation.  If so, we say the value b is "solvable". 
#
#     In particular, we might have a = [ 6, 9, 20 ] and b would be
#     the desired number of Chicken McNuggets.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
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
#    boolean solvable: true if there is a solution.
#
  a_num = len ( a )
  solvable = False
#
#  Check whether b is immediately solvable.
#
  if ( b == 0 ) :
    solvable = True
    return solvable

  for i in range ( 0, a_num ):
    if ( ( b % a[i] ) == 0 ):
      solvable = True
      return solvable
#
#  Initially, the set "item" contains "b".
#
  item = { b }
  item_num = 1
#
#  Loop on largest "descendant" of b.
#
  while ( 0 < item_num ):

#   n = item[-1]
    n = max ( item )
    item.remove ( n )
    item_num = item_num - 1

    for i in range ( 0, a_num ):

      n_minus_a = n - a[i]

      if ( n_minus_a == 0 ):
        solvable = True
        return solvable

      if ( 0 <= n_minus_a ):

        for j in range ( 0, a_num ):
          if ( ( n_minus_a % a[j] ) == 0 ):
            solvable = True
            return solvable
#
#  Add n_minus_a to set.  
#  Since it might already be a member, we use len() to update the set size.
#
        item.add ( n_minus_a )
        item_num = len ( item )

  return solvable

def mcnugget_solvable_test ( ):

#*****************************************************************************80
#
## mcnugget_solvable_test() tests mcnugget_solvable().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 October 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'mcnugget_solvable_test():' )
  print ( '  mcnugget_solvable() reports whether you can order exactly' )
  print ( '  N chicken McNuggets when they only come in packages' )
  print ( '  of 6, 9, and 20.' )

  print ( '' )
  print ( '    N  Solvable(N)' )
  print ( '' )

  a = [ 6, 9, 20 ]

  for b in range ( 0, 101 ):
    solvable = mcnugget_solvable ( a, b )
    if ( solvable ):
      print ( '  %3d  True' % ( b ) )
    else:
      print ( '  %3d  False' % ( b ) )

  return

def mcnugget_ways ( a, nmax ):

#*****************************************************************************80
#
## mcnugget_ways() determines the number of solutions to a McNugget problem.
#
#  Discussion:
#
#     We are given a Diophantine equation 
#
#       a1 x1 + a2 x2 + ... + an * xn = n
#
#     for which the coefficients a are positive integers, and
#     the right hand side n is a nonnegative integer.
#
#     In particular, we might have a = [ 6, 9, 20 ] and n would be
#     the desired number of Chicken McNuggets.
#
#     We want to know the number of distinct ways of ordering the
#     desired number of McNuggets.
#
#     Here, we assume that none of the values in a can be written
#     as a linear combination of the other a values.
#
#     We have to be careful so that we only count a given arrangement
#     once, that is, the order in which we combine the values does not
#     matter.  Although 6+6+9 and 6+9+6 and 6+6+9 look "different",
#     they should only count here as a single solution to the problem
#     of ordering 21 McNuggets.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2022
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
#    integer nmax: the maximum number of McNuggets desired.
#
#  Output:
#
#    integer ways(nmax+1): the number of distinct ways of ordering 0, 1, 2, ...,
#    nmax-1, nmax Chicken McNuggets.
#
  import numpy as np

  a_num = len ( a )
  a = np.sort ( a )
#
#  Count ways from 0 to nmax.
#
  ways = np.zeros ( nmax + 1 )
#
#  ways(i) = 0 + sum ( 1 <= j <= a_num ) ways(i-a(j)) if i-a(i) > 0
#
  ways[0] = 1
  for j in range ( 0, a_num ):
    for i in range ( 1, nmax + 1 ):
      pop = i - a[j]
      if ( 0 <= pop ):
        ways[i] = ways[i] + ways[pop]

  return ways

def mcnugget_ways_test ( ):

#*****************************************************************************80
#
## mcnugget_ways_test() tests mcnugget_ways().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'mcnugget_ways_test():' )
  print ( '  mcnugget_ways() reports the number of ways you can' )
  print ( '  order exactly N chicken McNuggets when they only come in' )
  print ( '  packages of 6, 9, and 20.' )

  print ( '' )
  print ( '    N  Ways(N)' )
  print ( '' )

  a = np.array ( [ 6, 9, 20 ] )
  nmax = 50
  ways = mcnugget_ways ( a, nmax )
  ways_exact = np.array ( [ \
    1,  0,  0,  0,  0,  0,  1,  0,  0,  1, \
    0,  0,  1,  0,  0,  1,  0,  0,  2,  0, \
    1,  1,  0,  0,  2,  0,  1,  2,  0,  1, \
    2,  0,  1,  2,  0,  1,  3,  0,  2,  2, \
    1,  1,  3,  0,  2,  3,  1,  2,  3,  1, \
    2,  3,  1,  2,  4,  1,  3,  3,  2,  2, \
    5,  1,  3,  4,  2,  3,  5,  2,  3,  5, \
    2,  3,  6,  2,  4,  5,  3,  3,  7,  2, \
    5,  6,  3,  4,  7,  3,  5,  7,  3,  5, \
    8,  3,  6,  7,  4,  5,  9,  3,  7,  8, \
    5 \
  ] )

  for n in range ( 0, nmax + 1 ):
    print ( '  %2d  %3d  %3d' % ( n, ways[n], ways_exact[n] ) )

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

if ( __name__ == "__main__" ):
  timestamp ( )
  mcnuggets_test ( )
  timestamp ( )

