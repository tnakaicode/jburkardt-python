#! /usr/bin/env python
#
def triangle_barycentric ( t, p ):

#*****************************************************************************80
#
#% TRIANGLE_BARYCENTRIC finds the barycentric coordinates of a point.
#
#  Discussion:
#
#    The barycentric coordinate of point X related to vertex A can be
#    interpreted as the ratio of the area of the triangle with
#    vertex A replaced by vertex X to the area of the original
#    triangle.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real T(2,3), the triangle vertices.
#    The vertices should be given in counter clockwise order.
#
#    Input, real P(2), the point to be checked.
#
#    Output, real XSI(3), the barycentric coordinates of (X,Y)
#    with respect to the triangle.
#
  import numpy as np
  from r8mat_solve import r8mat_solve
  from sys import exit

  nrhs = 1
#
#  Set up the linear system
#
#    ( X2-X1  X3-X1 ) XSI(1)  = X-X1
#    ( Y2-Y1  Y3-Y1 ) XSI(2)    Y-Y1
#
#  which is satisfied by the barycentric coordinates of (X,Y).
#
  a = np.zeros ( [ 2, 3 ] )

  a[0,0] = t[0,1] - t[0,0]
  a[0,1] = t[0,2] - t[0,0]
  a[0,2] = p[0]   - t[0,0]

  a[1,0] = t[1,1] - t[1,0]
  a[1,1] = t[1,2] - t[1,0]
  a[1,2] = p[1]   - t[1,0]
#
#  Solve the linear system.
#
  a, info = r8mat_solve ( 2, nrhs, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'TRIANGLE_BARYCENTRIC - Fatal error!' )
    print ( '  The linear system is singular.' )
    print ( '  The input data does not form a proper triangle.' )
    exit ( 'TRIANGLE_BARYCENTRIC - Fatal error!' )

  xsi = np.zeros ( 3 )

  xsi[0] = a[0,2]
  xsi[1] = a[1,2]
  xsi[2] = 1.0 - xsi[0] - xsi[1]

  return xsi

def triangle_barycentric_test ( ):

#*****************************************************************************80
#
## TRIANGLE_BARYCENTRIC_TEST tests TRIANGLE_BARYCENTRIC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 July 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_transpose_print import r8mat_transpose_print

  ntest = 7

  p_test = np.array ( [ \
    [ 0.25, 0.75, 1.00, 11.00, 0.00,   0.50, 0.60 ], \
    [ 0.25, 0.25, 1.00,  0.50, 1.00, -10.00, 0.60 ] ] )

  t = np.array ( [ \
    [ 0.0, 0.0, 1.0 ], \
    [ 1.0, 0.0, 0.0 ] ] )

  print ( '' )
  print ( 'TRIANGLE_BARYCENTRIC_TEST' )
  print ( '  TRIANGLE_BARYCENTRIC converts XY coordinates' )
  print ( '  to barycentric XSI coordinates in a triangle;' )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  print ( '' )
  print ( '   X       Y     XSI' )
  print ( '' )

  for j in range ( 0, ntest ):

    p = p_test[:,j]

    xsi = triangle_barycentric ( t, p )

    print ( '  %10f  %10f    %10f  %10f  %10f' \
      % ( p[0], p[1], xsi[0], xsi[1], xsi[2] ) )

#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_BARYCENTRIC_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_barycentric_test ( )
  timestamp ( )

