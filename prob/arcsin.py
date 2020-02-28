#! /usr/bin/env python
#
def arcsin_cdf_inv ( cdf, a ):

#*****************************************************************************80
#
## ARCSIN_CDF_INV inverts the Arcsin CDF.
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
#    0.0 <= CDF <= 1.0.
#
#    Input, real A, the parameter of the CDF.
#    A must be positive.
#
#    Output, real X, the corresponding argument.
#
  import numpy as np
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'ARCSIN_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'ARCSIN_CDF_INV - Fatal error!' )

  x = a * np.sin ( np.pi * ( cdf - 0.5 ) )

  return x

def arcsin_cdf ( x, a ):

#*****************************************************************************80
#
## ARCSIN_CDF evaluates the Arcsin CDF.
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
#    Input, real X, the argument of the CDF.
#
#    Input, real A, the parameter of the CDF.
#    A must be positive.
#
#    Output, real CDF, the value of the CDF.
#
  import numpy as np

  if ( x <= -a ):
    cdf = 0.0
  elif ( x < a ):
    cdf = 0.5 + np.arcsin ( x / a ) / np.pi
  else:
    cdf = 1.0

  return cdf

def arcsin_cdf_test ( ):

#*****************************************************************************80
#
## ARCSIN_CDF_TEST tests ARCSIN_CDF, ARCSIN_CDF_INV, ARCSIN_PDF.
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
  print ( 'ARCSIN_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ARCSIN_CDF evaluates the Arcsin CDF' )
  print ( '  ARCSIN_CDF_INV inverts the Arcsin CDF.' )
  print ( '  ARCSIN_PDF evaluates the Arcsin PDF' )

  a = 1.0

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )

  if ( not arcsin_check ( a ) ):
    print ( '' )
    print ( 'ARCSIN_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = arcsin_sample ( a, seed )

    pdf = arcsin_pdf ( x, a )

    cdf = arcsin_cdf ( x, a )

    x2 = arcsin_cdf_inv ( cdf, a )

    print ( ' %14f  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'ARCSIN_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def arcsin_check ( a ):

#*****************************************************************************80
#
## ARCSIN_CHECK checks the parameter of the Arcsin CDF.
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
#    0.0 < A.
#
#    Output, bool CHECK, is TRUE if the parameters are OK.
#
  if ( a <= 0.0 ):
    print ( '' )
    print ( 'ARCSIN_CHECK - Fatal error!' )
    print ( '  A <= 0.' )
    check = False
  else:
    check = True

  return check

def arcsin_mean ( a ):

#*****************************************************************************80
#
## ARCSIN_MEAN returns the mean of the Arcsin PDF.
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
#    Input, real A, the parameter of the CDF.
#    A must be positive.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = 0.0

  return mean

def arcsin_pdf ( x, a ):

#*****************************************************************************80
#
## ARCSIN_PDF evaluates the Arcsin PDF.
#
#  Discussion:
#
#    The LOGISTIC EQUATION has the form:
#
#      X(N+1) = 4.0D+00 * LAMBDA * ( 1.0 - X(N) ).
#
#    where 0 < LAMBDA <= 1.  This nonlinear difference equation maps
#    the unit interval into itself, and is a simple example of a system
#    exhibiting chaotic behavior.  Ulam and von Neumann studied the
#    logistic equation with LAMBDA = 1, and showed that iterates of the
#    function generated a sequence of pseudorandom numbers with
#    the Arcsin probability density function.
#
#    The derived sequence
#
#      Y(N) = ( 2 / PI ) * Arcsin ( SQRT ( X(N) ) )
#
#    is a pseudorandom sequence with the uniform probability density
#    function on [0,1].  For certain starting values, such as X(0) = 0, 0.75,
#    or 1.0D+00, the sequence degenerates into a constant sequence, and for
#    values very near these, the sequence takes a while before becoming
#    chaotic.
#
#    PDF(X) = 1 / ( PI * Sqrt ( A^2 - X^2 ) )
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
#  Reference:
#
#    Daniel Zwillinger and Stephen Kokoska,
#    CRC Standard Probability and Statistics Tables and Formulae,
#    Chapman and Hall/CRC, 2000, pages 114-115.
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    -A < X < A.
#
#    Input, real A, the parameter of the CDF.
#    A must be positive.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np
  from sys import exit

  if ( a <= 0.0 ):
    print ( '' )
    print ( 'ARCSIN_PDF - Fatal error!' )
    print ( '  Parameter A must be positive.' )
    exit ( 'ARCSIN_PDF - Fatal error!' )

  if ( x <= - a or a <= x ):
    pdf = 0.0
  else:
    pdf = 1.0 / ( np.pi * np.sqrt ( a * a - x * x ) )

  return pdf

def arcsin_sample ( a, seed ):

#*****************************************************************************80
#
## ARCSIN_SAMPLE samples the Arcsin PDF.
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
#    Input, real A, the parameter of the CDF.
#    A must be positive.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X, a sample of the PDF.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = arcsin_cdf_inv ( cdf, a )

  return x, seed

def arcsin_sample_test ( ):

#*****************************************************************************80
#
## ARCSIN_SAMPLE_TEST tests ARCSIN_MEAN, ARCSIN_SAMPLE, ARCSIN_VARIANCE.
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
  from r8vec_max import r8vec_max
  from r8vec_mean import r8vec_mean
  from r8vec_min import r8vec_min
  from r8vec_variance import r8vec_variance

  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'ARCSIN_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  ARCSIN_MEAN computes the Arcsin mean' )
  print ( '  ARCSIN_SAMPLE samples the Arcsin distribution' )
  print ( '  ARCSIN_VARIANCE computes the Arcsin variance.' )

  for i in range ( 1, 3 ):

    if ( i == 1 ):
      a = 1.0
    elif ( i == 2 ):
      a = 16.0

    print ( '' )
    print ( '  PDF parameter A = %14g' % ( a ) )

    if ( not arcsin_check ( a ) ):
      print ( '' )
      print ( 'ARCSIN_SAMPLE_TEST - Fatal error!' )
      print ( '  The parameters are not legal.' )
      return

    mean = arcsin_mean ( a )
    variance = arcsin_variance ( a )

    print ( '  PDF mean =        %14g' % ( mean ) )
    print ( '  PDF variance =    %14g' % ( variance ) )
  
    x = np.zeros ( nsample )
    for j in range ( 0, nsample ):
      x[j], seed = arcsin_sample ( a, seed )

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
  print ( 'ARCSIN_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def arcsin_variance ( a ):

#*****************************************************************************80
#
## ARCSIN_VARIANCE returns the variance of the Arcsin PDF.
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
#    Input, real A, the parameter of the CDF.
#    A must be positive.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = a * a / 2.0

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  arcsin_cdf_test ( )
  arcsin_sample_test ( )
  timestamp ( )
 
