#! /usr/bin/env python3
#
def pyramid_rule_test ( ):

#*****************************************************************************80
#
## pyramid_rule_test() tests pyramid_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 May 2023
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'pyramid_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test pyramid_rule().' )

  legendre_order = 4
  jacobi_order = 3
  filename = 'pyramid_l4_j3'
  pyramid_rule ( legendre_order, jacobi_order, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'pyramid_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def pyramid_rule ( legendre_order, jacobi_order, filename ):

#*****************************************************************************80
#
## pyramid_rule() generates a quadrature rule for a unit pyramid.
#
#  Discussion:
#
#    This program computes a quadrature rule for a pyramid
#    and writes it to a file.
#
#    The integration region is:
# 
#      - ( 1 - Z ) <= X <= 1 - Z
#      - ( 1 - Z ) <= Y <= 1 - Z
#                0 <= Z <= 1.
#
#    When Z is zero, the integration region is a square lying in the (X,Y) 
#    plane, centered at (0,0,0) with "radius" 1.  As Z increases to 1, the 
#    radius of the square diminishes, and when Z reaches 1, the square has 
#    contracted to the single point (0,0,1).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer LEGENDRE_ORDER, the number of points in the X and Y dimensions
#
#    integer the JACOBI_ORDER, the number of points in the Z dimension
#
#    character FILENAME, the root name of the output files.
#
  print ( '' )
  print ( 'pyramid_rule():' )
  print ( '  Compute a quadrature rule for approximating' )
  print ( '  the integral of a function over a unit pyramid.' )
  print ( '' )
  print ( '  The user specifies:' )
  print ( '  * LEGENDRE_ORDER, the order of the Legendre rule for X and Y.' )
  print ( '  * JACOBI_ORDER, the order of the Jacobi rule for Z,' )
  print ( '  * FILENAME, the prefix for the three output files:' )
  print ( '' )
  print ( '    filename_w.txt - the weight file' )
  print ( '    filename_x.txt - the abscissa file.' )
  print ( '    filename_r.txt - the region file.' )
#
#  Get the Legendre order.
#
  print ( '' )
  print ( '  The requested Legendre order is ', legendre_order )
  print ( '  The requested Jacobi order is ', jacobi_order )
  print ( '  The "root name" is "' + filename + '"' )

  pyramid_handle ( legendre_order, jacobi_order, filename )

  return

def jacobi_ek_compute ( n, alpha, beta ):

#*****************************************************************************80
#
## jacobi_ek_compute(): Elhay-Kautsky method for Gauss-Jacobi quadrature rule.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x <= 1 ) (1-x)^alpha * (1+x)^beta * f(x) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#  Input:
#
#    integer N, the number of abscissas.
#
#    real ALPHA, BETA, the exponents of (1-X) and
#    (1+X) in the quadrature rule.  For simple Gauss-Legendre quadrature,
#    set ALPHA = BETA = 0.0.  -1.0 < ALPHA and -1.0 < BETA are required.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np
  from scipy.special import gamma
#
#  Define the zero-th moment.
#
  zemu = 2.0 ** ( alpha + beta + 1 ) \
       * gamma ( alpha + 1.0 ) \
       * gamma ( beta + 1.0 ) \
       / gamma ( alpha + beta + 2.0 )
#
#  Define the Jacobi matrix.
#
  bj = np.zeros ( n )

  bj[0] = 4.0 * ( 1.0 + alpha ) * ( 1.0 + beta ) \
    / ( ( 3.0 + alpha + beta ) * ( 2.0 + alpha + beta ) ** 2 )

  for i in range ( 1, n ):
    ip1_r8 = float ( i + 1 )
    abi = 2.0 * ip1_r8 + alpha + beta
    bj[i] = 4.0 * ip1_r8 * ( ip1_r8 + alpha ) * ( ip1_r8 + beta ) \
      * ( ip1_r8 + alpha + beta ) \
      / ( ( abi - 1.0 ) * ( abi + 1.0 ) * abi * abi )

  for i in range ( 0, n ):
    bj[i] = np.sqrt ( bj[i] )

  x = np.zeros ( n )
  x[0] = ( beta - alpha ) / ( 2.0 + alpha + beta )
  for i in range ( 1, n ):
    ip1_r8 = float ( i + 1 )
    abi = 2.0 * ip1_r8 + alpha + beta
    x[i] = ( beta + alpha ) * ( beta - alpha ) / ( ( abi - 2.0 ) * abi )

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return x, w

def imtqlx ( n, d, e, z ):

#*****************************************************************************80
#
## imtqlx() diagonalizes a symmetric tridiagonal matrix.
#
#  Discussion:
#
#    This routine is a slightly modified version of the EISPACK routine to
#    perform the implicit QL algorithm on a symmetric tridiagonal matrix.
#
#    The authors thank the authors of EISPACK for permission to use this
#    routine.
#
#    It has been modified to produce the product Q' * Z, where Z is an input
#    vector and Q is the orthogonal matrix diagonalizing the input matrix.
#    The changes consist (essentially) of applying the orthogonal 
#    transformations directly to Z as they are generated.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#    Roger Martin, James Wilkinson,
#    The Implicit QL Algorithm,
#    Numerische Mathematik,
#    Volume 12, Number 5, December 1968, pages 377-383.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real D(N), the diagonal entries of the matrix.
#
#    real E(N), the subdiagonal entries of the
#    matrix, in entries E(1) through E(N-1). 
#
#    real Z(N), a vector to be operated on.
#
#  Output:
#
#    real LAM(N), the diagonal entries of the diagonalized matrix.
#
#    real QTZ(N), the value of Q' * Z, where Q is the matrix that 
#    diagonalizes the input symmetric tridiagonal matrix.
#
  import numpy as np

  lam = np.zeros ( n )
  for i in range ( 0, n ):
    lam[i] = d[i]

  qtz = np.zeros ( n )
  for i in range ( 0, n ):
    qtz[i] = z[i]

  if ( n == 1 ):
    return lam, qtz

  itn = 30

  prec = np.finfo(float).eps

  e[n-1] = 0.0

  for l in range ( 1, n + 1 ):

    j = 0

    while ( True ):

      for m in range ( l, n + 1 ):

        if ( m == n ):
          break

        if ( abs ( e[m-1] ) <= prec * ( abs ( lam[m-1] ) + abs ( lam[m] ) ) ):
          break

      p = lam[l-1]

      if ( m == l ):
        break

      if ( itn <= j ):
        print ( '' )
        print ( 'IMTQLX - Fatal error!' )
        print ( '  Iteration limit exceeded.' )
        raise Exception ( 'IMTQLX - Fatal error!' )

      j = j + 1
      g = ( lam[l] - p ) / ( 2.0 * e[l-1] )
      r = np.sqrt ( g * g + 1.0 )

      if ( g < 0.0 ):
        t = g - r
      else:
        t = g + r

      g = lam[m-1] - p + e[l-1] / ( g + t )
 
      s = 1.0
      c = 1.0
      p = 0.0
      mml = m - l

      for ii in range ( 1, mml + 1 ):

        i = m - ii
        f = s * e[i-1]
        b = c * e[i-1]

        if ( abs ( g ) <= abs ( f ) ):
          c = g / f
          r = np.sqrt ( c * c + 1.0 )
          e[i] = f * r
          s = 1.0 / r
          c = c * s
        else:
          s = f / g
          r = np.sqrt ( s * s + 1.0 )
          e[i] = g * r
          c = 1.0 / r
          s = s * c

        g = lam[i] - p
        r = ( lam[i-1] - g ) * s + 2.0 * c * b
        p = s * r
        lam[i] = g + p
        g = c * r - b
        f = qtz[i]
        qtz[i]   = s * qtz[i-1] + c * f
        qtz[i-1] = c * qtz[i-1] - s * f

      lam[l-1] = lam[l-1] - p
      e[l-1] = g
      e[m-1] = 0.0

  for ii in range ( 2, n + 1 ):

     i = ii - 1
     k = i
     p = lam[i-1]

     for j in range ( ii, n + 1 ):

       if ( lam[j-1] < p ):
         k = j
         p = lam[j-1]

     if ( k != i ):

       lam[k-1] = lam[i-1]
       lam[i-1] = p

       p        = qtz[i-1]
       qtz[i-1] = qtz[k-1]
       qtz[k-1] = p

  return lam, qtz

def legendre_ek_compute ( n ):

#*****************************************************************************80
#
## legendre_ek_compute(): Gauss-Legendre, Elhay-Kautsky method.
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 < x < +1 ) f(x) dx
#
#    The quadrature rule:
#
#      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2015
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#  Input:
#
#    integer N, the number of abscissas.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  import numpy as np
#
#  Define the zero-th moment.
#
  zemu = 2.0
#
#  Define the Jacobi matrix.
#
  bj = np.zeros ( n )
  for i in range ( 0, n ):
    ip1_r8 = float ( i + 1 )
    bj[i] = ip1_r8 * ip1_r8 / ( 4.0 * ip1_r8 * ip1_r8 - 1.0 )
    bj[i] = np.sqrt ( bj[i] )

  x = np.zeros ( n )

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return x, w

def pyramid_handle ( legendre_order, jacobi_order, filename ):

#*****************************************************************************80
#
## pyramid_handle() computes the requested pyramid rule and outputs it.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer LEGENDRE_ORDER, JACOBI_ORDER, the orders
#    of the component Legendre and Jacobi rules.
#
#    string FILENAME, the rootname for the files,
#    write files 'file_w.txt' and 'file_x.txt', and 'file_r.txt', weights,
#    abscissas, and region.
#
  import numpy as np
#
#  Compute the factor rules.
#
  legendre_x, legendre_w = legendre_ek_compute ( legendre_order )

  jacobi_alpha = 2.0
  jacobi_beta = 0.0

  jacobi_x, jacobi_w = jacobi_ek_compute ( jacobi_order, jacobi_alpha, \
    jacobi_beta )
#
#  Compute the pyramid rule.
#
  pyramid_order = legendre_order * legendre_order * jacobi_order

  volume = 4.0 / 3.0

  pyramid_w = np.zeros ( pyramid_order )
  pyramid_x = np.zeros ( [ pyramid_order, 3 ] )
  
  l = 0
  for k in range ( 0, jacobi_order ):
    xk = ( jacobi_x[k] + 1.0 ) / 2.0
    wk = jacobi_w[k] / 2.0
    for j in range ( 0, legendre_order ):
      xj = legendre_x[j]
      wj = legendre_w[j]
      for i in range ( 0, legendre_order ):
        xi = legendre_x[i]
        wi = legendre_w[i]
        pyramid_w[l] = wi * wj * wk / 4.0 / volume
        pyramid_x[l,0] = xi * ( 1.0 - xk )
        pyramid_x[l,1] = xj * ( 1.0 - xk )
        pyramid_x[l,2] =              xk
        l = l + 1

  pyramid_r = np.array ( [ \
    [ -1.0, -1.0, 0.0 ], \
    [ +1.0, -1.0, 0.0 ], \
    [ -1.0, +1.0, 0.0 ], \
    [ +1.0, +1.0, 0.0 ], \
    [  0.0,  0.0, 1.0 ] ] )
#
#  Write the rule to files.
#
  filename_w = filename + '_w.txt'
  filename_x = filename + '_x.txt'
  filename_r = filename + '_r.txt'

  print ( '' )
  print ( '  Creating quadrature files.' )
  print ( '' )
  print ( '  Weight file will be   "' + filename_w + '".' )
  print ( '  Abscissa file will be "' + filename_x + '".' )
  print ( '  Region file will be   "' + filename_r + '".' )

  np.savetxt ( filename_w, pyramid_w )
  np.savetxt ( filename_x, pyramid_x )
  np.savetxt ( filename_r, pyramid_r )

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
  pyramid_rule_test ( )
  timestamp ( )





