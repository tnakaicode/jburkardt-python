#! /usr/bin/env python
#
def knapsack_reorder ( n, p, w ):

#*****************************************************************************80
#
## KNAPSACK_REORDER reorders the knapsack data by "profit density".
#
#  Discussion:
#
#    This routine must be called to rearrange the data before calling
#    routines that handle a knapsack problem.
#
#    The "profit density" for object I is defined as P(I)/W(I).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the number of objects.
#
#    Input/output, real P(N), the "profit" or value of each object.
#
#    Input/output, real W(N), the "weight" or cost of each object.
#

#
#  Rearrange the objects in order of "profit density".
#
  for i in range ( 0, n ):
    for j in range ( i + 1, n ):

      if ( p[i] * w[j] < p[j] * w[i] ):

        t    = p[i]
        p[i] = p[j]
        p[j] = t

        t    = w[i]
        w[i] = w[j]
        w[j] = t

  return p, w

def knapsack_reorder_test ( ):

#*****************************************************************************80
#
## KNAPSACK_REORDER_TEST tests KNAPSACK_REORDER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  p = np.array ( [ 24.0, 13.0, 23.0, 15.0, 16.0 ] )
  w = np.array ( [ 12.0,  7.0, 11.0,  8.0,  9.0 ] )

  print ( '' )
  print ( 'KNAPSACK_REORDER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KNAPSACK_REORDER reorders knapsack data.' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'KNAPSACK_REORDER_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  knapsack_reorder_test ( )
  timestamp ( )
 
