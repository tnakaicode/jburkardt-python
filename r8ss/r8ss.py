#! /usr/bin/env python3
#
def r8ss_test ( ):

#*****************************************************************************80
#
## r8ss_test() tests r8ss().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8ss_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8ss().' )

  r8ss_dif2_test ( )
  r8ss_indicator_test ( )
  r8ss_mv_test ( )
  r8ss_print_test ( )
  r8ss_print_some_test ( )
  r8ss_random_test ( )
  r8ss_to_r8ge_test ( )
  r8ss_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8ss_test():' )
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

def i4vec_print ( n, a, title ):

#*****************************************************************************80
#
## i4vec_print() prints an I4VEC.
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
#    integer A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %6d' % ( i, a[i] ) )

  return

def r8ss_dif2 ( n ):

#*****************************************************************************80
#
# R8SS_DIF2 sets up an R8SS second difference matrix.
#
#  Discussion:
#
#    The R8SS storage format is used for real symmetric skyline matrices.
#    This storage is appropriate when the nonzero entries of the
#    matrix are generally close to the diagonal, but the number
#    of nonzeroes above each diagonal varies in an irregular fashion.
#
#    In this case, the strategy is essentially to assign column J
#    its own bandwidth, and store the strips of nonzeros one after
#    another.   Note that what's important is the location of the
#    furthest nonzero from the diagonal.  A slot will be set up for
#    every entry between that and the diagonal, whether or not
#    those entries are zero.
#
#    A skyline matrix can be Gauss-eliminated without disrupting
#    the storage scheme, as long as no pivoting is required.
#
#    The user must set aside ( N * ( N + 1 ) ) / 2 entries for the array,
#    although the actual storage needed will generally be about half of
#    that.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 July 2016
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
#    integer NA, the dimension of the array A, which for
#    this special case will 2*N-1.
#
#    integer DIAG(N), the indices in A of the N diagonal
#    elements.
#
#    real A(2*N-1), the R8SS matrix.
#
  import numpy as np

  diag = np.zeros ( n, dtype = np.int32 )
  a = np.zeros ( 2 * n - 1 )

  na = 0

  for j in range ( 0, n ):

    if ( 0 < j ):
      a[na] = -1.0
      na = na + 1

    a[na] = 2.0
    diag[j] = na
    na = na + 1

  return na, diag, a

def r8ss_dif2_test ( ):

#*****************************************************************************80
#
# R8SS_DIF2_TEST tests R8SS_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8SS_DIF2_TEST' )
  print ( '  R8SS_DIF2 returns the second difference matrix in R8SS format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  na, diag, a = r8ss_dif2 ( n )
#
#  Print information.
#
  print ( '' )
  print ( '  Number of nonzero entries stored is ', na )

  i4vec_print ( n, diag, '  Diagonal storage indices:' )

  r8ss_print ( n, na, diag, a, '  The R8SS second difference matrix:' )

  return

def r8ss_indicator ( n ):

#*****************************************************************************80
#
# R8SS_INDICATOR sets up a R8SS indicator matrix.
#
#  Discussion:
#
#    The R8SS storage format is used for real symmetric skyline matrices.
#    This storage is appropriate when the nonzero entries of the
#    matrix are generally close to the diagonal, but the number
#    of nonzeroes above each diagonal varies in an irregular fashion.
#
#    In this case, the strategy is essentially to assign column J
#    its own bandwidth, and store the strips of nonzeros one after
#    another.   Note that what's important is the location of the
#    furthest nonzero from the diagonal.  A slot will be set up for
#    every entry between that and the diagonal, whether or not
#    those entries are zero.
#
#    A skyline matrix can be Gauss-eliminated without disrupting
#    the storage scheme, as long as no pivoting is required.
#
#    The user must set aside ( N * ( N + 1 ) ) / 2 entries for the array,
#    although the actual storage needed will generally be about half of
#    that.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
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
#    integer NA, the dimension of the array A, which for this
#    special case will be the maximum, ( N * ( N + 1 ) ) / 2
#
#    integer DIAG(N), the indices in A of the N diagonal elements.
#
#    real A((N*(N+1))/2), the R8SS matrix.
#
  import numpy as np

  diag = np.zeros ( n, dtype = np.int32 )
  a = np.zeros ( ( n * ( n + 1 ) ) // 2 )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  na = 0

  for j in range ( 0, n ):

    for i in range ( 0, j + 1 ):
      a[na] = float ( fac * ( i + 1 ) + ( j + 1 ) )
      if ( i == j ):
        diag[j] = na
      na = na + 1

  return na, diag, a

def r8ss_indicator_test ( ):

#*****************************************************************************80
#
# R8SS_INDICATOR_TEST tests R8SS_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8SS_INDICATOR_TEST' )
  print ( '  R8SS_INDICATOR computes an indicator matrix.' )
  print ( '  for a symmetric skyline storage matrix,' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  na, diag, a = r8ss_indicator ( n )

  r8ss_print ( n, na, diag, a, '  The R8SS indicator matrix:' )

  return

def r8ss_mv ( n, na, diag, a, x ):

#*****************************************************************************80
#
# R8SS_MV multiplies a R8SS matrix times a vector.
#
#  Discussion:
#
#    The R8SS storage format is used for real symmetric skyline matrices.
#    This storage is appropriate when the nonzero entries of the
#    matrix are generally close to the diagonal, but the number
#    of nonzeroes above each diagonal varies in an irregular fashion.
#
#    In this case, the strategy is essentially to assign column J
#    its own bandwidth, and store the strips of nonzeros one after
#    another.   Note that what's important is the location of the
#    furthest nonzero from the diagonal.  A slot will be set up for
#    every entry between that and the diagonal, whether or not
#    those entries are zero.
#
#    A skyline matrix can be Gauss-eliminated without disrupting
#    the storage scheme, as long as no pivoting is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
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
#    integer NA, the dimension of the array A.
#    NA must be at least N.
#
#    integer DIAG(N), the indices in A of the N diagonal elements.
#
#    real A(NA), the R8SS matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A*x.
#
  import numpy as np

  b = np.zeros ( n )

  diagold = -1
  k = 0

  for j in range ( 0, n ):

    ilo = j + 1 - ( diag[j] - diagold )

    for i in range ( ilo, j ):
      b[i] = b[i] + a[k] * x[j]
      b[j] = b[j] + a[k] * x[i]
      k = k + 1

    b[j] = b[j] + a[k] * x[j]
    k = k + 1
    diagold = diag[j]

  return b

def r8ss_mv_test ( ):

#*****************************************************************************80
#
# R8SS_MV_TEST tests R8SS_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'R8SS_MV_TEST' )
  print ( '  R8SS_MV computes A*x, where A is an R8SS matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  na, diag, a = r8ss_random ( n )
#
#  Replace the random entries by marker values.
#
  ij = 0
  for j in range ( 0, n ):

    if ( j == 0 ):
      ilo = 0
    else:
      ilo = j + 1 - ( diag[j] - diag[j-1] )

    for i in range ( ilo, j + 1 ):
      a[ij] = float ( 10 * ( i + 1) + j + 1 )
      ij = ij + 1
#
#  Print information.
#
  print ( '' )
  print ( '  Number of nonzero entries stored is ', na )

  i4vec_print ( n, diag, '  Diagonal storage indices:' )

  r8ss_print ( n, na, diag, a, '  The R8SS matrix:' )
#
#  Copy the matrix into a general matrix.
#
  a2 = r8ss_to_r8ge ( n, na, diag, a )
#
#  Set the vector X.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the product.
#
  b = r8ss_mv ( n, na, diag, a, x )
#
#  Compute the product using the general matrix.
#
  b2 = np.dot ( a2, x )
#
#  Compare the results.
#
  r8vec2_print ( b, b2, '  R8SS_MV verse R8GE_MV' )

  return

def r8ss_print ( n, na, diag, a, title ):

#*****************************************************************************80
#
# R8SS_PRINT prints a R8SS matrix.
#
#  Discussion:
#
#    The R8SS storage format is used for real symmetric skyline matrices.
#    This storage is appropriate when the nonzero entries of the
#    matrix are generally close to the diagonal, but the number
#    of nonzeroes above each diagonal varies in an irregular fashion.
#
#    In this case, the strategy is essentially to assign column J
#    its own bandwidth, and store the strips of nonzeros one after
#    another.   Note that what's important is the location of the
#    furthest nonzero from the diagonal.  A slot will be set up for
#    every entry between that and the diagonal, whether or not
#    those entries are zero.
#
#    A skyline matrix can be Gauss-eliminated without disrupting
#    the storage scheme, as long as no pivoting is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
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
#    integer NA, the dimension of the array A.
#
#    integer DIAG(N), the indices in A of the N diagonal elements.
#
#    real A(NA), the R8SS matrix.
#
#    string TITLE, a title to be printed.
#
  r8ss_print_some ( n, na, diag, a, 0, 0, n - 1, n - 1, title )

  return

def r8ss_print_test ( ):

#*****************************************************************************80
#
# R8SS_PRINT_TEST tests R8SS_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8SS_PRINT_TEST' )
  print ( '  R8SS_PRINT prints an R8SS matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  na, diag, a = r8ss_random ( n )

  print ( '' )
  print ( '  Number of nonzero entries stored is ', na )

  i4vec_print ( n, diag, '  Diagonal storage indices:' )

  r8ss_print ( n, na, diag, a, '  The R8SS matrix:' )

  return

def r8ss_print_some ( n, na, diag, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
# R8SS_PRINT_SOME prints some of a R8SS matrix.
#
#  Discussion:
#
#    The R8SS storage format is used for real symmetric skyline matrices.
#    This storage is appropriate when the nonzero entries of the
#    matrix are generally close to the diagonal, but the number
#    of nonzeroes above each diagonal varies in an irregular fashion.
#
#    In this case, the strategy is essentially to assign column J
#    its own bandwidth, and store the strips of nonzeros one after
#    another.   Note that what's important is the location of the
#    furthest nonzero from the diagonal.  A slot will be set up for
#    every entry between that and the diagonal, whether or not
#    those entries are zero.
#
#    A skyline matrix can be Gauss-eliminated without disrupting
#    the storage scheme, as long as no pivoting is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
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
#    integer NA, the dimension of the array A.
#
#    integer DIAG(N), the indices in A of the N diagonal elements.
#
#    real A(NA), the R8SS matrix.
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
  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )

    inc = j2hi + 1 - j2lo

    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )
#
#  Determine the range of the rows in this strip.
#
    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, n - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      for j in range ( j2lo, j2hi + 1 ):

        aij = 0.0

        if ( j < i ):

          if ( i == 0 ):
            ijm1 = 0
          else:
            ijm1 = diag[i-1]

          ij = diag[i]

          if ( ijm1 < ij + j - i ):
            aij = a[ij+j-i]

        elif ( j == i ):
          ij = diag[j]
          aij = a[ij]

        elif ( i < j ):

          if ( j == 0 ):
            ijm1 = 0
          else:
            ijm1 = diag[j-1]

          ij = diag[j]
          if ( ijm1 < ij + i - j ):
            aij = a[ij+i-j]

        print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def r8ss_print_some_test ( ):

#*****************************************************************************80
#
# R8SS_PRINT_SOME_TEST tests R8SS_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 9

  print ( '' )
  print ( 'R8SS_PRINT_SOME_TEST' )
  print ( '  R8SS_PRINT_SOME prints some of an R8SS matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  na, diag, a = r8ss_random ( n )
#
#  Replace the random entries by marker values.
#
  ij = 0
  for j in range ( 0, n ):

    if ( j == 0 ):
      ilo = 0
    else:
      ilo = j + 1 - ( diag[j] - diag[j-1] )

    for i in range ( ilo, j + 1 ):
      a[ij] = float ( 10 * ( i + 1) + j + 1 )
      ij = ij + 1
#
#
#  Print information.
#
  print ( '' )
  print ( '  Number of nonzero entries stored is ', na )

  i4vec_print ( n, diag, '  Diagonal storage indices:' )

  r8ss_print_some ( n, na, diag, a, 1, 0, 7, 4, '  Rows 1-7, Cols 0:4' )

  return

def r8ss_random ( n ):

#*****************************************************************************80
#
# R8SS_RANDOM randomizes a R8SS matrix.
#
#  Discussion:
#
#    The R8SS storage format is used for real symmetric skyline matrices.
#    This storage is appropriate when the nonzero entries of the
#    matrix are generally close to the diagonal, but the number
#    of nonzeroes above each diagonal varies in an irregular fashion.
#
#    In this case, the strategy is essentially to assign column J
#    its own bandwidth, and store the strips of nonzeros one after
#    another.   Note that what's important is the location of the
#    furthest nonzero from the diagonal.  A slot will be set up for
#    every entry between that and the diagonal, whether or not
#    those entries are zero.
#
#    A skyline matrix can be Gauss-eliminated without disrupting
#    the storage scheme, as long as no pivoting is required.
#
#    The user must set aside ( N * ( N + 1 ) ) / 2 entries for the array,
#    although the actual storage needed will generally be about half of
#    that.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
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
#    integer NA, the dimension of the array A.
#    NA will be at least N and no greater than ( N * ( N + 1 ) ) / 2.
#
#    integer DIAG(N), the indices in A of the N diagonal elements.
#
#    real A((N*(N+1))/2), the R8SS matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  diag = np.zeros ( n, dtype = np.int32 )
  a = np.zeros ( ( n * ( n + 1 ) ) // 2 );

  na = 0
#
#  Set the values of DIAG.
#
  diag[0] = 0
  na = 1
#
#  Column J can have between 1 and J+1 entries.
#
  for j in range ( 1, n ):
    k = rng.integers ( low = 1, high = j + 1, endpoint = True )
    diag[j] = diag[j-1] + k
    na = na + k
#
#  Now set the values of A.
#
  diagold = -1
  k = 0

  for j in range ( 0, n ):

    ilo = j + 1 - ( diag[j] - diagold )

    for i in range ( ilo, j + 1 ):
      a[k] = rng.random ( )
      k = k + 1

    diagold = diag[j]

  return na, diag, a

def r8ss_random_test ( ):

#*****************************************************************************80
#
# R8SS_RANDOM_TEST tests R8SS_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8SS_RANDOM_TEST' )
  print ( '  R8SS_RANDOM returns a random R8SS matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  na, diag, a = r8ss_random ( n )

  r8ss_print ( n, na, diag, a, '  The random R8SS matrix:' )

  return

def r8ss_to_r8ge ( n, na, diag, a ):

#*****************************************************************************80
#
# R8SS_TO_R8GE copies a R8SS matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8SS storage format is used for real symmetric skyline matrices.
#    This storage is appropriate when the nonzero entries of the
#    matrix are generally close to the diagonal, but the number
#    of nonzeroes above each diagonal varies in an irregular fashion.
#
#    In this case, the strategy is essentially to assign column J
#    its own bandwidth, and store the strips of nonzeros one after
#    another.   Note that what's important is the location of the
#    furthest nonzero from the diagonal.  A slot will be set up for
#    every entry between that and the diagonal, whether or not
#    those entries are zero.
#
#    A skyline matrix can be Gauss-eliminated without disrupting
#    the storage scheme, as long as no pivoting is required.
#
#  Example:
#
#    11   0  13  0 15
#     0  22  23  0  0
#    31  32  33 34  0
#     0   0  43 44  0
#    51   0   0  0 55
#
#    A = ( 11 | 22 | 13, 23, 33 | 34, 44 | 15, 0, 0, 0, 55 )
#    NA = 12
#    DIAG = ( 1, 2, 5, 7, 12 )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
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
#    integer NA, the dimension of the array A.
#    NA must be at least N.
#
#    integer DIAG(N), the indices in A of the N diagonal elements.
#
#    real A(NA), the R8SS matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  diagold = -1
  k = 0

  for j in range ( 0, n ):

    ilo = j + 1 - ( diag[j] - diagold )

    for i in range ( ilo, j ):
      b[i,j] = a[k]
      b[j,i] = a[k]
      k = k + 1

    b[j,j] = a[k]
    k = k + 1

    diagold = diag[j]

  return b

def r8ss_to_r8ge_test ( ):

#*****************************************************************************80
#
# R8SS_TO_R8GE_TEST tests R8SS_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8SS_TO_R8GE_TEST' )
  print ( '  R8SS_TO_R8GE converts an R8SS matrix to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  na, diag, a = r8ss_random ( n )

  r8ss_print ( n, na, diag, a, '  The R8SS matrix:' )

  a_r8ge = r8ss_to_r8ge ( n, na, diag, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8ss_zeros ( n ):

#*****************************************************************************80
#
# R8SS_ZEROS zeros an R8SS matrix.
#
#  Discussion:
#
#    The R8SS storage format is used for real symmetric skyline matrices.
#    This storage is appropriate when the nonzero entries of the
#    matrix are generally close to the diagonal, but the number
#    of nonzeroes above each diagonal varies in an irregular fashion.
#
#    In this case, the strategy is essentially to assign column J
#    its own bandwidth, and store the strips of nonzeros one after
#    another.   Note that what's important is the location of the
#    furthest nonzero from the diagonal.  A slot will be set up for
#    every entry between that and the diagonal, whether or not
#    those entries are zero.
#
#    A skyline matrix can be Gauss-eliminated without disrupting
#    the storage scheme, as long as no pivoting is required.
#
#    The user must set aside ( N * ( N + 1 ) ) / 2 entries for the array,
#    although the actual storage needed will generally be about half of
#    that.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
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
#    integer NA, the dimension of the array A.
#
#    integer DIAG(N), the indices in A of the N diagonal elements.
#
#    real A((N*(N+1))/2), the R8SS matrix.
#
  import numpy as np

  diag = np.zeros ( n, dtype = np.int32 )
  k = -1
  for i in range ( 0, n ):
    k = k + i + 1
    diag[i] = k

  na = ( n * ( n + 1 ) ) // 2
  a = np.zeros ( na )

  return na, diag, a

def r8ss_zeros_test ( ):

#*****************************************************************************80
#
# R8SS_ZEROS_TEST tests R8SS_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8SS_ZEROS_TEST' )
  print ( '  R8SS_ZEROS zeros an R8SS matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  na, diag, a = r8ss_zeros ( n )

  r8ss_print ( n, na, diag, a, '  The zero R8SS matrix:' )

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
  import numpy as np

  a = np.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
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

def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

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
  r8ss_test ( )
  timestamp ( )
