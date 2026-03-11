#! /usr/bin/env python3
#
def r8poly_test ( ):

#*****************************************************************************80
#
## r8poly_test() tests r8poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 November 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8poly_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8poly()' )

  r8_sign_test ( )

  r82poly2_print_test ( )
  r82poly2_type_test ( )

  r8mat_inverse_3d_test ( );

  r8poly_add_test ( )
  r8poly_ant_coef_test ( )
  r8poly_ant_value_test ( )
  r8poly_degree_test ( )
  r8poly_deriv_test ( )
  r8poly_division_test ( )
  r8poly_lagrange_0_test ( )
  r8poly_lagrange_1_test ( )
  r8poly_lagrange_2_test ( )
  r8poly_lagrange_coef_test ( )
  r8poly_lagrange_factor_test ( )
  r8poly_lagrange_value_test ( )
  r8poly_multiply_test ( )
  r8poly_power_test ( )
  r8poly_print_test ( )
  r8poly_shift_test ( )
  r8poly_value_test ( )
  r8poly_value_horner_test ( )
  r8poly_values_horner_test ( )

  r8poly2_ex_test ( );
  r8poly2_ex2_test ( );
  r8poly2_root_test ( )
  r8poly2_rroot_test ( )
  r8poly2_val_test ( )
  r8poly2_val2_test ( )

  r8poly3_root_test ( )

  r8poly4_root_test ( )

  r8vec_even_test ( )
  r8vec_even_select_test ( )
  r8vec_indicator1_test ( )
  r8vec_is_distinct_test ( )
  r8vec_is_zero_test ( )

  r8vec2_print_test ( )

  roots_to_r8poly_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8poly_test():' )
  print ( '  Normal end of execution.' )
  return

def r82poly2_print ( a, b, c, d, e, f ):

#*****************************************************************************80
#
## r82poly2_print() prints a second order polynomial in two variables.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, D, E, F, the coefficients.
#
  print ( '  p(x,y) = %g * x^2 + %g * y^2 + %g * xy' % ( a, b, c ) )
  print ( '         + %g * x + %g * y + %g' % ( d, e, f ) )

  return

def r82poly2_print_test ( ):

#*****************************************************************************80
#
## r82poly2_print_test() tests r82poly2_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r82poly2_print_test():' )
  print ( '  r82poly2_print() prints an R82POLY2,' )
  print ( '  a quadratic polynomial in x and y.' )

  a = 1.0
  b = 2.0
  c = 3.0
  d = 4.0
  e = 5.0
  f = 6.0

  print ( '' )
  print ( '  Coefficients a, b, c, d, e, f:' )
  print ( '  %g  %g  %g  %g  %g  %g' % ( a, b, c, d, e, f ) )
  print ( '' )

  r82poly2_print ( a, b, c, d, e, f  )

  return

def r82poly2_type ( a, b, c, d, e, f ):

#*****************************************************************************80
#
## r82poly2_type() analyzes a second order polynomial in two variables.
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
#    This code is distributed under the MIT license.
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
#  Input:
#
#    real A, B, C, D, E, F, the coefficients.
#
#  Output:
#
#    integer TYPE, indicates the type of the solution set.
#

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
## r82poly2_type_print() prints the meaning of the output from r82poly2_type.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer TYPE, the type index returned by r82poly2_type.
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
## r82poly2_type_test() tests r82poly2_type().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'r82poly2_type_test():' )
  print ( '  r82poly2_type() determines the type of a second order' )
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

  return

def r8mat_inverse_3d ( a ):

#*****************************************************************************80
#
## r8mat_inverse_3d() inverts a 3 by 3 R8MAT using Cramer's rule.
#
#  Discussion:
#
#    If DET is zero, then A is singular, and does not have an
#    inverse.  In that case, B is simply set to zero, and a
#    message is printed.
#
#    If DET is nonzero, then its value is roughly an estimate
#    of how nonsingular the matrix A is.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(3,3), the matrix to be inverted.
#
#  Output:
#
#    real B(3,3), the inverse of the matrix.
#
#    real DET, the determinant of the matrix.
#
  import numpy as np
#
#  Compute the determinant of A
#
  det =   a[0,0] * ( a[1,1] * a[2,2] - a[1,2] * a[2,1] ) \
        + a[0,1] * ( a[1,2] * a[2,0] - a[1,0] * a[2,2] ) \
        + a[0,2] * ( a[1,0] * a[2,1] - a[1,1] * a[2,0] )
#
#  If the determinant is zero, bail out.
#
  if ( det == 0.0 ):
    b = np.zeros ( [ 3, 3 ] )
    return b, det
#
#  Compute the entries of the inverse matrix using an explicit
#  formula.
#
  b = np.zeros ( [ 3, 3 ] )

  b[0,0] = + ( a[1,1] * a[2,2] - a[1,2] * a[2,1] ) / det
  b[0,1] = - ( a[0,1] * a[2,2] - a[0,2] * a[2,1] ) / det
  b[0,2] = + ( a[0,1] * a[1,2] - a[0,2] * a[1,1] ) / det

  b[1,0] = - ( a[1,0] * a[2,2] - a[1,2] * a[2,0] ) / det
  b[1,1] = + ( a[0,0] * a[2,2] - a[0,2] * a[2,0] ) / det
  b[1,2] = - ( a[0,0] * a[1,2] - a[0,2] * a[1,0] ) / det

  b[2,0] = + ( a[1,0] * a[2,1] - a[1,1] * a[2,0] ) / det
  b[2,1] = - ( a[0,0] * a[2,1] - a[0,1] * a[2,0] ) / det
  b[2,2] = + ( a[0,0] * a[1,1] - a[0,1] * a[1,0] ) / det

  return b, det

def r8mat_inverse_3d_test ( ):

#*****************************************************************************80
#
## r8mat_inverse_3d_test() tests r8mat_inverse_3d().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 3
#
#  Each ROW of this definion is a COLUMN of the matrix.
#
  a = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 4.0, 5.0, 6.0 ], \
    [ 7.0, 8.0, 0.0 ] ] )

  print ( '' )
  print ( 'r8mat_inverse_3d_test():' )
  print ( '  r8mat_inverse_3d() inverts a 3 by 3 matrix.' )

  r8mat_print ( n, n, a, '  Matrix A to be inverted:' )
#
#  Compute the inverse matrix.
#
  b, det = r8mat_inverse_3d ( a )
 
  if ( det == 0.0 ):
    print ( '' )
    print ( '  The input matrix was singular, no inverse' )
    print ( '  could be computed.' )
    return

  r8mat_print ( n, n, b, '  Inverse matrix B:' )

  c = np.dot ( a, b )

  r8mat_print ( n, n, c, '  Product C = A * B:' )

  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8poly2_discriminant ( a, b, c ):

#*****************************************************************************80
#
## r8poly2_discriminant() returns the discriminant of a quadratic polynomial.
#
#  Discussion:
#
#    The polynomial has the form:
#
#      A * X^2 + B * X + C = 0 
#
#    If the discriminant is zero, then the polynomial has a multiple root.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the coefficients of the polynomial.
#
#  Output:
#
#    real VALUE, the discriminant.
#
  value = b * b - 4.0 * a * c

  return value

def r8poly2_ex2 ( x1, y1, x2, y2, x3, y3 ):

#*****************************************************************************80
#
## r8poly2_ex2() finds the extremal point of a parabola determined by three points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X1, Y1, X2, Y2, X3, Y3, the coordinates of 
#    three points on the parabola.  X1, X2 and X3 must be distinct.
#
#  Output:
#
#    real X, Y, the X coordinate of the extremal 
#    point of the parabola, and the value of the parabola at that point.
#
#    real A, B, C, the coefficients that define the
#    parabola: P(X) = A * X^2 + B * X + C.
#
#    integer IERROR, error flag.
#    0, no error.
#    1, two of the X values are equal.
#    2, the data lies on a straight line there is no finite extremal
#    point.
#
  import numpy as np

  ierror = 0
  x = x1
  y = y1
  a = 0.0
  b = 0.0
  c = 0.0

  if ( x1 == x2 or x2 == x3 or x3 == x1 ):
    ierror = 1
    return x, y, a, b, c, ierror

  if ( y1 == y2 and y2 == y3 and y3 == y1 ):
    x = x1
    y = y1
    return x, y, a, b, c, ierror
#
#  Set up the Vandermonde matrix.
#
  v = np.array ( [ \
    [ 1.0, x1, x1 * x1 ], \
    [ 1.0, x2, x2 * x2 ], \
    [ 1.0, x3, x3 * x3 ] ] )
#
#  Get the inverse.
#
  w, det = r8mat_inverse_3d ( v )
#
#  Compute the parabolic coefficients.
#
  c = w[0,0] * y1 + w[0,1] * y2 + w[0,2] * y3
  b = w[1,0] * y1 + w[1,1] * y2 + w[1,2] * y3
  a = w[2,0] * y1 + w[2,1] * y2 + w[2,2] * y3
#
#  Determine the extremal point.
#
  if ( a == 0.0 ):
    ierror = 2
    return x, y, a, b, c, ierror

  x = -b / ( 2.0 * a )
  y = a * x * x + b * x + c

  return x, y, a, b, c, ierror

def r8poly2_ex2_test ( ):

#*****************************************************************************80
#
## r8poly2_ex2_test() tests r8poly2_ex2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8poly2_ex2_test():' )
  print ( '  r8poly2_ex2() finds the extreme value' )
  print ( '  of a parabola determined by three points.' )

  a =  2.0
  b = -4.0
  c = 10.0

  x1 = 1.0
  y1 = a * x1 * x1 + b * x1 + c
  x2 = 2.0
  y2 = a * x2 * x2 + b * x2 + c
  x3 = 3.0
  y3 = a * x3 * x3 + b * x3 + c

  print ( '' )
  print ( '  Parabolic coefficients:' )
  print ( '  A = %f, B = %f, C = %f' % ( a, b, c ) )
  print ( '' )
  print ( '  Point 1: (%g,%g)' % ( x1, y1 ) )
  print ( '  Point 1: (%g,%g)' % ( x2, y2 ) )
  print ( '  Point 1: (%g,%g)' % ( x3, y3 ) )

  a = 0.0
  b = 0.0
  c = 0.0

  xmin, ymin, a, b, c, ierror = r8poly2_ex2 ( x1, y1, x2, y2, x3, y3 )

  print ( '\n' )
  print ( '  r8poly2_ex2 returns XMIN = %f, YMIN = %f' % ( xmin, ymin ) )
  print ( '  and A = %f, B = %f, C = %f' % ( a, b, c ) )

  return

def r8poly2_ex ( x1, y1, x2, y2, x3, y3 ):

#*****************************************************************************80
#
## r8poly2_ex() finds the extremal point of a parabola determined by three points.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X1, Y1, X2, Y2, X3, Y3, the coordinates of 
#    three points on the parabola.  X1, X2 and X3 must be distinct.
#
#  Output:
#
#    real X, Y, the X coordinate of the extremal point
#    of the parabola, and the value of the parabola at that point.
#
#    integer IERROR, error flag.
#    0, no error.
#    1, two of the X values are equal.
#    2, the data lies on a straight line there is no finite extremal
#    point.
#
  ierror = 0
  x = x1
  y = y1

  if ( x1 == x2 or x2 == x3 or x3 == x1 ):
    ierror = 1
    return x, y, ierror

  if ( y1 == y2 and y2 == y3 and y3 == y1 ):
    return x, y, ierror

  bot = ( x2 - x3 ) * y1 - ( x1 - x3 ) * y2 + ( x1 - x2 ) * y3

  if ( bot == 0.0 ):
    ierror = 2
    return x, y, ierror

  x = 0.5 * ( \
          x1 * x1 * ( y3 - y2 ) \
        + x2 * x2 * ( y1 - y3 ) \
        + x3 * x3 * ( y2 - y1 ) ) / bot

  y = ( \
         ( x - x2 ) * ( x - x3 ) * ( x2 - x3 ) * y1 \
       - ( x - x1 ) * ( x - x3 ) * ( x1 - x3 ) * y2 \
       + ( x - x1 ) * ( x - x2 ) * ( x1 - x2 ) * y3 ) / \
       ( ( x1 - x2 ) * ( x2 - x3 ) * ( x1 - x3 ) )

  return x, y, ierror

def r8poly2_ex_test ( ):

#*****************************************************************************80
#
## r8poly2_ex_test() tests r8poly2_ex().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8poly2_ex_test():' )
  print ( '  r8poly2_ex() finds the extreme value' )
  print ( '  of a parabola determined by three points.' )

  a =  2.0
  b = -4.0
  c = 10.0

  x1 = 1.0
  y1 = a * x1 * x1 + b * x1 + c
  x2 = 2.0
  y2 = a * x2 * x2 + b * x2 + c
  x3 = 3.0
  y3 = a * x3 * x3 + b * x3 + c

  print ( '' )
  print ( '  Parabolic coefficients:' )
  print ( '  A = %f, B = %f, C = %f' % ( a, b, c ) )
  print ( '' )
  print ( '  Point 1: (%g,%g)' % ( x1, y1 ) )
  print ( '  Point 1: (%g,%g)' % ( x2, y2 ) )
  print ( '  Point 1: (%g,%g)' % ( x3, y3 ) )

  a = 0.0
  b = 0.0
  c = 0.0

  xmin, ymin, ierror = r8poly2_ex ( x1, y1, x2, y2, x3, y3 )

  print ( '' )
  print ( '  r8poly2_ex returns XMIN = %f, YMIN = %f' % ( xmin, ymin ) )

  return

def r8poly2_root ( a, b, c ):

#*****************************************************************************80
#
## r8poly2_root() returns the two roots of a quadratic polynomial.
#
#  Discussion:
#
#    The polynomial has the form:
#
#      A * X^2 + B * X + C = 0 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the coefficients of the polynomial.
#    A must not be zero.
#
#  Output:
#
#    complex R1, R2, the roots of the polynomial, which
#    might be real and distinct, real and equal, or complex conjugates.
#
  import cmath
  import numpy as np

  if ( a == 0.0 ):
    print ( '' )
    print ( 'r8poly2_root(): Fatal error!' )
    print ( '  The coefficient A is zero.' )
    raise Exception ( 'r8poly2_root(): Fatal error!' )

  disc = b * b - 4.0 * a * c
  q = - 0.5 * ( b + r8_sign ( b ) * cmath.sqrt ( disc ) )
  r1 = q / a
  r2 = c / q

  return r1, r2

def r8poly2_root_test ( ):

#*****************************************************************************80
#
## r8poly2_root_test() tests r8poly2_root().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 3

  a_test = np.array ( [ 2.0, 1.0, 1.0 ] )
  b_test = np.array ( [ -2.0, -20.0, -2.0 ] )
  c_test = np.array ( [ -24.0, 100.0, 10.0 ] )
 
  print ( '' )
  print ( 'r8poly2_root_test():' )
  print ( '  r8poly2_root() finds quadratic equation roots.' )
  print ( '  r8poly2_discriminant() returns the discriminant.' )

  for test in range ( 0, test_num ):

    a = a_test[test]
    b = b_test[test]
    c = c_test[test]

    r1, r2 = r8poly2_root ( a, b, c )
    discr = r8poly2_discriminant ( a, b, c )

    print ( '' )
    print ( '  (A,B,C):      %8.4f  %8.4f  %8.4f' \
      % ( a, b, c ) )

    print ( '  (R1,R2,Disc): %8.4f  %8.4f  %8.4f  %8.4f  %8.4f' \
      % ( r1.real, r1.imag, r2.real, r2.imag, discr ) )

  return

def r8poly2_rroot ( a, b, c ):

#*****************************************************************************80
#
## r8poly2_rroot() returns the real parts of the roots of a quadratic polynomial.
#
#  Example:
#
#    A    B    C       roots              R1   R2
#   --   --   --     ------------------   --   --
#    1   -4    3     1          3          1    3
#    1    0    4     2*i      - 2*i        0    0
#    1   -6   10     3 +   i    3 -   i    3    3
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, the coefficients of the quadratic
#    polynomial A * X^2 + B * X + C = 0 whose roots are desired.
#    A must not be zero.
#
#  Output:
#
#    real R1, R2, the real parts of the roots
#    of the polynomial.
#
  import numpy as np

  if ( a == 0.0 ):
    print ( '' )
    print ( 'r8poly2_rroot(): Fatal error!' )
    print ( '  The coefficient A is zero.' )
    raise Exception ( 'r8poly2_rroot(): Fatal error!' )

  disc = b * b - 4.0 * a * c

  if ( 0.0 <= disc ):
    q = ( b + r8_sign ( b ) * np.sqrt ( disc ) )
    r1 = - 0.5 * q / a
    r2 = - 2.0 * c / q
  else:
    r1 = - b / 2.0 / a
    r2 = - b / 2.0 / a

  return r1, r2

def r8poly2_rroot_test ( ):

#*****************************************************************************80
#
## r8poly2_rroot_test() tests r8poly2_rroot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 December 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 5

  a_test = np.array ( [  2.0,    1.0,  1.0, 1.0,  1.0 ] )
  b_test = np.array ( [ -2.0,  -20.0, -2.0, 0.0, -6.0 ] )
  c_test = np.array ( [ -24.0, 100.0, 10.0, 1.0, 10.0 ] )
 
  print ( '' )
  print ( 'r8poly2_rroot_test()' )
  print ( '  r8poly2_rroot() finds the real parts of quadratic equation roots.' )
  print ( '' )
  print ( '         A         B         C     R1         R2' )
  print ( '' )

  for test in range ( 0, test_num ):

    a = a_test[test]
    b = b_test[test]
    c = c_test[test]

    r1, r2 = r8poly2_rroot ( a, b, c )
 
    print ( '  %8.4f  %8.4f  %8.4f  %8.4f  %8.4f' % ( a, b, c, r1, r2 ) )

  return

def r8poly2_val2 ( dim_num, ndata, tdata, ydata, left, tval ):

#*****************************************************************************80
#
## r8poly2_val2() evaluates a parabolic interpolant through tabular data.
#
#  Discussion:
#
#    This routine constructs the parabolic interpolant through the data in
#    3 consecutive entries of a table and evaluates this interpolant
#    at a given abscissa value.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    30 September 2006
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer DIM_NUM, the dimension of a single data point.
#    DIM_NUM must be at least 1.
#
#    integer NDATA, the number of data points.
#    NDATA must be at least 3.
#
#    real TDATA(NDATA), the abscissas of the data points.
#    The values in TDATA must be in strictly ascending order.
#
#    real YDATA(DIM_NUM,NDATA), the data points 
#    corresponding to the abscissas.
#
#    integer LEFT, the location of the first of the three
#    consecutive data points through which the parabolic interpolant
#    must pass.  1 <= LEFT <= NDATA - 2.
#
#    real TVAL, the value of T at which the parabolic
#    interpolant is to be evaluated.  Normally, TDATA(1) <= TVAL <= T(NDATA),
#    and the data will be interpolated.  For TVAL outside this range,
#    extrapolation will be used.
#
#  Output:
#
#    real YVAL(DIM_NUM), the value of the parabolic
#    interpolant at TVAL.
#
  import numpy as np
#
#  Check.
#
  if ( left < 1 or ndata - 2 < left ):
    print ( '' )
    print ( 'r8poly2_val2(): Fatal error!' )
    print ( '  LEFT < 1 or NDATA-2 < LEFT.' )
    print ( '  LEFT = ', left )
    raise Exception ( 'r8poly2_val2(): Fatal error!' )

  if ( dim_num < 1 ):
    print ( '' )
    print ( 'r8poly2_val2(): Fatal error!' )
    print ( '  DIM_NUM < 1.' )
    print ( '  DIM_NUM = ', dim_num )
    raise Exception ( 'r8poly2_val2(): Fatal error!' )
#
#  Copy out the three abscissas.
#
  t1 = tdata[left-1]
  t2 = tdata[left]
  t3 = tdata[left+1]

  if ( t2 <= t1 or t3 <= t2 ):
    print ( '' )
    print ( 'r8poly2_val2(): Fatal error!' )
    print ( '  T2 <= T1 or T3 <= T2.' )
    print ( '  T1 = ', t1 )
    print ( '  T2 = ', t2 )
    print ( '  T3 = ', t3 )
    raise Exception ( 'r8poly2_val2(): Fatal error!' )
#
#  Construct and evaluate a parabolic interpolant for the data
#  in each dimension.
#
  yval = np.zeros ( dim_num )

  for i in range ( 0, dim_num ):

    y1 = ydata[i,left-1]
    y2 = ydata[i,left]
    y3 = ydata[i,left+1]

    dif1 = ( y2 - y1 ) / ( t2 - t1 )
    dif2 = ( ( y3 - y1 ) / ( t3 - t1 ) \
           - ( y2 - y1 ) / ( t2 - t1 ) ) / ( t3 - t2 )

    yval[i] = y1 + ( tval - t1 ) * ( dif1 + ( tval - t2 ) * dif2 )

  return yval

def r8poly2_val2_test ( ):

#*****************************************************************************80
#
## r8poly2_val2_test() tests r8poly2_val2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  ndata = 5
  dim_num = 2

  print ( '' )
  print ( 'r8poly2_val2_test():' )
  print ( '  r8poly2_val2() evaluates parabolas through' )
  print ( '  3 points in a table' )
  print ( '' )
  print ( '  Our data tables will actually be parabolas:' )
  print ( '    A: 2*x^2 + 3 * x + 1.' )
  print ( '    B: 4*x^2 - 2 * x + 5.' )
  print ( '' )

  xdata = np.zeros ( ndata )
  ydata = np.zeros ( [ 2, ndata ] )

  for i in range ( 0, ndata ):
    xval = 2.0 * i
    xdata[i] = xval
    ydata[0,i] = 2.0 * xval * xval + 3.0 * xval + 1.0
    ydata[1,i] = 4.0 * xval * xval - 2.0 * xval + 5.0
    print ( '  %6d  %12f  %12f  %12f' % \
      ( i, xdata[i], ydata[0,i], ydata[1,i] ) )

  print ( '' )
  print ( '  Interpolated data:' )
  print ( '' )
  print ( '  LEFT, X, Y1, Y2' )
  print ( '' )

  for i in range ( 0, 5 ):
    xval = 2 * i + 1
    left = max ( min ( i + 1, ndata - 2 ), 1 )
    yval = r8poly2_val2 ( dim_num, ndata, xdata, ydata, left, xval )
    print ( '  %8d  %12f  %12f  %12f' % ( left, xval, yval[0], yval[1] ) )

  return

def r8poly2_val ( x1, y1, x2, y2, x3, y3, x ):

#*****************************************************************************80
#
## r8poly2_val() evaluates a parabola defined by three data values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X1, Y1, X2, Y2, X3, Y3, three pairs of data.
#    If the X values are distinct, then all the Y values represent
#    actual values of the parabola.
#
#    Three special cases are allowed:
#
#      X1 == X2 /= X3: Y2 is the derivative at X1
#      X1 /= X2 == X3: Y3 is the derivative at X3
#      X1 == X2 == X3: Y2 is the derivative at X1, and
#                      Y3 is the second derivative at X1.
#
#    real X, an abscissa at which the parabola is to be
#    evaluated.
#
#  Output:
#
#    real Y, YP, YPP, the values of the parabola and
#    its first and second derivatives at X.
#

#
#  If any X's are equal, put them and the Y data first.
#
  if ( x1 == x2 and x2 == x3 ):
    distinct = 1
  elif ( x1 == x2 ):
    distinct = 2
  elif ( x1 == x3 ):
    print ( '' )
    print ( 'r8poly2_val(): Fatal error!' )
    print ( '  X1 = X3 =/= X2.' )
    print ( '  X1 = %f' % ( x1 ) )
    print ( '  X2 = %f' % ( x2 ) )
    print ( '  X3 = %f' % ( x3 ) )
    raise Exception ( 'r8poly2_val(): Fatal error!' )
  elif ( x2 == x3 ):
    distinct = 2
    t  = x1
    x1 = x2
    x2 = t
    t  = x2
    x2 = x3
    x3 = t
    t  = y1
    y1 = y2
    y2 = t
    t  = y2
    y2 = y3
    y3 = t
  else:
    distinct = 3
#
#  Set up the coefficients.
#
  if ( distinct == 1 ):

    dif1 = y2
    dif2 = 0.5 * y3

  elif ( distinct == 2 ):

    dif1 = y2
    dif2 = ( ( y3 - y1 ) / ( x3 - x1 ) - y2 ) / ( x3 - x2 )

  elif ( distinct == 3 ):

    dif1 = ( y2 - y1 ) / ( x2 - x1 )
    dif2 =  ( ( y3 - y1 ) / ( x3 - x1 ) \
            - ( y2 - y1 ) / ( x2 - x1 ) ) / ( x3 - x2 )
#
#  Evaluate.
#
  y = y1 + ( x - x1 ) * dif1 + ( x - x1 ) * ( x - x2 ) * dif2
  yp = dif1 + ( 2.0 * x - x1 - x2 ) * dif2
  ypp = 2.0 * dif2

  return y, yp, ypp

def r8poly2_val_test ( ):

#*****************************************************************************80
#
## r8poly2_val_test() tests r8poly2_val().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8poly2_val_test():' )
  print ( '  r8poly2_val() evaluates a parabola given' )
  print ( '  3 data points.' )
  print ( '' )
  print ( '  Our parabola will be 2*x^2 + 3 * x + 1.' )
  print ( '' )
  print ( '  Case 1: 3 distinct data points:' )
  print ( '' )

  x1 = -1.0
  x2 = 1.0
  x3 = 3.0

  y1, yp, ypp = r8poly2_val_f ( x1 )
  y2, yp, ypp = r8poly2_val_f ( x2 )
  y3, yp, ypp = r8poly2_val_f ( x3 )

  print ( '  %12f  %12f' % ( x1, y1 ) )
  print ( '  %12f  %12f' % ( x2, y2 ) )
  print ( '  %12f  %12f' % ( x3, y3 ) )

  print ( '' )
  print ( '  Sampled data:' )
  print ( '' )
  print ( '  X, Y, Y'', Y"' )
  print ( '' )
  for i in range ( 0, 4 ):
    x = i
    y, yp, ypp = r8poly2_val ( x1, y1, x2, y2, x3, y3, x )
    print ( '  %12f  %12f  %12f  %12f' % ( x, y, yp, ypp ) )

  print ( '' )
  print ( '  Case 2: X1=X2, X3 distinct:' )
  print ( '' )

  x1 = -1.0
  x2 = -1.0
  x3 = 3.0

  y1, y2, ypp = r8poly2_val_f ( x1 )
  y3, yp, ypp = r8poly2_val_f ( x3 )
  print ( '  %12f  %12f' % ( x1, y1 ) )
  print ( '  %12f  %12f' % ( x2, y2 ) )
  print ( '  %12f  %12f' % ( x3, y3 ) )

  print ( '' )
  print ( '  Sampled data:' )
  print ( '' )
  print ( '  X, Y, Y'', Y"' )
  print ( '' )
  for i in range ( 0, 4 ):
    x = i
    y, yp, ypp = r8poly2_val ( x1, y1, x2, y2, x3, y3, x )
    print ( '  %12f  %12f  %12f  %12f' % ( x, y, yp, ypp ) )

  print ( '' )
  print ( '  Case 3: X1=X2=X3:' )
  print ( '' )

  x1 = -1.0
  x2 = -1.0
  x3 = -1.0

  y1, y2, y3 = r8poly2_val_f ( x1 )

  print ( '  %12f  %12f' % ( x1, y1 ) )
  print ( '  %12f  %12f' % ( x2, y2 ) )
  print ( '  %12f  %12f' % ( x3, y3 ) )

  print ( '' )
  print ( '  Sampled data:' )
  print ( '' )
  print ( '  X, Y, Y'', Y"' )
  print ( '' )
  for i in range ( 0, 4 ):
    x = i
    y, yp, ypp = r8poly2_val ( x1, y1, x2, y2, x3, y3, x )
    print ( '  %12f  %12f  %12f  %12f' % ( x, y, yp, ypp ) )

  return

def r8poly2_val_f ( x ):

#*****************************************************************************80
#
## r8poly2_val_f() evaluates a parabola for us.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument.
#
#  Output:
#
#    real Y, YP, YPP, the value, and first and second derivatives.
#
  y = 2.0 * x * x + 3.0 * x + 1.0
  yp = 4.0 * x + 3.0
  ypp = 4.0

  return y, yp, ypp

def r8poly3_discriminant ( a, b, c, d ):

#*****************************************************************************80
#
## r8poly3_discriminant() returns the discriminant of a cubic polynomial.
#
#  Discussion:
#
#    The polynomial has the form
#
#      A * X^3 + B * X^2 + C * X + D = 0
#
#    If the discriminant is zero, then the polynomial has a multiple root.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    When a cubic or quartic has a double root,
#    https://www.johndcook.com/blog/2022/11/16/cubic-quartic-double-root/
#    Posted 16 November 2022.
#
#  Input:
#
#    real A, B, C, D, the coefficients of the polynomial.
#    A must not be zero.
#
#  Output:
#
#    real VALUE, the discriminant.
#
  value = \
    18.0 * a    * b    * c    * d   \
   - 4.0        * b**3        * d   \
   +              b**2 * c**2       \
   - 4.0 * a           * c**3       \
  - 27.0 * a**2               * d**2

  return value

def r8poly3_root ( a, b, c, d ):

#*****************************************************************************80
#
## r8poly3_root() returns the three roots of a cubic polynomial.
#
#  Discussion:
#
#    The polynomial has the form
#
#      A * X^3 + B * X^2 + C * X + D = 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, D, the coefficients of the polynomial.
#    A must not be zero.
#
#  Output:
#
#    complex R1, R2, R3, the roots of the polynomial, which
#    will include at least one real root.
#
  import numpy as np
 
  if ( a == 0.0 ):
    print ( '' )
    print ( 'r8poly3_root(): Fatal error!' )
    print ( '  A must not be zero!' )
    raise Exception ( 'r8poly3_root(): Fatal error!' )

  q = ( ( b / a ) ** 2 - 3.0 * ( c / a ) ) / 9.0

  r = ( 2.0 * ( b / a ) ** 3 - 9.0 * ( b / a ) * ( c / a ) \
      + 27.0 * ( d / a ) ) / 54.0

  if ( r * r < q * q * q ):

    theta = np.arccos ( r / np.sqrt ( q ** 3 ) )
    r1 = -2.0 * np.sqrt ( q ) * np.cos (   theta                 / 3.0 )
    r2 = -2.0 * np.sqrt ( q ) * np.cos ( ( theta + 2.0 * np.pi ) / 3.0 )
    r3 = -2.0 * np.sqrt ( q ) * np.cos ( ( theta + 4.0 * np.pi ) / 3.0 )

  elif ( q * q * q <= r * r ):

    temp = -r + np.sqrt ( r ** 2 - q ** 3 )
    s1 = r8_sign ( temp ) * ( abs ( temp ) ) ** ( 1.0 / 3.0 )

    temp = -r - np.sqrt ( r ** 2 - q ** 3 )
    s2 = r8_sign ( temp ) * ( abs ( temp ) ) ** ( 1.0 / 3.0 )

    r1 = s1 + s2
    r2 = -0.5 * ( s1 + s2 ) + 0.5j * np.sqrt ( 3.0 ) * ( s1 - s2 )
    r3 = -0.5 * ( s1 + s2 ) - 0.5j * np.sqrt ( 3.0 ) * ( s1 - s2 )

  r1 = r1 - b / ( 3.0 * a )
  r2 = r2 - b / ( 3.0 * a )
  r3 = r3 - b / ( 3.0 * a )

  return r1, r2, r3

def r8poly3_root_test ( ):

#*****************************************************************************80
#
## r8poly3_root_test() tests r8poly3_root().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 4

  a_test = np.array ( [ 1.0, 9.0, 1.0, 1.0 ] )
  b_test = np.array ( [ -6.0, -36.0, -5.0, -8.0  ] )
  c_test = np.array ( [ 11.0, 54.0, 8.0, 25.0  ] )
  d_test = np.array ( [ -6.0, -27.0, -4.0, -26.0  ] )
#
#  1: Three distinct real roots, 1, 2, 3.
#  2: One repeated real root, 1.5, 1.5, 1.5.
#  3: Two real roots, one repeated, 1, 2, 2.
#  4: One real root, a complex conjugate pair, 2, 3+2I, 3-2I.
#
  print ( '' )
  print ( 'r8poly3_root_test' )
  print ( '  r8poly3_root finds roots of cubic equations.' )
  print ( '  r8poly3_discriminant() returns the discriminant.' )
 
  for test in range ( 0, test_num ):
 
    a = a_test[test]
    b = b_test[test]
    c = c_test[test]
    d = d_test[test]

    print ( '' )
    print ( '  Polynomial coefficients:' )
    print ( '' )
    print ( '  A = %f, B = %f, C = %f, D = %f' % ( a, b, c, d ) )
 
    r1, r2, r3 = r8poly3_root ( a, b, c, d )
 
    print ( '' )
    print ( '  Roots:' )
    print ( '' )
    print ( '  %f  %f' % ( r1.real, r1.imag ) )
    print ( '  %f  %f' % ( r2.real, r2.imag ) )
    print ( '  %f  %f' % ( r3.real, r3.imag ) )

    discr = r8poly3_discriminant ( a, b, c, d )
    print ( '' )
    print ( '  Discriminant = ', discr )

  return

def r8poly4_discriminant ( a, b, c, d, e ):

#*****************************************************************************80
#
## r8poly4_discriminant() returns the discriminant of a quartic polynomial.
#
#  Discussion:
#
#    The polynomial has the form
#
#      a * x^4 + b * x^3 + c * x^2 + d * x + e = 0
#
#    If the discriminant is negative, then the polynomial has two distinct
#    real roots and two distinct complex conjugate roots.
#
#    If the discriminant is positive, then all four roots are real, 
#    or all four roots are strictly complex.
#
#    If the discriminant is positive, let P=8*a*c-3*b^2
#    and D = 64*a^3*e - 16*a^2*c^2 + 16*a*b^2*c - 16*a^2*b*d - 3*b^4.
#    If P<0 and D<0, then all four roots are real and distinct.
#    If P>0 or D>0, there are two pairs of non-real complex conjugate roots
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John D Cook,
#    When a cubic or quartic has a double root,
#    https://www.johndcook.com/blog/2022/11/16/cubic-quartic-double-root/
#    Posted 16 November 2022.
#
#  Input:
#
#    real A, B, C, D, E: the coefficients of the polynomial.
#    A must not be zero.
#
#  Output:
#
#    real disc: the discriminant.
#
#    real p, r, d0, d1: additional discriminant information.
#
  value = \
                   b**2 * c**2 * d**2 \
    -   4 * a           * c**3 * d**2 \
    -   4        * b**3        * d**3 \
    +  18 * a    * b    * c    * d**3 \
    -  27 * a**2               * d**4 \
    -   4        * b**2 * c**3        * e \
    +  16 * a           * c**4        * e \
    +  18        * b**3 * c    * d    * e \
    -  80 * a    * b    * c**2 * d    * e \
    -   6 * a    * b**2        * d**2 * e \
    + 144 * a**2        * c    * d**2 * e \
    -  27        * b**4               * e**2 \
    + 144 * a    * b**2 * c           * e**2 \
    - 128 * a**2        * c**2        * e**2 \
    - 192 * a**2 * b           * d    * e**2 \
    + 256 * a**3                      * e**3

  p = 8.0 * a * c - 3.0 * b**2
  r = b**3 + 8.0 * d * a**2 - 4.0 * a * b * c
  d0 = c**2 - 3.0 * b * d + 12.0 * a * e
  d1 = \
      64.0 * a**3 * e \
    - 16.0 * a**2 * c**2 \
    + 16.0 * a   * b**2 * c \
    - 16.0 * a**2 * b * d \
    - 3.0 * b**4

  return value, p, r, d0, d1

def r8poly4_root ( a, b, c, d, e ):

#*****************************************************************************80
#
## r8poly4_root() returns the four roots of a quartic polynomial.
#
#  Discussion:
#
#    The polynomial has the form:
#
#      A * X^4 + B * X^3 + C * X^2 + D * X + E = 0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, C, D, the coefficients of the polynomial.
#    A must not be zero.
#
#  Output:
#
#    complex R1, R2, R3, R4, the roots of the polynomial.
#
  import numpy as np

  if ( a == 0.0 ):
    print ( '' )
    print ( 'r8poly4_root(): Fatal error!' )
    print ( '  A must not be zero!' )
    raise Exception ( 'r8poly4_root(): Fatal error!' )

  a4 = b / a
  b4 = c / a
  c4 = d / a
  d4 = e / a
#
#  Set the coefficients of the resolvent cubic equation.
#
  a3 = 1.0
  b3 = - b4
  c3 = a4 * c4 - 4.0 * d4
  d3 = - a4 * a4 * d4 + 4.0 * b4 * d4 - c4 * c4
#
#  Find the (complex) roots of the resolvent cubic.
#
  r1, r2, r3 = r8poly3_root ( a3, b3, c3, d3 )
#
#  Choose one root of the cubic, here R1.
#
#  Set R = sqrt ( 0.25 * A4^2 - B4 + R1 )
#
  r = np.sqrt ( 0.25 * a4 ** 2 - b4  + r1 + 0j )

  if ( r != 0.0 ):

    p = np.sqrt ( 0.75 * a4 ** 2 - r ** 2 - 2.0 * b4 \
        + 0.25 * ( 4.0 * a4 * b4 - 8.0 * c4 - a4 ** 3 ) / r )

    q = np.sqrt ( 0.75 * a4 ** 2 - r ** 2 - 2.0 * b4 \
        - 0.25 * ( 4.0 * a4 * b4 - 8.0 * c4 - a4 ** 3 ) / r )

  else:

    p = np.sqrt ( 0.75 * a4 ** 2 - 2.0 * b4 + 2.0 * np.sqrt ( r1 ** 2 - 4.0 * d4 ) )
    q = np.sqrt ( 0.75 * a4 ** 2 - 2.0 * b4 - 2.0 * np.sqrt ( r1 ** 2 - 4.0 * d4 ) )
#
#  Set the roots.
#
  r1 = -0.25 * a4 + 0.5 * r + 0.5 * p
  r2 = -0.25 * a4 + 0.5 * r - 0.5 * p
  r3 = -0.25 * a4 - 0.5 * r + 0.5 * q
  r4 = -0.25 * a4 - 0.5 * r - 0.5 * q

  return r1, r2, r3, r4

def r8poly4_root_test ( ):

#*****************************************************************************80
#
## r8poly4_root_test() tests r8poly4_root().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 7

  a_test = np.array ( [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ] )
  b_test = np.array ( [ -10.0, -5.0, -22.0, -16.0, -20.0, 2.0, 0.0 ] )
  c_test = np.array ( [ 35.0, 1.0, 141.0, 72.0, 150.0, 1.0, 13.0 ] )
  d_test = np.array ( [ -50.0, 21.0, -220.0, -128.0, -500.0, 8.0, 0.0 ] )
  e_test = np.array ( [ 24.0, -18.0, +100.0, 80.0, 625.0, -12.0, 36.0 ] )
#
#  1: Four distinct real roots, 1, 2, 3, 4.
#  2: Three distinct real roots, 1, -2, 3, 3
#  3: Two distinct real roots, 1, 1, 10, 10.
#  4: Two distinct real roots, 2, 2, 2, 10
#  5: One real root, 5, 5, 5, 5
#  6: Two distinct real roots, one complex conjugate pair.
#  7: Two distinct complex conjugate pairs.
#
  print ( '' )
  print ( 'r8poly4_root_test():' )
  print ( '  r8poly4_root() finds roots of quartic equations.' )
  print ( '  r8poly4_discriminant() returns the discriminant.' )

  for test in range ( 0, test_num ):
 
    a = a_test[test]
    b = b_test[test]
    c = c_test[test]
    d = d_test[test]
    e = e_test[test]

    print ( '' )
    print ( '  A = %f' % ( a ) )
    print ( '  B = %f' % ( b ) )
    print ( '  C = %f' % ( c ) )
    print ( '  D = %f' % ( d ) )
    print ( '  E = %f' % ( e ) )

    r1, r2, r3, r4 = r8poly4_root ( a, b, c, d, e )

    print ( '' )
    print ( '  Roots:' )
    print ( '' )
    print ( '  %f  %f'% ( r1.real, r1.imag ) )
    print ( '  %f  %f'% ( r2.real, r2.imag ) )
    print ( '  %f  %f'% ( r3.real, r3.imag ) )
    print ( '  %f  %f'% ( r4.real, r4.imag ) )

    discr, p, r, d0, d1 = r8poly4_discriminant ( a, b, c, d, e )

    print ( '' )
    print ( '  Discriminant = ', discr )
    print ( '  P = ', p )
    print ( '  R = ', r )
    print ( '  D0 = ', d0 )
    print ( '  D1 = ', d1 )

  return

def r8poly_add ( na, a, nb, b ):

#*****************************************************************************80
#
## r8poly_add() adds two R8POLY's.
#
#  Discussion:
#
#    The polynomials are in power sum form.
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1)*x + ... + a(n-1)*x^(n-1) + a(n)*x^(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NA, the degree of polynomial A.
#
#    real A(1:NA+1), the coefficients of the first
#    polynomial factor.
#
#    integer NB, the degree of polynomial B.
#
#    real B(1:NB+1), the coefficients of the
#    second polynomial factor.
#
#  Output:
#
#    real C(1:max(NA,NB)+1), the coefficients of A + B.
#
  import numpy as np

  nc = max ( na, nb )

  c = np.zeros ( nc + 1 )

  for i in range ( 0, na + 1 ):
    c[i] = c[i] + a[i]

  for i in range ( 0, nb + 1 ):
    c[i] = c[i] + b[i]

  return c

def r8poly_add_test ( ):

#*****************************************************************************80
#
## r8poly_add_test() tests r8poly_add().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8poly_add_test()' )
  print ( '  r8poly_add() adds two R8POLY\'s.' )

  na = 5
  a = np.array ( [ 0.0,  1.1, 2.2, 3.3, 4.4,  5.5 ] )
  nb = 5
  b = np.array ( [ 1.0, -2.1, 7.2, 8.3, 0.0, -5.5 ] )

  c = r8poly_add ( na, a, nb, b )

  r8poly_print ( a, '  Polynomial A:' )

  r8poly_print ( b, '  Polynomial B:' )

  nc = max ( na, nb )

  r8poly_print ( c, '  Polynomial C = A+B:' )

  return

def r8poly_ant_coef ( n, poly_cof ):

#*****************************************************************************80
#
## r8poly_ant_coef() integrates a polynomial in standard form.
#
#  Discussion:
#
#    The antiderivative of a polynomial P(X) is any polynomial Q(X)
#    with the property that d/dX Q(X) = P(X).
#
#    This routine chooses the antiderivative whose constant term is zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#    real POLY_COF(1:N+1), the polynomial coefficients.
#    POLY_COF(1) is the constant term, and POLY_COF(N+1) is the
#    coefficient of X^(N).
#
#  Output:
#
#    real POLY_COF2(1:N+2), the coefficients of
#    the antiderivative polynomial, in standard form.  The constant
#    term is set to zero.
#
  import numpy as np

  poly_cof2 = np.zeros ( n + 2 )
#
#  Set the constant term.
#
  poly_cof2[0] = 0.0
#
#  Integrate the polynomial.
#
  for i in range ( 1, n + 2 ):
    poly_cof2[i] = poly_cof[i-1] / float ( i )

  return poly_cof2

def r8poly_ant_coef_test ( ):

#*****************************************************************************80
#
## r8poly_ant_coef_test() tests r8poly_ant_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 October 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r8poly_ant_coef_test():' )
  print ( '  r8poly_ant_coef() computes the coefficients of the' )
  print ( '  antiderivative of a polynomial' )

  poly_cof = np.zeros ( n + 1 )
  for i in range ( 0, n + 1 ):
    poly_cof[i] = float ( n + 1 - i )

  r8poly_print ( poly_cof, '  Polynomial p(x):' )

  poly_cof2 = r8poly_ant_coef ( n, poly_cof )

  r8poly_print ( poly_cof2, '  Antideriv(p(x)):' )

  return

def r8poly_ant_value ( n, poly_cof, xval ):

#*****************************************************************************80
#
## r8poly_ant_value() evaluates evaluates the antiderivative of a polynomial.
#
#  Discussion:
#
#    The constant term of the antiderivative is taken to be zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2019
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n, the order of the polynomial.
#
#    real poly_cof(0:n), the polynomial coefficients.  
#    poly_cof(I) is the coefficient of X^I.
#
#    real xval, the evaluation point.
#
#  Output:
#
#    real yval, the polynomial value.
#
  yval = 0.0
  for i in range ( n, -1, -1 ):
    yval = ( yval + poly_cof[i] / float ( i + 1 ) ) * xval

  return yval

def r8poly_ant_value_test ( ):

#*****************************************************************************80
#
## r8poly_ant_value_test() tests r8poly_ant_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 October 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4;
  n = 16;
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )

  print ( '' )
  print ( 'r8poly_ant_value_test()' )
  print ( '  r8poly_ant_value() evaluates the antiderivative of a polynomial at a point' )
  print ( '  using a naive method.' )

  r8poly_print ( c, '  The polynomial coefficients:' )

  x_lo = 0.0
  x_hi = 5.0
  x = np.linspace ( x_lo, x_hi, n )

  print ( '' )
  print ( '   I    X    antiP(X)' )
  print ( '' )

  for i in range ( 0, n ):
    p = r8poly_ant_value ( m, c, x[i] )
    print ( '  %2d  %8.4f  %14.6g' % ( i, x[i], p ) )

  return

def r8poly_degree ( m, a ):

#*****************************************************************************80
#
## r8poly_degree() returns the degree of a polynomial.
#
#  Discussion:
#
#    The degree of a polynomial is the index of the highest power
#    of X with a nonzero coefficient.
#
#    The degree of a constant polynomial is 0.  The degree of the
#    zero polynomial is debatable, but this routine returns the
#    degree as 0.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the nominal degree of A.
#
#    real A(M+1), the coefficients of the polynomials.
#
#  Output:
#
#    integer VALUE, the degree of A.
#
  value = m

  while ( 0 < value ):
    if ( a[value] != 0.0 ):
      break
    value = value - 1

  return value

def r8poly_degree_test ( ):

#*****************************************************************************80
#
## r8poly_degree_test() tests r8poly_degree().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  c1 = np.array ( [ 1.0, 2.0, 3.0, 4.0 ] )
  c2 = np.array ( [ 1.0, 2.0, 3.0, 0.0 ] )
  c3 = np.array ( [ 1.0, 2.0, 0.0, 4.0 ] )
  c4 = np.array ( [ 1.0, 0.0, 0.0, 0.0 ] )
  c5 = np.array ( [ 0.0, 0.0, 0.0, 0.0 ] )

  print ( '' )
  print ( 'r8poly_degree_test()' )
  print ( '  r8poly_degree() determines the degree of an R8POLY.' )

  m = 3

  r8poly_print ( c1, '  The R8POLY:' )
  d = r8poly_degree ( m, c1 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  r8poly_print ( c2, '  The R8POLY:' )
  d = r8poly_degree ( m, c2 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  r8poly_print ( c3, '  The R8POLY:' )
  d = r8poly_degree ( m, c3 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  r8poly_print ( c4, '  The R8POLY:' )
  d = r8poly_degree ( m, c4 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  r8poly_print ( c5, '  The R8POLY:' )
  d = r8poly_degree ( m, c5 )
  print ( '  Dimensioned degree = %d,  Actual degree = %d' % ( m, d ) )

  return

def r8poly_deriv ( n, c, p ):

#*****************************************************************************80
#
## r8poly_deriv() returns the derivative of a polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the degree of the polynomial.
#
#    real C(1:N+1), the polynomial coefficients.
#    C(I+1) is the coefficient of X**I.
#
#    integer P, the order of the derivative.
#    0 means no derivative is taken.
#    1 means first derivative,
#    2 means second derivative and so on.
#    Values of P less than 0 are meaningless.  Values of P greater
#    than N are meaningful, but the code will behave as though the
#    value of P was N.
#
#  Output:
#
#    real CP(1:N+1-P), the polynomial coefficients of
#    the derivative.
#
  import numpy as np

  if ( n <= p ):
    cp = np.zeros ( 1 )
    return cp

  cp_temp = c.copy ( )

  for d in range ( 1, p + 1 ):
    for i in range ( 0, n + 1 - d ):
      cp_temp[i] = float ( i + 1 ) * cp_temp[i+1]
    cp_temp[n-d+1] = 0.0

  cp = cp_temp[0:n+1-p].copy ( )

  return cp

def r8poly_deriv_test ( ):

#*****************************************************************************80
#
## r8poly_deriv_test() tests r8poly_deriv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2017
#
#  Author:
#
#    John Burkardt
#
  n = 4

  print ( '' )
  print ( 'r8poly_deriv_test():' )
  print ( '  r8poly_deriv() computes the coefficients of' )
  print ( '  the derivative of a polynomial.' )

  x = r8vec_indicator1 ( n )

  c = roots_to_r8poly ( n, x )

  r8poly_print ( c, '  The initial polynomial' )

  for d in range ( 0, n + 1 ):
    cp = r8poly_deriv ( n, c, d )
    label = '  The derivative of order %d' % ( d )
    r8poly_print ( cp, label )

  return

def r8poly_division ( na, a, nb, b ):

#*****************************************************************************80
#
## r8poly_division() computes the quotient and remainder of two polynomials.
#
#  Discussion:
#
#    The polynomials are assumed to be stored in power sum form.
#
#    The power sum form of a polynomial is:
#
#      p(x) = a(0) + a(1) * x + ... + a(n-1) * x^(n-1) + a(n) * x^(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    30 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NA, the dimension of A.
#
#    real A(1:NA+1), the coefficients of the polynomial to be divided.
#
#    integer NB, the dimension of B.
#
#    real B(1:NB+1), the coefficients of the divisor polynomial.
#
#  Output:
#
#    integer NQ, the degree of Q.
#    If the divisor polynomial is zero, NQ is returned as -1.
#
#    real Q(1:NA-NB+1), contains the quotient of A/B.
#    If A and B have full degree, Q should be dimensioned Q(0:NA-NB).
#    In any case, Q(0:NA) should be enough.
#
#    integer NR, the degree of R.
#    If the divisor polynomial is zero, NR is returned as -1.
#
#    real R(1:NB), contains the remainder of A/B.
#    If B has full degree, R should be dimensioned R(0:NB-1).
#    Otherwise, R will actually require less space.
#
  import numpy as np

  na2 = r8poly_degree ( na, a )
  nb2 = r8poly_degree ( nb, b )

  if ( b[nb2] == 0.0 ):
    nq = -1
    q = np.zeros ( 0 )
    nr = -1
    r = np.zeros ( 0 )
    return nq, q, nr, r

  a2 = np.zeros ( na + 1 )
  for i in range ( 0, na + 1 ):
    a2[i] = a[i]

  nq = na2 - nb2
  q = np.zeros ( nq + 1 )

  for i in range ( nq, -1, -1 ):
    q[i] = a2[i+nb2] / b[nb2]
    a2[i+nb2] = 0.0
    for j in range ( 0, nb2 ):
      a2[i+j] = a2[i+j] - q[i] * b[j]

  nr = nb2 - 1
  r = np.zeros ( nr + 1 )
  for i in range ( 0, nr + 1 ):
    r[i] = a2[i]

  return nq, q, nr, r

def r8poly_division_test ( ):

#*****************************************************************************80
#
## r8poly_division_test() tests r8poly_division().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8poly_division_test():' )
  print ( '  r8poly_division() computes the quotient and' )
  print ( '  remainder for polynomial division.' )
#
#  1: Divide X^3 + 2*X^2 - 5*X - 6  by X-2.  
#     Quotient is 3+4*X+X^2, remainder is 0.
#
#  2: Divide X^4 + 3*X^3 + 2*X^2 - 2  by  X^2 + X - 3.
#     Quotient is X^2 + 2*X + 3, remainder 8*X + 7.
#
#  3: Divide X^3 - 2*X^2 + 0*X - 4  by  X - 3.
#     Quotient is X^2 + X + 3, remainder 5.
#
  ntest = 3
  
  for test in range ( 0,  ntest ):

    if ( test == 0 ):
      na = 3
      a = np.array ( [ -6.0, -5.0, 2.0, 1.0 ] )
      nb = 1
      b = np.array ( [ -2.0, 1.0 ] )
    elif ( test == 1 ):
      na = 4
      a = np.array ( [ -2.0, 5.0, 2.0, 3.0, 1.0 ] )
      nb = 2
      b = np.array ( [ -3.0, 1.0, 1.0 ] )
    elif ( test == 2 ):
      na = 3
      a = np.array ( [ -4.0, 0.0, -2.0, 1.0 ] )
      nb = 1
      b = np.array ( [ -3.0, 1.0 ] )

    r8poly_print ( a, '  The polynomial to be divided, A:' )
    r8poly_print ( b, '  The divisor polynomial, B:' )

    nq, q, nr, r = r8poly_division ( na, a, nb, b )
 
    r8poly_print ( q, '  The quotient polynomial, Q:' )
    r8poly_print ( r, '  The remainder polynomial, R:' )

  return

def r8poly_lagrange_0 ( npol, xpol, xval ):

#*****************************************************************************80
#
## r8poly_lagrange_0() evaluates the Lagrange factor at a point.
#
#  Formula:
#
#    W(X) = Product ( 1 <= I <= NPOL ) ( X - XPOL(I) )
#
#  Discussion:
#
#    For a set of points XPOL(I), 1 <= I <= NPOL, the IPOL-th Lagrange basis
#    polynomial L(IPOL)(X), has the property:
#
#      L(IPOL)( XPOL(J) ) = delta ( IPOL, J )
#
#    and may be expressed as:
#
#      L(IPOL)(X) = W(X) / ( ( X - XPOL(IPOL) ) * W'(XPOL(IPOL)) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPOL, the number of abscissas.
#    NPOL must be at least 1.
#
#    real XPOL(NPOL), the abscissas, which should be distinct.
#
#    real XVAL, the point at which the Lagrange factor is to be
#    evaluated.
#
#  Output:
#
#    real WVAL, the value of the Lagrange factor at XVAL.
#
  import numpy as np

  wval = np.prod ( xval - xpol[:] )

  return wval

def r8poly_lagrange_0_test ( ):

#*****************************************************************************80
#
## r8poly_lagrange_0_test() tests r8poly_lagrange_0().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
  npol = 5

  print ( '' )
  print ( 'r8poly_lagrange_0_test():' )
  print ( '  r8poly_lagrange_0() evaluates the Lagrange' )
  print ( '  factor W(X) at a point.' )
  print ( '' )
  print ( '  The number of data points is %d' % ( npol ) )
#
#  Set the abscissas of the polynomials.
#
  xlo = 0.0
  xhi = npol - 1

  xpol = r8vec_even ( npol, xlo, xhi )

  r8vec_print ( npol, xpol, '  Abscissas:' )
#
#  Evaluate W(X).
#
  print ( '' )
  print ( '      X          W(X)' )
  print ( '' )

  nx = 4 * npol - 1

  for ival in range ( 1, nx + 1 ):

    xval = r8vec_even_select ( nx, xlo, xhi, ival )

    w = r8poly_lagrange_0 ( npol, xpol, xval )

    print ( '%12f  %12e' % ( xval, w ) )

  return

def r8poly_lagrange_1 ( npol, xpol, xval ):

#*****************************************************************************80
#
## r8poly_lagrange_1() evaluates the first derivative of the Lagrange factor.
#
#  Formula:
#
#    W(XPOL(1:NPOL))(X) = Product ( 1 <= I <= NPOL ) ( X - XPOL(I) )
#
#    W'(XPOL(1:NPOL))(X)
#      = Sum ( 1 <= J <= NPOL ) Product ( I /= J ) ( X - XPOL(I) )
#
#    We also have the recursion:
#
#      W'(XPOL(1:NPOL))(X) = d/dX ( ( X - XPOL(NPOL) ) * W(XPOL(1:NPOL-1))(X) )
#                    = W(XPOL(1:NPOL-1))(X)
#                    + ( X - XPOL(NPOL) ) * W'(XPOL(1:NPOL-1))(X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPOL, the number of abscissas.
#
#    real XPOL(NPOL), the abscissas, which should be distinct.
#
#    real XVAL, the point at which the Lagrange factor is to be
#    evaluated.
#
#  Output:
#
#    real DWDX, the derivative of W with respect to XVAL.
#
  dwdx = 0.0
  w = 1.0

  for i in range ( 0, npol ):

    dwdx = w + ( xval - xpol[i] ) * dwdx
    w = w * ( xval - xpol[i] )

  return dwdx

def r8poly_lagrange_1_test ( ):

#*****************************************************************************80
#
## r8poly_lagrange_1_test() tests r8poly_lagrange_1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2018
#
#  Author:
#
#    John Burkardt
#
  npol = 5

  print ( '' )
  print ( 'r8poly_lagrange_1_test():' )
  print ( '  r8poly_lagrange_1() evaluates the Lagrange' )
  print ( '  factor W\'(X) at a point.' )
  print ( '' )
  print ( '  The number of data points is %d' % ( npol ) )
#
#  Set the abscissas of the polynomials.
#
  xlo = 0.0
  xhi = npol - 1

  xpol = r8vec_even ( npol, xlo, xhi )

  r8vec_print ( npol, xpol, '  Abscissas:' )

  print ( '' )
  print ( '      X          W''(X)' )
  print ( '' )

  nx = 4 * npol - 1

  for ival in range ( 1, nx + 1 ):

    xval = r8vec_even_select ( nx, xlo, xhi, ival )

    dwdx = r8poly_lagrange_1 ( npol, xpol, xval )

    print ( '  %12f  %12f' % ( xval, dwdx ) )

  return

def r8poly_lagrange_2 ( npol, xpol, xval ):

#*****************************************************************************80
#
## r8poly_lagrange_2() evaluates the second derivative of the Lagrange factor.
#
#  Formula:
#
#    W(X)  = Product ( 1 <= I <= NPOL ) ( X - XPOL(I) )
#
#    W'(X) = Sum ( 1 <= J <= NPOL )
#            Product ( I /= J ) ( X - XPOL(I) )
#
#    W"(X) = Sum ( 1 <= K <= NPOL )
#            Sum ( J =/ K )
#            Product ( I /= K, J ) ( X - XPOL(I) )
#
#    For a set of points XPOL(I), 1 <= I <= NPOL, the IPOL-th Lagrange basis
#    polynomial L(IPOL)(X), has the property:
#
#      L(IPOL)( XPOL(J) ) = delta ( IPOL, J )
#
#    and may be expressed as:
#
#      L(IPOL)(X) = W(X) / ( ( X - XPOL(IPOL) ) * W'(XPOL(IPOL)) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPOL, the number of abscissas.
#    NPOL must be at least 1.
#
#    real XPOL(NPOL), the abscissas, which should be distinct.
#
#    real XVAL, the point at which the Lagrange factor is to be
#    evaluated.
#
#  Output:
#
#    real DW2DX2, the second derivative of W with respect to XVAL.
#
  dw2dx2 = 0.0

  for k in range ( 0, npol ):

    for j in range ( 0, npol ):

      if ( j != k ):
        term = 1.0

        for i in range ( 0, npol ):
          if ( i != j and i != k ):
            term = term * ( xval - xpol[i] )

        dw2dx2 = dw2dx2 + term

  return dw2dx2

def r8poly_lagrange_2_test ( ):

#*****************************************************************************80
#
## r8poly_lagrange_2_test() tests r8poly_lagrange_2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  npol = 5

  print ( '' )
  print ( 'r8poly_lagrange_2_test():' )
  print ( '  r8poly_lagrange_2() evaluates the Lagrange' )
  print ( '  factor W"(X) at a point.' )
  print ( '' )
  print ( '  The number of data points is %d' % ( npol ) )
#
#  Set the abscissas of the polynomials.
#
  xlo = 0.0
  xhi = npol - 1

  xpol = r8vec_even ( npol, xlo, xhi )

  r8vec_print ( npol, xpol, '  Abscissas:' )

  print ( '' )
  print ( '      X          W"(X)' )
  print ( '' )

  nx = 4 * npol - 1

  for ival in range ( 1, nx + 1 ):

    xval = r8vec_even_select ( nx, xlo, xhi, ival )
    dw2dx2 = r8poly_lagrange_2 ( npol, xpol, xval )

    print ( ' %12f  %12e' % ( xval, dw2dx2 ) )

  return

def r8poly_lagrange_coef ( npol, ipol, xpol ):

#*****************************************************************************80
#
## r8poly_lagrange_coef() returns the coefficients of a Lagrange polynomial.
#
#  Discussion:
#
#    Given distinct abscissas XPOL(1:NPOL), the IPOL-th Lagrange
#    polynomial L(IPOL)(X) is defined as the polynomial of degree
#    NPOL - 1 which is 1 at XPOL(IPOL) and 0 at the NPOL - 1 other
#    abscissas.
#
#    A formal representation is:
#
#      L(IPOL)(X) = Product ( 1 <= I <= NPOL, I /= IPOL )
#       ( X - X(I) ) / ( X(IPOL) - X(I) )
#
#    However sometimes it is desirable to be able to write down
#    the standard polynomial coefficients of L(IPOL)(X).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPOL, the number of abscissas.
#    NPOL must be at least 1.
#
#    integer IPOL, the index of the polynomial to evaluate.
#    IPOL must be between 1 and NPOL.
#
#    real XPOL(NPOL), the abscissas of the
#    Lagrange polynomials.  The entries in XPOL must be distinct.
#
#  Output:
#
#    real PCOF(1:NPOL), the standard polynomial
#    coefficients of the IPOL-th Lagrange polynomial:
#      L(IPOL)(X) = SUM ( 0 <= I <= NPOL-1 ) PCOF(I+1) * X^I
#
  import numpy as np
#
#  Make sure IPOL is legal.
#
  if ( ipol < 1 or npol < ipol ):
    print ( '' )
    print ( 'r8poly_lagrange_coef(): Fatal error!' )
    print ( '  1 <= IPOL <= NPOL is required.' )
    raise Exception ( 'r8poly_lagrange_coef(): Fatal error!' )
#
#  Check that the abscissas are distinct.
#
  if ( not r8vec_is_distinct ( npol, xpol ) ):
    print ( '' )
    print ( 'r8poly_lagrange_coef(): Fatal error!' )
    print ( '  Two or more entries of XPOL are equal:' )
    raise Exception ( 'r8poly_lagrange_coef(): Fatal error!' )

  pcof = np.zeros ( npol )

  pcof[0] = 1.0

  indx = 0

  for i in range ( 1, npol + 1 ):

    if ( i != ipol ):

      indx = indx + 1

      for j in range ( indx, -1, -1 ):

        pcof[j] = - xpol[i-1] * pcof[j] / ( xpol[ipol-1] - xpol[i-1] )

        if ( 0 < j ):
          pcof[j] = pcof[j] + pcof[j-1] / ( xpol[ipol-1] - xpol[i-1] )

  return pcof

def r8poly_lagrange_coef_test ( ):

#*****************************************************************************80
#
## r8poly_lagrange_coef_test() tests r8poly_lagrange_coef().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
  npol = 5

  print ( '' )
  print ( 'r8poly_lagrange_coef_test():' )
  print ( '  r8poly_lagrange_coef() returns the coefficients' )
  print ( '  for a Lagrange basis polynomial.' )

  xpol = r8vec_indicator1 ( npol )

  r8vec_print ( npol, xpol, '  Abscissas:' )

  for ipol in range ( 1, npol + 1 ):

    pcof = r8poly_lagrange_coef ( npol, ipol, xpol )

    r8poly_print ( pcof, '  The Lagrange basis polynomial:' )

  return

def r8poly_lagrange_factor ( npol, xpol, xval ):

#*****************************************************************************80
#
## r8poly_lagrange_factor() evaluates the polynomial Lagrange factor at a point.
#
#  Formula:
#
#    W(X) = Product ( 1 <= I <= NPOL ) ( X - XPOL(I) )
#
#  Discussion:
#
#    Suppose F(X) is at least N times continuously differentiable in the
#    interval [A,B].  Pick NPOL distinct points XPOL(I) in [A,B] and compute
#    the interpolating polynomial P(X) of order NPOL ( and degree NPOL-1)
#    which passes through all the points ( XPOL(I), F(XPOL(I)) ).
#    Then in the interval [A,B], the maximum error
#
#      abs ( F(X) - P(X) )
#
#    is bounded by:
#
#      C * FNMAX * W(X)
#
#    where
#
#      C is a constant,
#      FNMAX is the maximum value of the NPOL-th derivative of F in [A,B],
#      W(X) is the Lagrange factor.
#
#    Thus, the value of W(X) is useful as part of an estimated bound
#    for the interpolation error.
#
#    Note that the Chebyshev abscissas have the property that they minimize
#    the value of W(X) over the interval [A,B].  Hence, if the abscissas may
#    be chosen arbitrarily, the Chebyshev abscissas have this advantage over
#    other choices.
#
#    For a set of points XPOL(I), 1 <= I <= NPOL, the IPOL-th Lagrange basis
#    polynomial L(IPOL)(X), has the property:
#
#      L(IPOL)( XPOL(J) ) = delta ( IPOL, J )
#
#    and may be expressed as:
#
#      L(IPOL)(X) = W(X) / ( ( X - XPOL(IPOL) ) * W'(XPOL(IPOL)) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPOL, the number of abscissas.
#    NPOL must be at least 1.
#
#    real XPOL(NPOL), the abscissas, which should 
#    be distinct.
#
#    real XVAL, the point at which the Lagrange 
#    factor is to be evaluated.
#
#  Output:
#
#    real WVAL, the value of the Lagrange factor at XVAL.
#
#    real DWDX, the derivative of W with respect to XVAL.
#
  import numpy as np

  wval = np.prod ( xval - xpol[:] )

  dwdx = 0.0

  for i in range ( 0, npol ):

    term = 1.0

    for j in range ( 0, npol ):
      if ( i != j ):
        term = term * ( xval - xpol[j] )

    dwdx = dwdx + term

  return wval, dwdx

def r8poly_lagrange_factor_test ( ):

#*****************************************************************************80
#
## r8poly_lagrange_factor_test() tests r8poly_lagrange_factor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  npol = 5

  print ( '' )
  print ( 'r8poly_lagrange_factor_test():' )
  print ( '  r8poly_lagrange_factor() evaluates the Lagrange' )
  print ( '  factor W(X) at a point.' )
  print ( '' )
  print ( '  For this test, we use %d functions.' % ( npol ) )
#
#  Set the abscissas of the polynomials.
#
  xlo = 0.0
  xhi = npol - 1

  xpol = np.zeros ( npol)

  for i in range ( 0, npol ):
    xpol[i] = ( ( npol - i ) * xlo \
              + (        i ) * xhi )\
              / ( npol             )
 
  r8vec_print ( npol, xpol, '  Abscissas:' )
#
#  Evaluate W(X) and W'(X).
#
  print ( '' )
  print ( '      X          W(X)          W''(X)' )
  print ( '' )
  
  for i in range ( 0, 2 * npol ):

    xval = r8vec_even_select ( 2 * npol - 1, xhi, xlo, i )
 
    wval, dwdx = r8poly_lagrange_factor ( npol, xpol, xval )
 
    print ( '  %10f  %10f  %10f' % ( xval, wval, dwdx ) )

  return

def r8poly_lagrange_value ( npol, ipol, xpol, xval ):

#*****************************************************************************80
#
## r8poly_lagrange_value() evaluates the IPOL-th Lagrange polynomial.
#
#  Discussion:
#
#    Given NPOL distinct abscissas, XPOL(1:NPOL), the IPOL-th Lagrange
#    polynomial L(IPOL)(X) is defined as the polynomial of degree
#    NPOL - 1 which is 1 at XPOL(IPOL) and 0 at the NPOL - 1 other
#    abscissas.
#
#    A formal representation is:
#
#      L(IPOL)(X) = Product ( 1 <= I <= NPOL, I /= IPOL )
#       ( X - X(I) ) / ( X(IPOL) - X(I) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NPOL, the number of abscissas.
#    NPOL must be at least 1.
#
#    integer IPOL, the index of the polynomial to evaluate.
#    IPOL must be between 1 and NPOL.
#
#    real XPOL(NPOL), the abscissas of the Lagrange
#    polynomials.  The entries in XPOL must be distinct.
#
#    real XVAL, the point at which the IPOL-th 
#    Lagrange polynomial is to be evaluated.
#
#  Output:
#
#    real PVAL, the value of the IPOL-th Lagrange
#    polynomial at XVAL.
#
#    real DPDX, the derivative of the IPOL-th 
#    Lagrange polynomial at XVAL.
#

#
#  Make sure IPOL is legal.
#
  if ( ipol < 0 or npol <= ipol ):
    print ( '' )
    print ( 'r8poly_lagrange_value(): Fatal error!' )
    print ( '  0 <= IPOL < NPOL is required.' )
    raise Exception ( 'r8poly_lagrange_value(): Fatal error!' )
#
#  Check that the abscissas are distinct.
#
  if ( not r8vec_is_distinct ( npol, xpol ) ):
    print ( '' )
    print ( 'r8poly_lagrange_value(): Fatal error!' )
    print ( '  Two or more entries of XPOL are equal:' )
    raise Exception ( 'r8poly_lagrange_value(): Fatal error!' )
#
#  Evaluate the polynomial.
#
  pval = 1.0

  for i in range ( 0, npol ):

    if ( i != ipol ):

      pval = pval * ( xval - xpol[i] ) / ( xpol[ipol] - xpol[i] )
#
#  Evaluate the derivative, which can be found by summing up the result
#  of differentiating one factor at a time, successively.
#
  dpdx = 0.0

  for i in range ( 0, npol ):

    if ( i != ipol ):

      p2 = 1.0
      for j in range ( 0, npol ):

        if ( j == i ):
          p2 = p2                      / ( xpol[ipol] - xpol[j] )
        elif ( j != ipol ):
          p2 = p2 * ( xval - xpol[j] ) / ( xpol[ipol] - xpol[j] )

      dpdx = dpdx + p2

  return pval, dpdx

def r8poly_lagrange_value_test ( ):

#*****************************************************************************80
#
## r8poly_lagrange_value_test() tests r8poly_lagrange_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 April 2009
#
#  Author:
#
#    John Burkardt
#
  npol = 5

  print ( '' )
  print ( 'r8poly_lagrange_value_test()' )
  print ( '  r8poly_lagrange_value() evaluates a Lagrange' )
  print ( '  interpolating polynomial at a point.' )
  print ( '' )
  print ( '  Number of data points = ', npol )
#
#  Set the abscissas of the polynomials.
#
  xlo = 0.0
  xhi = npol - 1
  xpol = r8vec_even ( npol, xlo, xhi )
 
  r8vec_print ( npol, xpol, '  Abscissas:' )
#
#  Evaluate the polynomials.
#
  print ( '' )
  print ( '  Here are the values of the functions at' )
  print ( '  several points:' )
  print ( '' )
  print ( '      X          L1          L2          L3      L4' )
  print ( '          L5' )
  print ( '' )
 
  nx = 2 * npol - 1
 
  for ival in range ( 1, nx + 1 ):
 
    xval = r8vec_even_select ( nx, xlo, xhi, ival )
    print ( '  %10f' % ( xval ) ),

    for ipol in range ( 0, npol ):
      pval, dpdx =  r8poly_lagrange_value ( npol, ipol, xpol, xval )
 
      print ( '  %10f' % ( pval ) ),

    print ( '' )
 
  print ( '' )
  print ( '  And the derivatives:' )
  print ( '' )
  print ( '      X          L''1         L''2         L''3' )
  print ( '     L''4         L''5' )
  print ( '' )
 
  nx = 2 * npol - 1
 
  for ival in range ( 1, nx + 1 ):
 
    xval = r8vec_even_select ( nx, xlo, xhi, ival )
    print ( '  %10f' % ( xval ) ),

    for ipol in range ( 0, npol ):
      pval, dpdx =  r8poly_lagrange_value ( npol, ipol, xpol, xval )
 
      print ( '  %10f' % ( dpdx ) ),

    print ( '' )

  return

def r8poly_multiply ( na, a, nb, b ):

#*****************************************************************************80
#
## r8poly_multiply() computes the product of two real polynomials A and B.
#
#  Discussion:
#
#    The polynomials are in power sum form.
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(n-1) * x^(n-1) + a(n) * x^(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NA, the dimension of A.
#
#    real A[0:NA], the coefficients of the first polynomial factor.
#
#    integer NB, the dimension of B.
#
#    real B[0:NB], the coefficients of the second polynomial factor.
#
#  Output:
#
#    real C[0:NC], the coefficients of A * B.
#
  import numpy as np

  nc = na + nb
  c = np.zeros ( nc + 1 )

  for i in range ( 0, na + 1 ):
    for j in range ( 0, nb + 1 ):
      c[i+j] = c[i+j] + a[i] * b[j]

  return c

def r8poly_multiply_test ( ):

#*****************************************************************************80
#
## r8poly_multiply_test() tests r8poly_multiply().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  ntest = 2

  print ( '' )
  print ( 'r8poly_multiply_test()' )
  print ( '  r8poly_multiply() multiplies two polynomials.' )
#
#  1: Multiply (1+X) times (1-X).  Answer is 1-X^2.
#  2: Multiply (1+2*X+3*X^2) by (1-2*X). Answer is 1 + 0*X - X^2 - 6*X^3
#
  for itest in range ( 0, ntest ):

    if ( itest == 0 ):
      na = 1
      a = np.array ( [ 1.0, 1.0 ] )
      nb = 1
      b = np.array ( [ 1.0, -1.0 ] )
    elif ( itest == 1 ):
      na = 2
      a = np.array ( [ 1.0, 2.0, 3.0 ] )
      nb = 1
      b = np.array ( [ 1.0, -2.0 ] )

    c = r8poly_multiply ( na, a, nb, b )

    r8poly_print ( a, '  The factor A:' )

    r8poly_print ( b, '  The factor B:' )

    r8poly_print ( c, '  The product C = A*B:' )

  return

def r8poly_power ( na, a, p ):

#*****************************************************************************80
#
## r8poly_power() computes a positive integer power of a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1)*x + ... + a(n-1)*x^(n-1) + a(n)*x^(n)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NA, the dimension of A.
#
#    real A(1:NA+1), the polynomial to be raised to the power.
#
#    integer P, the nonnegative power to which A is raised.
#
#  Output:
#
#    real B(P*NA+1), the power of the polynomial.
#
  import numpy as np
#
#  Zero out B.
#
  b = np.zeros ( p * na + 1 )
#
#  Search for the first nonzero element in A.
#
  nonzer = -1

  for i in range ( 0, na + 1 ):
    if ( a[i] != 0.0 ):
      nonzer = i
      break

  if ( nonzer == -1 ):
    return b

  b[0] = a[nonzer] ** p

  for i in range ( 1, p*(na-nonzer)+1 ):

    if ( i + nonzer <= na ):
      b[i] = i * p * b[0] * a[i+nonzer]
    else:
      b[i] = 0.0

    for j in range ( 1, i ):

      if ( j+nonzer <= na ):
        b[i] = b[i] - ( i - j ) * a[j+nonzer] * b[i-j]

      if ( i-j+nonzer <= na ):
        b[i] = b[i] + ( i - j ) * p * b[j] * a[i-j+nonzer]

    b[i] = b[i] / ( i * a[nonzer] )
#
#  Shift B up.
#
  for i in range ( p*nonzer, p*na + 1 ):
    b[i] = b[i-p*nonzer]

  for i in range ( 0, p * nonzer ):
    b[i] = 0.0

  return b

def r8poly_power_test ( ):

#*****************************************************************************80
#
## r8poly_power_test() tests r8poly_power().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8poly_power_test()' )
  print ( '  r8poly_power() takes a polynomial to a power.' )
#
#  Cube (2-X).  Answer is 8-12*X+6*X^2-X^3.
#
  na = 1
  a = np.array ( [ 2.0, -1.0 ] )
  p = 3

  r8poly_print ( a, '  The polynomial A:' )
 
  b = r8poly_power ( na, a, p )
 
  r8poly_print ( b, '  Raised to the power 3:' )
#
#  Square X+X^2
#
  na = 2
  a = np.array ( [ 0.0, 1.0, 1.0 ] )
  p = 2

  r8poly_print ( a, '  The polynomial A:' )
 
  b = r8poly_power ( na, a, p )
 
  r8poly_print ( b, '  Raised to the power 2:' )

  return

def r8poly_print ( a, title ):

#*****************************************************************************80
#
## r8poly_print() prints a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A[M+1], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    string TITLE, a title.
#
  import numpy as np

  m = len ( a ) - 1

  print ( title )

  if ( np.all ( a == 0.0 ) ):
    print ( '  p(x) = 0' )
    return
 
  first = True

  for i in range ( m, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( first ):
        print ( '  p(x) =', end = '' )
        if ( plus_minus == '+' ):
          plus_minus = ' '
        first = False

      if ( 2 <= i ):
        print ( ' %c %g * x^%d' % ( plus_minus, mag, i ), end = '' )
      elif ( i == 1 ):
        print ( ' %c %g * x' % ( plus_minus, mag ), end = '' )
      elif ( i == 0 ):
        print ( ' %c %g' % ( plus_minus, mag ), end = '' )

  print ( '' )

  return

def r8poly_print_test ( ):

#*****************************************************************************80
#
## r8poly_print_test() tests r8poly_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8poly_print_test()' )
  print ( '  r8poly_print() prints an R8POLY.' )

  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )
  print ( '' )
  r8poly_print ( c, '  The R8POLY:' )

  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 0.0 ] )
  print ( '' )
  r8poly_print ( c, '  The R8POLY:' )

  c = np.array ( [ 12.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  print ( '' )
  r8poly_print ( c, '  The R8POLY:' )

  c = np.array ( [ 0.0, 0.0, 0.0, 0.0, 0.0, 1.0 ] )
  print ( '' )
  r8poly_print ( c, '  The R8POLY:' )

  c = np.array ( [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] )
  print ( '' )
  r8poly_print ( c, '  The R8POLY:' )

  return

def r8poly_shift ( scale, shift, n, poly_cof ):

#*****************************************************************************80
#
## r8poly_shift() adjusts the coefficients of a polynomial for a new argument.
#
#  Discussion:
#
#    Assuming P(X) is a polynomial in the argument X, of the form:
#
#      P(X) =
#          C(N) * X^(N-1)
#        + ...
#        + C(2) * X
#        + C(1),
#
#    and that Z is related to X by the formula:
#
#      Z = SCALE * X + SHIFT
#
#    then this routine computes coefficients C for the polynomial Q(Z):
#
#      Q(Z) =
#          C(N) * Z^(N-1)
#        + ...
#        + C(2) * Z
#        + C(1)
#
#    so that:
#
#      Q(Z(X)) = P(X)e
#
#  Example:
#
#    P(X) = 2 * X^2 - X + 6
#
#    Z = 2.0 * X + 3.0
#
#    Q(Z) = 0.5 *         Z^2 -  3.5 * Z + 12
#
#    Q(Z(X)) = 0.5 * ( 4.0 * X^2 + 12.0 * X +  9 )
#            - 3.5 * (              2.0 * X +  3 )
#                                            + 12
#
#            = 2.0         * X^2 -  1.0 * X +  6
#
#            = P(X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real SHIFT, SCALE, the shift and scale applied to X,
#    so that Z = SCALE * X + SHIFT.
#
#    integer N, the order of the polynomial.
#
#    real POLY_COF(N), the coefficient array in terms of the X variable.
#
#  Output:
#
#    real POLY_COF(N), the coefficient array in terms of the Z variable.
#
  for i in range ( 0, n ):
    poly_cof[(i+1):n] = poly_cof[(i+1):n] / scale

  for i in range ( 0, n ):
    for j in range ( n - 2, i - 1, -1 ):
      poly_cof[j] = poly_cof[j] - shift * poly_cof[j+1]

  return poly_cof

def r8poly_shift_test ( ):

#*****************************************************************************80
#
## r8poly_shift_test() tests r8poly_shift().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8poly_shift_test():' )
  print ( '  r8poly_shift() shifts an R8POLY p(x) to q(z)' )
  print ( '  where z=scale*x+shift.' )

  order = 3
  degree = 2

  c = np.array ( [ 6.0, -1.0, 2.0 ] )
  r8poly_print ( c, '  p(x):' )

  scale = 2.0
  shift = 3.0
  print ( '' )
  print ( '  z = scale * x + shift' )
  print ( '  Scale = %g' % ( scale ) )
  print ( '  Shift = %g' % ( shift ) )

  c2 = r8poly_shift ( scale, shift, order, c )
  r8poly_print ( c2, '  q(z):' )

  c3 = np.array ( [ 12.0, -3.5, 0.5 ] )
  r8poly_print ( c3, '  Expected q(z):' )

  return

def r8poly_value_horner ( m, c, x ):

#*****************************************************************************80
#
## r8poly_value_horner() evaluates a polynomial using Horner's method.
#
#  Discussion:
#
#    The polynomial 
#
#      p(x) = c0 + c1 * x + c2 * x^2 + ... + cm * x^m
#
#    is to be evaluated at the value X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the degree.
#
#    real C(0:M), the polynomial coefficients.  
#    C(I) is the coefficient of X^I.
#
#    real X, the evaluation point.
#
#  Output:
#
#    real VALUE, the polynomial value.
#
  value = c[m]
  for i in range ( m - 1, -1, -1 ):
    value = value * x + c[i]

  return value

def r8poly_value_horner_test ( ):

#*****************************************************************************80
#
## r8poly_value_horner_test() tests r8poly_value_horner().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4;
  n = 16;
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )

  print ( '' )
  print ( 'r8poly_value_horner_test():' )
  print ( '  r8poly_value_horner() evaluates a polynomial at a point' )
  print ( '  using Horners method.' )

  r8poly_print ( c, '  The polynomial coefficients:' )

  x_lo = 0.0
  x_hi = 5.0
  x = np.linspace ( x_lo, x_hi, n )

  print ( '' )
  print ( '   I    X    P(X)' )
  print ( '' )

  for i in range ( 0, n ):
    p = r8poly_value_horner ( m, c, x[i] )
    print ( '  %2d  %8.4f  %14.6g' % ( i, x[i], p ) )

  return

def r8poly_value ( m, c, x ):

#*****************************************************************************80
#
## r8poly_value() evaluates a polynomial using a naive method.
#
#  Discussion:
#
#    The polynomial 
#
#      p(x) = c0 + c1 * x + c2 * x^2 + ... + cm * x^m
#
#    is to be evaluated at the value X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the degree.
#
#    real C(0:M), the polynomial coefficients.  
#    C(I) is the coefficient of X^I.
#
#    real X, the evaluation point.
#
#  Output:
#
#    real VALUE, the polynomial value.
#
  value = c[0]
  xi = 1.0
  for i in range ( 1, m + 1 ):
    xi = xi * x
    value = value + c[i] * xi

  return value

def r8poly_value_test ( ):

#*****************************************************************************80
#
## r8poly_value_test() tests r8poly_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4;
  n = 16;
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )

  print ( '' )
  print ( 'r8poly_value_test()' )
  print ( '  r8poly_value() evaluates a polynomial at a point' )
  print ( '  using a naive method.' )

  r8poly_print ( c, '  The polynomial coefficients:' )

  x_lo = 0.0
  x_hi = 5.0
  x = np.linspace ( x_lo, x_hi, n )

  print ( '' )
  print ( '   I    X    P(X)' )
  print ( '' )

  for i in range ( 0, n ):
    p = r8poly_value ( m, c, x[i] )
    print ( '  %2d  %8.4f  %14.6g' % ( i, x[i], p ) )

  return

def r8poly_values_horner ( m, c, n, x ):

#*****************************************************************************80
#
## r8poly_values_horner() evaluates a polynomial using Horner's method.
#
#  Discussion:
#
#    The polynomial 
#
#      p(x) = c0 + c1 * x + c2 * x^2 + ... + cm * x^m
#
#    can be evaluated at the vector x by the command
#
#      pval = r8poly_value ( m, c, n, x )
#
#    Note that C must actually be dimensioned of size M+1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the degree.
#
#    real C(M+1), the polynomial coefficients.  
#    C(I+1) is the coefficient of X^I.
#
#    integer N, the number of evaluation points.
#
#    real X(N), the evaluation points.
#
#  Output:
#
#    real P(N), the polynomial values.
#
  import numpy as np

  p = np.zeros ( n )

  for j in range ( 0, n ):
    p[j] = c[m]
    for i in range ( m - 1, -1, -1 ):
      p[j] = p[j] * x[j] + c[i]

  return p

def r8poly_values_horner_test ( ):

#*****************************************************************************80
#
## r8poly_values_horner_test() tests r8poly_values_horner().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8poly_values_horner_test():' )
  print ( '  r8poly_values_horner() evaluates a polynomial at a' )
  print ( '  point, using Horner\'s method.' )

  m = 4
  c = np.array ( [ 24.0, -50.0, +35.0, -10.0, 1.0 ] )
  r8poly_print ( c, '  The polynomial:' )

  n = 16
  x_lo = 0.0
  x_hi = 5.0
  x = np.linspace ( x_lo, x_hi, n )

  p = r8poly_values_horner ( m, c, n, x )

  r8vec2_print ( x, p, '  X, P(X):' )

  return

def r8_sign ( x ):

#*****************************************************************************80
#
## r8_sign() returns the sign of an R8.
#
#  Discussion:
#
#    The value is +1 if the number is positive or zero, and it is -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose sign is desired.
#
#  Output:
#
#    real VALUE, the sign of X.
#
  if ( x < 0.0 ):
    value = -1.0
  else:
    value = +1.0
 
  return value

def r8_sign_test ( ):

#*****************************************************************************80
#
## r8_sign_test() tests r8_sign().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 September 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  test_num = 5

  r8_test = np.array ( [ -1.25, -0.25, 0.0, +0.5, +9.0 ] )

  print ( '' )
  print ( 'r8_sign_test():' )
  print ( '  r8_sign() returns the sign of an R8.' )
  print ( '' )
  print ( '     R8     r8_sign(R8)' )
  print ( '' )

  for test in range ( 0, test_num ):
    r8 = r8_test[test]
    s = r8_sign ( r8 )
    print ( '  %8.4f  %8.0f' % ( r8, s ) )

  return

def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test() tests r8vec2_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec2_print_test():' )
  print ( '  r8vec2_print() prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( v, w, '  Print a pair of R8VEC\'s:' )

  return

def r8vec_even ( n, alo, ahi ):

#*****************************************************************************80
#
## r8vec_even() returns N real values, evenly spaced between ALO and AHI.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 January 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of values.
#
#    real ALO, AHI, the low and high values.
#
#  Output:
#
#    real A(N), N evenly spaced values.
#    Normally, A(1) = ALO and A(N) = AHI.
#    However, if N = 1, then A(1) = 0.5*(ALO+AHI).
#
  import numpy as np

  a = np.zeros ( n )

  if ( n == 1 ):

    a[0] = 0.5 * ( alo + ahi )

  else:

    for i in range ( 0, n ):
      a[i] = ( ( n - 1 - i ) * alo + i * ahi ) / float ( n - 1 )

  return a

def r8vec_even_test ( ):

#*****************************************************************************80
#
## r8vec_even_test() tests r8vec_even().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
  n = 10
  xlo = 0.0
  xhi = 99.0
 
  print ( '' )
  print ( 'r8vec_even_test():' )
  print ( '  r8vec_even() computes N evenly spaced values' )
  print ( '  between XLO and XHI.' )
  print ( '' )
  print ( '  XLO = %f' % ( xlo ) )
  print ( '  XHI = %f' % ( xhi ) )
  print ( '  while N = %d' % ( n ) )
 
  x = r8vec_even ( n, xlo, xhi )
 
  r8vec_print ( n, x, '  Resulting array:' )

  return

def r8vec_even_select ( n, xlo, xhi, ival ):

#*****************************************************************************80
#
## r8vec_even_select() returns the I-th of N evenly spaced values in [ XLO, XHI ].
#
#  Discussion:
#
#    XVAL = ( (N-IVAL) * XLO + (IVAL-1) * XHI ) / dble ( N - 1 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of values.
#
#    real XLO, XHI, the low and high values.
#
#    integer IVAL, the index of the desired point.
#    IVAL is normally between 1 and N, but may be any
#    integer value.
#
#  Output:
#
#    real XVAL, the IVAL-th of N evenly spaced values
#    between XLO and XHI.
#    Unless N = 1, X(1) = XLO and X(N) = XHI.
#    If N = 1, then X(1) = 0.5*(XLO+XHI).
#
  if ( n == 1 ):

    xval = 0.5 * ( xlo + xhi )

  else:

    xval = ( float ( n - ival     ) * xlo   \
           + float (     ival - 1 ) * xhi ) \
           / float ( n        - 1 )

  return xval

def r8vec_even_select_test ( ):

#*****************************************************************************80
#
## r8vec_even_select_test() tests r8vec_even_select().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 August 2018
#
#  Author:
#
#    John Burkardt
#
  n = 10
  xlo = 0.0
  xhi = 99.0
 
  print ( '' )
  print ( 'r8vec_even_select_test():' )
  print ( '  r8vec_even_select() returns the I-th of N evenly spaced values' )
  print ( '  between XLO and XHI.' )
  print ( '' )
  print ( '  XLO = %f' % ( xlo ) )
  print ( '  XHI = %f' % ( xhi ) )
  print ( '  while N = %d' % ( n ) )
  print ( '' )
 
  for i in range ( 2, n + 1, 3 ):
    xi = r8vec_even_select ( n, xlo, xhi, i )
    print ( '  X(%d) = %g' % ( i, xi ) )

  return

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## r8vec_indicator1() sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    real A(N), the indicator array.
#
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## r8vec_indicator1_test() tests r8vec_indicator1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_indicator1_test()' )
  print ( '  r8vec_indicator1() returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )

  return

def r8vec_is_distinct ( n, a ):

#*****************************************************************************80
#
## r8vec_is_distinct() is true if the entries in an R8VEC are distinct.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the vector.
#
#    real A(N), the vector to be checked.
#
#  Output:
#
#    bool VALUE is true if the elements of A are distinct.
#
  for i in range ( 1, n ):
    for j in range ( 0, i ):
      if ( a[i] == a[j] ):
        value = False;
        return value

  value = True

  return value

def r8vec_is_distinct_test ( ):

#*****************************************************************************80
#
## r8vec_is_distinct_test() tests r8vec_is_distinct().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_distinct_test()' )
  print ( '  r8vec_is_distinct() computes the maximum entry in an R8VEC.' )

  n = 5
  a = np.array ( [ 1.0, 2.0, 5.0, 3.0, 4.0 ] )
  r8vec_print ( n, a, '  Input vector:' )
  if ( r8vec_is_distinct ( n, a ) ):
    print ( '  Array entries are distinct.' )
  else:
    print ( '  Array entries are NOT distinct.' )

  n = 5
  a = np.array ( [ 1.0, 2.0, 5.0, 2.0, 4.0 ] )
  r8vec_print ( n, a, '  Input vector:' )
  if ( r8vec_is_distinct ( n, a ) ):
    print ( '  Array entries are distinct.' )
  else:
    print ( '  Array entries are NOT distinct.' )

  return

def r8vec_is_zero ( n, x ):

#*****************************************************************************80
#
## r8vec_is_zero() is true if every entry is zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vectors.
#
#    real X(N), the vector to be compared against.
#
#  Output:
#
#    bool VALUE, is true if all entries are zero.
#
  import numpy as np

  value = np.all ( x[0:n] == 0.0 )

  return value

def r8vec_is_zero_test ( ):

#*****************************************************************************80
#
## r8vec_is_zero_test() tests r8vec_is_zero().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_is_zero_test()' )
  print ( '  r8vec_is_zero() is TRUE if an R8VEC contains' )
  print ( '  only zero entries.' )

  n = 3

  x = np.array ( [ 0.0, 1.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_zero ( n, x ) ):
    print ( '  X contains only zero entries.' )
  else:
    print ( '  X contains at least one nonzero entry.' )

  x = np.array ( [ 0.0, 0.0, 0.0 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_zero ( n, x ) ):
    print ( '  X contains only zero entries.' )
  else:
    print ( '  X contains at least one nonzero entry.' )

  x = np.array ( [ -3.0, -99.0, -87.3 ] )
  print ( '' )
  r8vec_transpose_print ( n, x, '  X:' )
  if ( r8vec_is_zero ( n, x ) ):
    print ( '  X contains only zero entries.' )
  else:
    print ( '  X contains at least one nonzero entry.' )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  if ( a.ndim == 1 ):
    for i in range ( 0, n ):
      print ( '%6d:  %12g' % ( i, a[i] ) )
  else:
    for i in range ( 0, n ):
      print ( '%6d:  %12g' % ( i, a[i,0] ) )

  return

def r8vec_transpose_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_transpose_print() prints an R8VEC "transposed".
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Example:
#
#    A = (/ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 /)
#    TITLE = 'My vector:  '
#
#    My vector:   1.0    2.1    3.2    4.3    5.4
#                 6.5    7.6    8.7    9.8   10.9
#                11.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  title_length = len ( title )

  for ilo in range ( 0, n, 5 ):

    if ( ilo == 0 ):
      print ( title, end = '' )
    else:
      blanks = ''
      for i in range ( 0, title_length ):
        blanks = blanks + ' '
      print ( blanks, end = '' )

    print ( '  ', end = '' )

    ihi = min ( ilo + 5 - 1, n - 1 )

    for i in range ( ilo, ihi + 1 ):
      print ( '  %12g' % ( a[i] ), end = '' )
    print ( '' )

  return

def r8vec_transpose_print_test ( ):

#*****************************************************************************80
#
## r8vec_transpose_print_test() tests r8vec_transpose_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 11

  print ( '' )
  print ( 'r8vec_transpose_print_test()' )
  print ( '  r8vec_transpose_print() prints an R8VEC "tranposed",' )
  print ( '  that is, placing multiple entries on a line.' )

  x = np.array ( [ 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9, 11.0 ] )

  r8vec_transpose_print ( n, x, '  The vector X:' )

  return

def roots_to_r8poly ( n, x ):

#*****************************************************************************80
#
## roots_to_r8poly() converts polynomial roots to polynomial coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 April 2005
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of roots specified.
#
#    real X(N), the roots.
#
#  Output:
#
#    real C(1:N+1), the coefficients of the polynomial.
#
  import numpy as np
#
#  Initialize C to (0, 0, ..., 0, 1).
#  Essentially, we are setting up a divided difference table.
#
  c = np.zeros ( n + 1 )
  c[n] = 1.0
#
#  Convert to standard polynomial form by shifting the abscissas
#  of the divided difference table to 0.
#
  for j in range ( 1, n + 1 ):
    for i in range ( 1, n + 2 - j ):
      c[n-i] = c[n-i] - x[n+1-i-j] * c[n-i+1]

  return c

def roots_to_r8poly_test ( ):

#*****************************************************************************80
#
## roots_to_r8poly_test() tests roots_to_r8poly().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  x = np.array ( [ \
     1.0, \
    -4.0, \
     3.0, \
     0.0, \
     3.0 ] );

  print ( '' )
  print ( 'roots_to_r8poly_test()' )
  print ( '  roots_to_r8poly() is given N real roots,' )
  print ( '  and constructs the coefficient vector' )
  print ( '  of the corresponding polynomial.' )

  r8vec_print ( n, x, '  N real roots:' )

  c = roots_to_r8poly ( n, x )

  r8poly_print ( c, '  The polynomial:' )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  r8poly_test ( )
  timestamp ( )

