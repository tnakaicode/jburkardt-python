#! /usr/bin/env python
#
def triangle_diameter ( t ):

#*****************************************************************************80
#
## TRIANGLE_DIAMETER computes the diameter of a triangle in 2D.
#
#  Discussion:
#
#    The diameter of a triangle is the diameter of the smallest circle
#    that can be drawn around the triangle.  At least two of the vertices
#    of the triangle will intersect the circle, but not necessarily
#    all three!
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
#    Output, real DIAMETER, the diameter of the triangle.
#
  import numpy as np
#
#  Compute the squared length of each side.
#
  asq = ( t[0,0] - t[0,1] ) ** 2 + ( t[1,0] - t[1,1] ) ** 2
  bsq = ( t[0,1] - t[0,2] ) ** 2 + ( t[1,1] - t[1,2] ) ** 2
  csq = ( t[0,2] - t[0,0] ) ** 2 + ( t[1,2] - t[1,0] ) ** 2
#
#  Take care of a zero side.
#
  if ( asq == 0.0 ):
    diameter = np.sqrt ( bsq )
    return diameter
  elif ( bsq == 0.0 ):
    diameter = np.sqrt ( csq )
    return diameter
  elif ( csq == 0.0 ):
    diameter = np.sqrt ( asq )
    return diameter
#
#  Make ASQ the largest.
#
  if ( asq < bsq ):
    temp = asq
    asq = bsq
    bsq = temp

  if ( asq < csq ):
    temp = asq
    asq = csq
    csq = temp
#
#  If ASQ is very large...
#
  if ( bsq + csq < asq ):

    diameter = np.sqrt ( asq )

  else:

    a = np.sqrt ( asq )
    b = np.sqrt ( bsq )
    c = np.sqrt ( csq )

    diameter = 2.0 * a * b * c / np.sqrt ( ( a + b + c ) * ( - a + b + c ) \
      * ( a - b + c ) * ( a + b - c ) )

  return diameter

def triangle_diameter_test ( ):

#*****************************************************************************80
#
## TRIANGLE_DIAMETER_TEST tests TRIANGLE_DIAMETER.
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

  print ( '' )
  print ( 'TRIANGLE_DIAMETER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_DIAMETER computes the diameter of' )
  print ( '  the SMALLEST circle around a triangle.' )

  t = np.array ( [ \
    [ 4.0, 1.0, -2.0 ], \
    [ 2.0, 5.0,  2.0 ] ] )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  diameter = triangle_diameter ( t )

  print ( '' )
  print ( '  Diameter = %g' % ( diameter ) )

  t = np.array ( [ \
    [ 4.0, 5.0, 6.0 ], \
    [ 2.0, 4.0, 6.0 ] ] )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  diameter = triangle_diameter ( t )

  print ( '' )
  print ( '  Diameter = %g' % ( diameter ) )

  t = np.array ( [ \
    [ 4.0, 1.0, 4.0 ], \
    [ 2.0, 5.0, 2.0 ] ] )

  r8mat_transpose_print ( 2, 3, t, '  Triangle vertices:' )

  diameter = triangle_diameter ( t )

  print ( '' )
  print ( '  Diameter = %g' % ( diameter ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_DIAMETER_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  triangle_diameter_test ( )
  timestamp ( )
 
