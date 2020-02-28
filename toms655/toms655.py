#! /usr/bin/env python3
#
def gamma_values ( n_data ):

#*****************************************************************************80
#
## GAMMA_VALUES returns some values of the Gamma function.
#
#  Discussion:
#
#    The Gamma function is defined as:
#
#      Gamma(Z) = Integral ( 0 <= T < Infinity) T^(Z-1) exp(-T) dT
#
#    It satisfies the recursion:
#
#      Gamma(X+1) = X * Gamma(X)
#
#    Gamma is undefined for nonpositive integral X.
#    Gamma(0.5) = sqrt(PI)
#    For N a positive integer, Gamma(N+1) = N!, the standard factorial.
#
#    In Mathematica, the function can be evaluated by:
#
#      Gamma[x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 July 2014
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
#    Output, real X, the argument of the function.
#
#    Output, real FX, the value of the function.
#
  import numpy as np

  n_max = 25

  fx_vec = np.array ( ( \
     -0.3544907701811032E+01, \
     -0.1005871979644108E+03, \
      0.9943258511915060E+02, \
      0.9513507698668732E+01, \
      0.4590843711998803E+01, \
      0.2218159543757688E+01, \
      0.1772453850905516E+01, \
      0.1489192248812817E+01, \
      0.1164229713725303E+01, \
      0.1000000000000000E+01, \
      0.9513507698668732E+00, \
      0.9181687423997606E+00, \
      0.8974706963062772E+00, \
      0.8872638175030753E+00, \
      0.8862269254527580E+00, \
      0.8935153492876903E+00, \
      0.9086387328532904E+00, \
      0.9313837709802427E+00, \
      0.9617658319073874E+00, \
      0.1000000000000000E+01, \
      0.2000000000000000E+01, \
      0.6000000000000000E+01, \
      0.3628800000000000E+06, \
      0.1216451004088320E+18, \
      0.8841761993739702E+31 ) )

  x_vec = np.array ( ( \
     -0.50E+00, \
     -0.01E+00, \
      0.01E+00, \
      0.10E+00, \
      0.20E+00, \
      0.40E+00, \
      0.50E+00, \
      0.60E+00, \
      0.80E+00, \
      1.00E+00, \
      1.10E+00, \
      1.20E+00, \
      1.30E+00, \
      1.40E+00, \
      1.50E+00, \
      1.60E+00, \
      1.70E+00, \
      1.80E+00, \
      1.90E+00, \
      2.00E+00, \
      3.00E+00, \
      4.00E+00, \
     10.00E+00, \
     20.00E+00, \
     30.00E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    fx = 0.0
  else:
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, x, fx

def gamma_values_test ( ):

#*****************************************************************************80
#
## GAMMA_VALUE_TEST demonstrates the use of GAMMA_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 February 2009
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'GAMMA_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GAMMA_VALUES stores values of the Gamma function.' )
  print ( '' )
  print ( '      X            GAMMA(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx = gamma_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GAMMA_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4_sign ( i ):

#*****************************************************************************80
#
## I4_SIGN returns the sign of an integer.
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
#    05 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the number whose sign is desired.
#
#    Output, integer VALUE, the sign of I.
#
  if ( i < 0 ):
    value = -1
  else:
    value = +1

  return value

def i4_sign_test ( ):

#*****************************************************************************80
#
## I4_SIGN_TEST tests I4_SIGN.
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

  i4_vec = np.array ( ( -10, -7, 0, 5, 9 ) )

  print ( '' )
  print ( 'I4_SIGN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_SIGN returns the sign of an I4.' )
  print ( '' )
  print ( '    I4  I4_SIGN(I4)' )
  print ( '' )

  for test in range ( 0, test_num ):
    i4 = i4_vec[test]
    s = i4_sign ( i4 )
    print ( '  %4d  %11d' % ( i4, s ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_SIGN_TEST' )
  print ( '  Normal end of execution.' )
  return

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

def parchk ( kind, m, alpha, beta ):

#*****************************************************************************80
#
## PARCHK checks parameters ALPHA and BETA for classical weight functions.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 February 2010
#
#  Author:
#
#    Original FORTRAN77 version by Sylvan Elhay, Jaroslav Kautsky.
#    MATLAB version by John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#  Parameters:
#
#    Input, integer KIND, the rule.
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
#    Input, integer M, the order of the highest moment to
#    be calculated.  This value is only needed when KIND = 8.
#
#    Input, real ALPHA, BETA, the parameters, if required
#    by the value of KIND.
#
#    Output, logical CHECK, is TRUE if the variables are OK.
#
  from sys import exit

  check = True

  if ( kind < 1 ):
    check = False
    print ( '' )
    print ( 'PARCHK - Fatal error!' )
    print ( '  KIND < 1.' )
#   exit ( 'PARCHK - Fatal error!' )

  if ( 9 < kind ):
    check = False
    print ( '' )
    print ( 'PARCHK - Fatal error!' )
    print ( '  9 < KIND.' )
#   exit ( 'PARCHK - Fatal error!' )
#
#  Check ALPHA for Gegenbauer, Jacobi, Laguerre, Hermite, Exponential.
#
  if ( 3 <= kind and kind <= 8 and alpha <= -1.0 ):
    check = False
    print ( '' )
    print ( 'PARCHK - Fatal error!' )
    print ( '  ( 3 <= KIND <= 8 ) and ALPHA <= -1.' )
#   exit ( 'PARCHK - Fatal error!' )
#
#  Check BETA for Jacobi.
#
  if ( kind == 4 and beta <= -1.0 ):
    check = False
    print ( '' )
    print ( 'PARCHK - Fatal error!' )
    print ( '  KIND == 4 and BETA <= -1.0.' )
#   error ( 'PARCHK - Fatal error!' )
#
#  Check ALPHA and BETA for rational.
#
  if ( kind == 8 ):
    if ( 0.0 <= alpha + beta + m + 1.0 ):
      check = False
      print ( '' )
      print ( 'PARCHK - Fatal error!' )
      print ( '  KIND == 8 but 0 <= ALPHA + BETA + M + 1.' )
#     exit ( 'PARCHK - Fatal error!' )
    if ( alpha + m + 1.0 <= 0.0 ):
      check = False
      print ( '' )
      print ( 'PARCHK - Fatal error!' )
      print ( '  KIND == 8 but ALPHA + M + 1.0 <= 0.0.' )
#     exit ( 'PARCHK - Fatal error!' )

  return check

def parchk_test ( ):

#*****************************************************************************80
#
## PARCHK_TEST tests PARCHK.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    John Burkardt.
#
  import numpy as np
  import platform

  test_num = 18

  kind_vec  = np.array ( [  \
    0, \
    1, \
    2, \
    3, 3, \
    4, 4, 4, \
    5, 5, \
    6, 6, \
    7, 7, \
    8, 8, 8, \
    9 ] )
  m_vec = np.array ( [ \
    0, \
    0, \
    0, \
    0, 0, \
    0, 0, 0, \
    0, 0, \
    0, 0, \
    0, 0, \
    3, 3, 3, \
    0 ] )
  alpha_vec = np.array ( [ \
    0.5, \
    0.5, \
    0.5, \
   -0.5, -1.5, \
   -0.5, -1.5, 0.5, \
   -0.5, -1.5, \
   -0.5, -1.5, \
   -0.5, -1.5, \
   -2.0, -0.5, -0.5, \
    0.5, ] )
  beta_vec  = np.array ( [ \
    0.5, \
    0.5, \
    0.5, \
    0.5,  0.5, \
    0.5,  0.5, -2.0, \
    0.5,  0.5, \
    0.5,  0.5, \
    0.5,  0.5, \
   -3.0, -4.0, -3.0, \
    0.5, ] )

  print ( '' )
  print ( 'PARCHK_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PARCHK checks quadrature rule parameters.' )
  print ( '' )
  print ( '  KIND   M           ALPHA            BETA  CHECK?' )
  print ( '' )

  for test in range ( 0, test_num ):

    kind = kind_vec[test]
    m = m_vec[test]
    alpha = alpha_vec[test]
    beta = beta_vec[test]

    check = parchk ( kind, m, alpha, beta )
    print ( '     %1d  %2d  %14.6g  %14.6g  %s' % ( kind, m, alpha, beta, check ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PARCHK_TEST' )
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

def r8_gamma ( x ):

#*****************************************************************************80
#
## R8_GAMMA evaluates Gamma(X) for a real argument.
#
#  Discussion:
#
#    This routine calculates the gamma function for a real argument X.
#
#    Computation is based on an algorithm outlined in reference 1.
#    The program uses rational functions that approximate the gamma
#    function to at least 20 significant decimal digits.  Coefficients
#    for the approximation over the interval (1,2) are unpublished.
#    Those for the approximation for 12 <= X are from reference 2.
#
#    PYTHON provides a GAMMA function, which is likely to be faster, and more
#    accurate.  
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 July 2014
#
#  Author:
#
#    Original FORTRAN77 version by William Cody, Laura Stoltz.
#    PYTHON version by John Burkardt.
#
#  Reference:
#
#    William Cody,
#    An Overview of Software Development for Special Functions,
#    in Numerical Analysis Dundee, 1975,
#    edited by GA Watson,
#    Lecture Notes in Mathematics 506,
#    Springer, 1976.
#
#    John Hart, Ward Cheney, Charles Lawson, Hans Maehly,
#    Charles Mesztenyi, John Rice, Henry Thatcher,
#    Christoph Witzgall,
#    Computer Approximations,
#    Wiley, 1968,
#    LC: QA297.C64.
#
#  Parameters:
#
#    Input, real X, the argument of the function.
#
#    Output, real VALUE, the value of the function.
#
  import numpy as np
  from math import floor
#
#  Coefficients for minimax approximation over (12, INF).
#
  c = np.array ( [
   -1.910444077728E-03, \
    8.4171387781295E-04, \
   -5.952379913043012E-04, \
    7.93650793500350248E-04, \
   -2.777777777777681622553E-03, \
    8.333333333333333331554247E-02, \
    5.7083835261E-03 ] )
#
#  Mathematical constants
#
  sqrtpi = 0.9189385332046727417803297
#
#  Machine dependent parameters
#
  xbig = 171.624
  xminin = 2.23E-308
  eps = 2.22E-16
  xinf = 1.79E+308
#
#  Numerator and denominator coefficients for rational minimax
#  approximation over (1,2).
#
  p = np.array ( [ \
   -1.71618513886549492533811E+00, \
    2.47656508055759199108314E+01, \
   -3.79804256470945635097577E+02, \
    6.29331155312818442661052E+02, \
    8.66966202790413211295064E+02, \
   -3.14512729688483675254357E+04, \
   -3.61444134186911729807069E+04, \
    6.64561438202405440627855E+04 ] )

  q = np.array ( [ \
   -3.08402300119738975254353E+01, \
    3.15350626979604161529144E+02, \
   -1.01515636749021914166146E+03, \
   -3.10777167157231109440444E+03, \
    2.25381184209801510330112E+04, \
    4.75584627752788110767815E+03, \
   -1.34659959864969306392456E+05, \
   -1.15132259675553483497211E+05 ] )

  parity = 0
  fact = 1.0
  n = 0
  y = x
#
#  Argument is negative.
#
  if ( y <= 0.0 ):

    y = - x
    y1 = floor ( y )
    res = y - y1

    if ( res != 0.0 ):

      if ( y1 != floor ( y1 * 0.5 ) * 2.0 ):
        parity = 1

      fact = - np.pi / np.sin ( np.pi * res )
      y = y + 1.0

    else:

      res = xinf
      value = res
      return value
#
#  Argument is positive.
#
  if ( y < eps ):
#
#  Argument < EPS.
#
    if ( xminin <= y ):
      res = 1.0 / y
    else:
      res = xinf

    value = res
    return value

  elif ( y < 12.0 ):

    y1 = y
#
#  0.0 < argument < 1.0.
#
    if ( y < 1.0 ):

      z = y
      y = y + 1.0
#
#  1.0 < argument < 12.0.
#  Reduce argument if necessary.
#
    else:

      n = int ( floor ( y ) - 1 )
      y = y - n
      z = y - 1.0
#
#  Evaluate approximation for 1.0 < argument < 2.0.
#
    xnum = 0.0
    xden = 1.0
    for i in range ( 0, 8 ):
      xnum = ( xnum + p[i] ) * z
      xden = xden * z + q[i]

    res = xnum / xden + 1.0
#
#  Adjust result for case  0.0 < argument < 1.0.
#
    if ( y1 < y ):

      res = res / y1
#
#  Adjust result for case 2.0 < argument < 12.0.
#
    elif ( y < y1 ):

      for i in range ( 0, n ):
        res = res * y
        y = y + 1.0

  else:
#
#  Evaluate for 12.0 <= argument.
#
    if ( y <= xbig ):

      ysq = y * y
      sum = c[6]
      for i in range ( 0, 6 ):
        sum = sum / ysq + c[i]
      sum = sum / y - y + sqrtpi
      sum = sum + ( y - 0.5 ) * np.log ( y )
      res = np.exp ( sum )

    else:

      res = xinf
      value = res
      return value
#
#  Final adjustments and return.
#
  if ( parity ):
    res = - res

  if ( fact != 1.0 ):
    res = fact / res

  value = res

  return value

def r8_gamma_test ( ):

#*****************************************************************************80
#
## R8_GAMMA_TEST demonstrates the use of R8_GAMMA.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_GAMMA_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_GAMMA evaluates the Gamma function.' )
  print ( '' )
  print ( '      X            GAMMA(X)      R8_GAMMA(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = gamma_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamma ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAMMA_TEST' )
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

def toms655_test ( ):

#*****************************************************************************80
#
## TOMS655_TEST tests the TOMS655 library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TOMS655_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the TOMS655 library.' )

  gamma_values_test ( )

  i4_sign_test ( )

  imtqlx_test ( )

  parchk_test ( )

  r8_gamma_test ( )
  r8_sign_test ( )

  wm_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TOMS655_TEST:' )
  print ( '  Normal end of execution.' )
  return

def wm ( m, kind, alpha, beta ):

#*****************************************************************************80
#
## WM evaluates the first M moments of classical weight functions.
#
#  Discussion:
#
#    W(K) = Integral ( A <= X <= B ) X^(K-1) * W(X) dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    Original FORTRAN77 version by Sylvan Elhay, Jaroslav Kautsky.
#    Python version by John Burkardt.
#
#  Reference:
#
#    Sylvan Elhay, Jaroslav Kautsky,
#    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
#    Interpolatory Quadrature,
#    ACM Transactions on Mathematical Software,
#    Volume 13, Number 4, December 1987, pages 399-415.
#
#  Parameters:
#
#    Input, integer M, the number of moments to evaluate.
#
#    Input, integer KIND, the rule.
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
#    Input, real ALPHA, the value of Alpha, if needed.
#
#    Input, real BETA, the value of Beta, if needed.
#
#    Output, real W(M), the first M moments.
#
  import numpy as np

  parchk ( kind, m, alpha, beta )

  w = np.zeros ( m )

  if ( kind == 1 ):

    for k in range ( 0, m, 2 ):
      w[k] = 2.0 / float ( k + 1 )

  elif ( kind == 2 ):

    w[0] = np.pi
    for k in range ( 2, m, 2 ):
      w[k] = w[k-2] * float ( k - 1 ) / float ( k )

  elif ( kind == 3 ):

    w[0] = np.sqrt ( np.pi ) * r8_gamma ( alpha + 1.0 ) \
      / r8_gamma ( alpha + 3.0 / 2.0 )

    for k in range ( 2, m, 2 ):
      w[k] = w[k-2] * float ( k - 1.0 ) / ( 2.0 * alpha + k + 1 )

  elif ( kind == 4 ):

    als = alpha + beta + 1.0
    w[0] = 2.0 ** als * r8_gamma ( alpha + 1.0 ) \
      / r8_gamma ( als + 1.0 ) * r8_gamma ( beta + 1.0 )

    for k in range ( 1, m ):

      sum = 0.0
      trm = 1.0

      for i in range ( 0, ( k - 1 ) // 2 + 1 ):

        tmpa = trm
        for ja in range ( 1, 2 * i + 1 ):
          tmpa = tmpa * ( alpha + ja ) / ( als + ja )

        for jb in range ( 1, k + 1 - 2 * i ):
          tmpa = tmpa * ( beta + jb ) / ( als + 2 * i + jb )

        tmpa = tmpa / ( 2 * i + 1.0 ) * \
          ( 2 * i * ( beta + alpha ) + beta - k * alpha ) \
          / ( beta + k + 1 - 2 * i - 1.0 )
        sum = sum + tmpa

        trm = trm * ( k - 2 * i ) \
          / ( 2 * i + 1.0 ) * ( k - 2 * i - 1.0 ) / ( 2 * i + 2.0 )

      if ( ( k % 2 ) == 0 ):
        tmpb = 1.0
        for i in range ( 0, k ):
          tmpb = tmpb * ( alpha + i + 1 ) / ( als + i + 1 )
        sum = sum + tmpb

      w[k] = sum * w[0]

  elif ( kind == 5 ):

    w[0] = r8_gamma ( alpha + 1.0 )

    for k in range ( 1, m ):
      w[k] = ( alpha + k ) * w[k-1]

  elif ( kind == 6 ):

    w[0] = r8_gamma ( ( alpha + 1.0 ) / 2.0 )

    for k in range ( 2, m, 2 ):
      w[k] = w[k-2] * ( alpha + k - 1.0 ) / 2.0

  elif ( kind == 7 ):

    als = alpha
    for k in range ( 0, m, 2 ):
      w[k] = 2.0 / ( k + 1 + als )

  elif ( kind == 8 ):

    w[0] = r8_gamma ( alpha + 1.0 ) \
      * r8_gamma ( - alpha - beta - 1.0 ) \
      / r8_gamma ( - beta )

    for k in range ( 1, m ):
      w[k] = - w[k-1] * ( alpha + k ) / ( alpha + beta + k + 1 )

  elif ( kind == 9 ):

    w[0] = np.pi / 2.0
    for k in range ( 2, m, 2 ):
      w[k] = w[k-2] * float ( k - 1.0 ) / float ( k + 2.0 )

  return w

def wm_test ( ):

#*****************************************************************************80
#
## WM_TEST calls WM_TESTER with various parameter values.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 November 2015
#
#  Author:
#
#    John Burkardt.
#
  m = 5
  kind = 1
  alpha = 0.0
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 2
  alpha = 0.0
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 3
  alpha = 0.5
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 4
  alpha = 0.25
  beta = 0.75
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 5
  alpha = 2.0
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 6
  alpha = 1.0
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 7
  alpha = 2.0
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 8
  alpha = -0.5
  beta = -6.0
  wm_tester ( m, kind, alpha, beta )

  m = 5
  kind = 9
  alpha = 0.0
  beta = 0.0
  wm_tester ( m, kind, alpha, beta )
#
#  Terminate.
#
  print ( '' )
  print ( 'WM_TEST' )
  print ( '  Normal end of execution.' )
  return

def wm_tester ( m, kind, alpha, beta ):

#*****************************************************************************80
#
## WM_TESTER tests WM.
#
#  Discussion:
#
#    Moment(K) = Integral ( A <= X <= B ) X^(K-1) * W(X) dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 November 2015
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
#  Parameters:
#
#    Input, integer M, the number of moments to evaluate.
#
#    Input, integer KIND, the rule.
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
#    Input, real ALPHA, the value of Alpha, if needed.
#
#    Input, real BETA, the value of Beta, if needed.
#
  import platform

  w = wm ( m, kind, alpha, beta )

  print ( '' )
  print ( 'WM_TESTER:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WM_TEST computes moments for rule %d' % ( kind ) )
  print ( '  with ALPHA = %g, BETA = %g' % ( alpha, beta ) )
  print ( '' )
  print ( '  Order          Moment' )
  print ( '' )
  for i in range ( 0, m ):
    print ( '     %2d  %14.6g' % ( i, w[i] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'WM_TESTER:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  toms655_test ( )
  timestamp ( )
