#! /usr/bin/env python
#
def binomial_cdf ( x, a, b ):

#*****************************************************************************80
#
## BINOMIAL_CDF evaluates the Binomial CDF.
#
#  Discussion:
#
#    CDF(X)(A,B) is the probability of at most X successes in A trials,
#    given that the probability of success on a single trial is B.
#
#    A sequence of trials with fixed probability of success on
#    any trial is known as a sequence of Bernoulli trials.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the desired number of successes.
#    0 <= X <= A.
#
#    Input, integer A, the number of trials.
#    1 <= A.
#
#    Input, real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#    Output, real CDF, the value of the CDF.
#
  from i4_choose import i4_choose

  if ( x < 0 ):

    cdf = 0.0

  elif ( a <= x ):

    cdf = 1.0

  elif ( b == 0.0 ):

    cdf = 1.0

  elif ( b == 1.0 ):

    cdf = 0.0

  else:

    cdf = 0.0

    for j in range ( 0, x + 1 ):

      cnk = i4_choose ( a, j )

      pr = cnk * b ** j * ( 1.0 - b ) ** ( a - j )

      cdf = cdf + pr

  return cdf

def binomial_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## BINOMIAL_CDF_INV inverts the Binomial CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2016
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
#    Input, integer A, the number of trials.
#    1 <= A.
#
#    Input, real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#    Output, integer X, the corresponding argument.
#
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'BINOMIAL_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'BINOMIAL_CDF_INV - Fatal error!' )

  cdf2 = 0.0

  for x2 in range ( 0, a + 1 ):

    pdf = binomial_pdf ( x2, a, b )

    cdf2 = cdf2 + pdf

    if ( cdf <= cdf2 ):
      x = x2
      return x

  return x

def binomial_cdf_test ( ):

#*****************************************************************************80
#
## BINOMIAL_CDF_TEST tests BINOMIAL_CDF, BINOMIAL_CDF_INV, BINOMIAL_PDF
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'BINOMIAL_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BINOMIAL_CDF evaluates the Binomial CDF' )
  print ( '  BINOMIAL_CDF_INV inverts the Binomial CDF.' )
  print ( '  BINOMIAL_PDF evaluates the Binomial PDF' )

  a = 5
  b = 0.65

  check = binomial_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'BINOMIAL_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = binomial_sample ( a, b, seed )

    pdf = binomial_pdf ( x, a, b )

    cdf = binomial_cdf ( x, a, b )

    x2 = binomial_cdf_inv ( cdf, a, b )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'BINOMIAL_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def binomial_check ( a, b ):

#*****************************************************************************80
#
## BINOMIAL_CHECK checks the parameter of the Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the number of trials.
#    1 <= A.
#
#    Input, real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#    Output, logical CHECK, is TRUE if the parameters are legal.
#
  if ( a < 1 ):
    print ( '' )
    print ( 'BINOMIAL_CHECK - Fatal error!' )
    print ( '  A < 1.' )
    check = False
    return check

  if ( b < 0.0 or 1.0 < b ):
    print ( '' )
    print ( 'BINOMIAL_CHECK - Fatal error!' )
    print ( '  B < 0 or 1 < B.' )
    check = False
    return check

  check = True

  return check

def binomial_mean ( a, b ):

#*****************************************************************************80
#
## BINOMIAL_MEAN returns the mean of the Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the number of trials.
#    1 <= A.
#
#    Input, real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#    Output, real MEAN, the expected value of the number of
#    successes in A trials.
#
  mean = a * b

  return mean

def binomial_pdf ( x, a, b ):

#*****************************************************************************80
#
## BINOMIAL_PDF evaluates the Binomial PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) is the probability of exactly X successes in A trials,
#    given that the probability of success on a single trial is B.
#
#    PDF(X)(A,B) = C(N,X) * B^X * ( 1.0D+00 - B )^( A - X )
#
#    Binomial_PDF(X)(1,B) = Bernoulli_PDF(X)(B).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the desired number of successes.
#    0 <= X <= A.
#
#    Input, integer A, the number of trials.
#    1 <= A.
#
#    Input, real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#    Output, real PDF, the value of the PDF.
#
  from i4_choose import i4_choose

  if ( a < 1 ):

    pdf = 0.0

  elif ( x < 0 or a < x ):

    pdf = 0.0

  elif ( b == 0.0 ):

    if ( x == 0 ):
      pdf = 1.0
    else:
      pdf = 0.0

  elif ( b == 1.0 ):

    if ( x == a ):
      pdf = 1.0
    else:
      pdf = 0.0

  else:

    cnk = float ( i4_choose ( a, x ) )

    pdf = cnk * b ** x * ( 1.0 - b ) ** ( a - x )

  return pdf

def binomial_sample ( a, b, seed ):

#*****************************************************************************80
#
## BINOMIAL_SAMPLE samples the Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    William Kennedy and James Gentle,
#    Algorithm BU,
#    Statistical Computing,
#    Dekker, 1980.
#
#  Parameters:
#
#    Input, integer A, the number of trials.
#    1 <= A.
#
#    Input, real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer X, a sample of the PDF.
#
#    Output, integer SEED, a seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  x = 0

  for i in range ( 0, a ):

    u, seed = r8_uniform_01 ( seed )

    if ( u <= b ):
      x = x + 1

  return x, seed

def binomial_sample_test ( ):

#*****************************************************************************80
#
## BINOMIAL_SAMPLE_TEST tests BINOMIAL_MEAN, BINOMIAL_SAMPLE, BINOMIAL_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2016
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
  print ( 'BINOMIAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  BINOMIAL_MEAN computes the Binomial mean' )
  print ( '  BINOMIAL_SAMPLE samples the Binomial distribution' )
  print ( '  BINOMIAL_VARIANCE computes the Binomial variance.' )

  a = 5
  b = 0.30

  check = binomial_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'BINOMIAL_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = binomial_mean ( a, b )
  variance = binomial_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A = %6d' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i], seed = binomial_sample ( a, b, seed )

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
  print ( 'BINOMIAL_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def binomial_variance ( a, b ):

#*****************************************************************************80
#
## BINOMIAL_VARIANCE returns the variance of the Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, the number of trials.
#    1 <= A.
#
#    Input, real B, the probability of success on one trial.
#    0.0 <= B <= 1.0.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = a * b * ( 1.0 - b )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  binomial_cdf_test ( )
  binomial_sample_test ( )
  timestamp ( )
 
