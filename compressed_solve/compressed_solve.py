#! /usr/bin/env python3
#
def compressed_solve_test ( ):

#*****************************************************************************80
#
## compressed_solve_test() tests compressed_solve().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 March 2026
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform
  import pprint
  import scipy as sp
 
  print ( '' )
  print ( 'compressed_solve_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  scipy version:  ' + sp.version.version )
  print ( '  Test compressed_solve(), which seeks a solution of an' )
  print ( '  underdetermined linear system A*x=b, with the maximum' )
  print ( '  number of zero entries in x.' )

  A = np.array ( [ \
    [ 87, 190, 118, 140, 101 ], \
    [ 72, 170,  90, 135, 104 ], \
    [ 12,  31,  14,  25,  20 ] ] )

  print ( '' )
  print ( '  matrix A:' )
  pprint.pprint ( A )

  b = np.array ( [ 5, 10, 8 ] )
  print ( '' )
  print ( '  right hand side b:' )
  pprint.pprint ( b )

  x1 = compressed_solve ( A, b )
  print ( '' )
  print ( '  compressed solve x1:' )
  pprint.pprint ( x1 )
#
#  Compare with default least squares solver.
#
  x2, _, _, _ = np.linalg.lstsq ( A, b, rcond = None )
  print ( '' )
  print ( '  np.linalg.lstsq() x2:' )
  pprint.pprint ( x2 )

  return

def compressed_solve ( A, b ):

#*****************************************************************************80
#
## compressed_solve() seeks a solution to an underdetermined system with maximal zeros.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(m,n): the matrix.  It must be the case that m <= n.
#
#    real b(m): the right hand side.
#
#  Output:
#
#    real x(n): a solution of the system A*x=b, with the maximal number
#    of zero entries.
#
  from scipy.linalg import qr
  import numpy as np

  m, n = A.shape
#
#  Get the QR factorization, with pivoting: A(:,P) = Q * R
#  P is a reordering of the columns of A which reduces fillin in R.
#
  Q, R, p = qr ( A, pivoting = True )
#
#  Form and solve the reduced system:
#
  r = np.linalg.matrix_rank ( A )
  y = np.matmul ( np.transpose ( Q[:,0:r] ), b )
#
#  Start with a full vector of zeros.
#  Compute the solution of the reduced system and patch it into the full vector.
#
  x = np.zeros ( n )
  x[p[0:r]] = np.linalg.solve ( R[0:r,0:r], y )

  return x

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
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  compressed_solve_test ( )
  timestamp ( )

