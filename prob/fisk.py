#! /usr/bin/env python
#
def fisk_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## FISK_CDF evaluates the Fisk CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
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
#    0.0 < B,
#    0.0 < C.
#
#    Output, real CDF, the value of the CDF.
#
  if ( x <= a ):
    cdf = 0.0
  else:
    cdf = 1.0 / ( 1.0 + ( b / ( x - a ) ) ** c )

  return cdf

def fisk_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## FISK_CDF_INV inverts the Fisk CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
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
#    0.0 < B,
#    0.0 < C.
#
#    Output, real X, the corresponding argument of the CDF.
#
  from sys import exit

  r8_huge = 1.0E+30

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'FISK_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'FISK_CDF_INV - Fatal error!' )

  if ( cdf <= 0.0 ):
    x = a
  elif ( cdf < 1.0 ):
    x = a + b * ( cdf / ( 1.0 - cdf ) ) ** ( 1.0 / c )
  elif ( 1.0 <= cdf ):
    x = r8_huge

  return x

def fisk_cdf_test ( ):

#*****************************************************************************80
#
## FISK_CDF_TEST tests FISK_CDF, FISK_CDF_INV, FISK_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'FISK_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FISK_CDF evaluates the Fisk CDF' )
  print ( '  FISK_CDF_INV inverts the Fisk CDF.' )
  print ( '  FISK_PDF evaluates the Fisk PDF' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = fisk_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'FISK_CDF_TEST - Fatal error!' )
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

    x, seed = fisk_sample ( a, b, c, seed )

    pdf = fisk_pdf ( x, a, b, c )

    cdf = fisk_cdf ( x, a, b, c )

    x2 = fisk_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FISK_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def fisk_check ( a, b, c ):

#*****************************************************************************80
#
## FISK_CHECK checks the parameters of the Fisk PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
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
    print ( 'FISK_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'FISK_CHECK - Fatal error!' )
    print ( '  C <= 0.' )
    check = False

  return check

def fisk_mean ( a, b, c ):

#*****************************************************************************80
#
## FISK_MEAN returns the mean of the Fisk PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
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
  import numpy as np
  from r8_csc import r8_csc
  from sys import exit

  if ( c <= 1.0 ):
    print ( '' )
    print ( 'FISK_MEAN - Fatal error!' )
    print ( '  No mean defined for C <= 1.0' )
    exit ( 'FISK_MEAN - Fatal error!' )

  mean = a + np.pi * ( b / c ) * r8_csc ( np.pi / c )

  return mean

def fisk_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## FISK_PDF evaluates the Fisk PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) =
#      ( C / B ) * ( ( X - A ) / B )^( C - 1 ) /
#      ( 1 + ( ( X - A ) / B )^C )^2
#
#    The Fisk PDF is also known as the Log Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
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
  if ( x <= a ):

    pdf = 0.0 

  else:

    y = ( x - a ) / b

    pdf = ( c / b ) * y ** ( c - 1.0 ) / ( 1.0 + y ** c ) ** 2

  return pdf

def fisk_sample ( a, b, c, seed ):

#*****************************************************************************80
#
## FISK_SAMPLE samples the Fisk PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
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

  x = fisk_cdf_inv ( cdf, a, b, c )

  return x, seed

def fisk_sample_test ( ):

#*****************************************************************************80
#
## FISK_SAMPLE_TEST tests FISK_MEAN, FISK_SAMPLE, FISK_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
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
  print ( 'FISK_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FISK_MEAN computes the Fisk mean' )
  print ( '  FISK_SAMPLE samples the Fisk distribution' )
  print ( '  FISK_VARIANCE computes the Fisk variance.' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = fisk_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'FISK_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = fisk_mean ( a, b, c )
  variance = fisk_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i], seed = fisk_sample ( a, b, c, seed )

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
  print ( 'FISK_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def fisk_variance ( a, b, c ):

#*****************************************************************************80
#
## FISK_VARIANCE returns the variance of the Fisk PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2016
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
  import numpy as np
  from r8_csc import r8_csc
  from sys import exit

  if ( c <= 2.0 ):
    print ( '' )
    print ( 'FISK_VARIANCE - Fatal error!' )
    print ( '  No variance defined for C <= 2.0' )
    exit ( 'FISK_VARIANCE - Fatal error!' )

  g = np.pi / c

  variance = b ** 2 * ( 2.0 * g * r8_csc ( 2.0 * g ) - ( g * r8_csc ( g ) ) ** 2 )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  fisk_cdf_test ( )
  fisk_sample_test ( )
  timestamp ( )
 

