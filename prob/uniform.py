#! /usr/bin/env python
#
def uniform_cdf ( x, a, b ):

#*****************************************************************************80
#
## UNIFORM_CDF evaluates the Uniform CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
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
#    A < B.
#
#    Output, real CDF, the value of the CDF.
#
  if ( x < a ):
    cdf = 0.0
  elif ( b < x ):
    cdf = 1.0
  else:
    cdf = ( x - a ) / ( b - a )

  return cdf

def uniform_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## UNIFORM_CDF_INV inverts the Uniform CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
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
#    A < B.
#
#    Output, real X, the corresponding argument.
#
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'UNIFORM_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'UNIFORM_CDF_INV - Fatal error!' )

  x = a + ( b - a ) * cdf

  return x

def uniform_cdf_test ( ):

#*****************************************************************************80
#
## UNIFORM_CDF_TEST tests UNIFORM_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'UNIFORM_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNIFORM_CDF evaluates the Uniform CDF' )
  print ( '  UNIFORM_CDF_INV inverts the Uniform CDF.' )
  print ( '  UNIFORM_PDF evaluates the Uniform PDF' )

  a = 1.0
  b = 10.0

  check = uniform_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'UNIFORM_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =      %14g' % ( a ) )
  print ( '  PDF parameter B =      %14g' % ( b ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = uniform_sample ( a, b, seed )

    pdf = uniform_pdf ( x, a, b )

    cdf = uniform_cdf ( x, a, b )

    x2 = uniform_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNIFORM_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def uniform_check ( a, b ):

#*****************************************************************************80
#
## UNIFORM_CHECK checks the parameters of the Uniform CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    A < B.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= a ):
    print ( '' )
    print ( 'UNIFORM_CHECK - Fatal error!' )
    print ( '  B <= A.' )
    check = False

  return check

def uniform_mean ( a, b ):

#*****************************************************************************80
#
## UNIFORM_MEAN returns the mean of the Uniform PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    A < B.
#
#    Output, real MEAN, the mean of the discrete uniform PDF.
#
  mean = 0.5 * ( a + b )

  return mean

def uniform_pdf ( x, a, b ):

#*****************************************************************************80
#
## UNIFORM_PDF evaluates the Uniform PDF.
#
#  Discussion:
#
#    The Uniform PDF is also known as the "Rectangular" or "de Moivre" PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = 1 / ( B - A ) for A <= X <= B
#               = 0 otherwise
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
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
#    A < B.
#
#    Output, real PDF, the value of the PDF.
#
  if ( x < a or b < x ):
    pdf = 0.0
  else:
    pdf = 1.0 / ( b - a )

  return pdf

def uniform_sample ( a, b, seed ):

#*****************************************************************************80
#
## UNIFORM_SAMPLE samples the Uniform PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    A < B.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = uniform_cdf_inv ( cdf, a, b )

  return x, seed

def uniform_sample_test ( ):

#*****************************************************************************80
#
## UNIFORM_SAMPLE_TEST tests UNIFORM_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
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
  print ( 'UNIFORM_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNIFORM_MEAN computes the Uniform mean' )
  print ( '  UNIFORM_SAMPLE samples the Uniform distribution' )
  print ( '  UNIFORM_VARIANCE computes the Uniform variance.' )

  a = 1.0
  b = 10.0

  check = uniform_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'UNIFORM_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = uniform_mean ( a, b )
  variance = uniform_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =     %14g' % ( a ) )
  print ( '  PDF parameter B =     %14g' % ( b ) )
  print ( '  PDF mean =            %14g' % ( mean ) )
  print ( '  PDF variance =        %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = uniform_sample ( a, b, seed )

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
  print ( 'UNIFORM_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def uniform_variance ( a, b ):

#*****************************************************************************80
#
## UNIFORM_VARIANCE returns the variance of the Uniform PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    A < B.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = ( b - a ) ** 2 / 12.0

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  uniform_cdf_test ( )
  uniform_sample_test ( )
  timestamp ( )
 
