#! /usr/bin/env python3
#
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

def r8bin_print ( bin_num, bin, bin_limit, title ):

#*****************************************************************************80
#
## R8BIN_PRINT prints the bins of a real vector.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ( kind = 4 ) BIN_NUM, the number of bins.
#
#    Input, integer ( kind = 4 ) BIN(1:BIN_NUM+2).
#    BIN(1) counts entries of X less than BIN_LIMIT(1).
#    BIN(BIN_NUM+2) counts entries greater than or equal to BIN_LIMIT(BIN_NUM+1).
#    For 2 <= I <= BIN_NUM+1, BIN(I) counts the entries X(J) such that
#      BIN_LIMIT(I-1) <= X(J) < BIN_LIMIT(I).
#    where H is the bin spacing.
#
#    Input, real BIN_LIMIT(1:BIN_NUM+1), the "limits" of the bins.
#    BIN(I) counts the number of entries X(J) such that
#      BIN_LIMIT(I-1) <= X(J) < BIN_LIMIT(I).
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( '%s' % ( title ) )
  print ( '' )
  print ( '   Index     Lower Limit   Count     Upper Limit' )
  print ( '' )
  print ( '  %6d                  %6d  %14g' % ( 0, bin[0], bin_limit[0] ) )
  for i in range ( 0, bin_num ):
    print ( '  %6d  %14g  %6d  %14g' % ( i + 1, bin_limit[i], bin[i+1], bin_limit[i+1] ) )
  print ( '  %6d  %14g  %6d' % ( bin_num + 1, bin_limit[bin_num], bin[bin_num+1] ) )

  return

def r8mat_house_axh ( n, a, v ):

#*****************************************************************************80
#
## R8MAT_HOUSE_AXH computes A*H where H is a compact Householder matrix.
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

def r8mat_house_axh_test ( ):

#*****************************************************************************80
#
## R8MAT_HOUSE_AXH_TEST tests R8MAT_HOUSE_AXH.
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
  print ( 'R8MAT_HOUSE_AXH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_HOUSE_AXH multiplies a matrix A times a' )
  print ( '  compact Householder matrix.' )

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789

  a, seed = r8mat_uniform_ab ( n, n, r8_lo, r8_hi, seed )

  r8mat_print ( n, n, a, '  Matrix A:' )
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

  h = r8mat_house_form ( n, v )

  r8mat_print ( n, n, h, '  Householder matrix H:' )
#
#  Compute A*H.
#
  ah = r8mat_house_axh ( n, a, v )

  r8mat_print ( n, n, ah, '  Indirect product A*H:' )
#
#  Compare with a direct calculation.
#
  ah = np.dot ( a, h )

  r8mat_print ( n, n, ah, '  Direct product A*H:' )
#
#  Compute H*A to demonstrate packed column 3:
#
  ha = np.dot ( h, a )

  r8mat_print ( n, n, ha, '  H*A should pack column 3:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_HOUSE_AXH_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8mat_house_form ( n, v ):

#*****************************************************************************80
#
## R8MAT_HOUSE_FORM constructs a Householder matrix from its compact form.
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

def r8mat_house_form_test ( ):

#*****************************************************************************80
#
## R8MAT_HOUSE_FORM_TEST tests R8MAT_HOUSE_FORM.
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
  print ( 'R8MAT_HOUSE_FORM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_HOUSE_FORM forms a Householder' )
  print ( '  matrix from its compact form.' )

  r8vec_print ( n, v, '  Compact vector form V:' )

  h = r8mat_house_form ( n, v )
 
  r8mat_print ( n, n, h, '  Householder matrix H:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_HOUSE_FORM_TEST' )
  print ( '  Normal end of execution.' )
  return
  
def r8mat_orth_uniform ( n, seed ):

#*****************************************************************************80
#
## R8MAT_ORTH_UNIFORM returns a random orthogonal matrix.
#
#  Properties:
#
#    The inverse of A is equal to A'.
#
#    A * A'  = A' * A = I.
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
#    The determinant of A is +1 or -1.
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
#    24 April 2005
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
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real A(N,N), the orthogonal matrix.
#
#    Output, integer SEED, a seed for the random number generator.
#
  import numpy as np
  
  a = np.zeros ( [ n, n ] )
#
#  Start with A = the identity matrix.
#
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
  for j in range ( 0, n - 1 ):
#
#  Set the vector that represents the J-th column to be annihilated.
#
    x = np.zeros ( n )

    for i in range ( j, n ):
      x[i], seed = r8_normal_01 ( seed )
#
#  Compute the vector V that defines a Householder transformation matrix
#  H(V) that annihilates the subdiagonal elements of X.
#
    v = r8vec_house_column ( n, x, j )
#
#  Postmultiply the matrix A by H'(V) = H(V).
#
    a = r8mat_house_axh ( n, a, v )

  return a, seed

def r8mat_orth_uniform_test ( ):

#*****************************************************************************80
#
## R8MAT_ORTH_UNIFORM tests R8MAT_ORTH_UNIFORM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 July 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  
  n = 5
  seed = 123456789

  print ( '' )
  print ( 'R8MAT_ORTH_UNIFORM_TEST' )
  print ( '  R8SYMM_ORTH_UNIFORM generates a random orthogopnal matrix.' )

  q, seed = r8mat_orth_uniform ( n, seed )

  r8mat_print ( n, n, q, '  The matrix Q:' )

  qtq = np.dot ( np.transpose ( q ), q )
  
  r8mat_print ( n, n, qtq, '  The matrix Q\'Q:' )

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
    print ( '  Col: ' ),

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ) ),

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ) ),

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

def r8mat_uniform_ab ( m, n, a, b, seed ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_AB returns a scaled pseudorandom R8MAT.
#
#  Discussion:
#
#    An R8MAT is an array of R8's.
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
  import numpy
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8MAT_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8MAT_UNIFORM_AB - Fatal error!' )

  r = numpy.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r8mat_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8MAT_UNIFORM_AB_TEST tests R8MAT_UNIFORM_AB.
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

  m = 5
  n = 4
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'R8MAT_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_UNIFORM_AB computes a random R8MAT.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8mat_uniform_ab ( m, n, a, b, seed )

  r8mat_print ( m, n, v, '  Random R8MAT:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return
  
def r8nsymm_gen ( n, lamda_mean, lamda_dev, seed ):

#*****************************************************************************80
#
## R8NSYMM_GEN generates a nonsymmetric matrix with a certain eigenstructure.
#
#  Discussion:
#
#    An R8NSYMM is a real nonsymmetric matrix stored using full storage, and
#    using R8 arithmetic.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real LAMBDA_MEAN, the mean value of the normal
#    distribution from which the eigenvalues will be chosen.
#
#    Input, real LAMBDA_DEV, the standard deviation of the normal
#    distribution from which the eigenvalues will be chosen.
#
#    Input/output, integer SEED, a seed for the random
#    number generator.
#
#    Output, real A(N,N), the test matrix.
#
#    Output, real QL(N,N), the left eigenvector matrix.
#
#    Output, real QR(N,N), the right eigenvector matrix.
#
#    Output, real LAMDA(N), the eigenvalue vector.
#
  import numpy as np
#
#  Choose the eigenvalues LAMDA.
#
  lamda, seed = r8vec_normal_ab ( n, lamda_mean, lamda_dev, seed )
  
  l = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    l[i,i] = lamda[i]
#
#  Get random orthogonal matrices QL and QR.
#
  ql, seed = r8mat_orth_uniform ( n, seed )
  qr, seed = r8mat_orth_uniform ( n, seed )
#
#  Set A = QL * Lambda*I * QR'.
#
  a = np.dot ( ql, np.dot ( l, np.transpose ( qr ) ) )

  return a, ql, qr, lamda, seed
  
def r8nsymm_gen_test ( ):

#*****************************************************************************80
#
## R8NSYMM_GEN_TEST tests R8NSYMM_GEN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  
  n = 50
  bin_num = 10
  lamda_dev = 1.0
  lamda_mean = 1.0
  seed = 123456789

  print ( '' )
  print ( 'R8NSYMM_GEN_TEST' )
  print ( '  R8NSYMM_GEN makes an arbitrary size nonsymmetric matrix' )
  print ( '  with known eigenvalues and eigenvectors.' )

  a, ql, qr, lamda, seed = r8nsymm_gen ( n, lamda_mean, lamda_dev, seed )
#
#  Get the eigenvalue range.
#
  lamda_min = np.amin ( lamda )
  lamda_max = np.amax ( lamda )

  print ( '' )
  print ( '  LAMBDA_MIN = %g' % ( lamda_min ) )
  print ( '  LAMBDA_MAX = %g' % ( lamda_max ) )
#
#  Bin the eigenvalues.
#
  bin, bin_limit = r8vec_bin ( n, lamda, bin_num, lamda_min, lamda_max )

  r8bin_print ( bin_num, bin, bin_limit, '  Lambda bins:' )

  if ( False ):
    r8mat_print ( n, n, a, '  The matrix A:' )

  if ( False ):
    r8mat_print ( n, n, qr, '  The eigenvector matrix QR:' )

  aqr = np.dot ( a, qr )

  lamda2 = np.zeros ( n )
  
  for j in range ( 0, n ):
    lamda2[j] = np.linalg.norm ( aqr[:,j] )

  r8vec2_print ( n, lamda, lamda2, '  LAMBDA versus column norms of A*QR:' )

  return

def r8symm_gen ( n, lamda_mean, lamda_dev, seed ):

#*****************************************************************************80
#
## R8SYMM_GEN generates a symmetric matrix with a certain eigenstructure.
#
#  Discussion:
#
#    An R8SYMM is a real symmetric matrix stored using full storage, and
#    using R8 arithmetic.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real LAMBDA_MEAN, the mean value of the normal
#    distribution from which the eigenvalues will be chosen.
#
#    Input, real LAMBDA_DEV, the standard deviation of the normal
#    distribution from which the eigenvalues will be chosen.
#
#    Input/output, integer SEED, a seed for the random
#    number generator.
#
#    Output, real A(N,N), the test matrix.
#
#    Output, real Q(N,N), the eigenvector matrix.
#
#    Output, real LAMBDA(N), the eigenvalue vector.
#
  import numpy as np
#
#  Choose the eigenvalues LAMBDA.
#
  lamda, seed = r8vec_normal_ab ( n, lamda_mean, lamda_dev, seed )
  
  l = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    l[i,i] = lamda[i]
#
#  Get a random orthogonal matrix Q.
#
  q, seed = r8mat_orth_uniform ( n, seed )
#
#  Set A = Q * Lambda*I * Q'.
#
  a = np.dot ( q, np.dot ( l, np.transpose ( q ) ) )

  return a, q, lamda, seed
  
def r8symm_gen_test ( ):

#*****************************************************************************80
#
## R8SYMM_GEN_TEST tests R8SYMM_GEN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 July 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  
  n = 100
  bin_num = 10
  lamda_dev = 1.0
  lamda_mean = 1.0
  seed = 123456789

  print ( '' )
  print ( 'R8SYMM_GEN_TEST' )
  print ( '  R8SYMM_GEN makes an arbitrary size symmetric matrix' )
  print ( '  with known eigenvalues and eigenvectors.' )

  a, q, lamda, seed = r8symm_gen ( n, lamda_mean, lamda_dev, seed )
#
#  Get the eigenvalue range.
#
  lamda_min = np.amin ( lamda )
  lamda_max = np.amax ( lamda )

  print ( '' )
  print ( '  LAMBDA_MIN = %g' % ( lamda_min ) )
  print ( '  LAMBDA_MAX = %g' % ( lamda_max ) )
#
#  Bin the eigenvalues.
#
  bin, bin_limit = r8vec_bin ( n, lamda, bin_num, lamda_min, lamda_max )

  r8bin_print ( bin_num, bin, bin_limit, '  Lambda bins:' )

  if ( False ):
    r8mat_print ( n, n, a, '  The matrix A:' )

  if ( False ):
    r8mat_print ( n, n, q, '  The eigenvector matrix Q:' )

  aq = np.dot ( a, q )

  lamda2 = np.zeros ( n )
  
  for j in range ( 0, n ):
    lamda2[j] = np.linalg.norm ( aq[:,j] )

  r8vec2_print ( n, lamda, lamda2, '  LAMBDA versus column norms of A*Q:' )

  return
def r8vec_bin ( n, x, bin_num, bin_min, bin_max ):

#*****************************************************************************80
#
## R8VEC_BIN computes bins based on a given R8VEC.
#
#  Discussion:
#
#    The user specifies minimum and maximum bin values, BIN_MIN and
#    BIN_MAX, and the number of bins, BIN_NUM.  This determines a
#    "bin width":
#
#      H = ( BIN_MAX - BIN_MIN ) / BIN_NUM
#
#    so that bin I will count all entries X(J) such that
#
#      BIN_LIMIT(I-1) <= X(J) < BIN_LIMIT(I).
#
#    The array X does NOT have to be sorted.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries of X.
#
#    Input, real X(N), an (unsorted) array to be binned.
#
#    Input, integer BIN_NUM, the number of bins.  Two extra bins,
#    #1 and #BIN_NUM+2, count extreme values.
#
#    Input, real BIN_MIN, BIN_MAX, define the range and size
#    of the bins.  BIN_MIN and BIN_MAX must be distinct.
#    Normally, BIN_MIN < BIN_MAX, and the documentation will assume
#    this, but proper results will be computed if BIN_MIN > BIN_MAX.
#
#    Output, integer BIN[0:BIN_NUM+1].
#    BIN(1) counts entries of X less than BIN_MIN.
#    BIN(BIN_NUM+2) counts entries greater than or equal to BIN_MAX.
#    For 2 <= I <= BIN_NUM+1, BIN(I) counts the entries X(J) such that
#      BIN_LIMIT(I-1) <= X(J) < BIN_LIMIT(I).
#    where H is the bin spacing.
#
#    Output, real BIN_LIMIT[0:BIN_NUM], the "limits" of the bins.
#    BIN(I) counts the number of entries X(J) such that
#      BIN_LIMIT(I-1) <= X(J) < BIN_LIMIT(I).
#
  import numpy as np
  from sys import exit
  
  if ( bin_max == bin_min ):
    print ( '' );
    print ( 'R8VEC_BIN - Fatal error!' )
    print ( '  BIN_MIN = BIN_MAX.' )
    exit ( 'R8VEC_BIN - Fatal error!' )

  bin = np.zeros ( bin_num + 2, dtype = np.int32 )

  for i in range ( 0, n ):

    t = ( x[i] - bin_min ) / ( bin_max - bin_min )

    if ( t < 0.0 ):
      j = 0
    elif ( 1.0 <= t ):
      j = bin_num + 1
    else:
      j = 1 + int ( np.floor ( bin_num * t ) )

    bin[j] = bin[j] + 1
#
#  Compute the bin limits.
#
  bin_limit = np.zeros ( bin_num + 1 )
  
  for i in range ( 0, bin_num + 1 ):
    bin_limit[i] = (   ( bin_num - i ) * bin_min  \
                     + (           i ) * bin_max ) \
                     / ( bin_num    )

  return bin, bin_limit

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

  a, seed = r8mat_uniform_ab ( n, n, r8_lo, r8_hi, seed )

  r8mat_print ( n, n, a, '  Matrix A:' )

  a_col = np.zeros ( n )

  for k in range ( 0, n - 1 ):

    print ( '' )
    print ( '  Working on column K = %d' % ( k ) )

    for i in range ( 0, n ):
      a_col[i] = a[i,k]

    v = r8vec_house_column ( n, a_col, k )

    h = r8mat_house_form ( n, v )

    r8mat_print ( n, n, h, '  Householder matrix H:' )

    ha = np.dot ( h, a )

    r8mat_print ( n, n, ha, '  Product H*A:' )
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

def r8vec_normal_ab ( n, mu, sigma, seed ):

#*****************************************************************************80
#
## R8VEC_NORMAL_AB returns a scaled pseudonormal R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real MU, the average value of the PDF.
#
#    Input, real SIGMA, the standard deviation of the PDF.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X(N), the vector of pseudorandom values.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    xi, seed = r8_normal_01 ( seed )
    x[i] = mu + sigma * xi

  return x, seed

def r8vec_normal_ab_test ( ):

#*****************************************************************************80
#
## R8VEC_NORMAL_AB_TEST tests R8VEC_NORMAL_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_NORMAL_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORMAL_AB returns a vector of Normal AB values' )

  n = 10
  mu = 15.0
  sigma = 0.25
  seed = 123456789

  print ( '' )
  print ( '  Mean = %g' % ( mu ) )
  print ( '  Standard deviation = %g' % ( sigma ) )
  print ( '  SEED = %d' % ( seed ) )

  r, seed = r8vec_normal_ab ( n, mu, sigma, seed )

  r8vec_print ( n, r, '  Vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORMAL_AB_TEST:' )
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

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## R8VEC2_PRINT prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of components of the vector.
#
#    Input, real A1(N), A2(N), the vectors to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## R8VEC2_PRINT_TEST tests R8VEC2_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC2_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC2_PRINT prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC2_PRINT_TEST:' )
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

def test_eigen_test ( ):

#*****************************************************************************80
#
## TEST_EIGEN_TEST tests the TEST_EIGEN library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TEST_EIGEN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the TEST_EIGEN library.' )

  r8vec_house_column_test ( )
  r8mat_house_axh_test ( )
  r8mat_orth_uniform_test ( )
  r8nsymm_gen_test ( )
  r8symm_gen_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TEST_EIGEN_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  test_eigen_test ( )
  timestamp ( )
