#! /usr/bin/env python3
#
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
  from math import floor

  i = floor ( i )

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
  import platform

  n = 13

  x = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ]

  print ( '' )
  print ( 'i4_log_10_test():' )
  print ( '  i4_log_10(): whole part of log base 10,' )
  print ( '' )
  print ( '  X, i4_log_10' )
  print ( '' )

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print ( '%6d  %12d' % ( x[i], j ) )

  return

def r83_cg ( n, a, b, x_init ):

#*****************************************************************************80
#
## r83_cg() uses the conjugate gradient method on an R83 system.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#    The matrix A must be a positive definite symmetric band matrix.
#
#    The method is designed to reach the solution after N computational
#    steps.  However, roundoff may introduce unacceptably large errors for
#    some problems.  In such a case, calling the routine again, using
#    the computed solution as the new starting estimate, should improve
#    the results.
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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
#    John Burkardt
#
#  Reference:
#
#    Frank Beckman,
#    The Solution of Linear Equations by the Conjugate Gradient Method,
#    in Mathematical Methods for Digital Computers,
#    edited by John Ralston, Herbert Wilf,
#    Wiley, 1967,
#    ISBN: 0471706892,
#    LC: QA76.5.R3.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A(3,N), the matrix.
#
#    real B(N), the right hand side vector.
#
#    real X_INIT(N), an estimate for the solution, which may be 0.
#
#  Output:
#
#    real X(N), the approximate solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = x_init[i]
#
#  Initialize
#    AP = A * x,
#    R  = b - A * x,
#    P  = b - A * x.
#
  ap = r83_mv ( n, n, a, x )

  r = np.zeros ( n )
  for i in range ( 0, n ):
    r[i] = b[i] - ap[i]

  p = np.zeros ( n )
  for i in range ( 0, n ):
    p[i] = b[i] - ap[i]
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP=A*P.
#
    ap = r83_mv ( n, n, a, p )
#
#  Compute the dot products
#    PAP = P*AP,
#    PR  = P*R
#  Set
#    ALPHA = PR / PAP.
#
    pap = np.dot ( p, ap )
    pr = np.dot ( p, r )

    if ( pap == 0.0 ):
      return x

    alpha = pr / pap
#
#  Set
#    X = X + ALPHA * P
#    R = R - ALPHA * AP.
#
    for i in range ( 0, n ):
      x[i] = x[i] + alpha * p[i]

    for i in range ( 0, n):
      r[i] = r[i] - alpha * ap[i]
#
#  Compute the vector dot product
#    RAP = R*AP
#  Set
#    BETA = - RAP / PAP.
#
    rap = np.dot ( r, ap )

    beta = - rap / pap
#
#  Update the perturbation vector
#    P = R + BETA * P.
#
    for i in range ( 0, n ):
      p[i] = r[i] + beta * p[i]

  return x

def r83_cg_test ( rng ):

#*****************************************************************************80
#
## r83_cg_test() tests r83_cg().
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
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r83_cg_test():' )
  print ( '  r83_cg() applies CG to an R83 matrix.' )
#
#  Set A to the second difference matrix.
#
  n = 10

  a = r83_dif2 ( n, n )
#
#  Choose a random solution.
#
  x1 = rng.random ( size = n )
#
#  Compute the corresponding right hand side.
#
  b = r83_mv ( n, n, a, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x3 = r83_cg ( n, a, b, x2 )
#
#  Compute the residual.
#
  r = r83_res ( n, n, a, x3, b )
  r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
  e_norm = np.linalg.norm ( x1 - x3 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = %d' % ( n ) )
  print ( '  Norm of residual ||Ax-b|| = %g' % ( r_norm ) )
  print ( '  Norm of error ||x1-x2|| = %g' % ( e_norm ) )

  return

def r83_cr_fa ( n, a ):

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
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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

  a_cr = np.zeros ( [ 3, 2 * n + 1 ] )

  if ( n == 1 ):
    a_cr[1,0] = 1.0 / a[1,0]
    return a_cr
#
#  Zero out the workspace entries.
#
  for j in range ( 1, n ):
    a_cr[0,j] = a[0,j]
  for j in range ( 1, n + 1 ):
    a_cr[1,j] = a[1,j-1]
  for j in range ( 1, n ):
    a_cr[2,j] = a[2,j-1]

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
      a_cr[1,iful] = 1.0 / a_cr[1,iful]
      a_cr[2,iful]  = a_cr[2,iful]  * a_cr[1,iful]
      a_cr[0,ifulp] = a_cr[0,ifulp] * a_cr[1,ifulp+1]
      a_cr[1,ihaf] = a_cr[1,ifulp] - a_cr[0,iful]  * a_cr[2,iful] \
                    - a_cr[0,ifulp] * a_cr[2,ifulp]
      a_cr[2,ihaf] = - a_cr[2,ifulp] * a_cr[2,ifulp+1]
      a_cr[0,ihaf] = - a_cr[0,ifulp] * a_cr[0,ifulp+1]

  a_cr[1,ipntp+1] = 1.0 / a_cr[1,ipntp+1]

  return a_cr

def r83_cr_fa_test ( ):

#*****************************************************************************80
#
## r83_cr_fa_test() tests r83_cr_fa().
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
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r83_cr_fa_test():' )
  print ( '  r83_cr_fa() factors a real tridiagonal matrix;' )
  print ( '  Once the matrix has been factored, we can call' )
  print ( '  r83_CR_SL to solve a linear system.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
  print ( '  Demonstrate multiple system solution method.' )
  print ( '' )
#
#  Set the matrix values.
#
  a = r83_dif2 ( n, n )
#
#  Print the matrix.
#
  r83_print ( n, n, a, '  System matrix A:' )
#
#  Factor the matrix once.
#
  a_cr = r83_cr_fa ( n, a )

  for j in range ( 1, 3 ): 

    print ( '' )
    print ( '  Solve linear system number %d' % ( j ) )

    b = np.zeros ( n )

    if ( j == 1 ):
      b[n-1] = float ( n + 1 )
    else:
      b[0] = 1.0
      b[n-1] = 1.0
#
#  Solve the linear system.
#
    x = r83_cr_sl ( n, a_cr, b )

    print ( '' )
    print ( '  Solution:' )
    print ( '' )
    print ( x )

  return

def r83_cr_sl ( n, a_cr, b ):

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
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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
    print ( 'r83_cr_sl - Fatal error!' )
    print ( '  Nonpositive N = %d' % ( n ) )
    raise Exception ( 'r83_cr_sl - Fatal error!' )

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = a_cr[1,1] * b[0]
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
        - a_cr[2,iful-1] * rhs[iful-1] \
        - a_cr[0,iful] * rhs[iful+1]

  rhs[ihaf] = rhs[ihaf] * a_cr[1,ihaf]

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
      rhs[ifulm] = a_cr[1,ifulm] * ( rhs[ifulm] \
        - a_cr[2,ifulm-1] * rhs[ifulm-1] \
        - a_cr[0,ifulm] * rhs[iful] )

    for i in range ( 0, n ):
      x[i] = rhs[i+1]

  return x

def r83_cr_sl_test ( ):

#*****************************************************************************80
#
## r83_cr_sl_test() tests r83_cr_sl().
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
  import numpy as np

  n = 5

  print ( '' )
  print ( 'r83_cr_sl_test():' )
  print ( '  r83_cr_sl() solves a factored system after ' )
  print ( '  r83_cr_fa() has factored it..' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
  print ( '  Demonstrate multiple system solution method.' )
  print ( '' )
#
#  Set the matrix values.
#
  a = r83_dif2 ( n, n )
#
#  Print the matrix.
#
  r83_print ( n, n, a, '  System matrix A:' )
#
#  Factor the matrix once.
#
  a_cr = r83_cr_fa ( n, a )

  for j in range ( 1, 3 ): 

    print ( '' )
    print ( '  Solve linear system number %d' % ( j ) )

    b = np.zeros ( n )

    if ( j == 1 ):
      b[n-1] = float ( n + 1 )
    else:
      b[0] = 1.0
      b[n-1] = 1.0
#
#  Solve the linear system.
#
    x = r83_cr_sl ( n, a_cr, b )

    print ( '' )
    print ( '  Solution' )
    print ( '' )
    print ( x )

  return

def r83_cr_sls ( n, a_cr, nb, b ):

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
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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
    print ( 'r83_cr_sls - Fatal error!' )
    print ( '  Nonpositive N = %d' % ( n ) )
    raise Exception ( 'r83_cr_sls - Fatal error!' )

  x = np.zeros ( [ n, nb ] )

  if ( n == 1 ):
    for j in range ( 0, nb ):
      x[0,j] = a_cr[1,0] * b[0,j]
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
          - a_cr[2,iful-1] * rhs[iful-1,j] \
          - a_cr[0,iful] * rhs[iful+1,j]

  for j in range ( 0, nb ):
    rhs[ihaf,j] = rhs[ihaf,j] * a_cr[1,ihaf]

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
        rhs[ifulm,j] = a_cr[1,ifulm] * ( rhs[ifulm,j] \
          - a_cr[2,ifulm-1] * rhs[ifulm-1,j] \
          - a_cr[0,ifulm] * rhs[iful,j] )

  for j in range ( 0, nb ):
    for i in range ( 0, n ):
      x[i,j] = rhs[i+1,j]

  return x

def r83_cr_sls_test ( ):

#*****************************************************************************80
#
## r83_cr_sls_test() tests r83_cr_sls().
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
  import numpy as np

  n = 5
  nb = 2

  print ( '' )
  print ( 'r83_cr_sls_test():' )
  print ( '  r83_cr_sls solves linear systems by cyclic reduction' )
  print ( '  after the R83 matrix has been factored by r83_CR_FA.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
  print ( '  Demonstrate multiple system solution method.' )
  print ( '' )
#
#  Set the matrix values.
#
  a = r83_dif2 ( n, n )
#
#  Print the matrix.
#
  r83_print ( n, n, a, '  System matrix A:' )
#
#  Factor the matrix once.
#
  a_cr = r83_cr_fa ( n, a )

  b = np.zeros ( [ n, nb ] )

  b[n-1,0] = float ( n + 1 )

  b[0,1] = 1.0
  b[n-1,1] = 1.0
#
#  Solve the linear system.
#
  x = r83_cr_sls ( n, a_cr, nb, b )

  r8ge_print ( n, nb, x, '  Solutions:' )

  return

def r83_dif2 ( m, n ):

#*****************************************************************************80
#
## r83_dif2() returns the DIF2 matrix in R83 format.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)). 
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
#
#  Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is a special case of the TRIS or tridiagonal scalar matrix.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is Toeplitz: constant along diagonals.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is positive definite.
#
#    A is an M matrix.
#
#    A is weakly diagonally dominant, but not strictly diagonally dominant.
#
#    A has an LU factorization A = L * U, without pivoting.
#
#      The matrix L is lower bidiagonal with subdiagonal elements:
#
#        L(I+1,I) = -I/(I+1)
#
#      The matrix U is upper bidiagonal, with diagonal elements
#
#        U(I,I) = (I+1)/I
#
#      and superdiagonal elements which are all -1.
#
#    A has a Cholesky factorization A = L * L', with L lower bidiagonal.
#
#      L(I,I) =    sqrt ( (I+1) / I )
#      L(I,I-1) = -sqrt ( (I-1) / I )
#
#    The eigenvalues are
#
#      LAMBDA(I) = 2 + 2 * COS(I*PI/(N+1))
#                = 4 SIN^2(I*PI/(2*N+2))
#
#    The corresponding eigenvector X(I) has entries
#
#       X(I)(J) = sqrt(2/(N+1)) * sin ( I*J*PI/(N+1) ).
#
#    Simple linear systems:
#
#      x = (1,1,1,...,1,1),   A*x=(1,0,0,...,0,1)
#
#      x = (1,2,3,...,n-1,n), A*x=(0,0,0,...,0,n+1)
#
#    det ( A ) = N + 1.
#
#    The value of the determinant can be seen by induction,
#    and expanding the determinant across the first row:
#
#      det ( A(N) ) = 2 * det ( A(N-1) ) - (-1) * (-1) * det ( A(N-2) )
#                = 2 * N - (N-1)
#                = N + 1
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
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969,
#    ISBN: 0882756494,
#    LC: QA263.68
#
#    Morris Newman, John Todd,
#    Example A8,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#    John Todd,
#    Basic Numerical Mathematics,
#    Volume 2: Numerical Algebra,
#    Birkhauser, 1980,
#    ISBN: 0817608117,
#    LC: QA297.T58.
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real A(3,N), the matrix.
#
  import numpy as np

  a = np.zeros( [ 3, n ] )

  for j in range ( 0, n):
    for i in range ( max ( 0, j - 1 ), min ( m, j + 2 ) ):
      if ( i == j - 1 ):
        a[i-j+1,j] = -1.0
      elif ( i == j ):
        a[i-j+1,j] = +2.0
      elif ( i == j + 1 ):
        a[i-j+1,j] = -1.0
  
  return a

def r83_dif2_test ( ):

#*****************************************************************************80
#
## r83_dif2_test() tests r83_dif2().
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
  print ( '' )
  print ( 'r83_dif2_test():' )
  print ( '  r83_dif2 sets an R83 matrix to the second difference.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a = r83_dif2 ( m, n )
    r83_print ( m, n, a, '  Second difference in R83 format:' )

  return

def r83_gs_sl ( n, a, b, x, it_max ):

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
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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
      print ( 'r83_gs_sl - Fatal error!' )
      print ( '  Zero diagonal entry, index = %d' % ( i ) )
      raise Exception ( 'r83_gs_sl - Fatal error!' )

  for it_num in range ( 0, it_max ):

    x[0] = ( b[0] - a[0,1] * x[1]   ) / a[1,0]
    for i in range ( 1, n - 1 ):
      x[i] = ( b[i] - a[2,i-1] * x[i-1] - a[0,i+1] * x[i+1] ) / a[1,i]
    x[n-1] = ( b[n-1] - a[2,n-2] * x[n-2] ) / a[1,n-1]

  return x

def r83_gs_sl_test ( rng ):

#*****************************************************************************80
#
## r83_gs_sl_test() tests r83_gs_sl().
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
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r83_gs_sl_test():' )
  print ( '  r83_gs_sl() applies Gauss-Seidel iteration with an R83 matrix' )
  print ( '  to solve a linear system A*x=b.' )
#
#  Set A to the second difference matrix.
#
  n = 10
  a = r83_dif2 ( n, n )
#
#  Choose a random solution.
#
  x1 = rng.random ( size = n )
#
#  Compute the corresponding right hand side.
#
  b = r83_mv ( n, n, a, x1 )
#
#  Call the Gauss-Seidel routine.
#
  x2 = np.ones ( n )
  it_max = 100
  x3 = r83_gs_sl ( n, a, b, x2, it_max )
#
#  Compute the residual.
#
  r = r83_res ( n, n, a, x3, b )
  r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
  e_norm = np.linalg.norm ( x1 - x3 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = %d' % ( n ) )
  print ( '  Norm of residual ||Ax-b|| = %g' % ( r_norm ) )
  print ( '  Norm of error ||x1-x2|| = %g' % ( e_norm ) )

  return

def r83_indicator ( m, n ):

#*****************************************************************************80
#
## r83_indicator() sets up an R83 indicator matrix.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real A(3,N), the R83 indicator matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( [ 3, n ], dtype = np.float64 )

  for j in range ( 0, n ):
    i_lo = max ( 0, j - 1 )
    i_hi = min ( m - 1, j + 1 )
    for i in range ( i_lo, i_hi + 1 ):
      a[i-j+1,j] = fac * ( i + 1 ) +  ( j + 1)

  return a

def r83_indicator_test ( ):

#*****************************************************************************80
#
## r83_indicator_test() tests r83_indicator().
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
  print ( '' )
  print ( 'r83_indicator_test():' )
  print ( '  r83_indicator() returns an indicator matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a = r83_indicator ( m, n )
    r83_print ( m, n, a, '  R83 indicator matrix:' )

  return

def r83_jac_sl ( n, a, b, x, it_max ):

#*****************************************************************************80
#
## r83_jac_sl() solves an R83 system using Jacobi iteration.
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
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 2.
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
#    real X_NEW(N), an updated approximate solution to the system.
#
  import numpy as np

#
#  No diagonal matrix entry can be zero.
#
  for i in range ( 0, n ):
    if ( a[1,i] == 0.0 ):
      print ( '' )
      print ( 'r83_jac_sl - Fatal error!' )
      print ( '  Zero diagonal entry, index = %d' % ( i ) )
      raise Exception ( 'r83_jac_sl - Fatal error!' )

  x_new = np.zeros ( n )

  for it_num in range ( 0, it_max ):

    x_new = r83_mv ( n, n, a, x )

    for i in range ( 0, n ):
      x_new[i] = b[i] - x_new[i] + a[1,i] * x[i]
      x_new[i] = x_new[i] / a[1,i]
      x[i] = x_new[i]

  return x_new

def r83_jac_sl_test ( rng ):

#*****************************************************************************80
#
## r83_jac_sl_test() tests r83_jac_sl().
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
#    rng: the current random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'r83_jac_sl_test():' )
  print ( '  r83_jac_sl() applies Jacobi iteration with an R83 matrix' )
  print ( '  to solve a linear system A*x=b.' )
#
#  Set A to the second difference matrix.
#
  n = 10
  a = r83_dif2 ( n, n )
#
#  Choose a random solution.
#
  x1 = rng.random ( size = n )
#
#  Compute the corresponding right hand side.
#
  b = r83_mv ( n, n, a, x1 )
#
#  Call the Jacobi routine.
#
  x2 = np.ones ( n )
  it_max = 100
  x3 = r83_jac_sl ( n, a, b, x2, it_max )
#
#  Compute the residual.
#
  r = r83_res ( n, n, a, x3, b )
  r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
  e_norm = np.linalg.norm ( x1 - x3 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = %d' % ( n ) )
  print ( '  Norm of residual ||Ax-b|| = %g' % ( r_norm ) )
  print ( '  Norm of error ||x1-x2|| = %g' % ( e_norm ) )

  return

def r83_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## r83_mtv() multiplies a vector by an R83 matrix.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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
#    integer M, N, the order of the matrix.
#
#    real A(3,N), the R83 matrix.
#
#    real X(N), the vector to be multiplied by A'.
#
#  Output:
#
#    real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):
    for i in range ( max ( 0, j - 1 ), min ( m, j + 2 ) ):
      b[j] = b[j] + x[i] * a[i-j+1,j]

  return b

def r83_mtv_test ( rng ):

#*****************************************************************************80
#
## r83_mtv_test() tests r83_mtv().
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
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r83_mtv_test():' )
  print ( '  r83_mv() computes b=A\'*x, where A is an R83 matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a_83 = r83_random ( m, n, rng )
    x = range ( 1, m + 1 )
    ax_83 = r83_mtv ( m, n, a_83, x )
    a_ge = r83_to_r8ge ( m, n, a_83 )
    ax_ge = r8ge_mtv ( m, n, a_ge, x )
    r8vec2_print ( ax_83, ax_ge, '  Product comparison:' )

  return

def r83_mv ( m, n, a, x ):

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
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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
      b[i] = b[i] + a[i-j+1,j] * x[j]

  return b

def r83_mv_test ( rng ):

#*****************************************************************************80
#
## r83_mv_test() tests r83_mv().
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
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r83_mv_test():' )
  print ( '  r83_mv computes b=A*x, where A is an R83 matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a_83 = r83_random ( m, n, rng )
    x = range ( 1, n + 1 )
    ax_83 = r83_mv ( m, n, a_83, x )
    a_ge = r83_to_r8ge ( m, n, a_83 )
    ax_ge = r8ge_mv ( m, n, a_ge, x )
    r8vec2_print ( ax_83, ax_ge, '  Product comparison:' )

  return

def r83_print ( m, n, a, title ):

#*****************************************************************************80
#
## r83_print() prints a R83 matrix.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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
#    integer M, N, the order of the matrix.
#
#    real A(3,N), the R83 matrix.
#
#    string TITLE, a title.
#
  r83_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r83_print_test ( ):

#*****************************************************************************80
#
## r83_print_test() tests r83_print().
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
  print ( '' )
  print ( 'r83_print_test():' )
  print ( '  r83_print prints an R83 matrix.' )

  m = 5
  n = 5
  a = r83_indicator ( m, n )
  r83_print ( m, n, a, '  R83 matrix:' )

  return

def r83_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r83_print_some() prints some of a R83 matrix.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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
#    integer M, N, the order of the matrix.
#
#    real A(3,N), the R83 matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column, to be printed.
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
    i2lo = max ( ilo, 0 )
    i2lo = max ( i2lo, j2lo - 1 )
    i2hi = min ( ihi, m - 1 )
    i2hi = min ( i2hi, j2hi + 1 )

    for i in range ( i2lo, i2hi + 1 ):
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      print ( '%5d:' % ( i ), end = '' )

      for j2 in range ( 1, inc + 1 ):

        j = j2lo - 1 + j2

        if ( i - j + 1 < 0 or 2 < i - j + 1 ):
          print ( '              ', end = '' )
        else:
          print ( '%14g' % ( a[i-j+1,j] ), end = '' )

      print ( '' )

  return

def r83_print_some_test ( ):

#*****************************************************************************80
#
## r83_print_some_test() tests r83_print_some().
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
  print ( '' )
  print ( 'r83_print_some_test():' )
  print ( '  r83_print_some() prints some of an R83 matrix.' )

  m = 5
  n = 5
  a = r83_indicator ( m, n )
  r83_print_some ( m, n, a, 1, 1, 4, 3, '  Rows 1-4, Cols 1-3:' )

  return

def r83_random ( m, n, rng ):

#*****************************************************************************80
#
## r83_random() randomizes a R83 matrix.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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
#    rng: the current random number generator.
#
#  Output:
#
#    real A(3,N), the R83 matrix.
#
  import numpy as np

  a = np.zeros ( [ 3, n ] )

  for j in range ( 0, n ):
    for i in range ( max ( 0, j - 1 ), min ( m, j + 2 ) ):
      r = rng.random ( )
      a[i-j+1,j] = r
 
  return a

def r83_random_test ( rng ):

#*****************************************************************************80
#
## r83_random_test() tests r83_random().
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
  print ( '' )
  print ( 'r83_random_test():' )
  print ( '  r83_random() randomizes an R83 matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a = r83_random ( m, n, rng )
    r83_print ( m, n, a, '  Random R83 matrix:' )

  return

def r83_res ( m, n, a, x, b ):

#*****************************************************************************80
#
## r83_res() computes the residual R = B-A*X for R83 matrices.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(3,N), the matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#    real B(M), the desired result A * x.
#
#  Output:
#
#    real R(M), the residual R = B - A * X.
#
  r = r83_mv ( m, n, a, x )

  for i in range ( 0, m ):
    r[i] = b[i] - r[i]

  return r

def r83_res_test ( rng ):

#*****************************************************************************80
#
## r83_res_test() tests r83_res().
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
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r83_res_test():' )
  print ( '  r83_res() computes b-A*x, where A is an R83 matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a = r83_random ( m, n, rng )
    x = range ( 1, n + 1 )
    b = r83_mv ( m, n, a, x )
    r = r83_res ( m, n, a, x, b )

    print ( '' )
    print ( '  Residual A*x-b' )
    print ( '' )
    print ( r )

  return

def r83_to_r8ge ( m, n, a_83 ):

#*****************************************************************************80
#
## r83_to_r8ge() copies an R83 matrix to an R8GE matrix.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
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
#    integer M, N, the order of the matrix.
#
#    real A_83(3,N), the R83 matrix.
#
#  Output:
#
#    real A_GE(M,N), the R8GE matrix.
#
  import numpy as np

  a_ge = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( max ( 0, j - 1 ), min ( m, j + 2 ) ): 
      a_ge[i,j] = a_83[i-j+1,j]

  return a_ge

def r83_to_r8ge_test ( rng ):

#*****************************************************************************80
#
## r83_to_r8ge_test() tests r83_to_r8ge().
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
#    rng: the current random number generator.
#
  print ( '' )
  print ( 'r83_to_r8ge_test():' )
  print ( '  r83_to_r8ge() converts an R83 matrix to R8GE format.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a_83 = r83_random ( m, n, rng )
    r83_print ( m, n, a_83, '  R83 matrix:' )

    a_ge = r83_to_r8ge ( m, n, a_83 )
    r8ge_print ( m, n, a_ge, '  R8GE matrix:' )

  return

def r83_zeros ( m, n ):

#*****************************************************************************80
#
## r83_zeros() zeros an R83 matrix.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 September 2015
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
#    real A(3,N), the R83 matrix.
#
  import numpy as np

  a = np.zeros ( [ 3, n ] )
 
  return a

def r83_zeros_test ( ):

#*****************************************************************************80
#
## r83_zeros_test() tests r83_zeros().
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
  print ( '' )
  print ( 'r83_zeros_test():' )
  print ( '  r83_zeros zeros an R83 matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 1, 4 ):

    if ( i == 1 ):
      m = 3
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 5
    elif ( i == 3 ):
      m = 5
      n = 3

    a = r83_zeros ( m, n )
    r83_print ( m, n, a, '  Zeroed R83 matrix:' )

  return

def r83_test ( ):

#*****************************************************************************80
#
## r83_test() tests r83().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 August 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'r83_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r83().' )

  rng = default_rng ( )

  r83_cg_test ( rng )
  r83_cr_fa_test ( )
  r83_cr_sl_test ( )
  r83_cr_sls_test ( )
  r83_dif2_test ( )
  r83_gs_sl_test ( rng )
  r83_indicator_test ( )
  r83_jac_sl_test ( rng )
  r83_mtv_test ( rng )
  r83_mv_test ( rng )
  r83_print_test ( )
  r83_print_some_test ( )
  r83_random_test ( rng )
  r83_res_test ( rng )
  r83_to_r8ge_test ( rng )
  r83_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r83_test():' )
  print ( '  Normal end of execution.' )
  return

def r8ge_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## r8ge_mtv() multiplies a vector by a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8GE matrix.
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
      b[j] = b[j] + x[i] * a[i,j]

  return b

def r8ge_mv ( m, n, a, x ):

#*****************************************************************************80
#
## r8ge_mv() multiplies an R8GE matrix times a vector.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8GE matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M), the product A * x.
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
## r8ge_print() prints an R8GE matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
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
  r8ge_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8ge_print_test ( ):

#*****************************************************************************80
#
## r8ge_print_test() tests r8ge_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ge_print_test():' )
  print ( '  r8ge_print prints an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print ( m, n, v, '  Here is an R8GE:' )

  return

def r8ge_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8ge_print_some() prints out a portion of an R8GE.
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
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ' ),

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ) ),

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ) ),

      print ( '' )

  return

def r8ge_print_some_test ( ):

#*****************************************************************************80
#
## r8ge_print_some_test() tests r8ge_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8ge_print_some_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8ge_print_some prints some of an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print_some ( m, n, v, 0, 3, 2, 5, '  Rows 0:2, Cols 3:5:' )

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

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test() tests r8vec2_print().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_print_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_print() prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( v, w, '  Print a pair of R8VEC\'s:' )

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
  r83_test ( )
  timestamp ( )

