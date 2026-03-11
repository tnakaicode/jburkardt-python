#! /usr/bin/env python3
#
def test_nearest_test ( ):

#*****************************************************************************80
#
## test_nearest_test() tests test_nearest().
#
#  Discussion:
#
#    We are given R, a set of NR points in M dimensions.
#
#    We are given S, a set of NS points in M dimensions.
#
#    For each S(I) in S, we seek the index J of the point R(J)
#    which is nearest to S(I) over all points in R.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Local:
#
#    integer M, the spatial dimension.
#
#    integer NR, the number of data points.
#
#    integer NS, the number of sample points.
#
#    real R(M,NR), the data points.
#
#    real S(M,NS), the sample points. 
#
  from numpy.random import default_rng
  from time import perf_counter
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'test_nearest():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Consider various nearest neighbor algorithms.' )

  m_test_num = 3
  n_test_num = 6
  code_num = 1

  m_test_data = [ 2, 4, 8 ]
  nr_test_data = [ 1000000, 100000, 10000,  1000,    100,      10 ]
  ns_test_data = [ 10,    100,  1000, 10000, 100000, 1000000 ]

  for code in range ( 1, 2 ):

    if ( code == 1 ):
      print ( '' )
      print ( '  Testing find_closest1()' )
      print ( '  ----M---  ---NR---  ---NS---    Time' )

    for m in m_test_data:

      print ( '' )

      for test in range ( 0, n_test_num ):

        nr = nr_test_data[test]
        r = rng.random ( [ m, nr ] )
        ns = ns_test_data[test]
        s = rng.random ( [ m, ns ] )

        t = perf_counter ( )
        if ( code == 1 ):
          nearest = find_closest1 ( m, nr, r, ns, s )
        t = perf_counter ( ) - t
        print ( '  %8d  %8d  %8d  %14.6g' % ( m, nr, ns, t ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'test_nearest_test():' )
  print ( '  Normal end of execution.' )

  return

def find_closest1 ( m, nr, r, ns, s ):

#*****************************************************************************80
#
## find_closest1() finds the nearest R point to each S point.
#
#  Discussion:
#
#    We are given R, a set of NR points in M dimensions.
#
#    We are given S, a set of NS points in M dimensions.
#
#    For each S(I) in S, we seek the index J of the point R(J)
#    which is nearest to S(I) over all points in R.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 March 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the spatial dimension.
#
#    integer NR, the number of data points.
#
#    real R(M,NR), the data points.
#
#    integer NS, the number of sample points.
#
#    real S(M,NS), the sample points.
#
#  Output:
#
#    integer NEAREST(NS), the index of the nearest data point.
#
  import numpy as np

  nearest = - np.ones ( ns, dtype = int )

  for js in range ( 0, ns ):

    dist_min = np.inf

    for jr in range ( 0, nr ):

      dist = np.linalg.norm ( r[:,jr] - s[:,js] )

      if ( dist < dist_min ):
        dist_min = dist
        nearest[js] = jr

  return nearest

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
  test_nearest_test ( )
  timestamp ( )

