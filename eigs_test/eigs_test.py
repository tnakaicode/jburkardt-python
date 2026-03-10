#! /usr/bin/env python3
#
def eigs_test ( ):

#*****************************************************************************80
#
## eigs_test() tests np.linalg.eig().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'eigs_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test np.linalg.eig(), a built-in function for computing' )
  print ( '  eigenvalues and eigenvectors.' )

  eigs_symmetric_test ( rng )
  eigs_nonsymmetric_test ( rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'eigs_test():' )
  print ( '  Normal end of execution.' )

  return

def eigs_nonsymmetric_test ( rng ):

#*****************************************************************************80
#
## eigs_nonsymmetric_test() tests eigs() on a nonysymmetric matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2018
#
#  Author:
#
#    John Burkardt
#
  import sys
  sys.path.insert ( 0, '/home/john/public_html/py_src/test_eigen' )

  from numpy.linalg import eig
  from test_eigen import r8nsymm_gen
  import numpy as np

  n = 5
  lamda_dev = 5.0
  lamda_mean = 10.0

  print ( '' )
  print ( 'eigs_nonsymmetric_test():' )
  print ( '  Test eigs() on a nonsymmetric matrix.' )

  A, Q, T = r8nsymm_gen ( n, lamda_mean, lamda_dev, rng )
#
#  Print the matrix.
#
  print ( '' )
  print ( '  Real nonsymmetric test matrix A:' )
  print ( A )

  print ( '' )
  print ( '  Orthogonal factor Q:' )
  print ( Q )

  print ( '' )
  print ( '  Schur upper triangle T:' )
  print ( T )

  lamda = np.diag ( T )
  lamda = np.sort ( lamda )
  print ( '' )
  print ( '  Sorted eigenvalues lamda:' )
  print ( lamda )
#
#  Call eigs.
#
  lamda2, Q2 = eig ( A )

  print ( '' )
  print ( '  Computed eigenvectors Q2:' )
  print ( Q2 )

  lamda2 = np.sort ( lamda2 )
  print ( '' )
  print ( '  Computed eigenvalues lamda2:' )
  print ( lamda2 )
#
#  Errors.
#
  lamda_error = np.linalg.norm ( lamda - lamda2 )
  print ( '' )
  print ( '  Norm of eigenvalue error = ', lamda_error )

  return

def eigs_symmetric_test ( rng ):

#*****************************************************************************80
#
## eigs_symmetric_test() tests eigs() on a symmetric matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 June 2024
#
#  Author:
#
#    John Burkardt
#
  import sys
  sys.path.insert ( 0, '/home/john/public_html/py_src/test_eigen' )

  from numpy.linalg import eig
  from test_eigen import r8symm_gen
  import numpy as np

  n = 5
  lamda_dev = 5.0
  lamda_mean = 10.0
 
  print ( '' )
  print ( 'eigs_symmetric_test():' )
  print ( '  Test eigs() on a real symmetric matrix.' )
#
#  Generate a real symmetric test matrix with known eigenvalues and eigenvectors.
#
  A, Q, lamda = r8symm_gen ( n, lamda_mean, lamda_dev, rng )
#
#  Print the matrix.
#
  print ( '' )
  print ( '  Real symmetric test matrix A:' )
  print ( A )

  print ( '' )
  print ( '  Eigenvectors Q:' )
  print ( Q )

  lamda = np.sort ( lamda )
  print ( '' )
  print ( '  Eigenvalues lamda:' )
  print ( lamda )
#
#  Call eigs.
#
  lamda2, Q2 = eig ( A )

  print ( '' )
  print ( '  Computed eigenvectors Q2:' )
  print ( Q2 )

  lamda2 = np.sort ( lamda2 )
  print ( '' )
  print ( '  Computed eigenvalues lamda2:' )
  print ( lamda2 )
#
#  Errors.
#
  lamda_error = np.linalg.norm ( lamda - lamda2 )
  print ( '' )
  print ( '  Norm of eigenvalue error = ', lamda_error )

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
  eigs_test ( )
  timestamp ( )

