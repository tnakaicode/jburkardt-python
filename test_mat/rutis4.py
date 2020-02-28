#! /usr/bin/env python
#
def rutis4 ( n ):

#*****************************************************************************80
#
## RUTIS4 returns the RUTIS4 matrix.
#
#  Example:
#
#    N = 6
#
#    14 14  6  1  0  0
#    14 20 15  6  1  0
#     6 15 20 15  6  1
#     1  6 15 20 15  6
#     0  1  6 15 20 14
#     0  0  1  6 14 14
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is banded with a bandwidth of 7.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is the cube of the scalar tridiagonal matrix whose diagonals
#    are ( 1, 2, 1 ).
#
#    LAMBDA(I) = 64 * ( cos ( i * pi / ( 2 * ( n + 1 ) ) ) )^6
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
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
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):

    if ( 0 <= i - 3 ):
      a[i,i-3] = 1.0

    if ( 0 <= i - 2 ):
      a[i,i-2] = 6.0

    if ( 0 <= i - 1 ):
      a[i,i-1] = 15.0

    a[i,i] = 20.0

    if ( i + 1 <= n - 1 ):
      a[i,i+1] = 15.0

    if ( i + 2 <= n - 1 ):
      a[i,i+2] = 6.0

    if ( i + 3 <= n - 1 ):
      a[i,i+3] = 1.0

  a[0,0] = 14.0
  a[0,1] = 14.0
  a[1,0] = 14.0

  a[n-1,n-1] = 14.0
  a[n-2,n-1] = 14.0
  a[n-1,n-2] = 14.0

  return a

def rutis4_determinant ( n ):

#*****************************************************************************80
#
## RUTIS4_DETERMINANT returns the determinant of the RUTIS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real VALUE, the determinant.
#
  import numpy as np

  value = 1.0

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( 2 * ( n + 1 ) )
    value = value * 64.0 * ( np.cos ( angle ) ) ** 6

  return value

def rutis4_eigenvalues ( n ):

#*****************************************************************************80
#
## RUTIS4_EIGENVALUES returns the eigenvalues of the RUTIS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( 2 * ( n + 1 ) )
    lam[i] = 64.0 * ( np.cos ( angle ) ) ** 6

  return lam

def rutis4_inverse ( n ):

#*****************************************************************************80
#
## RUTIS4_INVERSE returns the inverse of the RUTIS4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from oto import oto_inverse
  from r8mat_mm import r8mat_mm

  c = oto_inverse ( n )

  b = r8mat_mm ( n, n, n, c, c )

  a = r8mat_mm ( n, n, n, c, b )

  return a

def rutis4_test ( ):

#*****************************************************************************80
#
## RUTIS4_TEST tests RUTIS4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'RUTIS4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RUTIS4 computes the RUTIS4 matrix.' )

  n = 5
  a = rutis4 ( n )
  r8mat_print ( n, n, a, '  RUTIS4 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'RUTIS4_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rutis4_test ( )
  timestamp ( )
