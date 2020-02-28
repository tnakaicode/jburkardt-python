#! /usr/bin/env python
#
def geometric_cdf ( x, a ):

#*****************************************************************************80
#
## GEOMETRIC_CDF evaluates the Geometric CDF.
#
#  Discussion:
#
#    CDF(X,P) is the probability that there will be at least one
#    successful trial in the first X Bernoulli trials, given that
#    the probability of success in a single trial is P.
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
#    Input, integer X, the maximum number of trials.
#
#    Input, real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#    Output, real CDF, the value of the CDF.
#
  if ( x <= 0 ):
    cdf = 0.0
  elif ( a == 0.0 ):
    cdf = 0.0
  elif ( a == 1.0 ):
    cdf = 1.0
  else:
    cdf = 1.0 - ( 1.0 - a ) ** x

  return cdf

def geometric_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## GEOMETRIC_CDF_INV inverts the Geometric CDF.
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
#    0.0 <= CDF <= 1.0
#
#    Input, real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#    Output, integer X, the corresponding value of X.
#
  import numpy as np
  from sys import exit

  r8_huge = 1.0E+30

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'GEOMETRIC_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'GEOMETRIC_CDF_INV - Fatal error!' )

  if ( a == 1.0 ):
    x = 1
  elif ( a == 0.0 ):
    x = r8_huge
  else:
    x = 1 + ( np.log ( 1.0 - cdf ) // np.log ( 1.0 - a ) )

  return x

def geometric_cdf_test ( ):

#*****************************************************************************80
#
## GEOMETRIC_CDF_TEST tests GEOMETRIC_CDF.
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
  print ( 'GEOMETRIC_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GEOMETRIC_CDF evaluates the Geometric CDF' )
  print ( '  GEOMETRIC_CDF_INV inverts the Geometric CDF.' )
  print ( '  GEOMETRIC_PDF evaluates the Geometric PDF' )

  a = 0.25

  check = geometric_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'GEOMETRIC_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = geometric_sample ( a, seed )

    pdf = geometric_pdf ( x, a )

    cdf = geometric_cdf ( x, a )

    x2 = geometric_cdf_inv ( cdf, a )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'GEOMETRIC_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def geometric_check ( a ):

#*****************************************************************************80
#
## GEOMETRIC_CHECK checks the parameter of the Geometric CDF.
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
#    Input, real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 0.0 or 1.0 < a ):
    print ( '' )
    print ( 'GEOMETRIC_CHECK - Fatal error!' )
    print ( '  A < 0 or 1 < A.' )
    check = False

  return check

def geometric_mean ( a ):

#*****************************************************************************80
#
## GEOMETRIC_MEAN returns the mean of the Geometric PDF.
#
#  Discussion:
#
#    MEAN is the expected value of the number of trials required
#    to obtain a single success.
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
#    Input, real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = 1.0 / a

  return mean

def geometric_pdf ( x, a ):

#*****************************************************************************80
#
## GEOMETRIC_PDF evaluates the Geometric PDF.
#
#  Discussion:
#
#    PDF(X)(A) = A * ( 1 - A )^(X-1)
#
#    PDF(X)(A) is the probability that exactly X Bernoulli trials, each
#    with probability of success A, will be required to achieve
#    a single success.
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
#    Input, integer X, the number of trials.
#    0 < X
#
#    Input, real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#    Output, real PDF, the value of the PDF.
#

#
#  Special cases.
#
  if ( x < 1 ):

    pdf = 0.0

  elif ( a == 0.0 ):

    pdf = 0.0

  elif ( a == 1.0 ):

    if ( x == 1 ):
      pdf = 1.0
    else:
      pdf = 0.0

  else:

    pdf = a * ( 1.0 - a ) ** ( x - 1 )

  return pdf

def geometric_sample ( a, seed ):

#*****************************************************************************80
#
## GEOMETRIC_SAMPLE samples the Geometric PDF.
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
#    Input, real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = geometric_cdf_inv ( cdf, a )

  return x, seed

def geometric_sample_test ( ):

#*****************************************************************************80
#
## GEOMETRIC_SAMPLE_TEST tests GEOMETRIC_SAMPLE.
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
  print ( 'GEOMETRIC_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  GEOMETRIC_MEAN computes the Geometric mean' )
  print ( '  GEOMETRIC_SAMPLE samples the Geometric distribution' )
  print ( '  GEOMETRIC_VARIANCE computes the Geometric variance.' )

  a = 0.25

  check = geometric_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'GEOMETRIC_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = geometric_mean ( a )
  variance = geometric_variance ( a )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = geometric_sample ( a, seed )

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
  print ( 'GEOMETRIC_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def geometric_variance ( a ):

#*****************************************************************************80
#
## GEOMETRIC_VARIANCE returns the variance of the Geometric PDF.
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
#    Input, real A, the probability of success on one trial.
#    0.0 <= A <= 1.0.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = ( 1.0 - a ) / ( a * a )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  geometric_cdf_test ( )
  geometric_sample_test ( )
  timestamp ( )
 
