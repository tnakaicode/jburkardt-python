#! /usr/bin/env python
#
def triangle_sample ( t, n, seed ):

#*****************************************************************************80
#
## TRIANGLE_SAMPLE returns random points in a triangle.
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
#  Parameters:
#
#    Input, real T(2,3), the triangle vertices.
#
#    Input, integer N, the number of points to generate.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real P(2,N), random points in the triangle.
#
#    Output, integer SEED, a seed for the random number generator.
#
  import numpy as np
  from r8vec_uniform_01 import r8vec_uniform_01

  alpha, seed = r8vec_uniform_01 ( n, seed )
#
#  Interpret R as a percentage of the triangle's area.
#
#  Imagine a line L, parallel to side 1, so that the area between
#  vertex 1 and line L is R percent of the full triangle's area.
#
#  The line L will intersect sides 2 and 3 at a fraction
#  ALPHA = SQRT ( R ) of the distance from vertex 1 to vertices 2 and 3.
#
  for i in range ( 0, n ):
    alpha[i] = np.sqrt ( alpha[i] )
#
#  Determine the coordinates of the points on sides 2 and 3 intersected
#  by line L.
#
  p12 = np.zeros ( [ 2, n ] )
  p13 = np.zeros ( [ 2, n ] )

  for i in range ( 0, 2 ):
    for j in range ( 0, n ):
      p12[i,j] = ( 1.0 - alpha[j] ) * t[i,0] \
                       + alpha[j]   * t[i,1]

      p13[i,j] = ( 1.0 - alpha[j] ) * t[i,0] \
                       + alpha[j]   * t[i,2]
#
#  Now choose, uniformly at random, a point on the line L.
#
  alpha, seed = r8vec_uniform_01 ( n, seed )

  p = np.zeros ( [ 2, n ] )

  for i in range ( 0, 2 ):
    for j in range ( 0, n ):
      p[i,j] = ( 1.0 - alpha[j] ) * p12[i,j] \
                     + alpha[j]   * p13[i,j]

  return p, seed

def triangle_sample_test ( ):

#*****************************************************************************80
#
## TRIANGLE_SAMPLE_TEST tests TRIANGLE_SAMPLE.
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
  from triangle_xy_to_xsi import triangle_xy_to_xsi

  seed = 123456789
  t = np.array ( [ \
    [ 4.0, 1.0, -2.0 ], \
    [ 2.0, 5.0,  2.0 ] ] )

  print ( '' )
  print ( 'TRIANGLE_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_SAMPLE samples a triangle.' )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  print ( '' )
  print ( '  Sample points (X,Y) and (XSI1,XSI2,XSI3) coordinates:' )
  print ( '' )

  for i in range ( 0, 10 ):

    p, seed = triangle_sample ( t, 1, seed )

    xsi = triangle_xy_to_xsi ( t, p )

    print ( '  %10g  %10g    %10g  %10g  %10g' % ( p[0], p[1], xsi[0], xsi[1], xsi[2] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_sample_test ( )
  timestamp ( )
 
