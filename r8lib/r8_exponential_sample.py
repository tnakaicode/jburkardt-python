#! /usr/bin/env python
#
def r8_exponential_sample ( beta ):

#*****************************************************************************80
#
## R8_EXPONENTIAL_SAMPLE samples the exponential PDF.
#
#  Discussion:
#
#    Note that the parameter LAMBDA is a multiplier.  In some formulations,
#    it is used as a divisor instead.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real BETA, the parameter of the PDF.
#
#    Output, real VALUE, a sample of the PDF.
#
  import numpy as np
  from r8_uniform_01_sample import r8_uniform_01_sample

  r = r8_uniform_01_sample ( )

  value = - np.log ( r ) * beta

  return value

def r8_exponential_sample_test ( ):

#*****************************************************************************80
#
## R8_EXPONENTIAL_SAMPLE_TEST tests R8_EXPONENTIAL_SAMPLE.
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
  from r8_exponential_pdf import r8_exponential_pdf
  from r8_uniform_ab import r8_uniform_ab

  print ( '' )
  print ( 'R8_EXPONENTIAL_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_EXPONENTIAL_SAMPLE samples the general exponential PDF:' )
  print ( '' )
  print ( '            BETA               R          PDF' )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):

    beta, seed = r8_uniform_ab ( 0.0, +10.0, seed )
    r = r8_exponential_sample ( beta )
    pdf = r8_exponential_pdf ( beta, r )
    print ( '  %14.6g  %14.6g  %14.6g' % ( beta, r, pdf ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_EXPONENTIAL_SAMPLE_TEST' )
  print ( '  Normal end of execution' )
  return

if ( __name__ == '__main__' ):
  from initialize import initialize
  from timestamp import timestamp
  timestamp ( )
  initialize ( )
  r8_exponential_sample_test ( )
  timestamp ( )
