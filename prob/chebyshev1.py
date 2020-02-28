#! /usr/bin/env python
#
def chebyshev1_cdf ( x ):

#*****************************************************************************80
#
## CHEBYSHEV1_CDF evaluates the Chebyshev1 CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np

  if ( x < - 1.0 ):
    cdf = 0.0
  elif ( 1.0 < x ):
    cdf = 1.0
  else:
    cdf = 0.5 + np.arcsin ( x ) / np.pi

  return cdf

def chebyshev1_cdf_inv ( cdf ):

#*****************************************************************************80
#
## CHEBYSHEV1_CDF_INV inverts the Chebyshev1 CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 August 2016
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
    print ( 'CHEBYSHEV1_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'CHEBYSHEV1_CDF_INV - Fatal error!' )

  x = np.sin ( np.pi * ( cdf - 0.5 ) )

  return x

def chebyshev1_cdf_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV1_CDF_TEST tests CHEBYSHEV1_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 AUgust 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CHEBYSHEV1_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHEBYSHEV1_CDF evaluates the Chebyshev1 CDF' )
  print ( '  CHEBYSHEV1_CDF_INV inverts the Chebyshev1 CDF.' )
  print ( '  CHEBYSHEV1_PDF evaluates the Chebyshev1 PDF' )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = chebyshev1_sample ( seed )

    pdf = chebyshev1_pdf ( x )

    cdf = chebyshev1_cdf ( x )

    x2 = chebyshev1_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHEBYSHEV1_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def chebyshev1_mean ( ):

#*****************************************************************************80
#
## CHEBYSHEV1_MEAN returns the mean of the Chebyshev1 PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = 0.0

  return mean

def chebyshev1_pdf ( x ):

#*****************************************************************************80
#
## CHEBYSHEV1_PDF evaluates the Chebyshev1 PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    0.0 <= X <= 1.0.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= -1.0 or 1.0 <= x ):
    pdf = 0.0
  else:
    pdf = 1.0 / np.pi / np.sqrt ( 1.0 - x * x )

  return pdf

def chebyshev1_sample ( seed ):

#*****************************************************************************80
#
## CHEBYSHEV1_SAMPLE samples the Chebyshev1 PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 August 2016
#
#  Parameters:
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real VALUE, a random value between 0 and 1.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  value = chebyshev1_cdf_inv ( cdf )

  return value, seed

def chebyshev1_sample_test ( ):

#*****************************************************************************80
#
## CHEBYSHEV1_SAMPLE_TEST tests CHEBYSHEV1_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 August 2016
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
  print ( 'CHEBYSHEV1_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHEBYSHEV1_MEAN computes the Chebyshev1 mean' )
  print ( '  CHEBYSHEV1_SAMPLE samples the Chebyshev1 distribution' )
  print ( '  CHEBYSHEV1_VARIANCE computes the Chebyshev1 variance.' )

  mean = chebyshev1_mean ( )
  variance = chebyshev1_variance ( )

  print ( '' )
  print ( '  PDF mean =            %14g' % ( mean ) )
  print ( '  PDF variance =        %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = chebyshev1_sample ( seed )

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
  print ( 'CHEBYSHEV1_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def chebyshev1_variance ( ):

#*****************************************************************************80
#
## CHEBYSHEV1_VARIANCE returns the variance of the Chebyshev1 PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 August 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = 0.5

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  chebyshev1_cdf_test ( )
  chebyshev1_sample_test ( )
  timestamp ( )
 
