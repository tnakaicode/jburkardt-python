#! /usr/bin/env python
#
def reciprocal_cdf ( x, a, b ):

#*****************************************************************************80
#
## RECIPROCAL_CDF evaluates the Reciprocal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
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
#    0.0 < A <= B.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= 0.0 ):

    cdf = 0.0

  elif ( 0.0 < x ):

    cdf = np.log ( a / x ) / np.log ( a / b )

  return cdf

def reciprocal_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## RECIPROCAL_CDF_INV inverts the Reciprocal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
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
#    0.0 < A <= B.
#
#    Output, real X, the corresponding argument of the CDF.
#
  if ( cdf <= 0.0 ):
    x = 0.0
  elif ( 0.0 < cdf ):
    x = b ** cdf / a ** ( cdf - 1.0 )

  return x

def reciprocal_cdf_test ( ):

#*****************************************************************************80
#
## RECIPROCAL_CDF_TEST tests RECIPROCAL_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'RECIPROCAL_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RECIPROCAL_CDF evaluates the Reciprocal CDF.' )
  print ( '  RECIPROCAL_CDF_INV inverts the Reciprocal CDF.' )
  print ( '  RECIPROCAL_PDF evaluates the Reciprocal PDF.' )

  a = 1.0
  b = 3.0

  check = reciprocal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'RECIPROCAL_CDF_TEST - Fatal error!' )
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

    x, seed = reciprocal_sample ( a, b, seed )

    pdf = reciprocal_pdf ( x, a, b )

    cdf = reciprocal_cdf ( x, a, b )

    x2 = reciprocal_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RECIPROCAL_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def reciprocal_check ( a, b ):

#*****************************************************************************80
#
## RECIPROCAL_CHECK checks the parameters of the Reciprocal CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A <= B.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'RECIPROCAL_CHECK - Fatal error!' )
    print ( '  A <= 0.0' )
    check = False

  if ( b < a ):
    print ( '' )
    print ( 'RECIPROCAL_CHECK - Fatal error!' )
    print ( '  B < A' )
    check = False

  return check

def reciprocal_mean ( a, b ):

#*****************************************************************************80
#
## RECIPROCAL_MEAN returns the mean of the Reciprocal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A <= B.
#
#    Output, real MEAN, the mean of the PDF.
#
  import numpy as np

  mean = ( a - b ) / np.log ( a / b )

  return mean

def reciprocal_pdf ( x, a, b ):

#*****************************************************************************80
#
## RECIPROCAL_PDF evaluates the Reciprocal PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = 1.0 / ( X * LOG ( B / A ) )
#    for 0.0 <= X
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
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
#    0.0 < A <= B.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= 0.0 ):
    pdf = 0.0
  elif ( 0.0 < x ):
    pdf = 1.0 / ( x * np.log ( b / a ) )

  return pdf

def reciprocal_sample ( a, b, seed ):

#*****************************************************************************80
#
## RECIPROCAL_SAMPLE samples the Reciprocal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A <= B.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = b ** cdf / a ** ( cdf - 1.0 )

  return x, seed

def reciprocal_sample_test ( ):

#*****************************************************************************80
#
## RECIPROCAL_SAMPLE_TEST tests RECIPROCAL_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
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
  print ( 'RECIPROCAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RECIPROCAL_MEAN computes the Reciprocal mean' )
  print ( '  RECIPROCAL_SAMPLE samples the Reciprocal distribution' )
  print ( '  RECIPROCAL_VARIANCE computes the Reciprocal variance.' )

  a = 1.0
  b = 3.0

  check = reciprocal_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'RECIPROCAL_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = reciprocal_mean ( a, b )
  variance = reciprocal_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =       %14g' % ( a ) )
  print ( '  PDF parameter B =       %14g' % ( b ) )
  print ( '  PDF mean =              %14g' % ( mean ) )
  print ( '  PDF variance =          %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = reciprocal_sample ( a, b, seed )

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
  print ( 'RECIPROCAL_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def reciprocal_variance ( a, b ):

#*****************************************************************************80
#
## RECIPROCAL_VARIANCE returns the variance of the Reciprocal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A <= B.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  import numpy as np

  d = np.log ( a / b )

  variance = ( a - b ) * ( a * ( d - 2.0 ) + b * ( d + 2.0 ) ) / ( 2.0 * d * d )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  reciprocal_cdf_test ( )
  reciprocal_sample_test ( )
  timestamp ( )
 
