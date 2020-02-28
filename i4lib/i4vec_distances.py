#! /usr/bin/env python
#
def i4vec_distances ( k, locate ):

#*****************************************************************************80
#
## I4VEC_DISTANCES computes a pairwise distance table.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer K, the number of objects.
#
#    Input, integer LOCATE(K), the obect locations.
#
#    Output, integer D(K*(K-1)/2), the pairwise distances.
#
  import numpy as np

  d = np.zeros ( k * ( k - 1 ) / 2 )

  l = 0
  for i in range ( 0, k ):
    for j in range ( i + 1, k ):
      d[l] = abs ( locate[i] - locate[j] )
      l = l + 1

  return d

def i4vec_distances_test ( ):

#*****************************************************************************80
#
## I4VEC_DISTANCES_TEST tests I4VEC_DISTANCES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 January 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_print import i4vec_print

  print ( '' )
  print ( 'I4VEC_DISTANCES_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_DISTANCES computes the pairwise distances between elements' )
  print ( '  of an I4VEC.' )

  n = 5
  locate = np.array ( [ 0, 3, 10, 20, 100 ] )
  d = i4vec_distances ( n, locate )

  i4vec_print ( n, locate, '  Locations:' )
  i4vec_print ( n * ( n - 1 ) / 2, d, '  Distances:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_DISTANCES_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_distances_test ( )
  timestamp ( )
