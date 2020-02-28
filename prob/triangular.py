#! /usr/bin/env python
#
def triangular_cdf ( x, a, b ):

#*****************************************************************************80
#
## TRIANGULAR_CDF evaluates the Triangular CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
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
  if ( x <= a ):
    cdf = 0.0
  elif ( x <= 0.5 * ( a + b ) ):
    cdf = 2.0 * ( x * x - 2.0 * a * x + a * a ) / ( b - a ) ** 2
  elif ( x <= b ):
    cdf = 0.5 + ( - 2.0 * x * x + 4.0 * b * x + 0.5 * a * a \
      - a * b - 1.5 * b * b ) / ( b - a ) ** 2
  else:
    cdf = 1.0

  return cdf

def triangular_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## TRIANGULAR_CDF_INV inverts the Triangular CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
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
  import numpy as np
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'TRIANGULAR_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'TRIANGULAR_CDF_INV - Fatal error!' )

  if ( cdf <= 0.5 ):
    x = a + 0.5 * ( b - a ) * np.sqrt ( 2.0 * cdf )
  else:
    x = b - 0.5 * ( b - a ) * np.sqrt ( 2.0 * ( 1.0 - cdf ) )

  return x

def triangular_cdf_test ( ):

#*****************************************************************************80
#
## TRIANGULAR_CDF_TEST tests TRIANGULAR_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'TRIANGULAR_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGULAR_CDF evaluates the Triangular CDF' )
  print ( '  TRIANGULAR_CDF_INV inverts the Triangular CDF.' )
  print ( '  TRIANGULAR_PDF evaluates the Triangular PDF' )

  a = 1.0
  b = 10.0

  check = triangular_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'TRIANGULAR_CDF_TEST - Fatal error!' )
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

    x, seed = triangular_sample ( a, b, seed )

    pdf = triangular_pdf ( x, a, b )

    cdf = triangular_cdf ( x, a, b )

    x2 = triangular_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'TRIANGULAR_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def triangular_check ( a, b ):

#*****************************************************************************80
#
## TRIANGULAR_CHECK checks the parameters of the Triangular CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
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
    print ( 'TRIANGULAR_CHECK - Fatal error!' )
    print ( '  B <= A.' )
    check = False

  return check

def triangular_mean ( a, b ):

#*****************************************************************************80
#
## TRIANGULAR_MEAN returns the mean of the Triangular PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
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
#    Output, real MEAN, the mean of the PDF.
#
  mean = 0.5 * ( a + b )

  return mean

def triangular_pdf ( x, a, b ):

#*****************************************************************************80
#
## TRIANGULAR_PDF evaluates the Triangular PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = 4 * ( X - A ) / ( B - A )^2 for  A <= X <= (A+B)/2
#                = 4 * ( B - X ) / ( B - A )^2 for  (A+B)/2 <= X <= B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
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
  if ( x <= a ):
    pdf = 0.0
  elif ( x <= 0.5 * ( a + b ) ):
    pdf = 4.0 * ( x - a ) / ( b - a ) ** 2
  elif ( x <= b ):
    pdf = 4.0 * ( b - x ) / ( b - a ) ** 2
  else:
    pdf = 0.0

  return pdf

def triangular_sample ( a, b, seed ):

#*****************************************************************************80
#
## TRIANGULAR_SAMPLE samples the Triangular PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
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

  x = triangular_cdf_inv ( cdf, a, b )

  return x, seed

def triangular_sample_test ( ):

#*****************************************************************************80
#
## TRIANGULAR_SAMPLE_TEST tests TRIANGULAR_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
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
  print ( 'TRIANGULAR_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TRIANGULAR_MEAN computes the Triangular mean' )
  print ( '  TRIANGULAR_SAMPLE samples the Triangular distribution' )
  print ( '  TRIANGULAR_VARIANCE computes the Triangular variance.' )

  a = 1.0
  b = 10.0

  check = triangular_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'TRIANGULAR_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = triangular_mean ( a, b )
  variance = triangular_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i], seed = triangular_sample ( a, b, seed )

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
  print ( 'TRIANGULAR_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def triangular_variance ( a, b ):

#*****************************************************************************80
#
## TRIANGULAR_VARIANCE returns the variance of the Triangular PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2016
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
  variance = ( b - a ) ** 2 / 24.0

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  triangular_cdf_test ( )
  triangular_sample_test ( )
  timestamp ( )
 
