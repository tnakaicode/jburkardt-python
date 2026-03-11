#! /usr/bin/env python3
#
def legendre_polynomial_test ( ):

#*****************************************************************************80
#
## legendre_polynomial_test() tests legendre_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'legendre_polynomial_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test legendre_polynomial().' )

  imtqlx_test ( )

  p = 5
  b = 0.0
  p_exponential_product_test ( p, b )

  p = 5
  b = 1.0
  p_exponential_product_test ( p, b )

  p_integral_test ( )

  p_polynomial_coefficients_test ( )
  p_polynomial_plot_test ( )
  p_polynomial_prime_test ( )
  p_polynomial_prime2_test ( )
  p_polynomial_value_test ( )
  p_polynomial_values_test ( )
  p_polynomial_zeros_test ( )

  p = 5
  e = 0
  p_power_product_test ( p, e )

  p = 5
  e = 1
  p_power_product_test ( p, e )

  p_quadrature_rule_test ( )

  pm_polynomial_value_test ( )
  pm_polynomial_values_test ( )

  pmn_polynomial_value_test ( )
  pmn_polynomial_values_test ( )

  pmns_polynomial_value_test ( )
  pmns_polynomial_values_test ( )

  p = 5
  pn_pair_product_test ( p )
  pn_polynomial_coefficients_test ( )
  pn_polynomial_value_test ( )
  pn_polynomial_values_test ( )

  r8_sign_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'legendre_polynomial_test():' )
  print ( '  Normal end of execution.' )
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

  epsilon = np.finfo(float).eps

  e[n-1] = 0.0

  for l in range ( 1, n + 1 ):

    j = 0

    while ( True ):

      for m in range ( l, n + 1 ):

        if ( m == n ):
          break

        if ( abs ( e[m-1] ) <= epsilon * ( abs ( lam[m-1] ) + abs ( lam[m] ) ) ):
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

def imtqlx_test ( ):

#*****************************************************************************80
#
## imtqlx_test() tests imtqlx().
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
  import numpy as np

  print ( '' )
  print ( 'imtqlx_test():' )
  print ( '  imtqlx() takes a symmetric tridiagonal matrix A' )
  print ( '  and computes its eigenvalues LAM.' )
  print ( '  It also accepts a vector Z and computes Q\'*Z,' )
  print ( '  where Q is the matrix that diagonalizes A.' )

  n = 5
  d = np.zeros ( n )
  for i in range ( 0, n ):
    d[i] = 2.0;
  e = np.zeros ( n )
  for i in range ( 0, n - 1 ):
    e[i] = -1.0
  e[n-1] = 0.0
  z = np.ones ( n )

  lam, qtz = imtqlx ( n, d, e, z )

  r8vec_print ( n, lam, '  Computed eigenvalues:' )

  lam2 = np.zeros ( n )
  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( 2 * ( n + 1 ) )
    lam2[i] = 4.0 * ( np.sin ( angle ) ) ** 2

  r8vec_print ( n, lam2, '  Exact eigenvalues:' )

  r8vec_print ( n, z, '  Vector Z:' )
  r8vec_print ( n, qtz, '  Vector Q''*Z:' )

  return

def legendre_to_monomial_matrix ( n ):

#*****************************************************************************80
#
## legendre_to_monomial_matrix() converts from Legendre to monomial form.
#
#  Discussion:
#
#    If PL(x) is a linear combination of Legendre polynomials
#    with coefficients CL, then PM(x) is a linear combination of
#    monomials with coefficients CM = A * CL.
#    
#    The coefficients are ordered so the constant term is first.
#
#  Example:
#
#    N = 11 (each column must be divided by factor at bottom)
#
#     1    .    -1     .      3     .     -5      .      35     .   -63
#     .    1     .    -3      .    15      .    -25       .   315     .
#     .    .     3     .    -30     .    105      .   -1260     .  3465
#     .    .     .     5      .   -70      .    315       . -4620     .
#     .    .     .     .     35     .   -315      .    6930     .-30030
#     .    .     .     .      .    63      .   -693       . 18018     .
#     .    .     .     .      .     .    231      .  -12012     . 90090
#     .    .     .     .      .     .      .    429       .-25740     .
#     .    .     .     .      .     .      .      .    6435     -109395
#     .    .     .     .      .     .      .      .       . 12155     .
#     .    .     .     .      .     .      .      .       .     . 46189
#
#    /1   /1    /2    /2     /8    /8    /16    /16    /128  /128  /256
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
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

  A = np.zeros ( ( n, n ) )

  if ( n <= 0 ):
    return A

  A[0,0] = 1.0

  if ( n == 1 ):
    return A

  A[1,1] = 1.0

  if ( n == 2 ):
    return A

  for j in range ( 3, n + 1 ):
    for i in range ( 1, n + 1 ):
      if ( i == 1 ):
        A[i-1,j-1] = - ( j - 2 ) * A[i-1,j-3] \
                     / ( j - 1 )
      else:
        A[i-1,j-1] = ( ( 2 * j - 3 ) * A[i-2,j-2] \
                     + (   - j + 2 ) * A[i-1,j-3] ) \
                     / (     j - 1 )

  return A

def monomial_to_legendre_matrix ( n ):

#*****************************************************************************80
#
## monomial_to_legendre_matrix(): convert monomial to Legendre basis.
#
#  Discussion:
#
#    If PM(x) is a linear combination of monomials
#    with coefficients CM, then PL(x) is a linear combination of
#    Legendre polynomials with coefficients CL = A * CM.
#    
#    The coefficients are ordered such that
#    the constant term is first.
#
#  Example:
#
#    N = 11 (each column must be divided by the underlying factor).
#
#       1     .      1     .      7     .    33    .   715    . 4199
#       .     1      .     3      .    27     .  143     . 3315    .
#       .     .      2     .     20     .   110    .  2600    .16150
#       .     .      .     2      .    28     .  182     . 4760    .
#       .     .      .     .      8     .    72    .  2160    .15504
#       .     .      .     .      .     8     .   88     . 2992    .
#       .     .      .     .      .     .    16    .   832    . 7904
#       .     .      .     .      .     .     .   16     .  960    .
#       .     .      .     .      .     .     .    .   128    . 2176
#       .     .      .     .      .     .     .    .     .  128    .
#       .     .      .     .      .     .     .    .     .    .  256
#
#      /1    /1     /3    /5    /35   /63  /231 /429 /6435/12155/46189  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 March 2015
#
#  Author:
#
#    John Burkardt 
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

  a[0,0] = 1.0

  if ( 1 < n ):

    a[1,1] = 1.0

    if ( 2 < n ):

      for j in range ( 2, n ):
        for i in range ( 0, n ):

          if ( i == 0 ):

            a[i,j] = (     i + 1 ) * a[i+1,j-1] / float ( 2 * i + 3 )

          elif ( i < n - 1 ):

            a[i,j] = (     i     ) * a[i-1,j-1] / float ( 2 * i - 1 ) \
                   + (     i + 1 ) * a[i+1,j-1] / float ( 2 * i + 3 )

          else:

            a[i,j] = (     i     ) * a[i-1,j-1] / float ( 2 * i - 1 )

  return a

def p_exponential_product ( p, b ):

#*****************************************************************************80
#
## p_exponential_product(): exponential products for P(n,x).
#
#  Discussion:
#
#    Let P(n,x) represent the Legendre polynomial of degree i.  
#
#    For polynomial chaos applications, it is of interest to know the
#    value of the integrals of products of exp(B*X) with every possible pair
#    of basis functions.  That is, we'd like to form
#
#      Tij = Integral ( -1 <= X <= +1 ) exp(B*x) * P(i,x) * P(j,x) dx
#
#    Because of the exponential factor, the quadrature will not be exact.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polyonomial factors.
#    0 <= P.
#
#    real B, the coefficient of X in the exponential factor.
#
#  Output:
#
#    real TABLE(P+1,P+1), the table of integrals.
#
  import numpy as np

  xvec = np.zeros ( 1 )
  table = np.zeros ( [ p + 1, p + 1 ] )

  order = ( ( 3 * p + 4 ) // 2 )

  x_table, w_table = p_quadrature_rule ( order )

  for k in range ( 0, order ):

    x = x_table[k]
    xvec[0] = x
    l_table = p_polynomial_value ( 1, p, xvec )
#
#  The following formula is an outer product in L_TABLE.
#
    for i in range ( 0, p + 1 ):
      for j in range ( 0, p + 1 ):
        table[i,j] = table[i,j] \
          + w_table[k] * np.exp ( b * x ) * l_table[0,i] * l_table[0,j]

  return table

def p_exponential_product_test ( p, b ):

#*****************************************************************************80
#
## p_exponential_product_test() tests p_exponential_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polynomial 
#    factors.
#
#    real B, the coefficient of X in the exponential factor.
#
  import platform

  print ( '' )
  print ( 'p_exponential_product_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  p_exponential_product computes an exponential product table for P(n,x):' )
  print ( '' )
  print ( '  Tij = integral ( -1 <= x <= +1 ) exp(b*x) P(i,x) P(j,x) dx' )

  print ( '' )
  print ( '  Maximum degree P = %d' % ( p ) )
  print ( '  Exponential argument coefficient B = %g' % ( b ) )

  table = p_exponential_product ( p, b )

  r8mat_print ( p + 1, p + 1, table, '  Exponential product table:' )

  return

def p_integral ( n ):

#*****************************************************************************80
#
## p_integral() evaluates a monomial integral associated with P(n,x).
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
#    15 March 2016
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

def p_integral_test ( ):

#*****************************************************************************80
#
## p_integral_test() tests p_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'p_integral_test()' )
  print ( '  p_integral() returns the integral of P(n,x) over [-1,+1].' )
  print ( '' )
  print ( '     N                  Integral' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = p_integral ( n )

    print ( '  %4d  %24.16g' % ( n, value ) )

  return

def pmn_polynomial_value ( mm, n, m, x ):

#*****************************************************************************80
#
## pmn_polynomial_value(): normalized Legendre polynomial Pmn(n,m,x).
#
#  Discussion:
#
#    The unnormalized associated Legendre functions p_N^M(X) have
#    the property that
#
#      Integral ( -1 <= X <= 1 ) ( p_N^M(X) )^2 dX 
#      = 2 * ( N + M )! / ( ( 2 * N + 1 ) * ( N - M )! )
#
#    By dividing the function by the square root of this term,
#    the normalized associated Legendre functions have norm 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 March 2017
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#  Input:
#
#    integer MM, the number of evaluation points.
#
#    integer N, the maximum first index of the Legendre
#    function, which must be at least 0.
#
#    integer M, the second index of the Legendre function,
#    which must be at least 0, and no greater than N.
#
#    real X(MM,1), the evaluation points.
#
#  Output:
#
#    real CX(MM,N+1), the function values.
#
  from scipy.special import factorial
  import numpy as np

  if ( m < 0 ):
    print ( '' )
    print ( 'pmn_polynomial_value - Fatal error!' )
    print ( '  Input value of M is %d' % ( m ) )
    print ( '  but M must be nonnegative.' )
    raise Exception ( 'pmn_polynomial_value - Fatal error!' )
 
  if ( n < m ):
    print ( '' )
    print ( 'pmn_polynomial_value - Fatal error!' )
    print ( '  Input value of M = %d' % ( m ) )
    print ( '  Input value of N = %d' % ( n ) )
    print ( '  but M must be less than or equal to N.' )
    raise Exception ( 'pmn_polynomial_value - Fatal error!' )

  cx = np.zeros ( [ mm, n + 1 ] )

  if ( m <= n ):
    for i in range ( 0, mm ):
      cx[i,m] = 1.0 
    factor = 1.0
    for j in range ( 0, m ):
      for i in range ( 0, mm ):
        cx[i,m] = - factor * cx[i,m] * np.sqrt ( 1.0 - x[i] ** 2 )
      factor = factor + 2.0

  if ( m + 1 <= n ):
    for i in range ( 0, mm ):
      cx[i,m+1] = ( 2 * m + 1 ) * x[i] * cx[i,m]

  for j in range ( m + 2, n + 1 ):
    for i in range ( 0, mm ):
      cx[i,j] = ( ( 2 * j     - 1 ) * x[i] * cx[i,j-1] \
                + (   - j - m + 1 ) *        cx[i,j-2] ) \
                / (     j - m     )
#
#  Normalization.
#
  for j in range ( m, n + 1 ):
    factor = np.sqrt ( ( ( 2 * j + 1 ) * factorial ( j - m ) ) \
      / ( 2.0 * factorial ( j + m ) ) )
    for i in range ( 0, mm ):
      cx[i,j] = cx[i,j] * factor

  return cx

def pmn_polynomial_value_test ( ):

#*****************************************************************************80
#
## pmn_polynomial_value_test() tests pmn_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  mm = 1
  xvec = np.zeros ( 1 )

  print ( '' )
  print ( 'pmn_polynomial_value_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pmn_polynomial_value evaluates the Legendre polynomial Pmn(n,m,x).' )
  print ( '' )
  print ( '                                          Tabulated                 Computed' )
  print ( '     N     M             X                Pmn(N,M,X)                Pmn(N,M,X)         Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, x, fx1 = pmn_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    xvec[0] = x
    v = pmn_polynomial_value ( mm, n, m, xvec )
    fx2 = v[0,n]

    e = fx1 - fx2

    print ( '  %4d  %4d  %12g  %24.16g  %24.16g  %8g' % ( n, m, x, fx1, fx2, e ) )

  return

def pmn_polynomial_values ( n_data ):

#*****************************************************************************80
#
## pmn_polynomial_values(): selected values of associated Legendre functions.
#
#  Discussion:
#
#    The function considered is the associated Legendre polynomial P^M_N(X).
#
#    In Mathematica, the function can be evaluated by:
#
#      LegendreP [ n, m, x ]
#
#    The function is normalized by dividing by
#
#      sqrt ( 2 * ( n + m )! / ( 2 * n + 1 ) / ( n - m )! )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
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
#    integer N_DATA.  The user sets N_DATA to 0 before the first call. 
#
#  Output:
#
#    integer N_DATA.   On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, integer M, real X, 
#    the arguments of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 21

  f_vec = np.array ( ( \
    0.7071067811865475E+00, \
    0.6123724356957945E+00, \
   -0.7500000000000000E+00, \
   -0.1976423537605237E+00, \
   -0.8385254915624211E+00, \
    0.7261843774138907E+00, \
   -0.8184875533567997E+00, \
   -0.1753901900050285E+00, \
    0.9606516343087123E+00, \
   -0.6792832849776299E+00, \
   -0.6131941618102092E+00, \
    0.6418623720763665E+00, \
    0.4716705890038619E+00, \
   -0.1018924927466445E+01, \
    0.6239615396237876E+00, \
    0.2107022704608181E+00, \
    0.8256314721961969E+00, \
   -0.3982651281554632E+00, \
   -0.7040399320721435E+00, \
    0.1034723155272289E+01, \
   -0.5667412129155530E+00 ))

  m_vec = np.array ( ( \
    0, 0, 1, 0, \
    1, 2, 0, 1, \
    2, 3, 0, 1, \
    2, 3, 4, 0, \
    1, 2, 3, 4, \
    5 ))

  n_vec = np.array ( ( \
    0,  1,  1,  2, \
    2,  2,  3,  3, \
    3,  3,  4,  4, \
    4,  4,  4,  5, \
    5,  5,  5,  5, \
    5 ))

  x_vec = np.array ( ( \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    m = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    m = m_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, m, x, f

def pmn_polynomial_values_test ( ):

#*****************************************************************************80
#
## pmn_polynomial_values_test() tests pmn_polynomial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pmn_polynomial_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pmn_polynomial_values stores values of the ' )
  print ( '  normalized associated Legendre function.' )
  print ( '' )
  print ( '      N       M            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, x, f = pmn_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %6d  %12g  %24.16g' % ( n, m, x, f ) )

  return

def pmns_polynomial_value ( mm, n, m, x ):

#*****************************************************************************80
#
## pmns_polynomial_value(): sphere_normalized Legendre polynomial Pmn(n,m,x).
#
#  Discussion:
#
#    The unnormalized associated Legendre functions p_N^M(X) have
#    the property that
#
#      Integral ( -1 <= X <= 1 ) ( p_N^M(X) )^2 dX 
#      = 2 * ( N + M )! / ( ( 2 * N + 1 ) * ( N - M )! )
#
#    By dividing the function by the square root of this term,
#    the normalized associated Legendre functions have norm 1.
#
#    However, we plan to use these functions to build spherical
#    harmonics, so we use a slightly different normalization factor of
#
#      sqrt ( ( ( 2 * N + 1 ) * ( N - M )! ) / ( 4 * pi * ( N + M )! ) ) 
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#  Input:
#
#    integer MM, the number of evaluation points.
#
#    integer N, the maximum first index of the Legendre
#    function, which must be at least 0.
#
#    integer M, the second index of the Legendre function,
#    which must be at least 0, and no greater than N.
#
#    real X(MM,1), the evaluation points.
#
#  Output:
#
#    real CX(MM,N+1), the function values.
#
  from scipy.special import factorial
  import numpy as np

  cx = np.zeros ( [ mm, n + 1 ] )

  if ( m <= n ):
    for i in range ( 0, mm ):
      cx[i,m] = 1.0 
    factor = 1.0
    for j in range ( 0, m ):
      for i in range ( 0, mm ):
        cx[i,m] = - factor * cx[i,m] * np.sqrt ( 1.0 - x[i] ** 2 )
      factor = factor + 2.0

  if ( m + 1 <= n ):
    for i in range ( 0, mm ):
      cx[i,m+1] = ( 2 * m + 1 ) * x[i] * cx[i,m]

  for j in range ( m + 2, n + 1 ):
    for i in range ( 0, mm ):
      cx[i,j] = ( ( 2 * j     - 1 ) * x[i] * cx[i,j-1] \
                + (   - j - m + 1 ) *        cx[i,j-2] ) \
                / (     j - m     )
#
#  Normalization.
#
  for j in range ( m, n + 1 ):
    factor = np.sqrt ( ( ( 2 * j + 1 ) * factorial ( j - m ) ) \
      / ( 4.0 * np.pi * factorial ( j + m ) ) )
    for i in range ( 0, mm ):
      cx[i,j] = cx[i,j] * factor

  return cx

def pmns_polynomial_value_test ( ):

#*****************************************************************************80
#
## pmns_polynomial_value_test() tests pmns_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  mm = 1
  xvec = np.zeros ( 1 )

  print ( '' )
  print ( 'pmns_polynomial_value_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pmns_polynomial_value evaluates the Legendre polynomial Pmns(n,m,x).' )
  print ( '' )
  print ( '                                         Tabulated                 Computed' )
  print ( '     N     M             X               Pmns(N,M,X)               Pmns(N,M,X)         Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, x, fx1 = pmns_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    xvec[0] = x
    v = pmns_polynomial_value ( mm, n, m, xvec )
    fx2 = v[0,n]

    e = fx1 - fx2

    print ( '  %4d  %4d  %12g  %24.16g  %24.16g  %8g' % ( n, m, x, fx1, fx2, e ) )

  return

def pmns_polynomial_values ( n_data ):

#*****************************************************************************80
#
## pmns_polynomial_values(): selected values of the associated Legendre polynomial normalized for sphere.
#
#  Discussion:
#
#    The function considered is the associated Legendre polynomial P^M_N(X).
#
#    In Mathematica, the function can be evaluated by:
#
#      LegendreP [ n, m, x ]
#
#    The function is normalized for the unit sphere by dividing by
#
#      sqrt ( 4 * pi * ( n + m )! / ( 2 * n + 1 ) / ( n - m )! )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
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
#    integer N_DATA.  The user sets N_DATA to 0 before the first call. 
#
#  Output:
#
#    integer N_DATA.   On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.g
#
#    integer N, integer M, real X, 
#    the arguments of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 21

  f_vec = np.array ( ( \
     0.2820947917738781, \
     0.2443012559514600, \
    -0.2992067103010745, \
    -0.07884789131313000, \
    -0.3345232717786446, \
     0.2897056515173922, \
    -0.3265292910163510, \
    -0.06997056236064664, \
     0.3832445536624809, \
    -0.2709948227475519, \
    -0.2446290772414100, \
     0.2560660384200185, \
     0.1881693403754876, \
    -0.4064922341213279, \
     0.2489246395003027, \
     0.08405804426339821, \
     0.3293793022891428, \
    -0.1588847984307093, \
    -0.2808712959945307, \
     0.4127948151484925, \
    -0.2260970318780046  ))

  m_vec = np.array ( ( \
    0, 0, 1, 0, \
    1, 2, 0, 1, \
    2, 3, 0, 1, \
    2, 3, 4, 0, \
    1, 2, 3, 4, \
    5 ))

  n_vec = np.array ( ( \
    0,  1,  1,  2, \
    2,  2,  3,  3, \
    3,  3,  4,  4, \
    4,  4,  4,  5, \
    5,  5,  5,  5, \
    5 ))

  x_vec = np.array ( ( \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50, \
    0.50 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    m = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    m = m_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, m, x, f

def pmns_polynomial_values_test ( ):

#*****************************************************************************80
#
## pmns_polynomial_values_test() tests pmns_polynomial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pmns_polynomial_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pmns_polynomial_values stores values of the ' )
  print ( '  associated Legendre function normalized for the surface of a sphere.' )
  print ( '' )
  print ( '      N       M            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, x, f = pmns_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %6d  %12g  %24.16g' % ( n, m, x, f ) )

  return

def pm_polynomial_value ( mm, n, m, x ):

#*****************************************************************************80
#
## pm_polynomial_value() evaluates the Legendre polynomials Pm(n,m,x).
#
#  Differential equation:
#
#    (1-X*X) * Y'' - 2 * X * Y + ( N (N+1) - (M*M/(1-X*X)) * Y = 0
#
#  First terms:
#
#    M = 0  ( = Legendre polynomials of first kind P(N,X) )
#
#    Pm(0,0,x) =    1
#    Pm(1,0,x) =    1 X
#    Pm(2,0,x) = (  3 X^2 -   1)/2
#    Pm(3,0,x) = (  5 X^3 -   3 X)/2
#    Pm(4,0,x) = ( 35 X^4 -  30 X^2 +   3)/8
#    Pm(5,0,x) = ( 63 X^5 -  70 X^3 +  15 X)/8
#    Pm(6,0,x) = (231 X^6 - 315 X^4 + 105 X^2 -  5)/16
#    Pm(7,0,x) = (429 X^7 - 693 X^5 + 315 X^3 - 35 X)/16
#
#    M = 1
#
#    Pm(0,1,x) =   0
#    Pm(1,1,x) =   1 * SQRT(1-X^2)
#    Pm(2,1,x) =   3 * SQRT(1-X^2) * X
#    Pm(3,1,x) = 1.5 * SQRT(1-X^2) * (5*X^2-1)
#    Pm(4,1,x) = 2.5 * SQRT(1-X^2) * (7*X^3-3*X)
#
#    M = 2
#
#    Pm(0,2,x) =   0
#    Pm(1,2,x) =   0
#    Pm(2,2,x) =   3 * (1-X^2)
#    Pm(3,2,x) =  15 * (1-X^2) * X
#    Pm(4,2,x) = 7.5 * (1-X^2) * (7*X^2-1)
#
#    M = 3
#
#    Pm(0,3,x) =   0
#    Pm(1,3,x) =   0
#    Pm(2,3,x) =   0
#    Pm(3,3,x) =  15 * (1-X^2)^1.5
#    Pm(4,3,x) = 105 * (1-X^2)^1.5 * X
#
#    M = 4
#
#    Pm(0,4,x) =   0
#    Pm(1,4,x) =   0
#    Pm(2,4,x) =   0
#    Pm(3,4,x) =   0
#    Pm(4,4,x) = 105 * (1-X^2)^2
#
#  Recursion:
#
#    if N < M:
#      Pm(N,M,x) = 0
#    if N = M:
#      Pm(N,M,x) = (2*M-1)!! * (1-X*X)^(M/2) where N!! means the product of
#      all the odd integers less than or equal to N.
#    if N = M+1:
#      Pm(N,M,x) = X*(2*M+1)*Pm(M,M,x)
#    if M+1 < N:
#      Pm(N,M,x) = ( X*(2*N-1)*Pm(N-1,M,x) - (N+M-1)*Pm(N-2,M,x) )/(N-M)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#  Input:
#
#    integer MM, the number of evaluation points.
#
#    integer N, the maximum first index of the Legendre
#    function, which must be at least 0.
#
#    integer M, the second index of the Legendre function,
#    which must be at least 0, and no greater than N.
#
#    real X(MM), the point at which the function is to be
#    evaluated.
#
#  Output:
#
#    real CX(MM,N+1), the function values.
#
  import numpy as np

  cx = np.zeros ( [ mm, n + 1 ] )
#
#  J = M is the first nonzero function.
#
  if ( m <= n ):
    for i in range ( 0, mm ):
      cx[i,m] = 1.0

    fact = 1.0
    for j in range ( 0, m ):
      for i in range ( 0, mm ):
        cx[i,m] = - cx[i,m] * fact * np.sqrt ( 1.0 - x[i] ** 2 )
      fact = fact + 2.0
#
#  J = M + 1 is the second nonzero function.
#
  if ( m + 1 <= n ):
    for i in range ( 0, mm ):
      cx[i,m+1] = ( 2 * m + 1 ) * x[i] * cx[i,m]
#
#  Now we use a three term recurrence.
#
  for j in range ( m + 2, n + 1 ):
    for i in range ( 0, mm ):
      cx[i,j] = ( ( 2 * j     - 1 ) * x[i] * cx[i,j-1] \
                + (   - j - m + 1 ) *        cx[i,j-2] ) \
                / (     j - m     )

  return cx

def pm_polynomial_value_test ( ):

#*****************************************************************************80
#
## pm_polynomial_value_test() tests pm_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  mm = 1
  xvec = np.zeros ( 1 )

  print ( '' )
  print ( 'pm_polynomial_value_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pm_polynomial_value evaluates the Legendre polynomial Pm(n,m,x).' )
  print ( '' )
  print ( '                                           Tabulated                 Computed' )
  print ( '     N     M             X                 Pm(N,M,X)                 Pm(N,M,X)     Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, x, fx1 = pm_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    xvec[0] = x

    v = pm_polynomial_value ( mm, n, m, xvec )
    fx2 = v[0,n]

    e = fx1 - fx2

    print ( '  %4d  %4d  %12g  %24.16g  %24.16g  %8g' % ( n, m, x, fx1, fx2, e ) )

  return

def pm_polynomial_values ( n_data ):

#*****************************************************************************80
#
## pm_polynomial_values(): selected values of associated Legendre functions.
#
#  Discussion:
#
#    The function considered is the associated Legendre polynomial P^M_N(X).
#
#    In Mathematica, the function can be evaluated by:
#
#      LegendreP [ n, m, x ]
#
#  Differential equation:
#
#    (1-X*X) * Y'' - 2 * X * Y + ( N (N+1) - (M*M/(1-X*X)) * Y = 0
#
#  First terms:
#
#    M = 0  ( = Legendre polynomials of first kind P(N)(X) )
#
#    P00 =    1
#    P10 =    1 X
#    P20 = (  3 X^2 -   1)/2
#    P30 = (  5 X^3 -   3 X)/2
#    P40 = ( 35 X^4 -  30 X^2 +   3)/8
#    P50 = ( 63 X^5 -  70 X^3 +  15 X)/8
#    P60 = (231 X^6 - 315 X^4 + 105 X^2 -  5)/16
#    P70 = (429 X^7 - 693 X^5 + 315 X^3 - 35 X)/16
#
#    M = 1
#
#    P01 =   0
#    P11 =   1 * SQRT(1-X*X)
#    P21 =   3 * SQRT(1-X*X) * X
#    P31 = 1.5 * SQRT(1-X*X) * (5*X*X-1)
#    P41 = 2.5 * SQRT(1-X*X) * (7*X*X*X-3*X)
#
#    M = 2
#
#    P02 =   0
#    P12 =   0
#    P22 =   3 * (1-X*X)
#    P32 =  15 * (1-X*X) * X
#    P42 = 7.5 * (1-X*X) * (7*X*X-1)
#
#    M = 3
#
#    P03 =   0
#    P13 =   0
#    P23 =   0
#    P33 =  15 * (1-X*X)^1.5
#    P43 = 105 * (1-X*X)^1.5 * X
#
#    M = 4
#
#    P04 =   0
#    P14 =   0
#    P24 =   0
#    P34 =   0
#    P44 = 105 * (1-X*X)^2
#
#  Recursion:
#
#    if N < M:
#      P(N,M) = 0
#    if N = M:
#      P(N,M) = (2*M-1)!! * (1-X*X)^(M/2) where N!! means the product of
#      all the odd integers less than or equal to N.
#    if N = M+1:
#      P(N,M) = X*(2*M+1)*P(M,M)
#    if M+1 < N:
#      P(N,M) = ( X*(2*N-1)*P(N-1,M) - (N+M-1)*P(N-2,M) )/(N-M)
#
#  Restrictions:
#
#    -1 <= X <= 1
#     0 <= M <= N
#
#  Special values:
#
#    P(N,0)(X) = P(N)(X), that is, for M=0, the associated Legendre
#    polynomial of the first kind equals the Legendre polynomial of the
#    first kind.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
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
#    integer N_DATA.  The user sets N_DATA to 0 before the first call. 
#
#  Output:
#
#    integer N_DATA.   On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, integer M, real X, 
#    the arguments of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
      0.0000000000000000E+00, \
     -0.5000000000000000E+00, \
      0.0000000000000000E+00, \
      0.3750000000000000E+00, \
      0.0000000000000000E+00, \
     -0.8660254037844386E+00, \
     -0.1299038105676658E+01, \
     -0.3247595264191645E+00, \
      0.1353164693413185E+01, \
     -0.2800000000000000E+00, \
      0.1175755076535925E+01, \
      0.2880000000000000E+01, \
     -0.1410906091843111E+02, \
     -0.3955078125000000E+01, \
     -0.9997558593750000E+01, \
      0.8265311444100484E+02, \
      0.2024442836815152E+02, \
     -0.4237997531890869E+03, \
      0.1638320624828339E+04, \
     -0.2025687389227225E+05  ))

  m_vec = np.array ( ( \
    0, 0, 0, 0, \
    0, 1, 1, 1, \
    1, 0, 1, 2, \
    3, 2, 2, 3, \
    3, 4, 4, 5 ))

  n_vec = np.array ( ( \
    1,  2,  3,  4, \
    5,  1,  2,  3, \
    4,  3,  3,  3, \
    3,  4,  5,  6, \
    7,  8,  9, 10 ))

  x_vec = np.array ( ( \
     0.00E+00, \
     0.00E+00, \
     0.00E+00, \
     0.00E+00, \
     0.00E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.20E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00 ))
  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    m = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    m = m_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, m, x, f

def pm_polynomial_values_test ( ):

#*****************************************************************************80
#
## pm_polynomial_values_test() tests pm_polynomial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pm_polynomial_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pm_polynomial_values stores values of the associated Legendre function.' )
  print ( '' )
  print ( '      N       M            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, x, f = pm_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %6d  %12f  %24.16g' % ( n, m, x, f ) )

  return

def pn_pair_product ( p ):

#*****************************************************************************80
#
## pn_pair_product(): pair products for normalized Legendre polynomial Pn(n,x).
#
#  Discussion:
#
#    Let Pn(n,x) represent the normalized Legendre polynomial of degree n.  
#
#    To check orthonormality, we compute
#
#      Tij = Integral ( -1.0 <= X <= +1.0 ) Pn(i,x) * Pn(j,x) dx
#
#    We will estimate these integrals using Gauss-Legendre quadrature.
#
#    The computed table should be the identity matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polyonomial 
#    factors.  0 <= P.
#
#  Output:
#
#    real TABLE(1:P+1,1:P+1), the table of integrals.  
#
  import numpy as np

  table = np.zeros ( [ p + 1, p + 1 ] )
  xvec = np.zeros ( 1 )

  order = 2 * p + 1

  x_table, w_table = p_quadrature_rule ( order )

  for k in range ( 0, order ):

    x = x_table[k]
    xvec[0] = x

    h_table = pn_polynomial_value ( 1, p, xvec )

    for i in range ( 0, p + 1 ):
      for j in range ( 0, p + 1 ):
        table[i,j] = table[i,j] + w_table[k] * h_table[0,i] * h_table[0,j]

  return table

def pn_pair_product_test ( p ):

#*****************************************************************************80
#
## pn_pair_product_test() tests pn_pair_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polynomial 
#    factors.
#
  import platform

  print ( '' )
  print ( 'pn_pair_product_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pn_pair_product computes a pair product table for Pn(n,x):' )
  print ( '' )
  print ( '  Tij = integral ( -1 <= x <= +1 ) Pn(i,x) Pn(j,x) dx' )
  print ( '' )
  print ( '  The Pn(n,x) polynomials are orthonormal,' )
  print ( '  so T should be the identity matrix.' )
  print ( '' )
  print ( '  Maximum degree P = %d' % ( p ) )

  table = pn_pair_product ( p )

  r8mat_print ( p + 1, p + 1, table, '  Pair product table:' )

  return

def pn_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## pn_polynomial_coefficients(): coefficients of normalized Legendre Pn(n,x).
#
#  Discussion:
#
#    Pn(n,x) = P(n,x) * sqrt ( (2n+1)/2 )
#
#          1       x       x^2     x^3     x^4      x^5    x^6     x^7
#
#    0   0.707
#    1   0.000   1.224
#    2  -0.790   0.000   2.371
#    3   0.000  -2.806   0.000   4.677
#    4   0.795   0.000  -7.954   0.000   9.280
#    5   0.000   4.397   0.000 -20.520   0.000   18.468
#    6  -0.796   0.000  16.731   0.000 -50.193    0.000  36.808
#    7   0.000  -5.990   0.000  53.916   0.000 -118.616   0.000  73.429 
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
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
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#  Output:
#
#    real C(1:N+1,1:N+1), the coefficients of the normalized Legendre 
#    polynomials of degree 0 through N.  Each polynomial is stored as a row.
#
  import numpy as np

  c = np.zeros ( [ n + 1, n + 1 ] )
#
#  Compute P(n,x) coefficients.
#
  c[0,0] = 1.0

  if ( 0 < n ):
    c[1,1] = 1.0

  for i in range ( 2, n + 1 ):
    for j in range ( 0, i ):
      c[i,j] = (   - i + 1 ) * c[i-2,j] / ( i )
    for j in range ( 1, i + 1 ):
      c[i,j] = c[i,j] + ( i + i - 1 ) * c[i-1,j-1] / ( i )
#
#  Normalize them.
#
  for i in range ( 0, n + 1 ):
    t = np.sqrt ( ( 2 * i + 1 ) / 2.0 )
    for j in range ( 0, i + 1 ):
      c[i,j] = c[i,j] * t

  return c

def pn_polynomial_coefficients_test ( ):

#*****************************************************************************80
#
## pn_polynomial_coefficients_test() tests pn_polynomial_coefficients().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'pn_polynomial_coefficients_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pn_polynomial_coefficients: polynomial coefficients of Pn(n,x).' )

  c = pn_polynomial_coefficients ( n )
 
  for i in range ( 0, n + 1 ):
    print ( '' )
    print ( '  P(%d,x) = ' % ( i ) )
    print ( '' )
    for j in range ( i, -1, -1 ):
      if ( c[i,j] == 0.0 ):
        continue
      elif ( j == 0 ):
        print ( '  %g' % ( c[i,j] ) )
      elif ( j == 1 ):
        print ( '  %g * x' % ( c[i,j] ) )
      else:
        print ( '  %g * x^%d' % ( c[i,j], j ) )

  return

def pn_polynomial_value ( m, n, x ):

#*****************************************************************************80
#
## pn_polynomial_value() evaluates the normalized Legendre polynomials Pn(n,x).
#
#  Discussion:
#
#    The normalized Legendre polynomials are orthonormal under the inner product 
#    defined as integration from -1 to 1:
#
#      Integral ( -1 <= x <= +1 ) Pn(i,x) * Pn(j,x) dx = delta(i,j)
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    real X(M,1), the evaluation points.
#
#  Output:
#
#    real V(M,1:N+1), the values of the Legendre polynomials 
#    of order 0 through N,
#
  import numpy as np

  v = p_polynomial_value ( m, n, x );

  for j in range ( 0, n + 1 ):
    norm = np.sqrt ( 2.0 / ( 2 * j + 1 ) )
    for i in range ( 0, m ):
      v[i,j] = v[i,j] / norm
 
  return v

def pn_polynomial_value_test ( ):

#*****************************************************************************80
#
## pn_polynomial_value_test() tests pn_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2012
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 1
  xvec = np.zeros ( 1 )

  print ( '' )
  print ( 'pn_polynomial_value_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pn_polynomial_value evaluates the normalized Legendre polynomial Pn(n,x).' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X          Pn(N,X)                   Pn(N,X)                     Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx1 = pn_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    xvec[0] = x
    v = pn_polynomial_value ( m, n, xvec )
    fx2 = v[0,n]

    e = fx1 - fx2

    print ( '  %4d  %12g  %24.16g  %24.16g  %8g' % ( n, x, fx1, fx2, e ) )

  return

def pn_polynomial_values ( n_data ):

#*****************************************************************************80
#
## pn_polynomial_values(): selected values of the normalized Legendre polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call. 
#
#  Output:
#
#    integer N_DATA.   On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 22

  f_vec = np.array ( ( \
    0.7071067811865475, \
    0.3061862178478972, \
   -0.642337649721702, \
   -0.6284815141846855, \
    0.3345637065282053, \
    0.7967179601799685, \
    0.06189376866246124, \
   -0.766588850921089, \
   -0.4444760242953344, \
    0.5450094674858101, \
    0.7167706229835538, \
    0.0000000000000000, \
   -0.2759472322745781, \
   -0.5238320341483518, \
   -0.7155919752205163, \
   -0.823164625090267, \
   -0.8184875533567997, \
   -0.6734983296193094, \
   -0.360134523476992, \
    0.1496662954709581, \
    0.8839665576253438, \
    1.870828693386971 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3 ))

  x_vec = np.array ( ( \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.00E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.90E+00, \
     1.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def pn_polynomial_values_test ( ):

#*****************************************************************************80
#
## pn_polynomial_values_test() tests pn_polynomial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'pn_polynomial_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  pn_polynomial_values stores values of the normalized Legendre polynomials.' )
  print ( '' )
  print ( '      N            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = pn_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12g  %24.16g' % ( n, x, f ) )

  return

def p_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## p_polynomial_coefficients(): coefficients of Legendre polynomials P(n,x).
#
#  First terms:
#
#     1
#     0     1
#    -1/2   0      3/2
#     0    -3/2    0     5/2
#     3/8   0    -30/8   0     35/8
#     0    15/8    0   -70/8    0     63/8
#    -5/16  0    105/16  0   -315/16   0    231/16
#     0   -35/16   0   315/16   0   -693/16   0    429/16
#
#     1.00000
#     0.00000  1.00000
#    -0.50000  0.00000  1.50000
#     0.00000 -1.50000  0.00000  2.5000
#     0.37500  0.00000 -3.75000  0.00000  4.37500
#     0.00000  1.87500  0.00000 -8.75000  0.00000  7.87500
#    -0.31250  0.00000  6.56250  0.00000 -19.6875  0.00000  14.4375
#     0.00000 -2.1875   0.00000  19.6875  0.00000 -43.3215  0.00000  26.8125
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
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
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#  Output:
#
#    real C(1:N+1,1:N+1), the coefficients of the Legendre polynomials 
#    of degree 0 through N.  Each polynomial is stored as a row.
#
  import numpy as np

  c = np.zeros ( [ n + 1, n + 1 ] )

  c[0,0] = 1.0

  if ( n <= 0 ):
    return c

  c[1,1] = 1.0
 
  for i in range ( 2, n + 1 ):
    for j in range ( 0, i - 1 ):
      c[i,j] = (   - i + 1 ) * c[i-2,j] / ( i )
    for j in range ( 1, i + 1 ):
      c[i,j] = c[i,j] + ( i + i - 1 ) * c[i-1,j-1] / ( i )
 
  return c

def p_polynomial_coefficients_test ( ):

#*****************************************************************************80
#
## p_polynomial_coefficients_test() tests p_polynomial_coefficients().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10

  print ( '' )
  print ( 'p_polynomial_coefficients_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  p_polynomial_coefficients determines polynomial coefficients of P(n,x).' )

  c = p_polynomial_coefficients ( n )
 
  for i in range ( 0, n + 1 ):
    print ( '' )
    print ( '  P(%d,x) = ' % ( i ) )
    print ( '' )
    for j in range ( i, -1, -1 ):
      if ( c[i,j] == 0.0 ):
        continue
      elif ( j == 0 ):
        print ( '  %g' % ( c[i,j] ) )
      elif ( j == 1 ):
        print ( '  %g * x' % ( c[i,j] ) )
      else:
        print ( '  %g * x^%d' % ( c[i,j], j ) )

  return

def p_polynomial_plot_test ( ):

#*****************************************************************************80
#
## p_polynomial_plot_test() tests p_polynomial_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2024
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'legendre_polynomial_plot_test():' )
  print ( '  p_polynomial_plot() plots one or more Legendre functions.' )

  index = np.array ( [ 0, 1, 2, 3, 4, 5 ] )
  filename = 'p_polynomial_plot.png'

  p_polynomial_plot ( index, filename )

  return

def p_polynomial_plot ( index, filename ):

#*****************************************************************************80
#
## p_polynomial_plot() plots Legendre polynomials.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer INDEX(*), the orders of 1 or more Legendre polynomials
#    to be plotted together.
#
#    string FILENAME, the name into which the graphics information is
#    to be stored.
#
  import matplotlib.pyplot as plt
  import numpy as np

  m = 501
  x = np.linspace ( -1.0, +1.0, m )
  index_num = len ( index )

  plt.clf ( )
  plt.plot ( [-1.0,+1.0], [0.0,0.0], 'b-', linewidth = 1 )
  for n in index:
    y = p_polynomial_value ( m, n, x )
    plt.plot ( x, y[:,n], linewidth = 3 )
  plt.grid ( True )
  plt.xlabel ( '<--- X --->' )
  plt.ylabel ( '<--- P(n,x) --->' )
  plt.title ( 'Legendre functions P(n,x)' )
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )

  return

def p_polynomial_prime2 ( m, n, x ):

#*****************************************************************************80
#
## p_polynomial_prime2(): second derivative of Legendre polynomials P(n,x).
#
#  Discussion:
#
#    P(0,X) = 1
#    P(1,X) = X
#    P(N,X) = ( (2*N-1)*X*P(N-1,X)-(N-1)*P(N-2,X) ) / N
#
#    P'(0,X) = 0
#    P'(1,X) = 1
#    P'(N,X) = ( (2*N-1)*(P(N-1,X)+X*P'(N-1,X)-(N-1)*P'(N-2,X) ) / N
#
#    P"(0,X) = 0
#    P"(1,X) = 0
#    P"(N,X) = ( (2*N-1)*(2*P'(N-1,X)+X*P"(N-1,X)-(N-1)*P'(N-2,X) ) / N
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    real X(M,1), the evaluation points.
#
#  Output:
#
#    real VPP(M,N+1), the second derivatives of the
#    Legendre polynomials of order 0 through N at the point X.
#
  import numpy as np

  v = np.zeros ( [ m, n + 1 ] )
  vp = np.zeros ( [ m, n + 1 ] )
  vpp = np.zeros ( [ m, n + 1 ] )

  for i in range ( 0, m ):
    v[i,0] = 1.0
    vp[i,0] = 0.0
    vpp[i,0] = 0.0

  if ( n < 1 ):
    return vpp

  for i in range ( 0, m ):
    v[i,1] = x[i]
    vp[i,1] = 1.0
    vpp[i,1] = 0.0
 
  for j in range ( 2, n + 1 ):
 
    for i in range ( 0, m ):

      v[i,j] = ( ( 2 * j - 1 ) * x[i] * v[i,j-1]   \
               - (     j - 1 ) *        v[i,j-2] ) \
               / (     j     )
 
      vp[i,j] = ( ( 2 * j - 1 ) * ( v[i,j-1] + x[i] * vp[i,j-1] ) \
                - (     j - 1 ) *                     vp[i,j-2] ) \
                / (     j     )

      vpp[i,j] = ( ( 2 * j - 1 ) * ( 2.0 * vp[i,j-1] + x[i] * vpp[i,j-1] ) \
                 - (     j - 1 ) *                            vpp[i,j-2] ) \
                 / (     j     )
  
  return vpp

def p_polynomial_prime2_test ( ):

#*****************************************************************************80
#
## p_polynomial_prime2_test() tests p_polynomial_prime2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'p_polynomial_prime2_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  p_polynomial_prime2 evaluates the second derivative of' )
  print ( '  the Legendre polynomial P(N,X).' )
  print ( '' )
  print ( '                                      Computed' )
  print ( '     N        X                         P"(N,X)' )

  m = 11
  n = 5
  x = np.linspace ( -1.0, +1.0, m )
  vpp = p_polynomial_prime2 ( m, n, x )

  for i in range ( 0, m ):
    print ( '' )
    for j in range ( 0, n + 1 ):
      print ( '  %4d  %12g  %24g' % ( j, x[i], vpp[i,j] ) )

  return

def p_polynomial_prime ( m, n, x ):

#*****************************************************************************80
#
## p_polynomial_prime() evaluates the derivative of Legendre polynomials P(n,x).
#
#  Discussion:
#
#    P(0,X) = 1
#    P(1,X) = X
#    P(N,X) = ( (2*N-1)*X*P(N-1,X)-(N-1)*P(N-2,X) ) / N
#
#    P'(0,X) = 0
#    P'(1,X) = 1
#    P'(N,X) = ( (2*N-1)*(P(N-1,X)+X*P'(N-1,X)-(N-1)*P'(N-2,X) ) / N
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    real X(M,1), the evaluation points.
#
#  Output:
#
#    real VP(M,N+1), the values of the derivatives of the
#    Legendre polynomials of order 0 through N at the point X.
#
  import numpy as np

  v = np.zeros ( [ m, n + 1 ] )
  vp = np.zeros ( [ m, n + 1 ] )

  for i in range ( 0, m ):
    v[i,0] = 1.0
    vp[i,0] = 0.0

  if ( n < 1 ):
    return vp

  for i in range ( 0, m ):
    v[i,1] = x[i]
    vp[i,1] = 1.0
 
  for j in range ( 2, n + 1 ):
    for i in range ( 0, m ):
      v[i,j]  = ( ( 2 * j - 1 ) * x[i] * v[i,j-1]   \
                - (     j - 1 ) *        v[i,j-2] ) \
                / (     j     )
 
      vp[i,j] = ( ( 2 * j - 1 ) * ( v[i,j-1] + x[i] * vp[i,j-1] ) \
                - (     j - 1 ) *                     vp[i,j-2] ) \
                / (     j     )
 
  return vp

def p_polynomial_prime_test ( ):

#*****************************************************************************80
#
## p_polynomial_prime_test() tests p_polynomial_prime().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'p_polynomial_prime_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  p_polynomial_prime evaluates the derivative of' )
  print ( '  the Legendre polynomial P(N,X).' )
  print ( '' )
  print ( '                                      Computed' )
  print ( '     N        X                         P\'(N,X)' )

  m = 11
  n = 5
  x = np.linspace ( -1.0, +1.0, m )
  vp = p_polynomial_prime ( m, n, x )

  for i in range ( 0, m ):
    print ( '' )
    for j in range ( 0, n + 1 ):
      print ( '  %4d  %12g  %24g' % ( j, x[i], vp[i,j] ) )

  return

def p_polynomial_value ( m, n, x ):

#*****************************************************************************80
#
## p_polynomial_value() evaluates the Legendre polynomials P(n,x).
#
#  Discussion:
#
#    P(n,1) = 1.
#    P(n,-1) = (-1)^N.
#    | P(n,x) | <= 1 in [-1,1].
#
#    The N zeroes of P(n,x) are the abscissas used for Gauss-Legendre
#    quadrature of the integral of a function F(X) with weight function 1
#    over the interval [-1,1].
#
#    The Legendre polynomials are orthogonal under the inner product defined
#    as integration from -1 to 1:
#
#      Integral ( -1 <= X <= 1 ) P(I,X) * P(J,X) dX 
#        = 0 if I =/= J
#        = 2 / ( 2*I+1 ) if I = J.
#
#    Except for P(0,X), the integral of P(I,X) from -1 to 1 is 0.
#
#    A function F(X) defined on [-1,1] may be approximated by the series
#      C0*P(0,x) + C1*P(1,x) + ... + CN*P(n,x)
#    where
#      C(I) = (2*I+1)/(2) * Integral ( -1 <= X <= 1 ) F(X) P(I,x) dx.
#
#    The formula is:
#
#      P(n,x) = (1/2^N) * sum ( 0 <= M <= N/2 ) C(N,M) C(2N-2M,N) X^(N-2*M)
#
#  Differential equation:
#
#    (1-X*X) * P(n,x)'' - 2 * X * P(n,x)' + N * (N+1) = 0
#
#  First terms:
#
#    P( 0,x) =      1
#    P( 1,x) =      1 X
#    P( 2,x) = (    3 X^2 -       1)/2
#    P( 3,x) = (    5 X^3 -     3 X)/2
#    P( 4,x) = (   35 X^4 -    30 X^2 +     3)/8
#    P( 5,x) = (   63 X^5 -    70 X^3 +    15 X)/8
#    P( 6,x) = (  231 X^6 -   315 X^4 +   105 X^2 -     5)/16
#    P( 7,x) = (  429 X^7 -   693 X^5 +   315 X^3 -    35 X)/16
#    P( 8,x) = ( 6435 X^8 - 12012 X^6 +  6930 X^4 -  1260 X^2 +   35)/128
#    P( 9,x) = (12155 X^9 - 25740 X^7 + 18018 X^5 -  4620 X^3 +  315 X)/128
#    P(10,x) = (46189 X^10-109395 X^8 + 90090 X^6 - 30030 X^4 + 3465 X^2-63)/256
#
#  Recursion:
#
#    P(0,x) = 1
#    P(1,x) = x
#    P(n,x) = ( (2*n-1)*x*P(n-1,x)-(n-1)*P(n-2,x) ) / n
#
#    P'(0,x) = 0
#    P'(1,x) = 1
#    P'(N,x) = ( (2*N-1)*(P(N-1,x)+X*P'(N-1,x)-(N-1)*P'(N-2,x) ) / N
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz, Irene Stegun,
#    Handbook of Mathematical Functions,
#    National Bureau of Standards, 1964,
#    ISBN: 0-486-61272-4,
#    LC: QA47.A34.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996.
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    real X(M), the evaluation points.
#
#  Output:
#
#    real V(0:M-1,0:N), the values of the Legendre polynomials 
#    of order 0 through N at the points X.
#
  import numpy as np

  v = np.zeros ( [ m, n + 1 ] )

  for i in range ( 0, m ):
    v[i,0] = 1.0

  if ( n < 1 ):
    return v

  for i in range ( 0, m ):
    v[i,1] = x[i]

  for j in range ( 2, n + 1 ):

    for i in range ( 0, m ):
 
      v[i,j] = ( ( 2 * j - 1 ) * x[i] * v[i,j-1]   \
              -  (     j - 1 ) *        v[i,j-2] ) \
              /  (     j     )

  return v

def p_polynomial_value_test ( ):

#*****************************************************************************80
#
## p_polynomial_value_test() tests p_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 1
  xvec = np.zeros ( m )

  print ( '' )
  print ( 'p_polynomial_value_test:' )
  print ( '  Python version: ' + platform.python_version ( ) )
  print ( '  p_polynomial_value evaluates the Legendre polynomial P(n,x).' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X           P(N,X)                    P(N,X)                     Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx1 = p_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    xvec[0] = x
    v = p_polynomial_value ( m, n, xvec )
    fx2 = v[0,n]

    e = fx1 - fx2

    print ( '  %4d  %12g  %24g  %24g  %8g' % ( n, x, fx1, fx2, e ) )

  return

def p_polynomial_values ( n_data ):

#*****************************************************************************80
#
## p_polynomial_values(): selected values of the Legendre polynomials.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      LegendreP [ n, x ]
#
#  Differential equation:
#
#    (1-X*X) * P(N,X)'' - 2 * X * P(N,X)' + N * (N+1) = 0
#
#  First terms:
#
#    P( 0,X) =       1
#    P( 1,X) =       1 X
#    P( 2,X) =  (    3 X^2 -       1)/2
#    P( 3,X) =  (    5 X^3 -     3 X)/2
#    P( 4,X) =  (   35 X^4 -    30 X^2 +     3)/8
#    P( 5,X) =  (   63 X^5 -    70 X^3 +    15 X)/8
#    P( 6,X) =  (  231 X^6 -   315 X^4 +   105 X^2 -     5)/16
#    P( 7,X) =  (  429 X^7 -   693 X^5 +   315 X^3 -    35 X)/16
#    P( 8,X) =  ( 6435 X^8 - 12012 X^6 +  6930 X^4 -  1260 X^2 +   35)/128
#    P( 9,X) =  (12155 X^9 - 25740 X^7 + 18018 X^5 -  4620 X^3 +  315 X)/128
#    P(10,X) =  (46189 X^10-109395 X^8 + 90090 X^6 - 30030 X^4 + 3465 X^2-63 ) /256
#
#  Recursion:
#
#    P(0,X) = 1
#    P(1,X) = X
#    P(N,X) = ( (2*N-1)*X*P(N-1,X)-(N-1)*P(N-2,X) ) / N
#
#    P'(0,X) = 0
#    P'(1,X) = 1
#    P'(N,X) = ( (2*N-1)*(P(N-1,X)+X*P'(N-1,X)-(N-1)*P'(N-2,X) ) / N
#
#  Formula:
#
#    P(N,X) = (1/2^N) * sum ( 0 <= M <= N/2 ) C(N,M) C(2N-2M,N) X^(N-2*M)
#
#  Orthogonality:
#
#    Integral ( -1 <= X <= 1 ) P(I,X) * P(J,X) dX
#      = 0 if I =/= J
#      = 2 / ( 2*I+1 ) if I = J.
#
#  Approximation:
#
#    A function F(X) defined on [-1,1] may be approximated by the series
#
#      C0*P(0,X) + C1*P(1,X) + \ + CN*P(N,X)
#
#    where
#
#      C(I) = (2*I+1)/(2) * Integral ( -1 <= X <= 1 ) F(X) P(I,X) dx.
#
#  Special values:
#
#    P(N,1) = 1.
#    P(N,-1) = (-1)^N.
#    | P(N,X) | <= 1 in [-1,1].
#
#    P(N,0,X) = P(N,X), that is, for M=0, the associated Legendre
#    function of the first kind and order N equals the Legendre polynomial
#    of the first kind and order N.
#
#    The N zeroes of P(N,X) are the abscissas used for Gauss-Legendre
#    quadrature of the integral of a function F(X) with weight function 1
#    over the interval [-1,1].
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
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
#    integer N_DATA.  The user sets N_DATA to 0 before the first call. 
#
#  Output:
#
#    integer N_DATA.   On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 22

  f_vec = np.array ( ( \
      0.1000000000000000E+01, \
      0.2500000000000000E+00, \
     -0.4062500000000000E+00, \
     -0.3359375000000000E+00, \
      0.1577148437500000E+00, \
      0.3397216796875000E+00, \
      0.2427673339843750E-01, \
     -0.2799186706542969E+00, \
     -0.1524540185928345E+00, \
      0.1768244206905365E+00, \
      0.2212002165615559E+00, \
      0.0000000000000000E+00, \
     -0.1475000000000000E+00, \
     -0.2800000000000000E+00, \
     -0.3825000000000000E+00, \
     -0.4400000000000000E+00, \
     -0.4375000000000000E+00, \
     -0.3600000000000000E+00, \
     -0.1925000000000000E+00, \
      0.8000000000000000E-01, \
      0.4725000000000000E+00, \
      0.1000000000000000E+01 ))

  n_vec = np.array ( ( \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3,  3,  3, \
     3 ))

  x_vec = np.array ( ( \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.25E+00, \
     0.00E+00, \
     0.10E+00, \
     0.20E+00, \
     0.30E+00, \
     0.40E+00, \
     0.50E+00, \
     0.60E+00, \
     0.70E+00, \
     0.80E+00, \
     0.90E+00, \
     1.00E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    f = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, f

def p_polynomial_values_test ( ):

#*****************************************************************************80
#
## p_polynomial_values_test() tests p_polynomial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'p_polynomial_values_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  p_polynomial_values stores values of the Legendre polynomials.' )
  print ( '' )
  print ( '      N            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = p_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, f ) )

  return

def p_polynomial_zeros ( nt ):

#*****************************************************************************80
#
## p_polynomial_zeros(): zeros of Legendre function P(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NT, the order of the rule.
#
#  Output:
#
#    real T(NT), the zeros.
#
  import numpy as np

  a = np.zeros ( nt )

  b = np.zeros ( nt )

  for i in range ( 0, nt ):
    ip1 = i + 1
    b[i] = ip1 / np.sqrt ( 4 * ip1 * ip1 - 1 )

  c = np.zeros ( nt )
  c[0] = np.sqrt ( 2.0 )

  t, w = imtqlx ( nt, a, b, c )

  return t

def p_polynomial_zeros_test ( ):

#*****************************************************************************80
#
## p_polynomial_zeros_test() tests p_polynomial_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'p_polynomial_zeros_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  p_polynomial_zeros computes the zeros of P(n,x)' )
  print ( '  Check by calling p_polynomial_value there.' )

  for degree in range ( 1, 6 ):

    z = p_polynomial_zeros ( degree )
    title = '  Computed zeros for P(%d,x)' % ( degree )
    r8vec_print ( degree, z, title )

    lz = p_polynomial_value ( degree, degree, z )
    title = '  Evaluate P(%d,z)' % ( degree )
    lzvec = np.zeros ( degree )
    for i in range ( 0, degree ):
      lzvec[i] = lz[i,degree]
    r8vec_print ( degree, lzvec, title )

  return

def p_power_product ( p, e ):

#*****************************************************************************80
#
## p_power_product(): power products for Legendre polynomial P(n,x).
#
#  Discussion:
#
#    Let P(n,x) represent the Legendre polynomial of degree i.  
#
#    For polynomial chaos applications, it is of interest to know the
#    value of the integrals of products of powers of X with every possible pair
#    of basis functions.  That is, we'd like to form
#
#      Tij = Integral ( -1 <= X <= +1 ) X^E * P(i,x) * P(j,x) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polyonomial factors.
#    0 <= P.
#
#    integer E, the exponent of X in the integrand.
#    0 <= E.
#
#  Output:
#
#    real TABLE(P+1,P+1), the table of integrals.
#
  import numpy as np

  table = np.zeros ( [ p + 1, p + 1 ] )
  xvec = np.zeros ( 1 )

  order = p + 1 + ( ( e + 1 ) // 2 )

  x_table, w_table = p_quadrature_rule ( order )

  for k in range ( 0, order ):

    x = x_table[k]
    xvec[0] = x
    l_table = p_polynomial_value ( 1, p, xvec )
#
#  The following formula is an outer product in L_TABLE.
#
    if ( e == 0 ):
      for i in range ( 0, p + 1 ):
        for j in range ( 0, p + 1 ):
          table[i,j] = table[i,j] + w_table[k] * l_table[0,i] * l_table[0,j]
    else:
      for i in range ( 0, p + 1 ):
        for j in range ( 0, p + 1 ):
          table[i,j] = table[i,j] + w_table[k] * x ** e * l_table[0,i] * l_table[0,j]

  return table

def p_power_product_test ( p, e ):

#*****************************************************************************80
#
## p_power_product_test() tests p_power_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer P, the maximum degree of the polynomial 
#    factors.
#
#    integer E, the exponent of X.
#
  import platform

  print ( '' )
  print ( 'p_power_product_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  p_power_product computes a power product table for P(n,x):' )
  print ( '' )
  print ( '  Tij = integral ( -1 <= x <= +1 ) x^e P(i,x) P(j,x) dx' )

  print ( '' )
  print ( '  Maximum degree P = %d' % ( p ) )
  print ( '  Exponent of X, E = %d' % ( e ) )

  table = p_power_product ( p, e )

  r8mat_print ( p + 1, p + 1, table, '  Power product table:' )

  return

def p_quadrature_rule ( nt ):

#*****************************************************************************80
#
## p_quadrature_rule(): quadrature for Legendre function P(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NT, the order of the rule.
#
#  Output:
#
#    real T(NT), W(NT), the points and weights
#    of the rule.
#
  import numpy as np

  a = np.zeros ( nt )

  b = np.zeros ( nt )

  for i in range ( 0, nt ):
    ip1 = i + 1
    b[i] = ip1 / np.sqrt ( 4 * ip1 * ip1 - 1 )

  c = np.zeros ( nt )
  c[0] = np.sqrt ( 2.0 )

  t, w = imtqlx ( nt, a, b, c )

  for i in range ( 0, nt ):
    w[i] = w[i] ** 2

  return t, w

def p_quadrature_rule_test ( ):

#*****************************************************************************80
#
## p_quadrature_rule_test() tests p_quadrature_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'p_quadrature_rule_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  p_quadrature_rule computes the quadrature rule' )
  print ( '  associated with P(n,x)' )

  n = 5
  x, w = p_quadrature_rule ( n )

  r8vec2_print ( n, x, w,  '      X            W' )

  print ( '' )
  print ( '  Use the quadrature rule to estimate:' )
  print ( '' )
  print ( '    Q = Integral ( -1 <= X < +1 ) X^E dx' )
  print ( '' )
  print ( '   E       Q_Estimate      Q_Exact' )
  print ( '' )

  for e in range ( 0, 2 * n ):
    if ( e == 0 ):
      f = np.ones ( n )
    else:
      f = x ** e
    q = np.dot ( w, f )
    q_exact = p_integral ( e )
    print ( '  %2d  %14g  %14g' % ( e, q, q_exact ) )

  return

def r8mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8mat_print() prints an R8MAT.
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
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8mat_print_some() prints out a portion of an R8MAT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
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

def r8_sign_test ( ):

#*****************************************************************************80
#
## r8_sign_test() tests r8_sign().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
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
  print ( 'r8_sign_test' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_sign returns the sign of an R8.' )
  print ( '' )
  print ( '     R8     r8_sign(R8)' )
  print ( '' )

  for test in range ( 0, test_num ):
    r8 = r8_test[test]
    s = r8_sign ( r8 )
    print ( '  %8.4f  %8.0f' % ( r8, s ) )

  return

def r8vec2_print ( n, a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 June 2015
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
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

  return

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

  return None

if ( __name__ == '__main__' ):
  timestamp ( )
  legendre_polynomial_test ( )
  timestamp ( )

