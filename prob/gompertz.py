#! /usr/bin/env python
#
def gompertz_cdf ( x, a, b ):

#*****************************************************************************80
#
## GOMPERTZ_CDF evaluates the Gompertz CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Johnson, Kotz, and Balakrishnan,
#    Continuous Univariate Distributions, Volume 2, second edition,
#    Wiley, 1994, pages 25-26.
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Input, real A, B, the parameters of the PDF.
#    1 < A, 0 < B.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= 0.0 ):
    cdf = 0.0
  else:
    cdf = 1.0 - np.exp ( - b * ( a ** x - 1.0 ) / np.log ( a ) )

  return cdf

def gompertz_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## GOMPERTZ_CDF_INV inverts the Gompertz CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Johnson, Kotz, and Balakrishnan,
#    Continuous Univariate Distributions, Volume 2, second edition,
#    Wiley, 1994, pages 25-26.
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#
#    Input, real A, B, the parameters of the PDF.
#    1 < A, 0 < B.
#
#    Output, real X, the corresponding argument.
#
  import numpy as np

  r8_huge = 1.0E+30

  if ( cdf < 0.0 ):
    x = 0.0
  elif ( cdf < 1.0 ):
    x = np.log ( 1.0 - np.log ( 1.0 - cdf ) * np.log ( a ) / b  ) / np.log ( a )
  else:
    x = r8_huge

  return x

def gompertz_cdf_test ( ):

#*****************************************************************************80
#
## GOMPERTZ_CDF_TEST tests GOMPERTZ_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'GOMPERTZ_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GOMPERTZ_CDF evaluates the Gompertz CDF' )
  print ( '  GOMPERTZ_CDF_INV inverts the Gompertz CDF.' )
  print ( '  GOMPERTZ_PDF evaluates the Gompertz PDF' )

  a = 2.0
  b = 3.0

  check = gompertz_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'GOMPERTZ_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =       %14g' % ( a ) )
  print ( '  PDF parameter B =       %14g' % ( b ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = gompertz_sample ( a, b, seed )

    pdf = gompertz_pdf ( x, a, b )

    cdf = gompertz_cdf ( x, a, b )

    x2 = gompertz_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GOMPERTZ_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def gompertz_check ( a, b ):

#*****************************************************************************80
#
## GOMPERTZ_CHECK checks the parameters of the Gompertz PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Johnson, Kotz, and Balakrishnan,
#    Continuous Univariate Distributions, Volume 2, second edition,
#    Wiley, 1994, pages 25-26.
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    1 < A, 0 < B.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 1.0 ):
    print ( '' )
    print ( 'GOMPERTZ_CHECK - Fatal error!' )
    print ( '  A <= 1.0!' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'GOMPERTZ_CHECK - Fatal error!' )
    print ( '  B <= 0.0!' )
    check = False

  return check

def gompertz_pdf ( x, a, b ):

#*****************************************************************************80
#
## GOMPERTZ_PDF evaluates the Gompertz PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = B * A^X / exp ( B * ( A^X - 1 ) / log ( A ) )
#
#    for
#
#      0.0 <= X
#      1.0 <  A
#      0.0 <  B
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Johnson, Kotz, and Balakrishnan,
#    Continuous Univariate Distributions, Volume 2, second edition,
#    Wiley, 1994, pages 25-26.
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real A, B, the parameters of the PDF.
#    1 < A, 0 < B.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < 0.0 ):

    pdf = 0.0

  elif ( 1.0 < a ):

    pdf = np.exp ( np.log ( b ) + x * np.log ( a ) \
      - ( b / np.log ( a ) ) * ( a ** x - 1.0 ) )

  return pdf

def gompertz_sample ( a, b, seed ):

#*****************************************************************************80
#
## GOMPERTZ_SAMPLE samples the Gompertz PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    1 < A, 0 < B.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = gompertz_cdf_inv ( cdf, a, b )

  return x, seed

def gompertz_sample_test ( ):

#*****************************************************************************80
#
## GOMPERTZ_SAMPLE_TEST tests GOMPERTZ_SAMPLE
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 April 2016
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
  print ( 'GOMPERTZ_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GOMPERTZ_SAMPLE samples the Gompertz distribution' )

  a = 2.0
  b = 3.0

  check = gompertz_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'GOMPERTZ_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =       %14g' % ( a ) )
  print ( '  PDF parameter B =       %14g' % ( b ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = gompertz_sample ( a, b, seed )

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
  print ( 'GOMPERTZ_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  gompertz_cdf_test ( )
  gompertz_sample_test ( )
  timestamp ( )

