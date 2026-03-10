#! /usr/bin/env python3
#
def chebyshev_polynomial_test ( ):

#*****************************************************************************80
#
## chebyshev_polynomial_test() tests chebyshev_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'chebyshev_polynomial_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test chebyshev_polynomial().' )
#
#  Utilities.
#
  imtqlx_test ( )
  r8_hyper_2f1_test ( )
  r8_mop_test ( )
  r8_psi_test ( )
  r8poly_print_test ( )
#
#  Library functions.
#
  t_mass_matrix_test ( )
  t_moment_test ( )
  t_polynomial_test ( )
  t_polynomial_01_values_test ( )
  t_polynomial_ab_test ( )
  t_polynomial_ab_value_test ( )
  t_polynomial_coefficients_test ( )
  t_polynomial_plot_test ( )
  t_polynomial_value_test ( )
  t_polynomial_values_test ( )
  t_polynomial_zeros_test ( )
  t_quadrature_rule_test ( )
  tt_product_test ( )
  tt_product_integral_test ( )
  ttt_product_integral_test ( )
  tu_product_test ( )

  u_mass_matrix_test ( )
  u_moment_test ( )
  u_polynomial_test ( )
  u_polynomial_01_values_test ( )
  u_polynomial_ab_test ( )
  u_polynomial_ab_value_test ( )
  u_polynomial_coefficients_test ( )
  u_polynomial_plot_test ( )
  u_polynomial_value_test ( )
  u_polynomial_values_test ( )
  u_polynomial_zeros_test ( )
  u_quadrature_rule_test ( )
  uu_product_test ( )
  uu_product_integral_test ( )

  v_mass_matrix_test ( )
  v_moment_test ( )
  v_polynomial_test ( )
  v_polynomial_01_values_test ( )
  v_polynomial_ab_test ( )
  v_polynomial_ab_value_test ( )
  v_polynomial_coefficients_test ( )
  v_polynomial_plot_test ( )
  v_polynomial_value_test ( )
  v_polynomial_values_test ( )
  v_polynomial_zeros_test ( )
  v_quadrature_rule_test ( )
  vv_product_integral_test ( )

  w_mass_matrix_test ( )
  w_moment_test ( )
  w_polynomial_test ( )
  w_polynomial_01_values_test ( )
  w_polynomial_ab_test ( )
  w_polynomial_ab_value_test ( )
  w_polynomial_coefficients_test ( )
  w_polynomial_plot_test ( )
  w_polynomial_value_test ( )
  w_polynomial_values_test ( )
  w_polynomial_zeros_test ( )
  w_quadrature_rule_test ( )
  ww_product_integral_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'chebyshev_polynomial_test():' )
  print ( '  Normal end of execution.' )
  return

def hyper_2f1_values ( n_data ):

#*****************************************************************************80
#
## hyper_2f1_values() returns some values of the hypergeometric 2F1 function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      fx = Hypergeometric2F1 [ a, b, c, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
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
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Cambridge University Press, 1999,
#    ISBN: 0-521-64314-7,
#    LC: QA76.95.W65.
#
#    Daniel Zwillinger, editor,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996,
#    ISBN: 0-8493-2479-3,
#    LC: QA47.M315.
#
#  Input:
#
#    integer N_DATA.  The user sets N_DATA to 0 before the first call.  
#
#  Output:
#
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real A, B, C, X, the parameters.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 24

  a_vec = np.array ( ( \
   -2.5, \
   -0.5, \
    0.5, \
    2.5, \
   -2.5, \
   -0.5, \
    0.5, \
    2.5, \
   -2.5, \
   -0.5, \
    0.5, \
    2.5, \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    3.3, \
    1.1, \
    1.1, \
    3.3 ))

  b_vec = np.array ( ( \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    3.3, \
    1.1, \
    1.1, \
    3.3, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7 ))

  c_vec = np.array ( ( \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
    6.7, \
   -5.5, \
   -0.5, \
    0.5, \
    4.5, \
   -5.5, \
   -0.5, \
    0.5, \
    4.5, \
   -5.5, \
   -0.5, \
    0.5, \
    4.5 ))

  f_vec = np.array ( ( \
    0.72356129348997784913, \
    0.97911109345277961340, \
    1.0216578140088564160, \
    1.4051563200112126405, \
    0.46961431639821611095, \
    0.95296194977446325454, \
    1.0512814213947987916, \
    2.3999062904777858999, \
    0.29106095928414718320, \
    0.92536967910373175753, \
    1.0865504094806997287, \
    5.7381565526189046578, \
    15090.669748704606754, \
   -104.31170067364349677, \
    21.175050707768812938, \
    4.1946915819031922850, \
    1.0170777974048815592E+10, \
   -24708.635322489155868, \
    1372.2304548384989560, \
    58.092728706394652211, \
    5.8682087615124176162E+18, \
   -4.4635010147295996680E+08, \
    5.3835057561295731310E+06, \
    20396.913776019659426 ))

  x_vec = np.array ( ( \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.55, \
    0.55, \
    0.55, \
    0.55, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.25, \
    0.25, \
    0.25, \
    0.25, \
    0.55, \
    0.55, \
    0.55, \
    0.55, \
    0.85, \
    0.85, \
    0.85, \
    0.85 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0
    b = 0
    c = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    b = b_vec[n_data]
    c = c_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, b, c, x, f

def hyper_2f1_values_test ( ):

#*****************************************************************************80
#
## hyper_2f1_values_test() tests hyper_2f1_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'hyper_2f1_values_test():' )
  print ( '  hyper_2f1_values() stores values of the hypergeometric function 2F1' )
  print ( '' )
  print ( '     A     B        C           X               F' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, a, b, c, x, f = hyper_2f1_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %4d  %4d  %12f  %12f  %24.16g' % ( a, b, c, x, f ) )

  print ( '' )
  print ( 'hyper_2f1_values_test():' )
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
  import platform

  print ( '' )
  print ( 'imtqlx_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
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

def psi_values ( n_data ):

#*****************************************************************************80
#
## psi_values() returns some values of the Psi or Digamma function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      PolyGamma[x]
#
#    or
#
#      PolyGamma[0,x]
#
#    PSI(X) = d ln ( Gamma ( X ) ) / d X = Gamma'(X) / Gamma(X)
#
#    PSI(1) = -Euler's constant.
#
#    PSI(X+1) = PSI(X) + 1 / X.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
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
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    real X, the argument of the function.
#
#    real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
    -10.42375494041108E+00, \
     -5.289039896592188E+00, \
     -3.502524222200133E+00, \
     -2.561384544585116E+00, \
     -1.963510026021423E+00, \
     -1.540619213893190E+00, \
     -1.220023553697935E+00, \
     -0.9650085667061385E+00, \
     -0.7549269499470514E+00, \
     -0.5772156649015329E+00, \
     -0.4237549404110768E+00, \
     -0.2890398965921883E+00, \
     -0.1691908888667997E+00, \
     -0.6138454458511615E-01, \
      0.3648997397857652E-01, \
      0.1260474527734763E+00, \
      0.2085478748734940E+00, \
      0.2849914332938615E+00, \
      0.3561841611640597E+00, \
      0.4227843350984671E+00 ))

  x_vec = np.array ( ( \
     0.1E+00, \
     0.2E+00, \
     0.3E+00, \
     0.4E+00, \
     0.5E+00, \
     0.6E+00, \
     0.7E+00, \
     0.8E+00, \
     0.9E+00, \
     1.0E+00, \
     1.1E+00, \
     1.2E+00, \
     1.3E+00, \
     1.4E+00, \
     1.5E+00, \
     1.6E+00, \
     1.7E+00, \
     1.8E+00, \
     1.9E+00, \
     2.0E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def psi_values_test ( ):

#*****************************************************************************80
#
## psi_values_test() tests psi_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'psi_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  psi_values() stores values of the PSI function.' )
  print ( '' )
  print ( '      X         PSI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )

  return

def r8_hyper_2f1 ( a, b, c, x ):

#*****************************************************************************80
#
## r8_hyper_2f1() evaluates the hypergeometric function F(A,B,C,X).
#
#  Discussion:
#
#    A minor bug was corrected.  The HW variable, used in several places as
#    the "old" value of a quantity being iteratively improved, was not
#    being initialized.  JVB, 11 February 2008.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    Original FORTRAN77 version by Shanjie Zhang, Jianming Jin.
#    This version by John Burkardt.
#
#  Reference:
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45
#
#  Input:
#
#    real A, B, C, X, the arguments of the function.
#    C must not be equal to a nonpositive integer.
#    X < 1.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  from scipy.special import gamma
  import numpy as np

  el = 0.5772156649015329

  l0 = ( c == int ( c ) ) and ( c < 0.0 )
  l1 = ( 1.0 - x < 1.0E-15 ) and ( c - a - b <= 0.0 )
  l2 = ( a == int ( a ) ) and ( a < 0.0 )
  l3 = ( b == int ( b ) ) and ( b < 0.0 )
  l4 = ( c - a == int ( c - a ) ) and ( c - a <= 0.0 )
  l5 = ( c - b == int ( c - b ) ) and ( c - b <= 0.0 )

  if ( l0 ):
    print ( '' )
    print ( 'r8_hyper_2f1 - Fatal error!' )
    print ( '  The hypergeometric series is divergent.' )
    print ( '  C is integral and negative.' )
    print ( '  C = %f' % ( c ) )

  if ( l1 ):
    print ( '' )
    print ( 'r8_hyper_2f1 - Fatal error!' )
    print ( '  The hypergeometric series is divergent.' )
    print ( '  1 = X < 0, C - A - B <= 0.' )
    print ( '  A = %f' % ( a ) )
    print ( '  B = %f' % ( b ) )
    print ( '  C = %f' % ( c ) )
    print ( '  X = %f' % ( x ) )

  if ( 0.95 < x ):
    eps = 1.0E-08
  else:
    eps = 1.0E-15

  if ( x == 0.0 or a == 0.0 or b == 0.0 ):

    value = 1.0
    return value

  elif ( 1.0 - x == eps and 0.0 < c - a - b ):

    gc = gamma ( c )
    gcab = gamma ( c - a - b )
    gca = gamma ( c - a )
    gcb = gamma ( c - b )
    value = gc * gcab / ( gca * gcb )
    return value

  elif ( 1.0 + x <= eps and abs ( c - a + b - 1.0 ) <= eps ):

    g0 = np.sqrt ( np.pi ) * 2.0 ** ( - a )
    g1 = gamma ( c )
    g2 = gamma ( 1.0 + a / 2.0 - b )
    g3 = gamma ( 0.5 + 0.5 * a )
    value = g0 * g1 / ( g2 * g3 )
    return value

  elif ( l2 or l3 ):

    if ( l2 ):
      nm = int ( abs ( a ) )

    if ( l3 ):
      nm = int ( abs ( b ) )

    value = 1.0
    r = 1.0

    for k in range ( 1, nm + 1 ):
      r = r * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
        / ( float ( k ) * ( c + float ( k ) - 1.0 ) ) * x
      value = value + r

    return value

  elif ( l4 or l5 ):

    if ( l4 ):
      nm = int ( abs ( c - a ) )
 
    if ( l5 ):
      nm = int ( abs ( c - b ) )

    value = 1.0
    r  = 1.0
    for k in range ( 1, nm + 1 ):
      r = r * ( c - a + float ( k ) - 1.0 ) * ( c - b + float ( k ) - 1.0 ) \
        / ( float ( k ) * ( c + float ( k ) - 1.0 ) ) * x
      value = value + r
    value = ( 1.0 - x ) ** ( c - a - b ) * hf
    return value

  aa = a
  bb = b
  x1 = x

  if ( x < 0.0 ):
    x = x / ( x - 1.0 )
    if ( a < c and b < a and 0.0 < b ):
      a = bb
      b = aa
    b = c - b

  if ( 0.75 <= x ):

    gm = 0.0

    if ( abs ( c - a - b - int ( c - a - b ) ) < 1.0E-15 ):

      m = int ( c - a - b )
      ga = gamma ( a )
      gb = gamma ( b )
      gc = gamma ( c )
      gam = gamma ( a + float ( m ) )
      gbm = gamma ( b + float ( m ) )

      pa = r8_psi ( a )
      pb = r8_psi ( b )

      if ( m != 0 ):
        gm = 1.0

      for j in range ( 1, abs ( m ) ):
        gm = gm * float ( j )

      rm = 1.0
      for j in range ( 1, abs ( m ) + 1 ):
        rm = rm * float ( j )
 
      f0 = 1.0
      r0 = 1.0
      r1 = 1.0
      sp0 = 0.0
      sp = 0.0

      if ( 0 <= m ):

        c0 = gm * gc / ( gam * gbm )
        c1 = - gc * ( x - 1.0 ) ** m / ( ga * gb * rm )

        for k in range ( 1, m ):
          r0 = r0 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
            / float ( k * ( k - m ) ) * ( 1.0 - x )
          f0 = f0 + r0
 
        for k in range ( 1, m + 1 ):
          sp0 = sp0 + 1.0 / ( a + float ( k ) - 1.0 ) \
            + 1.0 / ( b + float ( k ) - 1.0 ) - 1.0 / float ( k )

        f1 = pa + pb + sp0 + 2.0 * el + np.log ( 1.0 - x )
        hw = f1

        for k in range ( 1, 251 ):

          sp = sp + ( 1.0 - a ) / ( float ( k ) * ( a + float ( k ) - 1.0 ) ) \
            + ( 1.0 - b ) / ( float ( k ) * ( b + float ( k ) - 1.0 ) )

          sm = 0.0
          for j in range ( 1, m + 1 ):
            sm = sm + ( 1.0 - a ) \
              / ( float ( j + k ) * ( a + float ( j + k ) - 1.0 ) ) \
              + 1.0 / ( b + float ( j + k ) - 1.0 )

          rp = pa + pb + 2.0 * el + sp + sm + np.log ( 1.0 - x )

          r1 = r1 * ( a + m + float ( k ) - 1.0 ) * ( b + m + float ( k ) - 1.0 ) \
            / ( float ( k ) * float ( m + k ) ) * ( 1.0 - x )

          f1 = f1 + r1 * rp

          if ( abs ( f1 - hw ) < abs ( f1 ) * eps ):
            break
 
          hw = f1

        value = f0 * c0 + f1 * c1

      elif ( m < 0 ):

        m = - m
        c0 = gm * gc / ( ga * gb * ( 1.0 - x ) ** m )
        c1 = - ( - 1 ) ** m * gc / ( gam * gbm * rm )

        for k in range ( 1, m ):
          r0 = r0 * ( a - float ( m ) + float ( k ) - 1.0 ) \
            * ( b - float ( m ) + float ( k ) - 1.0 ) \
            / ( float ( k ) * float ( k - m ) ) * ( 1.0 - x )
          f0 = f0 + r0

        for k in range ( 1, m + 1 ):
          sp0 = sp0 + 1.0 / float ( k )

        f1 = pa + pb - sp0 + 2.0 * el + np.log ( 1.0 - x )
        hw = f1

        for k in range ( 1, 251 ):

          sp = sp + ( 1.0 - a ) \
            / ( float ( k ) * ( a + float ( k ) - 1.0 ) ) \
            + ( 1.0 - b ) / ( float ( k ) * ( b + float ( k ) - 1.0 ) )

          sm = 0.0
          for j in range ( 1, m + 1 ):
            sm = sm + 1.0 / float ( j + k )

          rp = pa + pb + 2.0 * el + sp - sm + np.log ( 1.0 - x )

          r1 = r1 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
            / float ( k * ( m + k ) ) * ( 1.0 - x )

          f1 = f1 + r1 * rp

          if ( abs ( f1 - hw ) < abs ( f1 ) * eps ):
            break

          hw = f1

        value = f0 * c0 + f1 * c1

    else:

      ga = gamma ( a )
      gb = gamma ( b )
      gc = gamma ( c )
      gca = gamma ( c - a )
      gcb = gamma ( c - b )
      gcab = gamma ( c - a - b )
      gabc = gamma ( a + b - c )
      c0 = gc * gcab / ( gca * gcb )
      c1 = gc * gabc / ( ga * gb ) * ( 1.0 - x ) ** ( c - a - b )
      value = 0.0
      hw = value
      r0 = c0
      r1 = c1

      for k in range ( 1, 251 ):

        r0 = r0 * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
          / ( float ( k ) * ( a + b - c + float ( k ) ) ) * ( 1.0 - x )

        r1 = r1 * ( c - a + float ( k ) - 1.0 ) \
          * ( c - b + float ( k ) - 1.0 ) \
          / ( float ( k ) * ( c - a - b + float ( k ) ) ) * ( 1.0 - x )

        value = value + r0 + r1

        if ( abs ( value - hw ) < abs ( value ) * eps ):
          break

        hw = value

      value = value + c0 + c1

  else:

    a0 = 1.0

    if ( a < c and c < 2.0 * a and b < c and c < 2.0 * b ):

      a0 = ( 1.0 - x ) ** ( c - a - b )
      a = c - a
      b = c - b

    value = 1.0
    hw = value
    r = 1.0

    for k in range ( 1, 251 ):

      r = r * ( a + float ( k ) - 1.0 ) * ( b + float ( k ) - 1.0 ) \
        / ( k * ( c + float ( k ) - 1.0 ) ) * x

      value = value + r

      if ( abs ( value - hw ) <= abs ( value ) * eps ):
        break

      hw = value

    value = a0 * value

  if ( x1 < 0.0 ):
    x = x1
    c0 = 1.0 / ( 1.0 - x ) ** aa
    value = c0 * value

  if ( 120 < k ):
    print ( '' )
    print ( 'r8_hyper_2f1 - Warning!' )
    print ( '  A large number of iterations were needed.' )
    print ( '  The accuracy of the results should be checked.' )

  return value

def r8_hyper_2f1_test ( ):

#*****************************************************************************80
#
## r8_hyper_2f1_test() tests r8_hyper_2f1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8_hyper_2f1_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_hyper_2f1() evaluates the hypergeometric 2F1 function.' )
  print ( '' )
  print ( '      A       B       C       X       2F1                       2F1                     DIFF' )
  print ( '                                     ' )
  print ( '(tabulated)               (computed)' )
  print ( '' )

  n_data = 0

  while ( True ):

    [ n_data, a, b, c, x, fx1 ] = hyper_2f1_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_hyper_2f1 ( a, b, c, x )
 
    diff = abs ( fx1 - fx2 )
    print ( '  %6g  %6g  %6g  %6g  %24g  %24g  %10g' \
      % ( a, b, c, x, fx1, fx2, diff ) )

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

def r8_mop ( i ):

#*****************************************************************************80
#
## r8_mop() returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the power of -1.
#
#  Output:
#
#    real r8_mop, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( ):

#*****************************************************************************80
#
## r8_mop_test() tests r8_mop().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'r8_mop_test():' )
  print ( '  r8_mop() evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  r8_mop(I4)' )
  print ( '' )

  i4_min = -100
  i4_max = +100

  for test in range ( 0, 10 ):
    i4 = rng.integers ( low = i4_min, high = i4_max, endpoint = True )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )

  return

def r8poly_print ( m, a, title ):

#*****************************************************************************80
#
## r8poly_print() prints a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the nominal degree of the polynomial.
#
#    real A[0:M], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    string TITLE, a title.
#
  if ( 0 < len ( title ) ):
    print ( '' )
    print ( title )
  print ( '' )

  if ( a[m] < 0.0 ):
    plus_minus = '-'
  else:
    plus_minus = ' '

  mag = abs ( a[m] )

  if ( 2 <= m ):
    print ( '  p(x) = %c %g * x^%d' % ( plus_minus, mag, m ) )
  elif ( m == 1 ):
    print ( '  p(x) = %c %g * x' % ( plus_minus, mag ) )
  elif ( m == 0 ):
    print ( '  p(x) = %c %g' % ( plus_minus, mag ) )

  for i in range ( m - 1, -1, -1 ):

    if ( a[i] < 0.0 ):
      plus_minus = '-'
    else:
      plus_minus = '+'

    mag = abs ( a[i] )

    if ( mag != 0.0 ):

      if ( 2 <= i ):
        print ( '         %c %g * x^%d' % ( plus_minus, mag, i ) )
      elif ( i == 1 ):
        print ( '         %c %g * x' % ( plus_minus, mag ) )
      elif ( i == 0 ):
        print ( '         %c %g' % ( plus_minus, mag ) )

def r8poly_print_test ( ):

#*****************************************************************************80
#
## r8poly_print_test() tests r8poly_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8poly_print_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8poly_print() prints an R8POLY.' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )

  r8poly_print ( m, c, '  The R8POLY:' )

  return

def r8_psi ( x ):

#*****************************************************************************80
#
## r8_psi() evaluates the function Psi(X).
#
#  Discussion:
#
#    This routine evaluates the logarithmic derivative of the
#    Gamma function,
#
#      PSI(X) = d/dX ( GAMMA(X) ) / GAMMA(X)
#             = d/dX LN ( GAMMA(X) )
#
#    for real X, where either
#
#      - XMAX1 < X < - XMIN, and X is not a negative integer,
#
#    or
#
#      XMIN < X.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    Original FORTRAN77 version by William Cody.
#    This version by John Burkardt.
#
#  Reference:
#
#    William Cody, Anthony Strecok, Henry Thacher,
#    Chebyshev Approximations for the Psi Function,
#    Mathematics of Computation,
#    Volume 27, Number 121, January 1973, pages 123-127.
#
#  Input:
#
#    real X, the argument of the function.
#
#  Output:
#
#    real VALUE, the value of the function.
#
  import numpy as np

  p1 = np.array ( ( \
   4.5104681245762934160E-03, \
   5.4932855833000385356, \
   3.7646693175929276856E+02, \
   7.9525490849151998065E+03, \
   7.1451595818951933210E+04, \
   3.0655976301987365674E+05, \
   6.3606997788964458797E+05, \
   5.8041312783537569993E+05, \
   1.6585695029761022321E+05 ))

  p2 = np.array ( ( \
  -2.7103228277757834192, \
  -1.5166271776896121383E+01, \
  -1.9784554148719218667E+01, \
  -8.8100958828312219821, \
  -1.4479614616899842986, \
  -7.3689600332394549911E-02, \
  -6.5135387732718171306E-21 ))

  piov4 = 0.78539816339744830962

  q1 = np.array ( ( \
   9.6141654774222358525E+01, \
   2.6287715790581193330E+03, \
   2.9862497022250277920E+04, \
   1.6206566091533671639E+05, \
   4.3487880712768329037E+05, \
   5.4256384537269993733E+05, \
   2.4242185002017985252E+05, \
   6.4155223783576225996E-08 ))

  q2 = np.array ( ( \
   4.4992760373789365846E+01, \
   2.0240955312679931159E+02, \
   2.4736979003315290057E+02, \
   1.0742543875702278326E+02, \
   1.7463965060678569906E+01, \
   8.8427520398873480342E-01 ))

  x01 = 187.0
  x01d = 128.0
  x02 = 6.9464496836234126266E-04
  xinf = 1.70E+38
  xlarge = 2.04E+15
  xmax1 = 3.60E+16
  xmin1 = 5.89E-39
  xsmall = 2.05E-09

  w = abs ( x )
  aug = 0.0
#
#  Check for valid arguments, then branch to appropriate algorithm.
#
  if ( xmax1 <= - x or w < xmin1 ):

    if ( 0.0 < x ):
      value = - xinf
    else:
      value = xinf;

    return value

  if ( x < 0.5 ):
#
#  X < 0.5, use reflection formula: psi(1-x) = psi(x) + pi * cot(pi*x)
#  Use 1/X for PI*COTAN(PI*X)  when  XMIN1 < |X| <= XSMALL.
#
    if ( w <= xsmall ):

      aug = - 1.0 / x
#
#  Argument reduction for cotangent.
#
    else:

      if ( x < 0.0 ):
        sgn = piov4
      else:
        sgn = - piov4

      w = w - int ( w )
      nq = int ( w * 4.0 )
      w = 4.0 * ( w - float ( nq ) * 0.25 )
#
#  W is now related to the fractional part of 4.0 * X.
#  Adjust argument to correspond to values in the first
#  quadrant and determine the sign.
#
      n = ( nq // 2 )

      if ( n + n != nq ):
        w = 1.0 - w

      z = piov4 * w

      if ( ( n % 2 ) != 0 ):
        sgn = - sgn
#
#  Determine the final value for  -pi * cotan(pi*x).
#
      n = ( ( nq + 1 ) // 2 )
      if ( ( n % 2 ) == 0 ):
#
#  Check for singularity.
#
        if ( z == 0.0 ):

          if ( 0.0 < x ):
            value = - xinf
          else:
            value = xinf

          return value

        aug = sgn * ( 4.0 / np.tan ( z ) )

      else:

        aug = sgn * ( 4.0 * np.tan ( z ) )

    x = 1.0 - x
#
#  0.5 <= X <= 3.0.
#
  if ( x <= 3.0 ):

    den = x
    upper = p1[0] * x
    for i in range ( 0, 7 ):
      den = ( den + q1[i] ) * x
      upper = ( upper + p1[i+1] ) * x

    den = ( upper + p1[8] ) / ( den + q1[7] )
    x = ( x - x01 / x01d ) - x02
    value = den * x + aug
    return value
#
#  3.0 < X.
#
  if ( x < xlarge ):
    w = 1.0 / ( x * x )
    den = w
    upper = p2[0] * w
    for i in range ( 0, 5 ):
      den = ( den + q2[i] ) * w
      upper = ( upper + p2[i+1] ) * w
    aug = ( upper + p2[6] ) / ( den + q2[5] ) - 0.5 / x + aug

  value = aug + np.log ( x )

  return value

def r8_psi_test ( ):

#*****************************************************************************80
#
## r8_psi_test() tests r8_psi().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'r8_psi_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8_psi() evaluates the PSI function.' )
  print ( '' )
  print ( '      X            PSI(X)    r8_psi(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_psi ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )

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

def r8vec2_print_test ( ):

#*****************************************************************************80
#
## r8vec2_print_test() tests r8vec2_print().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec2_print_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  r8vec2_print() prints a pair of R8VEC\'s.' )

  n = 6
  v = np.array ( [ 0.0, 0.20, 0.40, 0.60, 0.80, 1.0 ], dtype = np.float64 )
  w = np.array ( [ 0.0, 0.04, 0.16, 0.36, 0.64, 1.0 ], dtype = np.float64 )
  r8vec2_print ( n, v, w, '  Print a pair of R8VEC\'s:' )

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

  return

def t_mass_matrix ( n ):

#*****************************************************************************80
#
## t_mass_matrix() computes the mass matrix for the Chebyshev T polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#  Output:
#
#    real A[N+1,N+1], the mass matrix.
#
  import numpy as np

  x, w = t_quadrature_rule ( n + 1 )

  phi = t_polynomial ( n + 1, n, x )

  phiw = np.zeros ( [ n + 1, n + 1 ] )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      phiw[j,i] = w[i] * phi[i,j]

  a = np.dot ( phiw, phi )

  return a

def t_mass_matrix_test ( ):

#*****************************************************************************80
#
## t_mass_matrix_test() tests t_mass_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 't_mass_matrix_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  t_mass_matrix() computes the mass matrix for the' )
  print ( '  Chebyshev T polynomials T(i,x).' )
  print ( '  A(I,J) = integral ( -1 <=x <= +1 ) T(i,x) T(j,x) / sqrt ( 1 - x^2 ) dx' )
  print ( '  0    if i is not equal to j' )
  print ( '  pi   if i = j = 0' )
  print ( '  pi/2 if i = j =/= 0.' )

  n = 3

  a = t_mass_matrix ( n )

  r8mat_print ( n + 1, n + 1, a, '  T mass matrix:' )

  return

def t_moment ( e ):

#*****************************************************************************80
#
## t_moment(): integral ( -1 <= x <= +1 ) x^e dx / sqrt ( 1 - x^2 ).
#
#  Discussion:
#
#    Set 
#      x = cos ( theta ), 
#      dx = - sin ( theta ) d theta = - sqrt ( 1 - x^2 ) d theta
#    to transform the integral to
#      integral ( 0 <= theta <= pi ) - ( cos ( theta ) )^e d theta
#    which becomes
#      0 if E is odd,
#      (1/2^e) * choose ( e, e/2 ) * pi if E is even.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer E, the exponent of X.
#    0 <= E.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import comb
  import numpy as np

  if ( ( e % 2 ) == 1 ):

    value = 0.0

  else:

    value = comb ( e, e // 2 ) * np.pi / 2.0 ** e

  return value

def t_moment_test ( ):

#*****************************************************************************80
#
## t_moment_test() tests t_moment().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 't_moment_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  t_moment() returns the value of' )
  print ( '  integral ( -1 <=x <= +1 ) x^e / sqrt ( 1 - x^2 ) dx' )
  print ( '' )
  print ( '   E       Integral' )
  print ( '' )
  for e in range ( 0, 11 ):
    value = t_moment( e )
    print ( '  %2d  %14.6g' % ( e, value ) )

  return

def t_polynomial_01_values ( n_data ):

#*****************************************************************************80
#
## t_polynomial_01_values(): values of shifted Chebyshev polynomials T01(n,x).
#
#  Discussion:
#
#    T01(n,x) = T(n,2*x-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 July 2015
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
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 25

  fx_vec = np.array ( ( \
     0.0000000000000000, \
     1.0000000000000000, \
     0.7000000000000000, \
    -0.0200000000000000, \
    -0.7280000000000000, \
    -0.9992000000000000, \
    -0.6708800000000000, \
     0.0599680000000000, \
     0.7548352000000000, \
     0.9968012800000000, \
     0.6406865920000000, \
    -0.0998400512000000, \
    -0.7804626636800000, \
    -0.9928076779520000, \
    -1.0000000000000000, \
     0.2063872000000000, \
    -0.9784704000000000, \
     0.2580224000000000, \
     0.9870208000000000, \
     0.0000000000000000, \
    -0.9870208000000000, \
    -0.2580224000000000, \
     0.9784704000000000, \
    -0.2063872000000000, \
     1.0000000000000000 ) )

  n_vec = np.array ( ( \
    -1, \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  7,  7, \
     7,  7,  7, \
     7,  7,  7, \
     7,  7,  7 ))

  x_vec = np.array ( ( \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.00, \
    0.10, \
    0.20, \
    0.30, \
    0.40, \
    0.50, \
    0.60, \
    0.70, \
    0.80, \
    0.90, \
    1.00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def t_polynomial_01_values_test ( ):

#*****************************************************************************80
#
## t_polynomial_01_values_test() tests t_polynomial_01_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 't_polynomial_01_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  t_polynomial_01_values() stores values of the shifted Chebyshev T polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = t_polynomial_01_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )

  return

def t_polynomial_ab ( a, b, m, n, xab ):

#*****************************************************************************80
#
## t_polynomial_ab(): Chebyshev polynomials TAB(N,X) in [A,B].
#
#  Discussion:
#
#    TAB(n,x) = T(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the domain of definition.
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest polynomial to compute.
#
#    real XAB(M,1), the evaluation points.
#    It must be the case that A <= XAB(*) <= B.
#
#  Output:
#
#    real V(M,N+1), the values of the Chebyshev polynomials.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = t_polynomial ( m, n, x );
 
  return v

def t_polynomial_ab_test ( ):

#*****************************************************************************80
#
## t_polynomial_ab_test() tests t_polynomial_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 't_polynomial_ab_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  t_polynomial_ab() evaluates Chebyshev polynomials TAB(n,x)' )
  print ( '  shifted from [-1,+1] to the domain [A,B].' )
  print ( '' )
  print ( '  Here, we will use the new domain [0,1]' )
  print ( '  and the desired maximum polynomial degree will be N = 5.' )

  a = 0.0
  b = 1.0
  m = 11
  n = 5
  x = np.linspace ( a, b, m )
  
  v = t_polynomial_ab ( a, b, m, n, x )

  r8mat_print ( m, n + 1, v, '  Tables of T values:' )

  return

def t_polynomial_ab_value ( a, b, n, xab ):

#*****************************************************************************80
#
## t_polynomial_ab_value() Chebyshev polynomial TAB(N,X) in [A,B].
#
#  Discussion:
#
#    TAB(n,x) = T(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the domain of definition.
#
#    integer N, the degree of the polynomial.
#
#    real XAB, the evaluation points.
#    A <= XAB <= B.
#
#  Output:
#
#    real V, the value.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = t_polynomial_value ( n, x );
 
  return v

def t_polynomial_ab_value_test ( ):

#*****************************************************************************80
#
## t_polynomial_ab_value_test() tests t_polynomial_ab_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 't_polynomial_ab_value_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  t_polynomial_ab_value() evaluates a Chebyshev polynomial TAB(n,x)' )
  print ( '  shifted from [-1,+1] to the domain [A,B].' )
  print ( '' )
  print ( '  Here, we will use the new domain [0,1].' )
  print ( '' )
  print ( '                    Tabulated     Computed' )
  print ( '     N      X        T01(n,x)      T01(n,x)' )
  print ( '' )

  a = 0.0
  b = 1.0

  n_data = 0

  while ( True ):

    n_data, n, x01, fx = t_polynomial_01_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = t_polynomial_ab_value ( a, b, n, x01 )

    print ( '  %8d  %8.4f  %14.6g  %14.6g' % ( n, x01, fx, fx2 ) )

  return

def t_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## t_polynomial_coefficients(): coefficients of the Chebyshev polynomial T(n,x).
#
#  First terms:
#
#    N/K     0     1      2      3       4     5      6    7      8    9   10
#
#     0      1
#     1      0     1
#     2     -1     0      2
#     3      0    -3      0      4
#     4      1     0     -8      0       8
#     5      0     5      0    -20       0    16
#     6     -1     0     18      0     -48     0     32
#     7      0    -7      0     56       0  -112      0    64
#
#  Recursion:
#
#    T(0,X) = 1,
#    T(1,X) = X,
#    T(N,X) = 2 * X * T(N-1,X) - T(N-2,X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
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
#  Input:
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#  Output:
#
#    real C(1:N+1,1:N+1), the coefficients of the Chebyshev T
#    polynomials.
#
  import numpy as np

  c = np.zeros ( [ n + 1, n + 1 ] )

  c[0,0] = 1.0

  if ( 0 < n ):

    c[1,1] = 1.0
 
    for i in range ( 2, n + 1 ):
      c[i,0] = - c[i-2,0]
      for j in range ( 1, i - 1 ):
        c[i,j] = 2.0 * c[i-1,j-1] - c[i-2,j]
      c[i,i-1] = 2.0 * c[i-1,i-2]
      c[i,i] = 2.0 * c[i-1,i-1]
 
  return c

def t_polynomial_coefficients_test ( ):

#*****************************************************************************80
#
## t_polynomial_coefficients_test() tests t_polynomial_coefficients().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 't_polynomial_coefficients_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  t_polynomial_coefficients() determines the Chebyshev' )
  print ( '  polynomial coefficients.' )

  c = t_polynomial_coefficients ( n )
 
  for i in range ( 0, n + 1 ):
    c2 = np.zeros ( i + 1 )
    for j in range ( 0, i + 1 ):
      c2[j] = c[i,j]
    r8poly_print ( i, c2, '' )

  return

def t_polynomial_plot ( n_num, n_val, filename ):

#*****************************************************************************80
#
## t_polynomial_plot() plots Chebyshev polynomials T(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_NUM, the number of polynomials to plot.
#
#    integer N_VAL(N_NUM), the degree of each polynomial.
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

  for i in range ( 0, n_num ):
    n = n_val[i]
    y = t_polynomial ( m, n, x )
    plt.plot ( x, y, 'b-', linewidth = 2.0 )

  t = 'T(n,x), for n = '
  for i in range ( 0, n_num ):
    n = n_val[i]
    t = t + str ( n )
    if ( 1 < n_num and i < n_num - 1 ):
      t = t + ', '

  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---T(n,x)--->' )
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '  Created plot file "%s".' % ( filename ) )

  return

def t_polynomial_plot_test ( ):

#*****************************************************************************80
#
## t_polynomial_plot_test() tests t_polynomial_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 't_polynomial_plot_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  t_polynomial_plot() plots several Chebyshev T polynomials.' )

  n_num = 6
  n_val = np.array ( [ 0, 1, 2, 3, 4, 5 ], dtype = np.int32 )
  filename = 't_polynomial_plot.png'

  t_polynomial_plot ( n_num, n_val, filename )

  return

def t_polynomial ( m, n, x ):

#*****************************************************************************80
#
## t_polynomial() evaluates the Chebyshev polynomials T(N,X) of the first kind.
#
#  Discussion:
#
#    Chebyshev polynomials are useful as a basis for representing the
#    approximation of functions since they are well conditioned, in the sense
#    that in the interval [-1,1] they each have maximum absolute value 1.
#    Hence an error in the value of a coefficient of the approximation, of
#    size epsilon, is exactly reflected in an error of size epsilon between
#    the computed approximation and the theoretical approximation.
#
#    Typical usage is as follows, where we assume for the moment
#    that the interval of approximation is [-1,1].  The value
#    of N is chosen, the highest polynomial to be used in the
#    approximation.  Then the function to be approximated is
#    evaluated at the N+1 points XJ which are the zeroes of the N+1-th
#    Chebyshev polynomial.  Let these values be denoted by F(XJ).
#
#    The coefficients of the approximation are now defined by
#
#      C(I) = 2/(N+1) * sum ( 1 <= J <= N+1 ) F(XJ) T(I,XJ)
#
#    except that C(0) is given a value which is half that assigned
#    to it by the above formula,
#
#    and the representation is
#
#    F(X) approximated by sum ( 0 <= J <= N ) C(J) T(J,X)
#
#    Now note that, again because of the fact that the Chebyshev polynomials
#    have maximum absolute value 1, if the higher order terms of the
#    coefficients C are small, then we have the option of truncating
#    the approximation by dropping these terms, and we will have an
#    exact value for maximum perturbation to the approximation that
#    this will cause.
#
#    It should be noted that typically the error in approximation
#    is dominated by the first neglected basis function (some multiple of
#    T(N+1,X) in the example above).  If this term were the exact error,
#    then we would have found the minimax polynomial, the approximating
#    polynomial of smallest maximum deviation from the original function.
#    The minimax polynomial is hard to compute, and another important
#    feature of the Chebyshev approximation is that it tends to behave
#    like the minimax polynomial while being easy to compute.
#
#    To evaluate a sum like 
#
#      sum ( 0 <= J <= N ) C(J) T(J,X), 
#
#    Clenshaw's recurrence formula is recommended instead of computing the
#    polynomial values, forming the products and summing.
#
#    Assuming that the coefficients C(J) have been computed
#    for J = 0 to N, then the coefficients of the representation of the
#    indefinite integral of the function may be computed by
#
#      B(I) = ( C(I-1) - C(I+1))/2*(I-1) for I=1 to N+1, 
#
#    with
# 
#      C(N+1)=0
#      B(0) arbitrary.  
#
#    Also, the coefficients of the representation of the derivative of the 
#    function may be computed by:
#
#      D(I) = D(I+2)+2*I*C(I) for I=N-1, N-2, ..., 0, 
#
#    with
#
#      D(N+1) = D(N)=0.
#
#    Some of the above may have to adjusted because of the irregularity of C(0).
#
#  Differential equation:
#
#    (1-X*X) Y'' - X Y' + N N Y = 0
#
#  Formula:
#
#    T(N,X) = COS(N*ARCCOS(X))
#
#  First terms:
#
#    T(0,X) =  1
#    T(1,X) =  1 X
#    T(2,X) =  2 X^2 -   1
#    T(3,X) =  4 X^3 -   3 X
#    T(4,X) =  8 X^4 -   8 X^2 +  1
#    T(5,X) = 16 X^5 -  20 X^3 +  5 X
#    T(6,X) = 32 X^6 -  48 X^4 + 18 X^2 - 1
#    T(7,X) = 64 X^7 - 112 X^5 + 56 X^3 - 7 X
#
#  Inequality:
#
#    abs ( T(N,X) ) <= 1 for -1 <= X <= 1
#
#  Orthogonality:
#
#    For integration over [-1,1] with weight
#
#      W(X) = 1 / sqrt(1-X*X), 
#
#    if we write the inner product of T(I,X) and T(J,X) as
#
#      < T(I,X), T(J,X) > = integral ( -1 <= X <= 1 ) W(X) T(I,X) T(J,X) dX
#
#    then the result is:
#
#      0 if I /= J
#      PI/2 if I == J /= 0
#      PI if I == J == 0
#
#    A discrete orthogonality relation is also satisfied at each of
#    the N zeroes of T(N,X):  sum ( 1 <= K <= N ) T(I,X) * T(J,X)
#                              = 0 if I /= J
#                              = N/2 if I == J /= 0
#                              = N if I == J == 0
#
#  Recursion:
#
#    T(0,X) = 1,
#    T(1,X) = X,
#    T(N,X) = 2 * X * T(N-1,X) - T(N-2,X)
#
#    T'(N,X) = N * ( -X * T(N,X) + T(N-1,X) ) / ( 1 - X^2 )
#
#  Special values:
#
#    T(N,1) = 1
#    T(N,-1) = (-1)^N
#    T(2N,0) = (-1)^N
#    T(2N+1,0) = 0
#    T(N,X) = (-1)^N * T(N,-X)
#
#  Zeroes:
#
#    M-th zero of T(N,X) is cos((2*M-1)*PI/(2*N)), M = 1 to N
#
#  Extrema:
#
#    M-th extremum of T(N,X) is cos(PI*M/N), M = 0 to N
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 March 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest polynomial to compute.
#
#    real X(M,1), the evaluation points.
#
#  Output:
#
#    real V(1:M,1:N+1), the values of the Chebyshev polynomials 
#    0 through N at X(1:M).
#
  import numpy as np
 
  if ( n < 0 ):
    print ( '' )
    print ( 't_polynomial - Fatal error!' )
    print ( '  N < 0' )
    raise Exception ( 't_polynomial - Fatal error.' )

  v = np.zeros ( ( m, n + 1 ) )

  for i in range ( 0, m ):
    v[i,0] = 1.0

  if ( n < 1 ):
    return v

  for i in range ( 0, m ):
    v[i,1] = x[i]
 
  for i in range ( 0, m ):
    for j in range ( 2, n + 1 ):
      v[i,j] = 2.0 * x[i] * v[i,j-1] - v[i,j-2]
 
  return v

def t_polynomial_test ( ):

#*****************************************************************************80
#
## t_polynomial_test() tests t_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 't_polynomial_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  t_polynomial() evaluates the Chebyshev polynomial T(n,x).' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X           T(n,x)                    T(n,x)                     Error' )
  print ( '' )

  n_data = 0
  x_vec = np.zeros ( 1 )

  while ( True ):

    n_data, n, x, fx1 = t_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    if ( n < 0 ):
      continue

    x_vec[0] = x
    fx2_vec = t_polynomial ( 1, n, x_vec )
    fx2 = fx2_vec[0,n]
    e = fx1 - fx2

    print ( '  %4d  %12g  %24.16g  %24.16g  %8.2g' % ( n, x, fx1, fx2, e ) )

  return

def t_polynomial_value ( n, x ):

#*****************************************************************************80
#
## t_polynomial_value() returns the single value T(n,x).
#
#  Discussion:
#
#    In cases where calling t_polynomial is inconvenient, because it returns
#    a vector of values for multiple arguments X, this simpler interface
#    may be appropriate.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#    real X, the argument of the polynomial.
#
#  Output:
#
#    real VALUE, the value of T(n,x).
#
  import numpy as np

  if ( n < 0 ):
    value = 0.0
  else:
    m = 1
    x_vec = np.array ( [ x ] )
    v_vec = t_polynomial ( m, n, x_vec )
    value = v_vec[0,n]

  return value

def t_polynomial_value_test ( ):

#*****************************************************************************80
#
## t_polynomial_value_test() tests t_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 't_polynomial_value_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  t_polynomial_value() evaluates the Chebyshev polynomial T(n,x).' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X           T(n,x)                    T(n,x)                     Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx1 = t_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = t_polynomial_value ( n, x )
    e = fx1 - fx2

    print ( '  %4d  %12g  %24.16g  %24.16g  %8.2g' % ( n, x, fx1, fx2, e ) )

  return

def t_polynomial_values ( n_data ):

#*****************************************************************************80
#
## t_polynomial_values() returns values of Chebyshev polynomials T(n,x).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ChebyshevT[n,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 July 2015
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
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 14

  fx_vec = np.array ( ( \
      0.0000000000000000E+00, \
      0.1000000000000000E+01, \
      0.8000000000000000E+00, \
      0.2800000000000000E+00, \
     -0.3520000000000000E+00, \
     -0.8432000000000000E+00, \
     -0.9971200000000000E+00, \
     -0.7521920000000000E+00, \
     -0.2063872000000000E+00, \
      0.4219724800000000E+00, \
      0.8815431680000000E+00, \
      0.9884965888000000E+00, \
      0.7000513740800000E+00, \
      0.1315856097280000E+00 ) )

  n_vec = np.array ( ( \
    -1, \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12 ))

  x_vec = np.array ( ( \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def t_polynomial_values_test ( ):

#*****************************************************************************80
#
## t_polynomial_values_test() tests t_polynomial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 't_polynomial_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  t_polynomial_values() stores values of the Chebyshev T polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = t_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )

  return

def t_polynomial_zeros ( n ):

#*****************************************************************************80
#
## t_polynomial_zeros() returns zeroes of the Chebyshev polynomial T(n,x).
#
#  Discussion:
#
#    The I-th zero is cos((2*I-1)*PI/(2*N)), I = 1 to N
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#  Output:
#
#    real Z(N), the zeroes.
#
  import numpy as np

  z = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( 2 * i + 1 ) * np.pi / float ( 2 * n )
    z[i] = np.cos ( angle )

  return z

def t_polynomial_zeros_test ( ):

#*****************************************************************************80
#
## t_polynomial_zeros_test() tests t_polynomial_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 't_polynomial_zeros_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  t_polynomial_zeros() computes the zeros of T(n,x)' )
  print ( '' )
  print ( '     N      X         T(n,x)' )

  for n in range ( 0, 6 ):

    x = t_polynomial_zeros ( n )
    fx = t_polynomial ( n, n + 1, x )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %8.4g  %14.6g' % ( i, x[i], fx[i,n] ) )

  return

def t_quadrature_rule ( n ):

#*****************************************************************************80
#
## t_quadrature_rule() returns a quadrature rule for T(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real T(N), W(N), the points and weights of the rule.
#
  import numpy as np

  aj = np.zeros ( n )

  bj = np.ones ( n )
  for i in range ( 0, n ):
    bj[i] = 0.5 * bj[i]
  bj[0] = np.sqrt ( 0.5 )

  cj = np.zeros ( n )
  cj[0] = np.sqrt ( np.pi )

  t, w = imtqlx ( n, aj, bj, cj )

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return t, w

def t_quadrature_rule_test ( ):

#*****************************************************************************80
#
## t_quadrature_rule_test() tests t_quadrature_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 't_quadrature_rule_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  t_quadrature_rule() computes the quadrature rule' )
  print ( '  associated with T(n,x)' )

  n = 7
  x, w = t_quadrature_rule ( n )

  r8vec2_print ( n, x, w, '      X            W' )

  print ( '' )
  print ( '  Use the quadrature rule to estimate:' )
  print ( '' )
  print ( '    Q = Integral ( -1 <= X <= +1 ) X^E / sqrt ( 1-x^2) dx' )
  print ( '' )
  print ( '   E       Q_Estimate      Q_Exact' )
  print ( '' )

  f = np.zeros ( n )

  for e in range ( 0, 2 * n ):
    if ( e == 0 ):
      for i in range ( 0, n ):
        f[i] = 1.0
    else:
      for i in range ( 0, n ):
        f[i] = x[i] ** e

    q = np.dot ( w, f )
    q_exact = t_moment ( e )
    print ( '  %2d  %14g  %14g' % ( e, q, q_exact ) )

  return

def tt_product_integral ( i, j ):

#*****************************************************************************80
#
## tt_product_integral() evaluates integral (-1<=x<=1) T(i,x)*T(j,x)/sqrt(1-x^2) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the polynomial indices.
#    0 <= I, J.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  import numpy as np

  if ( i < 0 ):
    print ( '' )
    print ( 'tt_product_integral - Fatal error!' )
    print ( '  0 <= I is required.' )
    raise Exception ( 'tt_product_integral - Fatal error!' )

  if ( j < 0 ):
    print ( '' )
    print ( 'tt_product_integral - Fatal error!' )
    print ( '  0 <= J is required.' )
    raise Exception ( 'tt_product_integral - Fatal error!' )

  if ( i != j ):
    value = 0.0
  elif ( i == 0 ):
    value = np.pi
  elif ( 0 < i ):
    value = np.pi / 2.0

  return value

def tt_product_integral_test ( ):

#*****************************************************************************80
#
## tt_product_integral_test() tests tt_product_integral().
#
#  Discussion:
#
#    This process should match the t_mass_matrix computation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'tt_product_integral_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  tt_product_integral() computes the product integral' )
  print ( '  of a pair of Chebyshev T polynomials T(i,x) and T(j,x).' )
  print ( '  A(I,J) = integral ( -1 <=x <= +1 ) T(i,x) T(j,x) / sqrt ( 1 - x^2 ) dx' )
  print ( '  0    if i is not equal to j' )
  print ( '  pi   if i = j = 0' )
  print ( '  pi/2 if i = j =/= 0.' )

  n = 4
  a = np.zeros ( [ n + 1, n + 1 ] )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      a[i,j] = tt_product_integral ( i, j )

  r8mat_print ( n + 1, n + 1, a, '  T(i,x)*T(j,x) integral matrix:' )

  return

def tt_product ( i, j, x ):

#*****************************************************************************80
#
## tt_product() evaluates T(i,x)*T(j,x)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the indices.
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value.
#
  if ( i < 0 or j < 0 ):
    value = 0.0
  else:
    ipj = i + j
    tipj = t_polynomial_value ( ipj, x )
    imj = abs ( i - j )
    timj = t_polynomial_value ( imj, x )
    value = 0.5 * ( tipj + timj )

  return value

def tt_product_test ( ):

#*****************************************************************************80
#
## tt_product_test() tests tt_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'tt_product_test():' )
  print ( '  tt_product(I,J;X) = T(I,X) * T(J,X)' )

  r8_lo = -1.0
  r8_hi = +1.0

  print ( '' )
  print ( '   I   J      X               TI              TJ              TI*TJ       tt_product' )
  print ( '' )
  for test in range ( 0, 10 ):
    x = r8_lo + ( r8_hi - r8_lo ) * rng.random ( )
    i = rng.integers ( low = 0, high = 6, endpoint = True )
    ti = t_polynomial_value ( i, x )
    j = rng.integers ( low = -1, high = 4, endpoint = True )
    tj = t_polynomial_value ( j, x )
    titj = tt_product ( i, j, x )
    print ( '  %2d  %2d  %14.6g  %14.6g  %14.6g  %14.6g  %14.6g'\
      % ( i, j, x, ti, tj, ti * tj, titj ) )

  return

def ttt_product_integral ( i, j, k ):

#*****************************************************************************80
#
## ttt_product_integral(): integral (-1<=x<=1) T(i,x)*T(j,x)*T(k,x)/sqrt(1-x^2) dx
#
#  Discussion:
#
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Mason, David Handscomb,
#    Chebyshev Polynomials,
#    CRC Press, 2002,
#    ISBN: 0-8493-035509,
#    LC: QA404.5.M37.
#
#  Input:
#
#    integer I, J, K, the polynomial indices.
#    0 <= I, J.
#
#  Output:
#
#    real VALUE, the integral.
#
  if ( i < 0 ):
    value = 0.0
    return value

  if ( j < 0 ):
    value = 0.0
    return value

  if ( k < 0 ):
    value = 0.0
    return value

  value = 0.5 * ( \
      tt_product_integral (       i + j,   k ) + \
    + tt_product_integral ( abs ( i - j ), k ) )

  return value

def ttt_product_integral_test ( ):

#*****************************************************************************80
#
## ttt_product_integral_test() tests ttt_product_integral().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  test_num = 20

  print ( '' )
  print ( 'ttt_product_integral_test():' )
  print ( '  ttt_product_integral() computes the triple integral' )
  print ( '  Tijk = integral ( -1 <= x <= 1 ) T(i,x) T(j,x) T(k,x) / sqrt ( 1-x^2) dx' )
  print ( '' )
  print ( '   I   J   K     Tijk           Tijk' )
  print ( '                 computed       exact' )
  print ( '' )

  n = 15
  x, w = t_quadrature_rule ( n )

  for test in range ( 0, test_num ):
    i = rng.integers ( low = 2, high = 6, endpoint = True )
    j = rng.integers ( low = 1, high = 3, endpoint = True )
    k = rng.integers ( low = 0, high = 4, endpoint = True )
    fx1 = ttt_product_integral ( i, j, k )
    fx2 = 0.0
    for l in range ( 0, n ):
      ti = t_polynomial_value ( i, x[l] )
      tj = t_polynomial_value ( j, x[l] )
      tk = t_polynomial_value ( k, x[l] )
      fx2 = fx2 + w[l] * ti * tj * tk

    print ( '  %2d  %2d  %2d  %14.6g  %14.6g' % ( i, j, k, fx1, fx2 ) )

  return

def tu_product ( i, j, x ):

#*****************************************************************************80
#
## tu_product(): evaluate T(i,x)*U(j,x)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the indices.
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value.
#
  if ( i < 0 ):
    value = 0.0
  elif ( j < 0 ):
    value = 0.0
  elif ( i == 0 ):
    value = u_polynomial_value ( j, x )
  else:
    value = 0.5 * ( uu_product ( i, j, x ) - uu_product ( i - 2, j, x ) )

  return value

def tu_product_test ( ):

#*****************************************************************************80
#
## tu_product_test() tests tu_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 July 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'tu_product_test():' )
  print ( '  tu_product(I,J;X) = T(I,X) * U(J,X)' )

  r8_lo = -1.0
  r8_hi = +1.0

  print ( '' )
  print ( '   I   J      X               TI              UJ              TI*UJ       tu_product' )
  print ( '' )
  for test in range ( 0, 10 ):
    x = r8_lo + ( r8_hi - r8_lo ) * rng.random ( )
    i = rng.integers ( low = 0, high = 6, endpoint = True )
    ti = t_polynomial_value ( i, x )
    j = rng.integers ( low = -1, high = 4, endpoint = True )
    uj = u_polynomial_value ( j, x )
    tiuj = tu_product ( i, j, x )
    print ( '  %2d  %2d  %14.6g  %14.6g  %14.6g  %14.6g  %14.6g'\
      % ( i, j, x, ti, uj, ti * uj, tiuj ) )

  return

def u_mass_matrix ( n ):

#*****************************************************************************80
#
## u_mass_matrix() computes the mass matrix for the Chebyshev U polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#  Output:
#
#    real A[N+1,N+1], the mass matrix.
#
  import numpy as np

  x, w = u_quadrature_rule ( n + 1 )

  phi = u_polynomial ( n + 1, n, x )

  phiw = np.zeros ( [ n + 1, n + 1 ] )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      phiw[j,i] = w[i] * phi[i,j]

  a = np.dot ( phiw, phi )

  return a

def u_mass_matrix_test ( ):

#*****************************************************************************80
#
## u_mass_matrix_test() tests u_mass_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'u_mass_matrix_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  u_mass_matrix() computes the mass matrix for the' )
  print ( '  Chebyshev U polynomials U(i,x).' )
  print ( '  A(I,J) = integral ( -1 <=x <= +1 ) U(i,x) U(j,x) * sqrt ( 1 - x^2 ) dx' )
  print ( '  0    if i is not equal to j' )
  print ( '  pi/2 if i = j.' )

  n = 3

  a = u_mass_matrix ( n )

  r8mat_print ( n + 1, n + 1, a, '  U mass matrix:' )

  return

def u_moment ( e ):

#*****************************************************************************80
#
## u_moment(): integral ( -1 <= x <= +1 ) x^e sqrt ( 1 - x^2 ) dx.
#
#  Discussion:
#
#     E    u_moment
#    --    --------------  
#     0         pi /    2 
#     2         pi /    8
#     4         pi /   16
#     6     5 * pi /  128
#     8     7 * pi /  256
#    10    21 * pi / 1024
#    12    33 * pi / 2048
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer E, the exponent of X.
#    0 <= E.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import gamma
  import numpy as np

  if ( ( e % 2 ) == 1 ):

    value = 0.0

  else:

    arg1 = 0.5 * float ( 1 + e )
    arg2 = 2.0 + 0.5 * float ( e )
    value = 0.5 * np.sqrt ( np.pi ) * gamma ( arg1 ) / gamma ( arg2 )

  return value

def u_moment_test ( ):

#*****************************************************************************80
#
## u_moment_test() tests u_moment().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'u_moment_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  u_moment() returns the value of' )
  print ( '  integral ( -1 <=x <= +1 ) x^e * sqrt ( 1 - x^2 ) dx' )
  print ( '' )
  print ( '   E       Integral' )
  print ( '' )
  for e in range ( 0, 11 ):
    value = u_moment ( e )
    print ( '  %2d  %14.6g' % ( e, value ) )

  return

def u_polynomial_01_values ( n_data ):

#*****************************************************************************80
#
## u_polynomial_01_values(): values of shifted Chebyshev polynomials U01(n,x).
#
#  Discussion:
#
#    U01(n,x) = U(n,2*x-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 July 2015
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
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 25

  fx_vec = np.array ( ( \
     0.000000000000000, \
     1.000000000000000, \
     1.400000000000000, \
     0.9600000000000000, \
    -0.05600000000000000, \
    -1.038400000000000, \
    -1.397760000000000, \
    -0.9184640000000000, \
     0.1119104000000000, \
     1.075138560000000, \
     1.393283584000000, \
     0.8754584576000000, \
    -0.1676417433600000, \
    -1.110156898304000, \
    -8.000000000000000, \
     1.511014400000000, \
    -1.133260800000000, \
    -0.1636352000000000, \
     1.019801600000000, \
     0.000000000000000, \
    -1.019801600000000, \
     0.1636352000000000, \
     1.133260800000000, \
    -1.511014400000000, \
     8.000000000000000  ) )

  n_vec = np.array ( ( \
    -1, \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  7,  7, \
     7,  7,  7, \
     7,  7,  7, \
     7,  7,  7 ))

  x_vec = np.array ( ( \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.00, \
    0.10, \
    0.20, \
    0.30, \
    0.40, \
    0.50, \
    0.60, \
    0.70, \
    0.80, \
    0.90, \
    1.00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def u_polynomial_01_values_test ( ):

#*****************************************************************************80
#
## u_polynomial_01_values_test() tests u_polynomial_01_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'u_polynomial_01_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  u_polynomial_01_values() stores values of the shifted Chebyshev U polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = u_polynomial_01_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )

  return

def u_polynomial_ab ( a, b, m, n, xab ):

#*****************************************************************************80
#
## u_polynomial_ab(): Chebyshev polynomials UAB(N,X) in [A,B].
#
#  Discussion:
#
#    UAB(n,x) = U(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the domain of definition.
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest polynomial to compute.
#
#    real XAB(M,1), the evaluation points.
#    It must be the case that A <= XAB(*) <= B.
#
#  Output:
#
#    real V(M,N+1), the values of the Chebyshev polynomials.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = u_polynomial ( m, n, x );
 
  return v

def u_polynomial_ab_test ( ):

#*****************************************************************************80
#
## u_polynomial_ab_test() tests u_polynomial_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'u_polynomial_ab_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  u_polynomial_ab() evaluates Chebyshev polynomials UAB(n,x)' )
  print ( '  shifted from [-1,+1] to the domain [A,B].' )
  print ( '' )
  print ( '  Here, we will use the new domain [0,1]' )
  print ( '  and the desired maximum polynomial degree will be N = 5.' )

  a = 0.0
  b = 1.0
  m = 11
  n = 5
  x = np.linspace ( a, b, m )
  
  v = u_polynomial_ab ( a, b, m, n, x )

  r8mat_print ( m, n + 1, v, '  Tables of U values:' )

  return

def u_polynomial_ab_value ( a, b, n, xab ):

#*****************************************************************************80
#
## u_polynomial_ab_value(): Chebyshev polynomial UAB(N,X) in [A,B].
#
#  Discussion:
#
#    UAB(n,x) = U(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the domain of definition.
#
#    integer N, the degree of the polynomial.
#
#    real XAB, the evaluation points.
#    A <= XAB <= B.
#
#  Output:
#
#    real V, the value.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = u_polynomial_value ( n, x );
 
  return v

def u_polynomial_ab_value_test ( ):

#*****************************************************************************80
#
## u_polynomial_ab_value_test() tests u_polynomial_ab_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'u_polynomial_ab_value_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  u_polynomial_ab_value() evaluates a Chebyshev polynomial UAB(n,x)' )
  print ( '  shifted from [-1,+1] to the domain [A,B].' )
  print ( '' )
  print ( '  Here, we will use the new domain [0,1].' )
  print ( '' )
  print ( '                    Tabulated     Computed' )
  print ( '     N      X        U01(n,x)      U01(n,x)' )
  print ( '' )

  a = 0.0
  b = 1.0

  n_data = 0

  while ( True ):

    n_data, n, x01, fx = u_polynomial_01_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = u_polynomial_ab_value ( a, b, n, x01 )

    print ( '  %8d  %8.4f  %14.6g  %14.6g' % ( n, x01, fx, fx2 ) )

  return

def u_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## u_polynomial_coefficients(): coefficients of the Chebyshev polynomial U(n,x).
#
#  First terms:
#
#    N/K     0     1      2      3       4     5      6    7      8    9   10
#
#     0      1
#     1      0     2
#     2     -1     0      4
#     3      0    -4      0      8
#     4      1     0    -12      0      16
#     5      0     6      0    -32       0    32
#     6     -1     0     24      0     -80     0     64
#     7      0    -8      0     80       0  -192      0   128
#
#  Recursion:
#
#    U(0)(X) = 1,
#    U(1)(X) = 2*X,
#    U(N)(X) = 2 * X * U(N-1)(X) - U(N-2)(X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
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
#  Input:
#
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#  Output:
#
#    real C(1:N+1,1:N+1), the coefficients of the Chebyshev T
#    polynomials.
#
  import numpy as np

  c = np.zeros ( [ n + 1, n + 1 ] )

  c[0,0] = 1.0

  if ( 0 < n ):

    c[1,1] = 2.0
 
    for i in range ( 2, n + 1 ):
      c[i,0] = - c[i-2,0]
      for j in range ( 1, i - 1 ):
        c[i,j] = 2.0 * c[i-1,j-1] - c[i-2,j]
      c[i,i-1] = 2.0 * c[i-1,i-2]
      c[i,i] = 2.0 * c[i-1,i-1]
 
  return c

def u_polynomial_coefficients_test ( ):

#*****************************************************************************80
#
## u_polynomial_coefficients_test() tests u_polynomial_coefficients().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 5

  print ( '' )
  print ( 'u_polynomial_coefficients_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  u_polynomial_coefficients() determines the Chebyshev' )
  print ( '  polynomial coefficients.' )

  c = u_polynomial_coefficients ( n )
 
  for i in range ( 0, n + 1 ):
    c2 = np.zeros ( i + 1 )
    for j in range ( 0, i + 1 ):
      c2[j] = c[i,j]
    r8poly_print ( i, c2, '' )

  return

def u_polynomial_plot ( n_num, n_val, filename ):

#*****************************************************************************80
#
## u_polynomial_plot() plots Chebyshev polynomials U(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_NUM, the number of polynomials to plot.
#
#    integer N_VAL(N_NUM), the degree of each polynomial.
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

  for i in range ( 0, n_num ):
    n = n_val[i]
    y = u_polynomial ( m, n, x )
    plt.plot ( x, y, 'b-', linewidth = 2.0 )

  t = 'T(n,x), for n = '
  for i in range ( 0, n_num ):
    n = n_val[i]
    t = t + str ( n )
    if ( 1 < n_num and i < n_num - 1 ):
      t = t + ', '

  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---U(n,x)--->' )
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '  Created plot file "%s".' % ( filename ) )

  return

def u_polynomial_plot_test ( ):

#*****************************************************************************80
#
## u_polynomial_plot_test() tests u_polynomial_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'u_polynomial_plot_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  u_polynomial_plot() plots several Chebyshev U polynomials.' )

  n_num = 6
  n_val = np.array ( [ 0, 1, 2, 3, 4, 5 ] )
  filename = 'u_polynomial_plot.png'

  u_polynomial_plot ( n_num, n_val, filename )

  return

def u_polynomial ( m, n, x ):

#*****************************************************************************80
#
## u_polynomial() evaluates Chebyshev polynomials U(n,x).
#
#  Differential equation:
#
#    (1-X*X) Y'' - 3 X Y' + N (N+2) Y = 0
#
#  First terms:
#
#    U(0,X) =   1
#    U(1,X) =   2 X
#    U(2,X) =   4 X^2 -   1
#    U(3,X) =   8 X^3 -   4 X
#    U(4,X) =  16 X^4 -  12 X^2 +  1
#    U(5,X) =  32 X^5 -  32 X^3 +  6 X
#    U(6,X) =  64 X^6 -  80 X^4 + 24 X^2 - 1
#    U(7,X) = 128 X^7 - 192 X^5 + 80 X^3 - 8X
#
#  Recursion:
#
#    U(0,X) = 1,
#    U(1,X) = 2 * X,
#    U(N,X) = 2 * X * U(N-1,X) - U(N-2,X)
#
#  Norm:
#
#    Integral ( -1 <= X <= 1 ) ( 1 - X^2 ) * U(N,X)^2 dX = PI/2
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 April 2012
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest polynomial to compute.
#
#    real X(M,1), the evaluation points.
#
#  Output:
#
#    real V(1:M,1:N+1), the values of the N+1 Chebyshev polynomials.
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'u_polynomial - Fatal error!' )
    print ( '  N < 0' )
    raise Exception ( 'u_polynomial - Fatal error.' )

  v = np.zeros ( [ m, n+1 ] )

  for i in range ( 0, m ):
    v[i,0] = 1.0

  if ( n < 1 ):
    return v

  for i in range ( 0, m ):
    v[i,1] = 2.0 * x[i]

  for i in range ( 0, m ):
    for j in range ( 2, n + 1 ):
      v[i,j] = 2.0 * x[i] * v[i,j-1] - v[i,j-2]

  return v

def u_polynomial_test ( ):

#*****************************************************************************80
#
## u_polynomial_test() tests u_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'u_polynomial_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  u_polynomial() evaluates the Chebyshev polynomial U(n,x).' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X           U(n,x)                    U(n,x)                     Error' )
  print ( '' )

  n_data = 0
  x_vec = np.zeros ( 1 )

  while ( True ):

    n_data, n, x, fx1 = u_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    if ( n < 0 ):
      continue

    x_vec[0] = x
    fx2_vec = u_polynomial ( 1, n, x_vec )
    fx2 = fx2_vec[0,n]
    e = fx1 - fx2

    print ( '  %4d  %12g  %24.16g  %24.16g  %8.2g' % ( n, x, fx1, fx2, e ) )

  return

def u_polynomial_value ( n, x ):

#*****************************************************************************80
#
## u_polynomial_value(): returns the single value U(n,x).
#
#  Discussion:
#
#    In cases where calling u_polynomial is inconvenient, because it returns
#    a vector of values for multiple arguments X, this simpler interface
#    may be appropriate.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#    real X, the argument of the polynomial.
#
#  Output:
#
#    real VALUE, the value of U(n,x).
#
  import numpy as np

  if ( n < 0 ):
    value = 0.0
  else:
    m = 1
    x_vec = np.array ( [ x ] )
    v_vec = u_polynomial ( m, n, x_vec )
    value = v_vec[0,n]

  return value

def u_polynomial_value_test ( ):

#*****************************************************************************80
#
## u_polynomial_value_test() tests u_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'u_polynomial_value_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  u_polynomial_value() evaluates the Chebyshev polynomial U(n,x).' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X           U(n,x)                    U(n,x)                     Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx1 = u_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = u_polynomial_value ( n, x )
    e = fx1 - fx2

    print ( '  %4d  %12g  %24.16g  %24.16g  %8.2g' % ( n, x, fx1, fx2, e ) )

  return

def u_polynomial_values ( n_data ):

#*****************************************************************************80
#
## u_polynomial_values() returns values of Chebyshev polynomials U(n,x).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ChebyshevU[n,x]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 July 2015
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
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 14

  fx_vec = np.array ( ( \
      0.0000000000000000E+00, \
      0.1000000000000000E+01, \
      0.1600000000000000E+01, \
      0.1560000000000000E+01, \
      0.8960000000000000E+00, \
     -0.1264000000000000E+00, \
     -0.1098240000000000E+01, \
     -0.1630784000000000E+01, \
     -0.1511014400000000E+01, \
     -0.7868390400000000E+00, \
      0.2520719360000000E+00, \
      0.1190154137600000E+01, \
      0.1652174684160000E+01, \
      0.1453325357056000E+01 ) )

  n_vec = np.array ( ( \
    -1, \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12 ))

  x_vec = np.array ( ( \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def u_polynomial_values_test ( ):

#*****************************************************************************80
#
## u_polynomial_values_test() tests u_polynomial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'u_polynomial_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  u_polynomial_values() stores values of the Chebyshev U polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = u_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )

  return

def u_polynomial_zeros ( n ):

#*****************************************************************************80
#
## u_polynomial_zeros() returns zeroes of the Chebyshev polynomial U(n,x).
#
#  Discussion:
#
#    The I-th zero of U(n,x) is cos((I-1)*PI/(N-1)), I = 1 to N
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#  Output:
#
#    real Z(N), the zeroes.
#
  import numpy as np

  z = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( i + 1 ) * np.pi / float ( n + 1 )
    z[i] = np.cos ( angle )

  return z

def u_polynomial_zeros_test ( ):

#*****************************************************************************80
#
## u_polynomial_zeros_test() tests u_polynomial_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'u_polynomial_zeros_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  u_polynomial_zeros() computes the zeros of U(n,x)' )
  print ( '' )
  print ( '     N      X         U(n,x)' )

  for n in range ( 0, 6 ):

    x = u_polynomial_zeros ( n )
    fx = u_polynomial ( n, n + 1, x )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %8.4g  %14.6g' % ( i, x[i], fx[i,n] ) )

  return

def u_quadrature_rule ( n ):

#*****************************************************************************80
#
## u_quadrature_rule(): quadrature rule for U(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real T(N), W(N), the points and weights of the rule.
#
  import numpy as np

  aj = np.zeros ( n )

  bj = np.ones ( n )
  for i in range ( 0, n ):
    bj[i] = 0.5 * bj[i]

  cj = np.zeros ( n )
  cj[0] = np.sqrt ( np.pi / 2.0 )

  t, w = imtqlx ( n, aj, bj, cj )

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return t, w

def u_quadrature_rule_test ( ):

#*****************************************************************************80
#
## u_quadrature_rule_test() tests u_quadrature_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'u_quadrature_rule_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  u_quadrature_rule() computes the quadrature rule' )
  print ( '  associated with U(n,x)' )

  n = 7
  x, w = u_quadrature_rule ( n )

  r8vec2_print ( n, x, w, '      X            W' )

  print ( '' )
  print ( '  Use the quadrature rule to estimate:' )
  print ( '' )
  print ( '    Q = Integral ( -1 <= X <= +1 ) X^E * sqrt ( 1-x^2) dx' )
  print ( '' )
  print ( '   E       Q_Estimate      Q_Exact' )
  print ( '' )

  f = np.zeros ( n )

  for e in range ( 0, 2 * n ):
    if ( e == 0 ):
      for i in range ( 0, n ):
        f[i] = 1.0
    else:
      for i in range ( 0, n ):
        f[i] = x[i] ** e

    q = np.dot ( w, f )
    q_exact = u_moment ( e )
    print ( '  %2d  %14g  %14g' % ( e, q, q_exact ) )

  return

def uu_product_integral ( i, j ):

#*****************************************************************************80
#
## uu_product_integral(): integral (-1<=x<=1) U(i,x)*U(j,x)*sqrt(1-x^2) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the polynomial indices.
#    0 <= I, J.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  import numpy as np

  if ( i < 0 ):
    print ( '' )
    print ( 'uu_product_integral - Fatal error!' )
    print ( '  0 <= I is required.' )
    raise Exception ( 'uu_product_integral - Fatal error!' )

  if ( j < 0 ):
    print ( '' )
    print ( 'uu_product_integral - Fatal error!' )
    print ( '  0 <= J is required.' )
    raise Exception ( 'uu_product_integral - Fatal error!' )

  if ( i != j ):
    value = 0.0
  else:
    value = np.pi / 2.0

  return value

def uu_product_integral_test ( ):

#*****************************************************************************80
#
## uu_product_integral_test() tests uu_product_integral().
#
#  Discussion:
#
#    This process should match the uu_mass_matrix computation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'uu_product_integral_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  uu_product_integral() computes the product integral' )
  print ( '  of a pair of Chebyshev U polynomials U(i,x) and U(j,x).' )
  print ( '  A(I,J) = integral ( -1 <=x <= +1 ) U(i,x) U(j,x) sqrt ( 1 - x^2 ) dx' )
  print ( '  0    if i is not equal to j' )
  print ( '  pi/2 if i = j' )

  n = 4

  a = np.zeros ( [ n + 1, n + 1 ] )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      a[i,j] = uu_product_integral ( i, j )

  r8mat_print ( n + 1, n + 1, a, '  U(i,x)*U(j,x) integral matrix:' )

  return

def uu_product ( i, j, x ):

#*****************************************************************************80
#
## uu_product(): evaluate U(i,x)*U(j,x)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the indices.
#
#    real X, the argument.
#
#  Output:
#
#    real VALUE, the value.
#
  value = 0.0
  for k in range ( abs ( i - j ), i + j + 1, 2 ):
    value = value + u_polynomial_value ( k, x )

  return value

def uu_product_test ( ):

#*****************************************************************************80
#
## uu_product_test() tests uu_product().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'uu_product_test():' )
  print ( '  uu_product(I,J;X) = U(I,X) * U(J,X)' )

  r8_lo = -1.0
  r8_hi = +1.0

  print ( '' )
  print ( '   I   J      X               UI              UJ              UI*UJ       uu_product' )
  print ( '' )
  for test in range ( 0, 10 ):
    x = r8_lo + ( r8_hi - r8_lo ) * rng.random ( )
    i = rng.integers ( low = 0, high = 6, endpoint = True )
    ui = u_polynomial_value ( i, x )
    j = rng.integers ( low = -1, high = 4, endpoint = True )
    uj = u_polynomial_value ( j, x )
    uiuj = uu_product ( i, j, x )
    print ( '  %2d  %2d  %14.6g  %14.6g  %14.6g  %14.6g  %14.6g'\
      % ( i, j, x, ui, uj, ui * uj, uiuj ) )

  return

def v_mass_matrix ( n ):

#*****************************************************************************80
#
## v_mass_matrix() computes the mass matrix for the Chebyshev V polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  x, w = v_quadrature_rule ( n + 1 )

  phi = v_polynomial ( n + 1, n, x )

  phiw = np.zeros ( [ n + 1, n + 1 ] )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      phiw[j,i] = w[i] * phi[i,j]

  a = np.dot ( phiw, phi )

  return a

def v_mass_matrix_test ( ):

#*****************************************************************************80
#
## v_mass_matrix_test() tests v_mass_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'v_mass_matrix_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  v_mass_matrix() computes the mass matrix for the' )
  print ( '  Chebyshev polynomials V(i,x).' )
  print ( '  A(I,J) = integral ( -1 <=x <= +1 ) V(i,x) V(j,x) sqrt(1+x)/sqrt(1-x) dx' )
  print ( '  0  if i is not equal to j' )
  print ( '  pi if i = j =/= 0.' )

  n = 3

  a = v_mass_matrix ( n )

  r8mat_print ( n + 1, n + 1, a, '  V mass matrix:' )

  return

def v_moment ( e ):

#*****************************************************************************80
#
## v_moment(): integral ( -1 <= x <= +1 ) x^e sqrt(1+x) / sqrt(1-x) dx.
#
#  Discussion:
#
#    This function returns the moments of the distribution associated
#    with the Chebyshev V polynomial.
#
#     E  v_moment
#    --  -------------
#     0      pi
#     1      pi / 2
#     2      pi / 2
#     3    3 pi / 8
#     4    3 pi / 8
#     5    5 pi / 16
#     6    5 pi / 16
#     7   35 pi / 128
#     8   35 pi / 128
#     9   63 pi / 256
#    10   63 pi / 256
#    11  231 pi / 1024
#    12  231 pi / 1024
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer E, the exponent of X.
#    0 <= E.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import factorial
  from scipy.special import gamma
  import numpy as np

  r8_e = float ( e )

  f1 = 1.0 / gamma ( 1.5 + r8_e )
  f2 = r8_mop ( e )
  f3 = np.pi * gamma ( 1.5 + r8_e )
  f4 = 2.0 * r8_hyper_2f1 ( 0.5, - r8_e, 1.0, 2.0 )
  f5 = ( -1.0 + r8_mop ( e ) ) * r8_hyper_2f1 ( 0.5, - r8_e, 2.0, 2.0 )
  f6 = np.sqrt ( np.pi ) * factorial ( e )
  f7 = ( - 1.0 + r8_mop ( e ) ) * r8_hyper_2f1 ( -0.5, 1.0 + r8_e, 1.5 + r8_e, - 1.0 )
  f8 = 2.0 * r8_hyper_2f1 ( 0.5, 1.0 + r8_e, 1.5 + r8_e, -1.0 )

  value = f1 * f2 * ( f3 * ( f4 + f5 ) - f6 * ( f7 + f8 ) );

  return value

def v_moment_test ( ):

#*****************************************************************************80
#
## v_moment_test() tests v_moment().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'v_moment_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  v_moment() returns the value of' )
  print ( '  integral ( -1 <=x <= +1 ) x^e * sqrt(1+x) / sqrt(1-x) dx' )
  print ( '' )
  print ( '   E       Integral' )
  print ( '' )
  for e in range ( 0, 11 ):
    value = v_moment ( e )
    print ( '  %2d  %14.6g' % ( e, value ) )

  return

def v_polynomial_01_values ( n_data ):

#*****************************************************************************80
#
## v_polynomial_01_values(): values of shifted Chebyshev polynomials V01(n,x).
#
#  Discussion:
#
#    V01(n,x) = V(n,2*x-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 July 2015
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
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 25

  fx_vec = np.array ( ( \
     0.0000000000000000, \
     1.0000000000000000, \
     0.4000000000000000, \
    -0.4400000000000000, \
    -1.0160000000000000, \
    -0.9824000000000000, \
    -0.3593600000000000, \
     0.4792960000000000, \
     1.0303744000000000, \
     0.9632281600000000, \
     0.3181450240000000, \
    -0.5178251264000000, \
    -1.0431002009600000, \
    -0.9425151549440000, \
    -15.000000000000000, \
     3.1417984000000000, \
    -1.3912448000000000, \
    -1.2177792000000000, \
     1.1837056000000000, \
     1.0000000000000000, \
    -0.8558976000000000, \
    -0.8905088000000000, \
     0.8752768000000000, \
     0.1197696000000000, \
     1.0000000000000000 ) )

  n_vec = np.array ( ( \
    -1, \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  7,  7, \
     7,  7,  7, \
     7,  7,  7, \
     7,  7,  7 ))

  x_vec = np.array ( ( \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.00, \
    0.10, \
    0.20, \
    0.30, \
    0.40, \
    0.50, \
    0.60, \
    0.70, \
    0.80, \
    0.90, \
    1.00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def v_polynomial_01_values_test ( ):

#*****************************************************************************80
#
## v_polynomial_01_values_test() tests v_polynomial_01_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'v_polynomial_01_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  v_polynomial_01_values() stores values of the shifted Chebyshev V polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = v_polynomial_01_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )

  return

def v_polynomial_ab ( a, b, m, n, xab ):

#*****************************************************************************80
#
## v_polynomial_ab(): Chebyshev polynomials VAB(N,X) in [A,B].
#
#  Discussion:
#
#    VAB(n,x) = V(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the domain of definition.
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest polynomial to compute.
#
#    real XAB(M,1), the evaluation points.
#    It must be the case that A <= XAB(*) <= B.
#
#  Output:
#
#    real V(M,N+1), the values of the Chebyshev polynomials.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = v_polynomial ( m, n, x );
 
  return v

def v_polynomial_ab_test ( ):

#*****************************************************************************80
#
## v_polynomial_ab_test() tests v_polynomial_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'v_polynomial_ab_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  v_polynomial_ab() evaluates Chebyshev polynomials VAB(n,x)' )
  print ( '  shifted from [-1,+1] to the domain [A,B].' )
  print ( '' )
  print ( '  Here, we will use the new domain [0,1]' )
  print ( '  and the desired maximum polynomial degree will be N = 5.' )

  a = 0.0
  b = 1.0
  m = 11
  n = 5
  x = np.linspace ( a, b, m )
  
  v = v_polynomial_ab ( a, b, m, n, x )

  r8mat_print ( m, n + 1, v, '  Tables of V values:' )

  return

def v_polynomial_ab_value ( a, b, n, xab ):

#*****************************************************************************80
#
## v_polynomial_ab_value(): Chebyshev polynomial VAB(N,X) in [A,B].
#
#  Discussion:
#
#    VAB(n,x) = V(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the domain of definition.
#
#    integer N, the degree of the polynomial.
#
#    real XAB, the evaluation points.
#    A <= XAB <= B.
#
#  Output:
#
#    real V, the value.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = v_polynomial_value ( n, x );
 
  return v

def v_polynomial_ab_value_test ( ):

#*****************************************************************************80
#
## v_polynomial_ab_value_test() tests v_polynomial_ab_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'v_polynomial_ab_value_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  v_polynomial_ab_value() evaluates a Chebyshev polynomial VAB(n,x)' )
  print ( '  shifted from [-1,+1] to the domain [A,B].' )
  print ( '' )
  print ( '  Here, we will use the new domain [0,1].' )
  print ( '' )
  print ( '                    Tabulated     Computed' )
  print ( '     N      X        V01(n,x)      V01(n,x)' )
  print ( '' )

  a = 0.0
  b = 1.0

  n_data = 0

  while ( True ):

    n_data, n, x01, fx = v_polynomial_01_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = v_polynomial_ab_value ( a, b, n, x01 )

    print ( '  %8d  %8.4f  %14.6g  %14.6g' % ( n, x01, fx, fx2 ) )

  return

def v_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## v_polynomial_coefficients(): coefficients of the Chebyshev polynomial V(n,x).
#
#  First terms:
#
#    N/K     0     1      2      3       4     5      6    7      8    9   10
#
#     0      1
#     1     -1     2
#     2     -1    -2      4
#     3      1    -4     -4      8
#     4      1    +4    -12     -8      16
#     5     -1     6    +12    -32     -16    32
#     6     -1    -6     24    +32     -80   -32     64
#     7     +1    -8    -24     80     +80  -192    -64   128
#
#  Recursion:
#
#    V(0,X) = 1,
#    V(1,X) = 2 * X - 1,
#    V(N,X) = 2 * X * V(N-1,X) - V(N-2,X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
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
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#  Output:
#
#    real C(1:N+1,1:N+1), the coefficients of the polynomials.
#
  import numpy as np

  c = np.zeros ( [ n + 1, n + 1 ] )

  c[0,0] = 1.0

  if ( 0 < n ):

    c[1,0] = -1.0
    c[1,1] =  2.0
 
    for i in range ( 2, n + 1 ):
      c[i,0] = - c[i-2,0]
      for j in range ( 1, i - 1 ):
        c[i,j] = 2.0 * c[i-1,j-1] - c[i-2,j]
      c[i,i-1] = 2.0 * c[i-1,i-2]
      c[i,i] = 2.0 * c[i-1,i-1]
 
  return c

def v_polynomial_coefficients_test ( ):

#*****************************************************************************80
#
## v_polynomial_coefficients_test() tests v_polynomial_coefficients().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 7

  print ( '' )
  print ( 'v_polynomial_coefficients_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  v_polynomial_coefficients() determines the Chebyshev' )
  print ( '  polynomial coefficients.' )

  c = v_polynomial_coefficients ( n )
 
  for i in range ( 0, n + 1 ):
    c2 = np.zeros ( i + 1 )
    for j in range ( 0, i + 1 ):
      c2[j] = c[i,j]
    r8poly_print ( i, c2, '' )

  return

def v_polynomial_plot ( n_num, n_val, filename ):

#*****************************************************************************80
#
## v_polynomial_plot() plots Chebyshev polynomials V(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_NUM, the number of polynomials to plot.
#
#    integer N_VAL(N_NUM), the degree of each polynomial.
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

  for i in range ( 0, n_num ):
    n = n_val[i]
    y = v_polynomial ( m, n, x )
    plt.plot ( x, y, 'b-', linewidth = 2.0 )

  t = 'V(n,x), for n = '
  for i in range ( 0, n_num ):
    n = n_val[i]
    t = t + str ( n )
    if ( 1 < n_num and i < n_num - 1 ):
      t = t + ', '

  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---V(n,x)--->' )
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '  Created plot file "%s".' % ( filename ) )

  return

def v_polynomial_plot_test ( ):

#*****************************************************************************80
#
## v_polynomial_plot_test() tests v_polynomial_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'v_polynomial_plot_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  v_polynomial_plot() plots several Chebyshev V polynomials.' )

  n_num = 6
  n_val = np.array ( [ 0, 1, 2, 3, 4, 5 ] )
  filename = 'v_polynomial_plot.png'

  v_polynomial_plot ( n_num, n_val, filename )

  return

def v_polynomial ( m, n, x ):

#*****************************************************************************80
#
## v_polynomial() evaluates Chebyshev polynomials V(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2105
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest polynomial to compute.
#
#    real X(M,1), the evaluation points.
#
#  Output:
#
#    real V(1:M,1:N+1), the values of the N+1 Chebyshev polynomials.
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'v_polynomial - Fatal error!' )
    print ( '  N < 0' )
    raise Exception ( 'v_polynomial - Fatal error.' )

  v = np.zeros ( [ m, n + 1 ] )

  for i in range ( 0, m ):
    v[i,0] = 1.0

  if ( n < 1 ):
    return v

  for i in range ( 0, m ):
    v[i,1] = 2.0 * x[i] - 1.0

  for i in range ( 0, m ):
    for j in range ( 2, n + 1 ):
      v[i,j] = 2.0 * x[i] * v[i,j-1] - v[i,j-2]

  return v

def v_polynomial_test ( ):

#*****************************************************************************80
#
## v_polynomial_test() tests v_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'v_polynomial_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  v_polynomial() evaluates the Chebyshev polynomial V(n,x).' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X           V(n,x)                    V(n,x)                     Error' )
  print ( '' )

  n_data = 0
  x_vec = np.zeros ( 1 )

  while ( True ):

    n_data, n, x, fx1 = v_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    if ( n < 0 ):
      continue

    x_vec[0] = x
    fx2_vec = v_polynomial ( 1, n, x_vec )
    fx2 = fx2_vec[0,n]
    e = fx1 - fx2

    print ( '  %4d  %12g  %24.16g  %24.16g  %8.2g' % ( n, x, fx1, fx2, e ) )

  return

def v_polynomial_value ( n, x ):

#*****************************************************************************80
#
## v_polynomial_value() returns the single value V(n,x).
#
#  Discussion:
#
#    In cases where calling v_polynomial is inconvenient, because it returns
#    a vector of values for multiple arguments X, this simpler interface
#    may be appropriate.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#    real X, the argument of the polynomial.
#
#  Output:
#
#    real VALUE, the value of V(n,x).
#
  import numpy as np

  if ( n < 0 ):
    value = 0.0
  else:
    m = 1
    x_vec = np.array ( [ x ] )
    v_vec = v_polynomial ( m, n, x_vec )
    value = v_vec[0,n]

  return value

def v_polynomial_value_test ( ):

#*****************************************************************************80
#
## v_polynomial_value_test() tests v_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'v_polynomial_value_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  v_polynomial_value() evaluates the Chebyshev polynomial V(n,x).' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X           V(n,x)                    V(n,x)                     Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx1 = v_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = v_polynomial_value ( n, x )
    e = fx1 - fx2

    print ( '  %4d  %12g  %24.16g  %24.16g  %8.2g' % ( n, x, fx1, fx2, e ) )

  return

def v_polynomial_values ( n_data ):

#*****************************************************************************80
#
## v_polynomial_values() returns values of Chebyshev polynomials V(n,x).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      u = Sqrt[(x+1)/2],
#      ChebyshevT[2*n+1,u] / u
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 July 2015
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
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 14

  fx_vec = np.array ( ( \
     0.0000000000000000E+00, \
     1.0000000000000000E+00, \
     0.6000000000000000E+00, \
    -0.0400000000000000E+00, \
    -0.6640000000000000E+00, \
    -1.0224000000000000E+00, \
    -0.9718400000000000E+00, \
    -0.5325440000000000E+00, \
     0.1197696000000000E+00, \
     0.7241753600000000E+00, \
     1.0389109760000000E+00, \
     0.9380822016000000E+00, \
     0.4620205465600000E+00, \
    -0.1988493271040000E+00 ) )

  n_vec = np.array ( ( \
    -1, \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12 ))

  x_vec = np.array ( ( \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00  ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def v_polynomial_values_test ( ):

#*****************************************************************************80
#
## v_polynomial_values_test() tests v_polynomial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'v_polynomial_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  v_polynomial_values() stores values of the Chebyshev V polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = v_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )

  return

def v_polynomial_zeros ( n ):

#*****************************************************************************80
#
## v_polynomial_zeros() returns zeroes of the Chebyshev polynomial V(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#  Output:
#
#    real Z(N), the zeroes.
#
  import numpy as np

  z = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( 2 * n - 2 * i - 1 ) * np.pi / float ( 2 * n + 1 )
    z[i] = np.cos ( angle )

  return z

def v_polynomial_zeros_test ( ):

#*****************************************************************************80
#
## v_polynomial_zeros_test() tests v_polynomial_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'v_polynomial_zeros_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  v_polynomial_zeros() computes the zeros of V(n,x)' )
  print ( '' )
  print ( '     N      X         V(n,x)' )

  for n in range ( 0, 6 ):

    x = v_polynomial_zeros ( n )
    fx = v_polynomial ( n, n + 1, x )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %8.4g  %14.6g' % ( i, x[i], fx[i,n] ) )

  return

def v_quadrature_rule ( n ):

#*****************************************************************************80
#
## v_quadrature_rule(): quadrature rule for V(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real T(N), W(N), the points and weights of the rule.
#
  import numpy as np

  aj = np.zeros ( n )
  aj[0] = + 0.5

  bj = np.zeros ( n )
  for i in range ( 0, n ):
    bj[i] = 0.5

  cj = np.zeros ( n )
  cj[0] = np.sqrt ( np.pi )

  t, w = imtqlx ( n, aj, bj, cj )

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return t, w

def v_quadrature_rule_test ( ):

#*****************************************************************************80
#
## v_quadrature_rule_test() tests v_quadrature_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'v_quadrature_rule_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  v_quadrature_rule() computes the quadrature rule' )
  print ( '  associated with V(n,x)' )

  n = 7
  x, w = v_quadrature_rule ( n )

  r8vec2_print ( n, x, w, '      X            W' )

  print ( '' )
  print ( '  Use the quadrature rule to estimate:' )
  print ( '' )
  print ( '    Q = Integral ( -1 <= X <= +1 ) X^E * sqrt(1+x)/sqrt(1-x) dx' )
  print ( '' )
  print ( '   E       Q_Estimate      Q_Exact' )
  print ( '' )

  f = np.zeros ( n )

  for e in range ( 0, 2 * n ):
    if ( e == 0 ):
      for i in range ( 0, n ):
        f[i] = 1.0
    else:
      for i in range ( 0, n ):
        f[i] = x[i] ** e

    q = np.dot ( w, f )
    q_exact = v_moment ( e )
    print ( '  %2d  %14g  %14g' % ( e, q, q_exact ) )

  return

def vv_product_integral ( i, j ):

#*****************************************************************************80
#
## vv_product_integral(): integral (-1<=x<=1) V(i,x)*V(j,x)*sqrt(1+x)/sqrt(1-x) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the polynomial indices.
#    0 <= I, J.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  import numpy as np

  if ( i < 0 ):
    print ( '' )
    print ( 'vv_product_integral - Fatal error!' )
    print ( '  0 <= I is required.' )
    raise Exception ( 'vv_product_integral - Fatal error!' )

  if ( j < 0 ):
    print ( '' )
    print ( 'vv_product_integral - Fatal error!' )
    print ( '  0 <= J is required.' )
    raise Exception ( 'vv_product_integral - Fatal error!' )

  if ( i != j ):
    value = 0.0
  else:
    value = np.pi

  return value

def vv_product_integral_test ( ):

#*****************************************************************************80
#
## vv_product_integral_test() tests vv_product_integral().
#
#  Discussion:
#
#    This process should match the vv_mass_matrix computation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'vv_product_integral_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  vv_product_integral() computes the product integral' )
  print ( '  of a pair of Chebyshev V polynomials V(i,x) and V(j,x).' )
  print ( '  A(I,J) = integral ( -1 <=x <= +1 ) V(i,x) V(j,x) sqrt ( 1 + x ) / sqrt ( 1 - x ) dx' )
  print ( '  0  if i is not equal to j' )
  print ( '  pi if i = j' )

  n = 4

  a = np.zeros ( [ n + 1, n + 1 ] )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      a[i,j] = vv_product_integral ( i, j )

  r8mat_print ( n + 1, n + 1, a, '  V(i,x)*V(j,x) integral matrix:' )

  return

def w_mass_matrix ( n ):

#*****************************************************************************80
#
## w_mass_matrix() computes the mass matrix for the Chebyshev W polynomial.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#  Output:
#
#    real A[N+1,N+1], the mass matrix.
#
  import numpy as np

  x, w = w_quadrature_rule ( n + 1 )

  phi = w_polynomial ( n + 1, n, x )

  phiw = np.zeros ( [ n + 1, n + 1 ] )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      phiw[j,i] = w[i] * phi[i,j]

  a = np.dot ( phiw, phi )

  return a

def w_mass_matrix_test ( ):

#*****************************************************************************80
#
## w_mass_matrix_test() tests w_mass_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'w_mass_matrix_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  w_mass_matrix() computes the mass matrix for the' )
  print ( '  Chebyshev polynomials W(i,x).' )
  print ( '  A(I,J) = integral ( -1 <=x <= +1 ) W(i,x) W(j,x) sqrt(1-x)/sqrt(1+x) dx' )
  print ( '  0  if i is not equal to j' )
  print ( '  pi if i = j.' )

  n = 3

  a = w_mass_matrix ( n )

  r8mat_print ( n + 1, n + 1, a, '  W mass matrix:' )

  return

def w_moment ( e ):

#*****************************************************************************80
#
## w_moment(): integral ( -1 <= x <= +1 ) x^e sqrt(1-x) / sqrt(1+x) dx.
#
#  Discussion:
#
#    This function returns the moments of the distribution associated
#    with the Chebyshev W polynomial.
#
#     E  w_moment
#    --  -------------
#     0        pi
#     1  -     pi / 2
#     2        pi / 2
#     3  -   3 pi / 8
#     4      3 pi / 8
#     5  -   5 pi / 16
#     6      5 pi / 16
#     7  -  35 pi / 128
#     8     35 pi / 128
#     9  -  63 pi / 256
#    10     63 pi / 256
#    11  - 231 pi / 1024
#    12    231 pi / 1024
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer E, the exponent of X.
#    0 <= E.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  from scipy.special import factorial
  from scipy.special import gamma
  import numpy as np

  r8_e = float ( e )

  f1 = 1.0 / gamma ( 1.5 + r8_e )
  f2 = r8_mop ( e )
  f3 = np.pi * gamma ( 1.5 + r8_e )
  f4 = 2.0 * r8_mop ( e ) * r8_hyper_2f1 ( 0.5, - r8_e, 1.0, 2.0 )
  f5 = ( -1.0 + r8_mop ( e ) ) * r8_hyper_2f1 ( 0.5, - r8_e, 2.0, 2.0 )
  f6 = np.sqrt ( np.pi ) * factorial ( e )
  f7 = ( - 1.0 + r8_mop ( e ) ) * r8_hyper_2f1 ( -0.5, 1.0 + r8_e, 1.5 + r8_e, - 1.0 )
  f8 = 2.0 * r8_mop ( e ) * r8_hyper_2f1 ( 0.5, 1.0 + r8_e, 1.5 + r8_e, -1.0 )

  value = f1 * f2 * ( f3 * ( f4 - f5 ) + f6 * ( f7 - f8 ) )

  return value

def w_moment_test ( ):

#*****************************************************************************80
#
## w_moment_test() tests w_moment().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'w_moment_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  w_moment() returns the value of' )
  print ( '  integral ( -1 <=x <= +1 ) x^e * sqrt(1-x) / sqrt(1+x) dx' )
  print ( '' )
  print ( '   E       Integral' )
  print ( '' )
  for e in range ( 0, 11 ):
    value = w_moment ( e )
    print ( '  %2d  %14.6g' % ( e, value ) )

  return

def w_polynomial_01_values ( n_data ):

#*****************************************************************************80
#
## w_polynomial_01_values(): values of shifted Chebyshev polynomials W01(n,x).
#
#  Discussion:
#
#    W01(n,x) = W(n,2*x-1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 July 2015
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
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 25

  fx_vec = np.array ( ( \
     0.000000000000000, \
     1.000000000000000, \
     2.400000000000000, \
     2.360000000000000, \
     0.904000000000000, \
    -1.094400000000000, \
    -2.436160000000000, \
    -2.316224000000000, \
    -0.806553600000000, \
     1.187048960000000, \
     2.468422144000000, \
     2.268742041600000, \
     0.707816714240000, \
    -1.277798641664000, \
    -1.000000000000000, \
    -0.119769600000000, \
    -0.875276800000000, \
     0.890508800000000, \
     0.855897600000000, \
    -1.000000000000000, \
    -1.183705600000000, \
     1.217779200000000, \
     1.391244800000000, \
    -3.141798400000000, \
     15.00000000000000 ) )

  n_vec = np.array ( ( \
    -1, \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12,  7,  7, \
     7,  7,  7, \
     7,  7,  7, \
     7,  7,  7 ))

  x_vec = np.array ( ( \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.85, \
    0.00, \
    0.10, \
    0.20, \
    0.30, \
    0.40, \
    0.50, \
    0.60, \
    0.70, \
    0.80, \
    0.90, \
    1.00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def w_polynomial_01_values_test ( ):

#*****************************************************************************80
#
## w_polynomial_01_values_test() tests w_polynomial_01_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'w_polynomial_01_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  w_polynomial_01_values() stores values of the shifted Chebyshev W polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = w_polynomial_01_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )

  return

def w_polynomial_ab ( a, b, m, n, xab ):

#*****************************************************************************80
#
## w_polynomial_ab(): Chebyshev polynomials WAB(N,X) in [A,B].
#
#  Discussion:
#
#    WAB(n,x) = W(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the domain of definition.
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest polynomial to compute.
#
#    real XAB(M,1), the evaluation points.
#    A <= XAB(*) <= B.
#
#  Output:
#
#    real V(M,N+1), the values of the Chebyshev polynomials.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = w_polynomial ( m, n, x );
 
  return v

def w_polynomial_ab_test ( ):

#*****************************************************************************80
#
## w_polynomial_ab_test() tests w_polynomial_ab().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'w_polynomial_ab_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  w_polynomial_ab() evaluates Chebyshev polynomials WAB(n,x)' )
  print ( '  shifted from [-1,+1] to the domain [A,B].' )
  print ( '' )
  print ( '  Here, we will use the new domain [0,1]' )
  print ( '  and the desired maximum polynomial degree will be N = 5.' )

  a = 0.0
  b = 1.0
  m = 11
  n = 5
  x = np.linspace ( a, b, m )
  
  v = w_polynomial_ab ( a, b, m, n, x )

  r8mat_print ( m, n + 1, v, '  Tables of W values:' )

  return

def w_polynomial_ab_value ( a, b, n, xab ):

#*****************************************************************************80
#
## w_polynomial_ab(): Chebyshev polynomial WAB(N,X) in [A,B].
#
#  Discussion:
#
#    WAB(n,x) = W(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A, B, the domain of definition.
#
#    integer N, the degree of the polynomial.
#
#    real XAB, the evaluation points.
#    A <= XAB <= B.
#
#  Output:
#
#    real V, the value.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = w_polynomial_value ( n, x );
 
  return v

def w_polynomial_ab_value_test ( ):

#*****************************************************************************80
#
## w_polynomial_ab_value_test() tests w_polynomial_ab_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'w_polynomial_ab_value_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  w_polynomial_ab_value() evaluates a Chebyshev polynomial WAB(n,x)' )
  print ( '  shifted from [-1,+1] to the domain [A,B].' )
  print ( '' )
  print ( '  Here, we will use the new domain [0,1].' )
  print ( ' ' )
  print ( '                    Tabulated     Computed' )
  print ( '     N      X        W01(n,x)      W01(n,x)' )
  print ( ' ' )

  a = 0.0
  b = 1.0

  n_data = 0

  while ( True ):

    n_data, n, x01, fx = w_polynomial_01_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = w_polynomial_ab_value ( a, b, n, x01 )

    print ( '  %8d  %8.4f  %14.6g  %14.6g' % ( n, x01, fx, fx2 ) )

  return

def w_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## w_polynomial_coefficients(): coefficients of the Chebyshev polynomial W(n,x).
#
#  First terms:
#
#    N/K     0     1      2      3       4     5      6    7      8    9   10
#
#     0      1
#     1      1     2
#     2     -1     2      4
#     3     -1    -4      4      8
#     4      1    -4    -12      8      16
#     5      1     6    -12    -32     +16    32
#     6     -1     6     24    -32     -80    32     64
#     7     -1    -8    +24    +80     -80  -192     64   128
#
#  Recursion:
#
#    W(0,X) = 1,
#    W(1,X) = 2 * X + 1,
#    W(N,X) = 2 * X * W(N-1,X) - W(N-2,X)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
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
#    integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#  Output:
#
#    real C(1:N+1,1:N+1), the coefficients of the polynomials.
#
  import numpy as np

  c = np.zeros ( [ n + 1, n + 1 ] )

  c[0,0] = 1.0

  if ( 0 < n ):

    c[1,0] = +1.0
    c[1,1] =  2.0
 
    for i in range ( 2, n + 1 ):
      c[i,0] = - c[i-2,0]
      for j in range ( 1, i - 1 ):
        c[i,j] = 2.0 * c[i-1,j-1] - c[i-2,j]
      c[i,i-1] = 2.0 * c[i-1,i-2]
      c[i,i] = 2.0 * c[i-1,i-1]
 
  return c

def w_polynomial_coefficients_test ( ):

#*****************************************************************************80
#
## w_polynomial_coefficients_test() tests w_polynomial_coefficients().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  n = 7

  print ( '' )
  print ( 'w_polynomial_coefficients_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  w_polynomial_coefficients() determines the Chebyshev' )
  print ( '  polynomial coefficients.' )

  c = w_polynomial_coefficients ( n )
 
  for i in range ( 0, n + 1 ):
    c2 = np.zeros ( i + 1 )
    for j in range ( 0, i + 1 ):
      c2[j] = c[i,j]
    r8poly_print ( i, c2, '' )

  return

def w_polynomial_plot ( n_num, n_val, filename ):

#*****************************************************************************80
#
## w_polynomial_plot() plots Chebyshev polynomials W(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N_NUM, the number of polynomials to plot.
#
#    integer N_VAL(N_NUM), the degree of each polynomial.
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

  for i in range ( 0, n_num ):
    n = n_val[i]
    y = w_polynomial ( m, n, x )
    plt.plot ( x, y, 'b-', linewidth = 2.0 )

  t = 'W(n,x), for n = '
  for i in range ( 0, n_num ):
    n = n_val[i]
    t = t + str ( n )
    if ( 1 < n_num and i < n_num - 1 ):
      t = t + ', '

  plt.title ( t )
  plt.grid ( True )
  plt.xlabel ( '<---X--->' )
  plt.ylabel ( '<---W(n,x)--->' )
  plt.savefig ( filename )
  plt.show ( block = False )
  plt.close ( )

  print ( '  Created plot file "%s".' % ( filename ) )

  return

def w_polynomial_plot_test ( ):

#*****************************************************************************80
#
## w_polynomial_plot_test() tests w_polynomial_plot().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'w_polynomial_plot_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  w_polynomial_plot() plots several Chebyshev W polynomials.' )

  n_num = 6
  n_val = np.array ( [ 0, 1, 2, 3, 4, 5 ] )
  filename = 'w_polynomial_plot.png'

  w_polynomial_plot ( n_num, n_val, filename )

  return

def w_polynomial ( m, n, x ):

#*****************************************************************************80
#
## w_polynomial() evaluates Chebyshev polynomials W(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of evaluation points.
#
#    integer N, the highest polynomial to compute.
#
#    real X(M,1), the evaluation points.
#
#  Output:
#
#    real V(1:M,1:N+1), the values of the N+1 Chebyshev polynomials.
#
  import numpy as np

  if ( n < 0 ):
    print ( '' )
    print ( 'w_polynomial - Fatal error!' )
    print ( '  N < 0' )
    raise Exception ( 'w_polynomial - Fatal error.' )

  v = np.zeros ( [ m, n + 1 ] )

  for i in range ( 0, m ):
    v[i,0] = 1.0

  if ( n < 1 ):
    return v

  for i in range ( 0, m ):
    v[i,1] = 2.0 * x[i] + 1.0

  for i in range ( 0, m ):
    for j in range ( 2, n + 1 ):
      v[i,j] = 2.0 * x[i] * v[i,j-1] - v[i,j-2]

  return v

def w_polynomial_test ( ):

#*****************************************************************************80
#
## w_polynomial_test() tests w_polynomial().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'w_polynomial_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  w_polynomial() evaluates the Chebyshev polynomial W(n,x).' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X           W(n,x)                    W(n,x)                     Error' )
  print ( '' )

  n_data = 0
  x_vec = np.zeros ( 1 )

  while ( True ):

    n_data, n, x, fx1 = w_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    if ( n < 0 ):
      continue

    x_vec[0] = x
    fx2_vec = w_polynomial ( 1, n, x_vec )
    fx2 = fx2_vec[0,n]
    e = fx1 - fx2

    print ( '  %4d  %12g  %24.16g  %24.16g  %8.2g' % ( n, x, fx1, fx2, e ) )

  return

def w_polynomial_value ( n, x ):

#*****************************************************************************80
#
## w_polynomial_value() returns the single value W(n,x).
#
#  Discussion:
#
#    In cases where calling w_polynomial is inconvenient, because it returns
#    a vector of values for multiple arguments X, this simpler interface
#    may be appropriate.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#    real X, the argument of the polynomial.
#
#  Output:
#
#    real VALUE, the value of W(n,x).
#
  import numpy as np

  if ( n < 0 ):
    value = 0.0
  else:
    m = 1
    x_vec = np.array ( [ x ] )
    v_vec = w_polynomial ( m, n, x_vec )
    value = v_vec[0,n]

  return value

def w_polynomial_value_test ( ):

#*****************************************************************************80
#
## w_polynomial_value_test() tests w_polynomial_value().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'w_polynomial_value_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  w_polynomial_value() evaluates the Chebyshev polynomial W(n,x).' )
  print ( '' )
  print ( '                        Tabulated                 Computed' )
  print ( '     N        X           W(n,x)                    W(n,x)                     Error' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx1 = w_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = w_polynomial_value ( n, x )
    e = fx1 - fx2

    print ( '  %4d  %12g  %24.16g  %24.16g  %8.2g' % ( n, x, fx1, fx2, e ) )

  return

def w_polynomial_values ( n_data ):

#*****************************************************************************80
#
## w_polynomial_values() returns values of Chebyshev polynomials W(n,x).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      u = Sqrt[(x+1)/2],
#      ChebyshevU[2*n,u]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 July 2015
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
#    integer N_DATA.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    integer N, the order of the function.
#
#    real X, the point where the function is evaluated.
#
#    real FX, the value of the function.
#
  import numpy as np

  n_max = 14

  fx_vec = np.array ( ( \
     0.000000000000000E+00, \
     1.000000000000000E+00, \
     2.600000000000000E+00, \
     3.160000000000000E+00, \
     2.456000000000000E+00, \
     0.769600000000000E+00, \
    -1.224640000000000E+00, \
    -2.729024000000000E+00, \
    -3.141798400000000E+00, \
    -2.297853440000000E+00, \
    -0.534767104000000E+00, \
     1.442226073600000E+00, \
     2.842328821760000E+00, \
     3.105500041216000E+00 ) )

  n_vec = np.array ( ( \
    -1, \
     0,  1,  2, \
     3,  4,  5, \
     6,  7,  8, \
     9, 10, 11, \
    12 ))

  x_vec = np.array ( ( \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00, \
     0.8E+00 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    x = 0.0
    fx = 0.0
  else:
    n = n_vec[n_data]
    x = x_vec[n_data]
    fx = fx_vec[n_data]
    n_data = n_data + 1

  return n_data, n, x, fx

def w_polynomial_values_test ( ):

#*****************************************************************************80
#
## w_polynomial_values_test() tests w_polynomial_values().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'w_polynomial_values_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  w_polynomial_values() stores values of the Chebyshev W polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = w_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )

  return

def w_polynomial_zeros ( n ):

#*****************************************************************************80
#
## w_polynomial_zeros() returns zeroes of the Chebyshev polynomial W(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the polynomial.
#
#  Output:
#
#    real Z(N), the zeroes.
#
  import numpy as np

  z = np.zeros ( n )

  for i in range ( 0, n ):
    angle = float ( 2 * n - 2 * i ) * np.pi / float ( 2 * n + 1 )
    z[i] = np.cos ( angle )

  return z

def w_polynomial_zeros_test ( ):

#*****************************************************************************80
#
## w_polynomial_zeros_test() tests w_polynomial_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'w_polynomial_zeros_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  w_polynomial_zeros() computes the zeros of W(n,x)' )
  print ( '' )
  print ( '     N      X         W(n,x)' )

  for n in range ( 0, 6 ):

    x = w_polynomial_zeros ( n )
    fx = w_polynomial ( n, n + 1, x )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %8.4g  %14.6g' % ( i, x[i], fx[i,n] ) )

  return

def w_quadrature_rule ( n ):

#*****************************************************************************80
#
## w_quadrature_rule(): quadrature rule for W(n,x).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the rule.
#
#  Output:
#
#    real T(N), W(N), the points and weights of the rule.
#
  import numpy as np

  aj = np.zeros ( n )
  aj[0] = - 0.5

  bj = np.zeros ( n )
  for i in range ( 0, n ):
    bj[i] = 0.5

  cj = np.zeros ( n )
  cj[0] = np.sqrt ( np.pi )

  t, w = imtqlx ( n, aj, bj, cj )

  for i in range ( 0, n ):
    w[i] = w[i] ** 2

  return t, w

def w_quadrature_rule_test ( ):

#*****************************************************************************80
#
## w_quadrature_rule_test() tests w_quadrature_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'w_quadrature_rule_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  w_quadrature_rule() computes the quadrature rule' )
  print ( '  associated with W(n,x)' )

  n = 7
  x, w = w_quadrature_rule ( n )

  r8vec2_print ( n, x, w, '      X            W' )

  print ( '' )
  print ( '  Use the quadrature rule to estimate:' )
  print ( '' )
  print ( '    Q = Integral ( -1 <= X <= +1 ) X^E * sqrt (1-x)/sqrt(1+x) dx' )
  print ( '' )
  print ( '   E       Q_Estimate      Q_Exact' )
  print ( '' )

  f = np.zeros ( n )

  for e in range ( 0, 2 * n ):
    if ( e == 0 ):
      for i in range ( 0, n ):
        f[i] = 1.0
    else:
      for i in range ( 0, n ):
        f[i] = x[i] ** e

    q = np.dot ( w, f )
    q_exact = w_moment ( e )
    print ( '  %2d  %14g  %14g' % ( e, q, q_exact ) )

  return

def ww_product_integral ( i, j ):

#*****************************************************************************80
#
## ww_product_integral(): integral (-1<=x<=1) W(i,x)*W(j,x)*sqrt(1-x)/sqrt(1+x) dx
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, J, the polynomial indices.
#    0 <= I, J.
#
#  Output:
#
#    real VALUE, the value of the integral.
#
  import numpy as np

  if ( i < 0 ):
    print ( '' )
    print ( 'ww_product_integral - Fatal error!' )
    print ( '  0 <= I is required.' )
    raise Exception ( 'ww_product_integral - Fatal error!' )

  if ( j < 0 ):
    print ( '' )
    print ( 'ww_product_integral - Fatal error!' )
    print ( '  0 <= J is required.' )
    raise Exception ( 'ww_product_integral - Fatal error!' )

  if ( i != j ):
    value = 0.0
  else:
    value = np.pi

  return value

def ww_product_integral_test ( ):

#*****************************************************************************80
#
## ww_product_integral_test() tests ww_product_integral().
#
#  Discussion:
#
#    This process should match the ww_mass_matrix computation.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'ww_product_integral_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ww_product_integral() computes the product integral' )
  print ( '  of a pair of Chebyshev W polynomials W(i,x) and W(j,x).' )
  print ( '  A(I,J) = integral ( -1 <=x <= +1 ) W(i,x) W(j,x) sqrt ( 1 - x ) / sqrt ( 1 + x ) dx' )
  print ( '  0  if i is not equal to j' )
  print ( '  pi if i = j' )

  n = 4

  a = np.zeros ( [ n + 1, n + 1 ] )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      a[i,j] = ww_product_integral ( i, j )

  r8mat_print ( n + 1, n + 1, a, '  W(i,x)*W(j,x) integral matrix:' )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  chebyshev_polynomial_test ( )
  timestamp ( )

