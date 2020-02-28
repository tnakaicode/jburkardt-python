#! /usr/bin/env python
#
def triangle_edge_length ( t ):

#*****************************************************************************80
#
## TRIANGLE_EDGE_LENGTH returns edge lengths of a triangle in 2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T(2,3), the triangle vertices.
#
#    Output, real EDGE_LENGTH(3), the length of the edges.
#
  import numpy as np
  from i4_wrap import i4_wrap

  edge_length = np.zeros ( 3 )

  for j1 in range ( 0, 3 ):
    j2 = i4_wrap ( j1 + 1, 0, 2 )

    edge_length[j1] = np.sqrt ( ( t[0,j2] - t[0,j1] ) ** 2 \
                              + ( t[1,j2] - t[1,j1] ) ** 2 )

  return edge_length

def triangle_edge_length_test ( ):

#*****************************************************************************80
#
## TRIANGLE_EDGE_LENGTH_TEST tests TRIANGLE_EDGE_LENGTH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_transpose_print import r8mat_transpose_print
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'TRIANGLE_EDGE_LENGTH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_EDGE_LENGTH computes the edge lengths' )
  print ( '  of a triangle.' )

  t = np.array ( [ \
    [ 4.0, 1.0, -2.0 ], \
    [ 2.0, 5.0,  2.0 ] ] )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  edge_length = triangle_edge_length ( t )

  r8vec_print ( 3, edge_length, '  EDGE_LENGTHS:' )

  t = np.array ( [ \
    [ 4.0, 5.0, 6.0 ], \
    [ 2.0, 4.0, 6.0 ] ] )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  edge_length = triangle_edge_length ( t )

  r8vec_print ( 3, edge_length, '  EDGE_LENGTHS:' )

  t = np.array ( [ \
    [ 4.0, 1.0, 4.0 ], \
    [ 2.0, 5.0, 2.0 ] ] )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  edge_length = triangle_edge_length ( t )

  r8vec_print ( 3, edge_length, '  EDGE_LENGTHS:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_EDGE_LENGTH_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_edge_length_test ( )
  timestamp ( )
 
