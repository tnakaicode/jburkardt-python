#! /usr/bin/env python3
#
def tsp_brute ( filename ):

#*****************************************************************************80
#
## MAIN is the main program for TSP_BRUTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 November 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the file containing the distance
#    matrix information.  This is an optional input.  If it is not provided,
#    the program will prompt for it.
#
  import numpy as np
  import platform
  from path_cost import path_cost
  from perm0_next3 import perm0_next3
  from sys import exit

  timestamp ( )
  print ( '' )
  print ( 'TSP_BRUTE:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Solve small traveling salesman problems by brute force.' )
#
#  Get the distance table.
#
  print ( '' )
  print ( '  Distance matrix filename is "%s"' % ( filename ) )

  distance = np.loadtxt ( filename )
#
#  Approve the distance table.
#
  dims = distance.shape

  m = dims[0]
  n = dims[1]

  if ( m != n ):
    print ( '' )
    print ( 'TSP_BRUTE - Fatal error!' )
    print ( '  The distance matrix must be square.' )
    print ( '  Your matrix has M = %d, N = %d', m, n )
    exit ( 'TSP_BRUTE - Fatal error!' )

  v = np.diagonal ( distance )
  test = np.linalg.norm ( v )

  if ( 0.0 < test ):
    print ( '' )
    print ( 'TSP_BRUTE - Fatal error!' )
    print ( '  The distance matrix must have zero diagonal.' )
    print ( '  Your matrix has ||diag(D)|| = %g', test )
    exit ( 'TSP_BRUTE - Fatal error!' )

  test = np.linalg.norm ( distance - distance.transpose ( ) )

  if ( 0.0 < test ):
    print ( '' )
    print ( 'TSP_BRUTE - Fatal error!' )
    print ( '  The distance matrix must be symmetric.' )
    print ( '  Your matrix has ||D-D''|| = %g' % ( test ) )
    exit ( 'TSP_BRUTE - Fatal error!' )
#
#  Print the distance matrix.
#
  print ( '' )
  print ( '  The city-to-city distance matrix:' )
  print ( '' )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      print ( '  %4g' % ( distance[i,j] ), end = '' )
    print ( '' )
#
#  Examine every permutation.
#
  total_max = - np.inf
  total_min = np.inf
  total_ave = 0.0

  p = np.zeros ( n, dtype = np.int32 )
  more = False
  rank = 0

  p_min = np.zeros ( n, dtype = np.int32 )

  paths = 0

  while ( True ):

    p, more, rank = perm0_next3 ( n, p, more, rank )

    if ( not more ):
      break

    paths = paths + 1

    total = path_cost ( n, distance, p )

    total_ave = total_ave + total

    if ( total_max < total ):
      total_max = total

    if ( total < total_min ):
      total_min = total
      p_min = p.copy ( )

  total_ave = total_ave / paths
#
#  Report.
#
  print ( '' )
  print ( '  A minimal length itinerary:' )
  print ( '' )
  print ( '  Step  From  To        Distance' )
  print ( '' )
  for i1 in range ( 0, n ):
    i2 = ( ( i1 + 1 ) % n )
    print ( '  %4d    %2d  %2d  %14.6g' \
      % ( i2, p_min[i1], p_min[i2], distance[p_min[i1],p_min[i2]] ) )

  print ( '  ----    --  --  --------------' )
  print ( '  Total:          %14.6g' % ( total_min ) )

  print ( '' )
  print ( '  Number of paths checked = %d' % ( paths ) )
  print ( '' )
  print ( '  Minimum length = %g' % ( total_min ) )
  print ( '  Average length = %g' % ( total_ave ) )
  print ( '  Maximum length = %g' % ( total_max ) )

  return
#
#  Terminate.
#
  print ( '' )
  print ( 'TSP_BRUTE' )
  print ( '  Normal end of execution.' )
  return

def tsp_brute_test ( ):

#*****************************************************************************80
#
## TSP_BRUTE_TEST tests TSP_BRUTE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 November 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'TSP_BRUTE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TSP_BRUTE solves a small traveling salesman problem.' )

  filename = 'five.txt'

  print ( '' )
  print ( '  Call tsp_brute ( %s )' % ( filename ) )
  tsp_brute ( filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'TSP_BRUTE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tsp_brute_test ( )
  timestamp ( )


