#! /usr/bin/env python
#
def anglit_cdf ( x ):

#*****************************************************************************80
#
## ANGLIT_CDF evaluates the Anglit CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 March 2016
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

  if ( x <  -0.25 * np.pi ):
    cdf = 0.0
  elif ( x < 0.25 * np.pi ):
    cdf = 0.5 - 0.5 * np.cos ( 2.0 * x + np.pi / 2.0 )
  else:
    cdf = 1.0

  return cdf

def anglit_cdf_inv ( cdf ):

#*****************************************************************************80
#
## ANGLIT_CDF_INV inverts the Anglit CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 March 2016
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
    print ( 'ANGLIT_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'ANGLIT_CDF_INV - Fatal error!' )

  x = 0.5 * ( np.arccos ( 1.0 - 2.0 * cdf ) - np.pi / 2.0 )

  return x

def anglit_cdf_test ( ):

#*****************************************************************************80
#
## ANGLIT_CDF_TEST tests ANGLIT_CDF, ANGLIT_CDF_INV, ANGLIT_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ANGLIT_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ANGLIT_CDF evaluates the Anglit CDF' )
  print ( '  ANGLIT_CDF_INV inverts the Anglit CDF.' )
  print ( '  ANGLIT_PDF evaluates the Anglit PDF' )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = anglit_sample ( seed )

    pdf = anglit_pdf ( x )

    cdf = anglit_cdf ( x )

    x2 = anglit_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ANGLIT_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def anglit_mean ( ):

#*****************************************************************************80
#
## ANGLIT_MEAN returns the mean of the Anglit PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 March 2016
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

def anglit_pdf ( x ):

#*****************************************************************************80
#
## ANGLIT_PDF evaluates the Anglit PDF.
#
#  Formula:
#
#    PDF(X) = SIN ( 2 * X + PI / 2 ) for -PI/4 <= X <= PI/4
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= -0.25 * np.pi or 0.25 * np.pi <= x ):
    pdf = 0.0
  else:
    pdf = np.sin ( 2.0 * x + 0.25 * np.pi )

  return pdf

def anglit_sample ( seed ):

#*****************************************************************************80
#
## ANGLIT_SAMPLE samples the Anglit PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 March 2016
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

  x = anglit_cdf_inv ( cdf )

  return x, seed

def anglit_sample_test ( ):

#*****************************************************************************80
#
## ANGLIT_SAMPLE_TEST tests ANGLIT_MEAN, ANGLIT_SAMPLE, ANGLIT_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_mean import r8vec_mean
  from r8vec_variance import r8vec_variance

  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'ANGLIT_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ANGLIT_MEAN computes the Anglit mean' )
  print ( '  ANGLIT_SAMPLE samples the Anglit distribution' )
  print ( '  ANGLIT_VARIANCE computes the Anglit variance.' )

  mean = anglit_mean ( )
  variance = anglit_variance ( )

  print ( '' )
  print ( '  PDF mean =     %14g' % ( mean ) )
  print ( '  PDF variance = %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i], seed = anglit_sample ( seed )

  mean = r8vec_mean ( nsample, x )
  variance = r8vec_variance ( nsample, x )

  xmax = np.max ( x )
  xmin = np.min ( x )

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
  print ( 'ANGLIT_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def anglit_variance ( ):

#*****************************************************************************80
#
## ANGLIT_VARIANCE returns the variance of the Anglit PDF.
#
#  Discussion:
#
#    Variance =
#      Integral ( -PI/4 <= X <= PI/4 ) X^2 * SIN ( 2 * X + PI / 2 )
#
#    Antiderivative =
#      0.5 * X * SIN ( 2 * X + PI / 2 )
#      + ( 0.25 - 0.5 * X^2 ) * COS ( 2 * X + PI / 2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 March 2016
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

  variance = 0.0625 * np.pi ** 2 - 0.5

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  anglit_cdf_test ( )
  anglit_sample_test ( )
  timestamp ( )
 
