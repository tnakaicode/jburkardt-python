#! /usr/bin/env python3
#
def r8pp_test ( ):

#*****************************************************************************80
#
## r8pp_test() tests r8pp().
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
  print ( 'r8pp_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8pp().' )

  r8ge_to_r8pp_test ( )

  r8pp_det_test ( )
  r8pp_dif2_test ( )
  r8pp_fa_test ( )
  r8pp_indicator_test ( )
  r8pp_mv_test ( )
  r8pp_print_test ( )
  r8pp_print_some_test ( )
  r8pp_random_test ( )
  r8pp_sl_test ( )
  r8pp_to_r8ge_test ( )
  r8pp_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8pp_test():' )
  print ( '  Normal end of execution.' )
  return

def i4_log_10 ( i ):

#*****************************************************************************80
#
## i4_log_10() returns the integer part of the logarithm base 10 of ABS(X).
#
#  Example:
#
#        I  VALUE
#    -----  --------
#        0    0
#        1    0
#        2    0
#        9    0
#       10    1
#       11    1
#       99    1
#      100    2
#      101    2
#      999    2
#     1000    3
#     1001    3
#     9999    3
#    10000    4
#
#  Discussion:
#
#    i4_log_10 ( I ) + 1 is the number of decimal digits in I.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number whose logarithm base 10 is desired.
#
#  Output:
#
#    integer VALUE, the integer part of the logarithm base 10 of
#    the absolute value of X.
#
  import numpy as np

  i = np.floor ( i )

  if ( i == 0 ):

    value = 0

  else:

    value = 0
    ten_pow = 10

    i_abs = abs ( i )

    while ( ten_pow <= i_abs ):
      value = value + 1
      ten_pow = ten_pow * 10

  return value

def i4_log_10_test ( ) :

#*****************************************************************************80
#
## i4_log_10_test() tests i4_log_10().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
  n = 13

  x = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ]

  print ( '' )
  print ( 'i4_log_10_test():' )
  print ( '  i4_log_10() returns the whole part of log base 10,' )
  print ( '' )
  print ( '  X, i4_log_10' )
  print ( '' )

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print ( '%6d  %12d' % ( x[i], j ) )

  return

def r8ge_to_r8pp ( n, a ):

#*****************************************************************************80
#
## r8ge_to_r8pp() copies an R8GE matrix to an R8PO matrix.
#
#  Discussion:
#
#    The R8PO format assumes the matrix is square and symmetric; it is also 
#    typically assumed that the matrix is positive definite.  These are not
#    required here.  The copied R8PO matrix simply zeros out the lower triangle
#    of the R8GE matrix.
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    The R8PP storage format is appropriate for a symmetric positive
#    definite matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
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
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8GE matrix.
#
#  Output:
#
#    real B(N*(N+1)/2), the R8PP matrix.
#
  import numpy as np

  b = r8pp_zeros ( n )

  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, j + 1 ):
      b[k] = a[i,j]
      k = k + 1

  return b

def r8ge_to_r8pp_test ( ):

#*****************************************************************************80
#
## r8ge_to_r8pp_test() tests r8ge_to_r8pp().
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
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  n = 5
  seed = 123456789

  print ( '' )
  print ( 'r8ge_to_r8pp_test():' )
  print ( '  r8ge_to_r8pp() converts an R8GE matrix to R8PP format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = 2.0 * min ( i, j ) - 1.0

  print ( '' )
  print ( '  The positive definite symmetric R8GE matrix:' )
  print ( a )

  b = r8ge_to_r8pp ( n, a )

  print ( '' )
  print ( '  The RPP matrix:' )
  print ( b )

  return

def r8pp_det ( n, a_lu ):

#*****************************************************************************80
#
## r8pp_det() computes the determinant of a R8PP matrix factored by R8PP_FA.
#
#  Discussion:
#
#    The R8PP storage format is appropriate for a symmetric positive
#    definite matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A_LU((N*(N+1))/2), the LU factors from R8PP_FA.
#
#  Output:
#
#    real DET, the determinant of A.
#
  det = 1.0

  k = 0
  for i in range ( 0, n ):
    det = det * a_lu[k]
    k = k + i + 2

  det = det * det

  return det

def r8pp_det_test ( ):

#*****************************************************************************80
#
## r8pp_det_test() tests r8pp_det().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8pp_det_test():' )
  print ( '  r8pp_det() computes the determinant of an R8PP matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8pp_dif2 ( n )
  r8pp_print ( n, a, '  The R8PP matrix:' )
 
  r, info = r8pp_fa ( n, a )

  det = r8pp_det ( n, r )

  print ( '' )
  print ( '  Computed determinant = ', det )
  print ( '  Exact determinant = ', n + 1 )

  return

def r8pp_dif2 ( n ):

#*****************************************************************************80
#
## r8pp_dif2() sets up an R8PP second difference matrix.
#
#  Discussion:
#
#    The R8PP storage format is appropriate for a symmetric positive
#    definite matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#  Output:
#
#    real A((N*(N+1))/2), the R8PP matrix.
#
  import numpy as np

  nn = ( n * ( n + 1 ) ) // 2
  a = np.zeros ( nn )

  k = 0
  for j in range ( 1, n + 1 ):
    for i in range ( 1, j - 1 ):
      a[k] = 0.0
      k = k + 1
    if ( 1 < j ):
      a[k] = - 1.0
      k = k + 1
    a[k] = 2.0
    k = k + 1

  return a

def r8pp_dif2_test ( ):

#*****************************************************************************80
#
## r8pp_dif2_test() tests r8pp_dif2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8pp_dif2_test():' )
  print ( '  r8pp_dif2() sets up an R8PP second difference matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8pp_dif2 ( n )

  r8pp_print ( n, a, '  The R8PP second difference matrix:' )

  return

def r8pp_fa ( n, a ):

#*****************************************************************************80
#
## r8pp_fa() factors a R8PP matrix.
#
#  Discussion:
#
#    The R8PP storage format is appropriate for a symmetric positive
#    definite matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dongarra, Moler, Bunch and Stewart,
#    LINPACK User's Guide,
#    SIAM, (Society for Industrial and Applied Mathematics),
#    3600 University City Science Center,
#    Philadelphia, PA, 19104-2688.
#    ISBN 0-89871-172-X
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A((N*(N+1))/2), a R8PP matrix.
#
#  Output:
#
#    real R((N*(N+1))/2), an upper triangular matrix R, stored 
#    in packed form, so that A = R'*R.
#
#    integer INFO, error flag.
#    0, for normal return.
#    K, if the leading minor of order K is not positive definite.
#
  import numpy as np

  info = 0

  r = a.copy ( )

  jj = 0

  for j in range ( 1, n + 1 ):

    s = 0.0
    kj = jj
    kk = 0

    for k in range ( 1, j ):

      kj = kj + 1
      t = r[kj-1]
      for i in range ( 1, k ):
        t = t - r[kk+i-1] * r[jj+i-1]
      kk = kk + k
      t = t / r[kk-1]
      r[kj-1] = t
      s = s + t * t

    jj = jj + j
    s = r[jj-1] - s

    if ( s <= 0.0 ):
      info = j
      return r, info

    r[jj-1] = np.sqrt ( s )

  return r, info

def r8pp_fa_test ( ):

#*****************************************************************************80
#
## r8pp_fa_test() tests r8pp_fa().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5
  seed = 123456789

  print ( '' )
  print ( 'r8pp_fa_test():' )
  print ( '  r8pp_fa() factors an R8PP system,' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a, seed = r8pp_random ( n, seed )

  r8pp_print ( n, a, '  The R8PP matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  The desired solution:' )
#
#  Compute the corresponding right hand side.
#
  b = r8pp_mv ( n, a, x )

  r8vec_print ( n, b, '  The right hand side:' )
#
#  Factor the matrix.
#
  a_lu, info = r8pp_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8pp_fa_test(): Fatal error!' )
    print ( '  r8pp_fa() declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    return

  print ( '' )
  print ( '  The R8PP matrix has been factored.' )
#
#  Solve the linear system.
#
  x = r8pp_sl ( n, a_lu, b )
 
  r8vec_print ( n, x, '  Solution:' )

  return

def r8pp_indicator ( n ):

#*****************************************************************************80
#
## r8pp_indicator() sets up a R8PP indicator matrix.
#
#  Discussion:
#
#    The R8PP storage format is appropriate for a symmetric positive
#    definite matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#  Output:
#
#    real A((N*(N+1))/2), the R8PP matrix.
#
  import numpy as np

  nn = ( n * ( n + 1 ) ) // 2
  a = np.zeros ( nn )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  k = 0
  for j in range ( 1, n + 1 ):
    for i in range ( 1, j + 1 ):
      a[k] = float ( fac * i + j )
      k = k + 1

  return a

def r8pp_indicator_test ( ):

#*****************************************************************************80
#
## r8pp_indicator_test() tests r8pp_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8pp_indicator_test():' )
  print ( '  r8pp_indicator() sets up a R8PP indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8pp_indicator ( n )

  r8pp_print ( n, a, '  The R8PP indicator matrix:' )

  return

def r8pp_mv ( n, a, x ):

#*****************************************************************************80
#
## r8pp_mv() multiplies a R8PP matrix times a vector.
#
#  Discussion:
#
#    The R8PP storage format is appropriate for a symmetric positive
#    definite matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A((N*(N+1))/2), the R8PP matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A * x.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 1, n + 1 ):
    for j in range ( 1, i ):
      k = j + ( i * ( i - 1 ) ) // 2
      b[i-1] = b[i-1] + a[k-1] * x[j-1]
    for j in range ( i, n + 1 ):
      k = i + ( j * ( j - 1 ) ) // 2
      b[i-1] = b[i-1] + a[k-1] * x[j-1]

  return b

def r8pp_mv_test ( ):

#*****************************************************************************80
#
## r8pp_mv_test() tests r8pp_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8pp_mv_test():' )
  print ( '  r8pp_mv() computes b=A*x, where A is an R8PP matrix' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8pp_indicator ( n )
  r8pp_print ( n, a, '  The R8PP indicator matrix:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  Vector X:' )

  b = r8pp_mv ( n, a, x )
  r8vec_print ( n, b, '  Product b=A*x' )

  return

def r8pp_print ( n, a, title ):

#*****************************************************************************80
#
## r8pp_print() prints a R8PP matrix.
#
#  Discussion:
#
#    The R8PP storage format is appropriate for a symmetric positive
#    definite matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A((N*(N+1))/2), the R8PP matrix.
#
#    string TITLE, a title to be printed.
#
  r8pp_print_some ( n, a, 0, 0, n - 1, n - 1, title )

  return

def r8pp_print_test ( ):

#*****************************************************************************80
#
## r8pp_print_test() tests r8pp_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8pp_print_test():' )
  print ( '  r8pp_print() prints an R8PP  matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8pp_indicator ( n )

  r8pp_print ( n, a, '  The R8PP matrix:' )

  return

def r8pp_print_some ( n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8pp_print_some() prints some of a R8PP matrix.
#
#  Discussion:
#
#    The R8PP storage format is appropriate for a symmetric positive
#    definite matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#   16 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A((N*(N+1))/2), the R8PP matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )

  incx = 5
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( jlo, jhi + 1, incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, n - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )

      for j in range ( j2lo, j2hi + 1 ):

        if ( i <= j ):
          aij = a[i+(j*(j+1))//2]
        else:
          aij = a[j+(i*(i+1))//2]

        print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def r8pp_print_some_test ( ):

#*****************************************************************************80
#
## r8pp_print_some_test() tests r8pp_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'r8pp_print_some_test():' )
  print ( '  r8pp_print_some() prints some of an R8PP matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8pp_indicator ( n )

  r8pp_print_some ( n, a, 1, 2, 5, 4, '  Rows 1-5, Cols 2-4:' )

  return

def r8pp_random ( n, seed ):

#*****************************************************************************80
#
## r8pp_random() randomizes a R8PP matrix.
#
#  Discussion:
#
#    The R8PP storage format is appropriate for a symmetric positive
#    definite matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
#
#    The matrix is computed by setting a "random" upper triangular
#    Cholesky factor R, and then computing A = R'*R.
#    The randomness is limited by the fact that all the entries of
#    R will be between 0 and 1.  A truly random R is only required
#    to have positive entries on the diagonal.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    integer SEED, a seed for the random number generator.
#
#  Output:
#
#    real A((N*(N+1))/2), the R8PP matrix.
#
#    integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  nn = ( n * ( n + 1 ) ) // 2
  a = np.zeros ( nn )

  for i in range ( n, 0, -1 ):
#
#  Set row I of R.
#
    for j in range ( i, n + 1 ):
      ij = i + ( j * ( j - 1 ) ) // 2
      a[ij-1], seed = r8_uniform_01 ( seed )
#
#  Consider element J of row I, last to first.
#
    for j in range ( n, i - 1, -1 ):
#
#  Add multiples of row I to lower elements of column J.
#
      ij = i + ( j * ( j - 1 ) ) // 2

      for k in range ( i + 1, j + 1 ):
        kj = k + ( j * ( j - 1 ) ) // 2
        ik = i + ( k * ( k - 1 ) ) // 2
        a[kj-1] = a[kj-1] + a[ik-1] * a[ij-1]
#
#  Reset element J.
#
      ii = i + ( i * ( i - 1 ) ) // 2
      a[ij-1] = a[ii-1] * a[ij-1]

  return a, seed

def r8pp_random_test ( ):

#*****************************************************************************80
#
## r8pp_random_test() tests r8pp_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5
  seed = 123456789

  print ( '' )
  print ( 'r8pp_random_test():' )
  print ( '  r8pp_random() computes a random symmetric positive definite' )
  print ( '  packed matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a, seed = r8pp_random ( n, seed )

  r8pp_print ( n, a, '  The random R8PP matrix' )

  return

def r8pp_sl ( n, r, b ):

#*****************************************************************************80
#
## r8pp_sl() solves a R8PP system factored by R8PP_FA.
#
#  Discussion:
#
#    The R8PP storage format is appropriate for a symmetric positive
#    definite matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Dongarra, Moler, Bunch and Stewart,
#    LINPACK User's Guide,
#    SIAM, (Society for Industrial and Applied Mathematics),
#    3600 University City Science Center,
#    Philadelphia, PA, 19104-2688.
#    ISBN 0-89871-172-X
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real R((N*(N+1))/2), the R factor output from R8PP_FA.
#
#    real B(N), the right hand side.
#
#  Output:
#
#    real X(N), the solution.
#
  import numpy as np

  x = b.copy ( )

  kk = 0

  for k in range ( 1, n + 1 ):
    t = 0.0
    for i in range ( 1, k ):
      t = t + r[kk+i-1] * x[i-1]
    kk = kk + k
    x[k-1] = ( x[k-1] - t ) / r[kk-1]

  for k in range ( n, 0, -1 ):
    x[k-1] = x[k-1] / r[kk-1]
    kk = kk - k
    t = - x[k-1]
    for i in range ( 1, k ):
      x[i-1] = x[i-1] + t * r[kk+i-1]

  return x

def r8pp_sl_test ( ):

#*****************************************************************************80
#
## r8pp_sl_test() tests r8pp_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5
  seed = 123456789

  print ( '' )
  print ( 'r8pp_sl_test():' )
  print ( '  r8pp_sl() solves a linear system factored by R8PP_FA.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a, seed = r8pp_random ( n, seed )

  r8pp_print ( n, a, '  The R8PP matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  The desired solution:' )
#
#  Compute the corresponding right hand side.
#
  b = r8pp_mv ( n, a, x )

  r8vec_print ( n, b, '  The right hand side:' )
#
#  Factor the matrix.
#
  a_lu, info = r8pp_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r8pp_sl_test(): Fatal error!' )
    print ( '  r8pp_fa() declares the matrix is singular!' )
    print ( '  The value of INFO is ', info )
    return

  print ( '' )
  print ( '  The R8PP matrix has been factored.' )
#
#  Solve the linear system.
#
  x = r8pp_sl ( n, a_lu, b )
 
  r8vec_print ( n, x, '  Solution:' )

  return

def r8pp_to_r8ge ( n, a ):

#*****************************************************************************80
#
## r8pp_to_r8ge() copies a R8PP matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8PP storage format is appropriate for a symmetric positive
#    definite matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A((N*(N+1))/2), the R8PP matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        b[i,j] = a[i+(j*(j+1))//2]
      else:
        b[i,j] = a[j+(i*(i+1))//2]

  return b

def r8pp_to_r8ge_test ( ):

#*****************************************************************************80
#
## r8pp_to_r8ge_test() tests r8pp_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8pp_to_r8ge_test()' )
  print ( '  r8pp_to_r8ge() converts an R8PP matrix to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8pp_indicator ( n )

  print ( '' )
  print ( '  The R8PP indicator matrix:' )
  print ( a )

  a_r8ge = r8pp_to_r8ge ( n, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8pp_zeros ( n ):

#*****************************************************************************80
#
## r8pp_zeros() zeros an R8PP matrix.
#
#  Discussion:
#
#    The R8PP storage format is appropriate for a symmetric positive
#    definite matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#  Output:
#
#    real A((N*(N+1))/2), the R8PP matrix.
#
  import numpy as np

  nn = ( n * ( n + 1 ) ) // 2
  a = np.zeros ( nn )

  return a

def r8pp_zeros_test ( ):

#*****************************************************************************80
#
## r8pp_zeros_test() tests r8pp_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8pp_zeros_test():' )
  print ( '  r8pp_zeros() sets an R8PP zero matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8pp_zeros ( n )

  r8pp_print ( n, a, '  The R8PP zero matrix:' )

  return

def r8_uniform_01 ( seed ):

#*****************************************************************************80
#
## r8_uniform_01() returns a unit pseudorandom R8.
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
#    This code is distributed under the MIT license. 
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
#  Input:
#
#    integer SEED, the integer "seed" used to generate
#    the output random number.  SEED should not be 0.
#
#  Output:
#
#    real R, a random value between 0 and 1.
#
#    integer SEED, the updated seed.  This would
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
    print ( 'r8_uniform_01(): Fatal error!' )
    print ( '  Input SEED = 0!' )
    raise Exception ( 'r8_uniform_01(): Fatal error!' )

  k = floor ( seed / 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10

  return r, seed

def r8_uniform_01_test ( ):

#*****************************************************************************80
#
## r8_uniform_01_test() tests r8_uniform_01().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8_uniform_01_test():' )
  print ( '  r8_uniform_01() produces a sequence of random values.' )

  seed = 123456789

  print ( '' )
  print ( '  Using random seed ', seed )

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

  return

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## r8vec_indicator1() sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    real A(N), the indicator array.
#
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## r8vec_indicator1_test() tests r8vec_indicator1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_indicator1_test():' )
  print ( '  r8vec_indicator1() returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )

  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an r8vec.
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
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

  return

def r8vec_print_test ( ):

#*****************************************************************************80
#
## r8vec_print_test() tests r8vec_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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

  print ( '' )
  print ( 'r8vec_print_test():' )
  print ( '  r8vec_print() prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )

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
  print (  time.ctime ( t ) )

  return

def timestamp_test ( ):

#*****************************************************************************80
#
## timestamp_test() tests timestamp().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'timestamp_test():' )
  print ( '  timestamp() prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  r8pp_test ( )
  timestamp ( )

