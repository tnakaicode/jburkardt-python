#! /usr/bin/env python
#
def r8_uniform_01_sample ( ):

#*****************************************************************************80
#
## R8_UNIFORM_01_SAMPLE generates a uniform random deviate from [0,1].
#
#  Discussion:
#
#    This function should be the only way that the package accesses random
#    numbers.
#
#    Setting OPTION to 0 accesses the R8_UNI_01() function in RNGLIB,
#    for which there are versions in various languages, which should result
#    in the same values being returned.  This should be the only function
#    that invokes a function from RNGLIB.
#
#    Setting OPTION to 1 in the Python version calls the system
#    RNG "rand()".
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
#    Original FORTRAN77 version by Barry Brown, James Lovato.
#    Python version by John Burkardt.
#
#  Parameters:
#
#    Output, real VALUE, a random deviate 
#    from the distribution.
#
  import numpy as np
  from r8_uni_01 import r8_uni_01

  option = 0

  if ( option == 0 ):
    value = r8_uni_01 ( )
  else:
    value = np.rand ( 1, 1 )
 
  return value

def r8_uniform_01_sample_test ( ):

#*****************************************************************************80
#
## R8_UNIFORM_01_SAMPLE_TEST tests R8_UNIFORM_01_SAMPLE.
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

  print ( '' )
  print ( 'R8_UNIFORM_01_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_UNIFORM_01_SAMPLE returns random values in [0,1]:' )
  print ( '' )

  for i in range ( 0, 10 ):
    r = r8_uniform_01_sample ( )
    print ( '  %g' % ( r ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_UNIFORM_01_SAMPLE_TEST' )
  print ( '  Normal end of execution' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_uniform_01_sample_test ( )
  timestamp ( )
