#! /usr/bin/env python
#
def i4_uniform_sample ( a, b ):

#*****************************************************************************80
#
## I4_UNIFORM_SAMPLE returns a scaled pseudorandom I4 between A and B.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 January 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer A, B, the minimum and maximum acceptable values.
#
#    Output, integer C, the randomly chosen integer.
#
  from r8_uniform_01_sample import r8_uniform_01_sample
#
#  We prefer A < B.
#
  a2 = min ( a, b )
  b2 = max ( a, b )

  u = r8_uniform_01_sample ( )
#
#  Scale to [A2-0.5,B2+0.5].
#
  u = ( 1.0 - u ) * ( a2 - 0.5 ) \
    +         u   * ( b2 + 0.5 )
#
#  Round.
#
  value = round ( u )
#
#  Enforce limits.
#
  value = max ( value, a2 )
  value = min ( value, b2 )

  return value

def i4_uniform_sample_test ( ):

#*****************************************************************************80
#
## I4_UNIFORM_SAMPLE_TEST tests I4_UNIFORM_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 January 2018
#
#  Author:
#
#    John Burkardt
#
  from initialize import initialize
  import platform

  initialize ( )

  print ( '' )
  print ( 'I4_UNIFORM_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_UNIFORM_SAMPLE csamples the uniform distribution on integers.' )
  print ( '  Generate C between A and B.' )
  print ( '' )
  print ( '    A    B    C' )
  print ( '' )

  for i in range ( 0, 10 ):
    a = i4_uniform_sample ( -10, 10 )
    b = i4_uniform_sample ( a, 20 )
    c = i4_uniform_sample ( a, b )
    print ( '  %3d  %3d  %3d' % ( a, b, c ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_UNIFORM_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4_uniform_sample_test ( )
  timestamp ( )
