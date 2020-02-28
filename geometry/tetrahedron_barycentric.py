#! /usr/bin/env python
#
def tetrahedron_barycentric ( tetra, p ):

#*****************************************************************************80
#
## TETRAHEDRON_BARYCENTRIC returns barycentric coordinates of a point in 3D.
#
#  Discussion:
#
#    The barycentric coordinates of a point (X,Y,Z) with respect to
#    a tetrahedron are a set of four values C(1:4), each associated
#    with a vertex of the tetrahedron.  The values must sum to 1.
#    If all the values are between 0 and 1, the point is contained
#    within the tetrahedron.
#
#    The barycentric coordinate of point X related to vertex A can be
#    interpreted as the ratio of the volume of the tetrahedron with 
#    vertex A replaced by vertex X to the volume of the original 
#    tetrahedron.
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
#    Input, real P(3), the point to be checked.
#
#    Output, real C(4), the barycentric coordinates of (X,Y,Z) with
#    respect to the tetrahedron.
#
  import numpy as np
  from r8mat_solve import r8mat_solve
  from sys import exit
#
#  Set up the linear system
#
#    ( X2-X1  X3-X1  X4-X1 ) C1    X - X1
#    ( Y2-Y1  Y3-Y1  Y4-Y1 ) C2  = Y - Y1
#    ( Z2-Z1  Z3-Z1  Z4-Z1 ) C3    Z - Z1
#
#  which is satisfied by the barycentric coordinates of (X,Y,Z).
#
  a = np.zeros ( [ 3, 4 ] )

  a[0:3,0:3] = tetra[0:3,1:4]
  for i in range ( 0, 3 ):
    a[i,3] = p[i]

  for i in range ( 0, 3 ):
    a[i,0:4] = a[i,0:4] - tetra[i,0]
#
#  Solve the linear system.
#
  nrhs = 1
  a, info = r8mat_solve ( 3, nrhs, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'TETRAHEDRON_BARYCENTRIC - Fatal error!' )
    print ( '  The linear system is singular.' )
    print ( '  The input data does not form a proper tetrahedron.' )
    exit ( 'TETRAHEDRON_BARYCENTRIC - Fatal error!' )

  c = np.zeros ( 4 )

  c[1:4] = a[0:3,3]

  c[0] = 1.0 - np.sum ( c[1:4] )

  return c

def tetrahedron_barycentric_test ( ):

#*****************************************************************************80
#
## TETRAHEDRON_BARYCENTRIC_TEST tests TETRAHEDRON_BARYCENTRIC.
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
  from tetrahedron_sample import tetrahedron_sample

  seed = 123456789

  t = np.array ( [ \
    [ 1.0, 4.0, 3.0 ], \
    [ 2.0, 4.0, 3.0 ], \
    [ 1.0, 6.0, 3.0 ], \
    [ 1.0, 4.0, 4.0 ] ] )

  t = np.transpose ( t )

  print ( '' )
  print ( 'TETRAHEDRON_BARYCENTRIC_TEST' )
  print ( '  TETRAHEDRON_BARYCENTRIC converts XYZ to XSI.' )
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
  print ( 'TETRAHEDRON_BARYCENTRIC_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tetrahedron_barycentric_test ( )
  timestamp ( )

