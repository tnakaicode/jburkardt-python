#! /usr/bin/env python
#
def normal_truncated_ab_cdf ( x, mu, s, a, b ):

#*****************************************************************************80
#
## NORMAL_TRUNCATED_AB_CDF evaluates the truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Input, real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Output, real CDF, the value of the CDF.
#
  from normal_01 import normal_01_cdf

  alpha = ( a - mu ) / s
  beta = ( b - mu ) / s
  xi = ( x - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )
  xi_cdf = normal_01_cdf ( xi )

  cdf = ( xi_cdf - alpha_cdf ) / ( beta_cdf - alpha_cdf )

  return cdf

def normal_truncated_ab_cdf_inv ( cdf, mu, s, a, b ):

#*****************************************************************************80
#
## NORMAL_TRUNCATED_AB_CDF_INV inverts the truncated Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
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
#    Input, real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Output, real X, the corresponding argument.
#
  from normal_01 import normal_01_cdf
  from normal_01 import normal_01_cdf_inv
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'NORMAL_TRUNCATED_AB_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'NORMAL_TRUNCATED_AB_CDF_INV - Fatal error!' )

  alpha = ( a - mu ) / s
  beta = ( b - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  xi_cdf = ( beta_cdf - alpha_cdf ) * cdf + alpha_cdf
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + s * xi

  return x

def normal_truncated_ab_cdf_test ( ):

#*****************************************************************************80
#
## NORMAL_TRUNCATED_AB_CDF_TEST tests NORMAL_TRUNCATED_AB_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  seed = 123456789
  a = 50.0
  b = 150.0
  mu = 100.0
  s = 25.0

  print ( '' )
  print ( 'NORMAL_TRUNCATED_AB_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_TRUNCATED_AB_CDF evaluates the Normal Truncated AB CDF.' )
  print ( '  NORMAL_TRUNCATED_AB_CDF_INV inverts the Normal Truncated AB CDF.' )
  print ( '  NORMAL_TRUNCATED_AB_PDF evaluates the Normal Truncated AB PDF.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( s ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,%g]' % ( a, b ) )

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = normal_truncated_ab_sample ( mu, s, a, b, seed )

    pdf = normal_truncated_ab_pdf ( x, mu, s, a, b )

    cdf = normal_truncated_ab_cdf ( x, mu, s, a, b )

    x2 = normal_truncated_ab_cdf_inv ( cdf, mu, s, a, b )

    print ( '  %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_TRUNCATED_AB_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def normal_truncated_ab_mean ( mu, s, a, b ):

#*****************************************************************************80
#
## NORMAL_TRUNCATED_AB_MEAN returns the mean of the truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, S, the mean and standard deviatione of the
#    parent Normal distribution.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Output, real MEAN, the mean of the PDF.
#
  from normal_01 import normal_01_cdf
  from normal_01 import normal_01_pdf

  alpha = ( a - mu ) / s
  beta = ( b - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = normal_01_pdf ( beta )

  mean = mu + s * ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf )

  return mean

def normal_truncated_ab_pdf ( x, mu, s, a, b ):

#*****************************************************************************80
#
## NORMAL_TRUNCATED_AB_PDF evaluates the truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 August 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Output, real PDF, the value of the PDF.
#
  from normal_01 import normal_01_cdf
  from normal_01 import normal_01_pdf

  alpha = ( a - mu ) / s
  beta = ( b - mu ) / s
  xi = ( x - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )
  xi_pdf = normal_01_pdf ( xi )

  pdf = xi_pdf / ( beta_cdf - alpha_cdf ) / s

  return pdf

def normal_truncated_ab_sample ( mu, s, a, b, seed ):

#*****************************************************************************80
#
## NORMAL_TRUNCATED_AB_SAMPLE samples the truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Input/output, integer SEED, a seed for the random number
#    generator.
#
#    Output, real X, a sample of the PDF.
#
  from normal_01 import normal_01_cdf
  from normal_01 import normal_01_cdf_inv
  from r8_uniform_01 import r8_uniform_01

  alpha = ( a - mu ) / s
  beta = ( b - mu ) / s

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  [ u, seed ] = r8_uniform_01 ( seed )
  xi_cdf = alpha_cdf + u * ( beta_cdf - alpha_cdf )
  xi = normal_01_cdf_inv ( xi_cdf )

  x = mu + s * xi

  return x, seed

def normal_truncated_ab_sample_test ( ):

#*****************************************************************************80
#
## NORMAL_TRUNCATED_AB_SAMPLE_TEST tests NORMAL_TRUNCATED_AB_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
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

  sample_num = 1000
  seed = 123456789
  a = 50.0
  b = 150.0
  mu = 100.0
  s = 25.0

  print ( '' )
  print ( 'NORMAL_TRUNCATED_AB_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_TRUNCATED_AB_MEAN computes the Normal Truncated AB mean' )
  print ( '  NORMAL_TRUNCATED_AB_SAMPLE samples the Normal Truncated AB distribution' )
  print ( '  NORMAL_TRUNCATED_AB_VARIANCE computes the Normal Truncated AB variance.' )
  print ( '' )
  print ( '  The "parent" normal distribution has' )
  print ( '    mean =               %g' % ( mu ) )
  print ( '    standard deviation = %g' % ( s ) )
  print ( '  The parent distribution is truncated to' )
  print ( '  the interval [%g,%g]' % ( a, b ) )

  mean = normal_truncated_ab_mean ( mu, s, a, b )

  variance = normal_truncated_ab_variance ( mu, s, a, b )

  print ( '' )
  print ( '  PDF mean      =               %g' % ( mean ) )
  print ( '  PDF variance =                %g' % ( variance ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i], seed = normal_truncated_ab_sample ( mu, s, a, b, seed )

  mean = r8vec_mean ( sample_num, x )
  variance = r8vec_variance ( sample_num, x )
  xmax = r8vec_max ( sample_num, x )
  xmin = r8vec_min ( sample_num, x )

  print ( '' )
  print ( '  Sample size =     %d' % ( sample_num ) )
  print ( '  Sample mean =     %g' % ( mean ) )
  print ( '  Sample variance = %g' % ( variance ) )
  print ( '  Sample maximum =  %g' % ( xmax ) )
  print ( '  Sample minimum =  %g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_TRUNCATED_AB_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def normal_truncated_ab_variance ( mu, s, a, b ):

#*****************************************************************************80
#
## NORMAL_TRUNCATED_AB_VARIANCE returns the variance of the truncated Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, S, the mean and standard deviation of the
#    parent Normal distribution.
#
#    Input, real A, B, the lower and upper truncation limits.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  from normal_01 import normal_01_cdf
  from normal_01 import normal_01_pdf

  alpha = ( a - mu ) / s
  beta = ( b - mu ) / s

  alpha_pdf = normal_01_pdf ( alpha )
  beta_pdf = normal_01_pdf ( beta )

  alpha_cdf = normal_01_cdf ( alpha )
  beta_cdf = normal_01_cdf ( beta )

  variance = s * s * ( 1.0 \
    + ( alpha * alpha_pdf - beta * beta_pdf ) / ( beta_cdf - alpha_cdf ) \
    - ( ( alpha_pdf - beta_pdf ) / ( beta_cdf - alpha_cdf ) ) ** 2 )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  normal_truncated_ab_cdf_test ( )
  normal_truncated_ab_sample_test ( )
  timestamp ( )
 
