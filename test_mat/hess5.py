#! /usr/bin/env python
#
def hess5 ( ):

#*****************************************************************************80
#
## HESS5 returns the HESS5 matrix.
#
#  Example:
#
#     9     4     1     3     2
#     4     3     1     7     1
#     0     3     1     2     4
#     0     0     5     5     1
#     0     0     0     1     2
#
#  Properties:
#
#    A is integral.
#
#    A is not symmetric.
#
#    A is upper Hessenberg.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(5,5), the matrix.
# 
  import numpy as np

  a = np.array ( [ \
    [ 9.0,     4.0,     1.0,     3.0,     2.0 ], \
    [ 4.0,     3.0,     1.0,     7.0,     1.0 ], \
    [ 0.0,     3.0,     1.0,     2.0,     4.0 ], \
    [ 0.0,     0.0,     5.0,     5.0,     1.0 ], \
    [ 0.0,     0.0,     0.0,     1.0,     2.0 ] ] )

  return a

def hess5_determinant ( ):

#*****************************************************************************80
#
## HESS5_DETERMINANT returns the determinant of the HESS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant.
#
  value = 1479.0

  return value

def hess5_eigen_right ( ):

#*****************************************************************************80
#
## HESS5_EIGEN_RIGHT returns the right eigenvectors of the HESS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, complex A(5,5), the right eigenvector matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ -0.4048+0.0000*j, -0.2788-0.1981*j, -0.2788+0.1981*j,  1.0000+0.0000*j,  1.0000+0.0000*j ], \
    [  1.0000+0.0000*j,  1.0000+0.0000*j,  1.0000+0.0000*j,  0.0372+0.0000*j,  0.5780+0.0000*j ], \
    [  0.0565+0.0000*j, -0.0712-0.9695*j, -0.0712+0.9695*j, -0.2064+0.0000*j,  0.1887+0.0000*j ], \
    [  0.1687+0.0000*j, -0.3560+0.6933*j, -0.3560-0.6933*j, -0.5057+0.0000*j,  0.1379+0.0000*j ], \
    [ -0.8231+0.0000*j,  0.1938-0.0411*j,  0.1938+0.0411*j, -0.0966+0.0000*j,  0.0139+0.0000*j ] ] )

  return a

def hess5_eigenvalues ( ):

#*****************************************************************************80
#
## HESS5_EIGENVALUES returns the eigenvalues of the HESS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, complex LAMDA(4), the eigenvalues.
#
  import numpy as np

  lamda = np.array ( [ \
     1.795071645585215 + 0.000000000000000*j, \
    -0.484650565840867 + 3.050399870879445*j, \
    -0.484650565840867 - 3.050399870879445*j, \
     7.232089690415871 + 0.000000000000000*j, \
    11.942139795680633 + 0.000000000000000*j ] )

  return lamda

def hess5_inverse ( ):

#*****************************************************************************80
#
## HESS5_INVERSE returns the inverse of the HESS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real B(5,5), the matrix.
#
  import numpy as np

  b = np.array ( [ \
    [  0.131845841784990, -0.046653144016227, -0.129141311697093,  0.008789722785666,   0.145368492224476 ], \
    [ -0.024340770791075,  0.054766734279919,  0.311020960108181, -0.068289384719405,  -0.590939824205544 ], \
    [  0.073022312373225, -0.164300202839757,  0.066937119675456,  0.204868154158215,  -0.227180527383367 ], \
    [ -0.081135902636917,  0.182555780933063, -0.074374577417174, -0.005409060175794,   0.141311697092630 ], \
    [  0.040567951318458, -0.091277890466531,  0.037187288708587,  0.002704530087897,   0.429344151453685 ] ] )

  return b

def hess5_test ( ):

#*****************************************************************************80
#
## HESS5_TEST tests HESS5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2018
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'HESS5_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  HESS5 computes the HESS5 matrix.' )

  m = 5
  n = 5
  a = hess5 ( )

  r8mat_print ( m, n, a, '  HESS5 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'HESS5_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  hess5_test ( )
  timestamp ( )
