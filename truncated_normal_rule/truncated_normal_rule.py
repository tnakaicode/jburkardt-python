#! /usr/bin/env python3
#
def truncated_normal_rule_test ( ):

#*****************************************************************************80
#
## truncated_normal_rule_test() tests truncated_normal_rule().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'truncated_normal_rule_test():' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test truncated_normal_rule().' )
#
#  Utilities.
#
  r8_mop_test ( )
  r8vec_write_test ( )
  rule_write_test ( )
#
#  Library functions.
#
  normal_01_cdf_test ( )
  normal_01_moment_test ( )
  normal_01_pdf_test ( )
  normal_ms_moment_test ( )
  truncated_normal_a_moment_test ( )
  truncated_normal_ab_moment_test ( )
  truncated_normal_b_moment_test ( )
  moment_method_test ( )
#
#  Direct calls to truncated_normal_rule:
#
  option0_test ( )
  option1_test ( )
  option2_test ( )
  option3_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'truncated_normal_rule_test():' )
  print ( '  Normal end of execution.' )
  return

def moment_method ( n, moments ):

#*****************************************************************************80
#
## moment_method() computes a quadrature rule by the method of moments.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, John Welsch,
#    Calculation of Gaussian Quadrature Rules,
#    Mathematics of Computation,
#    Volume 23, Number 106, April 1969, pages 221-230.
#
#  Input:
#
#    integer N, the order of the quadrature rule.
#
#    real MOMENTS(2*N+1), moments 0 through 2*N.
#
#  Output:
#
#    real X(N), W(N), the points and weights of the quadrature rule.
#
  import numpy as np

  debug = False

  if ( debug ):
    r8vec_print ( 2 * n + 1, moments, '  Moments:' )
#
#  Define the N+1 by N+1 Hankel matrix H(I,J) = moment(I+J).
#
  h = np.zeros ( ( n + 1, n + 1 ) )

  for i in range ( 0, n + 1 ):
    for j in range ( 0, n + 1 ):
      h[i,j] = moments[i+j]

  if ( debug ):
    r8mat_print ( n + 1, n + 1, h, '  Hankel matrix H:' )
#
#  Compute R, the upper triangular Cholesky factor of H.
#
  r = np.linalg.cholesky ( h )
  r = np.transpose ( r )

  if ( debug ):
    r8mat_print ( n + 1, n + 1, r, '  Upper triangular Cholesky factor R:' )
#
#  Compute ALPHA and BETA from R, using Golub and Welsch's formula.
#
  alpha = np.zeros ( n )

  alpha[0] = r[0,1] / r[0,0]
  for i in range ( 1, n ):
    alpha[i] = r[i,i+1] / r[i,i] - r[i-1,i] / r[i-1,i-1]

  beta = np.zeros ( n - 1 )
  for i in range ( 0, n - 1 ):
    beta[i] = r[i+1,i+1] / r[i,i]
#
#  Set up the tridiagonal Jacobi matrix.
#
  jacobi = np.diag ( alpha, k = 0 ) \
         + np.diag ( beta, k = -1 ) \
         + np.diag ( beta, k = +1 )

  if ( debug ):
    r8mat_print ( n, n, jacobi, '  Jacobi matrix: ' )
#
#  Get the eigendecomposition of the Jacobi matrix.
#
  x, eigvec = np.linalg.eig ( jacobi )

  w = np.zeros ( n )
  for j in range ( 0, n ):
    w[j] = moments[0] * ( float ( eigvec[0,j] ) ) ** 2
#
#  Sort X, and W accordingly.
#
  for j in range ( 0, n ):
    for i in range ( j + 1, n ):
      if ( x[i] < x[j] ):
        t = x[i]
        x[i] = x[j]
        x[j] = t
        t = w[i]
        w[i] = w[j]
        w[j] = t 

  return x, w

def moment_method_test ( ):

#*****************************************************************************80
#
## moment_method_test() tests moment_method().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'moment_method_test' )
  print ( '  moment_method uses the method of moments for a quadrature rule.' )

  n = 5
  tnp1 = 2 * n + 1
  
  moments = np.zeros ( tnp1 )

  for i in range ( 0, tnp1 ):
    moments[i] = normal_01_moment ( i )

  x, w = moment_method ( n, moments )

  x_correct = np.array ( [ \
     -2.85697001387280565416230426401, \
     -1.35562617997426586583052129087, \
      0.0, \
     +1.35562617997426586583052129087, \
     +2.85697001387280565416230426401 ] )

  w_correct = np.array ( [ \
     0.0112574113277206889333702151856, \
     0.222075922005612644399963118148, \
     0.533333333333333333333333333333, \
     0.222075922005612644399963118148, \
     0.0112574113277206889333702151856 ] )

  print ( '' )
  print ( '           Computed        Correct' )
  print ( '   I           X              X' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %14.6g  %14.6g' % ( i, x[i], x_correct[i] ) )

  print ( '' )
  print ( '           Computed        Correct' )
  print ( '   I           W              W' )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %2d  %14.6g  %14.6g' % ( i, w[i], w_correct[i] ) )

  return

def normal_01_cdf ( x ):

#*****************************************************************************80
#
## normal_01_cdf() evaluates the Normal 01 CDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    A G Adams,
#    Areas Under the Normal Curve,
#    Algorithm 39,
#    Computer j.,
#    Volume 12, pages 197-198, 1969.
#
#  Input:
#
#    real X, the argument of the CDF.
#
#  Output:
#
#    real VALUE, the value of the CDF.
# 
  import numpy as np

  a1 = 0.398942280444
  a2 = 0.399903438504
  a3 = 5.75885480458
  a4 = 29.8213557808
  a5 = 2.62433121679
  a6 = 48.6959930692
  a7 = 5.92885724438
  b0 = 0.398942280385
  b1 = 3.8052E-08
  b2 = 1.00000615302
  b3 = 3.98064794E-04
  b4 = 1.98615381364
  b5 = 0.151679116635
  b6 = 5.29330324926
  b7 = 4.8385912808
  b8 = 15.1508972451
  b9 = 0.742380924027
  b10 = 30.789933034
  b11 = 3.99019417011
#
#  |X| <= 1.28.
#
  if ( abs ( x ) <= 1.28 ):

    y = 0.5 * x * x

    q = 0.5 - abs ( x ) * ( a1 - a2 * y / ( y + a3 \
      - a4 / ( y + a5 \
      + a6 / ( y + a7 ) ) ) )
#
#  1.28 < |X| <= 12.7
#
  elif ( abs ( x ) <= 12.7 ):

    y = 0.5 * x * x

    q = np.exp ( - y ) \
      * b0  / ( abs ( x ) - b1 \
      + b2  / ( abs ( x ) + b3 \
      + b4  / ( abs ( x ) - b5 \
      + b6  / ( abs ( x ) + b7 \
      - b8  / ( abs ( x ) + b9 \
      + b10 / ( abs ( x ) + b11 ) ) ) ) ) )
#
#  12.7 < |X|
#
  else:

    q = 0.0
#
#  Take account of negative X.
#
  if ( x < 0.0 ):
    value = q
  else:
    value = 1.0 - q

  return value

def normal_01_cdf_test ( ):

#*****************************************************************************80
#
## normal_01_cdf_test() tests normal_01_cdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'normal_01_cdf_test' )
  print ( '  normal_01_cdf evaluates the CDF;' )
  print ( '' )
  print ( '       X              CDF                       CDF' )
  print ( '                     (exact)                   (computed)' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, x, cdf1 = normal_01_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    cdf2 = normal_01_cdf ( x )

    print ( '  %14.6g  %24.16g  %24.16g' % ( x, cdf1, cdf2 ) )

  return

def normal_01_cdf_values ( n_data ):

#*****************************************************************************80
#
## normal_01_cdf_values() returns some values of the Normal 01 CDF.
#
#  Discussion:
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`ContinuousDistributions`"]
#      dist = NormalDistribution [ 0, 1 ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2015
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

  n_max = 17

  f_vec = np.array ( (\
     0.5000000000000000E+00, \
     0.5398278372770290E+00, \
     0.5792597094391030E+00, \
     0.6179114221889526E+00, \
     0.6554217416103242E+00, \
     0.6914624612740131E+00, \
     0.7257468822499270E+00, \
     0.7580363477769270E+00, \
     0.7881446014166033E+00, \
     0.8159398746532405E+00, \
     0.8413447460685429E+00, \
     0.9331927987311419E+00, \
     0.9772498680518208E+00, \
     0.9937903346742239E+00, \
     0.9986501019683699E+00, \
     0.9997673709209645E+00, \
     0.9999683287581669E+00 ))

  x_vec = np.array ((\
     0.0000000000000000E+00, \
     0.1000000000000000E+00, \
     0.2000000000000000E+00, \
     0.3000000000000000E+00, \
     0.4000000000000000E+00, \
     0.5000000000000000E+00, \
     0.6000000000000000E+00, \
     0.7000000000000000E+00, \
     0.8000000000000000E+00, \
     0.9000000000000000E+00, \
     0.1000000000000000E+01, \
     0.1500000000000000E+01, \
     0.2000000000000000E+01, \
     0.2500000000000000E+01, \
     0.3000000000000000E+01, \
     0.3500000000000000E+01, \
     0.4000000000000000E+01 ))

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

def normal_01_moment ( order ):

#*****************************************************************************80
#
## normal_01_moment() evaluates the moments of the Normal 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ORDER, the order of the moment.
#
#  Output:
#
#    real VALUE, the value of the moment.
#
  from scipy.special import factorial2

  if ( ( order % 2 ) == 0 ):
    value = factorial2 ( order - 1 )
  else:
    value = 0.0

  return value

def normal_01_moment_test ( ):

#*****************************************************************************80
#
## normal_01_moment_test() tests normal_01_moment().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'normal_01_moment_test' )
  print ( '  normal_01_moment evaluates moments of the Normal 01 PDF;' )
  print ( '' )
  print ( '   Order     Moment' )
  print ( '' )

  for order in range ( 0, +11 ):

    moment = normal_01_moment ( order )
    print ( '  %6d  %14.6g' % ( order, moment ) )

  return

def normal_01_pdf ( x ):

#*****************************************************************************80
#
## normal_01_pdf() evaluates the Normal 01 PDF.
#
#  Discussion:
#
#    The Normal 01 PDF is also called the "Standard Normal" PDF, or
#    the Normal PDF with 0 mean and standard deviation 1.
#
#  Formula:
#
#    PDF(x) = exp ( - 0.5 * x^2 ) / sqrt ( 2 * pi )
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real X, the argument of the PDF.
#
#  Output:
#
#    real VALUE, the value of the PDF.
# 
  import numpy as np

  value = np.exp ( - 0.5 * x * x ) / np.sqrt ( 2.0 * np.pi )

  return value

def normal_01_pdf_test ( ):

#*****************************************************************************80
#
## normal_01_pdf_test() tests normal_01_pdf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'normal_01_pdf_test' )
  print ( '  normal_01_pdf evaluates the PDF;' )
  print ( '' )
  print ( '       X              PDF' )
  print ( '' )

  for i in range ( -20, +21 ):

    x = float ( i ) / 10.0
    pdf = normal_01_pdf ( x )
    print ( '  %14.6g  %24.16g' % ( x, pdf ) )

  return

def normal_ms_moments ( order_max, mu, sigma ):

#*****************************************************************************80
#
## normal_ms_moments() evaluates the moments of the Normal MS distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ORDER_MAX, the maximum order of the moments.
#
#    real MU, the mean of the distribution.
#
#    real SIGMA, the standard deviation of the distribution.
#
#  Output:
#
#    real VALUE[0:ORDER_MAX], the value of the moments.
#
  import numpy as np

  value = np.zeros ( order_max + 1 )

  for order in range ( 0, order_max + 1 ):
    value[order] = normal_ms_moment ( order, mu, sigma )

  return value

def normal_ms_moment ( order, mu, sigma ):

#*****************************************************************************80
#
## normal_ms_moment() evaluates a moment of the Normal MS distribution.
#
#  Discussion:
#
#    The formula was posted by John D Cook.
#
#    Order  Moment
#    -----  ------
#      0    1
#      1    mu
#      2    mu ** 2 +         sigma ** 2
#      3    mu ** 3 +  3 mu   sigma ** 2
#      4    mu ** 4 +  6 mu ** 2 sigma ** 2 +   3      sigma ** 4
#      5    mu ** 5 + 10 mu ** 3 sigma ** 2 +  15 mu   sigma ** 4
#      6    mu ** 6 + 15 mu ** 4 sigma ** 2 +  45 mu ** 2 sigma ** 4 +  15      sigma ** 6
#      7    mu ** 7 + 21 mu ** 5 sigma ** 2 + 105 mu ** 3 sigma ** 4 + 105 mu   sigma ** 6
#      8    mu ** 8 + 28 mu ** 6 sigma ** 2 + 210 mu ** 4 sigma ** 4 + 420 mu ** 2 sigma ** 6 + 105 sigma ** 8
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ORDER, the order of the moment.
#
#    real MU, the mean of the distribution.
#
#    real SIGMA, the standard deviation of the distribution.
#
#  Output:
#
#    real VALUE, the value of the moment.
#
  from scipy.special import comb
  from scipy.special import factorial2

  j_hi = ( order // 2 )

  value = 0.0
  for j in range ( 0, j_hi + 1 ):
    value = value \
      + comb ( order, 2 * j ) \
      * factorial2 ( 2 * j - 1 ) \
      * mu ** ( order - 2 * j ) * sigma ** ( 2 * j )

  return value

def normal_ms_moment_values ( order, mu, sigma ):

#*****************************************************************************80
#
## normal_ms_moment_values() evaluates moments 0 through 8 of the Normal PDF.
#
#  Discussion:
#
#    The formula was posted by John D Cook.
#
#    Order  Moment
#    -----  ------
#      0    1
#      1    mu
#      2    mu ** 2 +         sigma ** 2
#      3    mu ** 3 +  3 mu   sigma ** 2
#      4    mu ** 4 +  6 mu ** 2 sigma ** 2 +   3      sigma ** 4
#      5    mu ** 5 + 10 mu ** 3 sigma ** 2 +  15 mu   sigma ** 4
#      6    mu ** 6 + 15 mu ** 4 sigma ** 2 +  45 mu ** 2 sigma ** 4 +  15      sigma ** 6
#      7    mu ** 7 + 21 mu ** 5 sigma ** 2 + 105 mu ** 3 sigma ** 4 + 105 mu   sigma ** 6
#      8    mu ** 8 + 28 mu ** 6 sigma ** 2 + 210 mu ** 4 sigma ** 4 + 420 mu ** 2 sigma ** 6 + 105 sigma ** 8
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ORDER, the order of the moment.
#    0 <= ORDER <= 8.
#
#    real MU, the mean of the distribution.
#
#    real SIGMA, the standard deviation of the distribution.
#
#  Output:
#
#    real VALUE, the value of the central moment.
#
  if ( order == 0 ):
    value = 1.0
  elif ( order == 1 ):
    value = mu
  elif ( order == 2 ):
    value = mu ** 2 + sigma ** 2
  elif ( order == 3 ):
    value = mu ** 3 + 3.0 * mu * sigma ** 2
  elif ( order == 4 ):
    value = mu ** 4 + 6.0 * mu ** 2 * sigma ** 2 + 3.0 * sigma ** 4
  elif ( order == 5 ):
    value = mu ** 5 + 10.0 * mu ** 3 * sigma ** 2 + 15.0 * mu * sigma ** 4
  elif ( order == 6 ):
    value = mu ** 6 + 15.0 * mu ** 4 * sigma ** 2 + 45.0 * mu ** 2 * sigma ** 4 \
      + 15.0 * sigma ** 6
  elif ( order == 7 ):
    value = mu ** 7 + 21.0 * mu ** 5 * sigma ** 2 + 105.0 * mu ** 3 * sigma ** 4 \
      + 105.0 * mu * sigma ** 6
  elif ( order == 8 ):
    value = mu ** 8 + 28.0 * mu ** 6 * sigma ** 2 + 210.0 * mu ** 4 * sigma ** 4 \
      + 420.0 * mu ** 2 * sigma ** 6 + 105.0 * sigma ** 8
  else:
    print ( '' )
    print ( 'normal_ms_moment_values - Fatal error!' )
    print ( '  Only ORDERS 0 through 8 are available.' )
    raise Exception ( 'normal_ms_moment_values - Fatal error!' )

  return value

def normal_ms_moment_test ( ):

#*****************************************************************************80
#
## normal_ms_moment_test() tests normal_ms_moment().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 4
  mu_test = np.array ( [ 0.0, 2.0, 10.0, 0.0 ] )
  sigma_test = np.array ( [ 1.0, 1.0, 2.0, 2.0 ] )

  print ( '' )
  print ( 'normal_ms_moment_test()' )
  print ( '  normal_ms_moment() evaluates moments of the Normal MS distribution.' )

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    print ( '' )
    print ( '  Mu = %g, Sigma = %g' % ( mu, sigma ) )
    print ( ' Order  Moment' )
    print ( '\n' )

    for order in range ( 0, 9 ):
      moment1 = normal_ms_moment ( order, mu, sigma )
      moment2 = normal_ms_moment_values ( order, mu, sigma )
      print ( '  %2d  %12g  %12g' % ( order, moment1, moment2 ) )

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
#    real VALUE, the I-th power of -1.
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

  for test in range ( 0, 10 ):
    i4 = rng.integers ( low = -100, high = 100, endpoint = True )
    r8 = r8_mop ( i4 )
    print ( '  %4d  %4.1f' % ( i4, r8 ) )

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

  return

def r8vec_write ( filename, n, a ):

#*****************************************************************************80
#
## r8vec_write() writes an R8VEC to a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string FILENAME, the name of the output file.
#
#    integer N, the number of entries in A.
#
#    real A(N), the matrix.
#
  output = open ( filename, 'w' )

  print ( 'fuckin a.shape' )
  print ( a.shape )
  for i in range ( 0, n ):
    s = '  %24.16g\n' % ( a[i] )
    output.write ( s )

  output.close ( )

  return

def r8vec_write_test ( ):

#*****************************************************************************80
#
## r8vec_write_test() tests r8vec_write().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8vec_write_test:' )
  print ( '  r8vec_write() writes an R8VEC to a file.' )

  filename = 'r8vec_write_test.txt'
  n = 5
  a = np.array ( ( 1.1, 2.2, 3.3, 4.4, 5.5 ) )
  r8vec_write ( filename, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )

  return

def rule_write ( order, header, x, w, r ):

#*****************************************************************************80
#
## rule_write() writes a quadrature rule to a file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ORDER, the order of the rule.
#
#    string HEADER, specifies the output files.
#    write files 'header_w.txt', 'header_x.txt', 'header_r.txt' defining
#    weights, abscissas, and region.
#
#    real X(ORDER), the abscissas.
#
#    real W(ORDER), the weights.
#
#    real R(2), the region.
#
  filename_x = header + '_x.txt'
  filename_w = header + '_w.txt'
  filename_r = header + '_r.txt'

  print ( '' )
  print ( '  Creating quadrature files.' )
  print ( '' )
  print ( '  Common header is      "%s".' % ( header ) )
  print ( '' )
  print ( '  Weight file will be   "%s".' % ( filename_w ) )
  print ( '  Abscissa file will be "%s".' % ( filename_x ) )
  print ( '  Region file will be   "%s".' % ( filename_r ) )

  r8vec_write ( filename_w, order, w )
  r8vec_write ( filename_x, order, x )
  r8vec_write ( filename_r, 2,     r )

  return

def rule_write_test ( ):

#*****************************************************************************80
#
## rule_write_test() tests rule_write().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'rule_write_test():' )
  print ( '  rule_write() writes a quadrature rule to three files.' )

  header = 'rule_write_test'
  order = 5
  x = np.array ( [ \
    -0.906179845938663992797626878299, \
    -0.538469310105683091036314420700, \
     0.000000000000000000000000000000, \
     0.538469310105683091036314420700, \
     0.906179845938663992797626878299 ] )
  w = np.array ( [ \
    0.236926885056189087514264040720, \
    0.478628670499366468041291514836, \
    0.568888888888888888888888888889, \
    0.478628670499366468041291514836, \
    0.236926885056189087514264040720 ] )
  r = np.array ( [ -1.0, +1.0 ] )

  rule_write ( order, header, x, w, r )

  print ( '' )
  print ( '  The quadrature rule has been written to files.' )

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

  return None

def truncated_normal_ab_moments ( order_max, mu, sigma, a, b ):

#*****************************************************************************80
#
## truncated_normal_ab_moments(): moments of the truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Phoebus Dhrymes,
#    Moments of Truncated Normal Distributions,
#    May 2005.
#
#  Input:
#
#    integer ORDER_MAX, the maximum order of the moments.
#    0 <= ORDER_MAX.
#
#    real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    real A, B, the lower and upper truncation limits.
#    A < B.
#
#  Output:
#
#    real VALUE[ORDER_MAX+1], the moments of the PDF.
#
  import numpy as np

  value = np.zeros ( order_max + 1 )

  for order in range ( 0, order_max + 1 ):
    value[order] = truncated_normal_ab_moment ( order, mu, sigma, a, b )

  return value

def truncated_normal_ab_moment ( order, mu, sigma, a, b ):

#*****************************************************************************80
#
## truncated_normal_ab_moment(): a moment of the truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Phoebus Dhrymes,
#    Moments of Truncated Normal Distributions,
#    May 2005.
#
#  Input:
#
#    integer ORDER, the order of the moment.
#    0 <= ORDER.
#
#    real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    real A, B, the lower and upper truncation limits.
#    A < B.
#
#  Output:
#
#    real VALUE, the moment of the PDF.
#
  from scipy.special import comb

  if ( order < 0 ):
    print ( '' )
    print ( 'truncated_normal_ab_moment - Fatal error!' )
    print ( '  ORDER < 0.' )
    raise Exception ( 'truncated_normal_ab_moment - Fatal error!' )

  if ( sigma <= 0.0 ):
    print ( '' )
    print ( 'truncated_normal_ab_moment - Fatal error!' )
    print ( '  SIGMA <= 0.0.' )
    raise Exception ( 'truncated_normal_ab_moment - Fatal error!' )

  if ( b <= a ):
    print ( '' )
    print ( 'truncated_normal_ab_moment - Fatal error!' )
    print ( '  B <= A.' )
    raise Exception ( 'truncated_normal_ab_moment - Fatal error!' )

  a_h = ( a - mu ) / sigma
  a_pdf = normal_01_pdf ( a_h )
  a_cdf = normal_01_cdf ( a_h )

  if ( a_cdf == 0.0 ):
    print ( '' )
    print ( 'truncated_normal_ab_moment - Fatal error!' )
    print ( '  PDF/CDF ratio fails, because A_cdf is too small.' )
    print ( '  A_pdf = %g' % ( a_pdf ) )
    print ( '  A_cdf = %g' % ( a_cdf ) )
    raise Exception ( 'truncated_normal_ab_moment - Fatal error!' )

  b_h = ( b - mu ) / sigma
  b_pdf = normal_01_pdf ( b_h )
  b_cdf = normal_01_cdf ( b_h )

  if ( b_cdf == 0.0 ):
    print ( '' )
    print ( 'truncated_normal_ab_moment - Fatal error!' )
    print ( '  PDF/CDF ratio fails, because B_cdf too small.' )
    print ( '  B_pdf = %g' % ( b_pdf ) )
    print ( '  B_cdf = %g' % ( b_cdf ) )
    raise Exception ( 'truncated_normal_ab_moment - Fatal error!' )

  value = 0.0
  irm2 = 0.0
  irm1 = 0.0

  for r in range ( 0, order + 1 ):

    if ( r == 0 ):
      ir = 1.0
    elif ( r == 1 ):
      ir = - ( b_pdf - a_pdf ) / ( b_cdf - a_cdf )
    else:
      ir = ( r - 1 ) * irm2 \
        - ( b_h ** ( r - 1 ) * b_pdf - a_h ** ( r - 1 ) * a_pdf ) \
        / ( b_cdf - a_cdf )

    value = value + comb ( order, r ) \
      * mu ** ( order - r ) \
      * sigma ** r * ir

    irm2 = irm1
    irm1 = ir

  return value

def truncated_normal_ab_moment_test ( ):

#*****************************************************************************80
#
## truncated_normal_ab_moment_test() tests truncated_normal_ab_moment().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 9
  mu_test =    np.array ( [  0.0, 0.0,  0.0,  0.0,  1.0, 0.0,  0.0,  0.0, 5.0 ] )
  sigma_test = np.array ( [  1.0, 1.0,  1.0,  2.0,  1.0, 1.0,  1.0,  1.0, 0.5 ] )
  a_test =     np.array ( [ -1.0, 0.0, -1.0, -1.0,  0.0, 0.5, -2.0, -4.0, 4.0 ] )
  b_test =     np.array ( [  1.0, 1.0,  0.0,  1.0,  2.0, 2.0,  2.0,  4.0, 7.0 ] )

  print ( '' )
  print ( 'truncated_normal_ab_moment_test' )
  print ( '  truncated_normal_ab_moment evaluates moments' )
  print ( '  of the Truncated Normal distribution.' )

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    a = a_test[test]
    b = b_test[test]
    print ( '' )
    print ( '  Test = %d, Mu = %g, Sigma = %g, A = %g, B = %g' \
      % ( test, mu, sigma, a, b ) )
    print ( ' Order  Moment' )
    print ( '\n' )

    for order in range ( 0, 9 ):
      value = truncated_normal_ab_moment ( order, mu, sigma, a, b )
      print ( '  %2d  %12g' % ( order, value ) )

  return

def truncated_normal_a_moments ( order_max, mu, sigma, a ):

#*****************************************************************************80
#
## truncated_normal_a_moments(): moments of the truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Phoebus Dhrymes,
#    Moments of Truncated Normal Distributions,
#    May 2005.
#
#  Input:
#
#    integer ORDER_MAX, the maximum order of the moments.
#    0 <= ORDER_MAX.
#
#    real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    real A, the lower truncation limit.
#
#  Output:
#
#    real VALUE[ORDER_MAX+1], the moments of the PDF.
#
  import numpy as np

  value = np.zeros ( order_max + 1 )

  for order in range ( 0, order_max + 1 ):
    value[order] =  truncated_normal_a_moment ( order, mu, sigma, a )

  return value

def truncated_normal_a_moment ( order, mu, sigma, a ):

#*****************************************************************************80
#
## truncated_normal_a_moment(): a moment of the truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Phoebus Dhrymes,
#    Moments of Truncated Normal Distributions,
#    May 2005.
#
#  Input:
#
#    integer ORDER, the order of the moment.
#    0 <= ORDER.
#
#    real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    real A, the lower truncation limit.
#
#  Output:
#
#    real VALUE, the moment of the PDF.
#
  value = r8_mop ( order ) \
    * truncated_normal_b_moment ( order, -mu, sigma, -a );

  return value

def truncated_normal_a_moment_test ( ):

#*****************************************************************************80
#
## truncated_normal_a_moment_test() tests truncated_normal_a_moment().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 6
  mu_test =    np.array ( [  0.0,  0.0,   0.0,   0.0,  0.0,  -5.0 ] )
  sigma_test = np.array ( [  1.0,  1.0,   1.0,   2.0,  2.0,   1.0 ] )
  a_test =     np.array ( [  0.0, -10.0, 10.0, -10.0, 10.0, -10.0 ] )

  print ( '' )
  print ( 'truncated_normal_a_moment_test' )
  print ( '  truncated_normal_a_moment evaluates moments' )
  print ( '  of the lower Truncated Normal distribution.' )

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    a = a_test[test]
    print ( '' )
    print ( '  Test = %d, Mu = %g, Sigma = %g, A = %g' \
      % ( test, mu, sigma, a ) )
    print ( ' Order  Moment' )
    print ( '\n' )

    for order in range ( 0, 9 ):
      value = truncated_normal_a_moment ( order, mu, sigma, a )
      print ( '  %2d  %12g' % ( order, value ) )

  return

def truncated_normal_b_moments ( order_max, mu, sigma, b ):

#*****************************************************************************80
#
## truncated_normal_b_moments(): moments of upper truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Phoebus Dhrymes,
#    Moments of Truncated Normal Distributions,
#    May 2005.
#
#  Input:
#
#    integer ORDER_MAX, the maximum order of the moments.
#    0 <= ORDER_MAX.
#
#    real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    real B, the upper truncation limit.
#
#  Output:
#
#    real VALUE[0:ORDER_MAX], the moment of the PDF.
#
  import numpy as np

  value = np.zeros ( order_max + 1 )

  for order in range ( 0, order_max + 1 ):
    value[order] = truncated_normal_b_moment ( order, mu, sigma, b )

  return value

def truncated_normal_b_moment ( order, mu, sigma, b ):

#*****************************************************************************80
#
## truncated_normal_b_moment(): a moment of upper truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Phoebus Dhrymes,
#    Moments of Truncated Normal Distributions,
#    May 2005.
#
#  Input:
#
#    integer ORDER, the order of the moment.
#    0 <= ORDER.
#
#    real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    real B, the upper truncation limit.
#
#  Output:
#
#    real VALUE, the moment of the PDF.
#
  from scipy.special import comb

  if ( order < 0 ):
    print ( '' )
    print ( 'truncated_normal_b_moment - Fatal error!' )
    print ( '  ORDER < 0.' )
    raise Exception ( 'truncated_normal_b_moment - Fatal error!' )

  if ( sigma <= 0.0 ):
    print ( '' )
    print ( 'truncated_normal_b_moment - Fatal error!' )
    print ( '  SIGMA <= 0.0.' )
    raise Exception ( 'truncated_normal_b_moment - Fatal error!' )

  b_h = ( b - mu ) / sigma
  b_pdf = normal_01_pdf ( b_h )
  b_cdf = normal_01_cdf ( b_h )

  if ( b_cdf == 0.0 ):
    print ( '' )
    print ( 'truncated_normal_b_moment - Fatal error!' )
    print ( '  PDF/CDF ratio fails, because B_cdf too small.' )
    print ( '  B_pdf = %g' % ( b_pdf ) )
    print ( '  B_cdf = %g' % ( b_cdf ) )
    raise Exception ( 'truncated_normal_b_moment - Fatal error!' )

  f = b_pdf / b_cdf

  value = 0.0
  irm2 = 0.0
  irm1 = 0.0

  for r in range ( 0, order + 1 ):

    if ( r == 0 ):
      ir = 1.0
    elif ( r == 1 ):
      ir = - f
    else:
      ir = - b_h ** ( r - 1 ) * f + ( r - 1 ) * irm2

    value = value + comb ( order, r ) \
      * mu ** ( order - r ) \
      * sigma ** r * ir

    irm2 = irm1
    irm1 = ir

  return value

def truncated_normal_b_moment_test ( ):

#*****************************************************************************80
#
## truncated_normal_b_moment_test() tests truncated_normal_b_moment().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  test_num = 6
  mu_test =    np.array ( [ 0.0,  0.0,  0.0,   0.0,   0.0,  5.0 ] )
  sigma_test = np.array ( [ 1.0,  1.0,  1.0,   2.0,   2.0,  1.0 ] )
  b_test =     np.array ( [ 0.0, 10.0, -10.0, 10.0, -10.0, 10.0 ] )

  print ( '' )
  print ( 'truncated_normal_b_moment_test' )
  print ( '  truncated_normal_b_moment evaluates moments' )
  print ( '  of the upper Truncated Normal distribution.' )

  for test in range ( 0, test_num ):

    mu = mu_test[test]
    sigma = sigma_test[test]
    b = b_test[test]
    print ( '' )
    print ( '  Test = %d, Mu = %g, Sigma = %g, B = %g' \
      % ( test, mu, sigma, b ) )
    print ( ' Order  Moment' )
    print ( '\n' )

    for order in range ( 0, 9 ):
      value = truncated_normal_b_moment ( order, mu, sigma, b )
      print ( '  %2d  %12g' % ( order, value ) )

  return

def truncated_normal_rule ( *args ):

#*****************************************************************************80
#
## truncated_normal_rule() computes a truncated normal quadrature rule.
#
#  Discussion:
#
#    This program computes a truncated normal quadrature rule
#    and writes it to a file.
#
#    The user specifies:
#    * option: 0/1/2/3 for none, lower, upper, double truncation.
#    * N, the number of points in the rule
#    * MU, the mean of the original normal distribution
#    * SIGMA, the standard deviation of the original normal distribution,
#    * A, the left endpoint (for options 1 or 3)
#    * B, the right endpoint (for options 2 or 3)
#    * HEADER, the root name of the output files.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'truncated_normal_rule():' )
  print ( '  For the (truncated) Gaussian probability density function' )
  print ( '    pdf(x) = exp(-0.5*((x-MU)/SIGMA)^2) / SIGMA / sqrt ( 2 * pi )' )
  print ( '  compute an N-point quadrature rule for approximating' )
  print ( '    Integral ( A <= x <= B ) f(x) pdf(x) dx' )
  print ( '' )
  print ( '  The value of OPTION determines the truncation interval [A,B]:' )
  print ( '  0: (-oo,+oo)' )
  print ( '  1: [A,+oo)' )
  print ( '  2: (-oo,B]' )
  print ( '  3: [A,B]' )
  print ( '' )
  print ( '  The user specifies OPTION, N, MU, SIGMA, A, B and FILENAME.' )
  print ( '' )
  print ( '  HEADER is used to generate 3 files:' )
  print ( '' )
  print ( '    header_w.txt - the weight file' )
  print ( '    header_x.txt - the abscissa file.' )
  print ( '    header_r.txt - the region file, listing A and B.' )

  argument_count = ( len ( args ) )

  iarg = 0
#
#  Get OPTION.
#
  if ( argument_count < iarg + 1 ):
    option = eval ( input ( '  Enter OPTION, 0/1/2/3:  ' ) )
  else:
    option = args[iarg]
    iarg = iarg + 1

  if ( option < 0 or 3 < option ):
    print ( '' )
    print ( 'truncated_normal_rule - Fatal error!' )
    print ( '  0 <= OPTION <= 3 was required.' )
    raise Exception ( 'truncated_normal_rule - Fatal error!' )
#
#  Get N.
#
  if ( argument_count < iarg + 1 ):
    n = eval ( input ( '  Enter the rule order N:  ' ) )
  else:
    n = args[iarg]
    iarg = iarg + 1
#
#  Get MU.
#
  if ( argument_count < iarg + 1 ):
    mu = eval ( input ( '  Enter MU, the mean value of the normal distribution:  ' ) )
  else:
    mu = args[iarg]
    iarg = iarg + 1
#
#  Get SIGMA.
#
  if ( argument_count < iarg + 1 ):
    sigma = eval ( input ( '  Enter SIGMA, the standard deviation:  ' ) )
  else:
    sigma = args[iarg]
    iarg = iarg + 1
#
#  Get A.
#
  if ( option == 1 or option == 3 ):
    if ( argument_count < iarg + 1 ):
      a = eval ( input ( '  Enter the left endpoint A:  ' ) )
    else:
      a = args[iarg]
      iarg = iarg + 1
  else:
    a = - np.finfo(float).max
#
#  Get B.
#
  if ( option == 2 or option == 3 ):
    if ( argument_count < iarg + 1 ):
      b = eval ( input ( '  Enter the right endpoint B:  ' ) )
    else:
      b = args[iarg]
      iarg = iarg + 1
  else:
    b = np.finfo(float).max
#
#  Get HEADER.
#
  if ( argument_count < iarg + 1 ):
    print ( '' )
    print ( '  HEADER is the "root name" of the quadrature files.' )
    header = input ( '  Enter HEADER as a quoted string:  ' )
  else:
    header = args[iarg]
    iarg = iarg + 1
#
#  Input summary.
#
  print ( '' )
  print ( '  OPTION = %d' % ( option ) )
  print ( '  N = %d' % ( n ) )
  print ( '  MU = %g' % ( mu ) )
  print ( '  SIGMA = %g' % ( sigma ) )
  if ( option == 1 or option == 3 ):
    print ( '  A = %g' % ( a ) )
  else:
    print ( '  A = -oo' )

  if ( option == 2 or option == 3 ):
    print ( '  B = %g' % ( b ) )
  else:
    print ( '  B = +oo' )

  print ( '  HEADER = "%s"' % ( header ) )
#
#  Compute the moments.
#
  if ( option == 0 ):
    moment = normal_ms_moments ( 2 * n + 1, mu, sigma )
  elif ( option == 1 ):
    moment = truncated_normal_a_moments ( 2 * n + 1, mu, sigma, a )
  elif ( option == 2 ):
    moment = truncated_normal_b_moments ( 2 * n + 1, mu, sigma, b )
  elif ( option == 3 ):
    moment = truncated_normal_ab_moments ( 2 * n + 1, mu, sigma, a, b )
#
#  Compute the rule.
#
  x, w = moment_method ( n, moment )

  r = np.array ( [ a, b ] )
#
#  Write the rule.
#
  rule_write ( n, header, x, w, r )

  return

def option0_test ( ):

#*****************************************************************************80
#
## option0_test() calls truncated_normal_rule() with OPTION = 0.
#
#  Discussion:
#
#    This program computes a truncated normal quadrature rule
#    and writes it to a file.
#
#    The user specifies:
#    * option: 0/1/2/3 for none, lower, upper, double truncation.
#    * N, the number of points in the rule
#    * MU, the mean of the original normal distribution
#    * SIGMA, the standard deviation of the original normal distribution,
#    * HEADER, the root name of the output files.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
 
  print ( '' )
  print ( 'option0_test:' )
  print ( '  Get a quadrature rule for the untruncated normal distribution.' )

  option = 0
  n = 5
  mu = 1.0
  sigma = 2.0
  header = 'option0'
  truncated_normal_rule ( option, n, mu, sigma, header )

  return

def option1_test ( ):

#*****************************************************************************80
#
## option1_test() calls truncated_normal_rule with OPTION = 1.
#
#  Discussion:
#
#    This program computes a truncated normal quadrature rule
#    and writes it to a file.
#
#    The user specifies:
#    * option: 0/1/2/3 for none, lower, upper, double truncation.
#    * N, the number of points in the rule
#    * MU, the mean of the original normal distribution
#    * SIGMA, the standard deviation of the original normal distribution,
#    * A, the lower truncation limit.
#    * HEADER, the root name of the output files.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
# 
  import platform

  print ( '' )
  print ( 'option1_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Get a quadrature rule for the lower truncated normal distribution.' )

  option = 1
  n = 9
  mu = 2.0
  sigma = 0.5
  a = 0.0
  header = 'option1'
  truncated_normal_rule ( option, n, mu, sigma, a, header )

  return

def option2_test ( ):

#*****************************************************************************80
#
## option2_test() calls truncated_normal_rule with OPTION = 2.
#
#  Discussion:
#
#    This program computes a truncated normal quadrature rule
#    and writes it to a file.
#
#    The user specifies:
#    * option: 0/1/2/3 for none, lower, upper, double truncation.
#    * N, the number of points in the rule
#    * MU, the mean of the original normal distribution
#    * SIGMA, the standard deviation of the original normal distribution,
#    * B, the upper truncation limit.
#    * HEADER, the root name of the output files.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'option2_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Get a quadrature rule for the upper truncated normal distribution.' )

  option = 2
  n = 9
  mu = 2.0
  sigma = 0.5
  b = 3.0
  header = 'option2'
  truncated_normal_rule ( option, n, mu, sigma, b, header )

  return

def option3_test ( ):

#*****************************************************************************80
#
## option3_test() calls truncated_normal_rule with OPTION = 3.
#
#  Discussion:
#
#    This program computes a truncated normal quadrature rule
#    and writes it to a file.
#
#    The user specifies:
#    * option: 0/1/2/3 for none, lower, upper, double truncation.
#    * N, the number of points in the rule
#    * MU, the mean of the original normal distribution
#    * SIGMA, the standard deviation of the original normal distribution,
#    * A, the lower truncation limit.
#    * B, the upper truncation limit.
#    * HEADER, the root name of the output files.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
# 
  import platform

  print ( '' )
  print ( 'option3_test:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Get a quadrature rule for the truncated normal distribution.' )

  option = 3
  n = 5
  mu = 100.0
  sigma = 25.0
  a = 50.0
  b = 150.0
  header = 'option3'
  truncated_normal_rule ( option, n, mu, sigma, a, b, header )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  truncated_normal_rule_test ( )
  timestamp ( )

