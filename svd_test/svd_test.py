#! /usr/bin/env python3
#
def svd_test ( ):

#*****************************************************************************80
#
## svd_test tests svd().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modififed:
#
#    11 December 2018
#
#  Author:
#
#    John Burkardt
#
#  Local:
#
#    real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    integer M, N, the number of rows and columns of the matrix.  
#
#    real S(M,N), the diagonal factor
#    int the singular value decomposition of A.
#
#    real U(M,M), the first orthogonal factor
#    in the singular value decomposition of A.
#
#    real V(N,N), the second orthogonal factor
#    in the singular value decomposition of A.
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  rng = default_rng ( )

  m = 3
  n = 3

  print ( '' )
  print ( 'svd_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  svd() carries out the singular value decomposition.' )
  print ( '' )
  print ( '  A real MxN matrix A can be factored as:' )
  print ( '' )
  print ( '    A = U * S * V''' )
  print ( '' )
  print ( '  where' )
  print ( '' )
  print ( '    U = MxM orthogonal,' )
  print ( '    S = MxN zero except for diagonal,' )
  print ( '    V = NxN orthogonal.' )
  print ( '' )
  print ( '  The diagonal of S contains only nonnegative numbers' )
  print ( '  and these are arranged in descending order.' )
#
#  If at least one command line argument, it's M.
#
  print ( '' )
  print ( '  Matrix row order    M = ', m )
  print ( '  Matrix column order N = ', n )
#
#  Generate the matrix A.
#
  print ( '' )
  print ( '  We choose a "random" matrix A, with integral' )
  print ( '  values between 0 and 10.' )

  a = rng.random ( size = [ m, n ] )

  a = np.round ( 10.0 * a )

  r8mat_print ( m, n, a, '  The matrix A:' )
#
#  Get the SVD.
#
  u, svec, v = np.linalg.svd ( a )
#
#  Note that Numpy's SVD has A=U*S*V, NOT A=U*S*V'.
#
  v = v.transpose ( )
#
#  Inflate SVEC to a matrix.
#
  s = np.zeros ( [ m, n ] )
  for ij in range ( 0, min ( m, n ) ):
    s[ij,ij] = svec[ij];
#
#  Print the SVD.
#
  r8mat_print ( m, m, u, '  The orthogonal factor U:' )
  r8mat_print ( m, n, s, '  The diagonal factor S:' )
  r8mat_print ( n, n, v, '  The orthogonal factor V:' )
#
#  Check that A = U * S * V'.
#
  svd_product_test ( m, n, a, u, s, v )
#
#  Compute the norm of the difference between A and the successive
#  sums of rank one approximants.
#
  rank_one_test ( m, n, a, u, s, v )
#
#  Actually print the sums of rank one approximants.
#
  rank_one_print_test ( m, n, a, u, s, v )
#
#  Compute the pseudoinverse.
#
  a_pseudo = pseudo_inverse ( m, n, u, s, v )

  r8mat_print ( n, m, a_pseudo, '  The pseudoinverse of A:' )
#
#  Test A*A+ = I+, A+*A = I+
#
  pseudo_product_test ( m, n, a, a_pseudo )
#
#  Demonstrate the use of the pseudoinverse for linear systems.
#
  pseudo_linear_solve_test ( m, n, a, a_pseudo, rng )
#
#  Terminate.
#
  print ( '' )
  print ( 'svd_test():' )
  print ( '  Normal end of execution.' )
  
  return

def pseudo_inverse ( m, n, u, s, v ):

#*****************************************************************************80
#
## pseudo_inverse() computes the pseudoinverse.
#
#  Discussion:
#
#    Given the singular value decomposition of a real MxN matrix A:
#
#      A = U * S * V'
#
#    where 
#
#      U is MxM orthogonal,
#      S is MxN, and entirely zero except for the diagonal
#      V is NxN orthogonal.
#
#    the pseudo inverse is the NxM matrix A+ with the form
#
#      A+ = V * S+ * U'
#
#    where 
#
#      S+ is the NxM matrix whose nonzero diagonal elements are
#      the inverses of the corresponding diagonal elements of S.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 December 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the matrix A.
#
#    real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    real U(M,M), S(M,N), V(N,N), the factors
#    that form the singular value decomposition of A.
#
#  Output:
#
#    real A_PSEUDO(N,M), the pseudoinverse of A.
#
  import numpy as np

  sp = np.zeros ( [ n, m ] )

  for i in range ( 0, min ( m, n ) ):
    if ( s[i,i] != 0.0 ):
      sp[i,i] = 1.0 / s[i,i]

  a_pseudo = np.matmul ( v, np.matmul ( sp, u.transpose() ) )

  return a_pseudo

def pseudo_linear_solve_test ( m, n, a, a_pseudo, rng ):

#*****************************************************************************80
#
## pseudo_linear_solve_test() uses the pseudoinverse for linear systems.
#
#  Discussion:
#
#    Given an MxN matrix A, and its pseudoinverse A+:
#
#      "Solve" A  * x = b by x = A+  * b.
#
#      "Solve" A' * x = b by x = A+' * b.
#
#    When the system is overdetermined, the solution minimizes the
#    L2 norm of the residual.  
#
#    When the system is underdetermined, the solution
#    is the solution of minimum L2 norm.     
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 December 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the matrix A.
#
#    real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    real A_PSEUDO(N,M), the pseudo_inverse of A.
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'pseudo_linear_solve_test():' )
#
#  A * x = b, b in range of A.
#
  xn1 = rng.random ( size = n )
  xn1 = np.round ( 10.0 * xn1 )
  bm = np.dot ( a, xn1 )
  xn2 = np.dot ( a_pseudo, bm )
  rm = np.dot ( a, xn2 ) - bm

  print ( '' )
  print ( '  Given:' )
  print ( '    b = A * x1' )
  print ( '  so that b is in the range of A, solve' )
  print ( '    A * x = b' )
  print ( '  using the pseudoinverse:' )
  print ( '    x2 = A+ * b.' )
  print ( '' )
  print ( '  Norm of x1 =       %f' % ( np.linalg.norm ( xn1 ) ) )
  print ( '  Norm of x2 =       %f' % ( np.linalg.norm ( xn2 ) ) )
  print ( '  Norm of residual = %f' % ( np.linalg.norm ( rm ) ) )
#
#  A * x = b, b not in range of A.
#
  if ( n < m ):

    print ( '' )
    print ( '  For N < M, most systems A*x=b will not be' )
    print ( '  exactly and uniquely solvable, except in the' )
    print ( '  least squares sense.' )
    print ( '' )
    print ( '  Here is an example:' )

    b8 = rng.random ( size = m )
    xn2 = np.dot ( a_pseudo, bm )
    rm = np.dot ( a, xn2 ) - bm

    print ( '' )
    print ( '  Given b is NOT in the range of A, solve' )
    print ( '    A * x = b' )
    print ( '  using the pseudoinverse:' )
    print ( '    x2 = A+ * b.' )
    print ( '' )
    print ( '  Norm of x2 =       %f' % ( np.linalg.norm ( xn2 ) ) )
    print ( '  Norm of residual = %f' % ( np.linalg.norm ( rm ) ) )
#
#  A' * x = b, b is in the range of A'.
#
  xm1 = rng.random ( size = m )
  xm1 = np.round ( 10.0 * xm1 )
  bn = np.dot ( a.transpose(), xm1 )
  xm2 = np.dot ( a_pseudo.transpose ( ), bn )
  rn = np.dot ( a.transpose ( ), xm2 ) - bn

  print ( '' )
  print ( '  Given:' )
  print ( '    b = A'' * x1' )
  print ( '  so that b is in the range of A'', solve' )
  print ( '    A'' * x = b' )
  print ( '  using the pseudoinverse:' )
  print ( '    x2 = A+'' * b.' )
  print ( '' )
  print ( '  Norm of x1 =       %f' % ( np.linalg.norm ( xm1 ) ) )
  print ( '  Norm of x2 =       %f' % ( np.linalg.norm ( xm2 ) ) )
  print ( '  Norm of residual = %f' % ( np.linalg.norm ( rn ) ) )
#
#  A' * x = b, b is not in the range of A'.
#
  if ( m < n ):

    print ( '' )
    print ( '  For M < N, most systems A''*x=b will not be' )
    print ( '  exactly and uniquely solvable, except in the' )
    print ( '  least squares sense.' )
    print ( '' )
    print ( '  Here is an example:' )

    bn = rng.random ( size = n )
    xm2 = np.dot ( a_pseudo.transpose () * bn )
    rn = np.dot ( a.transpose(), xm2 ) - bn

    print ( '' )
    print ( '  Given b is NOT in the range of A'', solve' )
    print ( '    A'' * x1 = b' )
    print ( '  using the pseudoinverse:' )
    print ( '    x2 = A+'' * b.' )
    print ( '' )
    print ( '  Norm of x2 =       %f' % ( np.linalg.norm ( xm2 ) ) )
    print ( '  Norm of residual = %f' % ( np.linalg.norm ( rn ) ) )

  return

def pseudo_product_test ( m, n, a, a_pseudo ):

#*****************************************************************************80
#
## pseudo_product_test() examines the products A*A+ and A+*A.
#
#  Discussion:
#
#    Given an MxN matrix A, and its pseudoinverse A+, we must have
#
#      A+ * A * A+ = A+
#      A * A+ * A = A
#      ( A * A+ )' = A * A+ (MxM symmetry)
#      ( A+ * A )' = A+ * A (NxN symmetry)
#
#    If M <= N, A * A+ may be "interesting" (equal to or "like" the identity),
#    if N <= M, A+ * A may be "interesting" (equal to or "like" the identity).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 December 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the matrix A.
#
#    real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    real A_PSEUDO(N,M), the pseudo_inverse of A.
#
  import numpy as np

  print ( '' )
  print ( 'pseudo_product_test():' )
  print ( '' )
  print ( '  The following relations MUST hold:' )
  print ( '' )
  print ( '   A  * A+ * A  = A' )
  print ( '   A+ * A  * A+ = A+' )
  print ( ' ( A  * A+ ) is MxM symmetric' )
  print ( ' ( A+ * A  ) is NxN symmetric' )

  bmn = np.matmul ( a, np.matmul ( a_pseudo, a ) )

  dif1 = np.linalg.norm ( a - bmn, ord = 'fro' )

  bnm  = np.matmul ( a_pseudo, np.matmul ( a, a_pseudo ) )

  dif2 = np.linalg.norm ( a_pseudo - bnm, ord = 'fro' )

  bmm = np.matmul ( a, a_pseudo ) 

  dif3 = np.linalg.norm ( bmm - bmm.transpose(), ord = 'fro' )

  bnn = np.matmul ( a_pseudo, a )

  dif4 = np.linalg.norm ( bnn - bnn.transpose(), ord = 'fro' )

  print ( '' )
  print ( '  Here are the Frobenius norms of the errors' )
  print ( '  in these relationships:' )
  print ( '' )
  print ( '   A  * A+ * A  = A           %f' % ( dif1 ) )
  print ( '   A+ * A  * A+ = A+          %f' % ( dif2 ) )
  print ( ' ( A  * A+ ) is MxM symmetric %f' % ( dif3 ) )
  print ( ' ( A+ * A  ) is NxN symmetric %f' % ( dif4 ) )

  print ( '' )
  print ( '  In some cases, the matrix A * A+' )
  print ( '  may be interesting (if M <= N, then' )
  print ( '  it MIGHT look like the identity.)' )

  r8mat_print ( m, m, bmm, '  A * A+:' )

  print ( '' )
  print ( '  In some cases, the matrix A+ * A' )
  print ( '  may be interesting (if N <= M, then' )
  print ( '  it MIGHT look like the identity.)' )

  r8mat_print ( n, n, bnn, '  A+ * A' )

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
#    31 August 2014
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
#    10 February 2015
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

def rank_one_test ( m, n, a, u, s, v ):

#*****************************************************************************80
#
## rank_one_test() compares A to the sum of rank one matrices.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    08 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the matrix A.
#
#    real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    real U(M,M), S(M,N), V(N,N), the factors
#    that form the singular value decomposition of A.
#
  import numpy as np

  a_norm = np.linalg.norm ( a, ord = 'fro' )

  print ( '' )
  print ( 'rank_one_test():' )
  print ( '  Compare A to the sum of R rank one matrices.' )
  print ( '' )
  print ( '         R    Absolute      Relative' )
  print ( '              Error         Error' )
  print ( '' )

  for r in range ( 0, min ( m, n ) + 1 ):

    if ( r == 0 ):
      usv = np.zeros ( [ m, n ] )
    else:
      usv = np.matmul ( u[:,0:r], np.matmul ( s[0:r,0:r],  v[0:n,0:r].transpose() ) )

    dif_norm = np.linalg.norm ( a - usv, ord = 'fro' )

    print ( '  %8d  %14f  %14f' % ( r, dif_norm, dif_norm / a_norm ) )

  return

def rank_one_print_test ( m, n, a, u, s, v ):

#*****************************************************************************80
#
## rank_one_print_test() prints the sums of rank one matrices.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the matrix A.
#
#    real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    real U(M,M), S(M,N), V(N,N), the factors
#    that form the singular value decomposition of A.
#
  import numpy as np

  a_norm = np.linalg.norm ( a, ord = 'fro' )

  print ( '' )
  print ( 'rank_one_print_test():' )
  print ( '  Print the sums of R rank one matrices.' )

  for r in range ( 0, min ( m, n ) + 1 ):

    if ( r == 0 ):
      usv = np.zeros ( [ m, n ] )
    else:
      usv = np.matmul ( u[:,0:r], np.matmul ( s[0:r,0:r],  v[0:n,0:r].transpose() ) )

    title = '  Rank R = %d' % ( r )
    r8mat_print ( m, n, usv, title )

  r8mat_print ( m, n, a, '  Original matrix A:' )

  return

def svd_product_test ( m, n, a, u, s, v ):

#*****************************************************************************80
#
## svd_product_test() tests that A = U * S * V'.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 December 2018
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns in the matrix A.
#
#    real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    real U(M,M), S(M,N), V(N,N), the factors
#    that form the singular value decomposition of A.
#
  import numpy as np

  print ( '' )
  print ( 'svd_product_test( ):' )
  print ( '  Compare A and U*S*V\'.' )

  a_norm = np.linalg.norm ( a, ord = 'fro' )

  usv = np.matmul ( u, np.matmul ( s, v.transpose() ) )

  r8mat_print ( m, n, usv, '  The product U * S * V''' )

  dif_norm = np.linalg.norm ( a - usv, 'fro' )

  print ( '' )
  print ( '  Frobenius Norm of A, A_NORM = %f' % ( a_norm ) )
  print ( '' )
  print ( '  ABSOLUTE ERROR for A = U*S*V\':' )
  print ( '  Frobenius norm of difference A-U*S*V\' = %f' % ( dif_norm ) )
  print ( '' )
  print ( '  RELATIVE ERROR for A = U*S*V\':' )
  print ( '  Ratio of DIF_NORM / A_NORM = %f' % ( dif_norm / a_norm ) )

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
  svd_test ( )
  timestamp ( )
 
