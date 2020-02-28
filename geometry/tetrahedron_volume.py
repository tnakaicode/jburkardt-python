#! /usr/bin/env python
#
def tetrahedron_volume ( tetra ):

#*****************************************************************************80
#
## TETRAHEDRON_VOLUME computes the volume of a tetrahedron.
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
#    Input, real TETRA(3,4), the vertices of the tetrahedron.
#
#    Output, real VOLUME, the volume of the tetrahedron.
#
  import numpy as np
  from r8mat_det_4d import r8mat_det_4d

  a = np.zeros ( [ 4, 4 ] )

  a[0:3,0:4] = tetra.copy ( )
  a[3,0:4] = 1.0

  value = abs ( r8mat_det_4d ( a ) ) / 6.0

  return value

def tetrahedron_volume_test ( ):

#*****************************************************************************80
#
## TETRAHEDRON_VOLUME_TEST tests TETRAHEDRON_VOLUME.
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
  import platform
  import numpy as np
  from r8mat_transpose_print import r8mat_transpose_print

  tetra = np.array ( [ \
    [  0.000000,  0.942809, -0.333333 ], \
    [ -0.816496, -0.816496, -0.333333 ], \
    [  0.816496, -0.816496, -0.333333 ], \
    [  0.000000,  0.000000,  1.000000 ] ] )

  tetra = np.transpose ( tetra )

  print ( '' )
  print ( 'TETRAHEDRON_VOLUME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TETRAHEDRON_VOLUME computes the volume of a tetrahedron' )

  r8mat_transpose_print ( 3, 4, tetra, '  Tetrahedron vertices' )

  volume = tetrahedron_volume ( tetra )

  print ( '' )
  print ( '  Volume = %g' % ( volume ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TETRAHEDRON_VOLUME_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tetrahedron_volume_test ( )
  timestamp ( )

