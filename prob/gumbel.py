#! /usr/bin/env python
#
def gumbel_cdf ( x ):

#*****************************************************************************80
#
## GUMBEL_CDF evaluates the Gumbel CDF.
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
#    Output, real CDF, the value of the CDF.
#
  import numpy as np

  cdf = np.exp ( - np.exp ( - x ) )

  return cdf

def gumbel_cdf_inv ( cdf ):

#*****************************************************************************80
#
## GUMBEL_CDF_INV inverts the Gumbel CDF.
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
#    Output, real X, the corresponding argument of the CDF.
#
  import numpy as np
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'GUMBEL_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'GUMBEL_CDF_INV - Fatal error!' )

  x =  - np.log ( - np.log ( cdf ) )

  return x

def gumbel_cdf_test ( ):

#*****************************************************************************80
#
## GUMBEL_CDF_TEST tests GUMBEL_CDF.
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
  print ( 'GUMBEL_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GUMBEL_CDF evaluates the Gumbel CDF.' )
  print ( '  GUMBEL_CDF_INV inverts the Gumbel CDF.' )
  print ( '  GUMBEL_PDF evaluates the Gumbel PDF.' )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = gumbel_sample ( seed )

    pdf = gumbel_pdf ( x )

    cdf = gumbel_cdf ( x )

    x2 = gumbel_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GUMBEL_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def gumbel_mean ( ):

#*****************************************************************************80
#
## GUMBEL_MEAN returns the mean of the Gumbel PDF.
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
#    Output, real MEAN, the mean of the PDF.
#
  euler_constant = 0.5772156649015328;

  mean = euler_constant

  return mean

def gumbel_pdf ( x ):

#*****************************************************************************80
#
## GUMBEL_PDF evaluates the Gumbel PDF.
#
#  Discussion:
#
#    PDF(X) = EXP ( - X - EXP ( - X  ) ).
#
#    GUMBEL_PDF(X) = EXTREME_PDF(X)(0,1)
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
#  Reference:
#
#    Eric Weisstein, editor,
#    CRC Concise Encylopedia of Mathematics,
#    CRC Press, 1998.
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  pdf = np.exp ( - x - np.exp ( - x ) )

  return pdf

def gumbel_sample ( seed ):

#*****************************************************************************80
#
## GUMBEL_SAMPLE samples the Gumbel PDF.
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
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = gumbel_cdf_inv ( cdf )

  return x, seed

def gumbel_sample_test ( ):

#*****************************************************************************80
#
## GUMBEL_SAMPLE_TEST tests GUMBEL_SAMPLE.
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
  print ( 'GUMBEL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GUMBEL_MEAN computes the Gumbel mean' )
  print ( '  GUMBEL_SAMPLE samples the Gumbel distribution' )
  print ( '  GUMBEL_VARIANCE computes the Gumbel variance.' )

  mean = gumbel_mean ( )

  variance = gumbel_variance ( )

  print ( '' )
  print ( '  PDF mean      =               %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = gumbel_sample ( seed )

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
  print ( 'GUMBEL_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def gumbel_variance ( ):

#*****************************************************************************80
#
## GUMBEL_VARIANCE returns the variance of the Gumbel PDF.
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
#    Output, real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = np.pi * np.pi / 6.0

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  gumbel_cdf_test ( )
  gumbel_sample_test ( )
  timestamp ( )
 
