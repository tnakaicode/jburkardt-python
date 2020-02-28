#! /usr/bin/env python
#
def frechet_cdf ( x, alpha ):

#*****************************************************************************80
#
## FRECHET_CDF evaluates the Frechet CDF.
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
#    Input, real ALPHA, the parameter.
#    It is required that 0.0 < ALPHA.
#
#    Input, real X, the argument of the CDF.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np
  from sys import exit

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'FRECHET_CDF - Fatal error!' )
    print ( '  ALPHA <= 0.0.' )
    exit ( 'FRECHET_CDF - Fatal error!' )

  if ( x <= 0.0 ):
    cdf = 0.0
  else:
    cdf = np.exp ( - 1.0 / x ** alpha )

  return cdf

def frechet_cdf_inv ( cdf, alpha ):

#*****************************************************************************80
#
## FRECHET_CDF_INV inverts the Frechet CDF.
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
#    Input, real ALPHA, the parameter.
#    It is required that 0.0 < ALPHA.
#
#    Output, real X, the corresponding argument of the CDF.
#
  import numpy as np
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'FRECHET_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'FRECHET_CDF_INV - Fatal error!' )

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'FRECHET_CDF_INV - Fatal error!' )
    print ( '  ALPHA <= 0.0.' )
    exit ( 'FRECHET_CDF_INV - Fatal error!' )

  if ( cdf == 0.0 ):
    x = 0.0
  else:
    x =  ( - 1.0 / np.log ( cdf ) ) ** ( 1.0 / alpha )
 
  return x

def frechet_cdf_test ( ):

#*****************************************************************************80
#
## FRECHET_CDF_TEST tests FRECHET_CDF.
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

  seed = 1213456789

  print ( '' )
  print ( 'FRECHET_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FRECHET_CDF evaluates the Frechet CDF' )
  print ( '  FRECHET_CDF_INV inverts the Frechet CDF.' )
  print ( '  FRECHET_PDF evaluates the Frechet PDF' )

  alpha = 3.0

  print ( '' )
  print ( '  PDF parameter ALPHA =         %g' % ( alpha ) )

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = frechet_sample ( alpha, seed )

    pdf = frechet_pdf ( x, alpha )

    cdf = frechet_cdf ( x, alpha )

    x2 = frechet_cdf_inv ( cdf, alpha )

    print ( '  %12g  %12g  %12g  %12g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FRECHET_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def frechet_mean ( alpha ):

#*****************************************************************************80
#
## FRECHET_MEAN returns the mean of the Frechet PDF.
#
#  Discussion:
#
#    The distribution does not have a mean value unless 1 < ALPHA.
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
#    Input, real ALPHA, the parameter.
#    It is required that 1.0 < ALPHA.
#
#    Output, real MEAN, the mean of the PDF.
#
  from r8_gamma import r8_gamma
  from sys import exit

  if ( alpha <= 1.0 ):
    print ( '' )
    print ( 'FRECHET_MEAN - Fatal error!' )
    print ( '  Mean does not exist if ALPHA <= 1.' )
    exit ( 'FRECHET_MEAN - Fatal error!' )

  mean = r8_gamma ( ( alpha - 1.0 ) / alpha )

  return mean

def frechet_pdf ( x, alpha ):

#*****************************************************************************80
#
## FRECHET_PDF evaluates the Frechet PDF.
#
#  Discussion:
#
#    PDF(X) = ALPHA * exp ( -1 / X^ALPHA ) / X^(ALPHA+1)
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
#    Input, real ALPHA, the parameter.
#    It is required that 0.0 < ALPHA.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from sys import exit

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'FRECHET_PDF - Fatal error!' )
    print ( '  ALPHA <= 0.0.' )
    exit ( 'FRECHET_PDF - Fatal error!' )

  pdf = alpha * np.exp ( - 1.0 / x ** alpha ) / x ** ( alpha + 1.0 )

  return pdf

def frechet_sample ( alpha, seed ):

#*****************************************************************************80
#
## FRECHET_SAMPLE samples the Frechet PDF.
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
#    Input, real ALPHA, the parameter.
#    It is required that 0.0 < ALPHA.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
  from r8_uniform_01 import r8_uniform_01
  from sys import exit

  if ( alpha <= 0.0 ):
    print ( '' )
    print ( 'FRECHET_SAMPLE - Fatal error!' )
    print ( '  ALPHA <= 0.0.' )
    exit ( 'FRECHET_SAMPLE - Fatal error!' )

  cdf, seed = r8_uniform_01 ( seed )

  x = frechet_cdf_inv ( cdf, alpha )

  return x, seed

def frechet_sample_test ( ):

#*****************************************************************************80
#
## FRECHET_SAMPLE_TEST tests FRECHET_SAMPLE.
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
  print ( 'FRECHET_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FRECHET_MEAN computes the Frechet mean' )
  print ( '  FRECHET_SAMPLE samples the Frechet distribution' )
  print ( '  FRECHET_VARIANCE computes the Frechet variance.' )

  alpha = 3.0

  print ( '' )
  print ( '  PDF parameter ALPHA =         %g' % ( alpha ) )

  mean = frechet_mean ( alpha )
  variance = frechet_variance ( alpha )

  print ( '  PDF mean =                    %g' % ( mean ) )
  print ( '  PDF variance =                %g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = frechet_sample ( alpha, seed )

  mean = r8vec_mean ( nsample, x )
  variance = r8vec_variance ( nsample, x )
  xmax = r8vec_max ( nsample, x )
  xmin = r8vec_min ( nsample, x )

  print ( '' )
  print ( '  Sample size =     %g' % ( nsample ) )
  print ( '  Sample mean =     %g' % ( mean ) )
  print ( '  Sample variance = %g' % ( variance ) )
  print ( '  Sample maximum =  %g' % ( xmax ) )
  print ( '  Sample minimum =  %g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FRECHET_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def frechet_variance ( alpha ):

#*****************************************************************************80
#
## FRECHET_VARIANCE returns the variance of the Frechet PDF.
#
#  Discussion:
#
#    The PDF does not have a variance unless 2 < ALPHA.
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
#    Input, real ALPHA, the parameter.
#    It is required that 2.0 < ALPHA.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  from r8_gamma import r8_gamma
  from sys import exit

  if ( alpha <= 2.0 ):
    print ( '' )
    print ( 'FRECHET_VARIANCE - Fatal error!' )
    print ( '  Variance does not exist if ALPHA <= 2.' )
    exit ( 'FRECHET_VARIANCE - Fatal error!' )

  mean = r8_gamma ( ( alpha - 1.0 ) / alpha )

  variance = r8_gamma ( ( alpha - 2.0 ) / alpha ) - mean * mean

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  frechet_cdf_test ( )
  frechet_sample_test ( )
  timestamp ( )
 
