#! /usr/bin/env python
#
def r8_uniform_sample ( a, b ):

#*****************************************************************************80
#
## R8_UNIFORM_SAMPLE generates a uniform random deviate from [A,B].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2015
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, real A, B, the lower and upper limits of the interval.
#
#    Output, real VALUE, a random deviate 
#    from the distribution.
#
  from r8_uniform_01_sample import r8_uniform_01_sample
  from sys import exit

  if ( b <= a ):
    print ( '' )
    print ( 'R8_UNIFORM_SAMPLE - Fatal error!' )
    print ( '  For uniform PDF, the lower limit must be ' )
    print ( '  less than the upper limit.' )
    exit ( 'R8_UNIFORM_SAMPLE - Fatal error!' )

  import numpy as np

  value = a + ( b - a ) * r8_uniform_01_sample ( )
 
  return value

def r8_uniform_sample_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_SAMPLE_TEST tests R8_UNIFORM_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 July 2014
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8_uniform_ab import r8_uniform_ab

  print ( '' )
  print ( 'R8_UNIFORM_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_SAMPLE returns random values in [A,B]:' )
  print ( '' )
  print ( '            A               B               R' )
  print ( '' )

  seed = 123456789

  for i in range ( 0, 10 ):

    a, seed = r8_uniform_ab ( -100.0, +100.0, seed )
    b, seed = r8_uniform_ab ( -100.0, +100.0, seed )
    t = max ( a, b )
    a = min ( a, b )
    b = t
    r = r8_uniform_sample ( a, b )
    print ( '  %14.6g  %14.6g  %14.6g' % ( a, b, r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_SAMPLE_TEST' )
  print ( '  Normal end of execution' )
  return

if ( __name__ == '__main__' ):
  from initialize import initialize
  from timestamp import timestamp
  timestamp ( )
  initialize ( )
  r8_uniform_sample_test ( )
  timestamp ( )
