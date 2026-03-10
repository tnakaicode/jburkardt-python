#! /usr/bin/env python3
#
def asa053_test ( ):

#*****************************************************************************80
#
## asa053_test() tests asa053().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2021
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  
  print ( '' )
  print ( 'asa053_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test asa053().' )

  asa053_test01 ( )
  asa053_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa053_test():' )
  print ( '  Normal end of execution.' )
  print ( '' )
  return

def asa053_test01 ( ):

#*****************************************************************************80
#
## asa053_test01() generates a random Wishart variate.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
   
  print ( '' )
  print ( 'asa053_test01():' )
  print ( '  Generate a single Wishart deviate.' )

  d = np.array ( [ \
    3.0, \
    2.0, 4.0, \
    1.0, 2.0, 5.0 ] )
  n = 1
  npp = 3
 
  print ( '' )
  print ( '  The number of variables is %d' % ( npp ) )
  print ( '  The number of degrees of freedom is %d' % ( n ) )

  r8utp_print ( npp, d, '  The upper Cholesky factor:' )

  sa = wshrt ( d, n, npp )

  r8pp_print ( npp, sa, '  The sample matrix:' )

  return

def asa053_test02 ( ):

#*****************************************************************************80
#
## asa053_test02() averages many Wishart samples.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  
  print ( '' )
  print ( 'asa053_test02():' )
  print ( '  Average many Wishart deviates.' )
  print ( '  Compare to D'' * D * npp / n.' )

  d = np.array( [ \
    3.0, \
    2.0, 4.0, \
    1.0, 2.0, 5.0 ] )
  n = 2
  npp = 3

  print ( '' )
  print ( '  The number of variables is %d' % ( npp ) )
  print ( '  The number of degrees of freedom is %d' % ( n ) )

  r8utp_print ( npp, d, '  The upper Cholesky factor:' )

  s_average = np.zeros ( ( npp * ( npp + 1 ) ) // 2 )

  test_num = 100000
  for i in range ( 0, test_num ):
    sa = wshrt ( d, n, npp )
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

  print ( '' )
  print ( '  Expected results:' )
  print ( sigma )

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

def r8utp_print ( n, a, title ):

#*****************************************************************************80
#
## r8utp_print() prints a R8UTP matrix.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2017
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
#    real A((N*(N+1))/2), the matrix.
#
#    string TITLE, a title to be printed.
#
  r8utp_print_some ( n, a, 1, 1, n, n, title )

  return

def r8utp_print_some ( n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8utp_print_some() prints some of an R8UTP matrix.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2017
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
#    real A((N*(N+1))/2), the matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
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
    print ( '  Row' )
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

def rnorm ( ):

#*****************************************************************************80
#
## rnorm() returns two independent standard random normal deviates.
#
#  Discussion:
#
#    This routine sets U1 and U2 to two independent standardized 
#    random normal deviates.   This is a version of the 
#    method given in Knuth.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2017
#
#  Author:
#
#    Original FORTRAN77 version by William Smith, Ronald Hocking.
#    This version by John Burkardt.
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
#  Output:
#
#    real U1, U2, two standard random normal deviates.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  while ( True ):

    x = rng.random ( )
    y = rng.random ( )

    x = 2.0 * x - 1.0
    y = 2.0 * y - 1.0
    s = x * x + y * y

    if ( s <= 1.0 ):
      break

  s = np.sqrt ( - 2.0 * np.log ( s ) / s )
  u1 = x * s
  u2 = y * s

  return u1, u2

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

  return
  
def wshrt ( d, n, npp ):

#*****************************************************************************80
#
## wshrt() returns a random Wishart variate.
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
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 January 2017
#
#  Author:
#
#    Original FORTRAN77 version by William Smith, Ronald Hocking.
#    This version by John Burkardt.
#
#  Reference:
#
#    William Smith, Ronald Hocking,
#    Algorithm AS 53, Wishart Variate Generator,
#    Applied Statistics,
#    Volume 21, Number 3, pages 341-345, 1972.
#
#  Input:
#
#    real D(NPP*(NPP+1)/2), the upper triangular array that
#    represents the Cholesky factor of the correlation matrix SIGMA.
#    D is stored in column-major form.
#
#    integer N, the number of degrees of freedom.
#    1 <= N <= NPP.
#
#    integer NPP, the size of variables.
#
#  Output:
#
#    real SA(NPP*(NPP+1)/2), a sample from the Wishart distribution.
#
  import numpy as np
  
  k = 0
#
#  Load SB with independent normal (0, 1) variates.
#
  nnp = ( npp * ( npp + 1 ) ) // 2
  sb = np.zeros ( nnp )

  while ( k < nnp ):

    u1, u2 = rnorm ( )

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

  return sa
  
if ( __name__ == '__main__' ):
  timestamp ( )
  asa053_test ( )
  timestamp ( )

