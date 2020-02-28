#! /usr/bin/env python
#
def exponential_cdf ( x, a, b ):

#*****************************************************************************80
#
## EXPONENTIAL_CDF evaluates the Exponential CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
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

  if ( x <= a ):
    cdf = 0.0
  else:
    cdf = 1.0 - np.exp ( ( a - x ) / b )

  return cdf

def exponential_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## EXPONENTIAL_CDF_INV inverts the Exponential CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
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
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real X, the corresponding argument.
#
  import numpy as np
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'EXPONENTIAL_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'EXPONENTIAL_CDF_INV - Fatal error!' )

  x = a - b * np.log ( 1.0 - cdf )

  return x

def exponential_cdf_test ( ):

#*****************************************************************************80
#
## EXPONENTIAL_CDF_TEST tests EXPONENTIAL_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'EXPONENTIAL_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EXPONENTIAL_CDF evaluates the Exponential CDF.' )
  print ( '  EXPONENTIAL_CDF_INV inverts the Exponential CDF.' )
  print ( '  EXPONENTIAL_PDF evaluates the Exponential PDF.' )

  a = 1.0
  b = 2.0

  check = exponential_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'EXPONENTIAL_CDF_TEST - Fatal error!' )
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

    x, seed = exponential_sample ( a, b, seed )

    pdf = exponential_pdf ( x, a, b )

    cdf = exponential_cdf ( x, a, b )

    x2 = exponential_cdf_inv ( cdf, a, b )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'EXPONENTIAL_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def exponential_check ( a, b ):

#*****************************************************************************80
#
## EXPONENTIAL_CHECK checks the parameters of the Exponential CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
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
    print ( 'EXPONENTIAL_CHECK - Fatal error!' )
    print ( '  B <= 0.0' )
    check = False

  return check

def exponential_mean ( a, b ):

#*****************************************************************************80
#
## EXPONENTIAL_MEAN returns the mean of the Exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
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
  mean = a + b

  return mean

def exponential_pdf ( x, a, b ):

#*****************************************************************************80
#
## EXPONENTIAL_PDF evaluates the Exponential PDF.
#
#  Discussion:
#
#    PDF(X)(A,B) = ( 1 / B ) * EXP ( ( A - X ) / B )
#
#    The time interval between two Poisson events is a random
#    variable with the Exponential PDF.  The parameter B is the
#    average interval between events.
#
#    In another context, the Exponential PDF is related to
#    the Boltzmann distribution, which describes the relative
#    probability of finding a system, which is in thermal equilibrium
#    at absolute temperature T, in a given state having energy E.
#    The relative probability is
#
#      Boltzmann_Relative_Probability(E,T) = exp ( - E / ( k * T ) ),
#
#    where k is the Boltzmann constant,
#
#      k = 1.38 * 10^(-23) joules / degree Kelvin
#
#    and normalization requires a determination of the possible
#    energy states of the system.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    A <= X
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < B.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  if ( x < a ):
    pdf = 0.0
  else:
    pdf = ( 1.0 / b ) * np.exp ( ( a - x ) / b )

  return pdf

def exponential_sample ( a, b, seed ):

#*****************************************************************************80
#
## EXPONENTIAL_SAMPLE samples the Exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
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

  x = exponential_cdf_inv ( cdf, a, b )

  return x, seed

def exponential_sample_test ( ):

#*****************************************************************************80
#
## EXPONENTIAL_SAMPLE_TEST tests EXPONENTIAL_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
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
  print ( 'EXPONENTIAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  EXPONENTIAL_MEAN computes the Exponential mean' )
  print ( '  EXPONENTIAL_SAMPLE samples the Exponential distribution' )
  print ( '  EXPONENTIAL_VARIANCE computes the Exponential variance.' )

  a = 1.0
  b = 10.0

  check = exponential_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'EXPONENTIAL_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = exponential_mean ( a, b )
  variance = exponential_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = exponential_sample ( a, b, seed )

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
  print ( 'EXPONENTIAL_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def exponential_variance ( a, b ):

#*****************************************************************************80
#
## EXPONENTIAL_VARIANCE returns the variance of the Exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 March 2016
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
  variance = b * b

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  exponential_cdf_test ( )
  exponential_sample_test ( )
  timestamp ( )
 
