#! /usr/bin/env python3
#
def asa007_test ( ):

#*****************************************************************************80
#
## asa007_test() tests asa007().
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
  print ( 'asa007_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa007().' )

  asa007_test01 ( )
  asa007_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa007_test():' )
  print ( '  Normal end of execution.' )

  return

def asa007_test01 ( ):

#*****************************************************************************80
#
## asa007_test01() tests syminv().
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

  n_max = 15

  print ( '' )
  print ( 'asa007_test01():' )
  print ( '  syminv() computes the inverse of a symmetric positive definite matrix.' )
  print ( '  A compressed storage format is used.' )
  print ( '' )
  print ( '  Here we look at the matrix A which is' )
  print ( '  N+1 on the diagonal and' )
  print ( '  N   on the off diagonals.' )
  print ( '' )
  print ( '    N   Nullty  RMS' )
  print ( '' )

  for n in range ( 1, n_max + 1 ):
#
#  Set A to the lower triangle of the matrix which is N+1 on the diagonal
#  and N on the off diagonals.
#
    nn = ( n * ( n + 1 ) ) // 2
    a = np.zeros ( nn )

    k = 0
    for i in range ( 0, n ):
      for j in range ( 0, i ):
        a[k] = n
        k = k + 1
      a[k] = n + 1
      k = k + 1

    c, nullty, ifault = syminv ( a, n )

    cfull = np.zeros ( [ n, n ] )
    k = 0
    for j in range ( 0, n ):
      for i in range ( 0, j ):
        cfull[i,j] = c[k]
        cfull[j,i] = c[k]
        k = k + 1
      cfull[j,j] = c[k]
      k = k + 1

    afull = np.zeros ( [ n, n ] )
    k = 0
    for j in range ( 0, n ):
      for i in range ( 0, j ):
        afull[i,j] = a[k]
        afull[j,i] = a[k]
        k = k + 1
      afull[j,j] = a[k]
      k = k + 1
#
#  Compute C * A - I.
#
    b = np.matmul ( cfull, afull ) - np.identity ( n )
    diff = np.linalg.norm ( b )

    print ( '  %2d  %2d  %g' % ( n, nullty, diff ) )

  return

def asa007_test02 ( ):

#*****************************************************************************80
#
## asa007_test02() tests syminv().
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

  n_max = 15

  print ( '' )
  print ( 'asa007_test02():' )
  print ( '  syminv() computes the inverse of a symmetric positive' )
  print ( '  definite matrix.' )
  print ( '  A compressed storage format is used.' )
  print ( '' )
  print ( '  Here we look at the Hilbert matrix' )
  print ( '  A(I,J) = 1 / ( I + J - 1 )' )
  print ( '' )
  print ( '  We expect errors to grow quickly with N.' )
  print ( '' )
  print ( '    N   Nullty  RMS' )
  print ( '' )

  for n in range ( 0, n_max + 1 ):
#
#  Set A to the Hilbert matrix.
#
    nn = ( n * ( n + 1 ) ) // 2
    a = np.zeros ( nn )

    k = 0
    for i in range ( 0, n ):
      for j in range ( 0, i + 1 ):
        a[k] = 1.0 / ( i + j + 1 )
        k = k + 1

    c, nullty, ifault = syminv ( a, n )

    cfull = np.zeros ( [ n, n ] )
    k = 0
    for j in range ( 0, n ):
      for i in range ( 0, j ):
        cfull[i,j] = c[k]
        cfull[j,i] = c[k]
        k = k + 1
      cfull[j,j] = c[k]
      k = k + 1

    afull = np.zeros ( [ n, n ] )
    k = 0
    for j in range ( 0, n ):
      for i in range ( 0, j ):
        afull[i,j] = a[k]
        afull[j,i] = a[k]
        k = k + 1
      afull[j,j] = a[k]
      k = k + 1
#
#  Compute C * A - I.
#
    b = np.matmul ( cfull, afull ) - np.identity ( n )
    diff = np.linalg.norm ( b )

    print ( '  %2d  %2d  %g' % ( n, nullty, diff ) )

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

def syminv ( a, n ):

#*****************************************************************************80
#
## syminv() computes the inverse of a symmetric matrix.
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
#    This version by John Burkardt.
#
#  Reference:
#
#    Michael Healy,
#    Algorithm AS 7:
#    Inversion of a Positive Semi-Definite Symmetric Matrix,
#    Applied Statistics,
#    Volume 17, Number 2, 1968, pages 198-199.
#
#  Input:
#
#    real A((N*(N+1))/2), a positive definite matrix stored
#    by rows in lower triangular form as a one dimensional array, in the sequence
#    A(1,1),
#    A(2,1), A(2,2),
#    A(3,1), A(3,2), A(3,3), and so on.
#
#    integer N, the order of A.
#
#  Output:
#
#    real C((N*(N+1))/2), the inverse of A, or generalized
#    inverse if A is singular, stored using the same storage scheme employed
#    for A. 
#
#    integer NULLTY, the rank deficiency of A.  If NULLTY is zero,
#    the matrix is judged to have full rank.
#
#    integer IFAULT, error indicator.
#    0, no error detected.
#    1, N < 1.
#    2, A is not positive semi-definite.
#
  import numpy as np

  nn = ( n * ( n + 1 ) ) // 2
  c = np.zeros ( nn )
  nullty = 0
  ifault = 0

  if ( n <= 0 ):
    ifault = 1
    return c, nullty, ifault

  nrow = n
#
#  Compute the Cholesky factorization of A.
#  The result is stored in C.
#
  c, nullty, ifault = cholesky ( a, n )

  if ( ifault != 0 ):
    return c, nullty, ifault
#
#  Invert C and form the product (Cinv)' * Cinv, where Cinv is the inverse
#  of C, row by row starting with the last row.
#  IROW = the row number,
#  NDIAG = location of last element in the row.
#
  irow = nrow
  ndiag = nn

  while ( True ):
#
#  Special case, zero diagonal element.
#
    w = np.zeros ( nrow )

    if ( c[ndiag-1] == 0.0 ):

      l = ndiag
      for j in range ( irow, nrow + 1 ):
        c[l-1] = 0.0
        l = l + j

    else:

      l = ndiag
      for i in range ( irow, nrow + 1 ):
        w[i-1] = c[l-1]
        l = l + i

      icol = nrow
      jcol = nn
      mdiag = nn

      while ( True ):

        l = jcol

        if ( icol == irow ):
          x = 1.0 / w[irow-1]
        else:
          x = 0.0

        k = nrow

        while ( irow < k ):

          x = x - w[k-1] * c[l-1]
          k = k - 1
          l = l - 1

          if ( mdiag < l ):
            l = l - k + 1

        c[l-1] = x / w[irow-1]

        if ( icol <= irow ):
          break

        mdiag = mdiag - icol
        icol = icol - 1
        jcol = jcol - 1

    ndiag = ndiag - irow
    irow = irow - 1

    if ( irow <= 0 ):
      break

  return c, nullty, ifault

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
  asa007_test ( )
  timestamp ( )

