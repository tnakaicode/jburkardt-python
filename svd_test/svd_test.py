#! /usr/bin/env python3
#
def svd_test ( m, n, seed ):

#*****************************************************************************80
#
## SVD_TEST demonstrates the SVD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modififed:
#
#    11 December 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.  
#
#    Input, integer SEED, a seed for the random number generator.
#
#  Local Parameters:
#
#    Local, real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    Local, real S(M,N), the diagonal factor
#    int the singular value decomposition of A.
#
#    Output, real U(M,M), the first orthogonal factor
#    in the singular value decomposition of A.
#
#    Output, real V(N,N), the second orthogonal factor
#    in the singular value decomposition of A.
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'SVD_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Demonstrate the singular value decomposition (SVD)' )
  print ( '' )
  print ( '  A real MxN matrix A can be factored as:' )
  print ( '' )
  print ( '    A = U * S * V''' )
  print ( '' )
  print ( '  where' )
  print ( '' )
  print ( '    U = MxM orthogonal,' )
  print ( '    S = MxN zero except for diagonal,' )
  print ( '    V = NxN orthogonal.' )
  print ( '' )
  print ( '  The diagonal of S contains only nonnegative numbers' )
  print ( '  and these are arranged in descending order.' )
#
#  If at least one command line argument, it's M.
#
  print ( '' )
  print ( '  Matrix row order    M = #d', m )
  print ( '  Matrix column order N = #d', n )
#
#  Generate the matrix A.
#
  print ( '' )
  print ( '  We choose a "random" matrix A, with integral' )
  print ( '  values between 0 and 10.' )

  a, seed = r8mat_uniform_01 ( m, n, seed )

  a = np.round ( 10.0 * a )

  r8mat_print ( m, n, a, '  The matrix A:' )
#
#  Get the SVD.
#
  [ u, svec, v ] = np.linalg.svd ( a )
#
#  Note that Numpy's SVD has A=U*S*V, NOT A=U*S*V'.
#
  v = v.transpose ( )
#
#  Inflate SVEC to a matrix.
#
  s = np.zeros ( [ m, n ] )
  for ij in range ( 0, min ( m, n ) ):
    s[ij,ij] = svec[ij];
#
#  Print the SVD.
#
  r8mat_print ( m, m, u, '  The orthogonal factor U:' )
  r8mat_print ( m, n, s, '  The diagonal factor S:' )
  r8mat_print ( n, n, v, '  The orthogonal factor V:' )
#
#  Check that A = U * S * V'.
#
  svd_product_test ( m, n, a, u, s, v )
#
#  Compute the norm of the difference between A and the successive
#  sums of rank one approximants.
#
  rank_one_test ( m, n, a, u, s, v )
#
#  Actually print the sums of rank one approximants.
#
  rank_one_print_test ( m, n, a, u, s, v )
#
#  Compute the pseudoinverse.
#
  a_pseudo = pseudo_inverse ( m, n, u, s, v )

  r8mat_print ( n, m, a_pseudo, '  The pseudoinverse of A:' )
#
#  Test A*A+ = I+, A+*A = I+
#
  pseudo_product_test ( m, n, a, a_pseudo )
#
#  Demonstrate the use of the pseudoinverse for linear systems.
#
  seed = pseudo_linear_solve_test ( m, n, a, a_pseudo, seed )
#
#  Terminate.
#
  print ( '' )
  print ( 'SVD_TEST:' )
  print ( '  Normal end of execution.' )
  
  return

def pseudo_inverse ( m, n, u, s, v ):

#*****************************************************************************80
#
## PSEUDO_INVERSE computes the pseudoinverse.
#
#  Discussion:
#
#    Given the singular value decomposition of a real MxN matrix A:
#
#      A = U * S * V'
#
#    where 
#
#      U is MxM orthogonal,
#      S is MxN, and entirely zero except for the diagonal
#      V is NxN orthogonal.
#
#    the pseudo inverse is the NxM matrix A+ with the form
#
#      A+ = V * S+ * U'
#
#    where 
#
#      S+ is the NxM matrix whose nonzero diagonal elements are
#      the inverses of the corresponding diagonal elements of S.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 December 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the matrix A.
#
#    Input, real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    Input, real U(M,M), S(M,N), V(N,N), the factors
#    that form the singular value decomposition of A.
#
#    Output, real A_PSEUDO(N,M), the pseudoinverse of A.
#
  import numpy as np

  sp = np.zeros ( [ n, m ] )

  for i in range ( 0, min ( m, n ) ):
    if ( s[i,i] != 0.0 ):
      sp[i,i] = 1.0 / s[i,i]

  a_pseudo = np.matmul ( v, np.matmul ( sp, u.transpose() ) )

  return a_pseudo

def pseudo_linear_solve_test ( m, n, a, a_pseudo, seed ):

#*****************************************************************************80
#
## PSEUDO_LINEAR_SOLVE_TEST uses the pseudoinverse for linear systems.
#
#  Discussion:
#
#    Given an MxN matrix A, and its pseudoinverse A+:
#
#      "Solve" A  * x = b by x = A+  * b.
#
#      "Solve" A' * x = b by x = A+' * b.
#
#    When the system is overdetermined, the solution minimizes the
#    L2 norm of the residual.  
#
#    When the system is underdetermined, the solution
#    is the solution of minimum L2 norm.     
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 December 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the matrix A.
#
#    Input, real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    Input, real A_PSEUDO(N,M), the pseudo_inverse of A.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  print ( '' )
  print ( 'PSEUDO_LINEAR_SOLVE_TEST' )
#
#  A * x = b, b in range of A.
#
  xn1, seed = r8vec_uniform_01 ( n, seed )
  xn1 = np.round ( 10.0 * xn1 )
  bm = np.dot ( a, xn1 )
  xn2 = np.dot ( a_pseudo, bm )
  rm = np.dot ( a, xn2 ) - bm

  print ( '' )
  print ( '  Given:' )
  print ( '    b = A * x1' )
  print ( '  so that b is in the range of A, solve' )
  print ( '    A * x = b' )
  print ( '  using the pseudoinverse:' )
  print ( '    x2 = A+ * b.' )
  print ( '' )
  print ( '  Norm of x1 =       %f' % ( np.linalg.norm ( xn1 ) ) )
  print ( '  Norm of x2 =       %f' % ( np.linalg.norm ( xn2 ) ) )
  print ( '  Norm of residual = %f' % ( np.linalg.norm ( rm ) ) )
#
#  A * x = b, b not in range of A.
#
  if ( n < m ):

    print ( '' )
    print ( '  For N < M, most systems A*x=b will not be' )
    print ( '  exactly and uniquely solvable, except in the' )
    print ( '  least squares sense.' )
    print ( '' )
    print ( '  Here is an example:' )

    b8, seed= r8vec_uniform_01 ( m, seed )
    xn2 = np.dot ( a_pseudo, bm )
    rm = np.dot ( a, xn2 ) - bm

    print ( '' )
    print ( '  Given b is NOT in the range of A, solve' )
    print ( '    A * x = b' )
    print ( '  using the pseudoinverse:' )
    print ( '    x2 = A+ * b.' )
    print ( '' )
    print ( '  Norm of x2 =       %f' % ( np.linalg.norm ( xn2 ) ) )
    print ( '  Norm of residual = %f' % ( np.linalg.norm ( rm ) ) )
#
#  A' * x = b, b is in the range of A'.
#
  xm1, seed = r8vec_uniform_01 ( m, seed )
  xm1 = np.round ( 10.0 * xm1 )
  bn = np.dot ( a.transpose(), xm1 )
  xm2 = np.dot ( a_pseudo.transpose ( ), bn )
  rn = np.dot ( a.transpose ( ), xm2 ) - bn

  print ( '' )
  print ( '  Given:' )
  print ( '    b = A'' * x1' )
  print ( '  so that b is in the range of A'', solve' )
  print ( '    A'' * x = b' )
  print ( '  using the pseudoinverse:' )
  print ( '    x2 = A+'' * b.' )
  print ( '' )
  print ( '  Norm of x1 =       %f' % ( np.linalg.norm ( xm1 ) ) )
  print ( '  Norm of x2 =       %f' % ( np.linalg.norm ( xm2 ) ) )
  print ( '  Norm of residual = %f' % ( np.linalg.norm ( rn ) ) )
#
#  A' * x = b, b is not in the range of A'.
#
  if ( m < n ):

    print ( '' )
    print ( '  For M < N, most systems A''*x=b will not be' )
    print ( '  exactly and uniquely solvable, except in the' )
    print ( '  least squares sense.' )
    print ( '' )
    print ( '  Here is an example:' )

    bn, seed = r8vec_uniform_01 ( n, seed )
    xm2 = np.dot ( a_pseudo.transpose () * bn )
    rn = np.dot ( a.transpose(), xm2 ) - bn

    print ( '' )
    print ( '  Given b is NOT in the range of A'', solve' )
    print ( '    A'' * x1 = b' )
    print ( '  using the pseudoinverse:' )
    print ( '    x2 = A+'' * b.' )
    print ( '' )
    print ( '  Norm of x2 =       %f' % ( np.linalg.norm ( xm2 ) ) )
    print ( '  Norm of residual = %f' % ( np.linalg.norm ( rn ) ) )

  return seed

def pseudo_product_test ( m, n, a, a_pseudo ):

#*****************************************************************************80
#
## PSEUDO_PRODUCT_TEST examines the products A*A+ and A+*A.
#
#  Discussion:
#
#    Given an MxN matrix A, and its pseudoinverse A+, we must have
#
#      A+ * A * A+ = A+
#      A * A+ * A = A
#      ( A * A+ )' = A * A+ (MxM symmetry)
#      ( A+ * A )' = A+ * A (NxN symmetry)
#
#    If M <= N, A * A+ may be "interesting" (equal to or "like" the identity),
#    if N <= M, A+ * A may be "interesting" (equal to or "like" the identity).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 December 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the matrix A.
#
#    Input, real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    Input, real A_PSEUDO(N,M), the pseudo_inverse of A.
#
  import numpy as np

  print ( '' )
  print ( 'PSEUDO_PRODUCT_TEST' )
  print ( '' )
  print ( '  The following relations MUST hold:' )
  print ( '' )
  print ( '   A  * A+ * A  = A' )
  print ( '   A+ * A  * A+ = A+' )
  print ( ' ( A  * A+ ) is MxM symmetric' )
  print ( ' ( A+ * A  ) is NxN symmetric' )

  bmn = np.matmul ( a, np.matmul ( a_pseudo, a ) )

  dif1 = np.linalg.norm ( a - bmn, ord = 'fro' )

  bnm  = np.matmul ( a_pseudo, np.matmul ( a, a_pseudo ) )

  dif2 = np.linalg.norm ( a_pseudo - bnm, ord = 'fro' )

  bmm = np.matmul ( a, a_pseudo ) 

  dif3 = np.linalg.norm ( bmm - bmm.transpose(), ord = 'fro' )

  bnn = np.matmul ( a_pseudo, a )

  dif4 = np.linalg.norm ( bnn - bnn.transpose(), ord = 'fro' )

  print ( '' )
  print ( '  Here are the Frobenius norms of the errors' )
  print ( '  in these relationships:' )
  print ( '' )
  print ( '   A  * A+ * A  = A           %f' % ( dif1 ) )
  print ( '   A+ * A  * A+ = A+          %f' % ( dif2 ) )
  print ( ' ( A  * A+ ) is MxM symmetric %f' % ( dif3 ) )
  print ( ' ( A+ * A  ) is NxN symmetric %f' % ( dif4 ) )

  print ( '' )
  print ( '  In some cases, the matrix A * A+' )
  print ( '  may be interesting (if M <= N, then' )
  print ( '  it MIGHT look like the identity.)' )

  r8mat_print ( m, m, bmm, '  A * A+:' )

  print ( '' )
  print ( '  In some cases, the matrix A+ * A' )
  print ( '  may be interesting (if N <= M, then' )
  print ( '  it MIGHT look like the identity.)' )

  r8mat_print ( n, n, bnn, '  A+ * A' )

  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8MAT_PRINT prints an R8MAT.
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
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_TEST tests R8MAT_PRINT.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8MAT_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT prints an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print ( m, n, v, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME prints out a portion of an R8MAT.
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

def r8mat_print_some_test ( ):

#*****************************************************************************80
#
## R8MAT_PRINT_SOME_TEST tests R8MAT_PRINT_SOME.
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
  print ( 'R8MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRINT_SOME prints some of an R8MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8mat_uniform_01 ( m, n, seed ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_01 returns a unit pseudorandom R8MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 April 2013
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
    print ( 'R8MAT_UNIFORM_01 - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8MAT_UNIFORM_01 - Fatal error!' )

  r = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = seed * 4.656612875E-10

  return r, seed

def r8mat_uniform_01_test ( ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_01_TEST tests R8MAT_UNIFORM_01.
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
  from r8mat_print import r8mat_print

  m = 5
  n = 4
  seed = 123456789

  print ( '' )
  print ( 'R8MAT_UNIFORM_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_UNIFORM_01 computes a random R8MAT.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8mat_uniform_01 ( m, n, seed )

  r8mat_print ( m, n, v, '  Random R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_UNIFORM_01_TEST:' )
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
  from r8vec_print import r8vec_print

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

def rank_one_test ( m, n, a, u, s, v ):

#*****************************************************************************80
#
## RANK_ONE_TEST compares A to the sum of rank one matrices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    11 December 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the matrix A.
#
#    Input, real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    Input, real U(M,M), S(M,N), V(N,N), the factors
#    that form the singular value decomposition of A.
#
  import numpy as np

  a_norm = np.linalg.norm ( a, ord = 'fro' )

  print ( '' )
  print ( 'RANK_ONE_TEST:' )
  print ( '  Compare A to the sum of R rank one matrices.' )
  print ( '' )
  print ( '         R    Absolute      Relative' )
  print ( '              Error         Error' )
  print ( '' )

  for r in range ( 1, min ( m, n ) + 1 ):

    usv = np.matmul ( u[:,0:r], np.matmul ( s[0:r,0:r],  v[0:n,0:r].transpose() ) )

    dif_norm = np.linalg.norm ( a - usv, ord = 'fro' )

    print ( '  %8d  %14f  %14f' % ( r, dif_norm, dif_norm / a_norm ) )

  return

def rank_one_print_test ( m, n, a, u, s, v ):

#*****************************************************************************80
#
## RANK_ONE_PRINT_TEST prints the sums of rank one matrices.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 December 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the matrix A.
#
#    Input, real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    Input, real U(M,M), S(M,N), V(N,N), the factors
#    that form the singular value decomposition of A.
#
  import numpy as np

  a_norm = np.linalg.norm ( a, ord = 'fro' )

  print ( '' )
  print ( 'RANK_ONE_PRINT_TEST:' )
  print ( '  Print the sums of R rank one matrices.' )

  for r in range ( 1, min ( m, n ) + 1 ):

    usv = np.matmul ( u[:,0:r], np.matmul ( s[0:r,0:r],  v[0:n,0:r].transpose() ) )

    title = '  Rank R = %d' % ( r )
    r8mat_print ( m, n, usv, title )

  r8mat_print ( m, n, a, '  Original matrix A:' )

  return

def svd_product_test ( m, n, a, u, s, v ):

#*****************************************************************************80
#
## SVD_PRODUCT_TEST tests that A = U * S * V'.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 December 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the matrix A.
#
#    Input, real A(M,N), the matrix whose singular value
#    decomposition we are investigating.
#
#    Input, real U(M,M), S(M,N), V(N,N), the factors
#    that form the singular value decomposition of A.
#
  import numpy as np

  a_norm = np.linalg.norm ( a, ord = 'fro' )

  usv = np.matmul ( u, np.matmul ( s, v.transpose() ) )

  r8mat_print ( m, n, usv, '  The product U * S * V''' )

  dif_norm = np.linalg.norm ( a - usv, 'fro' )

  print ( '' )
  print ( '  Frobenius Norm of A, A_NORM = %f' % ( a_norm ) )
  print ( '' )
  print ( '  ABSOLUTE ERROR for A = U*S*V'':' )
  print ( '  Frobenius norm of difference A-U*S*V'' = %f' % ( dif_norm ) )
  print ( '' )
  print ( '  RELATIVE ERROR for A = U*S*V'':' )
  print ( '  Ratio of DIF_NORM / A_NORM = %f' % ( dif_norm / a_norm ) )

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

if ( __name__ == '__main__' ):
  timestamp ( )
  m = 3
  n = 3
  seed = 123456789
  svd_test ( m, n, seed )
  timestamp ( )
