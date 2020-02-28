#! /usr/bin/env python
#
def weibull_discrete_cdf ( x, a, b ):

#*****************************************************************************80
#
## WEIBULL_DISCRETE_CDF evaluates the Discrete Weibull CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the argument of the CDF.
#    0 <= X.
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 <= A <= 1.0,
#    0.0 < B.
#
#    Output, real CDF, the value of the CDF.
#
  if ( x < 0 ):
    cdf = 0.0
  else:
    cdf = 1.0 - ( 1.0 - a ) ** ( ( x + 1 ) ** b )

  return cdf

def weibull_discrete_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## WEIBULL_DISCRETE_CDF_INV inverts the Discrete Weibull CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
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
#    0.0 <= A <= 1.0,
#    0.0 < B.
#
#    Output, integer X, the corresponding argument.
#
  import numpy as np
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'WEIBULL_DISCRETE_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'WEIBULL_DISCRETE_CDF_INV - Fatal error!' )

  x = 1 + int ( ( np.log ( 1.0 - cdf ) \
    / np.log ( 1.0 - a ) ) ** ( 1.0 / b ) - 1.0 )

  return x

def weibull_discrete_cdf_test ( ):

#*****************************************************************************80
#
## WEIBULL_DISCRETE_CDF_TEST tests WEIBULL_DISCRETE_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'WEIBULL_DISCRETE_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WEIBULL_DISCRETE_CDF evaluates the Weibull Discrete CDF' )
  print ( '  WEIBULL_DISCRETE_CDF_INV inverts the Weibull Discrete CDF.' )
  print ( '  WEIBULL_DISCRETE_PDF evaluates the Weibull Discrete PDF' )

  a = 0.50
  b = 1.5

  check = weibull_discrete_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'WEIBULL_DISCRETE_CDF_TEST - Fatal error!' )
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

    x, seed = weibull_discrete_sample ( a, b, seed )

    pdf = weibull_discrete_pdf ( x, a, b )

    cdf = weibull_discrete_cdf ( x, a, b )

    x2 = weibull_discrete_cdf_inv ( cdf, a, b )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'WEIBULL_DISCRETE_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def weibull_discrete_check ( a, b ):

#*****************************************************************************80
#
## WEIBULL_DISCRETE_CHECK checks the parameters of the discrete Weibull CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 <= A <= 1.0,
#    0.0 < B.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 0.0 or 1.0 < a ):
    print ( '' )
    print ( 'WEIBULL_DISCRETE_CHECK - Fatal error!' )
    print ( '  A < 0 or 1 < A.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'WEIBULL_DISCRETE_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def weibull_discrete_pdf ( x, a, b ):

#*****************************************************************************80
#
## WEIBULL_DISCRETE_PDF evaluates the discrete Weibull PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = ( 1 - A )^X^B - ( 1 - A )^(X+1)^B.
#
#    WEIBULL_DISCRETE_PDF(X)(A,1) = GEOMETRIC_PDF(X)(A)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the argument of the PDF.
#    0 <= X
#
#    Input, real A, B, the parameters that define the PDF.
#    0 <= A <= 1,
#    0 < B.
#
#    Output, real PDF, the value of the PDF.
#
  if ( x < 0 ):
    pdf = 0.0
  else:
    pdf = ( 1.0 - a ) ** ( x ** b ) - ( 1.0 - a ) ** ( ( x + 1 ) ** b )

  return pdf

def weibull_discrete_sample ( a, b, seed ):

#*****************************************************************************80
#
## WEIBULL_DISCRETE_SAMPLE samples the discrete Weibull PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 <= A <= 1.0,
#    0.0 < B.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = weibull_discrete_cdf_inv ( cdf, a, b )

  return x, seed

def weibull_discrete_sample_test ( ):

#*****************************************************************************80
#
## WEIBULL_DISCRETE_SAMPLE_TEST tests WEIBULL_DISCRETE_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 April 2016
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
  print ( 'WEIBULL_DISCRETE_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  WEIBULL_DISCRETE_SAMPLE samples the Weibull Discrete distribution' )

  a = 0.5
  b = 1.5

  check = weibull_discrete_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'WEIBULL_DISCRETE_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =     %14g' % ( a ) )
  print ( '  PDF parameter B =     %14g' % ( b ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = weibull_discrete_sample ( a, b, seed )

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
  print ( 'WEIBULL_DISCRETE_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  weibull_discrete_cdf_test ( )
  weibull_discrete_sample_test ( )
  timestamp ( )
 
