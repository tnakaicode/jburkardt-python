#! /usr/bin/env python3
#
def combin ( alpha, beta, n ):

#*****************************************************************************80
#
## COMBIN returns the COMBIN matrix.
#
#  Formula:
#
#    If ( I = J ) then
#      A(I,J) = ALPHA + BETA
#    else
#      A(I,J) = BETA
#
#  Example:
#
#    N = 5, ALPHA = 2, BETA = 3
#
#    5 3 3 3 3
#    3 5 3 3 3
#    3 3 5 3 3
#    3 3 3 5 3
#    3 3 3 3 5
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    det ( A ) = ALPHA^(N-1) * ( ALPHA + N * BETA ).
#
#    LAMBDA(1:N-1) = ALPHA,
#    LAMBDA(N) = ALPHA + N * BETA.
#
#    The eigenvector associated with LAMBDA(N) is (1,1,1,...,1)/sqrt(N).
#
#    The other N-1 eigenvectors are simply any (orthonormal) basis
#    for the space perpendicular to (1,1,1,...,1).
#
#    A is nonsingular if ALPHA /= 0 and ALPHA + N * BETA /= 0.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    Example 3.25,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 53,
#    LC: QA263.G68.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition,
#    Addison-Wesley, Reading, Massachusetts, 1973, page 36.
#
#  Parameters:
#
#    Input, real ALPHA, BETA, scalars that define A.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a[i,j] = beta
    a[j,j] = a[j,j] + alpha

  return a

def combin_condition ( alpha, beta, n ):

#*****************************************************************************80
#
## COMBIN_CONDITION returns the L1 condition of the COMBIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, BETA, scalars that define A.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real COND, the L1 condition.
#
  a_norm = abs ( alpha + beta ) + ( n - 1 ) * abs ( beta )

  b_norm_top = abs ( alpha + ( n - 1 ) * beta ) + ( n - 1 ) * abs ( beta )

  b_norm_bot = abs ( alpha * ( alpha + n * beta ) )

  b_norm = b_norm_top / b_norm_bot

  cond = a_norm * b_norm

  return cond

def combin_condition_test ( ):

#*****************************************************************************80
#
## COMBIN_CONDITION_TEST tests COMBIN_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'COMBIN_CONDITION_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  COMBIN_CONDITION computes the condition of the COMBIN matrix.' )

  seed = 123456789

  n = 3
  seed = 123456789
  alpha, seed = r8_uniform_01 ( seed )
  alpha = round ( 50.0 * alpha ) / 5.0
  beta, seed = r8_uniform_01 ( seed )
  beta = round ( 50.0 * beta ) / 5.0
  a = combin ( alpha, beta, n )
  r8mat_print ( n, n, a, '  COMBIN matrix:' )

  value = combin_condition ( alpha, beta, n )

  print ( '' )
  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'COMBIN_CONDITION_TEST' )
  print ( '  Normal end of execution.' )

  return

def combin_determinant ( alpha, beta, n ):

#*****************************************************************************80
#
## COMBIN_DETERMINANT computes the determinant of the COMBIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, BETA, scalars that define the matrix.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real DETERM, the determinant.
#
  determ = alpha ** ( n - 1 ) * ( alpha + n * beta )
 
  return determ

def combin_determinant_test ( ):

#*****************************************************************************80
#
## COMBIN_DETERMINANT_TEST tests COMBIN_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'COMBIN_DETERMINANT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  COMBIN_DETERMINANT computes the COMBIN determinant.' )

  m = 4
  n = 4
  seed = 123456789
  alpha, seed = r8_uniform_01 ( seed )
  alpha = round ( 50.0 * alpha ) / 5.0
  beta, seed = r8_uniform_01 ( seed )
  beta = round ( 50.0 * beta ) / 5.0
  a = combin ( alpha, beta, n )

  r8mat_print ( m, n, a, '  COMBIN matrix:' )

  value = combin_determinant ( alpha, beta, n )

  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'COMBIN_DETERMINANT_TEST' )
  print ( '  Normal end of execution.' )
  return

def combin_eigen_right ( alpha, beta, n ):

#*****************************************************************************80
#
## COMBIN_EIGEN_RIGHT returns the right eigenvectors of the COMBIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, BETA, scalars that define A.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real X(N,N), the right eigenvectors.
#
  import numpy as np

  x = np.zeros ( ( n, n ) )

  for j in range ( 0, n - 1 ):
    x[  0,j] = +1.0
    x[j+1,j] = -1.0

  j = n - 1
  for i in range ( 0, n ):
    x[i,j] = 1.0

  return x

def combin_eigenvalues ( alpha, beta, n ):

#*****************************************************************************80
#
## COMBIN_EIGENVALUES returns the eigenvalues of the COMBIN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, BETA, scalars that define A.
#
#    Input, integer N, the order of A.
#
#    Output, real LAM(N), the eigenvalues.
#
  import numpy as np

  lam = np.zeros ( n )

  for i in range ( 0, n - 1 ):
    lam[i] = alpha
  lam[n-1] = alpha + n * beta

  return lam

def combin_inverse ( alpha, beta, n ):

#*****************************************************************************80
#
## COMBIN_INVERSE returns the inverse of the combinatorial matrix A.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = (ALPHA+(N-1)*BETA) / (ALPHA*(ALPHA+N*BETA))
#    else
#      A(I,J) =             - BETA / (ALPHA*(ALPHA+N*BETA))
#
#  Example:
#
#    N = 5, ALPHA = 2, BETA = 3
#
#           14 -3 -3 -3 -3
#           -3 14 -3 -3 -3
#   1/34 *  -3 -3 14 -3 -3
#           -3 -3 -3 14 -3
#           -3 -3 -3 -3 14
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is Toeplitz: constant along diagonals.
#
#    det ( A ) = 1 / (ALPHA^(N-1) * (ALPHA+N*BETA)).
#
#    A is well defined if ALPHA /= 0.0 and ALPHA+N*BETA /= 0.
#
#    A is also a combinatorial matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition,
#    Addison-Wesley, Reading, Massachusetts, 1973, page 36.
#
#  Parameters:
#
#    Input, real ALPHA, BETA, scalars that define the matrix.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from sys import exit

  a = np.zeros ( ( n, n ) )

  if ( alpha == 0.0 ):
    print ( '' )
    print ( 'COMBIN_INVERSE - Fatal error!' )
    print ( '  The entries of the matrix are undefined' )
    print ( '  because ALPHA = 0.' )
    exit ( 'COMBIN_INVERSE - Fatal error!' )
  elif ( alpha + n * beta == 0.0 ):
    print ( '' )
    print ( 'COMBIN_INVERSE - Fatal error!' )
    print ( '  The entries of the matrix are undefined' )
    print ( '  because ALPHA+N*BETA is zero.' )
    exit ( 'COMBIN_INVERSE - Fatal error!' )

  bot = alpha * ( alpha + n * beta )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = ( alpha + float ( n - 1 ) * beta ) / bot
      else:
        a[i,j] = - beta / bot

  return a

def combin_test ( ):

#*****************************************************************************80
#
## COMBIN_TEST tests COMBIN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'COMBIN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  COMBIN computes the COMBIN matrix.' )

  n = 4
  seed = 123456789
  alpha, seed = r8_uniform_01 ( seed )
  alpha = round ( 50.0 * alpha ) / 5.0
  beta, seed = r8_uniform_01 ( seed )
  beta = round ( 50.0 * beta ) / 5.0
  a = combin ( alpha, beta, n )
  r8mat_print ( n, n, a, '  COMBIN matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'COMBIN_TEST' )
  print ( '  Normal end of execution.' )
  return

def condition_hager ( n, a ):

#*****************************************************************************80
#
## CONDITION_HAGER estimates the L1 condition number of a matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Hager,
#    Condition Estimates,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 5, Number 2, June 1984, pages 311-316.
#
#  Parameters:
#
#    Input, integer N, the dimension of the matrix.
#
#    Input, real A(N,N), the matrix.
#
#    Output, real VALUE, an estimate of the L1 condition number.
#
  import numpy as np

  i1 = -1
  c1 = 0.0
#
#  Factor the matrix.
#
  b = np.zeros ( n )
  for i in range ( 0, n ):
    b[i] = 1.0 / float ( n )

  while ( True ):

    b2 = np.linalg.solve ( a, b )

    for i in range ( 0, n ):
      b[i] = b2[i]

    c2 = 0.0
    for i in range ( 0, n ):
      c2 = c2 + abs ( b[i] )

    for i in range ( 0, n ):
      b[i] = r8_sign ( b[i] )

    b2 = np.linalg.solve ( np.transpose ( a ), b )

    for i in range ( 0, n ):
      b[i] = b2[i]

    i2 = r8vec_max_abs_index ( n, b )

    if ( 0 <= i1 ):
      if ( i1 == i2 or c2 <= c1 ):
        break

    i1 = i2
    c1 = c2

    for i in range ( 0, n ):
      b[i] = 0.0
    b[i1] = 1.0

  value = c2 * r8mat_norm_l1 ( n, n, a )

  return value

def condition_hager_test ( ):

#*****************************************************************************80
#
## CONDITION_HAGER_TEST tests CONDITION_HAGER.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'CONDITION_HAGER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONDITION_HAGER estimates the L1 condition number' )
  print ( '  for a matrix in general storage.' )
  print ( '' )
  print ( '  Matrix               Order   Condition         Hager' )
  print ( '' )
#
#  Combinatorial matrix.
#
  name = 'Combinatorial'
  n = 4
  alpha = 2.0
  beta = 3.0
  a = combin ( alpha, beta, n )
  a_inverse = combin_inverse ( alpha, beta, n )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1  = a_norm_l1 * a_inverse_norm_l1
  cond = condition_hager ( n, a )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  CONEX1
#
  name = 'CONEX1'
  n = 4
  alpha = 100.0
  a = conex1 ( alpha )
  a_inverse = conex1_inverse ( alpha )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1  = a_norm_l1 * a_inverse_norm_l1
  cond = condition_hager ( n, a )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  CONEX2
#
  name = 'CONEX2'
  n = 3
  alpha = 100.0
  a = conex2 ( alpha )
  a_inverse = conex2_inverse ( alpha )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1  = a_norm_l1 * a_inverse_norm_l1
  cond = condition_hager ( n, a )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  CONEX3
#
  name = 'CONEX3'
  n = 5
  a = conex3 ( n )
  a_inverse = conex3_inverse ( n )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1  = a_norm_l1 * a_inverse_norm_l1
  cond = condition_hager ( n, a )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  CONEX4
#
  name = 'CONEX4'
  n = 4
  a = conex4 ( )
  a_inverse = conex4_inverse ( )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1  = a_norm_l1 * a_inverse_norm_l1
  cond = condition_hager ( n, a )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  KAHAN
#
  name = 'KAHAN'
  n = 4
  alpha = 0.25
  a = kahan ( alpha, n, n )
  a_inverse = kahan_inverse ( alpha, n )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1  = a_norm_l1 * a_inverse_norm_l1
  cond = condition_hager ( n, a )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  Random
#
  seed = 123456789

  for j in range ( 0, 5 ):
    name = 'RANDOM'
    n = 4
    a, seed = r8mat_uniform_01 ( n, n, seed )
    a_inverse = np.linalg.inv ( a )
    a_norm_l1 = r8mat_norm_l1 ( n, n, a )
    a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
    cond_l1  = a_norm_l1 * a_inverse_norm_l1
    cond = condition_hager ( n, a )
    print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONDITION_HAGER_TEST' )
  print ( '  Normal end of execution.' )
  return

def condition_linpack ( n, a ):

#*****************************************************************************80
#
## CONDITION_LINPACK estimates the L1 condition number of a matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    For the system A * X = B, relative perturbations in A and B
#    of size EPSILON may cause relative perturbations in X of size
#    EPSILON*RCOND.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    Original FORTRAN77 version by Dongarra, Bunch, Moler, Stewart.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979
#
#  Parameters:
#
#    Input, integer N, the order of the matrix A.
#
#    Input, real A(N,N), a matrix to be factored.
#
#    Output, real VALUE, an estimate of the condition number of A.
#
  import numpy as np
#
#  Compute the L1 norm of A.
#
  anorm = r8mat_norm_l1 ( n, n, a )
#
#  Compute the LU factorization.
#
  a_lu, pivot, info = r8ge_fa ( n, a )
#
#  COND = norm(A) * (estimate of norm(inverse(A))) 
#
#  estimate of norm(inverse(A)) = norm(Z) / norm(Y)
#
#  where
#    A * Z = Y
#  and
#    A' * Y = E
#
#  The components of E are chosen to cause maximum local growth in the
#  elements of W, where U'*W = E.  The vectors are frequently rescaled
#  to avoid overflow.
#
#  Solve U' * W = E.
#
  ek = 1.0
  z = np.zeros ( n )

  for k in range ( 0, n ):

    if ( z[k] != 0.0 ):
      ek = - r8_sign ( z[k] ) * abs ( ek )

    if ( abs ( a_lu[k,k] ) < abs ( ek - z[k] ) ):
      s = abs ( a_lu[k,k] ) / abs ( ek - z[k] )
      for i in range ( 0, n ):
        z[i] = s * z[i]
      ek = s * ek

    wk = ek - z[k]
    wkm = - ek - z[k]
    s = abs ( wk )
    sm = abs ( wkm )

    if ( a_lu[k,k] != 0.0 ):
      wk = wk / a_lu[k,k]
      wkm = wkm / a_lu[k,k]
    else:
      wk = 1.0
      wkm = 1.0

    if ( k + 1 <= n - 1 ):

      for j in range ( k + 1, n ):
        sm = sm + abs ( z[j] + wkm * a_lu[k,j] )
        z[j] = z[j] + wk * a_lu[k,j]
        s = s + abs ( z[j] )

      if ( s < sm ):
        t = wkm - wk
        wk = wkm
        for j in range ( k + 1, n ):
          z[j] = z[j] + t * a_lu[k,j]

    z[k] = wk

  t = 0.0
  for i in range ( 0, n ):
    t = t + abs ( z[i] )

  for i in range ( 0, n ):
    z[i] = z[i] / t
#
#  Solve L' * Y = W
#
  for k in range ( n - 1, -1, -1 ):

    for i in range ( k + 1, n ):
      z[k] = z[k] + z[i] * a_lu[i,k]

    t = abs ( z[k] )

    if ( 1.0 < t ):
      for i in range ( 0, n ):
        z[i] = z[i] / t

    l = pivot[k]

    t = z[l]
    z[l] = z[k]
    z[k] = t

  t = 0.0
  for i in range ( 0, n ):
    t = t + abs ( z[i] )

  for i in range ( 0, n ):
    z[i] = z[i] / t

  ynorm = 1.0
#
#  Solve L * V = Y.
#
  for k in range ( 0, n ):

    l = pivot[k]

    t = z[l]
    z[l] = z[k]
    z[k] = t

    for i in range ( k + 1, n ):
      z[i] = z[i] + t * a_lu[i,k]

    if ( 1.0 < abs ( z[k] ) ):
      t = abs ( z[k] )
      ynorm = ynorm / t
      for i in range ( 0, n ):
        z[i] = z[i] / t

  t = 0.0
  for i in range ( 0, n ):
    t = t + abs ( z[i] )

  for i in range ( 0, n ):
    z[i] = z[i] / t

  ynorm = ynorm / t
#
#  Solve U * Z = V.
#
  for k in range ( n - 1, -1, -1 ):

    if ( abs ( a_lu[k,k] ) < abs ( z[k] ) ):
      s = abs ( a_lu[k,k] ) / abs ( z[k] )
      for i in range ( 0, n ):
        z[i] = s * z[i]
      ynorm = s * ynorm

    if ( a_lu[k,k] != 0.0 ):
      z[k] = z[k] / a_lu[k,k]
    else:
      z[k] = 1.0

    for i in range ( 0, k ):
      z[i] = z[i] - a_lu[i,k] * z[k]
#
#  Normalize Z in the L1 norm.
#
  t = 0.0
  for i in range ( 0, n ):
    t = t + abs ( z[i] )

  for i in range ( 0, n ):
    z[i] = z[i] / t

  ynorm = ynorm / t

  value = anorm / ynorm

  return value

def condition_linpack_test ( ):

#*****************************************************************************80
#
## CONDITION_LINPACK_TEST tests CONDITION_LINPACK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   06 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'CONDITION_LINPACK_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONDITION_LINPACK estimates the L1 condition number' )
  print ( '  for a matrix in general storage.' )
  print ( '' )
  print ( '  Matrix               Order   Condition       Linpack' )
  print ( '' )
#
#  Combinatorial matrix.
#
  name = 'Combinatorial'
  n = 4
  alpha = 2.0
  beta = 3.0
  a = combin ( alpha, beta, n )
  a_inverse = combin_inverse ( alpha, beta, n )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1  = a_norm_l1 * a_inverse_norm_l1
  cond = condition_linpack ( n, a )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  CONEX1
#
  name = 'CONEX1'
  n = 4
  alpha = 100.0
  a = conex1 ( alpha )
  a_inverse = conex1_inverse ( alpha )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1  = a_norm_l1 * a_inverse_norm_l1
  cond = condition_linpack ( n, a )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  CONEX2
#
  name = 'CONEX2'
  n = 3
  alpha = 100.0
  a = conex2 ( alpha )
  a_inverse = conex2_inverse ( alpha )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1  = a_norm_l1 * a_inverse_norm_l1
  cond = condition_linpack ( n, a )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  CONEX3
#
  name = 'CONEX3'
  n = 5
  a = conex3 ( n )
  a_inverse = conex3_inverse ( n )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1  = a_norm_l1 * a_inverse_norm_l1
  cond = condition_linpack ( n, a )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  CONEX4
#
  name = 'CONEX4'
  n = 4
  a = conex4 ( )
  a_inverse = conex4_inverse ( )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1  = a_norm_l1 * a_inverse_norm_l1
  cond = condition_linpack ( n, a )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  KAHAN
#
  name = 'KAHAN'
  n = 4
  alpha = 0.25
  a = kahan ( alpha, n, n )
  a_inverse = kahan_inverse ( alpha, n )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1  = a_norm_l1 * a_inverse_norm_l1
  cond = condition_linpack ( n, a )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  Random
#
  seed = 123456789

  for j in range ( 0, 5 ):
    name = 'RANDOM'
    n = 4
    a, seed = r8mat_uniform_01 ( n, n, seed )
    a_inverse = np.linalg.inv ( a )
    a_norm_l1 = r8mat_norm_l1 ( n, n, a )
    a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
    cond_l1  = a_norm_l1 * a_inverse_norm_l1
    cond = condition_linpack ( n, a )
    print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONDITION_LINPACK_TEST' )
  print ( '  Normal end of execution.' )
  return

def condition_sample1 ( n, a, m ):

#*****************************************************************************80
#
## CONDITION_SAMPLE1 estimates the L1 condition number of a matrix.
#
#  Discussion:
#
#    A naive sampling method is used.
#
#    Only "forward" sampling is used, that is, we only look at results
#    of the form y=A*x.
#
#    Presumably, solving systems A*y=x would give us a better idea of
#    the inverse matrix.
#
#    Moreover, a power sequence y1 = A*x, y2 = A*y1, ... and the same for
#    the inverse might work better too.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the matrix.
#
#    Input, real A(N,N), the matrix.
#
#    Input, integer M, the number of samples to use.
#
#    Output, real VALUE, an estimate of the L1 condition number.
#
  import numpy as np

  a_norm = 0.0
  ainv_norm = 0.0
  seed = 123456789

  for i in range ( 0, m ):

    x, seed = r8vec_uniform_unit ( n, seed )
    x_norm = r8vec_norm_l1 ( n, x )
    ax = np.dot ( a, x )
    ax_norm = r8vec_norm_l1 ( n, ax )

    if ( ax_norm == 0.0 ):
      value = 0.0
      return value

    a_norm    = max ( a_norm,    ax_norm / x_norm  )
    ainv_norm = max ( ainv_norm, x_norm  / ax_norm )

  value = a_norm * ainv_norm

  return value

def condition_sample1_test ( ):

#*****************************************************************************80
#
## CONDITION_SAMPLE1_TEST tests CONDITION_SAMPLE1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m_test = np.array ( [ 10, 1000, 100000 ] )

  print ( '' )
  print ( 'CONDITION_SAMPLE1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONDITION_SAMPLE1 estimates the L1 condition number using sampling' )
  print ( '  for a matrix in general storage.' )
  print ( '' )
  print ( '  Matrix                 Samples Order   Condition        Estimate' )
#
#  Combinatorial matrix.
#
  name = 'Combinatorial'
  n = 4
  alpha = 2.0
  beta = 3.0
  a = combin ( alpha, beta, n )
  a_inverse = combin_inverse ( alpha, beta, n )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1 = a_norm_l1 * a_inverse_norm_l1
  print ( '' )
  for i in range ( 0, 3 ):
    m = m_test[i]
    cond = condition_sample1 ( n, a, m )
    print ( '  %20s  %8d  %4d  %14.6g  %14.6g' % ( name, m, n, cond_l1, cond ) )
#
#  CONEX1
#
  name = 'CONEX1'
  n = 4
  alpha = 100.0
  a = conex1 ( alpha )
  a_inverse = conex1_inverse ( alpha )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1 = a_norm_l1 * a_inverse_norm_l1
  print ( '' )
  for i in range ( 0, 3 ):
    m = m_test[i]
    cond = condition_sample1 ( n, a, m )
    print ( '  %20s  %8d  %4d  %14.6g  %14.6g' % ( name, m, n, cond_l1, cond ) )
#
#  CONEX2
#
  name = 'CONEX2'
  n = 3
  alpha = 100.0
  a = conex2 ( alpha )
  a_inverse = conex2_inverse ( alpha )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1 = a_norm_l1 * a_inverse_norm_l1
  print ( '' )
  for i in range ( 0, 3 ):
    m = m_test[i]
    cond = condition_sample1 ( n, a, m )
    print ( '  %20s  %8d  %4d  %14.6g  %14.6g' % ( name, m, n, cond_l1, cond ) )
#
#  CONEX3
#
  name = 'CONEX3'
  n = 5
  a = conex3 ( n )
  a_inverse = conex3_inverse ( n )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1 = a_norm_l1 * a_inverse_norm_l1
  print ( '' )
  for i in range ( 0, 3 ):
    m = m_test[i]
    cond = condition_sample1 ( n, a, m )
    print ( '  %20s  %8d  %4d  %14.6g  %14.6g' % ( name, m, n, cond_l1, cond ) )
#
#  CONEX4
#
  name = 'CONEX4'
  n = 4
  a = conex4 ( )
  a_inverse = conex4_inverse ( )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1 = a_norm_l1 * a_inverse_norm_l1
  print ( '' )
  for i in range ( 0, 3 ):
    m = m_test[i]
    cond = condition_sample1 ( n, a, m )
    print ( '  %20s  %8d  %4d  %14.6g  %14.6g' % ( name, m, n, cond_l1, cond ) )
#
#  KAHAN
#
  name = 'KAHAN'
  n = 4
  alpha = 0.25
  a = kahan ( alpha, n, n )
  a_inverse = kahan_inverse ( alpha, n )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1 = a_norm_l1 * a_inverse_norm_l1
  print ( '' )
  for i in range ( 0, 3 ):
    m = m_test[i]
    cond = condition_sample1 ( n, a, m )
    print ( '  %20s  %8d  %4d  %14.6g  %14.6g' % ( name, m, n, cond_l1, cond ) )
#
#  Random
#
  seed = 123456789

  for j in range ( 0, 5 ):
    name = 'RANDOM'
    n = 4
    a, seed = r8mat_uniform_01 ( n, n, seed )
    a_inverse = np.linalg.inv ( a )
    a_norm_l1 = r8mat_norm_l1 ( n, n, a )
    a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
    cond_l1 = a_norm_l1 * a_inverse_norm_l1
    print ( '' )
    for i in range ( 0, 3 ):
      m = m_test[i]
      cond = condition_sample1 ( n, a, m )
      print ( '  %20s  %8d  %4d  %14.6g  %14.6g' % ( name, m, n, cond_l1, cond ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONDITION_SAMPLE1_TEST' )
  print ( '  Normal end of execution.' )
  return

def condition_test ( ):

#*****************************************************************************80
#
## CONDITION_TEST tests the CONDITION library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CONDITION_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the CONDITION library.' )
#
#  Utilities:
#
  combin_test ( )
  conex1_test ( )
  conex2_test ( )
  conex3_test ( )
  conex4_test ( )
  i4vec_print_test ( )
  kahan_test ( )
  r8_normal_01_test ( )
  r8_sign_test ( )
  r8_uniform_01_test ( )
  r8_uniform_ab_test ( )
  r8ge_fa_test01 ( )
  r8ge_fa_test02 ( )
  r8mat_norm_l1_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_uniform_01_test ( )
  r8mat_uniform_ab_test ( )
  r8vec_max_abs_index_test ( )
  r8vec_norm_test ( )
  r8vec_norm_l1_test ( )
  r8vec_normal_01_test ( )
  r8vec_print_test ( )
  r8vec_uniform_01_test ( )
  r8vec_uniform_ab_test ( )
  r8vec_uniform_unit_test ( )
#
#  Library.
#
  cond_test ( )
  condition_hager_test ( )
  condition_linpack_test ( )
  condition_sample1_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONDITION_TEST:' )
  print ( '  Normal end of execution.' )
  return

def cond_test ( ):

#*****************************************************************************80
#
## COND_TEST tests COND.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m_test = np.array ( [ 10, 1000, 100000 ] )

  print ( '' )
  print ( 'COND_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  COND is the condition number estimator built into Python.' )
  print ( '' )
  print ( '  Matrix               Order   Condition        Estimate' )
  print ( '' )
#
#  Combinatorial matrix.
#
  name = 'Combinatorial'
  n = 4
  alpha = 2.0
  beta = 3.0
  a = combin ( alpha, beta, n )
  a_inverse = combin_inverse ( alpha, beta, n )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1 = a_norm_l1 * a_inverse_norm_l1
  cond2 = np.linalg.cond ( a, 1 )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond2 ) )
#
#  CONEX1
#
  name = 'CONEX1'
  n = 4
  alpha = 100.0
  a = conex1 ( alpha )
  a_inverse = conex1_inverse ( alpha )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1 = a_norm_l1 * a_inverse_norm_l1
  cond2 = np.linalg.cond ( a, 1 )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond2 ) )
#
#  CONEX2
#
  name = 'CONEX2'
  n = 3
  alpha = 100.0
  a = conex2 ( alpha )
  a_inverse = conex2_inverse ( alpha )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1 = a_norm_l1 * a_inverse_norm_l1
  cond2 = np.linalg.cond ( a, 1 )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond2 ) )
#
#  CONEX3
#
  name = 'CONEX3'
  n = 5
  a = conex3 ( n )
  a_inverse = conex3_inverse ( n )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1 = a_norm_l1 * a_inverse_norm_l1
  cond2 = np.linalg.cond ( a, 1 )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond2 ) )
#
#  CONEX4
#
  name = 'CONEX4'
  n = 4
  a = conex4 ( )
  a_inverse = conex4_inverse ( )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1 = a_norm_l1 * a_inverse_norm_l1
  cond2 = np.linalg.cond ( a, 1 )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond2 ) )
#
#  KAHAN
#
  name = 'KAHAN'
  n = 4
  alpha = 0.25
  a = kahan ( alpha, n, n )
  a_inverse = kahan_inverse ( alpha, n )
  a_norm_l1 = r8mat_norm_l1 ( n, n, a )
  a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
  cond_l1 = a_norm_l1 * a_inverse_norm_l1
  cond2 = np.linalg.cond ( a, 1 )
  print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond2 ) )
#
#  Random
#
  seed = 123456789

  for j in range ( 0, 5 ):
    name = 'RANDOM'
    n = 4
    a, seed = r8mat_uniform_01 ( n, n, seed )
    a_inverse = np.linalg.inv ( a )
    a_norm_l1 = r8mat_norm_l1 ( n, n, a )
    a_inverse_norm_l1 = r8mat_norm_l1 ( n, n, a_inverse )
    cond_l1 = a_norm_l1 * a_inverse_norm_l1
    cond2 = np.linalg.cond ( a, 1 )
    print ( '  %20s  %4d  %14.6g  %14.6g' % ( name, n, cond_l1, cond2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'COND_TEST' )
  print ( '  Normal end of execution.' )
  return

def conex1 ( alpha ):

#*****************************************************************************80
#
## CONEX1 returns the CONEX1 matrix.
#
#  Discussion:
#
#    The CONEX1 matrix is a counterexample to the LINPACK condition
#    number estimator RCOND available in the LINPACK routine DGECO.
#
#  Formula:
#
#    1  -1 -2*ALPHA   0
#    0   1    ALPHA    -ALPHA
#    0   1  1+ALPHA  -1-ALPHA
#    0   0  0           ALPHA
#
#  Example:
#
#    ALPHA = 100
#
#    1  -1  -200     0
#    0   1   100  -100
#    0   1   101  -101
#    0   0     0   100
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Cline, RK Rew,
#    A set of counterexamples to three condition number estimators,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 4, 1983, pages 602-611.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [
    [ 1.0, -1.0, -2.0 * alpha,   0.0         ], \
    [ 0.0,  1.0,        alpha,       - alpha ], \
    [ 0.0,  1.0,  1.0 + alpha, - 1.0 - alpha ], \
    [ 0.0,  0.0,  0.0,                 alpha ] \
  ] )

  return a

def conex1_condition ( alpha ):

#*****************************************************************************80
#
## CONEX1_CONDITION returns the L1 condition of the CONEX1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#    Output, real VALUE, the L1 condition.
#
  a_norm = max ( 3.0, 3.0 * abs ( alpha ) + abs ( 1.0 + alpha ) )
  v1 = abs ( 1.0 - alpha ) + abs ( 1.0 + alpha ) + 1.0
  v2 = 2.0 * abs ( alpha ) + 1.0
  v3 = 2.0 + 2.0 / abs ( alpha )
  b_norm = max ( v1, max ( v2, v3 ) )
  value = a_norm * b_norm

  return value

def conex1_condition_test ( ):

#*****************************************************************************80
#
## CONEX1_CONDITION_TEST tests CONEX1_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from conex1 import conex1
  from r8mat_print import r8mat_print
  from r8_uniform_ab import r8_uniform_ab

  print ( '' )
  print ( 'CONEX1_CONDITION_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONEX1_CONDITION computes the condition of the CONEX1 matrix.' )

  m = 4
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = conex1 ( alpha )
  r8mat_print ( m, n, a, '  CONEX1 matrix:' )

  value = conex1_condition ( alpha )

  print ( '' )
  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONEX1_CONDITION_TEST' )
  print ( '  Normal end of execution.' )
  return

def conex1_determinant ( alpha ):

#*****************************************************************************80
#
## CONEX1_DETERMINANT returns the determinant of the CONEX1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#    Output, real DETERM, the determinant.
#
  determ = alpha

  return determ

def conex1_determinant_test ( ):

#*****************************************************************************80
#
## CONEX1_DETERMINANT_TEST tests CONEX1_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CONEX1_DETERMINANT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONEX1_DETERMINANT computes the determinant of the CONEX1 matrix.' )

  m = 4
  n = m

  alpha_lo = 1.0
  alpha_hi = 100.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( alpha_lo, alpha_hi, seed )

  a = conex1 ( alpha )
  r8mat_print ( m, n, a, '  CONEX1 matrix:' )

  value = conex1_determinant ( alpha )

  print ( '' )
  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONEX1_DETERMINANT_TEST' )
  print ( '  Normal end of execution.' )
  return

def conex1_inverse ( alpha ):

#*****************************************************************************80
#
#% CONEX1_INVERSE returns the inverse of the CONEX1 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np

  a = np.zeros ( ( 4, 4 ) )

  a[0,0] =  1.0
  a[0,1] =  1.0 - alpha
  a[0,2] =        alpha
  a[0,3] =  2.0

  a[1,0] =  0.0
  a[1,1] =  1.0 + alpha
  a[1,2] =      - alpha
  a[1,3] =  0.0

  a[2,0] =  0.0
  a[2,1] = -1.0
  a[2,2] =  1.0
  a[2,3] =  1.0 / alpha

  a[3,0] = 0.0
  a[3,1] = 0.0
  a[3,2] = 0.0
  a[3,3] = 1.0 / alpha

  return a

def conex1_test ( ):

#*****************************************************************************80
#
## CONEX1_TEST tests CONEX1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CONEX1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONEX1 computes the CONEX1 matrix.' )

  m = 4
  n = m

  alpha_lo = 1.0
  alpha_hi = 100.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( alpha_lo, alpha_hi, seed )

  a = conex1 ( alpha )
  r8mat_print ( m, n, a, '  CONEX1 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONEX1_TEST' )
  print ( '  Normal end of execution.' )
  return

def conex2 ( alpha ):

#*****************************************************************************80
#
## CONEX2 returns the CONEX2 matrix.
#
#  Discussion:
#
#    CONEX2 is a 3 by 3 LINPACK condition number counterexample.
#
#  Formula:
#
#    1   1-1/ALPHA^2 -2
#    0   1/ALPHA     -1/ALPHA
#    0   0            1
#
#  Example:
#
#    ALPHA = 100
#
#    1  0.9999  -2
#    0  0.01    -0.01
#    0  0        1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is upper triangular.
#
#    det ( A ) = 1 / ALPHA.
#
#    LAMBDA = ( 1, 1/ALPHA, 1 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Cline, RK Rew,
#    A set of counterexamples to three condition number estimators,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 4, 1983, pages 602-611.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#    A common value is 100.0.  ALPHA must not be zero.
#
#    Output, real A(3,3), the atrix.
#
  import numpy as np
  from sys import exit

  if ( alpha == 0.0 ):
    print ( '' )
    print ( 'CONEX2 - Fatal error!' )
    print ( '  The input value of ALPHA was zero.' )
    exit ( 'CONEX2 - Fatal error!' )

  a = np.array ( [ \
    [ 1.0, ( alpha * alpha - 1.0 ) / ( alpha * alpha ), -2.0         ], \
    [ 0.0,                     1.0 / alpha,             -1.0 / alpha ], \
    [ 0.0,                     0.0,                      1.0         ] \
  ] )

  return a

def conex2_condition ( alpha ):

#*****************************************************************************80
#
## CONEX2_CONDITION returns the L1 condition of the CONEX2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#
#    Output, real VALUE, the L1 condition.
#
  c1 = 1.0
  c2 = abs ( 1.0 - 1.0 / alpha ** 2 ) + 1.0 / abs ( alpha )
  c3 = 3.0 + 1.0 / abs ( alpha )
  a_norm = max ( c1, max ( c2, c3 ) )
  c1 = 1.0
  c2 = abs ( ( 1.0 - alpha * alpha ) / alpha ) + abs ( alpha )
  c3 = abs ( ( 1.0 + alpha * alpha ) / alpha ** 2 ) + 2.0
  b_norm = max ( c1, max ( c2, c3 ) )
  value = a_norm * b_norm

  return value

def conex2_condition_test ( ):

#*****************************************************************************80
#
## CONEX2_CONDITION_TEST tests CONEX2_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CONEX2_CONDITION_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONEX2_CONDITION computes the condition of the CONEX2 matrix.' )
  print ( '' )

  m = 3
  n = m

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )

  a = conex2 ( alpha )
  r8mat_print ( m, n, a, '  CONEX2 matrix:' )

  value = conex2_condition ( alpha )

  print ( '' )
  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONEX2_CONDITION_TEST' )
  print ( '  Normal end of execution.' )
  return

def conex2_determinant ( alpha ):

#*****************************************************************************80
#
## CONEX2_DETERMINANT returns the determinant of the CONEX2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#    A common value is 100.0.
#
#    Output, real DETERM, the determinant.
#
  determ = 1.0 / alpha

  return determ

def conex2_determinant_test ( ):

#*****************************************************************************80
#
## CONEX2_DETERMINANT_TEST tests CONEX2_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CONEX2_DETERMINANT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONEX2_DETERMINANT computes the determinant of the CONEX2 matrix.' )
  print ( '' )

  m = 3
  n = m

  alpha_lo = 1.0
  alpha_hi = 100.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( alpha_lo, alpha_hi, seed )

  a = conex2 ( alpha )
  r8mat_print ( m, n, a, '  CONEX2 matrix:' )

  value = conex2_determinant ( alpha )

  print ( '' )
  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONEX2_DETERMINANT_TEST' )
  print ( '  Normal end of execution.' )
  return

def conex2_inverse ( alpha ):

#*****************************************************************************80
#
## CONEX2_INVERSE returns the inverse of the CONEX2 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the scalar defining A.  
#    A common value is 100.0.  ALPHA must not be zero.
#
#    Output, real A(3,3), the matrix.
#
  import numpy as np
  from sys import exit

  a = np.zeros ( ( 3, 3 ) )

  if ( alpha == 0.0 ):
    print ( '' )
    print ( 'CONEX2_INVERSE - Fatal error!' )
    print ( '  The input value of ALPHA was zero.' )
    exit ( 'CONEX2_INVERSE - Fatal error!' )
 
  a[0,0] = 1.0
  a[0,1] = ( 1.0 - alpha * alpha ) / alpha
  a[0,2] = ( 1.0 + alpha * alpha ) / alpha ** 2

  a[1,0] = 0.0
  a[1,1] = alpha
  a[1,2] = 1.0

  a[2,0] = 0.0
  a[2,1] = 0.0
  a[2,2] = 1.0

  return a

def conex2_test ( ):

#*****************************************************************************80
#
## CONEX2_TEST tests CONEX2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CONEX2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONEX2 computes the CONEX2 matrix.' )

  m = 3
  n = m

  alpha_lo = 1.0
  alpha_hi = 100.0
  seed = 123456789
  alpha, seed = r8_uniform_ab ( alpha_lo, alpha_hi, seed )

  a = conex2 ( alpha )
  r8mat_print ( m, n, a, '  CONEX2 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONEX2_TEST' )
  print ( '  Normal end of execution.' )
  return

def conex3 ( n ):

#*****************************************************************************80
#
## CONEX3 returns the CONEX3 matrix.
#
#  Formula:
#
#    if ( I = J and I < N )
#      A(I,J) =  1.0 for 1<=I<N
#    else if ( I = J = N )
#      A(I,J) = -1.0
#    else if ( J < I )
#      A(I,J) = -1.0
#    else
#      A(I,J) =  0.0
#
#  Example:
#
#    N = 5
#
#     1  0  0  0  0
#    -1  1  0  0  0
#    -1 -1  1  0  0
#    -1 -1 -1  1  0
#    -1 -1 -1 -1 -1
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is integral: int ( A ) = A.
#
#    A is lower triangular.
#
#    det ( A ) = -1.
#
#    A is unimodular.
#
#    LAMBDA = ( 1, 1, 1, 1, -1 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Cline, RK Rew,
#    A set of counterexamples to three condition number estimators,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 4, 1983, pages 602-611.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j < i ):
        a[i,j] = -1.0
      elif ( j == i and i != n - 1 ):
        a[i,j] = 1.0
      elif ( j == i and i == n - 1 ):
        a[i,j] = - 1.0
      else:
        a[i,j] = 0.0

  return a

def conex3_condition ( n ):

#*****************************************************************************80
#
## CONEX3_CONDITION returns the L1 condition of the CONEX3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 April 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real COND, the L1 condition number.
#
  cond = n * 2.0 ** ( n - 1 )

  return cond

def conex3_condition_test ( ):

#*****************************************************************************80
#
## CONEX3_CONDITION_TEST tests CONEX3_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CONEX3_CONDITION_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONEX3_CONDITION computes the condition of the CONEX3 matrix.' )

  n = 5
  a = conex3 ( n )
  r8mat_print ( n, n, a, '  CONEX3 matrix:' )

  value = conex3_condition ( n )

  print ( '' )
  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONEX3_CONDITION_TEST' )
  print ( '  Normal end of execution.' )
  return

def conex3_determinant ( n ):

#*****************************************************************************80
#
## CONEX3_DETERMINANT returns the determinant of the CONEX3 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real DETERM, the determinant.
#
  determ = - 1.0

  return determ

def conex3_determinant_test ( ):

#*****************************************************************************80
#
## CONEX3_DETERMINANT_TEST tests CONEX3_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CONEX3_DETERMINANT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONEX3_DETERMINANT computes the determinant of the CONEX3 matrix.' )

  n = 5
  a = conex3 ( n )
  r8mat_print ( n, n, a, '  CONEX3 matrix:' )

  value = conex3_determinant ( n )

  print ( '' )
  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONEX3_DETERMINANT_TEST' )
  print ( '  Normal end of execution.' )
  return

def conex3_inverse ( n ):

#*****************************************************************************80
#
## CONEX3_INVERSE returns the inverse of the CONEX3 matrix.
#
#  Example:
#
#    N = 5
#
#     1  0  0  0  0
#     1  1  0  0  0
#     2  1  1  0  0
#     4  2  1  1  0
#    -8 -4 -2 -1 -1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alan Cline, RK Rew,
#    A set of counterexamples to three condition number estimators,
#    SIAM Journal on Scientific and Statistical Computing,
#    Volume 4, 1983, pages 602-611.
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
    for j in range ( 0, n ):

      if ( i < n - 1 ):
      
        if ( j < i ):
          a[i,j] = 2.0 ** ( i - j - 1 )
        elif ( i == j ):
          a[i,j] = 1.0

      elif ( i == n - 1 ):
      
        if ( j < i ):
          a[i,j] = - 2.0 ** ( i - j - 1 )
        else:
          a[i,j] = -1.0

  return a

def conex3_test ( ):

#*****************************************************************************80
#
## CONEX3_TEST tests CONEX3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CONEX3_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONEX3 computes the CONEX3 matrix.' )

  n = 5
  a = conex3 ( n )
  r8mat_print ( n, n, a, '  CONEX3 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONEX3_TEST' )
  print ( '  Normal end of execution.' )
  return

def conex4 ( ):

#*****************************************************************************80
#
## CONEX4 returns the CONEX4 matrix.
#
#  Discussion:
#
#    7  10   8   7
#    6   8  10   9
#    5   7   9  10
#    5   7   6   5
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [
    [ 7.0, 10.0,  8.0,  7.0 ], \
    [ 6.0,  8.0, 10.0,  9.0 ], \
    [ 5.0,  7.0,  9.0, 10.0 ], \
    [ 5.0,  7.0,  6.0,  5.0 ] \
  ] )

  return a

def conex4_condition ( ):

#*****************************************************************************80
#
## CONEX4_CONDITION returns the L1 condition of the CONEX4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real COND, the L1 condition number.
#
  a_norm = 33.0
  b_norm = 136.0
  cond = a_norm * b_norm

  return cond

def conex4_condition_test ( ):

#*****************************************************************************80
#
## CONEX4_CONDITION_TEST tests CONEX4_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CONEX4_CONDITION_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONEX4_CONDITION computes the condition of the CONEX4 matrix.' )

  n = 4
  a = conex4 ( )
  r8mat_print ( n, n, a, '  CONEX4 matrix:' )

  value = conex4_condition ( )

  print ( '' )
  print ( '  Value =  #g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONEX4_CONDITION_TEST' )
  print ( '  Normal end of execution.' )
  return

def conex4_determinant ( ):

#*****************************************************************************80
#
## CONEX4_DETERMINANT returns the determinant of the CONEX4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real DETERM, the determinant.
#
  determ = -1.0

  return determ

def conex4_determinant_test ( ):

#*****************************************************************************80
#
## CONEX4_DETERMINANT_TEST tests CONEX4_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CONEX4_DETERMINANT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONEX4_DETERMINANT computes the determinant of the CONEX4 matrix.' )

  m = 4
  n = m

  a = conex4 ( )
  r8mat_print ( m, n, a, '  CONEX4 matrix:' )

  value = conex4_determinant ( )

  print ( '' )
  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONEX4_DETERMINANT_TEST' )
  print ( '  Normal end of execution.' )
  return

def conex4_inverse ( ):

#*****************************************************************************80
#
## CONEX4_INVERSE returns the inverse of the CONEX4 matrix.
#
#  Discussion:
#
#   -41  -17   10   68
#    25   10   -6  -41
#    10    5   -3  -17
#    -6   -3    2   10
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
   [ -41.0,  -17.0,   10.0,   68.0 ], \
   [  25.0,   10.0,   -6.0,  -41.0 ], \
   [  10.0,    5.0,   -3.0,  -17.0 ], \
   [  -6.0,   -3.0,    2.0,   10.0 ] ] )

  return a

def conex4_test ( ):

#*****************************************************************************80
#
## CONEX4_TEST tests CONEX4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CONEX4_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CONEX4 computes the CONEX4 matrix.' )

  m = 4
  n = m

  a = conex4 ( )
  r8mat_print ( m, n, a, '  CONEX4 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'CONEX4_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## I4VEC_PRINT prints an I4VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, integer A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def i4vec_print_test ( ):

#*****************************************************************************80
#
## I4VEC_PRINT_TEST tests I4VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_PRINT prints an I4VEC.' )

  n = 4
  v = np.array ( [ 91, 92, 93, 94 ], dtype = np.int32 )
  i4vec_print ( n, v, '  Here is an I4VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def kahan ( alpha, m, n ):

#*****************************************************************************80
#
## KAHAN returns the KAHAN matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,I) =  sin(ALPHA)^(I)
#    elseif ( I < J )
#      A(I,J) = - sin(ALPHA)^(I) * cos(ALPHA)
#    else
#      A(I,J) = 0
#
#  Example:
#
#    ALPHA = 0.25, N = 4
#
#    S  -C*S    -C*S      -C*S
#    0     S^2  -C*S^2    -C*S^2
#    0     0       S^3    -C*S^3
#    0     0       0         S^4
#
#    where
#
#      S = sin(ALPHA), C=COS(ALPHA)
#
#  Properties:
#
#    A is upper triangular.
#
#    A = B * C, where B is a diagonal matrix and C is unit upper triangular.
#    For instance, for the case M = 3, N = 4:
#
#    A = | S 0    0    |  * | 1 -C -C  -C |
#        | 0 S^2  0    |    | 0  1 -C  -C |
#        | 0 0    S^3  |    | 0  0  1  -C |
#
#    A is generally not symmetric: A' /= A.
#
#    A has some interesting properties regarding estimation of
#    condition and rank.
#
#    det ( A ) = sin(ALPHA)^(N*(N+1)/2).
#
#    LAMBDA(I) = sin ( ALPHA )^I
#
#    A is nonsingular if and only if sin ( ALPHA ) =/= 0.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Nicholas Higham,
#    A survey of condition number estimation for triangular matrices,
#    SIAM Review,
#    Volume 9, 1987, pages 575-596.
#
#    W Kahan,
#    Numerical Linear Algebra,
#    Canadian Mathematical Bulletin,
#    Volume 9, 1966, pages 757-801.
#
#  Parameters:
#
#    Input, real ALPHA, the scalar that defines A.  A typical
#    value is 1.2.  The "interesting" range of ALPHA is 0 < ALPHA < PI.
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( m, n ) )

  for i in range ( 0, m ):

    si = np.sin ( alpha ) ** ( i + 1 )
    csi = - np.cos ( alpha ) * si

    for j in range ( 0, n ):

      if ( j == i ):
        a[i,j] = si
      elif ( i < j ):
        a[i,j] = csi

  return a

def kahan_determinant ( alpha, n ):

#*****************************************************************************80
#
## KAHAN_DETERMINANT computes the determinant of the KAHAN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real ALPHA, the parameter.
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  import numpy as np

  power = ( n * ( n + 1 ) ) // 2
  value = ( np.sin ( alpha ) ) ** power

  return value

def kahan_determinant_test ( ):

#*****************************************************************************80
#
## KAHAN_DETERMINANT_TEST tests KAHAN_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'KAHAN_DETERMINANT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KAHAN_DETERMINANT computes the KAHAN determinant.' )

  seed = 123456789

  m = 5
  n = m
  alpha, seed = r8_uniform_01 ( seed )
  a = kahan ( alpha, m, n )
  r8mat_print ( m, n, a, '  KAHAN matrix:' )

  value = kahan_determinant ( alpha, n )

  print ( '' )
  print ( '  Value =  %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'KAHAN_DETERMINANT_TEST' )
  print ( '  Normal end of execution.' )
  return

def kahan_inverse ( alpha, n ):

#*****************************************************************************80
#
## KAHAN_INVERSE returns the inverse of the KAHAN matrix.
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
#    Input, real ALPHA, the scalar that defines A.  A typical 
#    value is 1.2.  The "interesting" range of ALPHA is 0 < ALPHA < PI.
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  ci = np.cos ( alpha );

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == j ):
        a[i,j] = 1.0;
      elif ( i == j - 1 ):
        a[i,j] = ci;
      elif ( i < j ):
        a[i,j] = ci * ( 1.0 + ci ) ** ( j - i - 1 )
#
#  Scale the columns.
#
  for j in range ( 0, n):
    si = np.sin ( alpha ) ** ( j + 1 )
    for i in range ( 0, n ):
      a[i,j] = a[i,j] / si

  return a

def kahan_test ( ):

#*****************************************************************************80
#
## KAHAN_TEST tests KAHAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'KAHAN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  KAHAN computes the KAHAN matrix.' )

  seed = 123456789

  m = 5
  n = 5
  alpha, seed = r8_uniform_01 ( seed )
  a = kahan ( alpha, m, n )
  r8mat_print ( m, n, a, '  KAHAN matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'KAHAN_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_fa ( n, a ):

#*****************************************************************************80
#
## R8GE_FA performs a LINPACK style PLU factorization of a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    R8GE_FA is a simplified version of the LINPACK routine R8GEFA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be positive.
#
#    Input, real A(N,N), the matrix to be factored.
#
#    Output, real A_LU(N,N), an upper triangular matrix and 
#    the multipliers used to obtain it.  The factorization 
#    can be written A = L * U, where L is a product of 
#    permutation and unit lower triangular matrices and U 
#    is upper triangular.
#
#    Output, integer PIVOT(N), a vector of pivot indices.
#
#    Output, integer INFO, singularity flag.
#    0, no singularity detected.
#    nonzero, the factorization failed on the INFO-th step.
#
  import numpy as np
  from sys import exit

  a_lu = np.zeros ( [ n, n ], dtype = np.float64 )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a_lu[i,j] = a[i,j]

  info = 0

  pivot = np.zeros ( n, dtype = np.int32 )

  for k in range ( 0, n - 1 ):
#
#  Find L, the index of the pivot row.
#
    l = k
    for i in range ( k + 1, n ):
      if ( abs ( a_lu[l,k] ) < abs ( a_lu[i,k] ) ):
        l = i

    pivot[k] = l
#
#  If the pivot index is zero, the algorithm has failed.
#
    if ( a_lu[l,k] == 0.0 ):
      info = k
      return a_lu, pivot, info
#
#  Interchange rows L and K if necessary.
#
    if ( l != k ):
      t         = a_lu[l,k]
      a_lu[l,k] = a_lu[k,k]
      a_lu[k,k] = t
#
#  Normalize the values that lie below the pivot entry A(K,K).
#
    for i in range ( k + 1, n ):
      a_lu[i,k] = - a_lu[i,k] / a_lu[k,k]
#
#  Row elimination with column indexing.
#
    for j in range ( k + 1, n ):

      if ( l != k ):
        t         = a_lu[l,j]
        a_lu[l,j] = a_lu[k,j]
        a_lu[k,j] = t

      for i in range ( k + 1, n ):
        a_lu[i,j] = a_lu[i,j] + a_lu[i,k] * a_lu[k,j]

  pivot[n-1] = n - 1

  if ( a_lu[n-1,n-1] == 0.0 ):
    info = n - 1

  return a_lu, pivot, info

def r8ge_fa_test01 ( ):

#*****************************************************************************80
#
## R8GE_FA_TEST01 tests R8GE_FA, R8GE_SL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8GE_FA_TEST01' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  For a matrix in general storage,' )
  print ( '  R8GE_FA computes the LU factors,' )
  print ( '  R8GE_SL solves a factored system.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a, seed = r8ge_random ( n, n, seed )
#
#  Set the desired solution.
#
  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( i + 1 )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mxv ( n, n, a, x )
#
#  Factor the matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_FA_TEST01 - Warning!' )
    print ( '  R8GE_FA declares the matrix is singular!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return
#
#  Solve the linear system.
#
  job = 0
  x = r8ge_sl ( n, a_lu, pivot, b, job )
 
  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  for i in range ( 0, n ):
    x[i] = 1.0
#
#  Compute the corresponding right hand side.
#
  job = 0
  b = r8ge_ml ( n, a_lu, pivot, x, job )
#
#  Solve the system
#
  job = 0
  x = r8ge_sl ( n, a_lu, pivot, b, job )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution.
#
  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( i + 1 )
#
#  Compute the corresponding right hand side.
#
  job = 1
  b = r8ge_ml ( n, a_lu, pivot, x, job )
#
#  Solve the system
#
  job = 1
  x = r8ge_sl ( n, a_lu, pivot, b, job )

  r8vec_print ( n, x, '  Solution of transposed system:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_FA_TEST01' )
  print ( '  Normal end of execution.' )
  return

def r8ge_fa_test02 ( ):

#*****************************************************************************80
#
## R8GE_FA_TEST02 tests R8GE_FA, R8GE_SL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  seed = 123456789

  print ( '' )
  print ( 'R8GE_FA_TEST02' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  For a matrix in general storage,' )
  print ( '  R8GE_FA computes the LU factors,' )
  print ( '  R8GE_SL solves a factored system.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a, seed = r8ge_random ( n, n, seed )

  r8ge_print ( n, n, a, '  The matrix:' )
#
#  Set the desired solution.
#
  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( i + 1 )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mxv ( n, n, a, x )
#
#  Factor the matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )
 
  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_FA_TEST02 - Warning!' )
    print ( '  R8GE_FA declares the matrix is singular!' )
    print ( '  The value of INFO is %d' % ( info ) )
#
#  Display the gory details.
#
  r8ge_print ( n, n, a_lu, '  The compressed LU factors:' )

  i4vec_print ( n, pivot, '  The pivot vector P:' )
#
#  Solve the linear system.
#
  job = 0
  x = r8ge_sl ( n, a_lu, pivot, b, job )

  r8vec_print ( n, x, '  Solution:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_FA_TEST02' )
  print ( '  Normal end of execution.' )
  return

def r8ge_ml ( n, a_lu, pivot, x, job ):

#*****************************************************************************80
#
## R8GE_ML computes A * x or A' * x, using R8GE_FA factors.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    It is assumed that R8GE_FA has overwritten the original matrix
#    information by LU factors.  R8GE_ML is able to reconstruct the
#    original matrix from the LU factor data.
#
#    R8GE_ML allows the user to check that the solution of a linear
#    system is correct, without having to save an unfactored copy
#    of the matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be positive.
#
#    Input, real A_LU(N,N), the LU factors from R8GE_FA.
#
#    Input, integer PIVOT(N), the pivot vector computed by R8GE_FA.
#
#    Input, real X(N), the vector to be multiplied.
#
#    Input, integer JOB, specifies the operation to be done:
#    JOB = 0, compute A * x.
#    JOB nonzero, compute A' * X.
#
#    Output, real B(N), the result of the multiplication.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    b[i] = x[i]

  if ( job == 0 ):
#
#  Y = U * X.
#
    for j in range ( 0, n ):
      for i in range ( 0, j ):
        b[i] = b[i] + a_lu[i,j] * b[j]
      b[j] = a_lu[j,j] * b[j]
#
#  B = PL * Y = PL * U * X = A * x.
#
    for j in range ( n - 2, -1, -1 ):

      for i in range ( j + 1, n ):
        b[i] = b[i] - a_lu[i,j] * b[j]
      k = pivot[j]

      if ( k != j ):
        t    = b[k]
        b[k] = b[j]
        b[j] = t

  else:
#
#  Y = (PL)' * X:
#
    for j in range ( 0, n - 1 ):

      k = pivot[j]

      if ( k != j ):
        t    = b[k]
        b[k] = b[j]
        b[j] = t

      for i in range ( j + 1, n ):
        b[j] = b[j] - b[i] * a_lu[i,j]
#
#  B = U' * Y = ( PL * U )' * X = A' * X.
#
    for i in range ( n - 1, -1, -1 ):
      for j in range ( i + 1, n ):
        b[j] = b[j] + b[i] * a_lu[i,j]
      b[i] = b[i] * a_lu[i,i]

  return b

def r8ge_mxv ( m, n, a, x ):

#*****************************************************************************80
#
## R8GE_MXV multiplies an R8GE matrix times a vector.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrix.
#    M must be positive.
#
#    Input, integer N, the number of columns of the matrix.
#    N must be positive.
#
#    Input, real A(M,N), the R8GE matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Output, real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[i] = b[i] + a[i,j] * x[j]

  return b

def r8ge_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8GE_PRINT prints an R8GE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8ge_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8ge_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8GE_PRINT_SOME prints out a portion of an R8GE.
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
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
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

def r8ge_random ( m, n, seed ):

#*****************************************************************************80
#
## R8GE_RANDOM randomizes a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrix.
#    M must be positive.
#
#    Input, integer N, the number of columns of the matrix.
#    N must be positive.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real A(M,N), the R8GE matrix.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8GE_RANDOM - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8GE_RANDOM - Fatal error!' )

  r = numpy.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = seed * 4.656612875E-10

  return r, seed

def r8ge_sl ( n, a_lu, pivot, b, job ):

#*****************************************************************************80
#
## R8GE_SL solves a system factored by R8GE_FA.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    R8GE_SL is a simplified version of the LINPACK routine R8GESL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be positive.
#
#    Input, real A_LU(N,N), the LU factors from R8GE_FA.
#
#    Input, integer PIVOT(N), the pivot vector from R8GE_FA.
#
#    Input, real B(N), the right hand side vector.
#
#    Input, integer JOB, specifies the operation.
#    0, solve A * x = b.
#    nonzero, solve A' * x = b.
#
#    Output, real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]
#
#  Solve A * x = b.
#
  if ( job == 0 ):
#
#  Solve PL * Y = B.
#
    for k in range ( 0, n - 1 ):

      l = pivot[k]

      if ( l != k ):
        t    = x[l]
        x[l] = x[k]
        x[k] = t

      for i in range ( k + 1, n ):
        x[i] = x[i] + a_lu[i,k] * x[k]
#
#  Solve U * X = Y.
#
    for k in range ( n - 1, -1, -1 ):
      x[k] = x[k] / a_lu[k,k]
      for i in range ( 0, k ):
        x[i] = x[i] - a_lu[i,k] * x[k]
#
#  Solve A' * X = B.
#
  else:
#
#  Solve U' * Y = B.
#
    for k in range ( 0, n ):
      for i in range ( 0, k ):
        x[k] = x[k] - x[i] * a_lu[i,k]
      x[k] = x[k] / a_lu[k,k]
#
#  Solve ( PL )' * X = Y.
#
    for k in range ( n - 2, -1, -1 ):
      for i in range ( k + 1, n ):
        x[k] = x[k] + x[i] * a_lu[i,k]

      l = pivot[k]

      if ( l != k ):
        t    = x[l]
        x[l] = x[k]
        x[k] = t

  return x

def r8mat_norm_l1 ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_NORM_L1 returns the matrix L1 norm of an R8MAT.
#
#  Discussion:
#
#    The matrix L1 norm is defined as:
#
#      value = max ( 1 <= J <= N ) sum ( 1 <= I <= M ) abs ( A(I,J) ).
#
#    The matrix L1 norm is derived from the vector L1 norm, and
#    satisifies:
#
#      vec_norm_l1 ( A * x ) <= mat_norm_l1 ( A ) * vec_norm_l1 ( x ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix whose norm is desired.
#
#    Output, real VALUE, the norm of A.
#
  value = 0.0

  for j in range ( 0, n ):
    row_sum = 0.0
    for i in range ( 0, m ):
      row_sum = row_sum + abs ( a[i,j] )
    value = max ( value, row_sum )

  return value

def r8mat_norm_l1_test ( ):

#*****************************************************************************80
#
## R8MAT_NORM_L1_TEST tests R8MAT_NORM_L1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4
  x1 = -5.0
  x2 = +5.0
  seed = 123456789

  a, seed = r8mat_uniform_ab ( m, n, x1, x2, seed )
  
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = round ( a[i,j] )

  print ( '' )
  print ( 'R8MAT_NORM_L1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_NORM_L1 computes the L1 norm of an R8MAT;' )

  t = r8mat_norm_l1 ( m, n, a )

  r8mat_print ( m, n, a, '  A:' )
  print ( '' )
  print ( '  Computed L1 norm = %g' % ( t ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_NORM_L1_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_PRINT prints an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_TEST tests R8MAT_PRINT.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME prints out a portion of an R8MAT.
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
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
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

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT_SOME prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_uniform_01 ( m, n, seed ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_01 returns a unit pseudorandom R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.
#
#    Output, real R(M,N), an array of random values between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8MAT_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8MAT_UNIFORM_01 - Fatal error!' )

  r = numpy.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i][j] = seed * 4.656612875E-10

  return r, seed

def r8mat_uniform_01_test ( ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_01_TEST tests R8MAT_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  seed = 123456789

  print ( '' )
  print ( 'R8MAT_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_UNIFORM_01 computes a random R8MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8mat_uniform_01 ( m, n, seed )

  r8mat_print ( m, n, v, '  Random R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_UNIFORM_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_uniform_ab ( m, n, a, b, seed ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_AB returns a scaled pseudorandom R8MAT.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, real A, B, the range of the pseudorandom values.
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.
#
#    Output, real R(M,N), an array of random values between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = np.floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8MAT_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8MAT_UNIFORM_AB - Fatal error!' )

  r = np.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = np.floor ( seed )

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r8mat_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_AB_TEST tests R8MAT_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'R8MAT_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_UNIFORM_AB computes a random R8MAT.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8mat_uniform_ab ( m, n, a, b, seed )

  r8mat_print ( m, n, v, '  Random R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_normal_01 ( seed ):

#*****************************************************************************80
#
## R8_NORMAL_01 samples the standard normal probability distribution.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#    The Box-Muller method is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 January 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the standard normal PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  r1, seed = r8_uniform_01 ( seed )
  r2, seed = r8_uniform_01 ( seed )

  x = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )

  return x, seed

def r8_normal_01_test ( ):

#*****************************************************************************80
#
## R8_NORMAL_01_TEST tests R8_NORMAL_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  seed = 123456789
  test_num = 20

  print ( '' )
  print ( 'R8_NORMAL_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_NORMAL_01 generates normally distributed' )
  print ( '  random values.' )
  print ( '  Using initial random number seed = %d' % ( seed ) )
  print ( '' )

  for test in range ( 0, test_num ):

    x, seed = r8_normal_01 ( seed )
    print ( '  %f' % ( x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_NORMAL_01_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_sign ( x ):

#*****************************************************************************80
#
## R8_SIGN returns the sign of an R8.
#
#  Discussion:
#
#    The value is +1 if the number is positive or zero, and it is -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose sign is desired.
#
#    Output, real VALUE, the sign of X.
#
  if ( x < 0.0 ):
    value = -1.0
  else:
    value = +1.0
 
  return value

def r8_sign_test ( ):

#*****************************************************************************80
#
## R8_SIGN_TEST tests R8_SIGN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  test_num = 5

  r8_test = np.array ( [ -1.25, -0.25, 0.0, +0.5, +9.0 ] )

  print ( '' )
  print ( 'R8_SIGN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_SIGN returns the sign of an R8.' )
  print ( '' )
  print ( '     R8     R8_SIGN(R8)' )
  print ( '' )

  for test in range ( 0, test_num ):
    r8 = r8_test[test]
    s = r8_sign ( r8 )
    print ( '  %8.4f  %8.0f' % ( r8, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_SIGN_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_uniform_01 ( seed ):

#*****************************************************************************80
#
## R8_UNIFORM_01 returns a unit pseudorandom R8.
#
#  Discussion:
#
#    This routine implements the recursion
#
#      seed = 16807 * seed mod ( 2^31 - 1 )
#      r8_uniform_01 = seed / ( 2^31 - 1 )
#
#    The integer arithmetic never requires more than 32 bits,
#    including a sign bit.
#
#    If the initial seed is 12345, then the first three computations are
#
#      Input     Output      R8_UNIFORM_01
#      SEED      SEED
#
#         12345   207482415  0.096616
#     207482415  1790989824  0.833995
#    1790989824  2035175616  0.947702
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.  SEED should not be 0.
#
#    Output, real R, a random value between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8_UNIFORM_01 - Fatal error!' )

  k = floor ( seed / 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10

  return r, seed

def r8_uniform_01_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_01_TEST tests R8_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_01 produces a sequence of random values.' )

  seed = 123456789

  print ( '' )
  print ( '  Using random seed %d' % ( seed ) )

  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )
  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )

  print ( '' )
  print ( '  Verify that the sequence can be restarted.' )
  print ( '  Set the seed back to its original value, and see that' )
  print ( '  we generate the same sequence.' )

  seed = 123456789
  print ( '' )
  print ( '  SEED  R8_UNIFORM_01(SEED)' )
  print ( '' )

  for i in range ( 0, 10 ):
    seed_old = seed
    x, seed = r8_uniform_01 ( seed )
    print ( '  %12d  %14f' % ( seed, x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_01_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## R8_UNIFORM_AB returns a scaled pseudorandom R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, real A, B, the minimum and maximum values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real R, the randomly chosen value.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8_UNIFORM_AB - Fatal error!' )

  seed = floor ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r8_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_AB_TEST tests R8_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  a = 10.0
  b = 20.0

  print ( '' )
  print ( 'R8_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_AB returns random values in a given range:' )
  print ( '  [ A, B ]' )
  print ( '' )
  print ( '  For this problem:' )
  print ( '  A = %f' % ( a ) )
  print ( '  B = %f' % ( b ) )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):
    r, seed = r8_uniform_ab ( a, b, seed )
    print ( '  %f' % ( r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_AB_TEST' )
  print ( '  Normal end of execution' )
  return

def r8vec_max_abs_index ( n, a ):

#*****************************************************************************80
#
## R8VEC_MAX_ABS_INDEX: index of entry of maximum absolute value in an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the array.
#
#    Input, real A(N), the array.
#
#    Output, integer MAX_ABS_INDEX, the index of the entry of maximum
#    absolute value.
#
  if ( n <= 0 ):

    max_abs_index = -1

  else:

    max_abs_index = 0

    for i in range ( 1, n ):
      if ( abs ( a[max_abs_index] ) < abs ( a[i] ) ):
        max_abs_index = i

  return max_abs_index

def r8vec_max_abs_index_test ( ):

#*****************************************************************************80
#
## R8VEC_MAX_ABS_INDEX_TEST tests R8VEC_MAX_ABS_INDEX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10
 
  print ( '' )
  print ( 'R8VEC_MAX_ABS_INDEX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MAX_ABS_INDEX: index of entry of maximum absolute value' )
 
  r8_lo = - 10.0
  r8_hi = + 10.0

  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
 
  r8vec_print ( n, a, '  Input vector:' )

  ival = r8vec_max_abs_index ( n, a )

  print ( '' )
  print ( '  Maximum index: %d' % ( ival ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MAX_ABS_INDEX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_normal_01 ( n, seed ):

#*****************************************************************************80
#
## R8VEC_NORMAL_01 returns a unit pseudonormal R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i], seed = r8_normal_01 ( seed )

  return x, seed

def r8vec_normal_01_test ( ):

#*****************************************************************************80
#
## R8VEC_NORMAL_01_TEST tests R8VEC_NORMAL_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_NORMAL_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORMAL_01 returns a vector of Normal 01 values' )
  print ( '' )
  print ( '  SEED = %d' % ( seed ) )

  r, seed = r8vec_normal_01 ( n, seed )

  r8vec_print ( n, r, '  Vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORMAL_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_norm_l1 ( n, a ):

#*****************************************************************************80
#
## R8VEC_NORM_L1 returns the L1 norm of an R8VEC.
#
#  Discussion:
#
#    The vector L1 norm is defined as:
#
#      value = sum ( 1 <= I <= N ) abs ( A(I) ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), the vector whose L1 norm is desired.
#
#    Output, real VALUE, the L1 norm of A.
#
  value = 0.0
  for i in range ( 0, n ):
    value = value + abs ( a[i] )

  return value

def r8vec_norm_l1_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_L1_TEST tests R8VEC_NORM_L1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'R8VEC_NORM_L1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORM_L1 computes the L1 norm of an R8VEC.' )
 
  r8_lo = - 10.0
  r8_hi = + 10.0

  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
 
  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_norm_l1 ( n, a )

  print ( '' )
  print ( '  L1 norm = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORM_L1_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_norm ( n, a ):

#*****************************************************************************80
#
## R8VEC_NORM returns the L2 norm of an R8VEC.
#
#  Discussion:
#
#    The vector L2 norm is defined as:
#
#      value = sqrt ( sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), the vector whose L2 norm is desired.
#
#    Output, real VALUE, the L2 norm of A.
#
  import numpy as np

  value = 0.0
  for i in range ( 0, n ):
    value = value + a[i] * a[i]
  value = np.sqrt ( value )

  return value

def r8vec_norm_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_TEST tests R8VEC_NORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_NORM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORM computes the L2 norm of an R8VEC.' )

  n = 10
  seed = 123456789
  a, seed = r8vec_uniform_01 ( n, seed )
  r8vec_print ( n, a, '  Input vector:' )
  a_norm = r8vec_norm ( n, a )

  print ( '' )
  print ( '  L2 norm = %g' % ( a_norm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_01 ( n, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy
  from math import floor
  from sys import exit

  i4_huge = 2147483647;

  seed = floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_01 - Fatal error!' )

  x = numpy.zeros ( n );

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_01_TEST tests R8VEC_UNIFORM_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_01 computes a random R8VEC.' )
  print ( '' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_01 ( n, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_01_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_ab ( n, a, b, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_AB returns a scaled pseudorandom R8VEC.
#
#  Discussion:
#
#    Each dimension ranges from A to B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Springer Verlag, pages 201-202, 1983.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, pages 362-376, 1986.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, pages 136-143, 1969.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A, B, the range of the pseudorandom values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_AB - Fatal error!' )

  x = numpy.zeros ( n )

  for i in range ( 0, n ):

    k = ( seed // 127773 )

    seed = 16807 * ( seed - k * 127773 ) - k * 2836

    if ( seed < 0 ):
      seed = seed + i4_huge

    x[i] = a + ( b - a ) * seed * 4.656612875E-10

  return x, seed

def r8vec_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_AB_TEST tests R8VEC_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'R8VEC_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_AB computes a random R8VEC.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8vec_uniform_ab ( n, a, b, seed )

  r8vec_print ( n, v, '  Random R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_uniform_unit ( m, seed ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_UNIT generates a random unit vector.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the dimension of the space.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real W(M), a random direction vector,
#    with unit norm.
#
#    Output, integer SEED, a seed for the random number generator.
#

#
#  Get N values from a standard normal distribution.
#
  w, seed = r8vec_normal_01 ( m, seed )
#
#  Compute the length of the vector.
#
  norm = r8vec_norm ( m, w )
#
#  Normalize the vector.
#
  for i in range ( 0, m ):
    w[i] = w[i] / norm

  return w, seed

def r8vec_uniform_unit_test ( ):

#*****************************************************************************80
#
## R8VEC_UNIFORM_UNIT_TEST tests R8VEC_UNIFORM_UNIT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5

  print ( '' )
  print ( 'R8VEC_UNIFORM_UNIT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_UNIFORM_UNIT returns a random R8VEC' )
  print ( '  on the surface of the unit M sphere.' )
  print ( '' )

  seed = 123456789

  for j in range ( 0, 5 ):

    x, seed = r8vec_uniform_unit ( m, seed )

    r8vec_print ( m, x, '  Vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_UNIFORM_UNIT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  condition_test ( )
  timestamp ( )

