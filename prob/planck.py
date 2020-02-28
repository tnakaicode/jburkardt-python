#! /usr/bin/env python3
#
def planck_check ( a, b ):

#*****************************************************************************80
#
## PLANCK_CHECK checks the parameters of the Planck PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Output, logical CHECK, is TRUE if the parameters are legal.
#
  check = True

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'PLANCK_CHECK - Fatal error!' )
    print ( '  A <= 0.' )
    check = False

  if ( b <= 0.0 ):
    print ( '' )
    print ( 'PLANCK_CHECK - Fatal error!' )
    print ( '  B <= 0.' )
    check = False

  return check

def planck_mean ( a, b ):

#*****************************************************************************80
#
## PLANCK_MEAN returns the mean of the Planck PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Output, real MEAN, the mean of the PDF.
#
  from r8_zeta import r8_zeta

  mean = ( b + 1.0 ) * r8_zeta ( b + 2.0 ) / r8_zeta ( b + 1.0 )

  return mean

def planck_pdf ( x, a, b ):

#*****************************************************************************80
#
## PLANCK_PDF evaluates the Planck PDF.
#
#  Discussion:
#
#    The Planck PDF has the form
#
#      PDF(A,BX) = A^(B+1) * X^B / ( exp ( A * X ) - 1 ) / K
#
#    where K is the normalization constant, and has the value
#
#      K = Gamma ( B + 1 ) * Zeta ( B + 1 ).
#
#    The original Planck distribution governed the frequencies in
#    blackbody radiation at a given temperature T, and has the form
#
#      PDF(AX) = K * X^3 / ( exp ( A * X ) - 1 )
#
#    where 
#
#      K = 15 / PI^4.
#
#    Thus, in terms of the Planck PDF, the original Planck distribution
#    has A = 1, B = 3.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
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
#    Input, double A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from r8_gamma import r8_gamma
  from r8_zeta import r8_zeta

  if ( x < 0.0 ):
    pdf = 0.0
  else:
    k = r8_gamma ( b + 1.0 ) * r8_zeta ( b + 1.0 )
    pdf = a ** ( b + 1.0 ) * x ** b / ( np.exp ( a * x ) - 1.0 ) / k

  return pdf

def planck_pdf_test ( ):

#*****************************************************************************80
#
## PLANCK_PDF_TEST tests PLANCK_PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'PLANCK_PDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PLANCK_PDF evaluates the Planck PDF.' )

  a = 2.0
  b = 3.0

  if ( not planck_check ( a, b ) ):
    print ( '' )
    print ( 'PLANCK_PDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %g' % ( a ) )
  print ( '  PDF parameter B = %g' % ( b ) )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = planck_sample ( a, b, seed )

    pdf = planck_pdf ( x, a, b )

    print ( '  %12g  %12g' % ( x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'PLANCK_PDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def planck_sample ( a, b, seed ):

#*****************************************************************************80
#
## PLANCK_SAMPLE samples the Planck PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Luc Devroye,
#    Non-Uniform Random Variate Generation,
#    Springer Verlag, 1986, pages 552.
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from gamma import gamma_sample
  from zipf import zipf_sample

  a2 = 0.0
  b2 = 1.0
  c2 = b + 1.0

  g, seed = gamma_sample ( a2, b2, c2, seed )

  z, seed = zipf_sample ( c2, seed )

  x = g / ( a * z )

  return x, seed

def planck_sample_test ( ):

#*****************************************************************************80
#
## PLANCK_SAMPLE_TEST tests PLANCK_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
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
  print ( 'PLANCK_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  PLANCK_MEAN returns the mean of the Planck distribution.' )
  print ( '  PLANCK_SAMPLE samples the Planck distribution.' )
  print ( '  PLANCK_VARIANCE returns the variance of the Planck distribution.' )
  print ( '' )
  
  a = 2.0
  b = 3.0

  if ( not planck_check ( a, b ) ):
    print ( '' )
    print ( 'PLANCK_SAMPLE_TEST' )
    print ( '  The parameters are not legal.' )
    return

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  mean = planck_mean ( a, b )
  variance = planck_variance ( a, b )

  print ( '' )
  print ( '  PDF mean =     %14g' % ( mean ) )
  print ( '  PDF variance = %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = planck_sample ( a, b, seed )

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
  print ( 'PLANCK_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def planck_variance ( a, b ):

#*****************************************************************************80
#
## PLANCK_VARIANCE returns the variance of the Planck PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, the parameters of the PDF.
#    0.0 < A,
#    0.0 < B.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = 2.0281 ** 2

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  planck_pdf_test ( )
  planck_sample_test ( )
  timestamp ( )
 
