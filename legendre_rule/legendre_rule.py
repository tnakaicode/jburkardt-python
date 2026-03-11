#! /usr/bin/env python3
#
def legendre_rule_test ( ):

#*****************************************************************************80
#
## legendre_rule_test() tests legendre_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'legendre_rule_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test legendre_rule().' )

  legendre_rule ( 4, -1.0, +1.0, 'leg_o4' )
#
#  Terminate.
#
  print ( '' )
  print ( 'legendre_rule_test():' )
  print ( '  Normal end of execution.' )

  return

def legendre_rule ( order, a, b, filename ):

#*****************************************************************************80
#
## legendre_rule() generates a Gauss-Legendre rule.
#
#  Discussion:
#
#    This program computes a standard Gauss-Legendre quadrature rule
#    and writes it to a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 May 2023
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ORDER, the number of points in the rule
#
#    real A, B, the endpoints
#
#    character FILENAME, the root name of the output files.
#
  import numpy as np

  print ( '' )
  print ( 'legendre_rule()' )
  print ( '  Compute a Gauss-Legendre rule for approximating' )
  print ( '    Integral ( A <= x <= B ) f(x) dx' )
  print ( '  of order ORDER.' )
  print ( '' )
  print ( '  The user specifies ORDER, A, B, and FILENAME.' )
  print ( '' )
  print ( '  ORDER is the number of points' )
  print ( '  A is the left endpoint' )
  print ( '  B is the right endpoint' )
  print ( '  FILENAME is used to generate 3 files:' )
  print ( '    filename_w.txt - the weight file' )
  print ( '    filename_x.txt - the abscissa file.' )
  print ( '    filename_r.txt - the region file.' )
#
#  Initialize the parameters.
#
  alpha = 0.0
  beta = 0.0
#
#  Input summary.
#
  print ( '' )
  print ( '  ORDER = ', order )
  print ( '  A = ', a )
  print ( '  B = ', b )
  print ( '  FILENAME = "' + filename + '".' )
#
#  Construct the rule.
#
  kind = 1
  x, w = cgqf ( order, kind, alpha, beta, a, b )
#
#  Write the rule.
#
  r = np.array ( [ a, b ] )

  filename_x = filename + '_x.txt'
  np.savetxt ( filename_x, x )
  print ( '  abscissas saved as "' + filename_x + '"' )
  filename_w = filename + '_w.txt'
  np.savetxt ( filename_w, w )
  print ( '  weights saved as "' + filename_w + '"' )
  filename_r = filename + '_r.txt'
  np.savetxt ( filename_r, r )
  print ( '  region saved as "' + filename_r + '"' )

  return

def cdgqf ( nt, kind, alpha, beta ):

#*****************************************************************************80
#
## cdgqf() computes a Gauss quadrature formula with default A, B and simple knots.
#
#  Discussion:
#
#    This routine computes all the knots and weights of a Gauss quadrature
#    formula with a classical weight function with default values for A and B,
#    and only simple knots.
#
#    There are no moments checks and no printing is done.
#
#    Use routine EIQFS to evaluate a quadrature computed by CGQFS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 May 2023
#
#  Author:
#
#    Original FORTRAN77 version by Sylvan Elhay, Jaroslav Kautsky.
#    This version by John Burkardt.
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
#    integer NT, the number of knots.
#
#    integer KIND, the rule.
#    1, Legendre,             (a,b)       1.0
#    2, Chebyshev Type 1,     (a,b)       ((b-x)*(x-a))^(-0.5)
#    3, Gegenbauer,           (a,b)       ((b-x)*(x-a))^alpha
#    4, Jacobi,               (a,b)       (b-x)^alpha*(x-a)^beta
#    5, Generalized Laguerre, (a,inf)     (x-a)^alpha*exp(-b*(x-a))
#    6, Generalized Hermite,  (-inf,inf)  |x-a|^alpha*exp(-b*(x-a)^2)
#    7, Exponential,          (a,b)       |x-(a+b)/2.0|^alpha
#    8, Rational,             (a,inf)     (x-a)^alpha*(x+b)^beta
#
#    real ALPHA, the value of Alpha, if needed.
#
#    real BETA, the value of Beta, if needed.
#
#  Output:
#
#    real T(NT), the knots.
#
#    real WTS(NT), the weights.
#
  parchk ( kind, 2 * nt, alpha, beta )
#
#  Get the Jacobi matrix and zero-th moment.
#
  aj, bj, zemu = class_matrix ( kind, nt, alpha, beta )
#
#  Compute the knots and weights.
#
  t, wts = sgqf ( nt, aj, bj, zemu )

  return t, wts

def cgqf ( nt, kind, alpha, beta, a, b ):

#*****************************************************************************80
#
## cgqf() computes knots and weights of a Gauss quadrature formula.
#
#  Discussion:
#
#    The user may specify the interval (A,B).
#
#    Only simple knots are produced.
#
#    The user may request that the routine print the knots and weights,
#    and perform a moment check.
#
#    Use routine EIQFS to evaluate this quadrature formula.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 May 2023
#
#  Author:
#
#    Original FORTRAN77 version by Sylvan Elhay, Jaroslav Kautsky.
#    This version by John Burkardt.
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
#    integer NT, the number of knots.
#
#    integer KIND, the rule.
#    1, Legendre,             (a,b)       1.0
#    2, Chebyshev Type 1,     (a,b)       ((b-x)*(x-a))^(-0.5)
#    3, Gegenbauer,           (a,b)       ((b-x)*(x-a))^alpha
#    4, Jacobi,               (a,b)       (b-x)^alpha*(x-a)^beta
#    5, Generalized Laguerre, (a,+oo)     (x-a)^alpha*exp(-b*(x-a))
#    6, Generalized Hermite,  (-oo,+oo)   |x-a|^alpha*exp(-b*(x-a)^2)
#    7, Exponential,          (a,b)       |x-(a+b)/2.0|^alpha
#    8, Rational,             (a,+oo)     (x-a)^alpha*(x+b)^beta
#    9, Chebyshev Type 2,     (a,b)       ((b-x)*(x-a))^(+0.5)
#
#    real ALPHA, the value of Alpha, if needed.
#
#    real BETA, the value of Beta, if needed.
#
#    real A, B, the interval endpoints.
#
#  Output:
#
#    real T(NT), the knots.
#
#    real WTS(NT), the weights.
#
  import numpy as np
#
#  Compute the Gauss quadrature formula for default values of A and B.
#
  t, wts = cdgqf ( nt, kind, alpha, beta )
#
#  All knots have multiplicity = 1.
#
  mlt = np.ones ( nt, dtype = int )
#
#  NDX(I) = I.
#
  ndx = np.arange ( 1, nt + 1 )
#
#  Scale the quadrature rule.
#
  t, wts = scqf ( nt, t, mlt, wts, nt, ndx, kind, alpha, beta, a, b )

  return t, wts

def class_matrix ( kind, m, alpha, beta ):

#*****************************************************************************80
#
## class_matrix() computes the Jacobi matrix for a quadrature rule.
#
#  Discussion:
#
#    This routine computes the diagonal AJ and subdiagonal BJ
#    elements of the order M tridiagonal symmetric Jacobi matrix
#    associated with the polynomials orthogonal with respect to
#    the weight function specified by KIND.
#
#    For weight functions 1-7, M elements are defined in BJ even
#    though only M-1 are needed.  For weight function 8, BJ(M) is
#    set to zero.
#
#    The zero-th moment of the weight function is returned in ZEMU.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 May 2023
#
#  Author:
#
#    Original FORTRAN77 version by Sylvan Elhay, Jaroslav Kautsky.
#    This version by John Burkardt.
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
#    integer KIND, the rule.
#    1, Legendre,             (a,b)       1.0
#    2, Chebyshev Type 1,     (a,b)       ((b-x)*(x-a))^(-0.5)
#    3, Gegenbauer,           (a,b)       ((b-x)*(x-a))^alpha
#    4, Jacobi,               (a,b)       (b-x)^alpha*(x-a)^beta
#    5, Generalized Laguerre, (a,inf)     (x-a)^alpha*exp(-b*(x-a))
#    6, Generalized Hermite,  (-inf,inf)  |x-a|^alpha*exp(-b*(x-a)^2)
#    7, Exponential,          (a,b)       |x-(a+b)/2.0|^alpha
#    8, Rational,             (a,inf)     (x-a)^alpha*(x+b)^beta
#
#    integer M, the order of the Jacobi matrix.
#
#    real ALPHA, the value of Alpha, if needed.
#
#    real BETA, the value of Beta, if needed.
#
#  Output:
#
#    real AJ(M), BJ(M), the diagonal and subdiagonal
#    of the Jacobi matrix.
#
#    real ZEMU, the zero-th moment.
#
  from scipy.special import gamma
  import numpy as np

  epsilon = np.finfo(float).eps

  parchk ( kind, 2 * m - 1, alpha, beta )

  if ( 500.0 * epsilon < np.abs ( ( gamma ( 0.5 ) ) ** 2 - np.pi ) ):
    print ( '' )
    print ( 'class_matrix(): Fatal error!' )
    print ( '  Gamma function does not match machine parameters.' )
    raise Exception ( 'class_matrix(): Fatal error!' )

  bj = np.zeros ( m )
  aj = np.zeros ( m )

  if ( kind == 1 ):

    ab = 0.0

    zemu = 2.0 / ( ab + 1.0 )

    for im1 in range ( 0, m ):
      i = im1 + 1
      abi = i + ab * ( i % 2 )
      abj = 2 * i + ab
      bj[im1] = abi * abi / ( abj * abj - 1.0 )

    bj = np.sqrt ( bj )

  elif ( kind == 2 ):

    zemu = np.pi

    bj[0] = np.sqrt ( 0.5 )
    bj[1:m] = 0.5

  elif ( kind == 3 ):

    ab = alpha * 2.0
    zemu = 2.0 ** ( ab + 1.0 ) * gamma ( alpha + 1.0 ) ** 2 \
      / gamma ( ab + 2.0 )

    bj[0] = 1.0 / ( 2.0 * alpha + 3.0 )
    for im1 in range ( 0, m ):
      i = im1 + 1
      bj[im1] = i * ( i + ab ) / ( 4.0 * ( i + alpha ) ** 2 - 1.0 )

    bj = np.sqrt ( bj )

  elif ( kind == 4 ):

    ab = alpha + beta
    abi = 2.0 + ab
    zemu = 2.0 ** ( ab + 1.0 ) * gamma ( alpha + 1.0 ) \
      * gamma ( beta + 1.0 ) / gamma ( abi )
    aj[0] = ( beta - alpha ) / abi
    bj[0] = 4.0 * ( 1.0 + alpha ) * ( 1.0 + beta ) \
      / ( ( abi + 1.0 ) * abi * abi )
    a2b2 = beta * beta - alpha * alpha

    for im1 in range ( 1, m ):
      i = im1 + 1
      abi = 2.0 * i + ab
      aj[im1] = a2b2 / ( ( abi - 2.0 ) * abi )
      abi = abi * abi
      bj[im1] = 4.0 * i * ( i + alpha ) * ( i + beta ) * ( i + ab ) \
        / ( ( abi - 1.0 ) * abi )

    bj = np.sqrt ( bj )

  elif ( kind == 5 ):

    zemu = gamma ( alpha + 1.0 )

    for im1 in range ( 0, m ):
      i = im1 + 1
      aj[im1] = 2.0 * i - 1.0 + alpha
      bj[im1] = i * ( i + alpha )

    bj = np.sqrt ( bj )

  elif ( kind == 6 ):

    zemu = gamma ( ( alpha + 1.0 ) / 2.0 )

    for im1 in range ( 0, m ):
      i = im1 + 1
      bj[im1] = ( i + alpha * ( i % 2 ) ) / 2.0

    bj = np.sqrt ( bj )

  elif ( kind == 7 ):

    ab = alpha
    zemu = 2.0 / ( ab + 1.0 )

    for im1 in range ( 0, m ):
      i = im1 + 1
      abi = i + ab * ( i % 2 )
      abj = 2 * i + ab
      bj[im1] = abi * abi / ( abj * abj - 1.0 )

    bj = np.sqrt ( bj )

  elif ( kind == 8 ):

    ab = alpha + beta
    zemu = gamma ( alpha + 1.0 ) * gamma ( - ( ab + 1.0 ) ) \
      / gamma ( - beta )
    apone = alpha + 1.0
    aba = ab * apone
    aj[0] = - apone / ( ab + 2.0 )
    bj[0] = - aj[0] * ( beta + 1.0 ) / ( ab + 2.0 ) / ( ab + 3.0 )
    for im1 in range ( 1, m ):
      i = im1 + 1
      abti = ab + 2.0 * i
      aj[im1] = aba + 2.0 * ( ab + i ) * ( i - 1 )
      aj[im1] = - aj[im1] / abti / ( abti - 2.0 )

    for im1 in range ( 1, m - 1 ):
      i = im1 + 1
      abti = ab + 2.0 * i
      bj[im1] = i * ( alpha + i ) / ( abti - 1.0 ) * ( beta + i ) \
        / ( abti ** 2 ) * ( ab + i ) / ( abti + 1.0 )

    bj[m-1] = 0.0
    bj = np.sqrt ( bj )

  elif ( kind == 9 ):

    zemu = np.pi / 2.0
    bj = 0.5 * np.ones ( m )

  return aj, bj, zemu

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
        print ( 'imtqlx - Fatal error!' )
        print ( '  Iteration limit exceeded.' )
        raise Exception ( 'imtqlx - Fatal error!' )

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

def parchk ( kind, m, alpha, beta ):

#*****************************************************************************80
#
## parchk() checks parameters ALPHA and BETA for classical weight functions.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 February 2010
#
#  Author:
#
#    Original FORTRAN77 version by Sylvan Elhay, Jaroslav Kautsky.
#    This version by John Burkardt.
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
#    integer KIND, the rule.
#    1, Legendre,             (a,b)       1.0
#    2, Chebyshev Type 1,     (a,b)       ((b-x)*(x-a))^(-0.5)
#    3, Gegenbauer,           (a,b)       ((b-x)*(x-a))^alpha
#    4, Jacobi,               (a,b)       (b-x)^alpha*(x-a)^beta
#    5, Generalized Laguerre, (a,+oo)     (x-a)^alpha*exp(-b*(x-a))
#    6, Generalized Hermite,  (-oo,+oo)   |x-a|^alpha*exp(-b*(x-a)^2)
#    7, Exponential,          (a,b)       |x-(a+b)/2.0|^alpha
#    8, Rational,             (a,+oo)     (x-a)^alpha*(x+b)^beta
#    9, Chebyshev Type 2,     (a,b)       ((b-x)*(x-a))^(+0.5)
#
#    integer M, the order of the highest moment to
#    be calculated.  This value is only needed when KIND = 8.
#
#    real ALPHA, BETA, the parameters, if required
#    by the value of KIND.
#
#  Output:
#
#    bool CHECK, is TRUE if the variables are OK.
#
  check = True

  if ( kind < 1 ):
    check = False
    print ( '' )
    print ( 'parchk - Fatal error!' )
    print ( '  kind < 1.' )
    print ( '  kind = ', kind )
    raise Exception ( 'parchk - Fatal error!' )

  if ( 9 < kind ):
    check = False
    print ( '' )
    print ( 'parchk - Fatal error!' )
    print ( '  9 < KIND.' )
    raise Exception ( 'parchk - Fatal error!' )
#
#  Check ALPHA for Gegenbauer, Jacobi, Laguerre, Hermite, Exponential.
#
  if ( 3 <= kind and kind <= 8 and alpha <= -1.0 ):
    check = False
    print ( '' )
    print ( 'parchk - Fatal error!' )
    print ( '  ( 3 <= KIND <= 8 ) and ALPHA <= -1.' )
    raise Exception ( 'parchk - Fatal error!' )
#
#  Check BETA for Jacobi.
#
  if ( kind == 4 and beta <= -1.0 ):
    check = False
    print ( '' )
    print ( 'parchk - Fatal error!' )
    print ( '  KIND == 4 and BETA <= -1.0.' )
    raise Exception ( 'parchk - Fatal error!' )
#
#  Check ALPHA and BETA for rational.
#
  if ( kind == 8 ):
    if ( 0.0 <= alpha + beta + m + 1.0 ):
      check = False
      print ( '' )
      print ( 'parchk - Fatal error!' )
      print ( '  KIND == 8 but 0 <= ALPHA + BETA + M + 1.' )
      raise Exception ( 'parchk - Fatal error!' )
    if ( alpha + m + 1.0 <= 0.0 ):
      check = False
      print ( '' )
      print ( 'parchk - Fatal error!' )
      print ( '  KIND == 8 but ALPHA + M + 1.0 <= 0.0.' )
      raise Exception ( 'parchk - Fatal error!' )

  return check

def scqf ( nt, t, mlt, wts, nwts, ndx, kind, alpha, beta, a, b ):

#*****************************************************************************80
#
## scqf() scales a quadrature formula to a nonstandard interval.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    17 May 2023
#
#  Author:
#
#    Original FORTRAN77 version by Sylvan Elhay, Jaroslav Kautsky.
#    This version by John Burkardt.
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
#    integer NT, the number of knots.
#
#    real T(NT), the original knots.
#
#    integer MLT(NT), the multiplicity of the knots.
#
#    real WTS(NWTS), the weights.
#
#    integer NWTS, the number of weights.
#
#    integer NDX(NT), used to index the array WTS.
#    For more details see the comments in CAWIQ.
#
#    integer KIND, the rule.
#    1, Legendre,             (a,b)       1.0
#    2, Chebyshev Type 1,     (a,b)       ((b-x)*(x-a))^(-0.5)
#    3, Gegenbauer,           (a,b)       ((b-x)*(x-a))^alpha
#    4, Jacobi,               (a,b)       (b-x)^alpha*(x-a)^beta
#    5, Generalized Laguerre, (a,+oo)     (x-a)^alpha*exp(-b*(x-a))
#    6, Generalized Hermite,  (-oo,+oo)   |x-a|^alpha*exp(-b*(x-a)^2)
#    7, Exponential,          (a,b)       |x-(a+b)/2.0|^alpha
#    8, Rational,             (a,+oo)     (x-a)^alpha*(x+b)^beta
#    9, Chebyshev Type 2,     (a,b)       ((b-x)*(x-a))^(+0.5)
#
#    real ALPHA, the value of Alpha, if needed.
#
#    real BETA, the value of Beta, if needed.
#
#    real A, B, the interval endpoints.
#
#  Output:
#
#    real T(NT), the scaled knots.
#
#    real WTS(NWTS), the scaled weights.
#
  import numpy as np

  epsilon = np.finfo(float).eps

  parchk ( kind, 1, alpha, beta )

  if ( kind == 1 ):

    al = 0.0
    be = 0.0

    if ( np.abs ( b - a ) <= epsilon ):
      print ( '' )
      print ( 'scqf(): Fatal error!' )
      print ( '  |B - A| too small.' )
      print ( '  A = ', a )
      print ( '  B = ', b )
      raise Exception ( 'scqf(): Fatal error!' )

    shft = ( a + b ) / 2.0
    slp = ( b - a ) / 2.0

  elif ( kind == 2 ):

    al = -0.5
    be = -0.5

    if ( abs ( b - a ) <= epsilon ):
      print ( '' )
      print ( 'scqf(): Fatal error!' )
      print ( '  |B - A| too small.' )
      print ( '  A = ', a )
      print ( '  B = ', b )
      raise Exception ( 'scqf(): Fatal error!' )

    shft = ( a + b ) / 2.0
    slp = ( b - a ) / 2.0

  elif ( kind == 3 ):

    al = alpha
    be = alpha

    if ( abs ( b - a ) <= epsilon ):
      print ( '' )
      print ( 'scqf(): Fatal error!' )
      print ( '  |B - A| too small.' )
      print ( '  A = ', a )
      print ( '  B = ', b )
      raise Exception ( 'scqf(): Fatal error!' )

    shft = ( a + b ) / 2.0
    slp = ( b - a ) / 2.0

  elif ( kind == 4 ):

    al = alpha
    be = beta

    if ( abs ( b - a ) <= epsilon ):
      print ( '' )
      print ( 'scqf(): Fatal error!' )
      print ( '  |B - A| too small.' )
      print ( '  A = ', a )
      print ( '  B = ', b )
      raise Exception ( 'scqf(): Fatal error!' )

    shft = ( a + b ) / 2.0
    slp = ( b - a ) / 2.0

  elif ( kind == 5 ):

    if ( b <= 0.0 ):
      print ( '' )
      print ( 'scqf(): Fatal error!' )
      print ( '  B <= 0.' )
      print ( '  A = ', a )
      print ( '  B = ', b )
      raise Exception ( 'scqf(): Fatal error!' )

    shft = a
    slp = 1.0 / b
    al = alpha
    be = 0.0

  elif ( kind == 6 ):

    if ( b <= 0.0 ):
      print ( '' )
      print ( 'scqf(): Fatal error!' )
      print ( '  B <= 0.' )
      print ( '  A = ', a )
      print ( '  B = ', b )
      raise Exception ( 'scqf(): Fatal error!' )

    shft = a
    slp = 1.0 / np.sqrt ( b )
    al = alpha
    be = 0.0

  elif ( kind == 7 ):

    al = alpha
    be = 0.0

    if ( abs ( b - a ) <= epsilon ):
      print ( '' )
      print ( 'scqf(): Fatal error!' )
      print ( '  |B - A| too small.' )
      print ( '  A = ', a )
      print ( '  B = ', b )
      raise Exception ( 'scqf(): Fatal error!' )

    shft = ( a + b ) / 2.0
    slp = ( b - a ) / 2.0

  elif ( kind == 8 ):

    if ( a + b <= 0.0 ):
      print ( '' )
      print ( 'scqf(): Fatal error!' )
      print ( '  A + B <= 0.' )
      print ( '  A = ', a )
      print ( '  B = ', b )
      raise Exception ( 'scqf(): Fatal error!' )

    shft = a
    slp = a + b
    al = alpha
    be = beta

  elif ( kind == 9 ):

    al = 0.5
    be = 0.5

    if ( abs ( b - a ) <= epsilon ):
      print ( '' )
      print ( 'scqf(): Fatal error!' )
      print ( '  |B - A| too small.' )
      print ( '  A = ', a )
      print ( '  B = ', b )
      raise Exception ( 'scqf(): Fatal error!' )

    shft = ( a + b ) / 2.0
    slp = ( b - a ) / 2.0

  p = slp ** ( al + be + 1.0 )

  for k in range ( 0, nt ):

    t[k] = shft + slp * t[k]
    l = np.abs ( ndx[k] )

    if ( l != 0 ):
      tmp = p
      for i in range ( l, l + mlt[k] ):
        wts[i-1] = wts[i-1] * tmp
        tmp = tmp * slp

  return t, wts

def sgqf ( nt, aj, bj, zemu ):

#*****************************************************************************80
#
## sgqf() computes knots and weights of a Gauss Quadrature formula.
#
#  Discussion:
#
#    This routine computes all the knots and weights of a Gauss quadrature
#    formula with simple knots from the Jacobi matrix and the zero-th
#    moment of the weight function, using the Golub-Welsch technique.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 February 2010
#
#  Author:
#
#    Original FORTRAN77 version by Sylvan Elhay, Jaroslav Kautsky.
#    This version by John Burkardt.
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
#    integer NT, the number of knots.
#
#    real AJ(NT), the diagonal of the Jacobi matrix.
#
#    real BJ(NT), the subdiagonal of the Jacobi
#    matrix, in entries 1 through NT-1.  On BJ has been overwritten.
#
#    real ZEMU, the zero-th moment of the weight function.
#
#  Output:
#
#    real T(NT), the knots.
#
#    real WTS(NT), the weights.
#
  import numpy as np
#
#  Exit if the zero-th moment is not positive.
#
  if ( zemu <= 0.0 ):
    print ( '' )
    print ( 'sgqf(): Fatal error!' )
    print ( '  ZEMU <= 0.' )
    raise Exception ( 'sgqf(): Fatal error!' )
#
#  Set up vectors for IMTQLX.
#
  wts = np.zeros ( nt )

  wts[0] = np.sqrt ( zemu )
#
#  Diagonalize the Jacobi matrix.
#
  t, wts = imtqlx ( nt, aj, bj, wts )

  wts = wts ** 2

  return t, wts

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
  legendre_rule_test ( )
  timestamp ( )

