#! /usr/bin/env python
#
def zipf_cdf_inv ( a, cdf ):

#*****************************************************************************80
#
## ZIPF_CDF_INV inverts the Zipf CDF.
#
#  Discussion:
#
#    Simple summation is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
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
#    1.0 < A.
#
#    Output, integer X, the argument such that
#    CDF(X-1) < CDF <= CDF(X)
#    1 <= X <= 1000
#
  from r8_zeta import r8_zeta

  if ( cdf <= 0.0 ):

    x = 1

  else:

    c = r8_zeta ( a )
    cdf2 = 0.0

    x = 1000

    for y in range ( 1, 1001 ):
      pdf = ( 1.0 / y ** a ) / c
      cdf2 = cdf2 + pdf
      if ( cdf <= cdf2 ):
        x = y
        break

  return x

def zipf_cdf ( x, a ):

#*****************************************************************************80
#
## ZIPF_CDF evaluates the Zipf CDF.
#
#  Discussion:
#
#    Simple summation is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the argument of the PDF.
#    1 <= X
#
#    Input, real A, the parameter of the PDF.
#    1.0 < A.
#
#    Output, real CDF, the value of the CDF.
#
  from r8_zeta import r8_zeta

  if ( x < 1 ):

    cdf = 0.0

  else:

    c = r8_zeta ( a )
    cdf = 0.0

    for y in range ( 1, x + 1 ):
      pdf = ( 1.0 / y ** a ) / c
      cdf = cdf + pdf

  return cdf

def zipf_cdf_test ( ):

#*****************************************************************************80
#
## ZIPF_CDF_TEST tests ZIPF_CDF, ZIPF_CDF_INV, ZIPF_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'ZIPF_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ZIPF_PDF evaluates the Zipf PDF.' )
  print ( '  ZIPF_CDF evaluates the Zipf CDF.' )
  print ( '  ZIPF_CDF_INV inverts the Zipf CDF.' )

  a = 2.0

  check = zipf_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'ZIPF_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '' )
  print ( '       X          PDF(X)          CDF(X)  CDF_INV(CDF)' )
  print ( '' )

  for x in range ( 1, 21 ):

    pdf = zipf_pdf ( x, a )
    cdf = zipf_cdf ( x, a )
    x2 = zipf_cdf_inv ( a, cdf )
    print ( '  %6d  %14g  %14g  %6d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ZIPF_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def zipf_check ( a ):

#*****************************************************************************80
#
## ZIPF_CHECK checks the parameter of the Zipf PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the parameter of the PDF.
#    1.0 < A.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  if ( a <= 1.0 ):
    print ( '' )
    print ( 'ZIPF_CHECK - Fatal error!' )
    print ( '  A <= 1.' )
    check = False
    return check

  check = True

  return check

def zipf_mean ( a ):

#*****************************************************************************80
#
## ZIPF_MEAN returns the mean of the Zipf PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the parameter of the PDF.
#    1.0 < A.
#
#    Output, real MEAN, the mean of the PDF.
#    The mean is only defined for 2 < A.
#
  from sys import exit
  from r8_zeta import r8_zeta

  if ( a <= 2.0 ):
    print ( '' )
    print ( 'ZIPF_MEAN - Fatal error!' )
    print ( '  No mean defined for A <= 2.' )
    exit ( 'ZIPF_MEAN - Fatal error!' )

  mean = r8_zeta ( a - 1.0 ) / r8_zeta ( a )

  return mean

def zipf_pdf ( x, a ):

#*****************************************************************************80
#
## ZIPF_PDF evaluates the Zipf PDF.
#
#  Discussion:
#
#    PDF(X)(A) = ( 1 / X^A ) / C
#
#    where the normalizing constant is chosen so that
#
#    C = Sum ( 1 <= I < oo ) 1 / I^A.
#
#    From observation, the frequency of different words in long
#    sequences of text seems to follow the Zipf PDF, with
#    parameter A slightly greater than 1.  The Zipf PDF is sometimes
#    known as the "discrete Pareto" PDF.
#
#    Lotka's law is a version of the Zipf PDF in which A is 2 or approximately
#    2.  Lotka's law describes the frequency of publications by authors in a
#    given field, and estimates that the number of authors with X papers is
#    about 1/X^A of the number of authors with 1 paper.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alfred Lotka,
#    The frequency distribution of scientific productivity,
#    Journal of the Washington Academy of Sciences,
#    Volume 16, Number 12, 1926, pages 317-324.
#
#  Parameters:
#
#    Input, integer X, the argument of the PDF.
#    1 <= N
#
#    Input, real A, the parameter of the PDF.
#    1.0 < A.
#
#    Output, real PDF, the value of the PDF.
#
  from r8_zeta import r8_zeta

  if ( x < 1 ):

    pdf = 0.0

  else:

    c = r8_zeta ( a )
    pdf = ( 1.0 / x ** a ) / c

  return pdf

def zipf_sample ( a, seed ):

#*****************************************************************************80
#
## ZIPF_SAMPLE samples the Zipf PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Luc Devroye,
#    Non-Uniform Random Variate Generation,
#    Springer Verlag, 1986, pages 550-551.
#
#  Parameters:
#
#    Input, real A, the parameter of the PDF.
#    1.0 < A.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, integer X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  b = 2.0 ** ( a - 1.0 )

  while ( True ):

    u, seed = r8_uniform_01 ( seed )
    v, seed = r8_uniform_01 ( seed )
    w = np.floor ( 1.0 / u ** ( 1.0 / ( a - 1.0 ) ) )

    t = ( ( w + 1.0 ) / w ) ** ( a - 1.0 )

    if ( v * w * ( t - 1.0 ) * b <= t * ( b - 1.0 ) ):
      break

  x = np.floor ( w )

  return x, seed

def zipf_sample_test ( ):

#*****************************************************************************80
#
## ZIPF_SAMPLE_TEST tests ZIPF_MEAN, ZIPF_SAMPLE, ZIPF_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
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
  print ( 'ZIPF_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ZIPF_MEAN returns the mean of the Zipf distribution.' )
  print ( '  ZIPF_SAMPLE samples the Zipf distribution.' )
  print ( '  ZIPF_VARIANCE returns the variance of the Zipf distribution.' )

  a = 4.0

  check = zipf_check ( a )

  if ( not check ):
    print ( '' )
    print ( 'ZIPF_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = zipf_mean ( a )
  variance = zipf_variance ( a )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = zipf_sample ( a, seed )

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
  print ( 'ZIPF_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def zipf_variance ( a ):

#*****************************************************************************80
#
## ZIPF_VARIANCE returns the variance of the Zipf PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the parameter of the PDF.
#    1.0 < A.
#
#    Output, real VARIANCE, the variance of the PDF.
#    The variance is only defined for 3 < A.
#
  from sys import exit
  from r8_zeta import r8_zeta

  if ( a <= 3.0 ):
    print ( '' )
    print ( 'ZIPF_VARIANCE - Fatal error!' )
    print ( '  No variance defined for A <= 3.0.' )
    exit ( 'ZIPF_VARIANCE - Fatal error!' )

  mean = zipf_mean ( a )

  variance = r8_zeta ( a - 2.0 ) / r8_zeta ( a ) - mean * mean

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  zipf_cdf_test ( )
  zipf_sample_test ( )
  timestamp ( )
 
