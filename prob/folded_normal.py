#! /usr/bin/env python
#
def folded_normal_cdf ( x, a, b ):

#*****************************************************************************80
#
## FOLDED_NORMAL_CDF evaluates the Folded Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#    0.0 <= X.
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 <= A,
#    0.0 < B.
#
#    Output, real CDF, the value of the CDF.
#
  from normal_01 import normal_01_cdf

  if ( x < 0.0 ):
    cdf = 0.0
  else:
    x1 = ( x - a ) / b
    cdf1 = normal_01_cdf ( x1 )
    x2 = ( - x - a ) / b
    cdf2 = normal_01_cdf ( x2 )
    cdf = cdf1 - cdf2

  return cdf

def folded_normal_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## FOLDED_NORMAL_CDF_INV inverts the Folded Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
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
#    0.0 <= A,
#    0.0 < B.
#
#    Output, real X, the argument of the CDF.
#    0.0 <= X.
#
  from normal import normal_cdf_inv
  from sys import exit

  it_max = 100
  tol = 0.0001
  r8_huge = 1.0E+30

  if ( cdf <= 0.0 ):
    x = 0.0
    return x
  elif ( 1.0 <= cdf ):
    x = r8_huge
    return x
#
#  Find X1, for which the value of CDF will be too small.
#
  if ( 0.0 <= a ):
    x1 = normal_cdf_inv ( cdf, a, b )
  else:
    x1 = normal_cdf_inv ( cdf, -a, b )

  x1 = max ( x1, 0.0 )
  cdf1 = folded_normal_cdf ( x1, a, b )
#
#  Find X2, for which the value of CDF will be too big.
#
  cdf2 = ( 1.0 - cdf ) / 2.0

  xa = normal_cdf_inv ( cdf2, a, b )
  xb = normal_cdf_inv ( cdf2, -a, b )
  x2 = max ( abs ( xa ), abs ( xb ) )
  cdf2 = folded_normal_cdf ( x2, a, b )
#
#  Now use bisection.
#
  it = 0

  while ( True ):

    it = it + 1

    x3 = 0.5 * ( x1 + x2 )
    cdf3 = folded_normal_cdf ( x3, a, b )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      break

    if ( it_max < it ):
      print ( '' )
      print ( 'FOLDED_NORMAL_CDF_INV - Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      exit ( 'FOLDED_NORMAL_CDF_INV - Fatal error!' )

    if ( ( cdf3 < cdf and cdf1 < cdf ) or ( cdf < cdf3 and cdf < cdf1 ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def folded_normal_cdf_test ( ):

#*****************************************************************************80
#
## FOLDED_NORMAL_CDF_TEST tests FOLDED_NORMAL_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'FOLDED_NORMAL_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FOLDED_NORMAL_CDF evaluates the Folded Normal CDF.' )
  print ( '  FOLDED_NORMAL_CDF_INV inverts the Folded Normal CDF.' )
  print ( '  FOLDED_NORMAL_PDF evaluates the Folded Normal PDF.' )

  a = 2.0
  b = 3.0

  check = folded_normal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'FOLDED_NORMAL_CDF_TEST - Fatal error!' )
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

    x, seed = folded_normal_sample ( a, b, seed )

    pdf = folded_normal_pdf ( x, a, b )

    cdf = folded_normal_cdf ( x, a, b )

    x2 = folded_normal_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FOLDED_NORMAL_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def folded_normal_check ( a, b ):

#*****************************************************************************80
#
## FOLDED_NORMAL_CHECK checks the parameters of the Folded Normal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 <= A,
#    0.0 < B.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 0.0 ):
    print ( '' )
    print ( 'FOLDED_NORMAL_CHECK - Fatal error!' )
    print ( '  A < 0.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'FOLDED_NORMAL_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def folded_normal_mean ( a, b ):

#*****************************************************************************80
#
## FOLDED_NORMAL_MEAN returns the mean of the Folded Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 <= A,
#    0.0 < B.
#
#    Output, real MEAN, the mean of the PDF.
#
  import numpy as np
  from normal_01 import normal_01_cdf

  a2 = a / b

  cdf = normal_01_cdf ( a2 )

  mean = b * np.sqrt ( 2.0 / np.pi ) * np.exp ( - 0.5 * a2 * a2 ) \
    - a * ( 1.0 - 2.0 * cdf )

  return mean

def folded_normal_pdf ( x, a, b ):

#*****************************************************************************80
#
## FOLDED_NORMAL_PDF evaluates the Folded Normal PDF.
#
#  Discussion:
#
#    PDF(X)(A) = SQRT ( 2 / PI ) * ( 1 / B ) * COSH ( A * X / B^2 )
#      * EXP ( - 0.5 * ( X^2 + A^2 ) / B^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    0.0 <= X
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 <= A,
#    0.0 < B.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < 0.0 ):
    pdf = 0.0
  else:
    pdf = np.sqrt ( 2.0 / np.pi ) * ( 1.0 / b ) * np.cosh ( a * x / ( b * b ) ) \
      * np.exp ( - 0.5 * ( x * x + a * a ) / ( b * b ) )

  return pdf

def folded_normal_sample ( a, b, seed ):

#*****************************************************************************80
#
## FOLDED_NORMAL_SAMPLE samples the Folded Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 <= A,
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

  x = folded_normal_cdf_inv ( cdf, a, b )

  return x, seed

def folded_normal_sample_test ( ):

#*****************************************************************************80
#
## FOLDED_NORMAL_SAMPLE_TEST tests FOLDED_NORMAL_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
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
  print ( 'FOLDED_NORMAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FOLDED_NORMAL_MEAN computes the Folded Normal mean' )
  print ( '  FOLDED_NORMAL_SAMPLE samples the Folded Normal distribution' )
  print ( '  FOLDED_NORMAL_VARIANCE computes the Folded Normal variance.' )

  a = 2.0
  b = 3.0

  check = folded_normal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'FOLDED_NORMAL_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = folded_normal_mean ( a, b )
  variance = folded_normal_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = folded_normal_sample ( a, b, seed )

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
  print ( 'FOLDED_NORMAL_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def folded_normal_variance ( a, b ):

#*****************************************************************************80
#
## FOLDED_NORMAL_VARIANCE returns the variance of the Folded Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 <= A,
#    0.0 < B.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  mean = folded_normal_mean ( a, b )

  variance = a * a + b * b - mean * mean

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  folded_normal_cdf_test ( )
  folded_normal_sample_test ( )
  timestamp ( )
