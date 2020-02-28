#! /usr/bin/env python
#
def laplace_cdf ( x, a, b ):

#*****************************************************************************80
#
## LAPLACE_CDF evaluates the Laplace CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
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
#    Output, real CDF, the value of the PDF.
#
  import numpy as np

  y = ( x - a ) / b

  if ( x <= a ):
    cdf = 0.5 * np.exp ( y )
  else:
    cdf = 1.0 - 0.5 * np.exp ( - y )

  return cdf

def laplace_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## LAPLACE_CDF_INV inverts the Laplace CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
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
    print ( 'LAPLACE_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'LAPLACE_CDF_INV - Fatal error!' )

  if ( cdf <= 0.5 ):
    x = a + b * np.log ( 2.0 * cdf )
  else:
    x = a - b * np.log ( 2.0 * ( 1.0 - cdf ) )

  return x

def laplace_cdf_test ( ):

#*****************************************************************************80
#
## LAPLACE_CDF_TEST tests LAPLACE_CDF, LAPLACE_CDF_INV, LAPLACE_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LAPLACE_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LAPLACE_CDF evaluates the Laplace CDF' )
  print ( '  LAPLACE_CDF_INV inverts the Laplace CDF.' )
  print ( '  LAPLACE_PDF evaluates the Laplace PDF' )

  a = 1.0
  b = 2.0

  check = laplace_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'LAPLACE_CDF_TEST - Fatal error!' )
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

    x, seed = laplace_sample ( a, b, seed )

    pdf = laplace_pdf ( x, a, b )

    cdf = laplace_cdf ( x, a, b )

    x2 = laplace_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LAPLACE_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def laplace_check ( a, b ):

#*****************************************************************************80
#
## LAPLACE_CHECK checks the parameters of the Laplace PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
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
    print ( 'LAPLACE_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def laplace_mean ( a, b ):

#*****************************************************************************80
#
## LAPLACE_MEAN returns the mean of the Laplace PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
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

def laplace_pdf ( x, a, b ):

#*****************************************************************************80
#
## LAPLACE_PDF evaluates the Laplace PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = exp ( - abs ( X - A ) / B ) / ( 2 * B )
#
#    The Laplace PDF is also known as the Double Exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
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

  pdf = np.exp ( - abs ( x - a ) / b ) / ( 2.0 * b )

  return pdf

def laplace_sample ( a, b, seed ):

#*****************************************************************************80
#
## LAPLACE_SAMPLE samples the Laplace PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
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

  x = laplace_cdf_inv ( cdf, a, b )

  return x, seed

def laplace_sample_test ( ):

#*****************************************************************************80
#
## LAPLACE_SAMPLE_TEST tests LAPLACE_MEAN, LAPLACE_SAMPLE, LAPLACE_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
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
  print ( 'LAPLACE_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LAPLACE_MEAN computes the Laplace mean' )
  print ( '  LAPLACE_SAMPLE samples the Laplace distribution' )
  print ( '  LAPLACE_VARIANCE computes the Laplace variance.' )

  a = 1.0
  b = 2.0

  check = laplace_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'LAPLACE_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  mean = laplace_mean ( a, b )
  variance = laplace_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = laplace_sample ( a, b, seed )

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
  print ( 'LAPLACE_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def laplace_variance ( a, b ):

#*****************************************************************************80
#
## LAPLACE_VARIANCE returns the variance of the Laplace PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
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
  variance = 2.0 * b * b

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  laplace_cdf_test ( )
  laplace_sample_test ( )
  timestamp ( )
 
