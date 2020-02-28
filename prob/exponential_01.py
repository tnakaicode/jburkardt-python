#! /usr/bin/env python
#
def exponential_01_cdf ( x ):

#*****************************************************************************80
#
## EXPONENTIAL_01_CDF evaluates the Exponential 01 CDF.
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
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= 0.0 ):
    cdf = 0.0
  else:
    cdf = 1.0 - np.exp ( - x )

  return cdf

def exponential_01_cdf_inv ( cdf ):

#*****************************************************************************80
#
## EXPONENTIAL_01_CDF_INV inverts the Exponential 01 CDF.
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
#    Output, real X, the corresponding argument.
#
  import numpy as np
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'EXPONENTIAL_01_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'EXPONENTIAL_01_CDF_INV - Fatal error!' )

  x = - np.log ( 1.0 - cdf )

  return x

def exponential_01_cdf_test ( ):

#*****************************************************************************80
#
## EXPONENTIAL_01_CDF_TEST tests EXPONENTIAL_01_CDF.
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
  print ( 'EXPONENTIAL_01_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EXPONENTIAL_01_CDF evaluates the Exponential 01 CDF.' )
  print ( '  EXPONENTIAL_01_CDF_INV inverts the Exponential 01 CDF.' )
  print ( '  EXPONENTIAL_01_PDF evaluates the Exponential 01 PDF.' )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = exponential_01_sample ( seed )

    pdf = exponential_01_pdf ( x )

    cdf = exponential_01_cdf ( x )

    x2 = exponential_01_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'EXPONENTIAL_01_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def exponential_01_mean ( ):

#*****************************************************************************80
#
## EXPONENTIAL_01_MEAN returns the mean of the Exponential 01 PDF.
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
#    Output, real MEAN, the mean of the PDF.
#
  mean = 1.0;

  return mean

def exponential_01_pdf ( x ):

#*****************************************************************************80
#
## EXPONENTIAL_01_PDF evaluates the Exponential 01 PDF.
#
#  Discussion:
#
#    PDF(X) = EXP ( - X )
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
#    0.0 <= X
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < 0.0 ):
    pdf = 0.0
  else:
    pdf = np.exp ( - x )

  return pdf

def exponential_01_sample ( seed ):

#*****************************************************************************80
#
## EXPONENTIAL_01_SAMPLE samples the Exponential PDF with parameter 1.
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
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = - np.log ( 1.0 - cdf )

  return x, seed

def exponential_01_sample_test ( ):

#*****************************************************************************80
#
## EXPONENTIAL_01_SAMPLE_TEST tests EXPONENTIAL_01_SAMPLE.
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
  print ( 'EXPONENTIAL_01_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EXPONENTIAL_01_MEAN computes the Exponential 01 mean' )
  print ( '  EXPONENTIAL_01_SAMPLE samples the Exponential 01 distribution' )
  print ( '  EXPONENTIAL_01_VARIANCE computes the Exponential 01 variance.' )

  mean = exponential_01_mean ( )
  variance = exponential_01_variance ( )

  print ( '' )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = exponential_01_sample ( seed )

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
  print ( 'EXPONENTIAL_01_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def exponential_01_variance ( ):

#*****************************************************************************80
#
## EXPONENTIAL_01_VARIANCE returns the variance of the Exponential 01 PDF.
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
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = 1.0

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  exponential_01_cdf_test ( )
  exponential_01_sample_test ( )
  timestamp ( )
 
