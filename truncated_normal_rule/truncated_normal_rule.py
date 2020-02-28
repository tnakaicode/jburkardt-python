#! /usr/bin/env python3
#
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
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

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
    j, seed = i4_uniform_ab ( a, b, seed )
    print ( '  %8d  %8d' % ( i, j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def moment_method ( n, moments ):

#*****************************************************************************80
#
## MOMENT_METHOD computes a quadrature rule by the method of moments.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer N, the order of the quadrature rule.
#
#    Input, real MOMENTS(2*N+1), moments 0 through 2*N.
#
#    Output, real X(N), W(N), the points and weights of the quadrature rule.
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
## MOMENT_METHOD_TEST tests MOMENT_METHOD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'MOMENT_METHOD_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MOMENT_METHOD uses the method of moments for a quadrature rule.' )

  n = 5
  tnp1 = 2 * n + 1
  
  moments = np.zeros ( tnp1 )

  for i in range ( 0, tnp1 ):
    moments[i] = normal_01_moment ( i )

  x, w = moment_method ( n, moments )

  x_correct = np.array ( [ \
    [ -2.85697001387280565416230426401 ], \
    [ -1.35562617997426586583052129087 ], \
    [  0.0 ], \
    [ +1.35562617997426586583052129087 ], \
    [ +2.85697001387280565416230426401 ] ] )

  w_correct = np.array ( [ \
    [ 0.0112574113277206889333702151856 ], \
    [ 0.222075922005612644399963118148 ], \
    [ 0.533333333333333333333333333333 ], \
    [ 0.222075922005612644399963118148 ], \
    [ 0.0112574113277206889333702151856 ] ] )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'MOMENT_METHOD_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_01_cdf ( x ):

#*****************************************************************************80
#
## NORMAL_01_CDF evaluates the Normal 01 CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Output, real VALUE, the value of the CDF.
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
## NORMAL_01_CDF_TEST tests NORMAL_01_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'NORMAL_01_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_CDF evaluates the CDF;' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_CDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_01_cdf_values ( n_data ):

#*****************************************************************************80
#
## NORMAL_01_CDF_VALUES returns some values of the Normal 01 CDF.
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
#    This code is distributed under the GNU LGPL license.
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
## NORMAL_01_MOMENT evaluates the moments of the Normal 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#
#    Output, real VALUE, the value of the moment.
# 
  if ( ( order % 2 ) == 0 ):
    value = r8_factorial2 ( order - 1 )
  else:
    value = 0.0

  return value

def normal_01_moment_test ( ):

#*****************************************************************************80
#
## NORMAL_01_MOMENT_TEST tests NORMAL_01_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'NORMAL_01_MOMENT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_MOMENT evaluates moments of the Normal 01 PDF;' )
  print ( '' )
  print ( '   Order     Moment' )
  print ( '' )

  for order in range ( 0, +11 ):

    moment = normal_01_moment ( order )
    print ( '  %6d  %14.6g' % ( order, moment ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_MOMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_01_pdf ( x ):

#*****************************************************************************80
#
## NORMAL_01_PDF evaluates the Normal 01 PDF.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Output, real VALUE, the value of the PDF.
# 
  import numpy as np

  value = np.exp ( - 0.5 * x * x ) / np.sqrt ( 2.0 * np.pi )

  return value

def normal_01_pdf_test ( ):

#*****************************************************************************80
#
## NORMAL_01_PDF_TEST tests NORMAL_01_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'NORMAL_01_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_01_PDF evaluates the PDF;' )
  print ( '' )
  print ( '       X              PDF' )
  print ( '' )

  for i in range ( -20, +21 ):

    x = float ( i ) / 10.0
    pdf = normal_01_pdf ( x )
    print ( '  %14.6g  %24.16g' % ( x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_01_PDF_TEST:' )
  print ( '  Normal end of execution.' )
  return

def normal_ms_moments ( order_max, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENTS evaluates the moments of the Normal MS distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ORDER_MAX, the maximum order of the moments.
#
#    Input, real MU, the mean of the distribution.
#
#    Input, real SIGMA, the standard deviation of the distribution.
#
#    Output, real VALUE[0:ORDER_MAX], the value of the moments.
#
  import numpy as np

  value = np.zeros ( order_max + 1 )

  for order in range ( 0, order_max + 1 ):
    value[order] = normal_ms_moment ( order, mu, sigma )

  return value

def normal_ms_moment ( order, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT evaluates a moment of the Normal MS distribution.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#
#    Input, real MU, the mean of the distribution.
#
#    Input, real SIGMA, the standard deviation of the distribution.
#
#    Output, real VALUE, the value of the moment.
#
  j_hi = ( order // 2 )

  value = 0.0
  for j in range ( 0, j_hi + 1 ):
    value = value \
      + r8_choose ( order, 2 * j ) \
      * r8_factorial2 ( 2 * j - 1 ) \
      * mu ** ( order - 2 * j ) * sigma ** ( 2 * j )

  return value

def normal_ms_moment_values ( order, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT_VALUES evaluates moments 0 through 8 of the Normal PDF.
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
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#    0 <= ORDER <= 8.
#
#    Input, real MU, the mean of the distribution.
#
#    Input, real SIGMA, the standard deviation of the distribution.
#
#    Output, real VALUE, the value of the central moment.
#
  from sys import exit

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
    print ( 'NORMAL_MS_MOMENT_VALUES - Fatal error!' )
    print ( '  Only ORDERS 0 through 8 are available.' )
    exit ( 'NORMAL_MS_MOMENT_VALUES - Fatal error!' )

  return value

def normal_ms_moment_test ( ):

#*****************************************************************************80
#
## NORMAL_MS_MOMENT_TEST tests NORMAL_MS_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'NORMAL_MS_MOMENT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_MS_MOMENT evaluates moments of the Normal MS distribution.' )

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
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_MS_MOMENT_TEST:' )
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

def r8_factorial2 ( n ):

#*****************************************************************************80
#
## R8_FACTORIAL2 computes the double factorial function.
#
#  Formula:
#
#    FACTORIAL2( N ) = Product ( N * (N-2) * (N-4) * ... * 2 )  (N even)
#                    = Product ( N * (N-2) * (N-4) * ... * 1 )  (N odd)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the argument of the double factorial function.
#    If N is less than 1, VALUE is returned as 1.
#
#    Output, real VALUE, the value of N!!.
#
  value = 1;

  if ( n < 1 ):
    return value

  while ( 1 < n ):
    value = value * n
    n = n - 2

  return value

def r8_factorial2_test ( ):

#*****************************************************************************80
#
## R8_FACTORIAL2_TEST tests R8_FACTORIAL2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_FACTORIAL2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_FACTORIAL2 evaluates the double factorial function.' )
  print ( '' )
  print ( '      N                     Exact' ),
  print ( '                  Computed' )

  n_data = 0

  while ( True ):

    n_data, n, f1 = r8_factorial2_values ( n_data )

    if ( n_data == 0 ):
      break

    f2 = r8_factorial2 ( n )

    print ( '  %4d  %24.16g  %24.16g' % ( n, f1, f2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_FACTORIAL2_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8_factorial2_values ( n_data ):

#*****************************************************************************80
#
## R8_FACTORIAL2_VALUES returns values of the double factorial function.
#
#  Formula:
#
#    FACTORIAL2( N ) = Product ( N * (N-2) * (N-4) * ... * 2 )  (N even)
#                    = Product ( N * (N-2) * (N-4) * ... * 1 )  (N odd)
#
#    In Mathematica, the function can be evaluated by:
#
#      n!!
#
#  Example:
#
#     N    N!!
#
#     0     1
#     1     1
#     2     2
#     3     3
#     4     8
#     5    15
#     6    48
#     7   105
#     8   384
#     9   945
#    10  3840
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
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
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition,
#    CRC Press, 1996, page 16.
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
#    Output, real F, the value of the function.
# 
  import numpy as np

  n_max = 16

  f_vec = np.array ( ( 
          1.0, \
          1.0, \
          2.0, \
          3.0, \
          8.0, \
         15.0, \
         48.0, \
        105.0, \
        384.0, \
        945.0, \
       3840.0, \
      10395.0, \
      46080.0, \
     135135.0, \
     645120.0, \
    2027025.0 ) )

  n_vec = np.array ( ( 
    0, \
     1,  2,  3,  4,  5, \
     6,  7,  8,  9, 10, \
    11, 12, 13, 14, 15 ) )

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    n = 0
    f = 0.0
  else:
    n = n_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, n, f

def r8_factorial2_values_test ( ):

#*****************************************************************************80
#
## R8_FACTORIAL2_VALUES_TEST demonstrates the use of R8_FACTORIAL2_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_FACTORIAL2_VALUES_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_FACTORIAL2_VALUES returns values of the double factorial function.' )
  print ( '' )
  print ( '     N        N!!' )
  print ( '' )

  n_data = 0

  while ( True ):

    n_data, n, f = r8_factorial2_values ( n_data )

    if ( n_data == 0 ):
      break

    print ( '%6d  %14.6g' % ( n, f ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_FACTORIAL2_VALUES_TEST:' )
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
  print ( '      N                     Exact' ),
  print ( '                  Computed' )

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

      res = - np.log ( y )
#
#  EPS < X <= 1.5.
#
    elif ( y <= 1.5 ):

      if ( y < 0.6796875 ):
        corr = - np.log ( y );
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
      corr = np.log ( y )
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

def r8_huge ( ):

#*****************************************************************************80
#
## R8_HUGE returns a "huge" real number.
#
#  Discussion:
#
#    The value returned by this function is intended to be the largest
#    representable real value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, a huge number.
#
  value = 1.79769313486231571E+308

  return value

def r8_huge_test ( ):

#*****************************************************************************80
#
## R8_HUGE_TEST tests R8_HUGE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'R8_HUGE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_HUGE returns a "huge" R8;' )
  print ( '' )
  print ( '    R8_HUGE = %g' % ( r8_huge ( ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_HUGE_TEST' )
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

def r8vec_write ( filename, n, a ):

#*****************************************************************************80
#
## R8VEC_WRITE writes an R8VEC to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, string FILENAME, the name of the output file.
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, n ):
    s = '  %24.16g\n' % ( a[i] )
    output.write ( s )

  output.close ( )

  return

def r8vec_write_test ( ):

#*****************************************************************************80
#
## R8VEC_WRITE_TEST tests R8VEC_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'R8VEC_WRITE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test R8VEC_WRITE, which writes an R8VEC to a file.' )

  filename = 'r8vec_write_test.txt'
  n = 5
  a = np.array ( ( 1.1, 2.2, 3.3, 4.4, 5.5 ) )
  r8vec_write ( filename, n, a )

  print ( '' )
  print ( '  Created file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_WRITE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def rule_write ( order, header, x, w, r ):

#*****************************************************************************80
#
## RULE_WRITE writes a quadrature rule to a file.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ORDER, the order of the rule.
#
#    Input, string HEADER, specifies the output files.
#    write files 'header_w.txt', 'header_x.txt', 'header_r.txt' defining
#    weights, abscissas, and region.
#
#    Input, real X(ORDER), the abscissas.
#
#    Input, real W(ORDER), the weights.
#
#    Input, real R(2), the region.
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
## RULE_WRITE_TEST tests RULE_WRITE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'RULE_WRITE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RULE_WRITE writes a quadrature rule to three files.' )

  header = 'rule_write_test'
  order = 5
  x = np.array ( [ \
    [ -0.906179845938663992797626878299 ], \
    [ -0.538469310105683091036314420700 ], \
    [  0.000000000000000000000000000000 ], \
    [  0.538469310105683091036314420700 ], \
    [  0.906179845938663992797626878299 ] ] )
  w = np.array ( [ \
    [ 0.236926885056189087514264040720 ], \
    [ 0.478628670499366468041291514836 ], \
    [ 0.568888888888888888888888888889 ], \
    [ 0.478628670499366468041291514836 ], \
    [ 0.236926885056189087514264040720 ] ] )
  r = np.array ( [ [ -1.0 ], [ +1.0 ] ] )

  rule_write ( order, header, x, w, r )

  print ( '' )
  print ( '  The quadrature rule has been written to files.' )
#
#  Terminate.
#
  print ( '' )
  print ( 'RULE_WRITE_TEST:' )
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

def truncated_normal_ab_moments ( order_max, mu, sigma, a, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_MOMENTS: moments of the truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer ORDER_MAX, the maximum order of the moments.
#    0 <= ORDER_MAX.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    Input, real A, B, the lower and upper truncation limits.
#    A < B.
#
#    Output, real VALUE[ORDER_MAX+1], the moments of the PDF.
#
  import numpy as np

  value = np.zeros ( order_max + 1 )

  for order in range ( 0, order_max + 1 ):
    value[order] = truncated_normal_ab_moment ( order, mu, sigma, a, b )

  return value

def truncated_normal_ab_moment ( order, mu, sigma, a, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_MOMENT: a moment of the truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#    0 <= ORDER.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    Input, real A, B, the lower and upper truncation limits.
#    A < B.
#
#    Output, real VALUE, the moment of the PDF.
#
  from sys import exit

  if ( order < 0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )
    print ( '  ORDER < 0.' )
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  if ( sigma <= 0.0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )
    print ( '  SIGMA <= 0.0.' )
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  if ( b <= a ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )
    print ( '  B <= A.' )
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  a_h = ( a - mu ) / sigma
  a_pdf = normal_01_pdf ( a_h )
  a_cdf = normal_01_cdf ( a_h )

  if ( a_cdf == 0.0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )
    print ( '  PDF/CDF ratio fails, because A_CDF is too small.' )
    print ( '  A_PDF = %g' % ( a_pdf ) )
    print ( '  A_CDF = %g' % ( a_cdf ) )
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

  b_h = ( b - mu ) / sigma
  b_pdf = normal_01_pdf ( b_h )
  b_cdf = normal_01_cdf ( b_h )

  if ( b_cdf == 0.0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )
    print ( '  PDF/CDF ratio fails, because B_CDF too small.' )
    print ( '  B_PDF = %g' % ( b_pdf ) )
    print ( '  B_CDF = %g' % ( b_cdf ) )
    exit ( 'TRUNCATED_NORMAL_AB_MOMENT - Fatal error!' )

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

    value = value + r8_choose ( order, r ) \
      * mu ** ( order - r ) \
      * sigma ** r * ir

    irm2 = irm1
    irm1 = ir

  return value

def truncated_normal_ab_moment_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_AB_MOMENT_TEST tests TRUNCATED_NORMAL_AB_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'TRUNCATED_NORMAL_AB_MOMENT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_AB_MOMENT evaluates moments' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_AB_MOMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_a_moments ( order_max, mu, sigma, a ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_MOMENTS: moments of the truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer ORDER_MAX, the maximum order of the moments.
#    0 <= ORDER_MAX.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    Input, real A, the lower truncation limit.
#
#    Output, real VALUE[ORDER_MAX+1], the moments of the PDF.
#
  import numpy as np

  value = np.zeros ( order_max + 1 )

  for order in range ( 0, order_max + 1 ):
    value[order] =  truncated_normal_a_moment ( order, mu, sigma, a )

  return value

def truncated_normal_a_moment ( order, mu, sigma, a ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_MOMENT: a moment of the truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#    0 <= ORDER.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    Input, real A, the lower truncation limit.
#
#    Output, real VALUE, the moment of the PDF.
#
  value = r8_mop ( order ) \
    * truncated_normal_b_moment ( order, -mu, sigma, -a );

  return value

def truncated_normal_a_moment_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_A_MOMENT_TEST tests TRUNCATED_NORMAL_A_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'TRUNCATED_NORMAL_A_MOMENT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_A_MOMENT evaluates moments' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_A_MOMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_b_moments ( order_max, mu, sigma, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_MOMENTS: moments of upper truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer ORDER_MAX, the maximum order of the moments.
#    0 <= ORDER_MAX.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    Input, real B, the upper truncation limit.
#
#    Output, real VALUE[0:ORDER_MAX], the moment of the PDF.
#
  import numpy as np

  value = np.zeros ( order_max + 1 )

  for order in range ( 0, order_max + 1 ):
    value[order] = truncated_normal_b_moment ( order, mu, sigma, b )

  return value

def truncated_normal_b_moment ( order, mu, sigma, b ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_MOMENT: a moment of upper truncated Normal distribution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
#  Parameters:
#
#    Input, integer ORDER, the order of the moment.
#    0 <= ORDER.
#
#    Input, real MU, SIGMA, the mean and standard deviation of the
#    parent Normal distribution.
#    0 < S.
#
#    Input, real B, the upper truncation limit.
#
#    Output, real VALUE, the moment of the PDF.
#
  from sys import exit

  if ( order < 0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_B_MOMENT - Fatal error!' )
    print ( '  ORDER < 0.' )
    exit ( 'TRUNCATED_NORMAL_B_MOMENT - Fatal error!' )

  if ( sigma <= 0.0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_B_MOMENT - Fatal error!' )
    print ( '  SIGMA <= 0.0.' )
    exit ( 'TRUNCATED_NORMAL_B_MOMENT - Fatal error!' )

  b_h = ( b - mu ) / sigma
  b_pdf = normal_01_pdf ( b_h )
  b_cdf = normal_01_cdf ( b_h )

  if ( b_cdf == 0.0 ):
    print ( '' )
    print ( 'TRUNCATED_NORMAL_B_MOMENT - Fatal error!' )
    print ( '  PDF/CDF ratio fails, because B_CDF too small.' )
    print ( '  B_PDF = %g' % ( b_pdf ) )
    print ( '  B_CDF = %g' % ( b_cdf ) )
    exit ( 'TRUNCATED_NORMAL_B_MOMENT - Fatal error!' )

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

    value = value + r8_choose ( order, r ) \
      * mu ** ( order - r ) \
      * sigma ** r * ir

    irm2 = irm1
    irm1 = ir

  return value

def truncated_normal_b_moment_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_B_MOMENT_TEST tests TRUNCATED_NORMAL_B_MOMENT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'TRUNCATED_NORMAL_B_MOMENT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRUNCATED_NORMAL_B_MOMENT evaluates moments' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_B_MOMENT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_rule ( *args ):

#*****************************************************************************80
#
## MAIN is the main program for TRUNCATED_NORMAL_RULE.
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
#    This code is distributed under the GNU LGPL license.
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
  print ( 'TRUNCATED_NORMAL_RULE' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '' )
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
    print ( 'TRUNCATED_NORMAL_RULE - Fatal error!' )
    print ( '  0 <= OPTION <= 3 was required.' )
    exit ( 'TRUNCATED_NORMAL_RULE - Fatal error!' )
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
    a = - r8_huge ( )
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
    b = r8_huge ( )
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

  r = np.array ( [ [ a ], [ b ] ] )
#
#  Write the rule.
#
  rule_write ( n, header, x, w, r )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRUNCATED_NORMAL_RULE:' )
  print ( '  Normal end of execution.' )
  return

def option0_test ( ):

#*****************************************************************************80
#
## OPTION0_TEST calls TRUNCATED_NORMAL_RULE with OPTION = 0.
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
#    This code is distributed under the GNU LGPL license.
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
  print ( 'OPTION0_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Get a quadrature rule for the untruncated normal distribution.' )

  option = 0
  n = 5
  mu = 1.0
  sigma = 2.0
  header = 'option0'
  truncated_normal_rule ( option, n, mu, sigma, header )
#
#  Terminate.
#
  print ( '' )
  print ( 'OPTION0_TEST:' )
  print ( '  Normal end of execution.' )
  return

def option1_test ( ):

#*****************************************************************************80
#
## OPTION1_TEST calls TRUNCATED_NORMAL_RULE with OPTION = 1.
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
#    This code is distributed under the GNU LGPL license.
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
  print ( 'OPTION1_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Get a quadrature rule for the lower truncated normal distribution.' )

  option = 1
  n = 9
  mu = 2.0
  sigma = 0.5
  a = 0.0
  header = 'option1'
  truncated_normal_rule ( option, n, mu, sigma, a, header )
#
#  Terminate.
#
  print ( '' )
  print ( 'OPTION1_TEST:' )
  print ( '  Normal end of execution.' )
  return

def option2_test ( ):

#*****************************************************************************80
#
## OPTION2_TEST calls TRUNCATED_NORMAL_RULE with OPTION = 2.
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
#    This code is distributed under the GNU LGPL license.
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
  print ( 'OPTION2_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Get a quadrature rule for the upper truncated normal distribution.' )

  option = 2
  n = 9
  mu = 2.0
  sigma = 0.5
  b = 3.0
  header = 'option2'
  truncated_normal_rule ( option, n, mu, sigma, b, header )
#
#  Terminate.
#
  print ( '' )
  print ( 'OPTION2_TEST:' )
  print ( '  Normal end of execution.' )
  return

def option3_test ( ):

#*****************************************************************************80
#
## OPTION3_TEST calls TRUNCATED_NORMAL_RULE with OPTION = 3.
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
#    This code is distributed under the GNU LGPL license.
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
  print ( 'OPTION3_TEST:' )
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
#
#  Terminate.
#
  print ( '' )
  print ( 'OPTION3_TEST:' )
  print ( '  Normal end of execution.' )
  return

def truncated_normal_rule_test ( ):

#*****************************************************************************80
#
## TRUNCATED_NORMAL_RULE_TEST tests the functions in TRUNCATED_NORMAL_RULE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  print ( 'TRUNCATED_NORMAL_RULE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the functions used by TRUNCATED_NORMAL_RULE.' )
#
#  Utilities.
#
  i4_uniform_ab_test ( )
  r8_choose_test ( )
  r8_factorial_test ( )
  r8_factorial2_test ( )
  r8_huge_test ( )
  r8_mop_test ( )
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8vec_print_test ( )
  r8vec_write_test ( )
  rule_write_test ( )
  timestamp_test ( )
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
  print ( 'TRUNCATED_NORMAL_RULE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  truncated_normal_rule_test ( )
  timestamp ( )


