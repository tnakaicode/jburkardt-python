#! /usr/bin/env python3
#
def r8vm_test ( ):

#*****************************************************************************80
#
## r8vm_test() tests r8vm().
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
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vm_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8vm().' )

  rng = default_rng ( )

  r8ge_to_r8vm_test ( rng )

  r8vm_det_test ( )
  r8vm_indicator_test ( )
  r8vm_mtv_test ( rng )
  r8vm_mv_test ( rng )
  r8vm_print_test ( )
  r8vm_print_some_test ( )
  r8vm_random_test ( rng )
  r8vm_sl_test ( rng )
  r8vm_slt_test ( rng )
  r8vm_to_r8ge_test ( rng )
  r8vm_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vm_test():' )
  print ( '  Normal end of execution.' )
  return

def r8ge_to_r8vm ( m, n, a_ge ):

#*****************************************************************************80
#
## r8ge_to_r8vm() copies an R8GE matrix to an R8VM matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A_GE(M,N), the R8GE matrix.
#
#  Output:
#
#    real A_VM(N), the R8VM matrix.
#
  import numpy as np

  a_vm = np.zeros ( n )

  for j in range ( 0, n ):
    a_vm[j] = a_ge[1,j]

  return a_vm

def r8ge_to_r8vm_test ( rng ):

#*****************************************************************************80
#
## r8ge_to_r8vm_test() tests r8ge_to_r8vm().
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
#  Input:
#
#    rng: the current random number generator.
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_to_r8vm_test():' )
  print ( '  r8ge_to_r8vm() converts an R8GE matrix to R8VM format.' )

  a_ge = rng.random ( size = [ m, n] )

  print ( '' )
  print ( '  The random R8GE matrix:' )
  print ( a_ge )

  a_vm = r8ge_to_r8vm ( m, n, a_ge )

  r8vm_print ( m, n, a_vm, '  The R8VM matrix:' )

  return

def r8vm_det ( n, a ):

#*****************************************************************************80
#
## r8vm_det() computes the determinant of a R8VM matrix.
#
#  Discussion:
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix.
#
#    real A(N), the R8VM matrix.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  det = 1.0
  for j in range ( 0, n ):
    for i in range ( j + 1, n ):
      det = det * ( a[i] - a[j] )

  return det

def r8vm_det_test ( ):

#*****************************************************************************80
#
## r8vm_det_test tests r8vm_det.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8vm_det_test' )
  print ( '  r8vm_det computes the determinant of an R8VM matrix.' )
#
#  Set the matrix.
#
  n = 5
  a_vm = r8vm_indicator ( n, n )

  r8vm_print ( n, n, a_vm, '  The R8VM matrix:' )
#
#  Compute the determinant.
#
  det1 = r8vm_det ( n, a_vm )

  print ( '' )
  print ( '  R8VM_DET = ', det1 )

  det2 = r8vm_indicator_det ( n )

  print ( '  Exact    = ', det2 )

  return

def r8vm_indicator ( m, n ):

#*****************************************************************************80
#
## r8vm_indicator returns an R8VM indicator matrix.
#
#  Discussion:
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real A(N), the matrix.
#
  import numpy as np

  a = np.zeros ( n )
 
  for j in range ( 0, n ):
    a[j] = float ( j + 1 )

  return a

def r8vm_indicator_det ( n ):

#*****************************************************************************80
#
## r8vm_indicator_det returns the determinant of an R8VM indicator matrix.
#
#  Discussion:
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix.
#
#  Output:
#
#    real DET, the determinant.
#
  from math import factorial

  det = 1.0
  for i in range ( 0, n ):
    det = det * factorial ( i )

  return det

def r8vm_indicator_test ( ):

#*****************************************************************************80
#
## r8vm_indicator_test tests r8vm_indicator.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8vm_indicator_test' )
  print ( '  r8vm_indicator returns an R8VM indicator matrix.' )

  a = r8vm_indicator ( m, n )

  r8vm_print ( m, n, a, '  Matrix A:' )

  return

def r8vm_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## r8vm_mtv multiplies a vector by a R8VM matrix.
#
#  Discussion:
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(N,1), the R8VM matrix.
#
#    real X(M), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( i == 0 ):
        b[j] = b[j] + x[i]
      else:
        b[j] = b[j] + ( a[j] ** i ) * x[i]

  return b

def r8vm_mtv_test ( rng ):

#*****************************************************************************80
#
## r8vm_mtv_test() tests r8vm_mtv().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 5

  print ( '' )
  print ( 'r8vm_mtv_test()' )
  print ( '  r8vm_mtv)_ computes b=A\'*x, where A is an R8VM matrix.' )
#
#  Set A.
#
  a = r8vm_random ( n, n, rng )
#
#  Set X.
#
  x = r8vec_indicator1 ( n )
#
#  Compute b=A'*x.
#
  b = r8vm_mtv ( n, n, a, x )

  r8vec_print ( n, b, '  b=A\'*x' )
 
  return

def r8vm_mv ( m, n, a, x ):

#*****************************************************************************80
#
## r8vm_mv multiplies a R8VM matrix times a vector.
#
#  Discussion:
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 November 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(N,1), the R8VM matrix.
#
#    real X(N,1), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M,1), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i == 0 ):
        b[i] = b[i] + x[j]
      else:
        b[i] = b[i] + ( a[j] ** i ) * x[j]

  return b

def r8vm_mv_test ( rng ):

#*****************************************************************************80
#
## r8vm_mv_test() tests r8vm_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 5

  print ( '' )
  print ( 'r8vm_mv_test()' )
  print ( '  r8vm_mv() computes b=A*x, where A is an R8VM matrix.' )
#
#  Set A.
#
  a = r8vm_random ( n, n, rng )
#
#  Set X.
#
  x = r8vec_indicator1 ( n )
#
#  Compute b=A*x.
#
  b = r8vm_mv ( n, n, a, x )

  r8vec_print ( n, b, '  b=A*x' )
 
  return

def r8vm_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8vm_print prints a R8VM matrix.
#
#  Discussion:
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(N), the R8VM matrix.
#
#    string TITLE, a title to be printed.
#
  r8vm_print_some ( m, n, a, 1, 1, n, n, title )

  return

def r8vm_print_test ( ):

#*****************************************************************************80
#
## r8vm_print_test tests r8vm_print.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8vm_print_test' )
  print ( '  r8vm_print prints an R8VM matrix.' )

  a = r8vm_indicator ( m, n )

  r8vm_print ( m, n, a, '  The R8VM matrix:' )
 
  return

def r8vm_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8vm_print_some prints some of a R8VM matrix.
#
#  Discussion:
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(N), the R8VM matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )

  incx = 5
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( jlo, jhi + 1, incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )

    inc = j2hi + 1 - j2lo

    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )
    print ( '' )
    print ( '  Row' )
    print ( '  ---' )
#
#  Determine the range of the rows in this strip.
#
    i2lo = max ( ilo, 1 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%4d  ' % ( i ), end = '' )
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      for j2 in range ( 1, inc + 1 ):

        j = j2lo - 1 + j2

        if ( i == 1 ):
          aij = 1.0
        else:
          aij = a[j-1] ** ( i - 1 )

        print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def r8vm_print_some_test ( ):

#*****************************************************************************80
#
## r8vm_print_some_test tests r8vm_print_some.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8vm_print_some_test' )
  print ( '  r8vm_print_some prints some of an R8VM format.' )

  a = r8vm_indicator ( m, n )

  r8vm_print_some ( m, n, a, 2, 2, 5, 4, '  Rows 2-5, Cols 2:4' )
 
  return

def r8vm_random ( m, n, rng ):

#*****************************************************************************80
#
## r8vm_random() randomizes an R8VM matrix.
#
#  Discussion:
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Inpu:
#
#    integer M, N, the order of the matrix.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(N), the matrix.
#
  a = rng.random ( size = n )

  return a

def r8vm_random_test ( rng ):

#*****************************************************************************80
#
## r8vm_random_test() tests r8vm_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8vm_random_test():' )
  print ( '  r8vm_random() randomizes an R8VM matrix.' )

  a = r8vm_random ( m, n, rng )

  r8vm_print ( m, n, a, '  Matrix A:' )

  return

def r8vm_sl ( n, a, b ):

#*****************************************************************************80
#
## r8vm_sl() solves A*x=b, where A is an R8VM matrix.
#
#  Discussion:
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#    Vandermonde systems are very close to singularity.  The singularity
#    gets worse as N increases, and as any pair of values defining
#    the matrix get close.  Even a system as small as N = 10 will
#    involve the 9th power of the defining values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations,
#    Third Edition,
#    Johns Hopkins, 1996.
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix.
#
#    real A(N), the R8VM matrix.
#
#    real B(N), the right hand side.
#
#  Output:
#
#    real X(N), the solution of the linear system.
#
#    integer INFO.
#    0, no error.
#    nonzero, at least two of the values in A are equal.
#
  import numpy as np

  x = np.zeros ( n )
#
#  Check for explicit singularity.
#
  info = 0

  for j in range ( 0, n - 1 ):
    for i in range ( j + 1, n ):
      if ( a[i] == a[j] ):
        info = 1
        return x, info

  for i in range ( 0, n ):
    x[i] = b[i]

  for j in range ( 1, n ):
    for i in range ( n, j, -1 ):
      x[i-1] = x[i-1] - a[j-1] * x[i-2]

  for j in range ( n - 1, 0, -1 ):

    for i in range ( j + 1, n + 1 ):
      x[i-1] = x[i-1] / ( a[i-1] - a[i-j-1] )

    for i in range ( j, n ):
      x[i-1] = x[i-1] - x[i]

  return x, info

def r8vm_sl_test ( rng ):

#*****************************************************************************80
#
## r8vm_sl_test() tests r8vm_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vm_sl_test()' )
  print ( '  r8vm_sl() solves A*x=b, where A is an R8VM matrix.' )
#
#  Set the matrix.
#
  n = 5
  a = r8vm_random ( n, n, rng )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8vm_mv ( n, n, a, x )
#
#  Solve the linear system.
#
  x, info = r8vm_sl ( n, a, b )

  r8vec_print ( n, x, '  Solution:' )
 
  return

def r8vm_slt ( n, a, b ):

#*****************************************************************************80
#
## R8VM_SLT solves A'*x=b, where A is an R8VM matrix.
#
#  Discussion:
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#    Vandermonde systems are very close to singularity.  The singularity
#    gets worse as N increases, and as any pair of values defining
#    the matrix get close.  Even a system as small as N = 10 will
#    involve the 9th power of the defining values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations,
#    Third Edition,
#    Johns Hopkins, 1996.
#
#  Input:
#
#    integer N, the number of rows and columns of the matrix.
#
#    real A(N,1), the R8VM matrix.
#
#    real B(N,1), the right hand side.
#
#  Output:
#
#    real X(N,1), the solution of the linear system.
#
#    integer INFO.
#    0, no error.
#    nonzero, at least two of the values in A are equal.
#
  import numpy as np

  x = np.zeros ( n )
#
#  Check for explicit singularity.
#
  info = 0

  for j in range ( 0, n - 1 ):
    for i in range ( j + 1, n ):
      if ( a[i] == a[j] ):
        info = 1
        return x, info

  for i in range ( 0, n ):
    x[i] = b[i]

  for j in range ( 1, n ):
    for i in range ( n, j, -1 ):
      x[i-1] = ( x[i-1] - x[i-2] ) / ( a[i-1] - a[i-j-1] )

  for j in range ( n - 1, 0, -1 ):
    for i in range ( j, n ):
      x[i-1] = x[i-1] - x[i] * a[j-1]

  return x, info

def r8vm_slt_test ( rng ):

#*****************************************************************************80
#
## r8vm_slt_test() tests r8vm_slt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r8vm_slt_test()' )
  print ( '  r8vm_slt() solves a transposed Vandermonde system.' )
#
#  Set the matrix.
#
  n = 5
  a = r8vm_random ( n, n, rng )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8vm_mtv ( n, n, a, x )
#
#  Solve the linear system.
#
  x, info = r8vm_slt ( n, a, b )

  r8vec_print ( n, x, '  Solution to transposed system:' );

  return

def r8vm_to_r8ge ( m, n, a_vm ):

#*****************************************************************************80
#
## R8VM_TO_R8GE copies a R8VM matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A_VM(N,1), the R8VM matrix.
#
#  Output:
#
#    real A_GE(M,N), the R8GE matrix.
#
  import numpy as np

  a_ge = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i == 0 ):
        a_ge[i,j] = 1.0;
      else:
        a_ge[i,j] = a_ge[i-1,j] * a_vm[j]

  return a_ge

def r8vm_to_r8ge_test ( rng ):

#*****************************************************************************80
#
## r8vm_to_r8ge_test() tests r8vm_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8vm_to_r8ge_test()' )
  print ( '  r8vm_to_r8ge() converts an R8VM matrix to R8GE format.' )

  a_vm = r8vm_random ( m, n, rng )

  r8vm_print ( m, n, a_vm, '  The random R8VM matrix:' )

  a_ge = r8vm_to_r8ge ( m, n, a_vm )

  print ( '' )
  print ( '  The R8GE matrix' )
  print ( a_ge )

  return

def r8vm_zeros ( m, n ):

#*****************************************************************************80
#
## r8vm_zeros() zeros an R8VM matrix.
#
#  Discussion:
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real A(N), the zeroed out matrix.
#
  import numpy as np

  a = np.zeros ( n )

  return a

def r8vm_zeros_test ( ):

#*****************************************************************************80
#
## r8vm_zeros_test() tests r8vm_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8vm_zeros_test():' )
  print ( '  r8vm_zeros() zeros out an R8VM matrix.' )

  a = r8vm_zeros ( m, n )

  r8vm_print ( m, n, a, '  Matrix A:' )

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
  r8vm_test ( )
  timestamp ( )
 
