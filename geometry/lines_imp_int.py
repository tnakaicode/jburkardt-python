#! /usr/bin/env python
#
def lines_imp_int ( a1, b1, c1, a2, b2, c2 ):

#*****************************************************************************80
#
## LINES_IMP_INT determines where two implicit lines intersect in 2D.
#
#  Discussion:
#
#    The implicit form of a line in 2D is:
#
#      A * X + B * Y + C = 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2010
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A1, B1, C1, define the first line.
#    At least one of A1 and B1 must be nonzero.
#
#    Input, real A2, B2, C2, define the second line.
#    At least one of A2 and B2 must be nonzero.
#
#    Output, integer IVAL, reports on the intersection.
#    -1, both A1 and B1 were zero.
#    -2, both A2 and B2 were zero.
#     0, no intersection, the lines are parallel.
#     1, one intersection point, returned in X, Y.
#     2, infinitely many intersections, the lines are identical.
#
#    Output, real P(2,1), if IVAL = 1, then P is
#    the intersection point.  if IVAL = 2, then P is one of the
#    points of intersection.  Otherwise, P = [].
#
  import numpy as np
  from r8mat_solve import r8mat_solve

  p = np.zeros ( 2 )
#
#  Refuse to handle degenerate lines.
#
  if ( a1 == 0.0 and b1 == 0.0 ):
    ival = -1
    return ival, p
  elif ( a2 == 0.0 and b2 == 0.0 ):
    ival = -2
    return ival, p
#
#  Set up and solve a linear system.
#
  a = np.zeros ( [ 2, 3 ] )

  a[0,0] = a1
  a[0,1] = b1
  a[0,2] = - c1

  a[1,0] = a2
  a[1,1] = b2
  a[1,2] = - c2

  a, info = r8mat_solve ( 2, 1, a )
#
#  If the inverse exists, then the lines intersect at the solution point.
#
  if ( info == 0 ):

    ival = 1
    p[0] = a[0,2]
    p[1] = a[1,2]
#
#  If the inverse does not exist, then the lines are parallel
#  or coincident.  Check for parallelism by seeing if the
#  C entries are in the same ratio as the A or B entries.
#
  else:

    ival = 0

    if ( a1 == 0.0 ):
      if ( b2 * c1 == c2 * b1 ):
        ival = 2
        p[0] = 0.0
        p[1] = - c1 / b1
    else:
      if ( a2 * c1 == c2 * a1 ):
        ival = 2
        if ( abs ( a1 ) < abs ( b1 ) ):
          p[0] = 0.0
          p[1] = - c1 / b1
        else:
          p[0] = - c1 / a1
          p[1] = 0.0

  return ival, p

def lines_imp_int_test ( ):

#*****************************************************************************80
#
## LINES_IMP_INT_TEST tests LINES_IMP_INT.
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
  print ( '' )
  print ( 'LINES_IMP_INT_TEST' )
  print ( '  LINES_IMP_INT finds the intersection of' )
  print ( '  two lines written in implicit form.' )
#
#  x + 2y - 4 = 0
#
  a1 =  1.0
  b1 =  2.0
  c1 = -4.0
  print ( '' )
  print ( '  Line 1 coefficients:  %8f  %8f  %8f' % ( a1, b1, c1 ) )
#
#  x - y - 1 = 0
#
  a2 =  1.0
  b2 = -1.0
  c2 = -1.0
  print ( '  Line 2 coefficients:  %8f  %8f  %8f' % (  a2, b2, c2 ) )

  ival, p = lines_imp_int ( a1, b1, c1, a2, b2, c2 )

  if ( ival == 1 ):
    print ( '  Intersection at %8f  %8f' % ( p[0], p[1] ) )
  elif ( ival == 0 ):
    print ( '  Lines are parallel, no intersection.' )
  elif ( ival == 2 ):
    print ( '  Lines are coincident.' )
  else:
    print ( '  Unknown return value of ival = %d' % ( ival ) )
#
#  2x + 4y - 1 = 0
#
  print ( '' )
  print ( '  Line 1 coefficients:  %8f  %8f  %8f' % ( a1, b1, c1 ) )

  a2 =  2.0
  b2 = +4.0
  c2 = -1.0
  print ( '  Line 2 coefficients:  %8f  %8f  %8f' % ( a2, b2, c2 ) )

  ival, p = lines_imp_int (a1, b1, c1, a2, b2, c2 )

  if ( ival == 1 ):
    print ( '  Intersection at %8f  %8f' % ( p[0], p[1] ) )
  elif ( ival == 0 ):
    print ( '  Lines are parallel, no intersection.' )
  elif ( ival == 2 ):
    print ( '  Lines are coincident.' )
  else:
    print ( '  Unknown return value of ival = %d' % ( ival ) )
#
#  -3x - 6y +12 = 0
#
  print ( '' )
  print ( '  Line 1 coefficients:  %8f  %8f  %8f' % ( a1, b1, c1 ) )

  a2 =  -3.0
  b2 =  -6.0
  c2 = +12.0
  print ( '  Line 2 coefficients:  %8f  %8f  %8f' % ( a2, b2, c2 ) )
 
  ival, p = lines_imp_int  ( a1, b1, c1, a2, b2, c2 )

  if ( ival == 1 ):
    print ( '  Intersection at %8f  %8f' % ( p[0], p[1] ) )
  elif ( ival == 0 ):
    print ( '  Lines are parallel, no intersection.' )
  elif ( ival == 2 ):
    print ( '  Lines are coincident.' )
  else:
    print ( '  Unknown return value of ival = %d' % ( ival ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LINES_IMP_INT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  lines_imp_int_test ( )
  timestamp ( )

