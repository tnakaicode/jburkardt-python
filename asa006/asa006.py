#! /usr/bin/env python3
#
def asa006_test ( ):

#*****************************************************************************80
#
## asa006_test() tests asa006().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'asa006_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa006()' )

  print ( '' )
  print ( 'asa006_test01():' )
  print ( '  cholesky() computes the Cholesky factorization' )
  print ( '  of a symmetric positive definite matrix.' )
  print ( '  A compressed storage format is used.' )
  print ( '' )
  print ( '  Here we look at the matrix A which is' )
  print ( '  N+1 on the diagonal and' )
  print ( '  N   on the off diagonals.' )
  print ( '' )
  print ( '   N   Null  RMS error' )
  print ( '' )

  for n in range ( 1, 15 ):
    nullty, rms = asa006_test01 ( n )
    print ( '  %2d  %2d  %8.4f' % ( n, nullty, rms ) )

  print ( '' )
  print ( 'asa006_test02():' )
  print ( '  cholesky() computes the Cholesky factorization' )
  print ( '  of a symmetric positive definite matrix.' )
  print ( '  A compressed storage format is used.' )
  print ( '' )
  print ( '  Here we look at the Hilbert matrix' )
  print ( '  A(I,J) = 1 / ( I + J - 1 )' )
  print ( '' )
  print ( '  We expect errors to grow quickly with N.' )
  print ( '' )
  print ( '   N   Null  RMS error' )
  print ( '' )

  for n in range ( 1, 15 ):
    nullty, rms = asa006_test02 ( n )
    print ( '  %2d  %2d  %8.4f' % ( n, nullty, rms ) )

  n = 15
  asa006_test03 ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa006_test():' )
  print ( '  Normal end of execution.' )

  return

def asa006_test01 ( n ):

#*****************************************************************************80
#
## asa006_test01() tests cholesky().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the order of the matrix to be examined.
#
  import numpy as np

  nn = ( n * ( n + 1 ) ) // 2
#
#  Set A to the lower triangle of the matrix which is N+1 on the diagonal
#  and N on the off diagonals.
#
  a = np.zeros ( nn )

  k = 0
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      a[k] = n
      k = k + 1
    a[k] = n + 1
    k = k + 1
#
#  Analyze the matrix.
#
  u, nullty, ifault = cholesky ( a, n )
#
#  Form UFULL.
#
  ufull = np.zeros ( [ n, n ] )
  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      ufull[i,j] = u[k]
      k = k + 1
#
#  Compute || A - U' * U ||.
#
  k = 0
  rms = 0.0
  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):
      utu = 0.0
      for l in range ( 0, n ):
        utu = utu + ufull[l,i] * ufull[l,j]
      rms = rms + ( a[k] - utu ) * ( a[k] - utu )
      k = k + 1

  rms = np.sqrt ( rms )

  return nullty, rms

def asa006_test02 ( n ):

#*****************************************************************************80
#
## asa006_test02() tests cholesky().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the order of the matrix to be examined.
#
  import numpy as np

  nn = ( n * ( n + 1 ) ) // 2
#
#  Set A to the Hilbert matrix.
#
  a = np.zeros ( nn )

  k = 0
  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):
      a[k] = 1.0 / ( i + j + 1 )
      k = k + 1

  u, nullty, ifault = cholesky ( a, n )

  ufull = np.zeros ( [ n, n ] )
  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      ufull[i,j] = u[k]
      k = k + 1
#
#  Compute U' * U and compare to A.
#
  k = 0
  rms = 0.0
  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):
      utu = 0.0
      for l in range ( 0, n ):
        utu = utu + ufull[l,i] * ufull[l,j]
      rms = rms + ( a[k] - utu ) * ( a[k] - utu )
      k = k + 1

  rms = np.sqrt ( rms )

  return nullty, rms

def asa006_test03 ( n ):

#*****************************************************************************80
#
## asa006_test03() tests subchl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nn = ( n * ( n + 1 ) ) // 2

  print ( '' )
  print ( 'asa006_test03():' )
  print ( '  subchl() computes the Cholesky factor of a submatrix' )
  print ( '  of a symmetric positive definite matrix.' )
  print ( '  A compressed storage format is used.' )
  print ( '' )
  print ( '  Here we look at the Hilbert matrix' )
  print ( '  A(I,J) = 1/(I+J-1).' )
  print ( '' )
  print ( '  For this particular matrix, we expect the' )
  print ( '  errors to grow rapidly.' )
  print ( '' )
  print ( '  N  NSUB  NULLTY  DET  RMS' )
  print ( '' )
#
#  Set A to the N order Hilbert matrix.
#
  a = np.zeros ( nn )

  k = 0
  for i in range ( 0, n ):
    for j in range ( 0, i + 1 ):
      a[k] = 1.0 / ( i + j + 1 )
      k = k + 1
#
#  Now analyze submatrices of A.
#
  for nsub in range ( 1, n + 1 ):

    b = np.zeros ( nsub, dtype = int )

    for i in range ( 0, nsub ):
      b[i] = i + 1

    u, nullty, ifault, det = subchl ( a, b, nsub )

    if ( ifault != 0 ):

      print ( '  %2d  %2d  Numerical singularity!' % ( n, nsub ) )

    else:

      ufull = np.zeros ( [ nsub, nsub ] )

      k = 0
      for j in range ( 0, nsub ):
        for i in range ( 0, j + 1 ):
          ufull[i,j] = u[k]
          k = k + 1
#
#  Compute U' * U and compare to A.
#
      k = 0
      rms = 0.0
      for i in range ( 0, nsub ):
        for j in range ( 0, i + 1 ):
          utu = 0.0
          for l in range ( 0, nsub ):
            utu = utu + ufull[l,i] * ufull[l,j]
          rms = rms + ( a[k] - utu ) * ( a[k] - utu )
          k = k + 1

      rms = np.sqrt ( rms )

      print ( '  %2d  %2d  %2d  %8.4e  %8.4e' % ( n, nsub, nullty, det, rms ) )

  return

def cholesky ( a, n ):

#*****************************************************************************80
#
## cholesky() computes the Cholesky factorization of an SPD matrix.
#
#  Discussion:
#
#    For a positive definite symmetric matrix A, the Cholesky factor U
#    is an upper triangular matrix such that A = U' * U.
#
#    This routine was originally named "CHOL", but that conflicts with
#    the name of a built in MATLAB routine.
#
#    The missing initialization "II = 0" has been added to the code.
#
#    Making the Python version of this code was awkward and unpleasant.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    Original FORTRAN77 version by Michael Healy.
#    Modifications by AJ Miller.
#    This version by John Burkardt.
#
#  Reference:
#
#    Michael Healy,
#    Algorithm AS 6:
#    Triangular decomposition of a symmetric matrix,
#    Applied Statistics,
#    Volume 17, Number 2, 1968, pages 195-197.
#
#  Input:
#
#    real A((N*(N+1))/2), a symmetric positive definite matrix
#    stored by rows in lower triangular form as a one dimensional array,
#    in the sequence
#    A(1,1),
#    A(2,1), A(2,2),
#    A(3,1), A(3,2), A(3,3), and so on.
#
#    integer N, the order of A.
#
#    integer NN, the dimension of the array used to store A, 
#    which should be at least (N*(N+1))/2.
#
#  Output:
#
#    real U((N*(N+1))/2), an upper triangular matrix,
#    stored by columns, which is the Cholesky factor of A.  
#
#    integer NULLTY, the rank deficiency of A.  If NULLTY is zero,
#    the matrix is judged to have full rank.
#
#    integer IFAULT, an error indicator.
#    0, no error was detected
#    1, if N < 1
#    2, if A is not positive semi-definite.
#    3, if NN < (N*(N+1))/2.
#
#  Local:
#
#    real ETA, should be set equal to the smallest positive
#    value such that 1.0 + ETA is calculated as being greater than 1.0 in the
#    accuracy being used.
#
  import numpy as np
#
#  Initialize output.
#
  nn = ( n * ( n + 1 ) ) // 2
  u = np.zeros ( nn )
  nullty = 0
  ifault = 0

  eta = 1.0E-09

  if ( n <= 0 ):
    ifault = 1
    return u, nullty, ifault

  j = 1
  k = 0
  ii = 0
#
#  Factorize column by column, ICOL = column number.
#
  for icol in range ( 1, n + 1 ):

    ii = ii + icol
    x = eta * eta * a[ii-1]
    l = 0
    kk = 0
#
#  IROW = row number within column ICOL.
#
    for irow in range ( 1, icol + 1 ):

      kk = kk + irow
      k = k + 1
      w = a[k-1]
      m = j

      for i in range ( 1, irow ):
        l = l + 1
        w = w - u[l-1] * u[m-1]
        m = m + 1

      l = l + 1

      if ( irow == icol ):
        break

      if ( u[l-1] != 0.0 ):

        u[k-1] = w / u[l-1]

      else:

        u[k-1] = 0.0

        if ( np.abs ( x * a[k-1] ) < w * w ):
          ifault = 2
          return u, nullty, ifault
#
#  End of row, estimate relative accuracy of diagonal element.
#
    if ( np.abs ( w ) <= np.abs ( eta * a[k-1] ) ):

      u[k-1] = 0.0
      nullty = nullty + 1

    else:

      if ( w < 0.0 ):
        ifault = 2
        return u, nullty, ifault

      u[k-1] = np.sqrt ( w )

    j = j + icol

  return u, nullty, ifault

def subchl ( a, b, nsub ):

#*****************************************************************************80
#
## subchl() computes the Cholesky factorization of a submatrix of an SPD matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 August 2022
#
#  Author:
#
#    Original FORTRAN77 version by Michael Healy, PR Freeman.
#    This version by John Burkardt.
#
#  Reference:
#
#    PR Freeman,
#    Remark AS R44:
#    A Remark on AS 6 and AS7: Triangular decomposition of a symmetric matrix
#    and Inversion of a positive semi-definite symmetric matrix,
#    Applied Statistics,
#    Volume 31, Number 3, 1982, pages 336-339.
#
#    Michael Healy,
#    Algorithm AS 6:
#    Triangular decomposition of a symmetric matrix,
#    Applied Statistics,
#    Volume 17, Number 2, 1968, pages 195-197.
#
#  Input:
#
#    real A((N*(M+1))/2), a positive definite matrix
#    stored by rows in lower triangular form as a one dimensional array,
#    in the sequence
#    A(1,1),
#    A(2,1), A(2,2),
#    A(3,1), A(3,2), A(3,3), and so on.
#    In the simplest case, N, the order of A, is equal to NSUB.
#
#    integer B(NSUB), indicates the order in which the
#    rows and columns of A are to be used.  In the simplest case,
#    B = (1,2,3...,NSUB).
#
#    integer NSUB, the order of the submatrix, that is,
#    the matrix formed by using B to select NSUB rows and columns of A.
#
#  Output:
#
#    real U((NSUB*(NSUB+1))/2), an upper triangular matrix,
#    stored by columns, which is the Cholesky factor of A.  
#
#    integer NULLTY, the rank deficiency of A.
#    If NULLTY is zero, the matrix is judged to have full rank.
#
#    integer IFAULT, an error indicator.
#    0, no error was detected
#    1, if N < 1
#    2, if A is not positive semi-definite.
#
#    real DET, the determinant of the matrix.
#
  import numpy as np

  nnsub = ( nsub * ( nsub + 1 ) ) // 2
  u = np.zeros ( nnsub )

  eta = 1.0E-09
  ifault = 0
  nullty = 0
  det = 1.0

  if ( nsub <= 0 ):
    ifault = 1
    return u, nullty, ifault, det

  j = 1
  k = 0

  for icol in range ( 1, nsub + 1 ):

    ij = ( b[icol-1] * ( b[icol-1] - 1 ) ) // 2
    ii = ij + b[icol-1]
    x = eta * eta * a[ii-1]
    l = 0

    for irow in range ( 1, icol + 1 ):

      kk = ( b[irow-1] * ( b[irow-1] + 1 ) ) // 2
      k = k + 1
      jj = ij + b[irow-1]
      w = a[jj-1]
      m = j

      for i in range ( 1, irow ):
        l = l + 1
        w = w - u[l-1] * u[m-1]
        m = m + 1

      l = l + 1

      if ( irow == icol ):
        break

      if ( u[l-1] != 0.0 ):

        u[k-1] = w / u[l-1]

      else:

        if ( np.abs ( x * a[kk-1] ) < w * w ):
          ifault = 2
          return u, nullty, ifault, det

        u[k-1] = 0.0

    if ( np.abs ( eta * a[kk-1] ) <= np.abs ( w ) ):

      if ( w < 0.0 ):
        ifault = 2
        return u, nullty, ifault, det

      u[k-1] = np.sqrt ( w )

    else:

      u[k-1] = 0.0
      nullty = nullty + 1

    j = j + icol
    det = det * u[k-1] * u[k-1]

  return u, nullty, ifault, det

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
  asa006_test ( )
  timestamp ( )

