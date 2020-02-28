#! /usr/bin/env python
#
def r4_exponential_sample ( lam ):

#*****************************************************************************80
#
## R4_EXPONENTIAL_SAMPLE samples the exponential PDF.
#
#  Discussion:
#
#    Note that the parameter LAM is a multiplier.  In some formulations,
#    it is used as a divisor instead.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real LAM, the parameter of the PDF.
#
#    Output, real VALUE, a sample of the PDF.
#
  import numpy as np
  from r4_uni_01 import r4_uni_01

  r = r4_uni_01 ( );

  value = - np.log ( r ) * lam

  return value

def r4_exponential_sample_test ( ):

#*****************************************************************************80
#
## R4_EXPONENTIAL_TEST tests R4_EXPONENTIAL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2018
#
#  Author:
#
#    John Burkardt
#
  import platform

  test_num = 20

  print ( '' )
  print ( 'R4_EXPONENTIAL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R4_EXPONENTIAL samples the exponential distribution.' )
  print ( '' )

  lam = 0.5

  for test in range ( 0, test_num ):

    x = r4_exponential_sample ( lam )
    print ( '  %f' % ( x ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R4_EXPONENTIAL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r4_exponential_sample_test ( )
  timestamp ( )

