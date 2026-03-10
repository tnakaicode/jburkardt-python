#! /usr/bin/env python3
#
def hankel_cholesky_test ( ):

#*****************************************************************************80
#
## hankel_cholesky_test() tests hankel_cholesky().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2017
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'hankel_cholesky_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test hankel_cholesky().' )

  rng = default_rng ( )

  hankel_cholesky_upper_test ( rng )
  hankel_spd_cholesky_lower_test01 ( rng )
  hankel_spd_cholesky_lower_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'hankel_cholesky_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )
  return

def hankel_cholesky_upper ( n, h ):

#*****************************************************************************80
#
## hankel_cholesky_upper() computes the upper Cholesky factor of a Hankel matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    James Phillips,
#    The triangular decomposition of Hankel matrices,
#    Mathematics of Computation,
#    Volume 25, Number 115, July 1971, pages 599-602.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real H(2*N-1), the values defining the antidiagonals.
#
#  Output:
#
#    real R(N,N), the upper triangular Cholesky factor.
#
  import numpy as np

  c = np.zeros ( [ 2 * n - 1, 2 * n - 1 ] )

  for j in range ( 0, 2 * n - 1 ):
    c[0,j] = h[j]

  for i in range ( 0, n - 1 ):

    if ( i == 0 ):
      a = c[0,1] / c[0,0]
      b = 0.0
    else:
      a = c[i,i+1] / c[i,i] - c[i-1,i] / c[i-1,i-1]
      b = c[i,i] / c[i-1,i-1]

    for j in range ( i + 1, 2 * n - i - 2 ):
      c[i+1,j] = c[i,j+1] - a * c[i,j]
      if ( 0 < i ):
        c[i+1,j] = c[i+1,j] - b * c[i-1,j]

  r = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      r[i,j] = c[i,j]
#
#  Normalize.
#
  for i in range ( 0, n ):
    t = np.sqrt ( r[i,i] )
    for j in range ( 0, i ):
      r[i,j] = 0.0
    for j in range ( i, n ):
      r[i,j] = r[i,j] / t

  return r

def hankel_cholesky_upper_test ( rng ):

#*****************************************************************************80
#
## hankel_cholesky_upper_test() tests hankel_cholesky_upper().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'hankel_cholesky_upper_test():' )
  print ( '  hankel_cholesky_upper() is given a Hankel matrix H and ' )
  print ( '  computes an upper triangular matrix R such that ' )
  print ( '  H = R\' * R' )
#
#  Get a Hankel matrix that is positive definite.
#
  n = 5
  lii = rng.random ( size = n )
  liim1 = rng.random ( size = n - 1 )
  l = hankel_spd_cholesky_lower ( n, lii, liim1 )
  h = np.dot ( l, l.transpose ( ) )
  r8mat_print ( n, n, h, '  The Hankel matrix H:' )
#
#  Compute R using NUMPY.
#  The cholesky() function doesn't have upper option yet.
#
# try:
#   r1 = np.linalg.cholesky ( h, lower = False )
  l1 = np.linalg.cholesky ( h )
  r1 = l1.transpose ( )
  r8mat_print ( n, n, r1, '  R computed by NUMPY.LINALG.CHOLESKY:' )
# except np.linalg.LinAlgError:
#   print ( '' )
#   print ( ' NUMPY.LINALG.CHOLESKY says H is not positive definite.' )
#
#  Compute R using r8mat_cholesky_factor_upper.
#
  r2, flag = r8mat_cholesky_factor_upper ( n, h )
  if ( flag != 0 ):
    print ( '' )
    print ( ' r8mat_cholesky_factor_upper() says H is not positive definite.' )
  else:
    r8mat_print ( n, n, r2, '  R computed by r8mat_cholesky_factor_upper():' )
#
#  Compute R using hankel_cholesky.
#
  hanti = np.zeros ( 2 * n - 1 )
  for i in range ( 0, n ):
    hanti[i] = h[i,0]
  for j in range ( 1, n ):
    hanti[n-1+j] = h[n-1,j]

  r3 = hankel_cholesky_upper ( n, hanti )
  r8mat_print ( n, n, r3, '  R computed by hankel_cholesky_upper():' )

  return

def hankel_spd_cholesky_lower ( n, lii, liim1 ):

#*****************************************************************************80
#
## hankel_spd_cholesky_lower() returns L such that L*L' is Hankel SPD.
#
#  Discussion:
#
#    In other words, H = L * L' is a symmetric positive definite matrix
#    with the property that H is constant along antidiagonals, so that
#
#      H(I+J) = h(k-1), for 1 <= I, J <= N, 1 <= K <= 2*N-1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2017
#
#  Author:
#
#    S Al-Homidan, M Alshahrani.
#    Python implementation by John Burkardt.
#
#  Reference:
#
#    S Al-Homidan, M Alshahrani,
#    Positive Definite Hankel Matrices Using Cholesky Factorization,
#    Computational Methods in Applied Mathematics,
#    Volume 9, Number 3, pages 221-225, 2009.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real LII(N), values to be used in L(I,I), for 1 <= I <= N.
#
#    real LIIM1(N-1), values to be used in L(I+1,I) for 1 <= I <= N-1.
#
#  Output:
#
#    real L(N,N), the lower Cholesky factor.
#
  import numpy as np

  l = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    l[i,i] = lii[i]

  for i in range ( 0, n - 1 ):
    l[i+1,i] = liim1[i]

  for i in range ( 2, n ):
    for j in range ( 0, i - 1 ):

      if ( ( ( i + j ) % 2 ) == 0 ):
        q = int ( ( i + j ) / 2 )
        r = q
      else:
        q = int ( ( i + j - 1 ) / 2 )
        r = q + 1

      alpha = 0.0
      for s in range ( 0, q + 1 ):
        alpha = alpha + l[q,s] * l[r,s]

      beta = 0.0
      for t in range ( 0, j ):
        beta = beta + l[i,t] * l[j,t]

      l[i,j] = ( alpha - beta ) / l[j,j]

  return l

def hankel_spd_cholesky_lower_test01 ( rng ):

#*****************************************************************************80
#
## hankel_spd_cholesky_lower_test01() tests hankel_spd_cholesky_lower().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng(): the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'hankel_spd_cholesky_lower_test01():' )
  print ( '  hankel_spd_cholesky_lower() computes a lower Cholesky' )
  print ( '  matrix L such that the matrix H = L * L\' is a' )
  print ( '  symmetric positive definite Hankel matrix.' )

  n = 5
  lii = np.ones ( n )
  liim1 = np.ones ( n - 1 )

  l = hankel_spd_cholesky_lower ( n, lii, liim1 )

  r8mat_print ( n, n, l, '  The Cholesky factor L:' )

  h = np.dot ( l, l.transpose ( ) )

  r8mat_print ( n, n, h, '  The Hankel matrix H = L * L\':' )

  n = 5
  lii = np.zeros ( n )
  for i in range ( 0, n ):
    lii[i] = float ( i + 1 )

  liim1 = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    liim1[i] = n - float ( i + 1 )

  l = hankel_spd_cholesky_lower ( n, lii, liim1 )

  r8mat_print ( n, n, l, '  The Cholesky factor L:' )

  h = np.dot ( l, l.transpose ( ) )

  r8mat_print ( n, n, h, '  The Hankel matrix H = L * L\':' )

  n = 5
  lii = rng.random ( size = n )
  liim1 = rng.random ( size = n - 1 )

  l = hankel_spd_cholesky_lower ( n, lii, liim1 )

  r8mat_print ( n, n, l, '  The Cholesky factor L:' )

  h = np.dot ( l, l.transpose ( ) )

  r8mat_print ( n, n, h, '  The Hankel matrix H = L * L\':' )

  return

def hankel_spd_cholesky_lower_test02 ( ):

#*****************************************************************************80
#
## hankel_spd_cholesky_lower_test02() tests hankel_spd_cholesky_lower().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 January 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'hankel_spd_cholesky_lower_test02():' )
  print ( '  hankel_spd_cholesky_lower() computes a lower Cholesky' )
  print ( '  matrix L such that the matrix H = L * L\' is a' )
  print ( '  symmetric positive definite Hankel matrix.' )

  n = 5
  lii = np.ones ( n )
  liim1 = np.ones ( n - 1 )

  l = hankel_spd_cholesky_lower ( n, lii, liim1 )

  r8mat_print ( n, n, l, '  The Cholesky factor L:' )

  h = np.dot ( l, l.transpose ( ) )

  r8mat_print ( n, n, h, '  The Hankel matrix H = L * L\':' )

  l2, flag = r8mat_cholesky_factor ( n, h )

  r8mat_print ( n, n, l2, '  The Cholesky factor L2 of H:' )

  h2 = np.dot ( l2, l2.transpose ( ) )

  r8mat_print ( n, n, h2, '  The Hankel matrix H2 = L2 * L2\':' )

  return

def r8mat_cholesky_factor ( n, a ):

#*****************************************************************************80
#
## r8mat_cholesky_factor() computes the Cholesky factor of a symmetric matrix.
#
#  Discussion:
#
#    The matrix must be symmetric positive definite.
#
#    For a symmetric positive definite matrix A, the Cholesky factorization
#    is a lower triangular matrix L such that:
#
#      A = L * L'
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    04 October 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix A.
#
#    real A(N,N), the matrix.
#
#  Output:
#
#    real C(N,N), the N by N lower triangular Cholesky factor.
#
#    bool FLAG:
#    False, no error occurred.
#    True, the matrix is not positive definite.
#
  import numpy as np

  flag = False

  c = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      c[i,j] = a[i,j]

  for j in range ( 0, n ):

    c[0:j,j] = 0.0

    for i in range ( j, n ):

      sum2 = c[j,i]
      for k in range ( 0, j ):
        sum2 = sum2 - c[j,k] * c[i,k]

      if ( i == j ):
        if ( sum2 <= 0.0 ):
          flag = True
          return c, flag
        else:
          c[i,j] = np.sqrt ( sum2 )
      else:
        if ( c[j,j] != 0.0 ):
          c[i,j] = sum2 / c[j,j]
        else:
          c[i,j] = 0.0

  return c, flag

def r8mat_cholesky_factor_test ( ):

#*****************************************************************************80
#
## r8mat_cholesky_factor_test() tests r8mat_cholesky_factor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r8mat_cholesky_factor_test():' )
  print ( '  r8mat_cholesky_factor() determines the' )
  print ( '  lower triangular Cholesky factorization' )
  print ( '  of a symmetric positive definite matrix,' )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( j == i - 1 or j == i + 1 ):
        a[i,j] = -1.0

  r8mat_print ( n, n, a, '  Matrix to be factored:' )
#
#  Compute a Cholesky factor.
#
  l, flag = r8mat_cholesky_factor ( n, a )
  r8mat_print ( n, n, l, '  Cholesky factor L:' )
  d = np.dot ( l, l.transpose ( ) )
  r8mat_print ( n, n, d, '  Product L * L\':' )

  return

def r8mat_cholesky_factor_upper ( n, a ):

#*****************************************************************************80
#
## r8mat_cholesky_factor_upper(): upper Cholesky factor of a symmetric matrix.
#
#  Discussion:
#
#    The matrix must be symmetric positive definite.
#
#    For a symmetric positive definite matrix A, the upper Cholesky 
#    factorization is an upper triangular matrix R such that:
#
#      A = R' * R
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2017
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix A.
#
#    real A(N,N), the matrix.
#
#  Output:
#
#    real C(N,N), the N by N upper triangular Cholesky factor.
#
#    bool FLAG:
#    False, no error occurred.
#    True, the matrix is not positive definite.
#
  import numpy as np

  flag = False

  c = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      c[i,j] = a[i,j]

  for j in range ( 0, n ):

    c[j,0:j] = 0.0

    for i in range ( j, n ):

      sum2 = c[i,j]
      for k in range ( 0, j ):
        sum2 = sum2 - c[k,j] * c[k,i]

      if ( i == j ):
        if ( sum2 <= 0.0 ):
          flag = True
          return c, flag
        else:
          c[j,i] = np.sqrt ( sum2 )
      else:
        if ( c[j,j] != 0.0 ):
          c[j,i] = sum2 / c[j,j]
        else:
          c[j,i] = 0.0

  return c, flag

def r8mat_cholesky_factor_upper_test ( ):

#*****************************************************************************80
#
## r8mat_cholesky_factor_upper_test() tests r8mat_cholesky_factor_upper().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 January 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  n = 5

  print ( '' )
  print ( 'r8mat_cholesky_factor_upper_test():' )
  print ( '  r8mat_cholesky_factor_upper() determines the' )
  print ( '  upper triangular Cholesky factorization' )
  print ( '  of a symmetric positive definite matrix,' )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( j == i - 1 or j == i + 1 ):
        a[i,j] = -1.0

  r8mat_print ( n, n, a, '  Matrix to be factored:' )
#
#  Compute a Cholesky factor.
#
  r, flag = r8mat_cholesky_factor_upper ( n, a )
  r8mat_print ( n, n, r, '  Cholesky factor R:' )
  d = np.dot ( r.transpose ( ), r )
  r8mat_print ( n, n, d, '  Product R\' * R:' )

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
  hankel_cholesky_test ( )
  timestamp ( )

