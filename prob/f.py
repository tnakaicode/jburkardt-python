#! /usr/bin/env python
#
def f_cdf ( x, m, n ):

#*****************************************************************************80
#
## F_CDF evaluates the F central CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Formula 26.5.28
#    Abramowitz and Stegun,
#    Handbook of Mathematical Functions.
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Input, integer M, N, the parameters of the PDF.
#    1 <= M,
#    1 <= N.
#
#    Output, real CDF, the value of the CDF.
#
  from beta_inc import beta_inc

  if ( x <= 0.0 ):

    cdf = 0.0

  else:

    arg1 = 0.5 * float ( n )
    arg2 = 0.5 * float ( m )
    arg3 = float ( n ) / float ( n + m * x )

    cdf = beta_inc ( arg1, arg2, arg3 )

  return cdf

def f_cdf_test ( ):

#*****************************************************************************80
#
## F_CDF_TEST tests F_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'F_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  F_CDF evaluates the F CDF.' )
  print ( '  F_PDF evaluates the F PDF.' )

  m = 1
  n = 1
  seed = 123456789
  
  if ( not f_check ( m, n ) ):
    print ( '' )
    print ( 'F_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal!' )
    return

  print ( '' )
  print ( '  PDF parameter M = %6d' % ( m ) )
  print ( '  PDF parameter N = %6d' % ( n ) )

  print ( '' )
  print ( '      X        M     N        PDF         CDF' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = f_sample ( m, n, seed )

    pdf = f_pdf ( x, m, n )

    cdf = f_cdf ( x, m, n )

    print ( '  %14g  %6d  %6d  %14g  %14g' % ( x, m, n, pdf, cdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'F_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def f_check ( m, n ):

#*****************************************************************************80
#
## F_CHECK checks the parameters of the F PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the parameters of the PDF.
#    0 < M
#    0 < N
#
#    Output, logical CHECK, is TRUE if the parameters are legal.
#
  check = True

  if ( m <= 0 ):
    print ( '' )
    print ( 'F_CHECK - Fatal error!' )
    print ( '  M <= 0.' )
    check = False

  if ( n <= 0 ):
    print ( '' )
    print ( 'F_CHECK - Fatal error!' )
    print ( '  N <= 0.' )
    check = False

  return check

def f_mean ( m, n ):

#*****************************************************************************80
#
## F_MEAN returns the mean of the F central PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the parameters of the PDF.
#    1 <= M,
#    1 <= N.
#    Note, however, that the mean is not defined unless 3 <= N.
#
#    Output, real MEAN, the mean of the PDF.
#
  from sys import exit

  if ( n < 3 ):
    print ( '' )
    print ( 'F_MEAN - Fatal error!' )
    print ( '  The mean is not defined for N < 3.' )
    exit ( 'F_MEAN - Fatal error!' )

  mean = float ( n ) / float ( n - 2 )

  return mean

def f_pdf ( x, m, n ):

#*****************************************************************************80
#
## F_PDF evaluates the F central PDF.
#
#  Discussion:
#
#    PDF(X)(M,N) = M^(M/2) * X^((M-2)/2)
#      / ( Beta(M/2,N/2) * N^(M/2) * ( 1 + (M/N) * X )^((M+N)/2)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    0.0 <= X
#
#    Input, integer M, N, the parameters of the PDF.
#    1 <= M,
#    1 <= N.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from r8_beta import r8_beta

  if ( x < 0.0 ):

    pdf = 0.0

  else:

    a = m
    b = n

    top = np.sqrt ( float ( m ) ** m * float ( n ) ** n * x ** ( m - 2 ) )
    bot1 = r8_beta ( float ( m ) / 2.0, float ( n ) / 2.0 )
    bot2 = np.sqrt ( ( n + m * x ) ** ( m + n ) )

    pdf = top / ( bot1 * bot2 )

  return pdf

def f_sample ( m, n, seed ):

#*****************************************************************************80
#
## F_SAMPLE samples the F central PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the parameters of the PDF.
#    1 <= M,
#    1 <= N.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from chi_square import chi_square_sample

  xm, seed = chi_square_sample ( m, seed )

  xn, seed = chi_square_sample ( n, seed )

  x = float ( n ) * xm / ( float ( m ) * xn )

  return x, seed

def f_sample_test ( ):

#*****************************************************************************80
#
## F_SAMPLE_TEST tests F_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
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
  print ( 'F_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  F_MEAN computes the F mean' )
  print ( '  F_SAMPLE samples the F distribution' )
  print ( '  F_VARIANCE computes the F variance.' )

  m = 8
  n = 6

  if ( not f_check ( m, n ) ):
    print ( '' )
    print ( 'F_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal!' )
    return

  mean = f_mean ( m, n )
  variance = f_variance ( m, n )

  print ( '' )
  print ( '  PDF parameter M =       %6d' % ( m ) )
  print ( '  PDF parameter N =       %6d' % ( n ) )
  print ( '  PDF mean =              %14g' % ( mean ) )
  print ( '  PDF variance =          %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = f_sample ( m, n, seed )

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
  print ( 'F_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def f_variance ( m, n ):

#*****************************************************************************80
#
## F_VARIANCE returns the variance of the F central PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the parameters of the PDF.
#    1 <= M,
#    1 <= N.
#    Note, however, that the variance is not defined unless 5 <= N.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  from sys import exit

  if ( n < 5 ):
    print ( '' )
    print ( 'F_VARIANCE - Fatal error!' )
    print ( '  The variance is not defined for N < 5.' )
    exit ( 'F_VARIANCE - Fatal error!' )

  variance = float ( 2 * n * n * ( m + n - 2 ) ) \
    / float ( m * ( n - 2 ) ** 2 * ( n - 4 ) )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  f_cdf_test ( )
  f_sample_test ( )
  timestamp ( )
 
