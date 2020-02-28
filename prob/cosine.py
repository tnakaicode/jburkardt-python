#! /usr/bin/env python
#
def cosine_cdf ( x, a, b ):

#*****************************************************************************80
#
## COSINE_CDF evaluates the Cosine CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real A, B, the parameter of the PDF.
#    0.0 < B.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= a - np.pi * b ):

    cdf = 0.0

  elif ( x <= a + np.pi * b ):

    y = ( x - a ) / b

    cdf = 0.5 + ( y + np.sin ( y ) ) / ( 2.0 * np.pi )

  elif ( a + np.pi * b < x ):

    cdf = 1.0

  return cdf

def cosine_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## COSINE_CDF_INV inverts the Cosine CDF.
#
#  Discussion:
#
#    A simple bisection method is used on the interval
#    [ A - PI * B, A + PI * B ].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
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
#    0.0 < B.
#
#    Output, real X, the corresponding argument of the CDF.
#
  import numpy as np

  it_max = 100
  tol = 0.0001

  if ( cdf <= 0.0 ):
    x = a - np.pi * b
    return x
  elif ( 1.0 <= cdf ):
    x = a + np.pi * b
    return x

  x1 = a - np.pi * b
  cdf1 = 0.0

  x2 = a + np.pi * b
  cdf2 = 1.0
#
#  Now use bisection.
#
  it = 0

  for it in range ( 0, it_max ):

    x3 = 0.5 * ( x1 + x2 )
    cdf3 = cosine_cdf ( x3, a, b )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      return x

    if ( ( cdf3 < cdf and cdf1 < cdf ) or ( cdf < cdf3 and cdf < cdf1 ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  print ( '' )
  print ( 'COSINE_CDF_INV - Warning!' )
  print ( '  Iteration limit exceeded.' )

  return x

def cosine_cdf_test ( ):

#*****************************************************************************80
#
## COSINE_CDF_TEST tests COSINE_CDF, COSINE_CDF_INV, COSINE_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'COSINE_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  COSINE_CDF evaluates the Cosine CDF.' )
  print ( '  COSINE_CDF_INV inverts the Cosine CDF.' )
  print ( '  COSINE_PDF evaluates the Cosine PDF.' )

  a = 2.0
  b = 1.0

  check = cosine_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'COSINE_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %g' % ( a ) )
  print ( '  PDF parameter B = %g' % ( b ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = cosine_sample ( a, b, seed )

    pdf = cosine_pdf ( x, a, b )

    cdf = cosine_cdf ( x, a, b )

    x2 = cosine_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'COSINE_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def cosine_check ( a, b ):

#*****************************************************************************80
#
## COSINE_CHECK checks the parameters of the Cosine CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
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
    print ( 'COSINE_CHECK - Fatal error!' )
    print ( '  B <= 0.0' )
    check = False

  return check

def cosine_mean ( a, b ):

#*****************************************************************************80
#
## COSINE_MEAN returns the mean of the Cosine PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
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
  mean = a

  return mean

def cosine_pdf ( x, a, b ):

#*****************************************************************************80
#
## COSINE_PDF evaluates the Cosine PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = ( 1 / ( 2 * PI * B ) ) * COS ( ( X - A ) / B )
#    for A - PI * B <= X <= A + PI * B
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
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
#    0.0 < B.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < a - np.pi * b ):

    pdf = 0.0

  elif ( x <= a + np.pi * b ):

    y = ( x - a ) / b

    pdf = 1.0 / ( 2.0 * np.pi * b ) * np.cos ( y )

  elif ( a + np.pi * b < x ):

    pdf = 0.0

  return pdf

def cosine_sample ( a, b, seed ):

#*****************************************************************************80
#
## COSINE_SAMPLE samples the Cosine PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
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

  x = cosine_cdf_inv ( cdf, a, b )

  return x, seed

def cosine_sample_test ( ):

#*****************************************************************************80
#
## COSINE_SAMPLE_TEST tests COSINE_MEAN, COSINE_SAMPLE, COSINE_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
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
  print ( 'COSINE_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  COSINE_MEAN computes the Cosine mean' )
  print ( '  COSINE_SAMPLE samples the Cosine distribution' )
  print ( '  COSINE_VARIANCE computes the Cosine variance.' )

  a = 2.0
  b = 1.0

  check = cosine_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'COSINE_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = cosine_mean ( a, b )
  variance = cosine_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A = %g' % ( a ) )
  print ( '  PDF parameter B = %g' % ( b ) )
  print ( '  PDF mean =        %g' % ( mean ) )
  print ( '  PDF variance =    %g' % ( variance ) )
  
  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i], seed = cosine_sample ( a, b, seed )

  mean = r8vec_mean ( nsample, x )
  variance = r8vec_variance ( nsample, x )
  xmax = r8vec_max ( nsample, x )
  xmin = r8vec_min ( nsample, x )

  print ( '' )
  print ( '  Sample size =     %6d'% ( nsample ) )
  print ( '  Sample mean =     %g' % ( mean ) )
  print ( '  Sample variance = %g' % ( variance ) )
  print ( '  Sample maximum =  %g' % ( xmax ) )
  print ( '  Sample minimum =  %g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'COSINE_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def cosine_variance ( a, b ):

#*****************************************************************************80
#
## COSINE_VARIANCE returns the variance of the Cosine PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 March 2016
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

  variance = ( np.pi * np.pi / 3.0 - 2.0 ) * b * b

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  cosine_cdf_test ( )
  cosine_sample_test ( )
  timestamp ( )

