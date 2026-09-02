#! /usr/bin/env python3
#
def c83_test ( ):

#*****************************************************************************80
#
## c83_test() tests c83().
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
  import platform

  print ( '' )
  print ( 'c83_test():' )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  Test c83().' )

  c83_mv_test ( )
  c83_indicator_test ( )
  c83_random_test ( )
  c8vec_uniform_01_test ( )
  cyclic_reduction_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'c83_test():' )
  print ( '  Normal end of execution.' )

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
#    complex A_CR[2*N+1,3], factorization information computed by C83_CR_FA.
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

def c83_cr_sls ( n, A_cr, nb, b ):

#*****************************************************************************80
#
## c83_cr_sls() solves several complex linear systems factored by C83_CR_FA.
#
#  Discussion:
#
#    The matrix A must be tridiagonal.  C83_CR_FA is called to compute the
#    LU factors of A.  It does so using a form of cyclic reduction.  If
#    the factors computed by C83_CR_FA are passed to C83_CR_SLS, then one or many
#    linear systems involving the matrix A may be solved.
#
#    Note that C83_CR_FA does not perform pivoting, and so the solution 
#    produced by C83_CR_SLS may be less accurate than a solution produced 
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
#    complex A_cr[2*N+1,3], factorization information computed by C83_CR_FA.
#
#    integer NB, the number of right hand sides.
#
#    complex B[N,NB], the right hand side vectors.
#
#  Output:
#
#    complex X[N,NB], the solutions of the linear system.
#
  import numpy as np

  if ( n <= 0 ):
    print ( '\n' )
    print ( 'c83_cr_sls(): Fatal error!' )
    print ( '  Nonpositive N = \n', n )
    raise Exception ( 'c83_cr_sls(): Fatal error!' )

  x = np.zeros ( [ n, nb ], dtype = complex )

  if ( n == 1 ):
    x[0,:] = A_cr[1,1] * b[0,:]
    return x
#
#  Set up RHS.
#
  rhs = np.zeros ( [ 2 * n + 1, nb ] )
  rhs[1:n+1,:] = b[0:n,:]

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
      rhs[ihaf,:] = rhs[iful,:] \
        - A_cr[iful-1,2] * rhs[iful-1,:] \
        - A_cr[iful,0] * rhs[iful+1,:]

  rhs[ihaf,:] = rhs[ihaf,:] * A_cr[ihaf,1]
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
      rhs[iful,:] = rhs[ihaf,:]
      rhs[ifulm,:] = \
          A_cr[ifulm,1] * ( rhs[ifulm,:] \
        - A_cr[ifulm-1,3] * rhs[ifulm-1,:] \
        - A_cr[ifulm,1] *   rhs[iful,:] )

  x[:,:] = rhs[1:n+1,:]

  return x

def c83_indicator ( n ):

#*****************************************************************************80
#
## c83_indicator() sets up a C83 indicator matrix.
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
#    23 May 2026
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
#  Output:
#
#    complex A(N,3), the indicator matrix.
#
  import numpy as np

  A = np.zeros ( [ n, 3 ], dtype = complex );

  for i in range ( 1, n ):
    I = i + 1
    J = I - 1
    A[i,0] = I + J * 1j

  for i in range ( 0, n ):
    I = i + 1
    J = I
    A[i,1] = I + J * 1j

  for i in range ( 0, n - 1 ):
    I = i + 1
    J = I + 1
    A[i,2] = I + J * 1j

  return A

def c83_indicator_test ( ):

#*****************************************************************************80
#
## c83_indicator_test() tests c83_indicator().
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

  n = 4

  print ( '' )
  print ( 'c83_indicator_test():' )
  print ( '  c83_indicator() computes the indicator complex tridiagonal matrix.' )

  A = c83_indicator ( n )

  print ( '  The matrix A:' )
  pprint.pprint ( A )

  return

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
#    11 May 2010
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

def c83_mv_test ( ):

#*****************************************************************************80
#
## c83_mxv_test() tests c83_mv().
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

  print ( '' )
  print ( 'c83_mv_test():' )
  print ( '  c83_mv() multiplies a complex triadigonal matrix times a vector.' )

  n = 4

  A = c83_random ( n )
  print ( '  The tridiagonal matrix A:' )
  pprint.pprint ( A )

  x = c8vec_uniform_01 ( n )
  print ( '  The random vector x:' )
  pprint.pprint ( x )

  Ax = c83_mv ( n, A, x )
  print ( '  The product A*x:' )
  pprint.pprint ( Ax )

  return

def c83_random ( n ):

#*****************************************************************************80
#
## c83_random() returns a random complex tridiagonal matrix.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
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
#    23 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of rows and columns in the matrix.
#
#  Output:
#
#    complex C(3,N), stored in compressed tridiagonal form.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )
#
#  Create the right number of random complex values.
#
  r = rng.random ( 3 * n - 2 )
  r = np.sqrt ( r )
  theta = 2.0 * np.pi * rng.random ( )
  z = r * complex ( np.cos ( theta ), np.sin ( theta ) )
#
#  Pack them into the array.
#
  c = np.zeros ( ( n, 3 ), dtype = complex )
  k = 0
  for j in range ( 0, 3 ):
    for i in range ( 0, n ):
      if ( ( j == 0 and 0 < i ) or \
           ( j == 1 ) or \
           ( j == 2 and i < n-1 ) ):
        c[i,j] = z[k]
        k = k + 1

  return c

def c83_random_test ( ):

#*****************************************************************************80
#
## c83_random_test() tests c83_random().
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

  n = 4

  print ( '' )
  print ( 'c83_random_test():' )
  print ( '  c83_random() computes a random complex tridiagonal matrix.' )

  A = c83_random ( n )

  print ( '  The matrix A:' )
  pprint.pprint ( A )

  return

def c8vec_uniform_01 ( n ):

#*****************************************************************************80
#
## c8vec_uniform_01() returns a unit pseudorandom C8VEC.
#
#  Discussion:
#
#    The angles should be uniformly distributed between 0 and 2 * PI,
#    the square roots of the radius uniformly distributed between 0 and 1.
#
#    This results in a uniform distribution of values in the unit circle.
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
#  Input:
#
#    integer N, the number of values to compute.
#
#  Output:
#
#    complex C(N), the pseudorandom complex vector.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  c = np.zeros ( n, 'complex' )

  for j in range ( 0, n ):

    r = rng.random ( )
    r = np.sqrt ( r )

    theta = 2.0 * np.pi * rng.random ( )

    c[j] = r * complex ( np.cos ( theta ), np.sin ( theta ) )

  return c

def c8vec_uniform_01_test ( ):

#*****************************************************************************80
#
## c8vec_uniform_01_test() tests c8vec_uniform_01().
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
  print ( '' )
  print ( 'c8vec_uniform_01_test():' )
  print ( '  c8vec_uniform_01() computes pseudorandom complex values' )
  print ( '  in the unit circle.' )
  print ( '' )

  n = 10

  x = c8vec_uniform_01 ( n )

  for i in range ( 0, n ):
    print ( '  %6d  ( %f, %f )' % ( i, x[i].real, x[i].imag ) )

  return

def cyclic_reduction_test():

#*****************************************************************************80
#
## cyclic_reduction_test() tests c83_cr_fa(), c83_cr_sl().
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
  print ( 'cyclic_reduction_test():' )
  print ( '  c83_cr_fa() factors a complex tridiagonal matrix;' )
  print ( '  c83_cr_sl() solves a factored system.' )
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

if ( __name__ == '__main__' ):
  timestamp ( )
  c83_test ( )
  timestamp ( )

