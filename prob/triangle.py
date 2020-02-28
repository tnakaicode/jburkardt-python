#! /usr/bin/env python
#
def triangle_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## TRIANGLE_CDF evaluates the Triangle CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Input, real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#    Output, real CDF, the value of the CDF.
#
  if ( x <= a ):

    cdf = 0.0

  elif ( x <= b ):

    if ( a == b ):
      cdf = 0.0
    else:
      cdf = ( x - a ) * ( x - a ) / ( b - a ) / ( c - a )

  elif ( x <= c ):

    cdf = ( b - a ) / ( c - a ) \
      + ( 2.0 * c - b - x ) * ( x - b ) / ( c - b ) / ( c - a )

  else:

    cdf = 1.0

  return cdf

def triangle_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## TRIANGLE_CDF_INV inverts the Triangle CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    Input, real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#    Output, real X, the corresponding argument.
#
  import numpy as np
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'TRIANGLE_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'TRIANGLE_CDF_INV - Fatal error!' )

  d = 2.0 / ( c - a )
  cdf_mid = 0.5 * d * ( b - a )

  if ( cdf <= cdf_mid ):
    x = a + np.sqrt ( cdf * ( b - a ) * ( c - a ) )
  else:
    x = c - np.sqrt ( ( c - b ) * ( ( c - b ) - ( cdf - cdf_mid ) * ( c - a ) ) )

  return x

def triangle_cdf_test ( ):

#*****************************************************************************80
#
## TRIANGLE_CDF_TEST tests TRIANGLE_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRIANGLE_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_CDF evaluates the Triangle CDF' )
  print ( '  TRIANGLE_CDF_INV inverts the Triangle CDF.' )
  print ( '  TRIANGLE_PDF evaluates the Triangle PDF' )

  a = 1.0
  b = 3.0
  c = 10.0
  seed = 123456789

  print ( '' )
  print ( '  PDF parameter A =      %14g' % ( a ) )
  print ( '  PDF parameter B =      %14g' % ( b ) )
  print ( '  PDF parameter C =      %14g' % ( c ) )

  check = triangle_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'TRIANGLE_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = triangle_sample ( a, b, c, seed )

    pdf = triangle_pdf ( x, a, b, c )

    cdf = triangle_cdf ( x, a, b, c )

    x2 = triangle_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGLE_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def triangle_check ( a, b, c ):

#*****************************************************************************80
#
## TRIANGLE_CHECK checks the parameters of the Triangle CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#    Output, logical TRIANGLE_CHECK, is true if the parameters are legal.
#
  check = True

  if ( b < a ):
    print ( '' )
    print ( 'TRIANGLE_CHECK - Fatal error!' )
    print ( '  B < A.' )
    check = False

  if ( c < b ):
    print ( '' )
    print ( 'TRIANGLE_CHECK - Fatal error!' )
    print ( '  C < B.' )
    check = False

  if ( a == c ):
    print ( '' )
    print ( 'TRIANGLE_CHECK - Fatal error!' )
    print ( '  A == C.' )
    check = False

  return check

def triangle_mean ( a, b, c ):

#*****************************************************************************80
#
## TRIANGLE_MEAN returns the mean of the Triangle PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#    Output, real MEAN, the mean of the discrete uniform PDF.
#
  mean = a + ( c + b - 2.0 * a ) / 3.0

  return mean

def triangle_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## TRIANGLE_PDF evaluates the Triangle PDF.
#
#  Discussion:
#
#    Given points A <= B <= C, the probability is 0 to the left of A,
#    rises linearly to a maximum of 2/(C-A) at B, drops linearly to zero
#    at C, and is zero for all values greater than C.
#
#  Formula:
#
#    PDF(A,B,CX)
#      = 2 * ( X - A ) / ( B - A ) / ( C - A ) for A <= X <= B
#      = 2 * ( C - X ) / ( C - B ) / ( C - A ) for B <= X <= C.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#    Output, real PDF, the value of the PDF.
#
  if ( x <= a ):

    pdf = 0.0

  elif ( x <= b ):

    if ( a == b ):
      pdf = 0.0
    else:
      pdf = 2.0 * ( x - a ) / ( b - a ) / ( c - a )

  elif ( x <= c ):

    if ( b == c ):
      pdf = 0.0
    else:
      pdf = 2.0 * ( c - x ) / ( c - b ) / ( c - a )

  else:
    pdf = 0.0

  return pdf

def triangle_sample ( a, b, c, seed ):

#*****************************************************************************80
#
## TRIANGLE_SAMPLE samples the Triangle PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = triangle_cdf_inv ( cdf, a, b, c )

  return x, seed

def triangle_sample_test ( ):

#*****************************************************************************80
#
## TRIANGLE_SAMPLE_TEST tests TRIANGLE_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
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
  print ( 'TRIANGLE_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGLE_MEAN returns the Triangle mean' )
  print ( '  TRIANGLE_SAMPLE samples the Triangle distribution' )
  print ( '  TRIANGLE_VARIANCE returns the Triangle variance' )

  a = 1.0
  b = 3.0
  c = 10.0

  check = triangle_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'TRIANGLE_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )

  mean = triangle_mean ( a, b, c )
  variance = triangle_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter MEAN =          %14g' % ( mean ) )
  print ( '  PDF parameter VARIANCE =      %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = triangle_sample ( a, b, c, seed )

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
  print ( 'TRIANGLE_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def triangle_variance ( a, b, c ):

#*****************************************************************************80
#
## TRIANGLE_VARIANCE returns the variance of the Triangle PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    A <= B <= C and A < C.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = ( ( c - a ) * ( c - a ) \
             - ( c - a ) * ( b - a ) \
             + ( b - a ) * ( b - a ) ) / 18.0

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  triangle_cdf_test ( )
  triangle_sample_test ( )
  timestamp ( )

