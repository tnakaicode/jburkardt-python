#! /usr/bin/env python3
#
def pareto_cdf ( x, a, b ):

#*****************************************************************************80
#
## PARETO_CDF evaluates the Pareto CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
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
#    0.0 < A,
#    0.0 < B.
#
#    Output, real CDF, the value of the CDF.
#
  if ( x < a ):
    cdf = 0.0
  else:
    cdf = 1.0 - ( a / x ) ** b

  return cdf

def pareto_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## PARETO_CDF_INV inverts the Pareto CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
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
#    0.0 < A,
#    0.0 < B.
#
#    Output, real X, the corresponding argument.
#
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'PARETO_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'PARETO_CDF_INV - Fatal error!' )

  x = a / ( 1.0 - cdf ) ** ( 1.0 / b )

  return x

def pareto_cdf_test ( ):

#*****************************************************************************80
#
## PARETO_CDF_TEST tests PARETO_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PARETO_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PARETO_CDF evaluates the Pareto CDF' )
  print ( '  PARETO_CDF_INV inverts the Pareto CDF.' )
  print ( '  PARETO_PDF evaluates the Pareto PDF' )

  a = 0.5
  b = 5.0

  check = pareto_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'PARETO_CDF_TEST - Fatal error!' )
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

    x, seed = pareto_sample ( a, b, seed )

    pdf = pareto_pdf ( x, a, b )

    cdf = pareto_cdf ( x, a, b )

    x2 = pareto_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PARETO_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def pareto_check ( a, b ):

#*****************************************************************************80
#
## PARETO_CHECK checks the parameters of the Pareto CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
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
    print ( 'PARETO_CHECK - Fatal error!' )
    print ( '  A <= 0.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'PARETO_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def pareto_mean ( a, b ):

#*****************************************************************************80
#
## PARETO_MEAN returns the mean of the Pareto PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
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
  if ( b <= 1.0 ):

    print ( '' )
    print ( 'PARETO_MEAN - Fatal error!' )
    print ( '  For B <= 1, the mean does not exist.' )

    mean = 0.0

  else:

    mean = b * a / ( b - 1.0 )

  return mean

def pareto_pdf ( x, a, b ):

#*****************************************************************************80
#
## PARETO_PDF evaluates the Pareto PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = B * A^B / X^(B+1).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    A <= X
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A.
#    0.0 < B.
#
#    Output, real PDF, the value of the PDF.
#
  if ( x < a ):
    pdf = 0.0
  else:
    pdf = b * a ** b / x ** ( b + 1.0 )

  return pdf

def pareto_sample ( a, b, seed ):

#*****************************************************************************80
#
## PARETO_SAMPLE samples the Pareto PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A.
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

  x = pareto_cdf_inv ( cdf, a, b )

  return x, seed

def pareto_sample_test ( ):

#*****************************************************************************80
#
## PARETO_SAMPLE_TEST tests PARETO_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
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
  print ( 'PARETO_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PARETO_MEAN computes the Pareto mean' )
  print ( '  PARETO_SAMPLE samples the Pareto distribution' )
  print ( '  PARETO_VARIANCE computes the Pareto variance.' )

  a = 0.5
  b = 5.0

  check = pareto_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'PARETO_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = pareto_mean ( a, b )
  variance = pareto_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = pareto_sample ( a, b, seed )

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
  print ( 'PARETO_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def pareto_variance ( a, b ):

#*****************************************************************************80
#
## PARETO_VARIANCE returns the variance of the Pareto PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
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
  if ( b <= 2.0 ):

    print ( '' )
    print ( 'PARETO_VARIANCE - Warning!' )
    print ( '  For B <= 2, the variance does not exist.' )
    variance = 0.0

  else:

    variance = a * a * b / ( ( b - 1.0 ) ** 2 * ( b - 2.0 ) )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  pareto_cdf_test ( )
  pareto_sample_test ( )
  timestamp ( )
 
