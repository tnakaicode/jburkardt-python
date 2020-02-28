#! /usr/bin/env python
#
def weibull_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## WEIBULL_CDF evaluates the Weibull CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#    A <= X.
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np

  if ( x < a ):
    cdf = 0.0
  else:
    y = ( x - a ) / b
    cdf = 1.0 - 1.0 / np.exp ( y ** c )

  return cdf

def weibull_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## WEIBULL_CDF_INV inverts the Weibull CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#    0.0 < CDF < 1.0.
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#    Output, real X, the corresponding argument of the CDF.
#
  import numpy as np

  x = a + b * ( - np.log ( 1.0 - cdf ) ) ** ( 1.0 / c )

  return x

def weibull_cdf_test ( ):

#*****************************************************************************80
#
## WEIBULL_CDF_TEST tests WEIBULL_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'WEIBULL_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WEIBULL_CDF evaluates the Weibull CDF' )
  print ( '  WEIBULL_CDF_INV inverts the Weibull CDF.' )
  print ( '  WEIBULL_PDF evaluates the Weibull PDF' )

  x = 3.0

  a = 2.0
  b = 3.0
  c = 4.0

  check = weibull_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'WEIBULL_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )
 
  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = weibull_sample ( a, b, c, seed )

    pdf = weibull_pdf ( x, a, b, c )

    cdf = weibull_cdf ( x, a, b, c )

    x2 = weibull_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'WEIBULL_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def weibull_check ( a, b, c ):

#*****************************************************************************80
#
## WEIBULL_CHECK checks the parameters of the Weibull CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'WEIBULL_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'WEIBULL_CHECK - Fatal error!' )
    print ( '  C <= 0.' )
    check = False

  return check

def weibull_mean ( a, b, c ):

#*****************************************************************************80
#
## WEIBULL_MEAN returns the mean of the Weibull PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#    Output, real MEAN, the mean of the PDF.
#
  from r8_gamma import r8_gamma

  mean = b * r8_gamma ( ( c + 1.0 ) / c ) + a

  return mean

def weibull_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## WEIBULL_PDF evaluates the Weibull PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) = ( C / B ) * ( ( X - A ) / B )^( C - 1 )
#     * EXP ( - ( ( X - A ) / B )^C ).
#
#    The Weibull PDF is also known as the Frechet PDF.
#
#    WEIBULL_PDF(X)(A,B,1) is the Exponential PDF.
#
#    WEIBULL_PDF(X)(0,1,2) is the Rayleigh PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    A <= X
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < a ):

    pdf = 0.0

  else:

    y = ( x - a ) / b

    pdf = ( c / b ) * y ** ( c - 1.0 )  / np.exp ( y ** c )

  return pdf

def weibull_sample ( a, b, c, seed ):

#*****************************************************************************80
#
## WEIBULL_SAMPLE samples the Weibull PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = weibull_cdf_inv ( cdf, a, b, c )

  return x, seed

def weibull_sample_test ( ):

#*****************************************************************************80
#
## WEIBULL_SAMPLE_TEST tests WEIBULL_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
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
  print ( 'WEIBULL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WEIBULL_MEAN computes the Weibull mean' )
  print ( '  WEIBULL_SAMPLE samples the Weibull distribution' )
  print ( '  WEIBULL_VARIANCE computes the Weibull variance.' )

  a = 2.0
  b = 3.0
  c = 4.0

  check = weibull_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'WEIBULL_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = weibull_mean ( a, b, c )
  variance = weibull_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A =       %14g' % ( a ) )
  print ( '  PDF parameter B =       %14g' % ( b ) )
  print ( '  PDF parameter C =       %14g' % ( c ) )
  print ( '  PDF mean =              %14g' % ( mean ) )
  print ( '  PDF variance =          %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = weibull_sample ( a, b, c, seed )

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
  print ( 'WEIBULL_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def weibull_variance ( a, b, c ):

#*****************************************************************************80
#
## WEIBULL_VARIANCE returns the variance of the Weibull PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0.0 < B,
#    0.0 < C.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  from r8_gamma import r8_gamma

  g1 = r8_gamma ( ( c + 2.0 ) / c )
  g2 = r8_gamma ( ( c + 1.0 ) / c )

  variance = b * b * ( g1 - g2 * g2 )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  weibull_cdf_test ( )
  weibull_sample_test ( )
  timestamp ( )
 
