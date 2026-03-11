#! /usr/bin/env python3
#
def jacobi_polynomial_test ( ):

#*****************************************************************************80
#
## jacobi_polynomial_test() tests jacobi_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    02 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'jacobi_polynomial_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  jacobi_polynomial() evalutes the Jacobi polynomial' )
  print ( '  and associated functions.' )

  jacobi_polynomial_test01 ( )
  jacobi_polynomial_test02 ( )
  jacobi_polynomial_test03 ( )
  jacobi_polynomial_test04 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'jacobi_polynomial_test():' )
  print ( '  Normal end of execution.' )
  return

def jacobi_polynomial_test01 ( ):

#*****************************************************************************80
#
## jacobi_polynomial_test01() tests j_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'jacobi_polynomial_test01():' )
  print ( '  j_polynomial_values() stores values of' )
  print ( '  the Jacobi polynomials.' )
  print ( '  j_polynomial() evaluates the polynomial.' )
  print ( '' )
  print ( '                                    Tabulated                 Computed' )
  print ( '     N     A     B        X           J(N,A,B,X)                    J(N,A,B,X)                     Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, a, b, x, fx1 = j_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2_vec = j_polynomial ( 1, n, a, b, x )
    fx2 = fx2_vec[0,n]
    e = fx1 - fx2

    print ( '  %4d  %6f  %6f  %6f  %24.16e  %24.16e  %8.2g' 
      % ( n, a, b, x, fx1, fx2, e ) )

  return

def jacobi_polynomial_test02 ( ):

#*****************************************************************************80
#
## jacobi_polynomial_test02 tests j_polynomial_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'jacobi_polynomial_test02:' )
  print ( '  j_polynomial_zeros() computes the zeros of J(n,a,b,x)' )
  print ( '  Check by calling j_polynomial() there.' )

  for a, b in [ [ 0.5, 0.5 ], [ 1.0, 1.5 ], [2.0, 0.5 ] ]:

    for degree in range ( 1, 6 ):

      z = j_polynomial_zeros ( degree, a, b )
      my_title = '  zeros for J(' + str ( degree ) + ',' + str ( a ) + ',' + str ( b ) + ')'
      r8vec_print ( degree, z, my_title )

      hz = j_polynomial ( degree, degree + 1, a, b, z )
      my_title = '  J(' + str ( degree ) + ',' + str ( a ) + ',' + str ( b ) + ', z )'
      r8vec_print ( degree, hz[:,degree], my_title )

  return

def jacobi_polynomial_test03 ( ):

#*****************************************************************************80
#
## jacobi_polynomial_test03() tests j_quadrature_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'jacobi_polynomial_test03():' )
  print ( '  j_quadrature_rule() computes the quadrature rule' )
  print ( '  associated with J(n,a,b,x)' )

  n = 7
  a = 1.0
  b = 2.5
  x, w = j_quadrature_rule ( n, a, b )

  r8vec2_print ( x, w, '      X            W' )

  print ( '' )
  print ( '  Use the quadrature rule to estimate:' )
  print ( '' )
  print ( '    Q = Integral (-1<x<+1) J(i,a,b,x) J(j,a,b,x) (1-x)^a (1+x)^b dx' )
  print ( '' )
  print ( '   I   J      Q_Estimate         Q_Exact' )
  print ( '' )

  for i in range ( 0, 6 ):
    ji = j_polynomial ( n, i, a, b, x )
    for j in range ( i, 6 ):
      jj = j_polynomial ( n, j, a, b, x )
      f = ji[:,i] * jj[:,j]
      q = np.dot ( w, f )
      q_exact = j_double_product_integral ( i, j, a, b )
      print ( '  %2d  %2d  %14g  %14g' % ( i, j, q, q_exact ) )

  return

def jacobi_polynomial_test04 ( ):

#*****************************************************************************80
#
## jacobi_polynomial_test04() tests j_double_product_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2025
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'jacobi_polynomial_test04():' )
  print ( '  j_double_product_integral() computes the weighted integral of' )
  print ( '  J(i,a,b,x) * J(j,a,b,x)' )

  a = 1.0
  b = 2.5
  print ( '' )
  print ( '  For this example, we use a = ', a, ', b = ', b )
  print ( '' )
  print ( '    Q = Integral (-1<x<+1) J(i,a,b,x) J(j,a,b,x) (1-x)^a (1+x)^b dx' )
  print ( '' )
  print ( '   I   J      Q' )
  print ( '' )

  for i in range ( 0, 6 ):
    for j in range ( i, 6 ):
      q = j_double_product_integral ( i, j, a, b )
      print ( '  %2d  %2d  %14g' % ( i, j, q ) )

  return

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
        print ( 'imtqlx(): Fatal error!' )
        print ( '  Iteration limit exceeded.' )
        raise Exception ( 'imtqlx(): Fatal error!' )

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

def j_double_product_integral ( i, j, a, b ):

#*****************************************************************************80
#
## j_double_product_integral(): integral of J(i,x)*J(j,x)*(1-x)^a*(1+x)^b.
#
#  Discussion:
#
#    VALUE = integral ( -1 <= x <= +1 ) J(i,x)*J(j,x)*(1-x)^a*(1+x)^b dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the polynomial indices.
#
#    real A, B, the parameters.
#    -1 < A, B.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import factorial
  from scipy.special import gamma

  if ( i != j ):
    value = 0.0
  else:
    value = 2**( a + b + 1.0 ) / ( 2 * i + a + b + 1 ) \
      * gamma ( i + a + 1 ) * gamma ( i + b + 1 ) \
      / factorial ( i ) / gamma ( i + a + b + 1 )

  return value

def j_integral ( n ):

#*****************************************************************************80
#
## j_integral() evaluates a monomial integral associated with J(n,a,b,x).
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x < +1 ) x^n dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the exponent.
#    0 <= N.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  if ( ( n % 2 ) == 1 ):
    value = 0.0
  else:
    value = 2.0 / ( n + 1 )

  return value

def j_polynomial ( m, n, alpha, beta, x ):

#*****************************************************************************80
#
## j_polynomial() evaluates the Jacobi polynomials J(N,A,B,X).
#
#  Differential equation:
#
#    (1-X*X) Y'' + (BETA-ALPHA-(ALPHA+BETA+2) X) Y' + N (N+ALPHA+BETA+1) Y = 0
#
#  Recursion:
#
#    P(0,ALPHA,BETA,X) = 1,
#
#    P(1,ALPHA,BETA,X) = ( (2+ALPHA+BETA)*X + (ALPHA-BETA) ) / 2
#
#    P(N,ALPHA,BETA,X)  = 
#      ( 
#        (2*N+ALPHA+BETA-1) 
#        * ((ALPHA^2-BETA^2)+(2*N+ALPHA+BETA)*(2*N+ALPHA+BETA-2)*X) 
#        * P(N-1,ALPHA,BETA,X)
#        -2*(N-1+ALPHA)*(N-1+BETA)*(2*N+ALPHA+BETA) * P(N-2,ALPHA,BETA,X)
#      ) / 2*N*(N+ALPHA+BETA)*(2*N-2+ALPHA+BETA)
#
#  Restrictions:
#
#    -1 < ALPHA
#    -1 < BETA
#
#  Norm:
#
#    Integral ( -1 <= X <= 1 ) ( 1 - X )^ALPHA * ( 1 + X )^BETA 
#      * P(N,ALPHA,BETA,X)^2 dX 
#    = 2^(ALPHA+BETA+1) * Gamma ( N + ALPHA + 1 ) * Gamma ( N + BETA + 1 ) /
#      ( 2 * N + ALPHA + BETA ) * N! * Gamma ( N + ALPHA + BETA + 1 )
#
#  Special values:
#
#    P(N,ALPHA,BETA)(1) = (N+ALPHA)!/(N!*ALPHA!) for integer ALPHA.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest order polynomial to compute.  Note
#    that polynomials 0 through N will be computed.
#
#    real ALPHA, BETA, the parameters.
#    -1 < ALPHA, BETA.
#
#    real X(M,1), the evaluation points.
#
#  Output:
#
#    real V(M,1:N+1), the values of the first N+1 Jacobi
#    polynomials at the point X.
#
  import numpy as np

  if ( alpha <= -1.0 ):
    print ( '' )
    print ( 'j_polynomial(): Fatal error!' )
    print ( '  Illegal input value of ALPHA = ', alpha )
    print ( '  But ALPHA must be greater than -1.' )
    raise Exception ( 'j_polynomial(): Fatal error!' )
 
  if ( beta <= -1.0 ):
    print ( '' )
    print ( 'j_polynomial(): Fatal error!' )
    print ( '  Illegal input value of BETA = ', beta )
    print ( '  But BETA must be greater than -1.' )
    raise Exception ( 'j_polynomial(): Fatal error!' ) 
  
  if ( n < 0 ):
    v = np.array ( [] )
    return v

  v = np.zeros ( [ m, n + 1 ] )

  v[0:m,0] = 1.0

  x = np.atleast_1d ( x )

  if ( n == 0 ):
    return v

  v[0:m,1] = ( 1.0 + 0.5 * ( alpha + beta ) ) * x[0:m]  + 0.5 * ( alpha - beta )
 
  for i in range ( 2, n + 1 ):

    c1 = 2 * i * ( i + alpha + beta ) * ( 2 * i - 2 + alpha + beta )

    c2 = ( 2 * i - 1 + alpha + beta ) * ( 2 * i + alpha + beta ) \
      * ( 2 * i - 2 + alpha + beta )

    c3 = ( 2 * i - 1 + alpha + beta ) * ( alpha + beta ) * ( alpha - beta )

    c4 = - 2 * ( i - 1 + alpha ) * ( i - 1 + beta ) * ( 2 * i + alpha + beta )

    v[0:m,i] = ( ( c3 + c2 * x[0:m] ) * v[0:m,i-1] + c4 * v[0:m,i-2] ) / c1

  return v

def j_polynomial_plot ( n_vec, alpha_vec, beta_vec, filename ):

#*****************************************************************************80
#
## j_polynomial_plot() plots Jacobi polynomials J(n,a,b,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_VEC(*), the orders of 1 or more polynomials
#    to be plotted together.
#
#    integer ALPHA_VEC(*), BETA_VEC(*), the alpha and beta values
#    for each polynomial.
#
#    string FILENAME, the name into which the graphics information is
#    to be stored.  Note that the PNG format will be used.
#
  import matplotlib.pyplot as plt
  import numpy as np

  a = -1.0
  b = +1.0
  m = 501
  x = np.linspace ( a, b, m )
  vec_num = len ( n_vec )

  plt.clf ( )

  for i in range ( 0, vec_num ):
    n = n_vec[i]
    alpha = alpha_vec[i]
    beta = beta_vec[i]
    y = j_polynomial ( m, n, alpha, beta, x )
    plt.plot ( x, y[:,n], LineWidth = 2 )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- J(n,a,b,x) --->' )
  plt.title ( 'Jacobi polynomials J(n,a,b,x)' )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

  return

def j_polynomial_values ( n_data ):

#*****************************************************************************80
#
## j_polynomial_values() returns some values of the Jacobi polynomial.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      JacobiP[ n, a, b, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2025
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Input:
#
#    integer n_data.  The user sets n_data to 0 before the first call.  
#
#  Output:
#
#    integer n_data.  On each call, the routine increments n_data by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of n_data will be 0 again.
#
#    integer N, the degree of the polynomial.
#
#    real A, B, parameters of the function.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 26

  a_vec = np.array ( (\
     0.0, 0.0, 0.0, 0.0, \
     0.0, 0.0, 1.0, 2.0, \
     3.0, 4.0, 5.0, 0.0, \
     0.0, 0.0, 0.0, 0.0, \
     0.0, 0.0, 0.0, 0.0, \
     0.0, 0.0, 0.0, 0.0, \
     0.0, 0.0 ))

  b_vec = np.array ( (\
    1.0, 1.0, 1.0, 1.0, \
    1.0, 1.0, 1.0, 1.0, \
    1.0, 1.0, 1.0, 2.0, \
    3.0, 4.0, 5.0, 1.0, \
    1.0, 1.0, 1.0, 1.0, \
    1.0, 1.0, 1.0, 1.0, \
    1.0, 1.0 ))

  f_vec = np.array ( (\
      1.000000000000000, \
      0.2500000000000000, \
     -0.3750000000000000, \
     -0.4843750000000000, \
     -0.1328125000000000, \
      0.2753906250000000, \
     -0.1640625000000000, \
     -1.174804687500000, \
     -2.361328125000000, \
     -2.616210937500000, \
      0.1171875000000000, \
      0.4218750000000000, \
      0.5048828125000000, \
      0.5097656250000000, \
      0.4306640625000000, \
     -6.000000000000000, \
      0.03862000000000000, \
      0.8118400000000000, \
      0.03666000000000000, \
     -0.4851200000000000, \
     -0.3125000000000000, \
      0.1891200000000000, \
      0.4023400000000000, \
      0.01216000000000000, \
     -0.4396200000000000, \
      1.000000000000000 ))

  n_vec = np.array ( (\
     0, 1, 2, 3, \
     4, 5, 5, 5, \
     5, 5, 5, 5, \
     5, 5, 5, 5, \
     5, 5, 5, 5, \
     5, 5, 5, 5, \
     5, 5 ))

  x_vec = np.array ( (\
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
      0.5, \
     -1.0, \
     -0.8, \
     -0.6, \
     -0.4, \
     -0.2, \
      0.0, \
      0.2, \
      0.4, \
      0.6, \
      0.8, \
      1.0 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    a = 0.0
    b = 0.0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    a = a_vec[n_data]
    b = b_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, a, b, x, f

def j_polynomial_zeros ( n, alpha, beta ):

#*****************************************************************************80
#
## j_polynomial_zeros(): zeros of Jacobi polynomial J(n,a,b,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2025
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
#    integer N, the order.
#
#    real ALPHA, BETA, the parameters.
#    -1 < ALPHA, BETA.
#
#  Output:
#
#    real X(N), the zeros.
#
  from scipy.special import gamma
  import numpy as np

  ab = alpha + beta
  abi = 2.0 + ab
#
#  Define the zero-th moment.
#
  zemu = 2.0**( ab + 1.0 ) * gamma ( alpha + 1.0 ) \
    * gamma ( beta + 1.0 ) / gamma ( abi )
#
#  Define the Jacobi matrix.
#
  x = np.zeros ( n )
  bj = np.zeros ( n )

  x[0] = ( beta - alpha ) / abi
  bj[0] = 4.0 * ( 1.0 + alpha ) * ( 1.0 + beta ) \
    / ( ( abi + 1.0 ) * abi * abi )
  a2b2 = beta * beta - alpha * alpha

  for i in range ( 2, n + 1 ):
    abi = 2.0 * i + ab
    x[i-1] = a2b2 / ( ( abi - 2.0 ) * abi )
    abi = abi * abi
    bj[i-1] = 4.0 * i * ( i + alpha ) * ( i + beta ) * ( i + ab ) \
      / ( ( abi - 1.0 ) * abi )

  bj[0:n] = np.sqrt ( bj[0:n] )

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  return x

def j_quadrature_rule ( n, alpha, beta ):

#*****************************************************************************80
#
## j_quadrature_rule(): Gauss-Jacobi quadrature based on J(n,a,b,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 February 2025
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
#    integer N, the order.
#
#    real ALPHA, BETA, the parameters.
#    -1 < ALPHA, BETA.
#
#  Output:
#
#    real X(N), the abscissas.
#
#    real W(N), the weights.
#
  from scipy.special import gamma
  import numpy as np

  ab = alpha + beta
  abi = 2.0 + ab
#
#  Define the zero-th moment.
#
  zemu = 2.0**( ab + 1.0 ) * gamma ( alpha + 1.0 ) \
    * gamma ( beta + 1.0 ) / gamma ( abi )
#
#  Define the Jacobi matrix.
#
  x = np.zeros ( n )
  bj = np.zeros ( n )

  x[0] = ( beta - alpha ) / abi
  bj[0] = 4.0 * ( 1.0 + alpha ) * ( 1.0 + beta ) \
    / ( ( abi + 1.0 ) * abi * abi )
  a2b2 = beta * beta - alpha * alpha

  for i in range ( 2, n + 1 ):
    abi = 2.0 * i + ab
    x[i-1] = a2b2 / ( ( abi - 2.0 ) * abi )
    abi = abi * abi
    bj[i-1] = 4.0 * i * ( i + alpha ) * ( i + beta ) * ( i + ab ) \
      / ( ( abi - 1.0 ) * abi )

  bj[:] = np.sqrt ( bj[:] )

  w = np.zeros ( n )
  w[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  x, w = imtqlx ( n, x, bj, w )

  w[:] = w[:]**2

  return x, w

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

  return

def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#    In Python, use:
#
#      print ( title )
#      print ( np.c_ [ a1, a2 ] )
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
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

def r8_sign ( x ):

#*****************************************************************************80
#
## r8_sign() returns the sign of an R8.
#
#  Discussion:
#
#    The value is +1 if the number is positive or zero, and it is -1 otherwise.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the number whose sign is desired.
#
#  Output:
#
#    real VALUE, the sign of X.
#
  if ( x < 0.0 ):
    value = -1.0
  else:
    value = +1.0
 
  return value

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
  jacobi_polynomial_test ( )
  timestamp ( )

