#! /usr/bin/env python3
#
def cyclic_reduction_test ( ):

#*****************************************************************************80
#
## cyclic_reduction_test() tests cyclic_reduction().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'cyclic_reduction_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test cyclic_reduction().' )

  cyclic_reduction_test01 ( )
  cyclic_reduction_test02 ( )
  cyclic_reduction_test03 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'cyclic_reduction_test():' )
  print ( '  Normal end of execution.' )

  return

def cyclic_reduction_test01 ( ):

#*****************************************************************************80
#
## cyclic_reduction_test01() tests c83_cr_fa(), c83_cr_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  n = 10

  print ( '' )
  print ( 'cyclic_reduction_test01():' )
  print ( '  c83_cr_fa() factors a complex tridiagonal matrix;' )
  print ( '  c83_cr_sl() solves a factored system.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix values.
#
  A = np.zeros ( [ n, 3 ], dtype = complex )

  for i in range ( 1, n ):
    A[i,0] = - 1.0 - i * 1j

  for i in range ( 0, n ):
    A[i,1] = 2.0 + 2.0 * i * 1j

  for i in range ( 0, n - 1 ):
    A[i,2] = - 1.0 - ( i + 2 ) * 1j
#
#  Set the desired solution.
#
  x = np.zeros ( n, dtype = complex )

  for j in range ( 0, n ):
    x[j] = j + 1 + 10 * ( j + 1 ) * 1j
  print ( '  Desired solution x:' )
  pprint.pprint ( x )
#
#  Compute the corresponding right hand side.
#
  b = c83_mv ( n, A, x )
  print ( '  Right hand side b:' )
  pprint.pprint ( b )
#
#  Factor the matrix.
#
  A_cr = c83_cr_fa ( n, A )
#
#  Solve the linear system.
#
  x = c83_cr_sl ( n, A_cr, b )

  print ( '  Solution x:' )
  pprint.pprint ( x )

  return

def cyclic_reduction_test02 ( ):

#*****************************************************************************80
#
## cyclic_reduction_test02() tests r83_cr_fa(), r83_cr_sls().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  m = 3
  n = 5
  nb = 2
  debug = True

  print ( '' )
  print ( 'cyclic_reduction_test02():' )
  print ( '  r83_cr_fa(): factors a real tridiagonal matrix' )
  print ( '  r83_cr_sls() solves 1 or more systems.' )
  print ( '  Matrix order N = ', n )
  print ( '  Demonstrate multiple system solution method.' )
#
#  Set the matrix.
#
  A = np.zeros ( [ 3, n ] );

  for j in range ( 1, n ):
    A[0,j] = -1.0

  for j in range ( 0, n ):
    A[1,j] = 2.0
 
  for j in range ( 0, n - 1 ):
    A[2,j] = -1.0

  print ( '  The matrix A:' )
  pprint.pprint ( A )
#
#  Factor the matrix once.
#
  A_cr = r83_cr_fa ( n, A )
#
#  Solve 2 systems simultaneously.
#
  b = np.zeros ( [ n, nb ] )

  b[n-1,0] = n + 1

  b[0,1] = 1.0
  b[n-1,1] = 1.0
#
#  Solve the two linear systems simultaneously.
#
  x = r83_cr_sls ( n, A_cr, nb, b )

  print ( '  The pair of solutions [x1,x2]' )
  pprint.pprint ( x )

  return

def cyclic_reduction_test03 ( ):

#*****************************************************************************80
#
## cyclic_reduction_test03() tests r83_cr_fa(), r83_cr_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2010
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  n = 10
  debug = False

  print ( '' )
  print ( 'cyclic_reduction_test03():' )
  print ( '  r83_cr_fa() factors a real tridiagonal matrix' )
  print ( '  r83_cr_sl() solves 1 system.' )
  print ( '  Matrix order N = ', n )
  print ( '  The matrix is NOT symmetric.' )
#
#  Set the matrix values.
#
  A = np.zeros ( [ 3, n ] )

  for j in range ( 1, n ):
    A[0,j] = j + 1

  for j in range ( 0, n ):
    A[1,j] = 4 * ( j + 1 )

  for j in range ( 0, n - 1 ):
    A[2,j] = j + 1

  print ( '  The matrix A:' )
  pprint.pprint ( A )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side, b = A * x
#
  b = r83_mv ( n, n, A, x )

  print ( '  The right hand side b:' )
  pprint.pprint ( b )

  x = np.zeros ( n )
#
#  Factor the matrix.
#
  A_cr = r83_cr_fa ( n, A )

  if ( debug ):
    print ( '  The CR factor information:' )
    pprint.pprint ( A_cr )
#
#  Solve the linear system.
#
  x = r83_cr_sl ( n, A_cr, b )

  print ( '  The solution x:' )
  pprint.pprint ( x )

  return

def c83_cr_fa ( n, A ):

#*****************************************************************************80
#
## c83_cr_fa() decomposes a complex tridiagonal matrix using cyclic reduction.
#
#  Discussion:
#
#    The C83 storage format is used for a complex tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:N), the diagonal in
#    entries (2,1:N), and the subdiagonal in (3,1:N-1).  Thus, the
#    original matrix is "collapsed" vertically into the array.
#
#    Once C83_CR_FA has decomposed a matrix A, then C83_CR_SL may be used to solve
#    linear systems A * x = b.
#
#    C83_CR_FA does not employ pivoting.  Hence, the results can be more
#    sensitive to ill-conditioning than standard Gauss elimination.  In
#    particular, C83_CR_FA will fail if any diagonal element of the matrix
#    is zero.  Other matrices may also cause C83_CR_FA to fail.
#
#    C83_CR_FA can be guaranteed to work properly if the matrix is strictly
#    diagonally dominant, that is, if the absolute value of the diagonal
#    element is strictly greater than the sum of the absolute values of
#    the offdiagonal elements, for each equation.
#
#    The algorithm may be illustrated by the following figures:
#
#    The initial matrix is given by:
#
#          D1 U1
#          L1 D2 U2
#             L2 R83 U3
#                L3 D4 U4
#                   L4 D5 U5
#                      L5 D6
#
#    Rows and columns are permuted in an odd/even way to yield:
#
#          D1       U1
#             R83    L2 U3
#                D5    L4 U5
#          L1 U2    D2
#             L3 U4    D4
#                L5       D6
#
#    A block LU decomposition is performed to yield:
#
#          D1      |U1
#             R83   |L2 U3
#                D5|   L4 U5
#          --------+--------
#                  |D2'F3
#                  |F1 D4'F4
#                  |   F2 D6'
#
#    For large systems, this reduction is repeated on the lower right hand
#    tridiagonal subsystem until a completely upper triangular system
#    is obtained.  The system has now been factored into the product of a
#    lower triangular system and an upper triangular one, and the information
#    defining this factorization may be used by C83_CR_SL to solve linear
#    systems.
#
#    Here is how a C83 matrix of order 5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Roger Hockney,
#    A fast direct solution of Poisson's equation using Fourier Analysis,
#    Journal of the ACM,
#    Volume 12, Number 1, pages 95-113, January 1965.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    complex A[N,3], the R83 matrix.
#
#  Output:
#
#    complex A_cr[2*N+1,3), factorization information.
#
  import numpy as np

  if ( n <= 0 ):
    print ( '' )
    print ( 'c83_cr_fa(): Fatal error!' )
    print ( '  Nonpositive N = ', n )
    raise Exception ( 'c83_cr_fa(): Fatal error!' )

  A_cr = np.zeros ( [ 2 * n + 1, 3 ], dtype = complex )

  if ( n == 1 ):
    A_cr[1,1] = 1.0 / A[0,1]
    return A_cr
#
#  Copy the data.
#
  A_cr[1:n,0]   = A[1:n,0]
  A_cr[1:n+1,1] = A[0:n,1]
  A_cr[1:n,2]   = A[0:n-1,2]
 
  il = n
  ipntp = 0

  while ( 1 < il ):

    ipnt = ipntp
    ipntp = ipntp + il
    if ( ( il % 2 ) == 1 ):
      inc = il + 1
    else:
      inc = il

    incr = ( inc // 2 )
    il = ( il // 2 )
    ihaf = ipntp + incr + 1
    ifulp = ipnt + inc + 2

    for ilp in range ( incr, 0, -1 ):

      ifulp = ifulp - 2
      iful = ifulp - 1
      ihaf = ihaf - 1
      A_cr[iful,1]  = 1.0 / A_cr[iful,1]
      A_cr[iful,2]  =   A_cr[iful,2]  * A_cr[iful,1]
      A_cr[ifulp,0] =   A_cr[ifulp,0] * A_cr[ifulp+1,1]
      A_cr[ihaf,1]  =   A_cr[ifulp,1] \
                      - A_cr[iful,0]  * A_cr[iful,2] \
                      - A_cr[ifulp,0] * A_cr[ifulp,2]
      A_cr[ihaf,2]  = - A_cr[ifulp,2] * A_cr[ifulp+1,2]
      A_cr[ihaf,0]  = - A_cr[ifulp,0] * A_cr[ifulp+1,0]
 
  A_cr[ipntp+1,1] = 1.0 / A_cr[ipntp+1,1]

  return A_cr

def c83_cr_sl ( n, A_cr, b ):

#*****************************************************************************80
#
## c83_cr_sl() solves a complex linear system factored by C83_CR_FA.
#
#  Discussion:
#
#    The matrix A must be tridiagonal.  C83_CR_FA is called to compute the
#    LU factors of A.  It does so using a form of cyclic reduction.  If
#    the factors computed by C83_CR_FA are passed to C83_CR_SL, then one or many
#    linear systems involving the matrix A may be solved.
#
#    Note that C83_CR_FA does not perform pivoting, and so the solution 
#    produced by C83_CR_SL may be less accurate than a solution produced 
#    by a standard Gauss algorithm.  However, such problems can be 
#    guaranteed not to occur if the matrix A is strictly diagonally 
#    dominant, that is, if the absolute value of the diagonal coefficient 
#    is greater than the sum of the absolute values of the two off diagonal 
#    coefficients, for each row of the matrix.
#
#    Here is how a C83 matrix of order 5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2026
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Roger Hockney,
#    A fast direct solution of Poisson's equation using Fourier Analysis,
#    Journal of the ACM,
#    Volume 12, Number 1, pages 95-113, January 1965.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    complex A_CR(2*N+1,3), factorization information computed by C83_CR_FA.
#
#    complex B(N), the right hand side vector.
#
#  Output:
#
#    complex X(N), the solution of the linear system.
#
  import numpy as np

  if ( n <= 0 ):
    print ( '' )
    print ( 'c83_cr_sl(): Fatal error!' )
    print ( '  Nonpositive N =', n )
    raise Exception ( 'c83_cr_sl(): Fatal error!' )

  x = np.zeros ( n, dtype = complex )

  if ( n == 1 ):
    x[0] = A_cr[1,1] * b[0]
    return x
#
#  Set up RHS.
#
  rhs = np.zeros ( 2 * n + 1, dtype = complex )

  rhs[1:n+1] = b[0:n]

  il = n
  ndiv = 1
  ipntp = 0

  while ( 1 < il ):

    ipnt = ipntp
    ipntp = ipntp + il
    il = ( il // 2 )
    ndiv = ndiv * 2
    ihaf = ipntp

    for iful in range ( ipnt + 2, ipntp + 1, 2 ):

      ihaf = ihaf + 1
      rhs[ihaf] = rhs[iful] \
        - A_cr[iful-1,2] * rhs[iful-1] \
        - A_cr[iful,0] * rhs[iful+1]

  rhs[ihaf] = rhs[ihaf] * A_cr[ihaf,1]
  ipnt = ipntp

  while ( 0 < ipnt ):

    ipntp = ipnt
    ndiv = ( ndiv // 2 )
    il = ( n // ndiv )
    ipnt = ipnt - il
    ihaf = ipntp

    for ifulm in range ( ipnt + 1, ipntp + 1, 2 ):

      iful = ifulm + 1
      ihaf = ihaf + 1
      rhs[iful] = rhs[ihaf]
      rhs[ifulm] = \
          A_cr[ifulm,1] * ( rhs[ifulm] \
        - A_cr[ifulm-1,2] * rhs[ifulm-1] \
        - A_cr[ifulm,0] * rhs[iful] )

  x[0:n] = rhs[1:n+1]

  return x

def c83_mv ( n, A, x ):

#*****************************************************************************80
#
## c83_mv() multiplies a C83 matrix times a vector.
#
#  Discussion:
#
#    Here is how a C83 matrix of order 5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the linear system.
#
#    complex A(3,N), the C83 matrix.
#
#    complex X(N), the vector to be multiplied by A.
#
#  Output:
#
#    complex B(N), the product A * x.
#
  import numpy as np

  b = np.zeros ( n, dtype = complex );

  b[0:n]   =            A[0:n,1]   * x[0:n]
  b[0:n-1] = b[0:n-1] + A[1:n,0]   * x[1:n]
  b[1:n]   = b[1:n]   + A[0:n-1,2] * x[0:n-1]

  return b

def c8vec_indicator ( n ):

#*****************************************************************************80
#
## c8vec_indicator() sets a C8VEC to the indicator vector.
#
#  Discussion:
#
#    X(1:N) = ( 1-1i, 2-2i, 3-3i, 4-4i, ... )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements.
#
#  Output:
#
#    complex A(N), the array.
#
  import numpy as np

  a = np.zeros ( n, 'complex' )

  for i in range ( 0, n ):
    a[i] = float ( i + 1 ) - float ( i + 1 ) * 1j

  return a

def r83_cr_fa ( n, A ):

#*****************************************************************************80
#
## r83_cr_fa() decomposes an R83 matrix using cyclic reduction.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#    Once r83_CR_FA has decomposed a matrix A, then r83_CR_SL may be used to
#    solve linear systems A * x = b.
#
#    r83_CR_FA does not employ pivoting.  Hence, the results can be more
#    sensitive to ill-conditioning than standard Gauss elimination.  In
#    particular, r83_CR_FA will fail if any diagonal element of the matrix
#    is zero.  Other matrices may also cause r83_CR_FA to fail.
#
#    r83_CR_FA can be guaranteed to work properly if the matrix is strictly
#    diagonally dominant, that is, if the absolute value of the diagonal
#    element is strictly greater than the sum of the absolute values of
#    the offdiagonal elements, for each equation.
#
#    The algorithm may be illustrated by the following figures:
#
#    The initial matrix is given by:
#
#          D1 U1
#          L1 D2 U2
#             L2 R83 U3
#                L3 D4 U4
#                   L4 D5 U5
#                      L5 D6
#
#    Rows and columns are permuted in an odd/even way to yield:
#
#          D1       U1
#             R83    L2 U3
#                D5    L4 U5
#          L1 U2    D2
#             L3 U4    D4
#                L5       D6
#
#    A block LU decomposition is performed to yield:
#
#          D1      |U1
#             R83   |L2 U3
#                D5|   L4 U5
#          --------+--------
#                  |D2'F3
#                  |F1 D4'F4
#                  |   F2 D6' )
#
#    For large systems, this reduction is repeated on the lower right hand
#    tridiagonal subsystem until a completely upper triangular system
#    is obtained.  The system has now been factored into the product of a
#    lower triangular system and an upper triangular one, and the information
#    defining this factorization may be used by r83_CR_SL to solve linear
#    systems.
#
#    Here is how an R83 matrix of order 5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Roger Hockney,
#    A fast direct solution of Poisson's equation using Fourier Analysis,
#    Journal of the ACM,
#    Volume 12, Number 1, pages 95-113, January 1965.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A(3,N), the R83 matrix.
#
#  Output:
#
#    real A_CR(3,2*N+1), factorization information.
#
  import numpy as np

  A_cr = np.zeros ( [ 3, 2 * n + 1 ] )

  if ( n == 1 ):
    A_cr[1,0] = 1.0 / A[1,0]
    return a_cr
#
#  Zero out the workspace entries.
#
  for j in range ( 1, n ):
    A_cr[0,j] = A[0,j]
  for j in range ( 1, n + 1 ):
    A_cr[1,j] = A[1,j-1]
  for j in range ( 1, n ):
    A_cr[2,j] = A[2,j-1]

  il = n
  ipntp = 0

  while ( 1 < il ):

    ipnt = ipntp
    ipntp = ipntp + il
    if ( ( il % 2 ) == 1 ):
      inc = il + 1
    else:
      inc = il

    incr = ( inc // 2 )
    il = ( il // 2 )
    ihaf = ipntp + incr + 1
    ifulp = ipnt + inc + 2

    for ilp in range ( incr, 0, -1 ):
      ifulp = ifulp - 2
      iful = ifulp - 1
      ihaf = ihaf - 1
      A_cr[1,iful] = 1.0 / A_cr[1,iful]
      A_cr[2,iful]  =  A_cr[2,iful]  * A_cr[1,iful]
      A_cr[0,ifulp] =  A_cr[0,ifulp] * A_cr[1,ifulp+1]
      A_cr[1,ihaf] =   A_cr[1,ifulp] - A_cr[0,iful]  * A_cr[2,iful] \
                     - A_cr[0,ifulp] * A_cr[2,ifulp]
      A_cr[2,ihaf] = - A_cr[2,ifulp] * A_cr[2,ifulp+1]
      A_cr[0,ihaf] = - A_cr[0,ifulp] * A_cr[0,ifulp+1]

  A_cr[1,ipntp+1] = 1.0 / A_cr[1,ipntp+1]

  return A_cr

def r83_cr_sl ( n, A_cr, b ):

#*****************************************************************************80
#
## r83_cr_sl() solves a real linear system factored by r83_CR_FA.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)). 
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#    The matrix A must be tridiagonal.  r83_CR_FA is called to compute the
#    LU factors of A.  It does so using a form of cyclic reduction.  If
#    the factors computed by r83_CR_FA are passed to r83_CR_SL, then one or many
#    linear systems involving the matrix A may be solved.
#
#    Note that r83_CR_FA does not perform pivoting, and so the solution 
#    produced by r83_CR_SL may be less accurate than a solution produced 
#    by a standard Gauss algorithm.  However, such problems can be 
#    guaranteed not to occur if the matrix A is strictly diagonally 
#    dominant, that is, if the absolute value of the diagonal coefficient 
#    is greater than the sum of the absolute values of the two off diagonal 
#    coefficients, for each row of the matrix.
#
#    Here is how an R83 matrix of order 5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 March 2004
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Roger Hockney,
#    A fast direct solution of Poisson's equation using Fourier Analysis,
#    Journal of the ACM,
#    Volume 12, Number 1, pages 95-113, January 1965.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A_CR(3,2*N+1), factorization information computed by r83_CR_FA.
#
#    real B(N), the right hand side vector.
#
#  Output:
#
#    real X(N), the solution of the linear system.
#
  import numpy as np

  if ( n <= 0 ):
    print ( '' )
    print ( 'r83_cr_sl(): Fatal error!' )
    print ( '  Nonpositive N = ', n )
    raise Exception ( 'r83_cr_sl(): Fatal error!' )

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = A_cr[1,1] * b[0]
    return x
#
#  Set up RHS.
#
  rhs = np.zeros ( 2 * n + 1 )

  for i in range ( 1, n + 1 ):
    rhs[i] = b[i-1]

  il = n
  ndiv = 1
  ipntp = 0

  while ( 1 < il ):

    ipnt = ipntp
    ipntp = ipntp + il
    il = ( il // 2 )
    ndiv = ndiv * 2
    ihaf = ipntp

    for iful in range ( ipnt + 2, ipntp + 1, 2 ):
      ihaf = ihaf + 1
      rhs[ihaf] = rhs[iful] \
        - A_cr[2,iful-1] * rhs[iful-1] \
        - A_cr[0,iful]   * rhs[iful+1]

  rhs[ihaf] = rhs[ihaf] * A_cr[1,ihaf]

  ipnt = ipntp

  while ( 0 < ipnt ):

    ipntp = ipnt
    ndiv = ( ndiv // 2 )
    il = ( n // ndiv )
    ipnt = ipnt - il
    ihaf = ipntp

    for ifulm in range ( ipnt + 1, ipntp + 1, 2 ):
      iful = ifulm + 1
      ihaf = ihaf + 1
      rhs[iful] = rhs[ihaf]
      rhs[ifulm] = A_cr[1,ifulm] * ( rhs[ifulm] \
        - A_cr[2,ifulm-1] * rhs[ifulm-1] \
        - A_cr[0,ifulm]   * rhs[iful] )

    for i in range ( 0, n ):
      x[i] = rhs[i+1]

  return x

def r83_cr_sls ( n, A_cr, nb, b ):

#*****************************************************************************80
#
## r83_cr_sls() solves several real linear systems factored by r83_CR_FA.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)). 
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#    The matrix A must be tridiagonal.  r83_CR_FA is called to compute the
#    LU factors of A.  It does so using a form of cyclic reduction.  If
#    the factors computed by r83_CR_FA are passed to r83_cr_sls, then one or
#    many linear systems involving the matrix A may be solved.
#
#    Note that r83_CR_FA does not perform pivoting, and so the solution 
#    produced by r83_cr_sls may be less accurate than a solution produced 
#    by a standard Gauss algorithm.  However, such problems can be 
#    guaranteed not to occur if the matrix A is strictly diagonally 
#    dominant, that is, if the absolute value of the diagonal coefficient 
#    is greater than the sum of the absolute values of the two off diagonal 
#    coefficients, for each row of the matrix.
#
#    Here is how an R83 matrix of order 5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Roger Hockney,
#    A fast direct solution of Poisson's equation using Fourier Analysis,
#    Journal of the ACM,
#    Volume 12, Number 1, pages 95-113, January 1965.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A_CR(3,2*N+1), factorization information computed by r83_CR_FA.
#
#    integer NB, the number of right hand sides.
#
#    real B(N,NB), the right hand side vectors.
#
#  Output:
#
#    real X(N,NB), the solutions of the linear system.
#
  import numpy as np

  if ( n <= 0 ):
    print ( '' )
    print ( 'r83_cr_sls(): Fatal error!' )
    print ( '  Nonpositive N =', n )
    raise Exception ( 'r83_cr_sls(): Fatal error!' )

  x = np.zeros ( [ n, nb ] )

  if ( n == 1 ):
    for j in range ( 0, nb ):
      x[0,j] = A_cr[1,0] * b[0,j]
    return x
#
#  Set up RHS.
#
  rhs = np.zeros ( [ 2 * n + 1, nb ] )
  for j in range ( 0, nb ):
    for i in range ( 1, n + 1 ):
      rhs[i,j] = b[i-1,j]

  il = n
  ndiv = 1
  ipntp = 0

  while ( 1 < il ):

    ipnt = ipntp
    ipntp = ipntp + il
    il = ( il // 2 )
    ndiv = ndiv * 2
    ihaf = ipntp

    for iful in range ( ipnt + 2, ipntp + 1, 2 ):
      ihaf = ihaf + 1
      for j in range ( 1, nb ):
        rhs[ihaf,j] = rhs[iful,j] \
          - A_cr[2,iful-1] * rhs[iful-1,j] \
          - A_cr[0,iful]   * rhs[iful+1,j]

  for j in range ( 0, nb ):
    rhs[ihaf,j] = rhs[ihaf,j] * A_cr[1,ihaf]

  ipnt = ipntp

  while ( 0 < ipnt ):

    ipntp = ipnt
    ndiv = ( ndiv // 2 )
    il = ( n // ndiv )
    ipnt = ipnt - il
    ihaf = ipntp

    for ifulm in range ( ipnt + 1, ipntp + 1, 2 ):
      iful = ifulm + 1
      ihaf = ihaf + 1
      for j in range ( 0, nb ):
        rhs[iful,j] = rhs[ihaf,j]
        rhs[ifulm,j] = A_cr[1,ifulm]   * ( rhs[ifulm,j] \
                     - A_cr[2,ifulm-1] *   rhs[ifulm-1,j] \
                     - A_cr[0,ifulm]   *   rhs[iful,j] )

  for j in range ( 0, nb ):
    for i in range ( 0, n ):
      x[i,j] = rhs[i+1,j]

  return x

def r83_gs_sl ( n, A, b, x, it_max ):

#*****************************************************************************80
#
## r83_gs_sl() solves an R83 system using Gauss-Seidel iteration.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)). 
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#    This routine simply applies a given number of steps of the
#    iteration to an input approximate solution.  On first call, you can
#    simply pass in the zero vector as an approximate solution.  If
#    the returned value is not acceptable, you may call again, using
#    it as the starting point for additional iterations.
#
#    Here is how an R83 matrix of order 5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(3,N), the R83 matrix.
#
#    real B(N), the right hand side of the linear system.
#
#    real X(N), an approximate solution to the system.
#
#    integer IT_MAX, the maximum number of iterations.
#
#  Output:
#
#    real X_NEW(N), an approximate solution to the system.
#

#
#  No diagonal matrix entry can be zero.
#
  for i in range ( 0, n ):
    if ( a[1,i] == 0.0 ):
      print ( '' )
      print ( 'r83_gs_sl(): Fatal error!' )
      print ( '  Zero diagonal entry, index = ', i )
      raise Exception ( 'r83_gs_sl(): Fatal error!' )

  for it_num in range ( 0, it_max ):

    x[0] = ( b[0] - A[0,1] * x[1]   ) / A[1,0]

    for i in range ( 1, n - 1 ):
      x[i] = ( b[i] - A[2,i-1] * x[i-1] - A[0,i+1] * x[i+1] ) / A[1,i]

    x[n-1] = ( b[n-1] - A[2,n-2] * x[n-2] ) / A[1,n-1]

  return x

def r83_mv ( m, n, A, x ):

#*****************************************************************************80
#
## r83_mv() multiplies a R83 matrix times a vector.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#    Here is how an R83 matrix of order 5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the linear system.
#
#    real A(3,N), the R83 matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for j in range ( 0, n ):
    for i in range ( max ( 0, j - 1 ), min ( m, j + 2 ) ):
      b[i] = b[i] + A[i-j+1,j] * x[j]

  return b

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## r8vec_indicator1() sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    Here is how an R83 matrix of order 5 would be stored:
#
#       *  A11 A12
#      A21 A22 A23
#      A32 A33 A34
#      A43 A44 A45
#      A54 A55  *
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
  cyclic_reduction_test ( )
  timestamp ( )

