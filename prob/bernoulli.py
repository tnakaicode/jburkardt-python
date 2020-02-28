#! /usr/bin/env python
#
def bernoulli_cdf ( x, a ):

#*****************************************************************************80
#
## BERNOULLI_CDF evaluates the Bernoulli CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the number of successes on a single trial.
#    X = 0 or 1.
#
#    Input, real A, the probability of success on one trial.
#    0.0D+00 <= A <= 1.0.
#
#    Output, real CDF, the value of the CDF.
#
  if ( x < 0 ):
    cdf = 0.0
  elif ( x == 0 ):
    cdf = 1.0 - a
  else:
    cdf = 1.0

  return cdf

def bernoulli_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## BERNOULLI_CDF_INV inverts the Bernoulli CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#    0.0D+00 <= CDF <= 1.0.
#
#    Input, real A, the parameter of the PDF.
#    0.0D+00 <= A <= 1.0.
#
#    Output, integer X, the corresponding argument.
#
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'BERNOULLI_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'BERNOULLI_CDF_INV - Fatal error!' )

  if ( cdf <= 1.0 - a ):
    x = 0
  else:
    x = 1

  return x

def bernoulli_cdf_test ( ):

#*****************************************************************************80
#
## BERNOULLI_CDF_TEST tests BERNOULLI_CDF, BERNOULLI_CDF_INV, BERNOULLI_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BERNOULLI_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BERNOULLI_CDF evaluates the Bernoulli CDF' )
  print ( '  BERNOULLI_CDF_INV inverts the Bernoulli CDF.' )
  print ( '  BERNOULLI_PDF evaluates the Bernoulli PDF' )

  a = 0.75

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )

  check = bernoulli_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'BERNOULLI_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = bernoulli_sample ( a, seed )

    pdf = bernoulli_pdf ( x, a )

    cdf = bernoulli_cdf ( x, a )

    x2 = bernoulli_cdf_inv ( cdf, a )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BERNOULLI_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def bernoulli_check ( a ):

#*****************************************************************************80
#
## BERNOULLI_CHECK checks the parameter of the Bernoulli CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the parameter of the PDF.
#    0.0 <= A <= 1.0.
#
#    Output, logical CHECK, is TRUE if the parameters are OK.
#
  if ( a < 0.0 or 1.0 < a ):
    print ( '' )
    print ( 'BERNOULLI_CHECK - Fatal error!' )
    print ( '  A < 0 or 1 < A.' )
    check = False
  else:
    check = True

  return check

def bernoulli_mean ( a ):

#*****************************************************************************80
#
## BERNOULLI_MEAN returns the mean of the Bernoulli PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the probability of success.
#    0.0D+00 <= A <= 1.0.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def bernoulli_pdf ( x, a ):

#*****************************************************************************80
#
## BERNOULLI_PDF evaluates the Bernoulli PDF.
#
#  Discussion:
#
#    PDF(X)(A) = A^X * ( 1.0D+00 - A )^( X - 1 )
#
#    X = 0 or 1.
#
#    The Bernoulli PDF describes the simple case in which a single trial
#    is carried out, with two possible outcomes, called "success" and
#    "failure" the probability of success is A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the number of successes on a single trial.
#    X = 0 or 1.
#
#    Input, real A, the probability of success on one trial.
#    0.0D+00 <= A <= 1.0.
#
#    Output, real PDF, the value of the PDF.
#
  if ( x < 0 ):
    pdf = 0.0
  elif ( x == 0 ):
    pdf = 1.0 - a
  elif ( x == 1 ):
    pdf = a
  else:
    pdf = 0.0

  return pdf

def bernoulli_sample ( a, seed ):

#*****************************************************************************80
#
## BERNOULLI_SAMPLE samples the Bernoulli PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the probability of success on one trial.
#    0.0D+00 <= A <= 1.0.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = bernoulli_cdf_inv ( cdf, a )

  return x, seed

def bernoulli_sample_test ( ):

#*****************************************************************************80
#
## BERNOULLI_SAMPLE_TEST tests BERNOULLI_MEAN, BERNOULLI_SAMPLE, BERNOULLI_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2016
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
  print ( 'BERNOULLI_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BERNOULLI_MEAN computes the Bernoulli mean' )
  print ( '  BERNOULLI_SAMPLE samples the Bernoulli distribution' )
  print ( '  BERNOULLI_VARIANCE computes the Bernoulli variance.' )

  a = 0.75

  check = bernoulli_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'BERNOULLI_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = bernoulli_mean ( a )
  variance = bernoulli_variance ( a )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )
  
  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i], seed = bernoulli_sample ( a, seed )

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
  print ( 'BERNOULLI_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def bernoulli_variance ( a ):

#*****************************************************************************80
#
## BERNOULLI_VARIANCE returns the variance of the Bernoulli PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2016
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
  variance = a * ( 1.0 - a )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  bernoulli_cdf_test ( )
  bernoulli_sample_test ( )
  timestamp ( )
 
