#! /usr/bin/env python
#
def r8_normal_01_sample ( ):

#*****************************************************************************80
#
## R8_NORMAL_01_SAMPLE returns a unit pseudonormal R8.
#
#  Discussion:
#
#    The standard normal probability distribution function (PDF) has
#    mean 0 and standard deviation 1.
#
#    The Box-Muller method is used, which is efficient, but
#    generates two values at a time.  
#
#    Typically, we would use one value and save the other for the next call.
#    However, the fact that this function has saved memory makes it difficult
#    to correctly handle cases where we want to re-initialize the code,
#    or to run in parallel.  Therefore, we will instead use the first value
#    and DISCARD the second.
#
#    EFFICIENCY must defer to SIMPLICITY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, a sample of the standard normal PDF.
#
  import numpy as np
  from r8_uniform_01_sample import r8_uniform_01_sample

  r1 = r8_uniform_01_sample ( )
  r2 = r8_uniform_01_sample ( )

  x = np.sqrt ( - 2.0 * np.log ( r1 ) ) * np.cos ( 2.0 * np.pi * r2 )

  value = x

  return value

def r8_normal_01_sample_test ( ):

#*****************************************************************************80
#
## R8_NORMAL_01_SAMPLE_TEST tests R8_NORMAL_01_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    27 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_normal_01_pdf import r8_normal_01_pdf

  seed = 123456789

  print ( '' )
  print ( 'R8_NORMAL_01_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_NORMAL_01_SAMPLE samples the normal distribution.' )

  print ( '' )
  print ( '      X        PDF(X)' )
  print ( '' )

  for i in range ( 0, 10 ):
    x = r8_normal_01_sample ( )
    pdf = r8_normal_01_pdf ( x )
    print ( '  %14.6g  %14.6g' % ( x, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_NORMAL_01_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_normal_01_sample_test ( )
  timestamp ( )

