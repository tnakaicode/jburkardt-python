#! /usr/bin/env python
#
def chi_cdf ( x, a, b, c ):

#*****************************************************************************80
#
## CHI_CDF evaluates the Chi CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#
#    Input, real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#    Output, real CDF, the value of the CDF.
#
  from r8_gamma_inc import r8_gamma_inc

  if ( x <= a ):

    cdf = 0.0

  else:

    y = ( x - a ) / b
    x2 = 0.5 * y * y
    p2 = 0.5 * c

    cdf = r8_gamma_inc ( p2, x2 )

  return cdf

def chi_cdf_inv ( cdf, a, b, c ):

#*****************************************************************************80
#
## CHI_CDF_INV inverts the Chi CDF.
#
#  Discussion:
#
#    A simple bisection method is used.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#
#    Input, real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#    Output, real X, the corresponding argument of the CDF.
#
  from r8_huge import r8_huge
  from sys import exit

  it_max = 100
  tol = 0.0001

  if ( cdf <= 0.0 ):
    x = a
    return x
  elif ( 1.0 <= cdf ):
    x = r8_huge ( )
    return x

  x1 = a
  cdf1 = 0.0

  x2 = a + 1.0

  while ( True ):

    cdf2 = chi_cdf ( x2, a, b, c )

    if ( cdf < cdf2 ):
      break

    x2 = a + 2.0 * ( x2 - a )
#
#  Now use bisection.
#
  it = 0

  while ( True ):

    it = it + 1

    x3 = 0.5 * ( x1 + x2 )
    cdf3 = chi_cdf ( x3, a, b, c )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      return x

    if ( it_max < it ):
      print ( '' )
      print ( 'CHI_CDF_INV - Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      exit ( 'CHI_CDF_INV - Fatal error!' )

    if ( ( cdf3 < cdf and cdf1 < cdf ) or ( cdf < cdf3 and cdf < cdf1 ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def chi_cdf_test ( ):

#*****************************************************************************80
#
## CHI_CDF_TEST tests CHI_CDF, CHI_CDF_INV, CHI_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'CHI_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHI_CDF evaluates the Chi CDF.' )
  print ( '  CHI_CDF_INV inverts the Chi CDF.' )
  print ( '  CHI_PDF evaluates the Chi PDF.' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = chi_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'CHI_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %14g' % ( c ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = chi_sample ( a, b, c, seed )

    pdf = chi_pdf ( x, a, b, c )

    cdf = chi_cdf ( x, a, b, c )

    x2 = chi_cdf_inv ( cdf, a, b, c )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CHI_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def chi_check ( a, b, c ):

#*****************************************************************************80
#
## CHI_CHECK checks the parameters of the Chi CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'CHI_CHECK - Fatal error!' )
    print ( '  B <= 0.0.' )
    check = False

  if ( c <= 0.0 ):
    print ( '' )
    print ( 'CHI_CHECK - Fatal error!' )
    print ( '  C <= 0.0.' )
    check = False

  return check

def chi_mean ( a, b, c ):

#*****************************************************************************80
#
## CHI_MEAN returns the mean of the Chi PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#    Output, real MEAN, the mean value.
#
  import numpy as np
  from r8_gamma import r8_gamma

  mean = a + np.sqrt ( 2.0 ) * b * r8_gamma ( 0.5 * ( c + 1.0 ) ) \
    / r8_gamma ( 0.5 * c )

  return mean

def chi_pdf ( x, a, b, c ):

#*****************************************************************************80
#
## CHI_PDF evaluates the Chi PDF.
#
#  Discussion:
#
#    PDF(X)(A,B,C) = EXP ( - 0.5 * ( ( X - A ) / B )^2 )
#      * ( ( X - A ) / B )^( C - 1 ) /
#      ( 2^( 0.5 * C - 1 ) * B * GAMMA ( 0.5 * C ) )
#
#    CHI(A,B,1) is the Half Normal PDF
#    CHI(0,B,2) is the Rayleigh PDF
#    CHI(0,B,3) is the Maxwell PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
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
#    Input, real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from r8_gamma import r8_gamma

  if ( x <= a ):

    pdf = 0.0

  else:

    y = ( x - a ) / b

    pdf = np.exp ( - 0.5 * y * y ) * y ** ( c - 1.0 ) \
      / ( 2.0 ** ( 0.5 * c - 1.0 ) * b * r8_gamma ( 0.5 * c ) )

  return pdf

def chi_sample ( a, b, c, seed ):

#*****************************************************************************80
#
## CHI_SAMPLE samples the Chi PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from chi_square import chi_square_sample

  x, seed = chi_square_sample ( c, seed )

  x = a + b * np.sqrt ( x )

  return x, seed

def chi_sample_test ( ):

#*****************************************************************************80
#
## CHI_SAMPLE_TEST tests CHI_MEAN, CHI_SAMPLE, CHI_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
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
  print ( 'CHI_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CHI_MEAN computes the Chi mean' )
  print ( '  CHI_VARIANCE computes the Chi variance' )
  print ( '  CHI_SAMPLE samples the Chi distribution.' )

  a = 1.0
  b = 2.0
  c = 3.0

  check = chi_check ( a, b, c )

  if ( not check ):
    print ( '' )
    print ( 'CHI_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = chi_mean ( a, b, c )
  variance = chi_variance ( a, b, c )

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )
  print ( '  PDF parameter C = %14g' % ( c ) )
  print ( '  PDF mean =        %14g' % ( mean ) )
  print ( '  PDF variance =    %14g' % ( variance ) )

  x = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x[i], seed = chi_sample ( a, b, c, seed )

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
  print ( 'CHI_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def chi_variance ( a, b, c ):

#*****************************************************************************80
#
## CHI_VARIANCE returns the variance of the Chi PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the PDF.
#    0 < B,
#    0 < C.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  from r8_gamma import r8_gamma

  variance = b * b * ( c - 2.0 * ( r8_gamma ( 0.5 * ( c + 1.0 ) ) \
    / r8_gamma ( 0.5 * c ) ) ** 2 )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  chi_cdf_test ( )
  chi_sample_test ( )
  timestamp ( )

