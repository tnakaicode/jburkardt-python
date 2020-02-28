#! /usr/bin/env python
#
def normal_cdf ( x, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_CDF evaluates the Normal CDF.
#
#  Discussion:
#
#    The Normal CDF is related to the Error Function ERF(X) by:
#
#      ERF ( X ) = 2 * NORMAL_CDF ( SQRT ( 2 ) * X ) - 1.0.
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
#    Input, real X, the argument of the CDF.
#
#    Input, real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#    Output, real CDF, the value of the CDF.
#
  from normal_01 import normal_01_cdf

  y = ( x - mu ) / sigma

  cdf = normal_01_cdf ( y )

  return cdf

def normal_cdf_inv ( cdf, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_CDF_INV inverts the Normal CDF.
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
#    Input, real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#    Output, real X, the corresponding argument.
#
  from normal_01 import normal_01_cdf_inv
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'NORMAL_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'NORMAL_CDF_INV - Fatal error!' )

  x2 = normal_01_cdf_inv ( cdf )

  x = mu + sigma * x2

  return x

def normal_cdf_test ( ):

#*****************************************************************************80
#
## NORMAL_CDF_TEST tests NORMAL_CDF, NORMAL_CDF_INV, NORMAL_PDF
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
  print ( 'NORMAL_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_CDF evaluates the Normal CDF' )
  print ( '  NORMAL_CDF_INV inverts the Normal CDF.' )
  print ( '  NORMAL_PDF evaluates the Normal PDF' )

  mu = 100.0
  sigma = 15.0

  check = normal_check ( mu, sigma )

  if ( not check ):
    print ( '' )
    print ( 'NORMAL_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter MU =    %14g' % ( mu ) )
  print ( '  PDF parameter SIGMA = %14g' % ( sigma ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = normal_sample ( mu, sigma, seed )

    pdf = normal_pdf ( x, mu, sigma )

    cdf = normal_cdf ( x, mu, sigma )

    x2 = normal_cdf_inv ( cdf, mu, sigma )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def normal_check ( mu, sigma ):

#*****************************************************************************80
#
## NORMAL_CHECK checks the parameters of the Normal PDF.
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
#    Input, real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( sigma == 0.0 ):
    print ( '' )
    print ( 'NORMAL_CHECK - Fatal error!' )
    print ( '  SIGMA == 0.' )
    check = False

  return check

def normal_mean ( mu, sigma ):

#*****************************************************************************80
#
## NORMAL_MEAN returns the mean of the Normal PDF.
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
#    Input, real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#    Output, real MEAN, the mean of the PDF.
#
  return mu

def normal_pdf ( x, mu, sigma ):

#*****************************************************************************80
#
## NORMAL_PDF evaluates the Normal PDF.
#
#  Discussion:
#
#    The normal PDF is also known as the Gaussian PDF.
#
#  Formula:
#
#    PDF(X;MU,SIGMA) = 
#      EXP ( - 0.5 * ( ( X - MU ) / SIGMA )^2 ) / SQRT ( 2 * PI * SIGMA^2 )
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
#    Input, real X(), the argument of the PDF.
#
#    Input, real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#    Output, real PDF(), the value of the PDF.
#
  import numpy as np

  pdf = np.exp ( - 0.5 * ( ( x - mu ) / sigma ) ** 2 ) \
    / np.sqrt ( 2.0 * np.pi * sigma ** 2 )

  return pdf

def normal_sample ( mu, sigma, seed ):

#*****************************************************************************80
#
## NORMAL_SAMPLE samples the Normal PDF.
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
#    Input, real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from normal_01 import normal_01_sample

  y, seed = normal_01_sample ( seed )

  x = mu + sigma * y

  return x, seed

def normal_sample_test ( ):

#*****************************************************************************80
#
## NORMAL_SAMPLE_TEST tests NORMAL_MEAN, NORMAL_SAMPLE, NORMAL_VARIANCE.
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
  print ( 'NORMAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_MEAN computes the Normal mean' )
  print ( '  NORMAL_SAMPLE samples the Normal distribution' )
  print ( '  NORMAL_VARIANCE returns the Normal variance.' )

  mu = 100.0
  sigma = 15.0

  check = normal_check ( mu, sigma )

  if ( not check ):
    print ( '' )
    print ( 'NORMAL_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
 
  mean = normal_mean ( mu, sigma )
  variance = normal_variance ( mu, sigma )

  print ( '' )
  print ( '  PDF parameter MU =    %14g' % ( mu ) )
  print ( '  PDF parameter SIGMA = %14g' % ( sigma ) )
  print ( '  PDF mean =            %14g' % ( mean ) )
  print ( '  PDF variance =        %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i], seed = normal_sample ( mu, sigma, seed )

  mean = r8vec_mean ( nsample, x )
  variance = r8vec_variance ( nsample, x )
  xmax = r8vec_max ( nsample, x )
  xmin = r8vec_min ( nsample, x )

  print ( '' )
  print ( '  Sample size =     %6d'  % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def normal_samples ( n, mu, sigma, seed ):

#*****************************************************************************80
#
## NORMAL_SAMPLES returns multiple samples of the Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of samples.
#
#    Input, real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X[N], samples of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from normal_01 import normal_01_samples

  y, seed = normal_01_samples ( n, seed )

  x = np.zeros ( n )

  x[0:n] = mu + sigma * y[0:n]

  return x, seed

def normal_samples_test ( ):

#*****************************************************************************80
#
## NORMAL_SAMPLES_TEST tests NORMAL_MEAN, NORMAL_SAMPLES, NORMAL_VARIANCE.
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
  print ( 'NORMAL_SAMPLES_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NORMAL_MEAN computes the Normal mean' )
  print ( '  NORMAL_SAMPLES samples the Normal distribution' )
  print ( '  NORMAL_VARIANCE returns the Normal variance.' )

  mu = 100.0
  sigma = 15.0

  check = normal_check ( mu, sigma )

  if ( not check ):
    print ( '' )
    print ( 'NORMAL_SAMPLES_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
 
  mean = normal_mean ( mu, sigma )
  variance = normal_variance ( mu, sigma )

  print ( '' )
  print ( '  PDF parameter MU =    %14g' % ( mu ) )
  print ( '  PDF parameter SIGMA = %14g' % ( sigma ) )
  print ( '  PDF mean =            %14g' % ( mean ) )
  print ( '  PDF variance =        %14g' % ( variance ) )

  x, seed = normal_samples ( nsample, mu, sigma, seed )

  mean = r8vec_mean ( nsample, x )
  variance = r8vec_variance ( nsample, x )
  xmax = r8vec_max ( nsample, x )
  xmin = r8vec_min ( nsample, x )

  print ( '' )
  print ( '  Sample size =     %6d'  % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g' % ( xmax ) )
  print ( '  Sample minimum =  %14g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NORMAL_SAMPLES_TEST' )
  print ( '  Normal end of execution.' )
  return

def normal_variance ( mu, sigma ):

#*****************************************************************************80
#
## NORMAL_VARIANCE returns the variance of the Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real MU, SIGMA, the mean and standard deviation.
#    SIGMA should be nonzero.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = sigma * sigma

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  normal_cdf_test ( )
  normal_sample_test ( )
  normal_samples_test ( )
  timestamp ( )
 
