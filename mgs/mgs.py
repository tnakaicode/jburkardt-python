#! /usr/bin/env python3
#
def mgs_test ( ):

#*****************************************************************************80
#
## mgs_test() tests mgs().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'mgs_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test mgs():' )
#
#  Test the undocumented code.
#
  mgs_undoc_test ( )
#
#  Test the documented code.
#
  mgs_doc_test ( )
#
#  Test the vectorized code.
#
  mgs_vector_test ( )
#
#  Compare codes.
#
  mgs_comparison_test ( )
#
#  Time the codes.
#
  mgs_timing_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'mgs_test():' )
  print ( '  Normal end of execution.' )

  return

def mgs_undoc_test ( ):

#*****************************************************************************80
#
## mgs_undoc_test() tests mgs_undoc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'mgs_undoc_test():' )
  print ( '  mgs_undoc() is an undocumented function.' )
  print ( '  This code does a test on it.' )

  rng = default_rng ( )

  m = 200
  n = 50
  A = rng.random ( size = [ m, n ] )

  Q, R = mgs_undoc ( A )
  A2 = np.matmul ( Q, R )
  diff = np.linalg.norm ( A - A2, 'fro' )

  print ( '  A is a random ', m, ' by ', n, ' matrix.' )
  print ( '  mgs() computes factors Q and R.' )
  print ( '  Q is an ', m, ' by ', m, ' orthogonal matrix.' )
  print ( '  R is an ', m, ' by ', n, ' upper triangular matrix.' )
  print ( '  Frobenius norm of A - Q * R = ', diff )

  return

def mgs_undoc(A):

#*****************************************************************************80
#
## mgs_undoc() is an undocumented function.
#
  import numpy as np

  Atype = A.dtype

  A2 = A.copy()
  A2 = A2.astype ( Atype )

  m, n = A2.shape

  q = np.zeros ( [ m, n ], dtype = Atype )
  r = np.zeros ( [ n, n ], dtype = Atype )
  x = np.zeros ( m, dtype = Atype )

  for k in range ( 0, n ):

    for j in range ( 0, m ):
      x[j] = A2[j,k]
    xn = 0
    for j in range ( 0, m ):
      xn = xn + x[j]*x[j]
    r[k,k] = np.sqrt(xn)
    for j in range ( 0, m ):
      q[j,k] = A2[j,k]/r[k,k]
    for j in range ( k + 1, n ):
      r[k,j] = 0
      for p in range ( 0, m ):
        r[k,j] = r[k,j] + np.dot ( q[p,k], A2[p,j] )
      for p in range ( 0, m ):
        A2[p,j] = A2[p,j] - q[p,k]*r[k,j]

  return q, r

def mgs_doc_test ( ):

#*****************************************************************************80
#
## mgs_doc_test() tests mgs_doc().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'mgs_doc_test():' )
  print ( '  mgs_doc() is a documented function.' )
  print ( '  This code does a test on it.' )

  rng = default_rng ( )

  m = 200
  n = 50
  A = rng.random ( size = [ m, n ] )

  Q, R = mgs_doc ( A )
  A2 = np.matmul ( Q, R )
  diff = np.linalg.norm ( A - A2, 'fro' )

  print ( '  A is a random ', m, ' by ', n, ' matrix.' )
  print ( '  mgs() computes factors Q and R.' )
  print ( '  Q is an ', m, ' by ', m, ' orthogonal matrix.' )
  print ( '  R is an ', m, ' by ', n, ' upper triangular matrix.' )
  print ( '  Frobenius norm of A - Q * R = ', diff )

  return

def mgs_doc ( A ):

#*****************************************************************************80
#
## mgs_doc() implements the modified Gram Schmidt algorithm.
#
#  Discussion:
#
#    The function implements the Modified-Gram-Schmidt algorithm.
#    Given an m x n matrix C, modified Gram-Schmidt decomposes C such that
#    C = q*r, where q is an m x n orthogonal matrix and r is an n x n
#    upper triangular matrix.
#  
#    Documentation added by Dianne O'Leary, 09/2005
#
#  Reference: 
#
#    Golub and van Loan,
#    Matrix Computations,
#    Section 5.2.8
#
#  Author: 
#
#    Unknown, code written before 1995
#
  import numpy as np
#
#  Determine the size of the input matrix C.
#
  m, n = A.shape
  Atype = A.dtype
#
#  For each column of C, 
#  determine the component orthogonal to all previous columns,
#  normalize to length 1,
#  and store it in the corresponding column of q.

  A2 = A.copy ( )
  A2 = A2.astype ( Atype )
  Q = np.zeros ( [ m, m ], dtype = Atype )
  R = np.zeros ( [ m, n ], dtype = Atype )
  x = np.zeros ( m, dtype = Atype )
#
#  k records the index of the column of C under consideration.
#
  for k in range ( 0, n ):
#
#  Copy the k-th column of C into the vector x.
#
    for j in range ( 0, m ):
      x[j] = A2[j,k]
#
#  Compute xn, the Euclidean norm of x.
#
    xn = 0.0
    for j in range ( 0, m ):
      xn = xn + x[j] * x[j]
#
#  Set the (k,k) element of r to this norm and set the k-th column of q
#  to the k-th column of C, normalized to length 1.
#
    R[k,k] = np.sqrt ( xn )
    for j in range ( 0, m ):
      Q[j,k] = A2[j,k] / R[k,k]
#
#  Take the inner product of each of the later columns of C with this
#  new vector.  Record the inner products in row k of r, and modify the
#  columns of C to make them orthogonal to the new vector.
#
    for j in range ( k + 1, n ):
      R[k,j] = 0.0
      for p in range ( 0, m ):
        R[k,j] = R[k,j] + np.dot ( Q[p,k], A2[p,j] )

      for p in range ( 0, m ):
        A2[p,j] = A2[p,j] - Q[p,k] * R[k,j]

  return Q, R

def mgs_vector_test ( ):

#*****************************************************************************80
#
## mgs_vector_test() tests mgs_vector().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 October 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'mgs_vector_test():' )
  print ( '  mgs_vector() is a vectorized function.' )
  print ( '  This code does a test on it.' )

  rng = default_rng ( )

  m = 200
  n = 50
  A = rng.random ( size = [ m, n ] )

  Q, R = mgs_vector ( A )
  A2 = np.matmul ( Q, R )
  diff = np.linalg.norm ( A - A2, 'fro' )

  print ( '  A is a random ', m, ' by ', n, ' matrix.' )
  print ( '  mgs() computes factors Q and R.' )
  print ( '  Q is an ', m, ' by ', m, ' orthogonal matrix.' )
  print ( '  R is an ', m, ' by ', n, ' upper triangular matrix.' )
  print ( '  Frobenius norm of A - Q * R = ', diff )

  return

def mgs_vector ( A ):

#*****************************************************************************80
#
## mgs_vector() factors A=Q*R, using a vectorized algorithm.
#
#  Discussion:
#
#    Given m x n matrix A, the modified Gram-Schmidt algorithm computes
#    matrix factors Q and R such that:
#      A = Q*R, 
#    where Q is an m x min(m,n) orthogonal matrix
#    and R is an min(m,n) x n upper triangular matrix.
#
#  Author:
#
#    Dianne O'Leary, 09/2005
#
#  Reference: 
#
#    Golub and van Loan, Matrix Computations, Sec 5.2.8
#
  import numpy as np
#
#  Determine the matrix shape.
#
  m, n = A.shape
  Atype = A.dtype
#
#  Allocate storage.
#
  A2 = A.copy()
  A2 = A2.astype ( Atype )
  Q = np.zeros ( [ m, min ( m, n ) ], dtype = Atype )
  R = np.zeros ( [ min ( m, n ), n ], dtype = Atype )
#
#  Consider column k of A (k=1:min(m,n)),
#  Store it in column k of Q, after normalizing to length 1.
#  Orthogonalize each of the later columns of A against it,
#  saving the inner products in the k-th row of R.
#
  for k in range ( 0, min ( m, n ) ):
    R[k,k] = np.linalg.norm ( A2[:,k] )
    Q[:,k] = A2[:,k] / R[k,k]
    for j in range ( k + 1, n ):
      R[k,j] = np.dot ( np.conj ( Q[:,k] ), A2[:,j] )
      A2[:,j] = A2[:,j] - Q[:,k] * R[k,j]

  return Q, R

def mgs_comparison_test ( ):

#*****************************************************************************80
#
## mgs_comparison_test() tests mgs() and mgsfact() and compares with qr().
#
#  Discussion:
#
#    Test for orthogonality of Q, and accuracy of A-Q*R:
#    1.  A random 7x5 real matrix.
#    2.  A random 3x5 real matrix
#    3.  A random 8x4 complex matrix.
#
#  Modified:
#
#    23 October 2024
#
#  Author:
#
#    Original MATLAB version by Dianne O'Leary.
#    This version by John Burkardt.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'mgs_comparison_test():' )
  print ( '  Compare mgs_undoc(), mgs_doc(), mgs_vector() and np.linalg.qr() algorithms.' )
#
#  Test 1:
#
  print ( '' )
  print ( '  Test #1: 7x5 real matrix.' )
  print ( '  Algorithm     norm(Q^T*Q-I)    norm(Q*R-A)' )

  A = rng.random ( size = [ 7, 5 ] )

  m1, n1 = A.shape
  [ q1, r1 ] = mgs_undoc ( A )
  [ q2, r2 ] = mgs_undoc ( A )
  [ q3, r3 ] = mgs_vector ( A )
  [ q4, r4 ] = np.linalg.qr ( A )

  e1 = np.linalg.norm ( np.matmul ( q1.T, q1 ) - np.identity ( n1 ) )
  e2 = np.linalg.norm ( np.matmul ( q1, r1 ) - A, 'fro' )
  print ( '   mgs_undoc     %e     %e' % ( e1, e2 ) )

  e1 = np.linalg.norm ( np.matmul ( q2.T, q2 ) - np.identity ( n1 ) )
  e2 = np.linalg.norm ( np.matmul ( q2, r2 ) - A, 'fro' )
  print ( '   mgs_doc       %e     %e' % ( e1, e2 ) )

  e1 = np.linalg.norm ( np.matmul ( q3.T, q3 ) - np.identity ( n1 ) )
  e2 = np.linalg.norm ( np.matmul ( q3, r3 ) - A, 'fro' )
  print ( '   mgs_vector    %e     %e' % ( e1, e2 ) )

  e1 = np.linalg.norm ( np.matmul ( q4.T, q4 ) - np.identity ( n1 ) )
  e2 = np.linalg.norm ( np.matmul ( q4, r4 ) - A, 'fro' )
  print ( '   np.linalg.qr  %e     %e' % ( e1, e2 ) )
#
#  Test 2
#
  print ( '' )
  print ( '  Test #2: 3x5 real matrix.' )

  A = rng.random ( size = [ 3, 5 ] )
  m1, n1 = A.shape
  mn = min ( m1, n1 )

  [ q1, r1 ] = mgs_undoc ( A )
  [ q2, r2 ] = mgs_undoc ( A )
  [ q3, r3 ] = mgs_vector ( A )
  [ q4, r4 ] = np.linalg.qr ( A )

  print ( '  Algorithm     norm(Q^T*Q-I)    norm(Q*R-A)' )

  e1 = np.linalg.norm ( np.matmul ( q1.T[0:mn,0:mn], q1[0:mn,0:mn] ) \
    - np.identity ( mn ) )
  e2 = np.linalg.norm ( np.matmul ( q1, r1 ) - A, 'fro' )
  print ( '   mgs_undoc     %e     %e' % ( e1, e2 ) )

  e1 = np.linalg.norm ( np.matmul ( q2.T[0:mn,0:mn], q2[0:mn,0:mn] ) \
    - np.identity ( mn ) )
  e2 = np.linalg.norm ( np.matmul ( q2, r2 ) - A, 'fro' )
  print ( '   mgs_doc       %e     %e' % ( e1, e2 ) )

  e1 = np.linalg.norm ( np.matmul ( q3.T, q3 ) \
    - np.identity ( min ( m1, n1 ) ) )
  e2 = np.linalg.norm ( np.matmul ( q3, r3 ) - A, 'fro' )
  print ( '   mgs_vector    %e     %e' % ( e1, e2 ) )

  e1 = np.linalg.norm ( np.matmul ( q4.T, q4 ) \
    - np.identity ( min ( m1, n1 ) ) )
  e2 = np.linalg.norm ( np.matmul ( q4, r4 ) - A, 'fro' )
  print ( '   np.linalg.qr  %e     %e' % ( e1, e2 ) )
#
#  Test 3
#
  print ( '' )
  print ( '  Test #3: 8x4 complex matrix.' )

  A = rng.random ( size = [ 8, 4 ] ) + rng.random ( size = [ 8, 4 ] ) * 1j
  m1, n1 = A.shape
  [ q1, r1 ] = mgs_undoc ( A )
  [ q2, r2 ] = mgs_undoc ( A )
  [ q3, r3 ] = mgs_vector ( A )
  [ q4, r4 ] = np.linalg.qr ( A )

  print ( '  Algorithm     norm(Q^T*Q-I)    norm(Q*R-A)' )

  e1 = np.linalg.norm ( np.matmul ( q1.T, q1 ) - np.identity ( n1 ) )
  e2 = np.linalg.norm ( np.matmul ( q1, r1 ) - A, 'fro' )
  print ( '   mgs_undoc     %e     %e' % ( e1, e2 ) )

  e1 = np.linalg.norm ( np.matmul ( q2.T, q2 ) - np.identity ( n1 ) )
  e2 = np.linalg.norm ( np.matmul ( q2, r2 ) - A, 'fro' )
  print ( '   mgs_doc       %e     %e' % ( e1, e2 ) )

  e1 = np.linalg.norm ( np.matmul ( np.conj(q3.T), q3 ) - np.identity ( n1 ) )
  e2 = np.linalg.norm ( np.matmul ( q3, r3 ) - A, 'fro' )
  print ( '   mgs_vector    %e     %e' % ( e1, e2 ) )

  e1 = np.linalg.norm ( np.matmul ( np.conj(q4.T), q4 ) - np.identity ( n1 ) )
  e2 = np.linalg.norm ( np.matmul ( q4, r4 ) - A, 'fro' )
  print ( '   np.linalg.qr  %e     %e' % ( e1, e2 ) )

  return

def mgs_timing_test ( ):

#*****************************************************************************80
#
## mgs_timing does timing comparisons between mgs and mgs_fact.
#
#  Discussion:
#
#    This program compares the execution time of mgs.m to mgs_fact.m
#    on matrices with 200 rows and various numbers of columns ranging
#    from 50 to 200 in steps of 10.
#
#    The results are saved in a plot.
#
#  Modified:
#
#    24 October 2024
#
#  Author:
#
#    Dianne O'Leary 09/2005
#
  from numpy.random import default_rng
  from time import time
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'mgs_timing_test():' )
  print ( '  Compare timings of mgs algorithms.' )

  m = 200
  rng = default_rng ( )

  print ( '' )
  print ( '  n  mgs_undoc  mgs_doc  mgs_vector  np.linalg.qr' )
  print ( '' )

  j = 0
  
  n_num = 16
  nsizes = np.array ( [ \
     50,  60,  70,  80,  90, \
    100, 110, 120, 130, 140, \
    150, 160, 170, 180, 190, \
    200 ] )

  t1 = np.zeros ( n_num )
  t2 = np.zeros ( n_num )
  t3 = np.zeros ( n_num )
  t4 = np.zeros ( n_num )

  for j in range ( 0, n_num ):

    n = nsizes[j]

    A = rng.random ( size = [ m, n ] )

    seconds = time ( )
    Q, R = mgs_undoc ( A )
    t1[j] = time ( ) - seconds
    seconds = time ( )
    Q, R = mgs_doc ( A )
    t2[j] = time ( ) - seconds
    seconds = time ( )
    Q, R = mgs_vector ( A )
    t3[j] = time ( ) - seconds
    seconds = time ( )
    Q, R = np.linalg.qr ( A )
    t4[j] = time ( ) - seconds

    print ( '%3d  %8.4e  %8.4e  %8.4e  %8.4e' \
      % ( nsizes[j], t1[j], t2[j], t3[j], t4[j] ) )
#
#  Make a plot.
#
  plt.clf ( )
  plt.semilogy ( nsizes, t1 )
  plt.semilogy ( nsizes, t2 )
  plt.semilogy ( nsizes, t3 )
  plt.semilogy ( nsizes, t4 )
  plt.xlabel ( 'n = number of columns' )
  plt.ylabel ( 'time (sec)' )
  plt.title ( 'Times for matrices with m=200 rows' )
  plt.grid ( )
  plt.legend ( [ 'mgs_undoc', 'mgs_doc', 'mgs_vector', 'np.linalg.qr' ] )

  filename = 'mgs_timing.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

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
  mgs_test ( )
  timestamp ( )

