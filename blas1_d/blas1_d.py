#! /usr/bin/env python3
#
def dasum ( n, x, incx ):

#*****************************************************************************80
#
## DASUM takes the sum of the absolute values of a vector.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Jack Dongarra, Cleve Moler, Jim Bunch and Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
#    Basic Linear Algebra Subprograms for Fortran Usage,
#    Algorithm 539,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 3, September 1979, pages 308-323.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real X(*), the vector to be examined.
#
#    Input, integer INCX, the increment between successive entries of X.
#
#    Output, real VALUE, the sum of the absolute values of X.
#
  value = 0.0
  i = 0
  for j in range ( 0, n ):
    value = value + abs ( x[i] )
    i = i + incx

  return value

def dasum_test ( ):

#*****************************************************************************80
#
## DASUM_TEST tests DASUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  nx = 10

  x = np.zeros ( nx )

  for i in range ( 0, nx ):
    x[i] = ( - 1.0 ) ** ( i + 1 ) * 2.0 * float ( i + 1 ) 

  print ( '' )
  print ( 'DASUM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DASUM adds the absolute values of elements of a vector.' )

  r8vec_print ( nx, x, '  Vector x:' )

  print ( '' )
  print ( '  DASUM ( NX,    X, 1     ) = %g' % ( dasum ( nx,    x, 1     ) ) )
  print ( '  DASUM ( NX//2, X, 2     ) = %g' % ( dasum ( nx//2, x, 2     ) ) )
  print ( '  DASUM ( 2,     X, NX//2 ) = %g' % ( dasum ( 2,     x, nx//2 ) ) )

  lda = 6
  ma = 5
  na = 4

  a = np.zeros ( [ lda, na ] )

  for i in range ( 0, ma ):
    for j in range ( 0, na ):
      a[i,j] = ( - 1.0 ) ** ( i + j ) * float ( 10 * ( i + 1 ) + j + 1 )

  print ( '' )
  print ( '  Matrix A:' )
  print ( '' )
  for i in range ( 0, ma ):
    for j in range ( 0, na ):
      print ( '  %12g' % ( a[i,j] ), end = '' )
    print ( '' )

  print ( '' )
  print ( '  DASUM(MA,A(1:MA,2),1) = %g' % ( dasum ( ma, a[0:ma,1], 1 ) ) )
  print ( '  DASUM(NA,A(2,1:NA),1) = %g' % ( dasum ( na, a[1,0:na], 1 ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DASUM_TEST' )
  print ( '  Normal end of execution.' )
  return

def daxpy ( n, s, x, incx, y, incy ):

#*****************************************************************************80
#
## DAXPY adds a constant times one vector to another.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 September 2016
#
#  Author:
#
#    Python version by John Burkardt.
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
#    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
#    Basic Linear Algebra Subprograms for Fortran Usage,
#    Algorithm 539,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 3, September 1979, pages 308-323.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real S, the multiplier.
#
#    Input, real X(*), the vector to be scaled and added to Y.
#
#    Input, integer INCX, the increment between successive entries of X.
#
#    Input, real Y(*), the vector to which a
#    multiple of X is to be added.
#
#    Input, integer INCY, the increment between successive entries of Y.
#
#    Output, real Z(*), the vector X+S*Y.
#
  import numpy as np

  z = np.zeros ( n )

  i = 0
  j = 0
  for k in range ( 0, n ):
    z[k] = y[j] + s * x[i]
    i = i + incx
    j = j + incy

  return z

def daxpy_test ( ):

#*****************************************************************************80
#
## DAXPY_TEST tests DAXPY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  nx = 6
  x = np.zeros ( nx )
  for i in range ( 0, nx ):
    x[i] = float ( i + 1 )

  ny = 6
  y = np.zeros ( ny )
  for i in range ( 0, ny ):
    y[i] = float ( 100 * ( i + 1 ) )

  print ( '' )
  print ( 'DAXPY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DAXPY adds a multiple of vector X to vector Y.' )

  r8vec_print ( nx, x, '  X:' )
  r8vec_print ( ny, y, '  Y:' )

  nz = 6
  s = 1.0
  z = daxpy ( nz, s, x, 1, y, 1 )
  print ( '' )
  print ( '  z = daxpy ( %d, %f, x, 1, y, 1 )' % ( nz, s ) )
  print ( '' )
  for i in range ( 0, nz ):
    print ( '  %6d  %12f' % ( i, z[i] ) )

  nz = 6
  s = - 2.0
  z = daxpy ( nz, s, x, 1, y, 1 )
  print ( '' )
  print ( '  z = daxpy ( %d, %f, x, 1, y, 1 )' % ( nz, s ) )
  print ( '' )
  for i in range ( 0, nz ):
    print ( '  %6d  %12f' % ( i, z[i] ) )

  nz = 3
  s = + 3.0
  z = daxpy ( nz, s, x, 2, y, 1 )
  print ( '' )
  print ( '  z = daxpy ( %d, %f, x, 2, y, 1 )' % ( nz, s ) )
  print ( '' )
  for i in range ( 0, nz ):
    print ( '  %6d  %12f' % ( i, z[i] ) )

  nz = 3
  s = - 4.0
  z = daxpy ( 3, s, x, 1, y, 2 )
  print ( '' )
  print ( '  z = daxpy ( %d, %f, x, 1, y, 2 )' % ( nz, s ) )
  print ( '' )
  for i in range ( 0, nz ):
    print ( '  %6d  %12f' % ( i, z[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DAXPY_TEST' )
  print ( '  Normal end of execution.' )
  return

def dcopy ( n, dx, incx, dy, incy ):

#*****************************************************************************80
#
## DCOPY copies a vector X to a vector Y.
#
#  Discussion:
#
#    The routine uses unrolled loops for increments equal to one.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 September 2018
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Jack Dongarra, Cleve Moler, Jim Bunch and Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
#    Basic Linear Algebra Subprograms for Fortran Usage,
#    Algorithm 539,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 3, September 1979, pages 308-323.
#
#  Parameters:
#
#    Input, integer N, the number of elements in DX and DY.
#
#    Input, real DX(*), the first vector.
#
#    Input, integer INCX, the increment between successive entries of DX.
#
#    Input, real DY(*), the second vector, into which elements are copied.
#
#    Input, integer INCY, the increment between successive entries of DY.
#
#    Input, real DY(*), the second vector, into which data will be copied.
#
#    Output, real DY(*), the second vector, with elements copied from DX.
#
  if ( n <= 0 ):
    return dy

  if ( incx == 1 and incy == 1 ):

    m = ( n % 7 )

    if ( m != 0 ):
      for i in range ( 0, m ):
        dy[i] = dx[i]

    for i in range ( m, n, 7 ):
      dy[i] = dx[i]
      dy[i + 1] = dx[i + 1]
      dy[i + 2] = dx[i + 2]
      dy[i + 3] = dx[i + 3]
      dy[i + 4] = dx[i + 4]
      dy[i + 5] = dx[i + 5]
      dy[i + 6] = dx[i + 6]

  else:

    if ( 0 <= incx ):
      ix = 0
    else:
      ix = ( - n + 1 ) * incx

    if ( 0 <= incy ):
      iy = 0
    else:
      iy = ( -n + 1 ) * incy

    for i in range ( 0, n ):
      dy[iy] = dx[ix]
      ix = ix + incx
      iy = iy + incy

  return dy

def dcopy_test ( ):

#*****************************************************************************80
#
## DCOPY_TEST demonstrates DCOPY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'DCOPY_TEST' )
  print ( '  DCOPY copies one vector into another.' )
  print ( '' )

  x = np.zeros ( 10 )
  for i in range ( 0, 10 ):
    x[i] = i + 1

  y = np.zeros ( 10 )
  for i in range ( 0, 10 ):
    y[i] = 10 * ( i + 1 )

  a = np.zeros ( [ 5, 5 ] )

  for i in range ( 0, 5 ):
    for j in range ( 0, 5 ):
      a[i,j] = 10 * ( i + 1 ) + ( j + 1 )

  print ( '' )
  print ( '  X = ' )
  print ( '' )
  for i in range ( 0, 10 ):
    print ( '  %6d  %12f' % ( i, x[i] ) )
  print ( '' )
  print ( '  Y = ' )
  print ( '' )
  for i in range ( 0, 10 ):
    print ( '  %6d  %12f' % ( i, y[i] ) )
  print ( '' )
  print ( '  A = ' )
  print ( '' )
  for i in range ( 0, 5 ):
    for j in range ( 0, 5 ):
      print ( '  %8f' % a[i,j], end = '' )
    print ( '' )

  y = dcopy ( 5, x, 1, y, 1 )
  print ( '' )
  print ( '  DCOPY ( 5, X, 1, Y, 1 )' )
  print ( '' )
  for i in range ( 0, 10 ):
    print ( '  %6d  %12f' % ( i, y[i] ) )

  for i in range ( 0, 10 ):
    y[i] = 10 * ( i + 1 )

  y = dcopy ( 3, x, 2, y, 3 )
  print ( '' )
  print ( '  DCOPY ( 3, X, 2, Y, 3 )' )
  print ( '' )
  for i in range ( 0, 10 ):
    print ( '  %6d  %12f' % ( i, y[i] ) )

  a[0:5,0] = dcopy ( 5, x, 1, a[0:5,0], 1 )
  print ( '' )
  print ( '  A[0:5,0] = DCOPY ( 5, X, 1, A[0:5,0], 1 )' )
  print ( '' )
  print ( '' )
  print ( '  A = ' )
  print ( '' )
  for i in range ( 0, 5 ):
    for j in range ( 0, 5 ):
      print ( '  %8f' % a[i,j], end = '' )
    print ( '' )

  for i in range ( 0, 5 ):
    for j in range ( 0, 5 ):
      a[i,j] = 10 * ( i + 1 ) + ( j + 1 )

  a[0,0:5] = dcopy ( 5, x, 2, a[0,0:5], 1 )
  print ( '' )
  print ( '  A[0,0:5] = DCOPY ( 5, X, 2, A[0,0:5], 1 )' )
  print ( '' )
  print ( '  A = ' )
  print ( '' )
  for i in range ( 0, 5 ):
    for j in range ( 0, 5 ):
      print ( '  %8f' % a[i,j], end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'DCOPY_TEST' )
  print ( '  Normal end of execution.' )
  return

def ddot ( n, x, incx, y, incy ):

#*****************************************************************************80
#
## DDOT forms the dot product of two vectors.
#
#  Discussion:
#
#    This routine uses unrolled loops for increments equal to one.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 September 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Jack Dongarra, Cleve Moler, Jim Bunch and Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
#    Basic Linear Algebra Subprograms for Fortran Usage,
#    Algorithm 539,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 3, September 1979, pages 308-323.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vectors.
#
#    Input, real X(*), the first vector.
#
#    Input, integer INCX, the increment between successive entries in DX.
#
#    Input, real Y(*), the second vector.
#
#    Input, integer INCY, the increment between successive entries in DY.
#
#    Output, real VALUE, the sum of the product of the
#    corresponding entries of DX and DY.
#
  value = 0.0

  i = 0
  j = 0
  for k in range ( 0, n ):
    value = value + x[i] * y[j]
    i = i + incx
    j = j + incy

  return value

def ddot_test ( ):

#*****************************************************************************80
#
## DDOT_TEST demonstrates DDOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  lda = 10
  ldb = 7
  ldc = 6

  print ( '' )
  print ( 'DDOT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DDOT computes the dot product of vectors.' )

  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( i + 1 )

  y = np.zeros ( n )
  for i in range ( 0, n ):
    y[i] = float ( - ( i + 1 ) )

  a = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = float ( i + 1 + j + 1 )

  b = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      b[i,j] = float ( i - j )
#
#  Compute a simple dot product of two vectors:
#
  s = ddot ( n, x, 1, y, 1 )

  print ( '' )
  print ( '  ddot ( n, x, 1, y, 1 ) = %g' % ( s ) )
#
#  To multiply a ROW of a matrix A times a vector X:
#
  s = ddot ( n, a[1,0:n], 1, x, 1 )

  print ( '' )
  print ( '  ddot ( n, a[1,0:n], 1, x, 1 ) = %g' % ( s ) )
#
#  Product of a column of A and a vector:
#
  s = ddot ( n, a[0:n,1], 1, x, 1 )

  print ( '' )
  print ( '  ddot ( n, a[0:n,1], 1, x, 1 ) = %g' % ( s ) )
#
#  Here's how matrix multiplication, c = a*b, could be done
#  with DDOT:
#
  c = np.zeros ( [ n, n ] )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      c[i,j] = ddot ( n, a[i,0:n], 1, b[0:n,j], 1 )

  print ( '' )
  print ( '  Matrix product computed with c[i,j] = ddot ( n, a[i,0:n], 1, b[0:n,j), 1 ):' )
  print ( '' )
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      print ( '  %12f' % ( c[i,j] ), end = '' )
    print ( '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'DDOT_TEST' )
  print ( '  Normal end of execution.' )
  return

def dmach ( job ):

#*****************************************************************************80
#
## DMACH computes machine parameters of floating point arithmetic.
#
#  Discussion:
#
#    This routine uses double precision real arithmetic.
#
#    Assume the computer has
#
#      B = base of arithmetic;
#      T = number of base B digits;
#      L = smallest possible exponent;
#      U = largest possible exponent;
#
#    then
#
#      EPS = B^(1-T)
#      TINY = 100.0 * B^(-L+T)
#      HUGE = 0.01 * B^(U-T)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 September 2016
#
#  Author:
#
#    FORTRAN77 version by Jack Dongarra.
#    Python version by John Burkardt
#
#  Reference:
#
#    Jack Dongarra, Jim Bunch, Cleve Moler, Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979,
#    ISBN13: 978-0-898711-72-1,
#    LC: QA214.L56.
#
#    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
#    Basic Linear Algebra Subprograms for FORTRAN usage,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 3, pages 308-323, 1979.
#
#  Parameters:
#
#    Input, integer JOB:
#    1, EPS is desired;
#    2, TINY is desired;
#    3, HUGE is desired.
#
#    Output, double precision DMACH, the requested value.
#
  from sys import exit

  eps = 1.0

  while ( True ):
    eps = eps / 2.0
    s = 1.0 + eps
    if ( s <= 1.0 ):
      break

  eps = 2.0 * eps

  if ( job == 1 ):
    return eps

  s = 1.0

  while ( True ):

    tiny = s
    s = s / 16.0
    if ( s * 1.0 == 0.0 ):
      break

  tiny = ( tiny / eps ) * 100.0

  if ( job == 2 ):
    return tiny

  huge = 1.0 / tiny

  if ( job == 3 ):
    return huge

  print ( '' )
  print ( 'DMACH - Fatal error!' )
  print ( '  Illegal value of JOB = %d' % ( job ) )
  exit ( 'DMACH - Fatal error!' )

def dmach_test ( ):

#*****************************************************************************80
#
## DMACH_TEST demonstrates DMACH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 September 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'DMACH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DMACH returns some approximate machine numbers.' )
  print ( '' )
  job = 1
  print ( '  dmach(1) = eps =  %g' % ( dmach ( job ) ) )
  job = 2
  print ( '  dmach(2) = tiny = %g' % ( dmach ( job ) ) )
  job = 3
  print ( '  dmach(3) = huge = %g' % ( dmach ( job ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DMACH_TEST' )
  print ( '  Normal end of execution.' )
  return

def dnrm2 ( n, x, incx ):

#*****************************************************************************80
#
## DNRM2 returns the euclidean norm of a vector.
#
#  Discussion:
#
#     DNRM2 ( X ) = sqrt ( X' * X )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 June 2005
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Jack Dongarra, Cleve Moler, Jim Bunch and Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
#    Basic Linear Algebra Subprograms for Fortran Usage,
#    Algorithm 539,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 3, September 1979, pages 308-323.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real X(*), the vector whose norm is to be computed.
#
#    Input, integer INCX, the increment between successive entries of X.
#
#    Output, real VALUE, the Euclidean norm of X.
#
  import numpy as np

  value = 0.0

  if ( n < 1 ):

    pass

  elif ( n == 1 ):

    value = abs ( x[0] )

  else:

    scale = 0.0
    ssq = 1.0
    i = 0

    for k in range ( 0, n ):

      if ( x[i] != 0.0 ):

        absxi = abs ( x[i] )

        if ( scale < absxi ):
          ssq = 1.0 + ssq * ( scale / absxi ) ** 2
          scale = absxi
        else:
          ssq = ssq + ( absxi / scale ) ** 2

      i = i + incx

    value  = scale * np.sqrt ( ssq )

  return value

def dnrm2_test ( ):

#*****************************************************************************80
#
## DNRM2_TEST demonstrates DNRM2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5
  lda = n + 5
#
#  These parameters illustrate the fact that matrices are typically
#  dimensioned with more space than the user requires.
#
  print ( '' )
  print ( 'DNRM2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DNRM2 computes the Euclidean norm of a vector.' )
#
#  Compute the euclidean norm of a vector:
#
  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( i + 1 )

  r8vec_print ( n, x, '  x:' )

  incx = 1
  s = dnrm2 ( n, x, incx )

  print ( '' )
  print ( '  dnrm2 ( n, x, incx ) = %g' % ( s  ) )
#
#  Compute the euclidean norm of a row or column of a matrix:
#
  n = 5
  a = np.zeros ( [ 10, 10 ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = float ( i + 1 + j + 1 )

  incx = 1
  s = dnrm2 ( n, a[1,0:n], incx )

  print ( '' )
  print ( '  dnrm2 ( n, a[1,0:n], incx ) = %g' % ( s ) )

  incx = 1
  s = dnrm2 ( n, a[0:n,1], incx )

  print ( '' )
  print ( '  dnrm2 ( n, a[0:n,1], incx ) = %g' % ( s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DNRM2_TEST' )
  print ( '  Normal end of execution.' )
  return

def drot ( n, x, incx, y, incy, c, s ):

#*****************************************************************************80
#
## DROT applies a plane rotation.
#
#  Discussion:
#
#    Note that the FORTRAN version of this function allowed users to pass in
#    X and Y data that was noncontiguous, (such as rows of a FORTRAN matrix).
#    The rotated data overwrote the input data, and so it might therefore
#    also be noncontiguous.
#
#    This function does not assume that the output overwrites the input,
#    and treats the output vectors as new items of length exactly N.
#
#    Note, moreover, that Python does NOT allow a matrix to be treated as a 
#    vector in quite the simple way that FORTRAN does.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Jack Dongarra, Cleve Moler, Jim Bunch and Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
#    Basic Linear Algebra Subprograms for Fortran Usage,
#    Algorithm 539,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 3, September 1979, pages 308-323.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vectors.
#
#    Input, real X(INCX*N), one of the vectors to be rotated.
#
#    Input, integer INCX, the increment between successive entries of X.
#
#    Input, real Y(INCX*N), one of the vectors to be rotated.
#
#    Input, integer INCY, the increment between successive elements of Y.
#
#    Input, real C, S, parameters (presumably the cosine and
#    sine of some angle) that define a plane rotation.
#
#    Output, real XR(N), the rotated vector.
#
#    Output, real YR(N), the rotated vector.
#
  import numpy as np

  xr = np.zeros ( n )
  yr = np.zeros ( n )

  if ( n <= 0 ):

    pass

  elif ( incx == 1 and incy == 1 ):

    xr[0:n] = c * x[0:n] + s * y[0:n]
    yr[0:n] = c * y[0:n] - s * x[0:n]

  else:

    if ( 0 <= incx ):
      ix = 0
    else:
      ix = ( - n + 1 ) * incx

    if ( 0 <= incy ):
      iy = 0
    else:
      iy = ( - n + 1 ) * incy

    for i in range ( 0, n ):
      xr[ix] = c * x[ix] + s * y[iy]
      yr[iy] = c * y[iy] - s * x[ix]
      ix = ix + incx
      iy = iy + incy

  return xr, yr

def drot_test ( ):

#*****************************************************************************80
#
## DROT_TEST tests DROT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 6
  x = np.zeros ( n )
  y = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = float ( i + 1 )
    y[i] = x[i] * x[i] - 12.0
 
  print ( '' )
  print ( 'DROT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DROT carries out a Givens rotation.' )
  print ( '' )
  print ( '  Vectors X and Y' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %14.6g  %14.6g' % ( i, x[i], y[i] ) )

  c = 0.5
  s = np.sqrt ( 1.0 - c * c )
  xr, yr = drot ( n, x, 1, y, 1, c, s )
  print ( '' )
  print ( '  xr, yr = drot ( n, x, 1, y, 1, %g, %g )' % ( c, s ) )
  print ( '' )
  print ( '  Rotated vectors XR and YR' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %14.6g  %14.6g' % ( i, xr[i], yr[i] ) )

  t = np.arctan2 ( y[0], x[0] )
  c = np.cos ( t )
  s = np.sin ( t )
  xr, yr = drot ( n, x, 1, y, 1, c, s )
  print ( '' )
  print ( '  xr, yr = drot ( n, x, 1, y, 1, %g, %g )' % ( c, s ) )
  print ( '' )
  print ( '  Rotated vectors XR and YR' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d  %14.6g  %14.6g' % ( i, xr[i], yr[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DROT_TEST' )
  print ( '  Normal end of execution.' )
  return

def drotg ( a, b ):

#*****************************************************************************80
#
## DROTG constructs a Givens plane rotation.
#
#  Discussion:
#
#    Given values A and B, this routine computes
#
#    SIGMA = sign ( A ) if abs ( A ) >  abs ( B )
#          = sign ( B ) if abs ( A ) <= abs ( B )
#
#    R     = SIGMA * ( A * A + B * B )
#
#    C = A / R if R is not 0
#      = 1     if R is 0
#
#    S = B / R if R is not 0,
#        0     if R is 0.
#
#    The computed numbers then satisfy the equation
#
#    (  C  S ) ( A ) = ( R )
#    ( -S  C ) ( B ) = ( 0 )
#
#    The routine also computes
#
#    Z = S     if abs ( A ) > abs ( B ),
#      = 1 / C if abs ( A ) <= abs ( B ) and C is not 0,
#      = 1     if C is 0.
#
#    The single value Z encodes C and S, and hence the rotation:
#
#    If Z = 1, set C = 0 and S = 1
#    If abs ( Z ) < 1, set C = sqrt ( 1 - Z * Z ) and S = Z
#    if abs ( Z ) > 1, set C = 1/ Z and S = sqrt ( 1 - C * C )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Jack Dongarra, Cleve Moler, Jim Bunch and Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
#    Basic Linear Algebra Subprograms for Fortran Usage,
#    Algorithm 539,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 3, September 1979, pages 308-323.
#
#  Parameters:
#
#    Input, real A, B, the values A and B.
#
#    Output, real C, S, the cosine and sine of the Givens rotation.
#
#    Output, real R, Z, the values R and Z.
#
  import numpy as np

  if ( abs ( b ) < abs ( a ) ):
    roe = a
  else:
    roe = b

  scale = abs ( a ) + abs ( b )

  if ( scale == 0.0 ):
    c = 1.0
    s = 0.0
    r = 0.0
  else:
    r = scale * np.sqrt ( ( a / scale ) ** 2 + ( b / scale ) ** 2 )
    if ( roe < 0.0 ):
      r = - r
    c = a / r
    s = b / r

  if ( 0.0 < abs ( c ) and abs ( c ) <= s ):
    z = 1.0 / c
  else:
    z = s

  return c, s, r, z

def drotg_test ( ):

#*****************************************************************************80
#
## DROTG_TEST tests DROTG.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 September 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  test_num = 5

  print ( '' )
  print ( 'DROTG_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DROTG generates a real Givens rotation' )
  print ( '    (  C  S ) * ( A ) = ( R )' )
  print ( '    ( -S  C )   ( B )   ( 0 )' )
  print ( '' )

  seed = 123456789

  for test in range ( 0, test_num ):

    a, seed = r8_uniform_01 ( seed )
    b, seed = r8_uniform_01 ( seed )

    c, s, r, z = drotg ( a, b )

    print ( '' )
    print ( '  A =  %g  B =  %g' % ( a, b ) )
    print ( '  C =  %g  S =  %g' % ( c, s ) )
    print ( '  R =  %g  Z =  %g' % ( r, z ) )
    print ( '   C*A+S*B = %g' % (  c * a + s * b ) )
    print ( '  -S*A+C*B = %g' % ( -s * a + c * b ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DROTG_TEST' )
  print ( '  Normal end of execution.' )
  return

def dscal ( n, s, x, incx ):

#*****************************************************************************80
#
## DSCAL scales a vector by a constant.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 September 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Jack Dongarra, Cleve Moler, Jim Bunch and Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979.
#
#    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
#    Basic Linear Algebra Subprograms for Fortran Usage,
#    Algorithm 539,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 3, September 1979, pages 308-323.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real S, the multiplier.
#
#    Input, real X(*), the vector to be scaled.
#
#    Input, integer INCX, the increment between successive entries of X.
#
#    Output, real Y(N), the scaled vector.
#
  import numpy as np

  y = np.zeros ( n )

  i = 0
  for j in range ( 0, n ):
    y[j] = s * x[i]
    i = i + incx

  return y

def dscal_test ( ):

#*****************************************************************************80
#
## DSCAL_TEST tests DSCAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 6
  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = float ( i + 1 )

  print ( '' )
  print ( 'DSCAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  DSCAL multiplies a vector X by a scalar S.' )

  r8vec_print ( n, x, '  x:' )

  n = 6
  s = 5.0
  y = dscal ( n, s, x, 1 )
  r8vec_print ( n, y, '  y = dscal ( 6, 5.0, x, 1 )' )

  n = 3
  s = -2.0
  y = dscal ( n, s, x, 2 )
  r8vec_print ( n, y, '  y = dscal ( 3, -2.0, x, 2 )' )
#
#  Terminate.
#
  print ( '' )
  print ( 'DSCAL_TEST' )
  print ( '  Normal end of execution.' )
  return

def idamax ( n, x, incx ):

#*****************************************************************************80
#
## IDAMAX finds the index of the vector element of maximum absolute value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 September 2016
#
#  Author:
#
#    Python version by John Burkardt
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
#    Charles Lawson, Richard Hanson, David Kincaid, Fred Krogh,
#    Basic Linear Algebra Subprograms for Fortran Usage,
#    Algorithm 539,
#    ACM Transactions on Mathematical Software,
#    Volume 5, Number 3, September 1979, pages 308-323.
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real X(*), the vector to be examined.
#
#    Input, integer INCX, the increment between successive entries of X.
#
#    Output, integer VALUE, the index of the element of X of maximum
#    absolute value.
#
  value = -1
  index = -1
  
  i = 0
  for k in range ( 0, n ):
    if ( value < abs ( x[i] ) ):
      index = k
      value = abs ( x[i] )
    i = i + incx
 
  return index

def idamax_test ( ):

#*****************************************************************************80
#
## IDAMAX_TEST demonstrates IDAMAX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 September 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'IDAMAX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  IDAMAX returns the index of maximum magnitude' )
 
  n = 11
  x = np.zeros ( n )
  for i in range ( 0, n ):
    x[i] = ( ( 7 * ( i + 1 ) ) % 11 ) - ( n // 2 )

  r8vec_print ( n, x, '  The vector X:' )

  incx = 1

  index = idamax ( n, x, incx )

  print ( '' )
  print ( '  The index of maximum magnitude = %d' % ( index ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'IDAMAX_TEST' )
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
  dasum_test ( )
  daxpy_test ( )
  dcopy_test ( )
  ddot_test ( )
  dmach_test ( )
  dnrm2_test ( )
  drot_test ( )
  drotg_test ( )
  dscal_test ( )
  idamax_test ( )
  timestamp ( )

