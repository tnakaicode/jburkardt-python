#! /usr/bin/env python3
#
def chebyshev_polynomial_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV_POLYNOMIAL_TEST tests the CHEBYSHEV_POLYNOMIAL library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    21 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CHEBYSHEV_POLYNOMIAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the CHEBYSHEV_POLYNOMIAL library.' )
#
#  Utilities.
#
  gamma_values_test ( )
  i4_uniform_ab_test ( )
  imtqlx_test ( )
  r8_choose_test ( )
  r8_epsilon_test ( )
  r8_factorial_test ( )
  r8_gamma_test ( )
  r8_hyper_2f1_test ( )
  r8_mop_test ( )
  r8_psi_test ( )
  r8_uniform_ab_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8poly_print_test ( )
  r8vec_print_test ( )
  r8vec2_print_test ( )
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
  print ( 'CHEBYSHEV_POLYNOMIAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

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

def hyper_2f1_values ( n_data ):

#*****************************************************************************80
#
## HYPER_2F1_VALUES returns some values of the hypergeometric 2F1 function.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      fx = Hypergeometric2F1 [ a, b, c, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real A, B, C, X, the parameters.
#
#    Output, real F, the value of the function.
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
## HYPER_2F1_VALUES_TEST demonstrates the use of HYPER_2F1_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'HYPER_2F1_VALUES_TEST:' )
  print ( '  HYPER_2F1_VALUES stores values of the hypergeometric function 2F1' )
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
  print ( 'HYPER_2F1_VALUES_TEST:' )
  print ( '  Normal end of execution.' )

  return

def i4_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## I4_UNIFORM_AB returns a scaled pseudorandom I4.
#
#  Discussion:
#
#    The pseudorandom number will be scaled to be uniformly distributed
#    between A and B.
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
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer A, B, the minimum and maximum acceptable values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer C, the randomly chosen integer.
#
#    Output, integer SEED, the updated seed.
#
  from math import floor
  from sys import exit

  i4_huge = 2147483647

  seed = floor ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge; 

  if ( seed == 0 ):
    print ( '' )
    print ( 'I4_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'I4_UNIFORM_AB - Fatal error!' )

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
  a = round ( a )
  b = round ( b )

  r = ( 1.0 - r ) * ( min ( a, b ) - 0.5 ) \
    +         r   * ( max ( a, b ) + 0.5 )
#
#  Use rounding to convert R to an integer between A and B.
#
  value = round ( r )

  value = max ( value, min ( a, b ) )
  value = min ( value, max ( a, b ) )
  value = int ( value )

  return value, seed

def i4_uniform_ab_test ( ):

#*****************************************************************************80
#
## I4_UNIFORM_AB_TEST tests I4_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 October 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  a = -100
  b = 200
  seed = 123456789

  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_UNIFORM_AB computes pseudorandom values' )
  print ( '  in an interval [A,B].' )
  print ( '' )
  print ( '  The lower endpoint A = %d' % ( a ) )
  print ( '  The upper endpoint B = %d' % ( b ) )
  print ( '  The initial seed is %d' % ( seed ) )
  print ( '' )

  for i in range ( 1, 21 ):
    [ j, seed ] = i4_uniform_ab ( a, b, seed )
    print ( '  %8d  %8d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST:' )
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

def psi_values ( n_data ):

#*****************************************************************************80
#
## PSI_VALUES returns some values of the Psi or Digamma function.
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
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
## PSI_VALUES_TEST demonstrates the use of PSI_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'PSI_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PSI_VALUES stores values of the PSI function.' )
  print ( '' )
  print ( '      X         PSI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, f = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %12f  %24.16f' % ( x, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PSI_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_choose ( n, k ):

#*****************************************************************************80
#
## R8_CHOOSE computes the binomial coefficient C(N,K) as an R8.
#
#  Discussion:
#
#    The value is calculated in such a way as to avoid overflow and
#    roundoff.  The calculation is done in R8 arithmetic.
#
#    The formula used is:
#
#      C(N,K) = N! / ( K! * (N-K)! )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, K, are the values of N and K.
#
#    Output, real VALUE, the number of combinations of N
#    things taken K at a time.
#
  import numpy as np

  if ( n < 0 ):

    value = 0.0

  elif ( k == 0 ):

    value = 1.0

  elif ( k == 1 ):

    value = float ( n )

  elif ( 1 < k and k < n - 1 ):

    facn = r8_gamma_log ( float ( n + 1 ) )
    fack = r8_gamma_log ( float ( k + 1 ) )
    facnmk = r8_gamma_log ( float ( n - k + 1 ) )

    value = round ( np.exp ( facn - fack - facnmk ) )

  elif ( k == n - 1 ):

    value = float ( n )

  elif ( k == n ):

    value = 1.0

  else:

    value = 0.0

  return value

def r8_choose_test ( ):

#*****************************************************************************80
#
## R8_CHOOSE_TEST tests R8_CHOOSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_CHOOSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_CHOOSE evaluates C(N,K).' )
  print ( '' )
  print ( '         N         K       CNK' )
 
  for n in range ( 0, 6 ):
    print ( '' )
    for k in range ( 0, n + 1 ):
      cnk = r8_choose ( n, k )
      print ( '  %8d  %8d  %14.6g' % ( n, k, cnk ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_CHOOSE_TEST' )
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

def r8_gamma_log ( x ):

#*****************************************************************************80
#
## R8_GAMMA_LOG evaluates the logarithm of the gamma function.
#
#  Discussion:
#
#    This routine calculates the LOG(GAMMA) function for a positive real
#    argument X.  Computation is based on an algorithm outlined in
#    references 1 and 2.  The program uses rational functions that
#    theoretically approximate LOG(GAMMA) to at least 18 significant
#    decimal digits.  The approximation for X > 12 is from reference
#    3, while approximations for X < 12.0 are similar to those in
#    reference 1, but are unpublished.
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
#    William Cody, Kenneth Hillstrom,
#    Chebyshev Approximations for the Natural Logarithm of the
#    Gamma Function,
#    Mathematics of Computation,
#    Volume 21, Number 98, April 1967, pages 198-203.
#
#    Kenneth Hillstrom,
#    ANL/AMD Program ANLC366S, DGAMMA/DLGAMA,
#    May 1969.
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
#    Output, real R8_GAMMA_LOG, the value of the function.
#
  import numpy as np
  from math import log

  c = np.array ( [ \
    -1.910444077728E-03, \
     8.4171387781295E-04, \
    -5.952379913043012E-04, \
     7.93650793500350248E-04, \
    -2.777777777777681622553E-03, \
     8.333333333333333331554247E-02, \
     5.7083835261E-03 ] )
  d1 = -5.772156649015328605195174E-01
  d2 = 4.227843350984671393993777E-01
  d4 = 1.791759469228055000094023E+00
  frtbig = 2.25E+76
  p1 = np.array ( [ \
    4.945235359296727046734888E+00, \
    2.018112620856775083915565E+02, \
    2.290838373831346393026739E+03, \
    1.131967205903380828685045E+04, \
    2.855724635671635335736389E+04, \
    3.848496228443793359990269E+04, \
    2.637748787624195437963534E+04, \
    7.225813979700288197698961E+03 ] )
  p2 = np.array ( [ \
    4.974607845568932035012064E+00, \
    5.424138599891070494101986E+02, \
    1.550693864978364947665077E+04, \
    1.847932904445632425417223E+05, \
    1.088204769468828767498470E+06, \
    3.338152967987029735917223E+06, \
    5.106661678927352456275255E+06, \
    3.074109054850539556250927E+06 ] )
  p4 = np.array ( [ \
    1.474502166059939948905062E+04, \
    2.426813369486704502836312E+06, \
    1.214755574045093227939592E+08, \
    2.663432449630976949898078E+09, \
    2.940378956634553899906876E+10, \
    1.702665737765398868392998E+11, \
    4.926125793377430887588120E+11, \
    5.606251856223951465078242E+11 ] )
  q1 = np.array ( [ \
    6.748212550303777196073036E+01, \
    1.113332393857199323513008E+03, \
    7.738757056935398733233834E+03, \
    2.763987074403340708898585E+04, \
    5.499310206226157329794414E+04, \
    6.161122180066002127833352E+04, \
    3.635127591501940507276287E+04, \
    8.785536302431013170870835E+03 ] )
  q2 = np.array ( [ \
    1.830328399370592604055942E+02, \
    7.765049321445005871323047E+03, \
    1.331903827966074194402448E+05, \
    1.136705821321969608938755E+06, \
    5.267964117437946917577538E+06, \
    1.346701454311101692290052E+07, \
    1.782736530353274213975932E+07, \
    9.533095591844353613395747E+06 ] )
  q4 = np.array ( [ \
    2.690530175870899333379843E+03, \
    6.393885654300092398984238E+05, \
    4.135599930241388052042842E+07, \
    1.120872109616147941376570E+09, \
    1.488613728678813811542398E+10, \
    1.016803586272438228077304E+11, \
    3.417476345507377132798597E+11, \
    4.463158187419713286462081E+11 ] )
  r8_epsilon = 2.220446049250313E-016
  sqrtpi = 0.9189385332046727417803297
  xbig = 2.55E+305
  xinf = 1.79E+308

  y = x

  if ( 0.0 < y and y <= xbig ):

    if ( y <= r8_epsilon ):

      res = - log ( y )
#
#  EPS < X <= 1.5.
#
    elif ( y <= 1.5 ):

      if ( y < 0.6796875 ):
        corr = -log ( y );
        xm1 = y;
      else:
        corr = 0.0;
        xm1 = ( y - 0.5 ) - 0.5;

      if ( y <= 0.5 or 0.6796875 <= y ):

        xden = 1.0;
        xnum = 0.0;
        for i in range ( 0, 8 ):
          xnum = xnum * xm1 + p1[i]
          xden = xden * xm1 + q1[i]

        res = corr + ( xm1 * ( d1 + xm1 * ( xnum / xden ) ) )

      else:

        xm2 = ( y - 0.5 ) - 0.5
        xden = 1.0
        xnum = 0.0
        for i in range ( 0, 8 ):
          xnum = xnum * xm2 + p2[i]
          xden = xden * xm2 + q2[i]

        res = corr + xm2 * ( d2 + xm2 * ( xnum / xden ) )
#
#  1.5 < X <= 4.0.
#
    elif ( y <= 4.0 ):

      xm2 = y - 2.0
      xden = 1.0
      xnum = 0.0
      for i in range ( 0, 8 ):
        xnum = xnum * xm2 + p2[i]
        xden = xden * xm2 + q2[i]

      res = xm2 * ( d2 + xm2 * ( xnum / xden ) )
#
#  4.0 < X <= 12.0.
#
    elif ( y <= 12.0 ):

      xm4 = y - 4.0
      xden = -1.0
      xnum = 0.0
      for i in range ( 0, 8 ):
        xnum = xnum * xm4 + p4[i]
        xden = xden * xm4 + q4[i]

      res = d4 + xm4 * ( xnum / xden )
#
#  Evaluate for 12 <= argument.
#
    else:

      res = 0.0

      if ( y <= frtbig ):

        res = c[6]
        ysq = y * y

        for i in range ( 0, 6 ):
          res = res / ysq + c[i]

      res = res / y
      corr = log ( y )
      res = res + sqrtpi - 0.5 * corr
      res = res + y * ( corr - 1.0 )
#
#  Return for bad arguments.
#
  else:

    res = xinf

  return res

def r8_gamma_log_test ( ):

#*****************************************************************************80
#
## R8_GAMMA_LOG_TEST tests R8_GAMMA_LOG.
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
  print ( 'R8_GAMMA_LOG_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_GAMMA_LOG evaluates the logarithm of the Gamma function.' )
  print ( '' )
  print ( '      X            GAMMA_LOG(X)    R8_GAMMA_LOG(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = gamma_log_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_gamma_log ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_GAMMA_LOG_TEST' )
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
  from math import exp
  from math import floor
  from math import log
  from math import sin
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
  r8_pi = 3.141592653589793
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

      fact = - r8_pi / sin ( r8_pi * res )
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
      sum = sum + ( y - 0.5 ) * log ( y )
      res = exp ( sum )

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

def r8_hyper_2f1 ( a, b, c, x ):

#*****************************************************************************80
#
## R8_HYPER_2F1 evaluates the hypergeometric function F(A,B,C,X).
#
#  Discussion:
#
#    A minor bug was corrected.  The HW variable, used in several places as
#    the "old" value of a quantity being iteratively improved, was not
#    being initialized.  JVB, 11 February 2008.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 February 2015
#
#  Author:
#
#    Original FORTRAN77 version by Shanjie Zhang, Jianming Jin.
#    Python version by John Burkardt.
#
#    The F77 original version of this routine is copyrighted by
#    Shanjie Zhang and Jianming Jin.  However, they give permission to
#    incorporate this routine into a user program provided that the copyright
#    is acknowledged.
#
#  Reference:
#
#    Shanjie Zhang, Jianming Jin,
#    Computation of Special Functions,
#    Wiley, 1996,
#    ISBN: 0-471-11963-6,
#    LC: QA351.C45
#
#  Parameters:
#
#    Input, real A, B, C, X, the arguments of the function.
#    C must not be equal to a nonpositive integer.
#    X < 1.
#
#    Output, real VALUE, the value of the function.
#
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
    print ( 'R8_HYPER_2F1 - Fatal error!' )
    print ( '  The hypergeometric series is divergent.' )
    print ( '  C is integral and negative.' )
    print ( '  C = %f' % ( c ) )

  if ( l1 ):
    print ( '' )
    print ( 'R8_HYPER_2F1 - Fatal error!' )
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

    gc = r8_gamma ( c )
    gcab = r8_gamma ( c - a - b )
    gca = r8_gamma ( c - a )
    gcb = r8_gamma ( c - b )
    value = gc * gcab / ( gca * gcb )
    return value

  elif ( 1.0 + x <= eps and abs ( c - a + b - 1.0 ) <= eps ):

    g0 = np.sqrt ( np.pi ) * 2.0 ** ( - a )
    g1 = r8_gamma ( c )
    g2 = r8_gamma ( 1.0 + a / 2.0 - b )
    g3 = r8_gamma ( 0.5 + 0.5 * a )
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
      ga = r8_gamma ( a )
      gb = r8_gamma ( b )
      gc = r8_gamma ( c )
      gam = r8_gamma ( a + float ( m ) )
      gbm = r8_gamma ( b + float ( m ) )

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

      ga = r8_gamma ( a )
      gb = r8_gamma ( b )
      gc = r8_gamma ( c )
      gca = r8_gamma ( c - a )
      gcb = r8_gamma ( c - b )
      gcab = r8_gamma ( c - a - b )
      gabc = r8_gamma ( a + b - c )
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
    print ( 'R8_HYPER_2F1 - Warning!' )
    print ( '  A large number of iterations were needed.' )
    print ( '  The accuracy of the results should be checked.' )

  return value

def r8_hyper_2f1_test ( ):

#*****************************************************************************80
#
## R8_HYPER_2F1_TEST tests R8_HYPER_2F1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8_HYPER_2F1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_HYPER_2F1 evaluates the hypergeometric 2F1 function.' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_HYPER_2F1_TEST' )
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

def r8_mop ( i ):

#*****************************************************************************80
#
## R8_MOP returns the I-th power of -1 as an R8 value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the power of -1.
#
#    Output, real R8_MOP, the I-th power of -1.
#
  if ( ( i % 2 ) == 0 ):
    value = + 1.0
  else:
    value = - 1.0

  return value

def r8_mop_test ( ):

#*****************************************************************************80
#
## R8_MOP_TEST tests R8_MOP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 December 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_MOP_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_MOP evaluates (-1.0)^I4 as an R8.' )
  print ( '' )
  print ( '    I4  R8_MOP(I4)' )
  print ( '' )

  i4_min = -100;
  i4_max = +100;
  seed = 123456789;

  for test in range ( 0, 10 ):
    i4, seed = i4_uniform_ab ( i4_min, i4_max, seed )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_MOP_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8poly_print ( m, a, title ):

#*****************************************************************************80
#
## R8POLY_PRINT prints out a polynomial.
#
#  Discussion:
#
#    The power sum form is:
#
#      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the nominal degree of the polynomial.
#
#    Input, real A[0:M], the polynomial coefficients.
#    A[0] is the constant term and
#    A[M] is the coefficient of X^M.
#
#    Input, string TITLE, a title.
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
## R8POLY_PRINT_TEST tests R8POLY_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8POLY_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8POLY_PRINT prints an R8POLY.' )

  m = 5
  c = np.array ( [ 12.0, -3.4, 56.0, 0.0, 0.78, 9.0 ] )

  r8poly_print ( m, c, '  The R8POLY:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8POLY_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8_psi ( x ):

#*****************************************************************************80
#
## R8_PSI evaluates the function Psi(X).
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
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    Original FORTRAN77 version by William Cody.
#    Python version by John Burkardt.
#
#  Reference:
#
#    William Cody, Anthony Strecok, Henry Thacher,
#    Chebyshev Approximations for the Psi Function,
#    Mathematics of Computation,
#    Volume 27, Number 121, January 1973, pages 123-127.
#
#  Parameters:
#
#    Input, real X, the argument of the function.
#
#    Output, real VALUE, the value of the function.
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
## R8_PSI_TEST tests R8_PSI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8_PSI_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_PSI evaluates the PSI function.' )
  print ( '' )
  print ( '      X            PSI(X)    R8_PSI(X)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, fx1 = psi_values ( n_data )

    if ( n_data == 0 ):
      break

    fx2 = r8_psi ( x )

    print ( '  %12g  %24.16g  %24.16g' % ( x, fx1, fx2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_PSI_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_uniform_ab ( a, b, seed ):

#*****************************************************************************80
#
## R8_UNIFORM_AB returns a scaled pseudorandom R8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, real A, B, the minimum and maximum values.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real R, the randomly chosen value.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from sys import exit

  i4_huge = 2147483647

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8_UNIFORM_AB - Fatal error!' )

  seed = int ( seed )

  seed = ( seed % i4_huge )

  if ( seed < 0 ):
    seed = seed + i4_huge

  k = ( seed // 127773 )

  seed = 16807 * ( seed - k * 127773 ) - k * 2836

  if ( seed < 0 ):
    seed = seed + i4_huge

  r = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r8_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_AB_TEST tests R8_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  a = 10.0
  b = 20.0

  print ( '' )
  print ( 'R8_UNIFORM_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_AB returns random values in a given range:' )
  print ( '  [ A, B ]' )
  print ( '' )
  print ( '  For this problem:' )
  print ( '  A = %f' % ( a ) )
  print ( '  B = %f' % ( b ) )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):
    r, seed = r8_uniform_ab ( a, b, seed )
    print ( '  %f' % ( r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_AB_TEST' )
  print ( '  Normal end of execution' )
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

def t_mass_matrix ( n ):

#*****************************************************************************80
#
## T_MASS_MATRIX computes the mass matrix for the Chebyshev T polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
## T_MASS_MATRIX_TEST tests T_MASS_MATRIX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'T_MASS_MATRIX_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  T_MASS_MATRIX computes the mass matrix for the' )
  print ( '  Chebyshev T polynomials T(i,x).' )
  print ( '  A(I,J) = integral ( -1 <=x <= +1 ) T(i,x) T(j,x) / sqrt ( 1 - x^2 ) dx' )
  print ( '  0    if i is not equal to j' )
  print ( '  pi   if i = j = 0' )
  print ( '  pi/2 if i = j =/= 0.' )

  n = 3

  a = t_mass_matrix ( n )

  r8mat_print ( n + 1, n + 1, a, '  T mass matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'T_MASS_MATRIX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def t_moment ( e ):

#*****************************************************************************80
#
## T_MOMENT: integral ( -1 <= x <= +1 ) x^e dx / sqrt ( 1 - x^2 ).
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer E, the exponent of X.
#    0 <= E.
#
#    Output, real VALUE, the value of the integral.
#
  import numpy as np

  if ( ( e % 2 ) == 1 ):

    value = 0.0

  else:

    value = r8_choose ( e, e // 2 ) * np.pi / 2.0 ** e

  return value

def t_moment_test ( ):

#*****************************************************************************80
#
## T_MOMENT_TEST tests T_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'T_MOMENT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  T_MOMENT returns the value of' )
  print ( '  integral ( -1 <=x <= +1 ) x^e / sqrt ( 1 - x^2 ) dx' )
  print ( '' )
  print ( '   E       Integral' )
  print ( '' )
  for e in range ( 0, 11 ):
    value = t_moment( e )
    print ( '  %2d  %14.6g' % ( e, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'T_MOMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def t_polynomial_01_values ( n_data ):

#*****************************************************************************80
#
## T_POLYNOMIAL_01_VALUES: values of shifted Chebyshev polynomials T01(n,x).
#
#  Discussion:
#
#    T01(n,x) = T(n,2*x-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#    Output, real FX, the value of the function.
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
## T_POLYNOMIAL_01_VALUES_TEST demonstrates the use of T_POLYNOMIAL_01_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'T_POLYNOMIAL_01_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  T_POLYNOMIAL_01_VALUES stores values of the shifted Chebyshev T polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = t_polynomial_01_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'T_POLYNOMIAL_01_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def t_polynomial_ab ( a, b, m, n, xab ):

#*****************************************************************************80
#
## T_POLYNOMIAL_AB: Chebyshev polynomials TAB(N,X) in [A,B].
#
#  Discussion:
#
#    TAB(n,x) = T(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the domain of definition.
#
#    Input, integer M, the number of evaluation points.
#
#    Input, integer N, the highest polynomial to compute.
#
#    Input, real XAB(M,1), the evaluation points.
#    It must be the case that A <= XAB(*) <= B.
#
#    Output, real V(M,N+1), the values of the Chebyshev polynomials.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = t_polynomial ( m, n, x );
 
  return v

def t_polynomial_ab_test ( ):

#*****************************************************************************80
#
## T_POLYNOMIAL_AB_TEST tests T_POLYNOMIAL_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'T_POLYNOMIAL_AB_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  T_POLYNOMIAL_AB evaluates Chebyshev polynomials TAB(n,x)' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'T_POLYNOMIAL_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def t_polynomial_ab_value ( a, b, n, xab ):

#*****************************************************************************80
#
## T_POLYNOMIAL_AB: Chebyshev polynomial TAB(N,X) in [A,B].
#
#  Discussion:
#
#    TAB(n,x) = T(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the domain of definition.
#
#    Input, integer N, the degree of the polynomial.
#
#    Input, real XAB, the evaluation points.
#    A <= XAB <= B.
#
#    Output, real V, the value.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = t_polynomial_value ( n, x );
 
  return v

def t_polynomial_ab_value_test ( ):

#*****************************************************************************80
#
## T_POLYNOMIAL_AB_VALUE_TEST tests T_POLYNOMIAL_AB_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'T_POLYNOMIAL_AB_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  T_POLYNOMIAL_AB_VALUE evaluates a Chebyshev polynomial TAB(n,x)' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'T_POLYNOMIAL_AB_VALUE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def t_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## T_POLYNOMIAL_COEFFICIENTS: coefficients of the Chebyshev polynomial T(n,x).
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    Output, real C(1:N+1,1:N+1), the coefficients of the Chebyshev T
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
## T_POLYNOMIAL_COEFFICIENTS_TEST tests T_POLYNOMIAL_COEFFICIENTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'T_POLYNOMIAL_COEFFICIENTS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  T_POLYNOMIAL_COEFFICIENTS determines the Chebyshev' )
  print ( '  polynomial coefficients.' )

  c = t_polynomial_coefficients ( n )
 
  for i in range ( 0, n + 1 ):
    c2 = np.zeros ( i + 1 )
    for j in range ( 0, i + 1 ):
      c2[j] = c[i,j]
    r8poly_print ( i, c2, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'T_POLYNOMIAL_COEFFICIENTS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def t_polynomial_plot ( n_num, n_val, filename ):

#*****************************************************************************80
#
## T_POLYNOMIAL_PLOT plots Chebyshev polynomials T(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N_NUM, the number of polynomials to plot.
#
#    Input, integer N_VAL(N_NUM), the degree of each polynomial.
#
#    Input, string FILENAME, the name into which the graphics information is
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
  plt.clf ( )

  print ( '  Created plot file "%s".' % ( filename ) )

  return

def t_polynomial_plot_test ( ):

#*****************************************************************************80
#
## T_POLYNOMIAL_PLOT_TEST tests T_POLYNOMIAL_PLOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'T_POLYNOMIAL_PLOT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Plot several Chebyshev T polynomials.' )

  n_num = 6
  n_val = np.array ( [ 0, 1, 2, 3, 4, 5 ] )
  filename = 't_polynomial_plot.png'

  t_polynomial_plot ( n_num, n_val, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'T_POLYNOMIAL_PLOT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def t_polynomial ( m, n, x ):

#*****************************************************************************80
#
## T_POLYNOMIAL evaluates the Chebyshev polynomials T(N,X) of the first kind.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of evaluation points.
#
#    Input, integer N, the highest polynomial to compute.
#
#    Input, real X(M,1), the evaluation points.
#
#    Output, real V(1:M,1:N+1), the values of the Chebyshev polynomials 
#    0 through N at X(1:M).
#
  import numpy as np
  from sys import exit

  if ( n < 0 ):
    print ( '' )
    print ( 'T_POLYNOMIAL - Fatal error!' )
    print ( '  N < 0' )
    exit ( 'T_POLYNOMIAL - Fatal error.' )

  v = np.zeros ( [ m, n + 1 ] )

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
## T_POLYNOMIAL_TEST tests T_POLYNOMIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'T_POLYNOMIAL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  T_POLYNOMIAL evaluates the Chebyshev polynomial T(n,x).' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'T_POLYNOMIAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def t_polynomial_value ( n, x ):

#*****************************************************************************80
#
## T_POLYNOMIAL_VALUE: returns the single value T(n,x).
#
#  Discussion:
#
#    In cases where calling T_POLYNOMIAL is inconvenient, because it returns
#    a vector of values for multiple arguments X, this simpler interface
#    may be appropriate.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the polynomial.
#
#    Input, real X, the argument of the polynomial.
#
#    Output, real VALUE, the value of T(n,x).
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
## T_POLYNOMIAL_VALUE_TEST tests T_POLYNOMIAL_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'T_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  T_POLYNOMIAL_VALUE evaluates the Chebyshev polynomial T(n,x).' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'T_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def t_polynomial_values ( n_data ):

#*****************************************************************************80
#
## T_POLYNOMIAL_VALUES returns values of Chebyshev polynomials T(n,x).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ChebyshevT[n,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#    Output, real FX, the value of the function.
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
## T_POLYNOMIAL_VALUES_TEST demonstrates the use of T_POLYNOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'T_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  T_POLYNOMIAL_VALUES stores values of the Chebyshev T polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = t_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'T_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def t_polynomial_zeros ( n ):

#*****************************************************************************80
#
## T_POLYNOMIAL_ZEROS returns zeroes of the Chebyshev polynomial T(n,x).
#
#  Discussion:
#
#    The I-th zero is cos((2*I-1)*PI/(2*N)), I = 1 to N
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the polynomial.
#
#    Output, real Z(N), the zeroes.
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
## T_POLYNOMIAL_ZEROS_TEST tests T_POLYNOMIAL_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'T_POLYNOMIAL_ZEROS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  T_POLYNOMIAL_ZEROS computes the zeros of T(n,x)' )
  print ( '' )
  print ( '     N      X         T(n,x)' )

  for n in range ( 0, 6 ):

    x = t_polynomial_zeros ( n )
    fx = t_polynomial ( n, n + 1, x )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %8.4g  %14.6g' % ( i, x[i], fx[i,n] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'T_POLYNOMIAL_ZEROS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def t_quadrature_rule ( n ):

#*****************************************************************************80
#
## T_QUADRATURE_RULE: quadrature rule for T(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the rule.
#
#    Output, real T(N,1), W(N,1), the points and weights of the rule.
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
## T_QUADRATURE_RULE_TEST tests T_QUADRATURE_RULE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'T_QUADRATURE_RULE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  T_QUADRATURE_RULE computes the quadrature rule' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'T_QUADRATURE_RULE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def tt_product_integral ( i, j ):

#*****************************************************************************80
#
## TT_PRODUCT_INTEGRAL: integral (-1<=x<=1) T(i,x)*T(j,x)/sqrt(1-x^2) dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the polynomial indices.
#    0 <= I, J.
#
#    Output, real VALUE, the value of the integral.
#
  import numpy as np
  from sys import exit

  if ( i < 0 ):
    print ( '' )
    print ( 'TT_PRODUCT_INTEGRAL - Fatal error!' )
    print ( '  0 <= I is required.' )
    exit ( 'TT_PRODUCT_INTEGRAL - Fatal error!' )

  if ( j < 0 ):
    print ( '' )
    print ( 'TT_PRODUCT_INTEGRAL - Fatal error!' )
    print ( '  0 <= J is required.' )
    exit ( 'TT_PRODUCT_INTEGRAL - Fatal error!' )

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
## TT_PRODUCT_INTEGRAL_TEST tests TT_PRODUCT_INTEGRAL.
#
#  Discussion:
#
#    This process should match the T_MASS_MATRIX computation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'TT_PRODUCT_INTEGRAL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TT_PRODUCT_INTEGRAL computes the product integral' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'TT_PRODUCT_INTEGRAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def tt_product ( i, j, x ):

#*****************************************************************************80
#
## TT_PRODUCT: evaluate T(i,x)*T(j,x)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the indices.
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the value.
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
## TT_PRODUCT_TEST tests TT_PRODUCT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TT_PRODUCT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TT_PRODUCT(I,J;X) = T(I,X) * T(J,X)' )

  r8_lo = -1.0
  r8_hi = +1.0
  seed = 123456789

  print ( '' )
  print ( '   I   J      X               TI              TJ              TI*TJ       TT_PRODUCT' )
  print ( '' )
  for test in range ( 0, 10 ):
    x, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
    i, seed = i4_uniform_ab ( 0, 6, seed )
    ti = t_polynomial_value ( i, x )
    j, seed = i4_uniform_ab ( -1, 4, seed )
    tj = t_polynomial_value ( j, x )
    titj = tt_product ( i, j, x )
    print ( '  %2d  %2d  %14.6g  %14.6g  %14.6g  %14.6g  %14.6g'\
      % ( i, j, x, ti, tj, ti * tj, titj ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TT_PRODUCT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def ttt_product_integral ( i, j, k ):

#*****************************************************************************80
#
## TTT_PRODUCT_INTEGRAL: integral (-1<=x<=1) T(i,x)*T(j,x)*T(k,x)/sqrt(1-x^2) dx
#
#  Discussion:
#
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer I, J, K, the polynomial indices.
#    0 <= I, J.
#
#    Output, real VALUE, the integral.
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
## TTT_PRODUCT_INTEGRAL_TEST tests TTT_PRODUCT_INTEGRAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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

  test_num = 20

  print ( '' )
  print ( 'TTT_PRODUCT_INTEGRAL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TTT_PRODUCT_INTEGRAL computes the triple integral' )
  print ( '  Tijk = integral ( -1 <= x <= 1 ) T(i,x) T(j,x) T(k,x) / sqrt ( 1-x^2) dx' )
  print ( '' )
  print ( '   I   J   K     Tijk           Tijk' )
  print ( '                 computed       exact' )
  print ( '' )

  n = 15
  x, w = t_quadrature_rule ( n )

  seed = 123456789

  for test in range ( 0, test_num ):
    i, seed = i4_uniform_ab ( 2, 6, seed )
    j, seed = i4_uniform_ab ( 1, 3, seed )
    k, seed = i4_uniform_ab ( 0, 4, seed )
    fx1 = ttt_product_integral ( i, j, k )
    fx2 = 0.0
    for l in range ( 0, n ):
      ti = t_polynomial_value ( i, x[l] )
      tj = t_polynomial_value ( j, x[l] )
      tk = t_polynomial_value ( k, x[l] )
      fx2 = fx2 + w[l] * ti * tj * tk

    print ( '  %2d  %2d  %2d  %14.6g  %14.6g' % ( i, j, k, fx1, fx2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TTT_PRODUCT_INTEGRAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def tu_product ( i, j, x ):

#*****************************************************************************80
#
## TU_PRODUCT: evaluate T(i,x)*U(j,x)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the indices.
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the value.
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
## TU_PRODUCT_TEST tests TU_PRODUCT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    16 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TU_PRODUCT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TU_PRODUCT(I,J;X) = T(I,X) * U(J,X)' )

  r8_lo = -1.0
  r8_hi = +1.0
  seed = 123456789

  print ( '' )
  print ( '   I   J      X               TI              UJ              TI*UJ       TU_PRODUCT' )
  print ( '' )
  for test in range ( 0, 10 ):
    x, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
    i, seed = i4_uniform_ab ( 0, 6, seed )
    ti = t_polynomial_value ( i, x )
    j, seed = i4_uniform_ab ( -1, 4, seed )
    uj = u_polynomial_value ( j, x )
    tiuj = tu_product ( i, j, x )
    print ( '  %2d  %2d  %14.6g  %14.6g  %14.6g  %14.6g  %14.6g'\
      % ( i, j, x, ti, uj, ti * uj, tiuj ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TU_PRODUCT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def u_mass_matrix ( n ):

#*****************************************************************************80
#
## U_MASS_MATRIX computes the mass matrix for the Chebyshev T polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
## U_MASS_MATRIX_TEST tests U_MASS_MATRIX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'U_MASS_MATRIX_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  U_MASS_MATRIX computes the mass matrix for the' )
  print ( '  Chebyshev U polynomials U(i,x).' )
  print ( '  A(I,J) = integral ( -1 <=x <= +1 ) U(i,x) U(j,x) * sqrt ( 1 - x^2 ) dx' )
  print ( '  0    if i is not equal to j' )
  print ( '  pi/2 if i = j.' )

  n = 3

  a = u_mass_matrix ( n )

  r8mat_print ( n + 1, n + 1, a, '  U mass matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'U_MASS_MATRIX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def u_moment ( e ):

#*****************************************************************************80
#
## U_MOMENT: integral ( -1 <= x <= +1 ) x^e sqrt ( 1 - x^2 ) dx.
#
#  Discussion:
#
#     E    U_MOMENT
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer E, the exponent of X.
#    0 <= E.
#
#    Output, real VALUE, the value of the integral.
#
  import numpy as np

  if ( ( e % 2 ) == 1 ):

    value = 0.0

  else:

    arg1 = 0.5 * float ( 1 + e )
    arg2 = 2.0 + 0.5 * float ( e )
    value = 0.5 * np.sqrt ( np.pi ) * r8_gamma ( arg1 ) / r8_gamma ( arg2 )

  return value

def u_moment_test ( ):

#*****************************************************************************80
#
## U_MOMENT_TEST tests U_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'U_MOMENT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  U_MOMENT returns the value of' )
  print ( '  integral ( -1 <=x <= +1 ) x^e * sqrt ( 1 - x^2 ) dx' )
  print ( '' )
  print ( '   E       Integral' )
  print ( '' )
  for e in range ( 0, 11 ):
    value = u_moment ( e )
    print ( '  %2d  %14.6g' % ( e, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'U_MOMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def u_polynomial_01_values ( n_data ):

#*****************************************************************************80
#
## U_POLYNOMIAL_01_VALUES: values of shifted Chebyshev polynomials U01(n,x).
#
#  Discussion:
#
#    U01(n,x) = U(n,2*x-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#    Output, real FX, the value of the function.
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
## U_POLYNOMIAL_01_VALUES_TEST demonstrates the use of U_POLYNOMIAL_01_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'U_POLYNOMIAL_01_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  U_POLYNOMIAL_01_VALUES stores values of the shifted Chebyshev U polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = u_polynomial_01_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'U_POLYNOMIAL_01_VALUES_TEST:' )
  print ( '  Normal end of execution.' )

  return

def u_polynomial_ab ( a, b, m, n, xab ):

#*****************************************************************************80
#
## U_POLYNOMIAL_AB: Chebyshev polynomials UAB(N,X) in [A,B].
#
#  Discussion:
#
#    UAB(n,x) = U(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the domain of definition.
#
#    Input, integer M, the number of evaluation points.
#
#    Input, integer N, the highest polynomial to compute.
#
#    Input, real XAB(M,1), the evaluation points.
#    It must be the case that A <= XAB(*) <= B.
#
#    Output, real V(M,N+1), the values of the Chebyshev polynomials.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = u_polynomial ( m, n, x );
 
  return v

def u_polynomial_ab_test ( ):

#*****************************************************************************80
#
## U_POLYNOMIAL_AB_TEST tests U_POLYNOMIAL_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'U_POLYNOMIAL_AB_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  U_POLYNOMIAL_AB evaluates Chebyshev polynomials UAB(n,x)' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'U_POLYNOMIAL_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def u_polynomial_ab_value ( a, b, n, xab ):

#*****************************************************************************80
#
## U_POLYNOMIAL_AB: Chebyshev polynomial UAB(N,X) in [A,B].
#
#  Discussion:
#
#    UAB(n,x) = U(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the domain of definition.
#
#    Input, integer N, the degree of the polynomial.
#
#    Input, real XAB, the evaluation points.
#    A <= XAB <= B.
#
#    Output, real V, the value.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = u_polynomial_value ( n, x );
 
  return v

def u_polynomial_ab_value_test ( ):

#*****************************************************************************80
#
## U_POLYNOMIAL_AB_VALUE_TEST tests U_POLYNOMIAL_AB_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'U_POLYNOMIAL_AB_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  U_POLYNOMIAL_AB_VALUE evaluates a Chebyshev polynomial UAB(n,x)' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'U_POLYNOMIAL_AB_VALUE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def u_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## U_POLYNOMIAL_COEFFICIENTS: coefficients of the Chebyshev polynomial U(n,x).
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    Output, real C(1:N+1,1:N+1), the coefficients of the Chebyshev T
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
## U_POLYNOMIAL_COEFFICIENTS_TEST tests U_POLYNOMIAL_COEFFICIENTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'U_POLYNOMIAL_COEFFICIENTS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  U_POLYNOMIAL_COEFFICIENTS determines the Chebyshev' )
  print ( '  polynomial coefficients.' )

  c = u_polynomial_coefficients ( n )
 
  for i in range ( 0, n + 1 ):
    c2 = np.zeros ( i + 1 )
    for j in range ( 0, i + 1 ):
      c2[j] = c[i,j]
    r8poly_print ( i, c2, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'U_POLYNOMIAL_COEFFICIENTS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def u_polynomial_plot ( n_num, n_val, filename ):

#*****************************************************************************80
#
## U_POLYNOMIAL_PLOT plots Chebyshev polynomials U(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N_NUM, the number of polynomials to plot.
#
#    Input, integer N_VAL(N_NUM), the degree of each polynomial.
#
#    Input, string FILENAME, the name into which the graphics information is
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
  plt.clf ( )

  print ( '  Created plot file "%s".' % ( filename ) )

  return

def u_polynomial_plot_test ( ):

#*****************************************************************************80
#
## U_POLYNOMIAL_PLOT_TEST tests U_POLYNOMIAL_PLOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'U_POLYNOMIAL_PLOT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Plot several Chebyshev U polynomials.' )

  n_num = 6
  n_val = np.array ( [ 0, 1, 2, 3, 4, 5 ] )
  filename = 'u_polynomial_plot.png'

  u_polynomial_plot ( n_num, n_val, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'U_POLYNOMIAL_PLOT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def u_polynomial ( m, n, x ):

#*****************************************************************************80
#
## U_POLYNOMIAL evaluates Chebyshev polynomials U(n,x).
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2012
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of evaluation points.
#
#    Input, integer N, the highest polynomial to compute.
#
#    Input, real X(M,1), the evaluation points.
#
#    Output, real V(1:M,1:N+1), the values of the N+1 Chebyshev polynomials.
#
  import numpy as np
  from sys import exit

  if ( n < 0 ):
    print ( '' )
    print ( 'U_POLYNOMIAL - Fatal error!' )
    print ( '  N < 0' )
    exit ( 'U_POLYNOMIAL - Fatal error.' )

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
## U_POLYNOMIAL_TEST tests U_POLYNOMIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'U_POLYNOMIAL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  U_POLYNOMIAL evaluates the Chebyshev polynomial U(n,x).' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'U_POLYNOMIAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def u_polynomial_value ( n, x ):

#*****************************************************************************80
#
## U_POLYNOMIAL_VALUE: returns the single value U(n,x).
#
#  Discussion:
#
#    In cases where calling U_POLYNOMIAL is inconvenient, because it returns
#    a vector of values for multiple arguments X, this simpler interface
#    may be appropriate.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the polynomial.
#
#    Input, real X, the argument of the polynomial.
#
#    Output, real VALUE, the value of U(n,x).
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
## U_POLYNOMIAL_VALUE_TEST tests U_POLYNOMIAL_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'U_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  U_POLYNOMIAL_VALUE evaluates the Chebyshev polynomial U(n,x).' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'U_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def u_polynomial_values ( n_data ):

#*****************************************************************************80
#
## U_POLYNOMIAL_VALUES returns values of Chebyshev polynomials U(n,x).
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      ChebyshevU[n,x]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#    Output, real FX, the value of the function.
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
## U_POLYNOMIAL_VALUES_TEST demonstrates the use of U_POLYNOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'U_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  U_POLYNOMIAL_VALUES stores values of the Chebyshev U polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = u_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'U_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def u_polynomial_zeros ( n ):

#*****************************************************************************80
#
## U_POLYNOMIAL_ZEROS returns zeroes of the Chebyshev polynomial T(n,x).
#
#  Discussion:
#
#    The I-th zero of U(n,x) is cos((I-1)*PI/(N-1)), I = 1 to N
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the polynomial.
#
#    Output, real Z(N), the zeroes.
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
## U_POLYNOMIAL_ZEROS_TEST tests U_POLYNOMIAL_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'U_POLYNOMIAL_ZEROS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  U_POLYNOMIAL_ZEROS computes the zeros of U(n,x)' )
  print ( '' )
  print ( '     N      X         U(n,x)' )

  for n in range ( 0, 6 ):

    x = u_polynomial_zeros ( n )
    fx = u_polynomial ( n, n + 1, x )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %8.4g  %14.6g' % ( i, x[i], fx[i,n] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'U_POLYNOMIAL_ZEROS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def u_quadrature_rule ( n ):

#*****************************************************************************80
#
## U_QUADRATURE_RULE: quadrature rule for U(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the rule.
#
#    Output, real T(N,1), W(N,1), the points and weights of the rule.
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
## U_QUADRATURE_RULE_TEST tests U_QUADRATURE_RULE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'U_QUADRATURE_RULE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  U_QUADRATURE_RULE computes the quadrature rule' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'U_QUADRATURE_RULE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def uu_product_integral ( i, j ):

#*****************************************************************************80
#
## UU_PRODUCT_INTEGRAL: integral (-1<=x<=1) U(i,x)*U(j,x)*sqrt(1-x^2) dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the polynomial indices.
#    0 <= I, J.
#
#    Output, real VALUE, the value of the integral.
#
  import numpy as np
  from sys import exit

  if ( i < 0 ):
    print ( '' )
    print ( 'UU_PRODUCT_INTEGRAL - Fatal error!' )
    print ( '  0 <= I is required.' )
    exit ( 'UU_PRODUCT_INTEGRAL - Fatal error!' )

  if ( j < 0 ):
    print ( '' )
    print ( 'UU_PRODUCT_INTEGRAL - Fatal error!' )
    print ( '  0 <= J is required.' )
    exit ( 'UU_PRODUCT_INTEGRAL - Fatal error!' )

  if ( i != j ):
    value = 0.0
  else:
    value = np.pi / 2.0

  return value

def uu_product_integral_test ( ):

#*****************************************************************************80
#
## UU_PRODUCT_INTEGRAL_TEST tests UU_PRODUCT_INTEGRAL.
#
#  Discussion:
#
#    This process should match the UU_MASS_MATRIX computation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'UU_PRODUCT_INTEGRAL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UU_PRODUCT_INTEGRAL computes the product integral' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'UU_PRODUCT_INTEGRAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def uu_product ( i, j, x ):

#*****************************************************************************80
#
## UU_PRODUCT: evaluate U(i,x)*U(j,x)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the indices.
#
#    Input, real X, the argument.
#
#    Output, real VALUE, the value.
#
  value = 0.0
  for k in range ( abs ( i - j ), i + j + 1, 2 ):
    value = value + u_polynomial_value ( k, x )

  return value

def uu_product_test ( ):

#*****************************************************************************80
#
## UU_PRODUCT_TEST tests UU_PRODUCT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'UU_PRODUCT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UU_PRODUCT(I,J;X) = U(I,X) * U(J,X)' )

  r8_lo = -1.0
  r8_hi = +1.0
  seed = 123456789

  print ( '' )
  print ( '   I   J      X               UI              UJ              UI*UJ       UU_PRODUCT' )
  print ( '' )
  for test in range ( 0, 10 ):
    x, seed = r8_uniform_ab ( r8_lo, r8_hi, seed )
    i, seed = i4_uniform_ab ( 0, 6, seed )
    ui = u_polynomial_value ( i, x )
    j, seed = i4_uniform_ab ( -1, 4, seed )
    uj = u_polynomial_value ( j, x )
    uiuj = uu_product ( i, j, x )
    print ( '  %2d  %2d  %14.6g  %14.6g  %14.6g  %14.6g  %14.6g'\
      % ( i, j, x, ui, uj, ui * uj, uiuj ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'UU_PRODUCT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def v_mass_matrix ( n ):

#*****************************************************************************80
#
## V_MASS_MATRIX computes the mass matrix for the Chebyshev V polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
## V_MASS_MATRIX_TEST tests V_MASS_MATRIX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'V_MASS_MATRIX_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  V_MASS_MATRIX computes the mass matrix for the' )
  print ( '  Chebyshev polynomials V(i,x).' )
  print ( '  A(I,J) = integral ( -1 <=x <= +1 ) V(i,x) V(j,x) sqrt(1+x)/sqrt(1-x) dx' )
  print ( '  0  if i is not equal to j' )
  print ( '  pi if i = j =/= 0.' )

  n = 3

  a = v_mass_matrix ( n )

  r8mat_print ( n + 1, n + 1, a, '  V mass matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'V_MASS_MATRIX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def v_moment ( e ):

#*****************************************************************************80
#
## V_MOMENT: integral ( -1 <= x <= +1 ) x^e sqrt(1+x) / sqrt(1-x) dx.
#
#  Discussion:
#
#    This function returns the moments of the distribution associated
#    with the Chebyshev V polynomial.
#
#     E  V_MOMENT
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer E, the exponent of X.
#    0 <= E.
#
#    Output, real VALUE, the value of the integral.
#
  import numpy as np

  r8_e = float ( e )

  f1 = 1.0 / r8_gamma ( 1.5 + r8_e )
  f2 = r8_mop ( e )
  f3 = np.pi * r8_gamma ( 1.5 + r8_e )
  f4 = 2.0 * r8_hyper_2f1 ( 0.5, - r8_e, 1.0, 2.0 )
  f5 = ( -1.0 + r8_mop ( e ) ) * r8_hyper_2f1 ( 0.5, - r8_e, 2.0, 2.0 )
  f6 = np.sqrt ( np.pi ) * r8_factorial ( e )
  f7 = ( - 1.0 + r8_mop ( e ) ) * r8_hyper_2f1 ( -0.5, 1.0 + r8_e, 1.5 + r8_e, - 1.0 )
  f8 = 2.0 * r8_hyper_2f1 ( 0.5, 1.0 + r8_e, 1.5 + r8_e, -1.0 )

  value = f1 * f2 * ( f3 * ( f4 + f5 ) - f6 * ( f7 + f8 ) );

  return value

def v_moment_test ( ):

#*****************************************************************************80
#
## V_MOMENT_TEST tests V_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'V_MOMENT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  V_MOMENT returns the value of' )
  print ( '  integral ( -1 <=x <= +1 ) x^e * sqrt(1+x) / sqrt(1-x) dx' )
  print ( '' )
  print ( '   E       Integral' )
  print ( '' )
  for e in range ( 0, 11 ):
    value = v_moment ( e )
    print ( '  %2d  %14.6g' % ( e, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'V_MOMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def v_polynomial_01_values ( n_data ):

#*****************************************************************************80
#
## V_POLYNOMIAL_01_VALUES: values of shifted Chebyshev polynomials V01(n,x).
#
#  Discussion:
#
#    V01(n,x) = V(n,2*x-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#    Output, real FX, the value of the function.
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
## V_POLYNOMIAL_01_VALUES_TEST demonstrates the use of V_POLYNOMIAL_01_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'V_POLYNOMIAL_01_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  V_POLYNOMIAL_01_VALUES stores values of the shifted Chebyshev V polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = v_polynomial_01_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'V_POLYNOMIAL_01_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def v_polynomial_ab ( a, b, m, n, xab ):

#*****************************************************************************80
#
## V_POLYNOMIAL_AB: Chebyshev polynomials VAB(N,X) in [A,B].
#
#  Discussion:
#
#    VAB(n,x) = V(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the domain of definition.
#
#    Input, integer M, the number of evaluation points.
#
#    Input, integer N, the highest polynomial to compute.
#
#    Input, real XAB(M,1), the evaluation points.
#    It must be the case that A <= XAB(*) <= B.
#
#    Output, real V(M,N+1), the values of the Chebyshev polynomials.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = v_polynomial ( m, n, x );
 
  return v

def v_polynomial_ab_test ( ):

#*****************************************************************************80
#
## V_POLYNOMIAL_AB_TEST tests V_POLYNOMIAL_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'V_POLYNOMIAL_AB_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  V_POLYNOMIAL_AB evaluates Chebyshev polynomials VAB(n,x)' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'V_POLYNOMIAL_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def v_polynomial_ab_value ( a, b, n, xab ):

#*****************************************************************************80
#
## V_POLYNOMIAL_AB: Chebyshev polynomial VAB(N,X) in [A,B].
#
#  Discussion:
#
#    VAB(n,x) = V(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the domain of definition.
#
#    Input, integer N, the degree of the polynomial.
#
#    Input, real XAB, the evaluation points.
#    A <= XAB <= B.
#
#    Output, real V, the value.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = v_polynomial_value ( n, x );
 
  return v

def v_polynomial_ab_value_test ( ):

#*****************************************************************************80
#
## V_POLYNOMIAL_AB_VALUE_TEST tests V_POLYNOMIAL_AB_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'V_POLYNOMIAL_AB_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  V_POLYNOMIAL_AB_VALUE evaluates a Chebyshev polynomial VAB(n,x)' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'V_POLYNOMIAL_AB_VALUE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def v_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## V_POLYNOMIAL_COEFFICIENTS: coefficients of the Chebyshev polynomial V(n,x).
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    Output, real C(1:N+1,1:N+1), the coefficients of the polynomials.
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
## V_POLYNOMIAL_COEFFICIENTS_TEST tests V_POLYNOMIAL_COEFFICIENTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'V_POLYNOMIAL_COEFFICIENTS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  V_POLYNOMIAL_COEFFICIENTS determines the Chebyshev' )
  print ( '  polynomial coefficients.' )

  c = v_polynomial_coefficients ( n )
 
  for i in range ( 0, n + 1 ):
    c2 = np.zeros ( i + 1 )
    for j in range ( 0, i + 1 ):
      c2[j] = c[i,j]
    r8poly_print ( i, c2, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'V_POLYNOMIAL_COEFFICIENTS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def v_polynomial_plot ( n_num, n_val, filename ):

#*****************************************************************************80
#
## V_POLYNOMIAL_PLOT plots Chebyshev polynomials V(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N_NUM, the number of polynomials to plot.
#
#    Input, integer N_VAL(N_NUM), the degree of each polynomial.
#
#    Input, string FILENAME, the name into which the graphics information is
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
  plt.clf ( )

  print ( '  Created plot file "%s".' % ( filename ) )

  return

def v_polynomial_plot_test ( ):

#*****************************************************************************80
#
## V_POLYNOMIAL_PLOT_TEST tests V_POLYNOMIAL_PLOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'V_POLYNOMIAL_PLOT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Plot several Chebyshev V polynomials.' )

  n_num = 6
  n_val = np.array ( [ 0, 1, 2, 3, 4, 5 ] )
  filename = 'v_polynomial_plot.png'

  v_polynomial_plot ( n_num, n_val, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'V_POLYNOMIAL_PLOT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def v_polynomial ( m, n, x ):

#*****************************************************************************80
#
## V_POLYNOMIAL evaluates Chebyshev polynomials V(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 July 2105
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of evaluation points.
#
#    Input, integer N, the highest polynomial to compute.
#
#    Input, real X(M,1), the evaluation points.
#
#    Output, real V(1:M,1:N+1), the values of the N+1 Chebyshev polynomials.
#
  import numpy as np
  from sys import exit

  if ( n < 0 ):
    print ( '' )
    print ( 'V_POLYNOMIAL - Fatal error!' )
    print ( '  N < 0' )
    exit ( 'V_POLYNOMIAL - Fatal error.' )

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
## V_POLYNOMIAL_TEST tests V_POLYNOMIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'V_POLYNOMIAL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  V_POLYNOMIAL evaluates the Chebyshev polynomial V(n,x).' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'V_POLYNOMIAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def v_polynomial_value ( n, x ):

#*****************************************************************************80
#
## V_POLYNOMIAL_VALUE: returns the single value V(n,x).
#
#  Discussion:
#
#    In cases where calling V_POLYNOMIAL is inconvenient, because it returns
#    a vector of values for multiple arguments X, this simpler interface
#    may be appropriate.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the polynomial.
#
#    Input, real X, the argument of the polynomial.
#
#    Output, real VALUE, the value of V(n,x).
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
## V_POLYNOMIAL_VALUE_TEST tests V_POLYNOMIAL_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'V_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  V_POLYNOMIAL_VALUE evaluates the Chebyshev polynomial V(n,x).' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'V_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def v_polynomial_values ( n_data ):

#*****************************************************************************80
#
## V_POLYNOMIAL_VALUES returns values of Chebyshev polynomials V(n,x).
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
#    This code is distributed under the GNU LGPL license.
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
#    Output, real FX, the value of the function.
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
## V_POLYNOMIAL_VALUES_TEST demonstrates the use of V_POLYNOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'V_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  V_POLYNOMIAL_VALUES stores values of the Chebyshev V polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = v_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'V_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def v_polynomial_zeros ( n ):

#*****************************************************************************80
#
## V_POLYNOMIAL_ZEROS returns zeroes of the Chebyshev polynomial V(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the polynomial.
#
#    Output, real Z(N), the zeroes.
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
## V_POLYNOMIAL_ZEROS_TEST tests V_POLYNOMIAL_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'V_POLYNOMIAL_ZEROS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  V_POLYNOMIAL_ZEROS computes the zeros of V(n,x)' )
  print ( '' )
  print ( '     N      X         V(n,x)' )

  for n in range ( 0, 6 ):

    x = v_polynomial_zeros ( n )
    fx = v_polynomial ( n, n + 1, x )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %8.4g  %14.6g' % ( i, x[i], fx[i,n] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'V_POLYNOMIAL_ZEROS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def v_quadrature_rule ( n ):

#*****************************************************************************80
#
## V_QUADRATURE_RULE: quadrature rule for V(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the rule.
#
#    Output, real T(N,1), W(N,1), the points and weights of the rule.
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
## V_QUADRATURE_RULE_TEST tests V_QUADRATURE_RULE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'V_QUADRATURE_RULE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  V_QUADRATURE_RULE computes the quadrature rule' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'V_QUADRATURE_RULE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def vv_product_integral ( i, j ):

#*****************************************************************************80
#
## VV_PRODUCT_INTEGRAL: integral (-1<=x<=1) V(i,x)*V(j,x)*sqrt(1+x)/sqrt(1-x) dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the polynomial indices.
#    0 <= I, J.
#
#    Output, real VALUE, the value of the integral.
#
  import numpy as np
  from sys import exit

  if ( i < 0 ):
    print ( '' )
    print ( 'VV_PRODUCT_INTEGRAL - Fatal error!' )
    print ( '  0 <= I is required.' )
    exit ( 'VV_PRODUCT_INTEGRAL - Fatal error!' )

  if ( j < 0 ):
    print ( '' )
    print ( 'VV_PRODUCT_INTEGRAL - Fatal error!' )
    print ( '  0 <= J is required.' )
    exit ( 'VV_PRODUCT_INTEGRAL - Fatal error!' )

  if ( i != j ):
    value = 0.0
  else:
    value = np.pi

  return value

def vv_product_integral_test ( ):

#*****************************************************************************80
#
## VV_PRODUCT_INTEGRAL_TEST tests VV_PRODUCT_INTEGRAL.
#
#  Discussion:
#
#    This process should match the VV_MASS_MATRIX computation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'VV_PRODUCT_INTEGRAL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  VV_PRODUCT_INTEGRAL computes the product integral' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'VV_PRODUCT_INTEGRAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def w_mass_matrix ( n ):

#*****************************************************************************80
#
## W_MASS_MATRIX computes the mass matrix for the Chebyshev W polynomial.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
## W_MASS_MATRIX_TEST tests W_MASS_MATRIX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'W_MASS_MATRIX_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  W_MASS_MATRIX computes the mass matrix for the' )
  print ( '  Chebyshev polynomials W(i,x).' )
  print ( '  A(I,J) = integral ( -1 <=x <= +1 ) W(i,x) W(j,x) sqrt(1-x)/sqrt(1+x) dx' )
  print ( '  0  if i is not equal to j' )
  print ( '  pi if i = j.' )

  n = 3

  a = w_mass_matrix ( n )

  r8mat_print ( n + 1, n + 1, a, '  W mass matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'W_MASS_MATRIX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def w_moment ( e ):

#*****************************************************************************80
#
## W_MOMENT: integral ( -1 <= x <= +1 ) x^e sqrt(1-x) / sqrt(1+x) dx.
#
#  Discussion:
#
#    This function returns the moments of the distribution associated
#    with the Chebyshev W polynomial.
#
#     E  W_MOMENT
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer E, the exponent of X.
#    0 <= E.
#
#    Output, real VALUE, the value of the integral.
#
  import numpy as np

  r8_e = float ( e )

  f1 = 1.0 / r8_gamma ( 1.5 + r8_e )
  f2 = r8_mop ( e )
  f3 = np.pi * r8_gamma ( 1.5 + r8_e )
  f4 = 2.0 * r8_mop ( e ) * r8_hyper_2f1 ( 0.5, - r8_e, 1.0, 2.0 )
  f5 = ( -1.0 + r8_mop ( e ) ) * r8_hyper_2f1 ( 0.5, - r8_e, 2.0, 2.0 )
  f6 = np.sqrt ( np.pi ) * r8_factorial ( e )
  f7 = ( - 1.0 + r8_mop ( e ) ) * r8_hyper_2f1 ( -0.5, 1.0 + r8_e, 1.5 + r8_e, - 1.0 )
  f8 = 2.0 * r8_mop ( e ) * r8_hyper_2f1 ( 0.5, 1.0 + r8_e, 1.5 + r8_e, -1.0 )

  value = f1 * f2 * ( f3 * ( f4 - f5 ) + f6 * ( f7 - f8 ) )

  return value

def w_moment_test ( ):

#*****************************************************************************80
#
## W_MOMENT_TEST tests W_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'W_MOMENT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  W_MOMENT returns the value of' )
  print ( '  integral ( -1 <=x <= +1 ) x^e * sqrt(1-x) / sqrt(1+x) dx' )
  print ( '' )
  print ( '   E       Integral' )
  print ( '' )
  for e in range ( 0, 11 ):
    value = w_moment ( e )
    print ( '  %2d  %14.6g' % ( e, value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'W_MOMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def w_polynomial_01_values ( n_data ):

#*****************************************************************************80
#
## W_POLYNOMIAL_01_VALUES: values of shifted Chebyshev polynomials W01(n,x).
#
#  Discussion:
#
#    W01(n,x) = W(n,2*x-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#    Output, real FX, the value of the function.
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
## W_POLYNOMIAL_01_VALUES_TEST demonstrates the use of W_POLYNOMIAL_01_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'W_POLYNOMIAL_01_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  W_POLYNOMIAL_01_VALUES stores values of the shifted Chebyshev W polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = w_polynomial_01_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'W_POLYNOMIAL_01_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def w_polynomial_ab ( a, b, m, n, xab ):

#*****************************************************************************80
#
## W_POLYNOMIAL_AB: Chebyshev polynomials WAB(N,X) in [A,B].
#
#  Discussion:
#
#    WAB(n,x) = W(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the domain of definition.
#
#    Input, integer M, the number of evaluation points.
#
#    Input, integer N, the highest polynomial to compute.
#
#    Input, real XAB(M,1), the evaluation points.
#    A <= XAB(*) <= B.
#
#    Output, real V(M,N+1), the values of the Chebyshev polynomials.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = w_polynomial ( m, n, x );
 
  return v

def w_polynomial_ab_test ( ):

#*****************************************************************************80
#
## W_POLYNOMIAL_AB_TEST tests W_POLYNOMIAL_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'W_POLYNOMIAL_AB_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  W_POLYNOMIAL_AB evaluates Chebyshev polynomials WAB(n,x)' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'W_POLYNOMIAL_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def w_polynomial_ab_value ( a, b, n, xab ):

#*****************************************************************************80
#
## W_POLYNOMIAL_AB: Chebyshev polynomial WAB(N,X) in [A,B].
#
#  Discussion:
#
#    WAB(n,x) = W(n,(2*x-a-b)/(b-a))
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the domain of definition.
#
#    Input, integer N, the degree of the polynomial.
#
#    Input, real XAB, the evaluation points.
#    A <= XAB <= B.
#
#    Output, real V, the value.
#
  x = ( 2.0 * xab - a - b ) / ( b - a )

  v = w_polynomial_value ( n, x );
 
  return v

def w_polynomial_ab_value_test ( ):

#*****************************************************************************80
#
## W_POLYNOMIAL_AB_VALUE_TEST tests W_POLYNOMIAL_AB_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
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
  print ( 'W_POLYNOMIAL_AB_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  W_POLYNOMIAL_AB_VALUE evaluates a Chebyshev polynomial WAB(n,x)' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'W_POLYNOMIAL_AB_VALUE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def w_polynomial_coefficients ( n ):

#*****************************************************************************80
#
## W_POLYNOMIAL_COEFFICIENTS: coefficients of the Chebyshev polynomial W(n,x).
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
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the highest order polynomial to compute.
#    Note that polynomials 0 through N will be computed.
#
#    Output, real C(1:N+1,1:N+1), the coefficients of the polynomials.
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
## W_POLYNOMIAL_COEFFICIENTS_TEST tests W_POLYNOMIAL_COEFFICIENTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'W_POLYNOMIAL_COEFFICIENTS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  W_POLYNOMIAL_COEFFICIENTS determines the Chebyshev' )
  print ( '  polynomial coefficients.' )

  c = w_polynomial_coefficients ( n )
 
  for i in range ( 0, n + 1 ):
    c2 = np.zeros ( i + 1 )
    for j in range ( 0, i + 1 ):
      c2[j] = c[i,j]
    r8poly_print ( i, c2, '' )
#
#  Terminate.
#
  print ( '' )
  print ( 'W_POLYNOMIAL_COEFFICIENTS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def w_polynomial_plot ( n_num, n_val, filename ):

#*****************************************************************************80
#
## W_POLYNOMIAL_PLOT plots Chebyshev polynomials W(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N_NUM, the number of polynomials to plot.
#
#    Input, integer N_VAL(N_NUM), the degree of each polynomial.
#
#    Input, string FILENAME, the name into which the graphics information is
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
  plt.clf ( )

  print ( '  Created plot file "%s".' % ( filename ) )

  return

def w_polynomial_plot_test ( ):

#*****************************************************************************80
#
## W_POLYNOMIAL_PLOT_TEST tests W_POLYNOMIAL_PLOT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'W_POLYNOMIAL_PLOT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Plot several Chebyshev W polynomials.' )

  n_num = 6
  n_val = np.array ( [ 0, 1, 2, 3, 4, 5 ] )
  filename = 'w_polynomial_plot.png'

  w_polynomial_plot ( n_num, n_val, filename )
#
#  Terminate.
#
  print ( '' )
  print ( 'W_POLYNOMIAL_PLOT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def w_polynomial ( m, n, x ):

#*****************************************************************************80
#
## W_POLYNOMIAL evaluates Chebyshev polynomials W(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of evaluation points.
#
#    Input, integer N, the highest polynomial to compute.
#
#    Input, real X(M,1), the evaluation points.
#
#    Output, real V(1:M,1:N+1), the values of the N+1 Chebyshev polynomials.
#
  import numpy as np
  from sys import exit

  if ( n < 0 ):
    print ( '' )
    print ( 'W_POLYNOMIAL - Fatal error!' )
    print ( '  N < 0' )
    exit ( 'W_POLYNOMIAL - Fatal error.' )

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
## W_POLYNOMIAL_TEST tests W_POLYNOMIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'W_POLYNOMIAL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  W_POLYNOMIAL evaluates the Chebyshev polynomial W(n,x).' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'W_POLYNOMIAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

def w_polynomial_value ( n, x ):

#*****************************************************************************80
#
## W_POLYNOMIAL_VALUE: returns the single value W(n,x).
#
#  Discussion:
#
#    In cases where calling W_POLYNOMIAL is inconvenient, because it returns
#    a vector of values for multiple arguments X, this simpler interface
#    may be appropriate.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the polynomial.
#
#    Input, real X, the argument of the polynomial.
#
#    Output, real VALUE, the value of W(n,x).
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
## W_POLYNOMIAL_VALUE_TEST tests W_POLYNOMIAL_VALUE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'W_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  W_POLYNOMIAL_VALUE evaluates the Chebyshev polynomial W(n,x).' )
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
# 
#  Terminate.
#
  print ( '' )
  print ( 'W_POLYNOMIAL_VALUE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def w_polynomial_values ( n_data ):

#*****************************************************************************80
#
## W_POLYNOMIAL_VALUES returns values of Chebyshev polynomials W(n,x).
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
#    This code is distributed under the GNU LGPL license.
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
#    Output, real FX, the value of the function.
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
## W_POLYNOMIAL_VALUES_TEST demonstrates the use of W_POLYNOMIAL_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'W_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  W_POLYNOMIAL_VALUES stores values of the Chebyshev W polynomials.' )
  print ( '' )
  print ( '      N            X            FX' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, x, fx = w_polynomial_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '  %6d  %12f  %24.16g' % ( n, x, fx ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'W_POLYNOMIAL_VALUES_TEST:' )
  print ( '  Normal end of execution.' )
  return

def w_polynomial_zeros ( n ):

#*****************************************************************************80
#
## W_POLYNOMIAL_ZEROS returns zeroes of the Chebyshev polynomial W(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the polynomial.
#
#    Output, real Z(N), the zeroes.
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
## W_POLYNOMIAL_ZEROS_TEST tests W_POLYNOMIAL_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'W_POLYNOMIAL_ZEROS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  W_POLYNOMIAL_ZEROS computes the zeros of W(n,x)' )
  print ( '' )
  print ( '     N      X         W(n,x)' )

  for n in range ( 0, 6 ):

    x = w_polynomial_zeros ( n )
    fx = w_polynomial ( n, n + 1, x )

    print ( '' )
    for i in range ( 0, n ):
      print ( '  %4d  %8.4g  %14.6g' % ( i, x[i], fx[i,n] ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'W_POLYNOMIAL_ZEROS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def w_quadrature_rule ( n ):

#*****************************************************************************80
#
## W_QUADRATURE_RULE: quadrature rule for W(n,x).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the rule.
#
#    Output, real T(N,1), W(N,1), the points and weights of the rule.
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
## W_QUADRATURE_RULE_TEST tests W_QUADRATURE_RULE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'W_QUADRATURE_RULE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  W_QUADRATURE_RULE computes the quadrature rule' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'W_QUADRATURE_RULE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def ww_product_integral ( i, j ):

#*****************************************************************************80
#
## WW_PRODUCT_INTEGRAL: integral (-1<=x<=1) W(i,x)*W(j,x)*sqrt(1-x)/sqrt(1+x) dx
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, J, the polynomial indices.
#    0 <= I, J.
#
#    Output, real VALUE, the value of the integral.
#
  import numpy as np
  from sys import exit

  if ( i < 0 ):
    print ( '' )
    print ( 'WW_PRODUCT_INTEGRAL - Fatal error!' )
    print ( '  0 <= I is required.' )
    exit ( 'WW_PRODUCT_INTEGRAL - Fatal error!' )

  if ( j < 0 ):
    print ( '' )
    print ( 'WW_PRODUCT_INTEGRAL - Fatal error!' )
    print ( '  0 <= J is required.' )
    exit ( 'WW_PRODUCT_INTEGRAL - Fatal error!' )

  if ( i != j ):
    value = 0.0
  else:
    value = np.pi

  return value

def ww_product_integral_test ( ):

#*****************************************************************************80
#
## WW_PRODUCT_INTEGRAL_TEST tests WW_PRODUCT_INTEGRAL.
#
#  Discussion:
#
#    This process should match the WW_MASS_MATRIX computation.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'WW_PRODUCT_INTEGRAL_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WW_PRODUCT_INTEGRAL computes the product integral' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'WW_PRODUCT_INTEGRAL_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  chebyshev_polynomial_test ( )
  timestamp ( )

