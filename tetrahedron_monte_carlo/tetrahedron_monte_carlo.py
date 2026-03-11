#! /usr/bin/env python3
#
def tetrahedron_monte_carlo_tests ( ):

#*****************************************************************************80
#
## tetrahedron_monte_carlo_tests() tests tetrahedron_monte_carlo().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 April 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'tetrahedron_monte_carlo_tests():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test tetrahedron_monte_carlo().' )
#
#  Sample the unit tetrahedron.
#
  tetrahedron_monte_carlo_test01 ( );
#
#  Sample a general tetrahedron.
#
  tetrahedron_monte_carlo_test02 ( );
#
#  Terminate.
#
  print ( '' )
  print ( 'tetrahedron_monte_carlo_tests():' )
  print ( '  Normal end of execution.' )
  return

def tetrahedron_monte_carlo_test01 ( ):

#*****************************************************************************80
#
## tetrahedron_monte_carlo_test01() samples the unit tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t = np.array ( [ \
    [ 1.0, 0.0, 0.0 ], \
    [ 0.0, 1.0, 0.0 ], \
    [ 0.0, 0.0, 1.0 ], \
    [ 0.0, 0.0, 0.0 ] ] )

  print ( '' )
  print ( 'tetrahedron_monte_carlo_test01():' )
  print ( '  Integrate tetrahedron_integrand_03()' )
  print ( '  Integration region is the unit tetrahedron.' )
  print ( '  Use an increasing number of points P_NUM.' )

  print ( '' )
  print ( '     P_NUM      1/(x**2+y**2+1)' )
  print ( '' )

  p_num = 1

  while ( p_num <= 65536 ):

    result = tetrahedron_monte_carlo ( t, p_num, lambda x, y:1/(x**2+y**2+1) )

    print ( '  %8d  %14f' % ( p_num, result ) )

    p_num = 2 * p_num

  return

def tetrahedron_monte_carlo_test02 ( ):

#*****************************************************************************80
#
## tetrahedron_monte_carlo_test02() samples a general tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  t = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 4.0, 1.0, 2.0 ], \
    [ 2.0, 4.0, 4.0 ], \
    [ 3.0, 2.0, 5.0 ] ] )

  print ( '' )
  print ( 'tetrahedron_monte_carlo_test02():' )
  print ( '  Integrate tetrahedron_unit_integrand_user()' )
  print ( '  Integration region is over a general tetrahedron.' )
  print ( '  Use an increasing number of points P_NUM.' )
  print ( '' )
  print ( '  Tetrahedron vertices:' )
  print ( t )
  print ( '' )
  print ( '     P_NUM' )
  print ( '' )

  p_num = 1

  while ( p_num <= 65536 ):

    result = tetrahedron_monte_carlo ( t, p_num, lambda x, y:1/(x**2+y**2+1) )

    print ( '  %8d  %12f' % ( p_num, result ) )

    p_num = 2 * p_num

  return

def tetrahedron_reference_to_physical ( t, n, ref ):

#*****************************************************************************80
#
## tetrahedron_reference_to_physical() maps reference points to physical points.
#
#  Discussion:
#
#    Given the vertices of an order 4 physical tetrahedron and a point 
#    (R,S,T) in the reference tetrahedron, the routine computes the value 
#    of the corresponding image point (X,Y,Z) in physical space.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 April 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(4,3), the coordinates of the vertices.  
#    The vertices are assumed to be the images of (1,0,0), (0,1,0),
#    (0,0,1) and (0,0,0) respectively.
#
#    integer N, the number of points to transform.
#
#    real REF(N,3), points in the reference element.
#
#  Output:
#
#    real PHY(N,3), corresponding points in the physical element.
#
  import numpy as np

  phy = np.zeros ( [ n, 3 ] )

  for i in range ( 0, 3 ):
    phy[:,i] =                                            \
        t[0,i] *         ref[:,0]                         \
      + t[1,i] *                    ref[:,1]              \
      + t[2,i] *                               ref[:,2]   \
      + t[3,i] * ( 1.0 - ref[:,0] - ref[:,1] - ref[:,2] );

  return phy

def tetrahedron_monte_carlo ( t, p_num, integrand ):

#*****************************************************************************80
#
## tetrahedron_monte_carlo() applies the Monte Carlo rule to integrate a function.
#
#  Discussion:
#
#    The function f(x,y,z) is to be integrated over a tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 August 2009
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real T(4,3), the vertices.
#
#    integer P_NUM, the number of sample points.
#
#    external INTEGRAND, the integrand routine.
#
#  Output:
#
#    real RESULT, the approximate integral.
#
  import numpy as np

  volume = tetrahedron_volume ( t )

  p = tetrahedron01_sample ( p_num )

  p2 = tetrahedron_reference_to_physical ( t, p_num, p )

  fp2 = integrand ( p2[:,0], p2[:,1] )
  
  result = volume * np.sum ( fp2 ) / p_num;

  return result

def tetrahedron_volume ( tetra ):

#*****************************************************************************80
#
## tetrahedron_volume() computes the volume of a tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real tetra(4,3): the vertices of the tetrahedron.
#
#  Output:
#
#    real volume: the volume of the tetrahedron.
#
  import numpy as np

  a = np.zeros ( [ 4, 4 ] )
  a[0:4,0:3] = tetra[0:4,0:3]
  a[0:4,3] = 1.0

  volume = np.abs ( np.linalg.det ( a ) ) / 6.0

  return volume

def tetrahedron01_sample ( n ):

#*****************************************************************************80
#
## tetrahedron01_sample() samples the unit tetrahedron in 3D.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Reuven Rubinstein,
#    Monte Carlo Optimization, Simulation, and Sensitivity
#    of Queueing Networks,
#    Krieger, 1992,
#    ISBN: 0894647644,
#    LC: QA298.R79.
#
#  Input:
#
#    integer n: the number of points.
#
#  Output:
#
#    real x(n,3): the points.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  x = np.zeros ( [ n, 3 ] )
  el = np.zeros ( 4 )

  for i in range ( 0, n ):

    e = rng.random ( size = 4 )

    el_sum = 0.0
    for j in range ( 0, 4 ):
      el[j] = - np.log ( e[j] )
      el_sum = el_sum + el[j]

    for j in range ( 0, 3 ):
      x[i,j] = el[j] / el_sum

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
  tetrahedron_monte_carlo_tests ( )
  timestamp ( )

