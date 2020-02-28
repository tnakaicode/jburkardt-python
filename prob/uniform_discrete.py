#! /usr/bin/env python
#
def uniform_discrete_cdf ( x, a, b ):

#*****************************************************************************80
#
## UNIFORM_DISCRETE_CDF evaluates the Uniform Discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the argument of the CDF.
#
#    Input, integer A, B, the parameters of the PDF.
#    A <= B.
#
#    Output, real CDF, the value of the CDF.
#
  if ( x < a ):
    cdf = 0.0
  elif ( b < x ):
    cdf = 1.0
  else:
    cdf = ( x + 1 - a ) / ( b + 1 - a )

  return cdf

def uniform_discrete_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## UNIFORM_DISCRETE_CDF_INV inverts the Uniform Discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
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
#    Input, integer A, B, the parameters of the PDF.
#    A <= B.
#
#    Output, integer X, the smallest argument whose CDF is greater
#    than or equal to CDF.
#
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'UNIFORM_DISCRETE_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'UNIFORM_DISCRETE_CDF_INV - Fatal error!' )

  a2 = a - 0.5
  b2 = b + 0.5
  x2 = a + cdf * ( b2 - a2 )

  x = int ( x2 )

  x = max ( x, a )
  x = min ( x, b )

  return x

def uniform_discrete_cdf_test ( ):

#*****************************************************************************80
#
## UNIFORM_DISCRETE_CDF_TEST tests UNIFORM_DISCRETE_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'UNIFORM_DISCRETE_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNIFORM_DISCRETE_CDF evaluates the Uniform Discrete CDF' )
  print ( '  UNIFORM_DISCRETE_CDF_INV inverts the Uniform Discrete CDF.' )
  print ( '  UNIFORM_DISCRETE_PDF evaluates the Uniform Discrete PDF' )

  a = 1
  b = 6

  check = uniform_discrete_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'UNIFORM_DISCRETE_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =             %6d' % ( a ) )
  print ( '  PDF parameter B =             %6d' % ( b ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = uniform_discrete_sample ( a, b, seed )

    pdf = uniform_discrete_pdf ( x, a, b )

    cdf = uniform_discrete_cdf ( x, a, b )

    x2 = uniform_discrete_cdf_inv ( cdf, a, b )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNIFORM_DISCRETE_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def uniform_discrete_check ( a, b ):

#*****************************************************************************80
#
## UNIFORM_DISCRETE_CHECK checks the parameters of the Uniform discrete CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, B, the parameters of the PDF.
#    A <= B.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( b < a ):
    print ( '' )
    print ( 'UNIFORM_DISCRETE_CHECK - Fatal error!' )
    print ( '  B < A.' )
    check = False

  return check

def uniform_discrete_mean ( a, b ):

#*****************************************************************************80
#
## UNIFORM_DISCRETE_MEAN returns the mean of the Uniform discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, B, the parameters of the PDF.
#    A <= B.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = 0.5 * ( a + b )

  return mean

def uniform_discrete_pdf ( x, a, b ):

#*****************************************************************************80
#
## UNIFORM_DISCRETE_PDF evaluates the Uniform discrete PDF.
#
#  Discussion:
#
#    The Uniform Discrete PDF is also known as the "Rectangular"
#    Discrete PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = 1 / ( B + 1 - A ) for A <= X <= B.
#
#    The parameters define the interval of integers
#    for which the PDF is nonzero.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the argument of the PDF.
#
#    Input, integer A, B, the parameters of the PDF.
#    A <= B.
#
#    Output, real PDF, the value of the PDF.
#
  if ( x < a or b < x ):
    pdf = 0.0
  else:
    pdf = 1.0 / ( b + 1 - a )

  return pdf

def uniform_discrete_sample ( a, b, seed ):

#*****************************************************************************80
#
## UNIFORM_DISCRETE_SAMPLE samples the Uniform discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, B, the parameters of the PDF.
#    A <= B.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = uniform_discrete_cdf_inv ( cdf, a, b )

  return x, seed

def uniform_discrete_sample_test ( ):

#*****************************************************************************80
#
## UNIFORM_DISCRETE_SAMPLE_TEST tests UNIFORM_DISCRETE_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4vec_max import i4vec_max
  from i4vec_mean import i4vec_mean
  from i4vec_min import i4vec_min
  from i4vec_variance import i4vec_variance

  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'UNIFORM_DISCRETE_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNIFORM_DISCRETE_MEAN computes the Uniform Discrete mean' )
  print ( '  UNIFORM_DISCRETE_SAMPLE samples the Uniform Discrete distribution' )
  print ( '  UNIFORM_DISCRETE_VARIANCE computes the Uniform Discrete variance.' )

  a = 1
  b = 6

  check = uniform_discrete_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'UNIFORM_DISCRETE_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = uniform_discrete_mean ( a, b )
  variance = uniform_discrete_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %6d' % ( a ) )
  print ( '  PDF parameter B =             %6d' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = uniform_discrete_sample ( a, b, seed )

  mean = i4vec_mean ( nsample, x )
  variance = i4vec_variance ( nsample, x )
  xmax = i4vec_max ( nsample, x )
  xmin = i4vec_min ( nsample, x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNIFORM_DISCRETE_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def uniform_discrete_variance ( a, b ):

#*****************************************************************************80
#
## UNIFORM_DISCRETE_VARIANCE returns the variance of the Uniform discrete PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, B, the parameters of the PDF.
#    A <= B.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = ( ( b + 1.0 - a ) ** 2 - 1.0 ) / 12.0

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  uniform_discrete_cdf_test ( )
  uniform_discrete_sample_test ( )
  timestamp ( )
 
