#! /usr/bin/env python
#
def uniform_nsphere_sample ( n, seed ):

#*****************************************************************************80
#
## UNIFORM_NSPHERE_SAMPLE samples the Uniform Unit Sphere PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jerry Banks, editor,
#    Handbook of Simulation,
#    Engineering and Management Press Books, 1998, page 168.
#
#  Parameters:
#
#    Input, integer N, the dimension of the sphere.
#
#    Input, integer ISEED, a seed for the random number generator.
#
#    Output, real X(N), a point on the unit N sphere, chosen
#    with a uniform probability.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from normal_01 import normal_01_sample
  from r8vec_norm import r8vec_norm

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i], seed = normal_01_sample ( seed )

  norm = r8vec_norm ( n, x )

  for i in range ( 0, n ):
    x[i] = x[i] / norm

  return x, seed

def uniform_nsphere_sample_test ( ):

#*****************************************************************************80
#
## UNIFORM_NSPHERE_SAMPLE_TEST tests UNIFORM_NSPHERE_SAMPLE
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_transpose_print import r8vec_transpose_print

  n = 3
  seed = 123456789

  print ( '' )
  print ( 'UNIFORM_NSPHERE_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNIFORM_NSPHERE_SAMPLE samples the Uniform Nsphere distribution.' )

  print ( '' )
  print ( '  Dimension N of sphere =       %6d' % ( n ) )
  print ( '' )
  print ( '  Points on the sphere:' )
  print ( '' )

  for i in range ( 0, 10 ):
    x, seed = uniform_nsphere_sample ( n, seed )
    r8vec_transpose_print ( n, x, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNIFORM_NSPHERE_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  uniform_nsphere_sample_test ( )
  timestamp ( )
 
