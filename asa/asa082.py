#! /usr/bin/env python3
#
def asa082_test ( ):

#*****************************************************************************80
#
## asa082_test tests asa082.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    17 January 2020
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'asa082_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test asa082.' )

  detq_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'asa082_test:' )
  print ( '  Normal end of execution.' )
  return

def detq ( a, n ):

#*****************************************************************************80
#
## detq computes the determinant of an orthogonal matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2020
#
#  Author:
#
#    Original FORTRAN77 version by J C Gower.
#    This Python version by John Burkardt
#
#  Reference:
#
#    J C Gower,
#    Algorithm AS 82:
#    The determinant of an orthogonal matrix,
#    Applied Statistics,
#    Volume 24, Number 1, 1975, page 150-153.
#
#  Input:
#
#    real A(N,N), the orthogonal matrix stored by rows or columns.
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real D, the determinant of A.
#
#    integer IFAULT, 
#    0, no error occurred.
#    1, an error was detected.
#
  import numpy as np

  ifault = 0
  d = 0.0

  tol = 0.0001

  if ( n <= 0 ):
    print ( '' )
    print ( 'detq - Fatal error!' )
    print ( '  n <= 0' )
    ifault = 1
    return d, ifault

  a2 = np.zeros ( n * n )
  k = 0
  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a2[k] = a[i,j]
      k = k + 1

  d = 1.0
  r = 0

  for k in range ( 2, n + 2 ):

    q = r
    x = a2[r]
    y = np.sign ( x )
    d = d * y
    y = - 1.0 / ( x + y )
    x = np.abs ( x ) - 1.0

    if ( tol < np.abs ( x ) ):

      if ( 0.0 < x ):
        print ( '\n' )
        print ( 'detq - Fatal error!\n' )
        print ( '  x < 0.0\n' )
        print ( '  x = ', x )
        ifault = 1
        return d, ifault

      if ( k == n + 1 ):
        print ( '\n' )
        print ( 'detq - Fatal error!\n' )
        print ( '  k == n + 1\n' )
        ifault = 1
        return d, ifault

      for i in range ( k, n + 1 ):
        q = q + n
        x = a2[q] * y
        p = r
        s = q
        for j in range ( k, n + 1 ):
          p = p + 1
          s = s + 1
          a2[s] = a2[s] + x * a2[p]

    r = r + n + 1

  return d, ifault

def detq_test ( ):

#*****************************************************************************80
#
## detq_test tests detq.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 January 2020
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'detq_test:' )
  print ( '  detq computes the determinant of an orthogonal matrix.' )

  for n in range ( 5, 11 ):

    a = helmert_matrix ( n )
    print ( '' )
    print ( '  Helmert matrix of order', n )
    d1 = helmert_determinant ( n )
    print ( '  determinant =      ', d1 )
    d2, ifault = detq ( a, n )

    if ( ifault == 1 ):
      print ( '  DETQ failed for this case.' )
    else:
      print ( '  DETQ determinant = ', d2 )

  return

def helmert_matrix ( n ):

#*****************************************************************************80
#
## helmert_matrix returns the Helmert matrix.
#
#  Formula:
#
#    If I = 1 then
#      A(I,J) = 1 / sqrt ( N )
#    else if J < I then
#      A(I,J) = 1 / sqrt ( I * ( I - 1 ) )
#    else if J = I then
#      A(I,J) = (1-I) / sqrt ( I * ( I - 1 ) )
#    else
#      A(I,J) = 0
#
#  Discussion:
#
#    The matrix given above by Helmert is the classic example of
#    a family of matrices which are now called Helmertian or
#    Helmert matrices.
#
#    A matrix is a (standard) Helmert matrix if it is orthogonal,
#    and the elements which are above the diagonal and below the
#    first row are zero.
#
#    If the elements of the first row are all strictly positive,
#    then the matrix is a strictly Helmertian matrix.
#
#    It is possible to require in addition that all elements below
#    the diagonal be strictly positive, but in the reference, this
#    condition is discarded as being cumbersome and not useful.
#
#    A Helmert matrix can be regarded as a change of basis matrix
#    between a pair of orthonormal coordinate bases.  The first row
#    gives the coordinates of the first new basis vector in the old
#    basis.  Each later row describes combinations of (an increasingly
#    extensive set of) old basis vectors that constitute the new
#    basis vectors.
#
#    Helmert matrices have important applications in statistics.
#
#  Example:
#
#    N = 5
#
#    0.4472    0.4472    0.4472    0.4472    0.4472
#    0.7071   -0.7071         0         0         0
#    0.4082    0.4082   -0.8165         0         0
#    0.2887    0.2887    0.2887   -0.8660         0
#    0.2236    0.2236    0.2236    0.2236   -0.8944
#
#  Properties:
#
#    A is generally not symmetric: A' ~= A.
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    Because A is orthogonal, it is normal: A' * A = A * A'.
#
#    A is not symmetric: A' ~= A.
#
#    det ( A ) = (-1)^(N+1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    HO Lancaster,
#    The Helmert Matrices,
#    American Mathematical Monthly,
#    Volume 72, 1965, pages 4-12.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )
#
#  A begins with the first row, diagonal, and lower triangle set to 1.
#
  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 ):
        a[i,j] = 1.0 / np.sqrt ( n )
      elif ( j < i ):
        a[i,j] = 1.0 / np.sqrt ( float ( i * ( i + 1 ) ) )
      elif ( i == j ):
        a[i,j] = float ( - i ) / np.sqrt ( float ( i * ( i + 1 ) ) )

  return a

def helmert_determinant ( n ):

#*****************************************************************************80
#
## helmert_determinant computes the determinant of the Helmert matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real DETERM, the determinant.
#
  if ( ( n % 2 ) == 0 ):
    determ = - 1.0
  else:
    determ = 1.0

  return determ

def timestamp ( ):

#*****************************************************************************80
#
## timestamp prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  asa082_test ( )
  timestamp ( )

