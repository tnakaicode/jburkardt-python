#! /usr/bin/env python
#
def beta_binomial_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## BETA_BINOMIAL_CDF_INV inverts the Beta Binomial CDF.
#
#  Discussion:
#
#    A simple discrete approach is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#
#    Input, real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Input, integer C, a parameter of the PDF.
#    0 <= C.
#
#    Output, integer X, the smallest X whose cumulative density function
#    is greater than or equal to CDF.
#
  from r8_beta import r8_beta

  if ( cdf <= 0.0 ):

    x = 0

  else:

    cum = 0.0

    for y in range ( 0, c + 1 ):

      pdf = r8_beta ( a + y, b + c - y ) / ( ( c + 1 ) \
        * r8_beta ( y + 1, c - y + 1 ) * r8_beta ( a, b ) )

      cum = cum + pdf

      if ( cdf <= cum ):
        x = y
        return x

    x = c

  return x

def beta_binomial_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## BETA_BINOMIAL_CDF evaluates the Beta Binomial CDF.
#
#  Discussion:
#
#    A simple summing approach is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the argument of the CDF.
#
#    Input, real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Input, integer C, a parameter of the PDF.
#    0 <= C.
#
#    Output, real CDF, the value of the CDF.
#
  from r8_beta import r8_beta

  if ( x < 0 ):

    cdf = 0.0

  elif ( x < c ):

    cdf = 0.0
    for y in range ( 0, x + 1 ):
      pdf = r8_beta ( a + y, b + c - y ) / ( ( c + 1 ) \
        * r8_beta ( y + 1,  c - y + 1 ) * r8_beta ( a, b ) )
      cdf = cdf + pdf

  elif ( c <= x ):

    cdf = 1.0

  return cdf

def beta_binomial_cdf_test ( ):

#*****************************************************************************80
#
## BETA_BINOMIAL_CDF_TEST tests BETA_BINOMIAL_CDF, BETA_BINOMIAL_CDF_INV, BETA_BINOMIAL_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BETA_BINOMIAL_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BETA_BINOMIAL_CDF evaluates the Beta Binomial CDF' )
  print ( '  BETA_BINOMIAL_CDF_INV inverts the Beta Binomial CDF.' )
  print ( '  BETA_BINOMIAL_PDF evaluates the Beta Binomial PDF' )

  a = 2.0
  b = 3.0
  c = 4

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %6d' % ( c ) )

  check = beta_binomial_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'BETA_BINOMIAL_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = beta_binomial_sample ( a, b, c, seed )

    pdf = beta_binomial_pdf ( x, a, b, c )

    cdf = beta_binomial_cdf ( x, a, b, c )

    x2 = beta_binomial_cdf_inv ( cdf, a, b, c )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BETA_BINOMIAL_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def beta_binomial_check ( a, b, c ):

#*****************************************************************************80
#
## BETA_BINOMIAL_CHECK checks the parameters of the Beta Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Input, integer C, a parameter of the PDF.
#    0 <= C.
#
#    Output, logical CHECK, is TRUE if the parameters are OK.
#
  if ( a <= 0.0 ):
    print ( '' )
    print ( 'BETA_BINOMIAL_CHECK - Fatal error!' )
    print ( '  A <= 0.' )
    check = False
    return check

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'BETA_BINOMIAL_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False
    return check

  if ( c < 0 ):
    print ( '' )
    print ( 'BETA_BINOMIAL_CHECK - Fatal error!' )
    print ( '  C < 0.' )
    check = False
    return check

  check = True

  return check

def beta_binomial_mean ( a, b, c ):

#*****************************************************************************80
#
## BETA_BINOMIAL_MEAN returns the mean of the Beta Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Input, integer C, a parameter of the PDF.
#    0 <= N.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = c * a / ( a + b )

  return mean

def beta_binomial_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## BETA_BINOMIAL_PDF evaluates the Beta Binomial PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) = Beta(A+X,B+C-X)
#      / ( (C+1) * Beta(X+1,C-X+1) * Beta(A,B) )  for 0 <= X <= C.
#
#    This PDF can be reformulated as:
#
#      The beta binomial probability density function for X successes
#      out of N trials is
#
#      PDF2(X)( N, MU, THETA ) =
#        C(N,X) * Product ( 0 <= R <= X - 1 ) ( MU + R * THETA )
#               * Product ( 0 <= R <= N - X - 1 ) ( 1 - MU + R * THETA )
#               / Product ( 0 <= R <= N - 1 )  ( 1 + R * THETA )
#
#      where
#
#        C(N,X) is the combinatorial coefficient
#        MU is the expectation of the underlying Beta distribution
#        THETA is a shape parameter.
#
#      A THETA value of 0 ( or A+B --> Infinity ) results in the binomial
#      distribution:
#
#        PDF2(X) ( N, MU, 0 ) = C(N,X) * MU**X * ( 1 - MU )**(N-X)
#
#    Given A, B, C for PDF, then the equivalent PDF2 has:
#
#      N     = C
#      MU    = A / ( A + B )
#      THETA = 1 / ( A + B )
#
#    Given N, MU, THETA for PDF2, the equivalent PDF has:
#
#      A = MU / THETA
#      B = ( 1 - MU ) / THETA
#      C = N
#
#    BETA_BINOMIAL_PDF(X)(1,1,C) = UNIFORM_DISCRETE_PDF(X)(0,C-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the argument of the PDF.
#
#    Input, real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Input, integer C, a parameter of the PDF.
#    0 <= C.
#
#    Output, real PDF, the value of the PDF.
#
  from r8_beta import r8_beta

  if ( x < 0 ):

    pdf = 0.0

  elif ( x <= c ):

    pdf = r8_beta ( a + x, b + c - x ) \
      / ( ( c + 1 ) * r8_beta ( x + 1, c - x + 1 ) * r8_beta ( a, b ) )

  elif ( c < x ):

    pdf = 0.0

  return pdf

def beta_binomial_sample ( a, b, c, seed ):

#*****************************************************************************80
#
## BETA_BINOMIAL_SAMPLE samples the Beta Binomial CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Input, integer C, a parameter of the PDF.
#    0 <= C.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = beta_binomial_cdf_inv ( cdf, a, b, c )

  return x, seed

def beta_binomial_sample_test ( ):

#*****************************************************************************80
#
## BETA_BINOMIAL_SAMPLE_TEST tests BETA_BINOMIAL_MEAN, BETA_BINOMIAL_SAMPLE, BETA_BINOMIAL_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_max import i4vec_max
  from i4vec_mean import i4vec_mean
  from i4vec_min import i4vec_min
  from i4vec_variance import i4vec_variance

  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'BETA_BINOMIAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BETA_BINOMIAL_MEAN computes the Beta Binomial mean' )
  print ( '  BETA_BINOMIAL_SAMPLE samples the Beta Binomial distribution' )
  print ( '  BETA_BINOMIAL_VARIANCE computes the Beta Binomial variance.' )

  a = 2.0
  b = 3.0
  c = 4

  check = beta_binomial_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'BETA_BINOMIAL_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = beta_binomial_mean ( a, b, c )
  variance = beta_binomial_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %6d' % ( c ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )
 
  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i], seed = beta_binomial_sample ( a, b, c, seed )

  mean = i4vec_mean ( nsample, x )
  variance = i4vec_variance ( nsample, x )
  xmax = i4vec_max ( nsample, x )
  xmin = i4vec_min ( nsample, x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BETA_BINOMIAL_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def beta_binomial_variance ( a, b, c ):

#*****************************************************************************80
#
## BETA_BINOMIAL_VARIANCE returns the variance of the Beta Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Input, integer C, a parameter of the PDF.
#    0 <= C.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = c * a * b * ( a + b + c ) / ( ( a + b ) ** 2 * ( a + b + 1.0 ) )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  beta_binomial_cdf_test ( )
  beta_binomial_sample_test ( )
  timestamp ( )

