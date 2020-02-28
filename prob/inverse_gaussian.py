#! /usr/bin/env python
#
def inverse_gaussian_cdf ( x, a, b ):

#*****************************************************************************80
#
## INVERSE_GAUSSIAN_CDF evaluates the Inverse Gaussian CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#    0.0 < X.
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np
  from normal_01 import normal_01_cdf

  if ( x <= 0.0 ):

    cdf = 0.0

  else:

    x1 = np.sqrt ( b / x ) * ( x - a ) / a
    cdf1 = normal_01_cdf ( x1 )

    x2 = - np.sqrt ( b / x ) * ( x + a ) / a
    cdf2 = normal_01_cdf ( x2 )

    cdf = cdf1 + np.exp ( 2.0 * b / a ) * cdf2

  return cdf

def inverse_gaussian_cdf_test ( ):

#*****************************************************************************80
#
## INVERSE_GAUSSIAN_CDF_TEST tests INVERSE_GAUSSIAN_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'INVERSE_GAUSSIAN_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  INVERSE_GAUSSIAN_CDF evaluates the Inverse Gaussian CDF.' )
  print ( '  INVERSE_GAUSSIAN_PDF evaluates the Inverse Gaussian PDF.' )

  a = 5.0
  b = 2.0

  if ( not inverse_gaussian_check ( a, b ) ):
    print ( '' )
    print ( 'INVERSE_GAUSSIAN_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = inverse_gaussian_sample ( a, b, seed )

    pdf = inverse_gaussian_pdf ( x, a, b )

    cdf = inverse_gaussian_cdf ( x, a, b )

    print ( ' %14g  %14g  %14g' % ( x, pdf, cdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'INVERSE_GAUSSIAN_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def inverse_gaussian_check ( a, b ):

#*****************************************************************************80
#
## INVERSE_GAUSSIAN_CHECK checks the parameters of the Inverse Gaussian CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'INVERSE_GAUSSIAN_CHECK - Fatal error!' )
    print ( '  A <= 0.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'INVERSE_GAUSSIAN_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def inverse_gaussian_mean ( a, b ):

#*****************************************************************************80
#
## INVERSE_GAUSSIAN_MEAN returns the mean of the Inverse Gaussian PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def inverse_gaussian_pdf ( x, a, b ):

#*****************************************************************************80
#
## INVERSE_GAUSSIAN_PDF evaluates the Inverse Gaussian PDF.
#
#  Discussion:
#
#    The Inverse Gaussian PDF is also known as the Wald PDF
#    and the Inverse Normal PDF.
#
#    PDF(X)(A,B)
#      = SQRT ( B / ( 2 * PI * X^3 ) )
#        * EXP ( - B * ( X - A )^2 / ( 2.0 * A^2 * X ) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    0.0 < X
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= 0.0 ):
    pdf = 0.0
  else:
    pdf = np.sqrt ( b / ( 2.0 * np.pi * x ** 3 ) ) * \
      np.exp ( - b * ( x - a ) ** 2 / ( 2.0 * a ** 2 * x ) )

  return pdf

def inverse_gaussian_sample ( a, b, seed ):

#*****************************************************************************80
#
## INVERSE_GAUSSIAN_SAMPLE samples the Inverse Gaussian PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from normal_01 import normal_01_sample
  from r8_uniform_01 import r8_uniform_01

  phi = b / a
  z, seed = normal_01_sample ( seed )
  y = z * z

  t = 1.0 + 0.5 * ( y - np.sqrt ( 4.0 * phi * y + y * y ) ) / phi
  u, seed = r8_uniform_01 ( seed )

  if ( u * ( 1.0 + t ) <= 1.0 ):
    x = a * t
  else:
    x = a / t

  return x, seed

def inverse_gaussian_sample_test ( ):

#*****************************************************************************80
#
## INVERSE_GAUSSIAN_SAMPLE_TEST tests INVERSE_GAUSSIAN_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2016
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
  print ( 'INVERSE_GAUSSIAN_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  INVERSE_GAUSSIAN_MEAN computes the Inverse Gaussian mean' )
  print ( '  INVERSE_GAUSSIAN_SAMPLE samples the Inverse Gaussian distribution' )
  print ( '  INVERSE_GAUSSIAN_VARIANCE computes the Inverse Gaussian variance.' )

  a = 2.0
  b = 3.0

  check = inverse_gaussian_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'INVERSE_GAUSSIAN_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = inverse_gaussian_mean ( a, b )
  variance = inverse_gaussian_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = inverse_gaussian_sample ( a, b, seed )

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
  print ( 'INVERSE_GAUSSIAN_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def inverse_gaussian_variance ( a, b ):

#*****************************************************************************80
#
## INVERSE_GAUSSIAN_VARIANCE returns the variance of the Inverse Gaussian PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = a ** 3 / b

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  inverse_gaussian_cdf_test ( )
  inverse_gaussian_sample_test ( )
  timestamp ( )
 
