#! /usr/bin/env python
#
def triangle01_sample ( n, seed ):

#*****************************************************************************80
#
## TRIANGLE01_SAMPLE samples the interior of the unit triangle in 2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 November 2016
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
#  Parameters:
#
#    Input, integer N, the number of points.
#
#    Input/output, integer SEED, a seed for the random
#    number generator.
#
#    Output, real XY(2,N), the points.
#
  import numpy as np
  from r8vec_uniform_01 import r8vec_uniform_01

  m = 2

  xy = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):

    e, seed = r8vec_uniform_01 ( m + 1, seed )

    e = - np.log ( e )

    d = np.sum ( e )

    xy[0:2,j] = e[0:2] / d

  return xy, seed

def triangle01_sample_test ( ):

#*****************************************************************************80
#
## TRIANGLE01_SAMPLE_TEST tests TRIANGLE01_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_transpose_print import r8mat_transpose_print

  seed = 123456789
  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  print ( '' )
  print ( 'TRIANGLE01_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE01_SAMPLE samples the unit triangle.' )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  print ( '' )
  print ( '  Sample points (X,Y):' )
  print ( '' )

  n = 10
  xy, seed = triangle01_sample ( n, seed )
  r8mat_transpose_print ( 2, n, xy, '  Sample points:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE01_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle01_sample_test ( )
  timestamp ( )
 
