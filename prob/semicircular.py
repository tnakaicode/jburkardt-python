#! /usr/bin/env python
#
def semicircular_cdf ( x, a, b ):

#*****************************************************************************80
#
## SEMICIRCULAR_CDF evaluates the Semicircular CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2016
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

  if ( x <= a - b ):

    cdf = 0.0

  elif ( x <= a + b ):

    y = ( x - a ) / b

    cdf = 0.5 + ( y * np.sqrt ( 1.0 - y * y ) + np.arcsin ( y ) ) / np.pi

  elif ( a + b < x ):

    cdf = 1.0

  return cdf

def semicircular_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## SEMICIRCULAR_CDF_INV inverts the Semicircular CDF.
#
#  Discussion:
#
#    A simple bisection method is used on the interval [ A - B, A + B ].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2016
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
  from sys import exit

  it_max = 100
  tol = 0.0001

  if ( cdf <= 0.0 ):
    x = a - b
    return x
  elif ( 1.0 <= cdf ):
    x = a + b
    return x

  x1 = a - b
  cdf1 = 0.0

  x2 = a + b
  cdf2 = 1.0
#
#  Now use bisection.
#
  it = 0

  while ( True ):

    it = it + 1

    x3 = 0.5 * ( x1 + x2 )
    cdf3 = semicircular_cdf ( x3, a, b )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      break

    if ( it_max < it ):
      print ( '' )
      print ( 'SEMICIRCULAR_CDF_INV - Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      exit ( 'SEMICIRCULAR_CDF_INV - Fatal error!' )

    if ( ( cdf <= cdf3 and cdf <= cdf1 ) or ( cdf3 <= cdf and cdf1 <= cdf ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def semicircular_cdf_test ( ):

#*****************************************************************************80
#
## SEMICIRCULAR_CDF_TEST tests SEMICIRCULAR_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SEMICIRCULAR_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SEMICIRCULAR_CDF evaluates the Semicircular CDF.' )
  print ( '  SEMICIRCULAR_CDF_INV inverts the Semicircular CDF.' )
  print ( '  SEMICIRCULAR_PDF evaluates the Semicircular PDF.' )

  a = 3.0
  b = 2.0

  check = semicircular_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'SEMICIRCULAR_CDF_TEST - Fatal error!' )
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

    x, seed = semicircular_sample ( a, b, seed )

    pdf = semicircular_pdf ( x, a, b )

    cdf = semicircular_cdf ( x, a, b )

    x2 = semicircular_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SEMICIRCULAR_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def semicircular_check ( a, b ):

#*****************************************************************************80
#
## SEMICIRCULAR_CHECK checks the parameters of the Semicircular CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameter of the PDF.
#    0.0 < B.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'SEMICIRCULAR_CHECK - Fatal error!' )
    print ( '  B <= 0.0' )
    check = False

  return check

def semicircular_mean ( a, b ):

#*****************************************************************************80
#
## SEMICIRCULAR_MEAN returns the mean of the Semicircular PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2016
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

def semicircular_pdf ( x, a, b ):

#*****************************************************************************80
#
## SEMICIRCULAR_PDF evaluates the Semicircular PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = ( 2 / ( B * PI ) ) * SQRT ( 1 - ( ( X - A ) / B )^2 )
#    for A - B <= X <= A + B
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2016
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

  if ( x < a - b ):

    pdf = 0.0

  elif ( x <= a + b ):

    y = ( x - a ) / b

    pdf = 2.0 / ( b * np.pi ) * np.sqrt ( 1.0 - y * y )

  elif ( a + b < x ):

    pdf = 0.0

  return pdf

def semicircular_sample ( a, b, seed ):

#*****************************************************************************80
#
## SEMICIRCULAR_SAMPLE samples the Semicircular PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2016
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
#    Output, integer SEED, a seed for the random number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  radius, seed = r8_uniform_01 ( seed )
  radius = b * np.sqrt ( radius )
  angle, seed = r8_uniform_01 ( seed )
  x = a + radius * np.cos ( np.pi * angle )

  return x, seed

def semicircular_sample_test ( ):

#*****************************************************************************80
#
## SEMICIRCULAR_SAMPLE_TEST tests SEMICIRCULAR_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2016
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
  print ( 'SEMICIRCULAR_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SEMICIRCULAR_MEAN computes the Semicircular mean' )
  print ( '  SEMICIRCULAR_SAMPLE samples the Semicircular distribution' )
  print ( '  SEMICIRCULAR_VARIANCE computes the Semicircular variance.' )

  a = 3.0
  b = 2.0

  check = semicircular_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'SEMICIRCULAR_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = semicircular_mean ( a, b )
  variance = semicircular_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = semicircular_sample ( a, b, seed )

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
  print ( 'SEMICIRCULAR_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def semicircular_variance ( a, b ):

#*****************************************************************************80
#
## SEMICIRCULAR_VARIANCE returns the variance of the Semicircular PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 March 2016
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
  variance = b * b / 4.0

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  semicircular_cdf_test ( )
  semicircular_sample_test ( )
  timestamp ( )
