#! /usr/bin/env python
#
def r8_exponential_01_sample ( ):

#*****************************************************************************80
#
## R8_EXPONENTIAL_01_SAMPLE samples the standard exponential PDF.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, a sample of the PDF.
#
  import numpy as np
  from r8_uniform_01_sample import r8_uniform_01_sample

  r = r8_uniform_01_sample ( )

  value = - np.log ( r )

  return value

def r8_exponential_01_sample_test ( ):

#*****************************************************************************80
#
## R8_EXPONENTIAL_01_SAMPLE_TEST tests R8_EXPONENTIAL_01_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_exponential_01_pdf import r8_exponential_01_pdf

  print ( '' )
  print ( 'R8_EXPONENTIAL_01_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_EXPONENTIAL_01_SAMPLE samples the standard exponential PDF:' )
  print ( '' )
  print ( '          R               PDF(R)' )
  print ( '' )

  for i in range ( 0, 10 ):
    r = r8_exponential_01_sample ( )
    pdf = r8_exponential_01_pdf ( r )
    print ( '  %14.6g  %14.6g' % ( r, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_EXPONENTIAL_01_SAMPLE_TEST' )
  print ( '  Normal end of execution' )
  return

if ( __name__ == '__main__' ):
  from initialize import initialize
  from timestamp import timestamp
  initialize ( )
  timestamp ( )
  r8_exponential_01_sample_test ( )
  timestamp ( )
