#! /usr/bin/env python
#
def maxwell_cdf ( x, a ):

#*****************************************************************************80
#
## MAXWELL_CDF evaluates the Maxwell CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
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
#    Input, real A, the parameter of the PDF.
#    0 < A.
#
#    Output, real CDF, the value of the CDF.
#
  from r8_gamma_inc import r8_gamma_inc

  if ( x <= 0.0 ):

    cdf = 0.0

  else:

    x2 = x / a
    p2 = 1.5

    cdf = r8_gamma_inc ( p2, x2 )

  return cdf

def maxwell_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## MAXWELL_CDF_INV inverts the Maxwell CDF.
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
#    27 March 2016
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
#    0 < A.
#
#    Output, real X, the corresponding argument of the CDF.
#
  from sys import exit

  it_max = 100
  tol = 0.0001
  r8_huge = 1.0E+30

  if ( cdf <= 0.0 ):
    x = 0.0
    return x
  elif ( 1.0 <= cdf ):
    x = r8_huge
    return x

  x1 = 0.0
  cdf1 = 0.0

  x2 = 1.0

  while ( True ):

    cdf2 = maxwell_cdf ( x2, a )

    if ( cdf < cdf2 ):
      break

    x2 = 2.0 * x2

    if ( 1000000.0 < x2 ):
      print ( '' )
      print ( 'MAXWELL_CDF_INV - Fatal error!' )
      print ( '  Initial bracketing effort fails.' )
      exit ( 'MAXWELL_CDF_INV - Fatal error!' )
#
#  Now use bisection.
#
  it = 0

  while ( True ):

    it = it + 1

    x3 = 0.5 * ( x1 + x2 )
    cdf3 = maxwell_cdf ( x3, a )

    if ( abs ( cdf3 - cdf ) < tol ):
      x = x3
      break

    if ( it_max < it ):
      print ( '' )
      print ( 'MAXWELL_CDF_INV - Fatal error!' )
      print ( '  Iteration limit exceeded.' )
      exit ( 'MAXWELL_CDF_INV - Fatal error!' )

    if ( ( cdf3 <= cdf and cdf1 < cdf ) or ( cdf <= cdf3 and cdf <= cdf1 ) ):
      x1 = x3
      cdf1 = cdf3
    else:
      x2 = x3
      cdf2 = cdf3

  return x

def maxwell_cdf_test ( ):

#*****************************************************************************80
#
## MAXWELL_CDF_TEST tests MAXWELL_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'MAXWELL_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MAXWELL_CDF evaluates the Maxwell CDF.' )
  print ( '  MAXWELL_CDF_INV inverts the Maxwell CDF.' )
  print ( '  MAXWELL_PDF evaluates the Maxwell PDF.' )

  a = 2.0

  if ( not maxwell_check ( a ) ):
    print ( '' )
    print ( 'MAXWELL_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = maxwell_sample ( a, seed )

    pdf = maxwell_pdf ( x, a )

    cdf = maxwell_cdf ( x, a )

    x2 = maxwell_cdf_inv ( cdf, a )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'MAXWELL_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def maxwell_check ( a ):

#*****************************************************************************80
#
## MAXWELL_CHECK checks the parameters of the Maxwell CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the parameter of the PDF.
#    0 < A.
#
#    Output, logical CHECK, is true if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'MAXWELL_CHECK - Fatal error!' )
    print ( '  A <= 0.0.' )
    check = False

  return check

def maxwell_mean ( a ):

#*****************************************************************************80
#
## MAXWELL_MEAN returns the mean of the Maxwell PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the parameter of the PDF.
#    0 < A.
#
#    Output, real MEAN, the mean value.
#
  import numpy as np
  from r8_gamma import r8_gamma

  mean = np.sqrt ( 2.0 ) * a * r8_gamma ( 2.0 ) / r8_gamma ( 1.5 )

  return mean

def maxwell_pdf ( x, a ):

#*****************************************************************************80
#
## MAXWELL_PDF evaluates the Maxwell PDF.
#
#  Discussion:
#
#    PDF(X)(A) = EXP ( - 0.5 * ( X / A )^2 ) * ( X / A )^2 /
#      ( SQRT ( 2 ) * A * GAMMA ( 1.5 ) )
#
#    MAXWELL_PDF(X)(A) = CHI_PDF(0,A,3)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    0 < X
#
#    Input, real A, the parameter of the PDF.
#    0 < A.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from r8_gamma import r8_gamma

  if ( x <= 0.0 ):

    pdf = 0.0

  else:

    y = x / a

    pdf = np.exp ( -0.5 * y * y ) * y * y \
      / ( np.sqrt ( 2.0 ) * a * r8_gamma ( 1.5 ) )

  return pdf

def maxwell_sample ( a, seed ):

#*****************************************************************************80
#
## MAXWELL_SAMPLE samples the Maxwell PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the parameter of the PDF.
#    0 < A.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from chi_square import chi_square_sample

  a2 = 3.0
  x, seed = chi_square_sample ( a2, seed )

  x = a * np.sqrt ( x )

  return x, seed

def maxwell_sample_test ( ):

#*****************************************************************************80
#
## MAXWELL_SAMPLE_TEST tests MAXWELL_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
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
  print ( 'MAXWELL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  MAXWELL_MEAN computes the Maxwell mean' )
  print ( '  MAXWELL_VARIANCE computes the Maxwell variance' )
  print ( '  MAXWELL_SAMPLE samples the Maxwell distribution.' )

  a = 2.0

  if ( not maxwell_check ( a ) ):
    print ( '' )
    print ( 'MAXWELL_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = maxwell_mean ( a )
  variance = maxwell_variance ( a )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF mean =                    %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = maxwell_sample ( a, seed )

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
  print ( 'MAXWELL_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def maxwell_variance ( a ):

#*****************************************************************************80
#
## MAXWELL_VARIANCE returns the variance of the Maxwell PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the parameter of the PDF.
#    0 < A.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  from r8_gamma import r8_gamma

  variance = a * a * ( 3.0 - 2.0 * ( r8_gamma ( 2.0 ) / r8_gamma ( 1.5 ) ) ** 2 )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  maxwell_cdf_test ( )
  maxwell_sample_test ( )
  timestamp ( )
 
