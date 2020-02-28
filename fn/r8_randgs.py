#! /usr/bin/env python
#
def r8_randgs ( xmean, sd, seed ):

#*****************************************************************************80
#
## R8_RANDGS generates a normally distributed random number.
#
#  Discussion:
#
#    This function generate a normally distributed random number, that is,
#    it generates random numbers with a Gaussian distribution.  These
#    random numbers are not exceptionally good, especially in the tails
#    of the distribution, but this implementation is simple and suitable
#    for most applications.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    Python version by John Burkardt.
#
#  Reference:
#
#    Richard Hamming,
#    Numerical Methods for Scientists and Engineers,
#    Dover, 1986,
#    ISBN: 0486652416,
#    LC: QA297.H28.
#
#  Parameters:
#
#    Input, real XMEAN, the mean of the Gaussian distribution.
#
#    Input, real SD, the standard deviation of the
#    Gaussian function.
#
#    Input/output, integer SEED, a seed for the random number generator.
#
#    Output, real VALUE, a normally distributed random number.
#
  from r8_ren import r8_ren

  value = - 6.0
  for i in range ( 0, 12 ):
    r, seed = r8_ren ( seed )
    value = value + r

  value = xmean + sd * value

  return value, seed

def r8_randgs_test ( ):

#*****************************************************************************80
#
## R8_RANDGS_TEST tests R8_RANDGS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 3.0
  sd = 2.0
  seed = 123456789

  print ( '' )
  print ( 'R8_RANDGS_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8_RANDGS is a normal random number generator.' )
  print ( '  Mean = %g' % ( m ) )
  print ( '  Standard Deviation = %g' % ( sd ) )
  print ( '' )
  print ( '             I         R8_RANDGS' )
  print ( '' )

  m2 = 0.0
  sd2 = 0.0

  for i in range ( 0, 1000 ):

    r, seed = r8_randgs ( m, sd, seed )
    m2 = m2 + r
    sd2 = sd2 + ( r - m ) ** 2
    if ( i <= 10 ):
      print ( '  %14d  %14g' % ( i, r ) )

  m2 = m2 / 1000.0
  sd2 = np.sqrt ( sd2 / 1000.0 )

  print ( '' )
  print ( '  Sequence mean =  %g' % ( m2 ) )
  print ( '  Sequence standard deviation = %g' % ( sd2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8_RANDGS_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8_randgs_test ( )
  timestamp ( )
