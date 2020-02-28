#! /usr/bin/env python
#
def circle_imp_print_2d ( r, center, title ):

#*****************************************************************************80
#
## CIRCLE_IMP_PRINT_2D prints an implicit circle in 2D.
#
#  Discussion:
#
#    An implicit circle in 2D satisfies:
#
#      ( X - CENTER(1) )^2 + ( Y - CENTER(2) )^2 = R^2
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real R, the radius of the circle.
#
#    Input, real CENTER(2), the center of the circle.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( '%s' % ( title ) )
  print ( '' )
  print ( '  Radius = %f' % ( r ) )
  print ( '  Center = ( %f,  %f )' % ( center[0], center[1] ) )

  return

def circle_imp_print_2d_test ( ):

#*****************************************************************************80
#
## CIRCLE_IMP_PRINT_2D_TEST tests CIRCLE_IMP_PRINT_2D.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 January 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  center = np.array ( [ 5.0, -2.0 ] )
  r = 2.0
 
  print ( '' )
  print ( 'CIRCLE_IMP_PRINT_2D_TEST' )
  print ( '  CIRCLE_IMP_PRINT_2D prints a circle definition.' )

  circle_imp_print_2d ( r, center, '  An example circle:' )

  return

if ( __name__ == '__main__' ):
  circle_imp_print_2d_test ( )

