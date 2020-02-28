#! /usr/bin/env python
#
def log_series_cdf ( x, a ):

#*****************************************************************************80
#
## LOG_SERIES_CDF evaluates the Logarithmic Series CDF.
#
#  Discussion:
#
#    Simple summation is used, with a recursion to generate successive
#    values of the PDF.
#
#    Thanks to Oscar van Vlijmen.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the argument of the PDF.
#    0 < X
#
#    Input, real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np

  cdf = 0.0

  for x2 in range ( 1, x + 1 ):

    if ( x2 == 1 ):
      pdf = - a / np.log ( 1.0 - a )
    else:
      pdf = ( x2 - 1 ) * a * pdf / x2

    cdf = cdf + pdf
 
  return cdf

def log_series_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## LOG_SERIES_CDF_INV inverts the Logarithmic Series CDF.
#
#  Discussion:
#
#    Simple summation is used.  The only protection against an
#    infinite loop caused by roundoff is that X cannot be larger
#    than 1000.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#
#    Input, real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#    Output, real X, the argument of the CDF for which
#    CDF(X-1) <= CDF <= CDF(X).
#
  import numpy as np
  from sys import exit

  xmax = 1000

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'LOG_SERIES_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'LOG_SERIES_CDF_INV - Fatal error!' )

  cdf2 = 0.0
  x = 1

  while ( cdf2 < cdf and x < xmax ):

    if ( x == 1 ):
      pdf = - a / np.log ( 1.0 - a )
    else:
      pdf = ( x - 1 ) * a * pdf / x

    cdf2 = cdf2 + pdf

    x = x + 1

  return x

def log_series_cdf_test ( ):

#*****************************************************************************80
#
## LOG_SERIES_CDF_TEST tests LOG_SERIES_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'LOG_SERIES_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LOG_SERIES_CDF evaluates the Log Series CDF' )
  print ( '  LOG_SERIES_CDF_INV inverts the Log Series CDF.' )
  print ( '  LOG_SERIES_PDF evaluates the Log Series PDF' )

  a = 0.25

  check = log_series_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'LOG_SERIES_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A =  %14g' % ( a ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = log_series_sample ( a, seed )

    pdf = log_series_pdf ( x, a )

    cdf = log_series_cdf ( x, a )

    x2 = log_series_cdf_inv ( cdf, a )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'LOG_SERIES_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def log_series_check ( a ):

#*****************************************************************************80
#
## LOG_SERIES_CHECK checks the parameter of the Logarithmic Series PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 or 1.0 <= a ):
    print ( '' )
    print ( 'LOG_SERIES_CHECK - Fatal error!' )
    print ( '  A <= 0.0 or 1.0 <= A' )
    check = False

  return check

def log_series_mean ( a ):

#*****************************************************************************80
#
## LOG_SERIES_MEAN returns the mean of the Logarithmic Series PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#    Output, real MEAN, the mean of the PDF.
#
  import numpy as np

  mean = - a / ( ( 1.0 - a ) * np.log ( 1.0 - a ) )

  return mean

def log_series_pdf ( x, a ):

#*****************************************************************************80
#
## LOG_SERIES_PDF evaluates the Logarithmic Series PDF.
#
#  Discussion:
#
#    PDF(X)(A) = - A ^ X / ( X * log ( 1 - A ) )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the argument of the PDF.
#    0 < X
#
#    Input, real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  if ( x <= 0 ):
    pdf = 0.0
  else:
    pdf = - a ** x / ( x * np.log ( 1.0 - a ) )

  return pdf

def log_series_sample ( a, seed ):

#*****************************************************************************80
#
## LOG_SERIES_SAMPLE samples the Logarithmic Series PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Luc Devroye,
#    Non-Uniform Random Variate Generation,
#    Springer-Verlag, New York, 1986, page 547.
#
#  Parameters:
#
#    Input, real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  u, seed = r8_uniform_01 ( seed )
  v, seed = r8_uniform_01 ( seed )

  x = int ( 1.0 + np.log ( v ) / ( np.log ( 1.0 - ( 1.0 - a ) ** u ) ) )

  return x, seed

def log_series_sample_test ( ):

#*****************************************************************************80
#
## LOG_SERIES_SAMPLE_TEST tests LOG_SERIES_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
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
  print ( 'LOG_SERIES_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  LOG_SERIES_MEAN computes the Log Series mean' )
  print ( '  LOG_SERIES_VARIANCE computes the Log Series variance' )
  print ( '  LOG_SERIES_SAMPLE samples the Log Series distribution.' )

  a = 0.25

  check = log_series_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'LOG_SERIES_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = log_series_mean ( a )
  variance = log_series_variance ( a )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = log_series_sample ( a, seed )

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
  print ( 'LOG_SERIES_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def log_series_variance ( a ):

#*****************************************************************************80
#
## LOG_SERIES_VARIANCE returns the variance of the Logarithmic Series PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the parameter of the PDF.
#    0.0 < A < 1.0.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  import numpy as np

  alpha = - 1.0 / np.log ( 1.0 - a )

  variance = a * alpha * ( 1.0 - alpha * a ) / ( 1.0 - a ) ** 2

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  log_series_cdf_test ( )
  log_series_sample_test ( )
  timestamp ( )
 
