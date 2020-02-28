#! /usr/bin/env python
#
def log_normal_cdf ( x, a, b ):

#*****************************************************************************80
#
## LOG_NORMAL_CDF evaluates the Lognormal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    0.0 < X.
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np
  from normal import normal_cdf

  if ( x <= 0.0 ):

    cdf = 0.0

  else:

    logx = np.log ( x )

    cdf = normal_cdf ( logx, a, b )

  return cdf

def log_normal_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## LOG_NORMAL_CDF_INV inverts the Lognormal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 March 2016
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
#    Input, real X, the corresponding argument.
#
  import numpy as np
  from normal import normal_cdf_inv
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'LOG_NORMAL_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'LOG_NORMAL_CDF_INV - Fatal error!' )

  logx = normal_cdf_inv ( cdf, a, b )

  x = np.exp ( logx )

  return x

def log_normal_cdf_test ( ):

#*****************************************************************************80
#
## LOG_NORMAL_CDF_TEST tests LOG_NORMAL_CDF, LOG_NORMAL_CDF_INV, LOG_NORMAL_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LOG_NORMAL_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LOG_NORMAL_CDF evaluates the Log Normal CDF' )
  print ( '  LOG_NORMAL_CDF_INV inverts the Log Normal CDF.' )
  print ( '  LOG_NORMAL_PDF evaluates the Log Normal PDF' )

  a = 10.0
  b = 2.25

  check = log_normal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'LOG_NORMAL_CDF_TEST - Fatal error!' )
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

    x, seed = log_normal_sample ( a, b, seed )

    pdf = log_normal_pdf ( x, a, b )

    cdf = log_normal_cdf ( x, a, b )

    x2 = log_normal_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LOG_NORMAL_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def log_normal_check ( a, b ):

#*****************************************************************************80
#
## LOG_NORMAL_CHECK checks the parameters of the Lognormal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 March 2016
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
    print ( 'LOG_NORMAL_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def log_normal_mean ( a, b ):

#*****************************************************************************80
#
## LOG_NORMAL_MEAN returns the mean of the Lognormal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 March 2016
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
  import numpy as np

  mean = np.exp ( a + 0.5 * b * b )

  return mean

def log_normal_pdf ( x, a, b ):

#*****************************************************************************80
#
## LOG_NORMAL_PDF evaluates the Lognormal PDF.
#
#  Discussion:
#
#    PDF(X)(A,B)
#      = EXP ( - 0.5 * ( ( LOG ( X ) - A ) / B )^2 )
#        / ( B * X * SQRT ( 2 * PI ) )
#
#    The Lognormal PDF is also known as the Cobb-Douglas PDF,
#    and as the Antilog_normal PDF.
#
#    The Lognormal PDF describes a variable X whose logarithm
#    is normally distributed.
#
#    The special case A = 0, B = 1 is known as Gilbrat's PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    0.0 < X
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= 0.0 ):
    pdf = 0.0
  else:
    pdf = np.exp ( - 0.5 * ( ( np.log ( x ) - a ) / b ) ** 2 ) \
      / ( b * x * np.sqrt ( 2.0 * np.pi ) )

  return pdf

def log_normal_sample ( a, b, seed ):

#*****************************************************************************80
#
## LOG_NORMAL_SAMPLE samples the Lognormal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 March 2016
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

  x = log_normal_cdf_inv ( cdf, a, b )

  return x, seed

def log_normal_sample_test ( ):

#*****************************************************************************80
#
## LOG_NORMAL_SAMPLE_TEST tests LOG_NORMAL_MEAN, LOG_NORMAL_SAMPLE, LOG_NORMAL_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 March 2016
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
  print ( 'LOG_NORMAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LOG_NORMAL_MEAN computes the Log Normal mean' )
  print ( '  LOG_NORMAL_SAMPLE samples the Log Normal distribution' )
  print ( '  LOG_NORMAL_VARIANCE computes the Log Normal variance.' )

  a = 1.0
  b = 2.0

  check = log_normal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'LOG_NORMAL_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = log_normal_mean ( a, b )
  variance = log_normal_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = log_normal_sample ( a, b, seed )

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
  print ( 'LOG_NORMAL_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def log_normal_variance ( a, b ):

#*****************************************************************************80
#
## LOG_NORMAL_VARIANCE returns the variance of the Lognormal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    21 March 2016
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

  variance = np.exp ( 2.0 * a + b * b ) * ( np.exp ( b * b ) - 1.0 )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  log_normal_cdf_test ( )
  log_normal_sample_test ( )
  timestamp ( )

