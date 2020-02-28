#! /usr/bin/env python
#
def knapsack_01 ( n, mass_limit, p, w ):

#*****************************************************************************80
#
## KNAPSACK_01 solves the 0/1 knapsack problem.
#
#  Discussion:
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
#    This routine assumes that the objects have already been sorted
#    in order of decreasing "profit density", P(I)/W(I).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2016
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
#  Parameters:
#
#    Input, integer N, the number of objects.
#
#    Input, real MASS_LIMIT, the weight limit of the
#    chosen objects.
#
#    Input, real P(N), the "profit" or value of each object.
#    P is assumed to be nonnegative.
#
#    Input, real W(N), the "weight" or cost of each object.
#    W is assumed to be  nonnegative.
#
#    Output, real X(N), the choice function for the objects.
#    0, the object was not taken.
#    1, the object was taken.
#
#    Output, real MASS, the total mass of the objects taken.
#
#    Output, real PROFIT, the total profit of the objects taken.
#
  import numpy as np
  from knapsack_rational import knapsack_rational
  from r8vec_backtrack import r8vec_backtrack
  from sys import exit
#
#  Initialize the "best so far" data.
#
  x_best = np.zeros ( n )
  profit_best = 0.0
  mass_best = 0
#
#  Begin the backtracking solution.
#
  maxstack = 100
  stacks = np.zeros ( maxstack )
  x = np.zeros ( n )
  indx = 0
  k = 1
  nstack = 0
  ncan = np.zeros ( n )

  while ( True ):

    x, indx, k, nstack, stacks, ncan = r8vec_backtrack ( n, maxstack, x, indx, k, \
      nstack, stacks, ncan )
#
#  Got a new candidate.  Compare it to the best so far.
#
    if ( indx == 1 ):

      profit = np.dot ( p, x )
      mass = np.dot ( w, x )

      if ( profit_best < profit or \
         ( profit == profit_best and mass < mass_best ) ):
        profit_best = profit
        mass_best = mass
        for i in range ( 0, n ):
          x_best[i] = x[i]
#
#  Need candidates for X(K).
#
#  X(K) = 1 is possible if:
#
#    * adding W(K) to our mass doesn't put us over our mass limit
#    * and adding P(K) to our current profit, and taking the best we
#      could get using rational X for the remainder would put us over
#      our current best.
#
#  X(K) = 0 is always possible.
#
    elif ( indx == 2 ):

      ncan[k-1] = 0

      mass_1 = w[k-1]
      for i in range ( 0, k - 1 ):
        mass_1 = mass_1 + w[i] * x[i]

      if ( mass_1 <= mass_limit ):

        mass_remaining = mass_limit - mass_1

        profit_1 = p[k-1]
        for i in range ( 0, k - 1 ):
          profit_1 = profit_1 + p[i] * x[i]

        if ( k < n ):

          ptemp = np.zeros ( n - k )
          for i in range ( k, n ):
            ptemp[i-k] = p[i]
          wtemp = np.zeros ( n - k )
          for i in range ( k, n ):
            wtemp[i-k] = w[i]

          xtemp, mass_2, profit_2 = knapsack_rational ( n - k, \
            mass_remaining, ptemp, wtemp )

          for i in range ( k, n ):
            x[i] = xtemp[i-k]

        else:

          profit_2 = 0.0

        if ( profit_best < profit_1 + profit_2 ):

          if ( maxstack <= nstack ):
            print ( '' )
            print ( 'KNAPSACK_01 - Fatal error!' )
            print ( '  Exceeded stack space.' )
            exit ( 'KNAPSACK_01 - Fatal error!' )
 
          ncan[k-1] = ncan[k-1] + 1
          nstack = nstack + 1
          stacks[nstack-1] = 1.0

      if ( maxstack <= nstack ):
        print ( '' )
        print ( 'KNAPSACK_01 - Fatal error!' )
        print ( '  Exceeded stack space.' )
        exit ( 'KNAPSACK_01 - Fatal error!' )

      ncan[k-1] = ncan[k-1] + 1
      nstack = nstack + 1
      stacks[nstack-1] = 0.0
#
#  Done.  Return the best solution.
#
    else:

      profit = profit_best
      mass = mass_best
      for i in range ( 0, n ):
        x[i] = x_best[i]
      break

  return x, mass, profit

def knapsack_01_test ( ):

#*****************************************************************************80
#
## KNAPSACK_01_TEST tests KNAPSACK_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from knapsack_reorder import knapsack_reorder

  n = 5
  mass_limit = 26.0
  p = np.array ( [ 24.0, 13.0, 23.0, 15.0, 16.0 ] )
  w = np.array ( [ 12.0,  7.0, 11.0,  8.0,  9.0 ] )

  print ( '' )
  print ( 'KNAPSACK_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KNAPSACK_01 solves the 0/1 knapsack problem.' )

  print ( '' )
  print ( '  Object, Profit, Mass, "Profit Density"' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %7.3f  %7.3f  %7.3f' % ( i, p[i], w[i], p[i] / w[i] ) )

  p, w = knapsack_reorder ( n, p, w )

  print ( '' )
  print ( '  After reordering by Profit Density:' )
  print ( '' )
  print ( '  Object, Profit, Mass, "Profit Density"' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %7.3f  %7.3f  %7.3f' % ( i, p[i], w[i], p[i] / w[i] ) )

  print ( '' )
  print ( '  Total mass restriction is %f' % ( mass_limit ) )

  x, mass, profit = knapsack_01 ( n, mass_limit, p, w )

  print ( '' )
  print ( '  Object, Density, Choice, Profit, Mass' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %7.3f  %7.3f  %7.3f  %7.3f' \
      % ( i, p[i] / w[i], x[i],  x[i] * p[i], x[i] * w[i] ) )

  print ( '' )
  print ( '  Total:                  %7.3f  %7.3f' % ( profit, mass ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'KNAPSACK_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  knapsack_01_test ( )
  timestamp ( )
 
