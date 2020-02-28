#! /usr/bin/env python
#
def tetrahedron_centroid ( tetra ):

#*****************************************************************************80
#
## TETRAHEDRON_CENTROID computes the centroid of a tetrahedron in 3D.
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
#    Input, real TETRA(3,4) the tetrahedron vertices.
#
#    Output, real CENTROID(3), the coordinates of the centroid.
#
  import numpy as np

  centroid = np.sum ( tetra, 1 ) / 4.0

  return centroid

def tetrahedron_centroid_test ( ):

#*****************************************************************************80
#
## TETRAHEDRON_CENTROID_TEST tests TETRAHEDRON_CENTROID.
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
  import platform
  from r8mat_transpose_print import r8mat_transpose_print
  from r8vec_transpose_print import r8vec_transpose_print

  tetra = np.array ( [ \
    [  0.000000,  0.942809, -0.333333 ], \
    [ -0.816496, -0.816496, -0.333333 ], \
    [  0.816496, -0.816496, -0.333333 ], \
    [  0.000000,  0.000000,  1.000000 ] ] )

  tetra = np.transpose ( tetra )

  print ( '' )
  print ( 'TETRAHEDRON_CENTROID_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TETRAHEDRON_CENTROID computes the centroid of a tetrahedron' )

  r8mat_transpose_print ( 3, 4, tetra, '  Tetrahedron vertices:' )

  centroid = tetrahedron_centroid ( tetra )

  r8vec_transpose_print ( 3, centroid, '  Centroid:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TETRAHEDRON_CENTROID_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tetrahedron_centroid_test ( )
  timestamp ( )
