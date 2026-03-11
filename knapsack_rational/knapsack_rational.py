#! /usr/bin/env python3
#
def knapsack_rational_test ( ):

#*****************************************************************************80
#
## knapsack_rational_test() tests knapsack_rational().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 November 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'knapsack_rational_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test knapsack_rational().' )

  n = 5
  v = np.array ( [ 24, 13, 23, 15, 16 ] )
  w = np.array ( [ 12,  7, 11,  8,  9 ] )
  d = v / w
  k = 26

  print ( '' )
  print ( 'knapsack_rational_tester():' )
  print ( '  knapsack_rational() solves the rational knapsack problem.' )

  print ( '' )
  print ( '  Object  Value  Weight  Density' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %7d  %7d  %7.3f' % ( i, v[i], w[i], d[i] ) )

  index = np.argsort ( d )
  index = np.flip ( index )
  print ( '  Sort by density in descending order' )

  v = v[index]
  w = w[index]
  d = d[index]

  print ( '' )
  print ( '  After reordering by Density:' )
  print ( '' )
  print ( '  Object  Value  Weight  Density' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %7d  %7d  %7.3f' % ( i, v[i], w[i], d[i] ) )

  print ( '' )
  print ( '  Weight limit is ', k )

  s, vmax, wmax = knapsack_rational ( n, v, w, k  )

  print ( '' )
  print ( '  Object  Choice  Value  Weight  Density' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %7.3f  %7d  %7d  %7.3f' \
      % ( i, s[i], s[i] * v[i], s[i] * w[i], v[i] / w[i] ) )

  print ( '' )
  print ( '  Total:%7.3f  %7d  %7d  %7.3f' % ( np.sum(s), vmax, wmax, vmax / wmax ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'knapsack_rational_test():' )
  print ( '  Normal end of execution.' )
  return

def knapsack_rational ( n, v, w, k ):

#*****************************************************************************80
#
## knapsack_rational() solves the rational knapsack problem.
#
#  Discussion:
#
#    The rational knapsack problem is a generalization of the 0/1 knapsack
#    problem.  It is mainly used to derive a bounding function for the
#    0/1 knapsack problem.
#
#    The 0/1 knapsack problem is as follows:
#
#      Given:
#        a set of N objects,
#        a profit P(I) and weight W(I) associated with each object,
#        and a weight limit MASS_LIMIT,
#      Determine:
#        a set of choices X(I) which are 0 or 1, that maximizes the profit
#          P = Sum ( 1 <= I <= N ) P(I) * X(I)
#        subject to the constraint
#          Sum ( 1 <= I <= N ) W(I) * X(I) <= MASS_LIMIT.
#
#    By contrast, the rational knapsack problem allows the values X(I)
#    to be any value between 0 and 1.  A solution for the rational knapsack
#    problem is known.  Arrange the objects in order of their "profit density"
#    ratios P(I)/W(I), and then take in order as many of these as you can.
#    If you still have "room" in the weight constraint, then you should
#    take the maximal fraction of the very next object, which will complete
#    your weight limit, and maximize your profit.
#
#    If should be obvious that, given the same data, a solution for
#    the rational knapsack problem will always have a profit that is
#    at least as high as for the 0/1 problem.  Since the rational knapsack
#    maximum profit is easily computed, this makes it a useful bounding
#    function.
#
#    Note that this routine assumes that the objects have already been
#    arranged in order of the "profit density".
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Kreher, Douglas Simpson,
#    Combinatorial Algorithms,
#    CRC Press, 1998,
#    ISBN: 0-8493-3988-X,
#    LC: QA164.K73.
#
#  Input:
#
#    integer N, the number of objects.
#
#    real P(N), the "profit" or value of each object.
#    The entries of P are assumed to be nonnegative.
#
#    real W(N), the "weight" or cost of each object.
#    The entries of W are assumed to be nonnegative.
#
#    real K, the weight limit of the chosen objects.
#
#  Output:
#
#    real X(N), the choice function for the objects.
#    0.0, the object was not taken.
#    1.0, the object was taken.
#    R, where 0 < R < 1, a fractional amount of the object was taken.
#
#    real MASS, the total mass of the objects taken.
#
#    real PROFIT, the total profit of the objects taken.
#
  import numpy as np

  s = np.zeros ( n, dtype = float )
  vmax = 0
  wmax = 0

  for i in range ( 0, n ):

    if ( k <= wmax ):
      s[i] = 0
    elif ( wmax + w[i] <= k ):
      s[i] = 1
      wmax = wmax + w[i]
      vmax = vmax + v[i]
    else:
      s[i] = ( k - wmax ) / w[i]
      wmax = k
      vmax = vmax + s[i] * v[i]

  return s, vmax, wmax

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

if ( __name__ == '__main__' ):
  timestamp ( )
  knapsack_rational_test ( )
  timestamp ( )

