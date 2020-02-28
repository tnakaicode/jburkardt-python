#! /usr/bin/env python3
#
def i4_log_10 ( i ):

#*****************************************************************************80
#
## I4_LOG_10 returns the integer part of the logarithm base 10 of ABS(X).
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
#    I4_LOG_10 ( I ) + 1 is the number of decimal digits in I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the number whose logarithm base 10 is desired.
#
#    Output, integer VALUE, the integer part of the logarithm base 10 of
#    the absolute value of X.
#
  i = int ( i )

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
## I4_LOG_10_TEST tests I4_LOG_10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'I4_LOG_10_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_LOG_10: whole part of log base 10,' )
  print ( '' )
  print ( '  X, I4_LOG_10' )
  print ( '' )

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print ( '%6d  %12d' % ( x[i], j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_LOG_10_TEST' )
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
#    27 October 2014
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
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8_UNIFORM_01 - Fatal error!' )

  k = ( seed // 127773 )

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

def r8ge_cg ( n, a, b, x ):

#*****************************************************************************80
#
## R8GE_CG uses the conjugate gradient method on an R8GE system.
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
#    The matrix A must be a positive definite symmetric band matrix.
#
#    The method is designed to reach the solution after N computational
#    steps.  However, roundoff may introduce unacceptably large errors for
#    some problems.  In such a case, calling the routine again, using
#    the computed solution as the new starting estimate, should improve
#    the results.
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
#    Frank Beckman,
#    The Solution of Linear Equations by the Conjugate Gradient Method,
#    in Mathematical Methods for Digital Computers,
#    edited by John Ralston, Herbert Wilf,
#    Wiley, 1967,
#    ISBN: 0471706892,
#    LC: QA76.5.R3.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be positive.
#
#    Input, real A(N,N), the matrix.
#
#    Input, real B(N), the right hand side vector.
#
#    Input/output, real X(N).
#    On input, an estimate for the solution, which may be 0.
#    On output, the approximate solution vector.
#
  import numpy as np
#
#  Initialize
#    AP = A * x,
#    R  = b - A * x,
#    P  = b - A * x.
#
  ap = r8ge_mv ( n, n, a, x )

  r = np.zeros ( n, dtype = np.float64 )
  for i in range ( 0, n ):
    r[i] = b[i] - ap[i]

  p = np.zeros ( n, dtype = np.float64 )
  for i in range ( 0, n ):
    p[i] = b[i] - ap[i]
#
#  Do the N steps of the conjugate gradient method.
#
  for it in range ( 0, n ):
#
#  Compute the matrix*vector product AP=A*P.
#
    ap = r8ge_mv ( n, n, a, p )
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

def r8ge_cg_test ( ):

#*****************************************************************************80
#
## R8GE_CG_TEST tests R8GE_CG for a full storage matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8GE_CG_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_CG applies CG to an R8GE matrix.' )
#
#  Choose a random positive definite symmetric matrix A.
#
  n = 10
  key = 123456789

  a = r8ge_pds_random ( n, key )
#
#  Choose a random solution.
#
  seed = 123456789
  x1, seed = r8vec_uniform_01 ( n, seed )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x1 )
#
#  Call the CG routine.
#
  x2 = np.ones ( n )
  x3 = r8ge_cg ( n, a, b, x2 )
#
#  Compute the residual.
#
  r = r8ge_res ( n, n, a, x3, b )
  r_norm = r8vec_norm ( n, r )
#
#  Compute the error.
#
  e_norm = r8vec_norm_affine ( n, x1, x3 )
#
#  Report.
#
  print ( '' )
  print ( '  Number of variables N = %d' % ( n ) )
  print ( '  Norm of residual ||Ax-b|| = %g' % ( r_norm ) )
  print ( '  Norm of error ||x1-x2|| = %g' % ( e_norm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_CG_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_co ( n, a ):

#*****************************************************************************80
#
## R8GE_CO factors a R8GE matrix and estimates its condition number.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    For the system A * X = B, relative perturbations in A and B
#    of size EPSILON may cause relative perturbations in X of size
#    EPSILON/RCOND.
#
#    If RCOND is so small that the logical expression
#      1.0E+00 + rcond == 1.0E+00
#    is true, then A may be singular to working precision.  In particular,
#    RCOND is zero if exact singularity is detected or the estimate
#    underflows.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt.
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
#    Output, real A_LU(N,N), the LU factorization of the matrix.
#
#    Output, integer PIVOT(N), the pivot indices.
#
#    Output, real RCOND, an estimate of the reciprocal condition number of A.
#
#    Output, real Z(N), a work vector whose contents are usually unimportant.
#    If A is close to a singular matrix, then Z is an approximate null vector
#    in the sense that
#      norm ( A * Z ) = RCOND * norm ( A ) * norm ( Z ).
#
  import numpy as np
#
#  Compute the L1 norm of A.
#
  anorm = 0.0
  for j in range ( 0, n ):
    t = 0.0
    for i in range ( 0, n ):
      t = t + abs ( a[i,j] )
    anorm = max ( anorm, t )
#
#  Compute the LU factorization.
#
  a_lu, pivot, info = r8ge_fa ( n, a )
#
#  RCOND = 1 / ( norm(A) * (estimate of norm(inverse(A))) )
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
        for i in range ( k + 1, n ):
          z[i] = z[i] + t * a_lu[k,i]

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
      z[k] = z[k] + a_lu[i,k] * z[k]

    t = abs ( z[k] )

    if ( 1.0 < t ):
      for i in range ( 0, n ):
        z[i] = z[i] / t

    l = pivot[k]
    t    = z[l]
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
    t    = z[l]
    z[l] = z[k]
    z[k] = t

    for i in range ( k + 1, n ):
      z[i] = z[i] + t * a_lu[i,k]

    if ( 1.0 < abs ( z[k] ) ):
      ynorm = ynorm / abs ( z[k] )
      for i in range ( 0, n ):
        z[i] = z[i] / abs ( z[k] )

  s = 0.0
  for i in range ( 0, n ):
    s = s + abs ( z[i] )

  for i in range ( 0, n ):
    z[i] = z[i] / s

  ynorm = ynorm / s
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
      z[i] = z[i] - z[k] * a_lu[i,k]
#
#  Normalize Z in the L1 norm.
#
  t = 0.0
  for i in range ( 0, n ):
    t = t + abs ( z[i] )

  for i in range ( 0, n ):
    z[i] = z[i] / t

  ynorm = ynorm / t

  if ( anorm != 0.0E+00 ):
    rcond = ynorm / anorm
  else:
    rcond = 0.0

  return a_lu, pivot, rcond, z

def r8ge_co_test ( ):

#*****************************************************************************80
#
## R8GE_CO_TEST tests R8GE_CO.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4
  x = 2.0
  y = 3.0

  print ( '' )
  print ( 'R8GE_CO_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_CO estimates the condition number of an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = x + y
      else:
        a[i,j] = y

  a_norm_l1 = 0.0
  for j in range ( 0, n ):
    t = 0.0
    for i in range ( 0, n ):
      t = t + abs ( a[i,j] )
    a_norm_l1 = max ( a_norm_l1, t )

  a_lu, pivot, info = r8ge_fa ( n, a )

  a_inverse = r8ge_inverse ( n, a_lu, pivot )

  a_inverse_norm_l1 = 0.0
  for j in range ( 0, n ):
    t = 0.0
    for i in range ( 0, n ):
      t = t + abs ( a_inverse[i,j] )
    a_inverse_norm_l1 = max ( a_inverse_norm_l1, t )

  cond_l1 = a_norm_l1 * a_inverse_norm_l1

  print ( '' )
  print ( '  The L1 condition number is %g' % ( cond_l1 ) )
#
#  Factor the matrix.
#
  a_lu, pivot, rcond, z = r8ge_co ( n, a )

  print ( '' )
  print ( '  The R8GE_CO estimate is %g' % ( 1.0 / rcond ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_CO_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_det ( n, a_lu, pivot ):

#*****************************************************************************80
#
## R8GE_DET: determinant of a matrix factored by R8GE_FA or R8GE_TRF.
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
#    R8GE storage is used by LINPACK and LAPACK.
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
#    Jack Dongarra, Jim Bunch, Cleve Moler, Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979,
#    ISBN13: 978-0-898711-72-1,
#    LC: QA214.L56.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be positive.
#
#    Input, real A_LU(N,N), the LU factors from R8GE_FA 
#    or R8GE_TRF.
#
#    Input, integer PIVOT(N), as computed by R8GE_FA or R8GE_TRF.
#
#    Output, real DET, the determinant of the matrix.
#
  value = 1.0

  for i in range ( 0, n ):
    value = value * a_lu[i,i]
    if ( pivot[i] != i ):
      value = - value

  return value

def r8ge_det_test ( ):

#*****************************************************************************80
#
## R8GE_DET_TEST tests R8GE_DET.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4
  x = 2.0
  y = 3.0

  print ( '' )
  print ( 'R8GE_DET_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_DET computes the determinant of an R8GE matrix.' )
#
#  Set the matrix.
#
  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = x + y
      else:
        a[i,j] = y
#
#  Factor the matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )
#
#  Compute the determinant.
#
  det = r8ge_det ( n, a_lu, pivot )

  exact = x ** ( n - 1 ) * ( x + n * y )

  print ( '' )
  print ( '  R8GE_DET computes the determinant = %g' % ( det ) )
  print ( '  Exact determinant =                 %g' % ( exact ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_DET_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_dif2 ( m, n ):

#*****************************************************************************80
#
## R8GE_DIF2 returns the DIF2 matrix in R8GE format.
#
#  Example:
#
#    N = 5
#
#    2 -1  .  .  .
#   -1  2 -1  .  .
#    . -1  2 -1  .
#    .  . -1  2 -1
#    .  .  . -1  2
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
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = r8ge_zeros ( m, n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      if ( j == i - 1 ):
        a[i,j] = -1.0
      elif ( j == i ):
        a[i,j] = 2.0
      elif ( j == i + 1 ):
        a[i,j] = -1.0

  return a

def r8ge_dif2_test ( ):

#*****************************************************************************80
#
## R8GE_DIF2_TEST tests R8GE_DIF2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'R8GE_DIF2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_DIF2 returns the second difference matrix.' )

  a = r8ge_dif2 ( m, n )

  r8ge_print ( m, n, a, '  DIF2 matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_DIF2_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_dilu ( m, n, a ):

#*****************************************************************************80
#
## R8GE_DILU produces the diagonal incomplete LU factor of an R8GE matrix.
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
#    R8GE storage is used by LINPACK and LAPACK.
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
#    Input, real A(M,N), the R8GE matrix.
#
#    Output, real D(M), the DILU factor.
#
  import numpy as np

  d = np.zeros ( m, dtype = np.float64 )

  for i in range ( 0, m ):
    if ( i < n ):
      d[i] = a[i,i]

  mn = min ( m, n )

  for i in range ( 0, mn ):
    d[i] = 1.0 / d[i]
    for j in range ( i + 1, mn ):
      d[j] = d[j] - a[j,i] * d[i] * a[i,j]

  return d

def r8ge_dilu_test ( ):

#*****************************************************************************80
#
## R8GE_DILU_TEST tests R8GE_DILU.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  ncol = 3
  nrow = 3
  n = nrow * ncol
  m = n

  print ( '' )
  print ( 'R8GE_DILU_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_DILU returns the DILU factors of an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, nrow * ncol ):
    for j in range ( 0, nrow * ncol ):

      if ( i == j ):
        a[i,j] = 4.0
      elif ( i == j + 1 or i == j - 1 or i == j + nrow or i == j - nrow ):
        a[i,j] = -1.0
      else:
        a[i,j] = 0.0

  r8ge_print ( m, n, a, '  Matrix A:' )
#
#  Compute the incomplete LU factorization.
#
  d = r8ge_dilu ( m, n, a )

  r8vec_print ( m, d, '  DILU factor:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_DILU_TEST:' )
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

  a_lu = r8ge_zeros ( n, n )

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
  print ( '  R8GE_FA computes the LU factors of an R8GE matrix,' )
  print ( '  R8GE_SL solves a factored R8GE system.' )
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
  b = r8ge_mv ( n, n, a, x )
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
  print ( '  R8GE_FA computes the LU factors of an R8GE system,' )
  print ( '  R8GE_SL solves a factored R8GE system.' )
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
  b = r8ge_mv ( n, n, a, x )
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

def r8ge_fs ( n, a, b ):

#*****************************************************************************80
#
## R8GE_FS factors and solves a R8GE system.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    R8GE_FS does not save the LU factors of the matrix, and hence cannot
#    be used to efficiently solve multiple linear systems, or even to
#    factor A at one time, and solve a single linear system at a later time.
#
#    R8GE_FS uses partial pivoting, but no pivot vector is required.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
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
#    Input, real A(N,N), the coefficient matrix of the linear system.
#
#    Input, real B(N), the right hand side of the linear system.
#
#    Output, real X(N), the solution of the linear system.
#
  import numpy as np

  info = 0
  x = b.copy ( )

  for jcol in range ( 0, n ):
#
#  Find the maximum element in column I.
#
    piv = abs ( a[jcol,jcol] )
    ipiv = jcol
    for i in range ( jcol + 1, n ):
      if ( piv < abs ( a[i,jcol] ) ):
        piv = abs ( a[i,jcol] )
        ipiv = i

    if ( piv == 0.0 ):
      info = jcol
      return
#
#  Switch rows JCOL and IPIV, and B.
#
    if ( jcol != ipiv ):

      for j in range ( 0, n ):
        t         = a[jcol,j]
        a[jcol,j] = a[ipiv,j]
        a[ipiv,j] = t

      t       = x[jcol]
      x[jcol] = x[ipiv]
      x[ipiv] = t
#
#  Scale the pivot row.
#
    t = a[jcol,jcol]
    a[jcol,jcol] = 1.0
    for k in range ( jcol + 1, n ):
      a[jcol,k] = a[jcol,k] / t
    x[jcol] = x[jcol] / t
#
#  Use the pivot row to eliminate lower entries in that column.
#
    for i in range ( jcol + 1, n ):
      if ( a[i,jcol] != 0.0 ):
        t = - a[i,jcol]
        a[i,jcol] = 0.0
        for k in range ( jcol + 1, n ):
          a[i,k] = a[i,k] + t * a[jcol,k]
        x[i] = x[i] + t * x[jcol]
#
#  Back solve.
#
  for jcol in range ( n - 1, 0, -1 ):
    for k in range ( 0, jcol ):
      x[k] = x[k] - a[k,jcol] * x[jcol]

  return x

def r8ge_fs_test ( ):

#*****************************************************************************80
#
## R8GE_FS_TEST tests R8GE_FS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8GE_FS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_FS factors and solves a linear system involving' )
  print ( '  an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a, seed = r8ge_random ( n, n, seed )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x )
#
#  Factor and solve the system.
#
  x = r8ge_fs ( n, a, b )
 
  r8vec_print ( n, x, '  Solution:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_FS_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_fss ( n, a, nb, b ):

#*****************************************************************************80
#
## R8GE_FSS factors and solves a R8GE system.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    This routine does not save the LU factors of the matrix, and hence cannot
#    be used to efficiently solve multiple linear systems, or even to
#    factor A at one time, and solve a single linear system at a later time.
#
#    This routine uses partial pivoting, but no pivot vector is required.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 June 2009
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
#    Input, real A(N,N), the coefficient matrix of the linear system.
#
#    Input, integer NB, the number of right hand sides.
#
#    Input, real B(N,NB), the right hand side of the linear system.
#
#    Output, real B(N,NB), the solution of the linear system.
#
  import numpy as np

  info = 0

  for jcol in range ( 0, n ):
#
#  Find the maximum element in column I.
#
    piv = abs ( a[jcol,jcol] )
    ipiv = jcol
    for i in range ( jcol + 1, n ):
      if ( piv < abs ( a[i,jcol] ) ):
        piv = abs ( a[i,jcol] )
        ipiv = i

    if ( piv == 0.0 ):
      info = jcol
      return
#
#  Switch rows JCOL and IPIV, and B.
#
    if ( jcol != ipiv ):

      for j in range ( 0, n ):
        t         = a[jcol,j]
        a[jcol,j] = a[ipiv,j]
        a[ipiv,j] = t

      for j in range ( 0, nb ):
        t         = b[jcol,j]
        b[jcol,j] = b[ipiv,j]
        b[ipiv,j] = t
#
#  Scale the pivot row.
#
    t = a[jcol,jcol]
    a[jcol,jcol] = 1.0
    for k in range ( jcol + 1, n ):
      a[jcol,k] = a[jcol,k] / t
    for k in range ( 0, nb ):
      b[jcol,k] = b[jcol,k] / t
#
#  Use the pivot row to eliminate lower entries in that column.
#
    for i in range ( jcol + 1, n ):
      if ( a[i,jcol] != 0.0 ):
        t = - a[i,jcol]
        a[i,jcol] = 0.0
        for k in range ( jcol + 1, n ):
          a[i,k] = a[i,k] + t * a[jcol,k]
        for k in range ( 0, nb ):
          b[i,k] = b[i,k] + t * b[jcol,k]
#
#  Back solve.
#
  for j in range ( 0, nb ):
    for jcol in range ( n - 1, 0, -1 ):
      for k in range ( 0, jcol ):
        b[k,j] = b[k,j] - a[k,jcol] * b[jcol,j]

  return b

def r8ge_fss_test ( ):

#*****************************************************************************80
#
## R8GE_FSS_TEST tests R8GE_FSS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10
  nb = 3
  seed = 123456789

  print ( '' )
  print ( 'R8GE_FSS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_FSS factors and solves multiple linear systems' )
  print ( '  associated with an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a, seed = r8ge_random ( n, n, seed )
#
#  Set the desired solutions.
#
  x = np.zeros ( [ n, 3 ] )

  for i in range ( 0, n ):
    x[i,0] = 1.0
    x[i,1] = i + 1
    x[i,2] = ( i % 3 ) + 1

  b = r8ge_mm ( n, n, nb, a, x )
#
#  Factor and solve the system.
#
  x = r8ge_fss ( n, a, nb, b )
 
  r8ge_print ( n, nb, x, '  Solution:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_FSS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_hilbert ( m, n ):

#*****************************************************************************80
#
## R8GE_HILBERT returns the Hilbert matrix.
#
#  Formula:
#
#    A(I,J) = 1 / ( I + J - 1 )
#
#  Example:
#
#    N = 5
#
#    1/1 1/2 1/3 1/4 1/5
#    1/2 1/3 1/4 1/5 1/6
#    1/3 1/4 1/5 1/6 1/7
#    1/4 1/5 1/6 1/7 1/8
#    1/5 1/6 1/7 1/8 1/9
#
#  Rectangular Properties:
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#  Square Properties:
#
#    A is positive definite.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is totally positive.
#
#    A is a Cauchy matrix.
#
#    A is nonsingular.
#
#    A is very ill-conditioned.
#
#    The entries of the inverse of A are all integers.
#
#    The sum of the entries of the inverse of A is N*N.
#
#    The ratio of the absolute values of the maximum and minimum
#    eigenvalues is roughly EXP(3.5*N).
#
#    The determinant of the Hilbert matrix of order 10 is
#    2.16417... * 10^(-53).
#
#    If the (1,1) entry of the 5 by 5 Hilbert matrix is changed
#    from 1 to 24/25, the matrix is exactly singular.  And there
#    is a similar rule for larger Hilbert matrices.
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    MD Choi,
#    Tricks or treats with the Hilbert matrix,
#    American Mathematical Monthly,
#    Volume 90, 1983, pages 301-312.
#
#    Robert Gregory, David Karney,
#    Example 3.8,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, New York, 1969, page 33,
#    LC: QA263.G68.
#
#    Nicholas Higham,
#    Accuracy and Stability of Numerical Algorithms,
#    Society for Industrial and Applied Mathematics, Philadelphia, PA,
#    USA, 1996; section 26.1.
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 1, Fundamental Algorithms, Second Edition
#    Addison-Wesley, Reading, Massachusetts, 1973, page 37.
#
#    Morris Newman and John Todd,
#    Example A13,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, 1958, pages 466-476.
#
#    Joan Westlake,
#    Test Matrix A12,
#    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
#    John Wiley, 1968.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = 1.0 / ( i + j + 1 )

  return a

def r8ge_hilbert_test ( ):

#*****************************************************************************80
#
## R8GE_HILBERT_TEST tests R8GE_HILBERT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'R8GE_HILBERT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_HILBERT returns the Hilbert matrix.' )

  a = r8ge_hilbert ( m, n )

  r8ge_print ( m, n, a, '  Hilbert matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_HILBERT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_hilbert_inverse ( n ):

#*****************************************************************************80
#
## R8GE_HILBERT_INVERSE returns the inverse of the Hilbert matrix.
#
#  Formula:
#
#    A(I,J) =  (-1)^(I+J) * (N+I-1)! * (N+J-1)! /
#           [ (I+J-1) * ((I-1)!*(J-1)!)^2 * (N-I)! * (N-J)! ]
#
#  Example:
#
#    N = 5
#
#       25    -300     1050    -1400     630
#     -300    4800   -18900    26880  -12600
#     1050  -18900    79380  -117600   56700
#    -1400   26880  -117600   179200  -88200
#      630  -12600    56700   -88200   44100
#
#  Properties:
#
#    A is symmetric.
#
#    Because A is symmetric, it is normal, so diagonalizable.
#
#    A is almost impossible to compute accurately by general routines
#    that compute the inverse.
#
#    A is integral.
#
#    The sum of the entries of A is N^2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Output, real A(N,N), the inverse Hilbert matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )
#
#  Set the (1,1) entry.
#
  a[0,0] = n * n
#
#  Define Row 1, Column J by recursion on Row 1 Column J-1
#
  i = 0
  for j in range ( 1, n ):
    a[i,j] = - a[i,j-1] * float ( ( n + j ) * ( i + j ) * ( n - j ) ) \
      / float ( ( i + j + 1 ) * j * j )
#
#  Define Row I by recursion on row I-1
#
  for i in range ( 1, n ):
    for j in range ( 0, n ):

      a[i,j] = - a[i-1,j] * float ( ( n + i ) * ( i + j ) * ( n - i ) ) \
        / float ( ( i + j + 1 ) * i * i )

  return a

def r8ge_hilbert_inverse_test ( ):

#*****************************************************************************80
#
## R8GE_HILBERT_INVERSE_TEST tests R8GE_HILBERT_INVERSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 4

  print ( '' )
  print ( 'R8GE_HILBERT_INVERSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_HILBERT_INVERSE computes the inverse of the' )
  print ( '  Hilbert matrix, stored as an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = r8ge_hilbert ( n, n )
  r8ge_print ( n, n, a, '  Matrix A:' )

  b = r8ge_hilbert_inverse ( n )

  r8ge_print ( n, n, b, '  Inverse matrix B:' )
#
#  Check.
#
  c = r8ge_mm ( n, n, n, a, b )

  r8ge_print ( n, n, c, '  Product A * B:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_HILBERT_INVERSE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_house_axh ( n, a, v ):

#*****************************************************************************80
#
## R9GE_HOUSE_AXH computes A*H where H is a compact Householder matrix.
#
#  Discussion:
#
#    The Householder matrix H(V) is defined by
#
#      H(V) = I - 2 * v * v' / ( v' * v )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real A(N,N), the matrix to be postmultiplied.
#
#    Input, real V(N), a vector defining a Householder matrix.
#
#    Output, real AH(N,N), the product A*H.
#
  import numpy as np

  vtv = 0.0
  for i in range ( 0, n ):
    vtv = vtv + v[i] ** 2

  ah = np.zeros ( ( n, n ) )
 
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      ah[i,j] = a[i,j]
      for k in range ( 0, n ):
        ah[i,j] = ah[i,j] - 2.0 * a[i,k] * v[k] * v[j] / vtv
            
  return ah

def r8ge_house_axh_test ( ):

#*****************************************************************************80
#
## R8GE_HOUSE_AXH_TEST tests R8GE_HOUSE_AXH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  n = 5

  print ( '' )
  print ( 'R8GE_HOUSE_AXH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_HOUSE_AXH multiplies a matrix A times a' )
  print ( '  compact Householder matrix.' )

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789

  a, seed = r8ge_random_ab ( n, n, r8_lo, r8_hi, seed )

  r8ge_print ( n, n, a, '  Matrix A:' )
#
#  Request V, the compact form of the Householder matrix H
#  such that H*A packs column 3 of A.
#
  k = 3
  km1 = k - 1
  a_col = np.zeros ( n )
  for i in range ( 0, n ):
    a_col[i] = a[i,km1]

  v = r8vec_house_column ( n, a_col, km1 )

  r8vec_print ( n, v, '  Compact vector V so column 3 of H*A is packed:' )

  h = r8ge_house_form ( n, v )

  r8ge_print ( n, n, h, '  Householder matrix H:' )
#
#  Compute A*H.
#
  ah = r8ge_house_axh ( n, a, v )

  r8ge_print ( n, n, ah, '  Indirect product A*H:' )
#
#  Compare with a direct calculation.
#
  ah = r8ge_mm ( n, n, n, a, h )

  r8ge_print ( n, n, ah, '  Direct product A*H:' )
#
#  Compute H*A to demonstrate packed column 3:
#
  ha = r8ge_mm ( n, n, n, h, a )

  r8ge_print ( n, n, ha, '  H*A should pack column 3:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_HOUSE_AXH_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_house_form ( n, v ):

#*****************************************************************************80
#
## R8GE_HOUSE_FORM constructs a Householder matrix from its compact form.
#
#  Discussion:
#
#    H(v) = I - 2 * v * v' / ( v' * v )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real V(N,1), the vector defining the Householder matrix.
#
#    Output, real H(N,N), the Householder matrix.
#
  import numpy as np

  v_dot_v = 0.0
  for i in range ( 0, n ):
    v_dot_v = v_dot_v + v[i] * v[i]

  c = - 2.0 / v_dot_v

  h = np.zeros ( ( n, n ) )

  for j in range ( 0, n ):
    h[j,j] = 1.0
    for i in range ( 0, n ):
      h[i,j] = h[i,j] + c * v[i] * v[j]
            
  return h

def r8ge_house_form_test ( ):

#*****************************************************************************80
#
## R8GE_HOUSE_FORM_TEST tests R8GE_HOUSE_FORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  v = np.array ( ( 0.0, 0.0, 1.0, 2.0, 3.0 ) )

  print ( '' )
  print ( 'R8GE_HOUSE_FORM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_HOUSE_FORM forms a Householder' )
  print ( '  matrix from its compact form.' )

  r8vec_print ( n, v, '  Compact vector form V:' )

  h = r8ge_house_form ( n, v )
 
  r8ge_print ( n, n, h, '  Householder matrix H:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_HOUSE_FORM_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_identity ( m, n ):

#*****************************************************************************80
#
## R8GE_IDENTITY copies the identity matrix to an R8GE matrix.
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
#    R8GE storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of A.
#
#    Output, real A(M,N), the identity matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0

  return a

def r8ge_identity_test ( ):

#*****************************************************************************80
#
## R8GE_IDENTITY_TEST tests R8GE_IDENTITY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'R8GE_IDENTITY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_IDENTITY returns the identity matrix.' )

  a = r8ge_identity ( m, n )

  r8ge_print ( m, n, a, '  Identity matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_IDENTITY_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_ilu ( m, n, a ):

#*****************************************************************************80
#
## R8GE_ILU produces the incomplete LU factors of a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    The incomplete LU factors of the M by N matrix A are:
#
#      L, an M by M unit lower triangular matrix,
#      U, an M by N upper triangular matrix
#
#    with the property that L and U are computed in the same way as
#    the usual LU factors, except that, whenever an off diagonal element
#    of the original matrix is zero, then the corresponding value of
#    U is forced to be zero.
#
#    This condition means that it is no longer the case that A = L*U.
#
#    On the other hand, L and U will have a simple sparsity structure
#    related to that of A.  The incomplete LU factorization is generally
#    used as a preconditioner in iterative schemes applied to sparse
#    matrices.  It is presented here merely for illustration.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2016
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
#    Input, real A(M,N), the R8GE matrix.
#
#    Output, real L(M,M), the M by M unit lower triangular factor.
#
#    Output, real U(M,N), the M by N upper triangular factor.
#
  import numpy as np

  l = np.zeros ( [ m, m ] )

  for i in range ( 0, m ):
    l[i,i] = 1.0

  u = a.copy ( )

  for j in range ( 0, min ( m - 1, n ) ):
#
#  Zero out the entries in column J, from row J+1 to M.
#
    for i in range ( j + 1, m ):

      if ( u[i,j] != 0.0 ):

        l[i,j] = u[i,j] / u[j,j]
        u[i,j] = 0.0

        for k in range ( j + 1, n ):
          if ( u[i,k] != 0.0 ):
            u[i,k] = u[i,k] - l[i,j] * u[j,k]

  return l, u

def r8ge_ilu_test ( ):

#*****************************************************************************80
#
## R8GE_ILU_TEST tests R8GE_ILU.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  ncol = 3
  nrow = 3
  n = nrow * ncol
  m = n

  print ( '' )
  print ( 'R8GE_ILU_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_ILU returns the ILU factors of an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, nrow * ncol ):
    for j in range ( 0, nrow * ncol ):

      if ( i == j ):
        a[i,j] = 4.0
      elif ( i == j + 1 or i == j - 1 or i == j + nrow or i == j - nrow ):
        a[i,j] = -1.0
      else:
        a[i,j] = 0.0

  r8ge_print ( m, n, a, '  Matrix A:' )
#
#  Compute the incomplete LU factorization.
#
  l, u = r8ge_ilu ( m, n, a )

  r8ge_print ( m, m, l, '  Factor L:' )

  r8ge_print ( m, n, u, '  Factor U:' )

  lu = r8ge_mm ( m, m, n, l, u )

  r8ge_print ( m, n, lu, '  Product L*U:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_ILU_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_indicator ( m, n ):

#*****************************************************************************80
#
## R8GE_INDICATOR sets an R8GE indicator matrix.
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
#    R8GE storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = r8ge_zeros ( m, n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = float ( fac * ( i + 1 ) +  ( j + 1 ) )

  return a

def r8ge_indicator_test ( ):

#*****************************************************************************80
#
## R8GE_INDICATOR_TEST tests R8GE_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'R8GE_INDICATOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_INDICATOR returns the indicator matrix.' )

  a = r8ge_indicator ( m, n )

  r8ge_print ( m, n, a, '  Indicator matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_INDICATOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_inverse ( n, a_lu, pivot ):

#*****************************************************************************80
#
## R8GE_INVERSE computes the inverse of a matrix factored by R8GE_FA.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    R8GE_INVERSE is a simplified standalone version of the LINPACK routine
#    R8GEDI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix A.
#
#    Input, real A_LU(N,N), the factor information computed by R8GE_FA.
#
#    Input, integer PIVOT(N), the pivot vector from R8GE_FA.
#
#    Output, real A_INVERSE(N,N), the inverse matrix.
#
  import numpy as np

  a_inverse = a_lu.copy ( )
#
#  Compute Inverse(U).
#
  for k in range ( 0, n ):

    a_inverse[k,k] = 1.0 / a_inverse[k,k]
    for i in range ( 0, k ):
      a_inverse[i,k] = -a_inverse[i,k] * a_inverse[k,k]

    for j in range ( k + 1, n ):

      temp = a_inverse[k,j]
      a_inverse[k,j] = 0.0
      for i in range ( 0, k + 1 ):
        a_inverse[i,j] = a_inverse[i,j] + a_inverse[i,k] * temp
#
#  Form Inverse(U) * Inverse(L).
#
  work = np.zeros ( n )

  for k in range ( n - 2, -1, -1 ):

    for i in range ( k + 1, n ):
      work[i] = a_inverse[i,k]
      a_inverse[i,k] = 0.0

    for j in range ( k + 1, n ):
      for i in range ( 0, n ):
        a_inverse[i,k] = a_inverse[i,k] + a_inverse[i,j] * work[j]

    if ( pivot[k] != k ):

      for i in range ( 0, n ):
        t                     = a_inverse[i,k]
        a_inverse[i,k]        = a_inverse[i,pivot[k]]
        a_inverse[i,pivot[k]] = t

  return a_inverse

def r8ge_inverse_test ( ):

#*****************************************************************************80
#
## R8GE_INVERSE_TEST tests R8GE_INVERSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 March 2009
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 4
  x = 2.0
  y = 3.0

  print ( '' )
  print ( 'R8GE_INVERSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_INVERSE computes the inverse of an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      if ( i == j ):
        a[i,i] = x + y
      else:
        a[i,j] = y

  r8ge_print ( n, n, a, '  Matrix A:' )
#
#  Factor and invert the matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_INVERSE_TEST - Fatal error!' )
    print ( '  R8GE_FA reports the matrix is singular.' )
    return

  a_inverse = r8ge_inverse ( n, a_lu, pivot )

  r8ge_print ( n, n, a_inverse, '  Inverse matrix B:' )
#
#  Check.
#
  c = r8ge_mm ( n, n, n, a, a_inverse )

  r8ge_print ( n, n, c, '  Product matrix:' )

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

  b = x.copy ( )

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

def r8ge_ml_test ( ):

#*****************************************************************************80
#
## R8GE_ML_TEST tests R8GE_ML.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8GE_ML_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_ML computes A*x or A\'*X' )
  print ( '  where A has been factored by R8GE_FA.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  for job in range ( 0, 2 ):
#
#  Set the matrix.
#
    a, seed = r8ge_random ( n, n, seed )
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
    if ( job == 0 ):
      b = r8ge_mv ( n, n, a, x )
    else:
      b = r8ge_mtv ( n, n, a, x )
#
#  Factor the matrix.
#
    a_lu, pivot, info = r8ge_fa ( n, a )

    if ( info != 0 ):
      print ( '' )
      print ( 'R8GE_ML_TEST - Fatal error!' )
      print ( '  R8GE_FA declares the matrix is singular!' )
      print ( '  The value of INFO is %d,' % ( info ) )
      return
#
#  Now multiply factored matrix times solution to get right hand side again.
#
    b2 = r8ge_ml ( n, a_lu, pivot, x, job )

    if ( job == 0 ):
      r8vec2_print_some ( n, b, b2, 10, '  A*x and PLU*x' )
    else:
      r8vec2_print_some ( n, b, b2, 10, '  A\'*x and (PLU)\'*x' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_ML_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_mm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## R8GE_MM multiplies two R8GE's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N1, N2, N3, the order of the matrices.
#
#    Input, real A(N1,N2), B(N2,N3), the matrices to multiply.
#
#    Output, real  C(N1,N3), the product matrix C = A * B.
#
  import numpy as np

  c = r8ge_zeros ( n1, n3 )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]

  return c

def r8ge_mm_test ( ):

#*****************************************************************************80
#
## R8GE_MM_TEST tests R8GE_MM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'R8GE_MM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_MM computes a matrix-matrix product C = A * B;' )

  a = r8ge_zeros ( n1, n2 )

  for i in range ( 0, n1 ): 
    for j in range ( 0, n2 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = np.transpose ( a )

  c = r8ge_mm ( n1, n2, n3, a, b )

  r8ge_print ( n1, n2, a, '  A:' )
  r8ge_print ( n2, n3, b, '  B:' )
  r8ge_print ( n1, n3, c, '  C = A*B:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_MM_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_mtm ( n1, n2, n3, a, b ):

#*****************************************************************************80
#
## R8GE_MTM computes A' * B for two R8GE's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N1, N2, N3, the order of the matrices.
#
#    Input, real A(N2,N1), B(N2,N3), the matrices to multiply.
#
#    Output, real  C(N1,N3), the product matrix C = A' * B.
#
  import numpy as np

  c = r8ge_zeros ( n1, n3 )

  for j in range ( 0, n3 ):
    for i in range ( 0, n1 ):
      for k in range ( 0, n2 ):
        c[i,j] = c[i,j] + a[k,i] * b[k,j]

  return c

def r8ge_mtm_test ( ):

#*****************************************************************************80
#
## R8GE_MTM_TEST tests R8GE_MTM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 Augsut 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n1 = 4
  n2 = 3
  n3 = n1

  print ( '' )
  print ( 'R8GE_MTM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_MTM computes a matrix-matrix product C = A\' * B;' )

  a = r8ge_zeros ( n2, n1 )

  for i in range ( 0, n2 ): 
    for j in range ( 0, n1 ):
 
      if ( j == 0 ):
        a[i,j] = 1.0
      elif ( i == 0 ):
        a[i,j] = 0.0
      else:
        a[i,j] = a[i-1,j-1] + a[i-1,j]

  b = a

  c = r8ge_mtm ( n1, n2, n3, a, b )

  r8ge_print ( n2, n1, a, '  A:' )
  r8ge_print ( n2, n3, b, '  B:' )
  r8ge_print ( n1, n3, c, '  C = A\'*B:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_MTM_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## R8GE_MTV multiplies a vector by a R8GE matrix.
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
#    06 September 2015
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
#    Input, real X(M), the vector to be multiplied by A.
#
#    Output, real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      b[j] = b[j] + x[i] * a[i,j]

  return b

def r8ge_mtv_test ( ):

#*****************************************************************************80
#
## R8GE_MTV_TEST tests R8GE_MTV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8GE_MTV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_MTV computes a matrix product b=A\'*x for an R8GE matrix.' )

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

    a = r8ge_indicator ( m, n )
    r8ge_print ( m, n, a, '  The matrix A:' )

    x = r8vec_indicator1 ( m )
    r8vec_print ( m, x, '  The vector x:' )

    b = r8ge_mtv ( m, n, a, x )
    r8vec_print ( n, b, '  The vector b=A\'*x:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_MTV_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_mu ( m, n, a_lu, trans, pivot, x ):

#*****************************************************************************80
#
## R8GE_MU computes A * x or A' * x, using R8GE_TRF factors.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    It is assumed that R8GE_TRF has overwritten the original matrix
#    information by PLU factors.  R8GE_MU is able to reconstruct the
#    original matrix from the PLU factor data.
#
#    R8GE_MU allows the user to check that the solution of a linear
#    system is correct, without having to save an unfactored copy
#    of the matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Anderson, Bai, Bischof, Demmel, Dongarra, Du Croz, Greenbaum,
#    Hammarling, McKenney, Ostrouchov, Sorensen,
#    LAPACK User's Guide,
#    Second Edition,
#    SIAM, 1995.
#
#  Parameters:
#
#    Input, integer M, the number of rows in the matrix.
#
#    Input, integer N, the number of columns in the matrix.
#
#    Input, real A_LU(M,N), the LU factors from R8GE_TRF.
#
#    Input, character TRANS, specifies the form of the system of equations:
#    'N':  A * x = b  (No transpose)
#    'T':  A'* X = B  (Transpose)
#    'C':  A'* X = B  (Conjugate transpose = Transpose)
#
#    Input, integer PIVOT(*), the pivot vector computed by R8GE_TRF.
#
#    Input, real X(*), the vector to be multiplied.
#    For the untransposed case, X should have N entries.
#    For the transposed case, X should have M entries.
#
#    Output, real B(*), the result of the multiplication.
#    For the untransposed case, B should have M entries.
#    For the transposed case, B should have N entries.
#
  import numpy as np
  from sys import exit

  npiv = min ( m - 1, n )
  mn_max = max ( m, n )

  if ( trans == 'n' or trans == 'N' ):
#
#  Y[MN] = U[MNxN] * X[N].
#
    b = np.zeros ( m )
    y = np.zeros ( n )

    for j in range ( 0, n ):

      for i in range ( 0, min ( j + 1, m ) ):
        y[i] = y[i] + a_lu[i,j] * x[j]
#
#  Z[M] = L[MxMN] * Y[MN] = L[MxMN] * U[MNxN] * X[N].
#
    for i in range ( 0, m ):

      if ( i <= n - 1 ):
        b[i] = y[i]
      else:
        b[i] = 0.0

    for j in range ( min ( m - 2, n - 1 ), -1, -1 ):
      for i in range ( j + 1, m ):
        b[i] = b[i] + a_lu[i,j] * y[j]
#
#  B = P * Z = P * L * Y = P * L * U * X = A * x.
#
    for j in range ( npiv - 1, -1, -1 ):

      k = pivot[j]

      if ( k != j ):
        t    = b[k]
        b[k] = b[j]
        b[j] = t

  elif ( trans == 't' or trans == 'T' or trans == 'c' or trans == 'C' ):

    b = np.zeros ( n )
#
#  Y = transpose(P) * X:
#
    for i in range ( 0, npiv ):

      k = pivot[i]

      if ( k != i ):
        t    = x[k]
        x[k] = x[i]
        x[i] = t

    for i in range ( 0, n ):

      if ( i <= m - 1 ):
        b[i] = x[i]
      else:
        b[i] = 0.0
#
#  Z = tranpose(L) * Y:
#
    for j in range ( 0, min ( m - 1, n ) ):
      for k in range ( j + 1, m ):
        b[j] = b[j] + x[k] * a_lu[k,j]
#
#  B = U' * Z.
#
    for i in range ( m - 1, -1, -1 ):
      for j in range ( i + 1, n ):
        b[j] = b[j] + b[i] * a_lu[i,j]
      if ( i <= n - 1 ):
        b[i] = b[i] * a_lu[i,i]
#
#  Now restore X.
#
    for i in range ( npiv - 1, -1, -1 ):

      k = pivot[i]

      if ( k != i ):
        t    = x[k]
        x[k] = x[i]
        x[i] = t

  else:

    print ( '' )
    print ( 'R8GE_MU - Fatal error!' )
    print ( '  Illegal value of TRANS = %c' % ( trans ) )
    exit ( 'R8GE_MU - Fatal error!' )

  return b

def r8ge_mu_test ( ):

#*****************************************************************************80
#
## R8GE_MU_TEST tests R8GE_MU.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 3
  seed = 123456789

  print ( '' )
  print ( 'R8GE_MU_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_MU computes A*x or A\'*X' )
  print ( '  where A has been factored by R8GE_TRF.' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )

  for job in range ( 0, 2 ):

    if ( job == 0 ):
      trans = 'N'
    else:
      trans = 'T'
#
#  Set the matrix.
#
    amn, seed = r8ge_random ( m, n, seed )

    if ( job == 0 ):

      xn = r8vec_indicator1 ( n )

      cm = r8ge_mv ( m, n, amn, xn )

    else:

      xm = r8vec_indicator1 ( m )

      cn = r8ge_mtv ( m, n, amn, xm )
#
#  Factor the matrix.
#
    amn_lu, pivot, info = r8ge_trf ( m, n, amn )

    if ( info != 0 ):
      print ( '' )
      print ( 'R8GE_MU_TEST - Fatal error!' )
      print ( '  R8GE_TRF declares the matrix is singular!' )
      print ( '  The value of INFO is %d' % ( info ) )
      continue
#
#  Now multiply the factored matrix times solution to get right hand side again.
#
    if ( job == 0 ):

      bm = r8ge_mu ( m, n, amn_lu, trans, pivot, xn )

      r8vec2_print_some ( m, cm, bm, 10, '  A*x and PLU*x' )

    else:

      bn = r8ge_mu ( m, n, amn_lu, trans, pivot, xm )

      r8vec2_print_some ( n, cn, bn, 10, '  A\'*x and (PLU)\'*x' )

  print ( '' )
  print ( '  Matrix is %d by %d' % ( n, m ) )

  for job in range ( 0, 2 ):

    if ( job == 0 ):
      trans = 'N'
    else:
      trans = 'T'
#
#  Set the matrix.
#
    anm, seed = r8ge_random ( n, m, seed )

    if ( job == 0 ):

      xm = r8vec_indicator1 ( m )

      cn = r8ge_mv ( n, m, anm, xm )

    else:

      xn = r8vec_indicator1 ( n )

      cm = r8ge_mtv ( n, m, anm, xn )
#
#  Factor the matrix.
#
    anm_lu, pivot, info = r8ge_trf ( n, m, anm )

    if ( info != 0 ):
      print ( '' )
      print ( 'R8GE_MU_TEST - Fatal error!' )
      print ( '  R8GE_TRF declares the matrix is singular!' )
      print ( '  The value of INFO is %d' % ( info ) )
      continue
#
#  Now multiply factored matrix times solution to get right hand side again.
#
    if ( job == 0 ):

      bn = r8ge_mu ( n, m, anm_lu, trans, pivot, xm )

      r8vec2_print_some ( n, cn, bn, 10, '  A*x and PLU*x' )

    else:

      bm = r8ge_mu ( n, m, anm_lu, trans, pivot, xn )

      r8vec2_print_some ( m, cm, bm, 10, '  A\'*x and (PLU)\'*x' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_MU_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_mv ( m, n, a, x ):

#*****************************************************************************80
#
## R8GE_MV multiplies an R8GE matrix times a vector.
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

def r8ge_mv_test ( ):

#*****************************************************************************80
#
## R8GE_MV_TEST tests R8GE_MV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'R8GE_MV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_MV computes a matrix product b=A*x for an R8GE matrix.' )

  a = r8ge_indicator ( m, n )
  r8ge_print ( m, n, a, '  The matrix A:' )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  The vector X:' )

  b = r8ge_mv ( m, n, a, x )
  r8vec_print ( n, b, '  The vector b=A*x:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_MV_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_orth_random ( n, key ):

#*****************************************************************************80
#
## R8GE_ORTH_RANDOM returns a random orthogonal matrix.
#
#  Properties:
#
#    The inverse of A is equal to A'.
#
#    A is orthogonal: A * A'  = A' * A = I.
#
#    Because A is orthogonal, it is normal: A' * A = A * A'.
#
#    Columns and rows of A have unit Euclidean norm.
#
#    Distinct pairs of columns of A are orthogonal.
#
#    Distinct pairs of rows of A are orthogonal.
#
#    The L2 vector norm of A*x = the L2 vector norm of x for any vector x.
#
#    The L2 matrix norm of A*B = the L2 matrix norm of B for any matrix B.
#
#    det ( A ) = +1 or -1.
#
#    A is unimodular.
#
#    All the eigenvalues of A have modulus 1.
#
#    All singular values of A are 1.
#
#    All entries of A are between -1 and 1.
#
#  Discussion:
#
#    Thanks to Eugene Petrov, B I Stepanov Institute of Physics,
#    National Academy of Sciences of Belarus, for convincingly
#    pointing out the severe deficiencies of an earlier version of
#    this routine.
#
#    Essentially, the computation involves saving the Q factor of the
#    QR factorization of a matrix whose entries are normally distributed.
#    However, it is only necessary to generate this matrix a column at
#    a time, since it can be shown that when it comes time to annihilate
#    the subdiagonal elements of column K, these (transformed) elements of
#    column K are still normally distributed random values.  Hence, there
#    is no need to generate them at the beginning of the process and
#    transform them K-1 times.
#
#    For computational efficiency, the individual Householder transformations
#    could be saved, as recommended in the reference, instead of being
#    accumulated into an explicit matrix format.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Pete Stewart,
#    Efficient Generation of Random Orthogonal Matrices With an Application
#    to Condition Estimators,
#    SIAM Journal on Numerical Analysis,
#    Volume 17, Number 3, June 1980, pages 403-409.
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
#
#  Start with A = the identity matrix.
#
  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    a[i,i] = 1.0
#
#  Now behave as though we were computing the QR factorization of
#  some other random matrix.  Generate the N elements of the first column,
#  compute the Householder matrix H1 that annihilates the subdiagonal elements,
#  and set A := A * H1' = A * H.
#
#  On the second step, generate the lower N-1 elements of the second column,
#  compute the Householder matrix H2 that annihilates them,
#  and set A := A * H2' = A * H2 = H1 * H2.
#
#  On the N-1 step, generate the lower 2 elements of column N-1,
#  compute the Householder matrix HN-1 that annihilates them, and
#  and set A := A * H(N-1)' = A * H(N-1) = H1 * H2 * ... * H(N-1).
#  This is our random orthogonal matrix.
#
  x_col = np.zeros ( n )
 
  seed = key

  for j in range ( 0, n - 1 ):

    for i in range ( 0, j ):
      x_col[i] = 0.0

    for i in range ( j, n ):
      x_col[i], seed = r8_normal_01 ( seed )
#
#  Compute the vector V that defines a Householder transformation matrix
#  H(V) that annihilates the subdiagonal elements of X.
#
    v = r8vec_house_column ( n, x_col, j )
#
#  Postmultiply the matrix A by H'(V) = H(V).
#
    a = r8ge_house_axh ( n, a, v )

  return a

def r8ge_orth_random_test ( ):

#*****************************************************************************80
#
## R8GE_ORTH_RANDOM_TEST tests R8GE_ORTH_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8GE_ORTH_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_ORTH_RANDOM computes a random orthogonal matrix.' )

  m = 5
  n = m
  key = 123456789

  a = r8ge_orth_random ( n, key )

  r8ge_print ( m, n, a, '  ORTH_RANDOM matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_ORTH_RANDOM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_pds_random ( n, key ):

#*****************************************************************************80
#
## R8GE_PDS_RANDOM returns a random positive definite symmetric matrix.
#
#  Discussion:
#
#    The matrix returned will have eigenvalues in the range [0,1].
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    A is positive definite: 0 < x'*A*x for nonzero x.
#
#    The eigenvalues of A will be real.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, integer KEY, a positive value that selects the data.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
#
#  Get a random set of eigenvalues.
#
  seed = key
  lam, seed = r8vec_uniform_01 ( n, seed )
#
#  Get a random orthogonal matrix Q.
#
  q = r8ge_orth_random ( n, key )
#
#  Set A = Q * Lambda * Q'.
#
  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      for k in range ( 0, n ):
        a[i,j] = a[i,j] + q[i,k] * lam[k] * q[j,k]

  return a

def r8ge_pds_random_test ( ):

#*****************************************************************************80
#
## R8GE_PDS_RANDOM_TEST tests R8GE_PDS_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8GE_PDS_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_PDS_RANDOM computes the PDS_RANDOM matrix.' )

  n = 5
  key = 123456789
  a = r8ge_pds_random ( n, key )

  r8ge_print ( n, n, a, '  PDS_RANDOM matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_PDS_RANDOM_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_plu ( m, n, a ):

#*****************************************************************************80
#
## R8GE_PLU produces the PLU factors of a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    The PLU factors of the M by N matrix A are:
#
#      P, an M by M permutation matrix P,
#      L, an M by M unit lower triangular matrix,
#      U, an M by N upper triangular matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
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
#    Input, real A(M,N), the R8GE matrix.
#
#    Output, real P(M,M), the M by M permutation factor.
#
#    Output, real L(M,M), the M by M unit lower triangular factor.
#
#    Output, real U(M,N), the M by N upper triangular factor.
#
  l = r8ge_identity ( m, m )
  p = r8ge_identity ( m, m )
  u = a.copy ( )
#
#  On step J, find the pivot row and the pivot value.
#
  for j in range ( 0, min ( m - 1, n ) ):

    pivot_value = 0.0
    pivot_row = -1

    for i in range ( j, m ):

      if ( pivot_value < abs ( u[i,j] ) ):
        pivot_value = abs ( u[i,j] )
        pivot_row = i
#
#  If the pivot row is nonzero, swap rows J and PIVOT_ROW.
#
    if ( pivot_row != -1 ):

      for k in range ( 0, n ):
        t = u[j,k]
        u[j,k] = u[pivot_row,k]
        u[pivot_row,k] = t

      for k in range ( 0, m ):
        t = l[j,k]
        l[j,k] = l[pivot_row,k]
        l[pivot_row,k] = t

      for k in range ( 0, m ):
        t = l[k,j]
        l[k,j] = l[k,pivot_row]
        l[k,pivot_row] = t

      for k in range ( 0, m ):
        t = p[k,j]
        p[k,j] = p[k,pivot_row]
        p[k,pivot_row] = t
#
#  Zero out the entries in column J, from row J+1 to M.
#
      for i in range ( j + 1, m ):

        if ( u[i,j] != 0.0 ):

          l[i,j] = u[i,j] / u[j,j]
          u[i,j] = 0.0
          for k in range ( j + 1, n ):
            u[i,k] = u[i,k] - l[i,j] * u[j,k]

  return p, l, u

def r8ge_plu_test ( ):

#*****************************************************************************80
#
## R8GE_PLU_TEST tests R8GE_PLU.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4
  seed = 123456789
  
  print ( '' )
  print ( 'R8GE_PLU_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_PLU returns the PLU factors of an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )

  a, seed = r8ge_random ( m, n, seed )

  r8ge_print ( m, n, a, '  Matrix A:' )
#
#  Compute the PLU factors.
#
  p, l, u = r8ge_plu ( m, n, a )

  r8ge_print ( m, m, p, '  Factor P:' )

  r8ge_print ( m, m, l, '  Factor L:' )

  r8ge_print ( m, n, u, '  Factor U:' )

  lu = r8ge_mm ( m, m, n, l, u )
  plu = r8ge_mm ( m, m, n, p, lu )
        
  r8ge_print ( m, n, plu, '  Product P*L*U:')
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_PLU_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_poly ( n, a ):

#*****************************************************************************80
#
## R8GE_POLY computes the characteristic polynomial of a R8GE matrix.
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
#    07 February 2016
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
#    Input, real A(N,N), the R8GE matrix.
#
#    Output, real P(1:N+1), the coefficients of the characteristic
#    polynomial of A.  P(I+1) contains the coefficient of X**I.
#
  import numpy as np
#
#  Initialize WORK1 to the identity matrix.
#
  work1 = r8ge_identity ( n, n )

  p = np.zeros ( n + 1 )
  p[n] = 1.0

  for order in range ( n - 1, -1, -1 ):
#
#  Work2 = A * WORK1.
#
    work2 = r8ge_mm ( n, n, n, a, work1 )
#
#  Take the trace.
#
    trace = 0.0
    for i in range ( 0, n ):
      trace = trace + work2[i,i]
#
#  P(ORDER) = -Trace ( WORK2 ) / ( N - ORDER )
#
    p[order] = - trace / ( n - order )
#
#  WORK1 := WORK2 + P(ORDER) * Identity.
#
    work1 = work2.copy ( )

    for i in range ( 0, n ):
      work1[i,i] = work1[i,i] + p[order]

  return p

def r8ge_poly_test ( ):

#*****************************************************************************80
#
## R8GE_POLY_TEST tests R8GE_POLY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 12

  print ( '' )
  print ( 'R8GE_POLY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_POLY computes the characteristic polynomial of an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  p_true = np.array ( [ \
         1.0,    -23.0,    231.0,  -1330.0,   4845.0, \
    -11628.0,  18564.0, -19448.0,  12870.0,  -5005.0, \
      1001.0,    -78.0,      1.0 ] )
#
#  Set the matrix.
#
  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = float ( min ( i, j ) + 1 )
#
#  Get the characteristic polynomial.
#
  p = r8ge_poly ( n, a )
#
#  Compare.
#
  r8vec2_print_some ( n+1, p, p_true, 10, 'I, P(I), True P(I)' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_POLY_TEST:' )
  print ( '  Normal end of execution.' )
  return

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

def r8ge_print_test ( ):

#*****************************************************************************80
#
## R8GE_PRINT_TEST tests R8GE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8GE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_PRINT prints an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print ( m, n, v, '  Here is an R8GE:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
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
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row', end = '' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8ge_print_some_test ( ):

#*****************************************************************************80
#
## R8GE_PRINT_SOME_TEST tests R8GE_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8GE_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_PRINT_SOME prints some of an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print_some ( m, n, v, 0, 3, 2, 5, '  Rows 0:2, Cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
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
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8GE_RANDOM - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8GE_RANDOM - Fatal error!' )

  r = r8ge_zeros ( m, n )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = seed * 4.656612875E-10

  return r, seed

def r8ge_random_test ( ):

#*****************************************************************************80
#
## R8GE_RANDOM_TEST tests R8GE_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 February 2016
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
  print ( 'R8GE_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_RANDOM computes a random R8GE.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8ge_random ( m, n, seed )

  r8ge_print ( m, n, v, '  Random R8GE:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_RANDOM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_random_ab ( m, n, a, b, seed ):

#*****************************************************************************80
#
## R8GE_RANDOM_AB returns a scaled pseudorandom R8GE.
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
#    20 August 2015
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

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8GE_RANDOM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8GE_RANDOM_AB - Fatal error!' )

  r = np.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r8ge_random_ab_test ( ):

#*****************************************************************************80
#
## R8GE_RANDOM_AB_TEST tests R8GE_RANDOM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    20 August 2015
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
  print ( 'R8GE_RANDOM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_RANDOM_AB computes a random R8GE.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8ge_random_ab ( m, n, a, b, seed )

  r8ge_print ( m, n, v, '  Random R8GE:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_RANDOM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_res ( m, n, a, x, b ):

#*****************************************************************************80
#
## R8GE_RES computes the residual vector for an R8GE system.
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
#    R8GE storage is used by LINPACK and LAPACK.
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
#    Input, integer M, N, the number of rows and columns of 
#    the matrix.  M and N must be positive.
#
#    Input, real A(M,N), the original, UNFACTORED R8GE matrix.
#
#    Input, real X(N), the estimated solution.
#
#    Input, real B(M), the right hand side vector.
#
#    Output, real R(M), the residual vector, b - A * x.
#
  import numpy as np

  r = np.zeros ( m )

  for i in range ( 0, m ):
    r[i] = b[i]
    for j in range ( 0, n ):
      r[i] = r[i] - a[i,j] * x[j]

  return r

def r8ge_res_test ( ):

#*****************************************************************************80
#
## R8GE_RES_TEST tests R8GE_RES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8GE_RES_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_RES computes b-A*x, where A is an R8GE matrix.' )
  print ( '  We check three cases, M<N, M=N, M>N.' )

  for i in range ( 0, 3 ):

    if ( i == 0 ):
      m = 3
      n = 5
    elif ( i == 1 ):
      m = 5
      n = 5
    elif ( i == 2 ):
      m = 5
      n = 3

    seed = 123456789
    a, seed = r8ge_random ( m, n, seed )
    x = r8vec_indicator1 ( n )
    b = r8ge_mv ( m, n, a, x )
    r = r8ge_res ( m, n, a, x, b )
    r8vec_print ( m, r, '  Residual A*x-b:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_RES_TEST:' )
  print ( '  Normal end of execution.' )
  return

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

def r8ge_sl_test ( ):

#*****************************************************************************80
#
## R8GE_SL_TEST tests R8GE_SL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2016
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
  print ( 'R8GE_SL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_SL solves a linear system A*x=b that was factored' )
  print ( '  by R8GE_FA.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a, seed = r8ge_random ( n, n, seed )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x )
#
#  Factor the matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_SL_TEST - Fatal error!' )
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
  x = np.ones ( n )
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
  x = r8vec_indicator1 ( n )
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
  print ( 'R8GE_SL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_sl_it ( n, a, a_lu, pivot, b, job, x ):

#*****************************************************************************80
#
## R8GE_SL_IT applies one step of iterative refinement following R8GE_SL.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    It is assumed that:
#
#    * the original matrix A has been factored by R8GE_FA
#    * the linear system A * x = b has been solved once by R8GE_SL.
#
#    (Actually, it is not necessary to solve the system once using R8GE_SL.
#    You may simply supply the initial estimated solution X = 0.)
#
#    Each time this routine is called, it will compute the residual in
#    the linear system, apply one step of iterative refinement, and
#    add the computed correction to the current solution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
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
#    Input, real A(N,N), the original, UNFACTORED R8GE matrix.
#
#    Input, real A_LU(N,N), the LU factors from R8GE_FA.
#
#    Input, integer PIVOT(N), the pivot vector from R8GE_FA.
#
#    Input, real B(N), the right hand side vector.
#
#    Input, integer JOB, specifies the operation.
#    0, solve A*X=B.
#    nonzero, solve A'*X=B.
#
#    Input, real X(N), an estimate of the solution of A * x = b.
#
#    Output, real X(N), an improved estimate of the solution.
#
#    Output, real DX(N), contains the correction terms added to X.
#

#
#  Compute the residual vector.
#
  r = r8ge_res ( n, n, a, x, b )
#
#  Solve A * dx = r
#
  dx = r8ge_sl ( n, a_lu, pivot, r, job )
#
#  Add dx to x.
#
  for i in range ( 0, n ):
    x[i] = x[i] + dx[i]

  return x, dx

def r8ge_sl_it_test ( ):

#*****************************************************************************80
#
## R8GE_SL_IT_TEST tests R8GE_SL_IT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 6

  print ( '' )
  print ( 'R8GE_SL_IT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_SL_IT applies one step of iterative' )
  print ( '  refinement to a R8GE_SL solution.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the coefficient matrix.
#
  a = r8ge_hilbert_inverse ( n )
#
#  Set the right hand side b.
#
  b = np.zeros ( n )
  b[n-1] = 1.0
#
#  Compute the factored coefficient matrix.
#
  a_lu, pivot, info = r8ge_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_SL_IT_TEST - Fatal error!' )
    print ( '  R8GE_FA declares the matrix is singular!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return
#
#  Solve the system.
#
  job = 1
  x = r8ge_sl ( n, a_lu, pivot, b, job )
#
#  Compute and print the residual.
#
  r = r8ge_res ( n, n, a, x, b )

  r8vec2_print_some ( n, x, r, 10, '  i, x, b-A*x' )
#
#  Take a few steps of iterative refinement.
#
  for j in range ( 1, 6 ):

    print ( '' )
    print ( 'Iterative refinement step %d' % ( j ) )
#
#  Improve the solution.
#
    x_new, r = r8ge_sl_it ( n, a, a_lu, pivot, b, job, x )

    r8vec_print_some ( n, r, 10, '  I, DX:' )
#
#  Compute and print the residual.
#
    r = r8ge_res ( n, n, a, x_new, b )

    r8vec2_print_some ( n, x_new, r, 10, '  i, x, b-A*x' )

    x = x_new.copy ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_SL_IT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_to_r8gb ( m, n, ml, mu, a ):

#*****************************************************************************80
#
## R8GE_TO_R8GB copies a R8GE matrix to a R8GB matrix.
#
#  Discussion:
#
#    It usually doesn't make sense to try to store a general matrix
#    in a band matrix format.  You can always do it, but it will take
#    more space, unless the general matrix is actually banded.
#
#    The purpose of this routine is to allow a user to set up a
#    banded matrix in the easy-to-use general format, and have this
#    routine take care of the compression of the data into general
#    format.  All the user has to do is specify the bandwidths.
#
#    Note that this routine "believes" what the user says about the
#    bandwidth.  It will assume that all entries in the general matrix
#    outside of the bandwidth are zero.
#
#    The original M by N matrix is "collapsed" downward, so that diagonals
#    become rows of the storage array, while columns are preserved.  The
#    collapsed array is logically 2*ML+MU+1 by N.
#
#    The R8GB storage format is for an M by N banded matrix, with lower
#    bandwidth ML and upper bandwidth MU.  Storage includes room for ML
#    extra superdiagonals, which may be required to store nonzero entries
#    generated during Gaussian elimination.
#
#    LINPACK and LAPACK band storage requires that an extra ML
#    superdiagonals be supplied to allow for fillin during Gauss
#    elimination.  Even though a band matrix is described as
#    having an upper bandwidth of MU, it effectively has an
#    upper bandwidth of MU+ML.  This routine will copy nonzero
#    values it finds in these extra bands, so that both unfactored
#    and factored matrices can be handled.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Anderson, Bai, Bischof, Demmel, Dongarra, Du Croz, Greenbaum,
#    Hammarling, McKenney, Ostrouchov, Sorensen,
#    LAPACK User's Guide,
#    Second Edition,
#    SIAM, 1995.
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrices.
#    M must be positive.
#
#    Input, integer N, the number of columns of the matrices.
#    N must be positive.
#
#    Input, integer ML, MU, the lower and upper bandwidths of the matrix.
#    ML and MU must be nonnegative, and no greater than min(M,N)-1.
#
#    Input, real A(M,N), the R8GE matrix.
#
#    Output, real B(2*ML+MU+1,N), the R8GB matrix.
#
  import numpy as np

  b = np.zeros ( [ 2*ml+mu+1, n ] )

  for i in range ( 1, m + 1 ):
    jlo = max ( i - ml, 1 )
    jhi = min ( i + mu, n )
    for j in range ( jlo, jhi + 1 ):
      b[ml+mu+i-j,j-1] = a[i-1,j-1]

  return b

def r8ge_to_r8gb_test ( ):

#*****************************************************************************80
#
## R8GE_TO_R8GB_TEST tests R8GE_TO_R8GB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 July 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8gb import r8gb_print

  m = 5
  n = 5
  ml = 2
  mu = 1
  seed = 123456789

  print ( '' )
  print ( 'R8GE_TO_R8GB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_TO_R8GB converts an R8GE matrix to R8GB format.' )
  print ( '' )
  print ( '  Matrix order M = %d, N = %d' % ( m, n ) )
  print ( '  R8GB bands ML = %d, MU = %d' % ( ml, mu ) )

  a, seed = r8ge_random ( m, n, seed )

  r8ge_print ( m, n, a, '  The random R8GE matrix:' )
 
  b = r8ge_to_r8gb ( m, n, ml, mu, a )

  r8gb_print ( m, n, ml, mu, b, '  The R8GB matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_TO_R8GB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_to_r8lt ( m, n, a_ge ):

#*****************************************************************************80
#
## R8GE_TO_R8LT copies an R8GE matrix to an R8LT matrix.
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
#    The R8LT storage format is used for an M by N lower triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, real A_GE(M,N), the R8GE matrix.
#
#    Output, real A_LT(M,N), the R8LT matrix.
#
  import numpy as np

  a_lt = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( j, m ):
      a_lt[i,j] = a_ge[i,j]

  return a_lt

def r8ge_to_r8lt_test ( ):

#*****************************************************************************80
#
## R8GE_TO_R8LT_TEST tests R8GE_TO_R8LT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8lt import r8lt_print

  m = 5
  n = 4
  seed = 123456789

  print ( '' )
  print ( 'R8GE_TO_R8LT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_TO_R8LT converts an R8GE matrix to R8LT format.' )

  a_ge, seed = r8ge_random ( m, n, seed )

  r8ge_print ( m, n, a_ge, '  The random R8GE matrix:' )
 
  a_lt = r8ge_to_r8lt ( m, n, a_ge )

  r8lt_print ( m, n, a_lt, '  The R8LT matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_TO_R8LT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_to_r8po ( n, a ):

#*****************************************************************************80
#
## R8GE_TO_R8PO copies an R8GE matrix to an R8PO matrix.
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
#    The R8PO storage format is used for a symmetric positive definite 
#    matrix and its inverse.  (The Cholesky factor of an R8PO matrix is an
#    upper triangular matrix, so it will be in R8GE storage format.)
#
#    Only the diagonal and upper triangle of the square array are used.
#    This same storage scheme is used when the matrix is factored by
#    R8PO_FA, or inverted by R8PO_INVERSE.  For clarity, the lower triangle
#    is set to zero.
#
#    R8PO storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real A(N,N), the R8GE matrix.
#
#    Output, real B(N,N), the R8PO matrix.
#
  import numpy as np
  from r8po import r8po_zeros

  b = r8po_zeros ( n )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      b[i,j] = a[i,j]

  return b

def r8ge_to_r8po_test ( ):

#*****************************************************************************80
#
## R8GE_TO_R8PO_TEST tests R8GE_TO_R8PO.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8po import r8po_print

  n = 5
  seed = 123456789

  print ( '' )
  print ( 'R8GE_TO_R8PO_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_TO_R8PO converts an R8GE matrix to R8PO format.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a, seed = r8ge_random ( n, n, seed )

  r8ge_print ( n, n, a, '  The random R8GE matrix:' )
 
  b = r8ge_to_r8po ( n, a )

  r8po_print ( n, b, '  The R8PO matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_TO_R8PO_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_to_r8ut ( m, n, a_ge ):

#*****************************************************************************80
#
## R8GE_TO_R8UT copies an R8GE matrix to an R8UT matrix.
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
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, real A_GE(M,N), the R8GE matrix.
#
#    Output, real A_UT(M,N), the R8UT matrix.
#
  import numpy as np

  a_ut = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, min ( j + 1, m ) ):
      a_ut[i,j] = a_ge[i,j]

  return a_ut

def r8ge_to_r8ut_test ( ):

#*****************************************************************************80
#
## R8GE_TO_R8UT_TEST tests R8GE_TO_R8UT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8ut import r8ut_print

  m = 5
  n = 4
  seed = 123456789

  print ( '' )
  print ( 'R8GE_TO_R8UT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_TO_R8UT converts an R8GE matrix to R8UT format.' )

  a_ge, seed = r8ge_random ( m, n, seed )

  r8ge_print ( m, n, a_ge, '  The random R8GE matrix:' )
 
  a_ut = r8ge_to_r8ut ( m, n, a_ge )

  r8ut_print ( m, n, a_ut, '  The R8UT matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_TO_R8UT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_to_r8vec ( m, n, a ):

#*****************************************************************************80
#
## R8GE_TO_R8VEC copies an R8GE matrix to an R8VEC.
#
#  Discussion:
#
#    In C++ and FORTRAN, this routine is not really needed.  In MATLAB,
#    a data item carries its dimensionality implicitly, and so cannot be
#    regarded sometimes as a vector and sometimes as an array.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, real A(M,N), the array to be copied.
#
#    Output, real X(M*N), the vector.
#
  import numpy as np

  x = np.zeros ( m * n )

  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      x[k] = a[i,j]
      k = k + 1

  return x

def r8ge_to_r8vec_test ( ):

#*****************************************************************************80
#
## R8GE_TO_R8VEC_TEST tests R8GE_TO_R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 4
  n = 3

  print ( '' )
  print ( 'R8GE_TO_R8VEC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_TO_R8VEC converts an R8GE matrix to an R8VEC vector.' )

  a_r8ge = r8ge_indicator ( m, n )

  r8ge_print ( m, n, a_r8ge, '  R8GE matrix:' )

  a_r8vec = r8ge_to_r8vec ( m, n, a_r8ge )

  r8vec_print ( m * n, a_r8vec, '  Corresponding R8VEC vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_TO_R8VEC_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_to_r8vm ( m, n, a_ge ):

#*****************************************************************************80
#
## R8GE_TO_R8VM copies an R8GE matrix to an R8VM matrix.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, real A_GE(M,N), the R8GE matrix.
#
#    Output, real A_VM(N), the R8VM matrix.
#
  import numpy as np

  a_vm = np.zeros ( n )

  for j in range ( 0, n ):
    a_vm[j] = a_ge[1,j]

  return a_vm

def r8ge_to_r8vm_test ( ):

#*****************************************************************************80
#
## R8GE_TO_R8VM_TEST tests R8GE_TO_R8VM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 July 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vm import r8vm_print

  m = 5
  n = 4
  seed = 123456789

  print ( '' )
  print ( 'R8GE_TO_R8VM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_TO_R8VM converts an R8GE matrix to R8VM format.' )

  a_ge, seed = r8ge_random ( m, n, seed )

  r8ge_print ( m, n, a_ge, '  The random R8GE matrix:' )
 
  a_vm = r8ge_to_r8vm ( m, n, a_ge )

  r8vm_print ( m, n, a_vm, '  The R8VM matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_TO_R8VM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_transpose ( m, n, a ):

#*****************************************************************************80
#
## R8GE_TRANSPOSE makes a transposed copy of an R8GE matrix.
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
#    R8GE storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    05 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, real A(M,N), the matrix to be copied.
#
#    Output, real B(N,M), a copy of the transposed matrix.
#
  import numpy as np

  b = r8ge_zeros ( n, m )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      b[j,i] = a[i,j]

  return b

def r8ge_transpose_test ( ):

#*****************************************************************************80
#
## R8GE_TRANSPOSE_TEST tests R8GE_TRANSPOSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'R8GE_TRANSPOSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_TRANSPOSE makes a transposed copy of an R8GE matrix.' )

  a = r8ge_indicator ( m, n )

  r8ge_print ( m, n, a, '  Indicator matrix A:' )

  b = r8ge_transpose ( m, n, a )

  r8ge_print ( n, m, b, '  B = A\':' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_TRANSPOSE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8GE_TRANSPOSE_PRINT prints an R8GE matrix, transposed.
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
  r8ge_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8ge_transpose_print_test ( ):

#*****************************************************************************80
#
## R8GE_TRANSPOSE_PRINT_TEST tests R8GE_TRANSPOSE_PRINT.
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
  print ( 'R8GE_TRANSPOSE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_TRANSPOSE_PRINT prints the transpose of an R8GE matrix.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8ge_transpose_print ( m, n, v, '  Here is an R8GE matrix, transposed:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_TRANSPOSE_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8GE_TRANSPOSE_PRINT_SOME prints a portion of an R8GE matrix, transposed.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
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

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ' ),

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ) ),

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ) ),
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ) ),

      print ( '' )

  return

def r8ge_transpose_print_some_test ( ):

#*****************************************************************************80
#
## R8GE_TRANSPOSE_PRINT_SOME_TEST tests R8GE_TRANSPOSE_PRINT_SOME.
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
  print ( 'R8GE_TRANSPOSE_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_TRANSPOSE_PRINT_SOME prints some of an R8GE matrix, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8ge_transpose_print_some ( m, n, v, 0, 3, 2, 5, \
    '  R8GE matrix, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_TRANSPOSE_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_trf ( m, n, a ):

#*****************************************************************************80
#
## R8GE_TRF performs a LAPACK-style PLU factorization of a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    R8GE_TRF is a standalone version of the LAPACK routine R8GETRF.
#
#    The factorization uses partial pivoting with row interchanges,
#    and has the form
#      A = P * L * U
#    where P is a permutation matrix, L is lower triangular with unit
#    diagonal elements (lower trapezoidal if N < M), and U is upper
#    triangular (upper trapezoidal if M < N).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Anderson, Bai, Bischof, Demmel, Dongarra, Du Croz, Greenbaum,
#    Hammarling, McKenney, Ostrouchov, Sorensen,
#    LAPACK User's Guide,
#    Second Edition,
#    SIAM, 1995.
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrix A.  0 <= M.
#
#    Input, integer N, the number of columns of the matrix A.  0 <= N.
#
#    Input, real A(M,N), the M by N matrix to be factored.
#
#    Output, real A_LU(M,N), the factors L and U from the factorization
#    A = P*L*U the unit diagonal elements of L are not stored.
#
#    Output, integer PIVOT(min(M,N)), the pivot indices
#    for 1 <= I <= min(M,N), row i of the matrix was interchanged with
#    row PIVOT(I).
#
#    Output, integer INFO.
#    = 0: successful exit
#    < 0: if INFO = -K, the K-th argument had an illegal value
#    > 0: if INFO = K, U(K,K) is exactly zero. The factorization
#         has been completed, but the factor U is exactly
#         singular, and division by zero will occur if it is used
#         to solve a system of equations.
#
  import numpy as np

  a_lu = a.copy ( )

  pivot = np.zeros ( n, dtype = np.int32 )
#
#  Test the input parameters.
#
  info = 0

  if ( m < 0 ):
    info = -1
    return a_lu, pivot, info

  if ( n < 0 ):
    info = -2
    return a_lu, pivot, info

  if ( m == 0 or n == 0 ):
    return a_lu, pivot, info

  for j in range ( 0, min ( m, n ) ):
#
#  Find the pivot.
#
    t = abs ( a_lu[j,j] )
    jp = j
    for i in range ( j + 1, m ):
      if ( t < abs ( a_lu[i,j] ) ):
        t = abs ( a_lu[i,j] )
        jp = i

    pivot[j] = jp
#
#  Apply the interchange to columns 1:N.
#  Compute elements J+1:M of the J-th column.
#
    if ( a_lu[jp,j] != 0.0 ):

      if ( jp != j ):
        for jj in range ( 0, n ):
          t           = a_lu[j,jj]
          a_lu[j,jj]  = a_lu[jp,jj]
          a_lu[jp,jj] = t

      if ( j < m - 1 ):
        for i in range ( j + 1, m ):
          a_lu[i,j] = a_lu[i,j] / a_lu[j,j]

    elif ( info == 0 ):

      info = j
#
#  Update the trailing submatrix.
#
    if ( j < min ( m, n ) - 1 ):

      for ii in range ( j + 1, m ):
        for k in range ( j + 1, n ):
          a_lu[ii,k] = a_lu[ii,k] - a_lu[ii,j] * a_lu[j,k]

  return a_lu, pivot, info

def r8ge_trf_test ( ):

#*****************************************************************************80
#
## R8GE_TRF_TEST tests R8GE_TRF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  m = n
  nrhs = 1

  print ( '' )
  print ( 'R8GE_TRF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_TRF computes the LU factors of an R8GE matrix,' )
  print ( '  so that R8GE_TRS can solve the factored system.' )
  print ( '' )
  print ( '  Number of matrix rows M = %d' % ( m ) )
  print ( '  Number of matrix columns N = %d' % ( n ) )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( i == j - 1 ):
        a[i,j] = - 1.0
      elif ( i == j + 1 ):
        a[i,j] = - 1.0
      else:
        a[i,j] = 0.0

  a_lu, pivot, info = r8ge_trf ( m, n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_TRF_TEST - Fatal error!' )
    print ( '  R8GE_TRF declares the matrix is singular!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return

  b = np.zeros ( [ n, nrhs ] )
  b[n-1,0] = float ( n + 1 )

  x, info = r8ge_trs ( n, nrhs, 'N', a_lu, pivot, b )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_TRF_TEST - Fatal error!' )
    print ( '  R8GE_TRS returned an error condition!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return

  r8vec_print ( n, x, '  Solution:' )

  b = np.zeros ( [ n, nrhs ] )
  b[n-1,0] = float ( n + 1 )

  x, info = r8ge_trs ( n, nrhs, 'T', a_lu, pivot, b )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_TRF_TEST - Fatal error!' )
    print ( '  R8GE_TRS returned an error condition!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return

  r8vec_print ( n, x, '  Solution to transposed system:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_TRF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_trs ( n, nrhs, trans, a_lu, pivot, b ):

#*****************************************************************************80
#
## R8GE_TRS solves a system of linear equations factored by R8GE_TRF.
#
#  Discussion:
#
#    Note that in MATLAB we will have peculiar and maddening problems
#    if our input data B is actually a vector in fact, if B is a vector,
#    we must do something like call R8VEC_TO_R8GE in order to make it
#    look like a 2D array to MATLAB.
#
#    The R8GE storage format is used for a general M by N matrix.  A storage
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    R8GE_TRS is a standalone version of the LAPACK routine R8GETRS.
#
#    R8GE_TRS solves a system of linear equations
#      A * x = b  or  A' * X = B
#    with a general N by N matrix A using the PLU factorization computed
#    by R8GE_TRF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Anderson, Bai, Bischof, Demmel, Dongarra, Du Croz, Greenbaum,
#    Hammarling, McKenney, Ostrouchov, Sorensen,
#    LAPACK User's Guide,
#    Second Edition,
#    SIAM, 1995.
#
#  Parameters:
#
#    Input, integer N, the order of the matrix A.  0 <= N.
#
#    Input, integer NRHS, the number of right hand sides.  0 <= NRHS.
#
#    Input, character TRANS, specifies the form of the system of equations:
#    'N':  A * x = b  (No transpose)
#    'T':  A'* X = B  (Transpose)
#    'C':  A'* X = B  (Conjugate transpose = Transpose)
#
#    Input, real A_LU(N,N), the LU factors from R8GE_TRF.
#
#    Input, integer PIVOT(N), the pivot indices from R8GE_TRF.
#
#    Input, real B(N,NRHS), the right hand side matrix B.
#
#    Output, real X(N,NRHS), the solution matrix X.
#
#    Output, integer INFO
#    = 0:  successful exit
#    < 0:  if INFO = -I, the I-th argument had an illegal value.
#
  x = b.copy ( )

  info = 0

  if ( trans != 'n' and trans != 'N' and trans != 't' and trans != 'T' and \
       trans != 'c' and trans != 'C' ):
    info = -1
    return x, info
  elif ( n < 0 ):
    info = -2
    return x, info
  elif ( nrhs < 0 ):
    info = -3
    return x, info

  if ( n == 0 or nrhs == 0 ):
    return x, info

  if ( trans == 'n' or trans == 'N' ):
#
#  Apply row interchanges to the right hand sides.
#
    for i in range ( 0, n ):
      if ( pivot[i] != i ):
        for k in range ( 0, nrhs ):
          t             = x[i,k]
          x[i,k]        = x[pivot[i],k]
          x[pivot[i],k] = t
#
#  Solve L * x = b, overwriting b with x.
#
    for k in range ( 0, nrhs ):
      for j in range ( 0, n - 1 ):
        for i in range ( j + 1, n ):
          x[i,k] = x[i,k] - a_lu[i,j] * x[j,k]
#
#  Solve U * x = b, overwriting b with x.
#
    for k in range ( 0, nrhs ):
      for j in range ( n - 1, -1, -1 ):
        x[j,k] = x[j,k] / a_lu[j,j]

  else:
#
#  Solve U' * x = b, overwriting b with x.
#
    for k in range ( 0, nrhs ):
      for j in range ( 0, n ):
        x[j,k] = x[j,k] / a_lu[j,j]
        for i in range ( j + 1, n ):
          x[i,k] = x[i,k] - a_lu[j,i] * x[j,k]
#
#  Solve L' * x = b, overwriting b with x.
#
    for k in range ( 0, nrhs ):
      for j in range ( n - 1, 0, -1 ):
        for i in range ( 0, j ):
          x[i,k] = x[i,k] - a_lu[j,i] * x[j,k]
#
#  Apply row interchanges to the solution vectors.
#
    for i in range ( n - 1, -1, -1 ):
      if ( pivot[i] != i ):
        for k in range ( 0, nrhs ):
          t             = x[i,k]
          x[i,k]        = x[pivot[i],k]
          x[pivot[i],k] = t

  return x, info

def r8ge_trs_test ( ):

#*****************************************************************************80
#
## R8GE_TRS_TEST tests R8GE_TRS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  m = n
  nrhs = 1

  print ( '' )
  print ( 'R8GE_TRS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_TRS solves a linear system' )
  print ( '  that has been factored by R8GE_TRF.' )
  print ( '' )
  print ( '  Number of matrix rows M = %d' % ( m ) )
  print ( '  Number of matrix columns N = %d' % ( n ) )

  a = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        a[i,j] = 2.0
      elif ( i == j - 1 ):
        a[i,j] = - 1.0
      elif ( i == j + 1 ):
        a[i,j] = - 1.0
      else:
        a[i,j] = 0.0

  a_lu, pivot, info = r8ge_trf ( m, n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_TRS_TEST - Fatal error!' )
    print ( '  R8GE_TRF declares the matrix is singular!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return

  b = np.zeros ( [ n, nrhs ] )
  b[n-1,0] = float ( n + 1 )

  x, info = r8ge_trs ( n, nrhs, 'N', a_lu, pivot, b )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_TRS_TEST - Fatal error!' )
    print ( '  R8GE_TRS returned an error condition!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return

  r8vec_print ( n, x, '  Solution:' )

  b = np.zeros ( [ n, nrhs ] )
  b[n-1,0] = float ( n + 1 )

  x, info = r8ge_trs ( n, nrhs, 'T', a_lu, pivot, b )

  if ( info != 0 ):
    print ( '' )
    print ( 'R8GE_TRS_TEST - Fatal error!' )
    print ( '  R8GE_TRS returned an error condition!' )
    print ( '  The value of INFO is %d' % ( info ) )
    return

  r8vec_print ( n, x, '  Solution to transposed system:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_TRS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_zeros ( m, n ):

#*****************************************************************************80
#
## R8GE_ZEROS zeroes an R8GE matrix.
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
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#    N must be positive.
#
#    Output, real A(M,N), the zeroed out matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  return a

def r8ge_zeros_test ( ):

#*****************************************************************************80
#
## R8GE_ZEROS_TEST tests R8GE_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 August 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'R8GE_ZEROS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_ZEROS zeros out space for a general matrix.' )
  print ( '' )
  print ( '  Matrix order M, N = %d, %d' % ( m, n ) )

  a = r8ge_zeros ( m, n )

  r8ge_print ( m, n, a, '  Matrix A:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_ZEROS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_house_column ( n, a_vec, k ):

#*****************************************************************************80
#
## R8VEC_HOUSE_COLUMN defines a Householder premultiplier that "packs" a column.
#
#  Discussion:
#
#    The routine returns a vector V that defines a Householder
#    premultiplier matrix H(V) that zeros out the subdiagonal entries of
#    column K of the matrix A.
#
#       H(V) = I - 2 * v * v'
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix A.
#
#    Input, real A_VEC(N), a row or column of the matrix A.
#
#    Input, integer K, the "special" entry in A_VEC.
#    The Householder matrix will zero out the entries after this.
#
#    Output, real V(N), a vector of unit L2 norm which defines an
#    orthogonal Householder premultiplier matrix H with the property
#    that the K-th column of H*A is zero below the diagonal.
#
  import numpy as np

  v = np.zeros ( n )

  if ( k < 0 or n - 1 <= k ):
    return v

  s = 0.0
  for i in range ( k, n ):
    s = s + a_vec[i] ** 2
  s = np.sqrt ( s )

  if ( s == 0.0 ):
    return v

  if ( a_vec[k] < 0.0 ):
    v[k] = a_vec[k] - abs ( s )
  else:
    v[k] = a_vec[k] + abs ( s )

  for i in range ( k + 1, n ):
    v[i] = a_vec[i]

  s = 0.0
  for i in range ( k, n ):
    s = s + v[i] ** 2
  s = np.sqrt ( s )

  for i in range ( k, n ):
    v[i] = v[i] / s

  return v

def r8vec_house_column_test ( ):

#*****************************************************************************80
#
## R8VEC_HOUSE_COLUMN_TEST tests R8VEC_HOUSE_COLUMN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_HOUSE_COLUMN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_HOUSE_COLUMN returns the compact form of' )
  print ( '  a Householder matrix that "packs" a column' )
  print ( '  of a matrix.' )
#
#  Get a random matrix.
#
  n = 4
  r8_lo = 0.0
  r8_hi = 5.0
  seed = 123456789;

  a, seed = r8ge_random_ab ( n, n, r8_lo, r8_hi, seed )

  r8ge_print ( n, n, a, '  Matrix A:' )

  a_col = np.zeros ( n )

  for k in range ( 0, n - 1 ):

    print ( '' )
    print ( '  Working on column K = %d' % ( k ) )

    for i in range ( 0, n ):
      a_col[i] = a[i,k]

    v = r8vec_house_column ( n, a_col, k )

    h = r8ge_house_form ( n, v )

    r8ge_print ( n, n, h, '  Householder matrix H:' )

    ha = r8ge_mm ( n, n, n, h, a )

    r8ge_print ( n, n, ha, '  Product H*A:' )
#
#  If we set A := HA, then we can successively convert A to upper
#  triangular form.
#
    a = ha
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_HOUSE_COLUMN_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## R8VEC_INDICATOR1 sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements of the vector.
#
#    Output, real A(N), the indicator array.
#
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## R8VEC_INDICATOR1_TEST tests R8VEC_INDICATOR1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'R8VEC_INDICATOR1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_INDICATOR1 returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_INDICATOR1_TEST' )
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

def r8vec_norm_affine ( n, v0, v1 ):

#*****************************************************************************80
#
## R8VEC_NORM_AFFINE returns the affine norm of an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    The affine vector L2 norm is defined as:
#
#      R8VEC_NORM_AFFINE(V0,V1) 
#        = sqrt ( sum ( 1 <= I <= N ) ( V1(I) - V0(I) )^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    30 July 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the vector dimnension.
#
#    Input, real V0(N), the base vector.
#
#    Input, real V1(N), the vector.
#
#    Output, real VALUE, the affine L2 norm.
#
  import numpy as np

  value = 0.0
  for i in range ( 0, n ): 
    value = value + ( v0[i] - v1[i] ) ** 2
  value =  np.sqrt ( value )

  return value

def r8vec_norm_affine_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_AFFINE_TEST tests R8VEC_NORM_AFFINE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 10

  print ( '' )
  print ( 'R8VEC_NORM_AFFINE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORM_AFFINE computes the L2 norm of' )
  print ( '  the difference of two R8VECs.' )

  seed = 123456789;

  x, seed = r8vec_uniform_01 ( n, seed )
  y, seed = r8vec_uniform_01 ( n, seed )
  z = np.zeros ( n )
  for i in range ( 0, n ):
    z[i] = x[i] - y[i]

  print ( '' )
  print ( '  R8VEC_NORM_AFFINE(X,Y) = %g' % ( r8vec_norm_affine ( n, x, y ) ) )
  print ( '  R8VEC_NORM (X-Y):        %g' % ( r8vec_norm ( n, z ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORM_AFFINE_TEST:' )
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

def r8vec_print_some ( n, a, max_print, title ):

#*****************************************************************************80
#
## R8VEC_PRINT_SOME prints "some" of an R8VEC.
#
#  Discussion:
#
#    The user specifies MAX_PRINT, the maximum number of lines to print.
#
#    If N, the size of the vector, is no more than MAX_PRINT, then
#    the entire vector is printed, one entry per line.
#
#    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, integer MAX_PRINT, the maximum number of lines
#    to print.
#
#    Input, string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '  %6d  %14g' % ( i, a[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    print ( '  ......  ..............' )
    i = n - 1
    print ( '  %6d  %14g' % ( i, a[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '  %6d  %14g' % ( i, a[i] ) )
    i = max_print - 1
    print ( '  %6d  %14g  ...more entries...' % ( i, a[i] ) )

  return

def r8vec_print_some_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_SOME_TEST tests R8VEC_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT_SOME prints some of an R8VEC.' )

  n = 100
  a = r8vec_indicator1 ( n )

  max_print = 10

  r8vec_print_some ( n, a, max_print, '  No more than 10 lines of this vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_to_r8ge ( m, n, x ):

#*****************************************************************************80
#
## R8VEC_TO_R8GE copies an R8VEC into a R8GE matrix.
#
#  Discussion:
#
#    In C++  and FORTRAN, this routine is not really needed.  In MATLAB,
#    a data item carries its dimensionality implicitly, and so cannot be
#    regarded sometimes as a vector and sometimes as an array.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, real X(M*N), the vector to be copied into the array.
#
#    Output, real A(M,N), the array.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )
  
  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = x[k]
      k = k + 1

  return a

def r8vec_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8VEC_TO_R8GE_TEST tests R8VEC_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 4
  n = 3

  print ( '' )
  print ( 'R8VEC_TO_R8GE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_TO_R8GE converts an R8VEC vector to an R8GE matrix.' )

  a_r8vec = r8vec_indicator1 ( m * n )
  
  r8vec_print ( m * n, a_r8vec, '  The R8VEC vector:' )

  a_r8ge = r8vec_to_r8ge ( m, n, a_r8vec )

  r8ge_print ( m, n, a_r8ge, '  Corresponding R8GE matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_TO_R8GE_TEST:' )
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
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8VEC_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8VEC_UNIFORM_01 - Fatal error!' )

  x = np.zeros ( n );

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

def r8vec2_print_some ( n, x1, x2, max_print, title ):

#*****************************************************************************80
#
#% R8VEC2_PRINT_SOME prints "some" of an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is two R8VEC's.
#
#    An R8VEC is a vector of R8 values.
#
#    The user specifies MAX_PRINT, the maximum number of lines to print.
#
#    If N, the size of the vectors, is no more than MAX_PRINT, then
#    the entire vectors are printed, one entry of each per line.
#
#    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries of the vectors.
#
#    Input, real X1(N), X2(N), the vector to be printed.
#
#    Input, integer MAX_PRINT, the maximum number of lines to print.
#
#    Input, string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    print ( '......  ..............  ..............' )
    i = n - 1
    print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    i = max_print - 1
    print ( '%6d: %14g  %14g  ...more entries...' % ( i, x1[i], x2[i] ) )

  return

def r8vec2_print_some_test ( ):

#*****************************************************************************80
#
## R8VEC2_PRINT_SOME_TEST tests R8VEC2_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 January 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 100
  a = np.zeros ( n )
  b = np.zeros ( n )

  for i in range ( 0, n ):
    x = float ( i + 1 )
    a[i] = x * x
    b[i] = np.sqrt ( x )

  print ( '' )
  print ( 'R8VEC2_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC2_PRINT_SOME prints some of a pair of R8VEC\'s.' )

  r8vec2_print_some ( n, a, b, 10, '  Square and square root:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_PRINT_SOME_TEST:' )
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

def r8ge_test ( ):

#*****************************************************************************80
#
## R8GE_TEST tests the R8GE library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8GE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the R8GE library.' )

  i4_log_10_test ( )

  i4vec_print_test ( )

  r8_normal_01_test ( )
  r8_sign_test ( )
  r8_uniform_01_test ( )

  r8ge_cg_test ( )
  r8ge_co_test ( )
  r8ge_det_test ( )
  r8ge_dif2_test ( )
  r8ge_dilu_test ( )
  r8ge_fa_test01 ( )
  r8ge_fa_test02 ( )
  r8ge_fs_test ( )
  r8ge_fss_test ( )
  r8ge_hilbert_test ( )
  r8ge_hilbert_inverse_test ( )
  r8ge_house_axh_test ( )
  r8ge_house_form_test ( )
  r8ge_identity_test ( )
  r8ge_ilu_test ( )
  r8ge_indicator_test ( )
  r8ge_inverse_test ( )
  r8ge_ml_test ( )
  r8ge_mm_test ( )
  r8ge_mtm_test ( )
  r8ge_mtv_test ( )
  r8ge_mu_test ( )
  r8ge_mv_test ( )
  r8ge_orth_random_test ( )
  r8ge_pds_random_test ( )
  r8ge_plu_test ( )
  r8ge_poly_test ( )
  r8ge_print_test ( )
  r8ge_print_some_test ( )
  r8ge_random_test ( )
  r8ge_random_ab_test ( )
  r8ge_res_test ( )
  r8ge_sl_test ( )
  r8ge_sl_it_test ( )
# r8ge_to_r8lt_test ( )
# r8ge_to_r8po_test ( )
# r8ge_to_r8ut_test ( )
  r8ge_to_r8vec_test ( )
# r8ge_to_r8vm_test ( )
  r8ge_transpose_test ( )
  r8ge_transpose_print_test ( )
  r8ge_transpose_print_some_test ( )
  r8ge_trf_test ( )
  r8ge_trs_test ( )
  r8ge_zeros_test ( )

  r8vec_house_column_test ( )
  r8vec_indicator1_test ( )
  r8vec_norm_test ( )
  r8vec_norm_affine_test ( )
  r8vec_print_test ( )
  r8vec_print_some_test ( )
  r8vec_to_r8ge_test ( )
  r8vec_uniform_01_test ( )

  r8vec2_print_some_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  r8ge_test ( )
  timestamp ( )
 
