#! /usr/bin/env python
#
def circular_normal_mean ( a, b ):

#*****************************************************************************80
#
## CIRCULAR_NORMAL_MEAN returns the mean of the Circular Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A(2), a parameter of the PDF, the mean value.
#
#    Input, real B, a parameter of the PDF, the standard deviation.
#
#    Output, real MEAN(2), the mean of the PDF.
#
  import numpy as np

  mean = np.zeros ( 2 )

  mean[0] = a[0]
  mean[1] = a[1]

  return mean

def circular_normal_pdf ( x, a, b ):

#*****************************************************************************80
#
## CIRCULAR_NORMAL_PDF evaluates the Circular Normal PDF.
#
#  Discussion:
#
#    PDF(X) = EXP ( - 0.5 * ( ( (X(1)-A(1))^2 + (X(2)-A(2))^2 ) / B^2 )
#      / ( 2 * PI * B^2 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X(2), the argument of the PDF.
#
#    Input, real A(2), a parameter of the PDF, the mean value.
#
#    Input, real B, a parameter of the PDF, the standard deviation.
#
#    Output, real PDF, the value of the PDF.
#
  import numpy as np

  d = ( ( x[0] - a[0] ) ** 2 + ( x[1] - a[1] ) ** 2 ) / b ** 2

  pdf = np.exp ( - 0.5 * d ) / ( 2.0 * b ** 2 * np.pi )

  return pdf

def circular_normal_sample ( a, b, seed ):

#*****************************************************************************80
#
## CIRCULAR_NORMAL_SAMPLE samples the Circular Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A(2), a parameter of the PDF, the mean value.
#
#    Input, real B, a parameter of the PDF, the standard deviation.
#
#    Input/output, integer SEED, a seed for the random
#    number generator.
#
#    Output, real X(2), a sample of the PDF.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  v1, seed = r8_uniform_01 ( seed )
  v2, seed = r8_uniform_01 ( seed )

  r = np.sqrt ( - 2.0 * np.log ( v1 ) )

  x = np.zeros ( 2 )

  x[0] = a[0] + b * r * np.cos ( 2.0 * np.pi * v2 )
  x[1] = a[1] + b * r * np.sin ( 2.0 * np.pi * v2 )

  return x, seed

def circular_normal_sample_test ( ):

#*****************************************************************************80
#
## CIRCULAR_NORMAL_SAMPLE_TEST tests CIRCULAR_NORMAL_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2016
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

  a = np.array ( [ 1.0, 5.0 ] )
  b = 0.75

  print ( '' )
  print ( 'CIRCULAR_NORMAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  CIRCULAR_NORMAL_MEAN computes the Circular Normal mean' )
  print ( '  CIRCULAR_NORMAL_SAMPLE samples the Circular Normal distribution' )
  print ( '  CIRCULAR_NORMAL_VARIANCE computes the Circular Normal variance.' )

  mean = circular_normal_mean ( a, b )
  variance = circular_normal_variance ( a, b )

  print ( '' )
  print ( '  PDF means =               %14g  %14g' % ( mean[0], mean[1] ) )
  print ( '  PDF variances =           %14g  %14g' % ( variance[0], variance[1] ) )
  
  x_table = np.zeros ( nsample )
  y_table = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x, seed = circular_normal_sample ( a, b, seed )
    x_table[i] = x[0]
    y_table[i] = x[1]

  xmean = r8vec_mean ( nsample, x_table )
  xvariance = r8vec_variance ( nsample, x_table )
  xmax = r8vec_max ( nsample, x_table )
  xmin = r8vec_min ( nsample, x_table )

  ymean = r8vec_mean ( nsample, y_table )
  yvariance = r8vec_variance ( nsample, y_table )
  ymax = r8vec_max ( nsample, y_table )
  ymin = r8vec_min ( nsample, y_table )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g  %14g' % ( xmean, ymean ) )
  print ( '  Sample variance = %14g  %14g' % ( xvariance, yvariance ) )
  print ( '  Sample maximum =  %14g  %14g' % ( xmax, ymax ) )
  print ( '  Sample minimum =  %14g  %14g' % ( xmin, ymin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'CIRCULAR_NORMAL_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def circular_normal_variance ( a, b ):

#*****************************************************************************80
#
## CIRCULAR_NORMAL_VARIANCE returns the variance of the Circular Normal PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A(2), a parameter of the PDF, the mean value.
#
#    Input, real B, a parameter of the PDF, the standard deviation.
#
#    Output, real VARIANCE(2), the variance of the PDF.
#
  import numpy as np

  variance = np.zeros ( 2 )

  variance[0] = b ** 2
  variance[1] = b ** 2

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  circular_normal_sample_test ( )
  timestamp ( )

