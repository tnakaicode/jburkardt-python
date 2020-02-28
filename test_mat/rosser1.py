#! /usr/bin/env python
#
def rosser1 ( ):

#*****************************************************************************80
#
## ROSSER1 returns the ROSSER1 matrix.
#
#  Formula:
#
#    611  196 -192  407   -8  -52  -49   29
#    196  899  113 -192  -71  -43   -8  -44
#   -192  113  899  196   61   49    8   52
#    407 -192  196  611    8   44   59  -23
#     -8  -71   61    8  411 -599  208  208
#    -52  -43   49   44 -599  411  208  208
#    -49   -8    8   59  208  208   99 -911
#     29  -44   52  -23  208  208 -911   99
#
#  Properties:
#
#    A is singular.
#
#    det ( A ) = 0.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    The eigenvalues of A are:
#
#      a = sqrt(10405), b = sqrt(26),
#
#      LAMBDA = (-10*a, 0, 510-100*b, 1000, 1000, 510+100*b, 1020, 10*a)
#
#      ( 10*a = 1020.04901843, 510-100*b = 0.09804864072 )
#
#    The eigenvectors are
#
#      ( 2,  1,   1,  2, 102+a, 102+a, -204-2a, -204-2a )
#      ( 1,  2,  -2, -1,    14,    14,       7,       7 )
#      ( 2, -1,   1, -2,   5-b,  -5+b,  -10+2b,   10-2b )
#      ( 7, 14, -14, -7,    -2,    -2,      -1,      -1 )
#      ( 1, -2,  -2,  1,    -2,     2,      -1,       1 )
#      ( 2, -1,   1, -2,   5+b,  -5-b,  -10-2b,   10+2b )
#      ( 1, -2,  -2,  1,     2,    -2,       1,      -1 )
#      ( 2,  1,   1,  2, 102-a, 102-a, -204+2a, -204+2a )
#
#    trace ( A ) = 4040.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 4.10,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 61, 
#    LC: QA263.G68.
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Parameters:
#
#    Output, real A(8,8), the matrix.
#
  import numpy as np

  a = np.array ( [ \
      [  611.0,  196.0, -192.0,  407.0,   -8.0,  -52.0,  -49.0,   29.0 ], \
      [  196.0,  899.0,  113.0, -192.0,  -71.0,  -43.0,   -8.0,  -44.0 ], \
      [ -192.0,  113.0,  899.0,  196.0,   61.0,   49.0,    8.0,   52.0 ], \
      [  407.0, -192.0,  196.0,  611.0,    8.0,   44.0,   59.0,  -23.0 ], \
      [   -8.0,  -71.0,   61.0,    8.0,  411.0, -599.0,  208.0,  208.0 ], \
      [  -52.0,  -43.0,   49.0,   44.0, -599.0,  411.0,  208.0,  208.0 ], \
      [  -49.0,   -8.0,    8.0,   59.0,  208.0,  208.0,   99.0, -911.0 ], \
      [   29.0,  -44.0,   52.0,  -23.0,  208.0,  208.0, -911.0,   99.0 ] ] )

  return a

def rosser1_determinant ( ):

#*****************************************************************************80
#
## ROSSER1_DETERMINANT computes the determinant of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant.
#
  value = 0.0

  return value

def rosser1_determinant_test ( ):

#*****************************************************************************80
#
## ROSSER1_DETERMINANT_TEST tests ROSSER1_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from rosser1 import rosser1
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'ROSSER1_DETERMINANT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ROSSER1_DETERMINANT computes the ROSSER1 determinant.' )

  seed = 123456789

  m = 8
  n = m
  a = rosser1 ( )
  r8mat_print ( n, n, a, '  ROSSER1 matrix:' )

  value = rosser1_determinant ( )

  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ROSSER1_DETERMINANT_TEST' )
  print ( '  Normal end of execution.' )
  return

def rosser1_eigen_left ( ):

#*****************************************************************************80
#
## ROSSER1_EIGEN_LEFT returns left eigenvectors of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real X(8,8), the eigenvector matrix.
#
  import numpy as np

  a = np.sqrt ( 10405.0 )
  b = np.sqrt ( 26.0 )

  x = np.zeros ( ( 8, 8 ) )
#
#  Note that the matrix entries are listed by ROW
#
  x = np.array ( [ \
    [ 2.0, 1.0, 1.0, 2.0, 102.0 + a, 102.0 + a, -204.0 - 2.0 * a, -204.0 - 2.0 * a ], \
    [ 1.0, 2.0, -2.0, -1.0, 14.0, 14.0,       7.0,       7.0 ], \
    [ 2.0, -1.0, 1.0, -2.0, 5.0 - b, -5.0 + b, -10.0 + 2.0 * b, 10.0 - 2.0 * b ], \
    [ 7.0, 14.0, -14.0, -7.0,  -2.0, -2.0,      -1.0,      -1.0 ], \
    [ 1.0, -2.0,  -2.0,  1.0,  -2.0, 2.0,      -1.0,       1.0 ], \
    [ 2.0, -1.0, 1.0, -2.0, 5.0 + b, -5.0 - b, -10.0 - 2.0 * b, 10.0 + 2.0 * b ], \
    [ 1.0, -2.0,  -2.0,  1.0,   2.0, -2.0,       1.0,      -1.0 ], \
    [ 2.0, 1.0, 1.0, 2.0, 102.0 - a, 102.0 - a, -204.0 + 2.0 * a, -204.0 + 2.0 * a ] ] )

  return x

def rosser1_eigen_right ( ):

#*****************************************************************************80
#
## ROSSER1_EIGEN_RIGHT returns right eigenvectors of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real X(8,8), the eigenvector matrix.
#
  import numpy as np

  a = np.sqrt ( 10405.0 )
  b = np.sqrt ( 26.0 )

  x = np.zeros ( ( 8, 8 ) )
#
#  Note that the matrix entries are listed by ROW
#
  x = np.array ( [ \
    [ 2.0, 1.0, 1.0, 2.0, 102.0 + a, 102.0 + a, -204.0 - 2.0 * a, -204.0 - 2.0 * a ], \
    [ 1.0, 2.0, -2.0, -1.0, 14.0, 14.0,       7.0,       7.0 ], \
    [ 2.0, -1.0, 1.0, -2.0, 5.0 - b, -5.0 + b, -10.0 + 2.0 * b, 10.0 - 2.0 * b ], \
    [ 7.0, 14.0, -14.0, -7.0,  -2.0, -2.0,      -1.0,      -1.0 ], \
    [ 1.0, -2.0,  -2.0,  1.0,  -2.0, 2.0,      -1.0,       1.0 ], \
    [ 2.0, -1.0, 1.0, -2.0, 5.0 + b, -5.0 - b, -10.0 - 2.0 * b, 10.0 + 2.0 * b ], \
    [ 1.0, -2.0,  -2.0,  1.0,   2.0, -2.0,       1.0,      -1.0 ], \
    [ 2.0, 1.0, 1.0, 2.0, 102.0 - a, 102.0 - a, -204.0 + 2.0 * a, -204.0 + 2.0 * a ] ] )

  x = np.transpose ( x )

  return x

def rosser1_eigenvalues ( ):

#*****************************************************************************80
#
## ROSSER1_EIGENVALUES returns the eigenvalues of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real LAMBDA(8,1), the eigenvalues.
#
  import numpy as np

  a = np.sqrt ( 10405.0 )
  b = np.sqrt ( 26.0 )

  lam = np.array ( [ \
    [  -10.0 * a ], \
    [    0.0 ], \
    [  510.0 - 100.0 * b ], \
    [ 1000.0 ], \
    [ 1000.0 ], \
    [  510.0 + 100.0 * b ], \
    [ 1020.0 ], \
    [ 10.0 * a ] ] )

  return lam

def rosser1_null_left ( ):

#*****************************************************************************80
#
## ROSSER1_NULL_LEFT returns a left null vector of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real X(8), the null vector.
#
  import numpy as np

  x = np.array ( [ \
    [  1.0 ], \
    [  2.0 ], \
    [ -2.0 ], \
    [ -1.0 ], \
    [ 14.0 ], \
    [ 14.0 ], \
    [  7.0 ], \
    [  7.0 ] ] )

  return x

def rosser1_eigenvalues ( ):

#*****************************************************************************80
#
## ROSSER1_EIGENVALUES returns the eigenvalues of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real LAM(8), the eigenvalues.
#
  import numpy as np

  a = np.sqrt ( 10405.0 )
  b = np.sqrt ( 26.0 )

  lam = np.array ( [ \
    [  -10.0 * a ], \
    [    0.0 ], \
    [  510.0 - 100.0 * b ], \
    [ 1000.0 ], \
    [ 1000.0 ], \
    [  510.0 + 100.0 * b ], \
    [ 1020.0 ], \
    [ 10.0 * a ] ] )

  return lam

def rosser1_null_right ( ):

#*****************************************************************************80
#
## ROSSER1_NULL_RIGHT returns a right null vector of the ROSSER1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real X(8), the null vector.
#
  import numpy as np

  x = np.array ( [ \
    [  1.0 ], \
    [  2.0 ], \
    [ -2.0 ], \
    [ -1.0 ], \
    [ 14.0 ], \
    [ 14.0 ], \
    [  7.0 ], \
    [  7.0 ] ] )

  return x

def rosser1_test ( ):

#*****************************************************************************80
#
## ROSSER1_TEST tests ROSSER1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'ROSSER1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ROSSER1 computes the ROSSER1 matrix.' )

  n = 8
  a = rosser1 ( )
  r8mat_print ( n, n, a, '  ROSSER1 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ROSSER1_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rosser1_test ( )
  rosser1_determinant ( )
  timestamp ( )
