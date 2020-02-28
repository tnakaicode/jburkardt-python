#! /usr/bin/env python3
#
def power_cdf ( x, a, b ):

#*****************************************************************************80
#
## POWER_CDF evaluates the Power CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
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
#    0.0 < A, 0.0 < B,
#
#    Output, real CDF, the value of the CDF.
#
  if ( x <= 0.0 ):
    cdf = 0.0
  elif ( x <= b ):
    cdf = ( x / b ) ** a
  else:
    cdf = 1.0

  return cdf

def power_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## POWER_CDF_INV inverts the Power CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0.
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#    Output, real X, the argument of the CDF.
#
  import numpy as np

  if ( cdf <= 0.0 ):
    x = 0.0
  elif ( cdf < 1.0 ):
    x = b * np.exp ( np.log ( cdf ) / a )
  else:
    x = b

  return x

def power_cdf_test ( ):

#*****************************************************************************80
#
## POWER_CDF_TEST tests POWER_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'POWER_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POWER_CDF evaluates the Power CDF' )
  print ( '  POWER_CDF_INV inverts the Power CDF.' )
  print ( '  POWER_PDF evaluates the Power PDF' )

  a = 2.0
  b = 3.0

  check = power_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'POWER_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =       %14g' % ( a ) )
  print ( '  PDF parameter B =       %14g' % ( b ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = power_sample ( a, b, seed )

    pdf = power_pdf ( x, a, b )

    cdf = power_cdf ( x, a, b )

    x2 = power_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'POWER_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def power_check ( a, b ):

#*****************************************************************************80
#
## POWER_CHECK checks the parameter of the Power PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'POWER_CHECK - Fatal error!' )
    print ( '  A <= 0.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'POWER_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def power_mean ( a, b ):

#*****************************************************************************80
#
## POWER_MEAN returns the mean of the Power PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = a * b / ( a + 1.0 )

  return mean

def power_pdf ( x, a, b ):

#*****************************************************************************80
#
## POWER_PDF evaluates the Power PDF.
#
#  Formula:
#
#    PDF(X)(A) = (A/B) * (X/B)^(A-1)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Daniel Zwillinger and Stephen Kokoska,
#    CRC Standard Probability and Statistics Tables and Formulae,
#    Chapman and Hall/CRC, 2000, pages 152-153.
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    0.0 <= X <= B.
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#    Output, real PDF, the value of the PDF.
#
  if ( x < 0.0 or b < x ):
    pdf = 0.0
  else:
    pdf = ( a / b ) * ( x / b ) ** ( a - 1.0 )

  return pdf

def power_sample ( a, b, seed ):

#*****************************************************************************80
#
## POWER_SAMPLE samples the Power PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = power_cdf_inv ( cdf, a, b )

  return x, seed

def power_sample_test ( ):

#*****************************************************************************80
#
## POWER_SAMPLE_TEST tests POWER_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
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
  print ( 'POWER_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  POWER_MEAN computes the Power mean' )
  print ( '  POWER_SAMPLE samples the Power distribution' )
  print ( '  POWER_VARIANCE computes the Power variance.' )

  a = 2.0
  b = 3.0

  check = power_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'POWER_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  mean = power_mean ( a, b )
  variance = power_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = power_sample ( a, b, seed )

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
  print ( 'POWER_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def power_variance ( a, b ):

#*****************************************************************************80
#
## POWER_VARIANCE returns the variance of the Power PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A, 0.0 < B.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = b * b * a / ( ( a + 1.0 ) ** 2 * ( a + 2.0 ) )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  power_cdf_test ( )
  power_sample_test ( )
  timestamp ( )
 
