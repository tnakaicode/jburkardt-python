#! /usr/bin/env python
#
def negative_binomial_cdf ( x, a, b ):

#*****************************************************************************80
#
## NEGATIVE_BINOMIAL_CDF evaluates the Negative Binomial CDF.
#
#  Discussion:
#
#    A simple summing approach is used.
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
#    Input, integer X, the argument of the CDF.
#
#    Input, integer A, a parameter of the PDF.
#    0 <= A.
#
#    Input, real B, a parameter of the PDF.
#    0 < B <= 1.
#
#    Output, real CDF, the value of the CDF.
#
  from i4_choose import i4_choose

  cdf = 0.0

  for y in range ( a, x + 1 ):

    cnk = i4_choose ( y - 1, a - 1 )

    pdf = cnk * b ** a * ( 1.0 - b ) ** ( y - a )

    cdf = cdf + pdf

  return cdf

def negative_binomial_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## NEGATIVE_BINOMIAL_CDF_INV inverts the Negative Binomial CDF.
#
#  Discussion:
#
#    A simple discrete approach is used.
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
#    Input, real CDF, the value of the CDF.
#
#    Input, integer A, real B, parameters of the PDF.
#    0 <= A,
#    0 < B <= 1.
#
#    Output, integer X, the smallest X whose cumulative density function
#    is greater than or equal to CDF.
#
  x_max = 1000

  if ( cdf <= 0.0 ):

    x = a

  else:

    cum = 0.0

    x = a

    while ( True ):

      pdf = negative_binomial_pdf ( x, a, b )

      cum = cum + pdf

      if ( cdf <= cum or x_max <= x ):
        break

      x = x + 1

  return x

def negative_binomial_cdf_test ( ):

#*****************************************************************************80
#
## NEGATIVE_BINOMIAL_CDF_TEST tests NEGATIVE_BINOMIAL_CDF.
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
  print ( 'NEGATIVE_BINOMIAL_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NEGATIVE_BINOMIAL_CDF evaluates the Negative Binomial CDF.' )
  print ( '  NEGATIVE_BINOMIAL_CDF_INV inverts the Negative Binomial CDF.' )
  print ( '  NEGATIVE_BINOMIAL_PDF evaluates the Negative Binomial PDF.' )

  a = 2
  b = 0.25

  if ( not negative_binomial_check ( a, b ) ):
    print ( '' )
    print ( 'NEGATIVE_BINOMIAL_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  print ( '' )
  print ( '  PDF parameter A = %6d' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = negative_binomial_sample ( a, b, seed )

    pdf = negative_binomial_pdf ( x, a, b )

    cdf = negative_binomial_cdf ( x, a, b )

    x2 = negative_binomial_cdf_inv ( cdf, a, b )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'NEGATIVE_BINOMIAL_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def negative_binomial_check ( a, b ):

#*****************************************************************************80
#
## NEGATIVE_BINOMIAL_CHECK checks the parameters of the Negative Binomial PDF.
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
#    Input, integer A, a parameter of the PDF.
#    0 <= A.
#
#    Input, real B, a parameter of the PDF.
#    0 < B <= 1.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 0 ):
    print ( '' )
    print ( 'NEGATIVE_BINOMIAL_CHECK - Fatal error!' )
    print ( '  A < 0.' )
    check = False

  if ( b <= 0.0 or 1.0 < b ):
    print ( '' )
    print ( 'NEGATIVE_BINOMIAL_CHECK - Fatal error!' )
    print ( '  B <= 0 or 1 < B.' )
    check = False

  return check

def negative_binomial_mean ( a, b ):

#*****************************************************************************80
#
## NEGATIVE_BINOMIAL_MEAN returns the mean of the Negative Binomial PDF.
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
#    Input, integer A, a parameter of the PDF.
#    0 <= A.
#
#    Input, real B, a parameter of the PDF.
#    0 < B <= 1.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = a / b

  return mean

def negative_binomial_pdf ( x, a, b ):

#*****************************************************************************80
#
## NEGATIVE_BINOMIAL_PDF evaluates the Negative Binomial PDF.
#
#  Formula:
#
#    PDF(X)(A,B) = C(X-1,A-1) * B^A * ( 1 - B )^(X-A)
#
#  Discussion:
#
#    PDF(X)(A,B) is the probability that the A-th success will
#    occur on the X-th trial, given that the probability
#    of a success on a single trial is B.
#
#    The Negative Binomial PDF is also known as the Pascal PDF or
#    the "Polya" PDF.
#
#    NEGATIVE_BINOMIAL_PDF(X)(1,B) = GEOMETRIC_PDF(X)(B)
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
#    Input, integer X, the number of trials.
#    A <= X.
#
#    Input, integer A, the number of successes required.
#    0 <= A <= X, normally.
#
#    Input, real B, the probability of a success on a single trial.
#    0.0 < B <= 1.0.
#
#    Output, real PDF, the value of the PDF.
#
  from i4_choose import i4_choose

  if ( x < a ):

    pdf = 0.0

  else:

    cnk = i4_choose ( x - 1, a - 1 )

    pdf = cnk * b ** a * ( 1.0 - b ) ** ( x - a )

  return pdf

def negative_binomial_sample ( a, b, seed ):

#*****************************************************************************80
#
## NEGATIVE_BINOMIAL_SAMPLE samples the Negative Binomial PDF.
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
#    Input, integer A, a parameter of the PDF.
#    0 <= A.
#
#    Input, real B, a parameter of the PDF.
#    0 < B <= 1.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  r8_huge = 1.0E+30

  if ( b == 1.0 ):
    x = a
    return x, seed
  elif ( b == 0.0 ):
    x = r8_huge
    return x, seed

  x = 0
  num_success = 0

  while ( num_success < a ):

    x = x + 1
    r, seed = r8_uniform_01 ( seed )

    if ( r <= b ):
      num_success = num_success + 1

  return x, seed

def negative_binomial_sample_test ( ):

#*****************************************************************************80
#
## NEGATIVE_BINOMIAL_SAMPLE_TEST tests NEGATIVE_BINOMIAL_SAMPLE.
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
  from i4vec_max import i4vec_max
  from i4vec_mean import i4vec_mean
  from i4vec_min import i4vec_min
  from i4vec_variance import i4vec_variance

  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'NEGATIVE_BINOMIAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  NEGATIVE_BINOMIAL_MEAN computes the Negative Binomial mean' )
  print ( '  NEGATIVE_BINOMIAL_SAMPLE samples the Negative Binomial distribution' )
  print ( '  NEGATIVE_BINOMIAL_VARIANCE computes the Negative Binomial variance.' )

  a = 2
  b = 0.75

  if ( not negative_binomial_check ( a, b ) ):
    print ( '' )
    print ( 'NEGATIVE_BINOMIAL_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return
  
  mean = negative_binomial_mean ( a, b )
  variance = negative_binomial_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %6d' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )
  
  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = negative_binomial_sample ( a, b, seed )

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
  print ( 'NEGATIVE_BINOMIAL_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def negative_binomial_variance ( a, b ):

#*****************************************************************************80
#
## NEGATIVE_BINOMIAL_VARIANCE returns the variance of the Negative Binomial PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 September 2004
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, a parameter of the PDF.
#    0 <= A.
#
#    Input, real B, a parameter of the PDF.
#    0 < B <= 1.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = a * ( 1.0 - b ) / ( b * b )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  negative_binomial_cdf_test ( )
  negative_binomial_sample_test ( )
  timestamp ( )
