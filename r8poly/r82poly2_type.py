#! /usr/bin/env python3
#
def r82poly2_type ( a, b, c, d, e, f ):

#*****************************************************************************80
#
## R82POLY2_TYPE analyzes a second order polynomial in two variables.
#
#  Discussion:
#
#    The polynomial has the form
#
#      A x^2 + B y^2 + C xy + Dx + Ey + F = 0
#
#    The possible types of the solution set are:
#
#     1: a hyperbola
#        9x^2 -  4y^2       -36x - 24y -  36 = 0
#     2: a parabola
#        4x^2 +  1y^2 - 4xy + 3x -  4y +   1 = 0
#     3: an ellipse
#        9x^2 + 16y^2       +36x - 32y -  92 = 0
#     4: an imaginary ellipse (no real solutions)
#         x^2 +   y^2       - 6x - 10y + 115 = 0
#     5: a pair of intersecting lines
#                        xy + 3x -   y -   3 = 0
#     6: one point
#         x^2 +  2y^2       - 2x + 16y +  33 = 0
#     7: a pair of distinct parallel lines
#                 y^2            -  6y +   8 = 0
#     8: a pair of imaginary parallel lines (no real solutions)
#                 y^2            -  6y +  10 = 0
#     9: a pair of coincident lines.
#                 y^2            -  2y +   1 = 0
#    10: a single line
#                             2x -   y +   1 = 0
#    11 all space
#                                          0 = 0
#    12 no solutions
#                                          1 = 0
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    CRC Press, 30th Edition, 1996, pages 282-284.
#
#  Parameters:
#
#    Input, real A, B, C, D, E, F, the coefficients.
#
#    Output, integer TYPE, indicates the type of the solution set.
#
  from r8_sign import r8_sign
#
#  Handle the degenerate case.
#
  if ( a == 0.0 and b == 0.0 and c == 0.0 ):
    if ( d == 0.0 and e == 0.0 ):
      if ( f == 0.0 ):
        type = 11
      else:
        type = 12
    else:
      type = 10
    return type

  delta = 8.0 * a * b * f \
        + 2.0 * c * e * d \
        - 2.0 * a * e * e \
        - 2.0 * b * d * d \
        - 2.0 * f * c * c

  j = 4.0 * a * b - c * c

  if ( delta != 0.0 ):
    if ( j < 0.0 ):
      type = 1
    elif ( j == 0.0 ):
      type = 2
    elif ( 0.0 < j ):
      if ( r8_sign ( delta ) != r8_sign ( a + b ) ):
        type = 3
      elif ( r8_sign ( delta ) == r8_sign ( a + b ) ):
        type = 4
  elif ( delta == 0.0 ):
    if ( j < 0.0 ):
      type = 5
    elif ( 0.0 < j ):
      type = 6
    elif ( j == 0.0 ):

      k = 4.0 * ( a + b ) * f - d * d - e * e

      if ( k < 0.0 ):
        type = 7
      elif ( 0.0 < k ):
        type = 8
      elif ( k == 0.0 ):
        type = 9

  return type

def r82poly2_type_print ( type ):

#*****************************************************************************80
#
## R82POLY2_TYPE_PRINT prints the meaning of the output from R82POLY2_TYPE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer TYPE, the type index returned by R82POLY2_TYPE.
#
  if ( type == 1 ):
    print ( '  The set of solutions forms a hyperbola.' )
  elif ( type == 2 ):
    print ( '  The set of solutions forms a parabola.' )
  elif ( type == 3 ):
    print ( '  The set of solutions forms an ellipse.' )
  elif ( type == 4 ):
    print ( '  The set of solutions forms an imaginary ellipse.' )
    print ( '  (There are no real solutions).' )
  elif ( type == 5 ):
    print ( '  The set of solutions forms a pair of intersecting lines.' )
  elif ( type == 6 ):
    print ( '  The set of solutions is a single point.' )
  elif ( type == 7 ):
    print ( '  The set of solutions form a pair of distinct parallel lines.' )
  elif ( type == 8 ):
    print ( '  The set of solutions forms a pair of imaginary parallel lines.' )
    print ( '  (There are no real solutions).' )
  elif ( type == 9 ):
    print ( '  The set of solutions forms a pair of coincident lines.' )
  elif ( type == 10 ):
    print ( '  The set of solutions forms a single line.' )
  elif ( type == 11 ):
    print ( '  The set of solutions is all space.' )
  elif ( type == 12 ):
    print ( '  The set of solutions is empty.' )
  else:
    print ( '  This type index is unknown.' )

  return

def r82poly2_type_test ( ):

#*****************************************************************************80
#
## R82POLY2_TYPE_TEST tests R82POLY2_TYPE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r82poly2_print import r82poly2_print

  test_num = 12

  a_test = np.array ( [  \
    9.0, 4.0, 9.0,  1.0, 0.0, \
    1.0, 0.0, 0.0,  0.0, 0.0, \
    0.0, 0.0 ] )
  b_test = np.array ( [ \
    -4.0,   1.0,  16.0,   1.0, 0.0,  \
     2.0, 1.0,   1.0,  1.0,  0.0, \
     0.0, 0.0 ] )
  c_test = np.array ( [ \
     0.0,  -4.0,   0.0,   0.0, 1.0,  \
     0.0, 0.0,   0.0,  0.0,  0.0, \
     0.0, 0.0 ] )
  d_test = np.array ( [ \
    -36.0,  3.0,  36.0,  -6.0, 3.0, \
    -2.0, 0.0,   0.0,  0.0,  2.0, \
     0.0, 0.0 ] )
  e_test = np.array ( [ \
    -24.0, -4.0, -32.0, -10.0, -1.0, \
     16.0, -6.0, -6.0, -2.0, -1.0, \
     0.0, 0.0 ] )
  f_test = np.array ( [ \
    -36.0,  1.0, -92.0, 115.0, -3.0, \
     33.0, +8.0, 10.0,  +1.0,  1.0, \
      0.0, 1.0 ] )

  print ( '' )
  print ( 'R82POLY2_TYPE_TEST' )
  print ( '  R82POLY2_TYPE determines the type of a second order' )
  print ( '  equation in two variables.' )
  print ( '' )

  for test in range ( 0, test_num ):

    a = a_test[test]
    b = b_test[test]
    c = c_test[test]
    d = d_test[test]
    e = e_test[test]
    f = f_test[test]

    print ( '' )

    r82poly2_print ( a, b, c, d, e, f )

    type = r82poly2_type ( a, b, c, d, e, f )

    print ( '  Type = %d' % ( type ) )

    r82poly2_type_print ( type )
#
#  Terminate.
#
  print ( '' )
  print ( 'R82POLY2_TYPE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r82poly2_type_test ( )
  timestamp ( )

