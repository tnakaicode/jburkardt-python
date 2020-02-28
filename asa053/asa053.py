#! /usr/bin/env python3
#
def asa053_test01 ( ):

#*****************************************************************************80
#
## ASA053_TEST01 generates a random Wishart variate.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  
  print ( '' )
  print ( 'ASA053_TEST01' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Generate a single Wishart deviate.' )

  d = np.array ( [ \
    3.0, \
    2.0, 4.0, \
    1.0, 2.0, 5.0 ] )
  n = 1
  npp = 3
  seed = 123456789

  print ( '' )
  print ( '  The number of variables is %d' % ( npp ) )
  print ( '  The number of degrees of freedom is %d' % ( n ) )

  r8utp_print ( npp, d, '  The upper Cholesky factor:' )

  sa, seed = wshrt ( d, n, npp, seed )

  r8pp_print ( npp, sa, '  The sample matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ASA053_TEST01:' )
  print ( '  Normal end of execution.' )
  print ( '' )
  return

def asa053_test02 ( ):

#*****************************************************************************80
#
## ASA053_TEST02 averages many Wishart samples.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  
  print ( '' )
  print ( 'ASA053_TEST02' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Average many Wishart deviates.' )
  print ( '  Compare to D'' * D * npp / n.' )

  d = np.array( [ \
    3.0, \
    2.0, 4.0, \
    1.0, 2.0, 5.0 ] )
  n = 2
  npp = 3
  seed = 123456789

  print ( '' )
  print ( '  The number of variables is %d' % ( npp ) )
  print ( '  The number of degrees of freedom is %d' % ( n ) )

  r8utp_print ( npp, d, '  The upper Cholesky factor:' )

  s_average = np.zeros ( ( npp * ( npp + 1 ) ) // 2 )

  test_num = 100000
  for i in range ( 0, test_num ):
    sa, seed = wshrt ( d, n, npp, seed )
    s_average = s_average + sa

  s_average = s_average / float ( test_num )

  r8pp_print ( npp, s_average, '  The averaged matrix:' )
#
#  Compare the result to ( D' * D ) * npp / n.
#
  sigma = np.zeros ( [ npp, npp ] )
  
  for i in range ( 0, npp ):
    for j in range ( 0, npp ):
      for k in range ( 0, min ( i, j )+ 1 ):
        ki = k + ( i * ( i + 1 ) ) // 2
        kj = k + ( j * ( j + 1 ) ) // 2
        sigma[i,j] = sigma[i,j] + d[ki] * d[kj]
      sigma[i,j] = sigma[i,j] * float ( npp ) / float ( n )

  r8mat_print ( npp, npp, sigma, '  Expected results:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'ASA053_TEST02:' )
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
    print ( '  Row', end = '' )

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

def r8pp_print ( n, a, title ):

#*****************************************************************************80
#
## R8PP_PRINT prints a R8PP matrix.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 June 2016
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
#    Input, real A((N*(N+1))/2), the R8PP matrix.
#
#    Input, string TITLE, a title to be printed.
#
  r8pp_print_some ( n, a, 0, 0, n - 1, n - 1, title )

  return
  
def r8pp_print_some ( n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8PP_PRINT_SOME prints some of a R8PP matrix.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#   16 June 2016
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
#    Input, real A((N*(N+1))/2), the R8PP matrix.
#
#    Input, integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    Input, string TITLE, a title.
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
    print ( '  Row', end = '' )

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

def r8utp_print ( n, a, title ):

#*****************************************************************************80
#
## R8UTP_PRINT prints a R8UTP matrix.
#
#  Discussion:
#
#    The R8UTP storage format is appropriate for an upper triangular
#    matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2017
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
#    Input, real A((N*(N+1))/2), the matrix.
#
#    Input, string TITLE, a title to be printed.
#
  r8utp_print_some ( n, a, 1, 1, n, n, title )

  return

def r8utp_print_some ( n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8UTP_PRINT_SOME prints some of an R8UTP matrix.
#
#  Discussion:
#
#    The R8UTP storage format is appropriate for an upper triangular
#    matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array of length (N*(N+1))/2,
#    which contains (A11,A12,A22,A13,A23,A33,A14,...,ANN)  
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2017
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
#    Input, real A((N*(N+1))/2), the matrix.
#
#    Input, integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )

  if ( n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  incx = 5
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( jlo, jhi + 1, incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )
    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row', end = '' )
#
#  Determine the range of the rows in this strip.
#
    inc = j2hi + 1 - j2lo
    i2lo = max ( ilo, 1 )
    i2hi = min ( ihi, n )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        if ( j < i ):
          print ( '              ', end = '' )
        else:
          print ( '%12g  ' % ( a[i-1+(j*(j-1))//2] ), end = '' )

      print ( '' )
      
  return

def rnorm ( seed ):

#*****************************************************************************80
#
## RNORM returns two independent standard random normal deviates.
#
#  Discussion:
#
#    This routine sets U1 and U2 to two independent standardized 
#    random normal deviates.   This is a version of the 
#    method given in Knuth.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2017
#
#  Author:
#
#    Original FORTRAN77 version by William Smith, Ronald Hocking.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Donald Knuth,
#    The Art of Computer Programming,
#    Volume 2, Seminumerical Algorithms,
#    Third Edition,
#    Addison Wesley, 1997,
#    ISBN: 0201896842,
#    LC: QA76.6.K64.
#
#  Parameters:
#
#    Input/output, integer SEED, a seed for the random number generator.
#
#    Output, real U1, U2, two standard random normal deviates.
#
  import numpy as np
  
  while ( True ):

    x, seed = r8_uniform_01 ( seed )
    y, seed = r8_uniform_01 ( seed )

    x = 2.0 * x - 1.0
    y = 2.0 * y - 1.0
    s = x * x + y * y

    if ( s <= 1.0 ):
      break

  s = np.sqrt ( - 2.0 * np.log ( s ) / s )
  u1 = x * s
  u2 = y * s

  return u1, u2, seed

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
  
def wshrt ( d, n, npp, seed ):

#*****************************************************************************80
#
## WSHRT returns a random Wishart variate.
#
#  Discussion:
#
#    This routine is a Wishart variate generator.  
#
#    On output, SA is an upper-triangular matrix of size NPP * NPP,
#    written in linear form, column ordered, whose elements have a 
#    Wishart(N, SIGMA) distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 January 2017
#
#  Author:
#
#    Original FORTRAN77 version by William Smith, Ronald Hocking.
#    Python version by John Burkardt.
#
#  Reference:
#
#    William Smith, Ronald Hocking,
#    Algorithm AS 53, Wishart Variate Generator,
#    Applied Statistics,
#    Volume 21, Number 3, pages 341-345, 1972.
#
#  Parameters:
#
#    Input, real D(NPP*(NPP+1)/2), the upper triangular array that
#    represents the Cholesky factor of the correlation matrix SIGMA.
#    D is stored in column-major form.
#
#    Input, integer N, the number of degrees of freedom.
#    1 <= N <= NPP.
#
#    Input, integer NPP, the size of variables.
#
#    Input/output, integer SEED, a seed for the random number generator.
#
#    Output, real SA(NPP*(NPP+1)/2), a sample from the Wishart distribution.
#
  import numpy as np
  
  k = 0
#
#  Load SB with independent normal (0, 1) variates.
#
  nnp = ( npp * ( npp + 1 ) ) // 2
  sb = np.zeros ( nnp )

  while ( k < nnp ):

    u1, u2, seed = rnorm ( seed )

    sb[k] = u1
    k = k + 1

    if ( k < nnp ):
      sb[k] = u2
      k = k + 1
#
#  Load diagonal elements with square root of chi-square variates.
#
  sa = np.zeros ( nnp )

  ns = 0

  for i in range ( 1, npp + 1 ):

    df = float ( npp - i + 1 )
    ns = ns + i
    u1 = 2.0 / ( 9.0 * df )
    u2 = 1.0 - u1
    u1 = np.sqrt ( u1 )
#
#  Wilson-Hilferty formula for approximating chi-square variates:
#  The original code did not take the absolute value!
#
    sb[ns-1] = np.sqrt ( df * abs ( ( u2 + sb[ns-1] * u1 ) ** 3 ) )

  rn = float ( n )
  nr = 1

  for i in range ( 1, npp + 1 ):
    nr = nr + i - 1
    for j in range ( i, npp + 1 ):
      ip = nr
      nq = ( j * ( j - 1 ) ) // 2 + i - 1
      c = 0.0
      for k in range ( i, j + 1 ):
        ip = ip + k - 1
        nq = nq + 1
        c = c + sb[ip-1] * d[nq-1]
      sa[ip-1] = c

  for i in range ( 1, npp + 1 ):
    ii = npp - i + 1
    nq = nnp - npp
    for j in range ( 1, i + 1 ):
      ip = ( ii * ( ii - 1 ) ) // 2
      c = 0.0
      for k in range ( i, npp + 1 ):
        ip = ip + 1
        nq = nq + 1
        c = c + sa[ip-1] * sa[nq-1]
      sa[nq-1] = c / rn
      nq = nq - 2 * npp + i + j - 1

  return sa, seed
  
if ( __name__ == '__main__' ):
  timestamp ( )
  asa053_test01 ( )
  asa053_test02 ( )
  r8mat_print_test ( )
  timestamp ( )


