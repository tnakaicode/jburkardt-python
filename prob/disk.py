#! /usr/bin/env python
#
def disk_mean ( a, b, c ):

#*****************************************************************************80
#
## DISK_MEAN returns the mean of points in a disk.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the disk.
#    The disk is centered at (A,B) and has radius C.
#    0.0 < C.
#
#    Output, real MEAN(2), the mean.
#
  import numpy as np

  mean = np.array ( [ a, b ] )

  return mean

def disk_sample ( a, b, c, seed ):

#*****************************************************************************80
#
## DISK_SAMPLE samples points from a disk.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the disk.
#    The disk is centered at (A,B) and has radius C.
#    0.0 < C.
#
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real X1, X2, a sampled point of the disk.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from r8_uniform_01 import r8_uniform_01

  radius_frac, seed = r8_uniform_01 ( seed )
  radius_frac = np.sqrt ( radius_frac )

  angle, seed = r8_uniform_01 ( seed )
  angle = 2.0 * np.pi * angle

  x1 = a + c * radius_frac * np.cos ( angle )
  x2 = b + c * radius_frac * np.sin ( angle )

  return x1, x2, seed

def disk_sample_test ( ):

#*****************************************************************************80
#
## DISK_SAMPLE_TEST tests DISK_MEAN, DISK_SAMPLE, DISK_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_max import r8vec_max
  from r8vec_mean import r8vec_mean
  from r8vec_min import r8vec_min
  from r8vec_variance import r8vec_variance

  nsample = 1000
  seed = 123456789

  print ( '' )
  print ( 'DISK_SAMPLE_TEST' )
  print ( '  DISK_MEAN returns the Disk mean.' )
  print ( '  DISK_SAMPLE samples the Disk distribution.' )
  print ( '  DISK_VARIANCE returns the Disk variance.' )

  a = 10.0
  b = 4.0
  c = 5.0

  print ( '' )
  print ( '  X coordinate of center is A = %14g' % ( a ) )
  print ( '  Y coordinate of center is B = %14g' % ( b ) )
  print ( '  Radius is C =                 %14g' % ( c ) )

  mean = disk_mean ( a, b, c )
  v = disk_variance ( a, b, c )

  print ( '' )
  print ( '  Disk mean =     %14g  %14g' % ( mean[0], mean[1] ) )
  print ( '  Disk variance = %14g' % ( v ) )

  x_table = np.zeros ( nsample )
  y_table = np.zeros ( nsample )

  for i in range ( 0, nsample ):
    x, y, seed = disk_sample ( a, b, c, seed )
    x_table[i] = x
    y_table[i] = y

  variance = 0.0
  for i in range ( 0, nsample ):
    variance = variance + ( x_table[i] - a ) ** 2 \
                        + ( y_table[i] - b ) ** 2 
  variance = variance / nsample

  xmax = np.zeros ( 2 )
  xmin = np.zeros ( 2 )

  xmean = r8vec_mean ( nsample, x_table )
  xmax = r8vec_max ( nsample, x_table )
  xmin = r8vec_min ( nsample, x_table )

  ymean = r8vec_mean ( nsample, y_table )
  ymax = r8vec_max ( nsample, y_table )
  ymin = r8vec_min ( nsample, y_table )

  print ( '' )
  print ( '  Sample size =     %6d' % ( nsample ) )
  print ( '  Sample mean =     %14g  %14g' % ( xmean, ymean ) )
  print ( '  Sample variance = %14g' % ( variance ) )
  print ( '  Sample maximum =  %14g  %14g' % ( xmax, ymax ) )
  print ( '  Sample minimum =  %14g  %14g' % ( xmin, ymin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'DISK_SAMPLE_TEST' )
  print ( '  Normal end of execution.' )
  return

def disk_variance ( a, b, c ):

#*****************************************************************************80
#
## DISK_VARIANCE returns the variance of points in a disk.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real A, B, C, the parameters of the disk.
#    The disk is centered at (A,B) and has radius C.
#    0.0 < C.
#
#    Output, real VARIANCE, the variance.
#
  variance = 0.5 * c * c

  return variance

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  disk_sample_test ( )
  timestamp ( )
 
