#! /usr/bin/env python
#
def extreme_values_cdf ( x, a, b ):

#*****************************************************************************80
#
## EXTREME_VALUES_CDF evaluates the Extreme Values CDF.
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
#    Input, real X, the argument of the CDF.
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np

  y = ( x - a ) / b

  cdf = np.exp ( - np.exp ( - y ) )

  return cdf

def extreme_values_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## EXTREME_VALUES_CDF_INV inverts the Extreme Values CDF.
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
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real X, the corresponding argument of the CDF.
#
  import numpy as np

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'EXTREME_VALUES_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'EXTREME_VALUES_CDF_INV - Fatal error!' )

  x = a - b * np.log ( - np.log ( cdf ) )

  return x

def extreme_values_cdf_test ( ):

#*****************************************************************************80
#
## EXTREME_VALUES_CDF_TEST tests EXTREME_VALUES_CDF.
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

  print ( '' )
  print ( 'EXTREME_VALUES_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EXTREME_VALUES_CDF evaluates the Extreme Values CDF' )
  print ( '  EXTREME_VALUES_CDF_INV inverts the Extreme Values CDF.' )
  print ( '  EXTREME_VALUES_PDF evaluates the Extreme Values PDF' )

  a = 2.0
  b = 3.0

  check = extreme_values_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'EXTREME_VALUES_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = extreme_values_sample ( a, b, seed )

    pdf = extreme_values_pdf ( x, a, b )

    cdf = extreme_values_cdf ( x, a, b )

    x2 = extreme_values_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'EXTREME_VALUES_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def extreme_values_check ( a, b ):

#*****************************************************************************80
#
## EXTREME_VALUES_CHECK checks the parameters of the Extreme Values CDF.
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
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'EXTREME_VALUES_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def extreme_values_mean ( a, b ):

#*****************************************************************************80
#
## EXTREME_VALUES_MEAN returns the mean of the Extreme Values PDF.
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
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real MEAN, the mean of the PDF.
#
  euler_constant = 0.5772156649015328

  mean = a + b * euler_constant

  return mean

def extreme_values_pdf ( x, a, b ):

#*****************************************************************************80
#
## EXTREME_VALUES_PDF evaluates the Extreme Values PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) =
#      ( 1 / B ) *
#      EXP (
#        ( A - X ) / B - EXP ( ( A - X ) / B  )
#      ).
#
#    The Extreme Values PDF is also known as the Fisher-Tippet PDF
#    and the Log-Weibull PDF.
#
#    The special case A = 0 and B = 1 is the Gumbel PDF.
#
#    The Extreme Values PDF is the limiting distribution for the
#    smallest or largest value in a large sample drawn from
#    any of a great variety of distributions.
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
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  pdf = ( 1.0 / b ) * np.exp ( ( a - x ) / b - np.exp ( ( a - x ) / b ) )

  return pdf

def extreme_values_sample ( a, b, seed ):

#*****************************************************************************80
#
## EXTREME_VALUES_SAMPLE samples the Extreme Values PDF.
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

  x = extreme_values_cdf_inv ( cdf, a, b )

  return x, seed

def extreme_values_sample_test ( ):

#*****************************************************************************80
#
## EXTREME_VALUES_SAMPLE_TEST tests EXTREME_VALUES_SAMPLE.
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
  print ( 'EXTREME_VALUES_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EXTREME_VALUES_MEAN computes the Extreme Values mean' )
  print ( '  EXTREME_VALUES_SAMPLE samples the Extreme Values distribution' )
  print ( '  EXTREME_VALUES_VARIANCE computes the Extreme Values variance.' )

  a = 2.0
  b = 3.0

  check = extreme_values_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'EXTREME_VALUES_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = extreme_values_mean ( a, b )
  variance = extreme_values_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = extreme_values_sample ( a, b, seed )

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
  print ( 'EXTREME_VALUES_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def extreme_values_variance ( a, b ):

#*****************************************************************************80
#
## EXTREME_VALUES_VARIANCE returns the variance of the Extreme Values PDF.
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
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  import numpy as np

  variance = np.pi * np.pi * b * b / 6.0

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  extreme_values_cdf_test ( )
  extreme_values_sample_test ( )
  timestamp ( )

