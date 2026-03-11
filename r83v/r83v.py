#! /usr/bin/env python3
#
def r83v_test ( ):

#*****************************************************************************80
#
## r83v_test() tests r83v().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 August 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'r83v_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r83v().' )

  rng = default_rng ( )

  r83v_cg_test ( rng )
  r83v_copy_test ( )
  r83v_cr_fa_test ( )
  r83v_cr_sl_test ( )
  r83v_cr_sls_test ( )
  r83v_dif2_test ( )
  r83v_fs_test ( )
  r83v_gs_sl_test ( )
  r83v_indicator_test ( )
  r83v_jac_sl_test ( )
  r83v_mtv_test ( rng )
  r83v_mv_test ( rng )
  r83v_print_test ( )
  r83v_print_some_test ( )
  r83v_random_test ( rng )
  r83v_res_test ( rng )
  r83v_to_r8ge_test ( rng )
  r83v_to_r8vec_test ( )
  r83v_transpose_test ( )
  r83v_zeros_test ( )

  r8ge_to_r83v_test ( )

  r8vec_to_r83v_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r83v_test():' )
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

def r83v_cg ( n, a, b, c, ax, x ):

#*****************************************************************************80
#
## R83V_CG uses the conjugate gradient method on an R83V system.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2016
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
#    real A(min(M-1,N)), B(min(M,N)), C(min(M,N-1)), the R83V matrix.
#
#    real AX(N), the right hand side vector.
#
#    real X(N): an estimate for the solution, which may be 0.
#
#  Output:
#
#    real X(N): the approximate solution vector.
#
  import numpy as np
#
#  Initialize
#    AP = A * x,
#    R  = b - A * x,
#    P  = b - A * x.
#
  ap = r83v_mv ( n, n, a, b, c, x )

  r = np.zeros ( n )
  for i in range ( 0, n ):
    r[i] = ax[i] - ap[i]

  p = np.zeros ( n )
  for i in range ( 0, n ):
    p[i] = ax[i] - ap[i]
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP=A*P.
#
    ap = r83v_mv ( n, n, a, b, c, p )
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

    for i in range ( 0, n ):
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

def r83v_cg_test ( rng ):

#*****************************************************************************80
#
## r83v_cg_test() tests r83v_cg().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
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
  print ( 'r83v_cg_test()' )
  print ( '  r83v_cg() applies CG to an R83V matrix.' )
#
#  Set A to the second difference matrix.
#
  n = 10

  a, b, c = r83v_dif2 ( n, n )
#
#  Choose a random solution.
#
  x1 = rng.random ( size = n )
#
#  Compute the corresponding right hand side.
#
  ax = r83v_mv ( n, n, a, b, c, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x3 = r83v_cg ( n, a, b, c, ax, x2 )
#
#  Compute the residual.
#
  r = r83v_res ( n, n, a, b, c, x3, ax )
  r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
  e_norm = np.linalg.norm ( x1 - x3 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = ', n )
  print ( '  Norm of residual ||Ax-b|| = ', r_norm )
  print ( '  Norm of error ||x1-x2|| = ', e_norm )

  return

def r83v_copy ( m, n, a1, a2, a3 ):

#*****************************************************************************80
#
## R83V_COPY copies an R83V matrix.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A1(min(M-1,N)), A2(min(M,N)), A3(min(M,N-1)), the R83V matrix.
#
#  Output:
#
#    real B1(min(M-1,N)), B2(min(M,N)), B3(min(M,N-1)), the copy.
#
  import numpy as np

  b1 = np.zeros ( min ( m - 1, n     ) )
  b2 = np.zeros ( min ( m,     n     ) )
  b3 = np.zeros ( min ( m,     n - 1 ) )

  for i in range ( 0, min ( m - 1, n ) ):
    b1[i] = a1[i]

  for i in range ( 0, min ( m, n ) ):
    b2[i] = a2[i]

  for i in range ( 0, min ( m, n - 1 ) ):
    b3[i] = a3[i]

  return b1, b2, b3

def r83v_copy_test ( ):

#*****************************************************************************80
#
## R83V_COPY_TEST tests R83V_COPY.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'R83V_COPY_TEST' )
  print ( '  R83V_COPY copies an R83V matrix.' )

  a1, a2, a3 = r83v_indicator ( m, n )

  r83v_print ( m, n, a1, a2, a3, '  Indicator matrix A:' )

  b1, b2, b3 = r83v_copy ( m, n, a1, a2, a3 )

  r83v_print ( m, n, b1, b2, b3, '  B = copy of A:' )

  return

def r83v_cr_fa ( n, a, b, c ):

#*****************************************************************************80
#
## R83V_CR_FA decomposes an R83V matrix using cyclic reduction.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#    Once R83_CR_FA has decomposed a matrix A, then R83_CR_SL may be used to solve
#    linear systems A * x = b.
#
#    R83_CR_FA does not employ pivoting.  Hence, the results can be more
#    sensitive to ill-conditioning than standard Gauss elimination.  In
#    particular, R83_CR_FA will fail if any diagonal element of the matrix
#    is zero.  Other matrices may also cause R83_CR_FA to fail.
#
#    R83_CR_FA can be guaranteed to work properly if the matrix is strictly
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
#    defining this factorization may be used by R83_CR_SL to solve linear
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
#    10 February 2016
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
#    real A(min(M-1,N)), B(min(M,N)), C(min(M,N-1)), the R83V matrix.
#
#  Output:
#
#    real A_CR(3,2*N+1), factorization information.
#
  import numpy as np

  if ( n <= 0 ):
    print ( '' )
    print ( 'R83V_CR_FA - Fatal error!' )
    print ( '  Nonpositive N = ', n )
    raise Exception ( 'R83V_CR_FA - Fatal error!' )

  a_cr = np.zeros ( [ 3, 2 * n + 1 ] )

  if ( n == 1 ):
    a_cr[1,1] = 1.0 / b[0]
    return a_cr
#
#  Zero out the workspace entries.
#
  for i in range ( 1, n ):
    a_cr[0,i] = c[i-1]

  for i in range ( 1, n + 1 ):
    a_cr[1,i] = b[i-1]

  for i in range ( 1, n ):
    a_cr[2,i] = a[i-1]

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
      a_cr[1,ihaf]  = a_cr[1,ifulp] - a_cr[0,iful]  * a_cr[2,iful] \
                                    - a_cr[0,ifulp] * a_cr[2,ifulp]
      a_cr[2,ihaf] = - a_cr[2,ifulp] * a_cr[2,ifulp+1]
      a_cr[0,ihaf] = - a_cr[0,ifulp] * a_cr[0,ifulp+1]

  
  a_cr[1,ipntp+1] = 1.0 / a_cr[1,ipntp+1]

  return a_cr

def r83v_cr_fa_test ( ):

#*****************************************************************************80
#
## R83V_CR_FA_TEST tests R83V_CR_FA.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'R83V_CR_FA_TEST' )
  print ( '  R83V_CR_FA factors an R83V matrix' )
  print ( '  Once the matrix has been factored, we can call' )
  print ( '  R83V_CR_SL to solve a linear system.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Demonstrate multiple system solution method.' )
  print ( '' )
#
#  Set the matrix values.
#
  a, b, c = r83v_dif2 ( n, n )
#
#  Print the matrix.
#
  r83v_print ( n, n, a, b, c, '  System matrix A:' )
#
#  Factor the matrix once.
#
  a_cr = r83v_cr_fa ( n, a, b, c )
#
#  Print the factor information.
#
  if ( False ):
    r83_print ( n, 2*n+1, a_cr, '  Cyclic reduction factor information:' )

  for j in range ( 1, 3 ):

    print ( '' )
    print ( '  Solve linear system number ', j )

    ax = np.zeros ( n )

    if ( j == 1 ):
      ax[n-1] = float ( n + 1 )
    else:
      ax[0] = 1.0
      ax[n-1] = 1.0
#
#  Solve the linear system.
#
    x = r83v_cr_sl ( n, a_cr, ax )

    r8vec_print ( n, x, '  Solution:' )

  return

def r83v_cr_sl ( n, a_cr, ax ):

#*****************************************************************************80
#
## R83V_CR_SL solves a real linear system factored by R83V_CR_FA.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#    The matrix A must be tridiagonal.  R83_CR_FA is called to compute the
#    LU factors of A.  It does so using a form of cyclic reduction.  If
#    the factors computed by R83_CR_FA are passed to R83_CR_SL, then one or many
#    linear systems involving the matrix A may be solved.
#
#    Note that R83_CR_FA does not perform pivoting, and so the solution 
#    produced by R83_CR_SL may be less accurate than a solution produced 
#    by a standard Gauss algorithm.  However, such problems can be 
#    guaranteed not to occur if the matrix A is strictly diagonally 
#    dominant, that is, if the absolute value of the diagonal coefficient 
#    is greater than the sum of the absolute values of the two off diagonal 
#    coefficients, for each row of the matrix.
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
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
#    real A_CR(3,2*N+1), factorization information computed by R83V_CR_FA.
#
#    real AX(N), the right hand side vector.
#
#  Output:
#
#    real X(N), the solution of the linear system.
#
  import numpy as np

  if ( n <= 0 ):
    print ( '' )
    print ( 'R83V_CR_SL - Fatal error!' )
    print ( '  Nonpositive N = ', n )
    raise Exception ( 'R83V_CR_SL - Fatal error!' )

  if ( n == 1 ):
    x[0] = a_cr[1,1] * ax[0]
    return x
#
#  Set up RHS.
#
  rhs = np.zeros ( 2 * n + 1 )
  for i in range ( 1, n + 1 ):
    rhs[i] = ax[i-1]

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
      rhs[ihaf] = rhs[iful] - a_cr[2,iful-1] * rhs[iful-1] \
                            - a_cr[0,iful]   * rhs[iful+1]

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
        - a_cr[0,ifulm]   * rhs[iful] )

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = rhs[i+1]

  return x

def r83v_cr_sl_test ( ):

#*****************************************************************************80
#
## R83V_CR_SL_TEST tests R83V_CR_SL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'R83V_CR_SL_TEST' )
  print ( '  R83V_CR_SL solves a factored system' )
  print ( '  after R83V_CR_FA has factored it.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Demonstrate multiple system solution method.' )
  print ( '' )
#
#  Set the matrix values.
#
  a = 1.0 * np.ones ( n - 1 )
  b = 4.0 * np.ones ( n     )
  c = 2.0 * np.ones ( n - 1 )
#
#  Print the matrix.
#
  r83v_print ( n, n, a, b, c, '  Input matrix A:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the right hand side.
#
  ax = r83v_mv ( n, n, a, b, c, x )
  x = np.zeros ( n )
#
#  Factor the matrix.
#
  a_cr = r83v_cr_fa ( n, a, b, c )
#
#  Solve the linear system.
#
  x = r83v_cr_sl ( n, a_cr, ax )

  r8vec_print ( n, x, '  Solution:' )

  return

def r83v_cr_sls ( n, a_cr, nb, ax ):

#*****************************************************************************80
#
## R83V_CR_SLS solves several real linear systems factored by R83V_CR_FA.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)). 
#
#    The matrix A must be tridiagonal.  R83_CR_FA is called to compute the
#    LU factors of A.  It does so using a form of cyclic reduction.  If
#    the factors computed by R83_CR_FA are passed to R83_CR_SLS, then one or many
#    linear systems involving the matrix A may be solved.
#
#    Note that R83_CR_FA does not perform pivoting, and so the solution 
#    produced by R83_CR_SLS may be less accurate than a solution produced 
#    by a standard Gauss algorithm.  However, such problems can be 
#    guaranteed not to occur if the matrix A is strictly diagonally 
#    dominant, that is, if the absolute value of the diagonal coefficient 
#    is greater than the sum of the absolute values of the two off diagonal 
#    coefficients, for each row of the matrix.
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
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
#    real A_CR(3,2*N+1), factorization information computed by R83V_CR_FA.
#
#    integer NB, the number of right hand sides.
#
#    real AX(N,NB), the right hand side vectors.
#
#  Output:
#
#    real X(N,NB), the solutions of the linear system.
#
  import numpy as np

  if ( n <= 0 ):
    print ( '' )
    print ( 'R83V_CR_SLS - Fatal error!' )
    print ( '  Nonpositive N = ', n )
    raise Exception ( 'R83V_CR_SLS - Fatal error!' )

  x = np.zeros ( [ n, nb ] )

  if ( n == 1 ):
    for j in range ( 0, nb ):
      x[0,j] = a_cr[1,1] * ax[0,j]
    return x
#
#  Set up RHS.
#
  rhs = np.zeros ( [ 2 * n + 1, nb ] )
  for j in range ( 0, nb ):
    for i in range ( 1, n + 1 ):
      rhs[i,j] = ax[i-1,j]

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
      for j in range ( 0, nb ):
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

def r83v_cr_sls_test ( ):

#*****************************************************************************80
#
## R83V_CR_SLS_TEST tests R83V_CR_SLS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  print ( '' )
  print ( 'R83V_CR_SLS_TEST' )
  print ( '  R83V_CR_SLS solves multiple linear systems A*x1:xn=b1:bn' )
  print ( '  after R83V_CR_FA has factored it.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Demonstrate multiple system solution method.' )
  print ( '' )
#
#  Set the matrix values.
#
  a, b, c = r83v_dif2 ( n, n )
#
#  Print the matrix.
#
  r83v_print ( n, n, a, b, c, '  Input matrix A:' )
#
#  Factor the matrix once.
#
  a_cr = r83v_cr_fa ( n, a, b, c )
#
#  Set the number of right hand sides.
#
  nb = 2
  ax = np.zeros ( [ n, nb ] )

  ax[n-1,0] = float ( n + 1 )

  ax[0,1] = 1.0
  ax[n-1,1] = 1.0

  r8ge_print ( n, 2, ax, '  Right hand sides b1:b2' )
#
#  Solve the linear systems.
#
  x = r83v_cr_sls ( n, a_cr, nb, ax )

  r8ge_print ( n, 2, x, '  Solutions x1:x2' )

  return

def r83v_dif2 ( m, n ):

#*****************************************************************************80
#
## R83V_DIF2 returns the DIF2 matrix in R83V format.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
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
#    10 February 2016
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
#    real A(min(M-1,N)), B(min(M,N)), C(min(M,N-1)), the R83V matrix.
#
  import numpy as np

  a = -1.0 * np.ones ( min ( m - 1, n     ) )
  b = +2.0 * np.ones ( min ( m,     n     ) )
  c = -1.0 * np.ones ( min ( m,     n - 1 ) )

  return a, b, c

def r83v_dif2_test ( ):

#*****************************************************************************80
#
## R83V_DIF2_TEST tests R83V_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R83V_DIF2_TEST' )
  print ( '  R83V_DIF2 sets an R83V matrix to the second difference.' )
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

    a, b, c = r83v_dif2 ( m, n )
    r83v_print ( m, n, a, b, c, '  Second difference in R83V format:' )

  return

#! /usr/bin/env python
#
def r83v_fs ( n, a1, a2, a3, b ):

#*****************************************************************************80
#
## R83V_FS solves a linear system with R83V matrix.
#
#  Discussion:
#
#    This function is based on the LINPACK SGTSL routine.
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 February 2016
#
#  Author:
#
#    John Burkardt, based on the LINPACK SGTSL function.
#
#  Reference:
#
#    Jack Dongarra, Cleve Moler, Jim Bunch and Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, (Society for Industrial and Applied Mathematics),
#    3600 University City Science Center,
#    Philadelphia, PA, 19104-2688.
#    ISBN 0-89871-172-X
#
#  Input:
#
#    integer N, the order of the tridiagonal matrix.
#
#    real A1(N-1), A2(N), A3(N-1), the R83V matrix.
#
#    real B(N), the right hand side.
#
#  Output:
#
#    real X(N), the solution.
#
  import numpy as np
#
#  Copy the input data.
#
  c = np.zeros ( n )
  d = np.zeros ( n )
  e = np.zeros ( n )
  x = np.zeros ( n )

  c[0] = 0.0
  for i in range ( 1, n ):
    c[i] = a1[i-1]

  for i in range ( 0, n ):
    d[i] = a2[i]

  for i in range ( 0, n - 1 ):
    e[i] = a3[i]
  e[n-1] = 0.0

  for i in range ( 0, n ):
    x[i] = b[i]
#
#  Factor.
#
  c[0] = a2[0]

  if ( 2 <= n ):

    d[0] = e[0]
    e[0] = 0.0
    e[n-1] = 0.0

    for k in range ( 1, n ):
#
#  Find the larger of the two rows and interchange if necessary.
#
      if ( abs ( c[k-1] ) <= abs ( c[k] ) ):

        t = c[k]
        c[k] = c[k-1]
        c[k-1] = t

        t = d[k]
        d[k] = d[k-1]
        d[k-1] = t

        t = e[k]
        e[k] = e[k-1]
        e[k-1] = t

        t = x[k]
        x[k] = x[k-1]
        x[k-1] = t
#
#  Zero elements.
#
      if ( c[k-1] == 0.0 ):
        print ( '' )
        print ( 'R83V_FS - Fatal error!' )
        print ( '  Zero pivot on step K = ', k )
        raise Exception ( 'R83V_FS - Fatal error!' )

      t = - c[k] / c[k-1]
      c[k] = d[k] + t * d[k-1]
      d[k] = e[k] + t * e[k-1]
      e[k] = 0.0
      x[k] = x[k] + t * x[k-1]

  if ( c[n-1] == 0.0 ):
    print ( '' )
    print ( 'R83V_FS - Fatal error!' )
    print ( '  Zero pivot on step K = ', n )
    raise Exception ( 'R83V_FS - Fatal error!' )
#
#  Back solve.
#
  x[n-1] = x[n-1] / c[n-1]

  if ( 1 < n ):

    x[n-2] = ( x[n-2] - d[n-2] * x[n-1] ) / c[n-2]

    for k in range ( n - 2, 0, -1 ):
      x[k-1] = ( x[k-1] - d[k-1] * x[k] - e[k-1] * x[k+1] ) / c[k-1]

  return x

def r83v_fs_test ( ):

#*****************************************************************************80
#
## R83V_FS_TEST tests R83V_FS_SL.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 February 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'R83V_FS_TEST' )
  print ( '  R83V_FS factors and solves a linear system' )
  print ( '  for an R83V matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix values.
#
  a1, a2, a3 = r83v_dif2 ( n, n )
#
#  Set the desired solution.
#
  x1 = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r83v_mv ( n, n, a1, a2, a3, x1 )

  r8vec_print  ( n, b, '  The right hand side:' )
#
#  Solve the linear system.
#
  x2 = r83v_fs ( n, a1, a2, a3, b )

  r8vec_print ( n, x2, '  Solution:' )

  return

def r83v_gs_sl ( n, a, b, c, ax, x, it_max ):

#*****************************************************************************80
#
## R83V_GS_SL solves a R83V system using Gauss-Seidel iteration.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
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
#    real A(min(M-1,N)), B(min(M,N)), C(min(M,N-1)), the R83V matrix.
#
#    real AX(N), the right hand side of the linear system.
#
#    real X(N), an approximate solution to the system.
#
#    integer IT_MAX, the maximum number of iterations.
#
#  Output:
#
#    real X_NEW(N), an approximate solution to the system.
#
  import numpy as np
#
#  No diagonal matrix entry can be zero.
#
  for i in range ( 0, n ):
    if ( b[i] == 0.0 ):
      print ( '' )
      print ( 'R83V_GS_SL - Fatal error!' )
      print ( '  Zero diagonal entry, index = ', i )
      raise Exception ( 'R83V_GS_SL - Fatal error!' )

  x_new = np.zeros ( n )

  for it_num in range ( 0, it_max ):

    x_new[0] = ( ax[0] - c[0] * x[1]   ) / b[0]
    for i in range ( 1, n - 1 ):
      x_new[i] = ( ax[i] - a[i-1] * x_new[i-1] - c[i] * x[i+1] ) / b[i]
    x_new[n-1] = ( ax[n-1] - a[n-2] * x_new[n-2] ) / b[n-1]

    x = x_new.copy ( )

  return x_new
 
def r83v_gs_sl_test ( ):

#*****************************************************************************80
#
## R83V_GS_SL_TEST tests R83V_GS_SL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'R83V_GS_SL_TEST' )
  print ( '  R83V_GS_SL applies Gauss-Seidel iteration with an R83V matrix' )
  print ( '  to solve a linear system A*x=b.' )
#
#  Set A to the second difference matrix.
#
  n = 10

  a, b, c = r83v_dif2 ( n, n )
#
#  Choose a random solution.
#
  x1 = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  ax = r83v_mv ( n, n, a, b, c, x1 )
#
#  Set the starting solution.
#
  x2 = np.zeros ( n )
#
#  Call the Gauss-Seidel routine.
#
  it_max = 25

  for i in range ( 0, 3 ):

    x2 = r83v_gs_sl ( n, a, b, c, ax, x2, it_max )

    r8vec_print ( n, x2, '  Current solution estimate:' )

  return

def r83v_indicator ( m, n ):

#*****************************************************************************80
#
## R83V_INDICATOR sets up an R83V indicator matrix.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2016
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
#    real A(min(M-1,N)), B(min(M,N)), C(min(M,N-1)), the R83V matrix.
#
  import numpy as np

  a = np.zeros ( min ( m - 1, n     ) )
  b = np.zeros ( min ( m,     n     ) )
  c = np.zeros ( min ( m,     n - 1 ) )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for i in range ( 0, min ( m - 1, n ) ):
    a[i] = float ( ( fac * ( i + 2 ) + i ) + 1 )

  for i in range ( 0, min ( m, n ) ):
    b[i] = float ( ( fac * ( i + 1 ) + i ) + 1 )

  for i in range ( 0, min ( m, n - 1 ) ):
    c[i] = float ( ( fac * ( i + 1 ) + i + 1 ) + 1 )

  return a, b, c

def r83v_indicator_test ( ):

#*****************************************************************************80
#
## R83V_INDICATOR_TEST tests R83V_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 January 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R83V_INDICATOR_TEST' )
  print ( '  R83V_INDICATOR sets an R83V indicator matrix.' )
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

    a, b, c = r83v_indicator ( m, n )
    r83v_print ( m, n, a, b, c, '  R83V indicator matrix:' )

  return

def r83v_jac_sl ( n, a, b, c, ax, x, it_max ):

#*****************************************************************************80
#
## R83V_JAC_SL solves a R83V system A*x=b using Jacobi iteration.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
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
#    real A(min(M-1,N)), B(min(M,N)), C(min(M,N-1)), the R83V matrix.
#
#    real AX(N), the right hand side of the linear system.
#
#    real X(N), an approximate solution to the system.
#
#    integer IT_MAX, the maximum number of iterations.
#
#  Output:
#
#    real X(N), an updated approximate solution to the system.
#
  import numpy as np
#
#  No diagonal matrix entry can be zero.
#
  for i in range ( 0, n ):
    if ( b[i] == 0.0 ):
      print ( '' )
      print ( 'R83V_JAC_SL - Fatal error!' )
      print ( '  Zero diagonal entry, index = ', i )
      raise Exception ( 'R83V_JAC_SL - Fatal error!' )
#
#  Iterate IT_MAX times.
#
  x_new = np.zeros ( n )

  for it_num in range ( 0, it_max ):

    for i in range ( 0, n ):
      x_new[i] = ax[i]

    for i in range ( 0, n - 1 ):
      x_new[i] = x_new[i] - c[i] * x[i+1]

    for i in range ( 0, n - 1 ):
      x_new[i+1]   = x_new[i+1] - a[i] * x[i]
#
#  Divide by diagonal terms.
#
    for i in range ( 0, n ):
      x_new[i] = x_new[i] / b[i]
#
#  Update.
#
    x = x_new.copy ( )

  return x

def r83v_jac_sl_test ( ):

#*****************************************************************************80
#
## R83V_JAC_SL_TEST tests R83V_JAC_SL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    01 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'R83V_JAC_SL_TEST' )
  print ( '  R83V_JAC_SL applies Jacobi iteration with an R83V matrix' )
  print ( '  to solve a linear system A*x=b.' )
#
#  Set A to the second difference matrix.
#
  n = 10

  a, b, c = r83v_dif2 ( n, n )
#
#  Choose a random solution.
#
  x1 = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  ax = r83v_mv ( n, n, a, b, c, x1 )
#
#  Set the starting vector.
#
  x2 = np.zeros ( n )
#
#  Call the Jacobi routine.
#
  it_max = 25

  for i in range ( 0, 3 ):

    x2 = r83v_jac_sl ( n, a, b, c, ax, x2, it_max )

    r8vec_print ( n, x2, '  Current solution:' )

  return

def r83v_mtv ( m, n, a, b, c, x ):

#*****************************************************************************80
#
## R83V_MTV multiplies a vector by an R83V matrix.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the linear system.
#
#    real A(min(M-1,N)), B(min(M,N)), C(min(M,N-1)), the R83V matrix.
#
#    real X(M), the vector to be multiplied by A'.
#
#  Output:
#
#    real AX(N), the product A' * x.
#
  import numpy as np

  ax = np.zeros ( n )
#
#  Find each nonzero A(I,J), multiply by X(I), add to B(J).
#
#  A(K) = A(K+1,K) = A'(K,K+1)
#
  for k in range ( 0, min ( m - 1, n ) ):
    ax[k] = ax[k] + a[k] * x[k+1]
#
#  B(K) = A(K,K) = A'(K,K).
#
  for k in range ( 0, min ( m, n ) ):
    ax[k] = ax[k] + b[k] * x[k]
#
#  C(K) = A(K,K+1) = A'(K+1,K)
#
  for k in range ( 0, min ( m, n - 1 ) ):
    ax[k+1] = ax[k+1] + c[k] * x[k]

  return ax

def r83v_mtv_test ( rng ):

#*****************************************************************************80
#
## r83v_mtv_test() tests r83v_mtv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
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
  print ( 'r83v_mtv_test()' )
  print ( '  r83v_mv() computes b=A''*x, where A is an R83V matrix.' )
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

    a_83v, b_83v, c_83v = r83v_random ( m, n, rng )
    x = r8vec_indicator1 ( m )
    ax_83v = r83v_mtv ( m, n, a_83v, b_83v, c_83v, x )
    a_ge = r83v_to_r8ge ( m, n, a_83v, b_83v, c_83v )
    ax_ge = r8ge_mtv ( m, n, a_ge, x )
    r8vec2_print ( ax_83v, ax_ge, '  Product comparison:' )

  return

def r83v_mv ( m, n, a, b, c, x ):

#*****************************************************************************80
#
## r83v_mv() multiplies a R83V matrix times a vector.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the linear system.
#
#    real A(min(M-1,N)), B(min(M,N)), C(min(M,N-1)), the R83V matrix.
#
#    real X(N), the vector to be multiplied.
#
#  Output:
#
#    real AX(M), the product A * x.
#
  import numpy as np
#
#  Multiply.
#
  ax = np.zeros ( m )

  for k in range ( 0, min ( m - 1, n ) ):
    ax[k+1] = ax[k+1] + a[k] * x[k]

  for k in range ( 0, min ( m, n ) ):
    ax[k] = ax[k] + b[k] * x[k]

  for k in range ( 0, min ( m, n - 1 ) ):
    ax[k] = ax[k] + c[k] * x[k+1]

  return ax

def r83v_mv_test ( rng ):

#*****************************************************************************80
#
## r83v_mv_test() tests r83v_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
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
  print ( 'r83v_mv_test():' )
  print ( '  r83v_mv() computes b=A*x, where A is an R83V matrix.' )
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

    a_83v, b_83v, c_83v = r83v_random ( m, n, rng )
    x = r8vec_indicator1 ( n )
    ax_83v = r83v_mv ( m, n, a_83v, b_83v, c_83v, x )
    a_ge = r83v_to_r8ge ( m, n, a_83v, b_83v, c_83v )
    ax_ge = r8ge_mv ( m, n, a_ge, x )
    r8vec2_print ( ax_83v, ax_ge, '  Product comparison:' )

  return

def r83v_print ( m, n, a, b, c, title ):

#*****************************************************************************80
#
## R83V_PRINT prints an R83V matrix.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(min(M-1,N)), B(min(M,N)), C(min(M,N-1)), the R83V matrix.
#
#    string TITLE, a title.
#
  r83v_print_some ( m, n, a, b, c, 1, 1, m, n, title )

  return

def r83v_print_test ( ):

#*****************************************************************************80
#
## R83V_PRINT_TEST tests R83V_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R83V_PRINT_TEST' )
  print ( '  R83V_PRINT prints an R83V matrix.' )

  m = 5
  n = 5
  a, b, c = r83v_indicator ( m, n )
  r83v_print ( m, n, a, b, c, '  R83V matrix:' )

  return

def r83v_print_some ( m, n, a, b, c, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R83V_PRINT_SOME prints some of a R83V matrix.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2016
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
#    real A(min(M-1,N)), B(min(M,N)), C(min(M+1,N)), the R83V matrix.
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
    i2lo = max ( ilo, 1 )
    i2lo = max ( i2lo, j2lo - 1 )
    i2hi = min ( ihi, m )
    i2hi = min ( i2hi, j2hi + 1 )

    for i in range ( i2lo, i2hi + 1 ):
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      print ( '%5d:' % ( i ), end = '' )

      for j2 in range ( 1, inc + 1 ):

        j = j2lo - 1 + j2

        if ( j == i - 1 ):
          print ( '%14g' % ( a[i-2] ), end = '' )
        elif ( j == i ):
          print ( '%14g' % ( b[i-1] ), end = '' )
        elif ( j == i + 1  ):
          print ( '%14g' % ( c[i-1] ), end = '' )
        else:
          print ( '              ', end = '' )

      print ( '' )

  return

def r83v_print_some_test ( ):

#*****************************************************************************80
#
## R83V_PRINT_SOME_TEST tests R83V_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r83v_print_some_test():' )
  print ( '  r83v_print_some() prints some of an R83V matrix.' )

  m = 5
  n = 5
  a, b, c = r83v_indicator ( m, n )
  r83v_print_some ( m, n, a, b, c, 2, 2, 5, 4, '  Rows 2-5, Cols 2-4:' )

  return

def r83v_random ( m, n, rng ):

#*****************************************************************************80
#
## r83v_random() randomizes an R83V matrix.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(min(M-1,N)), B(min(M,N)), C(min(M,N-1)), the R83V matrix.
#
  a = rng.random ( size = min ( m - 1, n     ) )
  b = rng.random ( size = min ( m,     n     ) )
  c = rng.random ( size = min ( m,     n - 1 ) )

  return a, b, c

def r83v_random_test ( rng ):

#*****************************************************************************80
#
## r83v_random_test() tests r83v_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
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
  print ( 'r83v_random_test():' )
  print ( '  r83v_random() randomizes an R83V matrix.' )
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

    a, b, c = r83v_random ( m, n, rng )
    r83v_print ( m, n, a, b, c, '  Random R83V matrix:' )

  return

def r83v_res ( m, n, a, b, c, x, ax ):

#*****************************************************************************80
#
## r83v_res() computes the residual R = b-A*x for R83V matrices.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2016
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
#    real A(min(M-1,N)), B(min(M,N)), C(min(M,N-1)), the R83V matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#    real AX(M), the desired result A * x.
#
#  Output:
#
#    real R(M), the residual R = b - A * x.
#
  r = r83v_mv ( m, n, a, b, c, x )

  for i in range ( 0, m ):
    r[i] = ax[i] - r[i]

  return r

def r83v_res_test ( rng ):

#*****************************************************************************80
#
## r83v_res_test() tests r83v_res().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
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
  print ( 'r83v_res_test():' )
  print ( '  r83v_res() computes b-A*x, where A is an R83V matrix.' )
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

    a, b, c = r83v_random ( m, n, rng )
    x = r8vec_indicator1 ( n )
    ax = r83v_mv ( m, n, a, b, c, x )
    r = r83v_res ( m, n, a, b, c, x, ax )
    r8vec_print ( m, r, '  Residual A*x-b:' )

  return

def r83v_to_r8ge ( m, n, a_83v, b_83v, c_83v ):

#*****************************************************************************80
#
## r83v_to_r8ge() copies an R83V matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
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
#    real A_83V(min(M-1,N)), B_83V(min(M,N)), C_83V(min(M,N-1)), 
#    the R83V matrix.
#
#  Output:
#
#    real A_GE(M,N), the R8GE matrix.
#
  import numpy as np

  a_ge = np.zeros ( [ m, n ] )

  for k in range ( 0, min ( m - 1, n ) ):
    a_ge[k+1,k] = a_83v[k]

  for k in range ( 0, min ( m, n ) ):
    a_ge[k,k] = b_83v[k]

  for k in range ( 0, min ( m, n - 1 ) ):
    a_ge[k,k+1] = c_83v[k]

  return a_ge

def r83v_to_r8ge_test ( rng ):

#*****************************************************************************80
#
## r83v_to_r8ge_test() tests r83v_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
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
  print ( 'r83v_to_r8ge_test():' )
  print ( '  r83v_to_r8ge() converts an R83V matrix to R8GE format.' )
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

    a_83v, b_83v, c_83v = r83v_random ( m, n, rng )
    r83v_print ( m, n, a_83v, b_83v, c_83v, '  R83V matrix:' )

    a_ge = r83v_to_r8ge ( m, n, a_83v, b_83v, c_83v )
    r8ge_print ( m, n, a_ge, '  R8GE matrix:' )

  return

def r83v_to_r8vec ( m, n, a1, a2, a3 ):

#*****************************************************************************80
#
## R83V_TO_R8VEC copies an R83V matrix to an R8VEC.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A1(min(M-1,N)), A2(min(M,N)), A3(min(M,N-1)), 
#    the matrix.
#
#  Output:
#
#    real A(min(M-1,N)+min(M,N)+min(M,N-1)), the vector.
#
  import numpy as np

  a = np.zeros ( min ( m - 1, n ) + min ( m, n ) + min ( m, n - 1 ) )

  k = 0
  for j in range ( 0, n ):
 
    if ( j < m + 1 and 1 <= j ):
      a[k] = a3[j-1]
      k = k + 1

    if ( j < m ):
      a[k] = a2[j]
      k = k + 1

    if ( j < m - 1 ):
      a[k] = a1[j]
      k = k + 1

  return a

def r83v_to_r8vec_test ( ):

#*****************************************************************************80
#
## R83V_TO_R8VEC_TEST tests R83V_TO_R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R83V_TO_R8VEC_TEST' )
  print ( '  R83V_TO_R8VEC copies an R83V matrix to an R8VEC.' )
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

    a1, a2, a3 = r83v_indicator ( m, n )
    r83v_print ( m, n, a1, a2, a3, '  R83V matrix A:' )

    a = r83v_to_r8vec ( m, n, a1, a2, a3 )
    na = min ( m - 1, n ) + min ( m, n ) + min ( m, n - 1 )
    r8vec_print ( na, a, '  Vector version of A:' )

  return

def r83v_transpose ( m, n, a1, a2, a3 ):

#*****************************************************************************80
#
## R83V_TRANSPOSE makes a transposed copy of an R83V matrix.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A1(min(M-1,N)), A2(min(M,N)), A3(min(M,N-1)), the R83V matrix.
#
#  Output:
#
#    real B1(min(N-1,M)), B2(min(N,M)), B3(min(N,M-1)), 
#    the tranposed copy.
#
  import numpy as np

  b1 = np.zeros ( min ( n - 1, m     ) )
  b2 = np.zeros ( min ( n,     m     ) )
  b3 = np.zeros ( min ( n,     m - 1 ) )

  for i in range ( 0, min ( m, n - 1 ) ):
    b1[i] = a3[i]

  for i in range ( 0, min ( m, n ) ):
    b2[i] = a2[i]

  for i in range ( 0, min ( m - 1, n ) ):
    b3[i] = a1[i]

  return b1, b2, b3

def r83v_transpose_test ( ):

#*****************************************************************************80
#
## R83V_TRANSPOSE_TEST tests R83V_TRANSPOSE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'R83V_TRANSPOSE_TEST' )
  print ( '  R83V_TRANSPOSE makes a transposed copy of an R83V matrix.' )

  a1, a2, a3 = r83v_indicator ( m, n )

  r83v_print ( m, n, a1, a2, a3, '  Indicator matrix A:' )

  b1, b2, b3 = r83v_transpose ( m, n, a1, a2, a3 )

  r83v_print ( n, m, b1, b2, b3, '  B = transposed copy of A:' )

  return

def r83v_zeros ( m, n ):

#*****************************************************************************80
#
## R83V_ZEROS zeros an R83V matrix.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the linear system.
#
#  Output:
#
#    real A(min(M-1,N)), B(min(M,N)), C(min(M,N-1)), the R83V matrix.
#
  import numpy as np

  a = np.zeros ( min ( m - 1, n     ) )
  b = np.zeros ( min ( m,     n     ) )
  c = np.zeros ( min ( m,     n - 1 ) )
 
  return a, b, c

def r83v_zeros_test ( ):

#*****************************************************************************80
#
## R83V_ZEROS_TEST tests R83V_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R83V_ZEROS_TEST' )
  print ( '  R83V_ZEROS zeros an R83V matrix.' )
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

    a, b, c = r83v_zeros ( m, n )
    r83v_print ( m, n, a, b, c, '  Zeroed R83V matrix:' )

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
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8ge_to_r83v ( m, n, a ):

#*****************************************************************************80
#
## R8GE_TO_R83V copies (some of) an R8GE matrix to an R83V matrix.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(M,N), the R8GE matrix.
#
#  Output:
#
#    real A1(min(M-1,N)), A2(min(M,N)), A3(min(M,N-1)), 
#    the R83V matrix.
#
  import numpy as np
#
#  Get sizes of A1, A2, A3.
#
  a1hi = min ( m - 1, n )
  a2hi = min ( m,     n )
  a3hi = min ( m,     n - 1 )

  a1 = np.zeros ( a1hi )
  for k in range ( 0, a1hi ):
    a1[k] = a[k+1,k]

  a2 = np.zeros ( a2hi )
  for k in range ( 0, a2hi ):
    a2[k] = a[k,k]

  a3 = np.zeros ( a3hi )
  for k in range ( 0, a3hi ):
    a3[k] = a[k,k+1]
   
  return a1, a2, a3

def r8ge_to_r83v_test ( ):

#*****************************************************************************80
#
## r8ge_to_r83v_test() tests r8ge_to_r83v().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ge_to_r83v_test():' )
  print ( '  r8ge_to_r83v() copies an R8GE matrix to an R83V matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for k in range ( 0, 3 ):

    if ( k == 0 ):
      m = 3
      n = 5
    elif ( k == 1 ):
      m = 5
      n = 5
    elif ( k == 2 ):
      m = 5
      n = 3

    a = np.zeros ( [ m, n ] )

    for j in range ( 0, n ):
      for i in range ( 0, m ):
        a[i,j] = 10 * ( i + 1 ) + j + 1
 
    print ( '' )
    print ( '  Initial R8GE matrix A:' )
    print ( a )

    a1, a2, a3 = r8ge_to_r83v ( m, n, a )
    r83v_print ( m, n, a1, a2, a3, '  R83V copy of (some of ) matrix A:' )

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

def r8vec_to_r83v ( m, n, a ):

#*****************************************************************************80
#
## R8VEC_TO_R83V copies an R8VEC to an R83V matrix.
#
#  Discussion:
#
#    The R83V storage format is used for a tridiagonal matrix.
#    The subdiagonal is in A(min(M-1,N)).
#    The diagonal is in B(min(M,N)).
#    The superdiagonal is in C(min(M,N-1)).
#
#  Example:
#
#    An R83V matrix of order 3x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#
#    An R83 matrix of order 5x5 would be stored:
#
#      B1  C1  **  **  **
#      A1  B2  C2  **  **
#      **  A2  B3  C3  **
#      **  **  A3  B4  C4
#      **  **  **  A4  B5
#
#    An R83 matrix of order 5x3 would be stored:
#
#      B1  C1  **
#      A1  B2  C2
#      **  A2  B3
#      **  **  A3
#      **  **  **
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(min(N-1,M)+min(N,M)+min(N,M-1)), the vector.
#
#  Output:
#
#    real A1(min(M-1,N)), A2(min(M,N)), A3(min(M,N-1)), 
#    the matrix.
#
  import numpy as np

  ahi = min ( m - 1, n )
  bhi = min ( m,     n )
  chi = min ( m,     n - 1 )

  a1 = np.zeros ( ahi )
  a2 = np.zeros ( bhi )
  a3 = np.zeros ( chi )

  k = 0
  for j in range ( 0, n ):

    if ( j < m + 1 and 1 <= j ):
      a3[j-1] = a[k]
      k = k + 1

    if ( j < m ):
      a2[j] = a[k]
      k = k + 1

    if ( j < m - 1 ):
      a1[j] = a[k]
      k = k + 1
   
  return a1, a2, a3

def r8vec_to_r83v_test ( ):

#*****************************************************************************80
#
## R8VEC_TO_R83V_TEST tests R8VEC_TO_R83V.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8VEC_TO_R83V_TEST' )
  print ( '  R8VEC_TO_R83V copies an R8VEC to an R83V matrix.' )
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

    ahi = min ( m - 1, n )
    bhi = min ( m,     n )
    chi = min ( m,     n - 1 )

    na = ahi + bhi + chi

    a = r8vec_indicator1 ( na )
    r8vec_print ( na, a, '  R8VEC:' )

    a1, a2, a3 = r8vec_to_r83v ( m, n, a )
    r83v_print ( m, n, a1, a2, a3, '  R83V matrix:' )

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
  r83v_test ( )
  timestamp ( )
 
