#! /usr/bin/env python
#
def log_uniform_cdf ( x, a, b ):

#*****************************************************************************80
#
## LOG_UNIFORM_CDF evaluates the Log Uniform CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
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

  if ( x <= a ):
    cdf = 0.0
  elif ( x < b ):
    cdf = ( np.log ( x ) - np.log ( a ) ) / ( np.log ( b ) - np.log ( a ) )
  else:
    cdf = 1.0

  return cdf

def log_uniform_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## LOG_UNIFORM_CDF_INV inverts the Log Uniform CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
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
    print ( 'LOG_UNIFORM_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'LOG_UNIFORM_CDF_INV - Fatal error!' )

  x = a * np.exp ( ( np.log ( b ) - np.log ( a ) ) * cdf )

  return x

def log_uniform_cdf_test ( ):

#*****************************************************************************80
#
## LOG_UNIFORM_CDF_TEST tests LOG_UNIFORM_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LOG_UNIFORM_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LOG_UNIFORM_CDF evaluates the Log Uniform CDF' )
  print ( '  LOG_UNIFORM_CDF_INV inverts the Log Uniform CDF.' )
  print ( '  LOG_UNIFORM_PDF evaluates the Log Uniform PDF' )

  a = 2.0
  b = 20.0

  check = log_uniform_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'LOG_UNIFORM_CDF_TEST - Fatal error!' )
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

    x, seed = log_uniform_sample ( a, b, seed )

    pdf = log_uniform_pdf ( x, a, b )

    cdf = log_uniform_cdf ( x, a, b )

    x2 = log_uniform_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LOG_UNIFORM_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def log_uniform_check ( a, b ):

#*****************************************************************************80
#
## LOG_UNIFORM_CHECK checks the parameters of the Log Uniform CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    1.0 < A < B.
#
#    Output, logical LOG_UNIFORM_CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 1.0 ):
    print ( '' )
    print ( 'LOG_UNIFORM_CHECK - Fatal error!' )
    print ( '  A <= 1.' )
    check = False

  if ( b <= a ):
    print ( '' )
    print ( 'LOG_UNIFORM_CHECK - Fatal error!' )
    print ( '  B <= A.' )
    check = False

  return check

def log_uniform_mean ( a, b ):

#*****************************************************************************80
#
## LOG_UNIFORM_MEAN returns the mean of the Log Uniform PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    1.0 < A < B.
#
#    Output, real MEAN, the mean of the PDF.
#
  import numpy as np

  mean = ( b - a ) / ( np.log ( b ) - np.log ( a ) )

  return mean

def log_uniform_pdf ( x, a, b ):

#*****************************************************************************80
#
## LOG_UNIFORM_PDF evaluates the Log Uniform PDF.
#
#  Discussion:
#
#    PDF(A,BX) = 1 / ( X * ( log ( B ) - log ( A ) ) ) for A <= X <= B
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
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
#    1.0 < A < B.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < a ):
    pdf = 0.0
  elif ( x <= b ):
    pdf = 1.0 / ( x * ( np.log ( b ) - np.log ( a ) ) )
  else:
    pdf = 0.0

  return pdf

def log_uniform_sample ( a, b, seed ):

#*****************************************************************************80
#
## LOG_UNIFORM_SAMPLE samples the Log Uniform PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    1.0 < A < B.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = log_uniform_cdf_inv ( cdf, a, b )

  return x, seed

def log_uniform_sample_test ( ):

#*****************************************************************************80
#
## LOG_UNIFORM_SAMPLE_TEST tests LOG_UNIFORM_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
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
  print ( 'LOG_UNIFORM_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LOG_UNIFORM_MEAN computes the Log Uniform mean' )
  print ( '  LOG_UNIFORM_SAMPLE samples the Log Uniform distribution' )
  print ( '  LOG_UNIFORM_VARIANCE computes the Log Uniform variance' )

  a = 2.0
  b = 20.0

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )

  check = log_uniform_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'LOG_UNIFORM_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = log_uniform_mean ( a, b )
  variance = log_uniform_variance ( a, b )

  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = log_uniform_sample ( a, b, seed )

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
  print ( 'LOG_UNIFORM_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def log_uniform_variance ( a, b ):

#*****************************************************************************80
#
## LOG_UNIFORM_VARIANCE returns the variance of the Log Uniform PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    1.0 < A < B.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  import numpy as np

  mean = log_uniform_mean ( a, b )

  variance = \
    ( ( 0.5 * b * b - 2.0 * mean * b + mean * mean * np.log ( b ) ) \
    - ( 0.5 * a * a - 2.0 * mean * a + mean * mean * np.log ( a ) ) ) \
    / ( np.log ( b ) - np.log ( a ) )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  log_uniform_cdf_test ( )
  log_uniform_sample_test ( )
  timestamp ( )
