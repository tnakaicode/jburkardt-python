#! /usr/bin/env python
#
def tetrahedron_sample ( t, n, seed ):

#*****************************************************************************80
#
## TETRAHEDRON_SAMPLE returns random points in a tetrahedron.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T(3,4), the tetrahedron vertices.
#
#    Input, integer N, the number of points to generate.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real P(3,N), random points in the tetrahedron.
#
#    Output, integer SEED, a seed for the random number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  p = np.zeros ( [ 3, n ] )

  for j in range ( 0, n ):

    r, seed = r8_uniform_01 ( seed )
#
#  Interpret R as a percentage of the tetrahedron's volume.
#
#  Imagine a plane, parallel to face 1, so that the volume between
#  vertex 1 and the plane is R percent of the full tetrahedron volume.
#
#  The plane will intersect sides 12, 13, and 14 at a fraction
#  ALPHA = R^1/3 of the distance from vertex 1 to vertices 2, 3, and 4.
#
    alpha = r ** ( 1.0 / 3.0 )
#
#  Determine the coordinates of the points on sides 12, 13 and 14 intersected
#  by the plane, which form a triangle TR.
#
    tr = np.zeros ( [ 3, 3 ] )

    tr[:,0] = alpha * t[:,0] + ( 1.0 - alpha ) * t[:,1]
    tr[:,1] = alpha * t[:,0] + ( 1.0 - alpha ) * t[:,2]
    tr[:,2] = alpha * t[:,0] + ( 1.0 - alpha ) * t[:,3]
#
#  Now choose, uniformly at random, a point in this triangle.
#
    r, seed = r8_uniform_01 ( seed )
#
#  Interpret R as a percentage of the triangle's area.
#
#  Imagine a line L, parallel to side 1, so that the area between
#  vertex 1 and line L is R percent of the full triangle's area.
#
#  The line L will intersect sides 2 and 3 at a fraction
#  ALPHA = SQRT ( R ) of the distance from vertex 1 to vertices 2 and 3.
#
    alpha = np.sqrt ( r )
#
#  Determine the coordinates of the points on sides 2 and 3 intersected
#  by line L.
#
    p12 = alpha * tr[:,0] + ( 1.0 - alpha ) * tr[:,1]
    p13 = alpha * tr[:,0] + ( 1.0 - alpha ) * tr[:,2]
#
#  Now choose, uniformly at random, a point on the line L.
#
    beta, seed = r8_uniform_01 ( seed )

    p[:,j] = beta * p12[:] + ( 1.0 - beta ) * p13[:]

  return p, seed

def tetrahedron_sample_test ( ):

#*****************************************************************************80
#
## TETRAHEDRON_SAMPLE_TEST tests TETRAHEDRON_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_transpose_print import r8mat_transpose_print
  from tetrahedron_barycentric import tetrahedron_barycentric

  seed = 123456789

  t = np.array ( [ \
     [ 1.0, 4.0, 3.0 ], \
     [ 2.0, 4.0, 3.0 ], \
     [ 1.0, 6.0, 3.0 ], \
     [ 1.0, 4.0, 4.0 ] ] )

  t = np.transpose ( t )

  print ( '' )
  print ( 'TETRAHEDRON_SAMPLE_TEST' )
  print ( '  TETRAHEDRON_SAMPLE samples a tetrahedron.' )
  print ( '  We are computing the XSI coordinates just to verify' )
  print ( '  that the points are inside the tetrahedron.' )

  r8mat_transpose_print ( 3, 4, t, '  Tetrahedron vertices' )

  print ( '' )
  print ( '  (X,Y,Z)   (XSI1,XSI2,XSI3,XSI4):' )
  print ( '' )

  for i in range ( 0, 10 ):
    p, seed = tetrahedron_sample ( t, 1, seed )
    xsi = tetrahedron_barycentric ( t, p )
    print ( '  %8f  %8f  %8f    %8f  %8f  %8f  %8f' \
      % ( p[0], p[1], p[2], xsi[0], xsi[1], xsi[2], xsi[3] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TETRAHEDRON_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tetrahedron_sample_test ( )
  timestamp ( )


