#! /usr/bin/env python
#
def r8mat_det ( n, a ):

#*****************************************************************************80
#
## R8MAT_DET finds the determinant of an R8MAT.
#
#  Discussion:
#
#    A brute force calculation is made.
#
#    This routine should only be used for small matrices, since this
#    calculation requires the summation of N! products of N numbers.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of rows and columns of A.
#
#    Input, real A(N,N), the matrix whose determinant is desired.
#
#    Output, real DET, the determinant of the matrix.
#
  import numpy as np
  from perm0_next import perm0_next

  det = 0.0

  p = np.zeros ( n )
  more = False
  even = False

  while ( True ):

    p, more, even = perm0_next ( n, p, more, even )

    if ( even ):
      term = 1.0
    else:
      term = -1.0

    for i in range ( 0, n ):
      term = term * a[i,p[i]]

    det = det + term

    if ( not more ):
      break

  return det

def r8mat_det_test ( ):

#*****************************************************************************80
#
## R8MAT_DET_TEST tests R8MAT_DET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'R8MAT_DET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_DET: determinant of a real matrix.' )
 
  n = 3
  a = np.zeros ( [ n, n ] )

  k = 0
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )
 
  r8mat_print ( n, n, a, '  The 123/456/789 matrix:' )

  det = r8mat_det ( n, a )
 
  print ( '' )
  print ( '  Determinant of the 123/456/789 matrix is %g' % ( det ) )
 
  n = 4
  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = 1.0 / float ( i + j + 2 )
 
  r8mat_print ( n, n, a, '  The Hilbert matrix:' )

  det = r8mat_det ( n, a )
 
  print ( '' )
  print ( '  Determinant of the Hilbert matrix is %g' % ( det ) )
 
  n = 3
  a = np.zeros ( [ n, n ] )
 
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( i == j + 1 or i == j - 1 ):
        a[i,j] = -1.0
      else:
        a[i,j] = 0.0
 
  r8mat_print ( n, n, a, '  The -1,2,-1 matrix:' )

  det = r8mat_det ( n, a )
 
  print ( '' )
  print ( '  Determinant of the -1,2,-1 matrix is %g' % ( det ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_DET_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_det_test ( )
  timestamp ( )

