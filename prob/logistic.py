#! /usr/bin/env python
#
def logistic_cdf ( x, a, b ):

#*****************************************************************************80
#
## LOGISTIC_CDF evaluates the Logistic CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np

  cdf = 1.0 / ( 1.0 + np.exp ( ( a - x ) / b ) )

  return cdf

def logistic_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## LOGISTIC_CDF_INV inverts the Logistic CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
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
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real X, the corresponding argument.
#
  import numpy as np
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'LOGISTIC_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'LOGISTIC_CDF_INV - Fatal error!' )

  x = a - b * np.log ( ( 1.0 - cdf ) / cdf )

  return x

def logistic_cdf_test ( ):

#*****************************************************************************80
#
## LOGISTIC_CDF_TEST tests LOGISTIC_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LOGISTIC_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LOGISTIC_CDF evaluates the Logistic CDF' )
  print ( '  LOGISTIC_CDF_INV inverts the Logistic CDF.' )
  print ( '  LOGISTIC_PDF evaluates the Logistic PDF' )

  a = 1.0
  b = 2.0

  check = logistic_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'LOGISTIC_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = logistic_sample ( a, b, seed )

    pdf = logistic_pdf ( x, a, b )

    cdf = logistic_cdf ( x, a, b )

    x2 = logistic_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LOGISTIC_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def logistic_check ( a, b ):

#*****************************************************************************80
#
## LOGISTIC_CHECK checks the parameters of the Logistic CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'LOGISTIC_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def logistic_mean ( a, b ):

#*****************************************************************************80
#
## LOGISTIC_MEAN returns the mean of the Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def logistic_pdf ( x, a, b ):

#*****************************************************************************80
#
## LOGISTIC_PDF evaluates the Logistic PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = EXP ( ( A - X ) / B ) /
#      ( B * ( 1 + EXP ( ( A - X ) / B ) )^2 )
#
#    The Logistic PDF is also known as the Sech-Squared PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  temp = np.exp ( ( a - x ) / b )

  pdf = temp / ( b * ( 1.0 + temp ) ** 2 )

  return pdf

def logistic_sample ( a, b, seed ):

#*****************************************************************************80
#
## LOGISTIC_SAMPLE samples the Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = logistic_cdf_inv ( cdf, a, b )

  return x, seed

def logistic_sample_test ( ):

#*****************************************************************************80
#
## LOGISTIC_SAMPLE_TEST tests LOGISTIC_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
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
  print ( 'LOGISTIC_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LOGISTIC_MEAN computes the Logistic mean' )
  print ( '  LOGISTIC_SAMPLE samples the Logistic distribution' )
  print ( '  LOGISTIC_VARIANCE computes the Logistic variance.' )

  a = 2.0
  b = 3.0

  check = logistic_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'LOGISTIC_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = logistic_mean ( a, b )
  variance = logistic_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = logistic_sample ( a, b, seed )

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
  print ( 'LOGISTIC_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def logistic_variance ( a, b ):

#*****************************************************************************80
#
## LOGISTIC_VARIANCE returns the variance of the Logistic PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = ( np.pi * b ) ** 2 / 3.0

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  logistic_cdf_test ( )
  logistic_sample_test ( )
  timestamp ( )

