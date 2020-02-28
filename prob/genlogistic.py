#! /usr/bin/env python
#
def genlogistic_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## GENLOGISTIC_CDF evaluates the Generalized Logistic CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
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
  import numpy as np

  y = ( x - a ) / b

  cdf = 1.0 / ( 1.0 + np.exp ( - y ) ) ** c

  return cdf

def genlogistic_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## GENLOGISTIC_CDF_INV inverts the Generalized Logistic CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
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
#    Output, real X, the corresponding argument.
#
  import numpy as np

  r8_huge = 1.0E+30

  if ( cdf <= 0.0 ):
    x = - r8_huge
  elif ( cdf < 1.0 ):
    x = a - b * np.log ( cdf ** ( - 1.0 / c ) - 1.0 )
  elif ( 1.0 <= cdf ):
    x = r8_huge

  return x

def genlogistic_cdf_test ( ):

#*****************************************************************************80
#
## GENLOGISTIC_CDF_TEST tests GENLOGISTIC_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'GENLOGISTIC_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GENLOGISTIC_PDF evaluates the Genlogistic PDF.' )
  print ( '  GENLOGISTIC_CDF evaluates the Genlogistic CDF' )
  print ( '  GENLOGISTIC_CDF_INV inverts the Genlogistic CDF.' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = genlogistic_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'GENLOGISTIC_CDF_TEST - Fatal error!' )
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

    x, seed = genlogistic_sample ( a, b, c, seed )

    pdf = genlogistic_pdf ( x, a, b, c )

    cdf = genlogistic_cdf ( x, a, b, c )

    x2 = genlogistic_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GENLOGISTIC_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def genlogistic_check ( a, b, c ):

#*****************************************************************************80
#
## GENLOGISTIC_CHECK checks the parameters of the Generalized Logistic CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
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
    print ( 'GENLOGISTIC_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'GENLOGISTIC_CHECK - Fatal error!' )
    print ( '  C <= 0.' )
    check = False

  return check

def genlogistic_mean ( a, b, c ):

#*****************************************************************************80
#
## GENLOGISTIC_MEAN returns the mean of the Generalized Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
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
  from digamma import digamma

  euler_constant = 0.5772156649015328

  mean = a + b * ( euler_constant + digamma ( c ) )

  return mean

def genlogistic_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## GENLOGISTIC_PDF evaluates the Generalized Logistic PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) = ( C / B ) * EXP ( ( A - X ) / B ) /
#      ( ( 1 + EXP ( ( A - X ) / B ) )^(C+1) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
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
#    0.0 < B,
#    0.0 < C.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  y = ( x - a ) / b

  pdf = ( c / b ) * np.exp ( - y ) / ( 1.0 + np.exp ( - y ) ) ** ( c + 1.0 )

  return pdf

def genlogistic_sample ( a, b, c, seed ):

#*****************************************************************************80
#
## GENLOGISTIC_SAMPLE samples the Generalized Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
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

  x = genlogistic_cdf_inv ( cdf, a, b, c )

  return x, seed

def genlogistic_sample_test ( ):

#*****************************************************************************80
#
## GENLOGISTIC_SAMPLE_TEST tests GENLOGISTIC_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
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
  print ( 'GENLOGISTIC_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GENLOGISTIC_MEAN computes the Genlogistic mean' )
  print ( '  GENLOGISTIC_SAMPLE samples the Genlogistic distribution' )
  print ( '  GENLOGISTIC_VARIANCE computes the Genlogistic variance.' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = genlogistic_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'GENLOGISTIC_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = genlogistic_mean ( a, b, c )
  variance = genlogistic_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = genlogistic_sample ( a, b, c, seed )

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
  print ( 'GENLOGISTIC_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def genlogistic_variance ( a, b, c ):

#*****************************************************************************80
#
## GENLOGISTIC_VARIANCE returns the variance of the Generalized Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
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
  from trigamma import trigamma

  variance = b * b * ( np.pi * np.pi / 6.0 + trigamma ( c ) )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  genlogistic_cdf_test ( )
  genlogistic_sample_test ( )
  timestamp ( )
