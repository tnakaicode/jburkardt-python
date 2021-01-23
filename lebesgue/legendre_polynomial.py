#! /usr/bin/env python3
#
def imtqlx ( n, d, e, z ):

#*****************************************************************************80
#
## IMTQLX diagonalizes a symmetric tridiagonal matrix.
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Input, real D(N), the diagonal entries of the matrix.
#
#    Input, real E(N), the subdiagonal entries of the
#    matrix, in entries E(1) through E(N-1). 
#
#    Input, real Z(N), a vector to be operated on.
#
#    Output, real LAM(N), the diagonal entries of the diagonalized matrix.
#
#    Output, real QTZ(N), the value of Q' * Z, where Q is the matrix that 
#    diagonalizes the input symmetric tridiagonal matrix.
#
  import numpy as np
  from sys import exit

  lam = np.zeros ( n )
  for i in range ( 0, n ):
    lam[i] = d[i]

  qtz = np.zeros ( n )
  for i in range ( 0, n ):
    qtz[i] = z[i]

  if ( n == 1 ):
    return lam, qtz

  itn = 30

  prec = r8_epsilon ( )

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
        exit ( 'IMTQLX - Fatal error!' )

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
## IMTQLX_TEST tests IMTQLX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'IMTQLX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  IMTQLX takes a symmetric tridiagonal matrix A' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'IMTQLX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def legendre_polynomial_test ( ):

#*****************************************************************************80
#
## LEGENDRE_POLYNOMIAL_TEST tests the LEGENDRE_POLYNOMIAL library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'LEGENDRE_POLYNOMIAL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the LEGENDRE_POLYNOMIAL library.' )

  imtqlx_test ( )

  p = 5
  b = 0.0
  p_exponential_product_test ( p, b )

  p = 5
  b = 1.0
  p_exponential_product_test ( p, b )

  p_integral_test ( )

  p_polynomial_coefficients_test ( )
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

  r8_epsilon_test ( )
  r8_factorial_test ( )
  r8_sign_test ( )

  r8mat_print_test ( )
  r8mat_print_some_test ( )

  r8vec_print_test ( )

  r8vec2_print_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'LEGENDRE_POLYNOMIAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p_exponential_product ( p, b ):

#*****************************************************************************80
#
## P_EXPONENTIAL_PRODUCT: exponential products for P(n,x).
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer P, the maximum degree of the polyonomial factors.
#    0 <= P.
#
#    Input, real B, the coefficient of X in the exponential factor.
#
#    Output, real TABLE(P+1,P+1), the table of integrals.
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
## P_EXPONENTIAL_PRODUCT_TEST tests P_EXPONENTIAL_PRODUCT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer P, the maximum degree of the polynomial 
#    factors.
#
#    Input, real B, the coefficient of X in the exponential factor.
#
  import platform

  print ( '' )
  print ( 'P_EXPONENTIAL_PRODUCT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P_EXPONENTIAL_PRODUCT computes an exponential product table for P(n,x):' )
  print ( '' )
  print ( '  Tij = integral ( -1 <= x <= +1 ) exp(b*x) P(i,x) P(j,x) dx' )

  print ( '' )
  print ( '  Maximum degree P = %d' % ( p ) )
  print ( '  Exponential argument coefficient B = %g' % ( b ) )

  table = p_exponential_product ( p, b )

  r8mat_print ( p + 1, p + 1, table, '  Exponential product table:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'P_EXPONENTIAL_PRODUCT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p_integral ( n ):

#*****************************************************************************80
#
## P_INTEGRAL evaluates a monomial integral associated with P(n,x).
#
#  Discussion:
#
#    The integral:
#
#      integral ( -1 <= x < +1 ) x^n dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the exponent.
#    0 <= N.
#
#    Output, real VALUE, the value of the integral.
#
  if ( ( n % 2 ) == 1 ):
    value = 0.0
  else:
    value = 2.0 / ( n + 1 )

  return value

def p_integral_test ( ):

#*****************************************************************************80
#
## P_INTEGRAL_TEST tests P_INTEGRAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'P_INTEGRAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P_INTEGRAL returns the integral of P(n,x) over [-1,+1].' )
  print ( '' )
  print ( '     N                  Integral' )
  print ( '' )

  for n in range ( 0, 11 ):

    value = p_integral ( n )

    print ( '  %4d  %24.16g' % ( n, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P_INTEGRAL_TEST' )
  print ( '  Normal end of execution.' )
  return

def pmn_polynomial_value ( mm, n, m, x ):

#*****************************************************************************80
#
## PMN_POLYNOMIAL_VALUE: normalized Legendre polynomial Pmn(n,m,x).
#
#  Discussion:
#
#    The unnormalized associated Legendre functions P_N^M(X) have
#    the property that
#
#      Integral ( -1 <= X <= 1 ) ( P_N^M(X) )^2 dX 
#      = 2 * ( N + M )! / ( ( 2 * N + 1 ) * ( N - M )! )
#
#    By dividing the function by the square root of this term,
#    the normalized associated Legendre functions have norm 1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
#  Parameters:
#
#    Input, integer MM, the number of evaluation points.
#
#    Input, integer N, the maximum first index of the Legendre
#    function, which must be at least 0.
#
#    Input, integer M, the second index of the Legendre function,
#    which must be at least 0, and no greater than N.
#
#    Input, real X(MM,1), the evaluation points.
#
#    Output, real CX(MM,N+1), the function values.
#
  import numpy as np
  from sys import exit

  if ( m < 0 ):
    print ( '' )
    print ( 'PMN_POLYNOMIAL_VALUE - Fatal error!' )
    print ( '  Input value of M is %d' % ( m ) )
    print ( '  but M must be nonnegative.' )
    exit ( 'PMN_POLYNOMIAL_VALUE - Fatal error!' )
 
  if ( n < m ):
    print ( '' )
    print ( 'PMN_POLYNOMIAL_VALUE - Fatal error!' )
    print ( '  Input value of M = %d' % ( m ) )
    print ( '  Input value of N = %d' % ( n ) )
    print ( '  but M must be less than or equal to N.' )
    exit ( 'PMN_POLYNOMIAL_VALUE - Fatal error!' )

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
    factor = np.sqrt ( ( ( 2 * j + 1 ) * r8_factorial ( j - m ) ) \
      / ( 2.0 * r8_factorial ( j + m ) ) )
    for i in range ( 0, mm ):
      cx[i,j] = cx[i,j] * factor

  return cx

def pmn_polynomial_value_test ( ):

#*****************************************************************************80
#
## PMN_POLYNOMIAL_VALUE_TEST tests PMN_POLYNOMIAL_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'PMN_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PMN_POLYNOMIAL_VALUE evaluates the Legendre polynomial Pmn(n,m,x).' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'PMN_POLYNOMIAL_VALUE_TEST' )
  print ( '  Normal end of execution.' )
  return

def pmn_polynomial_values ( n_data ):

#*****************************************************************************80
#
## PMN_POLYNOMIAL_VALUES: selected values of associated Legendre functions.
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, integer M, real X, 
#    the arguments of the function.
#
#    Output, real F, the value of the function.
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
## PMN_POLYNOMIAL_VALUES_TEST demonstrates PMN_POLYNOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'PMN_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PMN_POLYNOMIAL_VALUES stores values of the ' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'PMN_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def pmns_polynomial_value ( mm, n, m, x ):

#*****************************************************************************80
#
## PMNS_POLYNOMIAL_VALUE: sphere_normalized Legendre polynomial Pmn(n,m,x).
#
#  Discussion:
#
#    The unnormalized associated Legendre functions P_N^M(X) have
#    the property that
#
#      Integral ( -1 <= X <= 1 ) ( P_N^M(X) )^2 dX 
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
#    This code is distributed under the GNU LGPL license. 
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
#  Parameters:
#
#    Input, integer MM, the number of evaluation points.
#
#    Input, integer N, the maximum first index of the Legendre
#    function, which must be at least 0.
#
#    Input, integer M, the second index of the Legendre function,
#    which must be at least 0, and no greater than N.
#
#    Input, real X(MM,1), the evaluation points.
#
#    Output, real CX(MM,N+1), the function values.
#
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
    factor = np.sqrt ( ( ( 2 * j + 1 ) * r8_factorial ( j - m ) ) \
      / ( 4.0 * np.pi * r8_factorial ( j + m ) ) )
    for i in range ( 0, mm ):
      cx[i,j] = cx[i,j] * factor

  return cx

def pmns_polynomial_value_test ( ):

#*****************************************************************************80
#
## PMNS_POLYNOMIAL_VALUE_TEST tests PMNS_POLYNOMIAL_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'PMNS_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PMNS_POLYNOMIAL_VALUE evaluates the Legendre polynomial Pmns(n,m,x).' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'PMNS_POLYNOMIAL_VALUE_TEST' )
  print ( '  Normal end of execution.' )
  return

def pmns_polynomial_values ( n_data ):

#*****************************************************************************80
#
## PMNS_POLYNOMIAL_VALUES: selected values of the associated Legendre polynomial normalized for sphere.
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, integer M, real X, 
#    the arguments of the function.
#
#    Output, real F, the value of the function.
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
## PMNS_POLYNOMIAL_VALUES_TEST demonstrates PMNS_POLYNOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'PMNS_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PMNS_POLYNOMIAL_VALUES stores values of the ' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'PMNS_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def pm_polynomial_value ( mm, n, m, x ):

#*****************************************************************************80
#
## PM_POLYNOMIAL_VALUE evaluates the Legendre polynomials Pm(n,m,x).
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
#    This code is distributed under the GNU LGPL license. 
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
#  Parameters:
#
#    Input, integer MM, the number of evaluation points.
#
#    Input, integer N, the maximum first index of the Legendre
#    function, which must be at least 0.
#
#    Input, integer M, the second index of the Legendre function,
#    which must be at least 0, and no greater than N.
#
#    Input, real X(MM), the point at which the function is to be
#    evaluated.
#
#    Output, real CX(MM,N+1), the function values.
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
## PM_POLYNOMIAL_VALUE_TEST tests PM_POLYNOMIAL_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'PM_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PM_POLYNOMIAL_VALUE evaluates the Legendre polynomial Pm(n,m,x).' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'PM_POLYNOMIAL_VALUE_TEST' )
  print ( '  Normal end of execution.' )
  return

def pm_polynomial_values ( n_data ):

#*****************************************************************************80
#
## PM_POLYNOMIAL_VALUES: selected values of associated Legendre functions.
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, integer M, real X, 
#    the arguments of the function.
#
#    Output, real F, the value of the function.
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
## PM_POLYNOMIAL_VALUES_TEST demonstrates the use of PM_POLYNOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'PM_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PM_POLYNOMIAL_VALUES stores values of the associated Legendre function.' )
  print ( '' )
  print ( '      N       M            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, m, x, f = pm_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %6d  %12f  %24.16g' % ( n, m, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PM_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def pn_pair_product ( p ):

#*****************************************************************************80
#
## PN_PAIR_PRODUCT: pair products for normalized Legendre polynomial Pn(n,x).
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer P, the maximum degree of the polyonomial 
#    factors.  0 <= P.
#
#    Output, real TABLE(1:P+1,1:P+1), the table of integrals.  
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
## PN_PAIR_PRODUCT_TEST tests PN_PAIR_PRODUCT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer P, the maximum degree of the polynomial 
#    factors.
#
  import platform

  print ( '' )
  print ( 'PN_PAIR_PRODUCT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PN_PAIR_PRODUCT computes a pair product table for Pn(n,x):' )
  print ( '' )
  print ( '  Tij = integral ( -1 <= x <= +1 ) Pn(i,x) Pn(j,x) dx' )
  print ( '' )
  print ( '  The Pn(n,x) polynomials are orthonormal,' )
  print ( '  so T should be the identity matrix.' )
  print ( '' )
  print ( '  Maximum degree P = %d' % ( p ) )

  table = pn_pair_product ( p )

  r8mat_print ( p + 1, p + 1, table, '  Pair product table:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'PN_PAIR_PRODUCT_TEST' )
  print ( '  Normal end of execution.' )
  return

def pn_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## PN_POLYNOMIAL_COEFFICIENTS: coefficients of normalized Legendre Pn(n,x).
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    Output, real C(1:N+1,1:N+1), the coefficients of the normalized Legendre 
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
## PN_POLYNOMIAL_COEFFICIENTS_TEST tests PN_POLYNOMIAL_COEFFICIENTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'PN_POLYNOMIAL_COEFFICIENTS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PN_POLYNOMIAL_COEFFICIENTS: polynomial coefficients of Pn(n,x).' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'PN_POLYNOMIAL_COEFFICIENTS_TEST' )
  print ( '  Normal end of execution.' )
  return

def pn_polynomial_value ( m, n, x ):

#*****************************************************************************80
#
## PN_POLYNOMIAL_VALUE evaluates the normalized Legendre polynomials Pn(n,x).
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
#    This code is distributed under the GNU LGPL license. 
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
#  Parameters:
#
#    Input, integer M, the number of evaluation points.
#
#    Input, integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    Input, real X(M,1), the evaluation points.
#
#    Output, real V(M,1:N+1), the values of the Legendre polynomials 
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
## PN_POLYNOMIAL_VALUE_TEST tests PN_POLYNOMIAL_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'PN_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PN_POLYNOMIAL_VALUE evaluates the normalized Legendre polynomial Pn(n,x).' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'PN_POLYNOMIAL_VALUE_TEST' )
  print ( '  Normal end of execution.' )
  return

def pn_polynomial_values ( n_data ):

#*****************************************************************************80
#
## PN_POLYNOMIAL_VALUES: selected values of the normalized Legendre polynomials.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, the order of the function.
#
#    Output, real X, the point where the function is evaluated.
#
#    Output, real F, the value of the function.
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
## PN_POLYNOMIAL_VALUES_TEST tests PN_POLYNOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'PN_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PN_POLYNOMIAL_VALUES stores values of the normalized Legendre polynomials.' )
  print ( '' )
  print ( '      N            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = pn_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12g  %24.16g' % ( n, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PN_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## P_POLYNOMIAL_COEFFICIENTS: coefficients of Legendre polynomials P(n,x).
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    Output, real C(1:N+1,1:N+1), the coefficients of the Legendre polynomials 
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
## P_POLYNOMIAL_COEFFICIENTS_TEST tests P_POLYNOMIAL_COEFFICIENTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'P_POLYNOMIAL_COEFFICIENTS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P_POLYNOMIAL_COEFFICIENTS determines polynomial coefficients of P(n,x).' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'P_POLYNOMIAL_COEFFICIENTS_TEST' )
  print ( '  Normal end of execution.' )
  return

def p_polynomial_prime2 ( m, n, x ):

#*****************************************************************************80
#
## P_POLYNOMIAL_PRIME2: second derivative of Legendre polynomials P(n,x).
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
#    This code is distributed under the GNU LGPL license. 
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
#  Parameters:
#
#    Input, integer M, the number of evaluation points.
#
#    Input, integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    Input, real X(M,1), the evaluation points.
#
#    Output, real VPP(M,N+1), the second derivatives of the
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
## P_POLYNOMIAL_PRIME2_TEST tests P_POLYNOMIAL_PRIME2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'P_POLYNOMIAL_PRIME2_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P_POLYNOMIAL_PRIME2 evaluates the second derivative of' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'P_POLYNOMIAL_PRIME2_TEST' )
  print ( '  Normal end of execution.' )
  return

def p_polynomial_prime ( m, n, x ):

#*****************************************************************************80
#
## P_POLYNOMIAL_PRIME evaluates the derivative of Legendre polynomials P(n,x).
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
#    This code is distributed under the GNU LGPL license. 
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
#  Parameters:
#
#    Input, integer M, the number of evaluation points.
#
#    Input, integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    Input, real X(M,1), the evaluation points.
#
#    Output, real VP(M,N+1), the values of the derivatives of the
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
## P_POLYNOMIAL_PRIME_TEST tests P_POLYNOMIAL_PRIME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'P_POLYNOMIAL_PRIME_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P_POLYNOMIAL_PRIME evaluates the derivative of' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'P_POLYNOMIAL_PRIME_TEST' )
  print ( '  Normal end of execution.' )
  return

def p_polynomial_value ( m, n, x ):

#*****************************************************************************80
#
## P_POLYNOMIAL_VALUE evaluates the Legendre polynomials P(n,x).
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
#    This code is distributed under the GNU LGPL license. 
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
#  Parameters:
#
#    Input, integer M, the number of evaluation points.
#
#    Input, integer N, the highest order polynomial to evaluate.
#    Note that polynomials 0 through N will be evaluated.
#
#    Input, real X(M), the evaluation points.
#
#    Output, real V(0:M-1,0:N), the values of the Legendre polynomials 
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
## P_POLYNOMIAL_VALUE_TEST tests P_POLYNOMIAL_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'P_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P_POLYNOMIAL_VALUE evaluates the Legendre polynomial P(n,x).' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'P_POLYNOMIAL_VALUE_TEST' )
  print ( '  Normal end of execution.' )
  return

def p_polynomial_values ( n_data ):

#*****************************************************************************80
#
## P_POLYNOMIAL_VALUES: selected values of the Legendre polynomials.
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, the order of the function.
#
#    Output, real X, the point where the function is evaluated.
#
#    Output, real F, the value of the function.
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
## P_POLYNOMIAL_VALUES_TEST tests P_POLYNOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'P_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P_POLYNOMIAL_VALUES stores values of the Legendre polynomials.' )
  print ( '' )
  print ( '      N            X            F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, f = p_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'P_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def p_polynomial_zeros ( nt ):

#*****************************************************************************80
#
## P_POLYNOMIAL_ZEROS: zeros of Legendre function P(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NT, the order of the rule.
#
#    Output, real T(NT), the zeros.
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
## P_POLYNOMIAL_ZEROS_TEST tests P_POLYNOMIAL_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'P_POLYNOMIAL_ZEROS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P_POLYNOMIAL_ZEROS computes the zeros of P(n,x)' )
  print ( '  Check by calling P_POLYNOMIAL_VALUE there.' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'P_POLYNOMIAL_ZEROS_TEST' )
  print ( '  Normal end of execution.' )
  return

def p_power_product ( p, e ):

#*****************************************************************************80
#
#% P_POWER_PRODUCT: power products for Legendre polynomial P(n,x).
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer P, the maximum degree of the polyonomial factors.
#    0 <= P.
#
#    Input, integer E, the exponent of X in the integrand.
#    0 <= E.
#
#    Output, real TABLE(P+1,P+1), the table of integrals.
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
## P_POWER_PRODUCT_TEST tests P_POWER_PRODUCT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer P, the maximum degree of the polynomial 
#    factors.
#
#    Input, integer E, the exponent of X.
#
  import platform

  print ( '' )
  print ( 'P_POWER_PRODUCT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P_POWER_PRODUCT computes a power product table for P(n,x):' )
  print ( '' )
  print ( '  Tij = integral ( -1 <= x <= +1 ) x^e P(i,x) P(j,x) dx' )

  print ( '' )
  print ( '  Maximum degree P = %d' % ( p ) )
  print ( '  Exponent of X, E = %d' % ( e ) )

  table = p_power_product ( p, e )

  r8mat_print ( p + 1, p + 1, table, '  Power product table:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'P_POWER_PRODUCT_TEST' )
  print ( '  Normal end of execution.' )
  return

def p_quadrature_rule ( nt ):

#*****************************************************************************80
#
## P_QUADRATURE_RULE: quadrature for Legendre function P(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NT, the order of the rule.
#
#    Output, real T(NT), W(NT), the points and weights
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
## P_QUADRATURE_RULE_TEST tests P_QUADRATURE_RULE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'P_QUADRATURE_RULE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  P_QUADRATURE_RULE computes the quadrature rule' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'P_QUADRATURE_RULE_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_epsilon ( ):

#*****************************************************************************80
#
## R8_EPSILON returns the R8 roundoff unit.
#
#  Discussion:
#
#    The roundoff unit is a number R which is a power of 2 with the 
#    property that, to the precision of the computer's arithmetic,
#      1 < 1 + R
#    but 
#      1 = ( 1 + R / 2 )
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
#    Output, real VALUE, the roundoff unit.
#
  value = 2.220446049250313E-016

  return value

def r8_epsilon_test ( ):

#*****************************************************************************80
#
## R8_EPSILON_TEST tests R8_EPSILON.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2012
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_EPSILON_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_EPSILON produces the R8 roundoff unit.' )
  print ( '' )

  r = r8_epsilon ( )
  print ( '  R = R8_EPSILON()         = %e' % ( r ) )

  s = ( 1.0 + r ) - 1.0
  print ( '  ( 1 + R ) - 1            = %e' % ( s ) )

  s = ( 1.0 + ( r / 2.0 ) ) - 1.0
  print ( '  ( 1 + (R/2) ) - 1        = %e' % ( s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_EPSILON_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_factorial ( n ):

#*****************************************************************************80
#
## R8_FACTORIAL returns N factorial.
#
#  Discussion:
#
#    factorial ( N ) = Product ( 1 <= I <= N ) I
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
#    Input, integer N, the argument of the function.
#    0 <= N.
#
#    Output, real VALUE, the factorial of N.
#
  from sys import exit

  if ( n < 0 ):
    print ( '' )
    print ( 'R8_FACTORIAL - Fatal error!' )
    print ( '  N < 0.' )
    exit ( 'R8_FACTORIAL - Fatal error!' )

  value = 1.0

  for i in range ( 2, n + 1 ):
    value = value * i

  return value

def r8_factorial_test ( ):

#*****************************************************************************80
#
## R8_FACTORIAL_TEST tests R8_FACTORIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_FACTORIAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_FACTORIAL evaluates the factorial function.' )
  print ( '' )
  print ( '      N                     Exact                  Computed' )

  n_data = 0

  while ( True ):

    n_data, n, f1 = r8_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_factorial ( n )

    print ( '  %4d  %24.16g  %24.16g' % ( n, f1, f2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_FACTORIAL_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_factorial_values ( n_data ):

#*****************************************************************************80
#
## R8_FACTORIAL_VALUES returns values of the real factorial function.
#
#  Discussion:
#
#    0! = 1
#    I! = Product ( 1 <= J <= I ) J
#
#    Although the factorial is an integer valued function, it quickly
#    becomes too large for an integer to hold.  This routine still accepts
#    an integer as the input argument, but returns the function value
#    as a real number.
#
#    In Mathematica, the function can be evaluated by:
#
#      n!
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
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
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, integer N, the argument of the function.
#
#    Output, real FN, the value of the function.
#
  import numpy as np

  n_max = 25

  fn_vec = np.array ( [ \
     0.1000000000000000E+01, \
     0.1000000000000000E+01, \
     0.2000000000000000E+01, \
     0.6000000000000000E+01, \
     0.2400000000000000E+02, \
     0.1200000000000000E+03, \
     0.7200000000000000E+03, \
     0.5040000000000000E+04, \
     0.4032000000000000E+05, \
     0.3628800000000000E+06, \
     0.3628800000000000E+07, \
     0.3991680000000000E+08, \
     0.4790016000000000E+09, \
     0.6227020800000000E+10, \
     0.8717829120000000E+11, \
     0.1307674368000000E+13, \
     0.2092278988800000E+14, \
     0.3556874280960000E+15, \
     0.6402373705728000E+16, \
     0.1216451004088320E+18, \
     0.2432902008176640E+19, \
     0.1551121004333099E+26, \
     0.3041409320171338E+65, \
     0.9332621544394415E+158, \
     0.5713383956445855E+263 ] )

  n_vec = np.array ( [ \
       0, \
       1, \
       2, \
       3, \
       4, \
       5, \
       6, \
       7, \
       8, \
       9, \
      10, \
      11, \
      12, \
      13, \
      14, \
      15, \
      16, \
      17, \
      18, \
      19, \
      20, \
      25, \
      50, \
     100, \
     150 ] )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    fn = 0
  else:
    n = n_vec[n_data]
    fn = fn_vec[n_data]
    n_data = n_data + 1

  return n_data, n, fn

def r8_factorial_values_test ( ):

#*****************************************************************************80
#
## R8_FACTORIAL_VALUES_TEST tests R8_FACTORIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_FACTORIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_FACTORIAL_VALUES returns values of the real factorial function.' )
  print ( '' )
  print ( '          N          R8_FACTORIAL(N)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, fn = r8_factorial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %8d  %14.6g' % ( n, fn ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_FACTORIAL_VALUES_TEST:' )
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
    print ( '  Row' )

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
  legendre_polynomial_test ( )
  timestamp ( )

