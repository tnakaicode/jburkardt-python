#! /usr/bin/env python
#
def quasigeometric_cdf ( x, a, b ):

#*****************************************************************************80
#
## QUASIGEOMETRIC_CDF evaluates the Quasigeometric CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer X, the number of trials.
#
#    Input, real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    Input, real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#    Output, real CDF, the value of the CDF.
#
  if ( x < 0 ):
    cdf = 0.0
  elif ( x == 0 ):
    cdf = a
  elif ( b == 0.0 ):
    cdf = 1.0
  else:
    cdf = a + ( 1.0 - a ) * ( 1.0 - b ** x )

  return cdf

def quasigeometric_cdf_inv ( cdf, a, b ):

#*****************************************************************************80
#
## QUASIGEOMETRIC_CDF_INV inverts the Quasigeometric CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real CDF, the value of the CDF.
#    0.0 <= CDF <= 1.0
#
#    Input, real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    Input, real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#    Output, integer X, the corresponding value of X.
#
  import numpy as np
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'QUASIGEOMETRIC_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'QUASIGEOMETRIC_CDF_INV - Fatal error!' )

  if ( cdf < a ):
    x = 0
  elif ( b == 0.0 ):
    x = 1
  else:
    x = 1 + int ( ( np.log ( 1.0 - cdf ) - np.log ( 1.0 - a ) ) / np.log ( b ) )

  return x

def quasigeometric_cdf_test ( ):

#*****************************************************************************80
#
## QUASIGEOMETRIC_CDF_TEST tests QUASIGEOMETRIC_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'QUASIGEOMETRIC_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  QUASIGEOMETRIC_CDF evaluates the Quasigeometric CDF' )
  print ( '  QUASIGEOMETRIC_CDF_INV inverts the Quasigeometric CDF.' )
  print ( '  QUASIGEOMETRIC_PDF evaluates the Quasigeometric PDF' )

  a = 0.4825
  b = 0.5893

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  check = quasigeometric_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'QUASIGEOMETRIC_CDF_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = quasigeometric_sample ( a, b, seed )

    pdf = quasigeometric_pdf ( x, a, b )

    cdf = quasigeometric_cdf ( x, a, b )

    x2 = quasigeometric_cdf_inv ( cdf, a, b )

    print ( '  %14d  %14g  %14g  %14d' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'QUASIGEOMETRIC_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def quasigeometric_check ( a, b ):

#*****************************************************************************80
#
## QUASIGEOMETRIC_CHECK checks the parameters of the Quasigeometric CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    Input, real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#    Output, logical QUASIGEOMETRIC_CHECK, is true if the parameters are legal.
#
  check = True

  if ( a < 0.0 or 1.0 < a ):
    print ( '' )
    print ( 'QUASIGEOMETRIC_CHECK - Fatal error!' )
    print ( '  A < 0 or 1 < A.' )
    check = False

  if ( b < 0.0 or 1.0 <= b ):
    print ( '' )
    print ( 'QUASIGEOMETRIC_CHECK - Fatal error!' )
    print ( '  B < 0 or 1 <= B.' )
    check = False

  return check

def quasigeometric_mean ( a, b ):

#*****************************************************************************80
#
## QUASIGEOMETRIC_MEAN returns the mean of the Quasigeometric PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    Input, real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#    Output, real MEAN, the mean of the PDF.
#
  mean = ( 1.0 - a  ) / ( 1.0 - b )

  return mean

def quasigeometric_pdf ( x, a, b ):

#*****************************************************************************80
#
## QUASIGEOMETRIC_PDF evaluates the Quasigeometric PDF.
#
#  Discussion:
#
#    PDF(A,BX) =    A                     if 0  = X
#               = (1-A) * (1-B) * B^(X-1)  if 1 <= X.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Darren Glass, Philip Lowry,
#    Quasiquasigeometric Distributions and Extra Inning Baseball Games,
#    Mathematics Magazine,
#    Volume 81, Number 2, April 2008, pages 127-137.
#
#    Paul Nahin,
#    Digital Dice: Computational Solutions to Practical Probability Problems,
#    Princeton University Press, 2008,
#    ISBN13: 978-0-691-12698-2,
#    LC: QA273.25.N34.
#
#  Parameters:
#
#    Input, integer X, the independent variable.
#    0 <= X
#
#    Input, real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    Input, real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#    Output, real PDF, the value of the PDF.
#
  if ( x < 0 ):

    pdf = 0.0

  elif ( x == 0 ):

    pdf = a

  elif ( b == 0.0 ):

    if ( x == 1 ):
      pdf = 1.0
    else:
      pdf = 0.0

  else:

    pdf = ( 1.0 - a ) * ( 1.0 - b ) * b ** ( x - 1 )

  return pdf

def quasigeometric_sample ( a, b, seed ):

#*****************************************************************************80
#
## QUASIGEOMETRIC_SAMPLE samples the Quasigeometric PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    Input, real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#    Input, integer SEED, a seed for the random 
#    number generator.
#
#    Output, integer X, a sample of the PDF.
#
#    Output, integer SEED, a seed for the random 
#    number generator.
#
  from r8_uniform_01 import r8_uniform_01

  cdf, seed = r8_uniform_01 ( seed )

  x = quasigeometric_cdf_inv ( cdf, a, b )

  return x, seed

def quasigeometric_sample_test ( ):

#*****************************************************************************80
#
## QUASIGEOMETRIC_SAMPLE_TEST tests QUASIGEOMETRIC_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
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

  sample_num = 1000
  seed = 123456789

  print ( '' )
  print ( 'QUASIGEOMETRIC_SAMPLE_TEST' )
  print ( '  QUASIGEOMETRIC_MEAN computes the Quasigeometric mean' )
  print ( '  QUASIGEOMETRIC_SAMPLE samples the Quasigeometric distribution' )
  print ( '  QUASIGEOMETRIC_VARIANCE computes the Quasigeometric variance.' )

  a = 0.4825
  b = 0.5893

  print ( '' )
  print ( '  PDF parameter A = %14g' % ( a ) )
  print ( '  PDF parameter B = %14g' % ( b ) )

  check = quasigeometric_check ( a, b )

  if ( not check ):
    print ( '' )
    print ( 'QUASIGEOMETRIC_SAMPLE_TEST - Fatal error!' )
    print ( '  The parameters are not legal.' )
    return

  mean = quasigeometric_mean ( a, b )
  variance = quasigeometric_variance ( a, b )

  print ( '' )
  print ( '  PDF parameter A =             %14g' % ( a ) )
  print ( '  PDF mean =                    %14g' % ( mean ) )
  print ( '  PDF variance =                %14g' % ( variance ) )

  x = np.zeros ( sample_num )
  for i in range ( 0, sample_num ):
    x[i], seed = quasigeometric_sample ( a, b, seed )

  mean = i4vec_mean ( sample_num, x )
  variance = i4vec_variance ( sample_num, x )
  xmax = i4vec_max ( sample_num, x )
  xmin = i4vec_min ( sample_num, x )

  print ( '' )
  print ( '  Sample size =     %6d' % ( sample_num ) )
  print ( '  Sample mean =     %14g' % ( mean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %6d' % ( xmax ) )
  print ( '  Sample minimum =  %6d' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'QUASIGEOMETRIC_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def quasigeometric_variance ( a, b ):

#*****************************************************************************80
#
## QUASIGEOMETRIC_VARIANCE returns the variance of the Quasigeometric PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, the probability of 0 successes.
#    0.0 <= A <= 1.0.
#
#    Input, real B, the depreciation constant.
#    0.0 <= B < 1.0.
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = ( 1.0 - a ) * ( a + b ) / ( 1.0 - b ) / ( 1.0 - b )

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  quasigeometric_cdf_test ( )
  quasigeometric_sample_test ( )
  timestamp ( )
 
