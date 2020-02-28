#! /usr/bin/env python
#
def uniform_01_cdf ( x ):

#*****************************************************************************80
#
## UNIFORM_01_CDF evaluates the Uniform 01 CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the CDF.
#
#    Output, real CDF, the value of the CDF.
#
  if ( x < 0.0 ):
    cdf = 0.0
  elif ( 1.0 < x ):
    cdf = 1.0
  else:
    cdf = x

  return cdf

def uniform_01_cdf_inv ( cdf ):

#*****************************************************************************80
#
## UNIFORM_01_CDF_INV inverts the Uniform 01 CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
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
#    Output, real X, the corresponding argument.
#
  from sys import exit

  if ( cdf < 0.0 or 1.0 < cdf ):
    print ( '' )
    print ( 'UNIFORM_01_CDF_INV - Fatal error!' )
    print ( '  CDF < 0 or 1 < CDF.' )
    exit ( 'UNIFORM_01_CDF_INV - Fatal error!' )

  x = cdf

  return x

def uniform_01_cdf_test ( ):

#*****************************************************************************80
#
## UNIFORM_01_CDF_TEST tests UNIFORM_01_CDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'UNIFORM_01_CDF_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNIFORM_01_CDF evaluates the Uniform 01 CDF' )
  print ( '  UNIFORM_01_CDF_INV inverts the Uniform 01 CDF.' )
  print ( '  UNIFORM_01_PDF evaluates the Uniform 01 PDF' )

  seed = 123456789

  print ( '' )
  print ( '       X            PDF           CDF            CDF_INV' )
  print ( '' )

  for i in range ( 0, 10 ):

    x, seed = uniform_01_sample ( seed )

    pdf = uniform_01_pdf ( x )

    cdf = uniform_01_cdf ( x )

    x2 = uniform_01_cdf_inv ( cdf )

    print ( ' %14g  %14g  %14g  %14g' % ( x, pdf, cdf, x2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'UNIFORM_01_CDF_TEST' )
  print ( '  Normal end of execution.' )
  return

def uniform_01_mean ( ):

#*****************************************************************************80
#
## UNIFORM_01_MEAN returns the mean of the Uniform 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real MEAN, the mean of the discrete uniform PDF.
#
  mean = 0.5

  return mean

def uniform_01_pdf ( x ):

#*****************************************************************************80
#
## UNIFORM_01_PDF evaluates the Uniform 01 PDF.
#
#  Formula:
#
#    PDF(X) = 1 for 0 <= X <= 1
#           = 0 otherwise
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the argument of the PDF.
#    0.0 <= X <= 1.0.
#
#    Output, real PDF, the value of the PDF.
#
  if ( x < 0.0 or 1.0 < x ):
    pdf = 0.0
  else:
    pdf = 1.0

  return pdf

def uniform_01_sample ( seed ):

#*****************************************************************************80
#
## UNIFORM_01_SAMPLE is a portable random number generator.
#
#  Formula:
#
#    SEED = SEED * (7^5) mod ( 2^31 - 1 )
#    UNIFORM_01_SAMPLE = SEED * / ( 2^31 - 1 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
#
#  Parameters:
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real VALUE, a random value between 0 and 1.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
#  Local parameters:
#
#    IA = 7^5
#    IB = 2^15
#    IB16 = 2^16
#    IP = 2^31-1
#
  ia = 16807
  ib15 = 32768
  ib16 = 65536
  ip = 2147483647
#
#  Don't let SEED be 0 or IP
#
  if ( seed == 0 or seed == ip ):
    seed = ( ip // 2 )
#
#  Get the 15 high order bits of SEED.
#
  ixhi = ( seed // ib16 )
#
#  Get the 16 low bits of SEED and form the low product.
#
  loxa = ( seed - ixhi * ib16 ) * ia
#
#  Get the 15 high order bits of the low product.
#
  leftlo = ( loxa // ib16 )
#
#  Form the 31 highest bits of the full product.
#
  iprhi = ixhi * ia + leftlo
#
#  Get overflow past the 31st bit of full product.
#
  k = ( iprhi // ib15 )
#
#  Assemble all the parts and presubtract IP.  The parentheses are essential.
#
  seed = ( ( ( loxa - leftlo * ib16 ) - ip ) + ( iprhi - k * ib15 ) * ib16 ) + k
#
#  Add IP back in if necessary.
#
  if ( seed < 0 ):
    seed = seed + ip
#
#  Multiply by 1 / (2^31-1).
#
  value = seed * 4.656612875E-10

  return value, seed

def uniform_01_sample_test ( ):

#*****************************************************************************80
#
## UNIFORM_01_SAMPLE_TEST tests UNIFORM_01_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
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
  print ( 'UNIFORM_01_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UNIFORM_01_MEAN computes the Uniform 01 mean' )
  print ( '  UNIFORM_01_SAMPLE samples the Uniform 01 distribution' )
  print ( '  UNIFORM_01_VARIANCE computes the Uniform 01 variance.' )

  mean = uniform_01_mean ( )
  variance = uniform_01_variance ( )

  print ( '' )
  print ( '  PDF mean =            %14g' % ( mean ) )
  print ( '  PDF variance =        %14g' % ( variance ) )

  x = np.zeros ( nsample )
  for i in range ( 0, nsample ):
    x[i], seed = uniform_01_sample ( seed )

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
  print ( 'UNIFORM_01_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def uniform_01_variance ( ):

#*****************************************************************************80
#
## UNIFORM_01_VARIANCE returns the variance of the Uniform 01 PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VARIANCE, the variance of the PDF.
#
  variance = 1.0 / 12.0

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  uniform_01_cdf_test ( )
  uniform_01_sample_test ( )
  timestamp ( )
 
