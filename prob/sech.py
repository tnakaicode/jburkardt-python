#! /usr/bin/env python
#
def sech_cdf ( x, a, b ):

#*****************************************************************************80
#
## SECH_CDF evaluates the Hyperbolic Secant CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real A, B, the parameter of the PDF.
#    0.0 < B.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np

  y = ( x - a ) / b

  cdf = 2.0 * np.arctan ( np.exp ( y ) ) / np.pi

  return cdf

def sech_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## SECH_CDF_INV inverts the Hyperbolic Secant CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real X, the corresponding argument of the CDF.
#
  import numpy as np

  r8_huge = 1.0E+30

  if ( cdf <= 0.0 ):
    x = - r8_huge
  elif ( cdf < 1.0 ):
    x = a + b * np.log ( np.tan ( 0.5 * np.pi * cdf ) )
  elif ( 1.0 <= cdf ):
    x = r8_huge

  return x

def sech_cdf_test ( ):

#*****************************************************************************80
#
## SECH_CDF_TEST tests SECH_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SECH_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SECH_CDF evaluates the Sech CDF.' )
  print ( '  SECH_CDF_INV inverts the Sech CDF.' )
  print ( '  SECH_PDF evaluates the Sech PDF.' )

  a = 3.0
  b = 2.0

  check = sech_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'SECH_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  print ( '' )
  print ( '  PDF parameter A =         %14g' % ( a ) )
  print ( '  PDF parameter B =         %14g' % ( b ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = sech_sample ( a, b, seed )

    pdf = sech_pdf ( x, a, b )

    cdf = sech_cdf ( x, a, b )

    x2 = sech_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SECH_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def sech_check ( a, b ):

#*****************************************************************************80
#
## SECH_CHECK checks the parameters of the Hyperbolic Secant CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameter of the PDF.
#    0.0 < B.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'SECH_CHECK - Fatal error!' )
    print ( '  B <= 0.0' )
    check = False

  return check

def sech_mean ( a, b ):

#*****************************************************************************80
#
## SECH_MEAN returns the mean of the Hyperbolic Secant PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
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

def sech_pdf ( x, a, b ):

#*****************************************************************************80
#
## SECH_PDF evaluates the Hypebolic Secant PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = sech ( ( X - A ) / B ) / ( PI * B )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
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

  y = ( x - a ) / b

  pdf = 1.0 / np.cosh ( y ) / ( np.pi * b )

  return pdf

def sech_sample ( a, b, seed ):

#*****************************************************************************80
#
## SECH_SAMPLE samples the Hyperbolic Secant PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
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
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = a + b * np.log ( np.tan ( 0.5 * np.pi * cdf ) )

  return x, seed

def sech_sample_test ( ):

#*****************************************************************************80
#
## SECH_SAMPLE_TEST tests SECH_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
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
  print ( 'SECH_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SECH_MEAN computes the Sech mean' )
  print ( '  SECH_SAMPLE samples the Sech distribution' )
  print ( '  SECH_VARIANCE computes the Sech variance.' )

  a = 3.0
  b = 2.0

  check = sech_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'SECH_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  mean = sech_mean ( a, b )
  variance = sech_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = sech_sample ( a, b, seed )

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
  print ( 'SECH_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def sech_variance ( a, b ):

#*****************************************************************************80
#
## SECH_VARIANCE returns the variance of the Hyperbolic Secant PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
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

  variance = 0.25 * np.pi * np.pi * b * b

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  sech_cdf_test ( )
  sech_sample_test ( )
  timestamp ( )
 
