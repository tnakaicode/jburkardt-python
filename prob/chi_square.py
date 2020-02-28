#! /usr/bin/env python
#
def chi_square_cdf ( x, a ):

#*****************************************************************************80
#
## CHI_SQUARE_CDF evaluates the Chi squared CDF.
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
#    Input, real X, the value of the random deviate.
#
#    Input, real A, the parameter of the distribution, usually
#    the number of degrees of freedom.
#
#    Output, real CDF, the value of the CDF.
#
  from gamma import gamma_cdf

  x2 = 0.5 * x

  a2 = 0.0
  b2 = 1.0
  c2 = 0.5 * a

  cdf = gamma_cdf ( x2, a2, b2, c2 )

  cdf = 1.0 - cdf

  return cdf

def chi_square_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## CHI_SQUARE_CDF_INV inverts the Chi squared PDF.
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
#    Python version by John Burkardt.
#
#  Reference:
#
#    Best and Roberts,
#    The Percentage Points of the Chi-Squared Distribution,
#    Algorithm AS 91,
#    Applied Statistics,
#    Volume 24, Number ?, pages 385-390, 1975.
#
#  Parameters:
#
#    Input, real CDF, a value of the chi-squared cumulative
#    probability density function.
#    0.000002 <= CDF <= 0.999998.
#
#    Input, real A, the parameter of the chi-squared
#    probability density function.  0 < A.
#
#    Output, real X, the value of the chi-squared random deviate
#    with the property that the probability that a chi-squared random
#    deviate with parameter A is less than or equal to PPCHI2 is P.
#
  import numpy as np
  from normal_01 import normal_01_cdf_inv
  from r8_gamma_inc import r8_gamma_inc
  from r8_gamma_log import r8_gamma_log
  from sys import exit

  aa = 0.6931471806
  c1 = 0.01
  c2 = 0.222222
  c3 = 0.32
  c4 = 0.4
  c5 = 1.24
  c6 = 2.2
  c7 = 4.67
  c8 = 6.66
  c9 = 6.73
  c10 = 13.32
  c11 = 60.0
  c12 = 70.0
  c13 = 84.0
  c14 = 105.0
  c15 = 120.0
  c16 = 127.0
  c17 = 140.0
  c18 = 175.0
  c19 = 210.0
  c20 = 252.0
  c21 = 264.0
  c22 = 294.0
  c23 = 346.0
  c24 = 420.0
  c25 = 462.0
  c26 = 606.0
  c27 = 672.0
  c28 = 707.0
  c29 = 735.0
  c30 = 889.0
  c31 = 932.0
  c32 = 966.0
  c33 = 1141.0
  c34 = 1182.0
  c35 = 1278.0
  c36 = 1740.0
  c37 = 2520.0
  c38 = 5040.0
  cdf_max = 0.999998
  cdf_min = 0.000002
  e = 0.0000005
  it_max = 20

  if ( cdf < cdf_min ):
    x = -1.0
    print ( '' )
    print ( 'CHI_SQUARE_CDF_INV - Fatal error!' )
    print ( '  CDF < CDF_MIN.' )
    exit ( 'CHI_SQUARE_CDF_INV - Fatal error!' )

  if ( cdf_max < cdf ):
    x = -1.0
    print ( '' )
    print ( 'CHI_SQUARE_CDF_INV - Fatal error!' )
    print ( '  CDF_MAX < CDF.' )
    exit ( 'CHI_SQUARE_CDF_INV - Fatal error!' )

  xx = 0.5 * a
  c = xx - 1.0
#
#  Compute Log ( Gamma ( A/2 ) ).
#
  g = r8_gamma_log ( a / 2.0 )
#
#  Starting approximation for small chi-squared.
#
  if ( a < - c5 * np.log ( cdf ) ):

    ch = ( cdf * xx * np.exp ( g + xx * aa ) ) ** ( 1.0 / xx )

    if ( ch < e ):
      x = ch
      return x
#
#  Starting approximation for A less than or equal to 0.32.
#
  elif ( a <= c3 ):

    ch = c4
    a2 = np.log ( 1.0 - cdf )

    while ( True ):

      q = ch
      p1 = 1.0 + ch * ( c7 + ch )
      p2 = ch * ( c9 + ch * ( c8 + ch ) )

      t = - 0.5 + ( c7 + 2.0 * ch ) / p1 - ( c9 + ch * ( c10 + 3.0 * ch ) ) / p2

      ch = ch - ( 1.0 - np.exp ( a2 + g + 0.5 * ch + c * aa ) * p2 / p1 ) / t

      if ( abs ( q / ch - 1.0 ) <= c1 ):
        break
#
#  Call to algorithm AS 111.
#  Note that P has been tested above.
#  AS 241 could be used as an alternative.
#
  else:

    x2 = normal_01_cdf_inv ( cdf )
#
#  Starting approximation using Wilson and Hilferty estimate.
#
    p1 = c2 / a
    ch = a * ( x2 * np.sqrt ( p1 ) + 1.0 - p1 ) ** 3
#
#  Starting approximation for P tending to 1.
#
    if ( c6 * a + 6.0 < ch ):
      ch = -2.0 * ( np.log ( 1.0 - cdf ) - c * np.log ( 0.5 * ch ) + g )
#
#  Call to algorithm AS 239 and calculation of seven term Taylor series.
#
  for i in range ( 0, it_max ):

    q = ch
    p1 = 0.5 * ch
    p2 = cdf - r8_gamma_inc ( xx, p1 )
    t = p2 * np.exp ( xx * aa + g + p1 - c * np.log ( ch ) )
    b = t / ch
    a2 = 0.5 * t - b * c

    s1 = ( c19 + a2 \
       * ( c17 + a2 \
       * ( c14 + a2 \
       * ( c13 + a2 \
       * ( c12 + a2 \
       *   c11 ) ) ) ) ) / c24

    s2 = ( c24 + a2 \
       * ( c29 + a2 \
       * ( c32 + a2 \
       * ( c33 + a2 \
       *   c35 ) ) ) ) / c37

    s3 = ( c19 + a2 \
       * ( c25 + a2 \
       * ( c28 + a2 \
       *   c31 ) ) ) / c37

    s4 = ( c20 + a2 \
       * ( c27 + a2 \
       *   c34 ) + c \
       * ( c22 + a2 \
       * ( c30 + a2 \
       *   c36 ) ) ) / c38

    s5 = ( c13 + c21 * a2 + c * ( c18 + c26 * a2 ) ) / c37

    s6 = ( c15 + c * ( c23 + c16 * c ) ) / c38

    ch = ch + t * ( 1.0 + 0.5 * t * s1 - b * c \
      * ( s1 - b \
      * ( s2 - b \
      * ( s3 - b \
      * ( s4 - b \
      * ( s5 - b \
      *   s6 ) ) ) ) ) )

    if ( e < abs ( q / ch - 1.0 ) ):
      x = ch
      return x

  x = ch
  print ( '' )
  print ( 'CHI_SQUARE_CDF_INV - Warning!' )
  print ( '  Convergence not reached.' )

  return x

def chi_square_cdf_test ( ):

#*****************************************************************************80
#
## CHI_SQUARE_CDF_TEST tests CHI_SQUARE_CDF, CHI_SQUARE_CDF_INV, CHI_SQUARE_PDF.
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
  print ( 'CHI_SQUARE_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHI_SQUARE_CDF evaluates the Chi Square CDF' )
  print ( '  CHI_SQUARE_CDF_INV inverts the Chi Square CDF.' )
  print ( '  CHI_SQUARE_PDF evaluates the Chi Square PDF' )

  a = 4.0

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )

  check = chi_square_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'CHI_SQUARE_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = chi_square_sample ( a, seed )

    pdf = chi_square_pdf ( x, a )

    cdf = chi_square_cdf ( x, a )

    x2 = chi_square_cdf_inv ( cdf, a )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHI_SQUARE_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def chi_square_check ( a ):

#*****************************************************************************80
#
## CHI_SQUARE_CHECK checks the parameter of the central Chi squared PDF.
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
#    Input, real A, the parameter of the distribution.
#    1 <= A.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 1.0 ):
    print ( '' )
    print ( 'CHI_SQUARE_CHECK - Fatal error!' )
    print ( '  A < 1.0.' )
    check = False

  return check

def chi_square_mean ( a ):

#*****************************************************************************80
#
## CHI_SQUARE_MEAN returns the mean of the central Chi squared PDF.
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
#    Input, real A, the parameter of the distribution.
#    1 <= A.
#
#    Output, real MEAN, the mean value.
#
  mean = a

  return mean

def chi_square_pdf ( x, a ):

#*****************************************************************************80
#
## CHI_SQUARE_PDF evaluates the central Chi squared PDF.
#
#  Discussion:
#
#    PDF(X)(A) =
#      EXP ( - X / 2 ) * X^((A-2)/2) / ( 2^(A/2) * GAMMA ( A/2 ) )
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
#    Input, real X, the argument of the PDF.
#    0.0 <= X
#
#    Input, real A, the parameter of the PDF.
#    1 <= A.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from r8_gamma import r8_gamma

  if ( x < 0.0 ):
    pdf = 0.0
  else:
    b = a / 2.0
    pdf = np.exp ( - 0.5 * x ) * x ** ( b - 1.0 ) / ( 2.0 ** b * r8_gamma ( b ) )
 
  return pdf

def chi_square_sample ( a, seed ):

#*****************************************************************************80
#
## CHI_SQUARE_SAMPLE samples the central Chi squared PDF.
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
#    Input, real A, the parameter of the PDF.
#    1 <= A.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from gamma import gamma_sample
  from normal_01 import normal_01_sample

  it_max = 100

  n = int ( a )

  if ( n == a and n <= it_max ):

    x = 0.0
    for i in range ( 0, n ):
      x2, seed = normal_01_sample ( seed )
      x = x + x2 * x2

  else:

    a2 = 0.0
    b2 = 1.0
    c2 = a / 2.0

    x, seed = gamma_sample ( a2, b2, c2, seed )

    x = 2.0 * x

  return x, seed

def chi_square_sample_test ( ):

#*****************************************************************************80
#
## CHI_SQUARE_SAMPLE_TEST tests CHI_SQUARE_SAMPLE.
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
  from r8vec_max import r8vec_max
  from r8vec_mean import r8vec_mean
  from r8vec_min import r8vec_min
  from r8vec_variance import r8vec_variance

  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'CHI_SQUARE_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHI_SQUARE_MEAN computes the Chi Square mean' )
  print ( '  CHI_SQUARE_SAMPLE samples the Chi Square distribution' )
  print ( '  CHI_SQUARE_VARIANCE computes the Chi Square variance.' )

  a = 10.0

  check = chi_square_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'CHI_SQUARE_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = chi_square_mean ( a )
  variance = chi_square_variance ( a )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = chi_square_sample ( a, seed )

  mean = r8vec_mean ( nsample, x )
  variance = r8vec_variance ( nsample, x )
  xmax = r8vec_max ( nsample, x )
  xmin = r8vec_min ( nsample, x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHI_SQUARE_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def chi_square_variance ( a ):

#*****************************************************************************80
#
## CHI_SQUARE_VARIANCE returns the variance of the central Chi squared PDF.
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
#    Input, real A, the parameter of the distribution.
#    1 <= A.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = 2.0 * a

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  chi_square_cdf_test ( )
  chi_square_sample_test ( )
  timestamp ( )

