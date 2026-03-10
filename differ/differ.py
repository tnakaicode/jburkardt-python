#! /usr/bin/env python3
#
def differ_backward ( h, o, p ):

#*****************************************************************************80
#
## differ_backward() computes backward difference coefficients.
#
#  Discussion:
#
#    We determine coefficients C to approximate the derivative at X0
#    of order O and precision P, using equally spaced backward
#    differences, so that 
#
#      d^o f(x)/dx^o = sum ( 0 <= i <= o+p-1 ) c(i) f(x-ih) + O(h^(p))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real H, the spacing.  0 < H.
#
#    integer O, the order of the derivative to be approximated.
#    1 <= O.
#
#    integer P, the order of the error, as a power of H.
#
#  Output:
#
#    real C(O+P), the coefficients.
#
#    real X(O+P), the evaluation points.
#
  from math import factorial
  import numpy as np

  n = o + p
  x = h * np.linspace ( - n + 1, 0, n )
  A = vand1 ( x )

  b = np.zeros ( n )
  b[o] = 1.0

  c = np.linalg.solve ( A, b )

  c = c * factorial ( o )

  return c, x

def differ_central ( h, o, p ):

#*****************************************************************************80
#
## differ_central() computes central difference coefficients.
#
#  Discussion:
#
#    We determine coefficients C to approximate the derivative at X0
#    of order O and precision P, using equally spaced central
#    differences, so that 
#
#      d^o f(x)/dx^o = sum ( 0 <= i <= o+p-1 ) c(i) f(x+(2*i-o-p+1)*h/2) 
#        + O(h^(p))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real H, the spacing.  0 < H.
#
#    integer O, the order of the derivative to be approximated.
#    1 <= O.
#
#    integer P, the order of the error, as a power of H.
#
#  Output:
#
#    real C(O+P), the coefficients.
#
#    real X(O+P), the evaluation points.
#
  from math import factorial
  import numpy as np

  n = o + p
  x = 0.5 * h * np.linspace ( - n + 1, n - 1, n )
  A = vand1 ( x )

  b = np.zeros ( n )
  b[o] = 1.0

  c = np.linalg.solve ( A, b )

  c = c * factorial ( o )

  return c, x

def differ_forward ( h, o, p ):

#*****************************************************************************80
#
## differ_forward() computes forward difference coefficients.
#
#  Discussion:
#
#    We determine coefficients C to approximate the derivative at X0
#    of order O and precision P, using equally spaced forward
#    differences, so that 
#
#      d^o f(x)/dx^o = sum ( 0 <= i <= o+p-1 ) c(i) f(x+ih) + O(h^(p))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real H, the spacing.  0 < H.
#
#    integer O, the order of the derivative to be approximated.
#    1 <= O.
#
#    integer P, the order of the error, as a power of H.
#
#  Output:
#
#    real C(O+P), the coefficients.
#
#    real X(O+P), the evaluation points.
#
  from math import factorial
  import numpy as np

  n = o + p
  x = h * np.linspace ( 0, n - 1, n )
  A = vand1 ( x )

  b = np.zeros ( n )
  b[o] = 1.0

  c = np.linalg.solve ( A, b )

  c = c * factorial ( o )

  return c, x

def differ_inverse ( stencil ):

#*****************************************************************************80
#
## differ_inverse() returns the inverse of the DIFFER matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real STENCIL(N), the values that define A.
#    The entries of STENCIL must be distinct.
#    No entry of STENCIL may be zero.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  n = len ( stencil )

  A = np.zeros ( [ n, n ] )

  A[:,0] = 1.0

  for i in range ( 0, n ):

    indx = 0

    for k in range ( 0, n ):

      if ( k != i ):

        for j in range ( indx + 1, -1, -1 ):

          A[i,j] = - stencil[k] * A[i,j] / ( stencil[i] - stencil[k] )

          if ( 0 < j ):
            A[i,j] = A[i,j] + A[i,j-1] / ( stencil[i] - stencil[k] )

        indx = indx + 1

  for i in range ( 0, n ):
    A[i,:] = A[i,:] / stencil[i]

  return A

def differ_matrix ( stencil ):

#*****************************************************************************80
#
## differ_matrix() computes the stencil matrix from the stencil vector.
#
#  Discussion:
#
#    If N = 4, and STENCIL = ( -3, -2, -1, 1 ), then A will be
#
#    -3  -2  -1  1
#     9   4   1  1
#   -27  -8  -1  1
#    81  16   1  1
#
#    This matrix is a generalized form of a Vandermonde matrix A2:
#
#     1   1   1  1
#    -3  -2  -1  1
#     9   4   1  1
#   -27  -8  -1  1    
#
#    and if A * x = b, the A2 * x2 = b, where x2(i) = x(i) * stencil(i)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real STENCIL(N), the stencil vector.
#    The entries in this vector must be distinct.
#    No entry of STENCIL may be 0.
#
#  Output:
#
#    real A(N,N), the stencil matrix.
#
  import numpy as np

  n = len ( stencil )
  A = np.zeros ( [ n, n ] )

  A[0,:] = stencil[:]
  for i in range ( 1, n ):
    A[i,:] = A[i-1,:] * stencil[:]

  return A

def differ_matrix_test ( ):

#*****************************************************************************80
#
## differ_matrix_test() tests differ_matrix().
#
#  Discussion:
#
#    differ_matrix() computes a modified Vandermonde matrix A1.
#
#    The solution of a system A1 * X1 = B is related to the solution
#    of the system A2 * X2 = B, where A2 is the standard Vandermonde
#    matrix, simply by X2(I) = X1(I) * A(I,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'differ_matrix_test():' )
  print ( '  Demonstrate that the DIFFER matrix is "really"' )
  print ( '  a Vandermonde matrix.' )

  stencil = np.array ( [ 2.5, 3.3, -1.3, 0.5 ] )
  x1 = np.array ( [ 1.0, 2.0, 3.0, 4.0 ] )
  A = differ_matrix ( stencil )
  print ( '  Stencil matrix:' )
  print ( A )
  b = np.matmul ( A, x1 )
#
#  Set up and solve the DIFFER system.
#
  x1 = np.linalg.solve ( A, b )

  print ( '  Solution of DIFFER system:' )
  print ( x1 )
#
#  R8VM_SL solves the related Vandermonde system.
#  A simple transformation gives us the solution to the DIFFER system.
#
  x2 = r8vm_sl ( stencil, b )

  print ( '  Solution of VANDERMONDE system:' )
  print ( x2 )

  x2 = x2 / stencil
  print ( '  Transformed solution of VANDERMONDE system:' )
  print ( x2 )

  return

def differ_solve ( n, stencil, order ):

#*****************************************************************************80
#
## differ_solve() solves for finite difference coefficients.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of stencil points.
#
#    real STENCIL(N), the stencil vector.
#    The entries in this vector must be distinct.
#    No entry of STENCIL may be 0.
#
#    integer ORDER, the order of the derivative to be approximated.
#    1 <= ORDER <= N.
#
#  Output:
#
#    real C(N,1), the coefficients to be used
#    to multiply U(STENCIL(I))-U(0), so that the sum forms an
#    approximation to the derivative of order ORDER, with error 
#    of order H^(N+1-ORDER).
#
  import numpy as np

  A = differ_matrix ( stencil )

  b = np.zeros ( n )
  b[order-1] = 1.0

  c = np.linalg ( A, b )

  return c

def differ_stencil ( x0, o, p, x ):

#*****************************************************************************80
#
## differ_stencil() computes finite difference coefficients.
#
#  Discussion:
#
#    We determine coefficients C to approximate the derivative at X0
#    of order O and precision P, using finite differences, so that 
#
#      d^o f(x)/dx^o (x0) = sum ( 0 <= i <= o+p-1 ) c(i) f(x(i)) 
#        + O(h^(p))
#
#    where H is the maximum spacing between X0 and any X(I).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X0, the point where the derivative is to be approximated.
#
#    integer O, the order of the derivative to be approximated.
#    1 <= O.
#
#    integer P, the order of the error.
#
#    real X(O+P), the evaluation points.
#
#  Output:
#
#    real C(O+P), the coefficients.
#
  from math import factorial
  import numpy as np

  n = o + p
  dx = x - x0
  A = vand1 ( dx )

  b = np.zeros ( n )
  b[o] = 1.0

  c = np.linalg.solve ( A, b )

  c = c * factorial ( o )

  return c

def differ_test02 ( ):

#*****************************************************************************80
#
## differ_test02() tests differ_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng

  rng = default_rng ( )

  print ( '' )
  print ( 'differ_test02():' )
  print ( '  differ_inverse() returns the inverse of a DIFFER matrix' )
  print ( '' )
  print ( '   N    Inverse error' )

  for n in range ( 2, 9 ):

    print ( '' )

    for test in range ( 0, 5 ):
      x = rng.random ( size = n )
      A = differ_matrix ( x )
      B = differ_inverse ( x )
      err = inverse_error ( A, B )
      print ( '  %2d    %g' % ( n, err ) )

  return

def differ_test03 ( ):

#*****************************************************************************80
#
## differ_test03() tests differ_matrix().
#
#  Discussion:
#
#    Reproduce a specific example.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 4

  print ( '' )
  print ( 'differ_test03():' )
  print ( '  Reproduce a specific example.' )
#
#  Compute the coefficients for a specific stencil.
#
  stencil = np.array ( [ -3.0, -2.0, -1.0, 1.0 ] )
  b = np.zeros ( n )
  order = 1
  b[order-1] = 1.0
  A = differ_matrix ( stencil )
  c = np.linalg.solve ( A, b )
  print ( '  Solution of DIFFER system:' )
  print ( c )
#
#  Use the coefficients C to estimate the first derivative of EXP(X)
#  at X0, using a spacing of DX = 0.1.
#
  x0 = 1.3
  dx = 0.1
  df = 0.0
  for i in range ( 0, n ):
    df = df + c[i] * ( np.exp ( x0 + stencil[i] * dx ) - np.exp ( x0 ) )
  dfdx = df / dx

  print ( '' )
  print ( '  DFDX =         ', dfdx )
  print ( '  d exp(x) /dx = ', np.exp ( x0 ) )

  return

def differ_test04 ( ):

#*****************************************************************************80
#
## differ_test04() tests differ_forward(), differ_backward(), differ_central().
#
#  Discussion:
#
#    Evaluate the coefficients for uniformly spaced finite difference
#    approximations of derivatives.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'differ_test04():' )
  print ( '  differ_forward(),' )
  print ( '  differ_backward(), and' )
  print ( '  differ_central() produce coefficients for difference' )
  print ( '  approximations of the O-th derivative, ' )
  print ( '  with error of order H^P, for a uniform spacing of H.' )

  h = 1.0
  print ( '' )
  print ( '  Use a spacing of H = ', h, 'for all examples.' )
#
#  Forward difference approximation to the third derivative with error of O(h).
#
  o = 3
  p = 1
  n = o + p
  c, x = differ_forward ( h, o, p )
  print ( '  Forward difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )
#
#  Backward difference approximation to the third derivative with error of O(h).
#
  o = 3
  p = 1
  n = o + p
  c, x = differ_backward ( h, o, p )
  print ( '  Backward difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )
#
#  Central difference approximation to the third derivative with error of O(h^2).
#
  o = 3
  p = 2
  n = o + p
  c, x = differ_central ( h, o, p )
  print ( '  Central difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )
#
#  Central difference approximation to the third derivative with error of O(h^4).
#
  o = 3
  p = 4
  n = o + p
  c, x = differ_central ( h, o, p )
  print ( '  Central difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )
#
#  Forward difference approximation to the fourth derivative with error of O(h).
#
  o = 4
  p = 1
  n = o + p
  c, x = differ_forward ( h, o, p )
  print ( '  Forward difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )
#
#  Backward difference approximation to the fourth derivative with error of O(h).
#
  o = 4
  p = 1
  n = o + p
  c, x = differ_backward ( h, o, p )
  print ( '  Backward difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )
#
#  Central difference approximation to the fourth derivative with error of O(h^3).
#
  o = 4
  p = 3
  n = o + p
  c, x = differ_central ( h, o, p )
  print ( '  Central difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )

  return

def differ_test05 ( ):

#*****************************************************************************80
#
## differ_test05() tests differ_stencil().
#
#  Discussion:
#
#    Use DIFFER_STENCIL to reproduce forward, backward and central differences.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'differ_test05():' )
  print ( '  differ_stencil() produces coefficients for difference' )
  print ( '  approximations of the O-th derivative, ' )
  print ( '  using arbitrarily spaced data, with maximum spacing H' )
  print ( '  with error of order H^P.' )
#
#  Let X0 = 0.0
#
  x0 = 0.0
  h = 1.0
  print ( '' )
  print ( '  For all tests, let X0 = ', x0 )
  print ( '  and use a uniformly spacing of ', h, ', so we can compare' )
  print ( '  with previous forward, backward and central differences.' )
#
#  Forward difference approximation to the third derivative with error of O(h).
#
  o = 3
  p = 1
  n = o + p
  x = h * np.linspace ( 0, n - 1, n )
  c = differ_stencil ( x0, o, p, x )
  print ( '  Finite difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )
#
#  Backward difference approximation to the third derivative with error of O(h).
#
  o = 3
  p = 1
  n = o + p
  x = h * np.linspace ( 1 - n, 0, n )
  c = differ_stencil ( x0, o, p, x )
  print ( '  Backward difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )
#
#  Central difference approximation to the third derivative with error of O(h^2).
#
  o = 3
  p = 2
  n = o + p
  x = 0.5 * h * np.linspace ( - n + 1, n - 1, n )
  c = differ_stencil ( x0, o, p, x )
  print ( '  Central difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )
#
#  Central difference approximation to the third derivative with error of O(h^4).
#
  o = 3
  p = 4
  n = o + p
  x = 0.5 * h * np.linspace ( - n + 1, n - 1, n )
  c = differ_stencil ( x0, o, p, x )
  print ( '  Central difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )
#
#  Forward difference approximation to the fourth derivative with error of O(h).
#
  o = 4
  p = 1
  n = o + p
  x = h * np.linspace ( 0, n - 1, n )
  c = differ_stencil ( x0, o, p, x )
  print ( '  Finite difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )
#
#  Backward difference approximation to the fourth derivative with error of O(h).
#
  o = 4
  p = 1
  n = o + p
  x = h * np.linspace ( 1 - n, 0, n )
  c = differ_stencil ( x0, o, p, x )
  print ( '  Backward difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )
#
#  Central difference approximation to the fourth derivative with error of O(h^3).
#
  o = 4
  p = 3
  n = o + p
  x = 0.5 * h * np.linspace ( - n + 1, n - 1, n )
  c = differ_stencil ( x0, o, p, x )
  print ( '  Central difference coefficients, O = ', o, ', P = ', p )
  print ( np.c_ [ x, c ] )

  return

def differ_test ( ):

#*****************************************************************************80
#
## differ_test() tests differ().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'differ_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test differ().' )

  differ_matrix_test ( )
  differ_test02 ( )
  differ_test03 ( )
  differ_test04 ( )
  differ_test05 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'differ_test():' )
  print ( '  Normal end of execution.' )

  return

def inverse_error ( A, B ):

#*****************************************************************************80
#
## inverse_error() determines the error in an inverse matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(N,N), the matrix.
#
#    real B(N,N), the inverse.
#
#  Output:
#
#    real ERROR_FROBENIUS, the Frobenius norm of (A*B-I) + (B*A-I).
#
  import numpy as np

  n = A.shape[0]

  error_frobenius = np.linalg.norm ( np.matmul ( A, B ) - np.identity ( n ), 'fro' ) \
                  + np.linalg.norm ( np.matmul ( B, A ) - np.identity ( n ), 'fro' )

  return error_frobenius

def r8vm_sl ( a, b ):

#*****************************************************************************80
#
## r8vm_sl() solves A*x=b, where A is an R8VM matrix.
#
#  Discussion:
#
#    The R8VM storage format is used for an M by N Vandermonde matrix.
#    An M by N Vandermonde matrix is defined by the values in its second
#    row, which will be written here as X(1:N).  The matrix has a first 
#    row of 1's, a second row equal to X(1:N), a third row whose entries
#    are the squares of the X values, up to the M-th row whose entries
#    are the (M-1)th powers of the X values.  The matrix can be stored
#    compactly by listing just the values X(1:N).
#
#    Vandermonde systems are very close to singularity.  The singularity
#    gets worse as N increases, and as any pair of values defining
#    the matrix get close.  Even a system as small as N = 10 will
#    involve the 9th power of the defining values.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations,
#    Third Edition,
#    Johns Hopkins, 1996.
#
#  Input:
#
#    real A(N), the R8VM matrix.
#
#    real B(N), the right hand side.
#
#  Output:
#
#    real X(N), the solution of the linear system.
#
  import numpy as np

  n = len ( b )

  x = np.zeros ( n )
#
#  Check for explicit singularity.
#
  for j in range ( 0, n - 1 ):
    for i in range ( j + 1, n ):
      if ( a[i] == a[j] ):
        print ( '' )
        print ( 'r8vm_sl(): Fatal error!' )
        print ( '  A[i] == A[j] for some i, j.' )
        raise Exception ( 'r8vm_sl(): Fatal error!' )

  for i in range ( 0, n ):
    x[i] = b[i]

  for j in range ( 1, n ):
    for i in range ( n, j, -1 ):
      x[i-1] = x[i-1] - a[j-1] * x[i-2]

  for j in range ( n - 1, 0, -1 ):

    for i in range ( j + 1, n + 1 ):
      x[i-1] = x[i-1] / ( a[i-1] - a[i-j-1] )

    for i in range ( j, n ):
      x[i-1] = x[i-1] - x[i]

  return x

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

def vand1 ( x ):

#*****************************************************************************80
#
## vand1() returns the Vandermonde1 matrix A with 1's on the first row.
#
#  Formula:
#
#    A(I,J) = X(J)^(I-1)
#
#  Example:
#
#    N = 5, X = ( 2, 3, 4, 5, 6 )
#
#    1  1   1   1   1
#    2  3   4   5   6
#    4  9  16  25  36
#    8 27  64 125  216
#   16 81 256 625 1296
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is nonsingular if, and only if, the X values are distinct.
#
#    det ( A ) = product ( 1 <= I <= N ) ( 1 <= J < I ) ( X(I) - X(J) ).
#             = product ( 1 <= J <= N ) X(J)
#             * product ( 1 <= I < J ) ( X(J) - X(I) ).
#
#    A is generally ill-conditioned.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 October 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969, page 27,
#    LC: QA263.G68.
#
#    Nicholas Higham,
#    Stability analysis of algorithms for solving confluent
#    Vandermonde-like systems,
#    SIAM Journal on Matrix Analysis and Applications,
#    Volume 11, 1990, pages 23-41.
#
#  Input:
#
#    integer N, the order of the matrix desired.
#
#    real X(N), the values that define A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  n = len ( x )

  A = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 and x[j] == 0.0 ):
        A[i,j] = 1.0
      else:
        A[i,j] = x[j]**( i )

  return A

if ( __name__ == "__main__" ):
  timestamp ( )
  differ_test ( )
  timestamp ( )

