#! /usr/bin/env python
#
def student_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## STUDENT_CDF evaluates the central Student T CDF.
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
#    Input, real X, the argument of the CDF.
#
#    Input, real A, B, shape parameters of the PDF,
#    used to transform the argument X to a shifted and scaled 
#    value Y = ( X - A ) / B.  It is required that B be nonzero.
#    For the standard distribution, A = 0 and B = 1.
#
#    Input, real C, is usually called the number of 
#    degrees of freedom of the distribution.  C is typically an 
#    integer, but that is not essential.  It is required that
#    C be strictly positive.
#
#    Output, real CDF, the value of the CDF.
#
  from beta_inc import beta_inc

  y = ( x - a ) / b

  a2 = 0.5 * c
  b2 = 0.5
  c2 = c / ( c + y * y )

  if ( y <= 0.0 ):
    cdf = 0.5 * beta_inc ( a2, b2, c2 )
  else:
    cdf = 1.0 - 0.5 * beta_inc ( a2, b2, c2 )

  return cdf

def student_cdf_test ( ):

#*****************************************************************************80
#
## STUDENT_CDF_TEST tests STUDENT_CDF.
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
  print ( 'STUDENT_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  STUDENT_CDF evaluates the Student CDF.' )
  print ( '  STUDENT_PDF evaluates the Student PDF.' )

  x = 2.447

  a = 0.5
  b = 2.0
  c = 6.0

  check = student_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'STUDENT_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  pdf = student_pdf ( x, a, b, c )

  cdf = student_cdf ( x, a, b, c )

  print ( '' )
  print ( '  PDF argument X =    %14g' % ( x ) )
  print ( '  PDF parameter A =   %14g' % ( a ) )
  print ( '  PDF parameter B =   %14g' % ( b ) )
  print ( '  PDF parameter C =   %14g' % ( c ) )
  print ( '  PDF value =         %14g' % ( pdf ) )
  print ( '  CDF value =         %14g' % ( cdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'STUDENT_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def student_check ( a, b, c ):

#*****************************************************************************80
#
## STUDENT_CHECK checks the parameter of the central Student T CDF.
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
#    Input, real A, B, shape parameters of the PDF,
#    used to transform the argument X to a shifted and scaled 
#    value Y = ( X - A ) / B.  It is required that B be nonzero.
#    For the standard distribution, A = 0 and B = 1.
#
#    Input, real C, is usually called the number of 
#    degrees of freedom of the distribution.  C is typically an 
#    integer, but that is not essential.  It is required that
#    C be strictly positive.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( b == 0.0 ):
    print ( '' )
    print ( 'STUDENT_CHECK - Fatal error!' )
    print ( '  B must be nonzero.' )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'STUDENT_CHECK - Fatal error!' )
    print ( '  C must be greater than 0.' )
    check = False

  return check

def student_mean ( a, b, c ):

#*****************************************************************************80
#
## STUDENT_MEAN returns the mean of the central Student T PDF.
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
#    Input, real A, B, shape parameters of the PDF,
#    used to transform the argument X to a shifted and scaled 
#    value Y = ( X - A ) / B.  It is required that B be nonzero.
#    For the standard distribution, A = 0 and B = 1.
#
#    Input, real C, is usually called the number of 
#    degrees of freedom of the distribution.  C is typically an 
#    integer, but that is not essential.  It is required that
#    C be strictly positive.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = a

  return mean

def student_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## STUDENT_PDF evaluates the central Student T PDF.
#
#  Formula:
#
#    PDF(X)(A,B,C) = Gamma ( (C+1)/2 ) /
#      ( Gamma ( C / 2 ) * Sqrt ( PI * C )
#      * ( 1 + ((X-A)/B)^2/C )^(C + 1/2 ) )
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
#    Input, real A, B, shape parameters of the PDF,
#    used to transform the argument X to a shifted and scaled 
#    value Y = ( X - A ) / B.  It is required that B be nonzero.
#    For the standard distribution, A = 0 and B = 1.
#
#    Input, real C, is usually called the number of 
#    degrees of freedom of the distribution.  C is typically an 
#    integer, but that is not essential.  It is required that
#    C be strictly positive.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from r8_gamma import r8_gamma

  y = ( x - a ) / b

  pdf = r8_gamma ( 0.5 * ( c + 1.0 ) ) / ( np.sqrt ( np.pi * c ) \
    * r8_gamma ( 0.5 * c ) * np.sqrt ( ( 1.0 + y * y / c ) \
    ** ( 2 * c + 1.0 ) ) )

  return pdf

def student_sample ( a, b, c, seed ):

#*****************************************************************************80
#
## STUDENT_SAMPLE samples the central Student T PDF.
#
#  Discussion:
#
#    For the sampling algorithm, it is necessary that 2 < C.
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
#    Input, real A, B, shape parameters of the PDF,
#    used to transform the argument X to a shifted and scaled 
#    value Y = ( X - A ) / B.  It is required that B be nonzero.
#    For the standard distribution, A = 0 and B = 1.
#
#    Input, real C, is usually called the number of 
#    degrees of freedom of the distribution.  C is typically an 
#    integer, but that is not essential.  It is required that
#    C be strictly positive.  
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from chi_square import chi_square_sample
  from normal import normal_sample
  from sys import exit

  if ( c <= 2.0 ):
    print ( '' )
    print ( 'STUDENT_SAMPLE - Fatal error!' )
    print ( '  Sampling fails for C <= 2.' )
    exit ( 'STUDENT_SAMPLE - Fatal error!' )

  a2 = 0.0
  b2 = c / ( c - 2.0 )

  x2, seed = normal_sample ( a2, b2, seed )

  a3 = c
  x3, seed = chi_square_sample ( a3, seed )
  x3 = x3 * c / ( c - 2.0 )

  x = a + b * x2 * np.sqrt ( c ) / x3

  return x, seed

def student_sample_test ( ):

#*****************************************************************************80
#
## STUDENT_SAMPLE_TEST tests STUDENT_SAMPLE.
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
  print ( 'STUDENT_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  STUDENT_MEAN computes the Student mean' )
  print ( '  STUDENT_SAMPLE samples the Student distribution' )
  print ( '  STUDENT_VARIANCE computes the Student variance.' )

  a = 0.5
  b = 2.0
  c = 6.0

  check = student_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'STUDENT_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = student_mean ( a, b, c )
  variance = student_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF parameter B =             %14g' % ( b ) )
  print ( '  PDF parameter C =             %14g' % ( c ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = student_sample ( a, b, c, seed )

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
  print ( 'STUDENT_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def student_variance ( a, b, c ):

#*****************************************************************************80
#
## STUDENT_VARIANCE returns the variance of the central Student T PDF.
#
#  Discussion:
#
#    For the variance to exist, it is necessary that 2 < C.
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
#    Input, real A, B, shape parameters of the PDF,
#    used to transform the argument X to a shifted and scaled 
#    value Y = ( X - A ) / B.  It is required that B be nonzero.
#    For the standard distribution, A = 0 and B = 1.
#
#    Input, real C, is usually called the number of 
#    degrees of freedom of the distribution.  C is typically an 
#    integer, but that is not essential.  It is required that
#    C be strictly positive.  
#
#    Output, real VARIANCE, the variance of the PDF.
#
  from sys import exit

  if ( c <= 2.0 ):
    print ( '' )
    print ( 'STUDENT_VARIANCE - Fatal error!' )
    print ( '  Variance not defined for C <= 2.' )
    exit ( 'STUDENT_VARIANCE - Fatal error!' )

  variance = b * b * c / ( c - 2.0 )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  student_cdf_test ( )
  student_sample_test ( )
  timestamp ( )
 
